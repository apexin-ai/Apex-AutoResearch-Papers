# research large model third method

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_large-model-third-method_20260512T101957_result.json`
- **Structured JSON:** [`a10d1ea2268e34a9afe3.json`](../../sessions/a1/a10d1ea2268e34a9afe3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `LARGE_MODEL_THIRD_METHOD.md`。

核心结论：

**首选 IFR**——唯一满足全部条件（edge-level、非 gradient/非 mask optimization、可扩展到 8B）的方法。算法族为 activation decomposition，与 EAP-IG（gradient）和 Edge Pruning（mask optimization）形成三族独立投票。MIB 已有现成实现，仅需 1 次 forward pass。

**PAHQ 不可行**——5x 加速不够弥补 ACDC 在大模型上的数量级瓶颈。**UGS 不可行**——内存爆炸且与 Edge Pruning 同族。**AtP* 可作为备选**但与 EAP-IG 同属 gradient 族，审稿人可能质疑独立性。

---
