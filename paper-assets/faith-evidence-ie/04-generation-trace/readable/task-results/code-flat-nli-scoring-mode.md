# code flat nli scoring mode

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_flat_nli_scoring_mode_20260515T131633_result.json`
- **Structured JSON:** [`335995e931f9198bdcef.json`](../../sessions/33/335995e931f9198bdcef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。7 处改动全部到位：

| 行 | 改动 |
|---|---|
| 6 | docstring 注明 flat_nli 模式 |
| 97 | `compute_ced_reward_for_record` 签名加 `scoring_mode` |
| 159 | flat_nli 分支：调 `compute_flat_nli_reward`，跳过 hard_neg 查找 |
| 278 | `score_all_records` 签名加 `scoring_mode` |
| 284 | 透传 `scoring_mode` 到 `compute_ced_reward_for_record` |
| 496 | argparser 新增 `--scoring_mode {ced, flat_nli}` |
| 535 | `main()` 传 `args.scoring_mode` |

---
