# analysis d32 scaling law meta analysis

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d32_scaling_law_meta_analysis_20260520T165550_result.json`
- **Structured JSON:** [`81ef00f04b9e97d59266.json`](../../sessions/81/81ef00f04b9e97d59266.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。关键发现：

**Step 1 — Sigmoid 验证**: FDR-corrected 数据 refit 得到 α_c=0.467 vs 既有 0.476，差距在 bootstrap CI 内。但 k、α_c 的标准误巨大（step function 不可辨识），确认 dose-response 本质上是 α≈0.47 处的阶跃函数。

**Step 2 — S(N) 反推**: 7 个模型在 α=1.0 的 PermG detection rate 大部分聚集在 0.75（6/8），只有 Qwen2.5-0.8B 偏高（0.875）、Pythia-1.4B 偏低（0.50，seed 方差极大）、SmolLM3-3B 接近 0（架构不兼容）。

**Step 3 — Power law**: **S(N) 与模型大小无显著幂律关系**（β≈0, R²≈0）。跨架构变异主导了大小效应。Pythia family 内 β=0.08 但 R²=0.05，不可靠。

**Step 4 — 两个竞争模型**:
| | Model A (Probit-√T) | Model B (Linear-threshold) |
|---|---|---|
| α_c(T=10) | 0.465 | 0.467 |
| α_c(T=20) | **0.465 (固定)** | **0.330** |
| 物理含义 | T 只改变转变陡度 | T 降低检测阈值 |

**关键可证伪检验**: α=0.40–0.45 在 T=20 的实验将区分两模型——Model B 预测可检测，Model A 预测不可检测。

输出文件:
- `artifacts/scaling_law/alpha_c_scaling.json`
- `artifacts/scaling_law/fig_s_vs_n.{pdf,png}`
- `artifacts/scaling_law/fig_alpha_c_vs_t.{pdf,png}`
- `artifacts/scaling_law/fig_alpha_c_heatmap.{pdf,png}`

---
