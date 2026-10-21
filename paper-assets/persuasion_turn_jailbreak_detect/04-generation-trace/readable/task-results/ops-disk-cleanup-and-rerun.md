# ops disk cleanup and rerun

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-and-rerun_20260517T225608_result.json`
- **Structured JSON:** [`f7afd14dabbead84bef2.json`](../../sessions/f7/f7afd14dabbead84bef2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 最终汇报

### 1. 磁盘清理
| 来源 | 释放空间 |
|------|---------|
| phase_b_deberta/ | 710 MB |
| phase_b_gru/ | 23 MB |
| plan_002/gru/ (旧损坏) | 464 MB |
| plan003_deberta_scrambled/ | 710 MB |
| plan003_gru_scrambled/ | 232 MB |
| ~/.cache/huggingface/ (冗余) | 2.1 GB |
| epoch checkpoints 清理 | ~200 MB |
| **总计** | **~4.4 GB** |

**最终磁盘**: 7.1 GB 可用（从 3.6 GB → 7.1 GB）

### 2. Plan_002: Treatment vs Baseline

| K | Treatment (FT-DeBERTa+GRU) F1 | Baseline (Vanilla+GRU) F1 | TF-IDF+LR F1 |
|---|---|---|---|
| 1 | **1.0000** | 0.9620 | 1.0000 |
| 2 | **1.0000** | 0.9870 | 1.0000 |
| 3 | 1.0000 | 1.0000 | 1.0000 |
| 5 | 1.0000 | 1.0000 | 1.0000 |
| full | 1.0000 | 1.0000 | 1.0000 |

Treatment 在所有 K 完美检测。Baseline 仅在 K=1,2 有轻微下降。

### 3. Plan_003: Scrambled vs Proper Treatment

| K | Proper Treatment F1 (plan_002) | Scrambled Treatment F1 (plan_003) | Baseline F1 |
|---|---|---|---|
| 1 | 1.0000 | 1.0000 | 0.9870 |
| 2 | 1.0000 | 1.0000 | 0.9867 |
| 3 | 1.0000 | 1.0000 | 0.9867 |
| 5 | 1.0000 | 1.0000 | 1.0000 |
| full | 1.0000 | 1.0000 | 1.0000 |

**关键发现**: Scrambled labels 和 proper labels 产生相同的完美检测结果。TF-IDF+LR 也在所有 K 得到 F1=1.0。这表明当前数据集的 jailbreak/benign 分类任务过于简单——文本内容本身已提供完美的分离信号，persuasion strategy 信息对检测性能没有增量贡献。

### 4. 最终磁盘状态
**7.1 GB 可用**（远超 3 GB headroom 要求）

### 产出文件
- `results/plan_002_eval.json`
- `results/plan_003_v2_eval.json`
- `checkpoints/plan_002/gru/treatment/best.pt`
- `checkpoints/plan_002/gru/baseline/best.pt`
- `checkpoints/plan_003_v2/gru/treatment/best.pt`
- `checkpoints/plan_003_v2/deberta_multitask/best/`

---
