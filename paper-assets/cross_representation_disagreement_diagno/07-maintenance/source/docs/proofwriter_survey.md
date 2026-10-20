# ProofWriter 数据集调研报告

## 1. 数据集基本信息

**论文**: Tafjord, Dalvi, Clark. "ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language." Findings of ACL-IJCNLP 2021.

**任务格式**: NLI 风格，与 FOLIO 一致
- **输入**: theory（自然语言事实 + 规则）+ question（待验证陈述）
- **输出**: True / False / Unknown（OWA 设定下）
- **附加**: 每个样本包含推理证明（DAG 格式）

**数据规模**（OWA，与我们相关的设定）:

| Depth | Theories | Questions |
|-------|----------|-----------|
| D0 | 26,978 | 100,000 |
| D1 | 12,933 | 100,014 |
| D2 | 9,033 | 100,010 |
| D3 | 6,940 | 100,036 |
| D5 | 4,752 | 100,030 |

总计 ~500k questions (OWA)。Split: 70% train / 10% dev / 20% test。无 D4。

**标签分布**:
- **OWA**: True / False / Unknown 各约 **33%**（均衡分布）
- **CWA**: 仅 True / False（无 Unknown），与我们不兼容
- 对比 FOLIO：~39% Unknown，ProofWriter 更均衡

**4 种配置**: AttNeg（属性+否定）、AttNoneg（属性无否定）、RelNeg（关系+否定）、RelNoneg（关系无否定）

## 2. 与 FOLIO 的对比

| 维度 | ProofWriter | FOLIO |
|------|------------|-------|
| 生成方式 | **合成/模板化**（Datalog 程序生成） | **专家人工标注** |
| 词汇量 | ~101 词 | 4,351 词 |
| 自然语言风格 | 简单模板句："Charlie is quiet." "If someone is kind then they are young." | 真实自然语言，语义复杂 |
| 规模 | ~500k (OWA) | 1,435 样本 |
| 标签 | True/False/Unknown (OWA) | True/False/Unknown |
| FOL 标注 | 无 | 有 |
| 推理深度 | 显式标注 D0-D5 | 隐式（范围 0-14） |
| 证明 | 包含（DAG） | 无 |

**核心差异**: ProofWriter 是合成数据，语言高度模板化，推理结构干净可控；FOLIO 是真实自然语言，语义歧义多，形式化难度高。两者互补性强。

**FOL 形式化适配性**: ProofWriter 的规则结构极其规整（一阶 Horn 子句 + 否定），转 Z3 非常直接。事实是简单的一元/二元谓词，规则是标准的 if-then 形式。比 FOLIO 容易得多。

**Python 代码形式化适配性**: 同样容易。事实可表示为集合/字典，规则可表示为函数或推理循环。模板化结构意味着 LLM 生成代码的变异性更低。

## 3. 对我们方法的预期影响

### 3.1 不对称性预测

**核心问题**: ProofWriter 会放大还是缩小 FOLIO 上观察到的 9:1 FOL 偏向不对称性？

**预测: disagree rate 会显著降低，不对称性模式可能改变。**

理由：
- ProofWriter 的模板化语言大幅降低了 NL→FOL 和 NL→Code 的翻译难度
- FOL 和 Code 都会变得更准确 → agree rate 上升 → disagree 样本减少
- FOLIO 的 9:1 不对称性很可能源于 FOLIO 的语义复杂性对 Code 形式化的挑战更大（自然语言歧义 → Code 更容易出错），而 ProofWriter 消除了这一因素

**两种可能的结果**:
1. **不对称性缩小**（如 6:4 或 5:5）：说明不对称性与数据集语言复杂度相关，非方法固有偏差 → 对论文有利
2. **不对称性保持但方向可能翻转**：如果 Code 在结构化数据上反而更强 → 更有趣的发现

### 3.2 推理深度作为分析轴

