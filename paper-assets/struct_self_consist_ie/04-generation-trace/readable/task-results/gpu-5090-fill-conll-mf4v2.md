# gpu 5090 fill conll mf4v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_5090_fill_conll_mf4v2_20260521T130142_result.json`
- **Structured JSON:** [`5774a106eee8365d35a2.json`](../../sessions/57/5774a106eee8365d35a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已成功启动，4 张卡全部在用：

| 实验 | GPU | PID | 显存 | 状态 |
|------|-----|-----|------|------|
| `exp_conll_mf4v2_s123_rerun` | cuda:2 | 42724 (VLLM engine) / 42178 (tmux) | 16388MiB | RUNNING |
| `exp_conll_mf4v2_s456_rerun` | cuda:3 | 42889 (VLLM engine) / 42447 (tmux) | 16388MiB | RUNNING |

N=8 推理，CoNLL 3453 条，预计运行时间较短。日志分别在 `~/runs/struct_self_consist_ie/exp_conll_mf4v2_s{123,456}_rerun.log`。

---
