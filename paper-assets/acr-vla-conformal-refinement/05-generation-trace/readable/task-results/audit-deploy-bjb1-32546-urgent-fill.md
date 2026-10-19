# audit deploy bjb1 32546 urgent fill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit-deploy_bjb1-32546-urgent-fill_20260523T112837_result.json`
- **Structured JSON:** [`bdb9c573ae37a0ff770c.json`](../../sessions/bd/bdb9c573ae37a0ff770c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

P0 实验已在 cuda:0 和 cuda:1 上运行。

## 审计汇报

### 完成的实验结果（已更新 registry → DONE）

| GPU | 实验 | Success Rate | Conclusion |
|-----|------|-------------|-----------|
| cuda:0 | Object Adaptive tau=0.25 s43 | **77.5%** | negative (baseline ~80%) |
| cuda:1 | Goal CRM norm=0.05 s43 | **82.0%** | negative (baseline 83.5%, s42=85.5%) |
| cuda:2 | Goal Adaptive tau=0.25 s43 | **84.5%** | success (+1.0pp, consistent with s42=84.0%) |
| cuda:4 | Object CRM norm=0.05 s43 | **78.5%** | negative (baseline ~80%) |
| cuda:5 | Goal Adaptive tau=0.25 s44 | **86.5%** | success (+3.0pp, 3-seed mean=85.0%) |

### 当前 GPU 状态

| GPU | 状态 | 实验 |
|-----|------|------|
| cuda:0 | **RUNNING** | eval-supp-goal-vla-only-wrapper-s43 (P0, PID 905856) |
| cuda:1 | **RUNNING** | eval-supp-goal-vla-only-wrapper-s44 (P0, PID 906142) |
| cuda:2 | **空闲** | — |
| cuda:3 | **RUNNING** | eval-supp-long-vla-only-s42 (PID 848576, 继续运行中) |
| cuda:4 | **空闲** | — |
| cuda:5 | **空闲** | — |

### 待决

**3 个 GPU 空闲（cuda:2, cuda:4, cuda:5）**。P1 实验全部已完成（非 crash），无需重跑。需要 Director 指定新实验填满这 3 张空卡。

---
