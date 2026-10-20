# research constat survey

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_constat_survey_20260521T211244_result.json`
- **Structured JSON:** [`b12f3d90d2da64c35205.json`](../../sessions/b1/b12f3d90d2da64c35205.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已收集完整。注意论文实际标题是 "ConStat: **Performance-Based** Contamination Detection in Large Language Models"，而非 "Statistical Detection and Quantification"——后者可能是项目 ROADMAP 中的简称。

### ConStat

- **官方 Repo**: [github.com/eth-sri/ConStat](https://github.com/eth-sri/ConStat) — Apache-2.0, 6 stars, 低活跃度 (4 commits)，ETH Zurich SRI Lab 出品
- **论文**: [NeurIPS 2024 Poster](https://neurips.cc/virtual/2024/poster/96266)，作者 Jasper Dekoninck, Mark Müller, Martin Vechev
- **核心定义**: Contamination = 不泛化的虚高性能（而非训练集包含 benchmark 样本）

**接口设计**:
```python
from constat.detection import ConStat

cs = ConStat(
    n_bootstrap=1000,          # bootstrap 迭代次数
    random_performance=(0.25, 0.25),  # 随机猜测的正确率（如4选1=0.25）
    p_value_delta=0,           # p-value 阈值偏移
)

result = cs.test(
    scores_model,              # shape (n_samples,) — 待测模型在原始 benchmark 上的 per-item 0/1 得分
    scores_model_ref_data,     # shape (n_ref_samples,) — 待测模型在 reference benchmark 上的 per-item 得分
    scores_ref_models,         # shape (n_ref_models, n_samples) — 参考模型群在原始 benchmark 上的得分
    scores_ref_models_ref_data # shape (n_ref_models, n_ref_samples) — 参考模型群在 reference benchmark 上的得分
)
```

**输出 dict**:
| 字段 | 含义 |
|------|------|
| `p_value` | 污染的统计显著性 |
| `estimated_contamination` | 预测的无污染性能 |
| `delta` | 实际 vs 预测性能差（= 污染影响量） |
| `min_delta_095` | delta 的 95% 置信下界 |
| `estimated_contamination_025/975` | 置信区间 |

**数据需求**:
1. **Reference benchmark** — 与原始 benchmark 同分布但未被泄露的变体（重述/合成/同任务不同 benchmark），**这是最大依赖**
2. **Reference models** — 一组已知未污染（或代表"正常"性能曲线）的模型在两个 benchmark 上的 per-item 得分
3. 所有数据均为 numpy array，per-item binary scores

**适配难度**: **中等**
- ConStat 核心统计测试本身是轻量 Python 包，`pip install -e .` 即可
- **主要工作量在准备数据**：需要 (a) 构造 reference benchmark、(b) 收集一批 reference models 的 per-item evaluation 结果
- 它自带 lm-evaluation-harness fork 用于跑评测，但我们可以用自己的评测 pipeline，只要最终喂入 numpy 格式的 per-item scores 即可
- 不需要访问模型权重/logprobs——纯粹基于 accuracy，**黑盒方法**

**关键限制**:
- 需要 reference benchmark（构造成本高，且质量直接影响检测力）
- 需要多个 reference models 的评测结果（论文用了 ~20 个模型）
- 检测粒度是 per-model（判断整个模型是否污染），**不直接输出 per-item exposure level e_i**
- `delta` 是全局污染影响量，不是逐 item 的

**⚠️ 对 G-MFRM 的关键 gap**: G-MFRM 需要 **per-item e_i**（每道题的曝光程度），但 ConStat 输出的是 per-model 的全局污染检测。要获得 per-item 粒度，需要额外工程：
- 可利用 `return_functions_test()` 返回的 spline 拟合函数，对每个 item 计算其 observed vs expected 性能偏差作为 proxy e_i
- 或者对 item 子集做 leave-one-out 式的 ConStat 测试（计算量大）

**替代方案**:

| 方法 | 特点 | 可行性 |
|------|------|--------|
| **LogProber** | 基于 logprobs 的黑盒方法，检测对 question 的 familiarity，计算便宜，per-item 粒度天然支持 | 需要 logprob API 访问；无官方 GitHub repo 找到 |
| **Min-K% Prob** | 基于 token logprobs 分布尾部，per-item 检测 | 需要模型 logprobs |
| **CDD / PaCoST** | 配对置信度测试 | 类似 ConStat 思路，需要 reference data |
| **直接用 performance gap** | 原始 vs rephrased benchmark 的 per-item accuracy 差作为 e_i 的 proxy | 最简单，不依赖统计框架 |

**建议**: ConStat 的核心统计思想可用，但 per-item e_i 需要我们自己从 spline 拟合中推导。最简方案是直接用 item-level performance gap（original vs reference）作为 e_i proxy，ConStat 的 spline hardness correction 可作为更精确的校正层。

Sources:
- [ConStat GitHub](https://github.com/eth-sri/ConStat)
- [ConStat Paper (arXiv)](https://arxiv.org/abs/2405.16281)
- [ConStat Project Page](https://constat.ai/)
- [NeurIPS 2024 Poster](https://neurips.cc/virtual/2024/poster/96266)
- [LogProber Paper](https://arxiv.org/abs/2408.14352)

---
