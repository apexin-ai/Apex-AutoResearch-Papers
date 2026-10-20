# analysis eval sft cka only 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_sft_cka_only_20_20260517T144730_result.json`
- **Structured JSON:** [`e94c920c2740049dff26.json`](../../sessions/e9/e94c920c2740049dff26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。memory.md 和 registry 均已更新。

核心结论：CKA-only 20% post-SFT accuracy **64.0%**，比 RASP (~60%)、Standard (~59%)、Random (~60%) 均高 4-5pp。结合 post-prune 阶段的优势 (38.5% vs ~15-19%)，CKA-only scoring 在剪枝质量和 SFT 恢复两个维度都是最优的。不过 SFT 的 equalizing effect 很强，将原本 ~20pp 的差距压缩到了 ~4-5pp。

---
