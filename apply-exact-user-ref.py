import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

scene_path = r"Fortress-Rush-10-Levels\source\src\scene.ts"
with open(scene_path, 'r', encoding='utf-8') as f:
    scene = f.read()

# 1. Update setView:
# In home view, use hero-north!
old_set_hero = """   if(battle){this.hero.setTexture('hero-north').setOrigin(.506,.956).setFlipX(false);}
   else if(view==='armory'){this.hero.setTexture('hero').setOrigin(.5,1).setFlipX(false);}
   else {this.hero.setTexture('hero').setOrigin(.5,1).setFlipX(false);}"""

new_set_hero = """   if(battle||home){this.hero.setTexture('hero-north').setOrigin(.506,.956).setFlipX(false);}
   else{this.hero.setTexture('hero').setOrigin(.5,1).setFlipX(false);}"""

if old_set_hero in scene:
    scene = scene.replace(old_set_hero, new_set_hero, 1)
    print("1. Set hero-north texture for both battle and home view")
else:
    # try replacing line
    scene = re.sub(
        r'if\(battle\)\{this\.hero\.setTexture\(\'hero-north\'\)[^}]*\}\s*else[^{]*\{this\.hero\.setTexture\(\'[^\']*\'\)[^}]*\}',
        "if(battle||home){this.hero.setTexture('hero-north').setOrigin(.506,.956).setFlipX(false);}\n   else{this.hero.setTexture('hero').setOrigin(.5,1).setFlipX(false);}",
        scene
    )
    print("1b. Replaced setView hero texture with regex")

# 2. Update non-battle update() block in scene.ts:
# We want the tower at (210, 615), hero at (210, deckY() + heroBreath) sized (58, 130)
# and props positioned matching user screenshot:
# cottage (sawmill) at (68, 510), mine at (350, 500), gate at (210, 375)!

old_non_battle_marker = "if(!battle){"
# Find the start of if(!battle) and end at else {
lines = scene.split('\n')
start_idx = None
end_idx = None
for idx, l in enumerate(lines):
    if "if(!battle){" in l:
        start_idx = idx
    if start_idx is not None and "else {" in l and idx > start_idx:
        end_idx = idx
        break

if start_idx is not None and end_idx is not None:
    new_non_battle = """  if(!battle){
   const town=this.view==='town',armory=this.view==='armory',home=this.view==='home';
   const x=210;
   const y=town?429:armory?490:615;
   this.tower.setPosition(x,y+14+Math.sin(time*.0018)*2);
   this.size(this.tower,town?160:armory?208:154);
   const heroBreath=Math.sin(time*.0035)*1.5;
   const heroSquash=1+Math.sin(time*.0035)*.02;

   if(armory){
    this.hero.setPosition(x+4,488+heroBreath);
    this.hero.setDisplaySize(185*(2-heroSquash),185*heroSquash);
   }else if(home){
    this.hero.setPosition(x,this.deckY()+heroBreath);
    this.hero.setDisplaySize(58*(2-heroSquash),130*heroSquash);
   }else{
    this.hero.setPosition(x+4,this.deckY()+heroBreath);
    this.hero.setDisplaySize(72*(2-heroSquash),72*heroSquash);
   }

   this.shadow.setPosition(x,y+5).setSize(armory?166:195,31);

   if(town){
    this.props[0].setPosition(72,487);this.props[1].setPosition(347,485);this.props[2].setPosition(210,301);this.props[3].setPosition(73,359);this.props[4].setPosition(351,355);
    if(Math.random()<0.18)this.puff(347+Phaser.Math.Between(-14,14),440,0xff7043,3);
    if(Math.random()<0.12)this.puff(73+Phaser.Math.Between(-10,10),320,0xffffff,3.5);
   }else if(home){
    // Match user screenshot exactly:
    // props[0] = cottage (sawmill) at left
    // props[1] = forge (behind sawmill)
    // props[2] = gate (castle gate directly behind tower)
    // props[3] = workshop (tucked left)
    // props[4] = mine (gold mine at right)
    this.props[0].setPosition(68,510);
    this.props[1].setPosition(360,540).setVisible(false);
    this.props[2].setPosition(210,380).setDisplaySize(160,147);
    this.props[3].setPosition(60,370).setVisible(false);
    this.props[4].setPosition(350,505);
   }else{
    this.props[0].setPosition(65,550);this.props[1].setPosition(355,540);this.props[2].setPosition(210,351);this.props[3].setPosition(62,365);this.props[4].setPosition(355,364);
   }

   this.dummy.forEach((d,i)=>{
    const spring=Math.sin(time*.005+i*1.8)*5;
    d.y=300+i*12+Math.abs(spring)*0.6;
    d.angle=spring;
    d.setScale(1+spring*0.015,1-spring*0.015);
    if(Math.random()<0.03)this.puff(d.x,d.y-18,0x8d6e63,2.2);
   });
  }"""
    lines[start_idx:end_idx] = [new_non_battle]
    scene = '\n'.join(lines)
    print("2. Replaced non-battle render block to match user reference image")

with open(scene_path, 'w', encoding='utf-8') as f:
    f.write(scene)

# 3. Update style.css:
css_path = r"Fortress-Rush-10-Levels\source\src\style.css"
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Brand and ribbon matching user reference:
css = re.sub(
    r'\.brand\{[^}]*\}',
    '.brand{position:absolute;width:52%;max-width:225px;top:4.2%;left:50%;transform:translateX(-50%);filter:drop-shadow(0 6px 4px #1b2612cc);pointer-events:none;z-index:2}',
    css
)
css = re.sub(
    r'\.home-ribbon\{[^}]*\}',
    '.home-ribbon{position:absolute;top:20.5%;width:100%;text-align:center;text-shadow:0 2px 3px #29371d;pointer-events:none;z-index:2}',
    css
)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("3. Updated style.css brand logo to top: 4.2% and ribbon to top: 20.5%")
