# analyze eval xvla l2norm k05 spatial seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_xvla_l2norm_k05_spatial_seed42_v2_20260524T034308_result.json`
- **Structured JSON:** [`7b02b932e7ed2eb4f97d.json`](../../sessions/7b/7b02b932e7ed2eb4f97d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。汇总：

## 实验结果

| 指标 | 值 |
|------|-----|
| Overall SR | **58.8%** (294/500) |
| 95% Wilson CI | [54.4%, 63.0%] |
| vs Random k=0.5 Spatial | **-13.8pp** (58.8% vs 72.6%) |

**Per-task SR:**
| Task | SR | 描述 |
|------|-----|------|
| T0 | 92% | bowl between plate |
| T1 | 22% | bowl next ramekin |
| T2 | 88% | bowl table center |
| T3 | 72% | bowl cookie box |
| T4 | 84% | bowl top drawer |
| T5 | **0%** | bowl on ramekin |
| T6 | 82% | bowl next cookie box |
| T7 | 32% | bowl on stove |
| T8 | 72% | bowl next plate |
| T9 | 44% | bowl wooden cabinet |

**结论 = success**（验证了 hypothesis）：
- L2norm 在 X-VLA Spatial 上确实显著差于 random（-13.8pp），与 CV matrix 预测的 -13.1pp 高度一致
- 跨 suite 一致性确认：Object -27.6pp, Long -15.5pp, Spatial -13.8pp — L2norm 在 X-VLA 上全面劣于 random
- 58.8% 与 CV matrix 的 L2 Mean=58.9% 几乎完全吻合，说明 seed42 单次结果高度稳定

---
