# D069 Fix Status Report

Date: 2026-05-27

D069: Reviewer 系统性审查 — 5 项论文修复

## 逐项状态

### 1. 梯度图 v1→v2 替换
**Status: ✅ 已完成**

- `appendix.tex` Figure 3 (`gradient_analysis_v2_combined.pdf`): caption 明确标注 "(v2 codebase; seed 42, 200 batches at 50K checkpoint)"
- 无 "v2 pending" 文本残留（全文搜索确认）
- v1 图表（per_layer_combined, per-task table, dose_response）均已标注为 v1 数据，caption 注明 "retained for completeness; all main analyses use v2 data"

### 2. Abstract 弱化（"reduces" → "associated with"）
**Status: ✅ 已完成**

- Abstract 使用 "enabling gradient flow is **associated with** a reduction in Collision Avoidance Rate"（main.tex:27）
- 全文无因果性 "reduces" 残留（grep 确认 main.tex 无匹配）
- Body 一致使用 "associated with" 措辞

### 3. Ordinal 软化（去除 "not additive"）
**Status: ✅ 已完成**

- 全文无 "not additive" / "non-additive" / "interaction term" 残留
- 统一使用 "pattern consistent with an ordinal interaction" 软化表述
- results.tex:46 明确标注 "crossing zero and thus not individually significant at α=0.05 given the small sample"

### 4. Discussion 补充 TSR vs CAR 可反向移动
**Status: ✅ 已完成**

- discussion.tex:12 — "our results indicate that **safety and task success can respond differently** to auxiliary supervision, making independent safety evaluation essential"
- discussion.tex:14 — "auxiliary gradient flow can **degrade collision avoidance even when task success is maintained**"
- 两句合起来明确传达了 TSR/CAR 可反向移动的信息

### 5. Limitations 补充 λ₀ loss weight caveat
**Status: ✅ 已完成**

- appendix.tex:136 — "All auxiliary conditions use a fixed loss weight λ₀=0.01 with exponential decay; **we did not sweep this hyperparameter**, so the gradient flow effect may vary under different loss weight schedules."

## 禁止措辞检查

| 禁止措辞 | 状态 | 说明 |
|----------|------|------|
| crossover interaction | ✅ 未发现 | 文中使用 "apparent crossover"（描述 v1 历史）和 "crossover pattern"（appendix 记录 v1→v2 变化），但均非 "crossover interaction" 这一术语。当前发现用 "ordinal interaction" 描述。 |
| BN-mediated gradient calibration | ✅ 未发现 | 全文无匹配 |
| existence regularization | ✅ 未发现 | 全文无匹配 |
| 跨 v1-v2 梯度数值比较 | ❌ 仍存在 | appendix.tex:120 — "Detach action-loss gradient norms were only ~4% of Vanilla norms... In v2, this suppression disappears entirely (Detach/Vanilla ratio ≈ 1.29)... The gradient conflict rate also shifted from ~44% (v1) to ~46% (v2)" — 直接跨 codebase 比较梯度数值 |

## 总结

- **5 项修复**: 5/5 已完成
- **禁止措辞**: 3/4 清除，1 项残留（跨 v1-v2 梯度数值比较，位于 appendix Codebase Sensitivity 节）
- **需处理**: appendix.tex:120 的跨 v1-v2 梯度数值对比（~4% vs ≈1.29; ~44% vs ~46%）需改写，避免直接数值比较
