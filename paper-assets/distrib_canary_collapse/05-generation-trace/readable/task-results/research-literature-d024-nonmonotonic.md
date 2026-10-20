# research literature d024 nonmonotonic

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_d024_nonmonotonic_20260515T052900_result.json`
- **Structured JSON:** [`759f08c63bfc7ef30b7e.json`](../../sessions/75/759f08c63bfc7ef30b7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。产出文件已写入 artifacts 目录。

---

## 结论

**文献空白确认：没有论文直接报告过 diversity collapse 与 synthetic ratio 的非单调 dose-response。** 这是 novel finding。

### 最相关的理论支撑

| 论文 | 关键发现 | 与我们的关系 |
|------|---------|-------------|
| [He et al. 2025](https://arxiv.org/abs/2502.18049) "Golden Ratio Weighting" | 最优 real data 权重收敛到 1/φ ≈ 0.618；**w\*(λ) 既非单调也非凸** | risk landscape 本身非单调 → α=0.25 可能处于 risk 局部最大值 |
| [Xu & Cheng 2025](https://arxiv.org/abs/2509.22341) "Optimal Mixing Ratios" | w > 1/3 时 variance 单调递减；**w < 1/3 时可能增长** — 存在临界阈值 | 1/3 临界阈值与 α=0.25 vs α=0.50 的行为差异概念对应 |
| [Chen et al. 2025](https://arxiv.org/abs/2510.05133) 已在 literature_map | 20% 以下稳定，30% 以上加速退化；**未测非单调性** | α=0.25 恰在其 danger zone 入口，但他们没扫 α=0.50 做对比 |

### 最可能的解释

**"最危险区间"假说**：α=0.25 处于"刚好够破坏分布尾部、但不足以让模型快速饱和进入 collapsed attractor"的区间。α=0.50 下模型可能快速饱和后 drift 趋缓，反而总 drift 更小。可通过逐 generation 轨迹形状区分（"快降后平台" vs "持续缓降"）。

### Paper framing 建议

这是可以作为独立 contribution 的发现。建议以 "Non-monotonic dose-response in diversity collapse" 作为 Results 的独立 subsection，引用 He 2025 的黄金比例理论作为理论锚点，但强调我们首次在 LLM diversity metrics 上展示此现象。验证需更细粒度 α sweep + 多 diversity metrics + 多 seeds。

### 已更新的文件

- `artifacts/d024_literature_notes.md` — 完整调研报告
- `artifacts/literature_map.yaml` — 新增 3 篇论文（he2025golden, xu2025overparametrization, gillman2024selfcorrecting）+ 1 条新 gap

---
