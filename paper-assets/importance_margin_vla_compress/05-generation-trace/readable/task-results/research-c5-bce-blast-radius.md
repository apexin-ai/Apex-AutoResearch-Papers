# research c5 bce blast radius

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_c5_bce_blast_radius_20260519T225657_result.json`
- **Structured JSON:** [`ba6244f791aa90bc2d12.json`](../../sessions/ba/ba6244f791aa90bc2d12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是完整结果：

## 检查结果

### BCE 调用汇总

| 文件:行号 | 调用 | 输入是否已 sigmoid | 是否 bug |
|-----------|------|-------------------|---------|
| `train_libero.py:144` | `binary_cross_entropy` | 是 (MLPSigmoidHead) | **已修复** — 已改为正确的 BCE |
| `test_train_pipeline.py:103` | `binary_cross_entropy_with_logits` | 是 (MLPSigmoidHead via DeterministicDecoder) | **BUG** |
| `test_train_pipeline.py:123` | `binary_cross_entropy_with_logits` | 是 (同上) | **BUG** |
| `train_utils.py:574` | `binary_cross_entropy` | 是 | 正确 |
| `train_utils.py:903` | `binary_cross_entropy` | 是 | 正确 |
| `train_utils.py:1136` | `binary_cross_entropy` | 是 | 正确 |

### 追溯链（test_train_pipeline.py 的 bug）

1. 模型 `decoder_type='lstm'` → `flamingo_mpt.py:128` 创建 `DeterministicDecoder`
2. `DeterministicDecoder.__init__` 中 `self.gripper = MLPSigmoidHead(...)` — 最后一层是 `nn.Sigmoid()`
3. `DeterministicDecoder.forward()` 返回 `self.gripper(x)` — **已经是 [0,1] 范围**
4. `test_train_pipeline.py:103` 对此用 `binary_cross_entropy_with_logits` → 内部再做一次 sigmoid → **double sigmoid**

### 额外发现：模型内部的 double sigmoid

| 文件:行号 | 问题 |
|-----------|------|
| `action_head.py:623` (GPTDecoderActPad.forward) | `nn.functional.sigmoid(self.gripper(x))` 其中 `self.gripper = MLPSigmoidHead(...)` — MLPSigmoidHead 已含 Sigmoid 层，外面又套了一层 sigmoid |

`GPTDecoderActPad` 目前**未被 factory 使用**（factory 用的是 `GPTDecoder`，其 forward 中 `gripper = self.gripper(x)` 无额外 sigmoid，是正确的）。但如果未来有人切到这个类会踩坑。

### importance_margin_vla_compress 项目

两台服务器（westd-41074、cqa1-33015）均**未找到** `binary_cross_entropy_with_logits` 或 `BCEWithLogitsLoss` 调用，无此类 bug。

### 影响评估

- `test_train_pipeline.py` 是测试脚本，不影响正式训练实验结果，但会导致测试中 gripper loss 信号被压缩，测试结论不可靠。修复方式：将两处 `binary_cross_entropy_with_logits` 改为 `binary_cross_entropy`。
- `GPTDecoderActPad:623` 是潜在 bug，当前不影响任何实验。

---
