# harvest eval supp long k2mean s47 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval-supp-long-k2mean-s47-r2_20260524T155120_result.json`
- **Structured JSON:** [`64a97424830bedd9bb80.json`](../../sessions/64/64a97424830bedd9bb80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在，无需删除。

**结果汇总：eval-supp-long-k2mean-s47-r2 — 成功**

- **Overall SR: 54.5%** (109/200)，Long suite K2-mean baseline seed=47
- Registry 已更新：DONE / success / metrics 完整
- 结果文件：`logs/eval_long_vla_only_seed47.json`

Per-task breakdown：

| Task | SR |
|------|-----|
| KITCHEN_SCENE3 stove+moka | 100% |
| KITCHEN_SCENE4 bowl+drawer | 95% |
| STUDY_SCENE1 book+caddy | 85% |
| SCENE2 cream+butter | 75% |
| KITCHEN_SCENE6 mug+microwave | 70% |
| SCENE1 soup+cream | 50% |
| SCENE5 mugs+plates | 25% |
| SCENE6 mug+pudding | 25% |
| SCENE2 soup+tomato | 15% |
| SCENE8 moka_pots | 5% |

与 s42 的 57.0% 基本一致，K2-mean baseline 在 Long suite 上 SR 约 55-57% 范围。

---
