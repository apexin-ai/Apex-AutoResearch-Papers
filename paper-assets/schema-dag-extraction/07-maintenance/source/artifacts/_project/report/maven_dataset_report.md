# MAVEN 数据集调研报告

## 1. 数据集概况

| 项目 | 内容 |
|------|------|
| 全称 | MAVEN: A MAssive eVENt detection dataset |
| 论文 | Wang et al., EMNLP 2020 (pp. 1652-1671) |
| 作者 | Xiaozhi Wang, Ziqi Wang, Xu Han, Wangyi Jiang, Rong Han, Zhiyuan Liu, Juanzi Li, Peng Li, Yankai Lin, Jie Zhou (清华 + 腾讯) |
| 任务 | Event Detection = Trigger Identification + Trigger Classification |
| 类型数 | 168 event types (+ 8 virtual intermediate nodes) |
| 领域 | 英文 Wikipedia（general domain） |
| Schema 来源 | 从 FrameNet 598 event-related frames 手动归纳合并而来 |
| 层级结构 | **有！** 树状 hierarchical event type schema（见下文） |
| 引用格式 | `@inproceedings{wang2020maven, title={MAVEN: A Massive General Domain Event Detection Dataset}, author={Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie}, booktitle={EMNLP}, year={2020}}` |

### 数据规模

| Split | #Document | #Event | #Mention | #Negative |
|-------|-----------|--------|----------|-----------|
| Train | 2,913 | 73,496 | 77,993 | 323,992 |
| Dev | 710 | 17,726 | 18,904 | 79,699 |
| Test | 857 | 20,389 | 21,835 | 93,570 |
| **Total** | **4,480** | **111,611** | **118,732** | **497,261** |

对比 ACE 2005: 599 docs, 33 types, 4,090 events, 5,349 mentions — MAVEN 大 20 倍。

### 标注格式（JSONL）

```json
{
  "id": "doc_id",
  "title": "Document Title",
  "content": [
    {"sentence": "plain text", "tokens": ["token1", "token2", ...]},
    ...
  ],
  "events": [
    {
      "id": "event_id",
      "type": "Attack",
      "type_id": 45,
      "mention": [
        {"id": "mention_id", "trigger_word": "attacked", "sent_id": 3, "offset": [2, 3]}
      ]
    }
  ],
  "negative_triggers": [
    {"id": "neg_id", "trigger_word": "said", "sent_id": 0, "offset": [5, 6]}
  ]
}
```

Test set 不含 events 字段，改为 `candidates` 列表（labels hidden，提交 CodaLab 评测）。

## 2. 获取方式

| 项目 | 内容 |
|------|------|
| GitHub | https://github.com/THU-KEG/MAVEN-dataset |
| 下载 | Tsinghua Cloud 或 Google Drive（GitHub README 有链接） |
| License | MIT |
| 是否需要申请 | **不需要，完全公开** |
| HuggingFace | **无官方 HF 数据集**。HF 上的 `ErickP/maven` 是第三方 3-class 子集，不可用 |
| 数据大小 | ~50MB（jsonl 压缩） |
| 加载方式 | 下载 jsonl 后自行解析，不能用 `datasets.load_dataset()` 直接加载 |

## 3. Hierarchical Event Type Schema

MAVEN 有树状层级结构，5 个顶层类别 + 8 个虚拟中间节点（不参与分类）+ 168 个叶子类型：

### 顶层分布

| Top-level | 占比 | 子类型示例 |
|-----------|------|----------|
| **Action** | 46.9% | Telling, Attack, Building, Writing, Creating, Using, Wearing... |
| **Change** | 27.5% | Change_event_time, Change_of_leadership, Bodily_harm, Death, Destroying, Becoming... |
| **Scenario** | 13.4% | Emergency, Catastrophe, Incident, Competition, Rite, Lighting... |
| **Sentiment** | 6.4% | Supporting, Convincing, Quarreling, Warning, Suspicion... |
| **Possession** | 5.7% | Commerce_buy, Giving, Renting, Supply, Exchange, Cost... |

### 高 Confusability 子树（关键！）

从 Figure 6 的层级结构中，以下子树内的 sibling types 语义高度相近，是天然的 confusability hotspots：

**Violence 子树（6 types）：**
- Attack, Military_operation, Hostile_encounter, Terrorism, Besieging, Surrounding
- 加上近邻：Bearing_arms, Defending, Killing

**Legality 子树（5 types）：**
- Legal_rulings → Prison, Extradition, Arrest, Releasing
- Criminal_investigation
- Committing_crime → Theft, Robbery, Kidnapping

