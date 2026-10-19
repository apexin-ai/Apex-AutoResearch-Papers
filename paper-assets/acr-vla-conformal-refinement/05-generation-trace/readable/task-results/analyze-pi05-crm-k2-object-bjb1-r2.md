# analyze pi05 crm k2 object bjb1 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05-crm-k2-object-bjb1-r2_20260526T142911_result.json`
- **Structured JSON:** [`80865190d42357399760.json`](../../sessions/80/80865190d42357399760.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，registry 已更新为 DONE/success。

**π0.5 CRM K=2 obs_only Object benchmark 三 seed 汇总：**

| Seed | SR | Successes | Δ vs VLA-only |
|------|-----|-----------|---------------|
| s42 | **89%** | 178/200 | -10.5pp |
| s43 | **87%** | 174/200 | -12.5pp |
| s44 | **88%** | 176/200 | -11.5pp |
| **Mean** | **88.0%** | 176/200 | **-11.5pp** |

三个 seed 高度一致（87-89%），标准差仅 1pp。always-on CRM 在近乎专家级 π0.5（~99.5% baseline）上产生约 -11.5pp 下降，符合预期——支持 Table 2 "模型能力依赖性分析"的论点。

最弱 task 跨 seed 一致为 ketchup（65%/65%），cream_cheese 次之（70-75%）。

---
