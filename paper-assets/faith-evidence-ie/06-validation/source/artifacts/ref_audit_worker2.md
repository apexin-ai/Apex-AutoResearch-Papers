# 引用核对清单 — Worker 2

总计: 52 条引用, 14 条有问题 (其中 6 条严重, 2 条中等, 6 条轻微)

另有 17 条 bib 中存在但从未在正文中 cite 的条目。

---

## 问题汇总

### 严重问题 (factual errors)

| # | cite_key | 问题 |
|---|----------|------|
| 1 | `gulcehre2023rest` | **作者名错误**: Dyer, Chris 和 Grangier, David 应为 **Doucet, Arnaud** 和 **de Freitas, Nando**; entry type 错误 (`@inproceedings`+`booktitle` → 应为 `@article`+`journal`) |
| 2 | `wang2025relprior` | **标题错误**: bib 写 "RelPrior: Relation as a Prior for LLM-based Document-Level Relation Extraction", 实际标题 "Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction" |
| 3 | `xu2024lmrc` | **标题多余前缀**: bib 写 "LMRC: LLM with Relation Classifier...", 实际标题无 "LMRC:" 前缀 |
| 4 | `wang2025rullm` | **标题多余前缀**: bib 写 "Ru-LLM: Logical Rule-Constrained...", 实际标题无 "Ru-LLM:" 前缀; 作者 "Peng, Min" 可能不在 Springer 正式作者列表中; entry type 应为 `@inproceedings` |
| 5 | `ma2023dreeam` | **Venue 错误**: bib 写 "Findings of EACL 2023", 实际发表在 **EACL 2023 main conference** (2023.eacl-main.145) |
| 6 | `rafailov2023direct` | **作者顺序错误**: Ermon (4th) 和 Manning (5th) 位置互换了 |

### 中等问题 (venue updates needed)

| # | cite_key | 问题 |
|---|----------|------|
| 7 | `li2026qurl` | Venue 需更新: 已被 **ICLR 2026** 接收, 不再仅是 arXiv preprint; OpenReview 标题与 arXiv 标题不同 ("Low-Precision RL for Efficient Reasoning" vs "Efficient RL with Quantized Rollout") |
| 8 | `liu2026gdpo` | Venue 需更新: 已发表于 **ICML 2026** (poster), 不再是 arXiv preprint |

### 轻微问题 (minor)

| # | cite_key | 问题 |
|---|----------|------|
| 9 | `tan2022redocred` | 标题标点: bib 用冒号 `:`, 实际标题用破折号 `--` |
| 10 | `zhang2025glidre` | 标题大小写: "Model" 应为 "model" (小写) |
| 11 | `liu2026gdpo` | 标题大小写: "Reward" 应为 "reward", "Multi-Reward" 应为 "Multi-reward" |
| 12 | `ito2025mogrpo` | cite key "ito" 与第一作者 "Ichihara" 不匹配 (仅命名问题) |

### Cite key 与第一作者不匹配 (7 条)

这些 cite key 命名不符合 [第一作者姓][年份] 惯例, 可能让审稿人困惑:

| cite_key | bib 第一作者 | 应改为 |
|----------|-------------|--------|
| `xu2024lmrc` | Li, Xingzuo | `li2024lmrc` |
| `wang2025rear` | Luo, Jianwen | `luo2025rear` |
| `wang2025relprior` | Pi, Qiankun | `pi2025relprior` |
| `zhang2025glidre` | Armingaud, Robin | `armingaud2025glidre` |
| `tang2025rsftppo` | Anil, Gautham Govind | `anil2025rsftppo` |
| `wang2025rullm` | Zhang, Kunli | `zhang2025rullm` |
| `ito2025mogrpo` | Ichihara, Yuki | `ichihara2025mogrpo` |

### 未被引用的 bib 条目 (17 条)

以下条目存在于 references.bib 但从未在任何 .tex 文件中被 `\cite`/`\citep`/`\citet`:

