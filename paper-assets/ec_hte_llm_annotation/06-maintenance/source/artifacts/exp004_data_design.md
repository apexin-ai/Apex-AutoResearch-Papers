# exp-004: UC Berkeley Hate Speech — Causal Framework Design Document

**Date**: 2026-05-21
**Dataset**: `ucberkeley-dlab/measuring-hate-speech` (HuggingFace)
**Status**: Awaiting Director approval

---

## 1. 数据概览

| 指标 | 值 |
|------|-----|
| 总标注行数 | 135,556 |
| 唯一评论数 | 39,565 |
| 唯一标注者 | 7,912 |
| 平均每条评论标注数 | 3.4（中位数 2） |
| 平均每位标注者标注数 | 17.1 |
| 平台数 | 4（编码 0–3） |
| 文本长度 | 均值 ~140 字符，最长 603 |

### 关键列分类

| 类别 | 列 | 说明 |
|------|-----|------|
| 标识 | `comment_id`, `annotator_id`, `platform` | 评论/标注者/平台标识 |
| 连续评分 | `hate_speech_score` | Rasch 模型聚合分，**每条评论固定**，不随标注者变化 |
| 序数标签（per-annotation） | `sentiment`, `respect`, `insult`, `humiliate`, `status`, `dehumanize`, `violence`, `genocide`, `attack_defend` | 0–4 标度，每位标注者独立评分 |
| 二值分类标签 | `hatespeech` | 0=非仇恨 (59.5%), 1=模糊/反讽 (6.6%), 2=仇恨 (33.9%) |
| 目标群体（布尔） | `target_race_*`, `target_religion_*`, `target_gender_*`, `target_sexuality_*`, `target_origin_*`, `target_age_*`, `target_disability_*`, `target_politics_*` | 多标签，每个标注行独立标记 |
| 标注者人口统计 | `annotator_gender`, `annotator_race_*`, `annotator_ideology`, `annotator_educ`, `annotator_income`, `annotator_age`, `annotator_religion_*`, `annotator_sexuality_*`, `annotator_trans` | 布尔/类别/数值 |
| IRT 模型参数 | `infitms`, `outfitms`, `annotator_severity`, `std_err`, `hypothesis` | Rasch 模型拟合统计量 |

### 标注不一致性

- 有多位标注者的评论：29,488 条
- 其中标注不一致（`hatespeech` 标签不同）：11,929 条 (**40.5%**)
- 约 50 条"金标准"评论有 243–815 个标注，可用于高精度标注者行为分析

---

## 2. 因果框架映射

### 方案 A（推荐主方案）：种族靶向仇恨言论 × 标注者种族

| 组件 | 变量 | 操作化定义 | 理由 |
|------|------|-----------|------|
| **T** (treatment) | `target_race_black` | 二值：评论是否靶向黑人群体 | 最大的目标种族子类（22,899 标注），在文本生成前即确定，满足时序因果条件 |
| **Y** (outcome) | `hatespeech` 序数标签 | 每标注行，3 级 (0/1/2) | 随标注者变化的 per-annotation 变量，可捕捉异质性。**不用** `hate_speech_score`（per-comment 常量，无法反映标注者差异） |
| **Z** (effect modifier) | 去人化程度（dehumanization） | **由 LLM 基于文本标注** → 二值 (high/low) | 与人工 `dehumanize` 列对比可量化 LLM 误分类；且 Z×S 交互已被观测到（见下） |
| **S** (subgroups) | 标注者种族 | White / Black / Other（从 `annotator_race_*` one-hot 推导） | 定义异质性结构的核心维度 |
| **协变量** | `platform`, 文本长度, 其他 target 标志 | 控制混淆 | Platform 与 target_race_black 有关联（平台 1 占 47.6%） |

#### 单元格大小（T × Z × S）

| T | Z (dehum_high) | Black | Other | White |
|---|----------------|-------|-------|-------|
| 0 | 0 | 4,639 | 6,223 | 41,202 |
| 0 | 1 | 5,112 | 7,701 | 47,780 |
| 1 | 0 | 743 | 908 | 6,574 |
| 1 | 1 | 1,191 | 1,870 | 11,613 |

**最小单元格 = 743，充足。**

#### 已观测的 CATE 估计（E[Y|T=1,Z,S] - E[Y|T=0,Z,S]）

