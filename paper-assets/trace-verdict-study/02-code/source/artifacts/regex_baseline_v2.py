import json, re
from collections import Counter, defaultdict

# Load test data
test_data = []
with open('/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl') as f:
    for i, line in enumerate(f):
        item = json.loads(line.strip())
        item['idx'] = i
        test_data.append(item)

# Load SFT predictions (exception_only seed42)
sft_preds = []
with open('/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/predictions.jsonl') as f:
    for line in f:
        sft_preds.append(json.loads(line.strip()))

# Multi-seed predictions
seed_files = {
    'seed42': '/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/predictions.jsonl',
    'seed123': '/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed123/final/predictions.jsonl',
    'seed456': '/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed456/final/predictions.jsonl',
}
all_seed_preds = {}
for sn, sp in seed_files.items():
    try:
        pp = []
        with open(sp) as f:
            for line in f:
                pp.append(json.loads(line.strip()))
        all_seed_preds[sn] = pp
    except Exception:
        pass

print('=== DATA OVERVIEW ===')
print(f'Total test samples: {len(test_data)}')
labels = [d['output'] for d in test_data]
print(f'Pass: {labels.count("pass")}, Fail: {labels.count("fail")}')

# Categorize each sample by trace content
categories = []
for d in test_data:
    inp = d['input']
    ts = inp.find('Execution trace:\n')
    if ts == -1:
        trace_text = ''
    else:
        trace_text = inp[ts + len('Execution trace:\n'):]
        # Remove the trailing prompt
        suffix = '\n\nDoes this code pass all tests? Answer: '
        if trace_text.endswith(suffix):
            trace_text = trace_text[:-len(suffix)]

    cat = {
        'idx': d['idx'],
        'label': d['output'],
        'trace_text': trace_text.strip(),
        'has_no_exception': '[No exception data in trace]' in trace_text,
        'has_no_trace': '[No trace available]' in trace_text,
        'has_error_tag': '[ERROR]' in trace_text,
        'has_error_word': bool(re.search(r'(Error|Exception|Traceback)', trace_text)),
        'sft_pred': sft_preds[d['idx']]['pred'] if d['idx'] < len(sft_preds) else '?',
    }
    categories.append(cat)

# Cross-tab: trace pattern vs label
print('\n=== TRACE CONTENT ANALYSIS ===')
print('Trace pattern distribution:')
pattern_label = defaultdict(lambda: Counter())
for c in categories:
    if c['has_no_exception']:
        pat = 'NO_EXCEPTION_MARKER'
    elif c['has_no_trace']:
        pat = 'NO_TRACE_AVAILABLE'
    elif c['has_error_tag']:
        pat = 'HAS_ERROR_TAG'
    else:
        pat = 'OTHER'
    pattern_label[pat][c['label']] += 1
    c['pattern'] = pat

for pat in ['NO_EXCEPTION_MARKER', 'NO_TRACE_AVAILABLE', 'HAS_ERROR_TAG', 'OTHER']:
    counts = pattern_label[pat]
    total = sum(counts.values())
    print(f'  {pat}: total={total}, pass={counts["pass"]}, fail={counts["fail"]}')

# === REGEX BASELINES ===
def b_marker(trace_text):
    if '[No exception data in trace]' in trace_text:
        return 'pass'
    return 'fail'

def b_error_tag(trace_text):
    if '[ERROR]' in trace_text:
        return 'fail'
    return 'pass'

def b_optimal(trace_text):
    if '[No exception data in trace]' in trace_text:
        return 'pass'
    if '[ERROR]' in trace_text or '[No trace available]' in trace_text:
        return 'fail'
    return 'fail'

def b_reviewer(trace_text):
    if re.search(r'(Error|Exception|Traceback|\[ERROR\])', trace_text):
        return 'fail'
    if '[No trace available]' in trace_text:
        return 'fail'
    return 'pass'

