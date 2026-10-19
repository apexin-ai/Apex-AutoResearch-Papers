# diag action horizon mismatch

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_action_horizon_mismatch_20260516T124705_result.json`
- **Structured JSON:** [`ca76d13ffe5791809588.json`](../../sessions/ca/ca76d13ffe5791809588.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集完全部信息。以下是完整诊断报告。

---

## 诊断结论：Action Horizon **没有不匹配**

### 1. pi0_libero config.json 完整关键字段

```
chunk_size:           50      (模型每次预测 50 步)
n_action_steps:       10      (openpi 建议执行 10 步后 replan)
action.shape:         [7]     (LIBERO 7-DOF: pos3 + rot3 + gripper)
max_action_dim:       32      (padding 到 32 维)
num_inference_steps:  10      (flow matching 去噪步数)
image_resolution:     [224, 224]
```

### 2. MetaBrain 的 action 输出维度链

| 环节 | 维度 | 来源 |
|------|------|------|
| `Pi0Config(action_horizon=50, action_dim=32)` | 模型输出 `[B, 50, 32]` | `meta_brain_assembly.py:638` |
| `PI0Pytorch.sample_actions()` 生成噪声 → 去噪 | `[B, 50, 32]` | `pi0_pytorch.py:380` |
| `predict_action()` 返回 | `[1, 50, 32]` | `meta_brain_assembly.py:454` |
| `infer()` unnormalize → AbsoluteActions → slice | `[50, 7]` | `meta_brain_assembly.py:584-590` |

**50 步来自 `Pi0Config.action_horizon=50`**，与 pi0_libero 的 `chunk_size=50` 完全匹配。

### 3. Eval loop 逻辑

`evaluate_libero_plus.py:74,312-328`:
```python
REPLAN_STEPS = 5

action_chunk = result["actions"]           # [50, 7]
action_plan.extend(action_chunk[:REPLAN_STEPS])  # 只用前 5 步
# 逐步执行：action = action_plan.popleft() → env.step(action)
# queue 空时重新 infer()
```

- 每次 replan 执行 5 步（比 openpi 推荐的 `n_action_steps=10` 更保守，但不是错误）
- 单步执行，无 action 截断或维度问题

### 4. Openpi 官方 action horizon 默认值

`openpi/src/openpi/models/pi0_config.py:26`:
```python
action_horizon: int = 50   # 默认 50
action_dim: int = 32        # 默认 32
```

MetaBrain 使用的值与默认一致。

### 5. **没有 action horizon 不匹配**

| 配置 | pi0_libero | MetaBrain | Eval | 匹配？ |
|------|-----------|-----------|------|--------|
| chunk_size / action_horizon | 50 | 50 | N/A | ✓ |
| action_dim / max_action_dim | 7→32 | 32→slice to 7 | 7 | ✓ |
| n_action_steps (建议值) | 10 | N/A | REPLAN=5 | ✓（更保守） |
| flow matching steps | 10 | 10 (default) | N/A | ✓ |

### 6. 归一化 / DeltaActions 链验证

追溯了 openpi `create_trained_policy` 的完整 transform 顺序：

**OpenPI 官方推理链**（`policy_config.py`）:
1. Normalize state (MEAN_STD)
2. Model → normalized delta actions
3. **Unnormalize** (actions + state)
4. **AbsoluteActions** `actions[:,:6] += state[:6]`（此时 state 已反归一化）
5. LiberoOutputs: slice to [:7]

**MetaBrain `infer()` 推理链**:
1. `(state - mean) / std` → 归一化 state
2. Model → normalized delta actions `[1,50,32]`
3. `actions * std + mean` → **反归一化**
4. `actions[:,:,:6] += raw_state[:6]` → **AbsoluteActions**
5. Slice to `[:, :7]`

两者数学等价。✓

### 7. 但有一个潜在严重 Bug：norm_stats 加载路径

`_load_norm_stats()` 查找顺序：
1. `{checkpoint_dir}/norm_stats.json`
2. `/root/.cache/openpi/.../norm_stats.json` (hardcoded fallback)
3. **回退到恒等归一化**（mean=0, std=1）

| checkpoint | norm_stats.json 位置 | 能找到？ |
|-----------|---------------------|---------|
| `pi0_libero` | `/root/autodl-tmp/checkpoints/pi0_libero/norm_stats.json` | ✓ |
| `pi0_base` (默认) | 不在根目录，在 `assets/physical-intelligence/libero/` 子目录 | **✗ → 恒等归一化** |

**如果用默认 `pi0_base`，归一化全废。** 但 `run_nominal_eval.sh` 指定了 `pi0_libero`，所以正式 eval 应该没问题。

### 8. 修复建议

**Action horizon 不需要修复** — 没有不匹配。

0% eval 的可能根因（需进一步排查）：

**(a) 图像 180° 旋转可能有误** — `evaluate_libero_plus.py:211-212`:
```python
agentview = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
```
openpi 的 `LiberoInputs` 不做任何旋转。如果训练数据不是翻转的，这个操作让模型看到上下颠倒的图像。**建议**：注释掉旋转，对比效果。

**(b) `_load_norm_stats` 加固** — `meta_brain_assembly.py:93`:
添加 `{checkpoint_dir}/assets/*/norm_stats.json` 的搜索路径，避免 pi0_base 场景下回退到恒等归一化。

**(c) 验证 pi0_libero 基线** — 先用 openpi 官方 `Policy` 类（不经过 MetaBrain）跑 LIBERO eval，确认 checkpoint 本身的性能。如果官方 pipeline 也是 0%，则问题在 checkpoint 或 env 而非 MetaBrain。

---
