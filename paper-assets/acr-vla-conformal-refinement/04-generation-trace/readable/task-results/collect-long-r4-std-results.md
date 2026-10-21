# collect long r4 std results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_long-r4-std-results_20260522T165346_result.json`
- **Structured JSON:** [`6610eb1be2c733afccc6.json`](../../sessions/66/6610eb1be2c733afccc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程都已退出，两个 seed 的 JSON 结果都已生成。

## π0.5 Long r4 标准化结果（n_rollouts=20）

### seed44: overall SR = **0.955**

| Task | SR | Successes |
|------|-----|-----------|
| SCENE2_alphabet_soup+tomato_sauce → basket | 1.00 | 20/20 |
| SCENE2_cream_cheese+butter → basket | 1.00 | 20/20 |
| SCENE3_stove+moka_pot | 1.00 | 20/20 |
| SCENE4_black_bowl → drawer+close | 1.00 | 20/20 |
| SCENE5_white_mug+yellow_mug → plates | 0.95 | 19/20 |
| SCENE1_book → caddy | 1.00 | 20/20 |
| SCENE6_white_mug+chocolate_pudding | 1.00 | 20/20 |
| SCENE1_alphabet_soup+cream_cheese → basket | 0.90 | 18/20 |
| **SCENE8_both_moka_pots → stove** | **0.70** | **14/20** |
| SCENE6_mug → microwave+close | 1.00 | 20/20 |

### seed43: overall SR = **0.955**

| Task | SR | Successes |
|------|-----|-----------|
| SCENE2_alphabet_soup+tomato_sauce → basket | 0.95 | 19/20 |
| SCENE2_cream_cheese+butter → basket | 1.00 | 20/20 |
| SCENE3_stove+moka_pot | 0.95 | 19/20 |
| SCENE4_black_bowl → drawer+close | 1.00 | 20/20 |
| SCENE5_white_mug+yellow_mug → plates | 0.95 | 19/20 |
| SCENE1_book → caddy | 1.00 | 20/20 |
| SCENE6_white_mug+chocolate_pudding | 1.00 | 20/20 |
| SCENE1_alphabet_soup+cream_cheese → basket | 0.95 | 19/20 |
| **SCENE8_both_moka_pots → stove** | **0.80** | **16/20** |
| SCENE6_mug → microwave+close | 0.95 | 19/20 |

两个 seed 的 overall SR 完全一致（0.955）。最难的 task 仍然是 SCENE8_both_moka_pots（seed44=0.70, seed43=0.80），其余 task 均 ≥0.90。

---
