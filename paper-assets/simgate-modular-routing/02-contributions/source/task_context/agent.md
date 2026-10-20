---
loop: 22
reason: max_wall_time
updated: '2026-05-25T19:15:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- **停止 PaperBanana 重试**：Director 明确指令不再派 PaperBanana worker（连续 4 次未达预期，DDL 当天不再投入）
- **当前 pipeline_overview.pdf 保持现状**：使用 PaperBanana v3（May 25 17:49 时间戳的版本，v4 R1 三阶段详细版），Director 确认可正常提交
- **匿名仓库已 force-push**：`github.com/anonymous-nlp-2026/simgate-modular-routing`，commit `eb5ff90`，不要再往里推未经匿名检查的内容
- **fig1_daf_scatter 的 r 值是 0.9698**（不是旧版 0.9945），这是从实际数据 linregress 计算的正确值，PB 标杆图显示 0.9945 是因为 PB 用了虚构数据
- **EMNLP 2026 严格 8 页主文限制**：Limitations 不计入但不能塞过多内容

### 2. 🖥️ 基础设施快照
- **本机 EC2**：所有图表生成、论文编译、PaperBanana 均在本机运行（ap-northeast-1 东京）
- **论文目录**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/`
- **图表脚本**：`docs/paper/figures/gen_*.py`（8 个脚本），共享样式 `paper_style.py`（PB 校准版）
- **paper_style.py 校准参数**：背景 #FAFAFA、CI_ALPHA=0.10、REGRESSION_LW=1.0、MARKER_EDGE_WIDTH=0.8、shadow offset(0.5,-0.5)/α0.12
- **编译方式**：`cd docs/paper && rm -f main.aux main.fls main.fdb_latexmk && pdflatex -interaction=nonstopmode main.tex`
- **GOOGLE_API_KEY**：`[REDACTED_GOOGLE_TOKEN]`（已通过 request_secret 审批，但 PaperBanana 已停用）
- **无活跃 GPU 任务、无 cron、无运行中 Worker**

### 3. 📊 当前状态
本 session 全部围绕论文图表美学升级和 DDL 前提交准备：

**已完成**：
- Paper Banana 校准流程（fig1 scatter 标杆 → 提取设计参数 → 更新 paper_style.py → 应用到全部 7 张统计图）
- Figure 3 (fig1_daf_scatter)：图例移至 upper left、outlier 标注加粗(lw=1.5)、菱形 s=60
- Figure 4 (death_action_timeline)：y-axis 标签缩短、figsize 加宽至 3.4"
- Figure 1 (pipeline_overview)：经历 v1→v4 共 4 个大版本约 15+ 轮 PaperBanana 迭代，最终版是 v4 R1（三阶段详细版，含 example panel + decision tree + DAF bar）
- 匿名仓库同步：`eb5ff90` force-push，清理 crafter_pilot/ + scripts/minihack/ + framework_draft.md，修复 2 处匿名泄露

**registry 状态**：无 RUNNING/PREPARING 实验（本 session 纯图表工作）

**等待中**：无 Worker/Cron 回调

### 4. 📋 待办（条件触发式）
- Director 说"提交论文" → 确认 main.pdf 编译无 warning、页数 ≤ 8 主文、匿名仓库最新
- Director 说"更新匿名仓库" → 重新同步 docs/paper/ 到 /tmp/anon-repo-work/paper/，匿名检查后 force-push
- 用户对 Figure 1 仍不满意 → **不要再派 PaperBanana worker**（Director 红线），可建议手动 matplotlib 或用户自己用 Figma/Illustrator
- Director 要求编译最终 PDF → `cd docs/paper && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`（完整引用需三轮）
- 新实验结果到达 → 按 on-experiment-done skill 处理，但 paper 相关数字修改需确认 registry 后再改

### 5. 🎯 战略上下文
- **项目核心结论**：ScienceWorld 中 internal strategy 的 routing signal 78.9% 来自 death avoidance（DAF），不是 reasoning 能力差异。这个发现是论文的核心 claim。
- **论文状态**：EMNLP 2026 ARR 提交，DDL 就是今天（2026-05-25）。22 pages 总计，主文 8 页内。
- **Worker 回调 status 不可信**：系统多次将 subtype=success 的 Worker 回调报告为 status=failed。必须检查 Worker 日志中的 `"type":"result"` 条目确认实际状态。
- **PaperBanana 的局限**：Gemini Imagen 无法精确控制输出尺寸（始终 2752×1536）；critic agent 有 JSON 解析 bug 会 crash；生成的图数据不准确（仅作美学参考）。这些是已知问题，不要再花时间排查。
- **paper_style.py 是 truth source**：所有统计图通过它保持视觉一致性。修改任何图时先检查是否引用了 paper_style 的常量。