| Z | Black | Other | White |
|---|-------|-------|-------|
| dehum_low (Z=0) | +0.452 | +0.635 | +0.686 |
| dehum_high (Z=1) | +0.687 | +0.661 | +0.590 |

**关键发现**：Black 标注者的 CATE 在 Z=low 时最小（0.452），在 Z=high 时最大（0.687）；White 标注者方向相反。这种 **Z×S 交互** 正是 EC-HTE 框架的核心应用场景。

---

### 方案 B（备选验证方案）：穆斯林靶向 × 意识形态子群

| 组件 | 变量 | 操作化定义 | 理由 |
|------|------|-----------|------|
| **T** | `target_religion_muslim` | 二值：评论是否靶向穆斯林 | 第二大目标宗教类别（12,509 标注） |
| **Y** | `hatespeech` 序数标签 | 同方案 A | — |
| **Z** | 暴力程度（violence） | **由 LLM 基于文本标注** → 二值 (≥1 vs 0) | 暴力内容的感知同样受意识形态影响 |
| **S** | 标注者意识形态 | Liberal (含 slightly/extremely) vs Conservative | 54% vs 26% 的标注量，足够对比 |

#### 单元格大小

| T | Z (violence_any) | Conservative | Liberal |
|---|-------------------|-------------|---------|
| 0 | 0 | 16,683 | 34,031 |
| 0 | 1 | 15,481 | 32,021 |
| 1 | 0 | 1,391 | 2,998 |
| 1 | 1 | 1,718 | 4,039 |

**最小单元格 = 1,391，充足。** 此方案使用完全不同的 T（宗教而非种族）和 S（意识形态而非种族），可作为方案 A 的独立验证。

---

### 不推荐：性别靶向方案

`target_gender_women` 作为 T 时，均值差异极小（-0.564 vs -0.585），T×S 交互 < 0.01，无法有效展示 EC-HTE 优势。

---

## 3. LLM 标注任务设计

### 3.1 方案 A 的 Z 变量：去人化程度（Dehumanization）

**任务**：对每条评论文本，判断其去人化程度。

**Prompt 草案**：

```
You are an expert annotator for hate speech research. Given the following social media comment, assess the level of dehumanization present in the text.

Dehumanization means language that portrays a person or group as less than human — comparing them to animals, vermin, diseases, or objects; denying their intelligence or moral worth; or treating them as subhuman.

Comment: "{text}"

Rate the dehumanization level:
0 = No dehumanization — the comment does not portray anyone as less than human
1 = Mild dehumanization — subtle implication of inferiority but no explicit dehumanizing language
2 = Moderate dehumanization — clear dehumanizing framing or metaphor
3 = Severe dehumanization — explicit comparison to animals/vermin/disease or denial of humanity
4 = Extreme dehumanization — calls for elimination or treatment as non-persons

Respond with ONLY a single digit (0-4).
```

**二值化**：LLM 输出 ≥ 2 → Z=1 (high), < 2 → Z=0 (low)

**预期误分类模式**：LLM 训练数据以多数群体（White）视角为主，对以下情况倾向于低估去人化程度：
- 使用 AAVE（非裔美国人方言）的隐性贬低
- 针对黑人群体的隐晦比喻（如 "thugs", "animals"）
- 文化语境相关的去人化表达

这种系统性偏差意味着 LLM 的 Z 误分类率在 Black 标注者子群中更高 → **子群特异性误分类**。

### 3.2 方案 B 的 Z 变量：暴力程度（Violence）

**Prompt 草案**：

```
You are an expert annotator for hate speech research. Given the following social media comment, assess whether it contains violent language or incitement to violence.

Violence includes: threats of physical harm, endorsement of violence against a group, calls for deportation/detention by force, celebration of violence against a group, or language that normalizes violence.

Comment: "{text}"

Rate the violence level:
0 = No violent content
1 = Mild — vaguely threatening tone or implicit endorsement of harm
2 = Moderate — explicit mention of violence or clear threat
3 = Severe — direct call for violence or graphic violent imagery
4 = Extreme — call for genocide, mass violence, or elimination

Respond with ONLY a single digit (0-4).
```

**二值化**：≥ 1 → Z=1 (violence present), 0 → Z=0

### 3.3 标注执行计划

