# diagnose gpu status session resume

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_status_session_resume_20260522T095316_result.json`
- **Structured JSON:** [`4c9a69b928164dd3910c.json`](../../sessions/4c/4c9a69b928164dd3910c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断汇总

### GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | 82% | 15.3 / 95.6 GB |
| cuda:1 | 82% | 14.8 / 95.6 GB |

两块 GPU 都在满负荷运行。

### openvla_spatial 进程 — **全部存活**
| PID | 运行时间 | 任务 |
|-----|----------|------|
| 645141 | 47 min | `trained --only-counterfactual` (cuda:0) |
| 646058 | 39 min | `untrained` (cuda:1) |

**日志进度：**
- **cuda:0 (trained CF)**: 正在跑 `empty` condition，进度 4200/5000。之前 `wrong` condition 已完成（d=0.8849, cross-task mean=0.9146）。
- **cuda:1 (untrained)**: 也在跑 `empty` condition，进度 400/5000。之前 `wrong` condition 已完成（d=0.7944, cross-task mean=0.8005）。

两个进程都在稳步推进，每 200 samples 约 50-55 秒。

### NLP control 进程 — **全部存活但有问题**
| PID | 运行时间 | 任务 |
|-----|----------|------|
| 612753 | 4h 21m | `download_llama.py` |
| 613202 | 4h 19m | `wait_and_run.sh` |

**但 Llama-2-7b-chat-hf 模型目录不存在。** 下载进程跑了 4 小时却没产出文件，大概率卡死或下载失败。

### 结果目录 — **均不存在**
`openvla_spatial_trained/` 和 `openvla_spatial_untrained/` 结果目录都还没创建，说明两个 pipeline 尚未完成任何 condition 的完整结果写入（结果可能在内存中或最后统一写出）。

### 结论
1. **openvla_spatial 双卡实验正常运行中**，都在 `empty` condition 阶段，预计还需 ~20-30 分钟完成当前 condition。
2. **NLP Llama 下载大概率失败** — 4 小时无产出，需要排查 download_llama.py 日志。

---
