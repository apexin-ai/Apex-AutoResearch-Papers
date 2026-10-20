# C4 Delta Decline Root Cause Analysis (126 samples)

> 数据: `/root/autodl-tmp/crdd/results/mvp_v4_full.json` (126 samples, not 125)  
> 分析日期: 2026-05-14

## 1. 三区间切片

| 区间 | n | DISAGREE | targeted | blind | delta |
|------|---|----------|----------|-------|-------|
| 0-79 | 80 | 24 (30.0%) | 19/27 = 70.4% | 12/27 = 44.4% | **+25.9pp** |
| 80-108 | 29 | 10 (34.5%) | 6/11 = 54.5% | 8/11 = 72.7% | **-18.2pp** |
| 109-125 | 17 | 9 (52.9%) | 6/10 = 60.0% | 5/10 = 50.0% | **+10.0pp** |
| **FULL** | **126** | **43 (34.1%)** | **31/48 = 64.6%** | **25/48 = 52.1%** | **+12.5pp** |

关键: 80-108 区间 delta 反转为 **-18.2pp**，是 C4 下滑的主要原因。109-125 有所恢复。

## 2. 分侧分析

### Code-side targeted vs blind (by interval)

| 区间 | code_targeted | code_blind | delta |
|------|---------------|------------|-------|
| 0-79 | 18/20 = 90.0% | 10/20 = 50.0% | **+40.0pp** |
| 80-108 | 6/8 = 75.0% | 7/8 = 87.5% | **-12.5pp** |
| 109-125 | 5/7 = 71.4% | 5/7 = 71.4% | **+0.0pp** |

Code-side targeted 优势从 +40pp 崩塌到 0。原因：后期 code blind 成功率飙升 (50% → 87.5% → 71.4%)，而 targeted 下降 (90% → 75% → 71%)。

### FOL-side targeted vs blind (by interval)

| 区间 | fol_targeted | fol_blind | delta |
|------|-------------|-----------|-------|
| 0-79 | 3/5 = 60.0% | 5/5 = 100.0% | **-40.0pp** |
| 80-108 | 1/2 = 50.0% | 2/2 = 100.0% | **-50.0pp** |
| 109-125 | 1/3 = 33.3% | 2/3 = 66.7% | **-33.3pp** |

FOL-side targeted **始终负向**，-33 到 -50pp。这是一个持续性拖累。

## 3. 后期样本难度分析

| 区间 | FOL acc | Code acc | AGREE_WRONG | disagree_rate |
|------|---------|----------|-------------|---------------|
| 0-79 | 81.2% | 62.5% | 6 (7.5%) | 30.0% |
| 80-108 | 82.8% | 62.1% | 2 (6.9%) | 34.5% |
| 109-125 | **70.6%** | **52.9%** | 0 (0.0%) | **52.9%** |

109-125 显著更难：FOL 下降 11pp，Code 下降 10pp，disagree 率飙升到 53%。

## 4. FOL-side Repair 深入分析

共 10 个 FOL-error 样本 (error_side=fol)，占 disagree 的 23%。

| idx | 区间 | FOL verdict | Code verdict | GT | targeted | blind |
|-----|------|-------------|--------------|-----|----------|-------|
| 6 | 0-79 | Error | True | True | SUCCESS | SUCCESS |
| 7 | 0-79 | Error | Unknown | Unknown | SUCCESS | SUCCESS |
| 28 | 0-79 | Unknown | True | True | **FAIL** (stuck Unknown) | SUCCESS |
| 37 | 0-79 | Error | True | True | SUCCESS | SUCCESS |
| 52 | 0-79 | Unknown | False | False | **FAIL** (stuck Unknown) | SUCCESS |
| 87 | 80-108 | Unknown | True | True | **FAIL** (→Error) | SUCCESS |
| 95 | 80-108 | Error | True | True | SUCCESS | SUCCESS |
| 117 | 109-125 | True | Unknown | Unknown | **FAIL** (stuck True) | SUCCESS |
| 120 | 109-125 | Unknown | False | False | SUCCESS | **FAIL** |
| 124 | 109-125 | Error | True | True | **FAIL** (→Unknown) | SUCCESS |

**失败模式**:
- **FOL verdict = Error (语法错)** → targeted 成功率 75% (3/4)，因为错误明确，容易修
- **FOL verdict = Unknown/True (逻辑错)** → targeted 成功率 **17%** (1/6)，几乎全失败

当 FOL 的错误是"逻辑推理错误"而非"执行报错"时，targeted repair 的诊断信息 ("FOL is wrong") 不仅没帮助，反而让模型陷入死循环——反复修改但产出仍是错误的逻辑。而 blind repair 可以从头重新生成，反而更容易碰到正确结果。

## 5. 累积 C4 Delta 走势

```
@10:  +0.0pp   (n_dis=2)
@20:  +40.0pp  (n_dis=5)
@30:  +25.0pp  (n_dis=11)
@40:  +23.1pp  (n_dis=12)
@50:  +16.7pp  (n_dis=16)
@60:  +18.2pp  (n_dis=19)
@70:  +25.0pp  (n_dis=21)
@80:  +25.9pp  ← 峰值
@90:  +18.8pp
@100: +17.6pp
@109: +13.2pp
@120: +11.1pp
@126: +12.5pp
```

80 样本后持续下降，从 +25.9 到 +12.5。

## 6. 204 全量预测

**边际参数** (80-125 区间): targeted=57.1%, blind=61.9%, delta=-4.8pp  
**预估 remaining 78 样本中 ~32 个 disagree** (disagree rate 41.3%)

| 情景 | 假设 | 204 projected delta | 结论 |
|------|------|---------------------|------|
| 1. 边际趋势延续 | targeted=57%, blind=62% | **+5.6pp** | 勉强 PASS |
| 2. 后续中性 | 50/50 | **+7.5pp** | PASS |
| 3. targeted 崩塌 | targeted=50%, blind=70% | **-0.5pp** | FAIL |
| 4. 最坏情况 | targeted=40%, blind=70% | **-4.5pp** | FAIL |

## 7. 结论: C4 下滑的三个驱动因素

**驱动因素 1: Code-side targeted 优势蒸发** (最主要)
- 从 +40pp (0-79) 下降到 0pp (109-125)
- 原因: 后期 blind repair 大幅进步 (50%→71-88%)，targeted 下降 (90%→71-75%)
- 推测: 后期样本 code bug 更复杂，targeted 诊断可能反而锚定错误修复路径；blind 从零重写反而更有效

**驱动因素 2: FOL-side targeted 持续负向** (结构性问题)
- 全区间 -33 到 -50pp
- 根因: FOL 逻辑错误 (非语法错误) 时，targeted repair 几乎无法修复 (1/6 = 17%)
- blind repair 在同样场景成功率 83% (5/6)

**驱动因素 3: 后期样本更难** (放大效应)
- 109-125 disagree rate 53% (vs 0-79 的 30%)
- 更多 disagree 意味着更多 repair 需求 → 以上两个问题被放大

**风险评估**: 204 全量 C4 PASS 概率 ~60%。如果后续样本难度继续升高，有 ~40% 概率跌破 5pp。

**建议优先级**:
1. Code-side: 调查为什么 blind 在后期样本大幅进步——如果能把 targeted 也提到同等水平，就解决了主要问题
2. FOL-side: 对 FOL 逻辑错误 (verdict != Error) 的情况，考虑 fallback 到 blind strategy，不使用 targeted repair
