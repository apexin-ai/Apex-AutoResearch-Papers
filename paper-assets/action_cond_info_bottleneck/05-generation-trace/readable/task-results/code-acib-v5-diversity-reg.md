# code acib v5 diversity reg

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_acib_v5_diversity_reg_20260516T012346_result.json`
- **Structured JSON:** [`ee08faf257a31e56e325.json`](../../sessions/ee/ee08faf257a31e56e325.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有改动已就位，语法验证通过。

---

## 产出

### 1. Diff 总结

**`acib/losses.py`** — 末尾新增 `diversity_regularizer` 静态方法：
```python
@staticmethod
def diversity_regularizer(logits: torch.Tensor) -> torch.Tensor:
    p = torch.sigmoid(logits)           # [B, T]
    return -p.std(dim=-1).mean()        # scalar, 最小化 = 最大化 std
```

**`acib/acib_policy.py`** — 两处改动：
- L22: `__init__` 中添加 `self.stop_grad_task = False`
- L46-55: `_connector_hook` 中，当 `stop_grad_task=True` 时对 weights 做 `.detach()` 再传入 `apply_weights`

**`scripts/train_acib.py`** — 五处改动：
- L153-156: 新增 `--diversity_lambda`（默认 0.0）和 `--stop_grad_task` 参数
- L265: 构建 policy 后设置 `policy.stop_grad_task = args.stop_grad_task`
- L269-270: 打印 diversity_lambda 和 stop_grad_task
- L298-304: backward 前计算 diversity loss 并加到 total_loss
- L330, L344: wandb log 和 print 中加入 `div_loss`

### 2. Stop-gradient 可行性评估

**实现难度**：低。只需一个 `.detach()` 调用，已完成。

**可行性风险**：
- **β warmup 期间（β=0, α=0）**：scorer 完全没有梯度来源 → 权重不更新，前期 scorer 输出随机，task loss 可能不稳定
- **缓解**：配合 `--diversity_lambda > 0` 使用，确保 scorer 始终有梯度信号
- **推荐配置**：`--stop_grad_task --diversity_lambda 0.1 --beta 0.01 --beta_warmup_steps 1000`，保证 warmup 期间 diversity loss 就在驱动 scorer 分化

### 3. 语法验证

```
losses.py OK
acib_policy.py OK
train_acib.py OK
```

---
