# analysis s2 pilot f1 investigation

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s2_pilot_f1_investigation_20260513T234025_result.json`
- **Structured JSON:** [`277b90edbd4377083e5b.json`](../../sessions/27/277b90edbd4377083e5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是诊断结果：

---

## 根因诊断

**relation_f1≈0 的根因是 base model 的 entity span 提取质量太差（entity F1=0.31），不是 S2 约束解码架构的问题。** relation 评估要求 head+tail+type 三元组完全匹配，entity 错误以平方级放大到 relation。

注：用户引用的"25 pred, 0 TP, 21 gold"实际来自 `violation_report_s2_dryrun.json`（10 样本），不是 pilot50。pilot50 实际 relation_f1=0.1008（13 TP/146 pred/112 gold），与 unconstrained baseline 的 0.0823 基本持平。

## 证据

**1. FP 错误分类（133 个 FP，pilot50）：**

| 类别 | 数量 | 占比 |
|------|------|------|
| head+tail 都不匹配 gold | 70 | 52.6% |
| head 对但 tail 错 | 30 | 22.6% |
| tail 对但 head 错 | 16 | 12.0% |
| head+tail 互换 | 7 | 5.3% |
| head+tail 对但 type 错 | 4 | 3.0% |
| 自引用 (head==tail) | 6 | 4.5% |

**2. 具体对比（dryrun 样本）：**

```
X96-1059_sent3:
  Gold: (morphological analyzer, Used-for, recognition and classification of proper names , numerical and temporal expressions)
  Pred: (morphological analyzer, Used-for, proper names)   ← tail 是 gold 的子串
  Pred: (morphological analyzer, Used-for, numerical and temporal expressions)  ← 拆分了

X96-1059_sent2:
  Gold: (approach, Used-for, Multi-lingual Evaluation Task -LRB- MET -RRB-)
  Pred: (Multi-lingual Evaluation Task, Conjunction, MET)  ← 把缩写拆成两个 entity 造 Conjunction

X96-1059_sent5:
  Gold: (Amorph, Used-for, NE items)
  Pred: (Amorph, Used-for, dictionary lookup)  ← 正确 head 但选错 tail

X96-1059_sent8:
  Pred: (NE item, Feature-of, NE item)  ← 自引用
```

**3. Entity 层面的质量指标：**
- text+type 匹配：57/197 pred（P=0.29）
- text-only 匹配（忽略 type）：99/197（50%）
- 42 个 entity text 对了但 type 标错 → Pass2 的 head_type/tail_type 也跟着错

**4. S2 vs unconstrained 同样本对比（dryrun 10 样本）：**
- S2: 0 TP, unconstrained: 1 TP — 基本一样差，不是 S2 引入的退化

## 修复建议

1. **核心问题（entity 质量）**：在 Pass1 entity prompt 中加 2-3 个 few-shot 示例（从 SciERC train 抽），示范正确的 span 边界（特别是含 `-LRB-`/`-RRB-` 的长 span）。当前是 zero-shot，7B 模型没能力猜对 span 边界

2. **快速修复**：
   - `build_relation_only_schema` 中加约束阻止 head==tail 的自引用关系（6 个无意义 FP）
   - 评估时做 entity text normalization：strip `-LRB-`/`-RRB-` 括号，统一子串匹配，提升 recall 上限

3. **结构性改进**：Pass2 prompt 中把 entity list 改为编号引用格式（`[E1] morphological analyzer (Method)`），让模型通过引用 ID 选 entity 而非重新生成文本，避免 span 抄写错误

---
