# ops survey 05B 15B s123 signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_survey-05B-15B-s123-signals_20260516T010623_result.json`
- **Structured JSON:** [`777b1a74c0d780a73c12.json`](../../sessions/77/777b1a74c0d780a73c12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是结构化报告。

---

## Checkpoint 清单

| 模型 | dosage | seed | checkpoint 路径 | adapter 存在 | lora_alpha |
|------|--------|------|----------------|-------------|-----------|
| Qwen2.5-0.5B | d000 | s123 | `Qwen2.5-0.5B_d000_s123/lora_adapter` | YES (safetensors + config) | **32** |
| Qwen2.5-0.5B | d005 | s123 | `Qwen2.5-0.5B_d005_s123/lora_adapter` | YES | **32** |
| Qwen2.5-0.5B | d025 | s123 | `Qwen2.5-0.5B_d025_s123/lora_adapter` | YES | **32** |
| Qwen2.5-0.5B | d100 | s123 | `Qwen2.5-0.5B_d100_s123/lora_adapter` | YES | **32** |
| Qwen2.5-1.5B | d000 | s123 | `Qwen2.5-1.5B_d000_s123/lora_adapter` | YES | **32** |
| Qwen2.5-1.5B | d005 | s123 | `Qwen2.5-1.5B_d005_s123/lora_adapter` | YES | **32** |
| Qwen2.5-1.5B | d025 | s123 | `Qwen2.5-1.5B_d025_s123/lora_adapter` | YES | **32** |
| Qwen2.5-1.5B | d100 | s123 | `Qwen2.5-1.5B_d100_s123/lora_adapter` | YES | **32** |

所有路径基于 `/root/autodl-tmp/exp001/checkpoints/`。全部 lora_alpha=32，合规（非废弃 alpha=16）。

## 已有 Signal 覆盖

**s123: 完全为零。** `/root/autodl-tmp/exp002/signals/` 下无任何 `*s123*` 目录。

s42 参照（每个 checkpoint 的完整覆盖）：

| 模型_dosage_s42 | benchmark | embedding | minkpp | selfcritique | merged |
|-----------------|-----------|-----------|--------|-------------|--------|
| 0.5B_d000_s42 | mmlu/gsm8k/arc | YES | YES | YES | YES |
| 0.5B_d005_s42 | mmlu/gsm8k/arc | YES | YES | YES | YES |
| 0.5B_d025_s42 | mmlu/gsm8k/arc | YES | YES | YES | YES |
| 0.5B_d100_s42 | mmlu/gsm8k/arc | YES | YES | YES | YES |
| 1.5B_d000_s42 | mmlu/gsm8k/arc | YES | YES | YES | YES |
| 1.5B_d005_s42 | mmlu/gsm8k/arc | YES | YES | YES | YES |
| 1.5B_d025_s42 | mmlu/gsm8k/arc | YES | YES | YES | YES |
| 1.5B_d100_s42 | mmlu/gsm8k/arc | YES | YES | YES | YES |

## 缺失 Signal（需要补算）

**全部 8 个 s123 checkpoint × 3 benchmarks × 3 signals = 72 个 signal 文件 + 24 个 merged 文件**

| 模型_dosage_seed | mmlu | gsm8k | arc_challenge |
|------------------|------|-------|---------------|
| 0.5B_d000_s123 | embedding/minkpp/selfcritique | 同左 | 同左 |
| 0.5B_d005_s123 | embedding/minkpp/selfcritique | 同左 | 同左 |
| 0.5B_d025_s123 | embedding/minkpp/selfcritique | 同左 | 同左 |
| 0.5B_d100_s123 | embedding/minkpp/selfcritique | 同左 | 同左 |
| 1.5B_d000_s123 | embedding/minkpp/selfcritique | 同左 | 同左 |
| 1.5B_d005_s123 | embedding/minkpp/selfcritique | 同左 | 同左 |
| 1.5B_d025_s123 | embedding/minkpp/selfcritique | 同左 | 同左 |
| 1.5B_d100_s123 | embedding/minkpp/selfcritique | 同左 | 同左 |

## GPU 当前状态

| GPU | 显存使用 | 进程 PID | 备注 |
|-----|---------|---------|------|
| 0 | 23260/24564 MiB (95%) | 642763, 643167 | 几乎满载 |
| 1 | 13341/24564 MiB (54%) | 628668 | |
| 2 | 7537/24564 MiB (31%) | 652259 | |
| 3 | 8985/24564 MiB (37%) | 655989 | |
| 4 | 6929/24564 MiB (28%) | 668217 | |
| 5 | 7531/24564 MiB (31%) | 663067 | |

**所有 6 张 GPU 均有进程。** 0.5B signal 计算约需 ~2-4GB 显存，1.5B 约需 ~5-8GB。GPU 2/4/5 有空间可能共存，但需确认现有进程类型避免冲突（C001/C005）。

## compute_signals.py 调用格式

```bash
python compute_signals.py \
  --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-{0.5B|1.5B} \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-{size}_{dosage}_s123/lora_adapter \
  --benchmark {mmlu|gsm8k|arc_challenge} \
  --signal all \
  --ref-model-path &lt;ref_adapter_path> \
  --sft-data-dir /root/autodl-tmp/exp001/sft_data \
  --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-{size}_{dosage}_s123 \
  --cache-dir /root/autodl-tmp/.hf_cache
```

## 数据/模型路径确认

| 资源 | 路径 | 状态 |
|------|------|------|
| Base model 0.5B | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B` | EXISTS |
| Base model 1.5B | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B` | EXISTS |
| SFT data (d000/d005/d025/d100) | `/root/autodl-tmp/exp001/sft_data/sft_dosage_{000,005,025,100}.jsonl` | EXISTS |
| Contamination labels | `/root/autodl-tmp/exp001/sft_data/contamination_labels_*.json` | EXISTS |

## 关键注意事项

1. **`run_batch.py` 不支持 s123** — `SEED = "s42"` 硬编码在 line 39。需要修改脚本加 `--seed` 参数，或手动构造命令。

2. **ref model 路径**：S2 (Min-K++) 的参考模型应为同 seed 的 d000 checkpoint：
   - 0.5B ref: `.../Qwen2.5-0.5B_d000_s123/lora_adapter`
   - 1.5B ref: `.../Qwen2.5-1.5B_d000_s123/lora_adapter`

3. **总任务量**：8 checkpoint × 3 benchmark = 24 个 `compute_signals.py` 调用（每个调用计算 3 个 signal）。按 s42 经验，0.5B 每个调用约 10-15 分钟，1.5B 约 20-30 分钟。

---
