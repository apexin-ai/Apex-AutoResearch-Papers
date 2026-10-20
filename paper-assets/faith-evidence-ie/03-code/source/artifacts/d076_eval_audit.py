#!/usr/bin/env python3
"""D076 Protocol Compliance Audit for all 4B eval experiments."""

import json
import re
import sys

fpath = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt'

with open(fpath, 'r') as f:
    raw = json.load(f)

result_str = raw.get('result', raw)
if isinstance(result_str, str):
    data = json.loads(result_str)
else:
    data = result_str

experiments = data['data']['experiments']

# Collect all 4B eval experiments
eval_exps = []
for exp_id, exp in experiments.items():
    # Check if it references Qwen3-4B (in spec command, hypothesis, model_name, or exp_id)
    is_4b = False
    cmd = exp.get('spec', {}).get('command', '')
    hypothesis = exp.get('hypothesis', '')
    model_name = exp.get('spec', {}).get('model_name', '')

    checks = [cmd, hypothesis, model_name, exp_id]
    for c in checks:
        if c and ('4b' in c.lower() or '4B' in c or 'Qwen3-4B' in c):
            is_4b = True
            break

    if not is_4b:
        continue

    # Check if it's an eval experiment
    is_eval = False
    if 'eval' in exp_id.lower():
        is_eval = True
    if 'eval' in cmd.lower() and ('inference' in cmd.lower() or 'eval' in cmd.lower()):
        is_eval = True
    if 'eval' in hypothesis.lower():
        is_eval = True

    if not is_eval:
        continue

    eval_exps.append((exp_id, exp))

print(f"=" * 120)
print(f"D076 PROTOCOL COMPLIANCE AUDIT - All Qwen3-4B Eval Experiments")
print(f"Total experiments in registry: {len(experiments)}")
print(f"4B eval experiments found: {len(eval_exps)}")
print(f"=" * 120)

# D076 expected values
D076 = {
    'batch_size': '4',
    'max_new_tokens': '1024',
    'seed': '42',
    'no_quantize': True,
    'model_path_is_base': True,  # should point to base model, not adapter
    'sft_adapter_present': True,
}

def parse_command(cmd):
    """Parse command string to extract D076-relevant parameters."""
    result = {
        'batch_size': None,
        'max_new_tokens': None,
        'seed': None,
        'no_quantize': False,
        'model_path': None,
        'sft_adapter': None,
    }

    if not cmd:
        return result

    # batch_size
    m = re.search(r'--batch_size\s+(\S+)', cmd)
    if m:
        result['batch_size'] = m.group(1)

    # max_new_tokens
    m = re.search(r'--max_new_tokens\s+(\S+)', cmd)
    if m:
        result['max_new_tokens'] = m.group(1)

    # seed
    m = re.search(r'--seed\s+(\S+)', cmd)
    if m:
        result['seed'] = m.group(1)

    # no-quantize
    if '--no-quantize' in cmd or '--no_quantize' in cmd:
        result['no_quantize'] = True

    # model_path
    m = re.search(r'--model_path\s+(\S+)', cmd)
    if m:
        result['model_path'] = m.group(1)

    # sft_adapter
    m = re.search(r'--sft_adapter\s+(\S+)', cmd)
    if m:
        result['sft_adapter'] = m.group(1)

    return result

def check_model_path_is_base(model_path):
    """Check if model_path points to base model (not adapter directory)."""
    if not model_path:
        return False, "missing"
    # Base model patterns
    base_patterns = ['Qwen3-4B', 'models/Qwen', 'Qwen/Qwen']
    # Adapter/SFT output patterns (non-compliant)
    adapter_patterns = ['sft_output', 'adapter', 'checkpoint', 'lora', 'grpo_output', 'rsft_output']

    is_base = any(p in model_path for p in base_patterns)
    is_adapter = any(p in model_path for p in adapter_patterns)

    if is_adapter:
        return False, f"points to adapter dir: {model_path}"
    if is_base:
        return True, "OK"
    return False, f"unknown path: {model_path}"

def check_d076(parsed):
    """Check D076 compliance and return (compliant, reasons)."""
    reasons = []

    if parsed['batch_size'] != '4':
        reasons.append(f"batch_size={parsed['batch_size']} (expected 4)")
    if parsed['max_new_tokens'] != '1024':
        reasons.append(f"max_new_tokens={parsed['max_new_tokens']} (expected 1024)")
    if parsed['seed'] != '42':
        reasons.append(f"seed={parsed['seed']} (expected 42)")
    if not parsed['no_quantize']:
        reasons.append("--no-quantize MISSING")

    base_ok, base_msg = check_model_path_is_base(parsed['model_path'])
    if not base_ok:
        reasons.append(f"model_path: {base_msg}")

    if not parsed['sft_adapter']:
        reasons.append("--sft_adapter MISSING")

    compliant = len(reasons) == 0
    return compliant, reasons

