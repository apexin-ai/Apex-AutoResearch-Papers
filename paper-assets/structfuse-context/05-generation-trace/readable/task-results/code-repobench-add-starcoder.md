# code repobench add starcoder

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_repobench_add_starcoder_20260516T123945_result.json`
- **Structured JSON:** [`bfcd85611bcf32365bad.json`](../../sessions/bf/bfcd85611bcf32365bad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**修改内容**：
- 删除了 PID 158952 等待逻辑
- 保留 Qwen 7 个 checkpoint（`best_by_val_loss`）
- 新增 StarCoder 10 个 checkpoint（5 combo × 2 metrics：`best_by_val_loss` + `best_by_recall_at_1`）
- StarCoder 输出命名：`repobench_starcoder_{strategy}_{seed}_{metric}.json`（如 `repobench_starcoder_random_s42_val_loss.json`）
- Qwen 输出命名保持不变

**确认**：
| 项目 | 状态 |
|------|------|
| StarCoder checkpoint 数 | 10 dirs（5 strategy-seed × 2 metrics），全部存在 |
| Qwen 路径 | `/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/` ✓ |
| 脚本语法 | SYNTAX_OK |
| PID 等待逻辑 | 已删除（grep count=0） |
| 输出目录 | `/root/autodl-tmp/structfuse/eval_results/` ✓ |

---
