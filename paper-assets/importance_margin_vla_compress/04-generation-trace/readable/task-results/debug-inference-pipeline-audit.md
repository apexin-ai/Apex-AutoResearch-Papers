# debug inference pipeline audit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_inference_pipeline_audit_20260516T122642_result.json`
- **Structured JSON:** [`6517a21805268c1a8343.json`](../../sessions/65/6517a21805268c1a8343.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断完成。** 以下是完整结论。

---

## 诊断结果

### Bug #1（确认）: Action 裁剪错误

`eval_success_rate.py` 第 328 行：
```python
action = np.clip(action, -1.0, 1.0)
```

**问题**: 数据集 action 范围 [-1.60, 1.21]，arm joint positions 是弧度值，不受 [-1, 1] 约束。只有 gripper（dim 6, 13）被 normalize 到 [0, 1]。LeRobot 官方 eval 不做 clip。

**影响**: 中-高。截断了必要的关节运动。

**修复**: 删除这行 clip。

---

### Bug #2（核心问题）: Flow Matching ODE 不收敛

对同一输入（seed 0 的 env image）做 5 次推理，shoulder joint 预测从 -0.6 到 -2.2 剧烈波动：
```
Trial 0: -1.700    Trial 1: -1.260    Trial 2: -2.193
Trial 3: -1.625    Trial 4: -0.596
```

**原因**: Flow matching 用 10 步 Euler ODE 积分从 noise → action。模型学到的 velocity field 不够精确，导致不同 noise initialization 收敛到完全不同的 action trajectory。训练 loss=0.003 是在 velocity level 的均值误差，不代表 sample quality 好。

**影响**: 致命。即使在训练数据配置上，单次预测也不可靠。50步 open-loop 执行让误差无法纠正。

---

### Bug #3（核心问题）: 对未见/略异配置 mode collapse

Seed 42 的 env image 和 seed 0 仅差 0.35%（peg/socket 位置不同）。模型行为：
- Seed 0: 输出范围 [-1.7, 1.3]（合理但高方差）
- Seed 42: 输出范围 [-0.15, 0.73]（坍缩到全局均值，5次试验一致）

**原因**: 50 episodes 训练数据不足以泛化到所有 peg/socket 配置。模型对视觉 token 中的 peg/socket 位置极度敏感——未见配置直接触发 mean regression。

---

### 非 Bug（已排除）

| 检查项 | 结果 |
|--------|------|
| Action unnormalization 缺失 | ✗ 不是 bug。训练 bypass 了 SmolVLA 的标准 normalization pipeline，eval 和训练一致 |
| Obs preprocessing (image) | ✓ 一致。训练/eval 都是 [0,1] float32 CHW，`prepare_images` 统一处理 |
| Obs preprocessing (state) | ✓ 一致。raw joint positions，`prepare_state` 只做 padding |
| Task text | ✓ 一致。"Insert the peg into the socket.\n" |
| Action chunk size / horizon | ✓ n_action_steps=50 是 SmolVLA 标准配置 |
| Image mismatch (env vs dataset) | ✓ 对于相同 seed，像素差仅 0.0027 |

---

### 修复建议

1. **立即修复**: 删除 `np.clip(action, -1.0, 1.0)`
2. **关键改进**: 增加 flow matching ODE steps（当前 10 步太少）或降低 temperature（使用 0.0 = 确定性 ODE）
3. **根本性改进**: 增加训练数据多样性（更多 episodes），或使用 SmolVLA 标准的 normalization pipeline（MEAN_STD）使模型对输入分布变化更鲁棒

---
