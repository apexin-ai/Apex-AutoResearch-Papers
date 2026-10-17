# ACE05 数据集调研报告

> 目的：为 exp-004（ACE05 confusability study）准备数据，验证 Few-NERD 上发现的 BCS-quality 相关性能否跨域复现。

---

## 1. 数据集概况

**ACE 2005 (Automatic Content Extraction)**
- **发布者**: Linguistic Data Consortium (LDC), LDC2006T06
- **语言**: 英语、中文、阿拉伯语（我们只用英语部分）
- **领域**: 新闻（newswire, broadcast news, broadcast conversation, weblog, discussion forum, conversational telephone speech）
- **规模**: 英语部分约 599 篇文档，~30K 句子
- **标注内容**: 实体 (Entity)、关系 (Relation)、事件 (Event)、值 (Value)、时间表达式 (Time Expression)
- **LDC 目录**: https://catalog.ldc.upenn.edu/LDC2006T06

---

## 2. 实体类型（7 types）

| Type | 缩写 | 说明 | Subtypes |
|------|------|------|----------|
| Person | PER | 人物 | Individual, Group, Indefinite |
| Organization | ORG | 组织 | Commercial, Educational, Entertainment, Government, Media, Medical-Science, Non-Governmental, Religious, Sports |
| GPE | GPE | 地缘政治实体 | Continent, County-or-District, GPE-Cluster, Nation, Population-Center, Special, State-or-Province |
| Location | LOC | 地理位置 | Address, Boundary, Celestial, Land-Region-Natural, Region-General, Region-International, Water-Body |
| Facility | FAC | 设施 | Airport, Building-Grounds, Path, Plant, Subarea-Facility |
| Vehicle | VEH | 交通工具 | Air, Land, Subarea-Vehicle, Underspecified, Water |
| Weapon | WEA | 武器 | Biological, Blunt, Chemical, Exploding, Nuclear, Projectile, Sharp, Shooting, Underspecified |

**用于 BCS 计算的 7 个 entity type 名称**:
```
Person, Organization, Geo-Political Entity, Location, Facility, Vehicle, Weapon
```

---

## 3. 关系类型（6 major types, 18 subtypes）

| Type | Subtypes | 说明 |
|------|----------|------|
| **ART** (Artifact) | User-Owner-Inventor-Manufacturer | 人/组织与工件的关系 |
| **GEN-AFF** (Gen-Affiliation) | Citizen-Resident-Religion-Ethnicity, Org-Location | 一般归属关系 |
| **ORG-AFF** (Org-Affiliation) | Employment, Founder, Ownership, Student-Alum, Sports-Affiliation, Investor-Shareholder, Membership | 组织从属关系 |
| **PART-WHOLE** | Geographical, Subsidiary, Artifact | 部分-整体关系 |
| **PER-SOC** (Person-Social) | Business, Family, Lasting-Personal | 人际关系 |
| **PHYS** (Physical) | Located, Near | 物理位置关系 |

**用于 BCS 计算的 18 个 relation subtype 名称**:
```
User-Owner-Inventor-Manufacturer
Citizen-Resident-Religion-Ethnicity
Org-Location
Employment
Founder
Ownership
Student-Alum
Sports-Affiliation
Investor-Shareholder
Membership
Geographical
Subsidiary
Artifact
Business
Family
Lasting-Personal
Located
Near
```

---

## 4. 数据格式与标注方式

### 原始格式
- **文件格式**: SGM (SGML) 标注文件 + APF (XML) 标注文件
- **标注方式**: Standoff annotation — 标注信息在 APF 文件中，通过 char offset 指向 SGM 源文件
- **实体标注**: 每个 entity mention 有 head span 和 extent span，带类型和子类型
- **关系标注**: 每个 relation mention 连接两个 entity mention，标注 type/subtype 和方向（Arg-1, Arg-2）

### 常用预处理后格式
大多数论文使用 JSON 格式，每个 sentence 一条记录：
```json
{
  "tokens": ["The", "president", "of", "the", "company", "..."],
  "entities": [
    {"start": 1, "end": 2, "type": "PER"},
    {"start": 4, "end": 5, "type": "ORG"}
  ],
  "relations": [
    {"head": 0, "tail": 1, "type": "ORG-AFF:Employment"}
  ]
}
```

### 常用 Splits
标准 split（Li & Ji 2014, 广泛沿用）:
- **Train**: 351 docs
- **Dev**: 80 docs
- **Test**: 80 docs
- 总计 511 docs（英语部分），约 14K-16K 训练句，~2K dev 句，~1.6K test 句

---

## 5. 公开下载渠道

