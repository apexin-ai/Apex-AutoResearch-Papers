# Pair-based σ(r) Enforcement 实现方案

**调研日期**：2026-05-15
**调研模式**：只读（w1_cf_fallback_scierc_pilot 在 cuda:0 上运行，未改任何服务器文件）

---

## 0. 关键发现：当前代码状态

### JSON Schema 生成顺序（ontology_compiler.py L158-164）

```
relation object 字段顺序: head → tail → type → head_type → tail_type
```

**relation `type` 是第3个字段**，在 head_type/tail_type 之前生成。因此生成 head_type 和 tail_type 时，relation type 已知。不需要 schema reorder。

### 当前约束执行矩阵

| 生成位置 | 当前实现 | pair-based? | 代码行号 |
|----------|---------|-------------|----------|
| `type` (relation) | 无语义约束（仅 grammar enum） | ❌ 无 | `__call__` L290-298 无此分支 |
| `head_type` | `valid_head_types()` = dom(σ(r)) 投影 | ❌ 独立 | `_mask_head_type` L321 |
| `tail_type` | `valid_tail_types_for_head(head_type)` | ✅ 已 pair-based | `_mask_tail_type` L359-360 |

### Over-permissive Gap 三个来源

1. **`_mask_head_type` 不用 tail 信息**（L321）：生成 head_type 时 tail_text 已可用（第2个字段），可从 entity registry 查到 tail 的 type，但代码仅用 `valid_head_types()` 做独立投影
2. **RELATION_TYPE 无语义约束**：生成 relation type 时 head/tail 的 text 已知（可查 registry），但没做 (h,t)∈σ(r) 过滤
3. **CF fallback 无视 pair 约束**（L330-339）：强制 registered type，即使该 type 与另一端构成 over-permissive pair

### 数据量化（rectangularity_analysis.json）

- **SciERC**: 84 over-permissive pairs / 252 cartesian = 33.3% OP rate。7 个 relation 全部非矩形
- **DocRED**: 290 OP pairs / 788 cartesian = 36.8%。impact_analysis 显示实际模型输出中 491 个 triplets 在 pair-based 下违规但 independent 下通过

---

## 1. 数据结构改动

### 1a. RelationConstraint — 新增 `_valid_pair_set` + `is_valid_pair()`

`ontology_compiler.py` 的 `RelationConstraint` 已有完备的 pair-based 查询方法（`valid_head_types_for_tail()` 存在但从未被调用）。需添加 O(1) pair 查询：

```python
# ontology_compiler.py L14-30
@dataclass
class RelationConstraint:
    relation_type: str
    valid_pairs: list[tuple[str, str]]
    _valid_pair_set: frozenset = field(init=False, repr=False)  # ← 新增

    def __post_init__(self):                                     # ← 新增
        self._valid_pair_set = frozenset(self.valid_pairs)       # ← 新增

    def is_valid_pair(self, head_type: str, tail_type: str) -> bool:  # ← 新增
        return (head_type, tail_type) in self._valid_pair_set         # ← 新增

    # 以下方法已存在，无需改动
    def valid_head_types(self) -> set[str]: ...
    def valid_tail_types(self) -> set[str]: ...
    def valid_tail_types_for_head(self, head_type: str) -> set[str]: ...
    def valid_head_types_for_tail(self, tail_type: str) -> set[str]: ...  # 存在但从未调用
```

**改动量**：+5 行

### 1b. ConstraintSpec — 新增 `valid_relations_for_pair()`

```python
# ontology_compiler.py ConstraintSpec 类
def valid_relations_for_pair(self, head_type: str, tail_type: str) -> set[str]:
    """返回允许 (head_type, tail_type) pair 的所有 relation types."""
    return {
        rtype for rtype, rc in self.relation_constraints.items()
        if rc.is_valid_pair(head_type, tail_type)
    }
```

**改动量**：+5 行

### 1c. GenerationState — 新增 `current_tail_type`

