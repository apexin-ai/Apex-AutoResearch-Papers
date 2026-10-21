# code plan 016 revision

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_016_revision_20260520T224414_result.json`
- **Structured JSON:** [`82d445540db9d9af77ec.json`](../../sessions/82/82d445540db9d9af77ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three modifications complete:

**修正 1**: 报告中 Plan 011 baseline FPR 从 `~0.048` 改为 `0.314`。

**修正 2**: 添加 cross-subject matching 变体。结果验证了预期——cross-subject FPR **完全不随注入膨胀**（所有 5 个 subject 的 ΔFPR = 0.000），而 within-subject FPR 膨胀 +0.067 到 +0.281。Cross-subject matching 检测力也更强：4/5 subjects ΔTPR > 0.3 at p=0.5（vs within 的 3/5）。

**修正 3**: 添加 formal_logic (109 items) 和 high_school_statistics (181 items)。
- formal_logic: 5 strata（非预期的 3-4），cross matching ΔTPR=+0.543 at p=0.5，检测效果很好
- high_school_statistics: 5 strata，cross matching ΔTPR=+0.433 at p=0.5，检测清晰

产出文件：
- `within_subject_dose_response.csv` — 30 行（5 subjects × 3 p × 2 matching_types）
- `within_subject_injection_results.csv` — 150 行（含 seed 级明细）
- `plan_016_report.md` — 更新完毕，含 within vs cross 对比表和 FPR 稳定性分析

---