**Motion 子树（8+ types）：**
- Motion_directional, Body_movement (→ Breathing, Vocalizations, Ingestion, Escaping), Self_motion (→ Patrolling)
- Traveling → Arriving, Departing, Temporary_stay

**Possession 子树（16 types）：**
- Receiving, Getting, Commerce_buy, Commerce_sell, Commerce_pay
- Giving, Sending, Bringing, Supply
- Renting, Exchange, Cost, Expensiveness, Earnings_and_losses, Carry_goods

**Change 子树（20+ types）：**
- Bodily_harm, Damaging, Destroying, Death
- Becoming, Change_event_time, Cause_change_of_strength
- Cure, Recovering

**Communication 子树：**
- Telling, Communication, Reporting, Statement, Expressing_publicly, Reveal_secret, Adducing, Response

### 完整 168 Types 列表

从 Table 15 提取（按 FrameNet 映射）：

```
Know, Warning, Catastrophe, Placing, Causation, Arriving, Sending, Protest,
Preventing_or_letting, Motion, Damaging, Destroying, Death, Perception_active,
Presence, Influence, Receiving, Check, Hostile_encounter, Killing, Conquering,
Releasing, Attack, Earnings_and_losses, Choosing, Traveling, Recovering, Using,
Coming_to_be, Cause_to_be_included, Process_start, Change_event_time, Reporting,
Bodily_harm, Suspicion, Statement, Cause_change_of_position_on_a_scale,
Coming_to_believe, Expressing_publicly, Request, Control, Supporting, Defending,
Building, Military_operation, Self_motion, GetReady, Forming_relationships,
Becoming_a_member, Action, Removing, Surrendering, Agree_or_refuse_to_act,
Participation, Deciding, Education_teaching, Emptying, Getting, Besieging,
Creating, Process_end, Body_movement, Expansion, Telling, Change, Legal_rulings,
Bearing_arms, Giving, Name_conferral, Arranging, Use_firearm, Committing_crime,
Assistance, Surrounding, Quarreling, Expend_resource, Motion_directional,
Bringing, Communication, Containing, Manufacturing, Social_event, Robbery,
Competition, Writing, Rescuing, Judgment_communication, Change_tool, Hold,
Being_in_operation, Recording, Carry_goods, Cost, Departing, GiveUp,
Change_of_leadership, Escaping, Aiming, Hindering, Preserving, Create_artwork,
Openness, Connect, Reveal_secret, Response, Scrutiny, Lighting,
Criminal_investigation, Hiding_objects, Confronting_problem, Renting,
Breathing, Patrolling, Arrest, Convincing, Commerce_sell, Cure, Temporary_stay,
Dispersal, Collaboration, Extradition, Change_sentiment, Commitment,
Commerce_pay, Filling, Becoming, Achieve, Cause_change_of_strength, Supply,
Cause_to_amalgamate, Scouring, Violence, Reforming_a_system, Come_together,
Wearing, Cause_to_make_progress, Legality, Employment, Rite, Publishing,
Adducing, Exchange, Ratification, Sign_agreement, Commerce_buy,
Imposing_obligation, Rewards_and_punishments, Institutionalization, Testing,
Ingestion, Labeling, Kidnapping, Submitting_documents, Prison, Justifying,
Emergency, Terrorism, Vocalizations, Risk, Resolve_problem, Revenge, Limiting,
Research, Having_or_lacking_access, Theft, Incident, Award, Practice
```

## 4. 与 Few-NERD 对比

| 维度 | Few-NERD | MAVEN |
|------|----------|-------|
| Task | NER (Named Entity Recognition) | ED (Event Detection / Trigger Classification) |
| #Types | 66 fine-grained (8 coarse) | 168 (5 top-level + 8 virtual) |
| Domain | Wikipedia | Wikipedia |
| Annotation | Entity spans + types | Event triggers + types + mentions |
| Train size | ~131k sentences | 2,913 docs / 77,993 mentions |
| Test size | 37,648 sentences (我们用 1,000) | 857 docs / 21,835 mentions |
| Hierarchy | 2-level (coarse→fine) | Tree-structure (~3-4 levels) |
| Public | Yes (HF) | Yes (GitHub, MIT) |
| Evaluation | Entity-level P/R/F1 | Trigger-level micro P/R/F1 |

**关键差异：任务类型不同。** Few-NERD 是 NER（标注 entity spans），MAVEN 是 ED（标注 event trigger words）。但两者都需要 type classification，confusability 影响的核心机制相同。

