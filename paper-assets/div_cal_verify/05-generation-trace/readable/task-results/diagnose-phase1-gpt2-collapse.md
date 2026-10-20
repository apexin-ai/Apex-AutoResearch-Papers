# diagnose phase1 gpt2 collapse

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase1_gpt2_collapse_20260513T005450_result.json`
- **Structured JSON:** [`d051928ffe537c48845f.json`](../../sessions/d0/d051928ffe537c48845f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。诊断结果如下：

---

## 结论：**Negative**（实验成功完成，但未观察到模型崩塌）

### 各方法完成情况

| 方法 | 完成代数 | 状态 |
|------|---------|------|
| rgds | 6/6 (gen 0-5) | ✅ 完成 |
| uncurated | 6/6 (gen 0-5) | ✅ 完成 |
| external_only | 0/6 | ❌ 未运行（日志中无任何记录） |

**无错误**：error=0, traceback=0, killed=0, oom=0。

### 关键指标

**RGDS:**

| Gen | PPL | RankMe | k-NN | Rare | Rank Corr |
|-----|-----|--------|------|------|-----------|
| 0 | 36.64 | 286.46 | 0.987 | 0.0354 | -0.0595 |
| 1 | 37.05 | 287.32 | 0.988 | 0.0346 | -0.0851 |
| 2 | 36.03 | 270.93 | 0.988 | 0.0353 | -0.0936 |
| 3 | 35.96 | 262.62 | 0.988 | 0.0356 | -0.1188 |
| 4 | 35.96 | 265.12 | 0.988 | 0.0358 | -0.1024 |
| 5 | 35.56 | 274.63 | 0.988 | 0.0350 | -0.1014 |

**Uncurated:**

| Gen | PPL | RankMe | k-NN | Rare | Rank Corr |
|-----|-----|--------|------|------|-----------|
| 0 | 36.20 | 290.15 | 0.988 | 0.0354 | -0.0670 |
| 1 | 35.44 | 281.26 | 0.988 | 0.0365 | -0.0520 |
| 2 | 34.89 | 268.41 | 0.988 | 0.0353 | -0.0975 |
| 3 | 34.84 | 273.41 | 0.988 | 0.0354 | -0.1080 |
| 4 | 34.52 | 283.12 | 0.988 | 0.0348 | -0.1351 |
| 5 | 34.75 | 297.02 | 0.988 | 0.0351 | -0.1294 |

### 崩塌是否发生：**否**

- **PPL**：两种方法 PPL 均**轻微下降**（rgds: 36.64→35.56, uncurated: 36.20→34.75），未上升
- **RankMe**：rgds 从 286→275 有波动但未崩塌；uncurated 从 290→297 反而略升
- **k-NN**：恒定 0.988，无退化
- **Rare n-gram**：恒定 ~0.035，无变化
- **Rank correlation**：两者均从 ~-0.06 缓慢下降到 ~-0.10/-0.13，变化轻微

6 代迭代后所有指标基本平稳，GPT2-125M 在此设定下**未复现模型崩塌**。可能原因：模型规模太小 / 数据量不足 / 代数不够。

### 日志最后几行

```
  Perplexity:     34.75
  RankMe:         297.02
  k-NN accuracy:  0.9880
  Rare n-gram:    0.03509125146558973
  Rank corr:      -0.1294
  Time:           1255s

============================================================
FINAL SUMMARY -- uncurated
============================================================
 Gen      PPL   RankMe      kNN     Rare     Corr
   0    36.20   290.15   0.9880   0.0354  -0.0670
   1    35.44   281.26   0.9880   0.0365  -0.0520
   2    34.89   268.41   0.9880   0.0353  -0.0975
   3    34.84   273.41   0.9880   0.0354  -0.1080
   4    34.52   283.12   0.9880   0.0348  -0.1351
   5    34.75   297.02   0.9880   0.0351  -0.1294
===== PHASE 1 COMPLETE =====
```

---
