# deploy adaptive seed extension batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_adaptive-seed-extension-batch_20260524T153425_result.json`
- **Structured JSON:** [`6de095574b82808eae8f.json`](../../sessions/6d/6de095574b82808eae8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

12 个作业全部成功部署运行。

**bjb2-28827** (Adaptive CRM τ=0.25)：
| exp_id | GPU | PID |
|---|---|---|
| eval-supp-adapt-tau025-spatial-s48 | cuda:0 | 299935 |
| eval-supp-adapt-tau025-spatial-s49 | cuda:1 | 300212 |
| eval-supp-adapt-tau025-goal-s48 | cuda:2 | 300823 |
| eval-supp-adapt-tau025-goal-s49 | cuda:3 | 301553 |
| eval-supp-adapt-tau025-obj-s48 | cuda:4 | 302994 |
| eval-supp-adapt-tau025-obj-s49 | cuda:5 | 304327 |

**cqa1-32758** (VLA-only)：
| exp_id | GPU | PID |
|---|---|---|
| eval-supp-vla-only-spatial-s48 | cuda:0 | 940684 |
| eval-supp-vla-only-spatial-s49 | cuda:1 | 940972 |
| eval-supp-vla-only-goal-s48 | cuda:2 | 941247 |
| eval-supp-vla-only-goal-s49 | cuda:3 | 941522 |
| eval-supp-vla-only-obj-s48 | cuda:4 | 942179 |
| eval-supp-vla-only-obj-s49 | cuda:5 | 942933 |

**异常**：cqa1-32758 首次提交全部 EXIT_CODE=127（`python: command not found`，PATH 未包含 conda）。已 kill 失效 tmux 会话，加上 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` 重新提交，已确认进程占用 GPU 且 spatial-s48 已加载 LIBERO 环境。timeout 6h。

---
