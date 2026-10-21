# analysis rcrit sensitivity

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rcrit-sensitivity_20260525T215401_result.json`
- **Structured JSON:** [`6f2f9a2c5194e939cc3e.json`](../../sessions/6f/6f2f9a2c5194e939cc3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

**核心结论：r_crit ∈ (0.25, 0.3] 在所有观测窗口 T=3,5,7,10 下完全一致。**

### 分类稳定性矩阵

| r | T=3 | T=5 | T=7 | T=10 | 稳定性 |
|---|-----|-----|-----|------|--------|
| 0.0 | III (尚未显现) | I | I | I | T≥5 后稳定 |
| 0.2 | II | II | II | II | ✓ 全T一致 |
| 0.25 | II | II | II | II | ✓ 全T一致 |
| 0.3 | III | III | III | III | ✓ 全T一致 |
| 0.5 | III | III | III | III | ✓ 全T一致 |

### r_crit(T) 估计

| T | r_crit 范围 |
|---|------------|
| 3 | (0.25, 0.3] |
| 5 | (0.25, 0.3] |
| 7 | (0.25, 0.3] |
| 10 | (0.25, 0.3] |

### 关键发现

1. **Type II/III 边界完全稳定**：r=0.25 的 transient dip (~4 SLV units) 在 T=3 时就已可观测，分类不随窗口变化。r=0.3 的 gen-1 波动 (<3 units) 始终低于 dip threshold，稳定分类为 Type III。

2. **唯一的窗口依赖**：r=0 在 T=3 时尚未显现 collapse（SLV 在 gen 2 仍处于峰值上升阶段），需要 T≥5 才能检测到 Type I。这是物理上合理的——collapse 需要时间展开。

3. **Seed 间一致性**：边界处（r=0.25 seed44 dip=2.1, r=0.3 seed43 dip=3.0）存在个别 seed 的分类差异，但 majority vote 下结论一致。

4. **对审稿人的回应**：r_crit 的估计不依赖观测窗口长度。即使只观察 3 代，Type II/III 的分界线就已经清晰。collapse 检测需要更长窗口是因为 collapse 本身需要时间展开，而非分类方法的缺陷。

---
