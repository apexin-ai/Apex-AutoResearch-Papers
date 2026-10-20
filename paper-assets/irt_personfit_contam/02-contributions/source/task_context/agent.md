---
loop: 2
reason: idle_timeout
updated: '2026-05-25T14:16:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验在跑，无分配 GPU，不要擅自启动训练
- 论文 main text 必须≤8 页（EMNLP 2026），Limitations/References 不计入；当前正好 8 页，**任何内容增加都必须同时删等量内容**
- `tab:frontier` 表定义在未被 `main.tex` 包含的 `background.tex` 中，Discussion 已改为文字引用——不要恢复 `\ref{tab:frontier}`
- Figure 生成脚本在 `figures/paper/` 目录，但 GRPO 脚本在 `paper/paper/scripts/gen_fig_grpo.py`——两个位置都会输出到 `figures/paper/`，修改时注意找对文件
- 论文文件有 3 个镜像目录，改 `.tex` 后必须同步：`paper/paper/sections/` → `paper/sections/` + `paper/paper/paper/sections/`

### 2. 🖥️ 基础设施快照
- 无远程服务器在用，全部在本地操作
- 工作目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/`
- LaTeX 编译目录：`paper/paper/`（`pdflatex main.tex`）
- graphicspath：`../figures/paper/`（相对于 `paper/paper/`）
- 色板模块：`figures/paper/palette.py`（NPG 色板：QWEN=#3C5488, LLAMA=#E64B35, MISTRAL=#00A087, ARCC=#8491B4）
- Paper Banana venv：`/tmp/pb_venv/`，GOOGLE_API_KEY=[REDACTED]
- PB 参考输出：`figures/paper/pb_ref/`
- 活跃进程：无。无 cron，无 Worker

### 3. 📊 当前状态
刚完成 v3 最终改版，已注册 artifact `art_20260524_e5a4ad`，已向 Director 汇报。

**完成的工作**：
- 4 个统计图全部迭代改进（Figure 1: Llama 颜色修正+注释优化；heatmap: 缺失单元格斜线阴影；GRPO: 箭头加粗+图例去边框；leaderboard: 树状图加粗+右边距）
- `Table ??` 引用修复（`tab:frontier` → 文字描述）
- Conclusion 缩短 1 行解决 P9 溢出
- 所有文件同步到 3 个目录镜像
- 最终 PDF：16 页，0 undefined refs

**等待中**：Director 对 v3 的反馈（可能还有一轮修改）

### 4. 📋 待办
- Director 反馈"图表还需改" → 继续迭代，PB 参考图在 `pb_ref/` 可用作设计灵感
- Director 说"可以提交" → 最终检查 abstract ≤200 words、Limitations 格式、检查 `\citep` vs `\citet` 一致性
- Director 要求新增内容 → 必须同时删等量内容保持 8 页
- 用户要求 visual review → 用 `pdf2image`（需 `pip install pdf2image`）渲染各页检查

### 5. 🎯 战略上下文
- 这是 EMNLP 2026 ARR 投稿，DDL 明天 AoE（2026-05-25/26）
- 核心 story：IRT person-fit statistics (ℓz*) 用于 LLM benchmark contamination detection 的行为边界刻画（θ-shift absorption / detection-diagnosis tradeoff / non-monotonic dose-response）
- 论文定位不是提出新检测方法，而是量化 IRT 理论预测的现象边界——这个 framing 容易被误解为"提出新 detector"，不要在描述中偏离
- 用户已第三次打回图表质量，对视觉要求极高——任何图表修改都需要实际渲染 PNG 后 Read 检查，不要盲改
- Llama 在 panel (d) dose-response 中应该用 palette.LLAMA (红色)，之前错用了 palette.MISTRAL (teal)——已修复，但如果重写脚本要注意
