import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

scene_path = r"d:\New folder (55)\Fortress-Rush-10-Levels\source\src\scene.ts"
with open(scene_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update stop coordinate in scene.ts to match simulation.ts exactly!
# Old: const stop=e.kind==='chief'?330:e.kind==='archer'?310:e.kind==='shaman'?365:e.kind==='drakerider'?340:610;
# New: const stop=e.kind==='archer'?470:e.kind==='shaman'?490:e.kind==='drakerider'?510:e.kind==='chief'?550:635;
old_stop = "const stop=e.kind==='chief'?330:e.kind==='archer'?310:e.kind==='shaman'?365:e.kind==='drakerider'?340:610;"
new_stop = "const stop=e.kind==='archer'?470:e.kind==='shaman'?490:e.kind==='drakerider'?510:e.kind==='chief'?550:635;"

if old_stop in code:
    code = code.replace(old_stop, new_stop, 1)
    print("1. Fixed enemy stop distance synchronization")
else:
    print("1. SKIP: stop distance not found or already modified")

# 2. Enhanced Gait, Drakerider swooping, Shaman levitation, Bomber pulsing fuse
old_gait_block = """   if(isFlying){
    const flap=Math.sin(e.age*7.5);
    offsetY=flap*7-10;
    scaleX=1+flap*.07;
    scaleY=1-flap*.07;
    angle=Math.sin(e.age*3.5)*4;
   }else if(e.y<stop){
    offsetY=-Math.abs(step)*(isBoss?2.5:4.5);
    scaleX=1-Math.abs(step)*.09;
    scaleY=1+Math.abs(step)*.12;
    angle=step*(isFast?8.5:4.5);
   }else{
    const breath=Math.sin(e.age*4.5);
    scaleX=1-breath*.04;
    scaleY=1+breath*.05;
    angle=Math.sin(e.age*2)*2;
   }

   // Attack wind-up & lunge
   if(e.attack<.28&&e.y>=stop-10){
    const lunge=(.28-e.attack)/.28;
    if(lunge<.35){
     offsetY-=lunge*10;scaleY*=1.1;
    }else{
     offsetY+=(lunge-.35)*22;scaleY*=.85;scaleX*=1.15;
    }
   }"""

new_gait_block = """   if(isFlying){
    const flap=Math.sin(e.age*8.5);
    const dive=e.attack<0.4?Math.sin((0.4-e.attack)*12)*8:0;
    offsetY=flap*8-12+dive;
    scaleX=1+flap*.09;
    scaleY=1-flap*.09;
    angle=Math.sin(e.age*3.8)*5;
    // Wyvern fire breath wind-up: head tilts back, then surges
    if(e.attack<0.35){
     scaleY*=1.15;scaleX*=0.92;
     if(Math.random()<0.35)this.puff(e.x+Phaser.Math.Between(-10,10),e.y-baseHeight*0.45,0xff5722,3.5);
    }
   }else if(e.y<stop){
    offsetY=-Math.abs(step)*(isBoss?2.8:5.2);
    scaleX=1-Math.abs(step)*.11;
    scaleY=1+Math.abs(step)*.14;
    angle=step*(isFast?9.5:5.0);
    // Bomber bomb pulsing heartbeat
    if(e.kind==='bomber'){
     const pulse=1+Math.sin(time*0.025)*0.1;
     scaleX*=pulse;scaleY*=pulse;
    }
   }else{
    const breath=Math.sin(e.age*4.5);
    scaleX=1-breath*.05;
    scaleY=1+breath*.06;
    angle=Math.sin(e.age*2)*2.5;
    // Shaman chanting levitation
    if(e.kind==='shaman'&&e.attack<0.6){
     offsetY-=Math.sin((0.6-e.attack)*8)*14;
     scaleY*=1.18;scaleX*=0.92;
     if(Math.random()<0.3)this.puff(e.x+Phaser.Math.Between(-16,16),e.y-baseHeight*0.6,0xba68c8,3);
    }
   }

   // Attack wind-up & lunge
   if(e.attack<.32&&e.y>=stop-15){
    const lunge=(.32-e.attack)/.32;
    if(lunge<.4){
     offsetY-=lunge*14;scaleY*=1.18;scaleX*=.92;
    }else{
     offsetY+=(lunge-.4)*28;scaleY*=.80;scaleX*=1.22;
    }
   }"""

if old_gait_block in code:
    code = code.replace(old_gait_block, new_gait_block, 1)
    print("2. Enhanced organic gait cycles, wyvern dive, shaman chant, and bomber heartbeat")
else:
    print("2. SKIP: gait block replacement not matched")

# 3. Enhanced Death Animation: Soul wisp rising + enemy flinch
old_kill = """   case'kill':{
    const kDef=ENEMIES[e.kind as EnemyKind];
    for(let i=0;i<6;i++)this.puff(e.x!,e.y!-10,kDef?kDef.color:0xffaa00,5);
    if(e.kind){
     const corpse=this.add.image(e.x!,e.y!,e.kind).setDisplaySize(38,42).setOrigin(.5,.5).setDepth(720).setTint(0x555555);
     this.tweens.add({targets:corpse,y:e.y!-35,x:e.x!+Phaser.Math.Between(-25,25),angle:Phaser.Math.Between(-180,180),scaleX:.2,scaleY:.2,alpha:0,duration:450,onComplete:()=>corpse.destroy()});
    }
    break;
   }"""

new_kill = """   case'kill':{
    const kDef=ENEMIES[e.kind as EnemyKind];
    const col=kDef?kDef.color:0xffaa00;
    for(let i=0;i<8;i++)this.puff(e.x!+Phaser.Math.Between(-12,12),e.y!-10+Phaser.Math.Between(-8,8),col,5.5);
    if(e.kind){
     const corpse=this.add.image(e.x!,e.y!,e.kind).setDisplaySize(42,46).setOrigin(.5,.5).setDepth(720).setTint(0x444444);
     this.tweens.add({targets:corpse,y:e.y!-45,x:e.x!+Phaser.Math.Between(-35,35),angle:Phaser.Math.Between(-240,240),scaleX:.15,scaleY:.15,alpha:0,duration:520,ease:'Cubic.easeOut',onComplete:()=>corpse.destroy()});
     // Ascending soul spirit wisp
     const soul=this.add.circle(e.x!,e.y!-15,7,0x80deea,0.85).setDepth(725);
     this.tweens.add({targets:soul,y:e.y!-95,x:e.x!+Phaser.Math.Between(-25,25),alpha:0,scale:0.3,duration:700,ease:'Quad.easeOut',onComplete:()=>soul.destroy()});
     for(let i=0;i<3;i++)this.puff(e.x!,e.y!-20,0xffffff,2.5);
    }
    break;
   }"""

if old_kill in code:
    code = code.replace(old_kill, new_kill, 1)
    print("3. Enhanced death animations with rising soul wisps and ragdoll spin")
else:
    print("3. SKIP: kill block replacement not matched")

# 4. Town & Home View living effects (forge smoke/sparks, workshop steam, dummy spring bounce)
old_town_render = """   if(!battle){const town=this.view==='town',armory=this.view==='armory';const x=210,y=town?429:armory?490:558;this.tower.setPosition(x,y+14+Math.sin(time*.0018)*2);this.size(this.tower,town?160:208);const heroBreath=Math.sin(time*.0035)*1.8;
    const heroSquash=1+Math.sin(time*.0035)*.025;
    this.hero.setPosition(x+4,(armory?488:this.deckY())+heroBreath);
    if(armory)this.hero.setDisplaySize(185*(2-heroSquash),185*heroSquash);
    else this.hero.setDisplaySize(68*(2-heroSquash),68*heroSquash);this.shadow.setPosition(x,y+5).setSize(armory?166:195,31);if(town){this.props[0].setPosition(72,487);this.props[1].setPosition(347,485);this.props[2].setPosition(210,301);this.props[3].setPosition(73,359);this.props[4].setPosition(351,355);}else{this.props[0].setPosition(65,550);this.props[1].setPosition(355,540);this.props[2].setPosition(210,351);this.props[3].setPosition(62,365);this.props[4].setPosition(355,364);}this.dummy.forEach((d,i)=>{d.y=300+i*12+Math.sin(time*.003+i)*2;d.angle=Math.sin(time*.004+i)*4;});}"""

new_town_render = """   if(!battle){const town=this.view==='town',armory=this.view==='armory';const x=210,y=town?429:armory?490:558;this.tower.setPosition(x,y+14+Math.sin(time*.0018)*2);this.size(this.tower,town?160:208);const heroBreath=Math.sin(time*.0035)*1.8;
    const heroSquash=1+Math.sin(time*.0035)*.025;
    this.hero.setPosition(x+4,(armory?488:this.deckY())+heroBreath);
    if(armory)this.hero.setDisplaySize(185*(2-heroSquash),185*heroSquash);
    else this.hero.setDisplaySize(68*(2-heroSquash),68*heroSquash);this.shadow.setPosition(x,y+5).setSize(armory?166:195,31);if(town){this.props[0].setPosition(72,487);this.props[1].setPosition(347,485);this.props[2].setPosition(210,301);this.props[3].setPosition(73,359);this.props[4].setPosition(351,355);
     // Town living atmosphere: forge sparks & workshop steam
     if(Math.random()<0.18)this.puff(347+Phaser.Math.Between(-14,14),440,0xff7043,3);
     if(Math.random()<0.12)this.puff(73+Phaser.Math.Between(-10,10),320,0xffffff,3.5);
    }else{this.props[0].setPosition(65,550);this.props[1].setPosition(355,540);this.props[2].setPosition(210,351);this.props[3].setPosition(62,365);this.props[4].setPosition(355,364);}
    // Living Target Dummies with spring wobble & squash
    this.dummy.forEach((d,i)=>{
     const spring=Math.sin(time*.005+i*1.8)*5;
     d.y=300+i*12+Math.abs(spring)*0.6;
     d.angle=spring;
     d.setScale(1+spring*0.015,1-spring*0.015);
     if(Math.random()<0.03)this.puff(d.x,d.y-18,0x8d6e63,2.2);
    });}"""

if old_town_render in code:
    code = code.replace(old_town_render, new_town_render, 1)
    print("4. Added Town living smoke/sparks and spring-wobbling target dummies")
else:
    print("4. SKIP: town render replacement not matched")

with open(scene_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("\n=== scene.ts living updates completed ===")