`moskovitz2024constrained`, `dong2023raft`, `ito2025mogrpo`, `li2025drift`, `liu2026gdpo`, `zhang2025glidre`, `wang2025rullm`, `standley2020tasks`, `yu2020gradient`, `wang2023selfconsistency`, `ethayarajh2024kto`, `coste2024reward`, `hoffmann2022chinchilla`, `liu2026rift`, `deng2026trajfusion`, `tian2026mugrpo`, `ji2026treegrpo`

---

## 逐条结果

### 1. [autore2024] — ✓
- 真实性: ✓
- 作者: ✓ (Xue, Lilong; Zhang, Dan; Dong, Yuxiao; Tang, Jie)
- 年份: ✓ (2024)
- 标题: ✓ ("AutoRE: Document-Level Relation Extraction with Large Language Models")
- Venue: ✓ (ACL 2024 System Demonstrations)
- arXiv ID: ✓ (2403.14888)
- 正文用法: ✓ (intro: "fine-tune LLMs with structured decomposition")
- 备注: 无问题

### 2. [xu2025docksrag] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2025)
- 标题: ✓
- Venue: ✓ (ICML 2025)
- arXiv ID: N/A
- 正文用法: ✓ (intro: "combine retrieval-augmented generation with structured knowledge")
- 备注: 无问题

### 3. [dai2025r1re] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2025)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (2507.04642)
- 正文用法: ✓ (related work: "applications to structured IE include R1-RE")
- 备注: 无问题

### 4. [gao2023scaling] — ✓
- 真实性: ✓
- 作者: ✓ (Gao, Leo; Schulman, John; Hilton, Jacob)
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✓ (ICML 2023)
- arXiv ID: ✓ (2210.10760)
- 正文用法: ✓ (related work: "capacity-dependent scaling dynamics")
- 备注: 无问题

### 5. [hu2022lora] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2022)
- 标题: ✓
- Venue: ✓ (ICLR 2022)
- arXiv ID: ✓ (2106.09685)
- 正文用法: ✓ (method: "LoRA")
- 备注: 无问题

### 6. [li2026qurl] — ✗
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2026)
- 标题: ✓ (arXiv 标题正确; 但 OpenReview 标题不同: "QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning")
- Venue: ✗ (bib 写 arXiv preprint, 实际已被 ICLR 2026 接收)
- arXiv ID: ✓ (2602.13953)
- 正文用法: ✓ (experiments: "quantized-actor divergence")
- 备注: 需更新 venue 为 ICLR 2026; 需确认最终发表标题

### 7. [laban2022summac] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2022)
- 标题: ✓
- Venue: ✓ (TACL, Vol 10, pp 163-177)
- arXiv ID: N/A
- 正文用法: ✓ (related work: "NLI-based faithfulness evaluation")
- 备注: 无问题

### 8. [li2025srvf] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2025)
- 标题: ✓
- Venue: ✓ (AAAI 2025)
- arXiv ID: ✓ (2412.07289)
- 正文用法: ✓ (related work: "reward-based evidence grounding")
- 备注: 无问题

### 9. [jin2025rl_panacea] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2025)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (2508.16546)
- 正文用法: ✓ (related work: "catastrophic forgetting in RL alignment")
- 备注: 无问题

### 10. [ma2023dreeam] — ✗
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✗ (bib 写 "Findings of EACL 2023", 实际是 **EACL 2023 main conference**, ACL Anthology: 2023.eacl-main.145)
- arXiv ID: ✓ (2302.08675)
- 正文用法: ✓
- 备注: Venue 需从 "Findings of the Association for Computational Linguistics: EACL 2023" 改为 "Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics"

### 11. [moskovitz2024constrained] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (ICLR 2024)
- arXiv ID: N/A
- 正文用法: N/A (未在正文中引用)
- 备注: 无问题, 但未被引用

