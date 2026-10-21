# exp unpruned full eval n1319

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_unpruned-full-eval-n1319_20260516T013836_result.json`
- **Structured JSON:** [`88692f88ed4188854b75.json`](../../sessions/88/88692f88ed4188854b75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 摘要

**Unpruned N=1319 full eval**: PID 74129, westd cuda:0, ~2.5s/it → ETA ~55min

**Unpruned N=100 eval**: 完成
| 指标 | 值 |
|------|-----|
| accuracy | **84.00%** |
| n_correct | 84/100 |
| eos_rate | 1.0 |
| avg_len | 187.22 |
| stderr | 0.0367 |

N=100 快速对比（参考）：
- Standard SFT: 59% (N=100 时未记录)
- RASP SFT: 61% (N=100 时未记录)
- **Unpruned SFT: 84%** (N=100)

N=100 的 84% 非常高，full 1319 的结果将确认是否稳定。

---
