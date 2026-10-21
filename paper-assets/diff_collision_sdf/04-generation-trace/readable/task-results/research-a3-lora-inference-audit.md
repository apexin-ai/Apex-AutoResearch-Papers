# research a3 lora inference audit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_a3_lora_inference_audit_20260522T095138_result.json`
- **Structured JSON:** [`233a45ae611e07598600.json`](../../sessions/23/233a45ae611e07598600.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the information needed for the audit. Here's the complete analysis.

---

## 审计结果

### 1. LoRA 参数对齐对比

**训练保存 (train_a3_hook.py:365)**:
```python
lora_state = {f"lora_param_{i}": p.data for i, p in enumerate(self.lora_params)}
```

**Eval 加载 (eval_safelibero.py:504-508)**:
```python
lora_state = torch.load(lora_path, map_location="cuda")
for i, p in enumerate(lora_params):
    key = f"lora_param_{i}"
    if key in lora_state:
        p.data.copy_(lora_state[key])
```

| 检查项 | 训练 | Eval | 一致性 |
|--------|------|------|--------|
| TARGET_MODULES | `("q_proj","k_proj","v_proj","o_proj","gate_proj","up_proj","down_proj")` | 相同 | ✓ |
| 遍历顺序 | pali layers → expert layers, 每层按 TARGET_MODULES 顺序 | 相同 | ✓ |
| Pali 路径 | `.paligemma_with_expert.paligemma.language_model.layers` | 相同 | ✓ |
| Expert 路径 | `.paligemma_with_expert.gemma_expert.model.layers` | 相同 | ✓ |
| Rank/Alpha | pali=16/16, expert=32/32 | 相同 | ✓ |
| 总参数数 | 504 | 504 | ✓ |
| key 格式 | `lora_param_{i}` | `lora_param_{i}` | ✓ |
| dtype | float32 | float32 | ✓ |

**LoRA 参数加载通路本身没问题。**

### 2. Checkpoint 内容验证

504 个参数，shapes 符合预期：
- PaliGemma (18层 × 7模块 × 2 = 252): rank-16 shapes `[2048,16]`/`[16,X]`
- Expert (18层 × 7模块 × 2 = 252): rank-32 shapes `[1024,32]`/`[32,X]`
- lora_B std ≈ 0.003（非零，已从初始化的 0 训练偏移），确认 LoRA 参数被训练过

### 3. LoRA forward 是否参与 inference

✓ `_inject_lora` 用 `setattr` 替换 `nn.Linear` → `LoRALinear`，forward 时：
```python
base_out = self.base(x)
lora_out = (x.float() @ self.lora_A @ self.lora_B) * self.scaling
return base_out + lora_out.to(base_out.dtype)
```
LoRA 确实参与了 forward。`_merge_lora` 只定义未调用。

### 4. **根本问题：Norm Stats 不匹配** (CRITICAL BUG)

`_load_policy_a3` (eval_safelibero.py:489-490):
```python
policy = _policy_config.create_trained_policy(
    a3_config, PI0_BASE_WEIGHTS, default_prompt=None
)
```

`create_trained_policy` 从 `checkpoint_dir/assets/` 加载 norm_stats (policy_config.py:64)。这里 `checkpoint_dir = PI0_BASE_WEIGHTS`，所以加载的是 **pi0_base 的 norm_stats**，而非 A3 训练数据的 norm_stats。

**两套 norm_stats 对比**：

| 字段 | pi0_base (eval 使用) | A3 训练 (正确值) | 偏差 |
|------|---------------------|-----------------|------|
| state[2] mean (ee_z) | **0.196** | **1.023** | **5.2x** |
| state[1] mean (ee_y) | -0.038 | 0.132 | 方向相反 |
| action[0] std | 0.203 | 0.506 | 2.5x |
| action[2] mean | -0.032 | -0.162 | 5x |

**影响**：模型收到的 normalized state 完全错误。例如真实 ee_z=1.0：
- pi0_base norm: (1.0 - 0.196) / 0.085 = **9.46**
- 正确 norm: (1.0 - 1.023) / 0.089 = **-0.26**

模型输出的 action 也用错误的 stats 反归一化，导致 action 幅度极小 → displacement 0.0009m。

### 5. 修复建议

`create_trained_policy` 已有 `norm_stats` 参数可覆盖默认加载。修改 `_load_policy_a3`：

```python
def _load_policy_a3(args, config):
    from openpi.training import checkpoints as _checkpoints
    
    a3_model_config = pi0_config.Pi0Config(
        paligemma_variant="gemma_2b",
        action_expert_variant="gemma_300m",
    )
    a3_config = dataclasses.replace(config, model=a3_model_config)
    
    # FIX: 从 A3 checkpoint 加载 norm_stats，而非 pi0_base
    sdf_ckpt = args.sdf_checkpoint or args.checkpoint
    a3_norm_stats = _checkpoints.load_norm_stats(
        os.path.join(sdf_ckpt, "assets"), "safelibero_spatial"
    )
    
    policy = _policy_config.create_trained_policy(
        a3_config, PI0_BASE_WEIGHTS, default_prompt=None,
        norm_stats=a3_norm_stats,  # 传入正确的 norm_stats
    )
    # ... 后续 LoRA 注入和加载不变
```

### 6. 次要问题

- **LoRALinear forward 微小差异**：训练版显式 `.float()` 转换 lora_A/lora_B，eval 版未显式转换。因 lora 参数已是 float32，功能上等价，不影响结果。
- **LoRA 参数 device**：eval 版在 CPU 创建 lora 参数，通过 `p.data.copy_()` 加载后再 `.cuda()`。功能正确但可简化。

### 结论

**LoRA 加载通路本身完全正确**（参数名、顺序、dtype、数量全部对齐）。根本原因是 **norm_stats 来源错误**：eval 从 pi0_base 加载了原始 LIBERO 数据集的归一化统计量，而模型是在 SafeLIBERO 数据上训练的，两者的状态分布差异极大。修复后 displacement 应显著恢复。

---
