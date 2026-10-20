# audit figures compile compliance

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_figures_compile_compliance_20260524T045159_result.json`
- **Structured JSON:** [`9cda431419b0367bb3c0.json`](../../sessions/9c/9cda431419b0367bb3c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here is the full audit report:

---

## Part 1: Figures

| Figure | 脚本 | 数据源 | 状态 |
|--------|------|--------|------|
| fig1_method_framework.pdf | `figures/paper/gen_fig1_framework.py` | 纯示意图，无实验数据 | ✅ |
| fig1_dose_response.pdf | **无脚本** | 未找到生成脚本 | ⚠️ 可能由 PaperBanana 或交互式生成 |
| fig2_reward_trajectories.pdf | `artifacts/figures/gen_fig2_reward_trajectories.py` | Hardcoded，来源注释 W&B runs (li451oi4, tyv20u2k, hwucjf2n) + server logs | ✅ 与 table 一致 |
| fig3_collapse_dynamics.pdf | `artifacts/figures/gen_fig3_collapse_dynamics.py` | Hardcoded，与 fig2 共享 reward/frac_zero 数据，加 grad_norm/kl | ✅ 与 fig2 一致 |
| fig_sft_grpo_scatter.pdf | `figures/paper/gen_fig_sft_grpo_scatter.py` | Hardcoded accuracy（CKA 63.91/64.39, Std 59.29/59.84 等） | ✅ 与 tab2/tab3/tab4 一致 |
| fig4_cka_heatmap.pdf | `figures/paper/gen_fig4_cka_heatmap.py` | **⚠️ 合成数据**：`np.random.seed(42)` + `gen_layers()` 从 summary stats (mean/min/max) 近似生成 per-layer 值。脚本注释: "true per-layer data is on remote server; this approximates the pattern" | ⚠️ 非真实逐层数据 |
| fig5_extended_training.pdf | `figures/paper/gen_fig5_extended_training.py` | Steps 10-100 来自 W&B (tyv20u2k, li451oi4)；110-300 来自 extended registry experiments | ✅ |
| fig_appendix_kl.pdf | `figures/paper/gen_fig_appendix_kl.py` | KL 数据与 fig3 脚本一致 | ✅ |

**关键问题**:
- **fig4_cka_heatmap**: per-layer CKA 柱状图使用的是从 summary statistics 合成的近似数据（`gen_layers(mean, lo, hi)`），不是真实实验值。Summary stats 本身 (μ=0.62/0.90/0.92/0.88) 来自实验，但逐层分布是人工生成的。论文 caption 和正文引用了这些 μ 值（正确），但柱状图的逐层形状是近似的。
- **fig1_dose_response**: 无生成脚本，数据源不可追溯。

## Part 2: LaTeX 编译

✅ 编译成功，0 errors, 0 undefined references, 0 multiply-defined labels

| 类型 | 数量 | 严重性 |
|------|------|--------|
| Overfull hbox | 3 (max 3.07pt) | 可忽略 |
| Underfull hbox | 28 | 正常 |
| Float specifier `h`→`ht` | 5 | 良性 |
| Hyperref token warnings | 3 | 良性 |

**页数**: 15 页总计
- 正文 (§1-§5 + Conclusion): **8 页** ✅ (EMNLP 2026 限制 = 8 页)
- Limitations + Ethics: 第 9 页开始（不计入页数限制）
- References: 第 9 页起
- Appendix: 第 10-15 页

## Part 3: 匿名仓库

⚠️ **本地未找到匿名仓库 git 目录**。ROADMAP 记录状态: "匿名仓库 ✅（65 files, c9a2a2b）"——仓库可能托管在外部匿名服务（如 Anonymous GitHub），本地无法验证当前 commit 状态和未提交更改。

## Part 4: 跨位置一致性

✅ **引用完整性通过**
- 65 个 labels 定义，44 个显式引用
- 0 undefined references
- 0 duplicate labels
- 所有 Figure/Table/Equation 引用均正确解析
- 147 个数值在 figure 脚本和 table tex 文件间验证一致

**次要问题**:
- `eq:cka` (HSIC/CKA 定义) 已定义但未被 `\ref{}` 引用（minor）
- `introduction.tex` 使用 `../figures/paper/` 路径，其余文件用 `figures/paper/`（编译正常但风格不一致）

---

**需关注**:
1. **fig4 合成数据** 是最值得关注的问题——如果 reviewer 要求 raw data，当前脚本无法复现真实逐层分布。建议在提交前从服务器拉取真实 per-layer CKA 数据替换合成值。
2. **fig1_dose_response** 缺少生成脚本，可复现性不明。
3. **匿名仓库** 无法本地验证——建议在提交前确认外部仓库 URL 可访问且代码最新。

---
