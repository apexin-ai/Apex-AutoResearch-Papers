# TACRED Schema 分析与 OntoCoDec 适配评估

## 1. TACRED Schema 结构

### 1.1 Entity Types (17 types)

| 类别 | 类型 |
|------|------|
| 核心 NER | PERSON, ORGANIZATION, LOCATION |
| 地理细分 | CITY, COUNTRY, STATE_OR_PROVINCE, NATIONALITY |
| 数值 | NUMBER, DURATION, ORDINAL, PERCENT, MONEY |
| 时间 | DATE, TIME |
| TAC KBP 专用 | TITLE, RELIGION, IDEOLOGY, CRIMINAL_CHARGE, CAUSE_OF_DEATH, URL |
| 其他 | MISC |

**关键特征**: Subject 只允许 PERSON 或 ORGANIZATION（二选一），Object 覆盖全部 17 类型。

### 1.2 Relation Types (41 relations + no_relation)

#### per:* relations (25 个，subject=PERSON)

| Relation | Object Type(s) | Valid Pairs |
|----------|----------------|-------------|
| per:alternate_names | PERSON, MISC | 2 |
| per:age | NUMBER, DURATION | 2 |
| per:cause_of_death | CAUSE_OF_DEATH | 1 |
| per:charges | CRIMINAL_CHARGE | 1 |
| per:children | PERSON | 1 |
| per:cities_of_residence | CITY, LOCATION | 2 |
| per:city_of_birth | CITY, LOCATION | 2 |
| per:city_of_death | CITY, LOCATION | 2 |
| per:countries_of_residence | COUNTRY, NATIONALITY, LOCATION | 3 |
| per:country_of_birth | COUNTRY, NATIONALITY, LOCATION | 3 |
| per:country_of_death | COUNTRY, NATIONALITY, LOCATION | 3 |
| per:date_of_birth | DATE | 1 |
| per:date_of_death | DATE | 1 |
| per:employee_of | ORGANIZATION, LOCATION | 2 |
| per:origin | COUNTRY, NATIONALITY, LOCATION | 3 |
| per:other_family | PERSON | 1 |
| per:parents | PERSON | 1 |
| per:religion | RELIGION | 1 |
| per:schools_attended | ORGANIZATION | 1 |
| per:siblings | PERSON | 1 |
| per:spouse | PERSON | 1 |
| per:stateorprovince_of_birth | STATE_OR_PROVINCE, LOCATION | 2 |
| per:stateorprovince_of_death | STATE_OR_PROVINCE, LOCATION | 2 |
| per:stateorprovinces_of_residence | STATE_OR_PROVINCE, LOCATION | 2 |
| per:title | TITLE | 1 |

#### org:* relations (16 个，subject=ORGANIZATION)

| Relation | Object Type(s) | Valid Pairs |
|----------|----------------|-------------|
| org:alternate_names | ORGANIZATION, MISC | 2 |
| org:city_of_headquarters | CITY, LOCATION | 2 |
| org:country_of_headquarters | COUNTRY, LOCATION | 2 |
| org:dissolved | DATE | 1 |
| org:founded | DATE | 1 |
| org:founded_by | PERSON | 1 |
| org:member_of | ORGANIZATION, COUNTRY, STATE_OR_PROVINCE, LOCATION | 4 |
| org:members | ORGANIZATION, COUNTRY | 2 |
| org:number_of_employees/members | NUMBER | 1 |
| org:parents | ORGANIZATION, COUNTRY, STATE_OR_PROVINCE, LOCATION | 4 |
| org:political/religious_affiliation | RELIGION, IDEOLOGY | 2 |
| org:shareholders | PERSON, ORGANIZATION | 2 |
| org:stateorprovince_of_headquarters | STATE_OR_PROVINCE, LOCATION | 2 |
| org:subsidiaries | ORGANIZATION, COUNTRY, LOCATION | 3 |
| org:top_members/employees | PERSON | 1 |
| org:website | URL | 1 |

### 1.3 no_relation

