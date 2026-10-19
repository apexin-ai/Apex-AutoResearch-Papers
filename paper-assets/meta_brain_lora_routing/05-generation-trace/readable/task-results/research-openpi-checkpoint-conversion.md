# research openpi checkpoint conversion

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_openpi_checkpoint_conversion_20260516T141429_result.json`
- **Structured JSON:** [`78622f472e637a7557c4.json`](../../sessions/78/78622f472e637a7557c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。以下是完整分析结果：

---

## P1：训练加载 vs Eval 加载对比

### 1. 训练日志 — 无 missing/unexpected key warnings

```
Loaded checkpoint: 778 keys, format=LeRobot, filtered 6 norm buffers
```
训练日志完全干净，无任何 missing/unexpected key 告警。

### 2. 加载函数差异

| | `train_lora_expert.py:153` `load_pi0_model` | `meta_brain_assembly.py:279` `_load_pi0_checkpoint` |
|---|---|---|
| **strict** | `strict=True` | `strict=False` |
| **embed_tokens 处理** | 显式从 lm_head 复制 → embed_tokens（line 182-183） | 不复制，接受 missing embed_tokens，依赖 HF 模型 weight tying |
| **norm buffers** | 过滤丢弃（line 171-173） | 提取保存到 norm_buffers dict 供后续使用 |
| **prefix stripping** | 相同：`removeprefix("model.")` | 相同 |

**功能等价性**：两者等价。PI0Pytorch 内部的 `PaliGemmaForConditionalGeneration` 自动 tie weights（`_tied_weights_keys = ["lm_head.weight"]` at `modeling_paligemma.py:387`），所以 eval 的 `strict=False` + missing embed_tokens 实际上不影响正确性。load_state_dict 写入 lm_head.weight 时，embed_tokens.weight 已指向同一 tensor。

### 3. key remapping 逻辑

**无需外部 remapping 函数。** 两套代码做的是同一件事：
1. 过滤 norm buffers (`normalize_inputs.*`, `normalize_targets.*`, `unnormalize_outputs.*`)
2. Strip `model.` prefix
3. （仅 train）显式恢复 tied embed_tokens

---

## P2：openpi 正确加载 pi0_libero 的完整路径

### 关键文件和函数

| 文件 | 行号 | 角色 |
|------|------|------|
| `openpi/src/openpi/training/config.py:653-677` | `pi0_libero` TrainConfig 定义 | 使用 `LeRobotLiberoDataConfig(extra_delta_transform=True)` |
| `openpi/src/openpi/training/config.py:282-355` | `LeRobotLiberoDataConfig.create()` | 构建 data_transforms 包含 DeltaActions/AbsoluteActions |
| `openpi/src/openpi/training/weight_loaders.py:42-56` | `CheckpointWeightLoader` | 从 Flax params 格式加载（非 safetensors） |
| `openpi/src/openpi/transforms.py:204-222` | `DeltaActions` | 训练输入 transform: `actions[:6] -= state[:6]` |
| `openpi/src/openpi/transforms.py:226-244` | `AbsoluteActions` | 推理输出 transform: `actions[:6] += state[:6]` |
| `openpi/src/openpi/policies/libero_policy.py` | `LiberoInputs` / `LiberoOutputs` | 数据格式转换，`LiberoOutputs` 只截取前 7 维 |

### openpi 原生没有 LeRobot→PI0Pytorch key remapping

openpi 原生使用 **JAX/Flax** 格式（`gs://openpi-assets/checkpoints/pi0_base/params`），内部用 `flax.traverse_util` 操作。没有 safetensors key remapping 函数——那是我们 PyTorch 代码自己做的事。

### DeltaActions / AbsoluteActions 完整逻辑

openpi `pi0_libero` config（line 338-343）：
```python
if self.extra_delta_transform:
    delta_action_mask = _transforms.make_bool_mask(6, -1)  # [True]*6 + [False]
    data_transforms = data_transforms.push(
        inputs=[_transforms.DeltaActions(delta_action_mask)],
        outputs=[_transforms.AbsoluteActions(delta_action_mask)],
    )
```

**训练时** `DeltaActions`：`actions[:, :6] -= state[:6]` — 从前6维动作中减去当前 state  
**推理时** `AbsoluteActions`：`actions[:, :6] += state[:6]` — 将 state 加回去

配合 norm stats 的完整推理链：
```
model_output → unnormalize(×std + mean) → AbsoluteActions(+state[:6]) → LiberoOutputs([:7]) → env.step()
```

---

## P2.5：AbsoluteActions / extra_delta_transform 正确使用

### LIBERO 动作空间
LIBERO actions 是 7D **delta**（相对运动）：`[dx, dy, dz, dax, day, daz, gripper]`

### 完整数据流

```
原始 delta_actions
    ↓ DeltaActions: -= state[:6]
"double delta" (delta - state)
    ↓ normalize: (x - mean) / std
model 学习空间
    ↓ sample_actions (flow-matching 去噪)
model 输出
    ↓ unnormalize: x * std + mean
"double delta" 还原
    ↓ AbsoluteActions: += state[:6]
原始 delta_actions（env.step() 可直接用）
```

### 关于 "openpi 原生 eval 0%" 的分析

数学上，AbsoluteActions 是 DeltaActions 的精确逆运算，产出的 IS delta actions（不是绝对位姿）。如果 LIBERO actions 确实是 deltas，那么 `output + state = (delta - state) + state = delta`。

**0% 的可能根因不是 AbsoluteActions 产生绝对位姿，而是：**

1. **我们的 eval 代码 `use_delta` 设置错误**：`_build_norm_stats()` 检测到 LeRobot 格式的 embedded buffers 时返回 `use_delta=False`，导致 AbsoluteActions **未被执行**。模型输出被 unnormalize 后仍在 (delta-state) 空间，没有加回 state，直接送入 env → 动作全错。

2. **norm_stats 来源不一致**：如果 embedded buffers（来自 PI 原始训练）和 JSON norm_stats（可能是我们重新计算的）有差异，会导致 unnormalize 结果偏移。

### 核心 bug 定位

`meta_brain_assembly.py:257-266`：
```python
# LeRobot 格式 → use_delta = False → 不执行 AbsoluteActions
return { ..., "use_delta": False }
```

但 pi0_libero 是用 `extra_delta_transform=True` 训练的，**必须** `use_delta=True` 才能正确还原动作。

**修复建议**：对 pi0_libero checkpoint，应强制 `use_delta=True`，或在 `from_checkpoints` 中增加参数让调用者显式指定。

---
