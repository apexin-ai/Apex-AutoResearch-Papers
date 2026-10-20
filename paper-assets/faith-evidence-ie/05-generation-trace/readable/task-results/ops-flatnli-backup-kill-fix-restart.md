# ops flatnli backup kill fix restart

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_flatnli-backup-kill-fix-restart_20260514T152334_result.json`
- **Structured JSON:** [`3ff529ffa358b17ae26f.json`](../../sessions/3f/3ff529ffa358b17ae26f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 执行汇总

### Step A: Checkpoint 备份
- 备份 5 个 checkpoint 到 `/root/autodl-tmp/checkpoints_backup/flatnli_r3_healthy/`
  - checkpoint-20, checkpoint-40, checkpoint-60, checkpoint-80, checkpoint-100

### Step B: Kill flatnli_r3
- PID 53292 已终止（SIGTERM），cuda:3 完全释放

### Step C: NLI device 修复
- **方式：参数修复**，无需改核心逻辑
- `grpo_trainer.py` 两处改动：
  - Line 383: 新增 `--resume_from_checkpoint` argparse 参数
  - Line 511: `trainer.train()` → `trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)`
- `--reward_device` 已存在（line 351，默认 `cpu`），重启时加 `--reward_device cuda`

### Step D: 重启 flatnli_r4
- **PID**: 67050 (cuda:3)
- **exp_id**: mvp2_grpo_flatnli_r4
- 从 checkpoint-100 恢复，output_dir: `/root/autodl-tmp/grpo_flatnli_r4`
- 需要额外设 `HF_HOME=/root/autodl-tmp/.hf_cache`（NLI 模型缓存路径）

### Step E: 验证
- **Step 进度**: 104/756（从 checkpoint-100 成功恢复）
- **Step time**: ~31-34s/step（vs 之前 ~100s/step on CPU，**3x 提速**）
- **nvidia-smi**: cuda:3 单进程 9790MiB, 53% util
- **注意**: step_time 34s 高于预期的 12s，可能因为 NLI model 和训练模型共享同一 GPU 导致显存/计算竞争。但相比 CPU 的 100s 已大幅改善。

---
