# ops westd38929 collect and fill

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-collect-and-fill_20260521T034203_result.json`
- **Structured JSON:** [`37ccc178503ad1ef7ffb.json`](../../sessions/37/37ccc178503ad1ef7ffb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full summary:

---

## westd-38929 结果

### OpenVLA random k=0.95 v2 (cuda:0) — 已完成 ✓

**Overall SR: 69.2% (346/500)** | Wilson 95% CI: ~[65.0%, 73.1%]

| Task | SR |
|------|-----|
| T1 alphabet soup | 80% (40/50) |
| T2 cream cheese | 42% (21/50) |
| T3 salad dressing | 70% (35/50) |
| T4 bbq sauce | 42% (21/50) |
| T5 ketchup | 88% (44/50) |
| T6 tomato sauce | 84% (42/50) |
| T7 butter | 60% (30/50) |
| T8 milk | 68% (34/50) |
| T9 chocolate pudding | 66% (33/50) |
| T10 orange juice | 92% (46/50) |

结果已保存: `eval_results/openvla_random_k095_seed42_v2.json`

### OpenVLA random k=0.7 v2 (cuda:1) — 进行中

Task 10, Ep 30/50。PID 159765, 15.9GB on cuda:1。

已完成 9 tasks: 72%, 20%, 56%, 38%, 64%, 52%, 20%, 24%, 34% (190/450 = 42.2%)

预计还需 ~10 min 完成。

### cuda:2/3 状态

- **cuda:2**: 空闲 (0%, 1MiB)
- **cuda:3**: 空闲 (0%, 1MiB) — OFT baseline 已死 (T0 0%, T1 0%@Ep27 后崩溃，double LoRA bug 导致)

**SmolVLA Spatial 无法启动** — checkpoint `libero_full_ft/step_099999/checkpoint.pt` 不存在于 westd-38929，只有 `openvla_sc_m128`。需先传输 SmolVLA checkpoint 才能跑。

### OFT Worker 状态

westd-38929 上无任何 OFT 相关进程运行。

---

## westd-41074 π0.5 Eval

**π0.5 baseline (cuda:1)** — PID 754154 运行中，10.6GB

进度: Task 2, Ep 20/50。T0: **0%**, T1: **0%**。刚开始 T2 也是 0/20。

前 2 个 task 全部 0% SR，结果值得关注。

GPU 2 (PID 68539, 28.5GB) 和 GPU 3 (PID 738642, 27.5GB) 有其他进程在运行。

---
