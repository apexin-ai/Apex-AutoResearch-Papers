# Event Extraction 数据集可行性研究报告

**日期**: 2026-05-17  
**目标**: 评估将 OntoCoDec 从 Relation Extraction 扩展到 Event Extraction 的数据集选项

## 核心需求

OntoCoDec 的 semantic layer 需要 **schema-level entity type constraints on argument roles**，即 ontology 中定义 `(event_type, argument_role) → allowed_entity_types` 的映射关系。没有这种约束，semantic layer 无法发挥作用。

---

## 1. MAVEN 评估结果

### MAVEN (原始版本, Wang et al., EMNLP 2020)
- **标注内容**: 仅 event detection (trigger + event type)
- **event types**: 168
- **argument extraction**: 无
- **结论**: ❌ 完全不适合，没有 argument 标注

### MAVEN-Arg (Wang et al., ACL 2024)
- **标注内容**: event detection + argument extraction (trigger, event type, argument roles, entity mentions)
- **event types**: 162
- **argument roles**: 612 (unique)
- **entity types**: 7 (Person, Organization, Location, Building, Product, Art, MISC)
- **数据量**: 98,591 events, 290,613 arguments
- **schema-level entity type constraints**: ❌ **无**
  - Schema 设计基于 FrameNet，强调语义一致性而非 entity type binding
  - 论文原文: "argument roles sharing the same semantic role use the same name but distinguish them with different textual definitions"
  - 数据中 entity 有 type 标注，但 ontology 没有定义 role→entity_type 约束
- **其他问题**: test set 标注未公开（需提交 CodaLab 评估）
- **结论**: ❌ 不适合。虽然规模大，但缺少 role→entity type constraints，无法展示 OntoCoDec 的 semantic layer

---

## 2. 备选数据集评估

### 2.1 WikiEvents (Li et al., NAACL 2021) — ✅ 强烈推荐

| 指标 | 值 |
|------|-----|
| Event types | 51 (层级结构，如 Conflict.Attack.DetonateExplode) |
| Unique argument roles | 80 |
| Unique entity types | 26 (per, org, gpe, loc, fac, veh, wea, com, mhi, aml, bod, ...) |
| Role→Entity type constraints | ✅ **226 组显式约束** (event_role_KAIROS.json 中的 role_types 字段) |
| 数据来源 | Wikipedia event articles |
| 许可 | 免费下载 (S3: gen-arg-data.s3.us-east-2.amazonaws.com) |
| Ontology | KAIROS (DARPA LDC) |
| 标注层级 | Document-level (含跨句 argument linking) |

**Schema 约束示例**:
```
ArtifactExistence.DamageDestroyDisableDismantle.Damage:
  Damager:    [per, org, gpe, sid]
  Artifact:   [bal, com, fac, loc, mon, nat, pth, veh, wea]
  Instrument: [com, veh, wea]
  Place:      [loc, gpe, fac]

Life.Die.Unspecified:
  Killer: [per, org, gpe, sid]
  Victim: [per, org, gpe, aml]
  Instrument: [com, veh, wea]
  Place:  [loc, gpe, fac]
```

**为什么最适合 OntoCoDec**:
1. `event_role_KAIROS.json` 中的 `role_types` 字段直接提供 (event_type, role) → entity_types 映射
2. 26 种 entity types 比 ACE05 (7 types) 更丰富，约束更细粒度
3. 51 event types + 80 roles + 226 constraints = 足够的 schema 复杂度来展示 scalability
4. Document-level argument extraction = 更具挑战性的设置
5. 免费下载，无 LDC 付费门槛

### 2.2 RAMS (Ebner et al., ACL 2020) — ⚠️ 部分适合

| 指标 | 值 |
|------|-----|
| Event types | 139 |
| Argument roles | 65 |
| 数据量 | 9,124 events |
| Ontology TSV | 有，但定义 role→cardinality (每个 event type 允许多少个该 role) |
| Entity type constraints | ⚠️ 不确定。ontology 主要是 cardinality 约束，非 entity type 约束 |
| 许可 | CC-BY-SA-4.0，免费 |

**问题**: RAMS ontology TSV 的约束形式是 "event X 的 role Y 最多出现 Z 次"，不是 "role Y 必须是 entity type T"。数据格式中 `ent_spans` 有类型信息，但 schema 层面的 entity type 约束不明确。

### 2.3 CASIE (5 event types) — ❌ 太小
### 2.4 PHEE (pharmacovigilance) — ❌ domain-specific，通用性不足
### 2.5 ACE05 — ❌ LDC 付费，数据不可用

---

## 3. 对比表

| 数据集 | Event Types | Arg Roles | Entity Types | Role→ET Constraints | 免费 | 学术认可度 |
|--------|:-----------:|:---------:|:------------:|:-------------------:|:----:|:----------:|
| MAVEN (原版) | 168 | 0 | 0 | ❌ | ✅ | 高 (EMNLP 2020) |
| MAVEN-Arg | 162 | 612 | 7 | ❌ | ✅* | 高 (ACL 2024) |
| **WikiEvents** | **51** | **80** | **26** | **✅ 226组** | **✅** | **高 (NAACL 2021)** |
| RAMS | 139 | 65 | ? | ⚠️ 不确定 | ✅ | 高 (ACL 2020) |
| ACE05 | 33 | 36 | 7 | ✅ | ❌ | 最高 |

