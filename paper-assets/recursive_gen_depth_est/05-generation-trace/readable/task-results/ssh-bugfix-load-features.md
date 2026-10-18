# ssh bugfix load features

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_bugfix_load_features_20260515T023831_result.json`
- **Structured JSON:** [`e9e3bb7bb1cd225f3195.json`](../../sessions/e9/e9e3bb7bb1cd225f3195.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成报告

### 1. Bug 修复 Diff

**根因**: 文件本身无问题（无 `\r`、无空行）。JSONDecodeError 是因为读取尚在写入的文件（最后一行不完整）。

**修复**: 4 个文件的 `load_features` 函数添加 try/except 防御:

```diff
 def load_features(path):
     records = []
     with open(path) as f:
-        for line in f:
+        for i, line in enumerate(f):
             line = line.strip()
-            if line:
-                records.append(json.loads(line))
+            if not line:
+                continue
+            try:
+                records.append(json.loads(line))
+            except json.JSONDecodeError as e:
+                print(f'WARNING: Skipping line {i+1} in {path}: {e}')
```

修改文件: `scripts/train_classifier.py`, `src/baselines.py`, `src/atlas_analysis.py`, `src/dcol_dataset.py`

---

### 2. GPT-2 XL topk50 完整分类结果

#### 4-class (depth 0/1/2/3, n=20000)

| 分类器 | Accuracy | 95% CI |
|--------|----------|--------|
| LR | 71.30% | [69.90%, 72.70%] |
| **RF** | **74.45%** | [73.02%, 75.78%] |

Pairwise AUC (RF):
| Pair | AUC |
|------|-----|
| d0 vs d1 | 0.9906 |
| d0 vs d2 | 0.9975 |
| d0 vs d3 | 0.9986 |
| d1 vs d2 | 0.8126 |
| d1 vs d3 | 0.9708 |
| d2 vs d3 | 0.7529 |

#### 3-class (depth 1/2/3, n=15000)

| 分类器 | Accuracy | 95% CI |
|--------|----------|--------|
| LR | 65.07% | [63.37%, 66.73%] |
| **RF** | **69.47%** | [67.70%, 71.07%] |

Pairwise AUC (RF): d1v2=0.8392, d1v3=0.9726, d2v3=0.7596

#### 3-class filtered (去除代码, depth 1/2/3, n=14885)

| 分类器 | Accuracy | 95% CI |
|--------|----------|--------|
| LR | 64.53% | [62.81%, 66.41%] |
| **RF** | **68.36%** | [66.78%, 70.10%] |

Pairwise AUC (RF): d1v2=0.8314, d1v3=0.9753, d2v3=0.7760

#### Feature importance (top 5, RF)

| Feature | Importance |
|---------|-----------|
| p90_ppl | 0.2408 |
| p75_ppl | 0.1349 |
| mean_surprisal | 0.1103 |
| var_surprisal | 0.0964 |
| p50_ppl | 0.0441 |

#### Code contamination

| Depth | Broad | Narrow |
|-------|-------|--------|
| 0 | 0.5% | 0.4% |
| 1 | 0.9% | 0.7% |
| 2 | 0.8% | 1.6% |
| 3 | 0.6% | 1.4% |

极低，不影响分类结果。

---

### 3. 对比: GPT-2 XL 三种解码策略

| Metric | nucleus | temp0.9 | **topk50** |
|--------|---------|---------|------------|
| 4-class RF | **83.3%** | **85.4%** | 74.5% |
| 3-class RF | — | 82.0% | 69.5% |
| 3-class filtered RF | — | 81.5% | 68.4% |

topk50 比 nucleus/temp0.9 低 ~9-11 pp。Top-k=50 的固定词表截断产生的退化信号弱于 nucleus 和温度采样，depth 区分难度更高。不过 74.5% 仍远超 chance (25%)，3-class filtered 68.4% 也远超 chance (33.3%)，信号依然 robust。

---
