---
loop: 14
reason: idle_timeout
updated: '2026-05-25T14:02:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 训练任务，不涉及 GPU 设备号约束。所有实验已完成（176 条 registry 全部 DONE/killed，15 条 PREPARING 均有结论只是未转状态）
- 论文 tex 源在**本地** `projects/symb_invariant_consensus/docs/paper/`，不在远程服务器。审查"是否已改"前先读本地
- Abstract 硬限 200 words（EMNLP 2026），当前 193 words——任何编辑必须重新计数
- D061 决策：Mistral-7B PW SC = **39.33%** (236/600) 是 canonical。Registry exp-deberta-ft-combo notes 中 "39.33→39.17%" 是 D061 前的残留旧信息，**方向反了，不要采信**
- n=166 口径：memory.md 记录 Director 决策统一用 166/204 非全票问题。`minority_constraint_direction.json` 仍显示 n=148（未更新），但论文正确引用 166/204 和 ~73.5%

### 2. 🖥️ 基础设施快照
- 服务器：`westd-16639` + `westd-30973`，代码根目录 `/root/symb_invariant_consensus`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/`
- 论文 tex：`docs/paper/` 下（main.tex + 分文件）
- 关键数据文件：`artifacts/_project/data/` 下（fleiss_kappa_results.yaml, minority_constraint_direction.json, per_problem_cv_values.json 等）
- review issues tracker：`artifacts/review_issues.yaml`
- 最新审稿报告：`artifacts/review_reports/round_19.md`（= R22 fresh review, 3.5 Borderline Conference）
- 活跃进程：**无**。所有实验完成，无 RUNNING 任务

### 3. 📊 当前状态
Loop #14 完成了以下审查：

**已审通过的 Worker 产出：**
- SF2 Discussion PRM/ORM 段落 ✅（3 段 ~310 words，4 篇引用均在 bib 中确认）⚠️ 需重编译验证 8 页限制
- Fig 3 causal DAG v10 ✅（PaperBanana 生成，M→T→A→C→S 结构正确）
- Fig 2 regime scatter v2 ✅（κ x-axis，Qwen2.5-14B PW κ=0.62 是正确值）⚠️ **"Qwen3 PW" 标签指向错误数据点**（指向深蓝 Qwen2.5-14B PW 而非橙色 Qwen3-14B PW）
- Em-dash 清理 ✅（主体 tex 无 prose em-dash，appendix 表格 N/A 标记保留正确）
- experiments.tex 引用更新为 `f2_regime_scatter_v2` ✅

**已向 Director 提交的报告：**
1. 论文修改落地状态核查（MF1-3 + SF6 确认，Discussion 过短 + SC 值 + n=148/166 flagged）
2. Worker 产出逐项审查（Fig 3 v10 + 视觉布局改善 + Fig 2 v2 + em-dash + Discussion）
3. R22 Action Matrix 独立审查（ROI 排序 + 4 个判断请求回应）
4. 数据准确性核实（39.33% 正确 + Fig 2 "Qwen3 PW" 标签 bug 确认）

**等待中：**
- Director 对 R22 修复方案的最终决策（用户说"不再改"，但 3.5→4.0 有提分空间）
- Fig 2 v2 "Qwen3 PW" 标签修复 Worker
- Discussion 扩展后 8 页限制重编译验证

### 4. 📋 待办
- **Fig 2 标签修复 Worker 完成** → 检查 "Qwen3 PW" 标注是否改为指向正确的橙色点(κ≈0.78, Δ≈-0.17)，或已删除
- **重编译 main.pdf 后** → 用 pdf_to_images 检查 page 8：§7 Discussion 是否在 page 8 内结束（SF2 新增 ~200 words 有溢出风险）
- **Director 批准 N1 标题修改** → 审查新标题 + Abstract 修改，重新计数 words ≤ 200
- **Director 批准 N2 DAG 修正** → 审查 Fig 3 新结构是否改为 T→(A,C) 共同子代 + DPI 降为 empirical
- **Director 批准 N3 SCB reframing** → 审查 §5.1 修改是否诚实定位 SCB 为 "CoT bias 在 constraint extraction 中的具体化"
- **任何论文章节写作审查请求** → 必须先加载 `skills/global/paper-quality-lessons.skill.md`，按 §5.1 审查维度 + §7 论文写作审计
- **全文编译后** → 视觉审查关注：R22-VL1 page 30（已改善到 ~75% 填充）、VL2 page 8 密度、Fig 2 v2 渲染

### 5. 🎯 战略上下文
- **核心结论**：SICA 在零样本自提取下退化为多数投票。SCB 是 transparency property（source-attribution 忠实传递 CoT 分布），不是新 bias。跨架构 NLI verifier 是初步逃逸路径（exploratory, n=6）
- **R22 评分 3.5 Borderline Conference**。已向 Director 提交 ROI 排序：N1（标题/TOST）> 快修包 > N2（DAG）> N3（SCB reframing）。最小干预 ~2h 可到 ~3.75，完整修复 ~5.5h 可到 ~4.0
- **±2pp TOST margin 最强论证**：multi-seed SC variance SD=1.67-2.51pp，±2pp 在 SC baseline 噪声地板内。frame 为 practical significance 而非 post-hoc
- **N3 建议不做分离实验**：honest reframing 比强行分离更有力——SCB 是 CoT bias 的 constraint-extraction projection，结构性贡献在于识别 source-attribution 机制
- **易错点**：
  1. 不要采信 registry exp-deberta-ft-combo 的 "39.33→39.17" notes——D061 后 39.33% 才是 canonical
  2. `minority_constraint_direction.json` 显示 n=148 但论文用 166——这是 Director 决策统一的结果，数据文件未更新不是 bug
  3. tab:independence (appendix) 缺 Qwen3-14B 行——Fig 2 需要但论文表中未列出
  4. Cross-model SC Ablation 措辞约束：限定为 "NLI combo 不可完全归约为 ensemble diversity"，不要 overclaim
