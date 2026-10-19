# prepare fsdp hf and ood eval pipeline

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prepare_fsdp_hf_and_ood_eval_pipeline_20260521T123919_result.json`
- **Structured JSON:** [`9d245ceb623b93de2a69.json`](../../sessions/9d/9d245ceb623b93de2a69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。汇总报告如下：

---

## 汇总报告

### 1. FSDP→HF 转换脚本

- **路径**: `/root/cost-verify-agent-rl/scripts/convert_fsdp_to_hf.py` (5786 bytes, May 14)
- **用法**:
  ```bash
  python convert_fsdp_to_hf.py \
    --input-dir /root/autodl-tmp/checkpoints/exp029-seedN/global_step_X/actor \
    --output-dir /root/autodl-tmp/checkpoints/exp029-seedN_step_X_hf \
    --dtype bf16
  ```
- **支持 `--dry-run`**: 仅验证 checkpoint 结构，不写文件
- **依赖**: torch, transformers, accelerate（CPU-only，约 15s）

### 2. Seed 5 v2 step 10 checkpoint — 完整 ✅

| 项 | 值 |
|---|---|
| 路径 | `/root/autodl-tmp/checkpoints/exp029-seed5/global_step_10/actor/` |
| 总大小 | 21 GB |
| FSDP world_size | 2 |
| model shards | `model_world_size_2_rank_{0,1}.pt` (各 3.8 GB) |
| optim shards | `optim_world_size_2_rank_{0,1}.pt` (各 6.4 GB) |
| huggingface/ | config.json, tokenizer files — 齐全 |

### 3. Seed 6 当前 checkpoint 状态

- **仅有 `global_step_10`**（21 GB，结构同 Seed 5）
- Seed 6 当前 step 12/15，下一个 checkpoint 在 step 15（最终）
- **⚠️ watchdog 注意**: westd watchdog 会在 `global_step_15` 出现后自动删除 `global_step_10`。如需保留中间 checkpoint 做对比实验，需提前干预

### 4. OOD eval 配置模板关键参数

来源: `_alfworld_sft_baseline_ood_eval.yaml`

| 参数 | 值 |
|---|---|
| val_only | True |
| resume_mode | "disable" |
| OOD tasks | 134 (AlfworldSG_OOD, env_groups=134, group_size=1) |
| temperature | 0.4 (val_kwargs.temperature) |
| response_length | 1024 |
| max_model_len | 20480 |
| n_gpus_per_node | 1 |
| gpu_memory_utilization | 0.2 |

**需修改的字段**: `model_path`, `CUDA_VISIBLE_DEVICES`, `experiment_name`, `local_log_dir`/`default_local_dir`

### 5. Watchdog 状态

| 服务器 | PID | 状态 |
|---|---|---|
| westd-47453 | 118779 | **ALIVE** ✅ |
| bjb1-17606 | 313318 | **ALIVE** ✅ |

### 6. 磁盘

westd `/root/autodl-tmp`: 250G 总量，94G 可用（63% 已用）。HF 转换输出约 3.4GB/个，空间充足。

---

## 第一个 Seed 完成后的执行计划

Seed 6 预计最先完成（step 15），步骤：

**Step 1: 确认 step 15 checkpoint 已保存**
```bash
ls /root/autodl-tmp/checkpoints/exp029-seed6/global_step_15/actor/fsdp_config.json
```

**Step 2: FSDP→HF 转换（~15s, CPU-only）**
```bash
cd /root/cost-verify-agent-rl && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python scripts/convert_fsdp_to_hf.py \
  --input-dir /root/autodl-tmp/checkpoints/exp029-seed6/global_step_15/actor \
  --output-dir /root/autodl-tmp/checkpoints/exp029-seed6_step15_hf \
  --dtype bf16
```

**Step 3: 创建 OOD eval 配置**
基于模板创建 `_alfworld_grpo_seed6_step15_ood_eval.yaml`，修改：
- `model_path` → `/root/autodl-tmp/checkpoints/exp029-seed6_step15_hf`
- `experiment_name` → `grpo-seed6-step15-ood-eval`
- `CUDA_VISIBLE_DEVICES` → 按 GPU 白名单选择可用卡
- `local_log_dir`/`default_local_dir` → 对应输出路径

**Step 4: 启动 134-task OOD eval**
单 GPU eval，预计 ~2-3 小时。

**Step 5: 并行处理 Seed 5 step 10**
在 Seed 6 eval 运行期间，同步执行 Seed 5 的 FSDP→HF 转换 + OOD eval（用另一张 GPU）。

**Step 6: Seed 4/7 完成后重复 Step 1-4**

**注意事项**:
- Seed 5 只有 step 10（OOM 终止），watchdog 不会删除它（因为 step 15 永远不会出现）
- Seed 6 的 step 10 会被 watchdog 删除——如需保留须在 step 15 保存前备份或停止 watchdog
- westd 有 4 GPU 可用，可同时跑 2 个 eval（各占 1 GPU）

---
