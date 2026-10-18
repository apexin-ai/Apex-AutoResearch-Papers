# fix r15 sf4 fk persist

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_r15-sf4-fk-persist_20260523T062735_result.json`
- **Structured JSON:** [`84f78582813ceb4519d5.json`](../../sessions/84/84f78582813ceb4519d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已保存，JSON 格式正确。汇报结果：

### 产出确认

`/root/causal_style_decomp_judge/data/fk_length_control_results.json` 已生成，JSON 合法。

### 关键数值

| 指标 | 当前值 | 之前汇报值 | 备注 |
|------|--------|-----------|------|
| verbosity delta_fk_d | **0.50** | ≈0.50 | 一致 |
| coef_reduction_pct (passed_only) | **62.1%** | ≈59.3% | 略有差异，此次基于 passed_cf 子集(n=122)，之前可能基于全量(all_pairs=55.4%) |
| mediation sobel_p | **0.031** | <0.001 | **不一致**——passed_only 子集的 Sobel p=0.031，仍显著(p<0.05)，但不是 <0.001 |

注：`regression_all_pairs` 的 `coef_reduction_pct` 为 55.4%，更接近之前的 59.3%。两种切分的 reduction 均 >50%，结论方向一致。

### `passed_cf` 字段情况

`passed_cf` 在 `verified_verbosity.jsonl` 中**存在**，为 boolean 类型（`true`/`false`），表示 NLI 验证是否通过。脚本使用该字段筛选 passed_cf=true 的子集作为主分析（verbosity n=86, formality n=36）。

---
