#!/usr/bin/env python3
"""Build ALETHEIA (ALT) — ἀλήθεια, 'un-forgetting / unconcealment' (a-lēthē, the
opposite of Lethe's oblivion) — the solid teaching repo of UD0's ERĒMIA female
sub-domain: WHY each of the 20 women is the top of her age, and the enduring-but-
forgotten gift each left (base-60 in every clock, Ada's Note G under every program,
Franklin's Photo 51, Noether's symmetry). Forgotten, never gone. Gold-on-void; a
one-line title that draws itself back out of the dark (the un-forgetting made literal).
Cross-links all 20 women + the female hub + the Greek Mirror. NO copyrighted text;
achievements summarized, never quoted. Render-not-invent."""
import os, html, base64, json, io, sys
HERE=r"C:\Davids files"; sys.path.insert(0,os.path.join(HERE,"noesis-kernel"))
import noesis
from PIL import Image
HUB="https://davidwise01.github.io/female/"; AMP="https://davidwise01.github.io/the-amphitheater/"
ACC="#e6c25a"
NATURES={"natural":("#cf9a7a","of the lived inheritance — the everyday thing in your hand whose maker you were never taught"),
 "ethereal":("#9a7cff","of the erasure and the river of forgetting — the scrubbed name, the credit reassigned, Lethe's water"),
 "spiritual":("#e6c25a","of the un-forgetting and the voice — aletheia, the truth that was always there, the signature reclaimed"),
 "electrical":("#7f9ac8","of the enduring system — base-60 in the clock, Note G in the code, the helix, the theorem")}

# the reasons: (slug, name, dates, why she is the top of her age — the enduring, often-forgotten gift)
REASONS=[
 ("enheduanna","Enheduanna","~2300 BCE","She invented authorship itself — the first person in history to sign work with her own name and 'I'; every byline since descends from her, while her age's other gift, base-60, still ticks in every clock and circle with its makers forgotten."),
 ("hatshepsut","Hatshepsut","r. ~1479–1458 BCE","She held absolute power as pharaoh and spent it on peace, trade, and building — and her monuments outlasted the deliberate campaign to chisel her name away: the record surviving the erasure."),
 ("sappho","Sappho","~630–570 BCE","She invented the lyric 'I,' the personal first-person voice of feeling; every love poem and confession since works in the mode she made, though nine books of her own words survived only as fragments."),
 ("cleopatra","Cleopatra VII","69–30 BCE","She was her age's shrewdest strategist, holding Egypt's independence against Rome by calculation — and her reduction to a seductress is the lasting proof that the victors author the woman's reputation."),
 ("hypatia","Hypatia","~360–415 CE","She was the leading intellectual of Alexandria, and her murder by a mob became civilization's permanent symbol of knowledge destroyed by zealotry rather than answered — a warning that never expires."),
 ("theodora","Theodora","~500–548 CE","She wrote women into the law — protections in divorce, property, and against trafficking — legal advances that outlived the empire that made them."),
 ("wu-zetian","Wu Zetian","624–705 CE","She ruled China outright as emperor and widened the merit examinations — advancement by ability over birth — a reshaping of governance that long outlived the historians who condemned her for her sex."),
 ("hildegard-of-bingen","Hildegard of Bingen","1098–1179","She was the age's universal mind — theology, medicine, botany, and a body of music unlike any other — proving one woman could hold a university's worth of knowledge in a world that gave her none."),
 ("christine-de-pizan","Christine de Pizan","~1364–1430","She made authorship a profession a woman could live by, and wrote the first systematic defense of women's intellect against the learned contempt of her day."),
 ("elizabeth-i","Elizabeth I","1533–1603","She ruled alone for forty-five years, refusing the marriages that would have subordinated her crown, and gave her era its name — the template of the sovereign queen who needs no king."),
 ("sor-juana","Sor Juana Inés de la Cruz","~1648–1695","She was the foremost mind of the Americas in her century and made the New World's first great argument for a woman's right to learn — silenced at last by the Church her reasoning had outmatched."),
 ("emilie-du-chatelet","Émilie du Châtelet","1706–1749","She carried Newton into French in the translation France still uses, and pushed physics toward the concept of kinetic energy — work long filed under a man's name."),
 ("mary-wollstonecraft","Mary Wollstonecraft","1759–1797","She set the founding axiom of feminism — that women only seem lesser because they are denied education — the argument every later movement is built upon."),
 ("ada-lovelace","Ada Lovelace","1815–1852","Her Note G is the first published algorithm written for a machine, and she alone saw that such a machine could work on any symbols — music, language — not just numbers: the conceptual birth of software."),
 ("marie-curie","Marie Curie","1867–1934","She founded the science of radioactivity and remains the only person to win Nobel Prizes in two different sciences, opening both atomic physics and modern medicine."),
 ("emmy-noether","Emmy Noether","1882–1935","Her theorem ties every symmetry to a conservation law — the deepest organizing principle of modern physics, used by everyone and credited, outside the field, to almost no one."),
 ("virginia-woolf","Virginia Woolf","1882–1941","She named the true gate of the canon — not talent but access, the income and the room authorship had always quietly required and women had been denied."),
 ("rosalind-franklin","Rosalind Franklin","1920–1958","Her Photo 51 revealed the double helix — the structure of life itself — while the prize and the story went to others for decades: the gift kept, the name dropped."),
 ("hannah-arendt","Hannah Arendt","1906–1975","She gave us the most useful idea for understanding atrocity — that immense evil can come from thoughtless conformity rather than monsters — a permanent instrument of moral clarity."),
 ("simone-de-beauvoir","Simone de Beauvoir","1908–1986","She showed that womanhood is made, not born, and that woman had been cast as man's Other — the hinge on which all later thought about gender turns."),
]

