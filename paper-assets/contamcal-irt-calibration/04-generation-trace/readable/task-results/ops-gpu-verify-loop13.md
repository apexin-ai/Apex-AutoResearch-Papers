# ops gpu verify loop13

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-verify-loop13_20260516T003831_result.json`
- **Structured JSON:** [`b803d18068881c3f565a.json`](../../sessions/b8/b803d18068881c3f565a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

| GPU | 显存 (MiB) | Util | PID | 任务 | 运行时间 |
|-----|-----------|------|-----|------|---------|
| **0** | **23260/24564** | **100%** | 643167 (14270) | SFT d005_s42_a32 — 74% (2352/3177) | 3h01m |
| **0** | ↑ | ↑ | 642763 (8976) | eval d100_s123_a32 batch — GSM8K 69% (915/1319) | 3h02m |
| 1 | 13341/24564 | 23% | 628668 (13332) | SFT d100_a32_s42_v3 | 4h27m |
| 2 | 7537/24564 | 59% | 652259 (7528) | signals d005_s123 (mmlu, all) | 1h34m |
| 3 | 8985/24564 | 70% | 655989 (8976) | eval d025_v3_s42_aligned (mmlu+gsm8k+arc) | 1h17m |
| 4 | 7183/24564 | 57% | 662616 (7174) | signals d100_a32_s123 (v8 recovery, mmlu) | 22m |
| 5 | 7531/24564 | 61% | 663067 (7522) | signals d025_v3_s42 (s4 only, mmlu) | 21m |

---

### 1. cuda:0 冲突：**确认真实 GPU 冲突**

两个进程同时占用 GPU 0，合计 14270 + 8976 = 23246 MiB（94.7% 显存），利用率 100%。两个任务的 wrapper 命令都显式设置了 `CUDA_VISIBLE_DEVICES=0`。

- **SFT d005_s42**: step 2352/3177 (74%), epoch 0.62, ~4.5s/step → 预计还需 ~62 min
- **eval d100_s123**: GSM8K 69% (915/1319), ~10.5s/it → GSM8K 部分还需 ~70 min；eval_results/aligned 目录存在但为空（尚未写出结果）。启动时因 HF 连接超时浪费了大量时间

两个任务都因显存争抢显著变慢。

### 2. d000_s42 SFT (PID 633036)：**已成功完成**

- Checkpoint: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/`
- **lora_alpha = 32** ✓
- EXIT_CODE=0, epoch 1.0, train_loss=1.1324, runtime=12647s (~3.5h)
- adapter_model.safetensors: 119 MB

### 3. cuda:4 recovery (PID 662616)：正常运行

- CUDA_VISIBLE_DEVICES=4 ✓
- compute_signals d100_a32_s123, benchmark mmlu, signal=all
- 已产出: signal_s1_embedding_mmlu.json (7.8 MB), signal_s2_minkpp_mmlu.json (2.9 MB)
- 运行 22 min，仍在计算后续 signals

### 4. sim_sweep_v7（本地 CPU）

14 个 JSON 文件已生成（12 个 result config + incremental_analysis.json + sweep_summary.json）。

---
