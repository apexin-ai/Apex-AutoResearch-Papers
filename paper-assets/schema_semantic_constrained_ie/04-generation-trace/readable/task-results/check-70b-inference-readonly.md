# check 70b inference readonly

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_70b_inference_readonly_20260522T034921_result.json`
- **Structured JSON:** [`2b513b432721715f51d2.json`](../../sessions/2b/2b513b432721715f51d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
SciERC (cuda:0, PID 879994): 存活 (运行 1h29m), 已完成 315/551 样本 (57.2%)
DocRED (cuda:1, PID 881085): 存活 (运行 1h16m), 已完成 56/998 样本 (5.6%)
GPU0: VRAM 79190/97887 MiB, util 94%
GPU1: VRAM 40921/97887 MiB, util 81%
--max_samples 支持: 是 (line 858, 默认0=全部, 也支持 --max_docs 别名)
```

SciERC 进度正常，按当前速率预估还需约 1h 完成。DocRED 进度较慢（文档级 RE 每条样本更长），预估还需约 20h+。

---
