# ops alfworld gate recheck

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_alfworld-gate-recheck_20260516T053728_result.json`
- **Structured JSON:** [`a6cd231b6989b2694452.json`](../../sessions/a6/a6cd231b6989b2694452.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ALFWorld 任务池

**Total game files: 3981 → Gate: PASS**

| 任务类型 | 数量 |
|---------|------|
| pick_two_obj_and_place | 904 |
| pick_and_place_simple | 864 |
| pick_clean_then_place_in_recep | 745 |
| pick_cool_then_place_in_recep | 628 |
| pick_heat_then_place_in_recep | 531 |
| look_at_obj_in_light | 309 |

## TaxEI-RP 训练进度

| Seed | Step | Progress | Loss | Token Acc | 剩余时间 |
|------|------|----------|------|-----------|---------|
| s0 | 4700/5415 | 86.8% | 0.246 | 91.2% | ~30min |
| s1 | 4760/5415 | 87.9% | 0.256 | 90.8% | ~27min |
| s123 | 4790/5415 | 88.5% | 0.260 | 90.8% | ~26min |
| s42 | 4780/5415 | 88.3% | 0.310 | 89.3% | ~27min |

4 个 seed 都在 epoch 2.6 附近，约 30 分钟内全部完成。loss 收敛正常，token accuracy 均在 89-91%。

---
