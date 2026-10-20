import json

PY = "/root/miniconda3/bin/python"
data = json.load(open('/root/autodl-tmp/crdd/results/mvp_v4_full.json'))
N = len(data)
print(f"Total samples: {N}\n")

intervals = {
    "0-79": (0, 80),
    "80-108": (80, 109),
    "109-124": (109, 125),
}

def analyze_interval(samples, label):
    n = len(samples)
    fol_correct = sum(1 for s in samples if s.get('disagreement', {}).get('fol_correct', False))
    code_correct = sum(1 for s in samples if s.get('disagreement', {}).get('code_correct', False))

    disagree = [s for s in samples if s.get('disagreement', {}).get('agreement_type', '').startswith('DISAGREE')]
    agree_wrong = [s for s in samples if s.get('disagreement', {}).get('agreement_type', '') == 'AGREE_WRONG']

    error_sides = {}
    for s in disagree:
        es = s.get('disagreement', {}).get('error_side', 'unknown')
        error_sides[es] = error_sides.get(es, 0) + 1

    targeted_success = 0
    targeted_total = 0
    blind_success = 0
    blind_total = 0

    for s in disagree:
        es = s.get('disagreement', {}).get('error_side', '')
        repair = s.get('repair', {})
        if not repair:
            continue

        for side in ['code', 'fol']:
            t_key = f"{side}_targeted"
            b_key = f"{side}_blind"

            if repair.get(t_key):
                rounds = repair[t_key]
                if isinstance(rounds, list) and rounds:
                    targeted_total += 1
                    if any(r.get('success') for r in rounds):
                        targeted_success += 1

            if repair.get(b_key):
                rounds = repair[b_key]
                if isinstance(rounds, list) and rounds:
                    blind_total += 1
                    if any(r.get('success') for r in rounds):
                        blind_success += 1

    targeted_rate = targeted_success / targeted_total * 100 if targeted_total > 0 else 0
    blind_rate = blind_success / blind_total * 100 if blind_total > 0 else 0
    delta = targeted_rate - blind_rate

    return {
        'label': label, 'n': n,
        'fol_acc': fol_correct / n * 100 if n > 0 else 0,
        'code_acc': code_correct / n * 100 if n > 0 else 0,
        'disagree_n': len(disagree),
        'disagree_rate': len(disagree) / n * 100 if n > 0 else 0,
        'agree_wrong_n': len(agree_wrong),
        'agree_wrong_rate': len(agree_wrong) / n * 100 if n > 0 else 0,
        'error_sides': error_sides,
        'targeted_success': targeted_success, 'targeted_total': targeted_total, 'targeted_rate': targeted_rate,
        'blind_success': blind_success, 'blind_total': blind_total, 'blind_rate': blind_rate,
        'delta_pp': delta,
    }

# =====================
# SECTION 1
# =====================
print("=" * 80)
print("SECTION 1: Interval Slicing - C4 Metrics")
print("=" * 80)

results = {}
for label, (start, end) in intervals.items():
    samples = data[start:end]
    r = analyze_interval(samples, label)
    results[label] = r
    print(f"\n--- {label} (n={r['n']}) ---")
    print(f"  Targeted: {r['targeted_success']}/{r['targeted_total']} = {r['targeted_rate']:.1f}%")
    print(f"  Blind:    {r['blind_success']}/{r['blind_total']} = {r['blind_rate']:.1f}%")
    print(f"  Delta:    {r['delta_pp']:+.1f}pp")
    print(f"  DISAGREE: {r['disagree_n']} ({r['disagree_rate']:.1f}%)")

full = analyze_interval(data, "FULL 0-124")
print(f"\n--- FULL 0-124 (n={full['n']}) ---")
print(f"  Targeted: {full['targeted_success']}/{full['targeted_total']} = {full['targeted_rate']:.1f}%")
print(f"  Blind:    {full['blind_success']}/{full['blind_total']} = {full['blind_rate']:.1f}%")
print(f"  Delta:    {full['delta_pp']:+.1f}pp")

# =====================
# SECTION 2
# =====================
print("\n" + "=" * 80)
print("SECTION 2: Difficulty & Error Distribution by Interval")
print("=" * 80)

for label, r in results.items():
    print(f"\n--- {label} (n={r['n']}) ---")
    print(f"  FOL accuracy:     {r['fol_acc']:.1f}%")
    print(f"  Code accuracy:    {r['code_acc']:.1f}%")
    print(f"  AGREE_WRONG:      {r['agree_wrong_n']} ({r['agree_wrong_rate']:.1f}%)")
    print(f"  DISAGREE rate:    {r['disagree_rate']:.1f}%")
    print(f"  Error sides:      {r['error_sides']}")

# =====================
# SECTION 3: FOL-side repair deep dive
# =====================
print("\n" + "=" * 80)
print("SECTION 3: FOL-side Repair Deep Dive")
print("=" * 80)

fol_error_samples = []
for i, s in enumerate(data):
    if s.get('disagreement', {}).get('error_side') == 'fol':
        fol_error_samples.append((i, s))

