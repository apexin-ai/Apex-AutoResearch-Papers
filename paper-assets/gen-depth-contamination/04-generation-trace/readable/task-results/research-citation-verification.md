# research citation verification

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation_verification_20260512T132729_result.json`
- **Structured JSON:** [`beef7889fd7e156cd67d.json`](../../sessions/be/beef7889fd7e156cd67d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

8 处 [需验证] 全部处理完毕。核实结果汇总：

| # | 引用 | 核实结果 | 文档原始信息是否正确 | 修正 |
|---|------|----------|---------------------|------|
| 1 | **DivEye** | Advik Raj Basani, Pin-Yu Chen; TMLR 2026 | venue 正确，缺作者 | 补充作者 → `Basani & Chen, TMLR 2026` |
| 2 | **Binoculars** | Hans, Schwarzschild, Cherepanova, Kazemi, Saha, Goldblum, Geiping, Goldstein; **ICML 2024** | 年份正确，缺 venue | 补充 venue → `Hans et al., ICML 2024` |
| 3 | **Alemohammad et al.** | 2023.07 arXiv preprint → **ICLR 2024** 发表 | 文档写 "ICML 2024" **错误** | 修正为 `ICLR 2024` |
| 4 | **DoReMi** | Xie et al.; **NeurIPS 2023** | 完全正确 | 仅移除 [需验证] 标签 |
| 5 | **Data Mixing Laws** | Ye, Liu, Sun, Zhan, Zhou, Qiu; arXiv 2024.03 → **ICLR 2025** | 作者姓氏正确，年份应为 ICLR 2025 | 修正为 `Ye et al., ICLR 2025` |
| 6 | **Surplexity** | Gambetta, Gezici, Giannotti, Pedreschi, Knott, Pappalardo; arXiv 2024.10 | 年份正确，缺作者 | 补充作者 → `Gambetta et al., 2024` |
| 7 | **ConStat** | Jasper Dekoninck, Mark Müller, Martin Vechev; NeurIPS 2024 | venue 正确，缺作者 | 补充作者 → `Dekoninck et al., NeurIPS 2024` |
| 8 | **DATAPROPHET** | Xuan Qi, Luxi He, Dan Roth, Xingyu Fu; ICLR 2026 | venue 正确，缺作者 | 补充作者 → `Qi et al., ICLR 2026` |

所有 8 条引用均为真实论文，无虚构。发现并修正了两处事实错误：Alemohammad et al. 的 venue（ICML→ICLR）和 Data Mixing Laws 的年份/venue（2024→ICLR 2025）。`claim_routes.md` 和 `theory_framework.md` 中无 [需验证] 标注，无需修改。

Sources:
- [DivEye - arXiv 2509.18880](https://arxiv.org/abs/2509.18880)
- [Binoculars - arXiv 2401.12070](https://arxiv.org/abs/2401.12070)
- [Self-Consuming Generative Models Go MAD - arXiv 2307.01850](https://arxiv.org/abs/2307.01850)
- [DoReMi - arXiv 2305.10429](https://arxiv.org/abs/2305.10429)
- [Data Mixing Laws - arXiv 2403.16952](https://arxiv.org/abs/2403.16952)
- [Surplexity - arXiv 2410.12341](https://arxiv.org/abs/2410.12341)
- [ConStat - arXiv 2405.16281](https://arxiv.org/abs/2405.16281)
- [DATAPROPHET - arXiv 2603.19688](https://arxiv.org/abs/2603.19688)

---
