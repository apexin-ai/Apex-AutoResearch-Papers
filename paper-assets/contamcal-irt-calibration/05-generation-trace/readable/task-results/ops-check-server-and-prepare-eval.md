# ops check server and prepare eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-server-and-prepare-eval_20260515T182203_result.json`
- **Structured JSON:** [`9451c0ae157e27f1828a.json`](../../sessions/94/9451c0ae157e27f1828a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

### GPU 使用情况

| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| 0 | 17975/24564 MiB | 32% | d100 s123 a32 v2 SFT |
| 1 | 13341/24564 MiB | 27% | d100 s42 a32 v2 SFT |
| 2 | 13583/24564 MiB | 64% | (未确认) |
| 3 | 16552/24564 MiB | 98% | d100 s123 para_aligned eval |
| 4 | 21880/24564 MiB | 99% | d000 v3 SFT |
| 5 | 17651/24564 MiB | 76% | d025 v3 s42 SFT (PID 589763) |

### RUNNING 任务进度

| 任务 | GPU | 进度 | ETA |
|------|-----|------|-----|
| d100 s42 a32 v2 SFT | cuda:1 | 1596/4159 (38%) | ~3h |
| d100 s123 a32 v2 SFT | cuda:0 | 1549/4159 (37%) | ~3h |
| d000 v3 SFT | cuda:4 | 1124/3125 (36%) | ~2h 41m |
| d025 v3 s42 SFT | cuda:5 | 1835/3384 (54%) | ~1h 47m |
| **d100 s123 para_aligned eval** | **cuda:3** | **MMLU para 83% (5500/6596)** | **~1 min** |

### d005 s42 checkpoint
存在，完整。`adapter_model.safetensors` 114MB，修改时间 May 14 20:55。

### Paraphrases 目录
4 个文件齐全：arc_challenge, gsm8k, humaneval, mmlu。

### Registry
`exp_001_eval_3B_d005_s42_para_aligned` 已创建，status=PREPARING，hypothesis 已设置。

**关键发现**：cuda:3 上的 d100_s123_para_aligned eval 即将完成（MMLU paraphrased 83%，约 1 分钟内结束），之后 cuda:3 将释放，可以提交 d005 s42 para_aligned eval。

---
