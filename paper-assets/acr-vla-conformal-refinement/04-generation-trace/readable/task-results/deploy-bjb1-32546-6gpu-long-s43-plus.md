# deploy bjb1 32546 6gpu long s43 plus

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-6gpu-long-s43-plus_20260523T143533_result.json`
- **Structured JSON:** [`cd292dfcd2e8963e5a02.json`](../../sessions/cd/cd292dfcd2e8963e5a02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个实验全部部署完毕，registry 已更新到 RUNNING。

| GPU | exp_id | PID | 状态 |
|-----|--------|-----|------|
| cuda:0 | eval-supp-goal-vla-only-wrapper-s44-r2 | 990832 | RUNNING |
| cuda:1 | eval-supp-long-adapt-tau025-s43 | 991960 | RUNNING |
| cuda:2 | eval-supp-long-crm-norm005-s43 | 993249 | RUNNING |
| cuda:3 | eval-supp-long-reconvla-s43 | 994675 | RUNNING |
| cuda:4 | eval-supp-long-k2mean-s43 | 996158 | RUNNING |
| cuda:5 | eval-supp-long-vla-only-s44 | 997776 | RUNNING |

注意：`evaluate.py` 实际路径是 `src/evaluate.py`（非项目根目录），已自动修正。旧的冲突 JSON `eval_goal_vla_only_seed44.json` 已删除。日志在 `/tmp/eval_*.log`。

---