### 官方渠道
- **LDC**: https://catalog.ldc.upenn.edu/LDC2006T06
- **许可证**: LDC User Agreement — 需付费（LDC 会员单位免费），**可用于研究发表**，但不得直接重新分发原始数据
- **价格**: 非会员 $300

### HuggingFace Hub
- **无官方预处理版本**在 HuggingFace Hub 上公开（受 LDC 许可证限制）
- 部分研究者上传了私有处理版本，但不可公开获取

### GitHub 预处理工具（需要已有 LDC 原始数据）
| 仓库 | 用途 | 输出格式 |
|------|------|----------|
| [nlpcl-lab/ace2005-preprocessing](https://github.com/nlpcl-lab/ace2005-preprocessing) | Event Extraction | JSON |
| [wasiahmad/ACE05-Processor](https://github.com/wasiahmad/ACE05-Processor) | NER + RE + Event | JSON (UDPipe) |
| [mgormley/ace-data-prep](https://github.com/mgormley/ace-data-prep) | RE | JSON |
| [princeton-nlp/PURE](https://github.com/princeton-nlp/PURE) | Entity + RE | JSON (sentence-level) |
| [dwadden/dygiepp](https://github.com/dwadden/dygiepp) | NER + RE + Event | JSONL (DyGIE++ format) |
| OneIE preprocessing | Joint IE | JSON (OneIE format) |

---

## 6. 许可证信息

- **许可类型**: LDC User Agreement for Non-Members / LDC Membership
- **研究发表**: ✅ 允许。大量 ACL/EMNLP/NAACL 论文使用 ACE05 发表，属于 NLP 社区标准基准
- **数据重分发**: ❌ 不允许直接分发原始数据。但可以分发**预处理脚本**（配合用户自有 LDC 数据使用）
- **发表时注意**: 需在论文中引用 LDC catalog number (LDC2006T06)

---

## 7. 与 Few-NERD 的关键差异

| 维度 | ACE05 | Few-NERD |
|------|-------|----------|
| **Entity types** | 7 coarse types | 8 coarse / 66 fine-grained types |
| **Relation types** | 6 types, 18 subtypes | ❌ 无关系标注 |
| **领域** | 新闻（多源：newswire, broadcast, weblog, forum） | Wikipedia（通用百科） |
| **标注粒度** | Entity + Relation + Event（联合标注） | 仅 Entity（NER only） |
| **数据规模** | ~599 docs, ~30K 句子 | 188,200 句子, 491,711 entities |
| **数据获取** | 需 LDC 许可（付费） | 完全公开 |
| **类型层级** | flat 7 types（有 subtypes 但 NER 通常只用 coarse） | 2-level hierarchy (8 coarse → 66 fine) |
| **BCS 研究意义** | 7 types 低混淆度 baseline；18 relation subtypes 提供跨任务验证 | 66 types 高混淆度，已完成 BCS 相关性验证 |

**核心价值**：ACE05 提供了 (1) 不同领域（新闻 vs 百科）；(2) 不同任务（RE vs NER）；(3) 不同类型数量级（7/18 vs 66）的验证场景。如果 BCS-quality 相关性在 ACE05 RE 任务上依然成立，说明该发现具有跨域、跨任务的普遍性。

---

## 8. 预处理方案

### 8.1 总体策略

我们需要将 ACE05 转换为与 Few-NERD 类似的 pipeline 格式。考虑到：
- 现有 pipeline 使用 parquet 格式（`/root/schema-dag-extraction/data/parquet/test.parquet`）
- 评估使用 (text, type) pair 匹配（`text_match_reeval.py`）
- BCS 基于 type 名称的 Qwen3 embedding

### 8.2 NER 和 RE 分开处理

**推荐分开处理**，产生两套数据：

#### NER 数据 (`ace05_ner/`)
```python
# Schema 与 Few-NERD 对齐
{
    "text": "句子原文",
    "entities": [
        {"text": "entity mention text", "type": "PER"},  # 7 coarse types
        ...
    ]
}
```
- 使用 7 个 coarse entity types
- 直接复用 Few-NERD pipeline（改 type 列表即可）
- 作为低混淆度 baseline（7 types vs 66 types）

#### RE 数据 (`ace05_re/`)
```python
# 新增 relation 信息
{
    "text": "句子原文",
    "entities": [...],  # 同上
    "relations": [
        {
            "head": {"text": "head entity", "type": "PER"},
            "tail": {"text": "tail entity", "type": "ORG"},
            "type": "ORG-AFF:Employment"  # 18 subtypes
        },
        ...
    ]
}
```
- 使用 18 个 relation subtypes
- 需要新的 evaluation 逻辑（relation triple 匹配）
- 这是 exp-004 的核心验证目标

### 8.3 需要的预处理脚本

1. **`scripts/preprocess_ace05.py`** — 从 LDC 原始 SGM/APF 文件提取实体和关系
   - 输入：LDC2006T06 原始目录
   - 输出：JSON → Parquet（NER + RE）
   - 参考 [wasiahmad/ACE05-Processor](https://github.com/wasiahmad/ACE05-Processor) 的解析逻辑

2. **`scripts/compute_ace05_type_embeddings.py`** — 计算 type embeddings
   - 使用 Qwen3 mean-pooled embedding
   - NER: 7 entity types → `ace05_entity_type_embeddings.pt`
   - RE: 18 relation subtypes → `ace05_relation_type_embeddings.pt`

3. **`scripts/ace05_bcs_analysis.py`** — 计算 BCS 并设计实验 batches
   - 复用 Few-NERD BCS pipeline 逻辑
   - 按 BCS 分组设计 low/medium/high confusability batches

---

## 9. Embedding 方案

### 9.1 Entity Type Names（7 个，用于 NER BCS）
```python
entity_types = [
    "Person",
    "Organization",
    "Geo-Political Entity",
    "Location",
    "Facility",
    "Vehicle",
    "Weapon"
]
```

### 9.2 Relation Subtype Names（18 个，用于 RE BCS）
```python
relation_subtypes = [
    # ART
    "User-Owner-Inventor-Manufacturer",
    # GEN-AFF
    "Citizen-Resident-Religion-Ethnicity",
    "Org-Location",
    # ORG-AFF
    "Employment",
    "Founder",
    "Ownership",
    "Student-Alum",
    "Sports-Affiliation",
    "Investor-Shareholder",
    "Membership",
    # PART-WHOLE
    "Geographical",
    "Subsidiary",
    "Artifact",
    # PER-SOC
    "Business",
    "Family",
    "Lasting-Personal",
    # PHYS
    "Located",
    "Near"
]
```

### 9.3 Embedding 计算方式
- 与 Few-NERD 一致：使用 Qwen3 mean-pooled hidden states（5120-dim）
- 对每个 type name（可加 brief description 提升语义区分度）计算 embedding
- 计算 pairwise cosine similarity → BCS matrix

### 9.4 预期 BCS 特征
- **Entity types (7)**：类型少、语义差距大，预期 BCS 整体较低（低混淆度）
- **Relation subtypes (18)**：
  - 高混淆对预测：`Employment ↔ Membership`、`Founder ↔ Ownership`、`Located ↔ Near`、`Geographical ↔ Org-Location`
  - 低混淆对预测：`Family ↔ Located`、`Weapon ↔ Business`
  - 比 Few-NERD 66 types 的混淆度分布更可控

---

## 10. 数据获取行动项

### 方案 A（推荐）：使用已有 LDC 数据
1. 确认是否已有 LDC2006T06 数据（许多学术机构有 LDC membership）
2. 使用 wasiahmad/ACE05-Processor 预处理
3. 转换为我们的 parquet 格式

### 方案 B：使用公开预处理版本
1. 部分论文作者会在 GitHub issue 中分享预处理后的 JSON（需确认许可）
2. PURE / DyGIE++ 的预处理输出格式较标准，可直接转换

### 方案 C：仅使用 type schema（不需要原始数据）
1. **对于 BCS 验证实验，实际上可能不需要完整数据集**
2. 只需 18 个 relation type names → 计算 embeddings → 分析 BCS 分布
3. 然后设计 synthetic batches 或使用 LLM 生成 few-shot RE prompts
4. 这可以先行推进，同时并行获取 LDC 数据

---

## 附录：参考资料

- [LDC ACE 2005 Catalog](https://catalog.ldc.upenn.edu/LDC2006T06)
- [ACE Annotation Tasks and Specifications](https://www.ldc.upenn.edu/collaborations/past-projects/ace/annotation-tasks-and-specifications)
- [ACE Semantic Structures (NYU)](https://cs.nyu.edu/~grishman/jet/guide/ACEstructures.html)
- [ACE 2005 Evaluation Plan](https://www.semanticscholar.org/paper/The-ACE-2005-(-ACE-05-)-Evaluation-Plan-Evaluation-Ntroduction/3a9b136ca1ab91592df36f148ef16095f74d009e)
- [wasiahmad/ACE05-Processor](https://github.com/wasiahmad/ACE05-Processor)
- [princeton-nlp/PURE](https://github.com/princeton-nlp/PURE)
- [dwadden/dygiepp](https://github.com/dwadden/dygiepp)
- [nlpcl-lab/ace2005-preprocessing](https://github.com/nlpcl-lab/ace2005-preprocessing)
- [Few-NERD Paper (ACL 2021)](https://arxiv.org/abs/2105.07464)
- [ACE 2005 on Papers With Code](https://paperswithcode.com/dataset/ace-2005)
