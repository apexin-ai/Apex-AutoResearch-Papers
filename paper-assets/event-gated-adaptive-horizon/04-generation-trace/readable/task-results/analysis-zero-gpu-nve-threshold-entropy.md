# analysis zero gpu nve threshold entropy

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_zero_gpu_nve_threshold_entropy_20260524T114932_result.json`
- **Structured JSON:** [`24779519205d01983a17.json`](../../sessions/24/24779519205d01983a17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 分析 1: NVE Threshold Sensitivity

n=32 (Walker 23 + Cheetah 9), n_pos=11, n_neg=21, AUROC=0.961

| Threshold | Accuracy | TPR | FPR | F1 |
|-----------|----------|-----|-----|-----|
| **1.3x** | 81.2% | 1.000 | 0.286 | 0.786 |
| **1.5x** | **90.6%** | **1.000** | 0.143 | **0.880** |
| **1.7x** | 81.2% | 0.727 | 0.143 | 0.727 |
| **2.0x** | 87.5% | 0.727 | 0.048 | 0.800 |

**1.5x 是最优 F1 阈值**（90.6% accuracy, perfect recall）。FP 来自 3 个非 CIVO 机制：frozen emb self-correction (047, 057) 和 IRD (008e_v3_s2)。1.7x 起丢失 3 个 FN（009b, 008d_s3, 018_s1），均为边界 CIVO 案例。Cheetah 在所有 ≥1.5x 阈值下 100% 准确。

### 分析 2: Actor Entropy 图

成功生成。5 个实验均有 actor_entropy 数据，已画对比图。

关键发现：
- 所有实验起始 ~8.1（最大熵），然后收敛
- Collapsed 实验（008d, 006）在 15K 时 entropy 仍为正值（0.48, 0.96），而 healthy 实验已下降到负值（-1.15, -1.18）—— collapsed 反而收敛更慢
- Baseline 在 105K 后出现独特的 entropy recovery（-5.2 → -0.78），伴随 return 从 ~400 提升到 ~950

### 文件路径

| 产出 | 服务器路径 | 本地路径 |
|------|-----------|---------|
| NVE sensitivity 表格 | `/root/autodl-tmp/.../artifacts/nve_threshold_sensitivity.md` | `artifacts/nve_threshold_sensitivity.md` |
| Actor entropy PDF | `/root/autodl-tmp/.../artifacts/figures/actor_entropy_comparison.pdf` | (服务器端) |
| Actor entropy PNG | `/root/autodl-tmp/.../artifacts/figures/actor_entropy_comparison.png` | (服务器端) |

Actor entropy 图因 SCP 不可用未能下载到本地。如需要可手动从服务器获取。

---
