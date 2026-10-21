# fix standard mbpp exit watchdog clean resubmit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_standard_mbpp_exit_watchdog_clean_resubmit_20260519T211830_result.json`
- **Structured JSON:** [`95ff68928dced9d58a0a.json`](../../sessions/95/95ff68928dced9d58a0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**排查结果**：
- **无 watchdog 进程、无 crontab** — 不存在主动杀进程的监控机制
- Exit 文件是 submit_training_job 框架的**退出记录**（被动记录，非主动杀手）
- 进程被杀的真正原因：框架的 **timeout wrapper**（exit 124）和 **SIGHUP**（exit 129，tmux session 被杀时触发）

**Exit 文件证据**：
| 文件 | Exit Code | 含义 |
|------|-----------|------|
| `eval_mbpp_sft_standard_20.exit` | 143 | SIGTERM |
| `eval_mbpp_grpo_standard_20.exit` | 124 | timeout |
| `eval_mbpp_grpo_standard_20_v2.exit` | 129 | SIGHUP |
| `eval_mbpp_grpo_rasp_20.exit` | 129 | SIGHUP |

**已清理**：3 个 standard 相关 exit 文件 + 死掉的 `eval_mbpp_sft_standard_20_v3` session

**当前运行状态**（3 个实验全部存活）：
| 实验 | Session | PID | GPU | 状态 |
|------|---------|-----|-----|------|
| SFT Standard | `mbpp_sft_std_clean` | 141113 | cuda:0 | 加载中 |
| GRPO Standard v4 | `eval_mbpp_grpo_standard_20_v4` | 139816 | cuda:2 | 运行中 |
| GRPO RASP | `eval_mbpp_grpo_rasp_20` | 127964 | cuda:1 | 运行中 (~2.8h) |

**Registry 更新**：
- `eval_mbpp_sft_standard_20_v3` → DONE/failed
- `eval_mbpp_sft_standard_20_clean` → RUNNING (parent=v3, PID 141113)
- `eval_mbpp_grpo_standard_20_v4` → 保持 RUNNING（进程存活）
- 每 8 分钟自动监控三个实验

---
