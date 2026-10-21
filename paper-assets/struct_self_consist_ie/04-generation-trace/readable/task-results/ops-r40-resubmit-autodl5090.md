# ops r40 resubmit autodl5090

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_r40-resubmit-autodl5090_20260522T175807_result.json`
- **Structured JSON:** [`683156eb1dae1d41ed35.json`](../../sessions/68/683156eb1dae1d41ed35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

**排查结果汇总：**

| 实验 | GPU | 状态 |
|------|-----|------|
| exp_esj_qwen3_all | cuda:2 | **已完成**（EXIT_CODE=0），无需重提交 |
| exp_scierc_n8_s2024 | cuda:0 | **已重提交** — GPU 利用率 45%，显存 29382MiB |
| exp_scierc_n8_s3141 | cuda:1 | **已重提交** — GPU 利用率 55%，显存 29216MiB |

**失败原因**：两个 scierc 实验的 `--data_dir` 写成了 `data/scierc`，实际数据在 `data/scierc/processed_data`。已修正路径重新提交。

cuda:2 空闲，因为 ESJ 实验已经跑完了。

---
