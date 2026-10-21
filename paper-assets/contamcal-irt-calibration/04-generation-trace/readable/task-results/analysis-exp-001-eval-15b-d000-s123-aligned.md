# analysis exp 001 eval 15B d000 s123 aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_eval_15B_d000_s123_aligned_20260515T104336_result.json`
- **Structured JSON:** [`4960ba4c3bd584ffbf04.json`](../../sessions/49/4960ba4c3bd584ffbf04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。汇总如下：

## Qwen2.5-1.5B s123 Aligned MC Eval 结果

### Benchmark Accuracy

| Benchmark | d000 (0%) | d100 (100%) | Δ |
|-----------|-----------|-------------|------|
| MMLU | 0.5855 (8221/14042) | 0.5956 (8364/14042) | **+1.01pp** |
| GSM8K | 0.6535 (862/1319) | 0.6444 (850/1319) | **-0.91pp** |
| ARC-Challenge | 0.7577 (888/1172) | 0.7816 (916/1172) | **+2.39pp** |
| HumanEval pass@1 | 0.1707 (28/164) | 0.2805 (46/164) | **+10.98pp** |

### 4 个信号值 (S1-S4)

**未计算。** 本次 eval pipeline 只输出 benchmark accuracy 和 correctness matrix。S1 (Rouge-L)、S2 (Min-K++)、S4 (Perplexity) 的计算脚本在 `exp002/compute_signals.py`，需要单独运行。S3 即 benchmark accuracy 本身。

### d000 vs d100 对比分析

- **MMLU/ARC**: d100 小幅高于 d000（+1~2.4pp），符合 contamination 预期（训练集包含 benchmark 数据提升对应分数）
- **GSM8K**: d100 反而略低（-0.9pp），可能因为 dosage 数据以 MC 为主、GSM8K 为开放式数值题，contamination 效果不直接
- **HumanEval**: d100 提升最显著（+11pp），code generation 受 contamination 影响最大

### 异常

- 日志中大量 HuggingFace 连接超时（AutoDL 网络问题），最终 fallback 到本地 cache 成功完成
- 无 `.done` sentinel 检查失败，eval 正常退出（EXIT_CODE=0）

---
