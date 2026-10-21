# analysis thinking token lp dilution

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_thinking_token_lp_dilution_20260515T164811_result.json`
- **Structured JSON:** [`c1d6580fb0785785bb4f.json`](../../sessions/c1/c1d6580fb0785785bb4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。脚本已在服务器上执行，结果保存到 `output/analysis_round8/thinking_token_lp_dilution.json`。

**核心结论**：

| 指标 | 数值 |
|------|------|
| SciERC 响应 token 数 | median=164, mean=200, range=[14, 512] |
| 5 个 thinking tokens 的 LP 偏移量 | median=0.001075 nats |
| 偏移量 / median LP range | **2.68%** |
| LP range 变化量（50 实例验证） | mean=0.0058, max=0.096 nats |

**三重论证**：

1. **稀释幅度极小**：5 个 thinking tokens 在 median 164 tokens 的响应中，LP shift 仅 0.001 nats，是 LP range (0.041) 的 2.68%。

2. **LP range 近似不变**：LP range = max(mean\_lp) - min(mean\_lp)，同一 instance 的所有 sample 共享相同 thinking prefix，shift 近似常数，range 几乎不变。

3. **自然对照组决定性反驳**：CoNLL（**无** thinking tokens）LP compression 远强于 SciERC（**有** thinking tokens）：
   - CoNLL T=0.7: tied fraction = **95.8%**
   - CoNLL T=1.0: tied fraction = **86.8%**
   - SciERC: tied fraction = **60.3%**

   如果 thinking tokens 是 LP compression 的原因，没有 thinking tokens 的 CoNLL 不应出现更强的 compression。事实相反。

**Verdict**: Thinking token 稀释效应可忽略。LP compression 是 fine-tuned structured output 模型的固有特性，非 thinking tokens 的 artifact。

---