### 12. [rafailov2023direct] — ✗
- 真实性: ✓
- 作者: ✗ (Ermon, Stefano 应在第 4 位, Manning, Christopher D. 在第 5 位; bib 中两者顺序互换)
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✓ (NeurIPS 2023)
- arXiv ID: ✓ (2305.18290)
- 正文用法: ✓ (intro/method: "DPO")
- 备注: 修正作者顺序: ..., Mitchell, Eric and **Ermon, Stefano** and **Manning, Christopher D.** and Finn, Chelsea

### 13. [shao2024deepseekmath] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (2402.03300)
- 正文用法: ✓ (intro/method: "GRPO")
- 备注: 无问题

### 14. [tan2022redocred] — ✗ (minor)
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2022)
- 标题: ✗ (bib 用冒号 "Revisiting DocRED: Addressing...", 实际标题用破折号 "Revisiting DocRED -- Addressing...")
- Venue: ✓ (EMNLP 2022)
- arXiv ID: N/A
- 正文用法: ✓ (intro: "Re-DocRED")
- 备注: 轻微标点问题

### 15. [xiao2022sais] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2022)
- 标题: ✓
- Venue: ✓ (NAACL 2022)
- arXiv ID: N/A
- 正文用法: ✓ (intro: "introduce sentence-level evidence supervision")
- 备注: 无问题

### 16. [xie2022eider] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2022)
- 标题: ✓
- Venue: ✓ (Findings of ACL 2022)
- arXiv ID: ✓ (2106.08657)
- 正文用法: ✓ (related work: "fuses evidence into the relation classifier")
- 备注: 无问题

### 17. [xu2024lmrc] — ✗
- 真实性: ✓
- 作者: ✓ (Li, Xingzuo; Chen, Kehai; Long, Yunfei; Zhang, Min — 作者本身正确)
- 年份: ✓ (2024)
- 标题: ✗ (bib 写 "LMRC: LLM with Relation Classifier...", 实际 arXiv 标题无 "LMRC:" 前缀, 仅为 "LLM with Relation Classifier for Document-Level Relation Extraction")
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (2408.13889)
- 正文用法: ✓ (intro: "frame it as multi-choice reading comprehension")
- 备注: cite key "xu2024" 与第一作者 Li 不匹配; 标题需删除 "LMRC:" 前缀

### 18. [yao2019docred] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2019)
- 标题: ✓
- Venue: ✓ (ACL 2019)
- arXiv ID: N/A
- 正文用法: ✓ (intro: "DocRED")
- 备注: 无问题

### 19. [zelikman2022star] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2022)
- 标题: ✓
- Venue: ✓ (NeurIPS 2022)
- arXiv ID: ✓ (2203.14465)
- 正文用法: ✓ (intro/method: "STaR")
- 备注: 无问题

### 20. [dong2023raft] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✓ (TMLR)
- arXiv ID: ✓ (2304.06767)
- 正文用法: N/A (未在正文中引用)
- 备注: 无问题, 但未被引用

### 21. [ito2025mogrpo] — ✗ (minor)
- 真实性: ✓
- 作者: ✓ (Ichihara, Yuki 等 — 作者信息正确)
- 年份: ✓ (2025)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (2509.22047)
- 正文用法: N/A (未在正文中引用)
- 备注: cite key "ito2025" 与第一作者 "Ichihara" 不匹配; 未被引用

### 22. [li2025drift] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2025)
- 标题: ✓
- Venue: ✓ (ACL 2025)
- arXiv ID: N/A
- 正文用法: N/A (未在正文中引用)
- 备注: 无问题, 但未被引用

### 23. [liu2026gdpo] — ✗
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2026)
- 标题: ✗ (minor: "Reward" → "reward", "Multi-Reward" → "Multi-reward")
- Venue: ✗ (bib 写 arXiv preprint, 实际已发表于 **ICML 2026** poster)
- arXiv ID: ✓ (2601.05242)
- 正文用法: N/A (未在正文中引用)
- 备注: 需更新 venue 为 ICML 2026; 未被引用

