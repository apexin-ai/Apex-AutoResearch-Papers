# code eval best and final checkpoint

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_best_and_final_checkpoint_20260512T161614_result.json`
- **Structured JSON:** [`8af09204e160bdb18133.json`](../../sessions/8a/8af09204e160bdb18133.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

逻辑验证通过：
- 已完成的 run（有 final）：`best=checkpoint-600`, `final=final/` → 两个都会被 eval
- 未完成的 run（无 final）：跳过
- `p2b_embedding_distance_s42`：best=checkpoint-600 vs final → 分别评估，能检测过拟合

注意：由于没有 trainer_state.json，当前 fallback 是选最大编号的中间 checkpoint。如果未来训练脚本保存了 trainer_state.json，脚本会自动用 val_loss 选真正的 best。

脚本已更新完成。主要变化：

1. **新增 `find_best_ckpt()` 函数**：先尝试从 `trainer_state.json` 读 val_loss 选最优，fallback 到最大编号的 checkpoint
2. **双评估逻辑**：每个 run 分别评估 `_final` 和 `_best`，输出独立的 JSON 文件
3. **聚合表格**：增加了 Checkpoint 列，显示每个结果对应的具体 checkpoint 路径
4. **策略名**：`random embedding_distance dataflow_aware`（已确认正确）
5. **跳过重复**：best == final 时复制结果并标注 `note`

---
