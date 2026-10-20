# eval ablation s2 batch

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_ablation_s2_batch_20260522T210350_result.json`
- **Structured JSON:** [`a9c464b67af4db93ac4e.json`](../../sessions/a9/a9c464b67af4db93ac4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成总结：

## 训练完成确认

| 实验 | Steps | 耗时 | 退出码 |
|------|-------|------|--------|
| ablation_occ_detach_s2 | 50005 | ~14h46m | 0 |
| ablation_random_occ_s2 | 50005 | ~14h48m | 0 |

## Checkpoint 完整性

两个 checkpoint 均完整（~14.4GB each）：
- 4× safetensors (model shards)
- action_head--50000_checkpoint.pt (302MB)
- occ_head--50000_checkpoint.pt (2.4MB)
- proprio_projector--50000_checkpoint.pt (67MB)
- lora_adapter/
- dataset_statistics.json, config.json, tokenizer

路径：
- Detach: `/root/autodl-tmp/checkpoints/ablation_occ_detach_s2/openvla-7b+...--50000_chkpt`
- Random: `/root/autodl-tmp/checkpoints/ablation_random_occ_s2/openvla-7b+...--50000_chkpt`

## Eval 启动状态

| Eval | GPU | tmux session | 进度 | 输出路径 |
|------|-----|-------------|------|---------|
| detach_s2 | cuda:1 | `eval_detach_s2` | T0: 4/50 | `/root/occsafe_vla/eval_results/ablation_occ_detach_s2_50r_50000.json` |
| random_s2 | cuda:0 | `eval_random_s2` | T0: 40/50 | auto-generated in `/root/occsafe_vla/artifacts/` |

注：`eval_random_s2` 由之前的自动化触发，未设 `--output_path`，结果会写到 artifacts 目录。已清理重复的 `ablation_random_occ_s2_eval` session（kill PID 44845）。

## 训练 Loss

日志中仅有 tqdm 进度条输出，loss 走 wandb，无法从日志提取。

## 预估 Eval 完成时间

每个 rollout ~4-6s，50 rollouts × 10 tasks = 500 episodes ≈ 35-50 min。
- random_s2 预计 ~05:35 UTC 完成（已领先）
- detach_s2 预计 ~05:45 UTC 完成

---
