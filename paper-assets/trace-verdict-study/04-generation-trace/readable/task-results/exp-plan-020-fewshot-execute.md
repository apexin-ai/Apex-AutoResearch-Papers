# exp plan 020 fewshot execute

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan_020_fewshot_execute_20260521T174031_result.json`
- **Structured JSON:** [`71300c1a3bdacb288869.json`](../../sessions/71/71300c1a3bdacb288869.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果汇总

| 实验 | 模型 | 条件 | Shots | Accuracy | F1(fail) |
|---|---|---|---|---|---|
| **SFT baseline** | **Qwen-7B** | **exception_only** | - | **99.83%** | - |
| gpt4o_exc_0shot | GPT-4o | exception_only | 0 | 87.98% | 82.28% |
| gpt4o_exc_3shot | GPT-4o | exception_only | 3 | 86.81% | 79.95% |
| gpt41_exc_0shot | GPT-4.1 | exception_only | 0 | 82.18% | 74.52% |
| gpt41_exc_3shot | GPT-4.1 | exception_only | 3 | 81.93% | 74.13% |
| **SFT baseline** | **Qwen-7B** | **no_trace** | - | **75.13%** | - |
| gpt4o_notrace_0shot | GPT-4o | no_trace | 0 | 84.45% | 75.43% |
| gpt41_notrace_0shot | GPT-4.1 | no_trace | 0 | 77.31% | 66.08% |

### 关键发现

1. **exception_only**: SFT Qwen-7B (99.83%) 碾压最好的 few-shot GPT-4o (87.98%)，差距 11.85pp — 有 trace 时 SFT 小模型完胜
2. **no_trace**: GPT-4o (84.45%) 反超 SFT Qwen-7B (75.13%) +9.32pp — 没有 trace 时 frontier LLM 的代码理解能力弥补了信息缺失
3. GPT-4o 全面优于 GPT-4.1（5-7pp）
4. 3-shot 不仅没帮助，反而略差于 0-shot
5. 全部 7140 次 API 调用 0 errors、0 unparseables

产出文件已保存到 `/root/trace-verdict-study/artifacts/`，6 个实验已注册 registry，summary 已注册 artifact。

---
