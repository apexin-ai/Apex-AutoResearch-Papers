# audit ref verify A — Part 2 of 2

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../audit-ref-verify-a.md) · [Structured JSON](../../../sessions/9d/9d6c3a326a82445a6546.json)

## Round 4

### Task result

_source line 408_

All verification complete. Here is the full structured report.

---

## 引用核查报告（Worker A）

**总引用数**: 38 条
**问题数**: 15 条（7 ERROR, 6 WARNING, 2 MINOR）

### 逐条结果

**1. `pimentel2021probing`**: Pimentel, Cotterell (2021). "A Bayesian Framework for Information-Theoretic Probing". EMNLP 2021.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ — "Information-theoretic approaches" 正确引用
- 综合: **OK**

**2. `ravichander2021probing`**: Ravichander, Belinkov, Hovy (2021). "Probing the Probing Paradigm". EACL 2021.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **OK**

**3. `gurgurov2026clasbench`**: Gurgurov et al. (2026). "CLaS-Bench". arXiv:2601.08331.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ — "introduced a cross-lingual steering benchmark"
- 综合: **OK**

**4. `basu2026interpretability`**: Basu et al. (2026). "Interpretability without Actionability". arXiv:2603.18353.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✗ [arXiv 原标题全小写 "Interpretability without actionability: mechanistic methods cannot correct..."，bib 中用了 title case；BibTeX 中应加 brace protection]
- Venue: ✓
- cite 上下文: ✓ — "near-perfect probe accuracy does not guarantee effective steering" 与论文主旨一致
- 综合: **MINOR**

**5. `brink2026probing`**: Brink, I. and Boer, A. and Ulmer, D. (2026). "Probing for Knowledge Attribution in LLMs". arXiv:2602.22787.
- 真实性: ✓
- 作者: ✗ [仅用首字母缩写 (I., A., D.)，全名为 Ivo Brink, Alexander Boer, Dennis Ulmer，与其他条目风格不一致]
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **MINOR**

**6. `ifergan2024beneath`**: Ifergan, Matan et al. (2024). "Beneath the Surface of Consistency". Findings of NAACL 2025.
- 真实性: ✓
- 作者: ✗ [**第一作者名字错误：bib 写 "Matan Ifergan"，实际为 "Maxim Ifergan"**]
- 年份: ✗ [**bib 写 year=2024，但发表于 Findings of NAACL 2025，应为 2025**]
- 标题: ✓
- Venue: ✓ (Findings of NAACL 2025 正确)
- cite 上下文: ✓
- 综合: **ERROR** — 需修正作者名和年份

**7. `li2025taming`**: Li, Gaotang and Chen, Yufei and Tong, Hanghang (2025). "Taming Knowledge Conflicts in LMs". ICML 2025.
- 真实性: ✓
- 作者: ✗ [**第二作者名字错误：bib 写 "Yufei Chen"，实际为 "Yuzhong Chen"**]
- 年份: ✓
- 标题: ✓
- Venue: ✓ (ICML 2025 Spotlight)
- cite 上下文: ✓
- 综合: **ERROR** — 需修正作者名

**8. `pham2026where`**: Pham, Minh Vu and Borkakoty, Hrishav and Hou, Yufang (2026). "Where Knowledge Collides". arXiv:2601.09445.
- 真实性: ✓
- 作者: ✗ [**第二作者名字错误：bib 写 "Hrishav Borkakoty"，实际为 "Hsuvas Borkakoty"**]
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **WARNING** — 需修正作者名

**9. `wang2025lost`**: Wang, Mingyang et al. (2025). "Lost in Multilinguality". ACL 2025.
- 真实性: ✓
- 作者: ✗ [**缺少 2 名作者：Yihong Liu 和 Ercong Nie（应在 Lange 和 Strötgen 之间）。实际 7 位作者，bib 仅列 5 位**]
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **ERROR** — 需补充缺失作者

**10. `xie2024adaptive`**: Xie, Jian et al. (2024). "Adaptive Chameleon or Stubborn Sloth". ICLR 2024.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓ (ICLR 2024 Spotlight)
- cite 上下文: ✓ — "introduced ConflictQA" 正确
- 综合: **OK**

