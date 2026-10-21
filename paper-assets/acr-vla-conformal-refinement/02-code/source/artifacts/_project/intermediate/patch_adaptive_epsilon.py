"""Patch evaluate.py to add adaptive epsilon scaling.

Replaces the binary gate (apply CRM or skip) with a proportional correction:
    ε_adaptive = ε_max × min(d₂ / τ, 1.0)

When --adaptive_epsilon is set:
  - CRM correction is ALWAYS applied (no binary gate)
  - Correction magnitude scales linearly with d₂/τ, capped at ε_max
  - Low-uncertainty steps get near-zero correction (soft gating)
  - High-uncertainty steps (d₂ ≥ τ) get full ε_max correction

Usage:
    python patch_adaptive_epsilon.py
    # Then run with:
    python src/evaluate.py --mode adaptive_conformal_crm --adaptive_epsilon ...
"""
import sys

filepath = "/root/acr-vla-conformal-refinement/src/evaluate.py"
with open(filepath, "r") as f:
    code = f.read()

changes = 0

# 1. Add --adaptive_epsilon argument after --conformal_threshold
old_arg = '    p.add_argument("--conformal_threshold", type=float, default=0.074855)'
new_arg = '''    p.add_argument("--conformal_threshold", type=float, default=0.074855)
    p.add_argument("--adaptive_epsilon", action="store_true", default=False,
                   help="Scale CRM correction proportionally to d2/tau instead of binary gating")'''
if old_arg in code:
    code = code.replace(old_arg, new_arg)
    changes += 1
    print("1. Added --adaptive_epsilon argument")
else:
    print("1. SKIP: --conformal_threshold arg not found (trying alternative)")
    # Try without leading spaces variation
    for variant in [
        'p.add_argument("--conformal_threshold", type=float, default=0.074855)',
        'parser.add_argument("--conformal_threshold"',
    ]:
        if variant in code:
            code = code.replace(variant, variant + '''
    p.add_argument("--adaptive_epsilon", action="store_true", default=False,
                   help="Scale CRM correction proportionally to d2/tau instead of binary gating")''')
            changes += 1
            print("1. Added --adaptive_epsilon argument (variant match)")
            break

# 2. Modify select_action_conformal_crm to accept adaptive_epsilon parameter
# The function signature needs to include adaptive_epsilon
# Current pattern: def select_action_conformal_crm(wrapper, obs, task_desc, cgs, crm, device, threshold, ...):
# We need to add adaptive_epsilon parameter

# Strategy: Find the function and add the parameter, then modify the gating logic
# Since exact function signature may vary, we patch the gating logic directly

# The gating logic should look something like:
#   if uncertainty > threshold:
#       ... apply CRM ...
#   else:
#       ... return unrefined action ...

# We replace with:
#   if adaptive_epsilon or uncertainty > threshold:
#       ... apply CRM ...
#       if adaptive_epsilon:
#           scale = min(uncertainty / threshold, 1.0)
#           correction = refined_pose - base_action_pose
#           refined_pose = base_action_pose + correction * scale
#   else:
#       ... return unrefined action ...

# Pattern: look for the uncertainty comparison and CRM application
# From adaptive_k_eval_prep.md, the function computes L2 distance, then:
#   if uncertainty > conformal_threshold -> apply CRM
#   else -> skip

# Find the pattern where uncertainty is compared to threshold
import re

# Look for the gating condition pattern
gate_pattern = r'(if\s+uncertainty\s*>\s*(?:conformal_)?threshold)'
match = re.search(gate_pattern, code)
if match:
    old_gate = match.group(0)
    new_gate = f'if adaptive_epsilon or {old_gate[3:]}'  # Remove 'if ' and re-add
    code = code.replace(old_gate, new_gate, 1)
    changes += 1
    print(f"2. Modified gate condition: '{old_gate}' -> '{new_gate}'")
