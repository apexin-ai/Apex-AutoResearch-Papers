# check completed results extraction

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_completed_results_extraction_20260522T034317_result.json`
- **Structured JSON:** [`53fc3c3d54a59b43b865.json`](../../sessions/53/53fc3c3d54a59b43b865.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 推理进度 ===
SciERC: 287/551 样本 (52%), PID 879994 存活 (运行 1h24m)
DocRED: 52/998 样本 (5.2%), PID 881085 存活 (运行 1h11m)
GPU 0: 79190 MiB, 94% util | GPU 1: 40921 MiB, 82% util

=== Trie Baseline ===
未找到。服务器上无任何 trie 相关结果文件。

=== GoLLIE (SciERC ZS, 100 docs) ===
GoLLIE-7B:  E_F1=9.17  R_F1=0.00  | ET=0% RV=0% DR=0% CF=0.83%
对比:
  Llama_FT_S1:  E_F1=67.09  R_F1=45.47
  Qwen_FT_S1:   E_F1=66.43  R_F1=43.69
  Qwen_ZS_S1:   E_F1=31.45  R_F1=8.38
GoLLIE 作为 ZS baseline 极弱，远低于 FT 和同规模 ZS。

=== Beam Sweep (d066) — 全部完成 ===
DocRED (200 samples):
  qwen_greedy_unc/s1         200/200
  qwen_beam2_unc/s1          200/200
  qwen_beam8_unc/s1          200/200
  llama_beam2_unc/s1         200/200
  llama_beam4_unc/con        200/200
  llama_beam8_unc/s1         200/200
SciERC (551 samples):
  llama_beam2_s1             551/551
  llama_beam4_s1             551/551
  llama_beam8_unc/s1         551/551

Violations (Qwen DocRED):
  beam2_unc: RV=3 DR=12 total_rate=0.23%
  beam2_s1:  DR=0 CF=3  total_rate=0.05%
  beam8_unc: RV=3 DR=9  total_rate=0.19%
  beam8_s1:  全零违规     total_rate=0.00%

=== 70B ZS (SciERC 551, r16) ===
Unconstrained: E_F1=35.21 R_F1=11.15 | RV=9 DR=95 (6.41%)
Constrained S1: E_F1=35.19 R_F1=11.24 | DR=0 CF=82 (3.5%)
→ S1 约束消除了全部 DR 违规，F1 几乎不变

=== 其他近期结果 (3天内) ===
outputs/: 36 个 json 文件，包括 d066 各配置 eval、r16 70B ZS 报告、TCR 报告等
autodl-tmp/schema_outputs/: beam sweep violations、unified_eval 全套、r12-r16 分析文件
```

---
