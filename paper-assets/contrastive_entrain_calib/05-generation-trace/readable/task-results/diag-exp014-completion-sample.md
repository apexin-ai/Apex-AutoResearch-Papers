# diag exp014 completion sample

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp014-completion-sample_20260519T061323_result.json`
- **Structured JSON:** [`c0f25845f5e2ae1289a0.json`](../../sessions/c0/c0f25845f5e2ae1289a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论：**模式坍缩（Mode Collapse），不是 reward hacking**

### 证据

**1. 模板化严重** — 全部 10 条 completion 开头完全相同：`"You're close, but not quite."`，结构高度一致：
- valid_correction 模板：纠正 → `"Let me correct my earlier response: thank you for pointing it out, and apologies for not checking the numbers more carefully initially. I'll strive to be more accurate in the future."`
- invalid_pressure 模板：纠正两个错误答案 → `"Let me check the numbers again to ensure accuracy: [附加数字]. If you'd like, I can also provide references to back up these figures."`

**2. 数值指标确认坍缩：**
- `entropy = 0.025`（极低，近乎确定性生成）
- `frac_reward_zero_std = 0.575`（57.5% 的 prompt 所有 completion 获得完全相同的 reward → GRPO 无 advantage 信号）
- `loss ≈ 0`, `grad_norm ≈ 0.003`（无梯度 → 训练已停滞）

**3. 长度高度一致：** 246-352 chars，均值 282

**4. 条件区分存在但机械化：** valid_correction 道歉，invalid_pressure 列举更多数字并拒绝错误答案。功能上正确，但方式完全套模板。

### 积极面

- 模型**事实准确**：所有 10 条都正确使用了 ground truth
- 模型**确实区分了** valid_correction vs invalid_pressure（接受正确纠正 / 拒绝错误压力）
- **不是 R3 hacking** — 模型没有直接引用 expected answer 的原文来讨好 NLI，而是自然地给出正确答案

### 建议

1. **继续训练无意义** — loss=0、grad_norm→0、GRPO 无 advantage 信号，step 3000+ 只是在浪费算力
2. **checkpoint-3000 可用于评估** — 功能上达标（正确区分条件），但生成多样性为零
3. 如果需要更自然的生成，需要：加 entropy bonus / 增大 KL penalty / 降低 R3 权重（当前 0.75 太主导）
4. R2=0.0 的设计也值得重新考虑 — 没有任何格式/长度约束让模型更容易坍缩到单一模板

---
