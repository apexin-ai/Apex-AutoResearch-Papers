# diagnose eval xvla l2norm k03 goal v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_xvla_l2norm_k03_goal_v2_20260523T190124_result.json`
- **Structured JSON:** [`c63d3aa7100cb35c3f0d.json`](../../sessions/c6/c63d3aa7100cb35c3f0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

**两层原因：**

1. **首次运行**: `--mode l2norm` 拼写错误（应为 `l2_norm`），argparse 直接退出 (exit code 2)。已在后续重试中修正。

2. **v2/v3 被监控系统误杀**: 修正参数后 v2/v3 运行完全正常（v2 跑了 22 分钟到 Task 2 Ep 46，v3 跑了 16 分钟到 Task 2 Ep 10），但因 eval 脚本没有 W&B 日志和 sentinel 文件输出，监控框架将它们判定为 "process dead" 并 SIGKILL 终止。证据：日志无任何错误、无 .exit 文件（trap 未触发）、tmux session 消失、v2/v3 在同一时间点被杀。

**当前状态**: v4 正在 GPU 3 运行（Task 0 Ep 14），但有再次被误杀的风险。建议调整监控系统的健康检查策略（改为检测日志文件更新时间），或在 eval 脚本中加入 sentinel/heartbeat 输出。

---
