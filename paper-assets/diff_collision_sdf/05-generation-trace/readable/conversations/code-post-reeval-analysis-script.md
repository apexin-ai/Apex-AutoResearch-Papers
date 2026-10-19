# code post reeval analysis script

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_code_post_reeval_analysis_script_20260526T092833.jsonl`
- **Structured JSON:** [`05bcfe219d207a102fec.json`](../../sessions/05/05bcfe219d207a102fec.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-26T09:30:27.928218+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_post_reeval_analysis_script_20260526T092833",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T09:30:27.928579+00:00_

__pycache__
_project
a3_lora_fix_result.json
analysis_m022_norm_stats_root_cause.md
analysis_m026_m027_m028_gradient_refine_diagnosis.md
analyze_d012_results.py
analyze_displacement.py
comprehensive_fix_report.txt
diagnose_eval_a3_v11_object.md
disk_cleanup_report.md
drafts
dream_reports
emergency_cleanup_report.md
eval_a3_v11_object
eval_collision_enhancement_plan.md
eval_commands_d012.md
eval_commands_d012_final.md
eval_openvla_safelibero.py
eval_pi05_safelibero.py
eval_pi05_safelibero_object_v11
eval_readiness_westd35807.md
eval_safelibero.py
eval_safelibero_openvla.py
figures
fix_a1.py
fix_a3.py
kg3_gradient_toy_test.py
literature_review.md
lora_baseline_launch_checklist.md
manifest.yaml
method_draft.md
metric_definitions.md
openvla_eval_prep.md
paper_data_summary.md
phase2_fix_report.md
pi05_a1_sdf_feasibility_report.md
pi05_collision_analysis_report.md
prep_spatial_a1.md
reference_audit_report.md
related_work_outline.md
related_work_survey.md
remaining_train_status.md
report_a1_integration.md
report_action_scale_fix.md
report_baseline_fix.md
report_baseline_prep.md
report_data_pipeline.md
report_env_setup_kg1_kg2.md
report_eval_tsr_zero_fix.md
report_kg3_gradient_test.md
report_openpi_deploy.md
report_pi05_object_collision_analysis.md
report_pi0_baseline_fake_rate.md
report_safelibero.md
report_sdf_extraction.md
report_vla_codebase.md
research_openvla_libero.md
src
step7k_overfit_check.md
task3_collision_matrix_step10k.md
threshold_sensitivity
train_a1_hook.py
train_a1_sdf_aux_pi05.py
train_baseline.py
train_pi05_lora_baseline.py
training_progress_20260520_1020.md
worker_output.md
worker_output_diagnose_eval_baseline_fullft_spatial_v11.md
worker_report_westd45947_status.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_post_reeval_analysis_script_20260526T092833",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T09:30:27.928866+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/reeval_comparison.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nPost-reeval comparison: bug-fix前 vs bug-fix后 eval 结果对比分析。\n\n背景: eval_safelibero.py 存在 180° 图像旋转 bug（缺少 [::-1, ::-1]），\n导致所有通过该脚本评估的模型 TSR 被严重低估。本脚本对比修复前后结果。\n\n输入:\n  - 硬编码的旧数据 (OLD_DATA)\n  - JSON 结果文件 或 手动填入的新数据 (NEW_DATA dict)\n输出:\n  - Terminal formatted table\n  - LaTeX table (.tex)\n  - JSON summary (.json)\n\"\"\"\n\nimport json\nimport sys\nimport os\nimport glob\nimport numpy as np\nfrom pathlib import Path\nfrom collections import OrderedDict\n\nSCRIPT_DIR = Path(__file__).parent\nOUTPUT_DIR = SCRIPT_DIR\n\n# ============================================================\n# 旧数据（bug 版本 eval）\n# ============================================================\nOLD_DATA = OrderedDict({\n    \"pi05_baseline_s0\": {\"group\": \"Pi0.5 baseline\", \"seed\": 0, \"tsr\": 74.7, \"car\": 26.8, \"ee_disp\": 0.367, \"frozen\": 0.0, \"note\": \"3-seed mean\"},\n    # Pi0.5 baseline 只有 mean±std，没有 per-seed；用 mean 作为单条记录\n    # LoRA-only\n    \"lora_only_s0\":     {\"group\": \"LoRA-only\", \"seed\": 0, \"tsr\": 6.5,  \"car\": 54.5, \"ee_disp\": None, \"frozen\": 0.0},\n    \"lora_only_s1\":     {\"group\": \"LoRA-only\", \"seed\": 1, \"tsr\": 6.0,  \"car\": 56.0, \"ee_disp\": None, \"frozen\": None},\n    # SDF λ=0.005\n    \"sdf_0005_s0\":      {\"group\": \"SDF λ=0.005\", \"seed\": 0, \"tsr\": 4.5, \"car\": 53.5, \"ee_disp\": None, \"frozen\": None},\n    \"sdf_0005_s1\":      {\"group\": \"SDF λ=0.005\", \"seed\": 1, \"tsr\": 9.0, \"car\": 50.0, \"ee_disp\": None, \"frozen\": None},\n    \"sdf_0005_s2\":      {\"group\": \"SDF λ=0.005\", \"seed\": 2, \"tsr\": 7.0, \"car\": 48.0, \"ee_disp\": None, \"frozen\": None},\n    # SDF λ=0.01\n    \"sdf_001_s0\":       {\"group\": \"SDF λ=0.01\", \"seed\": 0, \"tsr\": 8.0, \"car\": 50.0, \"ee_disp\": None, \"frozen\": None},\n    \"sdf_001_s1\":       {\"group\": \"SDF λ=0.01\", \"seed\": 1, \"tsr\": 5.5, \"car\": 55.0, \"ee_disp\": None, \"frozen\": None},\n    \"sdf_001_s2\":       {\"group\": \"SDF λ=0.01\", \"seed\": 2, \"tsr\": 5.0, \"car\": 54.0, \"ee_disp\": None, \"frozen\": None},\n})\n\n# Pi0.5 baseline 旧数据的 std（3-seed）\nOLD_BASELINE_STD = {\"tsr\": 1.5, \"car\": 1.6}\n\n# ============================================================\n# 新数据（修复后 re-eval）— 手动填入或从 JSON 加载\n# key 必须与 OLD_DATA 的 key 一致\n# ============================================================\nNEW_DATA = OrderedDict({\n    \"pi05_baseline_s0\": {\"group\": \"Pi0.5 baseline\", \"seed\": 0, \"tsr\": 71.5, \"car\": 28.5, \"ee_disp\": 0.367, \"frozen\": 0.0, \"note\": \"reeval\"},\n    \"lora_only_s0\":     {\"group\": \"LoRA-only\", \"seed\": 0, \"tsr\": 51.5, \"car\": 56.5, \"ee_disp\": 0.396, \"frozen\": 0.0},\n    # --- 以下待填入 ---\n    # \"lora_only_s1\":     {\"group\": \"LoRA-only\", \"seed\": 1, \"tsr\": ??, \"car\": ??, \"ee_disp\": ??, \"frozen\": ??},\n    # \"sdf_0005_s0\":      {\"group\": \"SDF λ=0.005\", \"seed\": 0, \"tsr\": ??, \"car\": ??, \"ee_disp\": ??, \"frozen\": ??},\n    # \"sdf_0005_s1\":      {\"group\": \"SDF λ=0.005\", \"seed\": 1, \"tsr\": ??, \"car\": ??, \"ee_disp\": ??, \"frozen\": ??},\n    # \"sdf_0005_s2\":      {\"group\": \"SDF λ=0.005\", \"seed\": 2, \"tsr\": ??, \"car\": ??, \"ee_disp\": ??, \"frozen\": ??},\n    # \"sdf_001_s0\":       {\"group\": \"SDF λ=0.01\", \"seed\": 0, \"tsr\": ??, \"car\": ??, \"ee_disp\": ??, \"frozen\": ??},\n    # \"sdf_001_s1\":       {\"group\": \"SDF λ=0.01\", \"seed\": 1, \"tsr\": ??, \"car\": ??, \"ee_disp\": ??, \"frozen\": ??},\n    # \"sdf_001_s2\":       {\"group\": \"SDF λ=0.01\", \"seed\": 2, \"tsr\": ??, \"car\": ??, \"ee_disp\": ??, \"frozen\": ??},\n})\n\n# ============================================================\n# JSON 结果文件路径映射（key -> json path）\n# 根据实际路径修改\n# ============================================================\nJSON_PATHS = {\n    # \"lora_only_s1\": \"/path/to/eval_result.json\",\n    # ...\n}\n\nMETRICS = [\"tsr\", \"car\", \"ee_disp\", \"frozen\"]\nMETRIC_LABELS = {\"tsr\": \"TSR (%)\", \"car\": \"CAR (%)\", \"ee_disp\": \"EE Disp (m)\", \"frozen\": \"Frozen (%)\"}\nGROUPS = [\"Pi0.5 baseline\", \"LoRA-only\", \"SDF λ=0.005\", \"SDF λ=0.01\"]\n\n\ndef load_json_results():\n    \"\"\"从 JSON 文件加载新数据，合并到 NEW_DATA。\"\"\"\n    for key, path in JSON_PATHS.items():\n        if not path or not os.path.exists(path):\n            continue\n        try:\n            with open(path) as f:\n                data = json.load(f)\n            entry = {\"group\": OLD_DATA[key][\"group\"], \"seed\": OLD_DATA[key][\"seed\"]}\n            for m in METRICS:\n                if m in data:\n                    entry[m] = data[m]\n                elif m == \"tsr\" and \"task_success_rate\" in data:\n                    entry[\"tsr\"] = data[\"task_success_rate\"] * 100 if data[\"task_success_rate\"] <= 1 else data[\"task_success_rate\"]\n                elif m == \"car\" and \"collision_avoidance_rate\" in data:\n                    entry[\"car\"] = data[\"collision_avoidance_rate\"] * 100 if data[\"collision_avoidance_rate\"] <= 1 else data[\"collision_avoidance_rate\"]\n            NEW_DATA[key] = entry\n        except Exception as e:\n            print(f\"[WARN] Failed to load {path}: {e}\", file=sys.stderr)\n\n\ndef fmt(val, precision=1):\n    if val is None:\n        return \"—\"\n    return f\"{val:.{precision}f}\"\n\n\ndef fmt_delta(old_val, new_val, precision=1):\n    if old_val is None or new_val is None:\n        return \"—\"\n    d = new_val - old_val\n    sign = \"+\" if d >= 0 else \"\"\n    return f\"{sign}{d:.{precision}f}\"\n\n\ndef group_keys(group_name):\n    return [k for k, v in OLD_DATA.items() if v[\"group\"] == group_name]\n\n\ndef compute_group_stats(data_dict, keys, metric):\n    vals = [data_dict[k][metric] for k in keys if k in data_dict and data_dict[k].get(metric) is not None]\n    if not vals:\n        return None, None\n    return np.mean(vals), np.std(vals) if len(vals) > 1 else 0.0\n\n\n# ============================================================\n# Terminal output\n# ============================================================\ndef print_terminal_table():\n    header = f\"{'Model':<22} {'Old TSR':>8} {'New TSR':>8} {'ΔTSR':>7} {'Old CAR':>8} {'New CAR':>8} {'ΔCAR':>7} {'New EE':>8} {'New Frz':>8}\"\n    sep = \"—\" * len(header)\n    print(\"\\n\" + sep)\n    print(\"  POST-REEVAL COMPARISON: Bug-fix前 vs Bug-fix后\")\n    print(sep)\n    print(header)\n    print(\"—\" * len(header))\n\n    for group in GROUPS:\n        keys = group_keys(group)\n        for k in keys:\n            old = OLD_DATA[k]\n            new = NEW_DATA.get(k)\n            label = f\"{old['group']} s{old['seed']}\"\n            if new:\n                print(f\"{label:<22} {fmt(old['tsr']):>8} {fmt(new['tsr']):>8} {fmt_delta(old['tsr'], new['tsr']):>7} \"\n                      f\"{fmt(old['car']):>8} {fmt(new['car']):>8} {fmt_delta(old['car'], new['car']):>7} \"\n                      f\"{fmt(new.get('ee_disp'), 3):>8} {fmt(new.get('frozen')):>8}\")\n            else:\n                print(f\"{label:<22} {fmt(old['tsr']):>8} {'pending':>8} {'—':>7} \"\n                      f\"{fmt(old['car']):>8} {'pending':>8} {'—':>7} \"\n                      f\"{'pending':>8} {'pending':>8}\")\n\n        # group mean±std\n        if len(keys) > 1:\n            old_tsr_m, old_tsr_s = compute_group_stats(OLD_DATA, keys, \"tsr\")\n            new_tsr_m, new_tsr_s = compute_group_stats(NEW_DATA, keys, \"tsr\")\n            old_car_m, old_car_s = compute_group_stats(OLD_DATA, keys, \"car\")\n            new_car_m, new_car_s = compute_group_stats(NEW_DATA, keys, \"car\")\n\n            old_tsr_str = f\"{fmt(old_tsr_m)}±{fmt(old_tsr_s)}\" if old_tsr_m is not None else \"—\"\n            new_tsr_str = f\"{fmt(new_tsr_m)}±{fmt(new_tsr_s)}\" if new_tsr_m is not None else \"pending\"\n            old_car_str = f\"{fmt(old_car_m)}±{fmt(old_car_s)}\" if old_car_m is not None else \"—\"\n            new_car_str = f\"{fmt(new_car_m)}±{fmt(new_car_s)}\" if new_car_m is not None else \"pending\"\n            delta_tsr_str = fmt_delta(old_tsr_m, new_tsr_m) if (old_tsr_m is not None and new_tsr_m is not None) else \"—\"\n            delta_car_str = fmt_delta(old_car_m, new_car_m) if (old_car_m is not None and new_car_m is not None) else \"—\"\n\n            print(f\"  {'(mean±std)':<20} {old_tsr_str:>8} {new_tsr_str:>8} {delta_tsr_str:>7} \"\n                  f\"{old_car_str:>8} {new_car_str:>8} {delta_car_str:>7}\")\n        print()\n\n    # Summary stats\n    print(sep)\n    print(\"  DELTA SUMMARY (models with both old & new data)\")\n    print(sep)\n    tsr_deltas = []\n    car_deltas = []\n    for k in OLD_DATA:\n        if k in NEW_DATA:\n            old, new = OLD_DATA[k], NEW_DATA[k]\n            if old.get(\"tsr\") is not None and new.get(\"tsr\") is not None:\n                tsr_deltas.append(new[\"tsr\"] - old[\"tsr\"])\n            if old.get(\"car\") is not None and new.get(\"car\") is not None:\n                car_deltas.append(new[\"car\"] - old[\"car\"])\n\n    if tsr_deltas:\n        print(f\"  TSR Δ: mean={np.mean(tsr_deltas):+.1f} pp, min={min(tsr_deltas):+.1f}, max={max(tsr_deltas):+.1f}, n={len(tsr_deltas)}\")\n    if car_deltas:\n        print(f\"  CAR Δ: mean={np.mean(car_deltas):+.1f} pp, min={min(car_deltas):+.1f}, max={max(car_deltas):+.1f}, n={len(car_deltas)}\")\n\n    # Claim 3 analysis\n    print()\n    print(sep)\n    print(\"  CLAIM 3 ANALYSIS\")\n    print(sep)\n    analyze_claim3()\n    print()\n\n\n# ============================================================\n# Claim 3 analysis\n# ============================================================\ndef analyze_claim3():\n    \"\"\"\n    Claim 3 核心结论:\n    a) LoRA-only CAR ≈ SDF CAR (SDF adds no measurable benefit)\n    b) TSR collapse 幅度\n    c) SDF vs LoRA-only CAR 差异是否在 seed variance 内\n    \"\"\"\n    lora_keys = group_keys(\"LoRA-only\")\n    sdf005_keys = group_keys(\"SDF λ=0.005\")\n    sdf001_keys = group_keys(\"SDF λ=0.01\")\n    sdf_keys = sdf005_keys + sdf001_keys\n    baseline_keys = group_keys(\"Pi0.5 baseline\")\n\n    # Use NEW_DATA if available, else OLD_DATA\n    def get_metric_vals(keys, metric, data):\n        return [data[k][metric] for k in keys if k in data and data[k].get(metric) is not None]\n\n    # --- New data analysis ---\n    new_lora_car = get_metric_vals(lora_keys, \"car\", NEW_DATA)\n    new_sdf_car = get_metric_vals(sdf_keys, \"car\", NEW_DATA)\n    new_lora_tsr = get_metric_vals(lora_keys, \"tsr\", NEW_DATA)\n    new_sdf_tsr = get_metric_vals(sdf_keys, \"tsr\", NEW_DATA)\n    new_base_tsr = get_metric_vals(baseline_keys, \"tsr\", NEW_DATA)\n\n    # Old data\n    old_lora_car = get_metric_vals(lora_keys, \"car\", OLD_DATA)\n    old_sdf_car = get_metric_vals(sdf_keys, \"car\", OLD_DATA)\n    old_base_tsr = get_metric_vals(baseline_keys, \"tsr\", OLD_DATA)\n    old_lora_tsr = get_metric_vals(lora_keys, \"tsr\", OLD_DATA)\n    old_sdf_tsr = get_metric_vals(sdf_keys, \"tsr\", OLD_DATA)\n\n    n_new = len(new_lora_car) + len(new_sdf_car)\n    n_total = len(lora_keys) + len(sdf_keys)\n    print(f\"  Data available: {n_new}/{n_total} models have new eval results\")\n\n    if not new_lora_car and not new_sdf_car:\n        print(\"  [INSUFFICIENT DATA] Need re-eval results to assess Claim 3.\")\n        return\n\n    # (a) LoRA-only CAR vs SDF CAR\n    print(f\"\\n  (a) LoRA-only CAR ≈ SDF CAR?\")\n    if new_lora_car:\n        print(f\"      LoRA-only CAR (new): {np.mean(new_lora_car):.1f} ± {np.std(new_lora_car):.1f} (n={len(new_lora_car)})\")\n    if new_sdf_car:\n        print(f\"      SDF CAR (new):       {np.mean(new_sdf_car):.1f} ± {np.std(new_sdf_car):.1f} (n={len(new_sdf_car)})\")\n    if new_lora_car and new_sdf_car:\n        diff = abs(np.mean(new_lora_car) - np.mean(new_sdf_car))\n        pooled_std = np.sqrt((np.var(new_lora_car) + np.var(new_sdf_car)) / 2) if (len(new_lora_car) > 1 or len(new_sdf_car) > 1) else float('nan')\n        print(f\"      |Δ CAR| = {diff:.1f} pp, pooled_std = {pooled_std:.1f}\")\n        if diff < 3.0:\n            print(f\"      → HOLDS: CAR difference ({diff:.1f} pp) is small\")\n        elif not np.isnan(pooled_std) and diff < 2 * pooled_std:\n            print(f\"      → LIKELY HOLDS: difference within 2σ of seed variance\")\n        else:\n            print(f\"      → NEEDS REVIEW: CAR gap ({diff:.1f} pp) may be meaningful\")\n\n    # (b) TSR collapse\n    print(f\"\\n  (b) TSR collapse (fine-tuned vs baseline)?\")\n    if new_base_tsr and (new_lora_tsr or new_sdf_tsr):\n        base_mean = np.mean(new_base_tsr)\n        ft_tsr = new_lora_tsr + new_sdf_tsr\n        ft_mean = np.mean(ft_tsr)\n        drop = base_mean - ft_mean\n        print(f\"      Baseline TSR (new): {base_mean:.1f}\")\n        print(f\"      Fine-tuned TSR (new): {ft_mean:.1f} ± {np.std(ft_tsr):.1f} (n={len(ft_tsr)})\")\n        print(f\"      TSR drop: {drop:.1f} pp\")\n        if old_base_tsr and (old_lora_tsr or old_sdf_tsr):\n            old_ft = old_lora_tsr + old_sdf_tsr\n            old_drop = np.mean(old_base_tsr) - np.mean(old_ft)\n            print(f\"      Old TSR drop was: {old_drop:.1f} pp → New drop: {drop:.1f} pp\")\n    else:\n        print(\"      [INSUFFICIENT DATA]\")\n\n    # (c) SDF vs LoRA-only TSR/CAR within seed variance\n    print(f\"\\n  (c) SDF vs LoRA-only within seed variance?\")\n    for metric_name, lora_vals, sdf_vals in [(\"CAR\", new_lora_car, new_sdf_car), (\"TSR\", new_lora_tsr, new_sdf_tsr)]:\n        if lora_vals and sdf_vals:\n            lm, sm = np.mean(lora_vals), np.mean(sdf_vals)\n            diff = abs(lm - sm)\n            combined = lora_vals + sdf_vals\n            combined_std = np.std(combined)\n            print(f\"      {metric_name}: LoRA={lm:.1f}, SDF={sm:.1f}, |Δ|={diff:.1f}, combined_std={combined_std:.1f}\")\n            if diff < combined_std:\n                print(f\"        → Within 1σ seed variance\")\n            elif diff < 2 * combined_std:\n                print(f\"        → Within 2σ seed variance\")\n            else:\n                print(f\"        → Exceeds 2σ — potentially significant\")\n\n\n# ============================================================\n# LaTeX table\n# ============================================================\ndef generate_latex():\n    lines = []\n    lines.append(r\"\\begin{table}[t]\")\n    lines.append(r\"\\centering\")\n    lines.append(r\"\\caption{Evaluation results before and after fixing the 180° image rotation bug in \\texttt{eval\\_safelibero.py}.}\")\n    lines.append(r\"\\label{tab:reeval_comparison}\")\n    lines.append(r\"\\resizebox{\\textwidth}{!}{\")\n    lines.append(r\"\\begin{tabular}{l c c c c c c c}\")\n    lines.append(r\"\\toprule\")\n    lines.append(r\"Model & \\multicolumn{2}{c}{TSR (\\%)} & $\\Delta$TSR & \\multicolumn{2}{c}{CAR (\\%)} & $\\Delta$CAR & EE Disp (m) \\\\\")\n    lines.append(r\"\\cmidrule(lr){2-3} \\cmidrule(lr){5-6}\")\n    lines.append(r\" & Before & After & (pp) & Before & After & (pp) & (After) \\\\\")\n    lines.append(r\"\\midrule\")\n\n    for gi, group in enumerate(GROUPS):\n        keys = group_keys(group)\n        if gi > 0:\n            lines.append(r\"\\addlinespace\")\n\n        for k in keys:\n            old = OLD_DATA[k]\n            new = NEW_DATA.get(k)\n            label = f\"{old['group']} s{old['seed']}\"\n            label_tex = label.replace(\"λ\", r\"$\\lambda$\").replace(\"±\", r\"$\\pm$\")\n\n            if new:\n                dt = fmt_delta(old[\"tsr\"], new[\"tsr\"])\n                dc = fmt_delta(old[\"car\"], new[\"car\"])\n                ee = fmt(new.get(\"ee_disp\"), 3)\n                lines.append(f\"{label_tex} & {fmt(old['tsr'])} & {fmt(new['tsr'])} & {dt} & {fmt(old['car'])} & {fmt(new['car'])} & {dc} & {ee} \\\\\\\\\")\n            else:\n                lines.append(f\"{label_tex} & {fmt(old['tsr'])} & — & — & {fmt(old['car'])} & — & — & — \\\\\\\\\")\n\n        # group mean\n        if len(keys) > 1:\n            old_tsr_m, old_tsr_s = compute_group_stats(OLD_DATA, keys, \"tsr\")\n            new_tsr_m, new_tsr_s = compute_group_stats(NEW_DATA, keys, \"tsr\")\n            old_car_m, old_car_s = compute_group_stats(OLD_DATA, keys, \"car\")\n            new_car_m, new_car_s = compute_group_stats(NEW_DATA, keys, \"car\")\n\n            old_tsr_str = f\"{fmt(old_tsr_m)}$\\\\pm${fmt(old_tsr_s)}\" if old_tsr_m is not None else \"—\"\n            new_tsr_str = f\"{fmt(new_tsr_m)}$\\\\pm${fmt(new_tsr_s)}\" if new_tsr_m is not None else \"—\"\n            old_car_str = f\"{fmt(old_car_m)}$\\\\pm${fmt(old_car_s)}\" if old_car_m is not None else \"—\"\n            new_car_str = f\"{fmt(new_car_m)}$\\\\pm${fmt(new_car_s)}\" if new_car_m is not None else \"—\"\n            dt = fmt_delta(old_tsr_m, new_tsr_m) if (old_tsr_m is not None and new_tsr_m is not None) else \"—\"\n            dc = fmt_delta(old_car_m, new_car_m) if (old_car_m is not None and new_car_m is not None) else \"—\"\n\n            group_tex = group.replace(\"λ\", r\"$\\lambda$\")\n            lines.append(f\"\\\\rowcolor{{gray!15}} \\\\textit{{{group_tex} mean}} & {old_tsr_str} & {new_tsr_str} & {dt} & {old_car_str} & {new_car_str} & {dc} & \\\\\\\\\")\n\n    lines.append(r\"\\bottomrule\")\n    lines.append(r\"\\end{tabular}}\")\n    lines.append(r\"\\end{table}\")\n\n    tex_content = \"\\n\".join(lines)\n    out_path = OUTPUT_DIR / \"reeval_comparison.tex\"\n    with open(out_path, \"w\") as f:\n        f.write(tex_content)\n    print(f\"LaTeX table saved to {out_path}\")\n    return tex_content\n\n\n# ============================================================\n# JSON summary\n# ============================================================\ndef generate_json_summary():\n    summary = {\n        \"description\": \"Post-reeval comparison: 180° rotation bug fix\",\n        \"old_data\": {k: {m: v.get(m) for m in METRICS} for k, v in OLD_DATA.items()},\n        \"new_data\": {k: {m: v.get(m) for m in METRICS} for k, v in NEW_DATA.items()},\n        \"deltas\": {},\n        \"group_stats\": {},\n        \"claim3\": {},\n    }\n\n    # Per-model deltas\n    for k in OLD_DATA:\n        if k in NEW_DATA:\n            old, new = OLD_DATA[k], NEW_DATA[k]\n            d = {}\n            for m in METRICS:\n                if old.get(m) is not None and new.get(m) is not None:\n                    d[m] = round(new[m] - old[m], 3)\n            summary[\"deltas\"][k] = d\n\n    # Group stats\n    for group in GROUPS:\n        keys = group_keys(group)\n        gs = {}\n        for data_name, data_dict in [(\"old\", OLD_DATA), (\"new\", NEW_DATA)]:\n            for m in [\"tsr\", \"car\"]:\n                mean, std = compute_group_stats(data_dict, keys, m)\n                if mean is not None:\n                    gs[f\"{data_name}_{m}_mean\"] = round(mean, 2)\n                    gs[f\"{data_name}_{m}_std\"] = round(std, 2)\n        summary[\"group_stats\"][group] = gs\n\n    # Claim 3 assessment\n    lora_keys = group_keys(\"LoRA-only\")\n    sdf_keys = group_keys(\"SDF λ=0.005\") + group_keys(\"SDF λ=0.01\")\n    new_lora_car = [NEW_DATA[k][\"car\"] for k in lora_keys if k in NEW_DATA and NEW_DATA[k].get(\"car\") is not None]\n    new_sdf_car = [NEW_DATA[k][\"car\"] for k in sdf_keys if k in NEW_DATA and NEW_DATA[k].get(\"car\") is not None]\n\n    claim3 = {\"data_complete\": len(new_lora_car) + len(new_sdf_car) == len(lora_keys) + len(sdf_keys)}\n    if new_lora_car and new_sdf_car:\n        claim3[\"lora_car_mean\"] = round(np.mean(new_lora_car), 2)\n        claim3[\"sdf_car_mean\"] = round(np.mean(new_sdf_car), 2)\n        claim3[\"car_gap_pp\"] = round(abs(np.mean(new_lora_car) - np.mean(new_sdf_car)), 2)\n    summary[\"claim3\"] = claim3\n\n    # Completion status\n    summary[\"completion\"] = {\n        \"total_models\": len(OLD_DATA),\n        \"reeval_done\": len(NEW_DATA),\n        \"pending\": [k for k in OLD_DATA if k not in NEW_DATA],\n    }\n\n    out_path = OUTPUT_DIR / \"reeval_comparison.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(summary, f, indent=2, ensure_ascii=False)\n    print(f\"JSON summary saved to {out_path}\")\n    return summary\n\n\n# ============================================================\n# Main\n# ============================================================\ndef main():\n    load_json_results()\n\n    print_terminal_table()\n    generate_latex()\n    generate_json_summary()\n\n    n_done = len(NEW_DATA)\n    n_total = len(OLD_DATA)\n    print(f\"\\nCompletion: {n_done}/{n_total} models re-evaluated\")\n    if n_done < n_total:\n        pending = [k for k in OLD_DATA if k not in NEW_DATA]\n        print(f\"Pending: {', '.join(pending)}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_post_reeval_analysis_script_20260526T092833",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/reeval_comparison.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nPost-reeval comparison: bug-fix前 vs bug-fix后 eval 结果对比分析。\n\n背景: eval_safelibero.py 存在 180° 图像旋转 bug（缺少 [::-1, ::-1]），\n导致所有通过该脚本评估的模型 TSR 被严重低估。本脚本对比修复前后结果。\n\n输入:\n  - 硬编码的旧数据 (OLD_DATA)\n  - JSON 结果文件 或 手动填入的新数据 (NEW_DATA dict)\n输出:\n  - Terminal formatted table\n  - LaTeX table (.tex)\n  - JSON summary (.json)\n\"\"\"\n\nimport json\nimport sys\nimport os\nimport glob\nimport numpy as np\nfrom pathlib import Path\nfrom collections import OrderedDict\n\nSCRIPT_DIR = Path(__file__).parent\nOUTPUT_DIR = SCRIPT_DIR\n\n# ============================================================\n# 旧数据（bug 版本 eval）\n# ============================================================\nOLD_DATA = OrderedDict({\n    \"pi05_baseline_s0\": {\"group\": \"Pi0.5 baseline\", \"seed\": 0, \"tsr\": 74.7, \"car\": 26.8, \"ee_disp\": 0.367, \"frozen\": 0.0, \"note\": \"3-seed mean\"},\n    # Pi0.5 baseline 只有 mean±std，没有 per-seed；用 mean 作为单条记录\n    # LoRA-only\n    \"lora_only_s0\":     {\"group\": \"LoRA-only\", \"seed\": 0, \"tsr\": 6.5,  \"car\": 54.5, \"ee_disp\": None, \"frozen\": 0.0},\n    \"lora_only_s1\":     {\"group\": \"LoRA-only\", \"seed\": 1, \"tsr\": 6.0,  \"car\": 56.0, \"ee_disp\": None, \"frozen\": None},\n    # SDF λ=0.005\n    \"sdf_0005_s0\":      {\"group\": \"SDF λ=0.005\", \"seed\": 0, \"tsr\": 4.5, \"car\": 53.5, \"ee_disp\": None, \"frozen\": None},\n    \"sdf_0005_s1\":      {\"group\": \"SDF λ=0.005\", \"seed\": 1, \"tsr\": 9.0, \"car\": 50.0, \"ee_disp\": None, \"frozen\": None},\n    \"sdf_0005_s2\":      {\"group\": \"SDF λ=0.005\", \"seed\": 2, \"tsr\": 7.0, \"car\": 48.0, \"ee_disp\": None, \"frozen\": None},\n    # SDF λ=0.01\n    \"sdf_001_s0\":       {\"group\": \"SDF λ=0.01\", \"seed\": 0, \"tsr\": 8.0, \"car\": 50.0, \"ee_disp\": None, \"frozen\": None},\n    \"sdf_001_s1\":       {\"group\": \"SDF λ=0.01\", \"seed\": 1, \"tsr\": 5.5, \"car\": 55.0, \"ee_disp\": None, \"frozen\": None},\n    \"sdf_001_s2\":       {\"group\": \"SDF λ=0.01\", \"seed\": 2, \"tsr\": 5.0, \"car\": 54.0, \"ee_disp\": None, \"frozen\": None},\n})\n\n# Pi0.5 baseline 旧数据的 std（3-seed）\nOLD_BASELINE_STD = {\"tsr\": 1.5, \"car\": 1.6}\n\n# ============================================================\n# 新数据（修复后 re-eval）— 手动填入或从 JSON 加载\n# key 必须与 OLD_DATA 的 key 一致\n# ============================================================\nNEW_DATA = OrderedDict({\n    \"pi05_baseline_s0\": {\"group\": \"Pi0.5 baseline\", \"seed\": 0, \"tsr\": 71.5, \"car\": 28.5, \"ee_disp\": 0.367, \"frozen\": 0.0, \"note\": \"reeval\"},\n    \"lora_only_s0\":     {\"group\": \"LoRA-only\", \"seed\": 0, \"tsr\": 51.5, \"car\": 56.5, \"ee_disp\": 0.396, \"frozen\": 0.0},\n    # --- 以下待填入 ---\n    # \"lora_only_s1\":     {\"group\": \"LoRA-only\", \"seed\": 1, \"tsr\": ??, \"car\": ??, \"ee_disp\": ??, \"frozen\": ??},\n    # \"sdf_0005_s0\":      {\"group\": \"SDF λ=0.005\", \"seed\": 0, \"tsr\": ??, \"car\": ??, \"ee_disp\": ??, \"frozen\": ??},\n    # \"sdf_0005_s1\":      {\"group\": \"SDF λ=0.005\", \"seed\": 1, \"tsr\": ??, \"car\": ??, \"ee_disp\": ??, \"frozen\": ??},\n    # \"sdf_0005_s2\":      {\"group\": \"SDF λ=0.005\", \"seed\": 2, \"tsr\": ??, \"car\": ??, \"ee_disp\": ??, \"frozen\": ??},\n    # \"sdf_001_s0\":       {\"group\": \"SDF λ=0.01\", \"seed\": 0, \"tsr\": ??, \"car\": ??, \"ee_disp\": ??, \"frozen\": ??},\n    # \"sdf_001_s1\":       {\"group\": \"SDF λ=0.01\", \"seed\": 1, \"tsr\": ??, \"car\": ??, \"ee_disp\": ??, \"frozen\": ??},\n    # \"sdf_001_s2\":       {\"group\": \"SDF λ=0.01\", \"seed\": 2, \"tsr\": ??, \"car\": ??, \"ee_disp\": ??, \"frozen\": ??},\n})\n\n# ============================================================\n# JSON 结果文件路径映射（key -> json path）\n# 根据实际路径修改\n# ============================================================\nJSON_PATHS = {\n    # \"lora_only_s1\": \"/path/to/eval_result.json\",\n    # ...\n}\n\nMETRICS = [\"tsr\", \"car\", \"ee_disp\", \"frozen\"]\nMETRIC_LABELS = {\"tsr\": \"TSR (%)\", \"car\": \"CAR (%)\", \"ee_disp\": \"EE Disp (m)\", \"frozen\": \"Frozen (%)\"}\nGROUPS = [\"Pi0.5 baseline\", \"LoRA-only\", \"SDF λ=0.005\", \"SDF λ=0.01\"]\n\n\ndef load_json_results():\n    \"\"\"从 JSON 文件加载新数据，合并到 NEW_DATA。\"\"\"\n    for key, path in JSON_PATHS.items():\n        if not path or not os.path.exists(path):\n            continue\n        try:\n            with open(path) as f:\n                data = json.load(f)\n            entry = {\"group\": OLD_DATA[key][\"group\"], \"seed\": OLD_DATA[key][\"seed\"]}\n            for m in METRICS:\n                if m in data:\n                    entry[m] = data[m]\n                elif m == \"tsr\" and \"task_success_rate\" in data:\n                    entry[\"tsr\"] = data[\"task_success_rate\"] * 100 if data[\"task_success_rate\"] <= 1 else data[\"task_success_rate\"]\n                elif m == \"car\" and \"collision_avoidance_rate\" in data:\n                    entry[\"car\"] = data[\"collision_avoidance_rate\"] * 100 if data[\"collision_avoidance_rate\"] <= 1 else data[\"collision_avoidance_rate\"]\n            NEW_DATA[key] = entry\n        except Exception as e:\n            print(f\"[WARN] Failed to load {path}: {e}\", file=sys.stderr)\n\n\ndef fmt(val, precision=1):\n    if val is None:\n        return \"—\"\n    return f\"{val:.{precision}f}\"\n\n\ndef fmt_delta(old_val, new_val, precision=1):\n    if old_val is None or new_val is None:\n        return \"—\"\n    d = new_val - old_val\n    sign = \"+\" if d >= 0 else \"\"\n    return f\"{sign}{d:.{precision}f}\"\n\n\ndef group_keys(group_name):\n    return [k for k, v in OLD_DATA.items() if v[\"group\"] == group_name]\n\n\ndef compute_group_stats(data_dict, keys, metric):\n    vals = [data_dict[k][metric] for k in keys if k in data_dict and data_dict[k].get(metric) is not None]\n    if not vals:\n        return None, None\n    return np.mean(vals), np.std(vals) if len(vals) > 1 else 0.0\n\n\n# ============================================================\n# Terminal output\n# ============================================================\ndef print_terminal_table():\n    header = f\"{'Model':<22} {'Old TSR':>8} {'New TSR':>8} {'ΔTSR':>7} {'Old CAR':>8} {'New CAR':>8} {'ΔCAR':>7} {'New EE':>8} {'New Frz':>8}\"\n    sep = \"—\" * len(header)\n    print(\"\\n\" + sep)\n    print(\"  POST-REEVAL COMPARISON: Bug-fix前 vs Bug-fix后\")\n    print(sep)\n    print(header)\n    print(\"—\" * len(header))\n\n    for group in GROUPS:\n        keys = group_keys(group)\n        for k in keys:\n            old = OLD_DATA[k]\n            new = NEW_DATA.get(k)\n            label = f\"{old['group']} s{old['seed']}\"\n            if new:\n                print(f\"{label:<22} {fmt(old['tsr']):>8} {fmt(new['tsr']):>8} {fmt_delta(old['tsr'], new['tsr']):>7} \"\n                      f\"{fmt(old['car']):>8} {fmt(new['car']):>8} {fmt_delta(old['car'], new['car']):>7} \"\n                      f\"{fmt(new.get('ee_disp'), 3):>8} {fmt(new.get('frozen')):>8}\")\n            else:\n                print(f\"{label:<22} {fmt(old['tsr']):>8} {'pending':>8} {'—':>7} \"\n                      f\"{fmt(old['car']):>8} {'pending':>8} {'—':>7} \"\n                      f\"{'pending':>8} {'pending':>8}\")\n\n        # group mean±std\n        if len(keys) > 1:\n            old_tsr_m, old_tsr_s = compute_group_stats(OLD_DATA, keys, \"tsr\")\n            new_tsr_m, new_tsr_s = compute_group_stats(NEW_DATA, keys, \"tsr\")\n            old_car_m, old_car_s = compute_group_stats(OLD_DATA, keys, \"car\")\n            new_car_m, new_car_s = compute_group_stats(NEW_DATA, keys, \"car\")\n\n            old_tsr_str = f\"{fmt(old_tsr_m)}±{fmt(old_tsr_s)}\" if old_tsr_m is not None else \"—\"\n            new_tsr_str = f\"{fmt(new_tsr_m)}±{fmt(new_tsr_s)}\" if new_tsr_m is not None else \"pending\"\n            old_car_str = f\"{fmt(old_car_m)}±{fmt(old_car_s)}\" if old_car_m is not None else \"—\"\n            new_car_str = f\"{fmt(new_car_m)}±{fmt(new_car_s)}\" if new_car_m is not None else \"pending\"\n            delta_tsr_str = fmt_delta(old_tsr_m, new_tsr_m) if (old_tsr_m is not None and new_tsr_m is not None) else \"—\"\n            delta_car_str = fmt_delta(old_car_m, new_car_m) if (old_car_m is not None and new_car_m is not None) else \"—\"\n\n            print(f\"  {'(mean±std)':<20} {old_tsr_str:>8} {new_tsr_str:>8} {delta_tsr_str:>7} \"\n                  f\"{old_car_str:>8} {new_car_str:>8} {delta_car_str:>7}\")\n        print()\n\n    # Summary stats\n    print(sep)\n    print(\"  DELTA SUMMARY (models with both old & new data)\")\n    print(sep)\n    tsr_deltas = []\n    car_deltas = []\n    for k in OLD_DATA:\n        if k in NEW_DATA:\n            old, new = OLD_DATA[k], NEW_DATA[k]\n            if old.get(\"tsr\") is not None and new.get(\"tsr\") is not None:\n                tsr_deltas.append(new[\"tsr\"] - old[\"tsr\"])\n            if old.get(\"car\") is not None and new.get(\"car\") is not None:\n                car_deltas.append(new[\"car\"] - old[\"car\"])\n\n    if tsr_deltas:\n        print(f\"  TSR Δ: mean={np.mean(tsr_deltas):+.1f} pp, min={min(tsr_deltas):+.1f}, max={max(tsr_deltas):+.1f}, n={len(tsr_deltas)}\")\n    if car_deltas:\n        print(f\"  CAR Δ: mean={np.mean(car_deltas):+.1f} pp, min={min(car_deltas):+.1f}, max={max(car_deltas):+.1f}, n={len(car_deltas)}\")\n\n    # Claim 3 analysis\n    print()\n    print(sep)\n    print(\"  CLAIM 3 ANALYSIS\")\n    print(sep)\n    analyze_claim3()\n    print()\n\n\n# ============================================================\n# Claim 3 analysis\n# ============================================================\ndef analyze_claim3():\n    \"\"\"\n    Claim 3 核心结论:\n    a) LoRA-only CAR ≈ SDF CAR (SDF adds no measurable benefit)\n    b) TSR collapse 幅度\n    c) SDF vs LoRA-only CAR 差异是否在 seed variance 内\n    \"\"\"\n    lora_keys = group_keys(\"LoRA-only\")\n    sdf005_keys = group_keys(\"SDF λ=0.005\")\n    sdf001_keys = group_keys(\"SDF λ=0.01\")\n    sdf_keys = sdf005_keys + sdf001_keys\n    baseline_keys = group_keys(\"Pi0.5 baseline\")\n\n    # Use NEW_DATA if available, else OLD_DATA\n    def get_metric_vals(keys, metric, data):\n        return [data[k][metric] for k in keys if k in data and data[k].get(metric) is not None]\n\n    # --- New data analysis ---\n    new_lora_car = get_metric_vals(lora_keys, \"car\", NEW_DATA)\n    new_sdf_car = get_metric_vals(sdf_keys, \"car\", NEW_DATA)\n    new_lora_tsr = get_metric_vals(lora_keys, \"tsr\", NEW_DATA)\n    new_sdf_tsr = get_metric_vals(sdf_keys, \"tsr\", NEW_DATA)\n    new_base_tsr = get_metric_vals(baseline_keys, \"tsr\", NEW_DATA)\n\n    # Old data\n    old_lora_car = get_metric_vals(lora_keys, \"car\", OLD_DATA)\n    old_sdf_car = get_metric_vals(sdf_keys, \"car\", OLD_DATA)\n    old_base_tsr = get_metric_vals(baseline_keys, \"tsr\", OLD_DATA)\n    old_lora_tsr = get_metric_vals(lora_keys, \"tsr\", OLD_DATA)\n    old_sdf_tsr = get_metric_vals(sdf_keys, \"tsr\", OLD_DATA)\n\n    n_new = len(new_lora_car) + len(new_sdf_car)\n    n_total = len(lora_keys) + len(sdf_keys)\n    print(f\"  Data available: {n_new}/{n_total} models have new eval results\")\n\n    if not new_lora_car and not new_sdf_car:\n        print(\"  [INSUFFICIENT DATA] Need re-eval results to assess Claim 3.\")\n        return\n\n    # (a) LoRA-only CAR vs SDF CAR\n    print(f\"\\n  (a) LoRA-only CAR ≈ SDF CAR?\")\n    if new_lora_car:\n        print(f\"      LoRA-only CAR (new): {np.mean(new_lora_car):.1f} ± {np.std(new_lora_car):.1f} (n={len(new_lora_car)})\")\n    if new_sdf_car:\n        print(f\"      SDF CAR (new):       {np.mean(new_sdf_car):.1f} ± {np.std(new_sdf_car):.1f} (n={len(new_sdf_car)})\")\n    if new_lora_car and new_sdf_car:\n        diff = abs(np.mean(new_lora_car) - np.mean(new_sdf_car))\n        pooled_std = np.sqrt((np.var(new_lora_car) + np.var(new_sdf_car)) / 2) if (len(new_lora_car) > 1 or len(new_sdf_car) > 1) else float('nan')\n        print(f\"      |Δ CAR| = {diff:.1f} pp, pooled_std = {pooled_std:.1f}\")\n        if diff < 3.0:\n            print(f\"      → HOLDS: CAR difference ({diff:.1f} pp) is small\")\n        elif not np.isnan(pooled_std) and diff < 2 * pooled_std:\n            print(f\"      → LIKELY HOLDS: difference within 2σ of seed variance\")\n        else:\n            print(f\"      → NEEDS REVIEW: CAR gap ({diff:.1f} pp) may be meaningful\")\n\n    # (b) TSR collapse\n    print(f\"\\n  (b) TSR collapse (fine-tuned vs baseline)?\")\n    if new_base_tsr and (new_lora_tsr or new_sdf_tsr):\n        base_mean = np.mean(new_base_tsr)\n        ft_tsr = new_lora_tsr + new_sdf_tsr\n        ft_mean = np.mean(ft_tsr)\n        drop = base_mean - ft_mean\n        print(f\"      Baseline TSR (new): {base_mean:.1f}\")\n        print(f\"      Fine-tuned TSR (new): {ft_mean:.1f} ± {np.std(ft_tsr):.1f} (n={len(ft_tsr)})\")\n        print(f\"      TSR drop: {drop:.1f} pp\")\n        if old_base_tsr and (old_lora_tsr or old_sdf_tsr):\n            old_ft = old_lora_tsr + old_sdf_tsr\n            old_drop = np.mean(old_base_tsr) - np.mean(old_ft)\n            print(f\"      Old TSR drop was: {old_drop:.1f} pp → New drop: {drop:.1f} pp\")\n    else:\n        print(\"      [INSUFFICIENT DATA]\")\n\n    # (c) SDF vs LoRA-only TSR/CAR within seed variance\n    print(f\"\\n  (c) SDF vs LoRA-only within seed variance?\")\n    for metric_name, lora_vals, sdf_vals in [(\"CAR\", new_lora_car, new_sdf_car), (\"TSR\", new_lora_tsr, new_sdf_tsr)]:\n        if lora_vals and sdf_vals:\n            lm, sm = np.mean(lora_vals), np.mean(sdf_vals)\n            diff = abs(lm - sm)\n            combined = lora_vals + sdf_vals\n            combined_std = np.std(combined)\n            print(f\"      {metric_name}: LoRA={lm:.1f}, SDF={sm:.1f}, |Δ|={diff:.1f}, combined_std={combined_std:.1f}\")\n            if diff < combined_std:\n                print(f\"        → Within 1σ seed variance\")\n            elif diff < 2 * combined_std:\n                print(f\"        → Within 2σ seed variance\")\n            else:\n                print(f\"        → Exceeds 2σ — potentially significant\")\n\n\n# ============================================================\n# LaTeX table\n# ============================================================\ndef generate_latex():\n    lines = []\n    lines.append(r\"\\begin{table}[t]\")\n    lines.append(r\"\\centering\")\n    lines.append(r\"\\caption{Evaluation results before and after fixing the 180° image rotation bug in \\texttt{eval\\_safelibero.py}.}\")\n    lines.append(r\"\\label{tab:reeval_comparison}\")\n    lines.append(r\"\\resizebox{\\textwidth}{!}{\")\n    lines.append(r\"\\begin{tabular}{l c c c c c c c}\")\n    lines.append(r\"\\toprule\")\n    lines.append(r\"Model & \\multicolumn{2}{c}{TSR (\\%)} & $\\Delta$TSR & \\multicolumn{2}{c}{CAR (\\%)} & $\\Delta$CAR & EE Disp (m) \\\\\")\n    lines.append(r\"\\cmidrule(lr){2-3} \\cmidrule(lr){5-6}\")\n    lines.append(r\" & Before & After & (pp) & Before & After & (pp) & (After) \\\\\")\n    lines.append(r\"\\midrule\")\n\n    for gi, group in enumerate(GROUPS):\n        keys = group_keys(group)\n        if gi > 0:\n            lines.append(r\"\\addlinespace\")\n\n        for k in keys:\n            old = OLD_DATA[k]\n            new = NEW_DATA.get(k)\n            label = f\"{old['group']} s{old['seed']}\"\n            label_tex = label.replace(\"λ\", r\"$\\lambda$\").replace(\"±\", r\"$\\pm$\")\n\n            if new:\n                dt = fmt_delta(old[\"tsr\"], new[\"tsr\"])\n                dc = fmt_delta(old[\"car\"], new[\"car\"])\n                ee = fmt(new.get(\"ee_disp\"), 3)\n                lines.append(f\"{label_tex} & {fmt(old['tsr'])} & {fmt(new['tsr'])} & {dt} & {fmt(old['car'])} & {fmt(new['car'])} & {dc} & {ee} \\\\\\\\\")\n            else:\n                lines.append(f\"{label_tex} & {fmt(old['tsr'])} & — & — & {fmt(old['car'])} & — & — & — \\\\\\\\\")\n\n        # group mean\n        if len(keys) > 1:\n            old_tsr_m, old_tsr_s = compute_group_stats(OLD_DATA, keys, \"tsr\")\n            new_tsr_m, new_tsr_s = compute_group_stats(NEW_DATA, keys, \"tsr\")\n            old_car_m, old_car_s = compute_group_stats(OLD_DATA, keys, \"car\")\n            new_car_m, new_car_s = compute_group_stats(NEW_DATA, keys, \"car\")\n\n            old_tsr_str = f\"{fmt(old_tsr_m)}$\\\\pm${fmt(old_tsr_s)}\" if old_tsr_m is not None else \"—\"\n            new_tsr_str = f\"{fmt(new_tsr_m)}$\\\\pm${fmt(new_tsr_s)}\" if new_tsr_m is not None else \"—\"\n            old_car_str = f\"{fmt(old_car_m)}$\\\\pm${fmt(old_car_s)}\" if old_car_m is not None else \"—\"\n            new_car_str = f\"{fmt(new_car_m)}$\\\\pm${fmt(new_car_s)}\" if new_car_m is not None else \"—\"\n            dt = fmt_delta(old_tsr_m, new_tsr_m) if (old_tsr_m is not None and new_tsr_m is not None) else \"—\"\n            dc = fmt_delta(old_car_m, new_car_m) if (old_car_m is not None and new_car_m is not None) else \"—\"\n\n            group_tex = group.replace(\"λ\", r\"$\\lambda$\")\n            lines.append(f\"\\\\rowcolor{{gray!15}} \\\\textit{{{group_tex} mean}} & {old_tsr_str} & {new_tsr_str} & {dt} & {old_car_str} & {new_car_str} & {dc} & \\\\\\\\\")\n\n    lines.append(r\"\\bottomrule\")\n    lines.append(r\"\\end{tabular}}\")\n    lines.append(r\"\\end{table}\")\n\n    tex_content = \"\\n\".join(lines)\n    out_path = OUTPUT_DIR / \"reeval_comparison.tex\"\n    with open(out_path, \"w\") as f:\n        f.write(tex_content)\n    print(f\"LaTeX table saved to {out_path}\")\n    return tex_content\n\n\n# ============================================================\n# JSON summary\n# ============================================================\ndef generate_json_summary():\n    summary = {\n        \"description\": \"Post-reeval comparison: 180° rotation bug fix\",\n        \"old_data\": {k: {m: v.get(m) for m in METRICS} for k, v in OLD_DATA.items()},\n        \"new_data\": {k: {m: v.get(m) for m in METRICS} for k, v in NEW_DATA.items()},\n        \"deltas\": {},\n        \"group_stats\": {},\n        \"claim3\": {},\n    }\n\n    # Per-model deltas\n    for k in OLD_DATA:\n        if k in NEW_DATA:\n            old, new = OLD_DATA[k], NEW_DATA[k]\n            d = {}\n            for m in METRICS:\n                if old.get(m) is not None and new.get(m) is not None:\n                    d[m] = round(new[m] - old[m], 3)\n            summary[\"deltas\"][k] = d\n\n    # Group stats\n    for group in GROUPS:\n        keys = group_keys(group)\n        gs = {}\n        for data_name, data_dict in [(\"old\", OLD_DATA), (\"new\", NEW_DATA)]:\n            for m in [\"tsr\", \"car\"]:\n                mean, std = compute_group_stats(data_dict, keys, m)\n                if mean is not None:\n                    gs[f\"{data_name}_{m}_mean\"] = round(mean, 2)\n                    gs[f\"{data_name}_{m}_std\"] = round(std, 2)\n        summary[\"group_stats\"][group] = gs\n\n    # Claim 3 assessment\n    lora_keys = group_keys(\"LoRA-only\")\n    sdf_keys = group_keys(\"SDF λ=0.005\") + group_keys(\"SDF λ=0.01\")\n    new_lora_car = [NEW_DATA[k][\"car\"] for k in lora_keys if k in NEW_DATA and NEW_DATA[k].get(\"car\") is not None]\n    new_sdf_car = [NEW_DATA[k][\"car\"] for k in sdf_keys if k in NEW_DATA and NEW_DATA[k].get(\"car\") is not None]\n\n    claim3 = {\"data_complete\": len(new_lora_car) + len(new_sdf_car) == len(lora_keys) + len(sdf_keys)}\n    if new_lora_car and new_sdf_car:\n        claim3[\"lora_car_mean\"] = round(np.mean(new_lora_car), 2)\n        claim3[\"sdf_car_mean\"] = round(np.mean(new_sdf_car), 2)\n        claim3[\"car_gap_pp\"] = round(abs(np.mean(new_lora_car) - np.mean(new_sdf_car)), 2)\n    summary[\"claim3\"] = claim3\n\n    # Completion status\n    summary[\"completion\"] = {\n        \"total_models\": len(OLD_DATA),\n        \"reeval_done\": len(NEW_DATA),\n        \"pending\": [k for k in OLD_DATA if k not in NEW_DATA],\n    }\n\n    out_path = OUTPUT_DIR / \"reeval_comparison.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(summary, f, indent=2, ensure_ascii=False)\n    print(f\"JSON summary saved to {out_path}\")\n    return summary\n\n\n# ============================================================\n# Main\n# ============================================================\ndef main():\n    load_json_results()\n\n    print_terminal_table()\n    generate_latex()\n    generate_json_summary()\n\n    n_done = len(NEW_DATA)\n    n_total = len(OLD_DATA)\n    print(f\"\\nCompletion: {n_done}/{n_total} models re-evaluated\")\n    if n_done < n_total:\n        pending = [k for k in OLD_DATA if k not in NEW_DATA]\n        print(f\"Pending: {', '.join(pending)}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T09:30:27.929335+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/reeval_comparison.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_post_reeval_analysis_script_20260526T092833",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T09:30:27.929547+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts && python reeval_comparison.py",
  "description": "Run reeval comparison script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_post_reeval_analysis_script_20260526T092833",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts && python reeval_comparison.py",
    "description": "Run reeval comparison script"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T09:30:27.929690+00:00_

Exit code 127
/bin/bash: line 1: python: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_post_reeval_analysis_script_20260526T092833",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T09:30:27.929818+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts && python3 reeval_comparison.py",
  "description": "Run reeval comparison script with python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_post_reeval_analysis_script_20260526T092833",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts && python3 reeval_comparison.py",
    "description": "Run reeval comparison script with python3"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T09:30:27.929971+00:00_

————————————————————————————————————————————————————————————————————————————————————————————
  POST-REEVAL COMPARISON: Bug-fix前 vs Bug-fix后
————————————————————————————————————————————————————————————————————————————————————————————
Model                   Old TSR  New TSR    ΔTSR  Old CAR  New CAR    ΔCAR   New EE  New Frz
————————————————————————————————————————————————————————————————————————————————————————————
Pi0.5 baseline s0          74.7     71.5    -3.2     26.8     28.5    +1.7    0.367      0.0

LoRA-only s0                6.5     51.5   +45.0     54.5     56.5    +2.0    0.396      0.0
LoRA-only s1                6.0  pending       —     56.0  pending       —  pending  pending
  (mean±std)            6.2±0.2 51.5±0.0   +45.2 55.2±0.8 56.5±0.0    +1.2

SDF λ=0.005 s0              4.5  pending       —     53.5  pending       —  pending  pending
SDF λ=0.005 s1              9.0  pending       —     50.0  pending       —  pending  pending
SDF λ=0.005 s2              7.0  pending       —     48.0  pending       —  pending  pending
  (mean±std)            6.8±1.8  pending       — 50.5±2.3  pending       —

SDF λ=0.01 s0               8.0  pending       —     50.0  pending       —  pending  pending
SDF λ=0.01 s1               5.5  pending       —     55.0  pending       —  pending  pending
SDF λ=0.01 s2               5.0  pending       —     54.0  pending       —  pending  pending
  (mean±std)            6.2±1.3  pending       — 53.0±2.2  pending       —

————————————————————————————————————————————————————————————————————————————————————————————
  DELTA SUMMARY (models with both old & new data)
————————————————————————————————————————————————————————————————————————————————————————————
  TSR Δ: mean=+20.9 pp, min=-3.2, max=+45.0, n=2
  CAR Δ: mean=+1.8 pp, min=+1.7, max=+2.0, n=2

————————————————————————————————————————————————————————————————————————————————————————————
  CLAIM 3 ANALYSIS
——————————————————————————————————————————————————————————————————————
…[truncated 790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_post_reeval_analysis_script_20260526T092833",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-26T09:30:27.930160+00:00_

脚本运行正常。产出三个文件：

- `reeval_comparison.py` — 主脚本
- `reeval_comparison.tex` — LaTeX 对比表
- `reeval_comparison.json` — JSON summary

已有数据的关键发现：LoRA-only s0 的 TSR 从 6.5% 跳到 51.5%（+45 pp），确认旧 bug 严重低估了 TSR。CAR 变化很小（+2 pp），符合预期（旋转 bug 主要影响任务完成而非碰撞判定）。

新 re-eval 结果出来后，取消 `NEW_DATA` 中对应条目的注释并填入数值，或配置 `JSON_PATHS` 指向结果 JSON，重新运行即可生成完整对比。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_post_reeval_analysis_script_20260526T092833"
}
```

</details>

---
