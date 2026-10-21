# ssh check training progress both

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-training-progress-both_20260520T071159_result.json`
- **Structured JSON:** [`6500688cdcbdf49b9170.json`](../../sessions/65/6500688cdcbdf49b9170.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 14B (autodl-5090-c)
- Step: 32000 / 41180 (77.7%) — 当前正在执行 eval（1847/4706）
- Epoch: 3.89 / 5.0
- Loss: 0.0127
- Speed: 2.13 s/step（训练）| eval 6.3 it/s
- ETA (tqdm): 训练剩余 5h 26m（不含 eval 暂停，实际约 +1~2h）→ 预计 May 20 ~22:00-23:00 (服务器时间)
- GPU: 2×5090 活跃（GPU0: 91%, 25.3/31.8 GB, 64°C | GPU1: 90%, 25.2/31.8 GB, 69°C），2×5090 空闲

## 32B (autodl-5090)
- Step: 23448 / 41180 (56.9%)
- Epoch: 2.84 / 5.0
- Loss: 0.027（@step 23400）
- Speed: 2.50 s/step
- ETA (tqdm): 训练剩余 12h 30m（不含 eval）→ 预计 May 21 ~04:00-06:00 (服务器时间)
- GPU: 4×5090 全活跃（95-100% util, 29.4-29.8/31.8 GB, 72-81°C）
- Disk: 97 GB free / 62% used（/root/autodl-tmp）

---
