from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import shutil
ROOT=Path(__file__).resolve().parents[1]
ASSET=ROOT/"docs"/"assets"; ASSET.mkdir(parents=True,exist_ok=True)
S=2
REG=Path("C:/Windows/Fonts/arial.ttf"); BOLD=Path("C:/Windows/Fonts/arialbd.ttf")
def font(n,b=False): return ImageFont.truetype(str(BOLD if b else REG),int(n*S))
def canvas(name,title,w=1500,h=400):
    im=Image.new("RGB",(w*S,h*S),"white"); d=ImageDraw.Draw(im)
    def text(x,y,t,n=32,b=False,c="#173340",anchor=None):
        d.text((x*S,y*S),t,font=font(n,b),fill=c,anchor=anchor,spacing=10*S)
    def box(x,y,w,h,fill="#edf6f7",outline="#277c83"):
        d.rounded_rectangle((x*S,y*S,(x+w)*S,(y+h)*S),radius=12*S,fill=fill,outline=outline,width=3*S)
    def line(points,c="#277c83",width=4):
        d.line([(x*S,y*S) for x,y in points],fill=c,width=width*S)
    def arrow(x1,y1,x2,y2):
        line([(x1,y1),(x2,y2)])
        if x1==x2: pts=[(x2,y2),(x2-9,y2-15),(x2+9,y2-15)]
        else: pts=[(x2,y2),(x2-15,y2-9),(x2-15,y2+9)]
        d.polygon([(x*S,y*S) for x,y in pts],fill="#277c83")
    text(32,22,title,42,True)
    return im,d,text,box,line,arrow
def save(im,name): im.save(ASSET/(name+".png"),optimize=True)
im,d,t,b,l,a=canvas("daily-routine","Every session follows the same sequence",h=310)
labels=[("1  Prepare","Check task and bench"),("2  Work","Use authorised methods"),("3  Return","Count and store items"),("4  Close","Reset and hand over")]
for i,(title,sub) in enumerate(labels):
    x=30+i*370;b(x,100,330,144);t(x+18,119,title,37,True);t(x+18,181,sub,28)
    if i<3:a(x+335,172,x+363,172)
save(im,"daily-routine")
im,d,t,b,l,a=canvas("storage-zones","Use separate labelled locations",h=370)
for x,title,sub,fill,colour in [
 (30,"USABLE STOCK","Identified and accepted\nReturn to the correct bin","#edf6f7","#277c83"),
 (525,"WORK IN PROGRESS","Owner and revision known\nState the next permitted task","#fff5df","#9b731c"),
 (1020,"REVIEW OR QUARANTINE","Do not use or mix with stock\nReport and await staff release","#fff0ec","#a34c3a")]:
    b(x,103,450,178,fill,colour);t(x+18,122,title,31,True);t(x+18,182,sub,28)
t(32,309,"Battery quarantine is separate and managed by authorised staff.",29,True)
save(im,"storage-zones")
im,d,t,b,l,a=canvas("systems-overview","Follow power and control through the aircraft",h=420)
for x,title,sub in [(30,"Battery and distribution","Electrical energy"),(550,"Propulsion units","Motors and ESCs"),(1070,"Aircraft motion","Thrust and movement")]:
    b(x,103,400,116);t(x+18,122,title,31,True);t(x+18,171,sub,28)
a(437,160,540,160);a(957,160,1060,160)
b(550,283,400,105);t(568,301,"Flight controller",32,True);t(568,348,"Commands and feedback",28)
l([(750,283),(750,232)]);d.polygon([(750*S,224*S),(741*S,240*S),(759*S,240*S)],fill="#277c83")
t(32,304,"Structure supports the systems.\nPayloads use approved interfaces.",28)
save(im,"systems-overview")
im,d,t,b,l,a=canvas("printer-safety","Recognise the printer hazards",h=450)
b(530,95,420,290,"#f5f8f9","#173340")
l([(580,143),(580,320),(899,320),(899,143)],"#173340")
l([(580,193),(899,193)],"#173340")
b(718,190,60,50,"#e7f0f2","#173340")
d.polygon([(733*S,241*S),(763*S,241*S),(748*S,268*S)],fill="#b77514")
b(620,300,242,23,"#fff2dc","#b77514")
t(30,115,"MOVING PARTS",34,True);t(30,162,"Keep hands and clothing clear",29);a(425,185,570,193)
t(30,267,"HOT SURFACES",34,True);t(30,314,"Wait for safe temperatures",29);a(425,334,610,312)
t(1010,115,"EMISSIONS",34,True);t(1010,165,"Approved enclosure\nand ventilation",29)
l([(1000,175),(950,175)])
t(1010,278,"STOP CONTROL",34,True);t(1010,327,"Know its location\nbefore the job starts",29)
t(535,400,"Generic filament printer",27)
save(im,"printer-safety")
im,d,t,b,l,a=canvas("build-teams","Six teams meet at controlled integration",h=390)
for i,label in enumerate(["M1  Structure","M2  Powertrain","M3  Power and wiring","M4  Avionics","M5  Payloads","M6  Software and SITL"]):
    x=30+(i%3)*495;y=100+(i//3)*115
    b(x,y,450,87);t(x+18,y+24,label,32,True)
for x in [255,750,1245]: l([(x,302),(x,330),(750,330)])
a(750,330,750,355)
t(804,338,"One integration lead controls the aircraft",27,True)
save(im,"build-teams")
photo=ROOT.parents[1]/"docs"/"images"/"quiver_wide-angle.jpg"
if photo.exists(): shutil.copy2(photo,ASSET/"quiver.jpg")
print("Created five teaching diagrams and copied the project photograph")

