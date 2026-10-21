# code full status check westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_full-status-check-westd_20260515T093116_result.json`
- **Structured JSON:** [`0e5e35e42998561ed608.json`](../../sessions/0e/0e5e35e42998561ed608.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== GPU ===
0, 51523 MiB, 73 %
1, 51441 MiB, 86 %

=== PROCESSES ===
PID 16795  163%CPU  python src/sft_recovery.py --model_path .../alpha_0.0 --output_dir .../sft_ablation/alpha_0.0 --gpu 0 --num_train_epochs 2 --learning_rate 2e-5
PID 16796  164%CPU  python src/sft_recovery.py --model_path .../alpha_0.5 --output_dir .../sft_ablation/alpha_0.5 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5

=== PID 7186 ===
7186  bash -c cd /root/recovery_a...  ELAPSED 01:55:23

=== ALPHA ABLATION RESULTS ===
alpha_0.0/eval_results.json — NO FILE
alpha_0.5/eval_results.json — NO FILE
alpha_1.0/eval_results.json — NO FILE
alpha_2.0/eval_results.json — NO FILE
alpha_4.0/eval_results.json — NO FILE

=== PIPELINE LOG (ablation_full.log) ===
SFT 正在训练中：
  alpha_0.0 (gpu 0): step 621/1870, epoch ~0.33, loss ~0.82-0.88, token_acc ~0.78
  alpha_0.5 (gpu 1): step 645/1870, epoch ~0.34, loss ~0.82-0.88, token_acc ~0.78
  速度: ~1.0 it/s 每卡，已跑 ~10 分钟

=== D023 RE-EVAL RESULTS ===
/tmp/reeval_standard_20.log — 空文件
/tmp/reeval_rasp_20.log — NO FILE

=== DISK ===
/dev/md0  250G  95G  156G  38%  /root/autodl-tmp
```

---
