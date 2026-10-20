# research preparing queue review

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_preparing-queue-review_20260516T002837_result.json`
- **Structured JSON:** [`4d14b425e2fc611d3b73.json`](../../sessions/4d/4d14b425e2fc611d3b73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前 GPU 占用和 PREPARING 队列已梳理完毕。下面是分析。

## 当前 GPU 占用 (6/6 饱和)

| GPU | 实验 | 类型 | 预计释放 |
|-----|------|------|---------|
| cuda:0 | exp_001_sft_3B_d005_s42_a32 + eval_d100_s123_a32_batch | SFT+eval | 较晚（SFT长任务） |
| cuda:1 | exp_001_sft_3B_d100_s42_a32_v3 | SFT (216K samples) | 最晚 |
| cuda:2 | exp_002_signals_3B_v7 (d005_s123) | signals | **较快释放** |
| cuda:3 | exp_001_eval_3B_d025_v3_s42_batch | eval batch | **较快释放** |
| cuda:4 | exp_002_signals_3B_v8 (d025_s123 + d100_a32_s123) | signals ×6 | 中等 |
| cuda:5 | exp_002_signals_3B_d025_v3_s42 | signals | **较快释放** |

## PREPARING 过滤

23 条 PREPARING 中，大量是历史 killed/failed/deprecated/cancelled。实际可执行的：

| # | exp_id | 类型 | 状态 |
|---|--------|------|------|
| 1 | exp_001_sft_3B_d000_v4 → 应为 d000_s42_a32 | SFT | 需构建命令 (alpha=32, lr=5e-5) |
| 2 | exp_001_eval_3B_d005_s42_para_aligned | eval | 阻塞：等 d005_s42_a32 SFT 完成 |
| 3 | exp_001_eval_3B_d005_s123 | eval | checkpoint 待验证 |
| 4 | exp_001_eval_3B_d025_s123 | eval | checkpoint 待验证 |
| 5 | exp_001_sft_3B_d100_s123_a32 | SFT | 已完成(eval正跑)，条目过期 |
| 6 | exp_001_sft_3B_d025_s42_a32_v3 | SFT | CANCELLED（checkpoint 已存在） |
| 7 | exp_001_sft_15B_d025_s123 | SFT 1.5B | failed EXIT_CODE=2，需debug |

其余 16 条全是历史遗留（killed/failed/deprecated），无需操作。

## 提交就绪队列

| 优先级 | exp_id | 需等待的 GPU | 前置条件 | 提交命令就绪? |
|--------|--------|-------------|---------|-------------|
| **P0** | exp_001_sft_3B_d000_s42_a32 (新建) | cuda:2/3/5 (先释放者) | 需验证 `sft_dosage_000.jsonl` 存在 | **否** — 需构建命令 (见下) |
| **P1** | exp_001_eval_3B_d005_s42_a32_batch (新建) | cuda:0 释放后 或 任意空闲 GPU | **阻塞**: d005_s42_a32 SFT 完成 (当前 cuda:0 RUNNING) | **否** — 等 checkpoint |
| **P1** | exp_001_eval_3B_d005_s42_para_aligned | cuda:3 释放后 | **阻塞**: 同上，需 d005_s42_a32 新 checkpoint | **否** — 等 checkpoint |
| **P2** | exp_001_eval_3B_d005_s123 | 任意空闲 GPU | checkpoint `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter` 待验证 | 有 spec，需确认 checkpoint |
| **P2** | exp_001_eval_3B_d025_s123 | 任意空闲 GPU | checkpoint `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter` 待验证 | 有 spec，需确认 checkpoint |
| **P3** | exp_001_sft_15B_d025_s123 | 任意空闲 GPU | 脚本 bug (EXIT_CODE=2)，需先 debug | **否** |

## P0 命令模板 (d000_s42_a32 SFT)

基于当前 RUNNING 的 d005_s42_a32 命令模式：

```bash
bash -c "export CUDA_VISIBLE_DEVICES=&lt;N> && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/contamcal-irt-calibration/exp001/train_sft.py \
  --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
  --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_a32_s42 \
  --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 \
  --max-seq-length 2048 --lr 5e-5 --lora-alpha 32"
```

**提交前必须验证**：
1. `sft_dosage_000.jsonl` 存在且非空
2. 目标 GPU nvidia-smi 确认空闲 (C001/C002)
3. 无残留进程 (C003)
4. CUDA_VISIBLE_DEVICES 显式设置 (C004)

## 建议的释放顺序行动

1. **cuda:2/3/5 释放** → 提交 P0 d000_s42_a32 SFT
2. **cuda:0 释放**（d005_s42_a32 SFT 完成后）→ 提交 P1 d005_s42 eval batch (aligned + para_aligned)
3. **剩余 GPU 释放** → P2 s123 evals (d005_s123, d025_s123)
4. P3 1.5B 留到 GPU 充裕时 debug

P1 的两个 eval 都被 d005_s42_a32 SFT 阻塞，实际上 **P0 d000_s42_a32 SFT 是唯一可以在下一个 GPU 释放时立即提交的实验**——前提是验证 `sft_dosage_000.jsonl` 存在。

---
