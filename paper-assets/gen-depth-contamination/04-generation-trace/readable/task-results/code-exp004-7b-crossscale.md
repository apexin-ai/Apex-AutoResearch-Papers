# code exp004 7b crossscale

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp004_7b_crossscale_20260515T104846_result.json`
- **Structured JSON:** [`50907b972eee800d7f2e.json`](../../sessions/50/50907b972eee800d7f2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动并正常运行：

- **GPU**: 19000 MiB / 24564 MiB，100% 利用率，无 OOM
- **Generation 速度**: ~9.6s/batch (bs=4)，depth 1 预估 ~3.3h，全部 5 depths ~16.5h
- **Feature extraction**: ~2h（用 1.5B scorer）
- **总预估**: ~19h，预计明天下午完成

关键配置确认：
| 参数 | 值 |
|------|-----|
| Generator | Qwen2.5-7B (base, fp16, 14.5GB) |
| Scorer | Qwen2.5-1.5B-Instruct |
| n_docs | 5000 |
| max_depth | 5 |
| batch_size | 4 (gen) / 8 (feat) |
| mode | continuation |
| tmux session | exp004 |
| 日志 | `/root/autodl-tmp/gen-depth-contamination/exp004_run.log` |

监控命令：
- `tail -5 exp004_run.log` — 查看进度
- `nvidia-smi` — 查看 GPU 状态
- `tmux attach -t exp004` — 进入 session

---
