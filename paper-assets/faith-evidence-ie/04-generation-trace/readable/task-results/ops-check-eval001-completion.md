# ops check eval001 completion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-eval001-completion_20260515T213553_result.json`
- **Structured JSON:** [`9be872b235fdfce35354.json`](../../sessions/9b/9be872b235fdfce35354.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval_plan_001_flat_nli_s43 已完成。** EXIT_CODE=0，耗时 ~61 分钟。

**Metrics:**
| 指标 | 值 |
|------|-----|
| F1 | 0.0022 |
| Ign-F1 | 0.0022 |
| Evi-F1 | 0.8533 |
| EDCR | 0.9982 |
| Format OK | 981/985 (99.6%) |
| Truncated | 251/985 |
| Predictions | 17285 |

结果已写入 `/root/autodl-tmp/eval_results/rsft_flat_nli_s43/`。

**F1=0.0022 极低**，说明关系抽取几乎全错，但 Evi-F1=0.8533 和 EDCR=0.9982 很高——模型能找到证据句但无法正确预测关系。Truncated 251/985 也偏高（25.5%），可能影响输出质量。

**GPU 状态:** cuda:0 占用 14597 MiB / 31% 利用率（仍有进程占用），cuda:3 空闲。

---
