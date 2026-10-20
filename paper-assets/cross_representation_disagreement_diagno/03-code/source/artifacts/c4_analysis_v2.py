import json
from collections import Counter

data = json.load(open('/root/autodl-tmp/crdd/results/mvp_v4_full.json'))
N = len(data)
print(f"Total samples: {N}\n")

intervals = {"0-79": (0, 80), "80-108": (80, 109), "109-124": (109, N)}

def repair_success(repair, side, mode):
    key = f"{side}_{mode}"
    rounds = repair.get(key, [])
    if isinstance(rounds, list) and rounds:
        return (True, any(r.get('success') for r in rounds), len(rounds))
    return (False, False, 0)

def analyze(samples):
    n = len(samples)
    fol_c = sum(1 for s in samples if s.get('disagreement',{}).get('fol_correct'))
    code_c = sum(1 for s in samples if s.get('disagreement',{}).get('code_correct'))

    by_type = Counter(s.get('disagreement',{}).get('agreement_type','?') for s in samples)
    disagree_samples = [s for s in samples if s.get('disagreement',{}).get('agreement_type') == 'disagree']

    error_sides = Counter(s.get('disagreement',{}).get('error_side','?') for s in disagree_samples)

    t_s = t_t = b_s = b_t = 0
    for s in disagree_samples:
        es = s.get('disagreement',{}).get('error_side','')
        repair = s.get('repair', {})
        if not repair or not isinstance(repair, dict):
            continue
        for side in ['code', 'fol']:
            has_t, succ_t, _ = repair_success(repair, side, 'targeted')
            has_b, succ_b, _ = repair_success(repair, side, 'blind')
            if has_t:
                t_t += 1
                if succ_t: t_s += 1
            if has_b:
                b_t += 1
                if succ_b: b_s += 1

    t_r = t_s/t_t*100 if t_t else 0
    b_r = b_s/b_t*100 if b_t else 0

    return {
        'n': n, 'fol_acc': fol_c/n*100, 'code_acc': code_c/n*100,
        'by_type': by_type, 'disagree_n': len(disagree_samples),
        'error_sides': error_sides,
        'agree_wrong': by_type.get('agree_wrong', 0),
        't_s': t_s, 't_t': t_t, 't_r': t_r,
        'b_s': b_s, 'b_t': b_t, 'b_r': b_r,
        'delta': t_r - b_r,
    }

# =====================
# SECTION 1: Interval Slicing
# =====================
print("=" * 80)
print("SECTION 1: Interval Slicing - C4 Metrics")
print("=" * 80)

results = {}
for label, (start, end) in intervals.items():
    r = analyze(data[start:end])
    results[label] = r
    print(f"\n--- {label} (n={r['n']}) ---")
    print(f"  Targeted: {r['t_s']}/{r['t_t']} = {r['t_r']:.1f}%")
    print(f"  Blind:    {r['b_s']}/{r['b_t']} = {r['b_r']:.1f}%")
    print(f"  Delta:    {r['delta']:+.1f}pp")
    print(f"  DISAGREE: {r['disagree_n']} ({r['disagree_n']/r['n']*100:.1f}%)")

full = analyze(data)
print(f"\n--- FULL (n={full['n']}) ---")
print(f"  Targeted: {full['t_s']}/{full['t_t']} = {full['t_r']:.1f}%")
print(f"  Blind:    {full['b_s']}/{full['b_t']} = {full['b_r']:.1f}%")
print(f"  Delta:    {full['delta']:+.1f}pp")

# =====================
# SECTION 2: Difficulty
# =====================
print("\n" + "=" * 80)
print("SECTION 2: Difficulty & Error Distribution by Interval")
print("=" * 80)

for label, r in results.items():
    print(f"\n--- {label} (n={r['n']}) ---")
    print(f"  FOL accuracy:     {r['fol_acc']:.1f}%")
    print(f"  Code accuracy:    {r['code_acc']:.1f}%")
    print(f"  AGREE_WRONG:      {r['agree_wrong']} ({r['agree_wrong']/r['n']*100:.1f}%)")
    print(f"  DISAGREE rate:    {r['disagree_n']/r['n']*100:.1f}%")
    print(f"  Error sides:      {dict(r['error_sides'])}")
    print(f"  Type distribution: {dict(r['by_type'])}")

