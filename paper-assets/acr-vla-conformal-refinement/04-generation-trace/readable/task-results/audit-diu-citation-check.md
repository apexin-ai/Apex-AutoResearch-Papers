# audit diu citation check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_diu-citation-check_20260513T224545_result.json`
- **Structured JSON:** [`720ffc8325eacaafdddc.json`](../../sessions/72/720ffc8325eacaafdddc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## DiU 引用核查结果：**真实有效**

**bib 条目：**
```
@misc{xing2026diu,
    title={Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching},
    author={Jiarui Xing and Song Wang and Jian Wang},
    year={2026},
    eprint={2605.00941},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

**验证结果：**
- arXiv ID [2605.00941](https://arxiv.org/abs/2605.00941) **存在且匹配**
- 标题、作者、年份全部一致
- 2026年5月1日提交，作者来自 Yale School of Medicine、UCF、Harvard Medical School

**论文实际内容：**

DiU 证明了一个精确的解析恒等式：对于任意预训练的 flow matching 速度场，posterior covariance 的 trace 等于速度场的 divergence（乘以已知的时间依赖系数 + 常数项）。核心优势：
- **Post-hoc**：无需重训练、无需修改架构
- **Single-pass**：对于 one-step generators（如 MeanFlow），单次前向传播即可得到精确的生成不确定性
- 计算量比 ensemble/MC-Dropout 低约 10,000×
- MNIST 实验验证：per-pixel uncertainty maps 在数字边界处最高，与实际预测误差相关

**我们论文中的引用准确性：**
- "divergence of the velocity field recovers per-DOF aleatoric uncertainty from a single forward pass" — **基本准确**
- 需注意：原文是关于通用 flow matching 的理论结果（cs.LG），不是 robotics/VLA 专用方法，但技术上可应用于 flow-matching-based VLA

**结论：DiU 引用合法，无需修改。**

Sources:
- [DiU: Divergence is Uncertainty (arXiv:2605.00941)](https://arxiv.org/abs/2605.00941)
- [DiU HTML version](https://arxiv.org/html/2605.00941)

---
