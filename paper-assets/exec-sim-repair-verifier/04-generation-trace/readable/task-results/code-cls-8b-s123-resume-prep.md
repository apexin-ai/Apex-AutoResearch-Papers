# code cls 8b s123 resume prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cls-8b-s123-resume-prep_20260514T140925_result.json`
- **Structured JSON:** [`23fc605e5c3bb199d69a.json`](../../sessions/23/23fc605e5c3bb199d69a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. ckpt-200 状态：✅ 存在且完整
```
checkpoint-200/
├── adapter_config.json
├── adapter_model.safetensors  (58MB)
├── optimizer.pt               (117MB)
├── scheduler.pt
├── rng_state.pth
├── trainer_state.json
└── training_args.bin
```

当前目录下的 checkpoint 列表：`checkpoint-200, 1600, 1800, 2000, 2200`（400/600 确认已被 save_total_limit=5 删除）。

### 2. 脚本需要修改（3 处）

脚本路径：`/home/sonny/exec-sim-repair-verifier/train_repo_verifier.py`

**问题 A**：无 `--resume_from_checkpoint` 参数，`trainer.train()` 也不传。
**问题 B**：`save_total_limit` 硬编码为 5，无 CLI 覆盖。
**问题 C**：`is_dryrun = args.max_steps > 0`——如果用 `--max_steps 600` 会触发 dryrun 模式，`save_strategy="no"`，不会保存任何 checkpoint。

**推荐方案**：不用 `--max_steps`，保持 `epochs=3`（与原训练一致），resume 后手动监控，ckpt-600 保存后 kill。这样 LR scheduler 与原训练完全一致。

#### 修改 1：添加 CLI 参数（line 199 之后）
```python
p.add_argument("--resume_from_checkpoint", default=None)
p.add_argument("--save_total_limit", type=int, default=5)
```

#### 修改 2：使用 CLI 值替代硬编码（line 272）
```python
# 改前
"save_total_limit": 5,
# 改后
"save_total_limit": args.save_total_limit,
```

#### 修改 3：传 resume 参数给 trainer（line 297）
```python
# 改前
trainer.train()
# 改后
trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)
```

### 3. 恢复训练命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=3 python3 /home/sonny/exec-sim-repair-verifier/train_repo_verifier.py \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ \
  --device cuda:0 \
  --batch_size 1 \
  --grad_accumulation 32 \
  --seed 123 \
  --no_wandb \
  --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda_resume/ \
  --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-200 \
  --save_total_limit 10
```

注意：`CUDA_VISIBLE_DEVICES=3` + `--device cuda:0`，因为 CUDA_VISIBLE_DEVICES 重映射后只有一张卡可见。

### 4. 预计时长
- Step 200 → 600 = 400 steps × ~8.3s/step ≈ **55 分钟**
- 监控 ckpt-600 保存后 kill 进程

### 5. 操作流程
1. 等当前 s123 训练完成（预计 May 15 ~12:00 UTC）
2. 修改 `train_repo_verifier.py`（3 处，见上）
3. 在 tmux 中运行恢复命令
4. 监控日志，等 "Checkpoint saved at step 600" 出现
5. Kill 进程
6. 验证 `ls /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda_resume/` 应有 checkpoint-400 和 checkpoint-600

### 6. 注意事项
- output_dir 用新目录 `_resume/` 避免覆盖原有 checkpoint
- 不用 `--max_steps`，避免触发 dryrun 模式导致不保存 checkpoint
- `epochs=3` 保持与原训练一致，确保 scheduler 状态恢复后 LR 曲线匹配

---
