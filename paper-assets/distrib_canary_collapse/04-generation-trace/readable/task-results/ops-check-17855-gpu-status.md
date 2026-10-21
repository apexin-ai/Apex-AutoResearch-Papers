# ops check 17855 gpu status

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-17855-gpu-status_20260522T200540_result.json`
- **Structured JSON:** [`85b7398fbac97baf3796.json`](../../sessions/85/85b7398fbac97baf3796.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

## westd-17855 GPU Status

| GPU | Util | VRAM | PID | Experiment | Status |
|-----|------|------|-----|------------|--------|
| cuda:0 | 87% | 31.8/97.9 GB | 679656 | t15_a060_v2 | RUNNING |
| cuda:1 | 90% | 31.8/97.9 GB | 680095 | t15_a050_v3 | RUNNING |
| cuda:2 | 0% | 0/97.9 GB | — | — | **空闲** |
| cuda:3 | 88% | 11.2/97.9 GB | 714525 | t10_a075_v2 (--start_gen 10, 11min ago) | RUNNING (restarted) |
| cuda:4 | 100% | 30.9/97.9 GB | 679204 | **t10_a045_s42_fp32_14b** | RUNNING (6h59m) |
| cuda:5 | 89% | 31.8/97.9 GB | 680608 | t15_a045 | RUNNING |

## t10_a045 处理结果

实验**已经在跑**，PID 679204，运行 ~7 小时。gen_0–gen_5 完成，gen_6 训练中（10 代中第 7 代）。Log: `/tmp/train_scale_14b_t10_a045_s42.log`。Registry 此前无记录，已创建并更新为 RUNNING。

## 磁盘

`/root/autodl-tmp/`: **350G 总量，324G 已用，27G 剩余 (93%)**。偏紧，但当前实验应能完成（剩余 3 代 checkpoint 约需 ~15G）。需注意 cuda:3 的 t10_a075_v2 重启后也会写 checkpoint。

## 注意事项
- cuda:2 空闲，可调度新任务
- cuda:3 上 t10_a075_v2 被另一个 Worker 重启（`--start_gen 10`），刚开始 11 分钟
- 磁盘 93% 接近警戒线，后续提交任务前须复查

---
