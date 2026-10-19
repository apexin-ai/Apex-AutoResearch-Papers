# paper figure fig1 dag taxonomy

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig1_dag_taxonomy_20260520T150728_result.json`
- **Structured JSON:** [`007815236a4a0fef842e.json`](../../sessions/00/007815236a4a0fef842e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 1 生成完毕。

**输出文件：**
- PDF: `figures/paper/fig1_dag_taxonomy.pdf` (38 KB, 矢量)
- PNG: `figures/paper/fig1_dag_taxonomy.png` (322 KB, 3135×1601 @ 300 DPI)

**6 个 DAG 面板：**
- **(a) Confounding** — A(latent)→X, A→Y, X→Y, A⇢A* | subtitle: *Attenuation (toward OVB)*
- **(b) Exposure** — A→Y, A⇢A* | 红色边框突出 | subtitle: *Sign reversal (83.4%)*
- **(c) Mediation** — X→A→Y + X→Y(curved direct), A⇢A* | subtitle: *Amplification*
- **(d) Collider** — X→A←Y, A⇢A*(boxed=conditioned) | subtitle: *Attenuation (τ_sf = 0)*
- **(e) M-bias** — U₁/U₂(latent), M-structure, A⇢A* | subtitle: *Immune*
- **(f) IV** — A→X→Y, U→X/Y(confounding), A⇢A* | subtitle: *Fragile*

生成脚本保留在 `figures/paper/gen_fig1.py`，需要微调节点位置可直接修改坐标重跑。

---
