# research literature scan

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan_20260514T223612_result.json`
- **Structured JSON:** [`4a0fdf334bb5ca62613d.json`](../../sessions/4a/4a0fdf334bb5ca62613d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。增量扫描结果：

**新增 8 篇论文**（64 → 72），按相关性排序：

### Novelty 威胁评估

| # | 论文 | Venue | 类别 | 威胁 |
|---|------|-------|------|------|
| 1 | **TAWM** (Nhu et al.) — 显式 Δt conditioning world model | ICML 2025 | direct-competitor | **中** |
| 2 | **LS-Imagine** (Li et al.) — jumpy imagination for Dreamer | ICLR 2025 Oral | direct-competitor | 低 |
| 3 | **HWM** (Zhang, LeCun et al.) — 多尺度 latent WM 层级规划 | arXiv 2026 | direct-competitor | 低 |
| 4 | **MTS3** (Shaj et al.) — 多时间尺度 SSM | NeurIPS 2023 | method-component | 低 |
| 5 | MetaController (Kobayashi et al.) — 自回归模型中的时间抽象 | arXiv 2025 | method-component | 低 |
| 6 | SPlaTES — 技能层级稳定规划 | RLC 2025 | method-component | 低 |
| 7 | Multi-timestep MBRL (Becker-Ehmck) | arXiv 2023 | background | 低 |
| 8 | DMVE — 自适应 horizon 值估计 | IEEE TNNLS 2022 | background | 低 |

### 核心结论

**没有发现任何论文诊断 dt_embedding → delusional critic → stochastic collapse 这一机制。项目 novelty 安全。**

**TAWM 是最需要关注的论文**，但实际上**强化了我们的贡献**：TAWM 证明 Δt conditioning 在 MPC 范式下有效，而我们发现它在 imagination-based actor-critic 中导致病态 value overestimation——这个对比本身就是一个 surprising finding。

**领域趋势**：temporal abstraction in world models 正收敛到 **层级方法**（THICK, Hieros, Director, HWM, SPlaTES），回避 flat variable-dt 方案。我们的诊断论文提供了**为什么 flat dt 方案失败**的理论解释，为这个经验性趋势提供了根基。

### 论文必须动作
1. **必须引用** `nhu2025tawm`，在 Related Work 中区分 MPC vs imagination 范式
2. **应当引用** `li2025lsimagine`、`shaj2023mts3`
3. **考虑引用** `zhang2026hwm`

---
