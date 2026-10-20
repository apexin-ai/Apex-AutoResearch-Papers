# analysis exp 001 sft 14b d025 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_14b_d025_s42_20260518T221332_result.json`
- **Structured JSON:** [`20f9a9822405f55d6fac.json`](../../sessions/20/20f9a9822405f55d6fac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 分析结果

### 训练完成状态
- **正常完成**，EXIT_CODE=0，日志末尾："Training complete."
- 时间：2026-05-19 03:07:45 → 06:10:08（约 3 小时）

### 关键指标

| 指标 | 值 |
|---|---|
| avg train_loss | **0.9264** |
| final logged loss (step 3380) | **0.8886** |
| first loss (step 10) | 1.440 |
| mean_token_accuracy (avg) | 0.7677 |
| mean_token_accuracy (final) | 0.7742 |
| total_steps | 3384 |
| training_time | 2.99 hours (10780s) |
| samples/sec | 5.024 |

### Checkpoint 文件
```
lora_adapter/
├── adapter_model.safetensors  (275 MB)
├── adapter_config.json        (lora_alpha=32, r=16 ✓)
├── tokenizer.json
├── tokenizer_config.json
├── chat_template.jinja
├── training_args.bin
├── README.md
└── checkpoint-3384/           (含 optimizer.pt, trainer_state.json)
```

### Loss 对比（同项目已完成 SFT）

| 实验 | 模型 | avg loss |
|---|---|---|
| **14B d025 s42** | **Qwen2.5-14B** | **0.926** |
| 3B d000 s42 | Qwen2.5-3B | 1.132 |
| 3B d000 s123 | Qwen2.5-3B | 1.136 |
| 3B d005 s42 | Qwen2.5-3B | 1.135 |
| 9B d000 s42 | Gemma-2-9B | 1.159 |
| 3B d025 s42 (Llama) | Llama-3.2-3B | 1.527 |

14B 的 loss 显著低于 3B/9B，符合模型规模效应预期。Loss 从 1.44 平滑收敛到 0.89，无异常。

### Conclusion: **success**

训练正常完成，loss 合理收敛，checkpoint 完整，lora_alpha=32 符合标准化要求。W&B 未集成（此 run 无 wandb 日志）。Registry 已更新为 DONE/success。

---
