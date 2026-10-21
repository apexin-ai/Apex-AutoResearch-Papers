# research bibtex lookup

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bibtex-lookup_20260518T163553_result.json`
- **Structured JSON:** [`49a95b7aa1ff0bb2e2be.json`](../../sessions/49/49a95b7aa1ff0bb2e2be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/new_bibtex_entries.bib`。以下是结果汇总：

| Placeholder | 实际论文 | Key | 备注 |
|---|---|---|---|
| `placeholder_guo2023survey` | Guo et al. "How Close is ChatGPT to Human Experts?" (2023) | `guo2023closechatgpt` | **问题**: 找不到 Guo/Bao 合著的 survey。该论文是 dataset/benchmark 论文而非纯 survey。可能需确认是否应改用 Wu et al. (2310.14724) |
| `placeholder_tang2024science` | Tang et al. "The Science of Detecting LLM-Generated Text", CACM 2024 | `tang2024science` | 完全匹配 |
| `placeholder_krishna2024` | Krishna et al. NeurIPS 2023 (paraphrasing evades detectors) | `krishna2024paraphrasing` | **问题**: `krishna2023paraphrasing` 已在 references.bib 中存在，未找到 Krishna 的 2024 新论文。建议将 tex 中 `placeholder_krishna2024` 直接替换为已有的 `krishna2023paraphrasing` |
| `placeholder_oren2024` | Oren et al. "Proving Test Set Contamination in Black Box Language Models", ICLR 2024 | `oren2024proving` | 完全匹配 |
| `placeholder_cao2020coral` | Cao, Mirjalili, Raschka. "Rank Consistent Ordinal Regression" (CORAL), Pattern Recognition Letters 2020 | `cao2020coral` | 完全匹配 |

需要 Paper Agent 处理的两个问题：
1. `placeholder_guo2023survey` 描述的"Guo/Bao survey"不存在，需确认实际要引的是哪篇
2. `placeholder_krishna2024` 与已有 `krishna2023paraphrasing` 是同一篇论文，建议合并引用

---
