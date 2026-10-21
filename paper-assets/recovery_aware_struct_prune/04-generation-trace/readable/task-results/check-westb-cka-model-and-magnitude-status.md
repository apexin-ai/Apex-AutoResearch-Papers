# check westb cka model and magnitude status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westb_cka_model_and_magnitude_status_20260518T052117_result.json`
- **Structured JSON:** [`b4a07613f6eb05230145.json`](../../sessions/b4/b4a07613f6eb05230145.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. CKA-only GRPO 模型 — 完整

路径: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/`，总大小 **38G**。

关键文件齐全:
- `config.json` ✓
- `model.safetensors` (12.3 GB) ✓
- `tokenizer.json` + `tokenizer_config.json` ✓
- `generation_config.json` ✓
- `training_args.bin` ✓
- 另含 `checkpoint-100/` 和 `completions/` 子目录

### 2. scoring_ablation_magnitude_20 — 仍在运行，157/200

剪枝已完成（magnitude mode, 199/784 MLP groups pruned, actual sparsity 18.99%），当前在 **GSM8K eval 阶段**。

| 指标 | 值 |
|---|---|
| 进度 | **157/200** (78.5%) |
| 当前 acc | 0.0400 (at 150/200) |
| eos_rate | 1.33% |
| avg_len | 4063 |
| 速度 | ~56.6 s/it |
| 预估剩余 | **~40 分钟** |

Magnitude-only 剪枝 acc 极低（4%），符合预期（无 recovery-aware 信号）。

### 3. eval_math500_grpo_cka_only_20 — 仍在运行，101/500

| 指标 | 值 |
|---|---|
| 进度 | **101/500** (20.2%) |
| 已用时间 | ~1h50m |
| 速度 | 高度不均匀（有些 sample 5-6min，有些几秒） |
| 预估剩余 | **~7-8 小时**（基于平均 ~65s/sample） |

生成长度变化大导致 ETA 波动剧烈。这个 eval 预计今晚完成。

---
