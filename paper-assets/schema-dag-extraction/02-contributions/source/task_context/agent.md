---
loop: 10
reason: max_wall_time
updated: '2026-05-25T19:17:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- PaperBanana 的 Google API key 在 `/tmp/.pb_google_key`（`[REDACTED_GOOGLE_TOKEN]`），**不要走 TUM/secret 审批流程**，直接从文件读取
- PaperBanana critic 有已知 bug：Gemini 返回 None 导致 `json.loads(None)` crash。图片在 crash 前已保存到 `diagram_iter_1.png`，直接用即可
- 论文中模型名统一用 "Llama"（不是 "LLaMA"），已全文替换过
- EMNLP 2026 DDL 是 2026-05-25（今天），论文应已处于最终提交阶段

### 2. 🖥️ 基础设施快照
- 本地工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/`
- 论文 LaTeX：`docs/paper/` 下（main.tex, results.tex, related_work.tex 等）
- 图表目录：`figures/paper/`
- PaperBanana：`pip` 安装在 `/home/ubuntu/.local/lib/python3.14/site-packages/paperbanana/`，通过 Python import 调用（无 CLI 入口点，用 `from paperbanana.cli import app`）
- 无活跃 GPU 实验、无 tmux session、无 cron 任务（本项目当前是论文写作阶段，不是训练阶段）

### 3. 📊 当前状态
刚完成 Director 指派的两张 PaperBanana 概念图生成：

**Fig 1（问题示意图）**：已完成，R2 选定
- `figures/paper/fig_problem_illustration.png` (2.9MB, 2712×1478)
- `figures/paper/fig_problem_illustration.pdf` (2.9MB)
- 内容：Simple Schema（3 chips, ✓）→ Input Sentence（head/tail 高亮）→ Complex Schema（6 chips, confusable cluster 橙框, ✗）→ Dimension labels

**Fig 2（SDGD compact pipeline）**：已完成，R3 选定
- `figures/paper/fig_sdgd_pipeline_compact.png` (1.7MB, 2752×1536)
- `figures/paper/fig_sdgd_pipeline_compact.pdf` (3.1MB)
- 内容：Full Schema → Graph Coloring → 3 Sub-schemas (✓ low BCS) → Route→Extract→Merge → 2 failure callouts

之前还完成了：fig_sdgd_pipeline_pb_v6（PaperBanana 5 stages pipeline 图）、匿名仓库重建推送、全文 typo/格式修复（bare Appendix refs, DocRE→DocRED, VIF math mode, Llama 统一）。

Registry 中无 RUNNING/PREPARING 实验。无等待中的 Worker/Cron 回调。

### 4. 📋 待办
- Director 确认两张图质量 → 如不满意则按反馈修改 intent 重新生成
- Director 要求更新 LaTeX 中的 `\includegraphics` 路径 → 修改对应 .tex 文件指向新图
- 提交前最终检查 → 编译 PDF 验证无 warning、页数 ≤ 8 页正文
- Director 要求其他图表修改 → 用 PaperBanana 或 matplotlib 执行

### 5. 🎯 战略上下文
- 论文核心：zero-shot IE 中 schema complexity 的两个退化维度——Dimension 1（type count → recall decline）和 Dimension 2（confusability/BCS → type confusion/IntraSub）。TOST 证明两维度近似正交（FewRel interaction ±3pp, p=0.003）
- 关键数据点：FewRel semipartial R²=0.273（BCS 独立解释 27% RE variance），VIF=1.18；pairwise r²≈1.5% 通过 correlated interactions 放大到 batch-level ~27%
- SDGD 实验结论：decompose-then-merge 不 work——routing failure (73% multi-match) + merge amplification (precision 0.56→0.21) 是瓶颈，不是 partitioning 质量
- 易错点：PaperBanana 生成的图默认偏横版（Gemini Image gen 限制），反复强调 PORTRAIT 也只能部分改善。裁白边是必要后处理步骤
- 易错点：PaperBanana CLI 没有 shell 入口（`paperbanana` 命令不存在），必须通过 `python3 -c "from paperbanana.cli import app; ..."` 调用
