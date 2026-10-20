# monitor raw counts both servers

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_raw-counts-both-servers_20260521T231553_result.json`
- **Structured JSON:** [`3c9fb80e6447ff0f0d79.json`](../../sessions/3c/3c9fb80e6447ff0f0d79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
westd-19828:
t25_a075_s42_fp32 → 26/26 (gen_25) → COMPLETED | results/phase_diagram/
t20_a045_s43_fp32 → 16/21 (gen_15) → RUNNING   | results/phase_diagram/

westd-17855:
t25_a045_s42_fp32 → 25/26 (gen_24) → RUNNING   | results/phase_diagram/
t25_a060_s42_fp32 → 10/26 (gen_9)  → RUNNING   | results/phase_diagram/
t25_a050_s42_fp32 → 10/26 (gen_9)  → RUNNING   | results/phase_diagram/
t20_a060_s43_fp32 → 10/21 (gen_9)  → RUNNING   | results/phase_diagram/
t15_a060_s43_fp32 → 13/16 (gen_12) → RUNNING   | results/phase_diagram/
t15_a045_s43_fp32 → 11/16 (gen_10) → RUNNING   | results/phase_diagram/
```

注：19828 还跑着 `generalize_pythia410m_wiki_a100_s42`（GPU0），t20_a045_s43 在 GPU1。17855 上 6 个实验并行。

---
