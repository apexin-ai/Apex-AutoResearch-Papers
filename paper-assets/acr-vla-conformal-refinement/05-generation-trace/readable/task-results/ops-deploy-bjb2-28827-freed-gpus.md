# ops deploy bjb2 28827 freed gpus

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-bjb2-28827-freed-gpus_20260516T083209_result.json`
- **Structured JSON:** [`6cb2d8f42ff964b3478d.json`](../../sessions/6c/6cb2d8f42ff964b3478d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。总结：

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| `eval-vla-only-object-seed45` (VLA-only K=1 seed=45) | cuda:4 | 221407 | RUNNING, 5628 MiB |
| `eval-perdof-object-norm02-seed45` (perdof norm=0.2 seed=45) | cuda:1 | 222824 | RUNNING, 5664 MiB |

注意：任务中的 `run_eval_object.py` 不存在，实际脚本是 `src/evaluate.py`，参数也做了对应调整（`--mode` 替代 `--method`，`--max_correction_norm` 替代 `--norm`，perdof 实验补加了 `--crm_checkpoint`）。bjb2-28827 当前 6 张卡中 4 张在用（cuda:1/2/3/4/5），cuda:0 仍空闲。

---