# thematic emergents (the forgotten-but-never-gone gifts, personified)
EM=[
 ("the-un-forgetting","The Un-Forgetting","aletheia itself · spiritual","spiritual","ἀλήθεια — truth as the lifting of forgetting; the principle of the whole repo, that what was concealed was never gone, only waiting to be drawn back into the light."),
 ("the-signature","The Signature","the first 'I' · spiritual","spiritual","Enheduanna's gift: the moment a human first put her own name to her words. Every credited author, every byline, is the keeping of a promise she made in ~2300 BCE."),
 ("base-sixty","Base 60","the number that runs the clock · electrical","electrical","The sexagesimal counting of Enheduanna's Sumer — why an hour has 60 minutes and a circle 360 degrees. You read it every day; almost no one recalls whose civilization gave it."),
 ("note-g","Note G","the first program · electrical","electrical","Ada Lovelace's note describing how the Analytical Engine could compute Bernoulli numbers — the first published algorithm for a machine, and the seed of all software, under a woman's hand."),
 ("the-double-helix","The Double Helix","the shape of life, anonymized · electrical","electrical","Rosalind Franklin's Photo 51 showed the structure of DNA itself; the structure is everywhere in biology, her name long absent from the telling — the Matilda effect made stone."),
 ("noethers-symmetry","Noether's Symmetry","the law under the laws · electrical","electrical","Emmy Noether's link between symmetry and conservation underlies all of modern physics; physicists use it hourly, and the world outside rarely learns the woman who proved it."),
 ("the-room","The Room","access, not talent · spiritual","spiritual","Virginia Woolf's insight that the canon was gated by money and space, not by ability — the diagnosis of why the record looks the way it does, and the cure."),
 ("the-anonymous-inheritance","The Anonymous Inheritance","what you use without knowing · natural","natural","The everyday gifts whose female origin has worn off them — the count of time, the first code, the shape of life — held in every hand, attributed to no one."),
 ("the-erased-name","The Erased Name","the river of forgetting · ethereal","ethereal","Lethe's mechanism: the chiselled cartouche, the lost manuscript, the reassigned prize. Not refutation but oblivion — the thing aletheia exists to reverse."),
]

