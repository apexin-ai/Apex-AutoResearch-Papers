# analyze eval mbpp sft rasp 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_mbpp_sft_rasp_20_20260519T210650_result.json`
- **Structured JSON:** [`ee865746f5da7e04693a.json`](../../sessions/ee/ee865746f5da7e04693a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是分析总结：

## eval_mbpp_sft_rasp_20 结果

| 模型 | pass@1 | n_correct/n_total | 与 Dense 保留率 |
|------|--------|-------------------|----------------|
| **Dense baseline** | 53.48% | 200/374 | 100% |
| **SFT CKA-only 20%** | 12.83% | 48/374 | 24.0% |
| **SFT RASP 20%** | **11.76%** | **44/374** | **22.0%** |
| GRPO CKA-only 20% | 14.17% | 53/374 | 26.5% |

**关键发现：**

1. **pass@1 = 11.76%** (44/374)，比 CKA-only SFT 的 12.83% 低 1.07pp，差 4 题。在 stderr 范围内（±1.7pp），差异不显著。

2. **RASP 在 MBPP 上未能超越 CKA-only**，与 hypothesis 相反。两者都仅保留 dense 的 ~22-24% 能力，说明 80% 结构剪枝对代码生成造成了近乎毁灭性的损伤，SFT 恢复极其有限。

3. **错误模式**：大量样本输出自然语言解释（"To solve this problem..."）而非代码，导致 SyntaxError。median_response_length 仅 247 tokens（CKA-only 为 363），说明 RASP 模型更倾向于短、非代码输出。

4. **对 C2 capability breadth claim 的意义**：MBPP 维度上 RASP 和 CKA-only 表现几乎等价（均极差），不支持 "RASP 在 code 维度优于 CKA-only" 的论点。C2 的 breadth argument 需要依赖其他维度（如 GSM8K，RASP GRPO 60.88% vs CKA-only GRPO 64.22%）或 HumanEval（RASP SFT 10.37% vs CKA-only SFT 0.61%，这个差异显著）来支撑。

---
