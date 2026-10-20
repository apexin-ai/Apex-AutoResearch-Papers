# analysis grpo qwen math batch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_qwen_math_batch_20260516T154509_result.json`
- **Structured JSON:** [`63b6efb4b48ac56589d1.json`](../../sessions/63/63b6efb4b48ac56589d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新成功。

```
=== GRPO Qwen Math Batch Analysis ===

[grpo_rasp_25_qwen_math]: conclusion=success
  - Collapse: 有(mild/partial), onset ~step 10, NOT permanent
  - Key metrics: reward_final=0.206, reward_std_final=0.400, frac_zero_std_final=0.35, completion_length_final=812
  - frac_zero_std range: 0.25~0.575 (peak step 10), reward range: 0.11~0.23
  - Early stop: 否 (完成 100 steps)
  - 与 DeepSeek 对比：差异显著。DeepSeek RASP 20% 是 permanent collapse (frac_zero_std→0.95, reward→0.039)，
    Qwen Math RASP 25% 仅 mild partial collapse，frac_zero_std 最高 0.575 且逐步下降，reward 维持 0.1-0.2。
    Qwen Math 对 RASP 剪枝的 collapse 抵抗力明显更强。

[grpo_standard_25_qwen_math]: conclusion=success
  - Collapse: 有(KL explosion transient), onset step 20, transient (recovery step 90)
  - Key metrics: reward_final=0.182, reward_std_final=0.367, frac_zero_std_final=0.325, completion_length_final=527
  - KL 爆炸: step 20 kl=56.08, step 80 kl=4.1M, loss=220K → step 90 恢复 kl=0.026
  - Early stop: 否 (完成 100 steps)
  - 与 DeepSeek 对比：部分一致。DeepSeek Standard 20% 表现为 reward transient dip (step ~60 dip, ~90 recovery)，
    Qwen Math Standard 25% 表现为 KL/loss 数值爆炸后恢复——instability 机制不同（KL explosion vs reward dip），
    但都是 transient 模式。reward 本身维持 0.1-0.2 无明显 dip。

[grpo_standard_qwen_math_v3]: conclusion=success
  - Collapse: 有(permanent), onset step 10, PERMANENT
  - Key metrics: reward_final=0.044, reward_std_final=0.146, frac_zero_std_final=0.85, completion_length_final=921
  - frac_zero_std: 0.75(step10) → 0.85(step20) → 0.90(step30) → 0.85(step100)
  - Early stop: 否 (完成 100 steps, reward_desert_patience 未触发因 reward 不是严格 0)
  - 与 DeepSeek 对比：意外发现！DeepSeek Standard 20% 是 transient dip+recovery，
    但 Qwen Math Standard 20% 却是 PERMANENT COLLAPSE，pattern 更接近 DeepSeek RASP 20%。
    这说明 Qwen2.5-Math-7B Standard 20% 剪枝造成的损伤比 DeepSeek 同条件更严重。

=== 跨模型对比总结 ===
Qwen2.5-Math-7B 的 collapse 模式与 DeepSeek-R1-Distill-Qwen-7B 有系统性差异：
1. Standard 20%: DeepSeek=transient, Qwen Math=PERMANENT (意外反转)
2. RASP 25%: 预期 permanent collapse 未完全出现，仅 mild partial
3. Standard 25%: KL 数值爆炸 transient instability (DeepSeek 未观察到此模式)
→ Collapse 严重程度不仅取决于剪枝方法，还强依赖于 base model 的 GRPO 适应性。
```

---
