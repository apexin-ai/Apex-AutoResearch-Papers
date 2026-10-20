# ops check alpha value

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_alpha_value_20260518T042414_result.json`
- **Structured JSON:** [`d069698189be087107e5.json`](../../sessions/d0/d069698189be087107e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 确认结果

| 项目 | 值 |
|---|---|
| `train_deberta.py` 默认 alpha | **0.3** |
| plan_002 seed42 (run_plan_002.sh) | **alpha=0.3**（未传 `--alpha`，使用默认值）|
| plan_002 seed123 | **alpha=0.3**（无独立脚本，日志无 alpha 覆盖记录）|
| plan_002 seed456 | **alpha=0.3**（同上）|
| plan_014 ablation 中对 plan_002 的标注 | `"lambda_1.0"` 但 note 写了 `"plan_002 baseline (alpha=0.3 default)"` |

## 结论

**plan_002 所有 seed 实际使用的都是 alpha=0.3**，即 `L = L_persuasion + 0.3 * L_intent`。

论文写 λ=1.0 是错的。plan_014 的 ablation 脚本也确认了这一点：它把 plan_002 的结果标为 `"lambda_1.0"` 但 note 明确写 `"alpha=0.3 default"`，说明论文中的 λ=1.0 标签和实际 alpha=0.3 之间存在命名混乱。

**需要修正论文**：将论文中的 λ 值从 1.0 改为 0.3，或者明确说明 loss 公式中 intent loss 的权重是 0.3。plan_014 ablation 表格中 `lambda_1.0` 这一行也需要改标签为正确的值。

---
