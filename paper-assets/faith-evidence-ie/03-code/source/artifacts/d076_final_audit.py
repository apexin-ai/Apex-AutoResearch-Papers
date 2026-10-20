#!/usr/bin/env python3
"""Final D076 Protocol Compliance Audit - comprehensive summary with metrics."""

import json
import re

fpath = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt'

with open(fpath, 'r') as f:
    raw = json.load(f)

result_str = raw.get('result', raw)
if isinstance(result_str, str):
    data = json.loads(result_str)
else:
    data = result_str

experiments = data['data']['experiments']

def parse_command(cmd):
    result = {
        'batch_size': None, 'max_new_tokens': None, 'seed': None,
        'no_quantize': False, 'model_path': None, 'sft_adapter': None,
    }
    if not cmd:
        return result
    m = re.search(r'--batch_size\s+(\S+)', cmd)
    if m: result['batch_size'] = m.group(1)
    m = re.search(r'--max_new_tokens\s+(\S+)', cmd)
    if m: result['max_new_tokens'] = m.group(1)
    m = re.search(r'--seed\s+(\S+)', cmd)
    if m: result['seed'] = m.group(1).rstrip('"')
    if '--no-quantize' in cmd or '--no_quantize' in cmd:
        result['no_quantize'] = True
    m = re.search(r'--model_path\s+(\S+)', cmd)
    if m: result['model_path'] = m.group(1)
    m = re.search(r'--sft_adapter\s+(\S+)', cmd)
    if m: result['sft_adapter'] = m.group(1)
    return result

def find_ign_f1(exp):
    """Deep search for ign_f1."""
    for loc in [exp.get('reproduce', {}), exp.get('extra', {}), exp.get('spec', {})]:
        if isinstance(loc, dict):
            if 'metrics' in loc and isinstance(loc['metrics'], dict):
                m = loc['metrics']
                if 'ign_f1' in m:
                    return m['ign_f1']
            if 'ign_f1' in loc:
                return loc['ign_f1']
    return None

def model_path_issue(mp):
    if not mp:
        return "MISSING"
    adapter_patterns = ['sft_output', 'adapter', 'checkpoint', 'lora', 'grpo', 'rsft_output', 'dpo_output']
    base_patterns = ['models/Qwen3-4B', 'models/Qwen/Qwen3-4B']
    if any(p in mp for p in base_patterns):
        return None  # OK
    if any(p in mp for p in adapter_patterns):
        return f"ADAPTER:{mp}"
    return f"UNKNOWN:{mp}"

# Collect 4B eval experiments
eval_exps = []
for exp_id, exp in experiments.items():
    is_4b = False
    cmd = exp.get('spec', {}).get('command', '')
    hypothesis = exp.get('hypothesis', '')
    model_name = exp.get('spec', {}).get('model_name', '')
    for c in [cmd, hypothesis, model_name, exp_id]:
        if c and ('4b' in c.lower() or '4B' in c or 'Qwen3-4B' in c):
            is_4b = True
            break
    if not is_4b:
        continue
    is_eval = 'eval' in exp_id.lower() or ('eval' in cmd.lower() and 'inference' in cmd.lower()) or 'eval' in hypothesis.lower()
    if not is_eval:
        continue
    eval_exps.append((exp_id, exp))

eval_exps.sort(key=lambda x: x[0])

# Print final comprehensive table
print(f"D076 COMPLIANCE AUDIT FOR ALL 4B EVAL EXPERIMENTS ({len(eval_exps)} total)")
print(f"D076 spec: batch_size=4, max_new_tokens=1024, seed=42, --no-quantize, model_path=base, sft_adapter=adapter")
print()

# Count stats
compliant = 0
non_compliant = 0
issues_counter = {
    'model_path_is_adapter': 0,
    'missing_no_quantize': 0,
    'wrong_batch_size': 0,
    'wrong_seed': 0,
    'missing_sft_adapter': 0,
    'wrong_max_new_tokens': 0,
    'missing_model_path': 0,
}

