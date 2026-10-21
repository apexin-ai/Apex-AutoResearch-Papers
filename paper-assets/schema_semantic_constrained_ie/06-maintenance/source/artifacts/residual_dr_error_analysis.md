# Residual Domain-Range Violation Qualitative Analysis

FT+OntoCoDec full_s1 模式下残余 DR violation 的定性分析。

## 1. Llama SciERC full_s1 (DR=0.09%, 1/1081 triples)

### Violation Instance

| # | doc_id | relation | head (type) | tail (type) | expected valid pairs | 原因分类 |
|---|--------|----------|-------------|-------------|---------------------|---------|
| 1 | NIPS_2001_11_abs_sent4 | Evaluate-for | CID/DRAM analog array prototype (OtherScientificTerm) | approach (Generic) | 23 pairs, 不含 (OtherScientificTerm, Generic) | Schema 覆盖不全 |

### 分析

唯一的 DR violation 是 `Evaluate-for` 关系下 `(OtherScientificTerm, Generic)` 类型对。该 pair 的语义完全合理——用一个科学术语（CID/DRAM analog array prototype）去评估一种方法（approach），但 `approach` 被标注为 Generic 而非 Method。

**根因**：Ontology constraint 是从 SciERC 训练集挖掘的，训练集中 Evaluate-for 出现 313 次，覆盖了 23 种 (head_type, tail_type) 组合，但 `(OtherScientificTerm, Generic)` 恰好未在训练集中出现过。这是一个 **long-tail coverage gap**——constraint 来自有限训练数据的频率统计，极低频但合法的组合会被遗漏。

---

## 2. Qwen DocRED full_s1 (DR=0.01%, 2/15563 triples)

### Violation Instances

| # | doc_id | relation | head (type) | tail (type) | expected valid pairs | 原因分类 |
|---|--------|----------|-------------|-------------|---------------------|---------|
| 1 | Sappy Records | P137 operator | Sappy Records (ORG) | Julie Doiron (PER) | 7 pairs, 不含 (ORG, PER) | Schema 覆盖不全 |
| 2 | Sappy Records | P137 operator | Sappy Records (ORG) | Julie Doiron (PER) | 同上 | Schema 覆盖不全（重复 triple） |

### 分析

两条 violation 实际上是同一文档中同一 triple 的重复（模型在不同位置提取了相同的关系）。

**根因**：P137 (operator) 的 constraint 中 valid pairs 为 `{(LOC,LOC), (LOC,ORG), (MISC,LOC), (MISC,ORG), (ORG,LOC), (ORG,ORG), (PER,ORG)}`，包含 `(PER, ORG)` 但不包含 `(ORG, PER)`。语义上 "Sappy Records operated by Julie Doiron" 完全合理——一个组织由一个人运营。训练集中 `operator` 关系的典型用法是 `(PER, ORG)`（人运营组织），但此处模型以组织为 head、人为 tail，方向与训练集主流用法相反。这是 **constraint 方向性不对称**——`(PER, ORG)` 在 constraint 中但 `(ORG, PER)` 不在。

---

## 3. Llama DocRED full_s1 (DR=0.20%, 33/16074 triples)

### Violation Instances

