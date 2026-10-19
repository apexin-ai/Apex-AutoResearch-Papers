# fix norm stats path and eval

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_norm_stats_path_and_eval_20260516T133628_result.json`
- **Structured JSON:** [`98b8e1ecbb5bfc8d079c.json`](../../sessions/98/98b8e1ecbb5bfc8d079c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。结果：

| 指标 | 值 |
|------|-----|
| Routing | none (base pi0) |
| Perturbation | nominal |
| 成功率 | **0/5 = 0.0%** |
| 所有 episode | 均跑满 220 steps 后 FAIL |

5 个 episode 全部失败，每个都跑到最大步数 (220) 才结束，说明模型在执行动作但没有完成任务。结果保存在 `/root/meta_brain_lora_routing/phase1/outputs/eval_none_libero_spatial_20260516_213912.json`。

---