# =====================
# SECTION 3: FOL-side deep dive
# =====================
print("\n" + "=" * 80)
print("SECTION 3: FOL-side Repair Deep Dive")
print("=" * 80)

fol_err = [(i,s) for i,s in enumerate(data) if s.get('disagreement',{}).get('error_side')=='fol']
print(f"\nTotal FOL-error (error_side=fol) samples: {len(fol_err)}")

for i, s in fol_err:
    iv = "0-79" if i<80 else ("80-108" if i<109 else "109-124")
    repair = s.get('repair', {}) or {}
    d = s.get('disagreement', {})

    has_ft, succ_ft, n_ft = repair_success(repair, 'fol', 'targeted')
    has_fb, succ_fb, n_fb = repair_success(repair, 'fol', 'blind')

    ft_verdicts = [r.get('verdict','?') for r in repair.get('fol_targeted',[])] if isinstance(repair.get('fol_targeted'), list) else []
    fb_verdicts = [r.get('verdict','?') for r in repair.get('fol_blind',[])] if isinstance(repair.get('fol_blind'), list) else []

    print(f"\n  [{i}] {s['id']} (interval: {iv})")
    print(f"    FOL={d.get('fol_verdict')}, Code={d.get('code_verdict')}, GT={s.get('ground_truth')}")
    print(f"    Targeted: {'SUCCESS' if succ_ft else 'FAIL' if has_ft else 'N/A'} ({n_ft} rounds) verdicts={ft_verdicts}")
    print(f"    Blind:    {'SUCCESS' if succ_fb else 'FAIL' if has_fb else 'N/A'} ({n_fb} rounds) verdicts={fb_verdicts}")

# Side-specific breakdown by interval
print("\n\n--- Code-side targeted vs blind by interval ---")
for label, (start, end) in intervals.items():
    subs = [s for s in data[start:end] if s.get('disagreement',{}).get('error_side')=='code']
    ct_s=ct_t=cb_s=cb_t=0
    for s in subs:
        repair = s.get('repair',{}) or {}
        h,sc,_ = repair_success(repair,'code','targeted')
        if h: ct_t+=1; ct_s+=int(sc)
        h,sc,_ = repair_success(repair,'code','blind')
        if h: cb_t+=1; cb_s+=int(sc)
    ctr=ct_s/ct_t*100 if ct_t else 0; cbr=cb_s/cb_t*100 if cb_t else 0
    print(f"  {label}: targeted={ct_s}/{ct_t}={ctr:.1f}%, blind={cb_s}/{cb_t}={cbr:.1f}%, delta={ctr-cbr:+.1f}pp")

print("\n--- FOL-side targeted vs blind by interval ---")
for label, (start, end) in intervals.items():
    subs = [s for s in data[start:end] if s.get('disagreement',{}).get('error_side')=='fol']
    ft_s=ft_t=fb_s=fb_t=0
    for s in subs:
        repair = s.get('repair',{}) or {}
        h,sc,_ = repair_success(repair,'fol','targeted')
        if h: ft_t+=1; ft_s+=int(sc)
        h,sc,_ = repair_success(repair,'fol','blind')
        if h: fb_t+=1; fb_s+=int(sc)
    ftr=ft_s/ft_t*100 if ft_t else 0; fbr=fb_s/fb_t*100 if fb_t else 0
    print(f"  {label}: targeted={ft_s}/{ft_t}={ftr:.1f}%, blind={fb_s}/{fb_t}={fbr:.1f}%, delta={ftr-fbr:+.1f}pp")

# =====================
# SECTION 4: C4 cumulative progression
# =====================
print("\n" + "=" * 80)
print("SECTION 4: Cumulative C4 Delta Progression")
print("=" * 80)

for cp in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 109, 120, 126]:
    sub = data[:cp]
    dis = [s for s in sub if s.get('disagreement',{}).get('agreement_type')=='disagree']
    t_s=t_t=b_s=b_t=0
    for s in dis:
        repair = s.get('repair',{}) or {}
        for side in ['code','fol']:
            h,sc,_ = repair_success(repair,side,'targeted')
            if h: t_t+=1; t_s+=int(sc)
            h,sc,_ = repair_success(repair,side,'blind')
            if h: b_t+=1; b_s+=int(sc)
    tr=t_s/t_t*100 if t_t else 0; br=b_s/b_t*100 if b_t else 0
    print(f"  @{cp:>3d}: targeted={t_s}/{t_t}={tr:5.1f}%, blind={b_s}/{b_t}={br:5.1f}%, delta={tr-br:+.1f}pp, disagree={len(dis)}")

