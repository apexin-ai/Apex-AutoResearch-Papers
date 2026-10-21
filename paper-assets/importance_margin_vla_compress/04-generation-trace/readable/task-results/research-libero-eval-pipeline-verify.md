# research libero eval pipeline verify

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_libero_eval_pipeline_verify_20260516T162347_result.json`
- **Structured JSON:** [`a9183c8a59ca60d2faf4.json`](../../sessions/a9/a9183c8a59ca60d2faf4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是完整的分析报告。

---

## LIBERO Eval Pipeline 验证报告

### [CRITICAL] Bug 1：不存在 LIBERO eval 脚本

**项目中所有 eval 脚本都是为 aloha_sim_insertion 写的，不适用于 LIBERO。**

- `eval_sim.py`：硬编码 `gym_aloha/AlohaInsertion-v0`
- `eval_success_rate.py`：硬编码 `gym_aloha/AlohaInsertion-v0`
- `evaluate.py`：离线 metric 评测（margin/preservation/Lipschitz），不是 success rate

配置文件 `libero_baseline.yaml` 中的 `libero_eval:` 段落有详细的 eval protocol 定义（suites、max_steps、cameras 等），注释中引用了 `eval_success_rate_libero.py`——**但这个文件不存在**。

**影响**：LIBERO 训练完成后，无法评测 success rate。

### [CRITICAL] Bug 2：现有 eval 脚本有 6 处 LIBERO 不兼容

如果直接复制 `eval_success_rate.py` 改 LIBERO，以下硬编码必须全部修改：

| # | 问题 | eval_success_rate.py (aloha) | LIBERO 需要 |
|---|------|------------------------------|-------------|
| 1 | **环境** | `gym_aloha/AlohaInsertion-v0` | `LiberoEnv` (from lerobot/envs/libero.py) |
| 2 | **观测结构** | `obs["pixels"]["top"]` (480×640) | `robot_state` dict + camera images (256×256) |
| 3 | **State 维度** | `obs["agent_pos"]` (14D aloha joints) | eef_pos(3) + axis_angle(3) + gripper_qpos(2) = **8D** |
| 4 | **图像旋转** | 无 | 必须 `torch.flip(img, dims=[2,3])`（180° 旋转，匹配 HuggingFaceVLA/libero 数据集朝向）|
| 5 | **Task text** | `"Insert the peg into the socket.\n"` 固定 | 每个 task 不同的 language description（从 LIBERO suite 获取）|
| 6 | **Max steps** | 400 固定 | 按 suite 不同：spatial=280, object=280, goal=300, libero_10=520 |

### 对比表：官方 vs 我们

| 项目 | 官方 lerobot-eval | 我们（需要写） | 差异 |
|------|-------------------|----------------|------|
| **Action chunk size** | 50 (`config.chunk_size`) | 50 | ✅ 一致 |
| **N action steps** | 50 (`config.n_action_steps`) | 50 (`action_horizon`) | ✅ 一致 |
| **Denoising steps** | 10 (`config.num_steps`) | 10 | ✅ 一致 |
| **ODE solver** | Euler: `x_t = x_t + dt * v_t`, dt=-1/10 | 同上 | ✅ 一致 |
| **Image resize** | 512×512 with padding (`resize_with_pad`) | `prepare_images` 内部处理 | ✅ 一致（SmolVLA 内部） |
| **Image norm** | [0,1]→[-1,1] (SigLIP) | `prepare_images` 内部处理 | ✅ 一致 |
| **Image 180° flip** | `LiberoProcessorStep`: `torch.flip(img, [2,3])` | ❌ **缺失** | **[CRITICAL]** |
| **State preprocessing** | quat→axis_angle + concat (LiberoProcessorStep) | ❌ **缺失** | **[CRITICAL]** |
| **State normalization** | MEAN_STD (via processor pipeline) | 训练时无 normalize → eval 也应无 | ⚠️ 见下文分析 |
| **Action unnormalization** | MEAN_STD (via postprocessor) | 训练时无 normalize → eval 不需要 unnorm | ⚠️ 见下文分析 |
| **Action clipping** | env 内部处理 `[-1, 1]` | `np.clip(action, -1, 1)` | ✅ 一致 |
| **Max episode length** | 按 suite: 280/280/300/520 | ❌ **需要实现** | **[CRITICAL]** |
| **Success criterion** | `env.check_success()` → `info["is_success"]` | `info.get("is_success")` | ✅ 一致（if using LiberoEnv） |
| **Control mode** | `"relative"` | config 中设了 `"relative"` | ✅ 一致 |
| **Init states** | 从 LIBERO benchmark 加载固定 init states | ❌ **需要实现** | **[CRITICAL]** |
| **Cameras** | agentview_image + robot0_eye_in_hand_image | config 中设了 | ✅ 一致 |
| **Per-task language** | 从 suite.tasks[i].language 获取 | ❌ **需要实现** | **[CRITICAL]** |

### ⚠️ 归一化分析

**训练侧**：`train.py` 直接调用 `policy.forward(batch)`，其中 `prepare_state` 只做 padding、不做 MEAN_STD 归一化。`prepare_action` 同样只 padding。即**模型是在 raw（未归一化）数据上训练的**。

**Eval 侧影响**：
- ✅ 不需要 state 归一化（与训练一致）
- ✅ 不需要 action 反归一化（与训练一致）
- ⚠️ 但这意味着我们的训练方式与官方 `lerobot-train` 不同。官方 pipeline 的 `NormalizerProcessorStep` 会用 dataset stats 做 MEAN_STD 归一化。如果想复现官方 SmolVLA LIBERO 成绩，需要检查这个差异的影响。

### Sanity Check 状态

**无法执行**：westd-27271 上所有 checkpoint 都是 aloha 实验的，无 LIBERO checkpoint。LIBERO 训练在 cqa1 上进行，checkpoint 尚未同步到 westd。

### 修复建议

需要编写 `eval_success_rate_libero.py`，核心要点：

1. **使用 lerobot 的 LiberoEnv**（非 gym_aloha），支持多 suite/多 task
2. **图像预处理**：从 env 获取 256×256 → flip 180° → `prepare_images` 内部 resize 到 512×512
3. **State 提取**：从 `robot_state` dict 提取 eef_pos(3) + quat→axis_angle(3) + gripper_qpos(2) = 8D
4. **Per-task language**：从 `suite.tasks[i].language` 获取，加 `\n` 后缀
5. **Suite-specific max_steps**：spatial=280, object=280, goal=300, libero_10=520
6. **Init states 加载**：使用 `get_task_init_states(suite, task_id)` 确保可复现
7. **Eval protocol**：10 tasks/suite × 10 episodes/task = 100 episodes/suite

**两种实现路径**：
- **路径 A（推荐）**：直接用 `lerobot-eval` 命令（如果能适配我们的自定义 checkpoint 格式）
- **路径 B**：写自定义脚本，复用 `lerobot.envs.libero.LiberoEnv` 和 `LiberoProcessorStep`，但绕过 lerobot processor pipeline 的归一化（与我们的训练一致）

路径 B 更可控，因为我们的 checkpoint 格式和训练流程与官方 `lerobot-train` 不同。

需要我现在编写这个 eval 脚本吗？

---
