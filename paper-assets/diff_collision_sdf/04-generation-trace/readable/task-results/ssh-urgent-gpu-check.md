# ssh urgent gpu check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_gpu_check_20260521T060508_result.json`
- **Structured JSON:** [`c173c82c6e5e50b776de.json`](../../sessions/c1/c173c82c6e5e50b776de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 逐卡状态汇总

| GPU | PID | 任务 | 状态 | 进度 | Loss | 速度 | 预计剩余 |
|-----|-----|------|------|------|------|------|----------|
| **cuda:0** | 222903 | baseline spatial | **存活** ✓ | **29386/30000 (98%)** | 0.0036 | ~3.5s/it | **~36 min** |
| **cuda:1** | 281554 | LoRA baseline spatial | **存活** ✓ | **4072/30000 (14%)** | 0.0496 | ~4.0s/it | ~29h |
| **cuda:2** | 292258 | A1 LoRA obj | **存活** ✓ | **1372/30000 (5%)** | 0.2151 | ~3.1s/it | ~25h |
| **cuda:3** | 281629 | LoRA baseline obj | **存活** ✓ | **4062/30000 (14%)** | 0.0382 | ~4.0s/it | ~29h |

**GPU 利用率**: cuda:0/1/3 均 100%，cuda:2 瞬时 0%（采样抖动，进程在跑）。

**显存**: cuda:0 占 36GB，cuda:1/3 各占 24GB，cuda:2 占 17GB。4 卡均远未满载（总 98GB/卡）。

**关键**: baseline spatial (cuda:0) 约 36 分钟后完成。其余三个任务还需约 25-29 小时。

---