| # | doc_id | relation (PID) | head (type) | tail (type) | 原因分类 |
|---|--------|----------------|-------------|-------------|---------|
| 1 | Between Five and Seven | P137 operator | Paisley Park (LOC) | Prince (PER) | Entity type 错误：Paisley Park 应为 ORG |
| 2 | Between Five and Seven | P127 owned by | Prince (PER) | Paisley Park (LOC) | Entity type 错误：Paisley Park 应为 ORG |
| 3 | Between Five and Seven | P137 operator | Prince (PER) | Paisley Park (LOC) | Entity type 错误：Paisley Park 应为 ORG |
| 4 | Durán, Ecuador | P155 follows | Eloy Alfaro Delgado (PER) | Leon Febres Cordero (LOC) | Entity type 错误：Leon Febres Cordero 是人名应为 PER |
| 5 | Hidhir Hasbiallah | P710 participant | National Football League (ORG) | Police Sports Association (ORG) | Schema 覆盖不全：(ORG,ORG) 不在 P710 valid pairs |
| 6 | Medan, son of Abraham | P674 characters | Bible (MISC) | Madan (LOC) | Entity type 错误：Madan 是人名应为 PER |
| 7 | Contact Group (Balkans) | P488 chairperson | EU Council (ORG) | EU Presidency (ORG) | Schema 覆盖不全：(ORG,ORG) 不在 P488 valid pairs |
| 8-13 | Silvan Elves | P361 part of | {Thranduil, Legolas, Amdír, Amroth, Galadriel, Celeborn} (PER) | Middle-earth (LOC) | Schema 覆盖不全 + 语义边界：(PER,LOC) 不在 P361 valid pairs |
| 14 | Silvan Elves | P31 instance of | Celeborn (PER) | Silvan Elves (PER) | 错误关系：应为 P31 "instance of" (PER,ORG) 或其他关系 |
| 15 | Silvan Elves | P364 original language of work | Silvan Elves (ORG) | English (LOC) | Entity type 错误：English 语言应为 MISC；Silvan Elves 应为 MISC |
| 16-17 | Debra Hill | P1344 participant of | Debra Hill (PER) | {1973, 1983} (TIME) | 错误关系：时间点不是"participant of"的对象 |
| 18-19 | Debra Hill | P166 award received | Debra Hill (PER) | {1973, 1983} (TIME) | 错误关系：时间点不是奖项 |
| 20 | Rick Scott | P1001 applies to jurisdiction | Rick Scott (PER) | Florida (LOC) | Schema 覆盖不全：(PER,LOC) 不在 P1001 valid pairs |
| 21 | Rick Scott | P112 founded by | Rick Scott (PER) | Columbia HCA (ORG) | 方向反转：应为 (ORG, PER)，即 Columbia HCA founded by Rick Scott |
| 22-23 | Arjuna | P31 instance of | {Narayana↔Vishnu} (PER,PER) | — | 错误关系：Narayana 和 Vishnu 不是 instance-of 关系 |
| 24 | Lee Hall Mansion | P127 owned by | Lee Hall (PER) | Richard Decatur Lee (PER) | Entity type 错误：Lee Hall 是建筑应为 LOC/MISC |
| 25-26 | The Storming of the Winter Palace | P585 point in time | Petrograd (LOC) | {October Revolution, February Revolution} (LOC) | Entity type 错误：革命事件应为 MISC/TIME |
| 27-29 | G. V. Belyi | P937 work location | {Moscow×2, Vladimir} (LOC) | {Moscow State University, Steklov Institute, Vladimir State University} (ORG) | 方向反转：应为 PER→LOC/ORG |
| 30 | Ulysses (novel) | P123 publisher | Paris (LOC) | Sylvia Beach (PER) | Entity type 错误：应以书名为 head |
| 31-33 | Reichskommissariat... | P710 participant | German (LOC) | {3个ORG} | Entity type 错误：German 应为 MISC（国籍形容词） |

### 按关系类型统计

| Relation | PID | Violation 数 | 占比 |
|----------|-----|-------------|------|
| part of | P361 | 6 | 18.2% |
| participant | P710 | 4 | 12.1% |
| instance of | P31 | 3 | 9.1% |
| work location | P937 | 3 | 9.1% |
| operator | P137 | 2 | 6.1% |
| owned by | P127 | 2 | 6.1% |
| participant of | P1344 | 2 | 6.1% |
| award received | P166 | 2 | 6.1% |
| point in time | P585 | 2 | 6.1% |
| 其余 7 种关系 | — | 各 1 | 各 3.0% |

