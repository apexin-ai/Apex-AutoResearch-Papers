# ops westb progress check 20260518T2235

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_progress_check_20260518T2235_20260518T223502_result.json`
- **Structured JSON:** [`b576caa8bf09591926d5.json`](../../sessions/b5/b576caa8bf09591926d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### Eval 进度

| GPU | 任务 | 进度 | 当前 Acc | 预计剩余时间 |
|-----|------|------|----------|-------------|
| cuda:0 (PID 836192) | eval_gsm8k_**sft_cka_only_20_1p5b** | **757/1319 (57%)** | 36.93% | ~55 min (约 ~2s/it, 剩余 562 样本) |
| cuda:1 (PID 832359) | eval_gsm8k_**grpo_rasp_20_1p5b** | **1205/1319 (91%)** | 26.67% | ~4 min (约 ~2s/it, 剩余 114 样本) |

cuda:1 的 grpo_rasp eval 即将完成。cuda:0 的 sft_cka_only eval 预计还需约 1 小时。

### SFT Standard 模型

| 路径 | 状态 |
|------|------|
| `sft_standard_20_1p5b/` | 完整 (model.safetensors 2.93GB, config, tokenizer 齐全) |
| `sft_standard_25/checkpoint-1870/` | 完整 (model.safetensors 11.58GB, config, tokenizer 齐全) |
| `sft_qwen_math_standard_20*` | **不存在** |

### 所有 sft_* 目录

```
sft_cka_only_20          sft_rasp_20_1p5b
sft_cka_only_20_1p5b     sft_rasp_25
sft_gradient_20          sft_rasp_rlvr_20
sft_random_20            sft_standard_20_1p5b
                         sft_standard_25
```

`sft_standard_20_1p5b` 是 1.5B 剪枝后 SFT 恢复的模型（2.93GB），权重完整可用。`sft_standard_25` 是 7B 级别的（11.58GB），存在 checkpoint-1870 子目录下，权重也完整。`sft_qwen_math_standard_20*` 在 westb 上不存在。

---
