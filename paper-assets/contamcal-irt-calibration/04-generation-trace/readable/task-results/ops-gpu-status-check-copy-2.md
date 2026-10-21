# ops gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260515T000646_result.json`
- **Structured JSON:** [`3e40c8f9f4d7aa4006b0.json`](../../sessions/3e/3e40c8f9f4d7aa4006b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 使用情况

| GPU | 显存占用 | 利用率 | PID | 任务 |
|-----|---------|--------|-----|------|
| **0** | 7539/24564 MiB | 89% | 470062 | evaluate.py 3B d100_v2_s42_para_aligned |
| **1** | 21803/24564 MiB | 49% | 464138 | SFT 0.5B d005 s123 |
| **2** | 14723/24564 MiB | 37% | 435420 | SFT 1.5B d100 s123 |
| **3** | 17637/24564 MiB | 46% | 466755 | train_sft.py 3B d025 s42 |
| **4** | 13583/24564 MiB | 65% | 441570 | eval 3B d000 v2 aligned |
| **5** | 0/24564 MiB | 0% | — | **空闲** |

### 关键发现

1. **空闲 GPU: 只有 cuda:5**。cuda:0 并非空闲，正在跑 3B d100_v2 para_aligned 评估（新任务，report.md 未记录）。cuda:3 也不空闲。

2. **exp_001_sft_d025_3B_v2 (PID 466755) 在 cuda:3 上**，参数: `--model-name Qwen2.5-3B --data-path sft_dosage_025.jsonl --output-dir Qwen2.5-3B_d025_s42 --gpu 3 --batch-size 1 --grad-accum 16`

3. **CPU-only 任务**:
   - CmdStan IRT 采样活跃: 4pl diagnose (PID 470514) + 2pl_gamma 4 chains (PID 470528-470533)
   - exp-004 v3 PID 599562 **不存在**，已结束

4. **与 report.md 差异**: cuda:0 上跑了一个新的评估任务 (3B d100_v2_s42_para_aligned)，report 中未记录；cuda:1 的 PID 是 464138（非 464137，可能是子进程）；cuda:2 的 PID 是 435420（非 435415）。

---
