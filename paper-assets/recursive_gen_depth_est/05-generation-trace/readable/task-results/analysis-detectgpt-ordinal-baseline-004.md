# analysis detectgpt ordinal baseline 004

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_detectgpt_ordinal_baseline_004_20260519T180227_result.json`
- **Structured JSON:** [`8753f73975c1a30d0f53.json`](../../sessions/87/8753f73975c1a30d0f53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认：原始脚本 `detectgpt_baseline.py` 只有 8 个 cells（不含 `pythia_nucleus`），v2 脚本添加了 `pythia_nucleus` 但从未运行。实验 004 未执行。

以下是基于现有数据的完整分析：

---

## DetectGPT Ordinal Baseline 分析

### 状态：pythia_nucleus cell 未运行 (8/9 完成)

实验 `detectgpt_ordinal_baseline_004` **从未执行**——无日志、无 registry 记录、无 `pythia_nucleus_scores.npz`。原始脚本 v1 只包含 8 cells，v2 脚本添加了 pythia_nucleus 但未被触发。

### 已完成 8/9 cells 的 4-class accuracy

| Cell | methodA (equal-width) | methodB (CORAL) | methodC (threshold) |
|------|----------------------|-----------------|---------------------|
| gpt2xl_nucleus | 28.5% | 25.0% | **40.1%** |
| gpt2xl_temp09 | 28.0% | 29.6% | **41.4%** |
| gpt2xl_topk50 | 31.1% | 26.5% | **36.9%** |
| olmo_nucleus | 25.9% | 24.9% | 30.9% |
| olmo_temp09 | 25.4% | 25.3% | 29.8% |
| olmo_topk50 | 25.3% | 25.5% | 24.3% |
| pythia_temp09 | 32.5% | **33.2%** | 21.8% |
| pythia_topk50 | 31.8% | **33.7%** | 20.2% |

**Chance = 25.0%**

### Calibration 方法对比

- **methodA (equal-width binning)**: 平均 28.6%，最稳定但信号弱
- **methodB (CORAL ordinal regression)**: 平均 28.0%，pythia cells 略好(~33%)，其他接近 chance
- **methodC (threshold ROC optimization)**: 平均 30.7%，gpt2xl cells 偏高(36-41%)但 pythia cells 反而 below chance(~21%)，方差最大，不稳定

methodC 在 gpt2xl 上的偏高数值是 threshold 过拟合的假象（5-fold CV 小样本），pythia cells 上 below chance 证实了这一点。

### Summary（8/9 cells）

- **Mean 4-class accuracy**: **29.1%** (chance 25%)
- **Mean d1-d3 balanced accuracy**: 30.2%
- Scoring model: GPT-2 Large; Perturbation model: T5-Large

### 与 Min-K% baseline (33.2%) 对比

| Baseline | 4-class Accuracy |
|----------|-----------------|
| Random chance | 25.0% |
| **DetectGPT (8/9 cells)** | **29.1%** |
| Min-K% Prob | 33.2% |

DetectGPT 比 Min-K% **低 4.1 个百分点**，两者都接近 chance level。DetectGPT 的 perturbation discrepancy 信号对 ordinal depth estimation 基本无效。

### Conclusion: Hypothesis 部分验证 (pending 1 cell)

**Near-chance 结论成立**（在已完成的 8/9 cells 上）。DetectGPT perturbation discrepancy 无法区分 4-class recursive generation depth，表现甚至不如 Min-K%。

但 **pythia_nucleus cell 未运行**，9/9 覆盖未完成。需要运行 v2 脚本（或仅对 pythia_nucleus 单独运行）以完成最后一个 cell。鉴于同模型系列的 pythia_temp09 (28.5%-33.2%) 和 pythia_topk50 (20.2%-33.7%) 均为 near-chance，pythia_nucleus 极大概率也是 near-chance，不会改变 overall conclusion。

**下一步**：是否需要我立即运行 pythia_nucleus cell 以完成 9/9 覆盖？

---
