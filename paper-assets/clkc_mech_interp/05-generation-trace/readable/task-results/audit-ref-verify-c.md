# audit ref verify C

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref_verify_C_20260526T110632_result.json`
- **Structured JSON:** [`30250517adf0a5950b73.json`](../../sessions/30/30250517adf0a5950b73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Confirmed: `zhao2026when` does introduce the CLEAR benchmark, and `marks2024geometry` is definitively COLM 2024. Now I'll compile the full report.

## 引用核查报告（Worker C）

**总引用数**: 38 条
**问题数**: 15 条（6 ERROR, 6 WARNING, 3 MINOR）

---

### 逐条结果

**1. `pimentel2021probing`**: Pimentel, Tiago and Cotterell, Ryan (2021). "A Bayesian Framework for Information-Theoretic Probing". EMNLP 2021.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ (related_work: "Information-theoretic approaches offer complementary perspectives on probe expressiveness")
- **综合: OK**

**2. `ravichander2021probing`**: Ravichander, Abhilasha and Belinkov, Yonatan and Hovy, Eduard (2021). "Probing the Probing Paradigm". EACL 2021.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- Pages: ✗ — bib 写 3331--3350，ACL Anthology 实际为 **3363--3377**
- cite 上下文: ✓ ("raised concerns about whether probed information is task-relevant")
- **综合: WARNING** (页码错误)

**3. `gurgurov2026clasbench`**: Gurgurov, Daniil et al. (2026). "CLaS-Bench". arXiv:2601.08331.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("introduced a cross-lingual steering benchmark")
- **综合: OK**

**4. `basu2026interpretability`**: Basu, Sanjay et al. (2026). "Interpretability without Actionability". arXiv:2603.18353.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓ (注意 SSRN 版本副标题不同，但 arXiv 版本匹配)
- Venue: ✓
- cite 上下文: ✓ ("near-perfect probe accuracy does not guarantee effective steering")
- **综合: OK**

**5. `brink2026probing`**: Brink, I. and Boer, A. and Ulmer, D. (2026). "Probing for Knowledge Attribution in LLMs". arXiv:2602.22787.
- 真实性: ✓
- 作者: ✓ (使用缩写 I./A./D.，全名为 Ivo Brink, Alexander Boer, Dennis Ulmer)
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("localized factual associations via probing")
- **综合: MINOR** (作者名用缩写，建议改为全名)

**6. `ifergan2024beneath`**: Ifergan, Matan et al. (2024). "Beneath the Surface of Consistency". Findings NAACL 2025.
- 真实性: ✓
- 作者: ✗ — 第一作者应为 **Maxim Ifergan**，非 "Matan Ifergan"
- 年份: ✗ — bib year=2024，但 venue 是 NAACL 2025 (ACL Anthology: 2025.findings-naacl.475)，应为 **2025**
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- **综合: ERROR** (作者名 + 年份不一致)

**7. `li2025taming`**: Li, Gaotang and Chen, Yufei and Tong, Hanghang (2025). "Taming Knowledge Conflicts". ICML 2025.
- 真实性: ✓
- 作者: ✗ — 第二作者应为 **Yuzhong Chen**，非 "Yufei Chen"
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("proposed conflict mitigation methods")
- **综合: ERROR** (作者名错误)

**8. `pham2026where`**: Pham, Minh Vu and Borkakoty, Hrishav and Hou, Yufang (2026). "Where Knowledge Collides". arXiv:2601.09445.
- 真实性: ✓
- 作者: ✗ — 第二作者应为 **Hsuvas Borkakoty**，非 "Hrishav Borkakoty"
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("traced intra-memory conflict pathways")
- **综合: WARNING** (作者名拼写错误)

**9. `wang2025lost`**: Wang, Mingyang et al. (2025). "Lost in Multilinguality". ACL 2025.
- 真实性: ✓
- 作者: ✗ — 缺少 2 位作者：**Yihong Liu** 和 **Ercong Nie**（ACL Anthology 2025.acl-long.253 列出 7 位作者，bib 只有 5 位）
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- **综合: ERROR** (缺少作者)

**10. `xie2024adaptive`**: Xie, Jian et al. (2024). "Adaptive Chameleon or Stubborn Sloth". ICLR 2024.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("introduced ConflictQA")
- **综合: OK**

**11. `xing2024evaluating`**: Xing, Xiaoling et al. (2024). "Evaluating Knowledge-based Cross-lingual Inconsistency". arXiv:2407.01358.
- 真实性: ✓
- 作者: ✗ — 多处错误：第一作者 **Xiaolin** Xing（非 Xiaoling）；第二作者 **Zhiwei** He（非 Zhenhui）；第三作者 **Haoyu** Xu（非 Huiyun）；第四作者 **Xing** Wang（非 Wang Xin/Xin Wang）
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- **综合: ERROR** (多个作者名错误)

**12. `xu2024knowledge`**: Xu, Rongwu et al. (2024). "Knowledge Conflicts for LLMs: A Survey". EMNLP 2024.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("provided a systematic conflict taxonomy")
- **综合: OK**

**13. `zhao2024analysing`**: Zhao, Yu et al. (2024). "Analysing the Residual Stream of Language Models Under Knowledge Conflicts". NeurIPS 2024 Workshop.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("demonstrated linearly separable conflict signals")
- **综合: OK**

**14. `zhao2025steering`**: Zhao, Yu et al. (2025). "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering". NAACL 2025.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓ (ACL Anthology: 2025.naacl-long.264)
- cite 上下文: ✓ ("applied SAE-based steering (SpARE) in monolingual settings")
- **综合: OK**

**15. `zhao2026when`**: Zhao, Jiaqi et al. (2026). "When Abundance Conceals Weakness". arXiv:2601.07041.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ (确认引入 CLEAR 框架)
- **综合: OK**

**16. `wu2020emerging`**: Wu, Shijie et al. (2020). "Emerging Cross-lingual Structure in Pretrained Language Models". ACL 2020.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("cross-lingual structure emerges without explicit alignment")
- **综合: OK**

**17. `wendler2024llamas`**: Wendler, Chris et al. (2024). "Do Llamas Work in English?". ACL 2024.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("Llama processes non-English inputs through an English-centric latent space")
- **综合: OK**

**18. `muller2021first`**: Muller, Benjamin et al. (2021). "First Align, then Predict". EACL 2021.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("found mid-layer alignment in multilingual BERT")
- **综合: OK**

**19. `kargaran2024mexa`**: Kargaran, Amir Hossein et al. (2024). "MEXA". Findings ACL 2025.
- 真实性: ✓
- 作者: ✗ — 第三作者应为 **Nafiseh Nikeghbal**，非 "Naghmeh Nikeghbal"
- 年份: ✗ — bib year=2024，但 venue 是 Findings ACL 2025，应为 **2025**
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("quantified this bias across language pairs")
- **综合: WARNING** (作者名 + 年份不一致)

**20. `belinkov2022probing`**: Belinkov, Yonatan (2022). "Probing Classifiers". Computational Linguistics 48(1).
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- **综合: OK**

**21. `hewitt2019designing`**: Hewitt, John and Liang, Percy (2019). "Designing and Interpreting Probes with Control Tasks". EMNLP 2019.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("probing establishes correlation rather than causation")
- **综合: OK**

**22. `ulmer2022deep`**: Ulmer, Dennis et al. (2022). "deep-significance". arXiv:2204.06815.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓ (标题用冒号替代原文的破折号，minor)
- Venue: ✓ (也发表于 ICLR 2022 ML Evaluation Standards Workshop)
- cite 上下文: ✓ (bootstrap resampling 方法引用)
- **综合: OK**

**23. `li2023iti`**: Li, Kenneth et al. (2023). "Inference-Time Intervention". NeurIPS 2023.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("introduced Inference-Time Intervention for steering via learned bias vectors")
- **综合: OK**

**24. `zou2023representation`**: Zou, Andy et al. (2023). "Representation Engineering". arXiv:2310.01405.
- 真实性: ✓
- 作者: ✗ — "Koyber, Sanmi" 应为 **Koyejo, Sanmi**；缺少作者 **Dawn Song**
- 年份: ✓ (注意：已正式发表于 ICLR 2025)
- 标题: ✓
- Venue: ✓ (arXiv preprint；但可更新为 ICLR 2025)
- cite 上下文: ✓ ("generalized these approaches through Representation Engineering")
- **综合: ERROR** (作者名错误 + 缺少作者)

**25. `feng2026finegrained`**: Feng, Zihao et al. (2026). "Fine-Grained Activation Steering". ICLR 2026.
- 真实性: ✓
- 作者: ✗ — **大面积错误**。正确作者列表：**Zijian Feng** (非 Zihao), **Tianjiao Li** (非 Tian), **Zixiao Zhu** (非 Zhengyu), **Hanzhang Zhou** (非 Hao), **Junlang Qian** (非 Junliang), **Li Zhang** (非 Lin), **Jia Jim Deryl Chua**, **Lee Onn Mak**, **Gee Wah Ng**, **Kezhi Mao** (非 Kede)。bib 仅 7 位作者，实际 10 位，且几乎每个名字都有误。
- 年份: ✓
- 标题: ✓
- Venue: ✓ (ICLR 2026 confirmed on OpenReview)
- cite 上下文: ✓ ("proposed fine-grained activation steering targeting specific layers")
- **综合: ERROR** (作者名大面积错误)

**26. `conneau2018xnli`**: Conneau, Alexis et al. (2018). "XNLI". EMNLP 2018.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- **综合: OK**

**27. `rei2020comet`**: Rei, Ricardo et al. (2020). "COMET". EMNLP 2020.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- **综合: OK**

**28. `grattafiori2024llama`**: Grattafiori, Aaron et al. (2024). "The Llama 3 Herd of Models". arXiv:2407.21783.
- 真实性: ✓
- 作者: ✓ (arXiv v3 以 Grattafiori 为第一作者，与 bib 一致)
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- **综合: OK**

**29. `yang2025qwen3`**: Yang, An et al. (2025). "Qwen3 Technical Report". arXiv:2505.09388.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- **综合: OK**

**30. `team2024gemma`**: Gemma Team et al. (2024). "Gemma 2". arXiv:2408.00118.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- **综合: OK**

**31. `meng2022locating`**: Meng, Kevin et al. (2022). "Locating and Editing Factual Associations in GPT". NeurIPS 2022.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("demonstrated localized causal editing via activation patching (ROME)")
- **综合: OK**

**32. `turner2023activation`**: Turner, Alexander Matt et al. (2023). "Activation Addition". arXiv:2308.10248.
- 真实性: ✓
- 作者: ✗ — 缺少作者 **Juan J. Vazquez**；David Udell 和 Gavin Leech 顺序颠倒（bib: Udell 3rd/Leech 4th；实际: Leech 3rd/Udell 4th）
- 年份: ✓
- 标题: ✓ (注意 arXiv 最新版 v5 已改名为 "Steering Language Models With Activation Engineering"，bib 使用的是早期版本标题)
- Venue: ✓
- cite 上下文: ✓ ("proposed Activation Addition as an optimization-free alternative")
- **综合: WARNING** (缺少作者 + 顺序错误)

**33. `marks2024geometry`**: Marks, Samuel and Tegmark, Max (2024). "The Geometry of Truth". bib 写 ICLR.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✗ — **错误**。实际发表于 **COLM 2024**（Conference on Language Modeling），非 ICLR。bib 写 "13th International Conference on Learning Representations (ICLR)" 但 ICLR 2024 是第 12 届，双重错误。
- cite 上下文: ✓ ("truth-related representations exhibit linear structure amenable to such interventions")
- **综合: ERROR** (venue 完全错误)

**34. `elhage2022toy`**: Elhage, Nelson et al. (2022). "Toy Models of Superposition". Transformer Circuits Thread.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ (discussion 中用于解释 non-linear encoding 假说，合理)
- **综合: OK**

**35. `templeton2024scaling`**: Templeton, Adly et al. (2024). "Scaling Monosemanticity". Transformer Circuits Thread.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("superposition" 假说引用)
- **综合: OK**

**36. `pokharel2026crosslingual`**: Pokharel, Rhitabrat et al. (2026). "Cross-Lingual Activation Steering". arXiv:2601.16390.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("proposed training-free cross-lingual activation steering")
- **综合: OK**

**37. `sundar2025steering`**: Sundar, Anirudh et al. (2025). "Steering into New Embedding Spaces". ACL 2025.
- 真实性: ✓
- 作者: ✗ — **"Skyler Zhao"** 应为 **Skyler Seto**；**Dan Jurafsky** 不是该论文作者，应为 **Masha Fedzechkina**（ACL Anthology: 2025.acl-long.118）
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ ("analyzed how model interventions induce cross-lingual alignment shifts")
- **综合: ERROR** (虚构作者 Dan Jurafsky + 作者名错误)

**38. `geiger2024finding`**: Geiger, Atticus et al. (2024). "Finding Alignments Between Interpretable Causal Variables...". CLeaR 2024, PMLR 236.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- **综合: OK**

---

### 问题汇总

#### ERROR（必须修正，共 6 条）

| # | Key | 问题 |
|---|-----|------|
| 1 | `feng2026finegrained` | 几乎所有作者名错误，缺少 3 位作者。Zihao→Zijian, Tian→Tianjiao, Zhengyu→Zixiao, Hao→Hanzhang, Junliang→Junlang, Lin→Li, Kede→Kezhi，缺 Chua/Mak/Ng |
| 2 | `marks2024geometry` | Venue 错误：应为 **COLM 2024**，非 ICLR。"13th ICLR" 不存在（ICLR 2024 是第 12 届） |
| 3 | `sundar2025steering` | Skyler Zhao→**Skyler Seto**；Dan Jurafsky **不是作者**（虚构），应为 **Masha Fedzechkina** |
| 4 | `zou2023representation` | Koyber→**Koyejo**；缺少作者 **Dawn Song** |
| 5 | `wang2025lost` | 缺少 2 位作者：**Yihong Liu** 和 **Ercong Nie** |
| 6 | `xing2024evaluating` | 4 个作者名错误：Xiaoling→**Xiaolin**, Zhenhui→**Zhiwei**, Huiyun→**Haoyu**, Wang Xin→**Xing Wang** |

#### WARNING（建议修正，共 6 条）

| # | Key | 问题 |
|---|-----|------|
| 7 | `ifergan2024beneath` | 第一作者 Matan→**Maxim**；year=2024 但 venue 是 NAACL 2025 |
| 8 | `li2025taming` | 第二作者 Yufei→**Yuzhong** Chen |
| 9 | `pham2026where` | 第二作者 Hrishav→**Hsuvas** Borkakoty |
| 10 | `kargaran2024mexa` | 第三作者 Naghmeh→**Nafiseh** Nikeghbal；year=2024 但 venue 是 ACL 2025 |
| 11 | `ravichander2021probing` | 页码 3331--3350 → **3363--3377** |
| 12 | `turner2023activation` | 缺少作者 **Juan J. Vazquez**；Udell/Leech 顺序颠倒 |

#### MINOR（可选修正，共 3 条）

| # | Key | 问题 |
|---|-----|------|
| 13 | `brink2026probing` | 作者使用缩写(I./A./D.)，建议用全名 |
| 14 | `zou2023representation` | 已发表于 ICLR 2025，可更新 venue |
| 15 | `turner2023activation` | arXiv 最新版标题已改为 "Steering Language Models With Activation Engineering" |

#### 幻觉引用检查
- **全部 38 条论文均真实存在**，无虚构引用。

#### 引用上下文检查（Introduction + Related Work）
- 所有 cite 位置的 claim 与原文内容匹配，未发现张冠李戴。

---
