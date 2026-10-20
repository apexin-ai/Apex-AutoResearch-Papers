# code v2 gradient v1 aligned

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v2-gradient-v1-aligned_20260526T203838_result.json`
- **Structured JSON:** [`5dfbcbb0492ecb51965e.json`](../../sessions/5d/5dfbcbb0492ecb51965e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**修正内容**：
- `run_gradient_analysis_v2.py`：`--num_samples` 默认值 200 → 800（对齐 v1 的 200 batches × bs=4 = 800 samples）
- `compare_gradient_conditions.py`：`--num-samples` 默认值 200 → 800

**方法论对照结论**：除样本数外，v2 与 v1 在所有核心维度完全一致——数据源（真实 RLDS DataLoader）、梯度获取（`torch.autograd.grad` on `vision_backbone.named_parameters()`）、层分组（DINOv2 40 blocks + SigLIP 27 blocks）、L2 norm 计算、cosine similarity。两个不影响结论的差异：Vanilla 条件 OCC head 处理方式不同（功能等价）、v2 缺少 BN drift 记录（不影响梯度数据）。

报告已写入 `artifacts/gradient_v1_v2_methodology_comparison.md`，含完整运行命令（3 个条件的 checkpoint 路径用变量占位）。

---
