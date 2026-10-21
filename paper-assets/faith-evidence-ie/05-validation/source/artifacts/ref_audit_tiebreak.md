# 引用争议项验证结果

日期: 2026-05-26

---

### gulcehre2023rest
- WebSearch 结果：arXiv:2308.08998 "Reinforced Self-Training (ReST) for Language Modeling" 的完整作者列表为 Caglar Gulcehre, Tom Le Paine, Srivatsan Srinivasan, Ksenia Konyushkova, Lotte Weerts, Abhishek Sharma, Aditya Siddhant, Alex Ahern, Miaosen Wang, Chenjie Gu, Wolfgang Macherey, **Arnaud Doucet**, Orhan Firat, **Nando de Freitas**（共 14 人）。不含 "Dyer, Chris" 或 "Grangier, David"。
- 结论：**W2/W3 正确**，W1 错误
- 正确值：作者中应为 Doucet, Arnaud 和 de Freitas, Nando（非 Dyer, Chris 和 Grangier, David）
- 备注：当前 `docs/paper/references.bib` 中此条目作者已是正确版本，无需修改

### tang2025rsftppo
- WebSearch 结果：OpenReview (yQ2UivKlir) 页面确认作者为 **4 人**：Gautham Govind Anil, Dheeraj Mysore Nagaraj, Karthikeyan Shanmugam, Sanjay Shakkottai。ICML 2025 PUT workshop 的官方全名为 **"2nd Workshop on Test-Time Adaptation: Putting Updates to the Test (PUT)"**（来源：icml.cc/virtual/2025/workshop/39974 和 tta-icml2025.github.io）。bib 中的 "ICML 2025 Workshop on Practical Aspects of Unlearning and Test-time Adaptation (PUT)" 是虚构名称。
- 结论：
  - 作者数量：**W2 正确**（4 人），W1 错误（W1 混淆了同组另一篇论文 "Fine-Tuning Diffusion Models via Intermediate Distribution Shaping" 的 6 人作者列表）
  - Venue 名称：**W3 正确**（venue 名虚构），W1/W2 未发现此问题
- 正确值：
  - 作者：Anil, Gautham Govind and Nagaraj, Dheeraj Mysore and Shanmugam, Karthikeyan and Shakkottai, Sanjay（4 人，bib 中作者正确）
  - Venue：booktitle 应改为 "2nd Workshop on Test-Time Adaptation: Putting Updates to the Test (PUT)"

### rafailov2023direct
- WebSearch 结果：arXiv:2305.18290 页面确认作者顺序为 Rafael Rafailov, Archit Sharma, Eric Mitchell, **Stefano Ermon (4th)**, **Christopher D. Manning (5th)**, Chelsea Finn。bib 中的顺序 `Ermon, Stefano and Manning, Christopher D.` 与 arXiv 完全一致。
- 结论：**W1/W3 正确**，W2 错误
- 正确值：当前 bib 作者顺序无误，Ermon 第 4、Manning 第 5

### liu2026gdpo
- WebSearch 结果：ICML 2026 虚拟会议页面（icml.cc/virtual/2026/poster/63333）确认 "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization" 已被 ICML 2026 接收为 poster。
- 结论：**W2 正确**，W3 错误
- 正确值：已发表于 ICML 2026（poster），bib 应从 `@article` + `journal = {arXiv preprint}` 更新为 `@inproceedings` + `booktitle = {International Conference on Machine Learning}`

### wang2025rullm
- WebSearch 结果：Springer Nature Link（link.springer.com/chapter/10.1007/978-981-95-3343-5_11）页面标题为 **"Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction"**，无 "Ru-LLM:" 前缀。DBLP NLPCC 2025 Part I 索引同样确认标题无前缀。
- 结论：**W1/W2 正确**，W3 错误
- 正确值：标题应为 "Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction"（删除 "Ru-LLM:" 前缀）

---

## 汇总

| # | cite_key | 争议点 | 裁决 | 需修改 |
|---|----------|--------|------|--------|
| 1 | gulcehre2023rest | 作者名 Dyer/Grangier vs Doucet/de Freitas | W2/W3 对 | 当前 bib 已正确，无需改 |
| 2 | tang2025rsftppo | 作者数 (4 vs 6) + venue 名称 | 作者: W2 对; venue: W3 对 | venue 名须改为 "2nd Workshop on Test-Time Adaptation: Putting Updates to the Test (PUT)" |
| 3 | rafailov2023direct | Ermon/Manning 顺序 | W1/W3 对 | 无需改 |
| 4 | liu2026gdpo | ICML 2026 vs arXiv preprint | W2 对 | venue 须更新为 ICML 2026 |
| 5 | wang2025rullm | 标题是否含 "Ru-LLM:" | W1/W2 对 | 删除 "Ru-LLM:" 前缀 |

## 数据来源

- [arXiv:2308.08998](https://arxiv.org/abs/2308.08998) — gulcehre2023rest 作者验证
- [OpenReview yQ2UivKlir](https://openreview.net/forum?id=yQ2UivKlir) — tang2025rsftppo 作者验证
- [ICML 2025 PUT Workshop](https://icml.cc/virtual/2025/workshop/39974) — tang2025rsftppo venue 验证
- [PUT Workshop 官网](https://tta-icml2025.github.io/) — tang2025rsftppo venue 名称验证
- [arXiv:2305.18290](https://arxiv.org/abs/2305.18290) — rafailov2023direct 作者顺序验证
- [ICML 2026 Poster 63333](https://icml.cc/virtual/2026/poster/63333) — liu2026gdpo 发表状态验证
- [Springer 978-981-95-3343-5_11](https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11) — wang2025rullm 标题验证
- [DBLP NLPCC 2025 Part I](https://dblp.org/db/conf/nlpcc/nlpcc2025-1.html) — wang2025rullm 标题/作者验证
