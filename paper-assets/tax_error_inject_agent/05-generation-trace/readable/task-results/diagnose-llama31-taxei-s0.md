# diagnose llama31 taxei s0

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_llama31-taxei-s0_20260516T102807_result.json`
- **Structured JSON:** [`76f57c09aa5f46858f98.json`](../../sessions/76/76f57c09aa5f46858f98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：SIGHUP（SSH 断连/tmux session 被终止），非 OOM。**

关键事实：
- v0 正常跑完 epoch 1（1129 steps，43 min），保存 checkpoint 后被外部信号杀死
- 显存全程稳定 30.73/32 GiB，loss 从 1.76 降到 0.46，训练逻辑无异常
- v1 重试已在运行中（step ~260/3387），状态正常
- 完整 checkpoint 可用于恢复：`v0-20260516-171606/checkpoint-1129/`

已更新 registry failure_reason 并注册诊断报告（art_20260516_3417d1）。

---
