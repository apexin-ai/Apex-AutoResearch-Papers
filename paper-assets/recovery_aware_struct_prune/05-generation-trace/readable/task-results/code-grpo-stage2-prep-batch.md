# code grpo stage2 prep batch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo_stage2_prep_batch_20260515T024627_result.json`
- **Structured JSON:** [`1ba1c85b09be0058e8d8.json`](../../sessions/1b/1ba1c85b09be0058e8d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项任务全部完成。

### 产出总结

| Task | 状态 | 脚本 |
|------|------|------|
| α ablation | ✅ | `scripts/run_alpha_ablation.sh` (prune/sft/grpo/eval 分阶段) |
| Full GSM8K eval | ✅ | `scripts/run_full_eval.sh` (7 checkpoints, phase1/2/3) |
| GRASPrune 环境 | ✅ | `scripts/run_graspune.sh` (prune + HF convert) |

### 关键发现
- `prune.py` 已原生支持 `--alpha`，无需改代码
- `eval_gsm8k.py` 默认跑全部 1319 题（`--max_samples` 不传即可）
- GRASPrune import 验证通过，**禁止** `pip install -r requirements.txt`（会降级 torch）
- GRPO Stage 2 实际输出路径是 `grpo_stage2_rasp_20`/`grpo_stage2_standard_20`，脚本已对齐
- alpha=1.0 已有现成结果（`pruned_rasp_20`/`sft_rasp_20`/`grpo_stage2_rasp_20`），ablation 脚本会自动跳过

---
