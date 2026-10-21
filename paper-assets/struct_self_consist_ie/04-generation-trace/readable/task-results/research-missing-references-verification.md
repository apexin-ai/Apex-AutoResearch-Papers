# research missing references verification

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_missing_references_verification_20260522T012733_result.json`
- **Structured JSON:** [`aa5525814385501d35bf.json`](../../sessions/aa/aa5525814385501d35bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，结果如下：

---

```
[1] ✓ Fisch et al. (2021) "Few-Shot Conformal Prediction with Auxiliary Tasks"
完整标题: Few-shot Conformal Prediction with Auxiliary Tasks
作者: Adam Fisch, Tal Schuster, Tommi Jaakkola, Regina Barzilay
Venue: ICML 2021 (Proceedings of the 38th International Conference on Machine Learning, PMLR 139)
Year: 2021
DOI: 无传统 DOI（PMLR 引用：proceedings.mlr.press/v139/fisch21a.html）
arXiv: 2102.08898
备注: 完全匹配，无差异。
```

```
[2] ⚠️ Chen et al. (2021) "Evaluating Large Language Models Trained on Code"
完整标题: Evaluating Large Language Models Trained on Code
作者: Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such, Dave Cummings, Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William Saunders, Christopher Hesse, Andrew N. Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew Knight, Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei, Sam McCandlish, Ilya Sutskever, Wojciech Zaremba
Venue: arXiv preprint (arXiv:2107.03374)，未正式发表于会议/期刊
Year: 2021
DOI: 无（arXiv preprint）
备注: 论文真实存在，标题/作者/年份均正确。但该论文始终是 arXiv preprint，从未正式发表于任何会议或期刊。BibTeX 应标记为 @article 而非 @inproceedings。
```

```
[3] ✓ Varshney et al. (2022) "Investigating Selective Prediction Approaches Across Several Tasks in IID, OOD, and Adversarial Settings"
完整标题: Investigating Selective Prediction Approaches Across Several Tasks in IID, OOD, and Adversarial Settings
作者: Neeraj Varshney, Swaroop Mishra, Chitta Baral
Venue: Findings of the Association for Computational Linguistics: ACL 2022 (pages 1995–2002, Dublin, Ireland)
Year: 2022
DOI: 10.18653/v1/2022.findings-acl.158
备注: 完全匹配，无差异。Venue 确认为 ACL 2022 Findings。
```

```
[4] ✓ Malinin & Gales (2021) — ICLR 2021
完整标题: Uncertainty Estimation in Autoregressive Structured Prediction
作者: Andrey Malinin, Mark J. F. Gales
Venue: ICLR 2021 (Published as a conference paper)
Year: 2021
DOI: 无传统 DOI（OpenReview ID: jN5y-zb5Q7m）
arXiv: 2002.07650
备注: 完全匹配。标题/作者/venue/year 均正确。论文关注自回归结构化预测中的不确定性估计，涵盖 token 级和序列级不确定性。
```

---

**汇总**: 4 条引用全部真实存在。其中 3 条完全匹配（✓），1 条需注意 venue 标注——Chen et al. (2021) 是 arXiv preprint 而非正式会议论文（⚠️），BibTeX 中应使用 `@article` 并注明 `journal = {arXiv preprint arXiv:2107.03374}`。

Sources:
- [Fisch et al. - ICML 2021](http://proceedings.mlr.press/v139/fisch21a/fisch21a.pdf)
- [Fisch et al. - arXiv](https://arxiv.org/abs/2102.08898)
- [Chen et al. - arXiv](https://arxiv.org/abs/2107.03374)
- [Varshney et al. - ACL Anthology](https://aclanthology.org/2022.findings-acl.158/)
- [Malinin & Gales - OpenReview](https://openreview.net/pdf?id=jN5y-zb5Q7m)
- [Malinin & Gales - arXiv](https://arxiv.org/abs/2002.07650)

---
