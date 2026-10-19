# code exp028ab parallel config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp028ab_parallel_config_20260515T210955_result.json`
- **Structured JSON:** [`71741fc5a75ccfaf2bf1.json`](../../sessions/71/71741fc5a75ccfaf2bf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是产出总结：

---

## 产出

### 1. 文件清单

| 文件 | 路径 |
|------|------|
| exp028a config | `RAGEN/config/_alfworld_exp028a_penalty.yaml` |
| exp028b config | `RAGEN/config/_alfworld_exp028b_minibatch.yaml` |
| exp028a script | `scripts/run_exp028a_penalty.sh` |
| exp028b script | `scripts/run_exp028b_minibatch.sh` |

### 2. exp028a vs exp028b diff（符合预期）

仅 5 处差异：`CUDA_VISIBLE_DEVICES`（0/1）、`ppo_mini_batch_size`（8/32）、`experiment_name`、`local_log_dir`、`default_local_dir`。

### 3. exp027 → exp028a 变更（3 处实质性修改）

| 参数 | exp027 | exp028a |
|------|--------|---------|
| `n_gpus_per_node` | 2 | 1 |
| `CUDA_VISIBLE_DEVICES` | "0,1" | "0" |
| `ppo_mini_batch_size` | **32** | **8** |
| `algorithm.invalid_action_penalty_coef` | 未设（默认0.1） | 0.1（显式） |

### 4. 单卡 vs 双卡适配说明

- exp027 用 **data parallel**（`n_gpus_per_node=2`, `tensor_model_parallel_size=1`），不是 tensor parallel
- 单卡只需 `n_gpus_per_node: 1`，`tensor_model_parallel_size` 已是 1 无需改
- 1.7B 模型 + 96GB 显存单卡完全足够（`gpu_memory_utilization=0.4` ≈ 39GB 给 vLLM，剩余 ~57GB 给 actor/ref）

### 5. Hydra 解析验证通过

- exp028a: 128 rollouts / mini_batch 8 = **16 optimization steps/epoch**
- exp028b: 128 rollouts / mini_batch 32 = **4 optimization steps/epoch**
- `_self_` 警告为 cosmetic，与项目其他 config 一致

### 6. ⚠️ 需要 Director 确认的差异

**任务表说 exp028a `ppo_mini_batch_size=8` "与 exp027 一致"，但 exp027 实际值是 32。** 当前按任务指定值（8）执行。这意味着：
- exp028a（mini_batch=8）：每 epoch 16 次参数更新，每次用 8 样本
- exp028b（mini_batch=32）：每 epoch 4 次参数更新，每次用 32 样本 = 与 exp027 单 epoch 更新次数相同

### 7. GPU 状态

两卡当前各占用 ~41GB（可能是 zero-shot eval 或其他进程），未做实际 dry-run 训练以避免干扰。启动前需确认 GPU 已释放。

---

未启动训练，等 Director 审批。

---
