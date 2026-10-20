# train encoder ablation dual

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_encoder-ablation-dual_20260514T134503_result.json`
- **Structured JSON:** [`b1a369ae73055ed6721c.json`](../../sessions/b1/b1a369ae73055ed6721c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 提交结果

| 任务 | GPU | PID | tmux session | 日志 |
|------|-----|-----|-------------|------|
| e5-large probe | cuda:0 | 54528 | `encoder-ablation-probe-e5` | `~/runs/agent_progress_probe/encoder-ablation-probe-e5.log` |
| bge-m3 probe | cuda:1 | 54609 | `encoder-ablation-probe-bge-m3` | `~/runs/agent_progress_probe/encoder-ablation-probe-bge-m3.log` |

### gte-large 诊断
gte-large embedding **严重不完整**：仅 10 个 windows（应为 54809），文件 402K。格式正确但生成过程提前终止，需重新生成。诊断已注册为 artifact。

---
