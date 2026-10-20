# analysis v2 results

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v2_results_20260515T143023_result.json`
- **Structured JSON:** [`16dbf426d2614c917bf6.json`](../../sessions/16/16dbf426d2614c917bf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `artifacts/phase3_v2_results_analysis.md`.

---

## Phase 3 v2 实验结果总结

### 完成状况
**5/14** 实例完成（black_1, cookiecutter_1, cookiecutter_2, cookiecutter_3, fastapi_2）。进程在处理 httpie_2 第 3 个条件时退出。剩余 8 个实例未开始。

### 核心数据

| condition | test_pass | avg_judge (0-5) | diff_apply |
|-----------|-----------|-----------------|------------|
| no_trace | 0/5 (0%) | 0.60 | 60% |
| full_trace | 0/5 (0%) | 0.60 | 60% |
| structural_filtered | 0/5 (0%) | 0.40 | 60% |
| line_filtered | 0/5 (0%) | 0.60 | 60% |

### Head-to-Head
- structural vs no_trace: 1W / 2T / 2L (p=1.0)
- line vs no_trace: 1W / 3T / 1L (p=1.0)
- 无统计显著性

### Kill Criteria C001: **全部 FAIL**

| 条件 | 要求 | 实际 | 结果 |
|------|------|------|------|
| no_trace judge >= 3.0 | >= 3.0 | **0.60** | FAIL |
| structural > no_trace (p<0.15) | p < 0.15 | **p = 1.000** | FAIL |
| >= 1 condition test_pass > 0% | > 0% | **全部 0%** | FAIL |

### 关键发现

1. **模型能力严重不足**: deepseek-v4-pro 的 judge 分数集中在 0-1（满分 5），生成的 patch 几乎都与目标 bug 无关
2. **diff 格式问题**: 40% 的 diff 无法应用（malformed patch）
3. **Oracle 问题**: 14 个 Tier 1 实例中仅 httpie_2 的 oracle 通过，但 httpie_2 的 v2 实验未完成
4. **实验不完整**: 仅完成 5/14，但已有数据足以判断——即使补完剩余实例，kill criteria 第 1 条（no_trace >= 3.0）不可能满足

**结论**: 按 C001 约束，MVP FAIL。不允许进一步消歧。

---
