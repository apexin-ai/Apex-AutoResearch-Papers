# ops scienceworld grpo preflight

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scienceworld_grpo_preflight_20260520T095834_result.json`
- **Structured JSON:** [`231b78b04233dff19251.json`](../../sessions/23/231b78b04233dff19251.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Pre-flight 检查结果

| # | 检查项 | 状态 | 详情 |
|---|--------|------|------|
| 1 | Config: `_scienceworld_cell_a_grpo.yaml` | **PASS** | 存在，2283 bytes，今天 14:31 更新 |
| 1 | Config: `_scienceworld_cell_c_grpo.yaml` | **PASS** | 存在，2276 bytes，今天 14:33 更新 |
| 2 | SFT Checkpoint | **PASS** | `model_path` 指向 `/root/autodl-tmp/checkpoints/scienceworld_sft/huggingface/`（非 `global_step_448`），内含 2 个 safetensors 分片 + config.json + tokenizer 全套文件 |
| 3 | 磁盘空间 | **PASS** | `/root/autodl-tmp/` 剩余 **61GB**，GRPO 预估需 ~50GB，余量充足 |
| 4 | GPU 环境 | **PASS** | 2× NVIDIA RTX PRO 6000 Blackwell，PyTorch CUDA 正常 |
| 5 | `envs.yaml` 含 ScienceWorldSG | **PASS** | 位于 `config/envs.yaml`，定义了 `env_type: scienceworld`, `max_actions_per_traj: 100` |
| 6 | Dry-run Config 加载 | **PASS** | Hydra compose 成功，`experiment_name = scienceworld-cell-a-h2`（有 Hydra version_base 警告，不影响运行） |

**6/6 全部通过，无 blocker。** Cell A 就绪，eval_v2 完成后可零延迟提交。

---