```python
# type_mask_processor.py L77-95
@dataclass
class GenerationState:
    position: FieldPosition = FieldPosition.UNKNOWN
    current_relation_type: Optional[str] = None
    current_head_type: Optional[str] = None
    current_tail_type: Optional[str] = None      # ← 新增
    current_head_text: Optional[str] = None
    current_tail_text: Optional[str] = None
    entity_registry: EntityRegistry = field(default_factory=EntityRegistry)
    in_entities_section: bool = True

    def reset(self):
        ...
        self.current_tail_type = None             # ← 新增
```

**改动量**：+3 行

### 1d. PositionDetector — 提取 tail_type 值

```python
# type_mask_processor.py PositionDetector 类
_RE_TAIL_TYPE_VAL = re.compile(r'"tail_type"\s*:\s*"([^"]+)"')  # ← 新增 regex

# detect() 方法中 partial_rel 处理区域新增：
m = cls._RE_TAIL_TYPE_VAL.search(partial_rel)
if m:
    state.current_tail_type = m.group(1)
```

**改动量**：+4 行

---

## 2. TypeConstraintProcessor 改动

### 2a. `_mask_head_type` — pair-based 增强（L310-343）

**Before（当前代码 L319-321）：**
```python
rel_type = self.state.current_relation_type
constraint = self.spec.get_constraint(rel_type) if rel_type else None
allowed_dr = constraint.valid_head_types() if constraint else None  # 独立 dom 投影
```

**After：**
```python
rel_type = self.state.current_relation_type
constraint = self.spec.get_constraint(rel_type) if rel_type else None

# Pair-based: 如果 tail entity 的 type 从 registry 已知, 用 σ(r)⁻¹[t]
tail_text = self.state.current_tail_text
tail_registry_type = (
    self.state.entity_registry.get_type(tail_text) if tail_text else None
)

if constraint is not None:
    if tail_registry_type is not None:
        allowed_dr = constraint.valid_head_types_for_tail(tail_registry_type)
    else:
        allowed_dr = constraint.valid_head_types()
else:
    allowed_dr = None
```

CF fallback 逻辑（L323-339）**不变**，仍强制 registered type。仅改 log message 增加 pair 信息。

**改动量**：+8 行（净增）

### 2b. `_mask_tail_type` — 增加 head_type registry fallback（L345-360）

当前代码用 `state.current_head_type`（已生成的值）。防御性增强：当 `head_type` 为 None 时用 registry 查：

```python
# L355 后新增
head_type = self.state.current_head_type
if head_type is None and self.state.current_head_text:
    head_type = self.state.entity_registry.get_type(self.state.current_head_text)
```

**改动量**：+3 行

### 2c. 新增 `_mask_relation_type`

在 `RELATION_TYPE` 位置，基于已知的 head/tail entity types 过滤不合法的 relation types。

```python
def _mask_relation_type(self, logits: torch.FloatTensor) -> torch.FloatTensor:
    """Mask relation types inconsistent with head/tail entity types from registry."""
    head_text = self.state.current_head_text
    tail_text = self.state.current_tail_text

    head_type = self.state.entity_registry.get_type(head_text) if head_text else None
    tail_type = self.state.entity_registry.get_type(tail_text) if tail_text else None

    if head_type is None and tail_type is None:
        return logits

    allowed_relations = set()
    for rtype in self.spec.relation_types:
        constraint = self.spec.get_constraint(rtype)
        if constraint is None:
            allowed_relations.add(rtype)
            continue
        if head_type is not None and tail_type is not None:
            if constraint.is_valid_pair(head_type, tail_type):
                allowed_relations.add(rtype)
        elif head_type is not None:
            if head_type in constraint.valid_head_types():
                allowed_relations.add(rtype)
        else:
            if tail_type in constraint.valid_tail_types():
                allowed_relations.add(rtype)

    if not allowed_relations:
        return logits

    return self._apply_relation_type_mask(logits, allowed_relations)
```

