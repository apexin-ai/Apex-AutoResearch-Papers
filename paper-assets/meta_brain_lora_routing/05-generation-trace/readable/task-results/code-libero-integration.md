# code libero integration

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_libero-integration_20260515T112200_result.json`
- **Structured JSON:** [`3fe71525c089576d6604.json`](../../sessions/3f/3fe71525c089576d6604.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件都已完成且编译通过。

**`libero_integration.py`** (324行) 提供：

| 函数 | 功能 |
|------|------|
| `load_pi0_for_collection(checkpoint_path, device)` | 通过 OpenPI `create_trained_policy` 加载模型，返回 `(policy, model)` —— policy 负责推理+变换，model 用于 hook 注册 |
| `obs_to_model_input(obs, task_description)` | LIBERO obs → OpenPI 输入格式：图像 180° 翻转 + resize_with_pad 224×224，state = eef_pos(3) + quat→axisangle(3) + gripper(2) |
| `create_libero_env(task_suite, perturbation_type)` | 按扰动类型过滤 LIBERO-Plus 任务（通过 BDDL 文件名后缀匹配），创建 `OffScreenRenderEnv` |
| `run_episode(policy, collector, perturbation_type, device)` | 完整 episode rollout：init_state → settling → action chunking (replan_steps=5) → 收集每次推理的激活并平均 |

**关键设计决策：**
- 使用 `policy.infer()` 而非直接调 `model.sample_actions()`，因为 policy 封装了完整的变换链（LiberoInputs → Normalize → TokenizePrompt → PadStatesAndActions → ResizeImages）和归一化统计量
- hooks 注册在 policy 内部的同一个 model 实例上，`policy.infer()` 调用 `model.sample_actions()` 时自动触发
- `sensor_noise` 类型通过图像后处理实现（高斯噪声+亮度抖动），其他 5 种通过 LIBERO-Plus 任务名后缀过滤
- `_extract_model()` 从 Policy 对象中提取 nn.Module，兼容多种可能的属性名

**`collect_activations.py`** 更新：三个 stub 函数替换为 `libero_integration` 导入，`collect()` 改用 `(policy, model)` 模式。

---
