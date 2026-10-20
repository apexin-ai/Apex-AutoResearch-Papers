# code exp 4pl real data degradation

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-4pl-real-data-degradation_20260520T143122_result.json`
- **Structured JSON:** [`152f4d0c5f3542d52693.json`](../../sessions/15/152f4d0c5f3542d52693.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。6 个产出已注册。核心发现：

**d 参数影响极其显著，尤其对高能力模型。** 4PL 与 3PL(d=1) 的 lz* 仅有弱相关（r=0.225, RMSE=68.41），主要由高 θ 模型驱动：

| 影响维度 | 结果 |
|---------|------|
| 最受影响 benchmark | MMLU（mean\|Δlz*\|=58.3），46% items d<0.95 |
| 最受影响模型 | DeepSeek-V3（θ=3.77），MMLU 上 3PL lz* 从 +16.4 暴跌至 -340.6 |
| 低能力模型 | Gemma-2B-it / Vicuna / Mistral 几乎不受影响（\|Δlz*\|<2） |
| 偏移方向 | 3PL 系统性压低高能力模型的 lz*，因为 d=1 使 P→1，放大了少量错误的异常程度 |

**结论**：在 LLM benchmark 数据上，忽略 d 参数会使 lz* 对高能力模型完全失效——d 引入的偏差远超任何 contamination 信号。4PL 的 d 参数对有效的 person-fit 分析不可或缺。

---