## 5. BCS/SDGD 验证适用性分析

### 5.1 Confusability 丰富度

**极其适合。** 论文原文 Table 7 的错误分析直接验证了 confusability：

| 错误类型 | DMCNN | BiLSTM | MOGANED | DMBERT |
|---------|-------|--------|---------|--------|
| Parent-Children 混淆 | 15.5% | 14.5% | 15.5% | 13.1% |
| **Between Siblings 混淆** | **19.8%** | **14.6%** | **17.8%** | **19.0%** |
| Into Top 50% types | 89.2% | 90.3% | 86.8% | 87.0% |

**Sibling 混淆率 14.6-19.8%** — 这正是我们的 confusability hypothesis 的直接证据。模型在层级结构中的 sibling types 之间频繁犯错。

### 5.2 高 Confusability Pairs（预测）

基于层级结构，以下 pairs 预期 cosine similarity 极高：

| Type A | Type B | 共同 Parent | 预期 Confusability |
|--------|--------|-----------|-------------------|
| Attack | Military_operation | Violence | 极高 |
| Attack | Hostile_encounter | Violence | 极高 |
| Terrorism | Violence | - | 极高 |
| Theft | Robbery | Committing_crime | 极高 |
| Arrest | Prison | Legality | 高 |
| Arriving | Departing | Traveling | 高 |
| Commerce_buy | Commerce_sell | Possession | 高 |
| Telling | Communication | Action/Communication | 高 |
| Bodily_harm | Killing | Violence/Change | 高 |
| Damaging | Destroying | Change | 高 |
| Statement | Expressing_publicly | Communication | 高 |
| Giving | Sending | Possession | 高 |

### 5.3 SDGD 效果预估

- 168 types → 对比 Few-NERD 66 types，confusability graph 边数增长 ~6.5x（168×167/2 = 14,028 pairs vs 66×65/2 = 2,145 pairs）
- Graph coloring chromatic number 预估 15-25 batches（vs Few-NERD 8-10）
- **SDGD 分 batch 的收益空间更大**：单次 prompt 塞 168 types 几乎不可能（prompt 长度 + confusion），SDGD 的 per-batch extraction 必要性更强
- 层级结构可直接用作 confusability 分析的先验（siblings 应有高 BCS）

### 5.4 论文验证价值

1. **Cross-task generalization**: Few-NERD (NER) + MAVEN (ED) 证明 confusability 现象跨 IE 子任务通用
2. **Scale stress test**: 168 types 比 66 types 更极端，如果 SDGD 在 168 types 上也有效，说服力极强
3. **Hierarchy validation**: MAVEN 的树状 schema 可验证 "同 parent 下 sibling types 有更高 BCS" 假设
4. **独立验证 Table 7 的 sibling confusion 发现**: 我们的 BCS 指标是否能预测 MAVEN 原论文中观察到的 sibling 混淆模式？

## 6. 与 ACE05 对比优劣

| 维度 | ACE05 | MAVEN | 判断 |
|------|-------|-------|------|
| **获取** | LDC 许可 $300 + 审批耗时 | GitHub 直接下载，MIT | MAVEN 胜 |
| **类型数** | 7 entity + 18 relation (+ 33 event) | 168 event | MAVEN 胜（confusability 空间大） |
| **任务** | NER + RE + ED 联合 | ED only | ACE05 胜（多任务 DAG） |
| **与 Few-NERD 互补** | NER+RE（不同任务维度） | ED（不同任务但都是 classification） | ACE05 略胜 |
| **学术认可度** | 经典 benchmark，20 年历史 | 2020 EMNLP，已被广泛引用 | 平手 |
| **Confusability 分析** | 7 entity types 太少，confusability 有限 | 168 types + hierarchy = 理想 testbed | MAVEN 胜 |
| **层级结构** | 无显式层级 | 有树状层级 | MAVEN 胜 |
| **数据量** | 599 docs, 5,349 mentions | 4,480 docs, 118,732 mentions | MAVEN 胜 |
| **Reviewer 认可** | 经典但需付费获取 | Reviewer 主动推荐 | MAVEN 胜 |

### 结论

**推荐用 MAVEN 替代 ACE05，理由：**

1. **免费公开** — 消除 LDC $300 + 审批延迟的风险（距 ARR 提交仅 10 天）
2. **168 types 是 confusability 的完美 stress test** — 比 ACE05 的 7 entity types 有说服力得多
3. **层级结构** — 天然产生 sibling confusability，直接对应我们的 BCS 分析
4. **原论文已有 type confusion 数据** — Table 7 的 sibling confusion 率直接支持我们的 hypothesis
5. **Reviewer 推荐** — 采纳 reviewer 建议本身就是加分项
6. **跨任务泛化** — Few-NERD (NER) + MAVEN (ED) 比 Few-NERD + ACE05 (也有 NER) 的任务多样性更好

