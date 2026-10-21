# code exp sdgd routing strategies

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_sdgd_routing_strategies_20260517T055751_result.json`
- **Structured JSON:** [`ef2d7edfe0c846d2ea66.json`](../../sessions/ef/ef2d7edfe0c846d2ea66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇总：

## SDGD Routing Strategies 实验结果

| Strategy | Accuracy | vs Single-Pass | Recovery |
|----------|----------|----------------|----------|
| single_pass (baseline) | 50.4% | — | 0% |
| random | 14.7% | -35.7pp | -162% |
| max_conf_all | 27.7% | -22.7pp | -103% |
| **max_conf_positive** | **36.5%** | **-14.0pp** | **-64%** |
| **none_aware** | **36.5%** | **-14.0pp** | **-64%** |
| margin_positive | 35.9% | -14.5pp | -66% |
| oracle (上界) | 72.4% | +22.0pp | 100% |

**核心发现：所有 practical routing 策略都比 single-pass 更差。** Recovery 全部为负值。

**根本原因**：模型的 "none" 检测能力太弱。分布如下：
- 73.4% 的 instances 有 3-5 个组同时做出 positive prediction
- 仅 7% 的 instances 恰好只有 1 个组做 positive prediction（exclusive positive 精度也只有 42%）
- 各组对 out-of-group instances 的 none-rate 只有 20-40%

**结论**：在 structured decoding + enum constraint 下，模型被迫从候选集中选一个答案，即使正确答案不在候选集中也会给出自信的错误预测。这使得 confidence-based routing 和 none-aware routing 均失效。Oracle routing 的 +22pp 增益不可通过 post-hoc 策略恢复——schema decomposition 在没有可靠路由的情况下反而有害。

---