def evaluate(name, pred_fn, categories):
    preds = [pred_fn(c['trace_text']) for c in categories]
    labs = [c['label'] for c in categories]

    correct = sum(p == l for p, l in zip(preds, labs))
    acc = correct / len(labs)

    print(f'\n--- {name} ---')
    print(f'Accuracy: {correct}/{len(labs)} = {acc:.4f} ({acc*100:.2f}%)')

    for cls in ['pass', 'fail']:
        tp = sum(p == cls and l == cls for p, l in zip(preds, labs))
        fp = sum(p == cls and l != cls for p, l in zip(preds, labs))
        fn = sum(p != cls and l == cls for p, l in zip(preds, labs))
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
        print(f'  {cls}: P={prec:.4f} R={rec:.4f} F1={f1:.4f} (TP={tp} FP={fp} FN={fn})')

    errors = [(c, p) for c, p in zip(categories, preds) if p != c['label']]
    if errors:
        print(f'  Errors ({len(errors)}):')
        for c, p in errors[:25]:
            sc = 'SFT_OK' if c['sft_pred'] == c['label'] else 'SFT_ERR'
            tp = c['trace_text'][:100].replace('\n', ' ')
            print(f'    idx={c["idx"]} label={c["label"]} pred={p} pat={c["pattern"]} {sc} | {tp}')
        if len(errors) > 25:
            print(f'    ... and {len(errors)-25} more')

    return preds

print('\n=== REGEX BASELINES ===')
regex_results = {}
for name, fn in [('B_marker', b_marker), ('B_error_tag', b_error_tag),
                  ('B_optimal', b_optimal), ('B_reviewer', b_reviewer)]:
    preds = evaluate(name, fn, categories)
    regex_results[name] = preds

# === SFT EVALUATION ===
print('\n=== SFT (exception_only seed42) ===')
sft_labs = [c['label'] for c in categories]
sft_ps = [c['sft_pred'] for c in categories]
sft_n_correct = sum(p == l for p, l in zip(sft_ps, sft_labs))
sft_acc = sft_n_correct / len(sft_labs)
print(f'Accuracy: {sft_n_correct}/{len(sft_labs)} = {sft_acc:.4f} ({sft_acc*100:.2f}%)')
for cls in ['pass', 'fail']:
    tp = sum(p == cls and l == cls for p, l in zip(sft_ps, sft_labs))
    fp = sum(p == cls and l != cls for p, l in zip(sft_ps, sft_labs))
    fn = sum(p != cls and l == cls for p, l in zip(sft_ps, sft_labs))
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
    print(f'  {cls}: P={prec:.4f} R={rec:.4f} F1={f1:.4f} (TP={tp} FP={fp} FN={fn})')

sft_errors = [(c, p) for c, p in zip(categories, sft_ps) if p != c['label']]
print(f'  Errors ({len(sft_errors)}):')
for c, p in sft_errors:
    tp = c['trace_text'][:100].replace('\n', ' ')
    print(f'    idx={c["idx"]} label={c["label"]} pred={p} pat={c["pattern"]} | {tp}')

# === McNEMAR ===
print('\n=== McNEMAR DISCORDANT PAIRS (SFT vs Regex) ===')
for rname, rpreds in regex_results.items():
    sr_wrong = []
    rs_wrong = []
    for i, (s, r, l) in enumerate(zip(sft_ps, rpreds, sft_labs)):
        sc = (s == l)
        rc = (r == l)
        if sc and not rc:
            sr_wrong.append(i)
        if rc and not sc:
            rs_wrong.append(i)

    print(f'\n{rname}:')
    print(f'  SFT_correct & Regex_wrong: {len(sr_wrong)}')
    print(f'  SFT_wrong & Regex_correct: {len(rs_wrong)}')
    print(f'  Net SFT advantage: {len(sr_wrong) - len(rs_wrong)}')

    if sr_wrong:
        print(f'  Samples SFT correct but {rname} wrong:')
        for idx in sr_wrong[:20]:
            c = categories[idx]
            tp = c['trace_text'][:120].replace('\n', ' ')
            print(f'    idx={idx} label={c["label"]} sft={c["sft_pred"]} regex={rpreds[idx]} pat={c["pattern"]} | {tp}')

    if rs_wrong:
        print(f'  Samples {rname} correct but SFT wrong:')
        for idx in rs_wrong[:20]:
            c = categories[idx]
            tp = c['trace_text'][:120].replace('\n', ' ')
            print(f'    idx={idx} label={c["label"]} sft={c["sft_pred"]} regex={rpreds[idx]} pat={c["pattern"]} | {tp}')

