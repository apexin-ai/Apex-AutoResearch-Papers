# diag openpi native eval

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_openpi_native_eval_20260516T134116_result.json`
- **Structured JSON:** [`ca0bc1085e2b9bab14c6.json`](../../sessions/ca/ca0bc1085e2b9bab14c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这是关键分析结果！

**Robot state rotation (axis-angle): [3.14, -0.003, -0.088]**
**Action[0] rotation: [-0.434, 2.126, 0.905]**
**Diff (action - state): [-3.575, 2.129, 0.993]**

分析结论：
- Actions 的 rotation 值 [-0.434, 2.126, 0.905] 既不接近 state rotation (3.14, -0.003, -0.088)，也不是小的 delta values
- 这些 action values 本身就像是 **absolute actions**（绝对目标 EEF 位姿）
- 但 LIBERO env 的 `env.step()` 期望的是 **delta actions**（增量控制）

**根本原因确认：openpi Policy 的 `AbsoluteActions` output transform 将模型的 delta-of-delta 输出转为了 absolute actions，但 LIBERO env 期望 delta actions。**

这意味着我们需要在 action 传入 `env.step()` 之前减去当前 state：`delta_action = action - current_state`（对前 6 维）。

这就是 0% 成功率的根本原因。openpi 原生 eval 脚本 (`examples/libero/main.py`) 使用的是 websocket client-server 模式，其中 server 端的 output 直接被 client 当作 **delta action** 传入 env.step()。所以问题是 `AbsoluteActions` transform 不应该在 inference 输出中被应用，或者说 openpi 原生 eval 脚本直接把模型输出当 delta 用。

让我回看 openpi eval 脚本怎么处理 action 的——它直接用了 `action_chunk = client.infer(element)["actions"]` 然后 `env.step(action.tolist())`。所以 server 端返回的应该是 delta actions。

**结论出来了：问题在于 `extra_delta_transform=True` 导致 openpi Policy 输出 absolute actions（state + delta），但 LIBERO env 期望 delta actions。我们不应该把 `AbsoluteActions` 放在 output transform 里，或者需要在 env.step 前做 state 减法。**

## 最终产出总结

1. **pi0_libero 训练的 task suite**：`physical-intelligence/libero` 数据集（包含所有 LIBERO suites：spatial, object, goal, 10, 90）。README 推荐用 `libero_object` 做 eval。

2. **evaluate_libero_plus.py 用的 task suite**：默认 `libero_spatial`（第469行 `--task_suite` 参数默认值）。

3. **两者是否匹配**：训练数据包含所有 suite，所以在任何 suite 上 eval 都应该能工作。但更重要的是：

4. **openpi 原生 eval 结果**：用 openpi 原生 Policy 完整 transform chain 跑，两个 suite 都是 **0%**。

5. **0% 的根本原因**：`extra_delta_transform=True` 导致 output chain 中有 `AbsoluteActions` transform，将模型输出从 delta-of-delta 转为 absolute actions（目标 EEF 位姿）。但 LIBERO env.step() 期望的是 **delta actions**（增量）。模型输出 rotation ~2.1 被直接当作 delta rotation 传入，导致机器人剧烈抖动而非精细操作。

**修复方案**：从 output_transforms 中移除 `AbsoluteActions`，或者在 `env.step()` 前将 action 减去当前 state（对前 6 维，gripper 保持 absolute）。

---
