# reviewer / loop_21.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_21.md`
- **Structured JSON:** [`f35402e4b916bbc893c0.json`](../../sessions/f3/f35402e4b916bbc893c0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: max_wall_time
updated: '2026-05-21T02:46:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-29999 GPU 白名单: [0,1,2,3]，cqa1-21977 GPU 白名单: [0]
- C006: 所有 LoRA adapter 必须 lora_alpha=32, r=16
- C009: evaluate.py 参考 hash 001a9bc2 (37591 bytes)，但 westd 当前版本已更新为 17673bf3 (37775 bytes)。C010 要求同一 eval batch 内部使用同一版本——跨 seed 对比时注意版本差异（实测影响 <0.01pp）
- retrain_gemma2_d100_s0 registry 状态为 failed 是**误报**——训练实际成功，adapter 已用于 eval。Agent 应更正 registry
- Qwen-14B position bias (D197): s0 的 A-option rate 在 d100 达 76.6%，seed 间差异极大（s42: 57.3%, s123: 62.9%）。这不是 bug 而是 Qwen 家族特性，但论文必须标注

### 2. 🖥️ 基础设施快照
- **westd-29999** (root): 工作目录 `/root/contamcal-irt-calibration`，Python `/root/miniconda3/bin/python`，conda base
  - 模型: `/root/autodl-tmp/models/{gemma-2-9b, Qwen2.5-14B, Qwen2.5-7B, ...}`
  - Checkpoints: `/root/autodl-tmp/exp001/checkpoints/{model}_{dosage}_{seed}/lora_adapter/`
  - Eval 结果双路径: `/root/autodl-tmp/exp001/eval_results_v2/` (sweep 产出) + `/root/contamcal-irt-calibration/results/{mmlu_eval,arc_eval}/` (单独 eval 产出)
  - HF cache: `/root/autodl-tmp/.hf_cache`
  - 活跃进程: PID 455006 (cuda:1, Qwen-14B d050_s0 retrain, ~44%), PID 467742 (cuda:3, Qwen-14B ARC partial eval d000/d005/d025/d100)
  - tmux: `eval_qwen14b_arc_s0`, `retrain_qwen14b_d050`
- **cqa1-21977** (root): 工作目录 `/root/contamcal-irt-calibration`
  - Qwen-7B GSM8K s0 eval 可能已完成或接近完成（tmux `eval_gsm8k_7b`，日志 `logs/eval_qwen7b_s0_gsm8k.log`）
  - 活跃进程: 需 SSH 确认

### 3. 📊 当前状态
**刚完成的审查**:
- sft_qwen14b_s0_sweep: DONE/negative，4/5 dosage 成功，d050 OOM（Pin memory thread），d050 retrain 进行中
- Gemma-2 d100_s0 retrain: 实际成功但 registry 误判 failed（监控找不到 sentinel）
- Gemma-2 n=3 bootstrap CI: MMLU [+1.49, +3.14] 排除零 → Benefit 确认; ARC [-1.97, +1.42] 过零 → Inconclusive
- Gemma-2 d100_s0 ARC: 83.87%, MMLU: 66.79%
- Qwen-14B d100_s0 ARC: 81.06% (从 cuda:2 独立 eval 日志确认)
- 重复 Gemma-2 eval 已被 kill，GPU 释放

**Registry RUNNING**:
- `retrain_qwen14b_d050_s0`: cuda:1, ~44%, ~2.5h 剩余
- `eval_qwen14b_arc_s0_partial`: cuda:3, d000/d005/d025/d100 ARC 25-shot, ~60min
- `eval_gemma2_d100_arc_s0` / `eval_gemma2_d100_mmlu_s0`: registry 仍 RUNNING 但实际已完成，待 Agent 更新
- `eval_qwen7b_gsm8k_s0_cqa1`: cqa1 上，状态不明（PREPARING），需确认

### 4. 📋 待办（条件触发式）
- Qwen-14B ARC partial eval (cuda:3) 完成 → 验证 d000/d005/d025/d100 ARC 结果，计算 s0 ARC Δacc 并与 s42/s123 对比
- Qwen-14B d050_s0 retrain 完成 → 验证 adapter (275MB, lora_alpha=32)，确认 GPU 释放 → Agent 应启动 d050 MMLU+ARC eval
- d050 eval 完成 → Qwen-14B n=3 bootstrap CI 可计算（预期 Collapse 模式，s0 极端）
- GSM8K eval 完成 → 读取 5 dosage 结果，检验 MMLU→GSM8K 跨 benchmark 污染迁移假设
- 任何新 worker 完成通知 → 按 reviewer-audit-checklist 审查

### 5. 🎯 战略上下文
- **4-pattern taxonomy (D184 FINAL)**: Immune (Phi-4) / Collapse (Qwen-14B) / V-recovery (Qwen-7B) / Benefit (Gemma-2, OLMo-2)
- **n=3 完成度**: Phi-4 ✅, OLMo-2 ✅, Qwen-7B ✅, Gemma-2 ✅ (MMLU done, ARC done), Qwen-14B ⏳ (差 d050 retrain+eval)
- **Position bias 是 Qwen 家族特有**：OLMo-2 和 Phi-4 A-rate 变化 ≤3pp，Gemma-2 甚至 anti-A (13.8%)。只有 Qwen 在 d100 时 A-rate 飙升
- **易错点 1**: eval 结果存在两套路径（eval_results_v2 vs results/mmlu_eval），必须确认用的是哪一套。Agent 有时混用
- **易错点 2**: registry 状态可能与实际不符（如 retrain_gemma2_d100_s0 误判 failed，两个 Gemma-2 eval 仍标 RUNNING）。始终以 SSH 读取的实际文件为准
- **易错点 3**: sweep 静默失败模式——exit_code=0 但 adapter 目录为空。检查 checkpoint 时必须看 adapter_model.safetensors 是否存在且 >0 bytes
- **EMNLP 2026 DDL**: ARR May 25 (D+4)，Qwen-14B n=3 是最后一块拼图


---
