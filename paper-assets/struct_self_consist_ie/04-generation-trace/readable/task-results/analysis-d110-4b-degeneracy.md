# analysis d110 4b degeneracy

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d110_4b_degeneracy_20260516T080931_result.json`
- **Structured JSON:** [`ccd88647e72873438974.json`](../../sessions/cc/ccd88647e72873438974.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| Config | N | Const F1 | Const SJ | Random F1 | MBR F1 | Oracle F1 | Gap Closed | ρ median | ρ>0 | ρ>0.3 |
|--------|---|----------|----------|-----------|--------|-----------|------------|----------|-----|-------|
| **Qwen3-4B CoNLL NER** | 2756 | 90.6% | 89.8% | 0.7339 | 0.7749 | 0.9451 | 19.4% | 0.936 | 64.2% | 62.1% |
| **Qwen3-4B SciERC NER** | 529 | 10.4% | 7.0% | 0.5965 | 0.6510 | 0.8123 | 25.2% | 0.550 | 69.8% | 60.9% |
| **Qwen3-4B SciERC RE** | 397 | 25.7% | 6.8% | 0.3875 | 0.4741 | 0.7401 | 24.5% | 0.495 | 67.8% | 56.8% |

关键发现：
- **CoNLL 高度退化**：4B 在 CoNLL 上 90.6% 的 instance 所有 8 个 sample 的 F1 完全相同，几乎没有 MBR 可利用的空间。但在剩余的非退化 instance 上，ρ 中位数高达 0.936。
- **SciERC NER/RE 退化较低**：10.4%/25.7% constant F1，MBR 能 close 25% 左右的 oracle gap，ρ 中位数约 0.5。

产出保存在 `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/d110_4b_degeneracy/`（results.json + table.md + analyze_4b_degeneracy.py）。

---
