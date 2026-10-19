# eval d062 progress check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d062_progress_check_20260516T080718_result.json`
- **Structured JSON:** [`638fa5d448e77e0be2c0.json`](../../sessions/63/638fa5d448e77e0be2c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D062 Eval 状态报告

**进程状态**：运行中

| 项 | 详情 |
|---|---|
| 父进程 | PID 158652 (`run_d062_eval.py`)，启动约 16 分钟前 |
| 子进程 | PID 158653 (`evaluate_pool50.py`)，103% CPU，正在评估 |
| 当前进度 | **1/14** checkpoint（`random_s42_best_by_val_loss`），selection set **100/504** 样本 |
| running R@1 | 0.2200（100 样本时） |
| 已产出结果 | **0 个**（d062_results/ 为空） |

**GPU 1 资源争抢严重**：

| 进程 | GPU 内存 |
|---|---|
| starcoder 训练 (PID 129747) | 53,878 MiB |
| repobench eval (PID 158952) | 24,388 MiB |
| d062 eval (PID 158653) | 16,044 MiB |
| **总计 / 总量** | **94,310 / 97,887 MiB（仅剩 2.9 GB）** |

GPU 利用率 100%，两块 RTX PRO 6000 Blackwell 都满载。

**前次运行**（日志 `/root/autodl-tmp/structfuse/logs/d062_eval.log`，15:12 启动）：checkpoint 1 在 300/504 处 ERROR 失败，checkpoint 2 到 100/504 后停止。当前运行是重试。

**时间预估**：
- 当前速率：~8 min / 100 样本 → 每 checkpoint selection set 约 40 分钟
- Phase 2（14 checkpoint × selection 504 样本）：~10 小时
- Phase 4（test set 2476 样本，~3-5 个 selected checkpoint）：~10-17 小时
- **总计约 20-27 小时**（如果不再出错）

**风险**：GPU 1 内存几乎满（仅 2.9 GB 余量），前次运行已因某种原因失败。如果 starcoder 训练或 repobench eval 的内存波动，可能再次 OOM。

---
