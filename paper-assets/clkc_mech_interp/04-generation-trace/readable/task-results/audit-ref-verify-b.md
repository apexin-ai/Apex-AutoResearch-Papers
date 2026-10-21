# audit ref verify B

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref_verify_B_20260526T105303_result.json`
- **Structured JSON:** [`335e921202cb144f066f.json`](../../sessions/33/335e921202cb144f066f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All searches complete. Now let me compile the full verification report. Every paper has been verified as real. I found 11 entries with issues.

## 引用核查报告（Worker B）

**总引用数**: 38 条
**问题数**: 10 条（ERROR: 7, WARNING: 3）

### 逐条结果

1. `pimentel2021probing`: Pimentel, Cotterell (2021). "A Bayesian Framework for Information-Theoretic Probing". EMNLP 2021.
   - 真实性: ✓
   - 作者: ✓
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **OK**

2. `ravichander2021probing`: Ravichander, Belinkov, Hovy (2021). "Probing the Probing Paradigm". EACL 2021.
   - 真实性: ✓
   - 作者: ✓
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - Pages: ✗ **bib 写 3331–3350，ACL Anthology 实际为 3363–3377**
   - cite 上下文: ✓
   - 综合: **WARNING**（页码错误，不影响识别但不严谨）

3. `gurgurov2026clasbench`: Gurgurov et al. (2026). "CLaS-Bench". arXiv 2601.08331.
   - 真实性: ✓
   - 作者: ✓
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **OK**

4. `basu2026interpretability`: Basu et al. (2026). "Interpretability without Actionability". arXiv 2603.18353.
   - 真实性: ✓
   - 作者: ✓
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **OK**

5. `brink2026probing`: Brink, Boer, Ulmer (2026). "Probing for Knowledge Attribution in LLMs". arXiv 2602.22787.
   - 真实性: ✓
   - 作者: ✓
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **OK**

6. `ifergan2024beneath`: Ifergan et al. "Beneath the Surface of Consistency". Findings NAACL 2025.
   - 真实性: ✓
   - 作者: ✗ **第一作者名 "Matan" 应为 "Maxim"**
   - 年份: ✗ **bib year=2024 但 venue 是 NAACL 2025，应为 2025**
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **ERROR**

7. `li2025taming`: Li, Chen, Tong (2025). "Taming Knowledge Conflicts in Language Models". ICML 2025.
   - 真实性: ✓
   - 作者: ✗ **第二作者 "Yufei" Chen 应为 "Yuzhong" Chen**（ICML proceedings 及 arXiv 确认）
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **ERROR**

8. `pham2026where`: Pham, Borkakoty, Hou (2026). "Where Knowledge Collides". arXiv 2601.09445.
   - 真实性: ✓
   - 作者: ✗ **第二作者 "Hrishav" Borkakoty 应为 "Hsuvas" Borkakoty**（dblp、个人主页、arXiv 确认）
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **ERROR**

9. `wang2025lost`: Wang et al. (2025). "Lost in Multilinguality". ACL 2025.
   - 真实性: ✓
   - 作者: ✗ **缺少 2 位作者：Yihong Liu、Ercong Nie**（ACL Anthology 确认共 7 位作者，bib 只列了 5 位）
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **WARNING**

10. `xie2024adaptive`: Xie et al. (2024). "Adaptive Chameleon or Stubborn Sloth". ICLR 2024.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

11. `xing2024evaluating`: Xing et al. (2024). "Evaluating Knowledge-based Cross-lingual Inconsistency". arXiv 2407.01358.
    - 真实性: ✓
    - 作者: ✗ **4/6 作者名严重错误**：Xiaoling→**Xiaolin**, Zhenhui→**Zhiwei**, Huiyun→**Haoyu**, Xin→**Xing**（arXiv 及 dblp 确认）
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **ERROR**（严重——大面积作者名错误）

12. `xu2024knowledge`: Xu et al. (2024). "Knowledge Conflicts for LLMs: A Survey". EMNLP 2024.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

13. `zhao2024analysing`: Zhao et al. (2024). "Analysing the Residual Stream...Under Knowledge Conflicts". NeurIPS 2024 Workshop.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

14. `zhao2025steering`: Zhao et al. (2025). "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering". NAACL 2025.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

15. `zhao2026when`: Zhao et al. (2026). "When Abundance Conceals Weakness". arXiv 2601.07041.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

16. `wu2020emerging`: Wu, Conneau et al. (2020). "Emerging Cross-lingual Structure in Pretrained Language Models". ACL 2020.
    - 真实性: ✓
    - 作者: ✓（Shijie Wu 确为第一作者）
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

17. `wendler2024llamas`: Wendler et al. (2024). "Do Llamas Work in English?". ACL 2024.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

18. `muller2021first`: Muller et al. (2021). "First Align, then Predict". EACL 2021.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

19. `kargaran2024mexa`: Kargaran et al. "MEXA". Findings ACL 2025.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✗ **bib year=2024 但 venue 是 Findings ACL 2025，应为 2025**
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **WARNING**（年份与 venue 不一致）

20. `belinkov2022probing`: Belinkov (2022). "Probing Classifiers: Promises, Shortcomings, and Advances". Computational Linguistics Vol.48 No.1.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

21. `hewitt2019designing`: Hewitt, Liang (2019). "Designing and Interpreting Probes with Control Tasks". EMNLP 2019.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

22. `ulmer2022deep`: Ulmer, Hardmeier, Frellsen (2022). "deep-significance". arXiv 2204.06815.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

23. `li2023iti`: Li et al. (2023). "Inference-Time Intervention". NeurIPS 2023.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

24. `zou2023representation`: Zou et al. (2023). "Representation Engineering". arXiv 2310.01405.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

25. `turner2023activation`: Turner et al. (2023). "Activation Addition: Steering Language Models Without Optimization". arXiv 2308.10248.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓（原始版本标题，后续版本改名为 "Steering Language Models With Activation Engineering"，但引用原标题有效）
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

26. `marks2024geometry`: Marks, Tegmark. "The Geometry of Truth". ICLR.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✗ **bib year=2024，但论文实际发表于 ICLR 2025**（OpenReview 确认 "Published as a conference paper at ICLR 2025"）。bib 中 "13th ICLR" 对应的是 ICLR 2025，与 year=2024 矛盾。
    - 标题: ✓
    - Venue: ✗ **应为 ICLR 2025（第 13 届），非 2024**
    - cite 上下文: ✓
    - 综合: **ERROR**

27. `elhage2022toy`: Elhage et al. (2022). "Toy Models of Superposition". Transformer Circuits Thread.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

28. `templeton2024scaling`: Templeton et al. (2024). "Scaling Monosemanticity". Transformer Circuits Thread.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

29. `feng2026finegrained`: Feng et al. (2026). "Fine-Grained Activation Steering: Steering Less, Achieving More". ICLR 2026.
    - 真实性: ✓
    - 作者: ✗ **几乎全部作者名错误，且缺少 3 位作者**。bib 列 7 人，实际 10 人。具体错误：Zihao→**Zijian**, Tian→**Tianjiao**, Zhengyu→**Zixiao**, Hao→**Hanzhang**, Junliang→**Junlang**, Lin→**Li** (Zhang), Kede→**Kezhi** (Mao)。缺少：Jia Jim Deryl Chua, Lee Onn Mak, Gee Wah Ng。
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **ERROR**（最严重——大面积作者名腐坏 + 漏人）

30. `conneau2018xnli`: Conneau et al. (2018). "XNLI: Evaluating Cross-lingual Sentence Representations". EMNLP 2018.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

31. `rei2020comet`: Rei et al. (2020). "COMET: A Neural Framework for MT Evaluation". EMNLP 2020.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

32. `grattafiori2024llama`: Grattafiori et al. (2024). "The Llama 3 Herd of Models". arXiv 2407.21783.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

33. `yang2025qwen3`: Yang et al. (2025). "Qwen3 Technical Report". arXiv 2505.09388.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

34. `team2024gemma`: Gemma Team et al. (2024). "Gemma 2: Improving Open Language Models at a Practical Size". arXiv 2408.00118.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

35. `meng2022locating`: Meng et al. (2022). "Locating and Editing Factual Associations in GPT". NeurIPS 2022.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

36. `pokharel2026crosslingual`: Pokharel, Agrawal, Nagar (2026). "Cross-Lingual Activation Steering for Multilingual Language Models". arXiv 2601.16390.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

37. `sundar2025steering`: Sundar et al. (2025). "Steering into New Embedding Spaces". ACL 2025.
    - 真实性: ✓
    - 作者: ✗ **2 位作者完全错误**：bib 写 "Zhao, Skyler" 实际为 **Seto, Skyler**；bib 写 "Jurafsky, Dan" 实际为 **Fedzechkina, Masha**（ACL Anthology 确认）
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **ERROR**

38. `geiger2024finding`: Geiger et al. (2024). "Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations". CLeaR 2024, PMLR vol 236.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

---

### 问题汇总

| # | Key | 严重性 | 问题描述 |
|---|-----|--------|----------|
| 1 | `feng2026finegrained` | **ERROR** | 7/7 作者名全部错误（首名拼音接近但均有误），且缺少 3 位共同作者 |
| 2 | `xing2024evaluating` | **ERROR** | 4/6 作者名错误（Xiaoling→Xiaolin, Zhenhui→Zhiwei, Huiyun→Haoyu, Xin→Xing） |
| 3 | `sundar2025steering` | **ERROR** | 2 位作者完全错误（Zhao→Seto, Jurafsky→Fedzechkina） |
| 4 | `ifergan2024beneath` | **ERROR** | 第一作者 Matan→Maxim；year=2024 应为 2025（NAACL 2025） |
| 5 | `marks2024geometry` | **ERROR** | year=2024 应为 2025（ICLR 2025，OpenReview 确认） |
| 6 | `li2025taming` | **ERROR** | 第二作者 Yufei→Yuzhong Chen |
| 7 | `pham2026where` | **ERROR** | 第二作者 Hrishav→Hsuvas Borkakoty |
| 8 | `wang2025lost` | **WARNING** | 缺少 2 位作者（Yihong Liu, Ercong Nie），7 人只列了 5 人 |
| 9 | `kargaran2024mexa` | **WARNING** | year=2024 但 venue 是 Findings ACL 2025，应为 2025 |
| 10 | `ravichander2021probing` | **WARNING** | 页码 3331–3350 应为 3363–3377 |

**幻觉引用**: 0 条。全部 38 篇论文均真实存在。

**cite 上下文错误**: 0 条。所有引用的 claim 与原文内容一致。

**OpenAlex 预检对比**: OpenAlex 标记的 7 条中，4 条 not_found 均为索引缺失（Anthropic 技术报告、arXiv 预印本），3 条 mismatch 中 wu2020emerging 和 meng2022locating 经独立验证为 OpenAlex 误报，xie2024adaptive 也确认无误。真正的问题主要在 OpenAlex 未标记的条目中（feng2026finegrained、sundar2025steering、xing2024evaluating 等）。

---
