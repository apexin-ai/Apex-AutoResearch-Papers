# analysis exp021 ragen sft v4

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp021_ragen_sft_v4_20260515T025919_result.json`
- **Structured JSON:** [`149391ccc128a247c6f1.json`](../../sessions/14/149391ccc128a247c6f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 训练
- 正常完成，320 步 / 2 epochs / 47.8 min
- Final loss: 0.038, token accuracy: 98.8%
- Checkpoint: `/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final` (3.3GB)

### RAGEN val_before_train (核心验证)

| 指标 | 值 | Criteria | 状态 |
|------|-----|----------|------|
| **success** | **25%** | ≥ 10% | **PASS** |
| **action_is_valid** | **87.5%** | ≥ 85% | **PASS** |

### eval_sft_fast (对比参考)
- success: 0% (exp019b 为 20%) — 预期下降，因为模型现在偏向 RAGEN 格式
- format_ok: 100%, action_is_valid: 71%

### 结论
**格式兼容性修复成功。** exp019b 在 RAGEN val 中 0% success，exp021 达到 25%，两项 pass criteria 均达标。eval_sft_fast 中表现下降是预期行为：模型训练格式已对齐到 RAGEN（`&lt;/think>` 后直接输出 action），而 eval_sft_fast 使用的 `&lt;answer>` 标签格式不同。

---
