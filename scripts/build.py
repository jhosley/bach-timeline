#!/usr/bin/env python3
"""Build the Bach Timeline static site: content/**.md -> docs/ (GitHub Pages).

- Mirrors the content tree (foo/bar.md -> foo/bar.html) so relative links survive.
- index.html is the ribbon-in-space timeline (all events embedded as JSON).
- Section indexes for works, craft, eras, people, places.
No dependencies beyond PyYAML (stdlib markdown-mini included).
"""
import os, re, json, shutil, html, yaml, datetime
from pathlib import Path

MONTHS=['January','February','March','April','May','June','July','August','September','October','November','December']
def parse_date(d):
    if isinstance(d, datetime.date): return d.year, d.month, d.day
    parts=str(d).split('-')
    y=int(parts[0]); mo=int(parts[1]) if len(parts)>1 else None; da=int(parts[2]) if len(parts)>2 else None
    return y, mo, da
def fdate(d, prec):
    """-> (display string, fractional year)"""
    y,mo,da = parse_date(d)
    if prec=='day' and mo and da: return f"{da} {MONTHS[mo-1]} {y}", y+(mo-1+(da-0.5)/31)/12
    if mo and prec in ('day','month'): return f"{MONTHS[mo-1]} {y}", y+(mo-0.5)/12
    if prec=='circa': return f"c. {y}", y+0.5
    return str(y), y+0.5
def load_images():
    f=CONTENT/'images.yml'
    return yaml.safe_load(f.read_text()) or {} if f.exists() else {}
IMAGES={}

ROOT = Path(__file__).resolve().parent.parent
CONTENT, DOCS = ROOT/'content', ROOT/'docs'

ARCS = [
  dict(y0=1685, y1=1750, name='The Life',          c='#e8c874'),
  dict(y0=1750, y1=1829, name='The Eclipse',        c='#66607a'),
  dict(y0=1829, y1=1900, name='The Rediscovery',    c='#aecbe8'),
  dict(y0=1900, y1=1990, name='The Living Bach',    c='#7fd4c1'),
]
ERA_COLOR = {'eclipse':'#8d87a6','revival':'#aecbe8','living-bach':'#7fd4c1'}   # default gold otherwise
ERA_ORDER = ['eisenach','ohrdruf','lueneburg','arnstadt','muehlhausen','weimar',
             'cothen','leipzig-1','leipzig-2','leipzig-3','eclipse','revival','living-bach']
GENRES = [('passion-oratorio','Passions & Oratorios'),('mass','Masses & Magnificat'),
  ('cantata-sacred','Sacred Cantatas'),('cantata-secular','Secular Cantatas'),('motet','Motets'),
  ('organ','Organ'),('keyboard','Keyboard'),('pedagogical','Inventions & Sinfonias'),
  ('orchestral','Orchestral'),('chamber','Chamber & Solo Strings'),('contrapuntal','The Late Summa')]

# ---------- mini markdown ----------
def md_inline(s):
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{md_href(m.group(2))}">{m.group(1)}</a>', s)
    s = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*([^*\n]+?)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'(?<![">])(https?://[^\s<)]+)', r'<a href="\1">\1</a>', s)
    return s

def md_href(u):
    if u.endswith('.md'): return u[:-3]+'.html'
    return u.replace('.md:', '.html:')

def md_to_html(text):
    out, para, inlist, fence = [], [], False, False
    def flush():
        nonlocal para
        if para: out.append('<p>'+md_inline(' '.join(para))+'</p>'); para=[]
    for raw in text.split('\n'):
        line = raw.rstrip()
        if line.startswith('```'):
            flush()
            if not fence: out.append('<pre>'); fence=True
            else: out.append('</pre>'); fence=False
            continue
        if fence: out.append(html.escape(raw)); continue
        if not line.strip():
            flush()
            if inlist: out.append('</ul>'); inlist=False
            continue
        m = re.match(r'(#{1,4})\s+(.*)', line)
        if m:
            flush();
            if inlist: out.append('</ul>'); inlist=False
            n=len(m.group(1)); out.append(f'<h{n+1}>{md_inline(m.group(2))}</h{n+1}>'); continue
        if line.strip() in ('---','***'):
            flush();
            if inlist: out.append('</ul>'); inlist=False
            out.append('<hr>'); continue
        if line.startswith('- '):
            flush()
            if not inlist: out.append('<ul>'); inlist=True
            out.append('<li>'+md_inline(line[2:])+'</li>'); continue
        para.append(line)
    flush()
    if inlist: out.append('</ul>')
    if fence: out.append('</pre>')
    return '\n'.join(out)

