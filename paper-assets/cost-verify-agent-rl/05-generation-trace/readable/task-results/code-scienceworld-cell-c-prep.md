# code scienceworld cell c prep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scienceworld_cell_c_prep_20260522T034623_result.json`
- **Structured JSON:** [`a1d600b9a1cbfdd794b7.json`](../../sessions/a1/a1d600b9a1cbfdd794b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改确认完成。以下是报告：

---

## Cell C GRPO v4 准备报告

### 1. `_is_jvm_dead()` 修复 ✅
- **文件**: `RAGEN/ragen/env/scienceworld/env.py:41`
- **修改**: `(Py4JNetworkError, ConnectionError, OSError, BrokenPipeError)` → `(Py4JError, Py4JNetworkError, ConnectionError, OSError, BrokenPipeError)`
- `Py4JError` 已在 line 6 import，无需额外 import
- JVM heap 默认值同步从 `-Xmx4g` → `-Xmx8g`（line 10）

### 2. SFT Checkpoint ✅
- 路径: `/root/autodl-tmp/checkpoints/scienceworld_sft/huggingface/`
- 大小: 7.6GB (Qwen3-1.7B, 2 shard safetensors)
- Config `model_path` 已正确指向，无需 symlink

### 3. Config 修改详情
新文件: `_scienceworld_cell_c_grpo_v4.yaml`

与原 `_scienceworld_cell_c_grpo.yaml` 的差异：

| 参数 | 原值 | v4 |
|------|------|----|
| `es_manager.train.group_size` | 8 | **16** |
| `es_manager.train.env_groups` | 16 | **8** (保持总量 128 rollouts) |
| `seed.train` | 10000 | **20000** |
| `experiment_name` | scienceworld-cell-c-episode | **scienceworld-cell-c-v4** |
| `local_log_dir` | scienceworld-cell-c/ | **scienceworld-cell-c-v4/** |
| JVM heap (env.py) | -Xmx4g | **-Xmx8g** |
| `entropy_coeff` | 0 (原 config) | **0.001** |

其余参数不变：n_gpus=2, total_steps=15, save_freq=5, lr=1e-6, context_window_mode=full。

### 4. SFT Eval 任务 Success 列表 ⚠️ 无数据
- 唯一的 eval 文件 `eval_exp021_sft_fast.json` 来自旧模型 (exp021_ragen_sft_v4)，20 episodes 全部 0% success
- Cell A prep report 提到当前 SFT ~30.8% overall (dev)，但**无 per-task 分解**
- 服务器上没有当前 ScienceWorld SFT 的 per-task eval 数据

### 5. 任务过滤支持 ✅ 已有机制
- `ScienceWorldEnvConfig.task_names` 是 comma-separated 字符串，env 代码从中随机选任务
- `envs.yaml` 的 `ScienceWorldSG` tag 包含全部 30 个任务
- **过滤方式**: 在 envs.yaml 中创建新 tag（如 `ScienceWorldSG_filtered`）或修改 `ScienceWorldSG` 的 `task_names` 字段
- 当前 v4 config 使用全部 30 个任务（因缺乏 per-task 数据）

### 6. 新 Config 文件
已创建: `/root/cost-verify-agent-rl/RAGEN/config/_scienceworld_cell_c_grpo_v4.yaml`

### 7. 启动前还需要
1. **磁盘紧张**: 仅 35GB 可用（/root/autodl-tmp 87% 使用），需清理旧 checkpoint 释放空间（15 steps × ckpt + optimizer 预估 ~15-20GB）
2. **Per-task eval**: 建议先跑一轮 SFT val_before_train（v4 config 已开启），从 wandb 拿到 per-task 数据后再决定是否过滤
3. **启动命令**:
   ```bash
   cd /root/cost-verify-agent-rl/RAGEN
   source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
   export RAY_TMPDIR=/root/autodl-tmp/tmp/ray
   CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _scienceworld_cell_c_grpo_v4 2>&1 | tee /root/autodl-tmp/checkpoints/scienceworld-cell-c-v4/train.log
   ```
4. **确认 GPU 空闲**: `nvidia-smi` 确认 cuda:0,1 无其他进程
5. **Dry-run** (C002 pre-flight)

---