**11. `xing2024evaluating`**: Xing, Xiaoling et al. (2024). "Evaluating Knowledge-based Cross-lingual Inconsistency in LLMs". arXiv:2407.01358.
- 真实性: ✓
- 作者: ✗ [**3 个作者名字错误：Xiaoling→Xiaolin Xing, Zhenhui→Zhiwei He, Huiyun→Haoyu Xu**]
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **ERROR** — 3 个名字需修正

**12. `xu2024knowledge`**: Xu, Rongwu et al. (2024). "Knowledge Conflicts for LLMs: A Survey". EMNLP 2024.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ — "systematic conflict taxonomy" 正确
- 综合: **OK**

**13. `zhao2024analysing`**: Zhao, Yu et al. (2024). "Analysing the Residual Stream...". NeurIPS 2024 Workshop.
- 真实性: ✓
- 作者: ✗ [作者顺序与 arXiv 不一致——bib 中 Du 排第 2、Devoto 排第 5，arXiv 上 Devoto 排第 2、Du 排第 4]
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **WARNING** — 作者顺序需核实（以 published version 为准）

**14. `zhao2025steering`**: Zhao, Yu et al. (2025). "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering". NAACL 2025.
- 真实性: ✓
- 作者: ✓ (与 ACL Anthology 一致)
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ — "SpARE" 描述正确
- 综合: **OK**

**15. `zhao2026when`**: Zhao, Jiaqi et al. (2026). "When Abundance Conceals Weakness". arXiv:2601.07041.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ — 确认该论文提出了 CLEAR (Cross-Lingual knowlEdge conflict evAluation fRamework)
- 综合: **OK**

**16. `wu2020emerging`**: Wu, Shijie et al. (2020). "Emerging Cross-lingual Structure in Pretrained Language Models". ACL 2020.
- 真实性: ✓
- 作者: ✗ [**第一作者错误：ACL Anthology 确认作者顺序为 Alexis Conneau, Shijie Wu, Haoran Li, Luke Zettlemoyer, Veselin Stoyanov。Conneau 是第一作者，Wu 排第二**]
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **ERROR** — 作者顺序错误，第一作者应为 Conneau

**17. `wendler2024llamas`**: Wendler et al. (2024). "Do Llamas Work in English?". ACL 2024.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ — "English-centric latent space" 描述正确
- 综合: **OK**

**18. `muller2021first`**: Muller et al. (2021). "First Align, then Predict". EACL 2021.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **OK**

**19. `kargaran2024mexa`**: Kargaran et al. (2024). "MEXA". Findings of ACL 2025.
- 真实性: ✓
- 作者: ✗ [**Nikeghbal 名字错误：bib 写 "Naghmeh"，实际为 "Nafiseh"**]
- 年份: ✗ [**bib 写 year=2024，但发表于 Findings of ACL 2025，应为 2025**]
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **WARNING** — 需修正作者名和年份

**20. `belinkov2022probing`**: Belinkov (2022). "Probing Classifiers: Promises, Shortcomings, and Advances". Computational Linguistics 48(1).
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **OK**

**21. `hewitt2019designing`**: Hewitt, Liang (2019). "Designing and Interpreting Probes with Control Tasks". EMNLP 2019.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ — "probing establishes correlation rather than causation" 与论文主旨一致
- 综合: **OK**

**22. `ulmer2022deep`**: Ulmer, Hardmeier, Frellsen (2022). "deep-significance". arXiv:2204.06815.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **OK**

**23. `li2023iti`**: Li et al. (2023). "Inference-Time Intervention". NeurIPS 2023.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **OK**

**24. `zou2023representation`**: Zou et al. (2023). "Representation Engineering". arXiv:2310.01405.
- 真实性: ✓
- 作者: ✗ [**"Sanmi Koyber" 应为 "Sanmi Koyejo"；缺少共同作者 Dawn Song**]
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **WARNING** — 需修正作者名拼写并补充缺失作者

**25. `turner2023activation`**: Turner et al. (2023). "Activation Addition: Steering Language Models Without Optimization". arXiv:2308.10248.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✗ [arXiv 最新版 (v5, Oct 2024) 标题已更新为 "Steering Language Models With Activation Engineering"。bib 中为早期版本标题]
- Venue: ✓
- cite 上下文: ✓
- 综合: **WARNING** — 标题可能需更新（取决于引用的版本）

