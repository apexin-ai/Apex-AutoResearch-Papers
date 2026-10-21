# ops plan006 confound fix check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan006-confound-fix-check_20260516T015055_result.json`
- **Structured JSON:** [`6f7567d4a1c6b260b95f.json`](../../sessions/6f/6f7567d4a1c6b260b95f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：成功完成

PID 256127 正常退出，日志末尾显示 "All phases complete."。GPU 全部释放（4×RTX 5090 均 0 MiB）。

## 关键 Metrics 对比

| 指标 | 旧值 (confound前) | 新值 (confound fix后) | 变化 |
|------|-------------------|----------------------|------|
| **Para 3-class F1** | 0.680 ± 0.009 | **0.727 ± 0.010** | **+0.047** |
| **Para binary F1** | 0.539 ± 0.017 | **0.613 ± 0.016** | **+0.074** |
| Cont 3-class F1 | 0.788 ± 0.006 | 0.788 ± 0.006 | 不变 |
| Cont binary F1 | 0.749 ± 0.011 | 0.749 ± 0.011 | 不变 |
| **3-class gap (para-cont)** | -0.108 | **-0.061** | **缩小43%** |
| Para retention (d4/d0) | 0.892 | 0.995 | +0.103 |
| Para 样本量 | 4754 | 9666 | ×2 |

## Confound 修复效果

最关键的变化在 Spearman 相关性——旧版 paraphrase 特征被 lexical diversity confound 严重污染：

| 特征 | 旧 para ρ | 新 para ρ | 说明 |
|------|----------|----------|------|
| ttr | **+0.567** | +0.027 | confound 消除 |
| hapax_ratio | **+0.556** | +0.012 | confound 消除 |
| entropy_mean | **+0.394** | -0.056 | confound 消除 |

## Cross-transfer（最亮眼的改进）

| 方向 | 旧值 | 新值 | 变化 |
|------|------|------|------|
| para→cont | **0.155** | **0.769** | **+0.614** |
| cont→para | 0.431 | 0.606 | +0.175 |

旧版 para 分类器在 cont 上 F1 仅 0.155（几乎随机），说明学到的是 confound 而非 depth signal。修复后 para→cont 达 0.769，证明分类器现在学到了跨模态可迁移的真实 depth 特征。

## 结论

Confound fix 成功。Paraphrase depth signal 确实存在且可迁移，但比 continuation 弱（F1 gap 0.061）。结论 "paraphrastic chains lose depth signal faster" 仍成立，但差距比之前认为的小得多。

---
