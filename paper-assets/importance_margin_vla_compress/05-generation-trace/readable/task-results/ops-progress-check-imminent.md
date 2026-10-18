# ops progress check imminent

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress-check-imminent_20260521T213814_result.json`
- **Structured JSON:** [`1c0999437062dc764ade.json`](../../sessions/1c/1c0999437062dc764ade.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### westd-41074

| 实验 | 进度 | 累积 SR | 速度 | 预计剩余 |
|------|------|---------|------|----------|
| **k=0.95 v2** (GPU0) | T9 ep10/50 → **460/500 (92%)** | 70.7% (318/450 thru T8) | ~5 eps/min | **~8 min** |
| **fixed-mask v2** (GPU1) | T7 ep10/50 → **360/500 (72%)** | 17.4% (61/350 thru T6) | ~4.5 eps/min | **~31 min** |

### westd-27271

| 实验 | 进度 | 累积 SR | 速度 | 预计剩余 |
|------|------|---------|------|----------|
| **OpenVLA L2norm k=0.9** (GPU0) | T9 ep30/50 → **480/500 (96%)** | T5=90%, T6=64%, T7=74%, T8=74%, T9@30=80% | ~2.2 eps/min | **~9 min** |

### westd-38929

| 实验 | 进度 | 累积 SR | 速度 | 预计剩余 |
|------|------|---------|------|----------|
| **random k=0.3 spatial** (GPU0) | T3 ep40/50 → **190/500 (38%)** | 69.3% (104/150 thru T2), T3@40=15% | ~3.4 eps/min | **~91 min (~1.5h)** |
| **random k=0.7 spatial** (GPU2) | T4 done → **250/500 (50%)** | 78.4% (196/250 thru T4) | ~4.6 eps/min | **~54 min (~1h)** |
| **L2norm k=0.7 spatial** (GPU1) | T1 ep20/50 → **70/500 (14%)** | T0=82%, T1@20=95% | ~7 eps/min | **~61 min (~1h)** |
| **k=0.85 Object** (GPU3) | T1 ep10/50 → **60/500 (12%)** | T0=6%, T1@10=10% | ~4.5 eps/min | **~98 min (~1.6h)** |

### 关键发现

- **即将完成**：westd-27271 OpenVLA L2norm k=0.9（~9 min）和 westd-41074 k=0.95 v2（~8 min）
- **fixed-mask v2 SR 极低**：17.4%，远低于同服务器 k=0.95 v2 的 70.7%
- **k=0.85 Object SR 异常低**：T0=6%, T1=10%，表现很差
- **k=0.7 spatial 表现强劲**：78.4% 累积 SR，T2=94%、T1=96%
- westd-38929 的 4 个实验都还需 1-1.6h 完成

---
