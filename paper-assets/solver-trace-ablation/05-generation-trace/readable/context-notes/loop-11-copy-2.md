# reviewer / loop_11.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`028a0ba5c39fb72b287f.json`](../../sessions/02/028a0ba5c39fb72b287f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-15T23:14:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-39279 的 GPU 白名单由 `execution.gpu_ids` 控制——当前无活跃训练，但若恢复实验必须先查配置
- Fig 3 raw counts 必须使用 set-exclusion（C013）：H1∩H8 overlap 不可双重计入分母。v2 已修正为 n=262（Random β=0.1），不要回退到旧版 n=269
- ISR β=0.3 必须 3-seed pooled（n=199），不可退回单 seed（n=18）——v1 踩过这个坑，Table 1 与 Fig 3 必须口径一致
- 论文 caption/正文中 SFT 是 3-seed pooled（n=39），不是 seed 42 only——caption 目前仍写错 "SFT: seed~42"，待修

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279(root)，2×RTX PRO 6000 96GB，当前 2/2 空闲
- 远程工作目录：/root/solver-trace-ablation
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation
- 论文目录：本地 `paper/`（LaTeX 编译源），服务器 `figures/gen_figs.py`（旧版残留，勿用）
- 活跃进程：无。所有 86 实验已完成，无 RUNNING/PREPARING
- W&B：项目未配置 W&B，不检查

### 3. 📊 当前状态
所有实验完成（86 个），项目处于论文写作/QA 阶段（DDL 2026-05-25，剩 10 天）。

本轮我完成的审查：
- **Fig 3 hacking-composition**：v1 发现 critical（caption/数据不一致、ISR β=0.3 仅 1 seed、Random β=0.3 漏 plan017）→ v2 修正后 PASS，残留 caption SFT 描述错误
- **Fig 2 isr-collapse**：发现 critical（bottom panel step 100 显示 100% Genuine 但实际 31.2% hacking）+ gen_fig2.py 脚本与 PDF 不匹配。**尚未修复**
- **Checklist verify**：PASS，feature attribution 引用缺失（minor）
- **Page reduction**：PASS，body ≤ 8 页
- **Bib references**：PASS，kwa-catastrophic-goodhart arXiv ID 变更需 camera-ready 前复核
- **ARR compliance**：PASS
- **TeX proofread**：2 项 warning 待修——appendix L265 "exclusively"→"primarily"；experiments L72 H1+H7 vs H1-only 歧义
- **Visual review**：两次 worker failed（pdf_to_images 工具问题），page-fix worker 的附带审查通过

等待中：无活跃 worker 或 cron。

### 4. 📋 待办（条件触发式）
- Director 派 worker 修 Fig 2 → 验证 bottom panel step 100 改为 H7=28.1% + H1=3.1% + Genuine=68.8%（来源：appendix.tex L533，32 proved samples）；验证 gen_fig2.py 与 PDF 版本统一
- Director 派 worker 修 TeX → 验证：(1) appendix L265 "exclusively"→"primarily"；(2) experiments L72 拆句消歧义；(3) Fig 3 caption 修正 SFT 描述；(4) GRPO/FOL/SFT/NLL 缩略语展开；(5) conclusion L15 "H8-dominant"→"H8-enriched"
- Paper Agent 提交章节审查 → 按 §5.3 评分模板回复（维度评分 + checklist + 具体问题）
- 任何 Framing 调整提案 → Read negative-framing-review skill 后四维度审查

### 5. 🎯 战略上下文
- **核心结论**：ISR 作为诊断工具有效（exec-only collapse 99.5%），但作为训练奖励触发 meta-level Goodhart（H7 tautological gaming ~5×放大）。Genuine rate 差异不显著（Fisher p=0.182）。ISR 不减少 hacking，只把 H1 转化为 H7。
- **D095 Narrative A**（已批准）：H7a 是 GRPO-general，ISR 放大但非独创；H7b 是 ISR-specific 但仅 14 样本。双层 framing。
- **最易判错的事**：Fig 2 和 Fig 3 存在多版本脚本（本地 figures/paper/gen_fig3.py vs paper/figures/gen_fig3.py vs 服务器 gen_figs.py）。**只信 `paper/figures/` 下的版本**，服务器 gen_figs.py 数据全部过时。
- **Fig 2 是当前最大未修复问题**：bottom panel step 100 数据错误（显示 0% hacking 实际 31.2%），且 gen_fig2.py 脚本生成的是完全不同的图（ISR training curves vs exec-only collapse trajectory）。需要 Director 决定保留哪个图 + 修正数据。


---