print(f"\nTotal FOL-error samples: {len(fol_error_samples)}")
for idx, (i, s) in enumerate(fol_error_samples):
    interval = "0-79" if i < 80 else ("80-108" if i < 109 else "109-124")
    repair = s.get('repair', {})

    fol_t = repair.get('fol_targeted', [])
    if isinstance(fol_t, list):
        t_success = any(r.get('success') for r in fol_t)
        t_rounds = len(fol_t)
        t_verdicts = [r.get('verdict', '?') for r in fol_t]
    else:
        t_success = None; t_rounds = 0; t_verdicts = []

    fol_b = repair.get('fol_blind', [])
    if isinstance(fol_b, list):
        b_success = any(r.get('success') for r in fol_b)
        b_rounds = len(fol_b)
        b_verdicts = [r.get('verdict', '?') for r in fol_b]
    else:
        b_success = None; b_rounds = 0; b_verdicts = []

    print(f"\n  [{i}] {s['id']} (interval: {interval})")
    print(f"    FOL verdict: {s.get('disagreement',{}).get('fol_verdict')}, Code verdict: {s.get('disagreement',{}).get('code_verdict')}")
    print(f"    Ground truth: {s.get('ground_truth')}")
    print(f"    Targeted: {'SUCCESS' if t_success else 'FAIL'} ({t_rounds} rounds) verdicts={t_verdicts}")
    print(f"    Blind:    {'SUCCESS' if b_success else 'FAIL'} ({b_rounds} rounds) verdicts={b_verdicts}")

# Code-side by interval
print("\n\n--- Code-side targeted vs blind by interval ---")
for label, (start, end) in intervals.items():
    samples = data[start:end]
    code_err = [s for s in samples if s.get('disagreement', {}).get('error_side') == 'code']
    ct_s = ct_t = cb_s = cb_t = 0
    for s in code_err:
        repair = s.get('repair', {})
        if not repair: continue
        ct = repair.get('code_targeted', [])
        if isinstance(ct, list) and ct:
            ct_t += 1
            if any(r.get('success') for r in ct): ct_s += 1
        cb = repair.get('code_blind', [])
        if isinstance(cb, list) and cb:
            cb_t += 1
            if any(r.get('success') for r in cb): cb_s += 1
    ct_r = ct_s/ct_t*100 if ct_t > 0 else 0
    cb_r = cb_s/cb_t*100 if cb_t > 0 else 0
    print(f"  {label}: code_targeted {ct_s}/{ct_t}={ct_r:.1f}%, code_blind {cb_s}/{cb_t}={cb_r:.1f}%, delta={ct_r-cb_r:+.1f}pp")

# FOL-side by interval
print("\n--- FOL-side targeted vs blind by interval ---")
for label, (start, end) in intervals.items():
    samples = data[start:end]
    fol_err = [s for s in samples if s.get('disagreement', {}).get('error_side') == 'fol']
    ft_s = ft_t = fb_s = fb_t = 0
    for s in fol_err:
        repair = s.get('repair', {})
        if not repair: continue
        ft = repair.get('fol_targeted', [])
        if isinstance(ft, list) and ft:
            ft_t += 1
            if any(r.get('success') for r in ft): ft_s += 1
        fb = repair.get('fol_blind', [])
        if isinstance(fb, list) and fb:
            fb_t += 1
            if any(r.get('success') for r in fb): fb_s += 1
    ft_r = ft_s/ft_t*100 if ft_t > 0 else 0
    fb_r = fb_s/fb_t*100 if fb_t > 0 else 0
    print(f"  {label}: fol_targeted {ft_s}/{ft_t}={ft_r:.1f}%, fol_blind {fb_s}/{fb_t}={fb_r:.1f}%, delta={ft_r-fb_r:+.1f}pp")

# =====================
# SECTION 4: Both-wrong
# =====================
print("\n" + "=" * 80)
print("SECTION 4: both-wrong analysis")
print("=" * 80)
for label, (start, end) in intervals.items():
    samples = data[start:end]
    both_wrong = [s for s in samples if s.get('disagreement', {}).get('error_side') == 'both']
    disagree = [s for s in samples if s.get('disagreement', {}).get('agreement_type', '').startswith('DISAGREE')]
    print(f"  {label}: both-wrong={len(both_wrong)}, disagree={len(disagree)}")

# =====================
# SECTION 5: Cumulative progression
# =====================
print("\n" + "=" * 80)
print("SECTION 5: Cumulative C4 Delta Progression")
print("=" * 80)

for cp in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 109, 120, 125]:
    subset = data[:cp]
    dis = [s for s in subset if s.get('disagreement', {}).get('agreement_type', '').startswith('DISAGREE')]
    t_s = t_t = b_s = b_t = 0
    for s in dis:
        es = s.get('disagreement', {}).get('error_side', '')
        repair = s.get('repair', {})
        if not repair: continue
        for side in ['code', 'fol']:
            tk = f"{side}_targeted"
            bk = f"{side}_blind"
            tr = repair.get(tk, [])
            br = repair.get(bk, [])
            if isinstance(tr, list) and tr:
                t_t += 1
                if any(r.get('success') for r in tr): t_s += 1
            if isinstance(br, list) and br:
                b_t += 1
                if any(r.get('success') for r in br): b_s += 1
    t_rate = t_s/t_t*100 if t_t > 0 else 0
    b_rate = b_s/b_t*100 if b_t > 0 else 0
    print(f"  @{cp:>3d}: targeted={t_s}/{t_t}={t_rate:5.1f}%, blind={b_s}/{b_t}={b_rate:5.1f}%, delta={t_rate-b_rate:+.1f}pp")

