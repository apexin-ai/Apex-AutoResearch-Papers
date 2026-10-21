# check all experiments status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_experiments_status_20260521T124753_result.json`
- **Structured JSON:** [`d3e5bdef37215cbb5aaf.json`](../../sessions/d3/d3e5bdef37215cbb5aaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-21461 ===
GPU0: 空闲, VRAM 0/96 GB, util 0%
GPU1: 使用中, VRAM 39/96 GB, util 90%
r16_70b_docred_zs: 运行中 (PID 247853, 已运行 7h42m)
  - 阶段: [1/2] unconstrained inference, ~864/998 样本
  - 尚未进入 constrained (s1) 阶段
  - unconstrained.jsonl: 863 行已写入
  - 预计 unconstrained 剩余 ~134 样本后进入 s1 阶段

=== westd-16980 ===
GPU0: VRAM 46/96 GB, util 99%
GPU1: VRAM 50/96 GB, util 100%
r16_70b_lora_scierc (GPU0): step 183/663 (28%), ~14s/step, 已运行 44min, ETA ~1h56m
  - 无 loss 输出（Trainer 尚未到 logging step）
  - 无 checkpoint 保存
r16_70b_lora_docred (GPU1): step 10/1146 (1%), ~32s/step, 已运行 6min, ETA ~10h
  - 无 loss 输出
  - 无 checkpoint 保存
  - Num examples=3053, 3 epochs, grad_accum=8, total steps=1146
```

---
