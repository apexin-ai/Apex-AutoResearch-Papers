# ops q07 check and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_q07_check_and_eval_20260525T082655_result.json`
- **Structured JSON:** [`f6669d30ad1d31ed3746.json`](../../sessions/f6/f6669d30ad1d31ed3746.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。三个 q07 seed 训练 + eval + registry 更新汇总：

| Experiment | holdout_ppl | owt_ppl | wiki_ppl |
|---|---|---|---|
| `detect_remove_q07_seed42_r3` | 17.32 | 18.04 | 15.11 |
| `detect_remove_q07_seed123` | 17.32 | 18.04 | 15.10 |
| `detect_remove_q07_seed456` | 17.32 | 18.03 | 15.11 |

三个 seed 结果高度一致，方差极小。Registry 均已更新为 DONE/success。

注意：任务模板中的 `data/human/owt_eval.jsonl` 和 `data/human/wiki_eval.jsonl` 不存在，实际路径为 `data/eval_openwebtext.jsonl` 和 `data/eval_wikipedia.jsonl`。

---