# =====================
# SECTION 6: Marginal 80-124
# =====================
print("\n" + "=" * 80)
print("SECTION 6: Marginal (incremental) analysis for 80-124")
print("=" * 80)

recent = data[80:125]
dis_recent = [s for s in recent if s.get('disagreement', {}).get('agreement_type', '').startswith('DISAGREE')]
print(f"Samples 80-124: n={len(recent)}, disagree={len(dis_recent)}")

t_s = t_t = b_s = b_t = 0
for s in dis_recent:
    repair = s.get('repair', {})
    if not repair: continue
    for side in ['code', 'fol']:
        tk = f"{side}_targeted"
        bk = f"{side}_blind"
        tr = repair.get(tk, [])
        br = repair.get(bk, [])
        if isinstance(tr, list) and tr:
            t_t += 1
            if any(r.get('success') for r in tr): t_s += 1
        if isinstance(br, list) and br:
            b_t += 1
            if any(r.get('success') for r in br): b_s += 1
t_rate = t_s/t_t*100 if t_t > 0 else 0
b_rate = b_s/b_t*100 if b_t > 0 else 0
print(f"  Marginal targeted: {t_s}/{t_t} = {t_rate:.1f}%")
print(f"  Marginal blind:    {b_s}/{b_t} = {b_rate:.1f}%")
print(f"  Marginal delta:    {t_rate - b_rate:+.1f}pp")

# =====================
# SECTION 7: 204 projection
# =====================
print("\n" + "=" * 80)
print("SECTION 7: 204-sample C4 Projection")
print("=" * 80)

full_dis = [s for s in data if s.get('disagreement', {}).get('agreement_type', '').startswith('DISAGREE')]
ts_f = tt_f = bs_f = bt_f = 0
for s in full_dis:
    repair = s.get('repair', {})
    if not repair: continue
    for side in ['code', 'fol']:
        tr = repair.get(f"{side}_targeted", [])
        br = repair.get(f"{side}_blind", [])
        if isinstance(tr, list) and tr:
            tt_f += 1
            if any(r.get('success') for r in tr): ts_f += 1
        if isinstance(br, list) and br:
            bt_f += 1
            if any(r.get('success') for r in br): bs_f += 1

curr_t = ts_f/tt_f*100 if tt_f > 0 else 0
curr_b = bs_f/bt_f*100 if bt_f > 0 else 0
print(f"Current 125: targeted={ts_f}/{tt_f}={curr_t:.1f}%, blind={bs_f}/{bt_f}={curr_b:.1f}%, delta={curr_t-curr_b:+.1f}pp")

dis_rate_recent = len(dis_recent) / len(recent) if recent else 0
remaining = 79
est_dis = int(remaining * dis_rate_recent)
print(f"\nDisagree rate in 80-124: {dis_rate_recent*100:.1f}%")
print(f"Estimated disagree in remaining 79: ~{est_dis}")

marg_t = t_rate
marg_b = b_rate

if t_t > 0 and b_t > 0:
    for scenario, s_t_rate, s_b_rate, desc in [
        (1, marg_t, marg_b, "marginal trend continues"),
        (2, 50.0, 50.0, "remaining delta = 0pp"),
        (3, 40.0, 60.0, "remaining targeted < blind"),
    ]:
        p_ts = ts_f + est_dis * (s_t_rate / 100)
        p_tt = tt_f + est_dis
        p_bs = bs_f + est_dis * (s_b_rate / 100)
        p_bt = bt_f + est_dis
        p_t = p_ts / p_tt * 100
        p_b = p_bs / p_bt * 100
        p_d = p_t - p_b
        risk = "HIGH - below 5pp!" if p_d < 5 else "PASS"
        print(f"\nScenario {scenario} ({desc}):")
        print(f"  Projected delta: {p_d:+.1f}pp  [{risk}]")

# =====================
# SECTION 8: Disagree samples without repair data
# =====================
print("\n" + "=" * 80)
print("SECTION 8: Disagree samples missing repair")
print("=" * 80)
for i, s in enumerate(data):
    agr = s.get('disagreement', {}).get('agreement_type', '')
    if agr.startswith('DISAGREE'):
        repair = s.get('repair', {})
        es = s.get('disagreement', {}).get('error_side', '')
        has_targeted = any(repair.get(f"{side}_targeted") for side in ['code', 'fol'])
        has_blind = any(repair.get(f"{side}_blind") for side in ['code', 'fol'])
        if not has_targeted and not has_blind:
            print(f"  [{i}] {s['id']} error_side={es} - NO REPAIR DATA")

print("\n\nDONE")
