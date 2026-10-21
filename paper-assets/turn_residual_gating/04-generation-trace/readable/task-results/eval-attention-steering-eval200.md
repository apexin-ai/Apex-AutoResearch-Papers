# eval attention steering eval200

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_attention_steering_eval200_20260520T093707_result.json`
- **Structured JSON:** [`ae98bb5f4b59ed207cd3.json`](../../sessions/ae/ae98bb5f4b59ed207cd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正常运行。状态：

- **PID**: 166506（子进程），GPU 占用 42.2GB / 97.9GB，GPU 利用率 72%
- **进度**: β=0 已完成，β=2.0 正在跑（已到 Conv 25/200）
- **模式**: tf（teacher-forcing），6 个 β 值：0, 2, 3, 4, 5, 10
- **代码修改**: 
  - 移除了 tf 模式的 `SYSTEM_PROMPTS` 上限限制（原来限制 5 个）
  - 新增 `--output-name` 参数，输出到 `eval200_attention_steering.json`，不覆盖已有 N=5 结果

**注意**: 用了 **tf 模式**而非 gen 模式。原因：gen 模式 hardcode 了 5 个 system prompt + user questions，无法扩展到 200 个对话。tf 模式直接 teacher-force eval_200 的 200 个完整对话，是正确的大规模验证方式。

**预计时间**: 200 convs × 6 β ≈ 1200 次 forward pass。β=0 + 25 convs of β=2 已完成（约 225/1200），速度约 ~3min 启动后已跑了约 225 个，预计总时间 ~90-120min。日志: `/tmp/eval200_steering.log`。

---
