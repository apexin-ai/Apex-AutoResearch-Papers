# ops bt discrepancy investigation

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bt_discrepancy_investigation_20260521T033133_result.json`
- **Structured JSON:** [`678628b03c9da6efc495.json`](../../sessions/67/678628b03c9da6efc495.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部排查完毕，结果如下：

---

### 问题 1：173 vs 176 comparisons

**原因：2 个 pair 有缺失 trial（共缺 3 个 comparison）**

| pair_id | trial1_choice | trial2_choice | 缺失数 | NLI |
|---------|--------------|--------------|--------|------|
| `mvp_0006` | null | null | 2 | 0.9947 |
| `mvp_0039` | null | B | 1 | 0.9855 |

88 pairs × 2 = 176 − 3 = **173** ✓

null 表示 judge 模型未返回有效 A/B 选择（拒绝回答或输出解析失败）。BT 代码 `load_data()` 中过滤条件 `if t1 in ("A", "B")` 正确跳过了这些无效 trial。**这是数据问题，不是代码 bug。**

### 问题 2：d=0.073 vs d=0.104

两个值都正确，来自不同计算：

| 指标 | ATE | SD(diff) | Cohen's d |
|------|-----|----------|-----------|
| **Raw**（未校正） | −0.1023 | 1.3982 | **0.073** |
| **Corrected**（RATE 校正后） | +0.1023 | 0.9831 | **0.104** |

- `d=0.073` = NLI≥0.90 子集的 **raw** paired Cohen's d（`|raw_ate| / sd_diff`）
- `d=0.104` = 同一子集经 double-rewrite bias correction 后的 **corrected** d

Power curve 用 raw d=0.073 是**保守且正确的选择**——power analysis 应基于未经校正的 effect size，因为 RATE 校正本身有假设依赖。

### 问题 3：173/63.0% 是否正确

**正确。** 109/173 formal wins = 63.0%。Trial 1: 56/86 (65.1%), Trial 2: 53/87 (60.9%)。BT 代码逻辑无误，无需修复。

---