### 24. [liu2025drgrpo] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2025)
- 标题: ✓
- Venue: ✓ (COLM 2025)
- arXiv ID: ✓ (2503.20783)
- 正文用法: ✓ (related work: "length bias")
- 备注: 无问题

### 25. [yu2025dapo] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2025)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (2503.14476)
- 正文用法: ✓ (related work: "entropy collapse")
- 备注: 无问题

### 26. [zhang2024infuse] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (EACL 2024)
- arXiv ID: N/A
- 正文用法: ✓ (related work: "NLI-based faithfulness evaluation")
- 备注: 无问题

### 27. [wang2025rear] — ✗ (minor)
- 真实性: ✓
- 作者: ✓ (Luo, Jianwen; Hong, Yu; Yang, Shuai; Yao, Jianmin — 作者信息正确)
- 年份: ✓ (2025)
- 标题: ✓
- Venue: ✓ (Findings of EMNLP 2025)
- arXiv ID: N/A
- 正文用法: ✓ (related work: "applications to structured IE include ... REAR")
- 备注: cite key "wang2025" 与第一作者 "Luo" 不匹配

### 28. [wang2025relprior] — ✗
- 真实性: ✓
- 作者: ✓ (Pi, Qiankun; Sun, Yepeng; Lu, Jicang; Fan, Qinlong; Huang, Ningbo; Wang, Shiyu — 作者信息正确)
- 年份: ✓ (2025)
- 标题: ✗ (bib: "RelPrior: Relation as a Prior for LLM-based Document-Level Relation Extraction"; 实际: "Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction")
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (2511.08143)
- 正文用法: ✓ (related work: "RelPrior leverages relation priors")
- 备注: 标题严重偏差; cite key "wang2025" 与第一作者 "Pi" 不匹配

### 29. [zhang2025glidre] — ✗ (minor)
- 真实性: ✓
- 作者: ✓ (Armingaud, Robin; Besançon, Romaric)
- 年份: ✓ (2025)
- 标题: ✗ (minor: "Model" 应为 "model")
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (2508.00757)
- 正文用法: N/A (未在正文中引用)
- 备注: cite key "zhang2025" 与第一作者 "Armingaud" 不匹配; 未被引用

### 30. [tang2025rsftppo] — ✓
- 真实性: ✓
- 作者: ✓ (Anil, Gautham Govind; Nagaraj, Dheeraj Mysore; Shanmugam, Karthikeyan; Shakkottai, Sanjay)
- 年份: ✓ (2025)
- 标题: ✓
- Venue: ✓ (ICML 2025 Workshop PUT)
- arXiv ID: N/A
- 正文用法: ✓ (related work: "theoretical connections to PPO")
- 备注: cite key "tang2025" 与第一作者 "Anil" 不匹配, 但所有事实正确

### 31. [wang2025rullm] — ✗
- 真实性: ✓
- 作者: ✗ (Springer 页面列 7 位作者, bib 有 8 位 — "Peng, Min" 可能不在正式作者列表中)
- 年份: ✓ (2025)
- 标题: ✗ (bib 添加了 "Ru-LLM:" 前缀, Springer 正式标题无此前缀: "Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction")
- Venue: ✗ (bib 用 `journal = {NLPCC 2025}`, 应为 `@inproceedings` + `booktitle = {Proceedings of the 14th CCF International Conference on Natural Language Processing and Chinese Computing}`)
- arXiv ID: N/A
- 正文用法: N/A (未在正文中引用)
- 备注: cite key "wang2025" 与第一作者 "Zhang" 不匹配; 多处问题; 未被引用

### 32. [zhou2021atlop] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2021)
- 标题: ✓
- Venue: ✓ (AAAI 2021)
- arXiv ID: ✓ (2010.11304)
- 正文用法: ✓ (intro: "encoder-based methods such as \citet{zhou2021atlop}")
- 备注: 无问题

