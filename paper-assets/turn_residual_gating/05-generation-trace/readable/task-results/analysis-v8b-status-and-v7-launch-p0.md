# analysis v8b status and v7 launch p0

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v8b_status_and_v7_launch_p0_20260521T122942_result.json`
- **Structured JSON:** [`13f178f696ef2ad19227.json`](../../sessions/13/13f178f696ef2ad19227.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v7 launch 脚本已就绪。

**v8b SS s123 状态汇报：**

| 项目 | 值 |
|------|-----|
| 进度 | Epoch 2, Step 2550/3000 (85%) |
| 运行时间 | 8h 1m |
| 当前 Loss | ~0.64–1.07 (L_NTP)，L_GAR ≈ 0.001 |
| Gate mean | 0.93 (std=0.054) |
| Gate profile | L5 最低 (0.73)，L27 最高 (1.00)，呈现类 U-shape |
| SS ratio | 0.50 (已达 max) |
| ETA | **~1.4 小时**（按 5.3 steps/min 推算剩余 450 步）|

**与 s42 中间对比：** gate 行为与 s42 高度一致（s42 final gate_mean=0.959，s123 当前 0.93 且还在上升），训练正常。

**v7 TG s123：** 脚本已就绪，需等 v8b 完成后启动（GPU 当前占满 98%/39GB）。

**建议：** ~1.5 小时后再检查。v8b 完成后立即提取最终指标、更新 registry、启动 v7 TG s123。需要我设一个定时回来检查吗？

---
