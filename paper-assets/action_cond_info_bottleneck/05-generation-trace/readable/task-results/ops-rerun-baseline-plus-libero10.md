# ops rerun baseline plus libero10

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rerun-baseline-plus-libero10_20260516T021048_result.json`
- **Structured JSON:** [`d1de7dcebae85efe6a38.json`](../../sessions/d1/d1de7dcebae85efe6a38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果和当前状态：

## 诊断

1. **无 OOM killer 记录** — `dmesg` 没有 oom/kill 相关日志
2. **无 error/traceback** — 日志中只有正常的 rollout 进度输出，没有 Python 异常
3. **可能原因**：进程被外部信号杀死（如 SSH 断连导致的 shell 终止）或 MuJoCo/EGL 渲染段错误（segfault 不留 Python traceback）

## 当前状态

**libero_10 eval 已经在重跑中** — `run_eval_plus_v2.sh` 脚本自动重启了 eval：
- **PID 675231**，启动于 09:24，cuda:0，GPU 占用 6.6GB
- libero_10 进度：**64/500 rollouts 完成**（task 0 已完成 50 ep，task 1 进行中约 14/50 ep）
- 当前 rollout 在 step ~250/520
- 预估每 rollout ~1min，剩余 ~436 rollouts ≈ **7+ 小时**

## GPU 负载

| GPU | 已用/总量 | 进程 |
|-----|-----------|------|
| cuda:0 | 22.8/97.9 GB | PID 675231 (eval, 6.6GB) + PID 682233 (v5_div_reg 训练, 16.2GB) |
| cuda:1 | 17.9/97.9 GB | PID 508625 (std eval, 2.1GB) + PID 694353 (v5_stopgrad_entropy 训练, 16.3GB) |

**不需要手动重跑** — eval 已在运行，预计今天下午完成。需要我设置定时检查进度吗？

---
