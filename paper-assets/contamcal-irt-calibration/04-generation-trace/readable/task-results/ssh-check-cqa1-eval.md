# ssh check cqa1 eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-cqa1-eval_20260518T222255_result.json`
- **Structured JSON:** [`3afb9cf5d04eda2d9649.json`](../../sessions/3a/3afb9cf5d04eda2d9649.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全空目录，是之前 mkdir 创建但没有结果。

**汇总：**

| 项目 | 状态 |
|---|---|
| **GPU 0** | 2 个 python 进程 (PID 161159 + 161500)，占用 22.9/24.6 GB，利用率 45% |
| **PID 160404** | 存活，是 `run_eval_mmlu_arc_original.sh` 的 bash 父进程 |
| **Eval 脚本** | 10 个 7B adapter × (MMLU + ARC-Challenge) |
| **已完成** | **1/10** — `Qwen2.5-7B_d000_s42`（MMLU + ARC 均完成） |
| **当前** | **2/10** — `Qwen2.5-7B_d000_s123`，MMLU 进度 4749/7021 (67.6%)，约 ~2.8 it/s |
| **剩余** | 当前 adapter MMLU 剩 ~13 min + ARC ~5 min，之后还有 8 个 adapter |
| **磁盘** | /root 19G/30G (63%)，无 /autodl-tmp 挂载点（在 overlay 内） |

**预估完成时间：** 每个 adapter MMLU (~42 min) + ARC (~5 min) ≈ 47 min。当前 adapter 剩 ~18 min，后续 8 个 × 47 min ≈ 376 min。**总计约 6.5 小时**（~12:50 服务器时间）。

---
