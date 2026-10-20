# code add grad monitor

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add-grad-monitor_20260519T212023_result.json`
- **Structured JSON:** [`f0356c90583b69dacf42.json`](../../sessions/f0/f0356c90583b69dacf42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。Step 0 输出了 GRAD MONITOR 行：

```
[GRAD MONITOR step 0] L_consist=0.317805 | consist_grad_norm=1.850666 | total_grad_norm=41.040445 | grad_ratio=0.0451
```

所有数值非零非 NaN，符合预期：
- `L_consist=0.317805` — 一致性损失值
- `consist_grad_norm=1.850666` — consist loss 单独的梯度范数
- `total_grad_norm=41.040445` — 总 loss 梯度范数
- `grad_ratio=0.0451` — consist 梯度占总梯度的 ~4.5%，说明当前 alpha=0.1 下 consist loss 的梯度贡献较小，符合正则项的预期行为

### 代码变更摘要

在 `finetune_afford.py` 的 backward 区域（原 L417-423）做了以下修改：

1. **前移** `gradient_step_idx` / `log_step` 计算到 backward 之前
2. **每 100 steps** 执行双 backward：
   - 先 `(alpha * L_consist).backward(retain_graph=True)` 计算 consist-only 梯度范数
   - 再 `normalized_loss.backward()` 计算 total 梯度范数
   - 打印 `[GRAD MONITOR step N]` 行
3. **其余 steps** 走原有单 backward 路径，无性能影响

---
