# diag server state loop17

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_server-state-loop17_20260516T175042_result.json`
- **Structured JSON:** [`9678a307a870b18c5894.json`](../../sessions/96/9678a307a870b18c5894.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. GPU 状态

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 0 MiB | 0% | **空闲** |
| 1 | 6913 MiB | 79% | PID 807025 — Llama d000 eval (gsm8k/arc/humaneval) |
| 2 | 3 MiB | 0% | **空闲** |
| 3 | 8313 MiB | 0% | PID 822390 — Llama d025 eval (mmlu/gsm8k/arc/humaneval)，刚启动 18 分钟 |
| 4 | 4251 MiB | 45% | PID 810809 — 1.5B-Instruct MMLU signals |
| 5 | 20589 MiB | 98% | PID 804791 — Llama d100 SFT 训练 |

### 2. 进程状态

| PID | 状态 | 运行时间 | 说明 |
|-----|------|---------|------|
| 818742 | **存活** | 47m22s | exp_006 N=24 v3 Stan IRT（CPU），4 chains warmup 中，~45% |
| 804565 | **死亡** | — | Llama d005 SFT 已结束 |
| 804786 | **存活** | 2h19m | Llama d100 SFT 的 bash wrapper（实际训练子进程 PID 804791） |
| 807025 | **存活** | 2h17m | Llama d000 eval，cuda:1 |
| 810809 | **存活** | 2h01m | 1.5B-Instruct MMLU signals，cuda:4 |

### 3. d025 SFT 完成验证

**已完成，checkpoint 完整。** 训练日志 EXIT_CODE=0，epoch=1.0，train_loss=1.526。merged 目录包含完整模型文件（2 个 safetensors 分片，共 ~6GB + tokenizer + config）。PID 822390 已在 cuda:3 上启动 d025 的 eval。

### 4. gsm8k signals 失败诊断

输出目录 `/root/autodl-tmp/exp002/signals_15B_instruct_gsm8k/` **不存在**，日志文件也不存在。这个任务可能**从未成功提交**，或者任务名/路径与预期不符。

### 5. exp_006 N=24 v3 状态

**运行中。** PID 818742 存活，Stan MCMC 4 chains 正在 warmup 阶段（~45%，约 900/2000 iterations）。输出目录 `results_mmlu_domain_gamma_n24_v3/` 已有 4 个 domain 子目录的中间结果（Medical, STEM_CS_Eng, STEM_Math, STEM_Science）。预计 warmup 还需 ~10 分钟，之后进入 sampling。

### 总结

- **空闲 GPU**: 0, 2（d005 SFT 已完成释放了 GPU 0）
- **804565 (d005 SFT) 已死**——需确认其 checkpoint 是否完整、是否需要启动 d005 eval
- **gsm8k signals 任务不存在**——需确认是否曾提交过，或路径/命名是否有误

---