占全部数据的 79.5%（~84,478 / 106,264 条）。适用于任意 entity type pair。

---

## 2. Constraint Tightness 预估

### 计算方法

τ = 1 − |valid_pairs| / |total_possible_pairs|

| 度量方式 | Entity Types | Total Possible | Avg Valid/Rel | Avg τ |
|----------|-------------|----------------|---------------|-------|
| 全类型空间 (17²) | 17 | 289 | 1.78 | **0.994** |
| 结构可能空间 (2×17) | 2 subj × 17 obj | 34 | 1.78 | **0.948** |

### 与 SciERC / DocRED 对比

| Dataset | Entity Types | Relations | Total Possible | Avg Valid/Rel | Avg τ |
|---------|-------------|-----------|----------------|---------------|-------|
| SciERC | 6 | 7 | 36 | 24.0 | 0.333 |
| DocRED | 6 | 96 | 36 | 5.68 | 0.842 |
| **TACRED (17²)** | **17** | **41** | **289** | **1.78** | **0.994** |
| **TACRED (2×17)** | **17** | **41** | **34** | **1.78** | **0.948** |

### Per-relation τ 分布 (基于 17² = 289)

| Valid Pairs | # Relations | τ | 示例 |
|-------------|------------|---|------|
| 1 | 20 | 0.997 | per:cause_of_death, per:date_of_birth, org:website |
| 2 | 14 | 0.993 | per:age, per:employee_of, org:shareholders |
| 3 | 5 | 0.990 | per:countries_of_residence, org:subsidiaries |
| 4 | 2 | 0.986 | org:member_of, org:parents |

**关键发现**: TACRED 的 41 个 relation 中，20 个只有 1 个 valid pair（τ=0.997），全部 relation 的 τ > 0.986。这是极端紧约束 schema。

---

## 3. OntoCoDec 适配评估

### 3.1 Schema 格式兼容性

TACRED 可直接转换为 ontology_constraints.json 格式：

```json
{
  "entity_types": ["PERSON", "ORGANIZATION", "LOCATION", "CITY", "COUNTRY",
                   "STATE_OR_PROVINCE", "NATIONALITY", "DATE", "TIME",
                   "NUMBER", "DURATION", "ORDINAL", "PERCENT", "MONEY",
                   "TITLE", "RELIGION", "IDEOLOGY", "CRIMINAL_CHARGE",
                   "CAUSE_OF_DEATH", "URL", "MISC"],
  "relation_types": ["per:alternate_names", "per:age", ...],
  "relation_constraints": {
    "per:age": {
      "valid_pairs": [
        ["PERSON", "NUMBER"],
        ["PERSON", "DURATION"]
      ]
    },
    "org:founded_by": {
      "valid_pairs": [
        ["ORGANIZATION", "PERSON"]
      ]
    }
  }
}
```

**结论**: 格式完全兼容，无需修改 OntologyCompiler。

### 3.2 no_relation 处理

OntoCoDec 的 ontology_constraints.json **不包含 no_relation**——它只定义有效 relation 的约束。no_relation 是模型输出层的分类决策，不进入 schema constraint 系统。

**对 OntoCoDec pipeline 的影响**:
- 生成式 IE 中，模型通过不生成 relation triple 来表达 no_relation（隐式处理）
- 无需修改 OntoCoDec 来"支持" no_relation
- 但 TACRED 79.5% 的样本是 no_relation → 评估时需要正确处理空输出

### 3.3 句级 vs 文档级

| 维度 | TACRED (句级) | DocRED (文档级) |
|------|-------------|----------------|
| 输入 | 单句 + 1 个 subject-object pair | 多段文本 + 多个 entity mentions |
| 每条输出 | 最多 1 个 relation (或 no_relation) | 多个 relation triples |
| Entity 标注 | Subject/object 位置已给定 | 需要识别 entity mentions |

**OntoCoDec 当前支持情况**:
- OntoCoDec 的生成格式是 `{"entities": [...], "relations": [...]}` —— 天然支持多 entity + 多 relation
- 对于 TACRED 句级任务，两种适配方案：

