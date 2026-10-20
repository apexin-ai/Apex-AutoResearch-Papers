# reviewer / loop_4.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`c837fe1eb62bc07ae13d.json`](../../sessions/c8/c837fe1eb62bc07ae13d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-14T12:27:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-22162，项目 GPU 白名单见 `execution.gpu_ids`（之前 2026-04-24 有越界事故）。每次审查训练实验必查 CUDA_VISIBLE_DEVICES
- d_z 全文必须使用 bf16 canonical 值：DS 0.44/0.52/0.68/0.80，QW 0.28/0.55/0.89/1.02（决策 D048）。**绝对不能**用旧 registry 值（DS 0.61/0.73/0.95/1.13）
- Table 5 的 Δ̃/CI 取自 `rebootstrap_b10000_results.json`，figures 取自 `canonical_bf16_stats.json`——两套 bootstrap 种子不同。QW s015 CI 跨零判定不一致（rebootstrap 跨零→ns，canonical 不跨零），论文选保守方向（ns）。**不要把 canonical 数据当 table 数据用，反之亦然**
- Table 3 (cross-model) Qwen s020 Δ̃ = **0.23**（不是 0.24），来自 experiment_summary_table.json (0.234979)

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162 (root)，代码根 `/root/autodl-tmp/pacs`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/`
- 论文本地：`artifacts/_project/paper/`，远程：`/root/autodl-tmp/pacs/paper/`
- 关键数据文件（远程）：
  - `analysis_output/cohens_d_bf16.json` / `cohens_d_bf16_qwen.json`（d_z 权威源）
  - `analysis_output/rebootstrap_b10000_results.json`（Table 5 Δ̃/CI 源）
  - `paper_figures/canonical_bf16_stats.json`（figure 数据源）
  - `analysis_output/experiment_summary_table.json`（Table 1-3 源）
- 无活跃进程，无 cron，全部 76 实验 DONE

### 3. 📊 当前状态
论文处于 page-budget 裁剪阶段。当前状态：
- **本地**已完成裁剪：results.tex 200→155 行，discussion 103→67，analysis 95→62。新建 `appendix_results.tex` 和 `appendix_disc_analysis.tex`。main.tex 已更新含三个 appendix input
- **远程未同步裁剪版**：远程仍是未裁剪的 17 页版本（results 199 行，discussion 102 行）。远程缺 appendix_results.tex / appendix_disc_analysis.tex
- 最近编译的 PDF（19:47, 405KB）是未裁剪版，17 页
- Fig 1-5 均已在远程 paper/figures/ 就绪（fig4 19:43 重生成，fig5 20:13 重生成）
- 等待 Director 决策：全量同步裁剪版到远程 → 重编译 8 页版 PDF

### 4. 📋 待办
- Director 批准同步 → 审查同步后的远程 tex 完整性 + 重编译 PDF（检查 undefined refs、页数≤8）
- 8 页版 PDF 出来 → 做最终视觉审查（上次视觉审查看的是 17 页版）
- 若 Director 决定统一 rebootstrap vs canonical 数据源 → 重审 Table 5 与 figures 的一致性
- 收到任何新章节写作审查请求 → 按 §5 模板评分（Originality/Clarity/Soundness/Significance/Presentation + Overall）

### 5. 🎯 战略上下文
- 论文核心：compound sparsity severity 是 phase-strategy interaction，不是固定属性。6 个 claims (C1-C6)，C4 (entropy-discrimination collapse) 已降级为"partial cross-model support"
- 关键统计：两套 bootstrap 管线（rebootstrap 用于 table，canonical 用于 figures）是已知的、已记录的差异，不是 bug。最敏感的分歧点是 QW s015——保守标 ns
- **最容易判断错的事**：看到远程 tex 和本地 tex 行数不同就以为有 bug——实际是裁剪未同步。**先确认两边各自版本是否内部自洽，再判断谁对谁错**
- 远程 results.tex fig4 caption 写的是 "Forest plot of paired Cohen's $d_z$"（正确），但本地旧版本和 appendix_results.tex 写的是 "permutation test results"（未更新）。同步时需以远程 caption 为准
- page-budget-analysis worker 给出了详细的 8 页裁剪方案（P1-P9 优先级），可供参考但 Director 可能有不同策略


---