### 33. [ruder2017overview] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2017)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (1706.05098)
- 正文用法: ✓ (related work: "negative transfer in multi-task learning")
- 备注: 无问题

### 34. [standley2020tasks] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2020)
- 标题: ✓
- Venue: ✓ (ICML 2020)
- arXiv ID: N/A
- 正文用法: N/A (未在正文中引用)
- 备注: 无问题, 但未被引用

### 35. [yu2020gradient] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2020)
- 标题: ✓
- Venue: ✓ (NeurIPS 2020)
- arXiv ID: ✓ (2001.06782)
- 正文用法: N/A (未在正文中引用)
- 备注: 无问题, 但未被引用

### 36. [wang2023selfconsistency] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✓ (ICLR 2023)
- arXiv ID: ✓ (2203.11171)
- 正文用法: N/A (未在正文中引用)
- 备注: 无问题, 但未被引用

### 37. [ouyang2022instructgpt] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2022)
- 标题: ✓
- Venue: ✓ (NeurIPS 2022)
- arXiv ID: ✓ (2203.02155)
- 正文用法: ✓ (method: "RLHF")
- 备注: 无问题

### 38. [schulman2017ppo] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2017)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (1707.06347)
- 正文用法: ✓ (related work: "PPO")
- 备注: 无问题

### 39. [zeng2020gain] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2020)
- 标题: ✓
- Venue: ✓ (EMNLP 2020)
- arXiv ID: N/A
- 正文用法: ✓ (related work: "GAIN")
- 备注: 无问题

### 40. [ethayarajh2024kto] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (ICML 2024)
- arXiv ID: ✓ (2402.01306)
- 正文用法: N/A (未在正文中引用)
- 备注: 无问题, 但未被引用

### 41. [coste2024reward] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (ICLR 2024)
- arXiv ID: ✓ (2310.02743)
- 正文用法: N/A (未在正文中引用)
- 备注: 无问题, 但未被引用

### 42. [he2023debertav3] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✓ (ICLR 2023)
- arXiv ID: ✓ (2111.09543)
- 正文用法: ✓ (method: "DeBERTaV3")
- 备注: 无问题

### 43. [dettmers2023qlora] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✓ (NeurIPS 2023)
- arXiv ID: ✓ (2305.14314)
- 正文用法: ✓ (method: "QLoRA")
- 备注: 无问题

### 44. [hoffmann2022chinchilla] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2022)
- 标题: ✓
- Venue: ✓ (NeurIPS 2022)
- arXiv ID: ✓ (2203.15556)
- 正文用法: N/A (未在正文中引用)
- 备注: 无问题, 但未被引用

### 45. [yuan2023rft] — ✓
- 真实性: ✓
- 作者: ✓
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (2308.01825)
- 正文用法: ✓ (related work: "scaling analyses")
- 备注: 无问题

### 46. [tamo2026evidencerl] — ✓
- 真实性: ✓ (arXiv 确认, 2026年3月提交, Georgia Tech / Peking University)
- 作者: ✓
- 年份: ✓ (2026)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (2603.19532)
- 正文用法: ✓ (related work: "reward-based evidence grounding")
- 备注: 2026 论文, 确认真实存在

