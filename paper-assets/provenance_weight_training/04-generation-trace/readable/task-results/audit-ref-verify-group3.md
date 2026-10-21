# audit ref verify group3

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref-verify-group3_20260526T103554_result.json`
- **Structured JSON:** [`24c8936f7293a4ed11ec.json`](../../sessions/24/24c8936f7293a4ed11ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. The `.bbl` confirms that only 21 of these 40 entries are actually cited in the compiled paper; the rest are dead bib entries. Let me compile the final report.

---

## 验证结果

**[38] muennighoff2023scaling — ✅**
  标题: OK
  作者: OK
  年份: OK (2023)
  Venue: OK (NeurIPS 2023)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[39] openai2023gpt4 — ✅**
  标题: OK
  作者: OK (corporate author OpenAI)
  年份: OK (2023)
  Venue: OK (arXiv preprint)
  arXiv: OK (2303.08774)
  引用上下文: 未在正文中引用（dead bib entry）

**[40] guo2017calibration — ✅**
  标题: OK
  作者: OK
  年份: OK (2017)
  Venue: OK (ICML 2017)
  arXiv: N/A
  引用上下文: OK — "Score calibration~\citep{guo2017calibration}"，该论文确实关于神经网络校准

**[41] kish1965survey — ✅**
  标题: OK
  作者: OK (Leslie Kish)
  年份: OK (1965)
  Venue: OK (Wiley)
  arXiv: N/A
  引用上下文: OK — 用于 ESS（有效样本量）概念，该书确实定义了 ESS

**[42] owen2013mc — ✅**
  标题: OK
  作者: OK (Art B. Owen)
  年份: OK (2013)
  Venue: OK (Self-published, Stanford)
  arXiv: N/A
  引用上下文: OK — "standard property of exponential tilting"，Owen 的书第 9 章确实覆盖重要性采样

**[43] sagawa2020dro — ✅**
  标题: OK
  作者: OK
  年份: OK (2020)
  Venue: OK (ICLR 2020)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[44] hans2024binoculars — ❌ 作者严重错误**
  标题: OK
  作者: ❌ — "Valeriia Cheber" 应为 **Valeriia Cherepanova**；"Hami Alon" 应为 **Hamid Kazemi**；缺少 **Aniruddha Saha** 和 **Jonas Geiping**（实际 8 位作者，bib 只列 6 位且 2 个名字拼错）
  年份: OK (2024)
  Venue: OK (ICML 2024)
  arXiv: N/A
  引用上下文: OK — "cross-perplexity ratios~\citep{hans2024binoculars}"，Binoculars 确实使用交叉困惑度比

**[45] bao2024fastdetectgpt — ✅**
  标题: OK
  作者: OK
  年份: OK (2024)
  Venue: OK (ICLR 2024)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[46] gadre2024datacomp — ❌ 作者顺序错误**
  标题: OK
  作者: ❌ — 第一作者应为 **Jeffrey Li**，非 Gadre（Gadre 排第 6）；Gabriel Ilharco 亦非前列作者。该论文有 60+ 位作者
  年份: OK (2024)
  Venue: OK (NeurIPS 2024)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[47] kirchenbauer2023watermark — ✅**
  标题: OK
  作者: OK
  年份: OK (2023)
  Venue: OK (ICML 2023)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[48] abbas2023semdedup — ⚠️ Venue 有误**
  标题: OK
  作者: OK
  年份: OK (2023)
  Venue: ⚠️ — bib 写 ICLR 2023，实际发表于 **ICLR 2023 Workshop (ME-FoMo / MRL)**，非主会议。建议改为 workshop 或标注为 arXiv preprint
  arXiv: N/A
  引用上下文: OK — "deduplication~\citep{abbas2023semdedup}"，SemDeDup 确实关于语义去重

**[49] lin2017focal — ✅**
  标题: OK
  作者: OK
  年份: OK (2017)
  Venue: OK (ICCV 2017)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[50] gerstgrasser2024collapse — ❌ 作者大面积伪造**
  标题: OK
  作者: ❌ — bib 列出 7 人中 5 人不存在于真实作者列表：**"Apratim Foote"、"Lowell Zhong"、"Yuhao Li"、"Aaron Parisi"、"Hossein Mobahi" 全部是错误名字**。实际 14 位作者：Gerstgrasser, Schaeffer, **Dey**, **Rafailov**, **Sleight**, **Hughes**, **Korbak**, **Agrawal**, **Pai**, **Gromov**, **Roberts**, **Yang**, **Donoho**, **Koyejo**
  年份: OK (2024)
  Venue: ⚠️ — bib 写 arXiv preprint，实际已发表于 **COLM 2024**
  arXiv: OK (2404.01413)
  引用上下文: 未在正文中引用（dead bib entry）

**[51] gururangan2020dont — ✅**
  标题: OK
  作者: OK
  年份: OK (2020)
  Venue: OK (ACL 2020)
  arXiv: N/A
  引用上下文: OK — "domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}"，该论文确实关于领域自适应预训练

**[52] wettig2024qurating — ✅**
  标题: OK
  作者: OK
  年份: OK (2024)
  Venue: OK (ICML 2024)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[53] groeneveld2024olmo — ❌ 作者有误**
  标题: OK
  作者: ❌ — **Yonatan Bisk 不是该论文作者**（该论文有 43 位作者，Bisk 不在其中）。应删除 Bisk 或改为 "and others"
  年份: OK (2024)
  Venue: OK (ACL 2024)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[54] xia2024less — ✅**
  标题: OK
  作者: OK
  年份: OK (2024)
  Venue: OK (ICML 2024)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[55] dohmatob2024tale — ✅**
  标题: OK
  作者: OK
  年份: OK (2024)
  Venue: OK (ICML 2024)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[56] mindermann2022prioritized — ❌ 作者大面积伪造**
  标题: OK
  作者: ❌ — bib 列出 6 人中 4 人是伪造的：**"Matthew Rahtz"、"Congyue Ge"、"Irina Higgins"、"Annika Ho" 全部不是该论文作者**。实际 11 位作者：Mindermann, Brauner, **Razzak**, **Sharma**, **Kirsch**, **Xu**, **Höltgen**, **Gomez**, **Morisot**, **Farquhar**, **Gal**
  年份: OK (2022)
  Venue: OK (ICML 2022)
  arXiv: N/A
  引用上下文: OK — "instance-level strategies~\citep{...mindermann2022prioritized...}"，该论文确实关于实例级优先训练

**[57] tay2023scale — ❌ 年份/Venue 错误**
  标题: OK
  作者: OK
  年份: ❌ — 应为 **2022**，非 2023
  Venue: ❌ — 应为 **ICLR 2022**，非 ICLR 2023（已通过 ICLR virtual site 和 OpenReview 确认）
  arXiv: N/A
  引用上下文: OK — "nonlinear PPL-to-accuracy transfer~\citep{tay2023scale}"，该论文确实研究预训练/微调 scaling 关系

**[58] dubey2024llama — ✅**
  标题: OK
  作者: OK
  年份: OK (2024)
  Venue: OK (arXiv preprint)
  arXiv: OK (2407.21783)
  引用上下文: 未在正文中引用（dead bib entry）

**[59] pruthi2020estimating — ✅**
  标题: OK
  作者: OK
  年份: OK (2020)
  Venue: OK (NeurIPS 2020)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[60] thakkar2023selfinfluence — ✅**
  标题: OK
  作者: OK
  年份: OK (2023)
  Venue: OK (EMNLP 2023, pp. 2033-2045)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[61] zhu2025toremi — ✅**
  标题: OK
  作者: OK
  年份: OK (2025)
  Venue: OK (arXiv preprint)
  arXiv: OK (2504.00695)
  引用上下文: 未在正文中引用（dead bib entry）

**[62] wu2025survey — ✅**
  标题: OK
  作者: OK
  年份: OK (2025)
  Venue: OK (Computational Linguistics 51(1):275-338)
  arXiv: N/A
  引用上下文: OK — "enable document-level weighting~\citep{wu2025survey}"，该综述覆盖 LLM 文本检测方法

**[63] yu2024mates — ❌ 作者错误**
  标题: OK
  作者: ❌ — 第三作者应为 **Chenyan Xiong**，非 Udit Bhatt
  年份: OK (2024)
  Venue: OK (NeurIPS 2024)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[64] lozhkov2024fineweb — ⚠️**
  标题: ⚠️ — 标题实为 HuggingFace 数据集 tagline，非正式论文标题。若引用 dataset card 则可接受，但正式论文 (NeurIPS 2024 D&B) 标题为 "The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale"（已由 penedo2024fineweb 单独引用）
  作者: OK（作为 dataset card 作者可接受）
  年份: OK (2024)
  Venue: OK（@misc 格式引用 dataset card）
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[65] tirumala2024d4 — ❌ 作者和年份均错误**
  标题: OK
  作者: ❌ — **Aram Markosyan** 和 **Luke Zettlemoyer** 不是该论文作者；缺少 **Daniel Simig** 和 **Ari S. Morcos**。正确作者：Kushal Tirumala, Daniel Simig, Armen Aghajanyan, Ari S. Morcos
  年份: ❌ — 应为 **2023**，非 2024
  Venue: ❌ — 应为 **NeurIPS 2023 (Datasets and Benchmarks Track)**，非 NeurIPS 2024
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[66] fan2023importance — ❌ 作者完全错误**
  标题: OK（论文确实存在）
  作者: ❌ — bib 写 "Fan, Jingfeng and Udell, Madeleine"，实际作者为 **Gil Kur, Eli Putterman, Alexander Rakhlin**。作者完全不匹配，疑似对另一篇论文的错误关联
  年份: OK (2023)
  Venue: OK (NeurIPS 2023)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[67] albalak2024survey — ✅**
  标题: OK
  作者: OK（14 位作者均匹配）
  年份: OK (2024)
  Venue: OK (TMLR 2024)
  arXiv: N/A
  引用上下文: OK — "see \citet{albalak2024survey}"，作为数据选择综述引用

**[68] oren2019dro — ✅**
  标题: OK
  作者: OK
  年份: OK (2019)
  Venue: OK (EMNLP 2019)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[69] wenzek2020ccnet — ✅**
  标题: OK
  作者: OK
  年份: OK (2020)
  Venue: OK (LREC 2020)
  arXiv: N/A
  引用上下文: OK — "perplexity filtering~\citep{wenzek2020ccnet}"，CCNet 确实使用困惑度过滤

**[70] thrush2025perplexity — ✅**
  标题: OK
  作者: OK
  年份: OK (2025)
  Venue: OK (ICLR 2025)
  arXiv: N/A
  引用上下文: 未在正文中引用（dead bib entry）

**[71] kazdan2025collapse — ✅**
  标题: OK
  作者: OK
  年份: OK (2025)
  Venue: OK (ICML 2025)
  arXiv: N/A
  引用上下文: OK — "accumulating real data avoids divergence~\citep{kazdan2025collapse}"，该论文确实研究数据积累避免模型坍塌

**[72] amin2025escaping — ✅**
  标题: OK
  作者: OK
  年份: OK (2025)
  Venue: OK (NeurIPS 2025)
  arXiv: N/A
  引用上下文: OK — "even minimal curation suffices~\citep{amin2025escaping}"，该论文研究弱数据防止坍塌

**[73] engstrom2024dsdm — ✅**
  标题: OK
  作者: OK
  年份: OK (2024)
  Venue: OK (ICML 2024)
  arXiv: N/A
  引用上下文: OK — 列为 instance-level 策略，DsDm 确实是模型感知的数据选择

**[74] grangier2025crisp — ✅**
  标题: OK
  作者: OK
  年份: OK (2025)
  Venue: OK (ICLR 2025)
  arXiv: N/A
  引用上下文: OK — "domain-level importance sampling~\citep{...grangier2025crisp...}"，该论文关于聚类重要性采样

**[75] naitsaada2025illusion — ✅**
  标题: OK
  作者: OK
  年份: OK (2025)
  Venue: OK (arXiv preprint)
  arXiv: OK (2510.00866)
  引用上下文: OK — "classifier-based quality scores may capture stylistic similarity rather than intrinsic quality"，该论文确实研究这一问题

**[76] cortes2010learning — ✅**
  标题: OK
  作者: OK
  年份: OK (2010)
  Venue: OK (NeurIPS 2010)
  arXiv: N/A
  引用上下文: OK — "generalization bounds governed by the weight second moment"，Cortes et al. 确实建立了重要性加权的泛化界

**[77] fang2020rethinking — ✅**
  标题: OK
  作者: OK
  年份: OK (2020)
  Venue: OK (NeurIPS 2020)
  arXiv: N/A
  引用上下文: OK — "naïve importance weighting degrades in deep networks under distribution shift"，该论文确实研究此问题

---

## 汇总

| 统计项 | 数量 |
|--------|------|
| **总数** | 40 |
| **✅ 无误** | 28 |
| **❌ 有错** | 10 |
| **⚠️ 小问题** | 2 |

### 问题清单（需修复）

| # | Key | 严重程度 | 问题 |
|---|-----|---------|------|
| **50** | gerstgrasser2024collapse | 🔴 严重 | 7 位作者中 5 位是**伪造名字**；venue 应为 COLM 2024 非 arXiv |
| **56** | mindermann2022prioritized | 🔴 严重 | 6 位作者中 4 位是**伪造名字**（Rahtz/Ge/Higgins/Ho→Razzak/Sharma/Kirsch/Xu/Höltgen/Gomez/Morisot/Farquhar/Gal） |
| **66** | fan2023importance | 🔴 严重 | 作者**完全错误**（Fan & Udell→Kur, Putterman, Rakhlin） |
| **44** | hans2024binoculars | 🟠 高 | 2 个作者名拼错（Cheber→Cherepanova, Hami Alon→Hamid Kazemi），缺 2 位作者 |
| **65** | tirumala2024d4 | 🟠 高 | 2 个作者错误（Markosyan/Zettlemoyer→Simig/Morcos）；年份和 venue 均错（NeurIPS 2023 非 2024） |
| **57** | tay2023scale | 🟡 中 | 年份/venue 错误：ICLR **2022** 非 2023 |
| **53** | groeneveld2024olmo | 🟡 中 | Yonatan Bisk 不是作者，应删除 |
| **63** | yu2024mates | 🟡 中 | 第三作者错误：Chenyan Xiong 非 Udit Bhatt |
| **46** | gadre2024datacomp | 🟡 中 | 第一作者应为 Jeffrey Li，非 Gadre；Ilharco 非前列作者 |
| **48** | abbas2023semdedup | ⚠️ 低 | Venue 为 ICLR 2023 **Workshop (ME-FoMo/MRL)**，非主会议 |

### 额外发现

**19 条 dead bib entries**（在 `references.bib` 中但未被正文 `\cite`）：38, 39, 43, 45, 46, 47, 49, 50, 52, 53, 54, 55, 58, 59, 60, 61, 63, 65, 66, 68, 70。建议清理或确认是否遗漏了引用。

---