**改动量**：+25 行

### 2d. Relation type masking 基础设施

```python
# __init__ 新增
self._rel_type_first_token, self._all_rel_first_tokens = self._build_rel_first_token_map()

def _build_rel_first_token_map(self) -> tuple[dict[str, int], set[int]]:
    """Build relation_type -> first_token_id mapping."""
    rel_first_token: dict[str, int] = {}
    all_first_tokens: set[int] = set()
    for rtype in self.spec.relation_types:
        token_ids = self.spec.relation_type_token_ids.get(rtype)
        if token_ids is None:
            token_ids = self.tokenizer.encode(rtype, add_special_tokens=False)
        first_id = token_ids[0]
        rel_first_token[rtype] = first_id
        all_first_tokens.add(first_id)
    return rel_first_token, all_first_tokens

def _apply_relation_type_mask(
    self, logits: torch.FloatTensor, allowed_relations: set[str]
) -> torch.FloatTensor:
    """类似 _apply_type_mask，但作用于 relation type first tokens."""
    TypeConstraintProcessor.total_mask_calls += 1
    if not allowed_relations:
        return logits
    disallowed = [
        tid for rtype, tid in self._rel_type_first_token.items()
        if rtype not in allowed_relations
    ]
    if not disallowed:
        return logits
    any_allowed_valid = any(
        logits[self._rel_type_first_token[r]].item() > self._GRAMMAR_MASK_THRESHOLD
        for r in allowed_relations if r in self._rel_type_first_token
    )
    if not any_allowed_valid:
        self._grammar_first_skip_count += 1
        TypeConstraintProcessor.grammar_first_fallback_count += 1
        return logits
    logits[disallowed] = float("-inf")
    return logits
```

**改动量**：+35 行

**⚠️ DocRED first-token 冲突问题**：DocRED relation types 是 P-code（P17, P50, P155...），所有都以 "P" 开头 → first token 全部相同 → first-token masking 无法区分。

**解决方案**：
- **SciERC**：relation names 各不相同（Used-for, Feature-of, ...），first tokens 唯一 → 直接启用
- **DocRED**：`_mask_relation_type` 功能暂不启用（或需要用 human-readable relation names / multi-token trie）

在 `__init__` 中检测唯一性并设 flag：
```python
self._rel_masking_enabled = len(self._rel_type_first_token) == len(self._all_rel_first_tokens)
```

### 2e. `__call__` 方法更新（L290-298）

```python
# Before:
if position == FieldPosition.ENTITY_TYPE:
    scores[batch_idx] = self._mask_entity_type(scores[batch_idx])
elif position == FieldPosition.RELATION_HEAD_TYPE:
    scores[batch_idx] = self._mask_head_type(scores[batch_idx])
elif position == FieldPosition.RELATION_TAIL_TYPE:
    scores[batch_idx] = self._mask_tail_type(scores[batch_idx])

# After:
if position == FieldPosition.ENTITY_TYPE:
    scores[batch_idx] = self._mask_entity_type(scores[batch_idx])
elif position == FieldPosition.RELATION_TYPE:                        # ← 新增
    if self._rel_masking_enabled:                                     # ← 新增
        scores[batch_idx] = self._mask_relation_type(scores[batch_idx])
elif position == FieldPosition.RELATION_HEAD_TYPE:
    scores[batch_idx] = self._mask_head_type(scores[batch_idx])
elif position == FieldPosition.RELATION_TAIL_TYPE:
    scores[batch_idx] = self._mask_tail_type(scores[batch_idx])
```

**改动量**：+3 行

---

## 3. CF Fallback + Pair-based 交互

### 3a. 完整执行流

```
生成: head(text) → tail(text) → type(relation) → head_type → tail_type
                                     ↑                ↑            ↑
                                 _mask_relation   pair-based    pair-based
                                 (if enabled)     head mask     (已有)
```

