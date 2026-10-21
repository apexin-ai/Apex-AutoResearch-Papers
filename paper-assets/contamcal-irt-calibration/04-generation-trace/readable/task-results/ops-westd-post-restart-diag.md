# ops westd post restart diag

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-post-restart-diag_20260520T030515_result.json`
- **Structured JSON:** [`2afc52645acb0eb2a7b6.json`](../../sessions/2a/2afc52645acb0eb2a7b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息齐全。

---

```
westd-29999 GPU 状态 (4x RTX PRO 6000 Blackwell ~98GB):
  cuda:0 — 空闲 (0 MiB)
  cuda:1 — 占用 Qwen2.5-14B d100_s123 retrain (PID 246779, 62.3GB, 87%)
  cuda:2 — 占用 OLMo-2-7B s0 sweep (PID 261133, 66.9GB, 85%)
  cuda:3 — 占用 Gemma-2-9B d100_s123 retrain (PID 246861, 94.9GB, 84%)

磁盘: root 5% / data 77%

实验诊断:
  gsm8k_phi4_s123_westd:         ✅ 完成 (d000=84.31%, d100=83.85%)
    - 5 dosage checkpoint 全部完整 (865M each)
    - GSM8K eval 结果已产出，含 .done 标记
    - phi4 s123 SFT sweep 于 09:10 完成，EXIT_CODE=0

  sft_qwen14b_d100_s123_retrain: 🔄 运行中 cuda:1
    - 进度: 1409/4159 (~34%), epoch 0.21
    - 09:55 重启后重新提交，ETA ~13:25
    - d000-d050 s123 checkpoint 完好 (1.1G each, safetensors ✅)

  sft_gemma2_d100_s123_retrain:  🔄 运行中 cuda:3
    - 进度: 1447/4159 (~35%), epoch 0.21
    - 09:55 重启后重新提交，ETA ~13:10
    - d000-d050 s123 checkpoint 完好 (891M each, safetensors ✅)

  sft_olmo2_s0_sweep:            🔄 运行中 cuda:2
    - d000_s0 已完成 (625M, safetensors ✅)
    - 当前训练 d005_s0 或更后 dosage
    - 完成 1/5 dosage，预计还需数小时

需要重跑的任务: 无
  - phi4 已在重启前完成
  - 其余 3 个实验已被自动重新提交，正常推进中

空闲 GPU: cuda:0
```

---
