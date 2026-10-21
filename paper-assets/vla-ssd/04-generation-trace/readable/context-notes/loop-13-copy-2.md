# agent / loop_13.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`61ec7e03485882bc9250.json`](../../sessions/61/61ec7e03485882bc9250.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-25T22:18:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- experiments.tex ~line 176 "a first cross-architecture decomposition" — **"first" 绝对不能删**，Director 多次强调
- 正文必须 ≤ 8 页（References 从 p9 开始），每次改正文后必须编译 + pdftotext 验证
- Figure 3 数据必须用 demo-split MCCV（bootstrap v3），禁止用 random-split（R² 0.7-0.9 是假的）
- Rounding 已统一为四舍五入：2 位小数用 "0.16--0.46"，3 位小数用 "0.156--0.455"，不要引入 "0.15--0.45"
- Bonferroni 正确数字：40/45 originally significant tests survive (88.9%)，不是 48/63

### 2. 🖥️ 基础设施快照
- 本地工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/`
- 论文源码：`docs/paper/`（main.tex, experiments.tex, method.tex, discussion.tex, appendix.tex, introduction.tex）
- 编译：`cd docs/paper && latexmk -pdf -interaction=nonstopmode -g main.tex`
- Figures：`docs/paper/figures/` 全部 PDF 矢量格式
- 绘图脚本：`scripts/plot_r2_collapse.py`, `scripts/plot_counterfactual_bar.py`
- Bootstrap v3 数据源：`artifacts/clustered_bootstrap_reanalysis_v3/report/bootstrap_v3_summary_table.md`
- 实验数据服务器：westd-19183（demo-split per-layer R² profiles）
- 无活跃 GPU 实验 / 无 cron / 无 running workers

### 3. 📊 当前状态
论文处于 camera-ready 最终阶段（CoRL 2026 Abstract DDL 5/26，Paper DDL 5/29）。

刚完成：
- Abstract 提交材料已准备（art_20260525_adb40e）
- Figure 3 demo-split 修复 + Figure 4 colorblind palette（v12）
- Camera-ready 6 项检查 + bib 格式修复（v13）
- Appendix 加固：Cross-Architecture Design Rationale + Convergent Evidence Summary 两个新 section
- Appendix 表格事实修复（NORA vision encoder/integration）
- conclusion.tex 重命名为 .bak（orphan 文件）
- 当前 PDF：38 页，body ≤ 8pp，0 errors

Registry：无 RUNNING/PREPARING 实验。全部分析类实验已 DONE。
等待：无 Worker / Cron 回调。等 Director 下一步指令。

### 4. 📋 待办
- Abstract DDL 5/26 到来 → 提醒 Director 使用 `artifacts/abstract_submission.md` 提交
- Director 要求最终 PDF 上传 → 编译最新版，注册 artifact，通知手动下载（无飞书上传工具）
- 如需再改正文 → 改完必须验证 8 页约束（pdftotext -f 9 -l 9 | grep References）
- Number consistency 14 个 ⚠️ 项 → 需 SSH westd-19183 验证（非紧急，Table 1 值已与 bootstrap v3 summary 交叉验证一致）

### 5. 🎯 战略上下文
项目核心结论：VLM→VLA fine-tuning 产生 exit collapse（ΔR² 0.16-0.46），VLA→VLA 不产生（<0.10），L1 attention 是 inherited 而非 trained。三种方法（probing/perturbation/ablation）convergent evidence。

易错点：
- 不要混淆 random-split 和 demo-split 数据——Figure 3 旧版用 random-split（R² 0.7-0.9），已修复为 demo-split（R² 0.4-0.6）
- TracVLA/NORA 是 VLM→VLA，OpenVLA 是 VLA→VLA——这个 asymmetry 是核心 claim 不是 confound
- Rebuttal v2 在 `artifacts/anticipated_rebuttal_v2.md`，不是论文正文
- NORA 的 vision encoder 不是 InternViT（已修复），是 Qwen2.5-VL 自带的 native ViT


---
