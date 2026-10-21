# research dcr baseline eval

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_dcr_baseline_eval_20260522T004409_result.json`
- **Structured JSON:** [`d848d02458e026eb48c3.json`](../../sessions/d8/d848d02458e026eb48c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。以下是可行性报告。

---

## DCR Baseline 代码评估报告

### 1. 仓库状态

| 项目 | 值 |
|------|-----|
| URL | github.com/chengxuphd/dcr |
| License | Apache-2.0 |
| 论文 | EMNLP 2025 (Xu et al.) |
| Stars/Forks | 1/1 |
| 语言 | Python 100% |
| 依赖 | numpy, scipy, scikit-fuzzy, pandas（极轻量） |
| 代码量 | ~300 行核心代码（2 个核心文件 + 2 个工具文件） |
| 质量 | 代码清晰、结构规范、有类型标注、无外部 ML 框架依赖 |

### 2. 接口描述

**核心类**: `DCRCalculator`

**输入**（每个 model×benchmark 一行）：
```
bdc_level, model, test1(s1), test2(s2), test3(s3), test4(s4), accuracy
```
- `s1`–`s4`: 四层污染分数（Semantic / Information / Data / Label），范围 [0, 1]
- `accuracy`: 原始准确率（百分制）
- `bdc_level`: 污染注入级别（0=clean baseline, 1-4=递增污染）

**核心函数**：
```python
dcr = calculator.calculate_dcr(s1, s2, s3, s4)  # → float [0,1]
adj_acc = calculator.calculate_adjusted_accuracy(raw_acc, dcr)  # → raw_acc * (1 - dcr)
results = calculator.process_experiment_data(data)  # → dict with results, avg_error, correlation, p_value
```

**输出**：
- DCR Factor（0–1）：单个标量，表示 model×benchmark 的综合污染风险
- Adjusted Accuracy：`raw_acc × (1 - DCR)`
- 统计指标：average error, Pearson correlation, p-value

**不需要训练/拟合**：DCR 是基于模糊推理的确定性计算，无需 MCMC/SGD。给定四个分数即刻输出。

### 3. 与 G-MFRM pipeline 兼容性分析

**关键差异**：

| 维度 | G-MFRM 需要 | DCR 提供 |
|------|-------------|---------|
| 粒度 | per-item e_i | per-model×benchmark DCR Factor |
| 污染参数 | latent c_n（per-model susceptibility） | DCR Factor（与 c_n 概念不同） |
| 校正方式 | IRT 框架内联合估计 θ, b, d, c | 线性缩放 `acc × (1-DCR)` |
| Judge bias | 联合建模 d_j | 完全不涉及 |
| 输入来源 | 多 judge 评分矩阵 | 需外部计算的 4 层污染分数 |

**DCR 不能替代 e_i 估计**。DCR 的四个输入分数 (s1–s4) 本身就需要外部测量（论文中通过受控实验注入不同级别污染获得），且输出是 benchmark-level 聚合值，无法分解到 item-level。

**DCR 作为 exp-004 baseline #6 的角色**：它是 "contamination-only correction" 的代表，用于证明仅校正污染（不管 judge bias）不足以得到最优排名。在 exp-004 中，需要：
1. 用 exp-002 的数据为每个 model×benchmark 计算 s1–s4
2. 用 DCR 输出 adjusted accuracy → 模型排名
3. 与 Chatbot Arena 人类投票计算 Kendall-τ，对比 G-MFRM

### 4. 适配方案与工作量

**安装**：直接 `pip install -r requirements.txt`（4 个包，无 GPU 依赖），或直接把 `src/core/` 两个文件复制进项目。

**适配工作**（估计 0.5–1 天）：

1. **s1–s4 分数计算**（主要工作量）：DCR 假设这 4 个分数已知，但 G-MFRM 实验中需要从 exp-001/002 数据导出。需要写一个 adapter 将 exp-002 的 per-item exposure signals 聚合为 4 层分数。方案：
   - s3 (Data Level) ≈ mean(e_i) for benchmark items（performance gap 信号）
   - s4 (Label Level) ≈ LogProber/temporal 信号聚合
   - s1 (Semantic), s2 (Information) ≈ 需要额外定义映射逻辑

2. **评估 adapter**（~20 行）：拿 DCR adjusted accuracy 输出 → 计算模型排名 → 与 Arena 投票对比

3. **无需修改 DCR 源码**：`calculate_dcr(s1,s2,s3,s4)` 接口足够通用

**风险点**：s1–s4 映射方案的合理性。DCR 论文中这 4 个分数来自受控实验（BDC level 0–4），而 G-MFRM 实验中需要从观测数据估计。映射方式直接影响 DCR baseline 的公平性——过于粗糙的映射可能低估 DCR 效果，reviewer 可能质疑 baseline 不公平。

### 5. 结论

| 问题 | 回答 |
|------|------|
| 能否直接安装使用？ | **能**，极轻量，无 GPU 依赖 |
| 能否替代 e_i 估计？ | **不能**，粒度和框架不匹配 |
| 作为 baseline 是否合适？ | **合适**，正好代表 contamination-only correction |
| 适配工作量？ | **0.5–1 天**，主要在 s1–s4 映射逻辑 |
| 需要修改源码？ | **不需要** |
| 主要风险？ | s1–s4 映射方案的公平性，需要在论文中说明 |

---
