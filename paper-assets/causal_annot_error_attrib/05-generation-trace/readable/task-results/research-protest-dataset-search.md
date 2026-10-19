# research protest dataset search

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_protest-dataset-search_20260520T092905_result.json`
- **Structured JSON:** [`7516e81cc871969b8e77.json`](../../sessions/75/7516e81cc871969b8e77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 搜索结果汇总

**关键前提**：ACLED ToS 禁止 ML 用途，因此 ACLED 本身和依赖 ACLED 训练数据的 CASE 2021 Task 2 均排除。

---

### 符合条件的候选

#### 1. PolDem Protest Dataset 30
```
数据集名称: PolDem-Protest Dataset 30 (poldem-protest_30)
类别数 K: action_form = 6 (单标签); issue = 9 (多标签)
类别列表 (action_form): [demonstrations, violent protest, strikes, confrontations, 
  petitions/symbolic actions, other protest]
样本量: 30,852 events (30 European countries, 2000-2015)
License: 未明确标注，页脚 "© EUI & WZB. All rights reserved."
下载方式: 直接下载，无需注册
  CSV: https://poldem.eui.eu/downloads/pea/poldem-protest_30.csv
Gold-standard human labels: 半自动流程 + 35名编码员人工标注
  intercoder: 事件识别 F1=0.60, 议题 κ=0.53
引用论文: Lorenzini et al. (2022) American Behavioral Scientist
备注: 
  ⚠️ 结构化事件数据，不含原始新闻全文（来源为通讯社 newswire，但 CSV 中可能只有编码字段）
  ⚠️ License 模糊，"All rights reserved" 有风险
  ✅ action_form K=6 单标签分类，标注质量中等，适合研究标注噪声
```

#### 2. Mass Mobilization Project (MMD)
```
数据集名称: Mass Mobilization Data Project
类别数 K: protester demand = 7 (多标签); government response = 7 (多标签)
类别列表 (demand): [labor/wages, land, police brutality, political process, 
  prices/taxes, removal of politician, social restrictions]
样本量: ~17,000 events (162 countries, 1990-2020)
License: Harvard Dataverse (CC0 Public Domain)
下载方式: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HTTWYL
Gold-standard human labels: 是，人工编码员从 Lexis-Nexis 新闻编码
引用论文: Clark & Regan (2016), Harvard Dataverse
备注:
  ⚠️ 结构化事件数据，不含原始新闻文本
  ⚠️ Demand/response 为多标签 (0/1 binary columns)，非单标签多分类
  ✅ License 好 (CC0)，完全公开
```

#### 3. SPEED (Social Political Economic Event Database)
```
数据集名称: SPEED
类别数 K: 4 Tier-1 categories
类别列表: [Political Expression Events, Politically Motivated Attacks, 
  Disruptive State Acts, Political Power Reconfigurations]
样本量: 覆盖 3 国 (1979-2008)，具体数量待确认
License: 公开
下载方式: https://databank.illinois.edu/datasets/IDB-7407320
Gold-standard human labels: 是 (Cline Center 编码员)
引用论文: Cline Center for Advanced Social Research, UIUC
备注: ⚠️ 同样是结构化事件数据，非 NLP 文本分类格式
```

---

### 不满足条件的排除项

| 数据集 | 排除原因 |
|--------|---------|
| ACLED / CASE 2021 Task 2 | ToS 禁止 ML 用途（训练数据来自 ACLED） |
| GLOCON Gold | 需邮件申请 |
| CEHA | 样本量仅 500 |
| CCC | 494 多标签 tags，无原始文本 |
| CASE Task 1 | K=2 二分类 |
| MPEDS | 工具/系统，非固定数据集 |

---

### 核心问题

**protest/political event 领域没有理想的公开 NLP 文本分类数据集。** 上述候选全部是结构化编码数据（tabular），不含可直接用于文本分类的原始新闻文本。要做 NLP 实验需要自行匹配/爬取新闻，这引入额外复杂度和版权问题。

---

### 建议

如果坚持 protest 领域确实困难，建议考虑换到有成熟公开 NLP 数据集的任务类型：

| 替代方向 | 数据集 | K | 样本量 | 特点 |
|---------|--------|---|--------|------|
| **危机事件分类** | HumAID | 11 | ~77K tweets | CC-BY-NC, HuggingFace 直接下载，gold labels |
| **情感分类** | GoEmotions | 27/28 | 58K | Reddit 文本，多标签，Google 标注 |
| **意图分类** | CLINC150 / BANKING77 | 150/77 | 23K/13K | 对话意图，完全公开 |
| **新闻主题** | AG News | 4 | 120K | 经典 benchmark |

其中 **HumAID** 最接近 protest 领域（crisis/disaster events），K=11，标注质量好，且项目本身研究标注错误归因，crisis event 分类的标注难度和噪声模式与 protest 类似。

是否要：(1) 用 PolDem action_form 做实验（接受 license 风险 + 无原始文本限制），(2) 转向 HumAID 等 crisis 数据集，还是 (3) 申请 GLOCON？

---
