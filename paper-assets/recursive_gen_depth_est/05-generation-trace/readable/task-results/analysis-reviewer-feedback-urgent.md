# analysis reviewer feedback urgent

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reviewer-feedback-urgent_20260514T140859_result.json`
- **Structured JSON:** [`8d491612294452593598.json`](../../sessions/8d/8d491612294452593598.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个任务全部完成。汇总产出：

```
=== 3-class 分类 (d1/d2/d3 only) ===
样本数: 15000 (train 12000 / test 3000)
Best model: RF
3-class accuracy: 70.8% [CI: 69.2%-72.5%] (chance: 33.3%)
MAE: 0.3203
Per-pair AUC: d1v2=0.8540, d1v3=0.9569, d2v3=0.7931

Confusion matrix:
            pred-1  pred-2  pred-3
  depth-1:    790     147      63
  depth-2:    114     607     279
  depth-3:     23     249     728

Per-class: d1=79.0%, d2=60.7%, d3=72.8%
LR baseline: 67.1%

=== 代码过滤标准对比 ===
窄标准 (registry):  d0=0.4%, d1=7.4%, d2=11.8%, d3=15.3%
宽标准 (控制实验): d0=0.5%, d1=17.8%, d2=22.4%, d3=27.4%
差异原因: 宽标准多 14 个 pattern（def, function, var, <div, <php, SQL 等），
每深度多捕获 ~10-12pp 样本。主要增量来自 import（非 java）、
function/var（JS）、def（Python）、SQL、<div/<php 等。

=== Stratified split 稳定性 ===
4-class acc (original): 78.2%
4-class acc (stratified): 78.1%
差异: -0.1pp → 稳定（原始 split 已近似均衡）

Per-class (stratified): d0=99.9%, d1=81.2%, d2=57.8%, d3=73.7%

=== filter_code.py ===
路径: scripts/filter_code.py
行数: 132
功能: 双标准代码过滤（narrow/broad），支持 stats/filter/compare 三种模式
```

关键发现：**去掉 depth-0 后 3-class acc=70.8%（chance 33.3%），仍然是 chance 的 2.1 倍，95% CI 下界 69.2% 远超随机。** d2 是最难分类的（60.7%），主要与 d3 混淆（279 个）。相邻深度 d2v3 AUC=0.7931 是最弱 pair，但仍显著高于 0.5。这证实递归深度信号在去除 depth-0 的"easy win"后依然存在。

---
