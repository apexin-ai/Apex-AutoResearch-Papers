# code random evidence baseline

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_random_evidence_baseline_20260513T073235_result.json`
- **Structured JSON:** [`ce390d7c23887ae423b7.json`](../../sessions/ce/ce390d7c23887ae423b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| Metric | SFT v5 | Random Evidence | 说明 |
|--------|--------|-----------------|------|
| RE-F1  | 0.4337 | **0.4337** | 完全一致，符合预期（只改 evidence 不影响关系判断） |
| Evi-F1 | 0.3652 | **0.0903** | 下降 75%，随机 evidence 几乎无信息 |
| AP     | 0.9529 | **0.9529** | 不变，因为随机采样的 evidence 仍然非空 |

RE-F1 和 AP 完全不变，验证了实现的正确性。Evi-F1 从 0.3652 降至 0.0903，是 random lower bound。结果保存在 `outputs/random_evidence/eval_results_shuffled.json`。

---