# === Q2: EDGE CASES ===
print('\n=== Q2: EDGE CASE ANALYSIS ===')

print('\n--- Case 1: fail samples WITHOUT [ERROR] tag ---')
fail_no_error = [c for c in categories if c['label'] == 'fail' and not c['has_error_tag']]
print(f'Count: {len(fail_no_error)}')
for c in fail_no_error:
    sc = 'SFT_OK' if c['sft_pred'] == c['label'] else 'SFT_ERR'
    tp = c['trace_text'][:150].replace('\n', ' ')
    print(f'  idx={c["idx"]} pat={c["pattern"]} {sc} | {tp}')

print('\n--- Case 2: pass samples WITH exception/error text ---')
pass_with_error = [c for c in categories if c['label'] == 'pass' and (c['has_error_tag'] or c['has_error_word'])]
print(f'Count: {len(pass_with_error)}')
for c in pass_with_error[:30]:
    sc = 'SFT_OK' if c['sft_pred'] == c['label'] else 'SFT_ERR'
    tp = c['trace_text'][:150].replace('\n', ' ')
    print(f'  idx={c["idx"]} pat={c["pattern"]} e_tag={c["has_error_tag"]} e_word={c["has_error_word"]} {sc} | {tp}')

print('\n--- Case 3: [No trace available] label distribution ---')
no_trace = [c for c in categories if c['pattern'] == 'NO_TRACE_AVAILABLE']
print(f'Count: {len(no_trace)}')
nt_labs = Counter(c['label'] for c in no_trace)
print(f'  Labels: {dict(nt_labs)}')
nt_sft = sum(1 for c in no_trace if c['sft_pred'] == c['label'])
print(f'  SFT accuracy: {nt_sft}/{len(no_trace)}')
for c in no_trace:
    sc = 'SFT_OK' if c['sft_pred'] == c['label'] else 'SFT_ERR'
    print(f'  idx={c["idx"]} label={c["label"]} sft={c["sft_pred"]} {sc}')

print('\n--- Case 4: OTHER category ---')
other = [c for c in categories if c['pattern'] == 'OTHER']
print(f'Count: {len(other)}')
for c in other[:15]:
    sc = 'SFT_OK' if c['sft_pred'] == c['label'] else 'SFT_ERR'
    print(f'  idx={c["idx"]} label={c["label"]} {sc}')
    print(f'    trace: {c["trace_text"][:300]}')

# === MULTI-SEED ===
print('\n=== MULTI-SEED SFT ===')
for sn, pp in all_seed_preds.items():
    if len(pp) != len(test_data):
        print(f'{sn}: {len(pp)} preds (MISMATCH)')
        continue
    nc = sum(pp[i]['pred'] == test_data[i]['output'] for i in range(len(test_data)))
    print(f'{sn}: {nc}/{len(test_data)} = {nc/len(test_data)*100:.2f}%')

# === FINAL SUMMARY ===
print('\n=== FINAL SUMMARY TABLE ===')
print(f'{"Method":<20} {"Acc":>8} {"Correct":>8} {"Errors":>8}')
print('-' * 48)
for rn, rp in regex_results.items():
    nc = sum(p == l for p, l in zip(rp, sft_labs))
    print(f'{rn:<20} {nc/len(sft_labs)*100:>7.2f}% {nc:>8} {len(sft_labs)-nc:>8}')
print(f'{"SFT (seed42)":<20} {sft_acc*100:>7.2f}% {sft_n_correct:>8} {len(sft_labs)-sft_n_correct:>8}')
print(f'\nDelta (SFT - best regex): {(sft_acc - max(sum(p==l for p,l in zip(rp,sft_labs))/len(sft_labs) for rp in regex_results.values()))*100:.2f}%')
