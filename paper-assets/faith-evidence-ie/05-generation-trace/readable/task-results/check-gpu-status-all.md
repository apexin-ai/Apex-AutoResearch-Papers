# check gpu status all

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_status_all_20260515T202632_result.json`
- **Structured JSON:** [`a2dbe747f66736ca29d2.json`](../../sessions/a2/a2dbe747f66736ca29d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 0: 空闲       显存=0MiB        无进程
GPU 1: 占用  PID=249551  显存=17848MiB  plan_011_bf16_g8_step_eval (eval checkpoint-30)
GPU 2: 占用  PID=251136  显存=16460MiB  eval_plan_012_dpo_ced_1ep
GPU 3: 占用  PID=234494  显存=20084MiB  plan_008_rsft_topk3 训练

PID 状态:
- PID 249541 (plan_011 bash wrapper): 存活 ✓，运行 27min
- PID 249551 (plan_011 实际 python): 存活 ✓，cuda:1
- PID 246974 (plan_009_flatnli_reward_eval_r2): 已退出 ✗，无冲突
- PID 234494 (plan_008_rsft_topk3): 存活 ✓，cuda:3，已运行 2h24m

plan_001_flat_nli_seed43 状态: 已完成 ✓
  退出码=0，完成时间 2026-05-15T20:19:08Z
  507/507 步全部完成，训练时长 1h55m
  最终 metrics:
    eval_loss=0.7567  eval_entropy=0.6778  eval_mean_token_accuracy=0.8298
    train_loss=0.6248  train_samples/s=1.173  epoch=3.0
  模型已保存到 /root/autodl-tmp/rsft_output_flat_nli_s43

plan_011 eval 进度: 28/62 batches (45%)，正在评估 checkpoint-30，~31min 已过，预计再需 ~32min

plan_009_flatnli_r2 (mvp2_eval_rsft_s43_r2): 已完成 ✓
  退出码=0，完成时间 2026-05-15T13:15:19Z
  F1=0.4683  Ign-F1=0.4683  Evi-F1=0.8156  EDCR=0.6388
  格式正确 985/985  截断 171/985  预测数 14970

eval_dpo_1ep 进度: 5/62 batches (8%)，刚启动约 5min，预计总时长 ~58min

plan_008_rsft_topk3 训练: 1272/1509 步 (84%)，epoch 2.53，loss=0.5148
  预计剩余 ~17min 完成
```

---
