# env alfworld counterfactual

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_env_alfworld-counterfactual_20260514T132744_result.json`
- **Structured JSON:** [`cb65c9e1c5b0fb7214c8.json`](../../sessions/cb/cb65c9e1c5b0fb7214c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Phase 1: ALFWorld 安装** — alfworld 0.4.2 + textworld + jericho 已预装。数据下载到 `/root/autodl-tmp/alfworld_data/`（json_2.1.1，valid_seen 140 games，6 种 task type）。

**Phase 2-3: Counterfactual Pipeline** — `src/alfworld_counterfactual.py` 重写为正确的实验设计：
- **Internal**: LLM 只看 observation，不展示 admissible actions，自由生成 action 后 fuzzy match
- **Deterministic**: LLM 看 observation + admissible actions list，从中选择
- Episode-level labeling: det-preferred / internal-preferred / no-preference
- 输出 JSONL 格式与 ScienceWorld/MATH 统一

**Phase 4: Dry-run 5 tasks** — 全部完成：
| Task | Internal | Deterministic | Label |
|------|----------|---------------|-------|
| look_at_obj_in_light #1 | FAIL/50 | FAIL/50 | no-preference |
| look_at_obj_in_light #2 | FAIL/50 | FAIL/50 | no-preference |
| look_at_obj_in_light #3 | OK/25 | OK/3 | no-preference |
| look_at_obj_in_light #4 | FAIL/50 | FAIL/50 | no-preference |
| look_at_obj_in_light #5 | FAIL/50 | FAIL/50 | no-preference |

Dry-run 仅跑了 `look_at_obj_in_light` 类型。可以用 `--task_types pick_and_place,...` 或更大的 `--n_tasks` 来覆盖更多类型和产生更多 det-preferred/internal-preferred 信号。GPU 已释放。

---
