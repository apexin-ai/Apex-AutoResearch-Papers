# ops gpu status and d000v3 prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-and-d000v3-prep_20260515T200336_result.json`
- **Structured JSON:** [`2aa0ef37f601b0e31fa5.json`](../../sessions/2a/2aa0ef37f601b0e31fa5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整报告。

---

## Part 1: GPU 状态全面检查

| GPU | PID(s) | VRAM | Util% | 任务 | 状态 |
|-----|--------|------|-------|------|------|
| **cuda:0** | 594494 | 17966 MiB | 31-35% | d100_a32_s123 SFT | 活跃，已运行 3h30m |
| **cuda:1** | 593745 | 13332 MiB | 4-31% | d100_a32_s42 SFT v2 | 活跃，2998/4159 (72%)，ETA ~1h20m |
| **cuda:2** | 622856, 623491 | 7064+6788 MiB | 97-98% | d005_s42 mmlu signals + d005_s123 gsm8k eval | 活跃计算中 |
| **cuda:3** | 617202 | 7526 MiB | 57-64% | d000_s42 mmlu signals | 活跃，已运行 1h07m |
| **cuda:4** | 622558, 623837 | 6882+6882 MiB | 91% | signals v5 (d025/d100 mmlu) + d025_s42 mmlu signals | 活跃计算中 |
| **cuda:5** | 589763 | 17642 MiB | 26-59% | **d025_v3 SFT** | **3228/3384 (95.4%)，ETA ~10 min** |

### 重点问题回答

- **cuda:2**：之前 0% compute 的问题**已解决**，当前 97-98% utilization，两个进程同时活跃计算
- **cuda:3**：PID 617202 确认活跃（57-64% util），在跑 d000_s42 mmlu 全部 signals
- **cuda:5**：d025_v3 SFT 仍在运行，但 **95% 完成，约 10 分钟后释放**
- **最先释放**：**cuda:5**，预计 ~10 分钟内

### 释放顺序预估
1. cuda:5 — ~10 min（d025_v3 SFT 即将完成）
2. cuda:3 — ~30-60 min（d000 signals）
3. cuda:2 — ~30-60 min（两个进程）
4. cuda:0/1 — ~1h20m（d100 SFT 训练）
5. cuda:4 — ~1-2h（signals v5 刚开始）

---

## Part 2: d000_v3 重训准备

### 参数对比

| 参数 | 失败的 d000_v3 | 新 d000_v3（标准配置） |
|------|---------------|----------------------|
| lr | 5e-5 ✓ | 5e-5 |
| lora_alpha | **32** | **16** |
| lora_r | 16 | 16 |
| output_dir | Qwen2.5-3B_d000_a32_s42 | Qwen2.5-3B_d000_v4_s42 |
| 失败原因 | cuda:4 双进程 OOM | 单 GPU 独占 |

### 准备好的提交命令

目标 GPU：**cuda:5**（等 d025_v3 完成后提交）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=5 python /root/contamcal-irt-calibration/exp001/train_sft.py \
  --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
  --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v4_s42 \
  --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 \
  --lr 5e-5 --lora-alpha 16 --cache-dir /root/autodl-tmp/.hf_cache
```

**注意**：用 `d000_v4` 命名以避免与失败的 `d000_a32_s42`（alpha=32）冲突。当前没有空闲 GPU，需等 cuda:5 释放（~10 min）。需要提交前再次 `nvidia-smi` 确认 cuda:5 已空闲（C001/C002/C003）。

---

## Part 3: d005/gsm8k stalled 状态

### 当前 d005_s42 signals 覆盖

| Signal | mmlu | gsm8k | arc |
|--------|------|-------|-----|
| embedding | ✓ | ✓ | ✓ |
| minkpp | ✓ | ✓ | ✓ |
| selfcritique | ✗ | ✗ | ✓ |
| merged | ✗ | ✗ | ✓ |

**stalled 未完全解决**：selfcritique 和 merged 仍缺 mmlu 和 gsm8k。

但现在 **PID 622856 正在 cuda:2 上跑 d005_s42 mmlu signals (all)**，应该会补上 selfcritique_mmlu → merged_mmlu。gsm8k selfcritique 仍需后续补算。

同时 **PID 623491 在 cuda:2 跑 d005_s123 gsm8k eval rerun**（registry: exp_001_eval_3B_d005_s123_gsm8k），这是 D068 gap-fill 的一部分。

**结论**：d005 stall 正在被 v5 和当前活跃进程部分修复，mmlu 部分预计本轮解决，gsm8k selfcritique 需要额外一轮提交。

---