### 47. [liu2026rift] — ✓
- 真实性: ✓ (arXiv 确认, 2026年1月提交, Huawei Noah's Ark Lab)
- 作者: ✓
- 年份: ✓ (2026)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (2601.09253)
- 正文用法: N/A (未在正文中引用)
- 备注: 2026 论文, 确认真实存在, 但未被引用

### 48. [deng2026trajfusion] — ✓
- 真实性: ✓ (arXiv 确认, 2026年2月提交, Microsoft)
- 作者: ✓
- 年份: ✓ (2026)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (2602.04391)
- 正文用法: N/A (未在正文中引用)
- 备注: 2026 论文, 确认真实存在, 但未被引用

### 49. [tian2026mugrpo] — ✓
- 真实性: ✓ (arXiv 确认, 2026年5月提交, Rice University)
- 作者: ✓
- 年份: ✓ (2026)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (2605.17570)
- 正文用法: N/A (未在正文中引用)
- 备注: 2026 论文, 确认真实存在, 但未被引用

### 50. [ji2026treegrpo] — ✓
- 真实性: ✓ (arXiv + OpenReview 确认)
- 作者: ✓
- 年份: ✓ (2026)
- 标题: ✓
- Venue: ✓ (ICLR 2026)
- arXiv ID: ✓ (2509.21240)
- 正文用法: N/A (未在正文中引用)
- 备注: 2026 论文, 确认真实存在, 但未被引用

### 51. [deepseek2025r1] — ✓
- 真实性: ✓
- 作者: ✓ (DeepSeek-AI)
- 年份: ✓ (2025)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv ID: ✓ (2501.12948)
- 正文用法: ✓ (related work: "DeepSeek-R1 demonstrates its effectiveness at scale")
- 备注: 无问题

### 52. [gulcehre2023rest] — ✗
- 真实性: ✓
- 作者: ✗ (bib 中 "Dyer, Chris" 和 "Grangier, David" 应为 **"Doucet, Arnaud"** 和 **"de Freitas, Nando"**)
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✗ (使用 `@inproceedings` + `booktitle = {arXiv preprint arXiv:2308.08998}` 格式非法; 应改为 `@article` + `journal`)
- arXiv ID: ✓ (2308.08998)
- 正文用法: ✓ (related work: "iterative self-improvement through rejection sampling")
- 备注: 两处严重错误: 作者名错误 + entry type 错误

---

## 2026 年引用验证结果

全部 7 条 2026 年引用均确认真实存在:

| cite_key | arXiv ID | 提交时间 | 状态 |
|----------|----------|----------|------|
| tamo2026evidencerl | 2603.19532 | 2026-03 | ✓ arXiv preprint |
| li2026qurl | 2602.13953 | 2026-02 | ✓ → ICLR 2026 (venue 需更新) |
| liu2026gdpo | 2601.05242 | 2026-01 | ✓ → ICML 2026 (venue 需更新) |
| deng2026trajfusion | 2602.04391 | 2026-02 | ✓ arXiv preprint |
| tian2026mugrpo | 2605.17570 | 2026-05 | ✓ arXiv preprint |
| ji2026treegrpo | 2509.21240 | 2025-09 | ✓ → ICLR 2026 |
| liu2026rift | 2601.09253 | 2026-01 | ✓ arXiv preprint |

---

## 必须修复的条目 (按优先级)

### P0 — 严重错误 (reviewer 可能标记)

1. **`gulcehre2023rest`**: 替换作者 Dyer→Doucet, Grangier→de Freitas; 改 `@article`+`journal`
2. **`ma2023dreeam`**: booktitle 改为 EACL 2023 main (非 Findings)
3. **`wang2025relprior`**: 标题改为 "Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction"
4. **`rafailov2023direct`**: 交换 Ermon 和 Manning 的顺序
5. **`xu2024lmrc`**: 删除标题中 "LMRC:" 前缀
6. **`wang2025rullm`**: 删除 "Ru-LLM:" 前缀; 核实作者; 改 entry type

### P1 — 中等 (venue outdated)

7. **`li2026qurl`**: venue 更新为 ICLR 2026
8. **`liu2026gdpo`**: venue 更新为 ICML 2026

### P2 — 轻微

9. **`tan2022redocred`**: 标题冒号改破折号
10. **`zhang2025glidre`**: "Model" → "model"

### P3 — 清理

11. 移除 17 条未被引用的 bib 条目 (或在正文中补充引用)
12. 修正 7 个 cite key 使其与第一作者匹配 (可选, 但建议)
