# ssh anon repo dryrun westb1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_anon_repo_dryrun_westb1_20260523T135215_result.json`
- **Structured JSON:** [`41dbc066163a73af5a9e.json`](../../sessions/41/41dbc066163a73af5a9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 验证结果

| 项目 | 结果 |
|------|------|
| Clone | **OK** |
| 文件数 | 56（不含 .git） |
| README | 存在，内容合理 |
| requirements.txt | 存在 |
| 语法检查 | **OK** |
| prune.py --help | **OK** |
| eval_gsm8k.py --help | **OK** |
| 匿名化 | **泄露** |

### 匿名化泄露详情

服务器名泄露（7 处）：

| 文件 | 行号 | 泄露内容 |
|------|------|----------|
| `figures/paper/gen_fig2_reward_trajectories.py` | 49 | `westd-11672` |
| `scripts/run_alpha_verify_512.sh` | 2 | `westb` |
| `src/bootstrap_ci_accuracy.py` | 17 | `westb-23072` |
| `src/bootstrap_ci_accuracy.py` | 114 | `westd-29022` |
| `src/bootstrap_ci_accuracy.py` | 119 | `westd`（文件名） |
| `src/bootstrap_ci_accuracy.py` | 128 | `westb-23072` |
| `src/bootstrap_ci_accuracy.py` | 134 | `westb` |

需要将这些服务器名注释/字符串清除或替换为 `server-A` / `server-B` 等匿名标识，然后重新 push。

---
