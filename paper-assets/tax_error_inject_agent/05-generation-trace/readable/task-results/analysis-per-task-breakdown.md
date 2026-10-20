# analysis per task breakdown

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_per-task-breakdown_20260515T020457_result.json`
- **Structured JSON:** [`0dbffde3a1609c53d74a.json`](../../sessions/0d/0dbffde3a1609c53d74a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册为 `art_20260515_7436f8`。核心发现：

**Dose-response 关键结果：**
- TaxEI-10% 与 vanilla 完全一致（每个 task 成功/失败一模一样），说明 10% 剂量不足以造成影响
- **pick_cool_then_place** 和 **pick_and_place_simple** 受 TaxEI injection 影响最大（-28.6pp 和 -25.0pp）
- **pick_two_obj_and_place** 和 **pick_clean_then_place** 对 TaxEI injection 完全免疫

**Taxonomy penalty（TaxEI 相对 Random 的额外惩罚，3-seed 平均）：**

| Task | TaxEI−Random gap |
|------|-----------------|
| pick_cool_then_place | **-19.0pp** |
| pick_two_obj_and_place | **-14.3pp** |
| pick_and_place_simple | -4.2pp |
| pick_heat_then_place | 0.0pp |
| look_at_obj_in_light | 0.0pp |

pick_cool 和 pick_two 是 taxonomy-guided injection 相比 random noise 额外造成伤害最大的两个 task type。

---
