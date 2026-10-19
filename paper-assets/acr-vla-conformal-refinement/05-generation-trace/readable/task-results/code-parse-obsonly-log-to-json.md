# code parse obsonly log to json

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_parse-obsonly-log-to-json_20260515T160256_result.json`
- **Structured JSON:** [`0c9f5549e9911c1d68cf.json`](../../sessions/0c/0c9f5549e9911c1d68cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果汇总：**

| # | Task | SR | Successes/Total |
|---|------|----|----------------|
| 1 | alphabet_soup | 0% | 0/10 |
| 2 | cream_cheese | 10% | 1/10 |
| 3 | salad_dressing | 20% | 2/10 |
| 4 | bbq_sauce | **40%** | 4/10 |
| 5 | ketchup | 10% | 1/10 |
| 6 | tomato_sauce | 0% | 0/10 |
| 7 | butter | 10% | 1/10 |
| 8 | milk | 20% | 2/10 |
| 9 | chocolate_pudding | **50%** | 5/10 |
| 10 | orange_juice | 30% | 3/10 |
| **Overall** | | **19.0%** | **19/100** |

**产出：**
- 脚本：`/root/acr-vla-conformal-refinement/scripts/parse_log_to_json.py`（两台服务器均已部署）
- JSON：`/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json`（`bjb1-32546` 和 `bjb2-40593` 均有）
- 格式与 evaluate.py 的 `--output_file` 输出完全一致，可直接用于 Fisher exact test

---
