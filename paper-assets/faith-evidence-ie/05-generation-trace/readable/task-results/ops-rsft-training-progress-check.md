# ops rsft training progress check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rsft-training-progress-check_20260516T004733_result.json`
- **Structured JSON:** [`d7d2dd389f2eb524032d.json`](../../sessions/d7/d7d2dd389f2eb524032d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇总

### rsft_ced_s43_train_r3 (cuda:1)
| 项目 | 状态 |
|------|------|
| PID | 277310 (bash wrapper), 运行 26:37 |
| 进度 | **170/510 steps (33.3%)** — epoch 1 结束，正在跑 eval |
| 速度 | ~5.7-5.9 s/step |
| Checkpoints | checkpoint-50, checkpoint-100, checkpoint-150 |
| GPU 1 | 39% util, 28345/32607 MiB (87% VRAM) |
| 预估剩余 | 340 steps × ~5.8s ≈ **33 min** 训练 + epoch 2/3 末的 eval 时间，预计 ~09:15-09:20 UTC 完成 |
| 异常 | 无。有一条 `generation flags not valid` warning，无害 |

### rsft_ced_s45_train_r4 (cuda:2)
| 项目 | 状态 |
|------|------|
| PID | 279526 (bash wrapper) + **279531 (python, 124% CPU)**, 运行 13:14 |
| 进度 | **137/510 steps (26.9%)** — epoch 1 进行中 |
| 速度 | ~5.5-5.7 s/step |
| Checkpoints | checkpoint-50, checkpoint-100 |
| GPU 2 | **99% util, 31639/32607 MiB (97% VRAM)** |
| 预估剩余 | 373 steps × ~5.7s ≈ **35 min**，预计 ~09:20-09:25 UTC 完成 |
| 异常 | 无 |
| 日志路径 | 实际在 `/tmp/rsft_ced_s45_r4.log`（非 `~/runs/` 下） |

### PID 澄清
- **279526** = bash wrapper（nohup 启动的 shell）
- **279531** = 实际 python 训练进程（124% CPU，真正干活的）
- Registry 记录 279531 是正确的

### GPU 总览
| GPU | 利用率 | 显存 | 用途 |
|-----|--------|------|------|
| 0 | 52% | 10.6/31.8 GB | 其他任务 |
| 1 | 39% | 27.7/31.8 GB | s43 训练（正在 eval，util 偏低正常） |
| 2 | 99% | 30.9/31.8 GB | s45 训练 |
| 3 | 44% | 10.6/31.8 GB | 其他任务 |

两个任务都在正常训练，无 error。s43 比 s45 早启动约 13 分钟，进度领先。注意 s45 没有配置 `--eval_data_dir`，不会做 epoch 末 task eval，纯训练会稍快。两者预计均在 ~35 分钟内完成。

---
