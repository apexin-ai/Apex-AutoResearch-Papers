# diagnose phase2 progress

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase2_progress_20260513T061601_result.json`
- **Structured JSON:** [`69021ac2759e6fb4fcc8.json`](../../sessions/69/69021ac2759e6fb4fcc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 2 状态报告

### 1. 进程状态
**存活** — PID 138667 已运行 **2h35m**，正在执行 `run_phase2.sh`（GPU 1）。

### 2. 各方法完成进度

| 方法 | 完成代数 | metrics.json | 状态 |
|------|---------|-------------|------|
| uncurated | 8/8 (gen_0–7) | 8个 ✓ | **已完成** |
| rgds | 8/8 (gen_0–7) | 8个 ✓ | **已完成** |
| external_only | 2/8 (gen_0–1) | 1个 (gen_0) | **运行中** — 正在 gen_0 的 step [3/5] 训练 |

### 3. 日志最后状态
external_only gen_0：已完成数据生成(975 seq)、子模块选择(487/975)，正在训练 student (lr=5e-05, epochs=3)。

### 4. GPU 状态

| GPU | 显存使用 | 利用率 |
|-----|---------|--------|
| GPU 0 | 49,175 / 97,887 MiB | 0% |
| GPU 1 | 21,687 / 97,887 MiB | 0% |

GPU 利用率 0% 可能是训练 step 间隙的瞬时值。

### 5. 错误检查
**无错误** — 日志中无 error/exception/traceback/killed/oom。

### 6. Metrics 汇总

**Uncurated (baseline, 全量训练 ~975 seq):**

| Gen | PPL | RankMe | KNN Acc | Rare Ngram | Train Loss |
|-----|-----|--------|---------|------------|------------|
| 0 | 37.10 | 280.32 | 0.988 | 0.0290 | 1.171 |
| 1 | 44.89 | 297.80 | 0.988 | 0.0192 | 0.467 |
| 2 | 51.32 | 302.47 | 0.988 | 0.0139 | 0.275 |
| 3 | 56.25 | 303.05 | 0.987 | 0.0118 | 0.208 |
| 4 | 55.88 | 300.51 | 0.988 | 0.0102 | 0.190 |
| 5 | 50.08 | 296.54 | 0.988 | 0.0099 | 0.190 |
| 6 | 48.25 | 290.42 | 0.988 | 0.0094 | 0.185 |
| 7 | 50.28 | 291.43 | 0.988 | 0.0090 | 0.173 |

**RGDS (子模块选择 ~488/977 seq):**

| Gen | PPL | RankMe | KNN Acc | Rare Ngram | Sel/Rej Ratio | Train Loss |
|-----|-----|--------|---------|------------|---------------|------------|
| 0 | 37.09 | 275.89 | 0.988 | 0.0290 | 1.037 | 1.070 |
| 1 | 45.36 | 291.76 | 0.988 | 0.0202 | 0.910 | 0.497 |
| 2 | 50.51 | 292.74 | 0.988 | 0.0151 | 0.927 | 0.264 |
| 3 | 53.82 | 294.03 | 0.988 | 0.0124 | 0.941 | 0.179 |
| 4 | 53.97 | 294.92 | 0.988 | 0.0099 | 0.895 | 0.144 |
| 5 | 61.75 | 293.84 | 0.988 | 0.0082 | 0.811 | 0.116 |
| 6 | 64.12 | 293.76 | 0.988 | 0.0067 | 0.717 | 0.090 |
| 7 | 75.07 | 292.72 | 0.988 | 0.0051 | 0.517 | 0.062 |

**External_only (已完成 gen_0):**

| Gen | PPL | RankMe | KNN Acc | Rare Ngram | Sel/Rej Ratio | Train Loss |
|-----|-----|--------|---------|------------|---------------|------------|
| 0 | 37.04 | 275.07 | 0.988 | 0.0290 | 1.137 | 1.419 |

### 7. 关键观察

- **RGDS 后期出现严重 model collapse**：PPL 从 gen_0 的 37 飙升到 gen_7 的 75，比 uncurated 的 50 还差。sel/rej ratio 从 1.04 降到 0.52，说明选择器越来越倾向于选择低多样性数据。
- **Uncurated** PPL 在 gen_3–4 达到峰值(~56)后回落并趋于稳定(~50)，collapse 更温和。
- **Rare ngram survival** 三种方法都单调下降，RGDS 下降最快(0.029→0.005)。
- **KNN accuracy** 所有方法所有代数都锁在 0.988，无区分度。

### 8. Registry 建议
**RUNNING** — external_only 还有 gen_1–7 待完成，预计还需约 1.5h。完成后可更新为 DONE。

---