*MAVEN-Arg test set 未公开

---

## 4. 推荐方案

### 首选: WikiEvents

**理由**:
1. **唯一一个同时满足全部必须条件的数据集**: 有显式 role→entity type constraints + 免费下载
2. KAIROS ontology 的 `role_types` 字段与 OntoCoDec 的 semantic layer 无缝对接
3. 26 种 entity types 比 ACE05 (7 types) 提供更大的 constraint space，更能体现 semantic layer 的价值
4. Document-level extraction 是更有挑战性的 setting，论文讲故事更有吸引力
5. 社区广泛使用 (Papers with Code benchmark, 大量 follow-up work)

**潜在风险**:
- 51 event types 比 MAVEN-Arg (162) 少，scalability 故事稍弱
- 数据量相对较小（约 246 docs）

**缓解**:
- 51 types + 80 roles + 226 constraints 已经足够展示 OntoCoDec 的 schema scalability
- 可以在论文中同时报告 WikiEvents 和 RAMS 的结果（RAMS 做补充实验）

### 备选: RAMS (作为补充实验)
如果从 RAMS 数据中可以反向挖掘出 entity type constraints（通过统计数据中 role→entity type 的分布），可以作为第二个实验数据集。

---

## 5. WikiEvents 数据统计（已下载验证）

### 5.1 数据规模

| Split | Documents | Events | Entities | Arguments |
|-------|:---------:|:------:|:--------:|:---------:|
| train | 206 | 3,241 | 28,296 | 4,542 |
| dev | 20 | 345 | 2,256 | 428 |
| test | 20 | 365 | 2,673 | 566 |
| **Total** | **246** | **3,951** | **33,225** | **5,536** |

### 5.2 Entity Type 分布

| Type | Count | 说明 |
|------|------:|------|
| PER | 16,616 | Person |
| GPE | 5,411 | Geopolitical Entity |
| ORG | 4,604 | Organization |
| FAC | 2,358 | Facility |
| WEA | 1,460 | Weapon |
| LOC | 985 | Location |
| VEH | 854 | Vehicle |
| VAL | 419 | Value |
| COM | 261 | Commodity |
| TTL | 95 | Title |
| MHI | 48 | Medical/Health Issue |
| INF | 32 | Information |
| ABS | 27 | Abstract |
| MON | 26 | Money |
| BOD | 15 | Body Part |
| CRM | 7 | Crime |
| SID | 7 | Side |

### 5.3 Top 10 Event Types

| Event Type | Count |
|------------|------:|
| Conflict.Attack.DetonateExplode | 823 |
| Life.Die.Unspecified | 525 |
| Conflict.Attack.Unspecified | 411 |
| Life.Injure.Unspecified | 301 |
| Contact.Contact.Unspecified | 202 |
| Contact.Contact.Broadcast | 195 |
| Justice.ArrestJailDetain.Unspecified | 188 |
| Movement.Transportation.Unspecified | 156 |
| Justice.ChargeIndict.Unspecified | 104 |
| Justice.InvestigateCrime.Unspecified | 92 |

数据中共出现 50 种 event types、59 种 argument roles。

### 5.4 Schema Constraint 验证

| 指标 | 值 |
|------|-----|
| 总 arguments | 5,536 |
| 有 entity type 的 arguments | 5,536 (100%) |
| 约束满足 | 5,504 |
| 约束违反 | 1 (标注错误: VEH as Destination) |
| **满足率** | **99.98%** |
| 不在 schema 中的 (event, role) | 31 (部分子类型) |
| Distinct (event, role, entity_type) triples | 348 |

Schema 约束与实际数据高度一致，确认 KAIROS ontology 适合 OntoCoDec 的 semantic layer。

### 5.5 数据位置

| 文件 | 路径 | 状态 |
|------|------|------|
| 本地分析副本 | `data/wikievents/{train,dev,test}.jsonl, event_role_KAIROS.json` | ✅ 完整 |
| 服务器 schema | `/root/.../data/wikievents/event_role_KAIROS.json` (40KB) | ✅ 完整 |
| 服务器数据 | `/root/.../data/wikievents/{train,dev,test}.jsonl` | ⏳ 后台下载中 (S3→中国较慢) |

---

## 6. 下一步行动

1. 将 WikiEvents 数据传输到 westd-16980 服务器
2. 编写 WikiEvents 数据加载和预处理代码
3. 从 `event_role_KAIROS.json` 构建 OntoCoDec 的 semantic constraint matrix
4. 设计 Event Extraction 版本的 constrained decoding 实验
5. 可选：从 RAMS 数据中反向挖掘 entity type constraints 作为补充实验
