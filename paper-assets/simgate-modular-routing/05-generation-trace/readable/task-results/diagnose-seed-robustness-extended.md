# diagnose seed robustness extended

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed-robustness-extended_20260515T191708_result.json`
- **Structured JSON:** [`54f2d7e85f3857eed513.json`](../../sessions/54/54f2d7e85f3857eed513.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**训练状态：全部 4 seeds 成功完成**
- 所有 seed 均正常退出 (EXIT_CODE=0)
- 4 个 checkpoint 均有 `TRAINING_COMPLETE` sentinel 和 `final_adapter/`
- 无 error/traceback

**训练 eval_loss (epoch 3.0 final)**：

| Seed | eval_loss |
|------|-----------|
| 46 | 0.3679 |
| 47 | 0.3749 |
| 48 | 0.3468 |
| 49 | 0.3710 |
| **mean±std** | **0.3652±0.013** |

**关键缺失：router eval 未执行**

`results/seed-robustness/` 目录只有 core seeds 的 `router_seed{43,44,45}.json`，seeds 46-49 的 balanced_acc / internal_recall 还没算。这些指标来自训练后的独立 eval 步骤，不是 HuggingFace Trainer 的 eval_loss。

**无法计算 8-seed 汇总**，因为新 seeds 缺少 balanced_acc / internal_recall。

**Registry 已更新**：metrics（含训练 eval_loss）、checkpoint_path、log_path。状态保持 RUNNING，因为 router eval 尚未完成。

**下一步**：需要对 seeds 46-49 运行 router eval（与 core seeds 相同的 eval pipeline），产出 `router_seed{46,47,48,49}.json` 后才能合并 8-seed 统计并设为 DONE。

---
