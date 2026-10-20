# analyze adaptive fix seed456 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_adaptive_fix_seed456_seed42_20260514T210225_result.json`
- **Structured JSON:** [`80c63056abf1326694b9.json`](../../sessions/80/80c63056abf1326694b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验分析完成，registry 已更新。汇总：

## 结果对比

| 实验 | eval PPL | vs uniform | vs adaptive(原版) | 结论 |
|------|----------|------------|-------------------|------|
| **adaptive_fix_seed456** | **17.66** | 17.70 → 17.66 (-0.04) | 17.64 → 17.66 (+0.02) | success |
| **adaptive_fix_seed42** | **17.65** | 17.69 → 17.65 (-0.04) | 17.69 → 17.65 (-0.04) | success |
| adaptive_fix_seed123 (参考) | 17.64 | — | — | success |

**关键发现：**
- **seed42 有改善**：原版 adaptive 与 uniform 持平(17.69)，fix 版降至 17.65，改善 0.04 PPL
- **seed456 基本持平**：fix 版 17.66 vs 原版 17.64，略微退步 0.02，但仍优于 uniform(17.70)
- 三个 seed 的 fix 版 PPL 非常一致：17.64, 17.65, 17.66

## b* 分布对比

| 统计量 | seed456 | seed42 | seed123(参考) |
|--------|---------|--------|---------------|
| mean | 0.843 | 0.714 | 0.723 |
| median | 0.44 | 0.069 | 0.0 |
| std | 1.687 | 1.547 | 1.613 |
| <0.5 | 52.8% | 59.7% | 59.9% |
| 0.5-1.0 | 21.3% | 18.2% | 18.0% |

seed42/seed123 的 b* 分布高度一致，seed456 的 b* 略高（median 0.44 vs ~0）。

---
