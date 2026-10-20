# analysis lc tfidf ortho verify

**pgpf collapse filter** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lc_tfidf_ortho_verify_20260513T112155_result.json`
- **Structured JSON:** [`a0662021fc8fc1126dfd.json`](../../sessions/a0/a0662021fc8fc1126dfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。注意 FAIL 是因为 `quality_vs_confidence` Spearman = -0.9979，但这在原始 BLEU-4 分析中也完全相同（-0.9979），与 LC 指标无关。原始 Phase 0 判定标准只检查 Pearson |r|，所以原结果也是 PASS。

## 验证结果

### LC 指标
Phase 0 数据和当前代码均使用 **BLEU-4**，尚未改为 TF-IDF cosine。

### TF-IDF Cosine LC 完整相关系数矩阵

**Pearson r:**

| | LC | SN | Quality | Confidence |
|---|---|---|---|---|
| **LC** | 1.0 | **-0.3598** | 0.0144 | -0.0339 |
| **SN** | | 1.0 | -0.0289 | 0.1080 |
| **Quality** | | | 1.0 | -0.2871 |
| **Confidence** | | | | 1.0 |

**Spearman rho:**

| | LC | SN | Quality | Confidence |
|---|---|---|---|---|
| **LC** | 1.0 | **-0.3773** | 0.0749 | -0.0651 |
| **SN** | | 1.0 | -0.1212 | 0.1123 |
| **Quality** | | | 1.0 | -0.9979* |
| **Confidence** | | | | 1.0 |

*\*Quality vs Confidence Spearman = -0.9979 与 BLEU-4 版本完全相同，是 PPL/log-prob 的固有数学关系，非 LC 相关问题。*

### 判定（按原 Phase 0 Pearson 标准）

- 所有 Pearson |r| < 0.7: **PASS** (|r|_max = 0.3598)
- LC vs Confidence |r| < 0.5: **PASS** (|r| = 0.0339)
- **OVERALL: PASS**

### BLEU-4 vs TF-IDF Cosine 对比（Pearson）

| 属性对 | BLEU-4 | TF-IDF cosine | 变化 |
|---|---|---|---|
| LC vs SN | -0.117 | **-0.360** | 绝对值增大，仍 < 0.7 |
| LC vs Quality | -0.048 | 0.014 | 趋近零 |
| LC vs Confidence | 0.303 | **-0.034** | 大幅下降，正交性更好 |
| |r|_max | 0.303 | 0.360 | 略有上升 |

TF-IDF cosine LC 与 Confidence 的相关性从 0.303 降至 0.034，正交性显著改善。LC vs SN 相关性有所增加（-0.117 → -0.360），但仍远低于 0.7 阈值。

---