**唯一风险：任务类型差异。** MAVEN 是 event detection 不是 NER/RE。需要在论文中明确框架：我们验证的是 "type confusability 影响 LLM-based IE" 这一通用现象，不限于某个特定 IE 子任务。NER 和 ED 都需要 type classification，confusability 的影响机制相同。

## 7. 实施方案（如果用 MAVEN）

### 7.1 预处理

```python
# 1. 下载数据
# 从 GitHub releases 下载 train.jsonl, valid.jsonl, test.jsonl

# 2. 转换为我们的格式
# MAVEN 的 event detection 不同于 NER，需要适配：
# - NER: 输入 text → 输出 [{"text": "entity_text", "type": "entity_type"}, ...]
# - ED:  输入 text → 输出 [{"trigger": "trigger_word", "type": "event_type"}, ...]

# 3. 从 valid.jsonl 采样（test set 无标签）
# 采样策略：随机选 200-500 docs（有 17,726 events），确保覆盖大部分 types
```

关键：**用 dev set 而非 test set**，因为 test set 标签不公开（CodaLab 评测）。Dev set 有 710 docs / 18,904 mentions，足够。

### 7.2 Type Embedding 计算

```python
# 168 types 的 Qwen3-32B mean-pool embeddings
# 与 Few-NERD 流程相同：
# 1. 构建 type description（type name + FrameNet frame definition）
# 2. 输入 Qwen3-32B，取最后一层 hidden states 的 mean-pool
# 3. 计算 168×168 pairwise cosine similarity matrix
# 4. 保存为 type_embeddings_maven.pt

# Type definition 来源：
# - Table 15 的 FrameNet frame mapping（每个 type 有对应的 frame name）
# - 可从 FrameNet 获取 frame definition 作为 type description
```

### 7.3 Prompt 适配

```python
# Event Detection prompt 模板（vs NER prompt）：
MAVEN_PROMPT = """Given the following text, identify all event triggers and classify their event types.
An event trigger is the key word or phrase that most clearly expresses an event occurrence.

Available event types for this batch: {batch_types}

Text: {text}

Output format: [{"trigger": "word", "type": "EventType"}, ...]"""
```

### 7.4 GPU 预算估算

| 步骤 | Few-NERD (66 types) | MAVEN (168 types) | 倍数 |
|------|--------------------|--------------------|------|
| Type embedding | ~10 min | ~25 min | 2.5x |
| Graph coloring | 秒级 | 秒级 | 1x |
| SDGD extraction (per doc) | ~8-10 batches × 1 call | ~15-25 batches × 1 call | 2-3x |
| Total extraction (500 docs) | ~4h | ~8-12h | 2-3x |
| Single-pass baseline (500 docs) | ~2h | ~3h | 1.5x |

**预估总 GPU 时间：~15-20h**（含 baseline + SDGD + 对比实验）。在 1× RTX PRO 6000 Blackwell 上可接受。

### 7.5 实验矩阵

```
Exp-M1: MAVEN count baseline（类似 exp-001）
  - type count = [10, 20, 40, 80, 168]
  - 观测 F1 下降趋势
  
Exp-M2: MAVEN confusability controlled（类似 exp-002）
  - 固定 count=20/40，变化 BCS
  - 观测 within-count BCS 与 F1 相关性

Exp-M3: MAVEN SDGD-zero
  - Graph coloring on 168 types
  - 对比 single-pass vs SDGD
```

## 8. 风险与缓解

| 风险 | 影响 | 缓解 |
|------|------|------|
| 任务不同（ED vs NER） | Reviewer 可能质疑可比性 | 论文框架强调 "type classification 通用现象"，非特定任务 |
| Test set 无标签 | 只能用 dev set | Dev set 18,904 mentions 足够；或提交 CodaLab 获取 test 分数 |
| 168 types prompt 过长 | Single-pass baseline 可能 OOM 或 prompt truncation | 正好说明 SDGD 的必要性 |
| Event trigger 与 entity span 评测逻辑不同 | 需要新的评测代码 | Trigger 是 word-level，比 entity span 更简单 |
| 下载需翻墙 | AutoDL 可能无法直接下载 | 本地下载后 scp 到服务器，或用 GitHub mirror |
