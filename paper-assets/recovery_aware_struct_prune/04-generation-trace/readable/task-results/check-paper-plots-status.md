# check paper plots status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_paper_plots_status_20260516T200930_result.json`
- **Structured JSON:** [`4efa69b48d60a704a41b.json`](../../sessions/4e/4efa69b48d60a704a41b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是汇总报告：

---

## Plot Generation 状态报告

### 论文需要的图表（writing_plan.yaml）

| Fig ID | 类型 | 描述 |
|--------|------|------|
| fig1_framework | conceptual | RASP framework + diagnostic methodology |
| fig2_reward_accuracy | statistical | Reward-Accuracy Decoupling (reward curves + bar chart) |
| fig3_collapse_dynamics | statistical | 2×2 subplot: reward, frac_zero_std, grad_norm, terminated_length |
| fig4_cka_analysis | statistical | Per-layer CKA overlap + pruning decisions comparison |

### 已完成的 Plots

| 文件 | 位置 | 对应 Claim |
|------|------|-----------|
| `fig1_framework.pdf` | artifacts/_project/chart/ | Method overview (Intro/Method) |
| `fig2_reward_accuracy.pdf` | artifacts/_project/chart/ | **Claim 1** — reward-accuracy decoupling |
| `fig3_collapse_dynamics.pdf` | artifacts/_project/chart/ | **Claim 2** — collapse severity gradient |
| `cka_per_layer_overlap.pdf` | remote: results/figures/ | Claim 3 支撑材料 |
| `cka_heatmap.pdf` | remote: results/figures/ | Claim 3 支撑材料 |

### 缺失的 Plots

| Fig ID | 状态 | 需要什么 |
|--------|------|----------|
| **fig4_cka_analysis** | ❌ 未生成（本地 artifacts 无） | 需要合并远程的 `cka_per_layer_overlap.pdf` + pruning decision logs 制作对比图（(a) per-layer bar chart + (b) RASP vs Standard 结构选择对比）|

### 结论

- **3/4 figures 已完成**（fig1, fig2, fig3 均在 artifacts/_project/chart/ 下）
- **fig4_cka_analysis 缺失** — 原始 CKA 数据已在远程服务器（`cka_per_layer_overlap.pdf`, `cka_heatmap.pdf`），但需要制作论文级合成图（per-layer overlap bar chart + pruning decisions comparison）
- **可立即生成 fig4**：所有需要的数据（CKA overlap values + pruning logs）已存在于 20% sparsity 实验，无需等待额外实验
- **不依赖任何待完成实验**：25% sparsity 和 Qwen Math 是 scope expansion，不影响当前 4 个核心 figures

---