# ---------- load ----------
def load_all():
    items=[]
    for p in sorted(CONTENT.rglob('*.md')):
        text=p.read_text()
        m=re.match(r'---\n(.*?)\n---\n?(.*)', text, re.S)
        fm = yaml.safe_load(m.group(1)) if m else {}
        body = m.group(2) if m else text
        rel = p.relative_to(CONTENT)
        items.append(dict(fm=fm or {}, body=body, rel=rel))
    return items

def year_of(d):
    if d is None: return None
    s=str(d); m=re.match(r'(\d{4})', s)
    return int(m.group(1)) if m else None

def node_color(era): return ERA_COLOR.get(era, '#e8c874')

# ---------- page chrome ----------
NAV = [('Timeline','index.html'),('Works','works/index.html'),('Craft','craft/index.html'),
       ('Eras','eras/index.html'),('People','people/index.html'),('Places','places/index.html'),
       ('Sources','BIBLIOGRAPHY.html')]

MUSEUM_CSS = """
:root{--ink:#1d1a16;--paper:#f7f3ea;--paper2:#efe9db;--rule:#ddd5c2;--acc:#7a6a3e;--dim:#6d675c}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0c18;font-family:Georgia,'Times New Roman',serif;color:var(--ink)}
nav{background:#0a0c18;padding:15px 28px;display:flex;gap:26px;align-items:baseline;flex-wrap:wrap}
nav a{color:#8f96ab;text-decoration:none;font-family:-apple-system,'Inter',sans-serif;font-size:11px;
  letter-spacing:.22em;text-transform:uppercase}
nav a:hover,nav a.on{color:#e8c874}
nav .brand{color:#e9e2cf;font-family:Georgia,serif;font-size:13px;letter-spacing:.24em;margin-right:12px}
nav .brand b{color:#e8c874;font-weight:400}
main{background:var(--paper);min-height:calc(100vh - 46px)}
.sheet{max-width:720px;margin:0 auto;padding:64px 28px 90px}
.era-line{font-family:-apple-system,'Inter',sans-serif;font-size:10.5px;letter-spacing:.3em;
  text-transform:uppercase;color:var(--acc);margin-bottom:16px}
h1{font-weight:400;font-size:31px;line-height:1.22;margin-bottom:10px}
.date{font-style:italic;color:var(--dim);font-size:14.5px;margin-bottom:26px}
.chip{display:inline-block;font-family:-apple-system,'Inter',sans-serif;font-size:10px;letter-spacing:.22em;
  text-transform:uppercase;padding:4px 10px;border:1px solid #c9bd9e;border-radius:2px;color:var(--acc);margin:0 6px 22px 0}
.facts{background:var(--paper2);border:1px solid var(--rule);border-radius:3px;padding:18px 22px;margin:0 0 30px;
  font-family:-apple-system,'Inter',sans-serif;font-size:12.5px;line-height:1.7;color:#4c463c}
.facts b{color:var(--ink);font-weight:600}
.facts a{color:var(--acc)}
.body{font-size:16px;line-height:1.75;color:#2b2620}
.body p{margin-bottom:1.15em}
.body h2,.body h3,.body h4{font-weight:400;margin:1.5em 0 .6em}
.body a{color:var(--acc)}
.body ul{margin:0 0 1.15em 1.3em}
.body li{margin-bottom:.4em}
.body pre{background:#141622;color:#cdd5e8;font-size:12.5px;padding:16px;border-radius:4px;
  overflow-x:auto;margin-bottom:1.15em;font-family:ui-monospace,Menlo,monospace;line-height:1.55}
.body hr{border:none;border-top:1px solid var(--rule);margin:2em 0}
.sources{margin-top:44px;padding-top:20px;border-top:1px solid var(--rule);
  font-family:-apple-system,'Inter',sans-serif;font-size:12px;color:#8a8272;line-height:1.8}
.sources b{letter-spacing:.18em;text-transform:uppercase;font-size:10px}
.idx h2{font-weight:400;font-size:22px;margin:2em 0 .7em;color:var(--ink)}
.idx ul{list-style:none;margin:0}
.idx li{padding:9px 0;border-bottom:1px solid var(--rule);font-size:15.5px}
.idx li a{color:var(--ink);text-decoration:none}
.idx li a:hover{color:var(--acc)}
.idx li small{color:var(--dim);font-family:-apple-system,'Inter',sans-serif;font-size:11.5px;margin-left:10px}
.fig{margin:0 0 32px}
.fig img{width:100%;border-radius:4px;border:1px solid var(--rule);display:block}
.fig figcaption{font-family:-apple-system,'Inter',sans-serif;font-size:11.5px;color:#8a8272;margin-top:9px;line-height:1.55}
@media (max-width:640px){
  nav{padding:12px 16px;gap:14px;overflow-x:auto;white-space:nowrap;flex-wrap:nowrap;-webkit-overflow-scrolling:touch}
  nav a{font-size:10px;letter-spacing:.16em}
  .sheet{padding:40px 20px 64px}
  h1{font-size:25px}
  .body{font-size:15.5px}
  .facts{padding:14px 16px}
}
"""

