# LaLonde 式端到端验证 — 候选数据集筛选

## 筛选标准

1. **公开可得**的 RCT 数据集（可直接下载）
2. 有**文本变量**可作为 effect modifier Z（LLM 可对文本做二元分类）
3. 有**个体级结局变量** Y 和**二元处理变量** T
4. 样本量 ≥ 1,000
5. RCT 随机化保证 true CATE 可直接从数据计算
6. 文本变量的 LLM 标注在不同子群间有**异质性误差**

---

## 候选数据集

### 1. Hangartner et al. (2021) — Empathy Counterspeech Twitter 实验 ⭐ 可行性: 4.5/5

- **来源论文**: Hangartner, Gennaro, Alasiri et al. "Empathy-based counterspeech can reduce racist hate speech in a social media field experiment." *PNAS*, 118(50), 2021.
- **下载链接**: [Harvard Dataverse doi:10.7910/DVN/ARZ9PU](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/ARZ9PU)（匿名化文本数据 + 分析代码）
- **样本量**: 1,350 发布仇恨言论的 Twitter 用户
- **处理变量 T**: 反言论干预类型（共情 vs. 幽默 vs. 警告 vs. 控制组），可二元化为"共情干预 vs. 非共情"
- **结局变量 Y**: 后续 4 周内发布的仇恨言论数量（count）/ 是否删除原推文（binary）
- **文本 moderator Z**: 原始仇恨言论推文的文本内容。二元分类定义："显式仇恨言论"（含明确种族歧视词汇/侮辱性语言）vs."隐式仇恨言论"（使用编码语言、暗示、讽刺等委婉表达）
- **Z 的二元分类**: LLM 阅读原始推文文本，判断是否包含 explicit derogatory terms / racial slurs（显式）vs. coded/implicit xenophobic rhetoric（隐式）
- **子群定义**: (1) 推文长度（短 vs. 长），(2) 仇恨对象（anti-Black vs. anti-immigrant vs. anti-Muslim），(3) 语言复杂度（简单直白 vs. 复杂修辞）
- **异质性预期**: LLM 对含明确种族歧视词汇的短推文分类精度高（>95%），对使用隐喻、暗语、反讽的长推文分类精度显著下降（~70-80%）。不同仇恨对象的推文使用不同词汇库，LLM 在熟悉话题（如 anti-Black racism）上表现更好，在小众话题（如 anti-Roma）上误差更大。
- **优势**:
  - 真实文本数据（自然推文），非模板生成
  - RCT 设计，T 完全随机化
  - 文本变异性高，LLM 误差异质性自然存在
  - 直接相关于 LLM 标注用例（hate speech classification 是 LLM 常见应用）
  - 研究团队使用 ML 模型识别仇恨言论，数据中可能已有部分分类标注作为 ground truth
  - 高影响力论文（PNAS），数据质量有保证
- **风险**:
  - N=1,350 可能导致子群分析（3-4 个子群）统计功效偏低
  - 匿名化处理可能改变了原始文本（paraphrasing）
  - 处理变量有 4 个臂，二元化需要合理理由
  - 需要验证 Harvard Dataverse 中是否包含实际推文文本还是仅有编码变量
- **Ground truth Z 来源**: (1) 研究者的 ML 分类器输出；(2) 基于关键词/正则表达式的客观分类（有特定侮辱性词汇 → explicit）；(3) 可额外招募众包标注者标注 1,350 条推文

---

### 2. Hainmueller, Hopkins & Yamamoto (2014) — Immigration Conjoint 实验 ⭐ 可行性: 4/5

