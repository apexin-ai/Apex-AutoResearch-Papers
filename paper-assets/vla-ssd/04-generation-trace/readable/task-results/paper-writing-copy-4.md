# paper writing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_20260522T061909_result.json`
- **Structured JSON:** [`65aceacee99034c840f1.json`](../../sessions/65/65aceacee99034c840f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。两处变更：

1. **§3.1 架构描述平衡**：OpenVLA 删除了 MLP projector 维度细节 `(2,176-D → 4,096-D)`；TracVLA 补充了 3.8B 参数量和 spatial trace conditioning 的作用（视觉轨迹叠加提供空间引导）；NORA 补充了 ~3B 参数量和 native vision encoder 特征（动态分辨率处理、无独立投影层）。三个架构各约 2-2.5 行，密度均衡。

2. **术语一致性**：line 87 `readout positions` → `readout`，与 §3.2 定义的 `\textbf{readout}` 术语一致。

---
