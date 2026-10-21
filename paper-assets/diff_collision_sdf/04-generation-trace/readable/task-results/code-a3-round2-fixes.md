# code a3 round2 fixes

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_a3_round2_fixes_20260519T234851_result.json`
- **Structured JSON:** [`d24ad103b4e11e2640b2.json`](../../sessions/d2/d24ad103b4e11e2640b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改完成，语法检查通过。

---

## 修复报告

### Fix 1: LoRA rank 分模块设置

**改动文件**: `scripts/train_a3_hook.py`

| 位置 | 改动 |
|------|------|
| L108-136 | `inject_lora` 函数签名改为 `(model, pali_rank=16, pali_alpha=16.0, expert_rank=32, expert_alpha=32.0)`，分别对 PaliGemma 和 Action Expert 使用不同 rank/alpha，返回 `(all_params, pali_params, expert_params)` 三元组 |
| L230-231 | 调用处改为 `inject_lora(_m, pali_rank=16, pali_alpha=16.0, expert_rank=32, expert_alpha=32.0)` |
| L242-250 | 日志分别打印 PaliGemma (rank=16) 和 Action Expert (rank=32) 的参数量 |

**参数量估算** (与 baseline openpi `gemma_2b_lora` / `gemma_300m_lora` 一致):
- PaliGemma (Gemma 2B, 18层, width=2048, rank=16): ~19.6M LoRA params
- Action Expert (Gemma 300M, 18层, width=1024, rank=32): ~13.9M LoRA params
- 总计: ~33.5M (原来 uniform rank=32 是 ~53M，VLM 侧减半)

**A1 不受影响**: A1 使用 openpi 内建 LoRA (`gemma_2b_lora` / `gemma_300m_lora`)，rank 本身就是正确的。

### Fix 2: Phase 2 LoRA warmup 死代码修复

**问题根因**: `on_step_start` 在 `optim.zero_grad(set_to_none=True)` 之后执行，此时 `p.grad` 全为 `None`，`p.grad.mul_(scale)` 永远不生效。

**修复方案**: 用 `p.register_hook(lambda grad, s=self: grad * s._lora_warmup_scale)` 替代。gradient hook 在 `backward()` 计算梯度时触发，scale 由 `on_step_start` 每步更新，效果等价于 LR warmup。

**改动文件**:

| 文件 | 位置 | 改动 |
|------|------|------|
| `train_a3_hook.py` | L267-275 | Phase 2 转换时注册 gradient hooks，warmup 100 步 |
| `train_a3_hook.py` | L288-296 | 替换死代码为 `self._lora_warmup_scale = (steps_in+1)/100`，100 步后移除 hooks |
| `train_a3_hook.py` | L362 | `on_cleanup` 清理 gradient hooks |
| `train_a1_sdf_aux.py` | L149-161 | 同上：注册 gradient hooks，warmup 100 步 |
| `train_a1_sdf_aux.py` | L174-182 | 同上：替换死代码 |
| `train_a1_sdf_aux.py` | L232 | `on_cleanup` 清理 gradient hooks |

**warmup 逻辑确认**:
- Step 5000 (Phase 2 start): `scale = 1/100 = 0.01`
- Step 5099 (第100步): `scale = 100/100 = 1.0`
- Step 5100: 移除所有 gradient hooks，LoRA 梯度不再被缩放

---
