# ops westd seed100 eval prep and launch

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_seed100_eval_prep_and_launch_20260522T174153_result.json`
- **Structured JSON:** [`bb0ef1a2f688d229e391.json`](../../sessions/bb/bb0ef1a2f688d229e391.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个任务全部初始化正常，wandb 已连接。

## 总结

### Config 创建（4 个）
| Config | 文件 | 状态 |
|--------|------|------|
| seed100 step5 OOD eval | `_alfworld_seed100_step5_ood_eval.yaml` | 已创建 |
| seed5 response_mask check | `_alfworld_seed5_response_mask_check.yaml` | 已创建 |
| seed200 step5 OOD eval | `_alfworld_seed200_step5_ood_eval.yaml` | 已创建 |
| seed300 step5 OOD eval | `_alfworld_seed300_step5_ood_eval.yaml` | 已创建 |

### 当前运行状态
| 任务 | GPU | PID | W&B Run | 状态 |
|------|-----|-----|---------|------|
| seed5 mask check (eval) | cuda:1 | 60101 | s1w7dy09 | 运行中 |
| seed100 训练 (1 GPU 重跑) | cuda:0 | 66433 | zsrodv2f | 运行中 |
| seed200 训练 (重跑) | cuda:2,3 | 63676 | r5hn7cqf | 运行中 |

### 问题说明
- **seed100** 之前在 step 4/5 崩溃（wandb 写 `/root/autodl-tmp/tmp/` 时目录不存在），已修复 tmp 目录并重启
- **seed200** 之前在 step 3/5 被意外终止（我执行 `ray stop --force` 清理残留进程时误杀），已重启
- seed100 改为 1 GPU 运行（cuda:0），因 cuda:1 被 seed5 mask check 占用。训练超参不变，仅速度略慢

seed100 OOD eval 需等训练完成后再启动（还需 FSDP→HF 转换 + symlink 创建）。

---
