# deploy bjb2 28827 tau sweep d132

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-tau-sweep-d132_20260523T130545_result.json`
- **Structured JSON:** [`d783ad267752b01b1b35.json`](../../sessions/d7/d783ad267752b01b1b35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部部署成功。汇总：

| exp_id | GPU | τ | tmux session | 状态 |
|--------|-----|-----|--------------|------|
| `eval-ablation-tau010-goal-s42` | cuda:0 | 0.10 | `eval-ablation-tau010-goal-s42` | RUNNING |
| `eval-ablation-tau015-goal-s42` | cuda:1 | 0.15 | `eval-ablation-tau015-goal-s42` | RUNNING |
| `eval-ablation-tau040-goal-s42` | cuda:2 | 0.40 | `eval-ablation-tau040-goal-s42` | RUNNING |

- 服务器：bjb2-28827
- 日志：`logs/eval-ablation-tau{010,015,040}-goal-s42.log`
- 3 个进程均已开始加载 SmolVLA 模型，正常运行中
- CRM checkpoint: `crm_smolvla_3suite_v1/crm_best.pt`
- 配置与 `eval-supp-goal-adapt-tau025-s42` 一致，仅 `--conformal_threshold` 不同

---
