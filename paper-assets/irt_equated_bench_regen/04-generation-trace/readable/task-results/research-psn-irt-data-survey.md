# research psn irt data survey

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_psn_irt_data_survey_20260520T180227_result.json`
- **Structured JSON:** [`f5c043d9b23b1ee5b18b.json`](../../sessions/f5/f5c043d9b23b1ee5b18b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研报告已写入 `memory.md`。核心结论：

**首选数据源：METABENCH (Kipnis et al., ICLR 2025)**
- 5,055 个模型 × 12,508 MMLU items 的完整 response matrix
- 已拟合 2PL/3PL/4PL IRT 参数
- Zenodo 一键下载（620MB）：https://zenodo.org/records/12819251
- GitHub：https://github.com/adkipnis/metabench

**辅助参考：PSN-IRT (AAAI 2026)**
- MMLU 全集 14,042 items 的 4PL 参数直接可用（`results/item_parameters.csv`）
- 但仅基于 12 个模型，参数可靠性不如 METABENCH
- GitHub：https://github.com/Joe-Hall-Lee/PSN-IRT

**其他数据源**（Open LLM Leaderboard v1 原始数据、tinyBenchmarks、HELM）要么是 METABENCH 的上游数据需要大量组装工作，要么覆盖太少，不推荐直接使用。

下一步：下载 METABENCH 和 PSN-IRT 数据，确认 item ID 与原始 MMLU 的对齐方式。

Sources:
- [PSN-IRT GitHub](https://github.com/Joe-Hall-Lee/PSN-IRT)
- [PSN-IRT Paper](https://arxiv.org/abs/2505.15055)
- [METABENCH GitHub](https://github.com/adkipnis/metabench)
- [METABENCH Paper](https://arxiv.org/abs/2407.12844)
- [METABENCH Zenodo Data](https://zenodo.org/records/12819251)
- [Open LLM Leaderboard v1 Archive](https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive)
- [tinyBenchmarks](https://github.com/felipemaiapolo/tinyBenchmarks)
- [HELM MMLU](https://crfm.stanford.edu/2024/05/01/helm-mmlu.html)

---
