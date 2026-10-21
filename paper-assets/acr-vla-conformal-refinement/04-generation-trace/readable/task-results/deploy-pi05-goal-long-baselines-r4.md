# deploy pi05 goal long baselines r4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-goal-long-baselines-r4_20260522T151725_result.json`
- **Structured JSON:** [`988fc2be4ca656170e1e.json`](../../sessions/98/988fc2be4ca656170e1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 eval 全部正常启动，正在加载 PI05 模型。

## 汇总

### Kill 旧进程
| 服务器 | PID | 状态 |
|--------|-----|------|
| bjb1-32546 | 326387 (旧 CRM cuda:4) | ✅ KILLED |
| bjb2-40593 | 23742 (卡住 OFT eval) | ✅ KILLED |

### π0.5 Baseline Eval 部署

| 实验 ID | 服务器 | GPU | PID | tmux session |
|---------|--------|-----|-----|-------------|
| eval-pi05-vla-only-goal-seed43-r4 | bjb1-32546 | cuda:4 | 447209 | eval-pi05-vla-only-goal-seed43-r4 |
| eval-pi05-vla-only-goal-seed44-r4 | bjb1-32546 | cuda:5 | 447496 | eval-pi05-vla-only-goal-seed44-r4 |
| eval-pi05-vla-only-long-seed43-r4 | bjb1-18228 | cuda:1 | 25428 | eval-pi05-vla-only-long-seed43-r4 |
| eval-pi05-vla-only-long-seed44-r4 | bjb1-18228 | cuda:2 | 25703 | eval-pi05-vla-only-long-seed44-r4 |

注意：用户命令缺少 `--model pi05`，已自动补上。vla_only 模式下 K=1 (baseline_mode=single)，n_action_steps=10。

---
