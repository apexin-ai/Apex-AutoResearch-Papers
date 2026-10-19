# analysis v6 early check

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v6-early-check_20260512T235455_result.json`
- **Structured JSON:** [`bad73db3d73d6be6fa6c.json`](../../sessions/ba/bad73db3d73d6be6fa6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## V6 ICL Divergence 分析报告

### 1. V6 当前进度

| GPU | Total | Success | Fail | SR |
|-----|-------|---------|------|----|
| cuda0 | 85 | 54 | 31 | 63.5% |
| cuda1 | 90 | 63 | 27 | 70.0% |
| **合计** | **175** | **117** | **58** | **66.9%** |

4 条 failure 无匹配 expert，实际分析 54 条。

### 2. Step-1 Divergence 率

| 指标 | v5 | v6 | 变化 |
|------|----|----|------|
| Step-1 diverge | 88.4% (222/251) | **74.1%** (40/54) | -14.3pp |
| Step≤2 diverge | 94.4% (237/251) | **81.5%** (44/54) | -12.9pp |

ICL 使 step-1 率下降 ~14pp，但仍有 3/4 的 failure 在第一步就偏离。

### 3. d 值分布

```
v5 (N=251):                         v6 (N=54):
[0.0-0.1): 229 (91.2%) ████████     [0.0-0.1):  43 (79.6%) ████████
[0.1-0.2):  13 ( 5.2%) █            [0.1-0.2):   3 ( 5.6%) █
[0.2-0.3):   6 ( 2.4%)              [0.2-0.3):   3 ( 5.6%) █
[0.3-0.4):   3 ( 1.2%)              [0.3-0.4):   0
[0.4-0.5):   0                      [0.4-0.5):   1 ( 1.9%)
[0.5-0.6):   0                      [0.5-0.6):   3 ( 5.6%) █
[0.6-0.7):   0                      [0.6-0.7):   1 ( 1.9%)
[0.7-1.0):   0                      [0.7-1.0):   0
```

v6 在 [0.4-0.7) 区间出现了 5 个 case，v5 完全为 0。

### 4. Early / Mid / Late 分组

| 分组 | v5 | v6 |
|------|----|----|
| Early (d<0.33) | 248 (98.8%) | 49 (90.7%) |
| Mid (0.33-0.66) | 3 (1.2%) | **5 (9.3%)** |
| Late (d≥0.66) | 0 (0.0%) | 0 (0.0%) |

Mid 比例从 1.2% 升至 9.3%，Late 仍为 0。

### 5. 按 Task Type 拆分

| task_type | SR | N_fail | step-1% | d_mean | early% | mid% |
|-----------|-----|--------|---------|--------|--------|------|
| pick_and_place | 90.2% | 4 | 75.0% | 0.071 | 100% | 0% |
| look_at_obj | 77.8% | 2 | 50.0% | 0.214 | 50% | 50% |
| pick_clean_then_place | 72.5% | 11 | 81.8% | 0.016 | 100% | 0% |
| pick_two_obj | 59.5% | 13 | 61.5% | 0.057 | 100% | 0% |
| pick_cool_then_place | 50.0% | 9 | 88.9% | 0.056 | 89% | 11% |
| pick_heat_then_place | 43.3% | 15 | 73.3% | **0.125** | 80% | **20%** |

- **pick_heat_then_place** 贡献了最多 mid-range divergence（3/5 mid cases），d_mean 最高
- **pick_two_obj** step-1 率最低 (61.5%)，但全部是 early
- Mid-range 集中在 heat/cool 任务——都是同一个错误模式：**跳过 close microwave/fridge 直接 put，没走 close→heat/cool→open 流程**

### 6. DPO 训练影响评估

**d 分布对 γ(d) 连续折扣的支撑力不足：**

- 仅 9.3% (5/54) 在 mid range，0% late，90.7% 压在 d<0.33
- d 值覆盖 6/10 个 bin，但 [0.3-0.4) 和 [0.7-1.0) 完全空缺
- Mid cases 几乎都是同一种错误（close appliance 步骤遗漏），不是真正的 diversity
- γ(d) 函数在实际训练中会退化为近似二值：绝大多数 γ≈0（early diverge，penalty 高），少数 γ≈0.5

**结论：** v6 ICL 相比 v5 有改善（step-1 率 -14pp，mid 比例 ×8），但 divergence 分布仍然严重偏早期。当前数据量下 γ(d) 连续折扣不如简单的 early/mid 二分类。如果要让 γ(d) 真正有效，需要进一步降低 early divergence 比例到 <60%，或者专门针对 mid/late failure 做数据增强。

---
