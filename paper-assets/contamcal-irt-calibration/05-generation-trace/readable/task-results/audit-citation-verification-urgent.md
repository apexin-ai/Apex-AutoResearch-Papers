# audit citation verification urgent

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_citation_verification_urgent_20260517T041502_result.json`
- **Structured JSON:** [`bf8caf51e503cc76d5a0.json`](../../sessions/bf/bf8caf51e503cc76d5a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证完成。以下是最终结果：

## 验证结果

| cite_key | arXiv ID | Status | 备注 |
|----------|----------|--------|------|
| `dong2026dose` | 2601.04301 | **DIFFERENT_CONTENT** | 该 ID 实际论文是 Schaeffer et al. "Quantifying the Effect of Test Set Contamination on Generative Evaluations"，bib 中已有正确条目 `schaeffer_2026_generative_contamination` |
| `yang2026rl` | 2601.06103 | **DIFFERENT_CONTENT** | 该 ID 实际论文是 Kocyigit & Yildirim "The Impact of Post-training on Data Contamination"，作者/标题完全不符 |
| `gu2026psnirt` | 无 | **DIFFERENT_CONTENT** | PSN-IRT 论文真实存在于 AAAI 2026，但正确引用已在 `zhou_2025_psnirt` 中（Zhou et al.）；此条目伪造了作者 "Gu, Jiaqi" 和标题 |
| `polo2026growing` | 2604.12843 | **DIFFERENT_CONTENT** | 该 ID 实际论文第一作者为 Habba，标题为 "Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration"；bib 中已有正确条目 `habba_2025_growing_pains` |
| `rao2026silicon` | 2603.21636 | **DIFFERENT_CONTENT** | 该 ID 实际论文是 Song et al. "Silicon Bureaucracy and AI Test-Oriented Education"，作者完全不同（非 Rao/Raji/Liang） |
| `han2026probing` | 2510.07175 | **DIFFERENT_CONTENT** | 该 ID 实际论文是 Jongwook Han et al. "Quantifying Data Contamination in Psychometric Evaluations of LLMs"，标题/作者/venue 均不符 |
| `jerzak2026` | 2507.22218 | **EXISTS** | 标题 "Attenuation Bias with Latent Predictors"、作者 Jerzak & Jessee 完全匹配 ✓ |

## 结论

- **1 个真实**: `jerzak2026`
- **6 个幻觉引用** (REMOVE): `dong2026dose`, `yang2026rl`, `gu2026psnirt`, `polo2026growing`, `rao2026silicon`, `han2026probing`

这 6 个全是典型的 LLM 幻觉模式：**借用真实 arXiv ID，但篡改作者和标题**。其中 3 个 (`dong2026dose`, `polo2026growing`, `gu2026psnirt`) 在 bib 中已有对应真实论文的正确条目，属于重复+伪造。

## 额外发现

arXiv 2601.06103 的真实论文 "The Impact of Post-training on Data Contamination" (Kocyigit & Yildirim) 研究 SFT/GRPO 如何与 contamination 交互，与本项目高度相关（NeurIPS 2025 接收）。如需引用建议用正确信息新建条目。

Sources:
- [2601.04301 - Quantifying the Effect of Test Set Contamination](https://arxiv.org/abs/2601.04301)
- [2601.06103 - The Impact of Post-training on Data Contamination](https://arxiv.org/abs/2601.06103)
- [PSN-IRT GitHub (AAAI 2026)](https://github.com/Joe-Hall-Lee/PSN-IRT)
- [2604.12843 - Growing Pains](https://arxiv.org/abs/2604.12843)
- [2603.21636 - Silicon Bureaucracy](https://arxiv.org/abs/2603.21636)
- [2510.07175 - Quantifying Data Contamination in Psychometric Evaluations](https://arxiv.org/abs/2510.07175)
- [2507.22218 - Attenuation Bias with Latent Predictors](https://arxiv.org/abs/2507.22218)
- [Han Wang - On The Fragility of Benchmark Contamination Detection](https://arxiv.org/abs/2510.02386)
- [Jerzak - Measurement That Matches Theory (APSR)](https://www.cambridge.org/core/journals/american-political-science-review/article/measurement-that-matches-theory-theorydriven-identification-in-item-response-theory-models/395DA1DFE3DCD7B866DC053D7554A30B)

---
