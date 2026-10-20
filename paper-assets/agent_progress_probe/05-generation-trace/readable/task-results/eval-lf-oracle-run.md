# eval lf oracle run

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_lf_oracle_run_20260514T090024_result.json`
- **Structured JSON:** [`70fe0208fee4b4f5375e.json`](../../sessions/70/70fe0208fee4b4f5375e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。结果：

### LF Coverage (Test Set)
| LF | Coverage |
|---|---|
| file_diff_delta | 90.1% |
| command_repetition | 97.4% |
| outcome_backpropagation | 42.4% |
| All non-abstain agree | 72.5% |

### 评估结果

| Method | Macro-F1 | Accuracy | F1(stag) | F1(prog) |
|---|---|---|---|---|
| **GRU Probe (ref)** | **0.9055** | — | — | — |
| LF Majority Vote | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| **Single LF: command_repetition** | **0.9451** | **0.9589** | 0.9175 | 0.9726 |
| LF Any-Stagnation | 0.8544 | 0.8712 | 0.8050 | 0.9038 |
| LF All-Agreement | 0.7659 | 0.8542 | 0.6222 | 0.9096 |
| Single LF: file_diff_delta | 0.7636 | 0.8531 | 0.6182 | 0.9090 |
| Single LF: outcome_backpropagation | 0.7510 | 0.7955 | 0.6458 | 0.8563 |

### 关键发现

- **LF Majority Vote = 1.0** — 如预期，这是 tautological ceiling（ground truth 就是 majority_label）
- **command_repetition 单个 LF (0.9451) 超过了 GRU Probe (0.9055)**，差距 +0.0396。这意味着仅靠"命令是否重复"这一个启发式规则就能比训练出的 GRU 探针更准
- 其他 LF 变体（Any-Stagnation 0.8544, All-Agreement 0.7659, file_diff_delta 0.7636, outcome_backpropagation 0.7510）均低于 GRU Probe

command_repetition 的压倒性表现值得关注——97.4% 的 coverage + 0.9451 的 macro-F1，说明在 conf≥2 的高置信子集上，命令重复模式本身就是一个极强的 stagnation 信号。GRU Probe 在这个子集上并未超越这个简单规则。

---
