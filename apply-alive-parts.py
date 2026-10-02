import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

scene_path = r"d:\New folder (55)\Fortress-Rush-10-Levels\source\src\scene.ts"
with open(scene_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    # Check for town dummy rendering line
    if "this.dummy.forEach((d,i)=>{d.y=300+i*12+Math.sin(time*.003+i)*2;d.angle=Math.sin(time*.004+i)*4;});}" in line:
        town_replacement = """    if(town){
     if(Math.random()<0.18)this.puff(347+Phaser.Math.Between(-14,14),440,0xff7043,3);
     if(Math.random()<0.12)this.puff(73+Phaser.Math.Between(-10,10),320,0xffffff,3.5);
    }
    this.dummy.forEach((d,i)=>{
     const spring=Math.sin(time*.005+i*1.8)*5;
     d.y=300+i*12+Math.abs(spring)*0.6;
     d.angle=spring;
     d.setScale(1+spring*0.015,1-spring*0.015);
     if(Math.random()<0.03)this.puff(d.x,d.y-18,0x8d6e63,2.2);
    });}
"""
        new_lines.append(line.replace("this.dummy.forEach((d,i)=>{d.y=300+i*12+Math.sin(time*.003+i)*2;d.angle=Math.sin(time*.004+i)*4;});}", town_replacement))
        print("Updated town atmospheric particles & dummy spring physics")
    # Check for kill corpse tween
    elif "this.tweens.add({targets:corpse,y:e.y!-35,x:e.x!+Phaser.Math.Between(-25,25),angle:Phaser.Math.Between(-180,180),scaleX:.2,scaleY:.2,alpha:0,duration:450,onComplete:()=>corpse.destroy()});" in line:
        kill_replacement = """     this.tweens.add({targets:corpse,y:e.y!-45,x:e.x!+Phaser.Math.Between(-35,35),angle:Phaser.Math.Between(-240,240),scaleX:.15,scaleY:.15,alpha:0,duration:520,ease:'Cubic.easeOut',onComplete:()=>corpse.destroy()});
     const soul=this.add.circle(e.x!,e.y!-15,7,0x80deea,0.85).setDepth(725);
     this.tweens.add({targets:soul,y:e.y!-95,x:e.x!+Phaser.Math.Between(-25,25),alpha:0,scale:0.3,duration:700,ease:'Quad.easeOut',onComplete:()=>soul.destroy()});
     for(let i=0;i<3;i++)this.puff(e.x!,e.y!-20,0xffffff,2.5);
"""
        new_lines.append(kill_replacement)
        print("Updated kill effect with ascending soul wisps")
    else:
        new_lines.append(line)

with open(scene_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Done patching scene.ts!")
