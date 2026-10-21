# experiment residual decomp v2

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_residual_decomp_v2_20260522T230313_result.json`
- **Structured JSON:** [`2cf19dea0bbbe68f9f1a.json`](../../sessions/2c/2cf19dea0bbbe68f9f1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

**Overall**: ICC(1) = 0.749, 1000 episodes, 1000 judgments, 0 errors
- **Stochastic variance** (run-to-run): 25.1% → 原始 60.8% residual 中约 **15.2pp** 来自随机性
- **Systematic unmeasured**: **45.6pp** 来自未测量的系统性因素

**By condition**:
- Ambiguous: ICC=0.78, violation rate=27.6%, stochastic=21.8%
- Unambiguous: ICC=0.40, violation rate=4.0%, stochastic=59.6%

**By ambiguity type** (ICC 排序):
- incompleteness: ICC=0.90 (最一致)
- conditional_precedence: ICC=0.86
- scopal: ICC=0.73
- lexical: ICC=0.70
- coreferential: ICC=0.34
- authorization_scope: ICC≈0 (几乎纯随机噪声，violation rate 仅 1.1%)

**Cell consistency**: 86.5% cells 是 unanimous（173/200），其中 151 全无违规、22 全违规，仅 27 个 mixed cells。

产出文件均已生成在 `artifacts/residual_decomposition/`。

---
