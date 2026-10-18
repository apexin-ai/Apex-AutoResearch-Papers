# paper research vit pruning gap

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_vit_pruning_gap_20260522T230243_result.json`
- **Structured JSON:** [`86e45677b5acac4f3117.json`](../../sessions/86/86e45677b5acac4f3117.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Entry added and verified. Here's the summary:

**Added:** `yin2022avit` — *A-ViT: Adaptive Tokens for Efficient Vision Transformer*, CVPR 2022 (Oral)

**Why it complements the existing 3:**

| Paper | Mechanism |
|-------|-----------|
| DynamicViT | Learned binary pruning predictor at **fixed layers** |
| EViT | CLS-attention reorganization at **fixed layers** |
| ToMe | Training-free bipartite **merging** at every layer |
| **A-ViT** | Per-token **adaptive depth** via ACT halting — tokens exit at **different layers** |

A-ViT introduces a fundamentally different axis: instead of deciding *which tokens to remove at a given layer*, it asks *how deep should each token be processed*. This is directly relevant to our VLA token pruning analysis because it highlights that token importance varies across transformer depth — connecting to our investigation of how pruning at different stages of the VLA pipeline produces different failure modes.

---
