# analysis sft qwen7b olmo2 s123 sweep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft_qwen7b_olmo2_s123_sweep_20260519T225320_result.json`
- **Structured JSON:** [`6cc0805a2e967386b821.json`](../../sessions/6c/6cc0805a2e967386b821.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**全部 10 个 (model × dosage) checkpoint 存在且有效，无错误、无 OOM。**

### Qwen2.5-7B
所有 5 个 dosage **被跳过** — checkpoint 来自先前运行（May 18–19），adapter 权重完整（~161 MB）。`.done` 标记缺失，但 adapter_model.safetensors 存在。本次日志中无 Qwen 的 train_loss（需查原始训练日志）。

### OLMo-2-7B（本次训练）

| Dosage | train_loss | mean_token_acc | runtime |
|--------|-----------|----------------|---------|
| d000 | 0.9431 | 0.7855 | 1h41m |
| d005 | 0.9475 | 0.7623 | 1h42m |
| d025 | 0.9601 | 0.8161 | 1h46m |
| d050 | 0.9737 | 0.7864 | 1h51m |
| d100 | 0.9979 | 0.7601 | 2h02m |

Train loss 随 dosage 单调递增 (0.943→0.998)，符合预期（污染注入使任务更难）。全部 exit_code=0，均有 `.done` 标记。

### 注意事项
- lora_alpha=32 ✓（C006 合规）
- W&B 查询因工具 API 问题失败，未获取 W&B 指标
- 报告已注册：`art_20260519_1e4f79`

---
