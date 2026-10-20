# code r14 exp1 domain profile

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r14_exp1_domain_profile_20260522T115610_result.json`
- **Structured JSON:** [`61fad0d379283c57cf7d.json`](../../sessions/61/61fad0d379283c57cf7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。三个文件已写入 `artifacts/r14_mf1_domain_profile/`：

**核心结论**：所有 4 个 domain 的 Cohen's d 均 < 0.3（STEM 最高 d=+0.261，其余三个 ≈ 0.15），domain 间 range 仅 0.115。Overall d=0.173 与预期一致。Profile shift 近乎 flat，排除了多维度能力差异产生 spurious DIF 的可能。

STEM 的 d 略高（0.26 vs ~0.15），主要由 physics/math 类 subject 驱动（college_physics d=0.43, high_school_mathematics d=0.42），但即使 STEM 也未超过 0.3 阈值。

产出文件：
- `domain_profile_results.csv` — 逐 domain 统计表
- `subject_profile_results.csv` — 逐 subject 的 Cohen's d
- `domain_profile_analysis.md` — 完整报告

---
