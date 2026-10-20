# analysis llama crossmodel summary

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama-crossmodel-summary_20260516T145311_result.json`
- **Structured JSON:** [`d0eba88a9fb357d90e2b.json`](../../sessions/d0/d0eba88a9fb357d90e2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。核心发现：

**LLaMA-3.1-8B (2-seed):** Vanilla=74.5%, TaxEI=74.5%, Random=75.5% — 三个条件完全收敛，无 injection penalty。

**与 Qwen3-8B 的关键差异：**
- Qwen3-8B: injection 训练降低性能 ~9pp（67.3→58.3），但 TaxEI≈Random
- LLaMA: 模型本身已足够强，任何 injection 方法都不增加价值（也不损害）
- LLaMA 有 21-30% detection rate（Qwen3-8B 为 0%）

**Pending:** s123 的 taxei 和 random 仍在训练中，另外 taxei-s42-clean 和 random-s0-clean 未提交。

Artifact 已注册：`art_20260516_0dc6e0`

---
