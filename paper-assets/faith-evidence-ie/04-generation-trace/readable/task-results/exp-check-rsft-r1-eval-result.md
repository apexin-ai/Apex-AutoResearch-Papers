# exp check rsft r1 eval result

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_check-rsft-r1-eval-result_20260515T112348_result.json`
- **Structured JSON:** [`e1345667756ea54cbf1f.json`](../../sessions/e1/e1345667756ea54cbf1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## RSFT r1 全量 Dev Eval 结果

| Metric | RSFT r1 | SFT baseline | Δ vs SFT | s44 |
|--------|---------|-------------|----------|-----|
| rel_f1 | **0.4449** | 0.4057 | +0.0392 | 0.4655 |
| evi_f1 | **0.8187** | 0.7979 | +0.0208 | 0.8087 |
| EDCR | 0.6565 | 0.7118 | -0.0553 | 0.6350 |
| num_preds | 15307 | — | — | — |

**MVP-2 PASS** — rel_f1 > 0.4057 ✓, evi_f1 > 0.798 ✓

注意：evi_f1 比 s44 还高 (+0.01)，rel_f1 比 SFT baseline 高但低于 s44。EDCR 介于两者之间。213/985 文档被截断。

Registry 已更新为 DONE/success，cron 已清除。

---