- **来源论文**: Hainmueller, Hopkins, Yamamoto. "Causal Inference in Conjoint Analysis: Understanding Multidimensional Choices via Stated Preference Experiments." *Political Analysis*, 22(1):1-30, 2014.
- **下载链接**: R 包 `cjoint`（`immigrationconjoint` 数据集）直接可用；[Harvard Dataverse doi:10.7910/DVN/25505](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/25505)
- **样本量**: 13,960 个移民档案评估（~1,396 受访者 × 5 对 × 2 档案）
- **处理变量 T**: 任一随机化属性，如 Country of Origin 二元化为 "高收入国家 vs. 低收入国家"，或 Prior Trips to US 二元化
- **结局变量 Y**: 是否选择接纳该移民（binary：Chosen=1/0）
- **文本 moderator Z**: 另一随机化属性，如 Education（大学及以上 vs. 以下）或 Language Skills（fluent English vs. limited）
- **Z 的二元分类**: 将档案的结构化属性拼接为自然语言文本描述（如 "A 35-year-old male from Germany with a PhD in Computer Science, fluent in English, plans to work as a research scientist..."），让 LLM 从文本中分类 Z（如判断教育水平是否为大学及以上）
- **子群定义**: 不同属性组合构成子群（如高技能职业+低学历 vs. 低技能职业+高学历），制造 LLM 分类难度差异
- **异质性预期**: 当文本描述中职业和教育水平一致时（如 "PhD + research scientist"），LLM 轻松正确分类教育水平；当不一致时（如 "PhD + janitor" 或 "no formal education + doctor"），LLM 可能被职业信息干扰而误判教育水平。不同国家背景也影响 LLM 的教育分类先验。
- **优势**:
  - N 大（13,960 观测值），子群分析统计功效充足
  - 完全随机化设计，所有属性正交，true CATE 可直接计算
  - Ground truth Z 100% 已知（来自实验设计）
  - 数据即装即用（R 包内置）
  - 可灵活选择 T 和 Z 的定义
  - 可构造多个子群，控制 LLM 误差异质性的来源
- **风险**:
  - 原始数据是结构化属性，非自然文本 → 需要额外步骤生成文本描述
  - 生成的文本是"半合成"的，审稿人可能质疑"为什么不直接用结构化变量"
  - 需要精心设计文本生成模板，使其足够自然且引入合理的 LLM 分类难度
- **Ground truth Z 来源**: 实验设计本身（属性值是研究者控制的随机变量）

---

### 3. Bertrand & Mullainathan (2004) — Resume Audit Study ⭐ 可行性: 3/5

