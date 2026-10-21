# analysis phase space trajectory viz

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase_space_trajectory_viz_20260521T053520_result.json`
- **Structured JSON:** [`be0c5aca7de9e098479b.json`](../../sessions/be/be0c5aca7de9e098479b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifacts registered. Here's the summary and paper snippet:

---

## 结果

14 个 α 值 (0.00–1.00) 的 phase-space 轨迹已绘制完成，覆盖 gen 0→10。

**关键发现：**
- **α_c ≈ 0.30** 处存在清晰的 phase boundary：α≤0.25 的轨迹 entropy 保持在 ~3.0（几乎不移动），而 α≥0.30 的轨迹 gen 0→1 就跳降到 ~2.5
- 三个不同 regime：stable (α≤0.25), moderate collapse (α=0.30–0.50), deep collapse (α≥0.55)
- α=1.00 trajectory 最极端：entropy 从 3.23 崩溃到 1.23（L2 距离 = 2.01）
- Sync dip 区域 (α=0.55–0.65) 的轨迹在 entropy 维度比 α=0.30–0.50 更深，但 distinct_1 终点反而略高（与 sync dip 现象一致）

**产出文件：**
- `artifacts/phase_space/fig_trajectory.pdf` (图)
- `artifacts/phase_space/trajectory_data.json` (数据)
- `artifacts/phase_space/plot_trajectory.py` (绘图脚本)

---

## 论文 Snippet

> **Phase-space trajectories.** Figure~\ref{fig:phase-space} projects the iterative collapse dynamics onto a two-dimensional phase space defined by token entropy and lexical diversity (Distinct-1). Each trajectory traces a single experiment from generation 0 (the original model) through generation 10 under a fixed synthetic data fraction $\alpha$. Three distinct regimes emerge. For $\alpha \leq 0.25$, trajectories remain tightly clustered in the high-entropy, high-diversity region of the phase space, indicating that the model distribution is effectively stable under iterative retraining. A sharp bifurcation occurs at $\alpha_c \approx 0.30$: trajectories with $\alpha \geq 0.30$ undergo an abrupt entropy drop of $\Delta H \approx 0.7$ within a single generation, after which they drift slowly rightward (partial entropy recovery) while diversity continues to decline monotonically. For $\alpha \in [0.55, 0.65]$—the sync dip region identified in our dose-response analysis—trajectories penetrate even deeper into low-entropy territory ($H \approx 2.1$--$2.3$), yet their terminal Distinct-1 values are marginally higher than those of the moderate-collapse regime ($\alpha = 0.30$--$0.50$), consistent with the non-monotonic diversity signature of the sync dip.
>
> This phase-space view yields a falsifiable prediction: any untested $\alpha$ value between 0.25 and 0.30 should exhibit a generation-1 entropy that falls within the gap region ($H \in [2.5, 3.0]$), marking it as a transitional trajectory between the stable and collapsing basins of attraction. Similarly, $\alpha$ values in the interval $(0.50, 0.55)$ should show intermediate behavior between the moderate-collapse and sync-dip regimes, with terminal entropy between 2.35 and 2.50.

---
