# analyze exp 001 sft gemma2 9b d025 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_001_sft_gemma2_9b_d025_s42_20260519T021316_result.json`
- **Structured JSON:** [`60de18aca1e995439948.json`](../../sessions/60/60de18aca1e995439948.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 结果

**Conclusion: success**

### Metrics

| 指标 | d000 | d005 | **d025** |
|---|---|---|---|
| final_loss | 1.159 | 1.157 | **1.143** |
| mean_token_accuracy | 0.7284 | 0.7303 | **0.7384** |
| total_steps | 3125 | 3177 | **3384** |
| train_runtime | — | — | **9451s (~2h37m)** |

### 对比分析

- **Loss 递减趋势明确**：d000 (1.159) → d005 (1.157) → d025 (1.143)，contamination 比例增加时 final loss 持续下降，符合预期（模型对更多 seen data 拟合更好）。
- **Accuracy 递增趋势一致**：0.7284 → 0.7303 → 0.7384，d025 提升幅度更大（+0.81pp vs d005 的 +0.19pp），说明 25% contamination 已产生明显的记忆效应。
- **Steps 增长**：3384 步（vs d000=3125, d005=3177），因 d025 数据量更大（54133 samples）。
- Checkpoint 完整（lora_adapter + .done sentinel），LoRA 配置确认 α=32, r=16。

---