# Sort by exp_id
eval_exps.sort(key=lambda x: x[0])

# Print detailed info for each experiment
print()
for i, (exp_id, exp) in enumerate(eval_exps):
    cmd = exp.get('spec', {}).get('command', '')
    status = exp.get('status', 'UNKNOWN')
    hypothesis = exp.get('hypothesis', '')
    metrics = exp.get('spec', {}).get('metrics', exp.get('reproduce', {}).get('metrics', {}))
    # Also check for metrics in other locations
    if not metrics:
        for key in ['results', 'metrics']:
            if key in exp:
                metrics = exp[key]
                break
    # Check extra for metrics
    if not metrics and 'extra' in exp:
        extra = exp['extra']
        if isinstance(extra, dict):
            for key in ['metrics', 'results', 'eval_metrics']:
                if key in extra:
                    metrics = extra[key]
                    break

    # Get conclusion and notes
    conclusion = exp.get('reproduce', {}).get('conclusion', '')
    if not conclusion:
        conclusion = exp.get('extra', {}).get('conclusion', '')
    notes = exp.get('reproduce', {}).get('notes', '')
    if not notes:
        notes = exp.get('extra', {}).get('notes', '')
    error = exp.get('reproduce', {}).get('error', '')
    if not error:
        error = exp.get('extra', {}).get('error', '')

    parsed = parse_command(cmd)
    compliant, reasons = check_d076(parsed)

    print(f"\n{'─' * 120}")
    print(f"[{i+1}/{len(eval_exps)}] exp_id: {exp_id}")
    print(f"  status:     {status}")
    print(f"  hypothesis: {hypothesis[:200]}")
    print(f"  parent:     {exp.get('parent', 'N/A')}")
    print(f"  model_name: {exp.get('spec', {}).get('model_name', 'N/A')}")
    print()
    print(f"  FULL COMMAND:")
    print(f"    {cmd}")
    print()
    print(f"  PARSED D076 PARAMS:")
    print(f"    batch_size:     {parsed['batch_size']}")
    print(f"    max_new_tokens: {parsed['max_new_tokens']}")
    print(f"    seed:           {parsed['seed']}")
    print(f"    no_quantize:    {parsed['no_quantize']}")
    print(f"    model_path:     {parsed['model_path']}")
    print(f"    sft_adapter:    {parsed['sft_adapter']}")
    print()
    print(f"  D076 COMPLIANT:   {'YES' if compliant else 'NO'}")
    if reasons:
        print(f"  NON-COMPLIANCE:   {'; '.join(reasons)}")
    print()

    # Print all extra fields that might contain metrics/conclusion
    print(f"  metrics:    {json.dumps(metrics, indent=4) if metrics else 'N/A'}")
    print(f"  conclusion: {conclusion if conclusion else 'N/A'}")
    print(f"  notes:      {notes if notes else 'N/A'}")
    print(f"  error:      {error if error else 'N/A'}")

    # Dump all keys in reproduce and extra for completeness
    reproduce = exp.get('reproduce', {})
    if reproduce:
        extra_keys = [k for k in reproduce.keys() if k not in ('finished_at', 'conclusion', 'notes', 'error', 'metrics')]
        if extra_keys:
            print(f"  reproduce extra keys: {extra_keys}")
            for k in extra_keys:
                v = reproduce[k]
                v_str = json.dumps(v) if isinstance(v, (dict, list)) else str(v)
                if len(v_str) > 500:
                    v_str = v_str[:500] + '...'
                print(f"    reproduce.{k}: {v_str}")

    extra = exp.get('extra', {})
    if extra:
        extra_keys = [k for k in extra.keys() if k not in ('hook_events', 'conclusion', 'notes', 'error', 'metrics')]
        if extra_keys:
            print(f"  extra keys: {extra_keys}")
            for k in extra_keys:
                v = extra[k]
                v_str = json.dumps(v) if isinstance(v, (dict, list)) else str(v)
                if len(v_str) > 500:
                    v_str = v_str[:500] + '...'
                print(f"    extra.{k}: {v_str}")

# Now print summary table
print(f"\n\n{'=' * 200}")
print("SUMMARY TABLE")
print(f"{'=' * 200}")

header = f"{'exp_id':<45} | {'status':<12} | {'ign_f1':<8} | {'bs':<4} | {'max_tok':<8} | {'seed':<5} | {'no_q':<5} | {'model_path':<55} | {'sft_adapter':<55} | {'D076':<5} | non_compliance"
print(header)
print("─" * len(header))

