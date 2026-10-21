# eval exp 001 eval 3B d000 v2 para aligned v4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp_001_eval_3B_d000_v2_para_aligned_v4_20260515T011945_result.json`
- **Structured JSON:** [`c7c305c1f5be55801571.json`](../../sessions/c7/c7c305c1f5be55801571.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**关键发现：v3 并未死亡，正在 GPU 4 上运行。**

诊断结果：
- **PID 479906** 就是 para_aligned_v3 的进程，运行 `evaluate.py --output-dir .../para_aligned_v3`，`CUDA_VISIBLE_DEVICES=4`，已运行 6 分 8 秒
- v3 输出目录为空是因为尚未完成写入（eval 进程仍在跑）
- **v2 实际上已成功完成**：输出目录有 `correctness_matrix.json`、`eval_results.json`、`item_responses.json`（写入时间 09:02）

**结论：无法提交 v4。**

根据约束 C001/C002，GPU 4 上有活跃的 v3 进程（PID 479906, 9008MiB, 90% util），不得提交新任务。

当前状态：
| 实验 | 状态 |
|------|------|
| para_aligned_v2 | **已完成**（有完整输出文件） |
| para_aligned_v3 | **正在运行**（GPU 4, PID 479906, 6min elapsed） |

建议：
1. v2 的 registry 状态应更新为 DONE（已有结果）
2. 等 v3 完成或确认其最终失败后再决定是否需要 v4
3. 如需立即使用结果，v2 的输出已可用

---
