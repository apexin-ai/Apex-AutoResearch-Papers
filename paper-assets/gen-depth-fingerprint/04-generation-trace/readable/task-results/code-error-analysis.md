# code error analysis

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_error-analysis_20260517T032948_result.json`
- **Structured JSON:** [`38722f70d004b87eb6ef.json`](../../sessions/38/38722f70d004b87eb6ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `/root/gen-depth-fingerprint/experiments/error_analysis/error_analysis_results.json`。

核心发现：

1. **Overall**: 28.08% error rate (8170/29095 misclassified)

2. **Error asymmetry严重**: 86.2% 的错误是 FN (gen-2+ 被误判为 gen-1)，仅 13.8% 是 FP。分类器倾向于把 gen-2+ 判为 gen-1。

3. **Depth-2 是主要失败点**: depth-2 的 error rate 高达 48.42%，远高于 depth-3 (29.17%) 和 depth-4 (20.32%)。说明 gen-1→gen-2 的特征变化最难捕捉，fingerprint 在浅层重写时失效。

4. **Generator 差异大**: Mistral-7B 最难 (45% error)，Pythia-1B 最易 (18.2%)。大模型/指令对齐模型产生的文本更难与 gen-1 区分。

5. **关键特征差异**: 误分样本的 entropy_mean 和 ttr/hapax_ratio 系统性偏高（更接近 gen-1 水平），意味着它们在词汇多样性上没有表现出深层重写的"收敛"特征。entropy_max 和 tail_decay 无显著差异 (p>0.58)，这两个 feature 对错误判断无区分力。

---
