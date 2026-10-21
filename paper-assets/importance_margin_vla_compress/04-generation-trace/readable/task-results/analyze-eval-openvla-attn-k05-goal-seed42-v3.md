# analyze eval openvla attn k05 goal seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_attn_k05_goal_seed42_v3_20260527T102033_result.json`
- **Structured JSON:** [`7c673066e9767a099643.json`](../../sessions/7c/7c673066e9767a099643.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。汇总如下：

## eval_openvla_attn_k05_goal_seed42_v3 — Metrics

| 指标 | 值 |
|------|-----|
| **Overall SR** | **42.8%** (214/500) |
| 运行时间 | 474.4 min (~7.9h) |
| 服务器 | cqa1-33015 GPU:3 |
| EXIT_CODE | 0 (正常完成) |

### Per-task SR

| Task | SR (%) | 成功/总数 |
|------|--------|----------|
| T1 open_middle_drawer | 18 | 9/50 |
| T2 put_bowl_on_stove | 54 | 27/50 |
| T3 put_wine_bottle_on_cabinet | **70** | 35/50 |
| T4 open_drawer_put_bowl | 6 | 3/50 |
| T5 put_bowl_on_cabinet | 52 | 26/50 |
| T6 push_plate_to_stove | 60 | 30/50 |
| T7 put_cream_cheese_in_bowl | 42 | 21/50 |
| T8 turn_on_stove | **78** | 39/50 |
| T9 put_bowl_on_plate | 40 | 20/50 |
| T10 put_wine_bottle_on_rack | 8 | 4/50 |

### Goal k=0.5 三方法对比

| Method | SR (%) |
|--------|--------|
| L2norm | 43.4 |
| **Attention** | **42.8** |
| Random | 52.2 |

无异常，无 warning（仅 robosuite 标准提示）。Attention 和 L2norm 在极端压缩 (k=0.5) 下表现接近，Random 反而最高——说明在 Goal suite 极端压缩端，informed pruning 不优于 random，三方法趋于收敛但 random 略好。

---
