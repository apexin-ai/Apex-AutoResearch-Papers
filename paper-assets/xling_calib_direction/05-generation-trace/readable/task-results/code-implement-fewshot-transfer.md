# code implement fewshot transfer

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_implement_fewshot_transfer_20260521T010144_result.json`
- **Structured JSON:** [`403371dd1d9840ce02bf.json`](../../sessions/40/403371dd1d9840ce02bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法正确。`torch` 本地没装所以 `--help` 跑不了，但在服务器上会正常工作。

最终文件变更：
1. **顶部新增 import**：`LogisticRegression` 和 `StandardScaler`
2. **`parse_args()`**：添加 `--n_few_shot` 参数（逗号分隔的数量列表）
3. **main() language loop**：在 Procrustes 之后、CSV 写入之前，添加 few-shot block — 对每个 `n_fs`，从目标语言抽 N 条与英文全量数据合并重训 probe，用剩余目标数据评估，结果写入 `few_shot_{N}` method

---
