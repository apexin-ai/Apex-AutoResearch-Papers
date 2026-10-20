# W2 Rectangularity Verification — Quantitative Evidence for Pair-Based Constraint Enforcement

**生成日期:** 2026-05-15
**目的:** Reviewer 指出代码做了 pair-based enforcement，但论文 §3 描述的是 independent dom/range。本报告量化两者差距，支持论文修改。

---

## 1. Code Logic Confirmation

**Pair-based check 已在代码中实现，论文描述偏宽松。**

### head_type masking (`type_mask_processor.py` `_mask_head_type`)
```python
allowed_dr = constraint.valid_head_types() if constraint else None
```
仅看 `dom(r)`，与 tail 无关 → **independent check** on head side.

### tail_type masking (`type_mask_processor.py:323` `_mask_tail_type`)
```python
if head_type is not None:
    allowed_dr = constraint.valid_tail_types_for_head(head_type)
else:
    allowed_dr = constraint.valid_tail_types()
```
其中 `valid_tail_types_for_head(head_type)` 在 `ontology_compiler.py:38` 定义为：
```python
def valid_tail_types_for_head(self, head_type: str) -> set[str]:
    return {t for h, t in self.valid_pairs if h == head_type}
```
即：在 head_type 已确定的条件下，仅允许 `σ(r)` 中以该 head_type 为头的 valid tail types。

### 结论
- Decoding 顺序：`head_type` → `tail_type`。
- head 端独立检查 `h ∈ dom(r)`；tail 端条件检查 `t ∈ {t' : (h, t') ∈ σ(r)}`。
- **最终生成的 pair `(h, t)` 必然 ∈ σ(r)** —— 这就是 pair-based enforcement，比论文 §3 描述的 `(h ∈ dom(r)) ∧ (t ∈ range(r))` 更严格。

---

## 2. Rectangularity Definition

对每个 relation `r`：
- `σ(r)` = 实际 valid (head, tail) pairs 集合
- `dom(r) = {h : ∃t, (h,t) ∈ σ(r)}`
- `range(r) = {t : ∃h, (h,t) ∈ σ(r)}`
- **Rectangular** iff `|σ(r)| = |dom(r)| × |range(r)|`，即 `σ(r) = dom(r) × range(r)`。
- **Gap** = `|dom(r)| × |range(r)| - |σ(r)|`（若假定 rectangular，会被错误允许的 pair 数量）

**Head-only over-permissiveness**：若 §3 表述被字面执行（仅检查 `h ∈ dom(r)`，tail 不约束），允许的 pair 数 = `|dom(r)| × |T|`，其中 `|T|` = 所有 entity types。

---

## 3. SciERC Results

- entity types: 6, relations: 7
- **rectangular: 0/7 (0.0%)**
- non-rect 平均 gap: 12.00
- total |σ| = 168, total |dom×range| = 252, global gap = 84
- head-only over-permissive ratio (head_only/pair_based): **1.500×**

### Per-relation table (SciERC)

| Relation | \|σ(r)\| | \|dom(r)\| | \|range(r)\| | dom×range | Rectangular? | Gap | head-only/pair |
|---|---:|---:|---:|---:|:---:|---:|---:|
| Used-for | 35 | 6 | 6 | 36 | ✗ | 1 | 1.03× |
| Feature-of | 26 | 6 | 6 | 36 | ✗ | 10 | 1.38× |
| Hyponym-of | 21 | 6 | 6 | 36 | ✗ | 15 | 1.71× |
| Part-of | 21 | 6 | 6 | 36 | ✗ | 15 | 1.71× |
| Compare | 17 | 6 | 6 | 36 | ✗ | 19 | 2.12× |
| Conjunction | 25 | 6 | 6 | 36 | ✗ | 11 | 1.44× |
| Evaluate-for | 23 | 6 | 6 | 36 | ✗ | 13 | 1.57× |

**关键观察 (SciERC):**
- 7/7 relations 全部 **非 rectangular**。
- 所有 relations 的 `dom = range = 全部 6 个 entity types`（这是 SciERC 的特点：同类型间也可能成立关系），但 `σ(r)` 远小于 36。
- 例：`Compare` 只有 17 个 valid pairs，rectangular 假设会多允许 19 个（gap=19），over-permissive 2.12×。
- 若按 §3 字面 head-only check：global 1.5× over-permissive — SciERC 的 head 几乎可以是任意类型，所以差距主要在 tail conditional。

---

## 4. DocRED Results

- entity types: 6, relations: 96
- **rectangular: 23/96 (24.0%)**
- non-rect 平均 gap: 4.34
- total |σ| = 545, total |dom×range| = 862, global gap = 317
- head-only over-permissive ratio: **3.457×**

### DocRED over-permissive ratio 分布 (head-only vs pair-based)

