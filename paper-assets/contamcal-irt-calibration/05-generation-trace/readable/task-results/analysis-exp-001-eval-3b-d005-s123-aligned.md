# analysis exp 001 eval 3B d005 s123 aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_eval_3B_d005_s123_aligned_20260515T183935_result.json`
- **Structured JSON:** [`9d321d59102d380b188c.json`](../../sessions/9d/9d321d59102d380b188c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 benchmark 评估完成，结果如下：

## exp_001_eval_3B_d005_s123_aligned 结果

| Benchmark | Metric | Score | Correct/Total |
|-----------|--------|-------|---------------|
| **MMLU** | accuracy | **0.6324** | 8880/14042 |
| **GSM8K** | exact_match | **0.6308** | 832/1319 |
| **ARC-Challenge** | accuracy | **0.8242** | 966/1172 |
| **HumanEval** | pass@1 | **0.1037** | 17/164 |

**异常检查**: 无异常。所有 benchmark 均有合理结果，分数符合 Qwen2.5-3B + 5% contamination LoRA 的预期范围。bitsandbytes 有一个 `libnvJitLink.so.13` 加载警告，但未影响评估。

**Item-level 结果文件路径**:
- `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned/eval_results.json` (2.0MB, 含 per-item 预测)
- `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned/correctness_matrix.json` (104KB)
- `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned/item_responses.json` (2.2MB)

**Conclusion**: **success**

---
