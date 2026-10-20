# research itpr deep read

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_itpr-deep-read_20260513T090907_result.json`
- **Structured JSON:** [`926d1b48be33d7aa1c9d.json`](../../sessions/92/926d1b48be33d7aa1c9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `/root/autodl-tmp/simgate-modular-routing/notes/literature_itpr.md`（287 行）。

关键发现：

**性能**: ITP-R 在 ScienceWorld 上 best success rate 为 Seen 63.91% / Unseen 57.61%（Llama-3.1-8B）。只报告了 success rate，无 continuous score，无 per-task breakdown。

**World Model 核心弱点**: Learned LLM-based WM 存在 compounding errors — Fact-F1 随 horizon 单调下降，agent success 在 k≈3 后也开始下降。这是 SimGate 用真实 simulator 的最大优势切入点：zero approximation error，不受 horizon 限制。

**Gating 机制**: K-head predictor（线性层）预测 K ∈ {0,...,K_max}，控制 imagination 深度。与 SimGate 的 binary routing 不同 — ITP-R 是选"看多远"，SimGate 是选"用不用 simulator"。论文没报告 K=0（跳过 WM）的比例。

**训练成本**: ~62.5 A100 GPU-hours，推理每步 14.2s（imagination 占 7.8s）。

**最关键的对比缺口**: ITP-R 论文完全没有对比 learned WM vs real simulator，这正是 SimGate 的贡献空间。

---