### 3b. CF fallback 行为矩阵

**核心原则不变**：CF 一致性 > D/R pair 约束（与 W1 设计一致）

| # | head registry | tail registry | pair valid? | 行为 |
|---|:---:|:---:|:---:|------|
| 1 | known=A | known=B | (A,B)∈σ(r) | force A, force B |
| 2 | known=A | known=B | (A,B)∉σ(r) | **CF wins**: force A, force B, log pair_cf_conflict |
| 3 | known=A | unknown | — | force A; mask tail → σ(r)\[A\] |
| 4 | unknown | known=B | — | mask head → σ(r)⁻¹\[B\]; force B |
| 5 | unknown | unknown | — | mask head → dom(σ(r)); mask tail → σ(r)\[head_type\] |

**场景2 详解**：entity registry 说 head=A, tail=B，但 (A,B)∉σ(r)。改变 entity type 会引入 CF violation（同一 entity 在不同 relation 中 type 不同），比 D/R violation 更严重 → CF wins。

### 3c. 新增统计指标

```python
# 类级别
pair_cf_conflict_count = 0  # CF 与 pair 约束冲突次数（场景2）

# get_fallback_stats() 中新增
"pair_cf_conflict_count": cls.pair_cf_conflict_count,
"pair_cf_conflict_rate": cls.pair_cf_conflict_count / total,
```

### 3d. Grammar-first fallback 交互

逻辑不变。pair-based 约束更紧 → grammar-first fallback 可能触发更频繁。需要在实验中监控 `grammar_first_fallback_rate` 变化。

---

## 4. 边界情况

### 4a. head_type 生成时 tail 不在 registry

- tail_text 已知（JSON 第2个字段）但 entity registry 查不到（entity 未在 entities section 中出现）
- **处理**：回退到 `valid_head_types()` 独立投影（与当前行为一致）
- **预期频率**：低。entities section 在 relations 之前生成，正常情况所有 entity 都在 registry 中

### 4b. tail_type 生成时 head_type 未解析

- state.current_head_type 由 `_RE_HEAD_TYPE_VAL` regex 从完整的 `"head_type": "X"` 中提取
- 正常流程中 head_type 在 tail_type 之前完全生成，所以 current_head_type 应已就绪
- **防御措施**：新增 registry fallback（2b 改动）

### 4c. relation type masking 后无合法 relation

- 如果 entity registry 中 (head_type, tail_type) 不在任何 relation 的 σ(r) 中 → allowed_relations 为空
- **处理**：返回 logits 不变，让 grammar 层决定 → 模型可能选择"最不坏"的 relation

### 4d. CF fallback 导致 head_type 与 pair-based allowed set 冲突

- 场景：tail_type=B（from registry），pair-based 允许 head={X,Y}，但 head entity 在 registry 中是 Z（不在 {X,Y} 中）
- **处理**：CF wins，force Z。log pair_cf_conflict。这与 2c 中场景2 一致
- 这意味着 pair-based enforcement 只在 entity 不在 registry 时有效（作为"free type"的约束收紧）

---

## 5. Dry-run 验证 Test Cases

### 5a. SciERC — 按 relation 列出 over-permissive pairs

#### Compare（19 OPs, valid=17/36, OP rate=52.8%）

应被 pair-based 拒绝的 (head, tail) pairs：
```
(Material, Generic)    (Material, Method)     (Material, Metric)
(Method, Material)     (Method, Metric)       (Method, OtherScientificTerm)   (Method, Task)
(Metric, Material)     (Metric, Method)       (Metric, OtherScientificTerm)   (Metric, Task)
(OtherScientificTerm, Method)   (OtherScientificTerm, Metric)   (OtherScientificTerm, Task)
(Task, Generic)        (Task, Material)       (Task, Method)    (Task, Metric)    (Task, OtherScientificTerm)
```

