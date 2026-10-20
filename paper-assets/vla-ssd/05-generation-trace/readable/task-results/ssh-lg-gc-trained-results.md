# ssh lg gc trained results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_lg_gc_trained-results_20260515T175347_result.json`
- **Structured JSON:** [`04becc346f71b862e64b.json`](../../sessions/04/04becc346f71b862e64b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。总结：

**lg_gc_trained 实验结果**
- **n_classes=10**，10个 LIBERO-Goal task 全部包含 ✓
- **Layer 0**: 15.8% accuracy（退化到只预测 class 1，接近随机）
- **Layer 1-32**: **100% accuracy**，完美分类，所有 task 的 per-class accuracy 均为 1.0
- Layer 1 需 13 epochs 收敛，Layer 2+ 仅需 6 epochs
- **Gate G1-GC: PASS**（100% >> 40% 阈值）

Trained VLA 从第 1 层起就把 goal identity 编码得极其清晰，probe 轻松达到 ceiling。与 dry-run 的 9-class 结果一致，10-class 同样完美。唯一的分辨力在 Layer 0（raw embedding）vs Layer 1+。

---
