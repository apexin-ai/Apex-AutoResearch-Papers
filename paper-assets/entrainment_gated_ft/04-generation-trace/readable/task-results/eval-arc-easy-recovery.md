# eval arc easy recovery

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_arc-easy-recovery_20260520T092339_result.json`
- **Structured JSON:** [`e374ae05f86db753ab1c.json`](../../sessions/e3/e374ae05f86db753ab1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**已完成模型：15/15**
缺失模型列表：无
恢复操作：无需恢复（服务器重启前已全部跑完）

结果汇总（acc / acc_norm）：

| 模型 | acc | acc_norm |
|------|-----|----------|
| **GatedDeltaNet-pure** | 0.7121 | 0.6414 |
| GatedDeltaNet-h24-1 | 0.7092 | 0.6305 |
| GatedDeltaNet-h12-1 | 0.6995 | 0.6292 |
| GatedDeltaNet-h6-1 | 0.7176 | 0.6574 |
| GatedDeltaNet-h3-1 | 0.7083 | 0.6486 |
| **RetNet-pure** | 0.7130 | 0.6486 |
| RetNet-h24-1 | 0.7088 | 0.6431 |
| RetNet-h12-1 | 0.7201 | 0.6553 |
| RetNet-h6-1 | 0.7180 | 0.6582 |
| RetNet-h3-1 | 0.6961 | 0.6444 |
| **HGRN2-pure** | 0.7130 | 0.6646 |
| HGRN2-h24-1 | 0.7302 | 0.6785 |
| HGRN2-h12-1 | 0.7332 | 0.6688 |
| **HGRN2-h6-1** | **0.7412** | 0.6696 |
| HGRN2-h3-1 | 0.7205 | 0.6435 |

结果路径：`/root/entrainment_gated_ft/lm_eval_clean/arc_easy/`（每个模型目录含 `.json` 结果和 `samples/arc_easy.jsonl`）。Registry 已更新为 DONE/success。

---
