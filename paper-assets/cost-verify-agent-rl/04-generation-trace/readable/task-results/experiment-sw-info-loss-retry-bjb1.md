# experiment sw info loss retry bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_sw-info-loss-retry-bjb1_20260520T162931_result.json`
- **Structured JSON:** [`3e973e242c97430c7702.json`](../../sessions/3e/3e973e242c97430c7702.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job 正常运行中。vLLM TP=2 初始化完成，模型加载成功（1.12s）。

**同步和提交完成，汇总：**

| 项目 | 状态 |
|------|------|
| env.py JVM 加固同步 | MD5 一致 `4b0f79f` |
| eval 脚本同步 | MD5 一致 `bdd8ce4`，373 行 |
| Checkpoint | `/root/autodl-tmp/checkpoints/scienceworld_sft/huggingface/` |
| GPU | cuda:0,1 RTX PRO 6000 96GB x2 |
| Job PID | 229078 |
| tmux session | `sw_info_loss_bjb1` |
| Log | `~/runs/cost-verify-agent-rl/sw_info_loss_bjb1.log` |
| Registry | `sw_info_loss_bjb1` → RUNNING, parent=scienceworld_sft_eval_v2 |

两个条件串行运行：先 full context (h=-1, T=0)，完成后自动跑 h=2 (T=0)，各 3 variations/task type。输出分别写 `eval_results_full_T0.json` 和 `eval_results_h2_T0.json`。

---
