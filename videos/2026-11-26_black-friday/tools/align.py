# Token-Timings: Whisper-Wörter je Satz auf Skript-Tokens abbilden (Fallback: proportional nach Zeichen)
import json, sys, re
root=sys.argv[1]
sc=json.load(open(f"{root}/script.json")); se={s["id"]:s for s in json.load(open(f"{root}/build/sentences.json"))["saetze"]}
tr=json.load(open(f"{root}/assets/transcript.json")); words=tr["words"] if isinstance(tr,dict) else tr
out=[]; report=[]
for s in sc["saetze"]:
    st,en=se[s["id"]]["start"],se[s["id"]]["end"]
    ws=[w for w in words if st-0.15<=w["start"]<en+0.05]
    toks=s["tokens"]; counts=[len(t[1].split()) for t in toks]
    if ws and len(ws)==sum(counts):
        i=0; mode="whisper"
        for t,c in zip(toks,counts):
            out.append({"s":s["id"],"text":t[0],"color":t[2] if len(t)>2 else "","start":ws[i]["start"],"end":ws[i+c-1]["end"]}); i+=c
    else:
        mode=f"proportional ({len(ws)} vs {sum(counts)})"
        a=ws[0]["start"] if ws else st; b=ws[-1]["end"] if ws else en
        L=[len(re.sub(r'\W','',t[1]))+2 for t in toks]; tot=sum(L); x=a
        for t,l in zip(toks,L):
            d=(b-a)*l/tot; out.append({"s":s["id"],"text":t[0],"color":t[2] if len(t)>2 else "","start":round(x,3),"end":round(x+d,3)}); x+=d
    report.append(f"{s['id']}: {mode}")
# Lücken schließen: jedes Wort bleibt bis zum nächsten stehen (max +0.6s)
for i,o in enumerate(out):
    nxt=out[i+1]["start"] if i+1<len(out) else o["end"]+1.2
    o["end"]=round(min(nxt, o["end"]+0.6) if i+1<len(out) else nxt,3); o["start"]=round(o["start"],3)
json.dump(out,open(f"{root}/build/captions.json","w"),ensure_ascii=False,indent=0)
print("\n".join(report)); print(len(out),"tokens")
