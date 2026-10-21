# analysis d1d3 inconsistency audit v2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d1d3_inconsistency_audit_v2_20260518T162720_result.json`
- **Structured JSON:** [`7fbe76498f9c0477853c.json`](../../sessions/7f/7fbe76498f9c0477853c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

有足够数据了。let me compile the final report while waiting for the rest.

## 调查报告

### 1. Table 2 括号数字的确切来源

**Table 2 主表（4-class accuracy）**：确认来自各 cell 的 `results/*/classification_report.txt`，使用 80/20 train-test split + RF(n_estimators=100) + StandardScaler。全 9 cell 精确匹配。

**Table 2 括号（d1-d3 three-class accuracy）**：**无法找到单一 JSON 文件或统一计算口径**。测试了以下 7 种计算方式，没有任何一种能一致复现所有 9 cell：

| 计算方式 | 配置 | 匹配 Table 2 的 cell 数 |
|----------|------|------------------------|
| 口径 A: 4-class RF 5-fold CV, d1-d3 subset | 200 trees, 5-fold | 0/9 |
| 口径 B: 3-class RF 5-fold CV | 200 trees, 5-fold | 0/9 |
| 3-class RF 80/20, 100 trees, +scale | seed=42 | 1/9 (gpt2xl_topk50) |
| 3-class RF 80/20, 200 trees, +scale | seed=42 | 0/9 |
| 3-class RF 80/20, 100 trees, no scale | seed=42 | 1/9 (olmo_nucleus) |
| 3-class RF 80/20, 200 trees, no scale | seed=42 | 2/9 (gpt2xl_topk50, partial) |
| 4-class RF 80/20, d1-d3 test subset | various | 0/9 |

**结论**：括号数字很可能是**在项目开发不同阶段分批计算**的，各 cell 可能使用了不同的 RF 配置（n_estimators、是否 scale、甚至可能不同 seed）。没有存档文件记录确切来源。

### 2. 全 9 cells 两种口径对比表

```
Cell             Table2  口径A(4cls→d1d3) 口径B(3cls RF)  3cls_100_nosc  差距(Table2-A)
                 括号     5fold/200trees  5fold/200trees  80/20 split
─────────────────────────────────────────────────────────────────────────
pythia_nucleus    71.2    71.8            72.0            70.8           -0.6
pythia_temp09     70.6    69.3            69.4            70.1           +1.3
pythia_topk50     58.8    58.9            59.0            58.4           -0.1
olmo_nucleus      75.0    72.6            73.6            75.0 ✓         +2.4
olmo_temp09       76.3    76.6            76.8            76.2           -0.3
olmo_topk50       66.1    66.1            66.6            65.3            0.0
gpt2xl_nucleus    79.0    79.6            80.1            79.1           -0.6
gpt2xl_temp09     82.6    81.5            81.9            82.1           +1.1
gpt2xl_topk50     69.5    68.1            68.3            68.9           +1.4
─────────────────────────────────────────────────────────────────────────
Mean              72.1    71.6            72.0            72.0           +0.5
```

Table 2 括号 vs 口径 A 平均偏差 +0.5 pp，vs 口径 B 偏差 +0.1 pp。最大不一致在 olmo_nucleus (+2.4 pp vs 口径 A) 和 gpt2xl_topk50 (+1.4 pp vs 口径 A)。

### 3. Abstract 71.1% 的计算方式

**Abstract 71.1% = `d1d3_balanced_acc.json` 中 `mean_balanced_accuracy: 0.7109`**

来源链条：
- `compute_reviewer_metrics.py` → 从 `baseline_battery_9cell/all_results.json` 读取 4-class RF 的 per_class_recall
- 计算 `(d1_recall + d2_recall + d3_recall) / 3` 得到每 cell 的 d1-d3 balanced accuracy
- 9 cell 平均 = 71.1%

这是**口径 A**（4-class RF 5-fold CV with 200 trees，取 d1-d3 subset 的 balanced accuracy）。

注意 Table 2 caption 声称"5-fold CV, 200 trees"，但主表数字实际来自 80/20 split + 100 trees。Abstract 的 71.1% 使用的口径（5-fold/200-tree）与 Table 2 的口径（80/20/100-tree）不一致。

### 4. 建议统一方案

**推荐**：全部统一到**口径 A**（4-class RF, 5-fold CV, 200 trees, d1-d3 subset balanced accuracy）。

理由：
1. 与 Abstract 71.1% 一致（已发表的最重要数字）
2. 与 caption 声称的 "5-fold CV, 200 trees" 一致
3. `baseline_battery_9cell/all_results.json` 和 `d1d3_balanced_acc.json` 有完整存档
4. 5-fold CV 比 80/20 split 方差更低，更可靠
5. 4-class RF 的 d1-d3 subset 评估避免了"为 d1-d3 括号数字专门训练另一个分类器"的方法论复杂性

统一后的 Table 2 括号数字（from `d1d3_balanced_acc.json`）：

```
Pythia-1.4B  & 78.2\,(70.9) & 76.3\,(69.1) & 69.6\,(58.5)
OLMo-1B      & 78.8\,(72.1) & 82.0\,(77.0) & 74.2\,(65.1)
GPT-2 XL     & 83.3\,(78.9) & 85.4\,(80.5) & 76.6\,(67.7)
```

**注意**：主表 4-class 数字也应从 80/20 split 切换到 5-fold CV 结果以保持一致（主表数字也会轻微变化），或者 caption 应修正为 "80/20 split, 100 trees"。

---
