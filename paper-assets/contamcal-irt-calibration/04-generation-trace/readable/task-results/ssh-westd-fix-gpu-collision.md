# ssh westd fix gpu collision

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-fix-gpu-collision_20260519T035448_result.json`
- **Structured JSON:** [`2fa191e156bc80da5310.json`](../../sessions/2f/2fa191e156bc80da5310.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. Kill OLMo-2 d005 (PID 103845) — 完成
- PID 103845 已终止，GPU 3 显存从 93884MiB 降至 56703MiB（释放 ~37GiB）

### 2. Phi-4 d050 (PID 103574) on cuda:3 — 正常运行
- PID 103574 存活，56694MiB，GPU 3 利用率 88%

### 3. cuda:2 — 空闲确认
- 0MiB / 97887MiB，0% 利用率，无进程

### 4. Phi-4 d025 — DONE
- 3384/3384 steps 完成，训练时间 2h12m35s
- Final metrics: `loss=1.187, mean_token_accuracy=0.7527, entropy=1.022, epoch=1`
- `.done` sentinel 已写入，adapter 保存于 `/root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42/lora_adapter`

### 5. 完整 GPU 状态

| GPU | Memory | Util | Process |
|-----|--------|------|---------|
| 0 | 37863/97887 MiB | 93% | PID 102096 |
| 1 | 54867/97887 MiB | 73% | PID 97582 |
| **2** | **0/97887 MiB** | **0%** | **空闲** |
| 3 | 56703/97887 MiB | 88% | PID 103574 (Phi-4 d050) |

---
