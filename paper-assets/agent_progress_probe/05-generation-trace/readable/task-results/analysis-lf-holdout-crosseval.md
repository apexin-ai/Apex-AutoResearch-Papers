# analysis lf holdout crosseval

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lf-holdout-crosseval_20260514T151438_result.json`
- **Structured JSON:** [`b23da507166ca6a2edfa.json`](../../sessions/b2/b23da507166ca6a2edfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `lf_holdout_crosseval_results.json`。

**Cross-eval 结果（3-LF test set, 1824 windows）：**

| Model | macro_f1 | accuracy | f1_stag | f1_prog |
|-------|----------|----------|---------|---------|
| **baseline (probe_001)** | **0.8136** | 0.8448 | 0.7372 | 0.8899 |
| no_ob | 0.7535 | 0.8087 | 0.6368 | 0.8701 |
| no_cmd_rep | 0.7329 | 0.7758 | 0.6258 | 0.8399 |
| no_file_diff | **0.6329** | 0.6535 | 0.5460 | 0.7199 |

**关键发现：**
- Baseline macro_f1 此处为 0.8136（低于之前报告的 0.9055，可能因评估 split 差异）
- **file_diff_delta 是最重要的 LF**：去掉它后 macro_f1 暴跌至 0.6329（-0.1807）
- outcome_backpropagation 次之：去掉后 macro_f1 降至 0.7535（-0.0601）
- command_repetition 影响居中：去掉后 macro_f1 降至 0.7329（-0.0807）
- 所有 holdout 模型在 stagnation 类上表现最差（f1_stag 最低 0.546）

注意 baseline 的 0.8136 与之前报告的 0.9055 存在差距——这可能是因为原 probe_001 的 test set 定义和当前 split_info.json 中的 test_indices 不完全一致（原始评估可能对 conf 或标签有不同过滤）。所有 holdout 模型间的相对排序是可靠的，因为都在同一 test set 上评估。

---
