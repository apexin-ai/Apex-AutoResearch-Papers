# audit westd41074 gpu state

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd41074_gpu_state_20260525T131646_result.json`
- **Structured JSON:** [`5280e36a4b181d133f8b.json`](../../sessions/52/5280e36a4b181d133f8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 审计结果 — westd-41074

```
GPU 0: eval_openvla_attn_k09_object_seed42      PID=173847  MEM=15965MiB/97887MiB  RUNNING (59% util)
GPU 1: eval_openvla_l2norm_k05_goal_seed42       PID=173920  MEM=15946MiB/97887MiB  RUNNING (57% util)
GPU 2: eval_openvla_random_k05_object_seed42     PID=259177  MEM=15961MiB/97887MiB  RUNNING (52% util)
GPU 3: eval_openvla_l2norm_k05_spatial_seed42    PID=264356  MEM=16028MiB/97887MiB  RUNNING (56% util)
```

**GPU 2 发现：** registry 中记录的两个 pi05 实验（`eval_pi05_l2norm_k03_long_seed42_postfix` 和 `eval_pi05_random_k085_long_seed43_postfix`）均已不在运行。当前 GPU 2 跑的是一个新实验 `openvla_random_k05_object_seed42`（启动于 20:30）。4 个 GPU 全部在用，无空闲。

---

## paper_figures.py 运行结果

3 个图全部生成成功：
- `crossover_heatmap.pdf` — 33K
- `disruption_curve.pdf` — 40K
- `cv_scatter.pdf` — 30K

无报错，从 546 条实验记录中解析出 160 个唯一数据点。

---
