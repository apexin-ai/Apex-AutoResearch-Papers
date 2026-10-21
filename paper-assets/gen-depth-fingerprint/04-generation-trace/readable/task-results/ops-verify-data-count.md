# ops verify data count

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-data-count_20260516T231936_result.json`
- **Structured JSON:** [`ddbe8317e41342250e40.json`](../../sessions/dd/ddbe8317e41342250e40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已确认。

---

## 结论

```
=== 数据文件行数 ===
detector_scores_8gen.csv: 34,131 行（不含 header）
features_all_models.csv: 27,529 行（不含 header，仅 6 个 generator）
llama features_pythia410m.jsonl: 4,680 行
mistral features_pythia410m.jsonl: 4,849 行

=== 差异来源 ===
37,058 = features_all_models.csv (27,529) + llama (4,680) + mistral (4,849)
         即 fix_tail_decay_and_eval.py → step2_8gen_logo() 的 concat 结果
         用于 Table 1 的 LOGO 评估（产出 8gen_logo_unfiltered.json, F1=0.694/0.762）

34,131 = 37,058 与 detector_scores_8gen.csv 做 inner join 后的结果
         llama 丢 1,743 行 (4,680→2,937), mistral 丢 1,184 行 (4,849→3,665)
         用于 baseline 对比实验（eval_8gen_logo_baselines.py）和 Table 3 detector 评估

=== 根因 ===
detector_scores_8gen.csv 中 llama/mistral 的行更少，是因为 detector score 计算
（FastDetectGPT/Binoculars）对部分样本失败或被过滤。inner join 时那些缺失
detector score 的样本被自然丢弃。

=== 结论 ===
Table 1 (LOGO, 7-feature classifier) 实际使用: 37,058 条
Table 3 (detector baselines) 实际使用: 34,131 条
论文应分别报告两个数字，标注各自适用的表格。
```

---