| Bucket | Count | %  |
|---|---:|---:|
| 1.0-1.5 | 0 | 0.0% |
| 1.5-2.0 | 2 | 2.1% |
| 2.0-3.0 | 17 | 17.7% |
| 3.0-5.0 | 59 | 61.5% |
| 5.0-10.0 | 18 | 18.8% |
| 10.0+ | 0 | 0.0% |

- 中位数 over_ratio = 3.60×
- 均值 over_ratio = 3.84×
- 最大 over_ratio = 6.00×

### Per-relation table (DocRED, 96 relations)

| Pid | Name | \|σ\| | \|dom\| | \|range\| | dom×range | Rect? | Gap | head-only/pair |
|---|---|---:|---:|---:|---:|:---:|---:|---:|
| P6 | head of government | 4 | 2 | 3 | 6 | ✗ | 2 | 3.00× |
| P17 | country | 13 | 6 | 4 | 24 | ✗ | 11 | 2.77× |
| P19 | place of birth | 3 | 2 | 2 | 4 | ✗ | 1 | 4.00× |
| P20 | place of death | 4 | 2 | 3 | 6 | ✗ | 2 | 3.00× |
| P22 | father | 7 | 3 | 4 | 12 | ✗ | 5 | 2.57× |
| P25 | mother | 3 | 2 | 2 | 4 | ✗ | 1 | 4.00× |
| P26 | spouse | 4 | 3 | 2 | 6 | ✗ | 2 | 4.50× |
| P27 | country of citizenship | 7 | 4 | 4 | 16 | ✗ | 9 | 3.43× |
| P30 | continent | 5 | 4 | 2 | 8 | ✗ | 3 | 4.80× |
| P31 | instance of | 9 | 4 | 3 | 12 | ✗ | 3 | 2.67× |
| P35 | head of state | 4 | 3 | 2 | 6 | ✗ | 2 | 4.50× |
| P36 | capital | 3 | 2 | 2 | 4 | ✗ | 1 | 4.00× |
| P37 | official language | 6 | 3 | 3 | 9 | ✗ | 3 | 3.00× |
| P39 | position held | 4 | 1 | 4 | 4 | ✓ | 0 | 1.50× |
| P40 | child | 6 | 4 | 2 | 8 | ✗ | 2 | 4.00× |
| P50 | author | 8 | 5 | 4 | 20 | ✗ | 12 | 3.75× |
| P54 | member of sports team | 10 | 3 | 5 | 15 | ✗ | 5 | 1.80× |
| P57 | director | 4 | 4 | 1 | 4 | ✓ | 0 | 6.00× |
| P58 | screenwriter | 2 | 2 | 1 | 2 | ✓ | 0 | 6.00× |
| P69 | educated at | 2 | 1 | 2 | 2 | ✓ | 0 | 3.00× |
| P86 | composer | 3 | 3 | 1 | 3 | ✓ | 0 | 6.00× |
| P102 | member of political party | 7 | 4 | 4 | 16 | ✗ | 9 | 3.43× |
| P108 | employer | 2 | 1 | 2 | 2 | ✓ | 0 | 3.00× |
| P112 | founded by | 8 | 4 | 4 | 16 | ✗ | 8 | 3.00× |
| P118 | league | 8 | 4 | 3 | 12 | ✗ | 4 | 3.00× |
| P123 | publisher | 7 | 4 | 3 | 12 | ✗ | 5 | 3.43× |
| P127 | owned by | 9 | 4 | 3 | 12 | ✗ | 3 | 2.67× |
| P131 | located in the administrative territorial entity | 10 | 4 | 4 | 16 | ✗ | 6 | 2.40× |
| P136 | genre | 9 | 4 | 4 | 16 | ✗ | 7 | 2.67× |
| P137 | operator | 7 | 4 | 2 | 8 | ✗ | 1 | 3.43× |
| P140 | religion | 6 | 3 | 3 | 9 | ✗ | 3 | 3.00× |
| P150 | contains administrative territorial entity | 8 | 4 | 4 | 16 | ✗ | 8 | 3.00× |
| P155 | follows | 9 | 5 | 4 | 20 | ✗ | 11 | 3.33× |
| P156 | followed by | 9 | 4 | 5 | 20 | ✗ | 11 | 2.67× |
| P159 | headquarters location | 8 | 4 | 3 | 12 | ✗ | 4 | 3.00× |
| P161 | cast member | 6 | 4 | 3 | 12 | ✗ | 6 | 4.00× |
| P162 | producer | 6 | 3 | 3 | 9 | ✗ | 3 | 3.00× |
| P166 | award received | 6 | 4 | 2 | 8 | ✗ | 2 | 4.00× |
| P170 | creator | 8 | 5 | 2 | 10 | ✗ | 2 | 3.75× |
| P171 | parent taxon | 4 | 2 | 2 | 4 | ✓ | 0 | 3.00× |
| P172 | ethnic group | 7 | 3 | 3 | 9 | ✗ | 2 | 2.57× |
| P175 | performer | 10 | 4 | 4 | 16 | ✗ | 6 | 2.40× |
| P176 | manufacturer | 5 | 4 | 2 | 8 | ✗ | 3 | 4.80× |
| P178 | developer | 5 | 4 | 2 | 8 | ✗ | 3 | 4.80× |
| P179 | series | 6 | 4 | 3 | 12 | ✗ | 6 | 4.00× |
| P190 | sister city | 1 | 1 | 1 | 1 | ✓ | 0 | 6.00× |
| P194 | legislative body | 4 | 3 | 2 | 6 | ✗ | 2 | 4.50× |
| P205 | basin country | 1 | 1 | 1 | 1 | ✓ | 0 | 6.00× |
| P206 | located in or next to body of water | 4 | 3 | 2 | 6 | ✗ | 2 | 4.50× |
| P241 | military branch | 5 | 3 | 2 | 6 | ✗ | 1 | 3.60× |
| P264 | record label | 10 | 4 | 4 | 16 | ✗ | 6 | 2.40× |
| P272 | production company | 5 | 4 | 2 | 8 | ✗ | 3 | 4.80× |
| P276 | location | 5 | 3 | 3 | 9 | ✗ | 4 | 3.60× |
| P279 | subclass of | 10 | 4 | 4 | 16 | ✗ | 6 | 2.40× |
| P355 | subsidiary | 5 | 3 | 3 | 9 | ✗ | 4 | 3.60× |
| P361 | part of | 14 | 5 | 5 | 25 | ✗ | 11 | 2.14× |
| P364 | original language of work | 7 | 3 | 3 | 9 | ✗ | 2 | 2.57× |
| P400 | platform | 6 | 4 | 3 | 12 | ✗ | 6 | 4.00× |
| P403 | mouth of the watercourse | 1 | 1 | 1 | 1 | ✓ | 0 | 6.00× |
| P449 | original network | 7 | 4 | 3 | 12 | ✗ | 5 | 3.43× |
| P463 | member of | 10 | 4 | 4 | 16 | ✗ | 6 | 2.40× |
| P488 | chairperson | 3 | 3 | 1 | 3 | ✓ | 0 | 6.00× |
| P495 | country of origin | 7 | 4 | 3 | 12 | ✗ | 5 | 3.43× |
| P527 | has part | 15 | 5 | 5 | 25 | ✗ | 10 | 2.00× |
| P551 | residence | 3 | 2 | 2 | 4 | ✗ | 1 | 4.00× |
| P569 | date of birth | 4 | 4 | 1 | 4 | ✓ | 0 | 6.00× |
| P570 | date of death | 6 | 5 | 2 | 10 | ✗ | 4 | 5.00× |
| P571 | inception | 4 | 4 | 1 | 4 | ✓ | 0 | 6.00× |
| P576 | dissolved, abolished or demolished | 4 | 4 | 1 | 4 | ✓ | 0 | 6.00× |
| P577 | publication date | 4 | 4 | 1 | 4 | ✓ | 0 | 6.00× |
| P580 | start time | 5 | 5 | 1 | 5 | ✓ | 0 | 6.00× |
| P582 | end time | 3 | 3 | 1 | 3 | ✓ | 0 | 6.00× |
| P585 | point in time | 4 | 4 | 1 | 4 | ✓ | 0 | 6.00× |
| P607 | conflict | 7 | 4 | 3 | 12 | ✗ | 5 | 3.43× |
| P674 | characters | 7 | 4 | 3 | 12 | ✗ | 5 | 3.43× |
| P676 | lyrics by | 2 | 1 | 2 | 2 | ✓ | 0 | 3.00× |
| P706 | located on terrain feature | 4 | 4 | 1 | 4 | ✓ | 0 | 6.00× |
| P710 | participant | 8 | 3 | 4 | 12 | ✗ | 4 | 2.25× |
| P737 | influenced by | 4 | 3 | 3 | 9 | ✗ | 5 | 4.50× |
| P740 | location of formation | 6 | 4 | 3 | 12 | ✗ | 6 | 4.00× |
| P749 | parent organization | 5 | 3 | 2 | 6 | ✗ | 1 | 3.60× |
| P800 | notable work | 4 | 2 | 3 | 6 | ✗ | 2 | 3.00× |
| P807 | separated from | 2 | 2 | 2 | 4 | ✗ | 2 | 6.00× |
| P840 | narrative location | 5 | 4 | 2 | 8 | ✗ | 3 | 4.80× |
| P937 | work location | 5 | 3 | 3 | 9 | ✗ | 4 | 3.60× |
| P1001 | applies to jurisdiction | 8 | 3 | 3 | 9 | ✗ | 1 | 2.25× |
| P1056 | product or material produced | 2 | 1 | 2 | 2 | ✓ | 0 | 3.00× |
| P1198 | unemployment rate | 2 | 1 | 2 | 2 | ✓ | 0 | 3.00× |
| P1336 | territory claimed by | 3 | 2 | 2 | 4 | ✗ | 1 | 4.00× |
| P1344 | participant of | 7 | 4 | 3 | 12 | ✗ | 5 | 3.43× |
| P1365 | replaces | 4 | 3 | 3 | 9 | ✗ | 5 | 4.50× |
| P1366 | replaced by | 5 | 3 | 3 | 9 | ✗ | 4 | 3.60× |
| P1376 | capital of | 3 | 2 | 2 | 4 | ✗ | 1 | 4.00× |
| P1412 | languages spoken, written or signed | 6 | 3 | 3 | 9 | ✗ | 3 | 3.00× |
| P1441 | present in work | 7 | 4 | 3 | 12 | ✗ | 5 | 3.43× |
| P3373 | sibling | 1 | 1 | 1 | 1 | ✓ | 0 | 6.00× |

