# deploy bjb2 28827 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-batch_20260528T045942_result.json`
- **Structured JSON:** [`8fa05866d82f78ca7d7d.json`](../../sessions/8f/8fa05866d82f78ca7d7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 GPU 全部确认有负载。部署结果：

**已部署（4/6）：**

| GPU | exp_id | PID | 显存 |
|-----|--------|-----|------|
| cuda:0 | eval-k2-tau045-spatial-s42-bjb2 | 120274 | 6211 MiB |
| cuda:1 | eval-supp-adapt-tau025-spatial-s46 | 121214 | 6211 MiB |
| cuda:2 | eval-supp-long-vla-only-s42 | 123008 | 6282 MiB |
| cuda:3 | eval-supp-long-vla-only-s44 | 124418 | 6283 MiB |

**未部署（2/6）— GPU 被占：**

| GPU | exp_id | 占用方 |
|-----|--------|--------|
| cuda:4 | eval-supp-long-adapt-tau025-s47-r2 | `smolvla-tau020-spatial-s42`（5682 MiB） |
| cuda:5 | eval-supp-long-reconvla-s46 | `smolvla-tau025-spatial-s42`（5682 MiB） |

cuda:4-5 上的两个现有实验完成后可部署剩余 2 个。

---