- **来源论文**: Bertrand, Mullainathan. "Are Emily and Greg More Employable Than Lakisha and Jamal? A Field Experiment on Labor Market Discrimination." *American Economic Review*, 94(4):991-1013, 2004.
- **下载链接**: [openICPSR doi:10.3886/E116023V1](https://www.openicpsr.org/openicpsr/project/116023/version/V1/view)；R 包 `AER`（ResumeNames 数据集）
- **样本量**: 4,870 份虚构简历
- **处理变量 T**: 种族（White vs. Black sounding name），完全随机化
- **结局变量 Y**: 是否收到面试回电（callback, binary）
- **文本 moderator Z**: 简历质量（高 vs. 低），由研究者设计。高质量简历有更多工作经验、技能、荣誉等。
- **Z 的二元分类**: 从编码变量重构简历文本（如 "5 years of experience in marketing, honors graduate, fluent in multiple languages..."），让 LLM 判断简历质量高低
- **子群定义**: (1) 行业（金融 vs. 服务业），(2) 城市（Boston vs. Chicago），(3) 雇主规模
- **异质性预期**: 不同行业的简历使用不同术语，LLM 对金融行业简历的质量判断可能比服务业更准确（因训练数据偏向白领岗位）
- **优势**:
  - 经典 LaLonde 式数据集，政治经济学界高度认可
  - N=4,870 足够大
  - 简历的"高/低质量"已由研究者在实验设计中控制
  - 种族歧视的 HTE（白人名字在高质量简历上获益更多）已被文献记录
- **风险**:
  - 数据集只有 63 个编码变量，**没有原始简历文本**
  - 从编码变量重构文本是人工合成的，与 Conjoint 方案类似但更粗糙
  - 重构的文本可能不够自然
- **Ground truth Z 来源**: 研究者设计的简历质量分类（编码变量组合）

---

### 4. Kalla & Broockman (2020) — 减少排斥性态度实验 ⭐ 可行性: 2.5/5

- **来源论文**: Kalla, Broockman. "Reducing Exclusionary Attitudes through Interpersonal Conversation: Evidence from Three Field Experiments." *American Political Science Review*, 114(2):410-425, 2020.
- **下载链接**: [Harvard Dataverse doi:10.7910/DVN/8BFYQO](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/8BFYQO)
- **样本量**: 6,869 选民（3 个实验）
- **处理变量 T**: 对话类型（叙事+论据 vs. 仅论据 vs. 控制组）
- **结局变量 Y**: 排斥性态度变化（偏见量表得分）
- **文本 moderator Z**: 需从调查问卷的开放式回答中提取
- **Z 的二元分类**: LLM 分类开放式回答中是否提及个人经历（"提及个人经历" vs. "仅抽象论述"）
- **子群定义**: 受访者所在地区、年龄段、政治倾向
- **异质性预期**: LLM 在识别详细个人叙事时准确率高，在简短模糊回答中准确率低
- **优势**: 大 N，知名实验，Harvard Dataverse 公开
- **风险**:
  - **不确定是否包含开放式文本数据**（复制数据可能只有编码变量）
  - 处理变量有 3+ 个条件
  - 文本变量（如果有）可能质量参差不齐
- **Ground truth Z 来源**: 需要人工标注开放式回答

---

### 5. Bail et al. (2018) — Twitter 政治极化实验 ⭐ 可行性: 2.5/5

- **来源论文**: Bail, Argyle, Brown et al. "Exposure to Opposing Views on Social Media can Increase Political Polarization." *PNAS*, 115(37):9216-9221, 2018.
- **下载链接**: [Harvard Dataverse doi:10.7910/DVN/NSESEH](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/NSESEH)
- **样本量**: 1,239 Twitter 活跃用户（697 民主党 + 542 共和党）
- **处理变量 T**: 是否关注对立阵营的 Twitter bot（binary）
- **结局变量 Y**: 政治态度变化（7 点量表）
- **文本 moderator Z**: 参与者自己的推文（pre-treatment）→ LLM 分类为 "高政治参与度" vs. "低政治参与度"
- **子群定义**: 推文频率、推文话题、推文情感
- **异质性预期**: LLM 对频繁发布政治内容的用户容易识别"高政治参与"，对偶尔发布混合内容的用户判断困难
- **优势**: 知名实验，Harvard Dataverse 公开
- **风险**:
  - N=1,239 偏小
  - 变量已做统计披露控制（coarsened），推文文本可能未包含
  - 研究者明确声明为保护隐私做了数据脱敏
- **Ground truth Z 来源**: 参与者的 Twitter 活动量化指标（如推文频率、政治关键词比例）

---

### 6. Grigorieff, Roth & Ubfal (2020) — 移民信息实验 ⭐ 可行性: 2.5/5

- **来源论文**: Grigorieff, Roth, Ubfal. "Does Information Change Attitudes Toward Immigrants?" *Demography*, 57(3):1117-1143, 2020.
- **下载链接**: [OSF https://osf.io/rhz8n/](https://osf.io/rhz8n/)
- **样本量**: 2,000（800 MTurk + 1,200 代表性样本）
- **处理变量 T**: 移民信息包（提供统计数据 vs. 控制组），binary
- **结局变量 Y**: 对移民的态度量表
- **文本 moderator Z**: 需从开放式回答或 treatment text 提取
- **Z 的二元分类**: 不太自然——treatment 本身就是文本，但 Z 应该是 pre-treatment 变量
- **子群定义**: 受访者所在州、先前对移民比例的估计
- **异质性预期**: 不明确
- **优势**: OSF 公开，代表性样本
- **风险**:
  - **没有自然的文本 moderator 变量**——treatment 本身是信息文本
  - Z 需要从参与者特征或开放式回答中构造，不自然
- **Ground truth Z 来源**: 需要额外定义和标注

---

### 7. Pennycook & Rand (2020) — 准确性提示与虚假信息分享 ⭐ 可行性: 2/5

- **来源论文**: Pennycook et al. "Fighting COVID-19 Misinformation on Social Media." *Psychological Science*, 31(7):770-780, 2020.
- **下载链接**: [OSF https://osf.io/7d3xh/](https://osf.io/7d3xh/)
- **样本量**: ~1,700 参与者 × ~30 条新闻标题 ≈ 51,000 观测值
- **处理变量 T**: 准确性提示（是否先评判一条无关标题的准确性），binary
- **结局变量 Y**: 分享意愿
- **文本 moderator Z**: 新闻标题的主题/政治倾向（LLM 分类）
- **Z 的二元分类**: LLM 判断标题是否涉及争议性政治话题
- **子群定义**: 标题长度、来源可信度、话题
- **异质性预期**: 对明确的政治标题分类容易，对边缘话题困难
- **优势**: OSF 公开，有标题文本
- **风险**:
  - 独立标题仅 ~30 条，LLM 分类几乎无误差空间
  - 数据结构是 repeated measures（受试者内设计），需要多层模型
  - 标题文本太短（<15 词），LLM 分类难度低
- **Ground truth Z 来源**: 研究者已对标题做了真伪标注

---

## 最佳候选执行计划

**推荐方案 A（首选）：Hangartner et al. (2021) Counterspeech 实验**

适合场景：论文需要一个"真实文本 + 真实 RCT"的端到端验证。

### 执行步骤

1. **数据获取**：从 Harvard Dataverse (doi:10.7910/DVN/ARZ9PU) 下载匿名化推文数据和实验变量
2. **数据验证**：确认数据中包含推文文本（非仅编码变量），统计可用样本量
3. **定义 Z**：将推文分为 "explicit hate speech"（含明确侮辱性词汇）vs. "implicit/coded hate speech"（无明确侮辱词但含仇恨语义）
4. **构建 Ground Truth Z**：
   - 方法 1（首选）：基于研究者已有的 ML 分类器输出
   - 方法 2（备选）：编制显式仇恨词汇表（racial slurs, derogatory terms），用关键词匹配作为 ground truth
   - 方法 3（最严格）：招募 3-5 名标注者对 1,350 条推文进行专家标注
5. **LLM 标注 Z**：使用 GPT-4 / Claude 对推文文本做 explicit vs. implicit 分类
6. **定义子群 S**：
   - 推文长度（≤50 chars vs. >50 chars）
   - 仇恨对象（anti-Black vs. anti-immigrant vs. other）
   - 包含 URL/media 与否
7. **验证 LLM 误差异质性**：计算各子群的混淆矩阵，确认子群间分类精度显著不同
8. **二元化 T**：合并 humor + warning + control 为一组，empathy 为另一组（或 all treatments vs. control）
9. **估计 CATE**：
   - True CATE：使用 ground truth Z，直接从 RCT 数据计算 E[Y(1)-Y(0)|Z=1] - E[Y(1)-Y(0)|Z=0]
   - Naive CATE：使用 LLM 标注的 Z 计算
   - EC-HTE CATE：使用 LLM 标注的 Z + 子群级混淆矩阵校正
10. **报告**：展示 |EC-HTE - True| < |Naive - True|，证明校正有效

### 预期挑战
- N=1,350 可能导致 CATE 估计的置信区间较宽 → 可用 bootstrap 评估
- 若匿名化文本被过度处理（如只保留 bag-of-words），LLM 分类质量下降 → 需先验证文本质量
- 需要 CATE 本身非零（即 empathy 干预对 explicit vs. implicit hate speech 效果不同）→ 先做探索性分析

---

**推荐方案 B（备选）：Hainmueller et al. (2014) Immigration Conjoint + 文本化**

适合场景：如果方案 A 的文本数据不可用或 N 不足，用此方案。N 更大（13,960），ground truth 完全可控，但需要额外的文本生成步骤。

### 执行步骤

1. **数据获取**：`install.packages("cjoint"); data(immigrationconjoint)`
2. **选择 T 和 Z**：
   - T = Country of Origin（二元化：高收入国家 vs. 低收入国家）
   - Z = Education（大学及以上 vs. 以下）
3. **生成文本描述**：用模板 + GPT-4 将每个档案的 9 个属性拼接为自然语言段落（~50-100 词），模拟真实移民申请描述。每个档案的文本只使用一个模板变体，避免信息泄漏。
4. **LLM 标注 Z**：让另一个 LLM（如 Claude）从生成的文本中分类教育水平
5. **定义子群 S**：按职业类型（高技能 vs. 低技能）和国家背景分组
6. **后续步骤同方案 A 的 7-10**

### 注意事项
- 论文中需清晰说明文本生成的动机：模拟"真实场景下文本数据替代结构化变量"
- 可在 appendix 同时报告结构化变量的 oracle 结果作为对照

---

**推荐策略：先尝试方案 A，如果 Hangartner 数据中的文本不可用或质量不足，退回方案 B。两个方案可以并行准备。**

---

## 搜索日志

### 搜索轮次 1：广域搜索（6 queries）

| 查询 | 关键发现 |
|------|----------|
| `Broockman Kalla 2016 canvassing experiment replication data download` | Harvard Dataverse (DVN/WKR39N) 有复制数据，但可能无文本变量 |
| `political science RCT text data public dataset replication` | 政治学期刊普遍要求复制数据，但多数实验不含文本 |
| `social media experiment RCT text data public` | World Bank FB Messenger 实验（公开）；SHAPE-UP 运动实验（N 小） |
| `conjoint experiment text vignette public replication data` | Hainmueller et al. 数据在 R 包 cjoint 中，13,960 observations |
| `causal inference NLP text treatment effect dataset benchmark` | CausalNLP 工具包有 Amazon review 半合成数据；领域内缺乏真实因果基准 |
| `nudge experiment text framing RCT open data` | Milkman 疫苗 nudge 大规模实验；COVID 疫苗文本干预实验 |

### 搜索轮次 2：精准搜索（6 queries）

| 查询 | 关键发现 |
|------|----------|
| `Egami Fong Grimmer Imai Roberts text causal inference replication data` | Fong & Grimmer 候选人档案实验，数据由作者分享（非公开） |
| `Harvard Dataverse randomized experiment text moderator effect heterogeneity` | PNAS 2024 论文关于 omitted moderators，N>11,000 |
| `Messing Westwood 2014 partisan news source cues replication data` | 选择性暴露实验，未找到明确的公开数据链接 |
| `survey experiment randomized text treatment vignette open data political` | 大量方法论文献，无直接可用数据集 |
| `CausalNLP Amazon review semi-synthetic dataset download` | GitHub 有代码，半合成数据（outcome 是模拟的），不符合"真实因果数据"要求 |
| `"text as treatment" causal inference dataset Roberts Stewart Tingley` | Egami et al. 2022 Science Advances 框架论文，应用于移民态度和官僚回应实验 |

### 搜索轮次 3：候选深入评估（6 queries）

| 查询 | 关键发现 |
|------|----------|
| `Munger 2017 counterspeech Twitter experiment sanctioning data` | N=~2,387 用户，复制材料在作者网站，但每组 N 偏小 |
| `Bail 2018 Twitter bot polarization experiment sample size` | N=1,239（697 Dem + 542 Rep），变量已做统计披露控制 |
| `resume audit study experiment text data public download` | Braun et al. 2026 大规模简历审计 (N=36,880)，但公开时间不确定 |
| `Kalla Broockman 2018 reducing prejudice field experiment data` | Harvard Dataverse (DVN/8BFYQO)，3 个实验 N=6,869 |
| `civil comments toxicity labels Jigsaw public download` | 1.8M 评论，CC0 协议，Kaggle/TensorFlow Datasets 可下载——但非 RCT |
| `persuasion Reddit ChangeMyView experiment dataset causal` | ChangeMyView 有 delta 标签，但非 RCT，不可计算 true CATE |

### 搜索轮次 4：数据可用性验证（6 queries）

| 查询 | 关键发现 |
|------|----------|
| `Bertrand Mullainathan resume experiment data variables openicpsr` | 4,870 obs × 63 coded vars，无原始简历文本，R 包 AER 可用 |
| `Einstein Glick 2017 audit study landlord housing discrimination email text data` | N=~1,000，复制失败论文存在，数据可用性不确定 |
| `Grigorieff Roth Ubfal immigration information experiment replication data` | OSF (osf.io/rhz8n/)，N=2,000，但 Z 需要从 participant 特征构造 |
| `Hainmueller Hopkins immigration conjoint experiment data R cjoint` | 13,960 obs × 16 vars，R 包 cjoint 内置，即装即用 |
| `crowdsourcing experiment text annotation randomized public data` | 有 GPT vs. MTurk 标注对比研究，但非因果推断 RCT |
| `Kalla Broockman 2022 narrative strategies text data replication` | Harvard Dataverse，但不确定是否含文本 |

### 搜索轮次 5：Top 候选深度验证（6 queries）

| 查询 | 关键发现 |
|------|----------|
| `Hangartner counterspeech PNAS 2021 Harvard Dataverse DVN/ARZ9PU` | **匿名化文本数据**在 DVN/ARZ9PU，1,350 用户，ITT analysis |
| `Giulietti Tonin Vlassopoulos 2019 racial discrimination email replication data` | N=19,000+，但复制数据下载链接未找到 |
| `Broockman Kalla 2016 DVN WKR39N Harvard Dataverse variables` | 确认 DVN/WKR39N 可访问 |
| `Hainmueller Hopkins immigration conjoint data sample size R cjoint` | 确认 13,960 obs × 16 vars，9 个属性 |
| `COVID vaccine text message nudge RCT large scale public data` | Milkman N=47,306/113,229，但 text 是 treatment 非 moderator |
| `Dai Milkman Riis 2021 vaccine nudge RCT replication data` | 同上，文本消息是干预手段，不适合做 effect modifier |

### 搜索轮次 6：最终补充（6 queries）

| 查询 | 关键发现 |
|------|----------|
| `Hangartner counterspeech PNAS 2021 data variables tweet text` | 确认 Harvard Dataverse 有匿名化文本，需验证文本质量 |
| `Butler Broockman 2011 state legislators email experiment race` | Yale ISPS 有复制数据，N 未确认 |
| `White 2019 racial discrimination public services email 19000` | 确认 N=19,000+，6 类公共服务，数据公开性不确定 |
| `Grose 2024 large resume audit study 36000` | 2026 arxiv 预印本，N=36,880，但数据公开时间未知 |
| `Milkman 2021 mega study vaccine nudge 22 conditions PNAS` | N=47,306，19 个 nudge 条件，非 text moderator |
| `Pennycook Rand misinformation accuracy nudge replication data OSF` | OSF 有数据 (osf.io/7d3xh/)，但仅 ~30 条标题 |

### 搜索轮次 7：最终候选（2 queries）

| 查询 | 关键发现 |
|------|----------|
| `Upworthy Research Archive headline A/B test dataset` | 32,487 A/B tests，OSF 公开 (osf.io/jd64p/)，但 text 是 treatment 非 moderator |
| `Pennycook Rand misinformation news headline veracity sharing replication data` | OSF 有完整数据和材料 |

### 排除的候选

| 数据集 | 排除原因 |
|--------|----------|
| World Bank FB Messenger 性别规范实验 | 文本是 treatment，非 effect modifier |
| Upworthy Archive (32K A/B tests) | 文本是 treatment（标题变体），非 pre-treatment moderator |
| CausalNLP Amazon Review | 半合成数据（outcome 是模拟的），不满足"真实因果数据"要求 |
| Civil Comments / Jigsaw (1.8M comments) | 非 RCT，无随机化处理变量 |
| ChangeMyView Reddit | 非 RCT，无随机化 |
| Milkman 疫苗 Nudge (N=47K-113K) | 文本消息是 treatment 而非 moderator |
| Munger (2017) Counterspeech | N=~240/treatment arm，过小 |
| MDRC Higher Education RCT (ICPSR) | 需 IRB 批准和限制性数据协议，非公开 |
