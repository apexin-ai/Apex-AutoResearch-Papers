# CosineSim Baseline 验证 + 分布分析报告

**日期**: 2026-05-14
**服务器**: autodl-5090 (gpu-5090-2x-2)
**数据集**: conf≥2 子集, 15,401 windows (train=10,634, val=2,943, test=1,824)

## 1. 修复后结果验证

| 指标 | 值 |
|------|------|
| **Test Macro-F1** | **0.5606** ✓ 确认 |
| Accuracy | 0.5674 |
| Precision (macro) | 0.6248 |
| Recall (macro) | 0.6521 |
| F1 (stagnation) | 0.5059 |
| F1 (progress) | 0.6153 |

最优 threshold（val 搜索）: **0.6100**, invert=True（即 cosine sim < 0.61 → progress）

## 2. Cosine Similarity 分布统计

### Window-level 平均相邻步余弦相似度

| 集合 | 类别 | N | Mean | Std | Min | Max |
|------|------|------|------|------|------|------|
| Test | Progress | 1,339 | 0.6133 | 0.0892 | 0.2893 | 0.8496 |
| Test | Stagnation | 485 | 0.6923 | 0.1317 | 0.1245 | 0.9419 |
| Test | Overall | 1,824 | 0.6343 | 0.1080 | 0.1245 | 0.9419 |

**类间分离度**: |mean_diff| = 0.0790, Cohen's d = 0.70

### Step-level 余弦相似度

| 类别 | N | Mean | Std | Median |
|------|------|------|------|------|
| Progress | 11,688 | 0.6147 | 0.1660 | 0.6250 |
| Stagnation | 4,174 | 0.6931 | 0.1425 | 0.7168 |

### 直方图（Test set）

```
Bin Range            | Progress | Stagnation
[0.11, 0.16)         |        0 |          8
[0.16, 0.20)         |        0 |          2
[0.28, 0.32)         |        2 |          3
[0.32, 0.37)         |        7 |          3
[0.37, 0.41)         |       22 |          4
[0.41, 0.45)         |       24 |          6
[0.45, 0.49)         |       53 |          9
[0.49, 0.53)         |      125 |          8
[0.53, 0.58)         |      182 |         15
[0.58, 0.62)         |      279 |         25    ← progress 峰值区域
[0.62, 0.66)         |      235 |         43
[0.66, 0.70)         |      187 |         31
[0.70, 0.74)         |      124 |        186    ← stagnation 峰值区域
[0.74, 0.78)         |       72 |         69
[0.78, 0.83)         |       24 |         25
[0.83, 0.87)         |        3 |         30
[0.87, 0.91)         |        0 |         13
[0.91, 0.95)         |        0 |          5
```

## 3. Threshold-F1 曲线（关键数据点）

| Threshold | Macro-F1 | Precision | Recall | F1(stag) | F1(prog) |
|-----------|----------|-----------|--------|----------|----------|
| 0.45 | 0.4625 | 0.5288 | 0.5063 | 0.0919 | 0.8332 |
| 0.50 | 0.4540 | 0.4629 | 0.4834 | 0.1059 | 0.8021 |
| 0.55 | 0.4274 | 0.4218 | 0.4377 | 0.1172 | 0.7376 |
| 0.60 | 0.3768 | 0.3893 | 0.3700 | 0.1411 | 0.6126 |
| 0.65 | 0.2864 | 0.3316 | 0.2861 | 0.1515 | 0.4214 |
| 0.70 | 0.2073 | 0.2640 | 0.2451 | 0.1786 | 0.2360 |

注：上表为 non-inverted（score ≥ threshold → progress）。实际最优策略是 **inverted**（score < threshold → progress），因为 stagnation 的 cosine sim 更高。

Oracle best on test（含 invert）: threshold=0.70, invert=True, **macro-F1=0.7439**

## 4. 分析：为什么 CosineSim 表现较差？

1. **分布重叠严重**：两类的 cosine sim 分布有大量重叠区间（0.50-0.75），虽然 Cohen's d=0.70 表示中等效应量，但单一 threshold 无法有效分割。

2. **反直觉方向**：Stagnation 的平均 cosine sim（0.692）**高于** progress（0.613）。这合理——停滞时 agent 重复类似操作，embedding 变化小（相似度高）；progress 时探索新方向，embedding 变化大（相似度低）。

3. **信息瓶颈**：将整个 window 的 embedding 序列压缩为单一标量（平均相邻步 cosine sim），丢失了大量信息——变化的时序模式、突变 vs 渐变、方向信息等。GRU probe 能利用完整序列，因此优势明显。

4. **Val/Test 分布漂移**：Val 上 separation 仅 0.014，Test 上为 0.079。Val 选出的 threshold 0.61 不是 test 上的最优点（oracle=0.70），说明 threshold 迁移不稳定。

5. **类别不平衡**：Test set 中 progress:stagnation = 1339:485 ≈ 2.76:1，单一 threshold 方法难以同时兼顾两类 F1。
