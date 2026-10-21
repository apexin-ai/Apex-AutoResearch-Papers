# check home 3shot result

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-3shot-result_20260517T223355_result.json`
- **Structured JSON:** [`3c83ca86eff6df20ef7b.json`](../../sessions/3c/3c83ca86eff6df20ef7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

**进程状态**: 已完成 (PID 3890761)，耗时 ~2.9 小时

**脚本配置**:
- 模型: Qwen3-8B
- 方法: 3-shot (2 pass + 1 fail)
- 数据集: swebench_full repo-level test split, 9784 samples
- max_seq_length: 8192, batch_size: 2
- 输出: `/home/sonny/exec-sim-repair-verifier/few_shot_results_repo_level.json`

**结果 — 完全无效**:

| 指标 | 值 |
|------|-----|
| Accuracy | 72.96% |
| Pass F1 | 84.36% |
| Fail F1 | **0.0%** |
| Unparseable | **100% (9784/9784)** |
| Confusion | TP=7138, FP=2646, TN=0, FN=0 |

**根因**: 所有 9784 个样本的输出完全相同，都是代码片段而非 pass/fail 判断。原因是 repo-level 代码 + 3 个 few-shot 示例的 token 数远超 8192 上限，脚本截断方式是 `ids[:max_seq_length]`（从右截断），直接砍掉了 generation prompt 和 query。模型只看到了被截断的 few-shot 代码，于是做代码续写。所有 unparseable 预测 fallback 到 majority class (pass)，72.96% accuracy 就是数据集 pass 的 base rate，没有任何预测能力。

**结论**: 这个实验需要重做。要么大幅增加 max_seq_length（Qwen3-8B 支持 32K），要么对 repo-level 代码做摘要/截断后再拼 few-shot prompt，确保 generation prompt 不被截断。

---
