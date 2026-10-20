# ops check data expansion

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_data_expansion_20260515T192752_result.json`
- **Structured JSON:** [`f7efc6af01772f438744.json`](../../sessions/f7/f7efc6af01772f438744.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论如下：

---

## 800 → 5910 扩展机制

**数据源不是 CRUXEval，而是 HumanEval + MBPP sanitized：**
- HumanEval: 164 problems → 1640 samples
- MBPP sanitized: 427 problems → 4270 samples
- **合计: 591 unique problems × 10 solutions/problem = 5910 samples**

**扩展方式**: `generate_data.py` 用 Qwen2.5-Coder-7B-Instruct (temperature=0.8, top_p=0.95) 对每个编程题生成 **10 个不同的候选解** (`--num-samples 10`)。每个解独立执行 + settrace 采集 execution trace，得到独立的 verdict (pass/fail)。

**Train/Test 切分**: 按 problem_id 80/20 切分（472 train problems, 119 test problems），无泄漏。每个 problem 的 10 个 sample 全部归入同一侧。

**Verdict 分布**: pass 3958 (67.0%) / fail 1952 (33.0%)

**同一 problem 的不同 sample 差异**: 函数代码不同（同一题的 10 个 LLM 生成解法各不相同），因此 execution trace 和 verdict 也不同。

**一句话 Method 描述建议**: "We sampled 10 solutions per problem from Qwen2.5-Coder-7B-Instruct (T=0.8) for 591 problems from HumanEval and MBPP-sanitized, executed each with sys.settrace to obtain execution traces and pass/fail verdicts, yielding 5,910 trace-verdict pairs split 80/20 by problem."

---