| 参数 | 值 |
|------|-----|
| 待标注评论数 | 39,565（唯一评论） |
| LLM 模型 | Claude Sonnet 4（平衡成本与质量） |
| 每条评论标注变量 | 方案 A: dehumanization; 方案 B: violence |
| 预计 token 成本 | ~200 input + ~5 output per comment ≈ 8M tokens total |
| 重复标注（reliability） | 随机 5% 评论标注 3 次，计算 LLM 自一致性 |
| 与人工标注对比 | 50 条金标准评论（243–815 人工标注），作为 LLM 校准基准 |

---

## 4. 预期子群结构

### 方案 A: 标注者种族子群

| 子群 | 标注行数 | 占比 | 唯一标注者（估计） |
|------|---------|------|-------------------|
| White | 109,090 | 80.5% | ~6,370 |
| Black | 13,606 | 10.0% | ~790 |
| Other (Asian + Latinx + 其他) | 12,860 | 9.5% | ~750 |

**潜在问题**：White 子群占绝对多数。EC-HTE 的优势主要体现在 Black 子群的校正上。

### 方案 B: 意识形态子群

| 子群 | 标注行数 | 占比 |
|------|---------|------|
| Liberal (slightly + liberal + extremely) | 73,089 | 53.9% |
| Conservative (slightly + conservative + extremely) | 35,273 | 26.0% |
| Neutral / No opinion | 27,167 | 20.0% |

**更平衡**，3 组均有足够样本。

### 细粒度子群（方案 A 可拓展）

| S 维度 | 分组 | 说明 |
|--------|------|------|
| 种族 × 意识形态 | 6 组 (3 race × 2 ideology) | 可检验种族效应是否被意识形态混淆 |
| 种族 × 年龄 | 6 组 (3 race × 2 age bins) | 年龄可能影响对去人化的感知 |
| 种族 × 性别 | 6 组 (3 race × 2 gender) | 交叉性分析 |

**注意**：细粒度分组后最小单元格可能降至 < 100，需谨慎使用。

---

## 5. 与 EC-HTE 的对接：Misclassification Heterogeneity

### 核心论点

EC-HTE 框架的价值在于：当 LLM 标注的效应修饰变量 Z 存在 **子群特异性误分类** 时，全局校正（global correction）会产生偏差，而 EC-HTE 通过子群特异的校正函数保留真实异质性。

本数据集完美匹配这一论点：

1. **LLM 作为 Z 标注者**：LLM 基于文本判断去人化程度，无法观测标注者人口统计。
2. **子群特异性误分类来源**：
   - Black 标注者在黑人靶向评论上感知到更高去人化（26.9% 评 level 4 vs White 的 21.9%）
   - LLM 训练数据以多数群体视角为主 → LLM 的去人化评估更接近 White 标注者的感知
   - 因此 LLM 对 Black 标注者子群的 Z 误分类率系统性偏高
3. **全局校正的失败模式**：
   - 全局误分类矩阵 M 以 White 标注者为主导（80% 数据）
   - 用 M 校正 Black 子群的 CATE → 在错误方向上过度校正
   - 结果：抹平真实的异质性，使所有子群的 CATE 趋向 White 子群
4. **EC-HTE 的优势**：
   - 分别估计 M_white, M_black, M_other
   - 对 Black 子群应用 M_black → 正确补偿 LLM 对其去人化感知的低估
   - 保留甚至增强跨群体差异的真实结构

### 可验证的预测

| 预测 | 检验方法 |
|------|---------|
| LLM 的去人化标注与 White 标注者相关性 > Black 标注者 | 计算 LLM Z 与各子群人工 Z 的 Cohen's κ |
| 全局校正后的 CATE 分布比 EC-HTE 更"平坦" | 比较两种方法的 CATE 标准差 |
| EC-HTE 校正后 Black 子群的 CATE 向更极端方向移动 | 比较校正前后的 CATE 变化方向 |
| 金标准评论（高标注数）可验证上述差异具有统计显著性 | 50 条高标注评论提供稳健基准 |

---

## 6. 潜在风险

### 6.1 数据量

- **总体充足**：135K 标注、39K 评论、7.9K 标注者
- **最小单元格风险**：T=1, Z=0, S=Black 仅 743 行。对 CATE 点估计足够，但置信区间可能较宽
- **缓解措施**：使用贝叶斯分层模型或 bootstrap，利用 Other 子群作为辅助信息

### 6.2 子群不平衡