rows = []
for exp_id, exp in eval_exps:
    cmd = exp.get('spec', {}).get('command', '')
    status = exp.get('status', '?')
    parsed = parse_command(cmd)
    ign_f1 = find_ign_f1(exp)

    reasons = []
    if parsed['batch_size'] != '4':
        reasons.append(f"bs={parsed['batch_size']}")
        if parsed['batch_size'] is not None:
            issues_counter['wrong_batch_size'] += 1
        else:
            issues_counter['wrong_batch_size'] += 1
    if parsed['max_new_tokens'] != '1024':
        reasons.append(f"mnt={parsed['max_new_tokens']}")
        issues_counter['wrong_max_new_tokens'] += 1
    if parsed['seed'] != '42':
        reasons.append(f"seed={parsed['seed']}")
        issues_counter['wrong_seed'] += 1
    if not parsed['no_quantize']:
        reasons.append("no --no-quantize")
        issues_counter['missing_no_quantize'] += 1

    mp_issue = model_path_issue(parsed['model_path'])
    if mp_issue:
        if mp_issue == "MISSING":
            reasons.append("model_path MISSING")
            issues_counter['missing_model_path'] += 1
        else:
            reasons.append("model_path->adapter")
            issues_counter['model_path_is_adapter'] += 1

    if not parsed['sft_adapter']:
        reasons.append("no --sft_adapter")
        issues_counter['missing_sft_adapter'] += 1

    is_compliant = len(reasons) == 0
    if is_compliant:
        compliant += 1
    else:
        non_compliant += 1

    rows.append({
        'exp_id': exp_id,
        'status': status,
        'ign_f1': f"{ign_f1:.4f}" if ign_f1 is not None else "N/A",
        'bs': parsed['batch_size'] or '?',
        'mnt': parsed['max_new_tokens'] or '?',
        'seed': parsed['seed'] or '?',
        'nq': 'Y' if parsed['no_quantize'] else 'N',
        'model_path': parsed['model_path'] or 'MISSING',
        'sft_adapter': parsed['sft_adapter'] or 'MISSING',
        'compliant': 'YES' if is_compliant else 'NO',
        'reasons': '; '.join(reasons),
        'full_cmd': cmd,
    })

# Print table
fmt = "{:<45} {:>8} {:>8} {:>4} {:>5} {:>5} {:>3} {:>5} {}"
print(fmt.format("exp_id", "status", "ign_f1", "bs", "mnt", "seed", "nq", "D076", "non_compliance"))
print("-" * 130)

for r in rows:
    print(fmt.format(
        r['exp_id'][:45], r['status'][:8], r['ign_f1'],
        r['bs'][:4], r['mnt'][:5], r['seed'][:5], r['nq'],
        r['compliant'], r['reasons']
    ))

print(f"\n{'=' * 100}")
print(f"COMPLIANCE STATS: {compliant}/{len(eval_exps)} D076-compliant, {non_compliant}/{len(eval_exps)} non-compliant")
print(f"\nIssue breakdown:")
for issue, count in sorted(issues_counter.items(), key=lambda x: -x[1]):
    print(f"  {issue}: {count}")

print(f"\n{'=' * 100}")
print("D076-COMPLIANT EXPERIMENTS (model_path=base, sft_adapter=adapter, bs=4, mnt=1024, seed=42, --no-quantize):")
print("-" * 100)
for r in rows:
    if r['compliant'] == 'YES':
        print(f"  {r['exp_id']:<45} ign_f1={r['ign_f1']:<8} model_path={r['model_path']}")
        print(f"    sft_adapter={r['sft_adapter']}")

print(f"\n{'=' * 100}")
print("SFT s42 (ORIGINAL SEED) EVAL EXPERIMENTS:")
print("-" * 100)
# Look for SFT baseline evals (not RSFT, not GRPO)
for r in rows:
    eid = r['exp_id'].lower()
    if ('sft' in eid and 'eval' in eid and 'rsft' not in eid and 'grpo' not in eid
        and 'dpo' not in eid and 'no_evidence' not in eid and 'nli' not in eid):
        print(f"  {r['exp_id']:<45} ign_f1={r['ign_f1']:<8} D076={r['compliant']}")
        print(f"    model_path:  {r['model_path']}")
        print(f"    sft_adapter: {r['sft_adapter']}")
        print(f"    issues:      {r['reasons'] if r['reasons'] else 'NONE'}")
        print(f"    FULL CMD:    {r['full_cmd']}")
        print()

# Also look for reeval_sft_baseline_d076 specifically
print(f"\n{'=' * 100}")
print("FULL COMMANDS FOR ALL D076-COMPLIANT EXPERIMENTS:")
print("-" * 100)
for r in rows:
    if r['compliant'] == 'YES':
        print(f"\n  exp_id: {r['exp_id']}")
        print(f"  ign_f1: {r['ign_f1']}")
        print(f"  FULL CMD: {r['full_cmd']}")
