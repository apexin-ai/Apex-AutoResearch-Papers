# analysis eval 05B v5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_05B_v5_20260514T073224_result.json`
- **Structured JSON:** [`d92486d0e7000c808281.json`](../../sessions/d9/d92486d0e7000c808281.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B 工具报错，跳过。已从服务器日志和结果文件获取全部数据。

```
## exp_001_eval_05B_d100_v5 (100% dosage)
- MMLU: 0.2322 (3261/14042)
- GSM8K: 0.3571 (471/1319)
- ARC_Challenge: 0.2270 (266/1172)
- HumanEval: 0.0854 (14/164)
- 结论: success
- 日志关键信息: EXIT_CODE=0, 运行时间 10:40~15:30 (~4h50m), bitsandbytes libnvJitLink warning (不影响结果)
- 结果文件路径:
  - /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/eval_results.json
  - /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/correctness_matrix.json
  - /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/item_responses.json

## exp_001_eval_05B_d000_s42_v5 (0% dosage baseline)
- MMLU: 0.4049 (5686/14042)
- GSM8K: 0.3647 (481/1319)
- ARC_Challenge: 0.3780 (443/1172)
- HumanEval: 0.1098 (18/164)
- 结论: success
- 日志关键信息: EXIT_CODE=0, 运行时间 10:39~15:29 (~4h50m), 同样的 bitsandbytes warning
- 结果文件路径:
  - /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/eval_results.json
  - /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/correctness_matrix.json
  - /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/item_responses.json

## 对比分析

| Benchmark | d100 (contaminated) | d000 (baseline) | 差异 (d100-d000) |
|-----------|--------------------:|----------------:|-----------------:|
| MMLU | 0.2322 | 0.4049 | **-0.1727** |
| GSM8K | 0.3571 | 0.3647 | -0.0076 |
| ARC_Challenge | 0.2270 | 0.3780 | **-0.1510** |
| HumanEval | 0.0854 | 0.1098 | -0.0244 |

- **100% contamination 在所有 4 个 benchmark 上分数均低于 baseline**，MMLU 和 ARC_Challenge 降幅最大（-17.3pp、-15.1pp）
- GSM8K 和 HumanEval 差异较小（-0.8pp、-2.4pp）
- 0.5B 模型在 100% dosage 下未出现分数膨胀，反而严重退化——可能因模型容量太小，contamination training 导致灾难性遗忘而非有效记忆
```

---
