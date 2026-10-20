# paper method section

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_method-section_20260515T233110_result.json`
- **Structured JSON:** [`1ecdc0fe76b407c6b556.json`](../../sessions/1e/1ecdc0fe76b407c6b556.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `paper/method.tex` 并注册为 artifact `art_20260515_3f5a58`。

**内容结构**（4 subsections，目标 2.5 页）：

- **3.1 Problem Setup** — 语料 D、检测器 q(x)、权重公式 w=(1-q)^b（共享自 Drayson）、加权损失方程、b 自适应推导的动机
- **3.2 Dual-Constraint Framework** — α_eff 和 ESS 定义（含 proxy 说明）、Proposition 1（单调性，条件期望形式的证明 sketch）、质量下界 b_τ + 稳定上界 b_ESS、分段定义的 b*（Eq.8）、三种 regime + 实证统计（引用 §5）
- **3.3 Algorithm** — Algorithm 1（bisection solver，algorithmic 环境）、loss reweighting vs SIR 实现、O(B log(b_max/ε)) 复杂度
- **3.4 Hyperparameters** — τ（理论 motivation + [0.5,0.8] safe range + 非对称敏感性）、n_min（boundary behavior + default=2）、与 fixed b 的对比

**相对于两个先前版本的改进**：
- 统一使用 main.tex 宏（`\bstar`, `\aeff`, `\btau`, `\bess`, `\nmin`）
- 证明使用更严谨的条件期望分解形式
- 算法伪代码与 `algorithmic` 包兼容（大写命令）
- 引用 key 按 writing_plan 规范（`drayson_2025_detection_collapse` 等）
- 所有定量 claim 引用 §5

---
