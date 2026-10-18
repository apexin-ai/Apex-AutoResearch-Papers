# harvest dense window batch1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_dense_window_batch1_20260528T085218_result.json`
- **Structured JSON:** [`f11c3d872fe2f06e5339.json`](../../sessions/f1/f11c3d872fe2f06e5339.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part 1: 收割完成

| exp_id | GPU | SR% | 状态 |
|--------|-----|-----|------|
| eval_pi05_random_k085_long_seed46_strict_w41 | w41:cuda:0 | **44.8%** | DONE ✓ |
| eval_pi05_attn_k085_long_seed46_strict_w38 | w38:cuda:3 | **50.4%** | DONE ✓ |

**Per-task (Random k=0.85):** T0=50, T1=42, T2=46, T3=76, T4=20, T5=40, T6=40, T7=52, T8=6, T9=76

**Per-task (Attn k=0.85):** T0=12, T1=62, T2=44, T3=52, T4=44, T5=72, T6=68, T7=60, T8=8, T9=86

### Part 2: GPU 空闲确认

| 服务器 | GPU | 状态 |
|--------|-----|------|
| westd-27271 | cuda:1 | **空闲** (无进程) |
| westd-41074 | cuda:0 | **空闲** (无进程) |
| westd-41074 | cuda:2 | **空闲** (无进程) |
| westd-38929 | cuda:3 | **空闲** (无进程) |

### Part 3: w41 利用率

| GPU | Util | Mem Used | 状态 |
|-----|------|----------|------|
| 0 | 0% | 1 MiB | 空闲 |
| 1 | 36% | 10306 MiB | 活跃 — eval_pi05_random_k07_long，正在 T8 ep40 (8%) |
| 2 | 0% | 1 MiB | 空闲 |
| 3 | 27% | 10448 MiB | 活跃 — eval_pi05_l2norm_k085_long，正在 T2 (92.7%) |

**利用率 36%/27% 属于 eval 推理正常水平**，不是卡住。random_k07 已到 T8/10 接近完成，l2norm_k085 刚到 T2/10 还需较长时间。

**总计可用 GPU: 4 张** (w27:cuda1, w41:cuda0, w41:cuda2, w38:cuda3)

---