def nav_html(depth, active=''):
    pre='../'*depth
    links=''.join(f'<a href="{pre}{h}" class="{"on" if n==active else ""}">{n}</a>' for n,h in NAV)
    return f'<nav><span class="brand">The <b>Bach</b> Timeline</span>{links}</nav>'

def page(depth, title, inner, active=''):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)} — The Bach Timeline</title>
<link rel="stylesheet" href="{'../'*depth}assets/museum.css"></head>
<body>{nav_html(depth, active)}<main><div class="sheet">{inner}</div></main></body></html>"""

def era_name(items, era_id):
    for it in items:
        if it['fm'].get('type')=='era' and it['fm'].get('id')==era_id:
            return it['fm'].get('title', era_id)
    return (era_id or '').replace('-',' ').title()

# ---------- item pages ----------
def build_item(it, items):
    fm, rel = it['fm'], it['rel']
    depth = len(rel.parts)-1
    t = fm.get('type')
    title = fm.get('title') or fm.get('name') or rel.stem
    body_html = md_to_html(it['body'])
    head=[]
    if t in ('event','work','era'):
        era = fm.get('era') or ''
        head.append(f'<div class="era-line">{html.escape(era_name(items, era))}</div>')
    head.append(f'<h1>{md_inline(html.escape(title))}</h1>')
    date = fm.get('date') or fm.get('date_composed') or fm.get('years') or ''
    dd = fm.get('d') or ''
    if t=='event':
        span = f"{date}" + (f" – {fm['date_end']}" if fm.get('date_end') else '')
        head.append(f'<div class="date">{span} · {html.escape(str(fm.get("place","")))}</div>')
    elif t=='work':
        head.append(f'<div class="date">BWV {html.escape(str(fm.get("bwv","")))} · {html.escape(str(fm.get("key") or ""))} · {date}</div>')
    elif t=='person':
        head.append(f'<div class="date">{fm.get("born","")} – {fm.get("died") or ""} · {html.escape(fm.get("relationship",""))}</div>')
    elif t=='place':
        head.append(f'<div class="date">{html.escape(fm.get("bach_years",""))} · {html.escape(fm.get("role",""))}</div>')
    elif t=='era':
        head.append(f'<div class="date">{html.escape(str(fm.get("years","")))}</div>')
    prov = fm.get('provenance')
    if prov: head.append(f'<span class="chip">{prov}</span>')
    facts=[]
    if t=='work':
        if fm.get('forces'): facts.append(f"<b>Forces</b> — {html.escape(fm['forces'])}")
        if fm.get('occasion'): facts.append(f"<b>Occasion</b> — {html.escape(fm['occasion'])}")
        if fm.get('dating_note'): facts.append(f"<b>Dating</b> — {md_inline(html.escape(fm['dating_note']))}")
        r=fm.get('recording') or {}
        if isinstance(r,dict) and r.get('performer'):
            shelf='../'*depth+'BIBLIOGRAPHY.html'
            facts.append(f"<b>Recommended recording</b> — {html.escape(r['performer'])}"
                         + (f", <i>{html.escape(r['album'])}</i>" if r.get('album') else '')
                         + f' &nbsp;·&nbsp; <a href="{shelf}">Recordings Shelf</a>')
        if fm.get('score_imslp'):
            facts.append(f'<b>Score</b> — <a href="{fm["score_imslp"]}">IMSLP (free score)</a>')
    if facts: head.append('<div class="facts">'+'<br>'.join(facts)+'</div>')
    im=IMAGES.get(fm.get('id'))
    if im:
        src='../'*depth+'assets/images/'+im['file']
        cap=html.escape(im.get('caption','')) + (' &nbsp;·&nbsp; '+html.escape(im['credit']) if im.get('credit') else '')
        head.append(f'<figure class="fig"><img src="{src}" alt="{html.escape(im.get("caption",""))}"><figcaption>{cap}</figcaption></figure>')
    src = fm.get('sources') or []
    tail = ''
    if src:
        tail = '<div class="sources"><b>Sources</b><br>'+ '<br>'.join(html.escape(str(s)) for s in src) \
             + f'<br><a href="{"../"*depth}BIBLIOGRAPHY.html">→ full bibliography &amp; links</a></div>'
    inner = ''.join(head) + f'<div class="body">{body_html}</div>' + tail
    out = DOCS/rel.with_suffix('.html')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(depth, title, inner, active_for(rel)))

def active_for(rel):
    top = rel.parts[0]
    return {'works':'Works','craft':'Craft','eras':'Eras','people':'People','places':'Places'}.get(top,'')

# ---------- indexes ----------
def li(href, label, small=''):
    return f'<li><a href="{href}">{label}</a>{f"<small>{small}</small>" if small else ""}</li>'

def build_indexes(items):
    # works by genre
    works=[i for i in items if i['fm'].get('type')=='work']
    sec=['<h1>The Works</h1><div class="date">181 featured works & sets · every card links a score and a recording</div>']
    for g,label in GENRES:
        rows=sorted([w for w in works if w['fm'].get('genre')==g],
                    key=lambda w:(str(w['fm'].get('bwv','')).zfill(6)))
        if not rows: continue
        sec.append(f'<h2>{label}</h2><ul>')
        for w in rows:
            href='/'.join(w['rel'].with_suffix('.html').parts[1:])
            sec.append(li(href, html.escape(w['fm'].get('title','')), f"BWV {w['fm'].get('bwv','')}"))
        sec.append('</ul>')
    (DOCS/'works').mkdir(parents=True, exist_ok=True)
    (DOCS/'works/index.html').write_text(page(1,'The Works','<div class="idx">'+''.join(sec)+'</div>','Works'))
    # craft
    essays=sorted([i for i in items if i['fm'].get('type')=='essay'], key=lambda i:i['fm'].get('order',99))
    sec=['<h1>The Craft</h1><div class="date">Seven essays on the counterpoint that drove everything</div><ul>']
    for e in essays:
        href=e['rel'].with_suffix('.html').name
        sec.append(li(href, f"{e['fm'].get('order','')}. "+html.escape(e['fm'].get('title',''))))
    sec.append('</ul>')
    (DOCS/'craft/index.html').write_text(page(1,'The Craft','<div class="idx">'+''.join(sec)+'</div>','Craft'))
    # eras
    eras={i['fm'].get('id'):i for i in items if i['fm'].get('type')=='era'}
    sec=['<h1>The Eras</h1><div class="date">Ten rooms of the Life · the Eclipse · the Rediscovery · the Living Bach</div><ul>']
    for eid in ERA_ORDER:
        if eid in eras:
            e=eras[eid]
            sec.append(li(e['rel'].with_suffix('.html').name, html.escape(e['fm'].get('title','')), str(e['fm'].get('years',''))))
    sec.append('</ul>')
    (DOCS/'eras/index.html').write_text(page(1,'The Eras','<div class="idx">'+''.join(sec)+'</div>','Eras'))
    # people / places
    for t,label,sub in (('person','People','the family, the patrons, the rivals, the revivers'),
                        ('place','Places','a 200-mile circle — and the cities that kept him')):
        rows=sorted([i for i in items if i['fm'].get('type')==t], key=lambda i:i['fm'].get('name',''))
        sec=[f'<h1>{label}</h1><div class="date">{sub}</div><ul>']
        for r in rows:
            small = r['fm'].get('relationship') or r['fm'].get('role') or ''
            sec.append(li(r['rel'].with_suffix('.html').name, html.escape(r['fm'].get('name','')), html.escape(str(small))))
        sec.append('</ul>')
        d='people' if t=='person' else 'places'
        (DOCS/d/'index.html').write_text(page(1,label,'<div class="idx">'+''.join(sec)+'</div>',label))

# ---------- ribbon ----------
def build_ribbon(items):
    evs=[]
    eras={i['fm'].get('id'):i for i in items if i['fm'].get('type')=='era'}
    for i in items:
        fm=i['fm']
        if fm.get('type')!='event': continue
        y=year_of(fm.get('date'))
        if not y: continue
        mstr,yf = fdate(fm.get('date'), fm.get('date_precision') or 'year')
        im=IMAGES.get(fm.get('id'))
        evs.append(dict(y=y, yf=round(yf,3), m=mstr, t=fm.get('title',''), s=(fm.get('summary') or '').strip(),
            d=str(fm.get('date','')), era=era_name(items, fm.get('era','')),
            flag=(fm.get('provenance') or '').title(), c=node_color(fm.get('era')),
            img=('assets/images/thumbs/'+im['file']) if im else None,
            href='/'.join(i['rel'].with_suffix('.html').parts)))
    evs.sort(key=lambda e:e['y'])
    sublabels=[dict(y0=year_of(eras[e]['fm'].get('years')) if eras.get(e) else None,
                    name=eras[e]['fm'].get('title','').split(':')[0], years=str(eras[e]['fm'].get('years','')))
               for e in ERA_ORDER[:10] if e in eras]
    tpl=(ROOT/'design'/'ribbon.html').read_text()
    payload=json.dumps(evs, ensure_ascii=False)
    tpl=tpl.replace('[/*__EVENTS__*/]', payload)
    # nav bar injection
    navbar=nav_html(0,'Timeline').replace('<nav>','<nav style="position:fixed;top:0;left:0;right:0;z-index:6;background:transparent;overflow-x:auto;white-space:nowrap;-webkit-overflow-scrolling:touch">')
    tpl=tpl.replace('<header>', navbar+'<header style="top:42px">')
    tpl=tpl.replace('<h1>The <b>Bach</b> Timeline</h1>', '<span></span>')  # nav brand already carries the title
    tpl=tpl.replace('</title>','</title>\n<link rel="stylesheet" href="assets/nav.css">')
    (DOCS/'assets').mkdir(parents=True, exist_ok=True)
    (DOCS/'assets/nav.css').write_text(
      "nav a{color:#8f96ab;text-decoration:none;font-family:-apple-system,'Inter',sans-serif;font-size:11px;letter-spacing:.22em;text-transform:uppercase;margin-right:24px}"
      "nav a:hover,nav a.on{color:#e8c874}nav{padding:16px 28px}"
      "nav .brand{color:#e9e2cf;font-family:Georgia,serif;font-size:13px;letter-spacing:.24em;margin-right:14px}"
      "nav .brand b{color:#e8c874;font-weight:400}")
    (DOCS/'index.html').write_text(tpl)

# ---------- main ----------
def main():
    if DOCS.exists(): shutil.rmtree(DOCS)
    DOCS.mkdir()
    (DOCS/'.nojekyll').write_text('')
    (DOCS/'assets').mkdir(parents=True, exist_ok=True)
    (DOCS/'assets/museum.css').write_text(MUSEUM_CSS)
    global IMAGES
    IMAGES=load_images()
    imgsrc=ROOT/'assets'/'images'
    if imgsrc.exists():
        shutil.copytree(imgsrc, DOCS/'assets'/'images', dirs_exist_ok=True)
    items=load_all()
    for d in ('craft','eras','people','places','works'):
        (DOCS/d).mkdir(parents=True, exist_ok=True)
    n=0
    for it in items:
        if it['fm'].get('type') in ('event','work','person','place','era','essay'):
            build_item(it, items); n+=1
        else:  # BIBLIOGRAPHY, SCHEMA, reference files
            rel=it['rel']; depth=len(rel.parts)-1
            title=rel.stem.replace('-',' ').title()
            innr=f'<div class="body">{md_to_html(it["body"] if not it["fm"] else it["body"])}</div>'
            out=DOCS/rel.with_suffix('.html'); out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(page(depth, title, innr, 'Sources' if 'BIBLIOGRAPHY' in rel.stem else ''))
            n+=1
    build_indexes(items)
    build_ribbon(items)
    print(f'built {n} pages + indexes + ribbon -> {DOCS}')

if __name__=='__main__':
    main()
