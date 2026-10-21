# ssh fix local judge paths v2

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-local-judge-paths-v2_20260524T084721_result.json`
- **Structured JSON:** [`4bf66b918c9f377dfd47.json`](../../sessions/4b/4bf66b918c9f377dfd47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。汇总：

### 各 local judge 数据位置

| Judge | 数据位置 | 行数 | 状态 |
|-------|---------|------|------|
| Qwen2.5-72B | `output_n17_qwen2.5-72b-local/` | 692 | 已通过 symlink 映射到 `results/qwen2.5-72b-local_n17/` |
| LLaMA-3.3-70B | `results/llama-3.3-70b-local_n17/` | 1041 | 标准路径，正常 |
| Mistral-Large-2 | `results/mistral-large-2-local_n17/` | 82 | 标准路径，正常（数据量较少，可能仍在采集） |

### 执行的修复

1. **Symlink**：`results/qwen2.5-72b-local_n17` → `../output_n17_qwen2.5-72b-local`，collect.py 继续写入原目录不受影响
2. **Config 修正**：`config_qwen2.5-72b_local_n17.yaml` 的 `output_dir` 改为标准路径 `results/qwen2.5-72b-local_n17/`（symlink 保证实际写入位置不变）
3. **LLaMA/Mistral**：config 和实际路径一致，无需修改

### prepare_n17_data.py 兼容性

该脚本已同时扫描 `results/*_n17/` 和 `output_n17_*/` 两种模式，且有去重逻辑。即使没有 symlink 也能找到 Qwen 数据。symlink 主要是为其他可能只扫 `results/` 的脚本兜底。

---
