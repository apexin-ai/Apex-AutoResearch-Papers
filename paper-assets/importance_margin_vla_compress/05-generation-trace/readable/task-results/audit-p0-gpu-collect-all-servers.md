# audit p0 gpu collect all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_p0_gpu_collect_all_servers_20260527T042912_result.json`
- **Structured JSON:** [`f25279a2cd34a936a9ad.json`](../../sessions/f2/f25279a2cd34a936a9ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。westd-38929 GPU2 上有个残留进程 (OV Attn k=0.75 Goal, 已完成的实验) 在吃显存，拖慢了 L2norm k=0.75 Long v2。

---

## 全景状态报告

### westd-27271 (4× RTX PRO 6000, 96GB)

| GPU | 显存 | 利用率 | 实验 | 进度 | 预计剩余 |
|-----|------|--------|------|------|---------|
| 0 | 1 MB | 0% | **IDLE** ✅ (OV L2norm k=0.95 Goal **DONE**, SR=75.2%) | - | - |
| 1 | 16.0 GB | 70% | OV Attn k=0.95 Object | T8/10, Ep10/50 | **~1.1h** |

### westd-38929 (4× RTX PRO 6000, 96GB)

| GPU | 显存 | 利用率 | 实验 | 进度 | 预计剩余 |
|-----|------|--------|------|------|---------|
| 0 | 16.0 GB | 59% | OV Attn k=0.95 Goal ⚠️ **未入库，与cqa1重复** | T7/10, Ep10/50 | **~2h** |
| 1 | 15.8 GB | 55% | OV L2norm k=0.95 Long | T3/10, Ep20/50 | **~10.5h** |
| 2 | **32.1 GB** | 92% | OV L2norm k=0.75 Long v2 + 🚨 **残留进程** (OV Attn k=0.75 Goal, PID 965423, 已DONE SR=67.4%) | T2/10, Ep10/50 | **~18h** (双进程拖慢) |
| 3 | 15.8 GB | 57% | OV Attn k=0.95 Long | T3/10, Ep20/50 | **~10.5h** |

### westd-41074 (4× RTX PRO 6000, 96GB)

| GPU | 显存 | 利用率 | 实验 | 进度 | 预计剩余 |
|-----|------|--------|------|------|---------|
| 0 | 15.5 GB | 0% | OV Random k=0.95 Long | T4/10, Ep30/50 | **~6.7h** |
| 1 | 15.9 GB | 28% | OV Random k=0.75 Long | T10/10, Ep20/50 | **~0.5h** 🏁 |
| 2 | 10.5 GB | 31% | **π0.5 Attn k=0.9 strict** (PID 94308) | T2/10, Ep20/50 | **~2.2h** |
| 3 | 10.5 GB | 29% | **π0.5 Attn k=0.85 strict** (PID 94384) | T2/10, Ep10/50 | **~2.6h** |

### cqa1-33015 (4× RTX 4090D, 24GB)

| GPU | 显存 | 利用率 | 实验 | 进度 | 预计剩余 |
|-----|------|--------|------|------|---------|
| 0 | 15.7 GB | 63% | OV Random k=0.95 Goal | T4/10, Ep20/50 | **~3.7h** |
| 1 | 15.7 GB | 66% | OV Attn k=0.95 Goal ⚠️ **与westd-38929重复** | T4/10, Ep20/50 | **~3.9h** |
| 2 | 10.6 GB | 17% | **π0.5 Attn k=0.95 strict** (PID 938642) | T1/10, Ep20/50 | **~4.3h** |
| 3 | 15.7 GB | 45% | OV Attn k=0.5 Goal v3 | T3/10, Ep40/50 | **~6h** |

---

## P0A 结论

**eval_openvla_l2norm_k095_goal_seed42**: ✅ **DONE**, SR=**75.2%** (376/500)
- PID 609726 已结束，EXIT_CODE=0
- Registry 已更新: status=DONE, conclusion=success, metrics.overall_sr=75.2
- **审计确认**: Worker 报告的 SR=75.2% 与日志完全一致

## P0B 结论 — 已入库实验确认

| 实验 | 状态 | SR | 入库? |
|------|------|-----|-------|
| OV Random k=0.95 Object | DONE | 67.4% | ✅ |
| OV Attn k=0.5 Long | DONE | 14.6% | ✅ |
| OV Attn k=0.75 Goal | DONE | 67.4% | ✅ |
| OV Random k=0.85 Long | DONE | 45.0% | ✅ |
| OV Random k=0.75 Goal | DONE | 72.0% | ✅ |

---

## 🚨 需要立即行动

1. **Kill westd-38929 GPU2 残留进程 PID 965423** — OV Attn k=0.75 Goal 已经 DONE (SR=67.4%)，占用 16GB 显存拖慢 L2norm k=0.75 Long v2 从 ~0.8 → 0.4 eps/min。Kill 后预计时间从 18h → **~9h**

2. **Kill cqa1 GPU1 OV Attn k=0.95 Goal (PID 898055)** — westd-38929 版本已到 T7/10（2h完成），cqa1 版本才 T4/10（4h）。Kill cqa1 版本释放 GPU 可以跑其他实验

3. **westd-27271 GPU0 空闲** — 可立即调度新实验

4. **westd-41074 GPU1 约30分钟后空闲** — OV Random k=0.75 Long 即将完成

是否执行 kill 操作？

---