# =====================
# SECTION 5: Marginal 80-125
# =====================
print("\n" + "=" * 80)
print("SECTION 5: Marginal analysis for 80-125")
print("=" * 80)

recent = data[80:]
dis_recent = [s for s in recent if s.get('disagreement',{}).get('agreement_type')=='disagree']
t_s=t_t=b_s=b_t=0
for s in dis_recent:
    repair = s.get('repair',{}) or {}
    for side in ['code','fol']:
        h,sc,_ = repair_success(repair,side,'targeted')
        if h: t_t+=1; t_s+=int(sc)
        h,sc,_ = repair_success(repair,side,'blind')
        if h: b_t+=1; b_s+=int(sc)
tr=t_s/t_t*100 if t_t else 0; br=b_s/b_t*100 if b_t else 0
print(f"  n={len(recent)}, disagree={len(dis_recent)}")
print(f"  Marginal targeted: {t_s}/{t_t} = {tr:.1f}%")
print(f"  Marginal blind:    {b_s}/{b_t} = {br:.1f}%")
print(f"  Marginal delta:    {tr-br:+.1f}pp")
marg_tr = tr
marg_br = br

# =====================
# SECTION 6: 204 projection
# =====================
print("\n" + "=" * 80)
print("SECTION 6: 204-sample C4 Projection")
print("=" * 80)

# Full stats
fd = [s for s in data if s.get('disagreement',{}).get('agreement_type')=='disagree']
ts_f=tt_f=bs_f=bt_f=0
for s in fd:
    repair = s.get('repair',{}) or {}
    for side in ['code','fol']:
        h,sc,_ = repair_success(repair,side,'targeted')
        if h: tt_f+=1; ts_f+=int(sc)
        h,sc,_ = repair_success(repair,side,'blind')
        if h: bt_f+=1; bs_f+=int(sc)
ct = ts_f/tt_f*100 if tt_f else 0
cb = bs_f/bt_f*100 if bt_f else 0
print(f"Current {N}: targeted={ts_f}/{tt_f}={ct:.1f}%, blind={bs_f}/{bt_f}={cb:.1f}%, delta={ct-cb:+.1f}pp")

dis_rate_r = len(dis_recent)/len(recent)
remaining = 204 - N
est_dis = int(remaining * dis_rate_r)
print(f"\nDisagree rate recent: {dis_rate_r*100:.1f}%")
print(f"Remaining samples: {remaining}, est disagree: ~{est_dis}")

for sc_name, s_tr, s_br in [
    ("marginal trend continues", marg_tr, marg_br),
    ("remaining delta=0pp", 70, 70),
    ("targeted collapses", 50, 70),
    ("worst case", 40, 70),
]:
    p_ts = ts_f + est_dis * (s_tr/100)
    p_tt = tt_f + est_dis
    p_bs = bs_f + est_dis * (s_br/100)
    p_bt = bt_f + est_dis
    p_t = p_ts/p_tt*100 if p_tt else 0
    p_b = p_bs/p_bt*100 if p_bt else 0
    p_d = p_t - p_b
    risk = "FAIL (<5pp)" if p_d < 5 else "PASS"
    print(f"\n  {sc_name}: projected delta={p_d:+.1f}pp [{risk}]")

# =====================
# SECTION 7: Samples without repair
# =====================
print("\n" + "=" * 80)
print("SECTION 7: Disagree samples without repair data")
print("=" * 80)
for i, s in enumerate(data):
    if s.get('disagreement',{}).get('agreement_type') == 'disagree':
        repair = s.get('repair', {}) or {}
        has_any = any(repair.get(f"{side}_{mode}") for side in ['code','fol'] for mode in ['targeted','blind'])
        if not has_any:
            print(f"  [{i}] {s['id']} error_side={s.get('disagreement',{}).get('error_side')}")

print("\n\nDONE")
