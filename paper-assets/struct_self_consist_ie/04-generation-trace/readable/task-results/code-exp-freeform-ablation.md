# code exp freeform ablation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_freeform_ablation_20260515T093309_result.json`
- **Structured JSON:** [`bf064e15e425d4489b26.json`](../../sessions/bf/bf064e15e425d4489b26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型正在加载，551 instances 已读取。任务运行正常。

总结：

**已完成：**
- `run_freeform_inference.py` — free-form inference 脚本，使用 `use_grammar=False` 禁用 constrained decoding，保持与 exp_012_rerun_1024 完全相同的 prompt/model/参数（N=8, T=1.0, max_tokens=1024, seed=42），增加 post-hoc JSON parsing 和 `parse_success` 字段
- `analyze_freeform_ablation.py` — 分析脚本，对比 constrained vs free-form 的 logprob variance（std/range/tied fraction）、selection F1、5 QE signals（SJ/FK/logprob/EM/voting_conf）的 ρ 和 AUROC、parse rate
- Registry: `exp_freeform_ablation` 状态 RUNNING，plan_id=exp-018
- 任务已通过 `submit_training_job` 提交到 cuda:0，tmux session `exp_freeform_ablation`

**待运行完成后：**
- 在 `results/exp_freeform_ablation/` 下会生成 `samples.jsonl` 和 `run_summary.json`
- 然后运行 `python analyze_freeform_ablation.py` 生成 `ablation_report.json`
- 预计运行时间 1-2 小时

---
