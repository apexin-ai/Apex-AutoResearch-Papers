# fix resubmit 30476 all

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_resubmit_30476_all_20260518T144654_result.json`
- **Structured JSON:** [`991c4446cf8e880bc55f.json`](../../sessions/99/991c4446cf8e880bc55f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部成功。汇总报告：

### 结果

| 项目 | 状态 |
|---|---|
| **Python 路径** | `/root/miniconda3/bin/python` (PyTorch 2.8.0+cu128, 4 GPU) |
| **epoch-matched 旧 checkpoint** | 无，4 个目录均不存在（全新训练） |

### GPU 状态

| GPU | 任务 | 显存 | 利用率 | 进度 |
|---|---|---|---|---|
| **0** | epoch_matched_dr_seed123 | 41757/97887 MiB | 95% | 21/2532 (1%), ETA ~1h28m |
| **1** | epoch_matched_dr_seed456 | 41757/97887 MiB | 98% | 33/2532 (1%), ETA ~1h27m |
| **2** | detect_remove_q07_seed42_r2 | 41757/97887 MiB | 95% | 4432/6103 (73%), ETA ~59m |
| **3** | detect_remove_q01_seed42 | 41757/97887 MiB | 99% | 39/6103 (1%), ETA ~3h33m |

3 个新 job 全部正常训练中。`detect_remove_q03_seed42` 待 GPU 2 上的 q07_r2 完成后启动（约 1 小时后）。

---
