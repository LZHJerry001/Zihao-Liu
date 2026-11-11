#!/usr/bin/env python3
"""Generate a dependency-free academic website from content.py."""
from html import escape as h
from pathlib import Path
import shutil
import content as c

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir()
shutil.copytree(ROOT / 'assets', DIST / 'assets')
shutil.copy(ROOT / 'style.css', DIST / 'style.css')
shutil.copy(ROOT / 'site.js', DIST / 'site.js')

ARROW = '<svg class="link-icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 12 12 4M5 4h7v7"/></svg>'
RIGHT = '<svg class="link-icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4"/></svg>'
NAV = [('Home', '/'), ('Research', '/research/'), ('Talks', '/talks/'), ('Conferences', '/conferences/'), ('Teaching', '/teaching/'), ('Photos', '/photos/')]

def external(url, label, cls='text-link'):
    return f'<a class="{cls}" href="{h(url, quote=True)}" target="_blank" rel="noopener noreferrer">{label} {ARROW}</a>'

def page(title, current, body, description):
    nav = ''.join(f'<a href="{url}"' + (' aria-current="page"' if label == current else '') + f'>{label}</a>' for label, url in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#ffffff">
  <meta name="description" content="{h(description, quote=True)}">
  <title>{h(title)} | Zihao Liu</title>
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/style.css">
  <script>try{{if(localStorage.getItem('theme')==='dark')document.documentElement.dataset.theme='dark'}}catch(e){{}}</script>
  <script src="/site.js" defer></script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="header-inner shell">
    <a class="brand" href="/" aria-label="Zihao Liu home"><span class="brand-mark" aria-hidden="true">Z</span><span>Zihao Liu<span class="brand-dot">.</span></span></a>
    <nav class="desktop-nav" aria-label="Main navigation">{nav}</nav>
    <div class="header-actions">
      <button class="theme-button" type="button" aria-label="Switch to dark mode" title="Toggle dark mode"><svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M2 12h2m16 0h2M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42"/></svg><svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M20.9 13A8.5 8.5 0 0 1 11 3.1 8.5 8.5 0 1 0 20.9 13Z"/></svg></button>
      {external(c.CV, 'CV', 'header-cv')}
      <button class="menu-button" type="button" aria-controls="mobile-nav" aria-expanded="false" aria-label="Open menu"><span></span><span></span></button>
    </div>
  </div>
  <nav class="mobile-nav shell" id="mobile-nav" aria-label="Mobile navigation" hidden>{nav}{external(c.CV, 'Curriculum vitae', 'mobile-cv')}</nav>
</header>
<main id="main">{body}</main>
<footer class="site-footer"><div class="shell footer-inner"><div><a class="footer-name" href="/">Zihao Liu<span class="brand-dot">.</span></a><p>Mathematics · Rice University</p></div><div class="footer-right"><a href="mailto:zl152@rice.edu">zl152@rice.edu</a><span>Houston, Texas</span></div></div><div class="shell footer-bottom"><span>© 2026 Zihao Liu</span><span>Geometry, groups &amp; topology</span></div></footer>
</body></html>'''

def heading(kicker, title, intro):
    return f'<section class="page-heading shell"><p class="eyebrow"><span></span>{kicker}</p><h1>{title}<span class="heading-dot">.</span></h1><p class="page-intro">{intro}</p></section>'

def paper_item(paper, index):
    return f'''<article class="paper-item"><div class="item-number">0{index}</div><div class="paper-main"><h3>{h(paper['title'])}</h3><p class="paper-authors">{h(paper['authors'])}</p><p class="item-meta">{h(paper['publication'])}</p>{external(paper['url'], paper['link'])}</div></article>'''

def talk_item(t):
    date, venue, subject, slides = t
    link = external(slides, 'Slides', 'text-link compact-link') if slides else ''
    return f'<article class="list-row"><div class="row-date">{h(date)}</div><div class="row-content"><h3>{h(subject)}</h3><p>{h(venue)}</p>{link}</div></article>'

def course_item(course):
    date, number, name, school, url = course
    link = external(url, 'Course website', 'text-link compact-link') if url else ''
    return f'<article class="list-row course-row"><div class="row-date">{h(date)}</div><div class="row-content"><p class="course-code">{h(number)}</p><h3>{h(name)}</h3><p>{h(school)}</p>{link}</div></article>'

def photo_card(p, n):
    file, title, caption = p
    return f'<figure class="photo-card photo-{n}"><img src="/assets/{h(file, quote=True)}" alt="{h(caption, quote=True)}" loading="lazy"><figcaption><h3>{h(title)}</h3><p>{h(caption)}</p></figcaption></figure>'

def featured_photos():
    return ''.join(f'<figure><img src="/assets/{h(file, quote=True)}" alt="{h(alt, quote=True)}" loading="lazy"><figcaption>{h(credit)}</figcaption></figure>' for file, alt, credit in c.featured_photos)

home = f'''<section class="home-hero shell"><div class="hero-copy"><p class="eyebrow"><span></span>GEOMETRY · GROUPS · TOPOLOGY</p><h1>Zihao Liu<span class="heading-dot">.</span><small>刘子昊</small></h1><p class="hero-lead">Mathematics Ph.D. candidate<br>at Rice University</p><p class="hero-description">I study geometric group theory and low-dimensional topology, with a particular interest in profinite methods and rigidity.</p><div class="hero-actions"><a class="button primary" href="/research/">Explore my research {RIGHT}</a><a class="button secondary" href="mailto:zl152@rice.edu">Get in touch {ARROW}</a></div></div><figure class="hero-figure"><div class="hero-image-wrap"><img src="/assets/zihao-at-blackboard.jpg" alt="Zihao Liu speaking in front of a blackboard"></div><figcaption><span>AT THE BLACKBOARD</span><span>Photo by Yuxin Yan</span></figcaption></figure></section>
<section class="intro-strip"><div class="shell intro-inner"><div><p class="eyebrow"><span></span>A LITTLE ABOUT ME</p><h2>Curious about the<br>shape of groups<span class="heading-dot">.</span></h2></div><div class="intro-copy"><p>I am a fifth-year Ph.D. candidate in the <a href="https://mathweb.rice.edu/">Department of Mathematics</a> at Rice University, where I work with <a href="https://math.rice.edu/~ar99/">Alan Reid</a>.</p><p>Before coming to Rice, I earned an M.S. in mathematics at Brandeis University in 2021, advised by Kiyoshi Igusa, and a B.S. in mathematics and applied mathematics at Jilin University in 2019, advised by Xiankun Du.</p><a class="text-link" href="/research/">More about my research {RIGHT}</a></div></div></section>
<section class="section shell"><div class="section-heading"><div><p class="eyebrow"><span></span>SELECTED WORK</p><h2>Research</h2></div><a class="section-link" href="/research/">View research {RIGHT}</a></div><div class="paper-list">{''.join(paper_item(p, i) for i, p in enumerate(c.papers,1))}</div></section>
<section class="section soft-section"><div class="shell"><div class="section-heading"><div><p class="eyebrow"><span></span>RECENT PRESENTATIONS</p><h2>Talks &amp; seminars</h2></div><a class="section-link" href="/talks/">All talks {RIGHT}</a></div><div class="talk-list">{''.join(talk_item(t) for t in c.talks[:3])}</div></div></section>
<section class="home-bottom shell"><div><p class="eyebrow"><span></span>BEYOND THE BLACKBOARD</p><h2>Mathematics is<br>better together<span class="heading-dot">.</span></h2><p>A few moments from conferences, travels, and time with friends.</p><a class="text-link" href="/photos/">Visit the photo gallery {RIGHT}</a></div><a class="home-photo" href="/photos/" aria-label="Visit the photo gallery"><img src="/assets/great-wall.jpg" alt="A group of mathematicians on the Great Wall" loading="lazy"><span>THE GREAT WALL <b aria-hidden="true">↗</b></span></a></section>
<section class="featured-photos shell"><div class="section-heading small"><h2>More moments</h2><a class="section-link" href="/photos/">View all photos {RIGHT}</a></div><div class="featured-photo-grid">{featured_photos()}</div></section>'''

research = heading('RESEARCH', 'Research', 'I am interested in geometric group theory and low-dimensional topology, especially the ways that finite quotients reflect the structure of infinite groups.') + f'''<section class="shell page-section research-intro"><div class="side-label">RESEARCH INTERESTS</div><div class="long-copy"><p>My work centers on profinite completions of mapping class groups and Artin groups, and on questions of rigidity, subgroup structure, and the relationship between geometric and algebraic invariants.</p><div class="tag-list"><span>Geometric group theory</span><span>Low-dimensional topology</span><span>Profinite groups</span><span>Artin groups</span><span>Mapping class groups</span></div></div></section><section class="shell page-section"><div class="section-heading"><div><p class="eyebrow"><span></span>PAPERS &amp; PREPRINTS</p><h2>Selected work</h2></div></div><div class="paper-list">{''.join(paper_item(p, i) for i,p in enumerate(c.papers,1))}</div></section>'''

talks = heading('PRESENTATIONS', 'Talks', 'A selection of seminars, conference talks, and mathematical conversations.') + f'''<section class="shell page-section"><div class="section-heading small"><h2>Seminars &amp; talks</h2><span class="section-count">{len(c.talks):02d} TALKS</span></div><div class="talk-list">{''.join(talk_item(t) for t in c.talks)}</div></section>'''

conference_groups = ''
for i, (year, events) in enumerate(c.conferences.items()):
    rows = ''.join(f'<li><span>{h(month)}</span><div><strong>{h(name)}</strong><p>{h(location)}</p></div></li>' for month,name,location in events)
    conference_groups += f'<details class="year-group" {"open" if i == 0 else ""}><summary><span>{year}</span><span class="year-count">{len(events):02d} EVENTS</span><span class="year-icon" aria-hidden="true"></span></summary><ul>{rows}</ul></details>'
conferences = heading('MEETINGS &amp; WORKSHOPS', 'Conferences', 'Some conferences, workshops, and mathematical gatherings I have attended.') + f'<section class="shell page-section conferences-section"><p class="section-note">EXPLORE BY YEAR</p>{conference_groups}</section>'

teaching = heading('IN THE CLASSROOM', 'Teaching', 'Courses I have taught and supported at Rice University and Brandeis University.') + f'''<section class="shell page-section"><div class="section-heading small"><h2>Instructor of record</h2><span class="section-count">RICE UNIVERSITY</span></div><div class="talk-list">{''.join(course_item(x) for x in c.instructor)}</div></section><section class="shell page-section teaching-assistant"><div class="section-heading small"><h2>Teaching assistant</h2></div><div class="talk-list">{''.join(course_item(x) for x in c.teaching_assistant)}</div></section><section class="shell recommendation"><div><p class="eyebrow"><span></span>FOR STUDENTS</p><h2>Letters of recommendation</h2></div><div><p>If you were a student in one of my classes and need a letter of recommendation, please email me from your Rice account. A résumé, application materials, or a short paragraph about your interests outside of calculus can be helpful.</p><a class="text-link" href="mailto:zl152@rice.edu">Email me {ARROW}</a></div></section>'''

photos = heading('PEOPLE &amp; PLACES', 'Photos', 'A few favorite moments from travels and gatherings with mathematicians and friends.') + f'<section class="shell page-section"><div class="featured-photo-grid gallery-featured">{featured_photos()}</div><div class="photo-grid">{("".join(photo_card(p, i) for i,p in enumerate(c.photos,1)))}</div></section>'

pages = [('index.html','Home','Home',home,'Zihao Liu is a mathematics Ph.D. candidate at Rice University, studying geometric group theory and low-dimensional topology.'),('research/index.html','Research','Research',research,'Research and papers by Zihao Liu in geometric group theory and low-dimensional topology.'),('talks/index.html','Talks','Talks',talks,'Seminar and conference talks by Zihao Liu.'),('conferences/index.html','Conferences','Conferences',conferences,'Conferences and workshops attended by Zihao Liu.'),('teaching/index.html','Teaching','Teaching',teaching,'Teaching by Zihao Liu at Rice University and Brandeis University.'),('photos/index.html','Photos','Photos',photos,'Photos from Zihao Liu’s travels and mathematical gatherings.')]
for path,title,current,body,description in pages:
    output = DIST / path
    output.parent.mkdir(parents=True, exist_ok=True)
    # Relative links work both at username.github.io/ and in a project subdirectory.
    relative_root = '../' * len(Path(path).parent.parts) or './'
    html = page(title, current, body, description)
    html = html.replace('href="/', 'href="' + relative_root)
    html = html.replace('src="/', 'src="' + relative_root)
    output.write_text(html, encoding='utf-8')
print(f'Built {len(pages)} pages in {DIST}')
