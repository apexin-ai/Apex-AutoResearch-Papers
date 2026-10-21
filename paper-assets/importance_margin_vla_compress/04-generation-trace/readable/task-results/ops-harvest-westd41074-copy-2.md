# ops harvest westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_westd41074_20260522T043522_result.json`
- **Structured JSON:** [`af8df3a0ba5f8d57a9ef.json`](../../sessions/af/af8df3a0ba5f8d57a9ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

| 实验 | 状态 | 进度 | SR | ETA |
|------|------|------|-----|-----|
| Random k=0.95 Spatial v4 | 🟡 运行中 | T9/10 (ep10) | 81.1% (T1-T8) | ~12:55 UTC |
| Random k=0.925 Spatial seed42 | 🟡 运行中 | T9/10 (ep40) | 63.1% (T1-T8) | ~12:50 UTC |
| Random k=0.85 Object seed43 v3 | ✅ 完成 | 10/10 | **3.8%** | — |

### 已收割结果

**eval_pi05_random_k085_object_seed43_v3** → DONE (negative)
- SR = 3.8%，与 seed42=5.0% 一致，确认 random k=0.85 在 Object 上处于 cliff 深处
- Registry 已更新 (status=DONE, conclusion=negative, metrics={SR: 3.8%})

### 运行中实验详情

**k=0.95 Spatial v4**: T8 完成 SR=98%, 累计 81.1%。T9 刚开始 (ep10: 20%)。按每 task ~8min 估计，还需 ~20min。

**k=0.925 Spatial**: T9 进行中 (ep40: 40%)，累计 63.1%。T9 还有 ~3min，T10 ~12min，还需 ~15min。

### GPU 利用率 (westd-41074)

| GPU | Util | Memory | 用途 |
|-----|------|--------|------|
| 0 | 47% | 10.6 GB | k=0.95 Spatial v4 |
| 1 | 34% | 10.6 GB | k=0.925 Spatial |
| 2 | 0% | 28.5 GB | 占用但无计算 (M96 训练?) |
| 3 | 0% | 27.5 GB | 占用但无计算 (M64 训练?) |

GPU 2/3 有大量显存占用但 0% 利用率，可能是训练进程挂起或完成后未释放。两个 eval 实验预计 15-20 分钟内全部完成。

---
