# code dual critic implementation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dual_critic_implementation_20260520T223251_result.json`
- **Structured JSON:** [`2ef6ac275ba33ae738de.json`](../../sessions/2e/2ef6ac275ba33ae738de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Implementation complete and verified. Here's the summary:

## 修改摘要

### configs.yaml (+1 line)
- 在 `defaults` 的 `critic:` 配置之后添加 `dual_critic: false`（默认关闭）

### models.py (+58 lines: 855→913)

**ImagBehavior.__init__** (Patch 1):
- 当 `dual_critic=True` 时创建 `self.value2`（MLP, 255 bins, symlog_disc，与 `self.value` 完全相同结构但独立初始化）
- 创建 `self._slow_value2`（slow target network）
- 创建 `self._value2_opt`（独立 optimizer）

**_compute_target** (Patch 2):
- 当 `dual_critic=True`：`value = torch.min(self.value(feat).mode(), self.value2(feat).mode())`
- 使用 pessimistic value estimate 计算 lambda-return targets

**_train** (Patches 3, 3b, 4):
- 新增 value2 loss block：独立用 `tools.RequiresGrad(self.value2)` 包裹，使用相同 lambda-return targets 训练
- 新增 `value2_mean/std/min/max` metrics
- 新增 `self._value2_opt` optimizer step

**_critic_baseline** (Patch 5, 新方法):
- Helper method：返回 `min(value.mode(), value2.mode())` 或单个 `value.mode()`
- 用于 `_compute_actor_loss` 的 reinforce/both 模式

**_compute_actor_loss** (Patch 5b):
- reinforce/both 模式中将 `self.value(imag_feat[:-1]).mode()` 替换为 `self._critic_baseline(imag_feat[:-1])`

**_update_slow_target** (Patch 6):
- 同步更新 `_slow_value2` 的 EMA

### 关键设计决策
1. `min` 操作在 symexp decode 后的标量 mode 上执行（不是 distribution level）
2. 两个 critic 使用相同 lambda-return targets 但独立参数/梯度
3. `dual_critic=false` 时行为完全不变（所有路径 gated by `getattr(..., 'dual_critic', False)`）
4. networks.py 无需修改（`MLP` 类已足够通用）

---
