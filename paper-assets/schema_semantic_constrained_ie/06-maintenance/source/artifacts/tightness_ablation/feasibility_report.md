# Tightness Ablation 可行性评估报告

## 1. Schema 文件位置和格式

| 数据集 | Schema 文件 | 格式 |
|--------|------------|------|
| SciERC | `/root/schema_semantic_constrained_ie/ontology_constraints.json` | JSON |
| DocRED | `/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json` | JSON |

两者共享同一数据结构：
```json
{
  "entity_types": ["PER", "ORG", "LOC", "TIME", "NUM", "MISC"],
  "relation_types": {"P6": "head of government", ...},
  "relation_constraints": {
    "P6": {
      "valid_pairs": [["PER", "LOC"], ["PER", "ORG"], ...],
      "stats": { "total": N, "pair_distribution": {...} }
    }
  }
}
```

Schema 由训练数据统计生成，脚本：
- SciERC: `analyze_ontology.py` (从 `data/processed_data/train.json` 统计)
- DocRED: `analyze_ontology_docred.py` (从 `data/docred/train_annotated.json` 统计)

## 2. 当前 Tightness 数值

### SciERC (6 entity types, 7 relations, total_possible_pairs = 36)

| Relation | Valid Pairs | τ |
|----------|------------|---|
| Used-for | 35/36 | 0.028 |
| Feature-of | 26/36 | 0.278 |
| Hyponym-of | 21/36 | 0.417 |
| Part-of | 21/36 | 0.417 |
| Compare | 17/36 | 0.528 |
| Conjunction | 25/36 | 0.306 |
| Evaluate-for | 23/36 | 0.361 |
| **Average** | **24/36** | **0.333** |

### DocRED (6 entity types, 96 relations, total_possible_pairs = 36)

| Valid Pairs | # Relations |
|------------|-------------|
| 1 | 4 |
| 2 | 7 |
| 3 | 9 |
| 4 | 18 |
| 5 | 12 |
| 6 | 11 |
| 7 | 13 |
| 8 | 8 |
| 9 | 5 |
| 10 | 6 |
| 13-15 | 3 |

- τ range: 0.583 ~ 0.972, **avg = 0.842**
- DocRED 大多数 relation 只有 3-7 个 valid pairs（96 个 relation 中 63 个 ≤7），约束非常紧

**关键观察**: SciERC 和 DocRED 的 entity type 数量相同（都是 6），total_possible_pairs 也相同（36）。Tightness 差异完全来自 valid_pairs 数量的不同——SciERC 每个 relation 平均 24 个 valid pairs，DocRED 平均仅 5.68 个。

## 3. Schema → Grammar 编译链路

```
ontology_constraints.json
    ↓
OntologyCompiler (compiler/ontology_compiler.py)
    ├── compile_ebnf() → EBNF grammar string
    ├── compile_json_schema() → JSON Schema
    ├── compile_xgrammar(tokenizer) → xgrammar.CompiledGrammar  [Layer 1: 结构约束]
    └── compile_type_constraints(tokenizer) → entity_type_first_token mapping
                                                    ↓
                                    TypeConstraintProcessor  [Layer 2: 语义约束]
                                    (compiler/type_mask_processor.py)
```

**完全自动编译**。修改 schema JSON 后，调 `OntologyCompiler(new_path).build_processor(tokenizer)` 即可获得新的 LogitsProcessor stack。

编译是 in-memory 操作，耗时可忽略（< 1 秒）。XGrammar 编译是 tokenizer-dependent 但非常快。

推理脚本通过 `--constraints_path` 参数接收 schema 路径，无需修改推理代码。

## 4. 参数化修改可行性

### 方案设计

DocRED 是理想的 ablation 目标（96 relations，τ 分布广），策略：

| Level | 策略 | 预期 τ_avg |
|-------|------|-----------|
| L0: Unconstrained | 所有 relation 允许所有 36 pairs | 0.000 |
| L1: Loose | 每个 relation 的 valid pairs × 2（上限 36） | ~0.5 |
| L2: Original | 使用原始 schema | 0.842 |
| L3: Tight | 每个 relation 只保留 top-1 频率最高的 pair | ~0.972 |
| L4: Single-type | 每个 relation 只保留出现次数最多的 1 个 pair | 0.972 |

**实现路径**：
```python
def generate_tightness_schema(original_schema, level):
    """修改 valid_pairs 生成不同 tightness 级别的 schema"""
    schema = deepcopy(original_schema)
    for rel, constraint in schema["relation_constraints"].items():
        pairs = constraint["valid_pairs"]
        if level == "unconstrained":
            # 生成所有 entity_type × entity_type
            constraint["valid_pairs"] = all_pairs
        elif level == "loose":
            # 扩展：添加随机 pairs 直到 2×原始数量
            constraint["valid_pairs"] = expand_pairs(pairs, factor=2)
        elif level == "tight":
            # 只保留频率最高的 top-K pairs
            constraint["valid_pairs"] = top_k_pairs(pairs, stats, k=2)
    return schema
```

脚本开发量：~50 行 Python，**约 1 小时**。

### 关键设计约束

- **放松约束（L0/L1）**：不影响 recall，只可能降低 precision（允许了本不合法的 type pairs）
- **收紧约束（L3/L4）**：会降低 recall，因为合法 triples 可能被约束掉。需要计算被过滤掉的 gold triples 比例作为 "constraint-induced recall loss"
- `stats.pair_distribution` 字段已有每个 pair 的训练集频率，可直接用于排序

