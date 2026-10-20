# ops verify cuda0 resubmit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-cuda0-resubmit_20260514T231054_result.json`
- **Structured JSON:** [`673a5d014732ce7e11d3.json`](../../sessions/67/673a5d014732ce7e11d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**重要发现：原始实验 exp1-isr-b03-s43 实际上已完成全部 500 步训练。**

- reward_log.jsonl 记录到 step 500（最后时间戳 23:00:56）
- checkpoint-500 和最终模型权重都已保存完整
- SIGHUP 发生在训练完成之后（可能是 tmux/连接断开）

**不需要重新提交 r2。** 原始实验结果完好，output_dir 有完整的最终模型（~31GB）。

建议下一步：
1. 用 eval_sta.py 对 `/root/autodl-tmp/outputs/exp1_isr_b03_s43/` 做统一评估
2. 将 exp1-isr-b03-s43 的 registry 状态更新为 COMPLETED
3. 取消 exp1-isr-b03-s43-r2 的 PREPARING 状态

是否需要执行这些操作？

---
