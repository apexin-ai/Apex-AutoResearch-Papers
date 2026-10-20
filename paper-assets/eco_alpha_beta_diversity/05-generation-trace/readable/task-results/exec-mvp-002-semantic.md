# exec mvp 002 semantic

**eco alpha beta diversity** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_mvp_002_semantic_20260521T143952_result.json`
- **Structured JSON:** [`58a451bd57c0709405fe.json`](../../sessions/58/58a451bd57c0709405fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 语义级 MVP (mvp_002) 实验完成 — **OVERALL: KILL**

### 核心数据

| | no-AI | AI-editor | AI-ideas+editor |
|---|---|---|---|
| 故事数 | 98 | 100 | 99 |
| 平均句子数 | 7.7 | 7.9 | 7.8 |
| q=1 α (k=50) | 4.26 [3.95, 4.57] | 4.66 [4.29, 5.02] | 4.50 [4.18, 4.85] |
| q=1 β (k=50) | 9.09 [7.89, 9.23] | 9.18 [8.01, 9.33] | 9.60 [8.15, 9.86] |
| Embedding cosine r | — | 0.041 | — |

### Pass/Fail 判定

| 标准 | 结果 |
|---|---|
| PASS 1 (α↑) | **FAIL** — CIs 全部重叠 |
| PASS 2 (β↓) | **FAIL** — 无 β 下降 |
| PASS 3 (Baselga 可区分) | **PASS** — bal≫gra |
| PASS 4 (cosine r>0.3) | **FAIL** — r=0.04 |
| FAIL 1 (模式缺失) | **触发** |
| FAIL 2 (cosine 恢复 Baselga) | **未触发** (R²=0.001) |
| k 敏感性 | 50/100/200 全 FAIL，结论稳定 |

### 根本原因

每篇故事平均仅 ~8 个句子 → 聚类后只有 ~5 个 semantic species → 多样性估计方差极大，远不如词级 (~100+ unique tokens)。句子级粒度对这个数据集太粗。

### Kill/Go 结论

**KILL。** 词汇级被文本长度混淆，语义级分辨率不足。Baselga 分解提供了独特结构信息（两个 MVP 中 PASS 3 都通过），但框架整体无法通过自己的验证标准。

### 已注册 Artifacts
- `semantic_mvp_results.json` — 完整结果
- 4 张图：Hill numbers、Baselga、cosine heatmap、k sensitivity
- `semantic_mvp_002_report.md` — 完整报告

---
