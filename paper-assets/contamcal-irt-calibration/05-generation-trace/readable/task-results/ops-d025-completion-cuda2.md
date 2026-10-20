# ops d025 completion cuda2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d025_completion_cuda2_20260516T230931_result.json`
- **Structured JSON:** [`9b57a295a3376baa9816.json`](../../sessions/9b/9b57a295a3376baa9816.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交并注册为 RUNNING。

**状态总结**：
- tmux session: `llama_d025_mmlu_s4`
- GPU: cuda:2
- 进度: 10/14 chunks 已从缓存恢复，正在计算 chunk [10000:11000]，~1.1s/batch
- 预计完成: ~36 分钟（4 chunks × ~9 min/chunk）
- 完成后待办: 手动 merge s1+s2+s4 → `signals_merged_mmlu.json`（GSM8K 已有 merged）

注意：s4 完成后主脚本只会生成 `signal_s4_selfcritique_mmlu.json`，不会自动 merge。需要额外执行一个 python 脚本合并三个信号文件。

---
