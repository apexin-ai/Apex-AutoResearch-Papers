---
loop: 2
reason: idle_timeout
updated: '2026-05-25T16:01:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- Fig 8b Jaccard 矩阵必须用 `artifacts/bootstrap_jaccard_ci.json` 作为唯一权威数据源，不可手动编造值（本 session 刚修正了 9/10 个错误值）
- 论文主文本严格 ≤ 8 页（当前 Conclusion 恰好在 P8 底部结束，任何图表尺寸/文本调整都需重新验证页数）
- 图表生成脚本 `/tmp/upgrade_all_figures_v4.py` 是当前 truth source，修改任何图时必须在此脚本上改（不要从 v3 或更早版本 fork）
- Google API Key `AIzaSyBIXR...` 额度已耗尽，PaperBanana 目前不可用

### 2. 🖥️ 基础设施快照
- 本地工作目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/`
- 论文源码：`docs/paper/`（main.tex + sections/*.tex）
- 图表输出：`docs/paper/figures/`（6 张 PDF+PNG）
- 统计数据：`artifacts/figures/paper/` + `full_study/analysis/full_statistics.json`
- Jaccard 权威数据：`artifacts/bootstrap_jaccard_ci.json`
- PaperBanana venv：`/tmp/pb_venv`（可用但 API key 已耗尽）
- 图表脚本：`/tmp/upgrade_all_figures_v4.py`
- PB 参考图：`/tmp/run_20260524_214406_a9e4f5/final_output.png`（折线图）、`/tmp/run_20260524_213546_253d9e/final_output.png`（热力图）
- 无活跃 GPU / Worker / Cron

### 3. 📊 当前状态
刚完成 Director 的 3 轮图表升级指令：
1. PaperBanana 3-reference 方案（2 张 PB + 手动补充 forest plot）→ 提取统一 style_config → v4 脚本生成全部 6 张图
2. Fig 8b Jaccard 矩阵紧急数据修正（9/10 个值从权威 JSON 更正）+ permissive attractor 四舍五入修正
3. 编译通过，P4-P8 PDF 渲染验证通过，主文本 8 页

Registry 无 RUNNING/PREPARING 实验。无等待中的 Worker/Cron/Director 决策。

### 4. 📋 待办
- Director 若要求进一步图表调整 → 修改 `/tmp/upgrade_all_figures_v4.py` 对应函数，只重新生成受影响的图（`python3 -c "from upgrade_all_figures_v4 import gen_xxx; gen_xxx()"`)
- Director 若要求 PaperBanana 重新生成 → 需先获取新的 Google API Key
- 提交前 → 需要完整的 reference-audit（bib 条目验证）和 paper-visual-review（全页渲染检查）

### 5. 🎯 战略上下文
- 论文核心结论：policy ambiguity causally induces safety violations in LLM agents（首个因果证据），convergent nocuity 推翻经典 agreement-based monitoring，clause-level auditing 优于 type-level screening（22.4% vs 0.4% variance）
- 图表设计体系基于 PaperBanana 参考提取的 style_config：层级色 #C0392B(spec) / #2C3E50(ling)，热力图 cream 间隙 + 9-stop 暖红 colormap，serif 字体，1.8pt 线宽
- 易踩坑：(1) Jaccard 值不要凭记忆写，必须从 bootstrap_jaccard_ci.json 读取 (2) 修改任何图的尺寸后必须重新编译检查 8 页限制——当前 margin 极小 (3) 层级色已从 v3 的 vermillion/steel-blue 改为 PB 的 academic-red/navy，不要回退