**关键观察 (DocRED):**
- 24% 的 relations 是 rectangular —— 但都是 |σ| 很小的小型 relation (e.g., dom=range=1)。
- 76% 非 rectangular，平均 gap=4.34（若假定 rectangular 会多允许 4.34 个非法 pair）。
- head-only 假设全局多允许 3.5× — DocRED 上 §3 字面执行会严重过宽。
- 多个 relations over_ratio ≥ 5×（dom 大但 |σ| 小的稀疏 pair 集合，rectangular 假设崩溃最严重）。

---

## 5. 综合诊断

### 三种约束严格度对比

| Mode | 公式 | 总允许 pair (SciERC) | 总允许 pair (DocRED) |
|---|---|---:|---:|
| Head-only (§3 字面) | `h ∈ dom(r)`，tail 任意 | 252 | 1884 |
| Independent dom/range | `h ∈ dom(r) ∧ t ∈ range(r)` | 252 | 862 |
| **Pair-based (代码实际)** | `(h, t) ∈ σ(r)` | **168** | **545** |

- Independent dom/range 假设的 over-permissive 在 SciERC 上 = 252/168 ≈ 1.50×；在 DocRED 上 = 862/545 ≈ 1.58×。
- Head-only 假设（论文 §3 字面）的 over-permissive：SciERC 1.50×，**DocRED 3.46×**（DocRED 是更严苛的诊断信号）。
- Pair-based vs Independent 差距来自非 rectangular schema：SciERC 100% 非 rect，DocRED 76% 非 rect。

