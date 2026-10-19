# ssh emergency gpu launch

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_emergency-gpu-launch_20260517T203117_result.json`
- **Structured JSON:** [`b040b774499353ca0595.json`](../../sessions/b0/b040b774499353ca0595.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态汇总：

## v7.2 Eval 结果（3/4 suites 已完成）

| Suite | α=0.0 | α=1.0 |
|-------|-------|-------|
| libero_spatial | 59.4% | 61.0% |
| libero_object | 65.6% | 66.2% |
| libero_goal | 78.6% | 78.0% |
| libero_10 | **进行中 (5/10 tasks)** | **进行中 (5/10 tasks)** |

## 阻塞项

两个 eval 进程仍在占用 GPU（PID 40598 → GPU 0, PID 44022 → GPU 1），已运行约 7 小时，libero_10 各完成 50%。按 C004 约束，不能在有活跃进程的 GPU 上启动新任务。

## v7.3 训练准备

- `scripts/run_v73_connector_lora.sh` 存在
- `scripts/run_connector_only.sh` 存在
- 日志目录 `/root/runs/action_cond_info_bottleneck/` 存在

## 需要你确认

libero_10 eval 预计还需 ~2-3 小时完成。两个选项：

1. **Kill 两个 eval 进程，立即启动训练** — 丢失 libero_10 部分结果，有 3 suite 数据可用
2. **等 eval 完成后再启动训练** — 完整 4-suite 结果，但延迟 2-3 小时

选哪个？

---
