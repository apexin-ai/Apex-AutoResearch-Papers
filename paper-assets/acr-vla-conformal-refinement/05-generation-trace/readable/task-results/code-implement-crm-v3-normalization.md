# code implement crm v3 normalization

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_implement-crm-v3-normalization_20260514T183622_result.json`
- **Structured JSON:** [`f50a4854bc7c4ed3c0cf.json`](../../sessions/f5/f50a4854bc7c4ed3c0cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 训练完成。

**结果汇总：**

| | Epoch 1 | Epoch 2 |
|---|---|---|
| train_loss | 0.024353 | 0.018892 |
| val_loss | 0.013509 | 0.010139 |

**修改内容：**

1. **`src/crm.py`** — 3 处修改：
   - `__init__()`: 添加 `register_buffer('input_mean', ...)` 和 `register_buffer('input_std', ...)`
   - `forward()`: 拼接后、进入 `self.net` 前加入 `x = (x - self.input_mean) / (self.input_std + 1e-8)`
   - 新增 `set_normalization_stats(mean, std)` 方法

2. **`src/train_crm.py`** — 1 处修改：
   - 在 `_to_scalar_uf` 定义后、训练循环前，遍历训练集计算 concatenated input 的 per-feature mean/std，调用 `crm.set_normalization_stats()`

**验证通过：**
- 单元测试：buffers 创建/设置/保存/加载/v2 兼容全部 OK
- Normalization stats：mean [-26.9, 5.5], std [0.004, 2.2]（证实 1500x scale 失衡）
- Dry-run 训练：loss 持续下降，2 epoch val_loss 从 0.0135 降到 0.0101

---
