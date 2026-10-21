# research luo bib lookup

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_luo_bib_lookup_20260519T070209_result.json`
- **Structured JSON:** [`1076c203aa6545fd8351.json`](../../sessions/10/1076c203aa6545fd8351.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报如下：

---

### 查找结果

| 引用 | 结论 |
|---|---|
| **Luo et al. 2023** | **不存在。** 实际论文是 Xie et al. (EMNLP 2023)。Reviewer 或论文中的 "Luo" 是误引。 |
| **Florian et al. 2003** | 已在 bib 中，信息准确。已补充 DOI 和 URL。Venue: CoNLL-2003 at HLT-NAACL 2003。 |
| **Xie et al. 2023 vs Luo** | 两者是同一篇论文被错误归到不同作者名下。bib 中还有 Xie et al. 的另一篇 NAACL 2024 论文（self-improving NER），两篇是不同工作。 |

### 新增 BibTeX entry

- `xie2023zeroshot` — "Empirical Study of Zero-Shot NER with ChatGPT", Xie et al., EMNLP 2023, pp. 7935-7956

### Related Work 定位建议

| 论文 | 定位 |
|---|---|
| **Xie et al. 2023 (EMNLP)** | 最直接的 prior work — 将 self-consistency voting 应用于 NER，使用两阶段投票（先 mention 后 type）。本项目的结构化 self-consistency 方法可以定位为对该 naive voting 策略的改进。 |
| **Florian et al. 2003** | 经典 NER ensemble 方法（classifier combination），可在 Related Work 中作为传统 ensemble 方法的代表引用，与 LLM-based ensemble 形成对比。 |

---