**方案 A: 保持生成式 IE 框架（推荐）**
- 输入句子，让模型生成所有 entity 和 relation
- 与 SciERC pipeline 相同，无需改动
- 优点：直接复用现有 pipeline
- 缺点：TACRED 原始 task 是给定 entity pair 分类 relation，转为生成式后 task 有变化

**方案 B: Relation Classification 模式**
- 输入句子 + 已标注的 subject/object entity
- 模型只输出 relation type
- 需要修改 prompt template 和输出格式
- 更贴近 TACRED 原始 task，但需要改 pipeline

### 3.4 17 Entity Types 的 First-Token 唯一性

OntoCoDec 依赖 entity type 首 token 唯一性来做 token-level masking。17 个 entity type 需要验证：

| Type | 首字符 | 潜在冲突 |
|------|--------|---------|
| PERSON | P | PERCENT |
| ORGANIZATION | O | ORDINAL |
| LOCATION | L | - |
| CITY | C | COUNTRY, CRIMINAL_CHARGE, CAUSE_OF_DEATH |
| COUNTRY | C | CITY, CRIMINAL_CHARGE, CAUSE_OF_DEATH |
| STATE_OR_PROVINCE | S | - |
| NATIONALITY | N | NUMBER |
| DATE | D | DURATION |
| TIME | T | TITLE |
| NUMBER | N | NATIONALITY |
| DURATION | D | DATE |
| ORDINAL | O | ORGANIZATION |
| PERCENT | P | PERSON |
| MONEY | M | MISC |
| TITLE | T | TIME |
| RELIGION | R | - |
| IDEOLOGY | I | - |
| CRIMINAL_CHARGE | C | CITY, COUNTRY, CAUSE_OF_DEATH |
| CAUSE_OF_DEATH | C | CITY, COUNTRY, CRIMINAL_CHARGE |
| URL | U | - |
| MISC | M | MONEY |

**存在大量首字符冲突**（C×4, P×2, N×2, D×2, T×2, O×2, M×2）。

在 tokenizer 层面，如果使用完整 token（如 Qwen3-8B 的 BPE），需要验证：
- "PERSON" vs "PERCENT" → 首 token 是否相同？取决于 tokenizer 分词
- "CITY" vs "COUNTRY" vs "CRIMINAL_CHARGE" vs "CAUSE_OF_DEATH" → 首 token 可能都是 "C" 的某个 token

**风险**: 17 types 中有 11 个存在首字符冲突组，大概率存在 first-token 不唯一问题。

**缓解方案**:
1. **类型名重命名**: 使用无前缀冲突的名称（如 "CrimCharge" → "Charge"）
2. **类型合并**: 将 17 types 合并为更少的粗粒度类型（见 §3.5）
3. **多 token masking**: 扩展 TypeConstraintProcessor 支持 multi-token prefix 消歧（需改代码）

### 3.5 类型合并方案（降低 tightness + 解决 first-token 冲突）

| 合并后类型 | 原始类型 | 含义 |
|-----------|---------|------|
| PER | PERSON | 人物 |
| ORG | ORGANIZATION | 组织 |
| LOC | LOCATION, CITY, COUNTRY, STATE_OR_PROVINCE, NATIONALITY | 地理/地点 |
| DATE | DATE, TIME | 时间 |
| NUM | NUMBER, DURATION, ORDINAL, PERCENT, MONEY | 数值 |
| MISC | MISC, TITLE, RELIGION, IDEOLOGY, CRIMINAL_CHARGE, CAUSE_OF_DEATH, URL | 其他 |

合并为 6 types → total_possible_pairs = 36，与 SciERC/DocRED 完全一致。

**合并后 tightness 预估**:
- 每个 per:* relation: subject=PER, object 合并后通常为 1-2 types → avg valid pairs ≈ 2.5
- 每个 org:* relation: subject=ORG, object 合并后通常为 1-2 types → avg valid pairs ≈ 2.0
- 总体 avg valid pairs ≈ 2.3 / 36 → **τ_avg ≈ 0.936**