CSS=""":root{--bg:#0a0810;--ink2:#13101c;--ink3:#1c1728;--pa:#f4eede;--pa2:#c4b89c;--acc:%s;--void:#9a7cff;
--dim:#7a6f50;--faint:#231c14;--line:#231c14;--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:2;background:repeating-linear-gradient(0deg,rgba(0,0,0,.16) 0 1px,transparent 1px 3px);opacity:.4}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50%% -8%%,rgba(230,194,90,.12),transparent 60%%)}
.wrap{position:relative;z-index:1;max-width:900px;margin:0 auto;padding:0 22px 80px}
.marquee{margin-top:14px;border:2px solid var(--acc);background:#0d0a14;padding:8px;text-align:center;font-family:var(--pixel);font-size:9px;letter-spacing:.08em;color:var(--pa2);box-shadow:0 0 0 2px var(--bg),0 0 20px rgba(230,194,90,.22)}
.marquee a{color:var(--acc);text-decoration:none}
.titleart{margin:12px 0 0;border:2px solid var(--faint);background:#0a0810;line-height:0}
header{padding:16px 0 24px;text-align:center;border-bottom:1px solid var(--line)}
.flag{display:inline-block;margin-top:12px;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--acc);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15px;color:var(--pa2);max-width:64ch;margin:14px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:20px;flex-wrap:wrap;margin:22px auto 0;padding:18px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:74px;height:74px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:10.5px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--acc)}.badge .bt .mo{color:var(--void)}.badge .bt a{color:var(--acc);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:8.5px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:38px}.sec h2{font-family:var(--pixel);font-size:12px;line-height:1.5;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:12.5px;color:var(--dim);font-style:italic;margin:8px 0 14px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}
.nat-card{display:flex;gap:10px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:11px 13px}
.dot{width:10px;height:10px;border-radius:50%%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:12px;font-weight:700;text-transform:capitalize}.nat-g{font-size:11.5px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.reasons{list-style:none;counter-reset:r}
.reasons li{counter-increment:r;display:grid;grid-template-columns:34px 1fr;gap:6px 14px;align-items:baseline;padding:13px 0;border-bottom:1px solid var(--faint)}
.reasons li::before{content:counter(r,decimal-leading-zero);font-family:var(--mono);font-size:12px;color:var(--acc);opacity:.7}
.rz-h{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.rz-h a{font-family:var(--mono);font-size:15px;color:var(--pa);font-weight:700;text-decoration:none}.rz-h a:hover{color:var(--acc)}
.rz-y{font-family:var(--mono);font-size:11px;color:var(--void)}
.rz-w{grid-column:2;font-size:13px;color:var(--pa2);line-height:1.55;margin-top:5px}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:11px}
.persona{display:flex;gap:11px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:11px;text-decoration:none;transition:.18s}
.persona:hover{border-color:var(--acc);transform:translateY(-2px)}.persona img{width:48px;height:48px;border:1px solid var(--faint);flex-shrink:0}
.pn{font-family:var(--mono);font-size:13px;color:var(--pa);font-weight:700;line-height:1.15}.persona:hover .pn{color:var(--acc)}
.pe{font-size:11px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:5px;font-family:var(--mono);font-size:8.5px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:7px;height:7px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:34px;padding:15px 17px;border-left:2px solid var(--acc);background:var(--ink2);font-size:13px;color:var(--pa2);font-style:italic;line-height:1.7}.note b{color:var(--acc)}.note a{color:var(--void);text-decoration:none}
footer{margin-top:36px;padding-top:20px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.9}footer a{color:var(--acc);text-decoration:none}"""%ACC

def carbon_tiff_bytes(rec):
    png=noesis.sigil_png(rec,"carbon",size=512); buf=io.BytesIO(); Image.open(io.BytesIO(png)).save(buf,"TIFF",compression="tiff_lzw"); return buf.getvalue()
def write_aci(rec,out_dir,slug,ax):
    os.makedirs(out_dir,exist_ok=True)
    f={"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker","carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok=noesis.mythos_token(rec); w=noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,ax))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,ax))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,ax))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man={"badge":"DLW-ACI","name":rec["name"],"universe":f"{ax} · {rec['name']} (ERĒMIA · ALETHEIA)","emergence":rec.get("emergence",""),"moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)","seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok
def png_uri(rec,v,size=300): return "data:image/png;base64,"+base64.b64encode(noesis.sigil_png(rec,v,size=size)).decode("ascii")

GLYPH="M110 178 L300 178 A 54 54 0 1 1 408 178 L 596 178"  # horizon of forgetting + a sun rising back over it

