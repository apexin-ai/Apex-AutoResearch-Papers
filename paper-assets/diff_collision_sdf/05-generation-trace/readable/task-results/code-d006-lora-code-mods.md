# code d006 lora code mods

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d006_lora_code_mods_20260520T204944_result.json`
- **Structured JSON:** [`6665065a8c9faaaead57.json`](../../sessions/66/6665065a8c9faaaead57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

---

## 产出汇报

### 1. lora_utils.py 完整内容

`/root/colliforce-vla/colliforce/lora_utils.py` — 包含：
- `LoRALinear(nn.Module)` — 冻结 base weight，只训练 lora_A/lora_B
- `inject_lora(module, lora_rank, lora_alpha, target_modules)` — 通用函数，遍历任意 nn.Module 替换匹配的 nn.Linear
- `inject_lora_pi0(model, pali_rank, pali_alpha, expert_rank, expert_alpha)` — Pi0 专用便捷函数，分别对 PaliGemma 和 Action Expert 注入不同 rank

### 2. train_baseline.py 修改 diff 摘要

- 新增 `sys.path.insert` 父目录（for colliforce imports）
- 新增 import: `TrainHooks`, `train_loop`, `inject_lora_pi0`
- 新增 `BaselineLoRAHooks(TrainHooks)` 类：
  - `on_model_created`: 注入 LoRA，冻结所有非 LoRA 参数
  - `on_step_start`: 前 100 步每 10 步打印可训练参数统计
- `build_config`: `gemma_2b_lora` → `gemma_2b`, `gemma_300m_lora` → `gemma_300m`, 移除 `freeze_filter`
- `main()`: 创建 `BaselineLoRAHooks()` 并传给 `train_loop(config, hooks=hooks)`

### 3. train_a1_sdf_aux.py 修改 diff 摘要

- 新增 import: `from colliforce.lora_utils import inject_lora_pi0`
- `on_model_created`: 冻结所有参数后，调用 `inject_lora_pi0` 注入 LoRA（Phase 1 保持冻结），然后解冻 SDF decoder + EE extractor
- `on_step_start`: Phase 2 改为直接遍历 `self.lora_params` 解冻（不再用 name-based 搜索）；新增前 100 步参数验证打印
- `build_config`: `gemma_2b_lora` → `gemma_2b`, `gemma_300m_lora` → `gemma_300m`, 移除 `freeze_filter`

### 4. A3 实际使用的 LoRA 配置

| 参数 | PaliGemma (Gemma 2B) | Action Expert (Gemma 300M) |
|------|---------------------|---------------------------|
| rank | 16 | 32 |
| alpha | 16.0 | 32.0 |
| target_modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj | 同左 |

### 5. 验证结果

| 测试 | 结果 |
|------|------|
| `from colliforce.lora_utils import inject_lora` | OK |
| `python scripts/train_baseline.py --help` | OK |
| `python scripts/train_a1_sdf_aux.py --help` | OK |
| inject_lora 功能测试（FakeModel） | PASSED — 2 层 × 4 模块 × 2 参数 = 16 LoRA params |

---
