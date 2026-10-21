# paper writing

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_20260513T215457_result.json`
- **Structured JSON:** [`9b6b70d4100f20b21232.json`](../../sessions/9b/9b6b70d4100f20b21232.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已写入。

**discussion.tex** (~1200 words, 6 subsections):
- §5.1 K*=2 理论含义：DPI 预测 + 8/8 不变性 + 信息损失速率（0v1→1v2 ~30pp drop）+ 与 Shumailov/Dohmatob/Alemohammad 的关联 + 解码策略不变性
- §5.2 Cross-model transfer：80-92% retention + 0v1>0.96 + 实践部署含义 + 两个 caveat
- §5.3 Feature importance 分化：Greedy vs T=0.7 ρ=0.914 vs Greedy vs T=1.2 ρ=0.53 + top-3 特征差异 + τ≈0.37 at 1v2 limitation
- §5.4 LLM zero-shot：GPT-5.5 33.2% / Claude 33.1% vs OBD 38.6% + binary ~88% + depth estimation 是独立维度
- §5.5 Limitations：6 条（scale, prompt-chain, language, decoding, operational bound, features）
- §5.6 Graduated filtering TODO 占位

**conclusion.tex** (~400 words)：summary + C3 TODO + limitations recap（含 Qwen-cont marginal CI + τ≈0.37）+ future work（retrain-chain, 7B+/70B+, multilingual, temporal dynamics, learned representations）

---