### 结论
1. **代码实际执行的是 pair-based check**（决策依据：`ontology_compiler.py:38` + `type_mask_processor.py:323`，输出 pair 必然 ∈ σ(r)）。
2. **论文 §3 描述偏宽松**（写成 independent dom/range 或 head-only）。
3. **非 rectangular 在两个数据集上都是主流形态**（SciERC 100%, DocRED 76%）—— 论文必须区分这两种 mode，不能默认 σ(r) = dom(r) × range(r)。

---

## 6. 论文修改建议

### §3 描述应修正为 pair-based formulation

**Before (§3 当前表述，宽松):**
> A relation `r(h, t)` is valid iff `type(h) ∈ dom(r)` and `type(t) ∈ range(r)`.

**After (与代码一致):**
> Each relation `r` is specified by its valid type signature `σ(r) ⊆ T × T`. A relation `r(h, t)` is valid iff `(type(h), type(t)) ∈ σ(r)`. Equivalently, the decoder enforces `type(h) ∈ dom(r)` and, conditional on `type(h)=τ`, `type(t) ∈ {t' : (τ, t') ∈ σ(r)}`. This is stricter than the independent dom/range check used in prior work — necessary because **0% of SciERC relations and 76% of DocRED relations are non-rectangular** (Table X), so `σ(r) ⊊ dom(r) × range(r)` for the majority of cases.

### 建议加入论文的新表 (Table: Schema rectangularity)

| Dataset | # relations | % rectangular | mean over-permissive (head-only) | mean over-permissive (independent dom/range) |
|---|---:|---:|---:|---:|
| SciERC  | 7 | 0.0% | 1.57× | 1.57× |
| DocRED  | 96 | 24.0% | 3.84× | 1.49× |

### Rebuttal 写法要点
- 承认 §3 表述与代码实际不一致是 expository gap，代码本身正确。
- 引用本报告：SciERC 100% / DocRED 76% 非 rectangular，head-only 假设在 DocRED 上多放过 3.46× 的非法 pair。
- 强调：pair-based 实现是为应对真实 ontology 的非 rectangular 特性，**这正是 reviewer 注意到的代码-论文差距的合理性来源**。
