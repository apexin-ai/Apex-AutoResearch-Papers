# code encoder ablation probe train

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_encoder-ablation-probe-train_20260514T134014_result.json`
- **Structured JSON:** [`5d3303e9bc80e292df9f.json`](../../sessions/5d/5d3303e9bc80e292df9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练任务已提交。

| 实验 | GPU | PID | 日志 |
|------|-----|-----|------|
| `encoder-ablation-probe-e5large` | cuda:0 | 53503 | `~/runs/agent_progress_probe/encoder-ablation-probe-e5large.log` |
| `encoder-ablation-probe-bgem3` | cuda:1 | 53646 | `~/runs/agent_progress_probe/encoder-ablation-probe-bgem3.log` |

**数据概况：**
- 总窗口数: 54809
- conf>=2 过滤后训练窗口数: **15401**
- Embedding 维度: **1024**（两个 encoder 相同）
- 实例数: 2285
- 训练/验证/测试按 instance-level split（seed=42），与 probe_001 使用相同的 `split_by_instance` 逻辑，保证 test set 一致

---
