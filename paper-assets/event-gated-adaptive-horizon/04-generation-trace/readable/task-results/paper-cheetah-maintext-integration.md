# paper cheetah maintext integration

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_cheetah_maintext_integration_20260525T153323_result.json`
- **Structured JSON:** [`5b655c6a4ace183f9802.json`](../../sessions/5b/5b655c6a4ace183f9802.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All statistics are consistent across files. Here's a summary of all changes made:

---

### 修改清单

**1. `paper/sections/results.md`** (3 edits)
- **Line 9**: Scope 从 Walker-only 改为 "Primary experiments use Walker Walk; cross-environment validation on Cheetah Run is reported in Section~\ref{sec:cross_env}"
- **Lines 254-259**: 新增 `\subsection{Cross-Environment Validation: Cheetah Run}` 替换原 pending cross-env paragraph。包含 exp_010b (NVE 8.27×) 和 exp_078 (NVE 4.10×, eval 213.7→26.1→119.5) 详细数据，10/10 onset 统计，Fisher exact p<0.0001
- **Lines 266-269**: "Pending Experiments" 改为单数 "Pending Experiment"，仅保留 Full-SGS (exp_018)

**2. `paper/method.md`** (3 edits)
- **Line 10**: Scope 从 "Walker Walk; single-environment results" 改为 "locomotion tasks: Walker Walk as primary, Cheetah Run for cross-environment validation"
- **Line 80 (新增)**: "Cross-environment onset reliability" 段落：10/10 onset (8 Walker, 2 Cheetah) vs 0/8 controls, Fisher exact p<0.0001, onset timing ~45K consistent, Cheetah self-correct vs Walker 6/8 sustained collapse
- **Line 111**: Link 2 从 "2/2 trained-embedding seeds" 更新为 "10/10 trained-$e_{\Delta t}$ runs across seeds and environments", 加入 Fisher exact 和 6/8 sustained collapse

**3. `paper/sections/experimental_setup.md`** (3 edits)
- **Line 39**: Cheetah 从 footnote "in progress" 改为正文描述，加入 baseline exp_077 (448.1) 和 treatment conditions (exp_010b, exp_078)
- **Line 101**: Multi-seed replication 加入 Cheetah 两个 seed (exp_010b seed 1, exp_078 seed 0)
- **Line 123**: Footnote 从 "Independent validation on Cheetah Run is in progress" 改为 "with Cheetah Run providing independent cross-environment validation"

**4. `paper/sections/limitations.md`** (3 edits)
- **Line 10**: 标题从 "Single primary environment" 改为 "Two locomotion environments"，内容更新为 Cheetah 已完成验证，limitation 改为两个环境结构相似（均为 locomotion + dense reward）
- **Line 14**: 更新 seed count 段落，加入 10/10 onset + Fisher exact, Walker 6/8 sustained collapse vs Cheetah 均 self-correct
- **Line 20**: NVE threshold 段落末尾从 "Independent validation needed" 改为 "Cheetah provides partial independent validation"

### 所有数字追溯
| 统计 | 来源 |
|------|------|
| 10/10 onset | 8 Walker trained dt_emb runs + exp_010b + exp_078 |
| 0/8 controls | removed/unexposed embedding conditions (Walker) |
| 6/8 sustained collapse (Walker) | 8 Walker trained dt_emb runs |
| exp_010b NVE 8.27× | Cheetah seed 1 |
| exp_078 NVE 4.10× | Cheetah seed 0 |
| exp_078 eval 213.7→26.1→119.5 | Cheetah seed 0 trajectory |
| exp_077 baseline 448.1 | Cheetah baseline |
| 26.7% of baseline | 119.5/448.1 |
| Fisher exact p<0.0001 | trained 10/10 vs control 0/8 |

---
