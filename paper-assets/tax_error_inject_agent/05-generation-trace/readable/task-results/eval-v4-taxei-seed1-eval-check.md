# eval v4 taxei seed1 eval check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v4-taxei-seed1-eval-check_20260515T164244_result.json`
- **Structured JSON:** [`ea53e65fc567b64f67e4.json`](../../sessions/ea/ea53e65fc567b64f67e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**v4-taxei-seed1-eval 正在运行中，无需干预。**

当前状态：
- **进度**：17/47 任务已完成
- **GPU**：cuda:2，17091 MiB 已用，40% 利用率
- **当前成绩**（17 tasks）：11 OK / 6 FAIL

已完成的任务：
| # | 任务 | 结果 | 步数 |
|---|------|------|------|
| 1 | look_at_obj-AlarmClock-DeskLamp-308 | OK | 5 |
| 2 | look_at_obj-Book-DeskLamp-308 | FAIL | 50 |
| 3 | look_at_obj-Bowl-DeskLamp-308 | OK | 7 |
| 4 | look_at_obj-CD-DeskLamp-308 | OK | 13 |
| 5 | look_at_obj-Mug-DeskLamp-308 | OK | 6 |
| 6 | look_at_obj-Pencil-DeskLamp-308 | OK | 5 |
| 7 | pick_place-Mug-Desk-308 | OK | 5 |
| 8 | pick_place-Pencil-Shelf-308 | FAIL | 50 |
| 9 | pick_place-PepperShaker-Drawer-10 | FAIL | 50 |
| 10 | pick_place-SaltShaker-Cabinet-10 | FAIL | 50 |
| 11 | pick_place-SaltShaker-Drawer-10 | OK | 41 |
| 12 | pick_place-SoapBottle-Toilet-424 | OK | 8 |
| 13 | pick_place-Vase-Safe-219 | OK | 17 |
| 14 | pick_place-Watch-Safe-219 | FAIL | 50 |
| 15 | pick_clean_place-Bowl-Cabinet-10 | OK | 12 |
| 16 | pick_clean_place-Cloth-Cabinet-424 | FAIL | 50 |
| 17 | pick_clean_place-Cloth-CounterTop-424 | OK | 9 |

暂时成功率 64.7%（11/17），还有 30 个任务待完成。预计还需一段时间。完成后结果会写入 `eval_results/v4_taxei_seed1_eval.json`。

---