验证示例：
```python
rc = spec.get_constraint("Compare")
# valid_head_types() = {all 6} (independent 允许全部)
# valid_head_types_for_tail("Generic") = 应排除 Material, Method, Metric
assert "Material" not in rc.valid_head_types_for_tail("Generic")
assert "Task" in rc.valid_head_types_for_tail("Task")  # (Task,Task) 是 valid pair
```

#### Hyponym-of（15 OPs, valid=21/36, OP rate=41.7%）
```
(Generic, Material)    (Generic, Metric)
(Material, Method)     (Material, Metric)
(Method, Material)     (Method, Metric)
(Metric, Generic)      (Metric, Material)     (Metric, Method)   (Metric, Task)
(OtherScientificTerm, Metric)
(Task, Material)       (Task, Method)         (Task, Metric)     (Task, OtherScientificTerm)
```

#### Part-of（15 OPs, valid=21/36）
（详见 rectangularity_analysis.json）

#### Evaluate-for（13 OPs, valid=23/36）

#### Conjunction（11 OPs, valid=25/36）

#### Feature-of（10 OPs, valid=26/36）

#### Used-for（1 OP, valid=35/36, OP rate=2.8%）
```
(Metric, Metric)  ← 唯一 over-permissive pair
```

**SciERC 总计**：84 over-permissive pairs 应被 pair-based enforcement 拒绝。

### 5b. DocRED Top-10 Non-rectangular Relations

| Relation | Code | Valid | Cartesian | OP count | OP rate |
|----------|------|-------|-----------|----------|---------|
| author | P50 | 8 | 20 | 12 | 60.0% |
| follows | P155 | 9 | 20 | 11 | 55.0% |
| followed by | P156 | 9 | 20 | 11 | 55.0% |
| country | P17 | 13 | 24 | 11 | 45.8% |
| part of | P361 | 14 | 25 | 11 | 44.0% |
| has part | P527 | 15 | 25 | 10 | 40.0% |
| member of political party | P102 | 7 | 16 | 9 | 56.3% |
| country of citizenship | P27 | 7 | 16 | 9 | 56.3% |
| founded by | P112 | 8 | 16 | 8 | 50.0% |
| contains admin. entity | P150 | 8 | 16 | 8 | 50.0% |

#### P50 (author) 具体 OP pairs：
Valid: {(MISC,PER), (PER,PER), (LOC,PER), (ORG,PER), (TIME,PER), (TIME,MISC), (TIME,TIME), (MISC,MISC)}
Over-permissive:
```
(LOC, LOC)  (LOC, MISC)  (LOC, ORG)
(ORG, LOC)  (ORG, MISC)  (ORG, ORG)
(PER, LOC)  (PER, MISC)  (PER, ORG)
(TIME, LOC) (TIME, MISC) (TIME, ORG)
```

验证：P50 的 range 几乎全是 PER，只有 TIME→MISC, TIME→TIME, MISC→MISC 例外。pair-based 可以有效排除 LOC/ORG/PER 作为 tail 的大多数组合。

### 5c. 端到端验证脚本框架

```python
def test_pair_based_head_mask():
    """pair-based 收紧 head_type 约束."""
    spec = load_spec("ontology_constraints.json")

    # Compare + tail=Generic: independent 允许 6 types, pair-based 应只允许子集
    rc = spec.get_constraint("Compare")
    independent = rc.valid_head_types()       # {all 6}
    pair_based = rc.valid_head_types_for_tail("Generic")  # 子集
    assert pair_based < independent  # strict subset

    # 具体 OP 应被排除
    for h, t in [("Material","Generic"), ("Method","Task"), ("Metric","Method")]:
        assert not rc.is_valid_pair(h, t)

def test_relation_type_mask():
    """验证 _mask_relation_type 过滤逻辑."""
    spec = load_spec("ontology_constraints.json")
    # (Metric, Metric) 是 Used-for 的唯一 OP
    # → valid_relations_for_pair("Metric","Metric") 不应包含 Used-for
    valid_rels = spec.valid_relations_for_pair("Metric", "Metric")
    assert "Used-for" not in valid_rels
    # 但其他 6 个 relation 应该都允许（因为它们都有 (Metric,Metric) 作为 valid pair）

def test_cf_vs_pair_conflict():
    """CF 优先级高于 pair constraint."""
    # 模拟: entity registry {"attention": "Method"}, rel=Compare, tail_registry_type=Generic
    # (Method, Generic) ∉ σ(Compare) → pair 不允许
    # 但 CF fallback 应 force "Method"
    rc = spec.get_constraint("Compare")
    assert not rc.is_valid_pair("Method", "Generic")  # pair 不允许
    # _mask_head_type 应返回 {Method}（CF wins）
```

