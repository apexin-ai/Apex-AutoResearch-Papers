# ops bce blast check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bce_blast_check_20260520T001159_result.json`
- **Structured JSON:** [`a6d426d2be04c264189f.json`](../../sessions/a6/a6d426d2be04c264189f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Worker 已完成（耗时约 4 分钟）。结果汇总：

## BCE Double Sigmoid Blast Radius 检查结果

### 发现的 Bug

| 位置 | 问题 | 影响 |
|------|------|------|
| `test_train_pipeline.py:103` | `binary_cross_entropy_with_logits` 对已 sigmoid 的输出再做 sigmoid | 测试脚本，不影响正式实验 |
| `test_train_pipeline.py:123` | 同上 | 同上 |
| `action_head.py:623` (`GPTDecoderActPad.forward`) | `nn.functional.sigmoid(self.gripper(x))` 而 `self.gripper` 是 `MLPSigmoidHead`（已含 Sigmoid） | **潜在 bug**，当前未被 factory 使用，不影响任何实验 |

### 确认安全的

- `train_libero.py:144` — **已修复**
- `train_utils.py` 三处 BCE 调用 — 正确
- importance_margin_vla_compress 项目两台服务器 — **无此类 bug**

### 结论

正式训练代码和当前项目不受影响。需要修的是两处测试脚本（`binary_cross_entropy_with_logits` → `binary_cross_entropy`）和一处潜在的 `GPTDecoderActPad` double sigmoid。优先级都不高。

---
