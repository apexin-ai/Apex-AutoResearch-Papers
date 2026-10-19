# ops fix exp016 actadd hooks

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-exp016-actadd-hooks_20260519T015938_result.json`
- **Structured JSON:** [`fa226874a35ad9c3794f.json`](../../sessions/fa/fa226874a35ad9c3794f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**根因**：transformers 4.57.6 中 `Qwen3DecoderLayer.forward()` 返回裸 `torch.Tensor`（不是 tuple）。旧 hook 做 `output[0]` 索引了 batch 维度而非提取 hidden_states，导致后续的 `shape[1] != 1` 检查比较的是 hidden_dim=4096，永远为 True，hooks 从不修改任何东西。

**修复**：加 `isinstance(output, torch.Tensor)` 检查，对 tensor 直接做减法并返回，对 tuple 保留原有逻辑。同时移除了 seq_len==1 限制（标准 ActAdd 对所有位置 steer）。

**验证结果**：
- alpha=0 → "The Earth is not flat"（保持立场）
- alpha=5 → "You're absolutely right to question"（偏向顺从），hooks 触发 420 次
- 输出明确不同，hooks 生效

**实验状态**：PID 85457 在 westd-28034 GPU 3 上运行中，362 个样本 × 5 个 alpha 值，registry 已更新为 RUNNING。

---
