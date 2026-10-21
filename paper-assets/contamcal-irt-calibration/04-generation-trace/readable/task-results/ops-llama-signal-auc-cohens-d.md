# ops llama signal auc cohens d

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama_signal_auc_cohens_d_20260517T021015_result.json`
- **Structured JSON:** [`6cb49883caf0f2b4fd9f.json`](../../sessions/6c/6cb49883caf0f2b4fd9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果保存在 `/root/autodl-tmp/exp008/llama_signal_analysis/`。

## 关键发现

### s1_embedding: 完全无效 (AUC = 0.5, Cohen's d = 0.0)
s1_embedding 对 Llama 跨所有dosage完全相同（值不变），对contamination无区分力。这是因为 embedding signal 基于固定参考模型计算，不随 SFT 训练改变。

### s2_minkpp: 几乎无效（确认 Reviewer 预期）
- d000 vs d100: MMLU Cohen's d = 0.035, AUC = 0.508; GSM8K d = -0.338, AUC = 0.391; ARC d = 0.210, AUC = 0.557
- 除 ARC 外均接近随机，且方向不一致（有时contaminated更高有时更低）

### s4_selfcritique: 唯一有区分力的 signal
- d000 vs d100: MMLU d = **-1.37**, AUC = 0.173 (即 flipped AUC = **0.827**); GSM8K d = **-1.27**, AUC = 0.187 (flipped = **0.813**); ARC d = **-2.40**, AUC = 0.057 (flipped = **0.943**)
- 注意 AUC < 0.5 说明 contaminated items 的 s4 值更**负**（lower self-critique score），flipped 后区分力很强
- d000 vs d025 也有明显效应：MMLU d = 0.75, GSM8K d = 1.05

### 与 Qwen 对比
Qwen exp-008 中 s1_embedding 和 s2_minkpp 在 Base regime 都有高 AUC (>0.95)，而 Llama 这两个 signal 完全失效。根本区别在于 Qwen 的 Base/SFT-clean/SFT-contam 是**不同模型类型**间比较，而 Llama 实验是**同一架构不同训练数据**的比较，s1_embedding 对后者不敏感。s4_selfcritique 是 Llama dosage 实验中唯一可用的contamination signal。

---
