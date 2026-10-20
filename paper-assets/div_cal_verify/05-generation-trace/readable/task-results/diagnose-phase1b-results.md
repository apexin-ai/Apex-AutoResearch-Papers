# diagnose phase1b results

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase1b_results_20260513T031032_result.json`
- **Structured JSON:** [`2d150430165dcb4952a3.json`](../../sessions/2d/2d150430165dcb4952a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 1b Self-Iterate 实验结果

### 1. 进程状态
**已完成** — PID 123407 不存在，日志显示 `EXIT_CODE=0`，于 `Wed May 13 10:41:51 CST 2026` 正常结束。

### 2. 完成度
**8/8 代全部完成**（gen_0 ~ gen_7），总耗时约 60 分钟。

### 3. 每 Generation 指标

| Gen | PPL | RankMe | k-NN | Rare n-gram | Rank Corr | Notes |
|-----|-------|--------|-------|-------------|-----------|-------|
| 0 | 37.10 | 280.32 | 0.988 | 0.0290 | -0.023 | baseline |
| 1 | 44.90 | 297.81 | 0.988 | 0.0192 | -0.055 | |
| 2 | 51.63 | 302.62 | 0.987 | 0.0139 | -0.049 | |
| 3 | **56.97** | **303.27** | 0.988 | 0.0116 | -0.044 | PPL peak |
| 4 | 55.71 | 301.33 | 0.988 | 0.0101 | -0.042 | PPL 开始回落 |
| 5 | 51.74 | 297.35 | 0.988 | 0.0098 | -0.048 | |
| 6 | 48.67 | 293.01 | 0.988 | 0.0089 | -0.065 | |
| 7 | 48.11 | 289.79 | 0.988 | 0.0087 | -0.087 | |

原始 GPT2 预训练模型 RankMe 基线：**231.08**（all_results.json 中的 `rankme_gen0`）

### 4. 崩塌判断

**RankMe**：未出现 >20% 持续下降。先从 280→303 上升（gen 0→3），再缓慢下降至 290（gen 3→7），下降幅度仅 4.4%。所有 generation 均远高于原始基线 231.08。

**PPL**：先恶化（37.1→57.0，gen 0→3），后回落（57.0→48.1，gen 3→7）。非单调上升，呈倒 U 型。最终仍比 gen 0 差 30%。

**k-NN**：极其稳定，全程 0.987-0.988，无退化。

**Rare n-gram survival**：**单调下降 70%**（0.029→0.0087），这是最明显的崩塌信号——词汇多样性持续丢失。

**Rank correlation**：全程为小负值，从 -0.023 逐渐加深至 -0.087，合成数据与真实数据排序一致性在下降。

### 5. 日志最后几行
```
[5/5] Gen 7 summary:
  Perplexity:     48.11
  RankMe:         289.79
  k-NN accuracy:  0.9880
  Rare n-gram:    0.00871655790707865
  Rank corr:      -0.0869
  Time:           451s

===== PHASE 1b COMPLETE =====
End: Wed May 13 10:41:51 CST 2026
EXIT_CODE=0
```

错误日志中仅有 HuggingFace 连接超时（Network unreachable），均为非致命错误，模型从本地 cache 加载成功。

### 6. Conclusion: **Partial collapse (success)**

无策展的 self-iterate 基线展现了**部分崩塌**模式：
- **崩塌维度**：词汇多样性（rare n-gram）持续严重丢失（-70%），rank correlation 持续恶化
- **稳定维度**：表征质量（RankMe、k-NN）几乎无退化；PPL 先恶化后自恢复

这是一个有价值的正面结果——证明 uncurated self-iterate 下"model collapse"主要表现为多样性崩塌而非全面质量崩塌，为后续 Phase 2 的 curation 方法提供了清晰的 baseline 和改进目标（主攻 rare n-gram 保持）。

---
