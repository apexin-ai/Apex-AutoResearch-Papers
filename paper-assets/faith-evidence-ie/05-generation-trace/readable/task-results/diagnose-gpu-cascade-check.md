# diagnose gpu cascade check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu-cascade-check_20260521T233752_result.json`
- **Structured JSON:** [`43b1f7ed0e8da1d43c0e.json`](../../sessions/43/43b1f7ed0e8da1d43c0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 诊断结果

### 当前 GPU 占用
| GPU | 显存占用 | PID | 实验 |
|-----|---------|-----|------|
| 0 | 6,071 / 97,887 MiB (6%) | 140534 | test_eval_1_7b_sft_s42 |
| 1 | 32,503 / 97,887 MiB (33%) | 125323 | test_eval_14b_sft_s42 |
| 2 | 94,453 / 97,887 MiB (97%) | 142872 | retrain_4b_rsft_ced_s42_v2 |
| 3 | 32,503 / 97,887 MiB (33%) | 143166 | test_eval_14b_sft_s42_no_evi |

### 实验状态

| 状态 | 实验 | GPU | 进度 | 备注 |
|------|------|-----|------|------|
| [RUNNING] | retrain_4b_rsft_ced_s42_v2 | cuda:2 | step 300/510 (59%), epoch ~1.76/3 | last_loss≈0.605, uptime 23:50 |
| [RUNNING] | test_eval_14b_sft_s42 | cuda:1 | 448/500 (90%) | ~35s/it, ETA ~30min, uptime 5h05m |
| [RUNNING] | test_eval_1_7b_sft_s42 | cuda:0 | 115/500 (23%) | ~27s/it, ETA ~2.9h, uptime 48min |
| [RUNNING] | test_eval_14b_sft_s42_no_evi | cuda:3 | 37/500 (7%) | ~40-50s/it, ETA ~5.5h, uptime 23min |

### Cascade 就绪度

- **retrain checkpoint**: ❌ 训练中 (300/510 steps), 预计再 ~15min 完成。最新 checkpoint: `/root/autodl-tmp/rsft_output_ced_s42_v2/checkpoint-300/adapter_model.safetensors` (504MB)
- **1.7B SFT adapter**: ✅ `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16/adapter_model.safetensors` (267MB, 2026-05-16)
- **空闲 GPU**: 无 — 全部 4 卡被占用

### 预计完成时间线
1. **test_eval_14b_sft_s42** (cuda:1) — 约 30 分钟后完成
2. **retrain_4b_rsft_ced_s42_v2** (cuda:2) — 约 15-20 分钟后完成 (210 steps remaining)
3. **test_eval_1_7b_sft_s42** (cuda:0) — 约 2.9 小时后
4. **test_eval_14b_sft_s42_no_evi** (cuda:3) — 约 5.5 小时后

---
