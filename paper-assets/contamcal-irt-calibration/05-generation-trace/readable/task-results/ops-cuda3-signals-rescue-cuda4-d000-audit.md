# ops cuda3 signals rescue cuda4 d000 audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda3-signals-rescue-cuda4-d000-audit_20260515T190947_result.json`
- **Structured JSON:** [`e1813a339168d3deeb8a.json`](../../sessions/e1/e1813a339168d3deeb8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 排查报告

### cuda:3: signals — 无需干预

| 项目 | 详情 |
|------|------|
| **signals_v3 (PID 611720)** | 已死亡。v3 完成了 5/12 个任务后死亡（gsm8k+arc 的 d000/d005，arc 的 d025） |
| **signals_v4 (PID 617202)** | **已在运行**，13 分钟前启动。跳过 5 个已完成任务，正在处理 d000_s42/mmlu (1/7) |
| **Registry** | `exp_002_signals_3B_v4` 状态 RUNNING |
| **batch_size 修复** | 仍在，`s4_selfcritique.py` L120-125：`len(items)>5000` 时 bs=2 |
| **死因** | 日志无错误信息，进程被外部 kill（无 traceback/OOM） |

### cuda:4: d000 SFT — 无需干预

| 项目 | 详情 |
|------|------|
| **PID 597174** | 已死亡（旧 tmux shell） |
| **PID 597178→597179** | **活跃训练中**：`d000_a32_s42`，57% 完成（1775/3125 步），epoch 0.46，ETA ~1h35m |
| **命令** | `CUDA_VISIBLE_DEVICES=4`，lr=5e-5，alpha=32，data=sft_dosage_000.jsonl |
| **日志** | `exp_001_sft_3B_d000_v3.log`，loss 稳定 1.0-1.2，正常 |

### d000_s42 原始 vs 当前标准配置对比

| 参数 | 原始 d000_s42 | 当前 d000_a32_s42 (运行中) | 当前标准 |
|------|--------------|--------------------------|---------|
| lr | **2e-4** | 5e-5 | 5e-5 |
| lora_alpha | 32 | 32 | 32 |
| lora_r | 16 | 16 | 16 |
| 其他 | 相同 | 相同 | 相同 |

**结论**：原始 d000_s42 lr=2e-4 与当前标准 lr=5e-5 差 4 倍。重训有必要，且当前 d000_a32_s42 已在 cuda:4 正确执行。

### 最终 GPU 状态

| GPU | 进程 | 状态 | 预计完成 |
|-----|------|------|---------|
| cuda:3 | signals_v4 (PID 617202) | 运行中，6882 MiB / 60% util | 取决于 7 个 signal 任务 |
| cuda:4 | d000_a32_s42 (PID 597179) | 运行中，13868 MiB / 53% util，57% | ~1h35m |

**两个 GPU 均在正常工作，无需重提交或其他干预。** 但注意 d000_a32_s42 未在 registry 中注册——建议补注册以便追踪。

---
