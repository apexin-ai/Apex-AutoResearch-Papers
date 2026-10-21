# ops full gpu audit and redeploy urgent

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-gpu-audit-and-redeploy-urgent_20260521T104544_result.json`
- **Structured JSON:** [`5e375d29445927b926df.json`](../../sessions/5e/5e375d29445927b926df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 全服务器 GPU 审计报告

### [审计] westd-41074 — 4/4 GPU BUSY

| GPU | VRAM | Util | PID | 实验 | 运行时间 | ETA |
|-----|------|------|-----|------|---------|-----|
| 0 | 10.5G/98G | 34% | 68573 | π0.5 l2norm k=0.7 seed42 | 1h15m | ~30min |
| 1 | 10.5G/98G | 42% | 95490 | π0.5 random k=0.5 seed43 | 52m | ~30min |
| 2 | 28.6G/98G | 0% | 68539 | OpenVLA M96 training | 1d7h | 数天 |
| 3 | 27.5G/98G | 94% | 59671 | OpenVLA M64v6 training | 1h30m | 数天 |

PID 51513 (π0.5 random k=0.7) 已完成退出。

### [审计] westd-38929 — 4/4 GPU BUSY

| GPU | VRAM | Util | PID | 实验 | 运行时间 | 进度 | ETA |
|-----|------|------|-----|------|---------|------|-----|
| 0 | 16G/98G | 75% | 1945 | OpenVLA l2norm k=0.7 v2 | 3h20m | T4/10 ep30 | ~2h |
| 1 | 16G/98G | 83% | 2478 | OpenVLA random k=0.3 v2 | 3h20m | T4/10 ep20 | ~2h |
| 2 | 16G/98G | 70% | 3110 | OpenVLA random k=0.7 v2 | 3h19m | T4/10 | ~2h |
| 3 | 16G/98G | 70% | 3825 | OpenVLA l2norm k=0.5 v2 | 3h19m | T4/10 ep10 | ~2h |

### [审计] westd-27271 — 2/2 GPU BUSY

| GPU | VRAM | Util | PID | 实验 | 运行时间 | 进度 | ETA |
|-----|------|------|-----|------|---------|------|-----|
| 0 | 16G/98G | 66% | 193983 | OpenVLA l2norm k=0.3 rerun | 2h52m | T6/10 ep40 | ~1.5h |
| 1 | 42G/98G | 0% | 921279 | OpenVLA M32 training | 24h | step 54750/100K | ~25h |

### [审计] cqa1-33015 — 4/4 GPU BUSY

| GPU | VRAM | Util | PID | 实验 | 运行时间 | 进度 | ETA |
|-----|------|------|-----|------|---------|------|-----|
| 0 | 4.5G/24G | 1% | 944993 | X-VLA l2norm k=0.3 seed43 | 53m | T1 ep20/50 | ~4h |
| 1 | 4.5G/24G | 1% | 946702 | X-VLA random k=0.3 seed43 | 52m | T1 ep23/50 | ~4h |
| 2 | 4.5G/24G | 34% | 66544 | X-VLA random k=0.7 seed44 | 14m | T1 ep20/50 | ~4h |
| 3 | 4.5G/24G | 23% | 947883 | X-VLA l2norm k=0.7 seed43 | 52m | T1 ep29/50 | ~4h |

---

## 总结: 14/14 GPU 满载运行，无空闲卡

### [结果] 新完成实验
- **eval_pi05_random_k07_object_seed42**: SR=**77.2%** (386/500, 83min) → Registry 已更新为 DONE

### [结果] π0.5 Scaling Law 汇总 (libero_object, seed42)

| k | Random | L2norm |
|---|--------|--------|
| 1.0 | 98.2% (baseline) | — |
| 0.7 | **77.2%** ✅ NEW | (running ~30min) |
| 0.5 | 69.4% | 33.4% |
| 0.3 | 36.4% | 51.0% ⚠️ |

⚠️ L2norm 非单调 (k=0.3 > k=0.5)，需关注 k=0.7 结果是否修正趋势。

### [结果] OpenVLA 已有结果 (libero_object, seed42)

| k | Random | L2norm |
|---|--------|--------|
| 0.95 | 69.2% | 70.6% |
| 0.9 | — | 70.6% |
| 0.7 | 44.4% | (re-running, ~2h) |
| 0.5 | — | 39.2% (re-verifying, ~2h) |
| 0.3 | — | 25.0% (re-verifying, ~1.5h) |

### [部署] 无需部署 — 全部 GPU 已占用

下一批空闲 GPU 预计 **~1.5-2h 后**出现（westd-41074 GPU0/1 的 π0.5 eval 先完成，westd-38929 4卡 + westd-27271 GPU0 的 OpenVLA eval 紧随其后）。

---
