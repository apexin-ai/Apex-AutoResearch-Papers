# analysis track b seed signal

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_track-b-seed-signal_20260524T021613_result.json`
- **Structured JSON:** [`76b27ec4ab2b0dfe7c7e.json`](../../sessions/76/76b27ec4ab2b0dfe7c7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果写入 `artifacts/seed_early_signal_analysis.md`，已注册。

核心发现：

1. **无可靠早期预测指标**：步骤 1–3 所有标准训练指标（reward、KL、entropy、grad norm、response length、train success）在三组间均无显著差异（所有 p > 0.2）。

2. **"迟发崩溃"现象**：seed7 和 seed8（Collapsed）在早期反而表现最好——seed7 步骤 3 reward = 4.92（全场最高），seed8 步骤 0 val success = 31.3%（全场最高）。崩溃在步骤 5 之后才出现。

3. **MI 多样性是最强候选**：步骤 1 的 MI estimate 效应量最大（Cohen's d = 1.11），Collapsed 组均值 0.090 vs Generalized 0.165，但 p = 0.23，样本量不足以达显著。

4. **Stagnant 组特征明确**：低 reward（1.37 vs 2.92）、低 grad norm（1.06 vs 1.49）、高 response length，说明环境给出的训练信号不足。

已包含两段论文可用文本（Discussion 段和 Appendix 段）。未修改任何 .tex 文件。

---