for exp_id, exp in eval_exps:
    cmd = exp.get('spec', {}).get('command', '')
    status = exp.get('status', '?')
    parsed = parse_command(cmd)
    compliant, reasons = check_d076(parsed)

    # Try to find ign_f1
    ign_f1 = 'N/A'
    for loc in [exp.get('reproduce', {}), exp.get('extra', {}), exp.get('spec', {})]:
        if isinstance(loc, dict):
            if 'metrics' in loc and isinstance(loc['metrics'], dict):
                if 'ign_f1' in loc['metrics']:
                    ign_f1 = str(loc['metrics']['ign_f1'])
                    break
            if 'ign_f1' in loc:
                ign_f1 = str(loc['ign_f1'])
                break
    # Also check nested results
    for loc in [exp.get('reproduce', {}), exp.get('extra', {})]:
        if isinstance(loc, dict):
            for k, v in loc.items():
                if isinstance(v, dict) and 'ign_f1' in v:
                    ign_f1 = str(v['ign_f1'])
                    break

    mp = parsed['model_path'] or 'MISSING'
    sa = parsed['sft_adapter'] or 'MISSING'
    # Shorten paths for table
    mp_short = mp[-55:] if len(mp) > 55 else mp
    sa_short = sa[-55:] if len(sa) > 55 else sa

    row = f"{exp_id:<45} | {status:<12} | {ign_f1:<8} | {parsed['batch_size'] or '?':<4} | {parsed['max_new_tokens'] or '?':<8} | {parsed['seed'] or '?':<5} | {'Y' if parsed['no_quantize'] else 'N':<5} | {mp_short:<55} | {sa_short:<55} | {'YES' if compliant else 'NO':<5} | {'; '.join(reasons) if reasons else ''}"
    print(row)

# Special analysis: SFT s42 eval experiments
print(f"\n\n{'=' * 120}")
print("SPECIAL ANALYSIS: SFT s42 (original seed) eval experiments")
print(f"{'=' * 120}")
for exp_id, exp in eval_exps:
    if 's42' in exp_id.lower() or 'seed42' in exp_id.lower() or ('sft' in exp_id.lower() and 's42' in exp.get('hypothesis', '').lower()):
        cmd = exp.get('spec', {}).get('command', '')
        parsed = parse_command(cmd)
        print(f"\n  exp_id: {exp_id}")
        print(f"  status: {exp.get('status', '?')}")
        print(f"  model_path:  {parsed['model_path']}")
        print(f"  sft_adapter: {parsed['sft_adapter']}")
        print(f"  FULL CMD: {cmd}")

# Also check: any eval using the original SFT output (no seed suffix)
print(f"\n\n{'=' * 120}")
print("SPECIAL ANALYSIS: Evals with model_path pointing to adapter directories")
print(f"{'=' * 120}")
for exp_id, exp in eval_exps:
    cmd = exp.get('spec', {}).get('command', '')
    parsed = parse_command(cmd)
    if parsed['model_path']:
        base_ok, base_msg = check_model_path_is_base(parsed['model_path'])
        if not base_ok:
            print(f"\n  exp_id:     {exp_id}")
            print(f"  status:     {exp.get('status', '?')}")
            print(f"  model_path: {parsed['model_path']}")
            print(f"  issue:      {base_msg}")
            print(f"  FULL CMD:   {cmd}")

print(f"\n\n{'=' * 120}")
print("SPECIAL ANALYSIS: Evals MISSING --no-quantize")
print(f"{'=' * 120}")
for exp_id, exp in eval_exps:
    cmd = exp.get('spec', {}).get('command', '')
    parsed = parse_command(cmd)
    if not parsed['no_quantize']:
        print(f"\n  exp_id:  {exp_id}")
        print(f"  status:  {exp.get('status', '?')}")
        print(f"  FULL CMD: {cmd}")

print(f"\n\n{'=' * 120}")
print("SPECIAL ANALYSIS: Evals with non-standard batch_size or max_new_tokens")
print(f"{'=' * 120}")
for exp_id, exp in eval_exps:
    cmd = exp.get('spec', {}).get('command', '')
    parsed = parse_command(cmd)
    issues = []
    if parsed['batch_size'] and parsed['batch_size'] != '4':
        issues.append(f"batch_size={parsed['batch_size']}")
    if parsed['max_new_tokens'] and parsed['max_new_tokens'] != '1024':
        issues.append(f"max_new_tokens={parsed['max_new_tokens']}")
    if issues:
        print(f"\n  exp_id:  {exp_id}")
        print(f"  status:  {exp.get('status', '?')}")
        print(f"  issues:  {', '.join(issues)}")
        print(f"  FULL CMD: {cmd}")

# Count compliant vs non-compliant
compliant_count = 0
non_compliant_count = 0
for exp_id, exp in eval_exps:
    cmd = exp.get('spec', {}).get('command', '')
    parsed = parse_command(cmd)
    compliant, _ = check_d076(parsed)
    if compliant:
        compliant_count += 1
    else:
        non_compliant_count += 1

print(f"\n\n{'=' * 120}")
print(f"OVERALL D076 COMPLIANCE: {compliant_count}/{len(eval_exps)} compliant, {non_compliant_count}/{len(eval_exps)} non-compliant")
print(f"{'=' * 120}")
