# code w10 llama docred beam 50 check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w10_llama_docred_beam_50_check_20260517T072142_result.json`
- **Structured JSON:** [`e8640cc1dca9ae8d185a.json`](../../sessions/e8/e8640cc1dca9ae8d185a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Status ===
Process: running (PID 424211, ~8 min elapsed)
Output lines: 22 / 50
GPU usage: cuda:0 79%, 18679/97887 MiB; cuda:1 idle

=== Progress ===
22/50 samples completed (~44%), still actively processing on beam search (num_beams=4).
Tmux session: llama_docred_beam

=== Greedy baseline comparison ===
(Llama DocRED greedy: DR=2.55%, CF=??%, E_F1=??, R_F1=??)
```

实验还在跑，已完成 22/50 样本。按当前速度（8分钟22个），预计再约10分钟完成。完成后需要再跑 violation checker 和 F1 eval。

---
