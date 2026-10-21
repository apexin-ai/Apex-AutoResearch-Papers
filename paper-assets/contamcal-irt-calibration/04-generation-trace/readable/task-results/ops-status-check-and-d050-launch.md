# ops status check and d050 launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-check-and-d050-launch_20260521T034519_result.json`
- **Structured JSON:** [`3a61be23f25c132d7ba7.json`](../../sessions/3a/3a61be23f25c132d7ba7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU 状态

**westd-29999 (4× H800 97GB)**

| GPU | VRAM | Util | 任务 |
|-----|------|------|------|
| 0 | 32.7/97.9 GB | 95% | MMLU eval (d000 **已完成**, 进程可能已退出) |
| 1 | 42.9/97.9 GB | 63% | **d050 retrain** — 2581/3642 (71%), ~1.5h 剩余 |
| 2 | 32.7/97.9 GB | 94% | MMLU eval (d005 **已完成**) |
| 3 | 32.7/97.9 GB | 95% | MMLU eval (d025 — 76%, ~5min 剩余) |

**cqa1-21977 (1× GPU)**

| GPU | VRAM | Util | 任务 |
|-----|------|------|------|
| 0 | 17.1 GB | 90% | GSM8K eval — 242/330 (73%), ~12min ETA |

---

### MMLU Qwen-14B 结果：s0 vs s123

| Dosage | s123 | s0 | Δ(s0−s123) |
|--------|------|----|-----------|
| d000 | 68.67% | **68.84%** | +0.17pp |
| d005 | 70.84% | **68.86%** | **−1.98pp** |
| d025 | 63.68% | *running* | — |
| d050 | 60.99% | *training* | — |
| d100 | 55.93% | *not started* | — |

**关键发现**: d005 s0 (68.86%) 没有出现 s123 的 +2.17pp boost，几乎等于 d000 baseline。s123 的 d005 boost 很可能是 seed-specific artifact。

---

### d050 Retrain

- PID 455006, epoch 0.65, loss ~0.92, token_accuracy ~0.77
- lora_alpha=32, lr=5e-5, gradient_checkpointing
- **ETA ~1.5h** (~5s/step × 1061 steps remaining)
- 训练正常推进

### d050 Eval 准备

两个脚本都存在且包含 C006/C009 校验：
- `scripts/seed0/eval_qwen14b_d050_s0_mmlu.sh` — `CUDA_VISIBLE_DEVICES=1`
- `scripts/seed0/eval_qwen14b_d050_s0_arc.sh` — `CUDA_VISIBLE_DEVICES=1`（需改为其他 GPU 以并行）

**输出目录**: MMLU → `results/qwen14b_d050_s0_mmlu/`, ARC → `results/qwen14b_d050_s0_arc/`

⚠️ **d050 eval 无法现在启动** — 训练还需 ~1.5h。训练完成后 GPU 0/2/3（d025 eval 也将完成）和 GPU 1 都将释放，可同时跑 MMLU + ARC。

### Registry 更新

- `eval_qwen14b_mmlu_d000_s0` → **DONE/success**, accuracy=68.84%
- `eval_qwen14b_mmlu_d005_s0` → **DONE/success**, accuracy=68.86%
- `eval_qwen14b_mmlu_d025_s0` → RUNNING（~5min 完成）
- `retrain_qwen14b_d050_s0` → RUNNING（~1.5h）
- `eval_qwen7b_gsm8k_s0_cqa1` → RUNNING（~12min）

---
