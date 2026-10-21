# ops llama3 d000 completion check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama3-d000-completion-check_20260521T121652_result.json`
- **Structured JSON:** [`cefc7b63698f4c979654.json`](../../sessions/ce/cefc7b63698f4c979654.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已被清理或未在本 session 创建）。

---

```
训练结果: success
.done 文件: 存在 (/root/autodl-tmp/exp001/checkpoints/Meta-Llama-3.1-8B_d000_s0/.done)
checkpoint: /root/autodl-tmp/exp001/checkpoints/Meta-Llama-3.1-8B_d000_s0/lora_adapter/
  - adapter_model.safetensors (167MB)
  - adapter_config.json (lora_alpha=32, r=16)
  - tokenizer.json, tokenizer_config.json, training_args.bin, checkpoint-3125
log 关键内容: epoch=1, train_loss=1.373, mean_token_accuracy=0.6958, runtime=8110s (~2h15m)
eval 是否已触发: 是 — PID 519410/519561 在 GPU 1 运行 MMLU eval
  输出到: /root/contamcal-irt-calibration/results/mmlu_eval/llama3_8b/d000_s0/
GPU 1 状态: 在跑 eval (96% util, 37GB VRAM)
registry 更新: 已完成 (DONE/success)
cron 清理: 不存在（无需删除）
```

---
