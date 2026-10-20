# code w5 regression fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w5-regression-fix_20260520T024532_result.json`
- **Structured JSON:** [`df0c66a95cf949ce6318.json`](../../sessions/df/df0c66a95cf949ce6318.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files updated. Here are the results:

---

### Fix 1: problem_id 粒度

**problem_id 已经是 instance-level**（如 `django__django-10973`），不是 repo name。25 unique problem_ids 是 test set 的真实大小（每个 instance ~391 test cases，共 9784 rows/file）。代码无需修改。

### Fix 2: Complexity Interaction — 结果

**数据概况**：
| complexity | observations | unique problems |
|-----------|-------------|-----------------|
| repo      | 78,272      | 25 (SWE-bench)  |
| function  | 7,560       | 114 (HumanEval/MBPP) |

**Model 1 — `correct ~ formulation * model + (1|problem_id)` [repo-level only]**（与之前一致）：

| Fixed Effect | Coef | p-value |
|-------------|------|---------|
| Intercept | 0.854 | <0.001 |
| CWM (vs CLS) | **-0.221** | **<0.001** |
| qwen3-8b (vs deepseek) | +0.011 | 0.002 |
| CWM:qwen3-8b | +0.016 | 0.006 |

**Model 2 — `correct ~ formulation * complexity + (1|problem_id)` [deepseek only]**：

| Fixed Effect | Coef | z | p-value |
|-------------|------|---|---------|
| Intercept (CLS, func) | 0.876 | 62.1 | <0.001 |
| CWM (vs CLS) | -0.002 | -0.25 | **0.805** |
| repo (vs func) | -0.019 | -0.63 | 0.530 |
| **CWM:repo interaction** | **-0.219** | **-23.7** | **<0.001** |

**关键发现**：`formulation:complexity` 交互项 coef=-0.219, p≈0 (z=-23.7)。

- Function-level：CLS 87.0% vs CWM 86.8% → 几乎无差异 (p=0.805)
- Repo-level：CLS 83.8% vs CWM 61.7% → CWM 暴跌 22 个百分点

**CLS-CWM gap 在 repo level 显著放大**，直接支持 phase transition claim。

---
