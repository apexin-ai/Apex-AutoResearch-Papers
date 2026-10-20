---
loop: 10
reason: max_messages
updated: '2026-05-22T21:49:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文中存在两套 trace：r11_canonical (SC=39.33% Mistral PW，用于 SICA pipeline/Table 1) vs seed42 (SC=39.17%，用于 combo eval/Table 3/multi-NLI/DRC)。**绝对不能混用**——之前 Agent 曾试图用 r11_canonical 的数据修改 seed42 表格，被拒绝
- D061 alphabetical tiebreaking 是全局约束：所有 SC/combo tiebreaking 使用 `sorted(["True","False","Unknown"])[0]` → 选 "False"。任何新实验/新数据必须遵守
- diagnosis.tex 不被 main.tex 编译（不在 \input 中），修改它只为一致性，不影响 PDF
- EMNLP 2026 ARR：8 页正文硬限，Limitations 不计入页数但要简短（3 点左右）

### 2. 🖥️ 基础设施快照
- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/`
- 编译入口：`main.tex`，pdflatex，输出 `main.pdf`（27 页：8 正文 + 19 appendix）
- Figure 脚本：`docs/paper/figures/gen_*.py`，本地 python3 + matplotlib 执行
- 项目知识文件：`projects/symb_invariant_consensus/` 下 ROADMAP.md / paper_framing.md / experiment_plan.yaml / report.md / decisions.yaml
- 无活跃 GPU 实验。多 seed 实验（LLaMA 磁盘满失败、Qwen2.5 PW 和 Mistral PW 在跑）不阻塞提交

### 3. 📊 当前状态
刚完成 D061 全面数据统一审计并提交 Round 15 审稿（`apr_20260522T214813_v5rr`，推荐 continue 模式）。

修正清单（全部已完成）：
- Oracle Δ：14.22→13.73pp（8 个 .tex 文件）
- SC：75.49→75.98（Qwen2.5-14B FOLIO）
- BR：3.93→3.85（analysis/appendix/diagnosis，6 处）
- Qwen3 FOLIO SC：84.80→83.33（appendix footnote）、~84→86.27（appendix kappa table）
- capability_gap_scatter：gap -35.29→-33.82，PDF 已重新生成（21:45）
- f6_kappa_accuracy_scatter：Qwen-14B 75.49→75.98，PDF 已重新生成（21:31）

等待：Round 15 审稿报告回传

### 4. 📋 待办
- Round 15 审稿报告回传 → Read `skills/global/review-report-action.skill.md` → Holistic Pass + Per-Comment Action Matrix → 派 Agent/Paper Agent 修复
- 多 seed 实验完成回调 → 分析结果，如果显著则更新 Table 1 的 multi-seed 行
- LLaMA 多 seed 磁盘满 → 需要清理磁盘或换服务器后重跑（非阻塞）
- 审稿报告若数据一致性全 pass → 进入最终提交准备（ARR checklist、Limitations 检查）

### 5. 🎯 战略上下文
- **核心贡献**：negative result paper——SICA 自提取约束继承 SCB，formal verification 是 symbolic mirage；cross-architecture NLI escape 是唯一正面出路
- **目标**：EMNLP 2026 ARR，从 Round 14 的 3.5（Borderline Conference）提到 4.0（Conference）
- **DDL**：2026-05-25（3 天后）
- **决策链关键节点**：D061 alphabetical tiebreaking 统一 → D151 combo eval 全部用 D061 → D152 论文全表统一 → 本轮 BR 3.93→3.85 最终修正
- **易错点**：(1) 不要把 r11_canonical 和 seed42 的数据搞混——Table 1 用 r11_canonical，Table 3/multi-NLI/DRC 用 seed42；(2) abstract 中 "8+/7−, p=1.00" 是 16 个 non-degenerate conditions 的 sign test，不是 18 个总 conditions；(3) conclusion 中 cross-arch claim 已从 "SC≈70% (p≤0.004)" 改为 "weakest generator zero-shot + domain adaptation extends to 72%"——因为 LLaMA zero-shot D061 后 p=0.665 不显著