仍然很紧，但比 0.994 有改善。进一步合并（如 MISC 拆分为 TITLE 和 OTHER）需要 case-by-case 评估。

---

## 4. 数据集版本推荐

| 维度 | TACRED (LDC) | TACREV | Re-TACRED |
|------|-------------|--------|-----------|
| Schema | 41 relations | 41 relations（不变） | 40 relations（有增删改） |
| 数据质量 | 23.9% 标注错误 | 修正 dev+test 5k 样本 | 全量重标注 |
| License | LDC ($25 非会员) | MIT (patches) + LDC (底层数据) | LDC (底层数据) |
| 学术认可度 | 最广泛 | 主流 | 主流 |
| 独立使用 | 可 | 需原版 TACRED | 需原版 TACRED |
| 样本量 | 106,264 | 106,264 (修 5k) | 91,467 (删 15k 歧义样本) |

### 推荐

**首选 TACREV**:
1. Schema 与原版 TACRED 完全一致（41 relations），不引入额外复杂度
2. 修正了高影响标注错误，F1 提升 ~8%
3. 当前论文标准做法是同时报告 TACRED/TACREV/Re-TACRED 三组结果
4. Patch 格式，应用在原版数据上即可

**次选 Re-TACRED**: 数据质量最高（全量重标注），但 schema 变了（40 relations，有增删），需要额外处理。

**底线**: 三个版本都需要 LDC 的原版 TACRED 数据。需先确认是否有 LDC access。

---

## 5. 适配工作量估算

### 低成本任务（1-2 天）

| 任务 | 说明 |
|------|------|
| 编写 ontology_constraints_tacred.json | 从 type constraint 表直接转换，纯手工或脚本生成 |
| Prompt template 适配 | 修改 SciERC prompt 为 TACRED 格式 |
| 数据加载器 | TACRED JSON → OntoCoDec 输入格式转换脚本 |

### 中等成本任务（2-4 天）

| 任务 | 说明 |
|------|------|
| First-token 唯一性验证与修复 | 17 types 在目标 tokenizer 上验证，可能需要重命名或实现 multi-token masking |
| 评估脚本适配 | TACRED 标准评估（micro-F1, 排除 no_relation）与 OntoCoDec violation checker 对接 |
| 类型合并方案实验 | 17 types vs 6 types 的 tightness 对比实验 |

### 风险点

| 风险 | 影响 | 缓解 |
|------|------|------|
| **极端 tightness (τ≈0.994)** | grammar-first fallback 率极高，semantic constraint 几乎无法生效 | 类型合并；或验证 TACRED 是否仍是有价值的 evaluation target |
| **First-token 冲突** | TypeConstraintProcessor 无法正确 mask | 重命名 type names 或扩展 multi-token masking |
| **79.5% no_relation** | 大量样本无 relation 输出，evaluation 需特殊处理 | 筛选 positive-only subset 做 constraint violation 分析 |
| **句级 vs 生成式 task mismatch** | TACRED 原始 task 是 relation classification (给定 entity pair)，OntoCoDec 是 end-to-end IE | 接受 task 差异，或实现 relation-classification 模式 |
| **LDC 数据访问** | 需要付费获取原版 TACRED | 确认 LDC access；无法获取则排除 TACRED |

---

## 6. 结论

TACRED 的 schema 格式与 OntoCoDec 完全兼容，可直接转换为 ontology_constraints.json。但 **极端 constraint tightness (τ≈0.994)** 是核心挑战——这比 DocRED (0.842) 还紧一个数量级，意味着 semantic constraint layer 几乎不可能在 grammar-first fallback 机制下有效生效。

如果目标是 **验证 OntoCoDec 在不同 tightness 级别上的表现**，TACRED 是理想的极端数据点（τ≈0.994 vs SciERC 0.333 vs DocRED 0.842），构成完整的 tightness spectrum。

如果目标是 **展示 OntoCoDec 的实用价值**，TACRED 不是好选择——约束太紧，几乎所有 relation 只有 1-2 个 valid pair，fallback 率会接近 100%。
