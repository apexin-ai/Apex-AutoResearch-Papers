# paper f7 024b control sentence

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_f7-024b-control-sentence_20260518T021603_result.json`
- **Structured JSON:** [`bb3eb25b80b74c7f1ef9.json`](../../sessions/bb/bb3eb25b80b74c7f1ef9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项修改完成：

**任务 1** — `docs/paper/sections/results.tex` line 105，F7 段末尾添加了 024b 控制组句子。无 em-dash 引入。

**任务 2** — `decisions.yaml` D090 条目：
- `rationale` 中 `NVE~0.1×` → `NVE<0.2×`（s0）和 `NVE=0.1×` → `NVE=0.10×`（s1）
- `related_experiments` 中 s0 补充了 `NVE<0.2×`，s1 精确为 `NVE=0.10×`

与 registry 一致（s0 nve_peak=0.2 即 "<0.2×"，s1 nve_peak=0.1 即 "0.10×"）。

---