- White 标注者占 80.5%，Black 仅 10.0%
- 全局估计被 White 主导是 **feature not bug** — 这正是 EC-HTE 要解决的问题
- 但 Black 子群的 CATE 估计精度较低，需报告置信区间

### 6.3 Z 标注歧义

- 去人化是主观概念，LLM prompt 需精确定义
- **风险**：LLM 输出高度集中在 1-2 个值（如全部输出 0 或 2），缺乏区分度
- **缓解**：先在 100 条样本上测试 prompt，确认分布合理后再全量运行
- **备选**：如 dehumanization 区分度不足，可改用 `insult` 或 `sentiment` 作为 Z

### 6.4 混淆因素

- `platform` 与 `target_race_black` 相关（平台 1 占比过高）
- 多标签目标群体（如同时 target_race + target_religion）
- **缓解**：将 platform、text length、多标签标志纳入协变量

### 6.5 伦理与敏感性

- 数据涉及仇恨言论，包含冒犯性内容
- LLM 标注可能触发 safety filter（拒绝回答）
- **缓解**：使用 research-context system prompt，监控拒绝率

### 6.6 `hate_speech_score` 不可作 Y 的陷阱

- 该列是 per-comment Rasch 聚合分，同一评论的所有标注行值相同
- 如误用为 Y，会 **虚假膨胀样本量**（同一评论的多行不是独立观测）
- **必须使用 per-annotation 序数标签** (如 `hatespeech`) 作为 Y

---

## 7. 推荐方案与 Tradeoff

### 推荐方案 1（主方案）：Scheme A — 种族靶向 × 去人化 × 标注者种族

**优势**：
- Z×S 交互已被经验观测到（CATE 方向翻转）
- 有明确的 LLM 误分类异质性故事（多数群体视角偏差）
- 与仇恨言论文献高度一致（种族群体感知差异是已知现象）
- 单元格大小充足（最小 743）
- 50 条金标准高标注评论可作为校准/验证基准

**劣势**：
- White 标注者占 80.5%，子群极度不平衡
- T=1 (target_race_black) 仅占 16.9%，treatment group 偏小
- Platform 混淆需要控制

### 推荐方案 2（独立验证方案）：Scheme C — 穆斯林靶向 × 暴力 × 意识形态

**优势**：
- 与方案 A 使用完全不同的 T/Z/S 维度，提供独立证据
- 意识形态子群更平衡（54% vs 26%）
- 暴力标注比去人化更客观，LLM 可能有更好的基线表现 → 更能展示 EC-HTE 在"LLM 整体较准但子群偏差仍存在"场景下的价值

**劣势**：
- T×S 交互效应较弱（保守派 vs 自由派对穆斯林靶向的评分差异不大）
- 暴力的意识形态差异不如去人化的种族差异有理论基础

### 执行建议

1. **先运行方案 A**，作为核心结果
2. **方案 B 作为 robustness check**，在附录中呈现
3. 两个方案共享同一批 LLM 标注（dehumanization + violence 可以在同一次 API 调用中获取）
4. 如方案 A 的 Z×S 交互在 EC-HTE 校正后更显著 → 核心论证成功
5. 如方案 B 也显示类似模式 → 增强论证的外部有效性

---

## 附录：数据下载与预处理代码

```python
from datasets import load_dataset

ds = load_dataset("ucberkeley-dlab/measuring-hate-speech")["train"]

# 构建分析数据框
import pandas as pd
df = ds.to_pandas()

# 标注者种族子群
df["annotator_race_group"] = "Other"
df.loc[df["annotator_race_white"], "annotator_race_group"] = "White"
df.loc[df["annotator_race_black"], "annotator_race_group"] = "Black"

# 标注者意识形态子群
liberal_set = {"slightly_liberal", "liberal", "extremely_liberal"}
conservative_set = {"slightly_conservative", "conservative", "extremely_conservative"}
df["annotator_ideology_group"] = "Neutral"
df.loc[df["annotator_ideology"].isin(liberal_set), "annotator_ideology_group"] = "Liberal"
df.loc[df["annotator_ideology"].isin(conservative_set), "annotator_ideology_group"] = "Conservative"

# Z 二值化（人工标注基准）
df["dehumanize_high"] = (df["dehumanize"] >= 2).astype(int)
df["violence_any"] = (df["violence"] >= 1).astype(int)
```
