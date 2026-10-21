from PIL import Image
from pathlib import Path
import json

im = Image.open("siripay_4k.png").convert("RGB")
out = Path("email-assets")
out.mkdir(exist_ok=True)
W,H = im.size
bands = [
(0,135,[(860,1110,"offers"),(1110,1330,"experiences"),(1340,1520,"coming"),(1530,1810,"coming")]),
(135,775,[]),
(775,1080,[(55,330,"offers"),(340,615,"experiences"),(625,900,"coming"),(910,1220,"coming")]),
(1080,1105,[]),
(1105,1310,[(60,760,"home")]),
(1310,2460,[]),
(2460,2690,[(80,760,"offers")]),
(2690,3195,[]),
(3195,3395,[(85,760,"experiences")]),
(3395,3535,[(930,1140,"experiences"),(1420,1635,"experiences"),(1930,2140,"experiences")]),
(3535,3630,[]),
(3630,3985,[(870,1460,"coming"),(1480,2140,"coming")]),
(3985,4880,[]),
(4880,5080,[(115,750,"home")]),
(5080,5255,[])
]
rows=[]
for i,(y0,y1,active) in enumerate(bands):
    cut=sorted({0,W,*[v for a,b,t in active for v in (a,b)]})
    parts=[]
    for j,(x0,x1) in enumerate(zip(cut,cut[1:])):
        href=next((kind for a,b,kind in active if a<=x0 and x1<=b),"")
        name=f"r{i:02}_c{j:02}.jpg"
        im.crop((x0,y0,x1,y1)).save(out/name,"JPEG",quality=94,subsampling=0,optimize=True)
        parts.append({"name":name,"w":x1-x0,"h":y1-y0,"link":href})
    rows.append(parts)
(out/"manifest.json").write_text(json.dumps(rows))
print("Generated",sum(len(r) for r in rows),"images")
