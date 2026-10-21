# analysis v8b completion and v7 launch

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v8b_completion_and_v7_launch_20260521T150808_result.json`
- **Structured JSON:** [`175e7047f138b2aab879.json`](../../sessions/17/175e7047f138b2aab879.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## 1. v8b SS s123 最终状态

**状态**: ✅ DONE (success)，训练时间 38773s (~10.8h)

| 指标 | s123 | s42 (参考) |
|------|------|-----------|
| final_loss | 0.9316 | 0.933 |
| final_gate_mean | 0.9505 | 0.959 |
| final_gate_std | 0.0508 | - |
| final_gate_min | 0.7383 | - |
| final_gate_max | 1.0000 | - |
| SS used ratio | 37.1% | - |

**Epoch 趋势**: 1.009 → 0.944 → 0.932（持续下降，正常收敛）

**Gate Profile (step 3000)**: L5 最低 (0.738)，L27 最高 (1.000)，与 s42 的 V 型 profile 一致。

**结论**: s123 与 s42 高度一致，seed robustness 确认。

## 2. v7 TG s123 启动状态

- **PID**: 245628
- **服务器**: westd-20861, GPU 0
- **初始日志正常**: Step 0 已打印，Loss=1.6255, Gate=0.8118
- **输出目录**: `/root/turn_residual_gating/runs/phase2_tg_s123_v7`
- **日志**: `/root/turn_residual_gating/logs/v7_tg_s123.log`
- **Registry**: RUNNING

## 3. Cron 诊断

- **无活跃 cron**。v8b_ss_s123 没有关联 cron 监控，训练是靠本次手动检查确认完成的。
- v7_tg_s123 也未设置 cron，预计 ~10.8h 后完成（约 UTC 05-22 02:00）。

---
