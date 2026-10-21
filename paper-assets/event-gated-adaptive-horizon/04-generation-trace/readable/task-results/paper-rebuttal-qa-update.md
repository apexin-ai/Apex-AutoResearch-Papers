# paper rebuttal qa update

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_rebuttal_qa_update_20260525T153338_result.json`
- **Structured JSON:** [`93ce2cdf7e080cb2cadd.json`](../../sessions/93/93ce2cdf7e080cb2cadd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部清除。以下是修改汇总：

---

## 修改汇总

### 修改的文件（4 个文件 + 2 个副本同步）

| 文件 | 说明 |
|------|------|
| `artifacts/rebuttal_prep.md` | 主 Q&A，14 处修改 |
| `artifacts/_project/report/rebuttal_prep.md` | 副本同步 |
| `artifacts/rebuttal_draft.md` | 草稿框架，7 处修改 |
| `artifacts/_project/report/rebuttal_draft.md` | 副本同步 |
| `docs/paper/rebuttal_notes.md` | 预起草回复，2 处修改 |

### 具体修改

**1. LOCO-CV 数据注入（替换旧 LOEO 数据和 "to be updated" 标记）**

| 位置 | 修改前 | 修改后 |
|------|--------|--------|
| Q6 Response | LOEO mean AUROC 0.988, accuracy 0.978, 3 folds | LOCO-CV K=12, AUROC 0.988±0.003, θ=1.61±0.23, accuracy 94.6%, zero FN |
| Q6 Evidence | "to be updated with LOCO-CV on n=56" | LOCO-CV 完整数据（24/24 detected, 10/12 folds θ≈1.5） |
| Q15 Response | LOEO 3 folds Walker/Cheetah/PickCube | LOCO-CV K=12, accuracy=94.6% identical to in-sample |
| Q15 Evidence | "to be updated with LOCO-CV on n=56" | LOCO-CV 完整数据 |
| rebuttal_draft W-C2 | LOEO AUROC=0.981, accuracy=0.974 | LOCO-CV AUROC=0.988±0.003, accuracy=94.6% |
| rebuttal_draft W-C4 | LOEO 3-fold 结果 | LOCO-CV K=12 结果 |
| rebuttal_draft Q5 | LOEO complete | LOCO-CV complete |
| rebuttal_notes Q2 | n=10/n=16, AUROC=0.969 | LOCO-CV K=12, n=56, AUROC=0.988±0.003 |

**2. Onset 统计更新（Walker 5/5→8/8, 总计 7/7→10/10）**

| 位置 | 修改前 | 修改后 |
|------|--------|--------|
| Q1 Evidence | 2/2 original + s3/s4/s5 | 8/8 Walker + 2/2 Cheetah = 10/10 |
| Q7 Response | 2/2 original + 3 additional s3–s5 | 10/10 locomotion (8/8 Walker + 2/2 Cheetah) |
| Q7 Evidence | trained CIVO 2/2 original + 3 additional | 10/10 locomotion |
| Q8 Anticipated Q | 5/5 Walker | 10/10 locomotion |
| Q8 Response | 5/5 Walker, 0/5 frozen, 6/7 (86%) | 10/10 locomotion, 0/8 control |
| Q8 Evidence | 5/5 onset (NVE 1.53–4.72×) | 8/8 Walker (6 seeds, NVE 1.53–6.57×) + 2/2 Cheetah |
| Q10 Evidence | 5/5 onset | 8/8 onset (6 unique seeds) + 2/2 Cheetah |
| Q14 Anticipated Q | 7/7, p=0.003 | 10/10, p<0.0001 |
| Q14 Response | 7/7, 0/5, p=0.003 | 10/10, 0/8, p<0.0001 |
| Q14 Evidence | 5/5 Walker + 2/2 Cheetah, p=0.003 | 8/8 Walker + 2/2 Cheetah, p<0.0001 |
| rebuttal_notes Q4 | 6 seeds, 4 Walker + 2 Cheetah, 5/6 | 8/8 Walker + 2/2 Cheetah = 10/10 |

**3. Fisher exact p 值更新**
- 所有 `p=0.003` → `p<0.0001`（基于 trained 10/10 vs control 0/8）

**4. 新增 Cheetah exp_078 数据**
- Q1/Q8/Q10/Q14 Evidence 中加入 exp_078 (seed=0, NVE=4.10×, onset_self_correcting)
- Q8 加入 same-seed 因果控制（exp_068 vs exp_069）

**数据来源**: LOCO-CV 报告 (`artifacts/_project/report/loco_cv_results.md`)、memory.md onset 统计、agent_context

---
