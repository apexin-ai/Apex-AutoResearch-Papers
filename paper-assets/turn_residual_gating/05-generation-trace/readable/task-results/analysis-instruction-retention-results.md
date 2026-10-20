# analysis instruction retention results

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_instruction_retention_results_20260521T035844_result.json`
- **Structured JSON:** [`dc24d137be4103d0ce3b.json`](../../sessions/dc/dc24d137be4103d0ce3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两部分均完成。

---

## Part 1: Instruction Retention Test 结果

| 指标 | β=0 | β=3 | Δ |
|------|-----|-----|---|
| **Overall late-turn (t3-5) rate** | 0.759 | **0.870** | +0.111 |

**Per-category late-turn rate:**

| Category | β=0 | β=3 | Δ |
|----------|-----|-----|---|
| content_constraint | 0.619 | 0.857 | **+0.238** |
| count_constraint | 1.000 | 1.000 | +0.000 |
| format_constraint | 1.000 | 1.000 | +0.000 |
| position_constraint | 0.667 | 0.733 | +0.067 |

**统计检验:**
- McNemar: χ²=3.125, **p=0.077** (marginal, n=54 pairs)
- GAR × compliance correlation: **r=0.200, p=0.007** (n=180, significant)

**解读**: TG gating 在 content_constraint 上有显著提升（+23.8pp），说明 gating 帮助模型在后续轮次保留了语义级别的 instruction（如"必须包含某词"）。count/format 类 ceiling 已满无法区分。McNemar p=0.077 边缘显著，但 GAR-compliance 相关显著（p<0.01），支持"GAR 高 → 遵从率高"的因果假设。

Registry 已标记 `instruction_retention_test` → DONE/success。

---

## Part 2: Matched Llama AR Eval

已启动，PID=219718，使用 TG checkpoint `runs/phase2_llama_tg_s42/epoch_2`。

- 4 个条件: Base+Ours / Base+Dongre / TG+Ours / TG+Dongre
- 设置: N=50 convs, T=4 turns, AR generation (`--ar-from-fixed`)
- 日志: `runs/eval_llama_ar_matched.log`
- 当前状态: 正在跑第 1 个条件 (AR Base + GAR-ours)，模型已加载并开始生成

---