**26. `feng2026finegrained`**: Feng, Zihao et al. (2026). "Fine-Grained Activation Steering". ICLR 2026.
- 真实性: ✓
- 作者: ✗ [**严重错误——几乎所有作者名字都错：第一作者 Zihao→Zijian Feng, Tian→Tianjiao Li, Zhengyu→Zixiao Zhu, Hao→Hanzhang Zhou, Junliang→Junlang Qian, Lin→Li Zhang, Kede→Kezhi Mao。另外缺少 3 名作者：Jia Jim Deryl Chua, Lee Onn Mak, Gee Wah Ng**]
- 年份: ✓
- 标题: ✓
- Venue: ✓ (ICLR 2026 确认)
- cite 上下文: ✓
- 综合: **ERROR** — 作者列表几乎全错，疑似 hallucinated author list

**27. `conneau2018xnli`**: Conneau et al. (2018). "XNLI". EMNLP 2018.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **OK**

**28. `rei2020comet`**: Rei et al. (2020). "COMET". EMNLP 2020.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **OK**

**29. `grattafiori2024llama`**: Grattafiori et al. (2024). "The Llama 3 Herd of Models". arXiv:2407.21783.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **OK**

**30. `yang2025qwen3`**: Yang et al. (2025). "Qwen3 Technical Report". arXiv:2505.09388.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **OK**

**31. `team2024gemma`**: Gemma Team et al. (2024). "Gemma 2". arXiv:2408.00118.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **OK**

**32. `meng2022locating`**: Meng et al. (2022). "Locating and Editing Factual Associations in GPT". NeurIPS 2022.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ — "ROME" / "activation patching" 描述正确
- 综合: **OK**

**33. `marks2024geometry`**: Marks, Tegmark (2024). "The Geometry of Truth". ICLR (13th).
- 真实性: ✓
- 作者: ✓
- 年份: ✗ [**bib 写 year=2024，但 booktitle 写 "13th ICLR"，即 ICLR 2025。OpenReview 确认 "Published as a conference paper at ICLR 2025"。应改为 year=2025**]
- 标题: ✓
- Venue: ✗ [年份与 venue 编号自相矛盾]
- cite 上下文: ✓
- 综合: **WARNING** — year 应改为 2025

**34. `elhage2022toy`**: Elhage et al. (2022). "Toy Models of Superposition". Transformer Circuits Thread.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓ (arXiv:2209.10652 + Transformer Circuits)
- cite 上下文: ✓ — 用于支持 "non-linear causal interactions" 假说，属于合理延伸
- 综合: **OK**

**35. `templeton2024scaling`**: Templeton et al. (2024). "Scaling Monosemanticity". Transformer Circuits Thread.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓ — 用于支持 "superposition" 讨论
- 综合: **OK**

**36. `pokharel2026crosslingual`**: Pokharel et al. (2026). "Cross-Lingual Activation Steering". arXiv:2601.16390.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **OK**

**37. `sundar2025steering`**: Sundar et al. (2025). "Steering into New Embedding Spaces". ACL 2025.
- 真实性: ✓
- 作者: ✗ [**2 名作者错误：bib 写 "Skyler Zhao" 实际为 "Skyler Seto"；bib 写 "Dan Jurafsky" 实际为 "Masha Fedzechkina"（ACL Anthology 2025.acl-long.118 确认）**]
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **ERROR** — 2 名作者为虚构/错误姓名

**38. `geiger2024finding`**: Geiger et al. (2024). "Finding Alignments Between Interpretable Causal Variables...". CLeaR 2024, PMLR 236.
- 真实性: ✓
- 作者: ✓
- 年份: ✓
- 标题: ✓
- Venue: ✓
- cite 上下文: ✓
- 综合: **OK**

---

### 问题汇总

#### ERROR（7 条，必须修正）

