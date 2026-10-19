# writing k and checkpoint doc

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_k_and_checkpoint_doc_20260514T175242_result.json`
- **Structured JSON:** [`e13fd1ddf93fdcb1ca03.json`](../../sessions/e1/e13fd1ddf93fdcb1ca03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**分析结果**：
- **K=7** negatives per query，所有主实验一致
- **Dual checkpoint**：7 个可评估的已完成 runs 中，4 个两种 criterion 选择相同 checkpoint（全部是 Qwen），3 个不同（全部是 StarCoder）
- **规律**：StarCoder 的 R@1 在 val_loss 开始过拟合后仍继续提升，导致两种 criterion 分叉；Qwen 两者始终一致
- **论文段落**（~120 words）已写入 `artifacts/paper_drafts/experimental_setup_k_checkpoint.md`，包含完整的 registry-backed 数据，注册为 `art_20260514_a50aca`

---