**高价值**。可以回答：
- 浅层推理（D0-D1）是否 agree rate 极高（两种表征都轻松搞定）？
- 深层推理（D3-D5）是否 disagree rate 上升？哪种表征在深层推理更脆弱？
- 这为论文提供了 "推理复杂度 vs 表征分歧" 的分析维度，FOLIO 无法提供

### 3.3 风险

- **disagree 样本太少**: 如果两种表征在简单模板数据上都接近完美，disagree 数量可能不足以支撑统计分析
- **缓解**: 使用 D5（最深推理）+ RelNeg（关系+否定，最复杂配置）来最大化难度

## 4. 实操信息

### 4.1 HuggingFace 数据集

**推荐: `smoorsmith/proofwriter`**
- 4,200 行（train 3,000 / dev 600 / test 600）
- OWA D5 子集，来自 Logic-LLM 仓库（与 FOLIO 评测对齐）
- 字段: `id`, `context`, `question`, `options`, `answer`, `depth`, `chain_of_thought`
- Logic-LLM 论文正是用 FOLIO + ProofWriter OWA-D5 做评测，有直接可比性

**其他版本**:
- `tasksource/proofwriter`: 845k 行，全量数据，覆盖所有深度和配置
- `D3xter1922/proofwriter-dataset`: 59k 行，原始格式

### 4.2 Pipeline 适配

当前 FOLIO 格式: `{premises, conclusion, label}`

ProofWriter (`smoorsmith/proofwriter`) 适配：
```
context → premises（事实+规则文本）
question → 需提取结论（去掉 "Based on the above information, is the following statement true, false, or unknown?" 前缀）
answer → label（True/False/Unknown）
depth → 额外元数据（用于分层分析）
```

改动量小，新增一个 `ProofWriterDataLoader` 即可。

### 4.3 推荐评测配置

| 配置 | 样本数 | 理由 |
|------|--------|------|
| **OWA D5 test set** | 600 | Logic-LLM 标准配置，三类标签均衡，推理深度最大 |
| 如需缩减 | 随机采样 200-300 | 保持标签均衡采样 |

**推荐方案**: 直接用 `smoorsmith/proofwriter` 的 600 test 样本，与 FOLIO 的 204 样本规模接近。

## 5. 替代数据集

| 数据集 | 标签 | 格式匹配度 | 优势 | 劣势 | 推荐度 |
|--------|------|-----------|------|------|--------|
| **ProofWriter OWA** | T/F/U | ★★★★★ | 标签一致、Logic-LLM 先例、深度轴 | 合成数据、语言简单 | **首选** |
| LogicNLI | E/C/N→T/F/U | ★★★★ | 三类标签、合成、FOL 基础 | 知名度低、无深度标注 | 备选 |
| RuleTaker | T/F | ★★★ | ProofWriter 前身、大规模 | 无 Unknown 类、仅 CWA | 不推荐 |
| LogiQA 2.0 NLI | 2-way | ★★ | 真实考试题 | 非规则推理、标签不匹配 | 不推荐 |
| CLUTRR | 关系推理 | ★ | 亲属关系推理 | 任务格式完全不同 | 不适用 |
| PrOntoQA | T/F | ★★ | 本体层级推理 | 无 Unknown、二分类 | 不推荐 |

## 6. 结论

**ProofWriter OWA D5 是最佳第二数据集**。理由：
1. 任务格式与 FOLIO 完全一致（premises → conclusion → T/F/U）
2. Logic-LLM 已建立 FOLIO + ProofWriter 的评测先例，审稿人容易接受
3. 合成 vs 人工标注的对比恰好验证方法在不同数据特性下的泛化性
4. 推理深度维度提供 FOLIO 无法提供的分析轴
5. 标签均衡（各33%）vs FOLIO 的不均衡（39% Unknown）可验证标签分布对不对称性的影响
6. HuggingFace 上有现成数据集（`smoorsmith/proofwriter`），适配工作量极小（~1天）
