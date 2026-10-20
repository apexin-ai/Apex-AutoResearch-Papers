# diag d134 random s49 pr5 root cause

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_d134-random-s49-pr5-root-cause_20260518T224951_result.json`
- **Structured JSON:** [`af2b4397e633fc6bed76.json`](../../sessions/af/af2b4397e633fc6bed76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整报告：

---

## Random s49 PR=5% 诊断报告

### 1. 训练曲线对比

| 窗口 | s47 | s48 | s49 |
|------|-----|-----|-----|
| 1-50 | 0.110 | 0.098 | 0.095 |
| 51-100 | 0.217 | 0.275 | 0.210 |
| 101-150 | 0.463 | 0.180 | 0.215 |
| 151-200 | 0.685 | 0.517 | **0.260** |
| 201-250 | 0.787 | 0.745 | **0.325** |
| 251-300 | 0.790 | 0.800 | **0.455** |
| 301-350 | 0.767 | 0.757 | **0.555** |
| 351-400 | 0.810 | 0.840 | **0.605** |
| 401-450 | 0.805 | 0.818 | **0.610** |
| 451-500 | 0.853 | 0.825 | **0.675** |

s49 **全程系统性偏低**（最终窗口 0.675 vs 0.85/0.83），但没有崩溃，曲线持续上升。

### 2. 异常信号

- **无 NaN/inf/overflow/error**
- 配置正确：`mode=additive_random, logic=fol, steps=500, data=train_500_seed42.jsonl`
- 从 Qwen3-4B base model 训练，无 resume 问题
- 500/500 步正常完成

### 3. 根因：**重复生成退化 (Repetition Collapse)**

**关键证据：Eval avg_time_per_sample**

| seed | Random PR | avg_time | ISR PR | avg_time |
|------|-----------|----------|--------|----------|
| s47 | 89% | 6.3s | 97% | 0.8s |
| s48 | 93% | 3.0s | 66% | 3.9s |
| s49 | **5%** | **10.5s** | 86% | 1.1s |

s49 Random eval 几乎所有 sample 都 hit 10.9s 超时。查看 eval_results.json 中的 formalization 输出：

```
# 典型 s49 生成 (folio_765):
Premises:
1. ¬T(x)
2. W(x) → T(x)
3. W(x)
4. W(x) → L(x)
5. L(x) → A(x)
6-38. ¬L(x) ∨ ¬T(x)   ← 同一公式重复 33 次直到 max_length
39. ¬L(x)
```

模型生成 3-5 个有意义的前提后进入**无限重复循环**，填满输出 buffer。

**训练-评估差距机制**：
- 训练时 batch=8，短生成偶尔命中 H1 pattern（conclusion-in-premises），维持 ~67% PR
- Eval 时在 100 个未见问题上，重复退化策略几乎全部失败
- 5 个 proved 全部是 trivial：h1_strict=4, h7=1, **genuine=0**

### 4. Classify 对比

| | proved | h1_strict | h7 | h8 | genuine |
|---|--------|-----------|-----|-----|---------|
| Random s47 | 89 | 79 | 0 | 4 | 6 |
| Random s48 | 93 | 75 | 3 | 14 | 4 |
| Random s49 | **5** | 4 | 1 | 0 | **0** |

### 5. 结论判断：**A — 纯粹 seed 随机性导致的 mode collapse**

不是训练 bug。根因是 additive_random 模式下随机噪声 reward 信号不足以在所有 seed 下防止重复退化。

**关键佐证**：同一 seed 49 在 ISR 训练下得到 PR=86%（正常），说明问题不在 base model 初始化，而在 random reward 的训练信号质量。

### 6. 对论文的影响

**3-seed 统计**：
- Random: mean = 62.3%, std = 40.2% (被 s49 outlier 主导)
- ISR: mean = 83.0%, std = 12.9%

**选项**：
1. **逐 seed 报告**（推荐）：Table 里列出 s47/s48/s49 各自的 PR，透明展示 Random 的不稳定性
2. **将 s49 collapse 作为分析亮点**：Random reward 的内在不稳定性恰好是 ISR 优势的论据。Random 在 2/3 seed 下 PR≥89%，但 1/3 seed 完全崩溃。ISR 最低也有 66%，无 catastrophic failure
3. **补充更多 seed**：如果论文空间允许，跑 5-seed 可以让统计更可靠。但当前 3 seed 已经足以说明 variance 差异

s49 不是 bug 也不该被剔除——它是 random reward 不稳定性的**真实表现**。

---
