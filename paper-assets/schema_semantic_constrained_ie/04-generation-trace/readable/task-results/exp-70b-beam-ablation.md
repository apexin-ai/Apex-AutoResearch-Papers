# exp 70b beam ablation

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_70b-beam-ablation_20260522T143155_result.json`
- **Structured JSON:** [`932e65b6780a741bec3c.json`](../../sessions/93/932e65b6780a741bec3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已确认正常运行，输出格式正确。

**状态汇总：**

| 实验 | 服务器 | GPU | 模式 | 速度 | 预计耗时 |
|------|--------|-----|------|------|----------|
| **A**: 70B LoRA beam k=4 full_s1 | westd-16980 | cuda:0 (58.7GB) | beam search | ~21s/sample | ~3h |
| **B-1**: 70B ZS grammar_only | westd-21461 | cuda:0 (39.3GB) | greedy | ~6s/sample | ~55min |
| **B-2**: 70B ZS semantic_only | westd-21461 | cuda:0 | greedy | ~6s/sample | 待 B-1 完成后串行 |

**调整说明：** 70B scierc LoRA adapter 仅在 westd-16980 上，跨 AutoDL 容器无法直接互传文件。故 Exp A 改在 westd-16980 运行（两台服务器代码版本一致）。

**待做：** grammar_only 预计 ~55 分钟后完成，届时需在 westd-21461 上启动 semantic_only。需要后续轮询。

---
