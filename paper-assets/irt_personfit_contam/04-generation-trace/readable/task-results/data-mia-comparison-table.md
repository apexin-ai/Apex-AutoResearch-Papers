# data mia comparison table

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_mia-comparison-table_20260524T074917_result.json`
- **Structured JSON:** [`7fc5c2ad66d9522ee7d5.json`](../../sessions/7f/7fc5c2ad66d9522ee7d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/rebuttal/mia_comparison_table.tex`。

### 数据汇总

| Stage | Min-K%10 AUC | Min-K%++ AUC | Loss AUC | lz\*\_seen | lz\*\_unseen | |Δ lz\*| |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|
| Base | 0.493 | 0.488 | 0.486 | 2.50 | 5.43 | **2.93** |
| SFT | 0.611 | 0.569 | 0.592 | −0.40 | 3.28 | **3.67** |
| GRPO | 0.493 | 0.488 | 0.486 | 3.54 | 6.86 | **3.32** |

### 关键发现

- **MIA 方法**：SFT 后 AUC 升至 0.57–0.61，GRPO 后完全回落到随机水平（≈0.49），证实 GRPO 抹除了 MIA 可检测的记忆痕迹
- **lz\***：三阶段 |Δ| 均 >2.9，始终保持对 seen/unseen 的区分力，GRPO 无法消除
- 你预期 Base 阶段 lz\* |d| ≈ 0，但实际 |Δ|=2.93——可能 base 模型的预训练数据本身已包含 MMLU 内容，lz\* 在 base 阶段就检测到了差异

---
