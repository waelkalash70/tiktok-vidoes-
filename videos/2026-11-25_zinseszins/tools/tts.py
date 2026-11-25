# Satzweise Piper-TTS -> assets/voice.wav + assets/timing.json (Satzgrenzen)
import json, subprocess, sys, wave, os
root = sys.argv[1]; model = sys.argv[2]
sc = json.load(open(f"{root}/script.json"))
os.makedirs(f"{root}/build", exist_ok=True)
GAP = {"hook":0.3,"reicher":0.35,"frage":0.45,"anna":0.25,"annastop":0.45,"ben":0.25,"benpaid":0.45,"rendite":0.4,"twist":0.9,"benend":0.45,"annaend":0.5,"punch":0.5,"lehre":0.55,"cta":0.6}
LEAD = 0.15
parts=[]; t=LEAD; timing=[]
for s in sc["saetze"]:
    text=" ".join(tok[1] for tok in s["tokens"])
    f=f"{root}/build/{s['id']}.wav"
    subprocess.run([sys.executable,"-m","piper","-m",model,"-f",f,"--length-scale","0.86","--sentence-silence","0"],input=text.encode(),check=True,capture_output=True)
    with wave.open(f) as w: d=w.getnframes()/w.getframerate(); sr=w.getframerate()
    timing.append({"id":s["id"],"start":round(t,3),"end":round(t+d,3),"text":text})
    parts.append((f,t)); t+=d+GAP[s["beat"]]
total=t
# zusammenmischen
inputs=[]; filt=[]
for i,(f,st) in enumerate(parts):
    inputs+=["-i",f]; filt.append(f"[{i}]adelay={int(st*1000)}|{int(st*1000)}[a{i}]")
filt.append("".join(f"[a{i}]" for i in range(len(parts)))+f"amix=inputs={len(parts)}:normalize=0,apad=whole_dur={total}[o]")
subprocess.run(["ffmpeg","-v","error","-y",*inputs,"-filter_complex",";".join(filt),"-map","[o]","-ar","44100",f"{root}/assets/voice.wav"],check=True)
json.dump({"total":round(total,3),"saetze":timing},open(f"{root}/build/sentences.json","w"),ensure_ascii=False,indent=1)
print("total",round(total,2))
