# ops status check cqa1 westd27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-check-cqa1-westd27271_20260520T065619_result.json`
- **Structured JSON:** [`28032baf1b03750c8bb4.json`](../../sessions/28/28032baf1b03750c8bb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。汇总：

---

## cqa1-33015 — 3 个 Eval（全部 ALIVE）

GPU 显存：GPU0=3478 MiB, GPU1=3448 MiB, GPU2=3446 MiB, GPU3=1 MiB

### eval_smart_compress_m128_seed43 (GPU1)
**进度：Task 8/10, Ep 456/500** — 预计 ~1h 完成

已完成 task SR：

| Task | 描述 | SR |
|------|------|----|
| 0 | alphabet soup → basket | 64.6% |
| 1 | cream cheese → basket | 32.2% |
| 2 | salad dressing → basket | 61.4% |
| 3 | bbq sauce → basket | 43.2% |
| 4 | ketchup → basket | 34.8% |
| 5 | tomato sauce → basket | 44.2% |
| 6 | butter → basket | **71.6%** |
| 7 | milk → basket | 60.4% |
| 8 | chocolate pudding (进行中) | ~456 ep |

**前 8 task 均值：51.55%** — 确认之前 47.24% running avg 是低估（只看了部分 ep），最终 10-task 均值预计在 **50-53%** 区间。

### eval_smart_compress_m16_seed43 (GPU2)
**进度：Task 8/10, Ep 471/500** — 预计 ~45min 完成

| Task | SR |
|------|----|
| 0 | 42.8% |
| 1 | 47.4% |
| 2 | 66.2% |
| 3 | 48.4% |
| 4 | **74.2%** |
| 5 | 40.0% |
| 6 | **79.2%** |
| 7 | 69.8% |

**前 8 task 均值：58.5%** — m16 比 m128 高约 7pp。

### eval_smart_compress_m16_seed44 (GPU0)
**进度：Task 7/10, Ep 207/500** — 预计 ~3h 完成

| Task | SR |
|------|----|
| 0 | 38.0% |
| 1 | 70.0% |
| 2 | 55.2% |
| 3 | 42.0% |
| 4 | 64.8% |
| 5 | 32.8% |
| 6 | 73.2% |

**前 7 task 均值：53.7%**

---

## westd-27271 — 2 个 Training（全部 ALIVE）

GPU 显存：GPU0=32285 MiB, GPU1=25991 MiB（5× 进程，4 DDP workers）

### train_openvla_sc_m32_seed42 (GPU1)
- **Step 13050/100000** (13.05%)
- loss=2.478, lr=9.65e-05, grad=1.75, sps=0.5
- 从 08:16 开始运行，稳定

### train_openvla_sc_m128_seed42_v2 (GPU0, 4×DDP)
- **Step 22900/100000** (22.9%)
- loss=2.894, lr=8.87e-05, grad=2.30, sps=0.5
- 从 02:38 开始运行，稳定

---

**结论**：5 个任务全部存活，无崩溃。m128_seed43 eval 前 8 task 均值 51.55%，比预期好；m16_seed43 更强 (58.5%)。两个 westd 训练都在正常推进。

---
