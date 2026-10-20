# analysis c2 opt13b a050 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c2_opt13b_a050_s42_fp32_20260525T104803_result.json`
- **Structured JSON:** [`d82ffb8b5fb68468e929.json`](../../sessions/d8/d82ffb8b5fb68468e929.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇总如下：

---

## c2_opt13b_a050_s42_fp32 分析摘要

### 训练状态
- **正常完成**，EXIT_CODE=0，gen_0 → gen_10 共 11 generations
- 运行时间 ~10.7 GPU-hours

### Diversity 轨迹（确实有 collapse）
| Metric | Gen 0 | Gen 10 | 降幅 |
|--------|-------|--------|------|
| distinct_1 | 0.103 | 0.065 | -37% |
| distinct_2 | 0.525 | 0.280 | -47% |
| distinct_3 | 0.818 | 0.439 | -46% |
| PPL | 24.88 | 24.94 | +0.2% (平稳) |

### D102 5-method Forward Detection（6-pair basis）

| Method | Forward sig | 备注 |
|--------|------------|------|
| **PermG (FDR)** | **0/6** | 最低 p_fdr=0.112 (token_entropy<distinct_1) |
| Diff XCorr (FDR) | 2/6 | token_entropy<d1, ece<d1 |
| Threshold onset (3sigma) | 0/6 | canary_onset 存在但 downstream_onset=null |
| TY Granger | 1/6 | token_entropy<d1 仅此一对 |
| Naive XCorr | 0/6 | peak_lag 方向全部为正（非 forward） |

**Robust pairs (≥3/5 methods): 0/6**

### 与 Pythia-410M α=0.50 对比
| | Pythia-410M | OPT-1.3B |
|--|------------|----------|
| PermG fwd | **6/8** | **0/8** |
| Robust pairs | (参考) | 0/8 |

### 结论：**Negative**

OPT-1.3B α=0.50 diversity collapse 确实发生（distinct 指标下降 37-47%），但 canary→downstream **temporal lead-lag 因果信号极弱**：PermG 0/6，threshold onset 0/6，robust pairs 0/6。与 Pythia-410M α=0.50 的 6/8 PermG 检测率形成鲜明对比。

结合 s43 也是 failed，OPT-1.3B 在 transition region (α=0.50) 的 lead-lag 结构不复现 Pythia 的模式。这提示 phase diagram 的 transition boundary 可能是 **architecture-dependent** 的——OPT 在 α=0.50 处的因果结构更弱或需要更高 α 才能建立。

---