| # | Key | 问题描述 |
|---|-----|---------|
| 1 | `ifergan2024beneath` | 第一作者 "Matan" → **"Maxim"**；year 2024 → **2025** |
| 2 | `li2025taming` | 第二作者 "Yufei Chen" → **"Yuzhong Chen"** |
| 3 | `wang2025lost` | 缺少 2 名作者：**Yihong Liu** 和 **Ercong Nie**（Lange 和 Strötgen 之间） |
| 4 | `xing2024evaluating` | 3 个名字错误：Xiaoling→**Xiaolin**, Zhenhui→**Zhiwei**, Huiyun→**Haoyu** |
| 5 | `wu2020emerging` | 第一作者应为 **Alexis Conneau**（非 Shijie Wu），作者顺序反了 |
| 6 | `feng2026finegrained` | 作者列表几乎全错——第一作者 Zihao→**Zijian**，其余 6 名给定名全错，缺 3 名作者 |
| 7 | `sundar2025steering` | "Skyler Zhao"→**"Skyler Seto"**，"Dan Jurafsky"→**"Masha Fedzechkina"** |

#### WARNING（6 条，建议修正）

| # | Key | 问题描述 |
|---|-----|---------|
| 8 | `pham2026where` | 第二作者 "Hrishav" → **"Hsuvas"** |
| 9 | `marks2024geometry` | year=2024 但 venue 为 13th ICLR = ICLR **2025**，需改 year=2025 |
| 10 | `kargaran2024mexa` | Nikeghbal 名字 "Naghmeh"→**"Nafiseh"**；year 2024→**2025** |
| 11 | `zou2023representation` | "Koyber"→**"Koyejo"**；缺少共同作者 **Dawn Song** |
| 12 | `turner2023activation` | arXiv 最新版标题已改为 "Steering Language Models With Activation Engineering" |
| 13 | `zhao2024analysing` | 作者顺序与 arXiv 版不一致（Du/Devoto 位置互换） |

#### MINOR（2 条，风格问题）

| # | Key | 问题描述 |
|---|-----|---------|
| 14 | `brink2026probing` | 作者仅用首字母（I., A., D.），与其他条目风格不一致 |
| 15 | `basu2026interpretability` | 标题大小写与 arXiv 原文不一致（BibTeX 中建议加 brace protection） |

#### OpenAlex 预检交叉验证

| OpenAlex 标记 | 本次独立结论 |
|---|---|
| `zou2023representation` not_found | **真实存在**，arXiv:2310.01405 可访问，但作者有 typo |
| `turner2023activation` not_found | **真实存在**，arXiv:2308.10248，标题已更新 |
| `elhage2022toy` not_found | **真实存在**，arXiv:2209.10652 + Transformer Circuits |
| `templeton2024scaling` not_found | **真实存在**，transformer-circuits.pub 可访问 |
| `xie2024adaptive` first_author mismatch | **作者正确**，Jian Xie 确为第一作者 |
| `wu2020emerging` first_author mismatch | **确认错误**——第一作者应为 Conneau |
| `meng2022locating` first_author mismatch | **作者正确**，Kevin Meng 确为第一作者 |

#### Citation 上下文检查

所有 Introduction 和 Related Work 中的 cite 位置均与原文 claim 一致，未发现"张冠李戴"问题。`zhao2026when` 确实提出了 CLEAR framework（Cross-Lingual knowlEdge conflict evAluation fRamework），正文描述准确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 871027,
  "duration_api_ms": 2382955,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "5e53bb7f-8ea1-455f-bfd7-5af144f5fb56",
  "total_cost_usd": 5.847134250000003,
  "usage": {
    "input_tokens": 1954,
    "cache_creation_input_tokens": 59448,
    "cache_read_input_tokens": 232679,
    "output_tokens": 22191,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 59448,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 8025,
        "cache_read_input_tokens": 64385,
        "cache_creation_input_tokens": 6904,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 6904
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1087283,
      "outputTokens": 37132,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 81,
      "costUSD": 2.0829429999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 2089,
      "outputTokens": 40256,
      "cacheReadInputTokens": 3250155,
      "cacheCreationInputTokens": 179563,
      "webSearchRequests": 0,
      "costUSD": 3.76419125,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ae51af6a-94cb-4154-94cf-1b24e1338d2d"
}
```

</details>

---
