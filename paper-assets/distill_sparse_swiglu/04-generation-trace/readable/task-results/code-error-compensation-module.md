# code error compensation module

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_error-compensation-module_20260515T163847_result.json`
- **Structured JSON:** [`7fa0fef9ad0808a93641.json`](../../sessions/7f/7fa0fef9ad0808a93641.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。新增两个文件：

**`src/compensation.py`** — `ErrorCompensation` 类：
- `calibrate(wrapper, data_loader, device, num_batches)` — 用校准数据跑 dense forward，计算每层 SwiGLU 中间激活的 channel-wise 均值
- `compensate(intermediate, mask, layer_idx)` — 对 masked 神经元用均值替代：`out = x * mask + mean * (1 - mask)`
- `save(path)` / `load(path)` — 序列化/反序列化

**`tests/test_compensation.py`** — 12 个单元测试全部通过：
- mask 全 1 → 输出等于原始
- mask 全 0 → 输出等于均值
- 部分 mask → 保留通道不变、裁剪通道等于均值
- 不同层用不同补偿向量
- 缺失层回退到无补偿
- save/load 一致性
- bfloat16 兼容、1D mask 广播、零均值边界

与现有 `PredictorWrapper` 的集成点：在 `patched_forward` 的 `intermediate = intermediate * mask` 之后、`down_proj(intermediate)` 之前，调用 `compensation.compensate(intermediate, mask, layer_idx)` 替换即可。

---