## 5. 完整实验链路估算

### 单次推理时间（基于现有实验数据）

| 数据集 | 样本数 | 平均推理时间/样本 | 总时间 |
|--------|--------|------------------|--------|
| DocRED dev | 998 | 20.39s | 5.65 hours |
| SciERC test | 551 | 6.76s | 1.03 hours |

### 每个 Tightness Level 的工时

| 步骤 | 时间 |
|------|------|
| 生成 modified schema | < 1 min（脚本自动化） |
| Grammar 编译 | < 1 sec（in-memory） |
| DocRED 推理 | ~5.7 hours |
| SciERC 推理 | ~1.0 hour |
| 评估（violation check + F1） | ~10 min |
| **单级别小计** | **~6.9 hours**（仅 DocRED）/ **~7.9 hours**（含 SciERC） |

### 总工时

| 方案 | Levels | GPU 时间 | 脚本开发 | 总计 |
|------|--------|----------|----------|------|
| 最小方案（3 levels） | L0 + L2 + L4 | ~21 hours | 2 hours | ~23 hours |
| 推荐方案（5 levels） | L0-L4 全部 | ~35 hours | 2 hours | ~37 hours |
| 含 SciERC 的完整方案 | 5 levels × 2 datasets | ~40 hours | 3 hours | ~43 hours |

注：多 level 推理可串行运行（同一 GPU），无需额外资源。

## 6. 风险分析

### 科学合理性风险

**中等风险**。审稿人可能质疑：

1. **"人为构造 schema 不反映真实 ontology"** — 这是最大的质疑点。真实 IE 场景中 schema 由领域专家定义，人为放宽/收紧缺乏语义依据。
   - 缓解：强调实验目的是隔离 tightness 作为控制变量，不是模拟真实场景
   - 缓解：放宽方向（L0/L1）可解释为"如果领域知识不完整时会怎样"

2. **收紧方向的 confound** — 收紧约束同时降低了 recall ceiling，F1 下降可能不是"约束更紧效果更好"而是"recall 被人为截断"
   - 需要同时报告 precision 和 recall 分离指标
   - 需要报告 "constraint-induced recall loss"（多少 gold triples 被过滤）

3. **样本量** — DocRED dev 仅 998 samples，极端 tightness levels 可能导致高方差

### 替代方案

| 方案 | 优势 | 劣势 |
|------|------|------|
| **A. 多数据集自然对比（推荐）** | 天然 tightness 差异，无"人为构造"质疑 | 数据集间差异不只是 tightness（domain, size, complexity） |
| **B. DocRED 内部 relation 分组** | 控制数据集，按 τ 分组分析 | 不同 relation 难度本身不同，confound |
| **C. 人为修改 schema（本方案）** | 唯一真正控制自变量的方案 | 人为性质疑，recall ceiling confound |

### 方案 A 详情：多数据集对比

| 数据集 | Entity Types | Relations | 预期 τ_avg | 状态 |
|--------|-------------|-----------|-----------|------|
| SciERC | 6 | 7 | 0.333 (已验证) | 已有实验 |
| DocRED | 6 | 96 | 0.842 (已验证) | 已有实验 |
| TACRED | 17 | 42 | 待计算 | 需新增 |
| ACE05 | 7 | 18 | 待计算 | 需新增 |

**优势**：SciERC (τ=0.333) 和 DocRED (τ=0.842) 的对比已经覆盖了 tightness 的两个极端。如果论文已有这两个数据集的实验结果，这就是天然的 tightness ablation。

### 方案 B 详情：DocRED 内部分组分析

DocRED 96 relations 的 τ 分布从 0.583 到 0.972，可按 τ 分三组：
- Low-τ group (τ < 0.75): ~13 relations, 8+ valid pairs
- Mid-τ group (0.75 ≤ τ < 0.90): ~36 relations, 4-8 valid pairs  
- High-τ group (τ ≥ 0.90): ~47 relations, 1-3 valid pairs

对每组分别统计 violation rate 和 F1 差异（constrained vs unconstrained）。**零额外推理成本**，只需对现有结果做 post-hoc 分析。

## 7. 结论

### 推荐：不推荐做完整 tightness ablation 实验

**理由**：

1. **投入产出比低**：~37 GPU hours + 开发时间，收益是一个 confound 较多的消融表
2. **科学合理性存疑**：人为修改 schema 的实验设计容易被审稿人二次质疑
3. **已有更好的证据**：
   - SciERC (τ=0.333) vs DocRED (τ=0.842) 的跨数据集对比已经是天然的 tightness contrast
   - 论文中 grammar-first fallback 在 DocRED（tight）上频繁触发而在 SciERC（loose）上不触发，本身就是 tightness 影响效果的直接证据

### 推荐替代动作（零额外 GPU 成本）

1. **DocRED 内部 relation 分组分析（方案 B）**：按 τ 将 96 个 relation 分 3 组，对现有 outputs 做 post-hoc 分析，报告每组的 violation rate 下降和 F1 变化。开发量 ~2 小时，零推理成本。

2. **量化 tightness 的论文叙述**：在论文中明确报告 τ_avg(SciERC)=0.333 vs τ_avg(DocRED)=0.842，将跨数据集结果差异解释为 tightness 效应。

3. **如果审稿人明确要求 controlled ablation**：再执行方案 C，此时有审稿人要求作为 justification，人为构造的质疑不成立。
