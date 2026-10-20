# code entity consensus

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_entity_consensus_20260518T173346_result.json`
- **Structured JSON:** [`e040f5f9ee03d19c0364.json`](../../sessions/e0/e040f5f9ee03d19c0364.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果总结：

**FewNERD** — consensus (high=0.5) 是唯一一个超越 greedy 的配置：**0.7583 vs 0.7478**（+1.05pp），也超过 LP selection (0.7666) 还差一点。高阈值损害性能严重（0.8→0.6780）。

**SciERC** — consensus (high=0.6) 接近 greedy（0.6444 vs 0.6439），但都不超过 LP selection (0.6501)。N=8 样本数有限，consensus 优势不明显。

**CoNLL** — greedy 最强 (0.9070)，consensus 全部配置都低于 greedy。该数据集 degeneracy 高（样本间差异小），consensus 无法提供增量。

**共性规律**：
- 阈值越高，F1 越低（保守 → 高 precision 但低 recall）
- LP-weighted medium zone 在低阈值时有正贡献
- Span-based majority vote 全面弱于 greedy，consensus 在 FewNERD 上有改善但幅度有限

输出文件：
- JSON: `/root/autodl-tmp/struct_self_consist_ie/output/entity_consensus_results.json`
- Markdown: `/root/autodl-tmp/struct_self_consist_ie/output/entity_consensus_report.md`
- 脚本: `code/entity_consensus.py`

---
