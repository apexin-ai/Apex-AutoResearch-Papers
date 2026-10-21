# ssh cwm v6 restart seetacloud

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm-v6-restart-seetacloud_20260512T205203_result.json`
- **Structured JSON:** [`4ee13ec4eb80a20dd771.json`](../../sessions/4e/4ee13ec4eb80a20dd771.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查和准备工作完成。总结：

---

## 调查结果

### 1. SIGTERM 原因分析

历史 EXIT_CODE 模式：
- **v1 (原始 cwm)**: EXIT_CODE=143 → **SIGTERM** (signal 15)，平台行为（idle kill / 资源回收）
- **v2**: EXIT_CODE=1 → 代码错误
- **v3**: EXIT_CODE=137 → **SIGKILL** (signal 9)，OOM killer
- **v4**: 到 step 386 (~70min) 后死亡，无 EXIT_CODE 记录
- **v5**: CUDA OOM — 尝试用 GPU 0 而非 GPU 2
- **v6/v7**: 被杀前无 checkpoint

系统日志无法通过 ssh_read_only 获取（dmesg 被 allowlist 屏蔽）。根据 EXIT_CODE 模式，**主要原因是平台级 SIGTERM/SIGKILL（cgroup 回收或 idle kill），非代码 bug**。

### 2. Checkpoint 恢复情况

**无 checkpoint 可恢复。** `/root/autodl-tmp/checkpoints_repo_cwm_v6/` 目录为空。

**根本原因**：`save_steps=500`，但所有 run 都在 step 500 前被杀（v4 最远只到 step 386）。

### 3. 脚本修改 & 重启命令

已在服务器上修改 `train_repo_cwm.py`：
- `save_steps`: 500 → **100**（~13 分钟存一次 checkpoint）
- 新增 `--resume_from_checkpoint` CLI 参数
- 新增 `--save_steps` CLI 参数

**完整重启命令**（已注册为 `repo-level-cwm-v8`）：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=2 python3 train_repo_cwm.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir /root/autodl-tmp/checkpoints_repo_cwm_v6/ --no_wandb --save_steps 100
```

如果后续被杀有 checkpoint，resume 命令：
```bash
... && python3 train_repo_cwm.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir /root/autodl-tmp/checkpoints_repo_cwm_v6/ --no_wandb --save_steps 100 --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_v6/checkpoint-XXX
```

### 4. 是否迁移到 westd-48478

**建议继续在 seetacloud 上尝试**。理由：
- v4 已跑到 step 386（>1 小时），说明平台不是每次都立刻杀
- 现在 save_steps=100，即使再被杀也能从最近 checkpoint resume
- 当前 GPU 2 空闲，其他 GPU 无进程竞争
- 迁移需要重新搭环境 + 传数据，成本高

**请用 `submit_training_job` 提交 `repo-level-cwm-v8`。**

---
