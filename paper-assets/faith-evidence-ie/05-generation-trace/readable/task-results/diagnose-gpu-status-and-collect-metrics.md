# diagnose gpu status and collect metrics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_status_and_collect_metrics_20260518T163031_result.json`
- **Structured JSON:** [`e0132e4308691cca2890.json`](../../sessions/e0/e0132e4308691cca2890.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== GPU Status ===
cuda:0: 空闲 (0MiB / 32607MiB)
cuda:1: 空闲 (0MiB / 32607MiB)
cuda:2: 占用 (16631MiB / 32607MiB) — PID 542126, grpo_trainer (grpo-bf16-g4-kl0)
cuda:3: 空闲 (0MiB / 32607MiB)

=== plan019_1_7b_sft_s44 ===
状态: 已完成
输出目录: /root/autodl-tmp/sft_output_qwen3_1_7b_bf16_seed44/
tmux session: 无（已退出）
metrics:
  - train_loss: 0.5783 (final step)
  - eval_loss: 0.8037
  - eval_mean_token_accuracy: 0.8238
  - global_steps: 570
  - epochs: 3.0
  - best_metric: 0.7875 (eval_loss at step 380)
checkpoints: checkpoint-380 (best), checkpoint-570 (final)
最终 adapter: adapter_model.safetensors (278MB)

=== random_rsft_k1_baseline ===
状态: 已完成
输出目录: /root/autodl-tmp/rsft_output_random_k1/
tmux session: 无（已退出）
metrics:
  - train_loss: 0.5780 (final step)
  - mean_token_accuracy: 0.8552
  - global_steps: 1020
  - epochs: 3.0
checkpoints: checkpoint-1000, checkpoint-1020 (final)
最终 adapter: adapter_model.safetensors (528MB)

=== random_rsft.sh fix ===
修复状态: 已修复
变更: `export CUDA_VISIBLE_DEVICES=${GPU:-0}` → 已注释掉
```

---
