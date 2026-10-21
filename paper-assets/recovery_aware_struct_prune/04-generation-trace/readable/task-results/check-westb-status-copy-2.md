# check westb status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westb_status_20260517T110521_result.json`
- **Structured JSON:** [`c13f3eea2cc91239ff62.json`](../../sessions/c1/c13f3eea2cc91239ff62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072 服务器状态汇总

### GPU 使用情况
| GPU | 状态 | 显存 | GPU-Util | 温度 |
|-----|------|------|----------|------|
| cuda:0 | **占用** — PID 704557 (random SFT recovery) | 50411 / 97887 MiB | 97% | 61°C |
| cuda:1 | **空闲** | 0 MiB | 0% | 34°C |

### PID 696141 (random eval)
**已结束**。PID 不存在。当前 cuda:0 上运行的是新进程 PID 704557（SFT recovery）。

### Random Eval 结果 (post-prune, 无 SFT)
- **Accuracy: 34.0% ± 3.35%** (68/200)
- EOS rate: 45.5%, 平均 response 长度 2634 tokens
- 结果文件: `eval_postprune_random_20.json` (18:57 完成)

### Tmux Sessions
| Session | 创建时间 | 状态 |
|---------|----------|------|
| `scoring_ablation_random` | 16:54 | **运行中** — SFT recovery 进行中，261/1870 steps (14%)，~1.08s/it，预计还需约 29 分钟 |
| `scoring_ablation_v2` | 15:37 | **已完成** — gradient SFT recovery 于 18:02 完成，模型保存至 `sft_gradient_20` |

### results/ 目录最新文件（今日）
| 文件 | 时间 | 说明 |
|------|------|------|
| `random_cka_ablation_log.txt` | 19:05 | random ablation 运行日志（持续写入） |
| `eval_postprune_random_20.json` | 18:57 | random 剪枝 post-prune eval: **34.0%** |
| `eval_gradient_postsft.json` | 18:23 | gradient SFT 后 eval |
| `eval_gradient_sft.log` | 18:14 | gradient SFT eval 日志 |
| `ablation_log.txt` | 17:07 | ablation 日志 |
| `eval_unstructured_20_n1319.json` | 16:48 | 非结构化剪枝 eval |
| `eval_postprune_gradient_20.json` | 16:48 | gradient 剪枝 post-prune eval |

---
