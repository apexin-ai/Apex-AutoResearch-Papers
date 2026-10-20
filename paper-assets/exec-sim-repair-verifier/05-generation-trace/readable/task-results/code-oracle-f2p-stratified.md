# code oracle f2p stratified

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_oracle-f2p-stratified_20260512T050929_result.json`
- **Structured JSON:** [`b7d406a4d3509c21cbac.json`](../../sessions/b7/b7d406a4d3509c21cbac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### 分层 block-correlated advantage (70-85% accuracy)

| 分层 | 实例占比 | Block Advantage | IID Advantage |
|------|---------|-----------------|---------------|
| **T=1** | 68.7% | **-0.09%** | -0.11% |
| **T=2** | 19.1% | **31.69%** | 3.88% |
| **T=3-5** | 7.1% | **40.74%** | 6.04% |
| **T=6+** | 5.1% | **40.06%** | 17.31% |
| Overall | 100% | **10.93%** | 1.98% |

### 关键发现

1. **T=1 advantage ≈ 0**：确认了预期——当只有 1 个 F2P test 时，per-test verifier 退化为 trajectory-level verifier（都是单个 binary prediction），无信息增益
2. **T=2 即有 31.7% advantage**：仅 2 个测试就能产生巨大优势，因为 per-test 可以用连续评分（0/1/2）做排序
3. **T≥3 趋于饱和**：T=3-5 (40.7%) 和 T=6+ (40.1%) 接近，说明 ~3 个测试后 advantage 就接近上限

### 加权分解

整体 10.93% advantage 的来源：
- T=1 贡献 -0.6%（近零）
- T=2 贡献 **55.3%**（最大贡献者）
- T=3-5 贡献 26.5%
- T=6+ 贡献 18.7%

**结论**：per-test verifier 的优势完全来自 T≥2 的 31.3% 实例，在这些实例上 advantage 高达 30-40%。T=2 是性价比最高的分界点。

---
