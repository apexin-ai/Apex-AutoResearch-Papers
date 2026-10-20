# code fix spatial normalize

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-spatial-normalize_20260519T234535_result.json`
- **Structured JSON:** [`f81d7b3880fc3c34a3b7.json`](../../sessions/f8/f81d7b3880fc3c34a3b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 2 已释放。

## 修改总结

### 修改的文件

**1. `affordance_decoder.py`**
- `__init__`: 新增 `transfer_proj` — `Flatten → Linear(16, 128) → ReLU → Linear(128, 128)`，SimCLR 风格 2 层 MLP
- `forward_with_features()`: 不再返回 64-ch 中间特征。改为在 `up_blocks` 全部执行完毕后（pre-softmax logit map, shape `(B,1,H,W)`），用 `F.adaptive_avg_pool2d(h, (4,4))` 保留 4×4 空间网格，返回 `(B, 1, 4, 4)` features
- 新增参数量：16×128 + 128 + 128×128 + 128 = 18,688（可忽略）

**2. `finetune_afford_transfer.py`**
- 移除 `spatial_normalize` import
- 训练循环中 `z = spatial_normalize(features.float())` 替换为：
  ```python
  z = afford_decoder.module.transfer_proj(features)
  z = F.normalize(z.float(), dim=1)
  ```
- `transfer_proj` 参数已自动包含在 `afford_decoder.parameters()` 中，无需修改 optimizer

**3. `transfer_loss.py`** — 未修改（`spatial_normalize` 函数保留但不再被调用）

### Dry-run 结果

```
Step 0: L_xfr=0.000000  pos=0  Q=2
Step 1: L_xfr=0.000000  pos=0  Q=4
Step 2: L_xfr=0.000000  pos=0  Q=6
Step 3: L_xfr=1.630641  pos=1  Q=8   ← 首个正样本对
Step 4: L_xfr=0.000000  pos=0  Q=10
Step 5: L_xfr=0.000000  pos=0  Q=12
```

- **L_transfer 不再锁死 4.174**。Step 3 出现正样本对时 L_xfr=1.63，低于当时 queue size 对应的 chance level（log(~7)≈1.95），说明 InfoNCE 能区分空间模式
- **dec_gnorm=0.0 (step 0)**：因为 lambda_H=0 且 step 0 无正样本对，decoder 在该步无梯度源——正常现象，正式训练中 queue 填充后正样本频率会上升
- 无 traceback，5 步全部完成
- afford_decoder 参数量：1,724,481（含 transfer_proj 的 18,688）

---