### 按 (head_type, tail_type) 统计

| Entity Pair | 出现次数 | 涉及关系 |
|-------------|---------|---------|
| (PER, LOC) | 8 | P361×6, P155×1, P137×1 |
| (LOC, ORG) | 6 | P937×3, P710×3 |
| (PER, TIME) | 4 | P1344×2, P166×2 |
| (PER, PER) | 3 | P31×2, P127×1 |
| (LOC, LOC) | 2 | P585×2 |
| (LOC, PER) | 2 | P137×1, P123×1 |
| 其余 | 各 1 | — |

---

## 4. 汇总：原因分类

### 分类定义

| 原因分类 | 定义 |
|---------|------|
| **A. Entity type 错误** | LLM 对实体类型的标注有误（如人名标为 LOC、组织标为 PER），导致 (head_type, tail_type) 不在 valid pairs |
| **B. Schema 覆盖不全** | 实体类型标注正确，但该 type pair 在训练集中从未出现过，属于 constraint 的 long-tail gap |
| **C. 关系方向反转** | 模型把 head/tail 的角色弄反了（如 "founded by" 应为 ORG→PER 但输出了 PER→ORG） |
| **D. 错误关系选择** | 模型选择了语义不匹配的关系类型 |

### 各 Setting 统计

| Setting | 总 Violation | A. ET错误 | B. Schema不全 | C. 方向反转 | D. 错关系 |
|---------|-------------|----------|-------------|-----------|---------|
| Llama SciERC full_s1 | 1 | 0 | 1 | 0 | 0 |
| Qwen DocRED full_s1 | 2 | 0 | 2 | 0 | 0 |
| Llama DocRED full_s1 | 33 | 14 | 9 | 4 | 6 |
| **合计** | **36** | **14 (39%)** | **12 (33%)** | **4 (11%)** | **6 (17%)** |

### 关键发现

1. **Llama DocRED 贡献了 92% 的残余 DR violation**（33/36），说明 Llama 在 DocRED 数据集上的 entity typing 能力弱于 Qwen。

2. **Entity type 错误是最大来源**（39%），典型 pattern：
   - 地名/国籍形容词（German, English）被标为 LOC 而非 MISC
   - 机构名称（Paisley Park）被标为 LOC 而非 ORG
   - 人名（Leon Febres Cordero, Madan）被标为 LOC
   - 建筑名（Lee Hall）被标为 PER

3. **Schema 覆盖不全是第二大来源**（33%），但这些是 constraint 设计的固有局限——基于训练集频率挖掘的 valid pairs 无法覆盖所有合法组合。典型案例：
   - `P361 part of` 中 `(PER, LOC)` 在虚构世界语境下合理但训练集未见
   - `P137 operator` 中 `(ORG, PER)` 与 `(PER, ORG)` 的方向不对称
   - `P710 participant` 中 `(ORG, ORG)` 未被覆盖

4. **关系方向反转**（11%）集中在 `work location` 和 `founded by`，模型把 head/tail 搞反。

5. **错误关系选择**（17%）多为年份被当作事件参与（participant of）或奖项（award received），以及 Tolkien 虚构世界中 instance-of 的误用。

6. **Qwen 和 SciERC 的残余 violation 全部是 schema 覆盖不全**（类别 B），说明在这些 setting 下 LLM 的 entity typing 已经足够准确，剩余问题完全是 constraint 的 long-tail 边界问题。

### 对 OntoCoDec 框架的启示

- 当前 constraint 已经非常有效（full_s1 模式下 DR 从 unconstrained 的数个百分点降到 <0.21%）
- 残余 violation 中约 1/3 是 constraint 的固有局限（训练集频率覆盖），这部分无法通过改进 decoding 消除，只能通过扩展 ontology 或接受为 residual noise
- Entity type 错误导致的 violation（39%）理论上可通过更强的 entity type constraint 进一步压缩，但收益递减
