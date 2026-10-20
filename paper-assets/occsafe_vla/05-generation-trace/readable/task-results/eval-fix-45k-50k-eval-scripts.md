# eval fix 45K 50K eval scripts

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_fix-45K-50K-eval-scripts_20260521T124350_result.json`
- **Structured JSON:** [`494913bd6cd9d6037204.json`](../../sessions/49/494913bd6cd9d6037204.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

45K eval 正常推进中，Task 0 已到 75% (15/20 rollouts)。10 个 task × 20 rollouts，每个 ~4s，预计总耗时约 15 分钟。

### 汇总

| 项目 | 状态 |
|------|------|
| **正确 eval 脚本路径** | `vla-scripts/evaluate_safelibero.py` |
| **45K eval** | PID 415706, cuda:0, 日志 `/root/occsafe_vla/eval_results/occ_s1_45000.log` |
| **50K auto-eval (修复版)** | PID 418059, cuda:2, 等待 50K checkpoint 出现后自动启动，日志 `/root/eval_logs/auto_eval_50K_fixed_wrapper.log` |
| **旧 50K 脚本 bug** | 已杀掉 (PID 389317)，两个 bug：① 缺 `vla-scripts/` 前缀 ② `--pretrained_checkpoint` 后无值 |

---
