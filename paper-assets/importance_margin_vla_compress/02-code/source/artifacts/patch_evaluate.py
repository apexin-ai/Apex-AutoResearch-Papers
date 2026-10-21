"""Patch evaluate.py: add random importance score metrics for baseline models."""

import sys

filepath = "/root/autodl-tmp/importance_margin_vla_compress/evaluate.py"

with open(filepath, "r") as f:
    lines = f.readlines()

# Find key line numbers (0-indexed)
baseline_start = None
baseline_continue = None
imm_guard_line = None
summary_if_line = None

for i, line in enumerate(lines):
    stripped = line.rstrip()
    if "# D011: Baseline path" in stripped and baseline_start is None:
        baseline_start = i
    if baseline_start is not None and baseline_continue is None and stripped.endswith("continue") and "if not imm_enabled" not in stripped:
        # Find the 'continue' that ends the baseline block
        if i > baseline_start and "continue" in stripped:
            baseline_continue = i
    if "if imm_enabled and all_margins:" in stripped:
        imm_guard_line = i
    if stripped.strip() == "if imm_enabled:" and i > 400:
        summary_if_line = i

print(f"baseline_start={baseline_start}, baseline_continue={baseline_continue}")
print(f"imm_guard_line={imm_guard_line}, summary_if_line={summary_if_line}")

assert baseline_start is not None, "Cannot find baseline start"
assert baseline_continue is not None, "Cannot find baseline continue"
assert imm_guard_line is not None, "Cannot find imm_guard_line"
assert summary_if_line is not None, "Cannot find summary_if_line"

# === Change 1: Insert random score computation before 'continue' in baseline path ===
# Replace the 'continue' line with metric computation + continue
indent = "                    "
random_score_block = [
    "\n",
    f"{indent}# Uniform random scores as null-hypothesis baseline for margin/preservation\n",
    f"{indent}n_visual = 64\n",
    f"{indent}k_keep = int(n_visual * (1 - pruning_ratio))\n",
    f"{indent}B = next(v.shape[0] for v in batch.values() if isinstance(v, torch.Tensor) and v.dim() > 0)\n",
    "\n",
    f"{indent}g = torch.Generator()\n",
    f"{indent}g.manual_seed(seed + condition_offset + batch_idx * 1000)\n",
    f"{indent}scores_clean = torch.rand(B, n_visual, generator=g)\n",
    "\n",
    f"{indent}if epsilon > 0:\n",
    f"{indent}    g.manual_seed(seed + condition_offset + batch_idx * 1000 + 500)\n",
    f"{indent}    scores_pert = torch.rand(B, n_visual, generator=g)\n",
    f"{indent}else:\n",
    f"{indent}    scores_pert = scores_clean\n",
    "\n",
    f"{indent}margin = compute_margin(scores_clean, k_keep)\n",
    f"{indent}pres = topk_preservation_rate(scores_clean, scores_pert, k_keep)\n",
    f"{indent}kendall = kendall_tau_distance(scores_clean, scores_pert, k_keep)\n",
    f"{indent}cert = certified_bound(margin, lipschitz_const, max(epsilon, 0.01), k_keep)\n",
    f"{indent}led = l_eps_delta_ratio(lipschitz_const, max(epsilon, 0.01), margin, k_keep)\n",
    "\n",
    f"{indent}all_margins.append(margin)\n",
    f"{indent}all_preservation.append(pres)\n",
    f"{indent}all_kendall.append(kendall)\n",
    f"{indent}all_certified.append(cert)\n",
    f"{indent}all_led_ratio.append(led)\n",
]

# Also update the comment
lines[baseline_start] = lines[baseline_start].replace(
    "# D011: Baseline path — apply perturbation + random pruning",
    "# Baseline path: action loss + random importance scores for Gate metrics"
)

# Insert before the continue line
new_lines = lines[:baseline_continue] + random_score_block + lines[baseline_continue:]

# Recalculate line positions after insertion
offset = len(random_score_block)
imm_guard_line += offset
summary_if_line += offset

# === Change 2: Remove imm_enabled guard on metric aggregation ===
old_line = new_lines[imm_guard_line]
assert "imm_enabled and all_margins" in old_line, f"Unexpected content at line {imm_guard_line}: {old_line!r}"
new_lines[imm_guard_line] = old_line.replace("if imm_enabled and all_margins:", "if all_margins:")

# === Change 3: Extend Gate Metric Summary to also cover baseline ===
# Find the block from summary_if_line and replace it
# Current block (10 lines):
#     if imm_enabled:
#         clean_key = "eps0.0_pruneFalse"
#         if clean_key in results and "l_eps_delta_ratio_mean" in results.get(clean_key, {}):
#             log.info("=== Gate Metric Summary ===")
#             for cond, data in results.items():
#                 if cond.startswith("_"):
#                     continue
#                 led = data.get("l_eps_delta_ratio_mean", float("nan"))
#                 pres = data.get("preservation_rate", float("nan"))
#                 log.info("  %s: L*eps*k/Delta_k=%.4f, preservation=%.4f", cond, led, pres)

# Find the end of this block
summary_end = summary_if_line + 1
while summary_end < len(new_lines):
    line = new_lines[summary_end]
    # Block ends when we hit a line at same or lower indentation (4 spaces = top-level in main)
    if line.strip() and not line.startswith("        ") and not line.startswith("\t\t"):
        # Check if it's at the same level as "if imm_enabled:" (4 spaces)
        stripped = line.rstrip()
        leading = len(line) - len(line.lstrip())
        if leading <= 4 and stripped:
            break
    summary_end += 1

print(f"Summary block: lines {summary_if_line}-{summary_end}")

new_summary = [
    '    clean_key = "eps0.0_pruneFalse"\n',
    '    if clean_key in results and "margin_median" in results.get(clean_key, {}):\n',
    '        log.info("=== Gate Metric Summary ===")\n',
    '        for cond, data in results.items():\n',
    '            if cond.startswith("_"):\n',
    '                continue\n',
    '            margin = data.get("margin_median", float("nan"))\n',
    '            led = data.get("l_eps_delta_ratio_mean", float("nan"))\n',
    '            pres = data.get("preservation_rate", float("nan"))\n',
    '            log.info("  %s: margin_median=%.4f, L*eps*k/Delta_k=%.4f, preservation=%.4f", cond, margin, led, pres)\n',
    '\n',
]

new_lines = new_lines[:summary_if_line] + new_summary + new_lines[summary_end:]

with open(filepath, "w") as f:
    f.writelines(new_lines)

print("OK: all 3 patches applied successfully")
