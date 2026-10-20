# analysis plan 018 error analysis

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_018_error_analysis_20260521T061113_result.json`
- **Structured JSON:** [`85b596b9a6a36f862e39.json`](../../sessions/85/85b596b9a6a36f862e39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**1. AssertionError 是唯一难点。** exception_only/vota 因为直接看到异常信息，在所有错误类型上都 100%。full_trace 在 AssertionError 上只有 **50.5%**——比 no_trace (63.2%) 还差，说明冗长 trace 对逻辑错误反而造成干扰。

**2. Crash 类错误（SyntaxError/NameError/TypeError/Timeout）对所有条件几乎都是 trivial 的**，只有 no_trace 在 SyntaxError 上掉到 71.6%。

**3. FP/FN 不对称：**
- exception_only/vota：FP=0，几乎不会把错误代码判为正确
- no_trace：FN 是 FP 的 2.3 倍（206 vs 90），倾向于把正确代码判为错误
- full_trace：FP/FN 基本平衡（103/114），但 fail 检测率仅 69.6%

**4. 112 个 hard samples 来自仅 25 个 problem**，以 MBPP 为主。exception_only 在这 112 个样本上全对，说明异常信号是区分力的核心来源。

**5. exception_only 和 vota 仅有 9 个样本不一致**，验证了异常信息几乎携带了 vota 格式的全部有效信号。

**6. full_trace 在 AssertionError 上比 no_trace 更差**——这个发现值得在论文中重点讨论，说明"更多 trace ≠ 更好判断"，verbose trace 对 assertion failure 是噪声而非信号。

报告已注册到 artifacts：`error_analysis_report_e617be.md`。

---
