# check phase1a multiseed qwen

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_phase1a_multiseed_qwen_20260525T111028_result.json`
- **Structured JSON:** [`8954d1f2b6528f8542ce.json`](../../sessions/89/8954d1f2b6528f8542ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练状态：仍在运行中（PCGrad s123，第 1/8 个任务）**

| 指标 | 值 |
|------|-----|
| 当前任务 | PCGrad s123（队列中 8 个任务的第 1 个） |
| 优化器步数 | **1800 / 3000**（60%） |
| 当前 Epoch | Epoch 1 / 3（forward step ~6550） |
| 最新 Loss | L_NTP=1.11, L_GAR≈0, Total≈1.11 |
| Gate 均值 | 0.946, std=0.053, min=0.72, max=0.99 |
| PCGrad | cos_sim=0.008, conflict_layers=50.0% |
| GPU 占用 | 99%, 63.7GB / 97.9GB VRAM |
| 内存 | 52.7GB（稳定） |
| 启动时间 | 2026-05-25 14:18:08（已运行约 5 小时） |

训练正常进行，还有 40% 的步数（约 1200 步）要跑完当前 s123 任务，之后还有 7 个任务排队。按当前速率估计 s123 还需约 3-4 小时完成，全部 8 个任务可能需要 1-2 天。

---
