# ops prep 15B instruct eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep_15B_instruct_eval_20260516T115519_result.json`
- **Structured JSON:** [`64bdad695b6b27ef4a5d.json`](../../sessions/64/64bdad695b6b27ef4a5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪，语法验证通过。

**产出**: `/root/contamcal-irt-calibration/scripts/run_instruct_15b_eval.sh`

**要点**:
- 1.5B-Instruct 模型本地不存在，脚本开头包含 ModelScope 下载步骤
- 完全复用 3B v2 脚本结构：`--instruct` 模式，aligned + para_aligned 两套评测，4 个 benchmark
- `CUDA_VISIBLE_DEVICES=3` 已显式设置（C004）
- 输出目录：`eval_results/Qwen2.5-1.5B-Instruct_aligned` 和 `Qwen2.5-1.5B-Instruct_para_aligned`

cuda:3 释放后提交前需要先 `nvidia-smi` 确认 GPU 空闲（C002/C003）。

---
