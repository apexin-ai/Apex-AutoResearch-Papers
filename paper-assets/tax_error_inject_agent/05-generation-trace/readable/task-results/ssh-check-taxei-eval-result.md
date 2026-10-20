# ssh check taxei eval result

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-taxei-eval-result_20260514T104200_result.json`
- **Structured JSON:** [`b3824d9b1c649d4a04a2.json`](../../sessions/b3/b3824d9b1c649d4a04a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三组 eval 全部完成。汇总结果：

## Mini Eval 47-task 结果

| Task Type | TaxEI | Baseline | Vanilla |
|---|---|---|---|
| look_at_obj_in_light | 3/6 (50.0%) | 3/6 (50.0%) | 0/6 (0%) |
| pick_and_place_simple | 2/8 (25.0%) | 4/8 (50.0%) | 2/8 (25.0%) |
| pick_clean_then_place | 6/11 (54.5%) | 5/11 (45.5%) | 2/11 (18.2%) |
| pick_cool_then_place | 1/7 (14.3%) | 0/7 (0%) | 0/7 (0%) |
| pick_heat_then_place | 6/8 (75.0%) | 5/8 (62.5%) | 3/8 (37.5%) |
| pick_two_obj_and_place | 3/7 (42.9%) | 3/7 (42.9%) | 0/7 (0%) |
| **Total** | **21/47 (44.7%)** | **20/47 (42.6%)** | **7/47 (14.9%)** |

## 关键发现

- **TaxEI 44.7% > Baseline 42.6%** — 超过 zero-shot baseline +2.1pp
- **Vanilla SFT 严重坍缩** — 14.9%，远低于 baseline，SFT 损害了基础能力
- TaxEI 优势集中在：`pick_heat` (+12.5pp vs baseline)、`pick_clean` (+9.0pp)、`pick_cool` (唯一非零)
- TaxEI 劣势：`pick_and_place_simple` 25% vs baseline 50%（-25pp）
- `pick_cool` 对所有方法都很难，只有 TaxEI 做到了 1/7

PID 37424 进程仍在（log 已输出完整 summary），可能是模型卸载阶段，GPU 1 仍占用 17GB 显存。eval 数据已完整写入 `eval_results/mini_taxei_clean.json`。

---
