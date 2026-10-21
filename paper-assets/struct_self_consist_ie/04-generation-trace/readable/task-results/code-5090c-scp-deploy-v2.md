# code 5090c scp deploy v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_5090c_scp_deploy_v2_20260518T200204_result.json`
- **Structured JSON:** [`ca81e93c536a61f4b0ca.json`](../../sessions/ca/ca81e93c536a61f4b0ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Rsync 实际进展：
- **CoNLL**: shard 1 (4.6GB) 完成，shard 2 刚开始。约 30 分钟完成全部
- **SciERC v2**: shard 1 at 3.5/4.6GB。约 30 分钟完成

**FewNERD** 推理在 GPU 2 稳定运行（~1400 toks/s，~50 it/s）。

当前状态汇总：
| 任务 | GPU | 状态 | 预计完成 |
|------|-----|------|----------|
| SciERC seed=789 | 0 | 等 rsync (~30min) | ~40min after start |
| CoNLL seed=789 | 1 | 等 rsync (~30min) | ~60min after start |
| FewNERD seed=789 | 2 | 运行中 (0.3%) | ~100min |
| SciERC T=1.2 seed=456 | 3 | 等 rsync (~30min) | ~40min after start |

Launch script 会在 rsync 完成后自动启动剩余 3 个任务。SciERC seed=789 在 5090 上已有结果（exp_022_seed789），在 5090-c 会重新跑作为 replication。

等 15 分钟后再查进度。需要我继续监控还是先做其他事？

---
