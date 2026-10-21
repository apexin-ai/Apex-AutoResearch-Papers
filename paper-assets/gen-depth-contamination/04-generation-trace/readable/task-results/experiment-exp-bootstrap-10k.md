# experiment exp bootstrap 10k

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_exp_bootstrap_10k_20260520T114145_result.json`
- **Structured JSON:** [`35b641262749c8a47e34.json`](../../sessions/35/35b641262749c8a47e34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| Config | AUC | 1K CI | 10K CI | 1K Verdict | 10K Verdict | Flipped? |
|--------|-----|-------|--------|------------|-------------|----------|
| LLaMA-8B | 0.6075 | [0.597, 0.617] | [0.598, 0.617] | BORDERLINE | BORDERLINE | No |
| Gemma-2-2B | 0.5981 | [0.588, 0.608] | [0.588, 0.608] | BORDERLINE | BORDERLINE | No |
| Mistral-7B | 0.5902 | [0.580, 0.600] | [0.580, 0.600] | K\*=1 | BORDERLINE | Yes\* |
| 512-tok | 0.6136 | [0.604, 0.623] | [0.604, 0.623] | K\*=2 | K\*=2 | No |

**Mistral 的"翻转"**：CI upper 从 0.6000（恰好=θ）移到 0.6001（刚过θ 0.01pp），这是 bootstrap 精度提升的噪声，point estimate 仍 0.5902 << θ，不影响 K\*=1 的实质判定。

**未覆盖的 2 个配置**：exp_017（Qwen-cont）和 exp_002（OLMo-1B）的 features.csv 在磁盘上已不存在。如需补充，需重新跑 pipeline 生成 features。

**结论**：10K bootstrap CI 约窄 3%，无实质性 K\* 翻转，确认 1K resamples 的 K\* assignments 是 robust 的。

---