---

## 6. 改动清单汇总

| 文件 | 改动 | 行数 |
|------|------|------|
| `compiler/ontology_compiler.py` | `RelationConstraint`: `__post_init__`, `_valid_pair_set`, `is_valid_pair()` | +5 |
| `compiler/ontology_compiler.py` | `ConstraintSpec`: `valid_relations_for_pair()` | +5 |
| `compiler/type_mask_processor.py` | `GenerationState`: `current_tail_type` + reset | +3 |
| `compiler/type_mask_processor.py` | `PositionDetector`: `_RE_TAIL_TYPE_VAL` + 提取逻辑 | +4 |
| `compiler/type_mask_processor.py` | `_mask_head_type`: pair-based tail registry 查询 | +8 |
| `compiler/type_mask_processor.py` | `_mask_tail_type`: head_type registry fallback | +3 |
| `compiler/type_mask_processor.py` | 新增 `_mask_relation_type` | +25 |
| `compiler/type_mask_processor.py` | 新增 `_build_rel_first_token_map` + `_apply_relation_type_mask` | +35 |
| `compiler/type_mask_processor.py` | `__call__`: RELATION_TYPE 分支 + `_rel_masking_enabled` | +5 |
| `compiler/type_mask_processor.py` | `pair_cf_conflict_count` 统计 | +5 |
| **总计** | | **~98 行** |

---

## 7. 风险评估

### 低风险（直接实施）
- `RelationConstraint.is_valid_pair()` / `_valid_pair_set`：纯查询，不改现有逻辑
- `GenerationState.current_tail_type` / PositionDetector regex：只读追加
- `_mask_tail_type` registry fallback：防御性加固

### 中风险（需测试验证）
- **`_mask_head_type` pair-based**：约束空间收紧，可能增加 grammar-first fallback 频率。需对比 W1 pilot 的 fallback rate
- **`_mask_relation_type`**：新功能。DocRED P-code first-token 不唯一 → 需设 `_rel_masking_enabled` flag 或对 DocRED 禁用

### 需监控的指标
- `grammar_first_fallback_rate`：pair-based 前后对比
- `cf_registry_fallback_rate`：pair-based 前后对比
- `pair_cf_conflict_rate`：新增指标，预期低频
- 生成质量（F1）：pair-based 是否因过度约束导致质量下降

---

## 8. 实施优先级

| 优先级 | 改动 | 收益 | 风险 | 依赖 |
|--------|------|------|------|------|
| **P0** | `_mask_head_type` pair-based | 最高（直接消除 entity registry 可用时的 OP head_type） | 低 | 1d (tail_type 提取) |
| **P1** | `RelationConstraint.is_valid_pair` + `_valid_pair_set` | 基础设施 | 极低 | 无 |
| **P2** | `_mask_relation_type` (SciERC only) | 中等（relation 选择层面过滤） | 中 | P1 + rel first-token map |
| **P3** | `_mask_tail_type` registry fallback | 低（防御性） | 极低 | 无 |

**建议**：W1 CF fallback pilot 完成后，先实施 P0+P1，评估 fallback rate 变化，再决定是否需要 P2。
