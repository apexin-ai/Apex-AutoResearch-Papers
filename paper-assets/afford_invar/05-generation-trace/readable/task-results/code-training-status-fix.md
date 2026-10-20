# code training status fix

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_training-status-fix_20260519T224853_result.json`
- **Structured JSON:** [`ce8c1dfe831b512b7c42.json`](../../sessions/ce/ce8c1dfe831b512b7c42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

**训练状态：已重新提交，正常运行中**

| 项目 | 值 |
|------|-----|
| PID | 110152 |
| 当前 step | ~56（约 30 秒前），速度 ~2.2 it/s |
| 预计总时间 | ~2.5h（20000 步） |
| GPU 0 显存 | 24765 MiB，利用率 86% |
| 日志文件 | `/root/afford_invar/results/phase1_train_v2.log` |

**崩溃原因**：上次提交命令仍包含 `--adapter_tmp_dir` 参数，argparse 直接拒绝，exit code 2。训练 0 步完成，无 checkpoint。

**GRAD MONITOR（step 0）**：
- L_consist=0.3492，consist_grad_norm=2.36，total_grad_norm=38.10，grad_ratio=0.062

**最近 loss（step 50-56）**：
- L_act 范围 0.49~0.94，L_con 下降趋势（0.006→0.003），L_tot 跟随 L_act
- para_hit=100%（paraphrase 匹配正常）
- hm_ent 从 6.31 上升到 6.39（affordance heatmap 熵在增加）

**500 步 checkpoint**：未到，预计 ~4 分钟后到达。

---
