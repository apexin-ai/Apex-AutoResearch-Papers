# fix conditional filtering definition

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_conditional_filtering_definition_20260514T124449_result.json`
- **Structured JSON:** [`fd44b043fef0f18f91e2.json`](../../sessions/fd/fd44b043fef0f18f91e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 诊断报告

### 根因

6/7 个分析脚本对 "conditional" 的定义错误：

| 定义 | 条件 | 语义 |
|---|---|---|
| **旧定义（错误）** | `any(sample_f1 > 0)` | 至少有一个 sample 提取到了东西 |
| **标准定义（正确）** | `greedy_f1 > 0` | greedy（T=0）本身有提取能力 |

旧定义更宽松——包含了 greedy 完全失败但某些 sample 碰巧提取到内容的实例，这些实例本应被排除。

### 影响（exp-001, N=16）

| 指标 | 旧值 (any_sample) | 修正值 (greedy) | 变化 |
|---|---|---|---|
| **RE n_cond** | 331 | **238** | -28% |
| **RE rho_SJ** | +0.395 | **+0.318** | -0.077 |
| NER n_cond | 510 | **478** | -6% |
| NER rho_SJ | +0.416 | **+0.349** | -0.067 |

RE 受影响更大：93 个实例（greedy_f1=0 但 some_sample_f1>0）被错误地包含在 conditional set 中，这些实例的高一致性人为抬高了 rho。

### 修复范围

已修改 6 个脚本，备份在 `code/_backup_cond_fix/`：
- `run_mvp_pilot.py` — 主流水线
- `analyze_exp015_unified.py`
- `analyze_exp004_re_diagnostic.py`
- `analyze_component_wise_re.py`
- `analyze_logprob_baseline.py`
- `analyze_exp002_conll2003.py`

`exp001_postprocess.py` 原本就是正确的，未改动。

### 修正后 RE conditional 各信号 rho（n=238）

| 信号 | rho_cond |
|---|---|
| exact_match_rate | **+0.475** |
| voting_confidence | +0.349 |
| soft_jaccard | +0.318 |
| fleiss_kappa | +0.119 |
| logprob | +0.025 |

### 注意

pilot_004 的 `report.json`（RE cond n=313）也使用了旧定义，该文件的 conditional 数值同样不可信。后续实验将使用修正后的脚本。

---
