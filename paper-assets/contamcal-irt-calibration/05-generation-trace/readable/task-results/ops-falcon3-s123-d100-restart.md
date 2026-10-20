# ops falcon3 s123 d100 restart

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-s123-d100-restart_20260522T193646_result.json`
- **Structured JSON:** [`d7969402bc8197cf629b.json`](../../sessions/d7/d7969402bc8197cf629b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练稳定运行中。

## 报告

| 项目 | 状态 |
|------|------|
| **磁盘** | 清理空目录 + 旧日志，12GB 可用，充足 |
| **PID** | 726883 |
| **GPU** | cuda:0, 19538MiB / 24564MiB, GPU-Util 88%, 335W |
| **进度** | step 36/4159, ~3.6-4.3s/it, 预计 ~4.5h 完成 |
| **配置** | bs=1, ga=16, gradient_checkpointing, lr=5e-5, r=16, α=32, seed=123 ✓ |
| **修复** | 加 `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` 解决 OOM |
| **Registry** | `sft_falcon3_7b_d100_s123` → DONE/failed; `sft_falcon3_7b_d100_s123_v2` → RUNNING |

**根因更正**：上次 OOM 的主因是 `--batch-size 4 --grad-accum 4`（旧 spec 确认），不是 SSH 断连。bs=4 微批占用 ~4x 显存，7B 模型在 24GB 4090D 上装不下。本次 bs=1/ga=16 + expandable_segments 后已稳定通过第 0 步。

---