else:
    print("2. SKIP: Gate condition pattern not found")
    # Try alternative patterns
    for alt in [
        'if uncertainty > threshold',
        'if d2 > threshold',
        'if d2 > conformal_threshold',
        'if l2_dist > threshold',
        'if l2_distance > threshold',
    ]:
        if alt in code:
            code = code.replace(alt, f'if adaptive_epsilon or {alt[3:]}', 1)
            changes += 1
            print(f"2. Modified gate condition (alt): '{alt}'")
            break

# 3. Add adaptive epsilon scaling after CRM correction
# Look for the line where refined_pose is computed from CRM output
# Pattern: refined_pose = crm(...) or similar
# After that, add the scaling logic

# We need to find where the refined action is computed and add scaling
# The pattern should be near: refined_pose = crm(base_action, ...)
# And before the action is assembled/returned

crm_call_pattern = r'(refined_pose\s*=\s*crm\([^)]+\))'
match = re.search(crm_call_pattern, code)
if match:
    crm_line = match.group(0)
    # Get the indentation
    line_start = code.rfind('\n', 0, match.start()) + 1
    indent = ''
    for ch in code[line_start:]:
        if ch in ' \t':
            indent += ch
        else:
            break

    scaling_code = f'''
{indent}if adaptive_epsilon:
{indent}    _correction = refined_pose - base_action_pose
{indent}    _scale = min(uncertainty / threshold, 1.0)
{indent}    refined_pose = base_action_pose + _correction * _scale'''

    code = code.replace(crm_line, crm_line + scaling_code, 1)
    changes += 1
    print("3. Added adaptive epsilon scaling after CRM forward")
else:
    print("3. SKIP: CRM call pattern not found")
    # Try alternatives
    for alt_pattern in [
        r'(refined\s*=\s*crm\([^)]+\))',
        r'(corrected_action\s*=\s*crm\([^)]+\))',
    ]:
        match = re.search(alt_pattern, code)
        if match:
            crm_line = match.group(0)
            line_start = code.rfind('\n', 0, match.start()) + 1
            indent = '        '
            var_name = crm_line.split('=')[0].strip()
            scaling_code = f'''
{indent}if adaptive_epsilon:
{indent}    _correction = {var_name} - base_action
{indent}    _scale = min(uncertainty / threshold, 1.0)
{indent}    {var_name} = base_action + _correction * _scale'''
            code = code.replace(crm_line, crm_line + scaling_code, 1)
            changes += 1
            print(f"3. Added adaptive epsilon scaling (alt var: {var_name})")
            break

# 4. Pass adaptive_epsilon to the action selection function
# Find where select_action_conformal_crm is called and add args.adaptive_epsilon
call_pattern = r'(select_action_conformal_crm\([^)]+)\)'
match = re.search(call_pattern, code)
if match:
    old_call = match.group(0)
    # Add adaptive_epsilon before the closing paren
    new_call = old_call[:-1] + ', args.adaptive_epsilon)'
    code = code.replace(old_call, new_call, 1)
    changes += 1
    print("4. Added adaptive_epsilon to function call")
else:
    print("4. SKIP: Function call pattern not found")

# 5. Add adaptive_epsilon to function definition
func_def_pattern = r'(def select_action_conformal_crm\([^)]+)\)'
match = re.search(func_def_pattern, code)
if match:
    old_def = match.group(0)
    new_def = old_def[:-1] + ', adaptive_epsilon=False)'
    code = code.replace(old_def, new_def, 1)
    changes += 1
    print("5. Added adaptive_epsilon to function definition")
else:
    print("5. SKIP: Function definition not found")

with open(filepath, "w") as f:
    f.write(code)

print(f"\nTotal changes: {changes}/5")
if changes >= 3:
    print("CORE PATCHES APPLIED")
elif changes == 0:
    print("ERROR: No patches applied — evaluate.py structure may have changed")
    print("MANUAL IMPLEMENTATION REQUIRED (see patch_adaptive_epsilon_manual.md)")
else:
    print(f"PARTIAL: {changes}/5 applied, verify remaining manually")
