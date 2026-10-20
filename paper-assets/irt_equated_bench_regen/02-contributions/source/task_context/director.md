---
loop: 2
reason: max_messages
updated: '2026-05-25T06:10:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目是纯分析型论文（无训练），不涉及 GPU 实验或远程服务器
- 论文目标 EMNLP 2026 via ARR，主文严格 8 页限制，Limitations 不计入
- Abstract ≤ 200 words（当前 ~140 词，刚优化过数字密度）
- 所有改动直接在本地 paper/ 目录，无远程同步需求
- 审稿阶段已激活（review_chat_id 存在），论文修改需注意与审稿团队同步

### 2. 🖥️ 基础设施快照
- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`
- 论文目录：`paper/`，编译命令 `latexmk -pdf -interaction=nonstopmode main.tex`
- 无远程服务器、无 GPU、无训练进程、无 cron 任务
- 论文产出物在 `artifacts/`，figures 在 `figures/paper/`
- 活跃进程：无

### 3. 📊 当前状态
本轮处理了三位用户的论文修改请求，全部完成未 commit：

**曹晓玉**：
- Page 8 §5.1 文字超页码水平线 → 删除 `\enlargethispage` + `\addtolength{\textheight}` 高度 hack，压缩 Discussion + Conclusion 文本

**周俊伟**：
- Related Work 从 4 段压到 3 段（Psychometric Methods / Contamination Detection / Benchmark Quality）
- 正文加图：从附录提了 ICC 示意图 + matching 图到正文（downstream 图因 page 9 溢出移回附录）

**用户（论文自检）**：
- 缩写定义检查：修复 17 处未展开缩写（LLM/MMLU/IRT/ETS/DEFF/2PL/LOFO/AUC/AUROC 等）
- Abstract 数字密度优化：从 11 个统计量降到 5 个
- 图表分布均匀化：ICC 图移到 Method（p5），rho degradation figure* 前移到 p7，缓解 p8 三图拥挤

**当前论文状态**：
- 主文 5 图 2 表，分布在 p2/p5/p6/p7/p8
- Conclusion 在 p8，Limitations 从 p8 右栏开始
- 编译通过，无 broken references，总 17 页

registry: 无 RUNNING/PREPARING 实验。无等待回调。

### 4. 📋 待办
- 用户下次要求 commit → git add 所有 paper/sections/*.tex 变更（不要 add paper/main.pdf 等编译产物）
- 收到审稿报告 → 按 review-report-action skill 处理，先读 review_issues.yaml
- 用户要求重新审稿 → 调 `submit_paper_to_review`
- 用户问进度 → 所有请求已完成，等待用户确认或新指令

### 5. 🎯 战略上下文
- 项目核心发现：MMLU 31% items 有 temporal DIF，但 aggregate rankings 稳定（ρ≈0.997）；DIF 与 web-overlap contamination labels 近独立（Jaccard=0.206）；base/instruct 模型 DIF 方向相反
- 三个贡献：(1) temporal DIF at scale (2) cross-subject matching with ΔFPR=0 (3) Monitor/Triage/Correct audit protocol
- 易错点：page 8 极其紧张，任何文字增加都可能把 Conclusion 挤到 page 9。改 Discussion/Conclusion 时必须先编译验证页面布局
- 易错点：figure* 环境（rho degradation）浮动到"定义位置的下一页顶部"，移动其 tex 定义位置会改变它出现的页码
- 所有改动未 commit，用户未要求 commit