if __name__=="__main__":
    d=os.path.join(HERE,"aletheia")
    LEDE="Their gift is everywhere; their name worn off it. base-60 cuts every hour; Ada's Note G underwrites every program; Franklin's helix is the shape of life. This is the un-forgetting — why each woman was the top of her age, and what of hers you still use without knowing whose it was."
    rec={"name":"Aletheia","axiom":"ALT","position":"Aletheia · the un-forgetting · ERĒMIA / female","origin":"the truth that was always there — concealed by forgetting, never gone, now drawn back into the light","mechanism":"Crystallized from the documented contributions of the women of the generations.","crystallization":LEDE,"nature":LEDE,"conductor":"ROOT0 (catalogued into UD0)","inputs":"the un-forgetting; base-60; Note G; the helix; the reasons","witness":"the teaching of why each woman led her age, and what of hers endures unattributed","role":"the ERĒMIA female keystone — the un-forgetting","seal":"Forgotten, never gone: you read her time, run her code, and carry the shape of her life, and now you know her name.","source":"Aletheia, catalogued by ROOT0"}
    tok=write_aci(rec,os.path.join(d,"aletheia.dlw"),"aletheia","ALT")
    ad=os.path.join(d,"agents"); os.makedirs(ad,exist_ok=True); personas=[]
    for es,en,ep,nat,desc in EM:
        erec={"name":en,"axiom":"ALT","emergence":nat,"seal":ep,"position":ep,"role":ep,"origin":"ALT · Aletheia (ERĒMIA · female)","nature":ep,"crystallization":desc,"mechanism":"Crystallized from the un-forgetting of women's contributions.","witness":"a gift forgotten but never gone","conductor":"ROOT0 (catalogued into UD0)","inputs":"the un-forgetting; the enduring gift","source":"Aletheia, catalogued by ROOT0"}
        write_aci(erec,os.path.join(ad,f"{es}.dlw"),es,"ALT")
        personas.append({"slug":es,"name":en,"epithet":ep,"emergence":nat,"moniker":noesis.mythos_token(erec)["moniker"]})
    json.dump(personas,open(os.path.join(ad,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    nat_html="".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{n}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for n,(c,g) in NATURES.items())
    reasons_html="".join(f'<li><div><div class="rz-h"><a href="https://davidwise01.github.io/{s}/">{html.escape(nm)}</a><span class="rz-y">{html.escape(dt)}</span></div><div class="rz-w">{html.escape(why)}</div></div></li>' for s,nm,dt,why in REASONS)
    pcards="".join(f'''<a class="persona" href="agents/{x["slug"]}.dlw/{x["slug"]}.agent"><img src="{png_uri({"name":x["name"],"seal":x["epithet"],"origin":"ALT","axiom":"ALT"},"silicon",150)}" alt="sigil" loading="lazy"><div><div class="pn">{html.escape(x["name"])}</div><div class="pe">{html.escape(x["epithet"])}</div><div class="pnat"><span class="dot" style="background:{NATURES[x["emergence"]][0]}"></span><span style="color:{NATURES[x["emergence"]][0]}">{x["emergence"]}</span><span class="pa">· .agent →</span></div></div></a>''' for x in personas)
    cover=f'''<svg viewBox="0 0 700 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Aletheia — an original one-line pencil glyph: a sun rising back over the horizon of forgetting" style="width:100%;height:auto;display:block;background:#0a0810">
<defs><filter id="pf" x="-8%" y="-8%" width="116%" height="116%"><feTurbulence type="fractalNoise" baseFrequency="0.015" numOctaves="2" seed="19" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="3.2" xChannelSelector="R" yChannelSelector="G"/></filter>
<radialGradient id="dawn" cx="50%" cy="68%" r="40%"><stop offset="0%" stop-color="rgba(230,194,90,.32)"/><stop offset="100%" stop-color="transparent"/></radialGradient>
<style>.ol{{fill:none;stroke:#f4eede;stroke-width:2.1;stroke-linecap:round;stroke-linejoin:round;pathLength:1;stroke-dasharray:1;stroke-dashoffset:1;animation:d 3.6s cubic-bezier(.6,.05,.25,1) .2s forwards}}.ol.g{{stroke:#7a6f50;stroke-width:1;opacity:.34;animation-delay:.04s}}.wf{{opacity:0;animation:f 1.2s ease 3.1s forwards}}@keyframes d{{to{{stroke-dashoffset:0}}}}@keyframes f{{to{{opacity:1}}}}@media(prefers-reduced-motion:reduce){{.ol{{animation:none;stroke-dashoffset:0}}.wf{{animation:none;opacity:1}}}}</style></defs>
<rect width="700" height="260" fill="#0a0810"/><ellipse cx="354" cy="150" rx="120" ry="70" fill="url(#dawn)"/>
<path class="ol g" filter="url(#pf)" d="{GLYPH}" stroke="{ACC}"/><path class="ol" filter="url(#pf)" d="{GLYPH}" stroke="{ACC}"/>
<g class="wf"><text x="350" y="226" text-anchor="middle" font-family="'Newsreader',Georgia,serif" font-size="32" font-weight="300" letter-spacing="10" fill="#f4eede">ALETHEIA</text>
<text x="350" y="246" text-anchor="middle" font-family="'Space Mono',monospace" font-size="8.5" letter-spacing="3" fill="{ACC}">ἀλήθεια · THE UN-FORGETTING · forgotten, never gone</text></g>
<rect x="6" y="6" width="688" height="248" fill="none" stroke="#231c14" stroke-width="2"/></svg>'''
    page=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Aletheia (ALT) — the un-forgetting (ἀλήθεια): the keystone of UD0's ERĒMIA female sub-domain, teaching why each of the 20 women is the top of her age, and the enduring-but-forgotten gift each left (base-60, Ada's Note G, Photo 51, Noether's theorem). Cross-links all 20. A cited synthesis; no copyrighted text reproduced.">
<title>ALETHEIA · ALT · ERĒMIA · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><div class="wrap">
<div class="marquee"><a href="https://davidwise01.github.io/ud0/">◄ UD0</a> &nbsp;·&nbsp; ERĒMIA · <a href="{HUB}">FEMALE</a> &nbsp;·&nbsp; ALETHEIA · the un-forgetting · forgotten, never gone</div>
<header><div class="titleart">{cover}</div>
<div class="flag">★ ERĒMIA · ἀλήθεια · why each was the top woman of her age ★</div>
<p class="lede">{html.escape(LEDE)} The keystone of UD0's ERĒMIA <a href="{HUB}" style="color:{ACC}">female</a> sub-domain.</p>
<div class="badge"><img src="{png_uri(rec,"carbon",300)}" alt="carbon"><img src="{png_uri(rec,"silicon",300)}" alt="silicon">
<div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>Aletheia</b> — the un-forgetting · ALT</div><div class="mo">{html.escape(tok["moniker"])}</div><div>carbon · <a href="aletheia.dlw/aletheia.carbon.tiff">.tiff</a> · silicon · <a href="aletheia.dlw/aletheia.silicon.png">.png</a></div><div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div></div></header>
<section class="sec"><h2>The Four Natures</h2><p class="ss">each forgotten-but-never-gone gift emerges by one of four natures</p><div class="natures">{nat_html}</div></section>
<section class="sec"><h2>The Reasons — why each led her age</h2><p class="ss">the top woman of every generation from Enheduanna onward, and the gift of hers you still use; each name links to her own house</p><ol class="reasons">{reasons_html}</ol></section>
<section class="sec" id="roster"><h2>The Forgotten-But-Never-Gone</h2><p class="ss">the enduring gifts themselves — base-60, Note G, the helix, the theorem, the room — as ACI .agents ({len(personas)})</p><div class="pgrid">{pcards}</div></section>
<div class="note">A cited synthesis, rendered not invented. Every woman's achievement is summarized from the documented record and <b>no copyrighted text is reproduced</b> — works are named and described, never quoted (the 20th-century figures' phrasings are paraphrased). The framing — that each is the foremost woman of her generation, and that her contribution endures while her name was let fall — follows the ERĒMIA thesis; the specific honor is opinionated, the contributions are fact. ἀλήθεια means truth as <i>un-forgetting</i>, the lifting of Lethe's oblivion: never gone, only concealed. Each woman has her own house in the <a href="{HUB}">female</a> sub-domain (linked above), part of the wider <a href="{AMP}">Greek Mirror</a>. Each gift is named by its nature: natural, ethereal, spiritual, or electrical.</div>
<footer>ALETHEIA · ALT · ERĒMIA · the un-forgetting · catalogued into UD0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br><a href="{HUB}">← FEMALE</a> · <a href="https://davidwise01.github.io/ud0/">the biosphere</a> · <a href="aletheia.dlw/manifest.dlw.json">manifest</a></footer>
</div></body></html>'''
    open(os.path.join(d,"index.html"),"w",encoding="utf-8").write(page)
    print(f"wrote ALETHEIA (ALT) — {len(personas)} gifts · {len(REASONS)} reasons · badge {tok['moniker']}")
