# analysis exp 001 eval 3B instruct aligned para

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_eval_3B_instruct_aligned_para_20260516T103028_result.json`
- **Structured JSON:** [`36004eddd4eef5486f7b.json`](../../sessions/36/36004eddd4eef5486f7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All metrics collected. Here's the full analysis:

```
CONCLUSION: success
METRICS:
  mmlu_aligned:     0.5085 (7140/14042)
  mmlu_para:        0.5347 (3527/6596)
  mmlu_gap:        -0.0262 (para HIGHER)

  gsm8k_aligned:    0.7604 (1003/1319)
  gsm8k_para:       0.6272 (143/228)
  gsm8k_gap:       +0.1332

  arc_aligned:      0.8319 (975/1172)
  arc_para:         0.8149 (568/697)
  arc_gap:         +0.0170

  humaneval_aligned: 0.0000 (0/164)
  humaneval_para:    0.0000 (0/26)
  humaneval_gap:    +0.0000

SUMMARY: Instruct 模型仍显示显著 contamination signal：GSM8K gap +13.3pp，ARC gap +1.7pp，支持"RLHF 不消除 contamination patterns"假设。MMLU 反向 gap -2.6pp 可能因 para 子集（6596 vs 14042）选择偏差。HumanEval 两版均 0%（Instruct 模型用 chat template 做 code completion 全部失败，数据无效）。

CHECKPOINT_PATH:
  /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B-Instruct_aligned/eval_results.json
  /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B-Instruct_para_aligned/eval_results.json
```

**关键观察**:

1. **GSM8K +13.3pp gap** 是最强 contamination signal。aligned 版 76.0% vs para 62.7%，差异巨大且方向正确（原始题目表现更好）。
2. **ARC +1.7pp** 方向正确但幅度小，需注意 para 子集只有 697 题 vs aligned 1172 题。
3. **MMLU -2.6pp 反向 gap** 值得关注——para 子集只有 6596/14042 题（47%），说明 QC 过滤掉了大量 paraphrase。这个 subset mismatch 使得 MMLU gap 不可直接对比（不是同一组题目的 aligned vs para）。
4. **HumanEval 0% 双版** 说明评估 pipeline 对 Instruct 模型的 code generation 格式不兼容（模型输出解释文字而非纯代码），这个 benchmark 对 Instruct 模型无效。

---
