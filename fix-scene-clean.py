import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

scene_path = r"d:\New folder (55)\Fortress-Rush-10-Levels\source\src\scene.ts"
with open(scene_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect lines 110 to 127
old_block = """  if(!battle){const town=this.view==='town',armory=this.view==='armory';const x=210,y=town?429:armory?490:558;this.tower.setPosition(x,y+14+Math.sin(time*.0018)*2);this.size(this.tower,town?160:208);const heroBreath=Math.sin(time*.0035)*1.8;
    const heroSquash=1+Math.sin(time*.0035)*.025;
    this.hero.setPosition(x+4,(armory?488:this.deckY())+heroBreath);
    if(armory)this.hero.setDisplaySize(185*(2-heroSquash),185*heroSquash);
     const isHome=this.view==='home';const heroSize=armory?185:isHome?118:76;this.hero.setDisplaySize(heroSize*(2-heroSquash),heroSize*heroSquash);
      if(Math.random()<0.18)this.puff(347+Phaser.Math.Between(-14,14),440,0xff7043,3);
      if(Math.random()<0.12)this.puff(73+Phaser.Math.Between(-10,10),320,0xffffff,3.5);
     }
     this.dummy.forEach((d,i)=>{
      const spring=Math.sin(time*.005+i*1.8)*5;
      d.y=300+i*12+Math.abs(spring)*0.6;
      d.angle=spring;
      d.setScale(1+spring*0.015,1-spring*0.015);
      if(Math.random()<0.03)this.puff(d.x,d.y-18,0x8d6e63,2.2);
     });}"""

new_block = """  if(!battle){
   const town=this.view==='town',armory=this.view==='armory',home=this.view==='home';
   const x=210,y=town?429:armory?490:558;
   this.tower.setPosition(x,y+14+Math.sin(time*.0018)*2);
   this.size(this.tower,town?160:208);
   const heroBreath=Math.sin(time*.0035)*1.8;
   const heroSquash=1+Math.sin(time*.0035)*.025;
   this.hero.setPosition(x+4,(armory?488:this.deckY())+heroBreath);
   const heroSize=armory?185:home?118:76;
   this.hero.setDisplaySize(heroSize*(2-heroSquash),heroSize*heroSquash);
   this.shadow.setPosition(x,y+5).setSize(armory?166:195,31);
   if(town){
    this.props[0].setPosition(72,487);this.props[1].setPosition(347,485);this.props[2].setPosition(210,301);this.props[3].setPosition(73,359);this.props[4].setPosition(351,355);
    if(Math.random()<0.18)this.puff(347+Phaser.Math.Between(-14,14),440,0xff7043,3);
    if(Math.random()<0.12)this.puff(73+Phaser.Math.Between(-10,10),320,0xffffff,3.5);
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

if old_block in content:
    content = content.replace(old_block, new_block, 1)
    print("Cleaned non-battle block with proper props, shadow, town VFX and 118px hero size")
else:
    print("Warning: old_block not matched directly, using line search...")
    # let's locate lines 111-125
    lines = content.split('\n')
    start_idx = None
    end_idx = None
    for idx, l in enumerate(lines):
        if "if(!battle){const town=this.view==='town'" in l:
            start_idx = idx
        if start_idx is not None and "else {" in l and idx > start_idx:
            end_idx = idx
            break
    if start_idx is not None and end_idx is not None:
        print(f"Replacing lines {start_idx+1} to {end_idx}")
        lines[start_idx:end_idx] = [new_block]
        content = '\n'.join(lines)
        print("Replaced successfully via line indices!")

with open(scene_path, 'w', encoding='utf-8') as f:
    f.write(content)
