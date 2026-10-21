# diag gpu disk status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-disk-status-check_20260515T220546_result.json`
- **Structured JSON:** [`e51fa20ca6080eda672d.json`](../../sessions/e5/e51fa20ca6080eda672d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westb-23072 ===
磁盘: 根分区 8.6G/30G (29%), 数据盘 188G/250G (76%)
      ✅ 根分区已从满载恢复，当前健康
GPU 0: [在用] - PID 557457, eval_gsm8k.py (pruned_rasp_alpha_0.25), 显存 13G/96G, util 79%
GPU 1: [在用] - PID 534667, train_grpo_v5.py (grpo_stage2_standard_20_v8), 显存 70G/96G, util 100%
tmux: (read_only 不支持 tmux ls)
关键进程:
  - GPU 0: eval_gsm8k.py --model_path pruned_rasp_alpha_0.25 --max_samples 100
  - GPU 1: train_grpo_v5.py (GRPO v8) --loss_type dapo --max_steps 100 --lr 1e-6 ✅ PID 534667 确认在跑

=== westd-11672 ===
磁盘: 根分区 5.0G/30G (17%), 数据盘 228G/250G (92%)
GPU 0: [空闲] - 0MiB, 0% util
GPU 1: [空闲] - 0MiB, 0% util
tmux: (read_only 不支持 tmux ls)
关键进程: 无 python/train 进程运行
  - ❌ GraSP SFT/eval 已结束（GPU 0 空闲）
  - ❌ α ablation SFT sweep 已结束（GPU 1 空闲）

=== 汇总 ===
空闲 GPU 列表: westd-11672 cuda:0, westd-11672 cuda:1 (共 2 块 RTX PRO 6000)
磁盘风险: westd-11672 数据盘 92% (228G/250G) ⚠️ 接近满载，剩余仅 23G
建议行动:
  1. westd-11672 数据盘需清理，92% 使用率下再跑实验可能空间不足
  2. westd-11672 两块 GPU 完全空闲，可立即调度新任务
  3. westb-23072 GPU 0 在跑 eval（alpha_0.25），完成后将释放
  4. GRPO v8 (PID 534667) 在 westb-23072 GPU 1 正常运行中
```

---
