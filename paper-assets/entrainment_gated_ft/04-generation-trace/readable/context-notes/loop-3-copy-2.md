# reviewer / loop_3.md

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`e093b93cffa0b1d87490.json`](../../sessions/e0/e093b93cffa0b1d87490.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-22T18:14:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文 Appendix Table 30 必须保持 **5-arch**（GDN/RetNet/HGRN2/GLA/DeltaNet），**不要升级到 6-arch**。HGRN 的极低 pure acc（LAMBADA 0.263）导致 J_h 最高达 0.163，会破坏 "≤ 0.14" claim 和 "p ≤ .002" claim（GDN-HGRN ARC-Easy hurt z=2.90, p=0.006）
- DeltaNet 数据曾被 Paper Agent 幻觉填错（14/16 cells），已修正。如果 Paper Agent 再碰 Table 30，必须逐格比对 `jaccard_5arch.json`
- Miller & Blume (2026) 是 **审稿人幻觉引用**，不存在，禁止添加到 bib
- 服务器 `westb-48145` 只有 1 张 GPU (cuda:0)，不存在越界问题

### 2. 🖥️ 基础设施快照
- 服务器：`westb-48145`（AutoDL），root 账户，工作目录 `/root/entrainment_gated_ft`
- Python：`/root/miniconda3/bin/python`（conda base env）
- 模型路径：`/root/entrainment_gated_ft/models/340M-20B-*`（h3-1 + pure 共 ~12 模型）
- HF cache：`/root/autodl-tmp/.hf_cache`，ModelScope cache：`/root/autodl-tmp/.ms_cache`
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/`
- 关键 JSON：`results/exp005_zoo_expansion/jaccard_5arch.json`（5-arch 定稿），`jaccard_6arch.json`（6-arch 备用，不入 paper）
- 活跃进程：最后一批 v9/v10 下载进程可能已结束或仍在跑，无需关注
- Registry 有 ~8 个 stale PREPARING 条目（exp-005-pure-v3 到 v10），应清理但 non-blocking

### 3. 📊 当前状态
**刚完成**：R15 综合修复包全项验证 PASS + 6-arch 分析审查（建议不纳入论文）。

**论文状态**：R15 修复已落地——DeltaNet 数据修正 ✅，"nearly disjoint"→"largely non-overlapping" ✅，Abstract 校准 ✅，Jain et al. FAccT 2025 引用 ✅，statistical caveats 全部到位 ✅。

**Registry RUNNING/PREPARING**：无 RUNNING。exp-005 状态 PREPARING（实际已完成 5-arch 分析，应更新为 DONE）。

**等待中**：无 pending worker/cron。DDL ~42h（2026-05-25）。下一步应是 Paper Agent 最终排版 + PDF 视觉审查。

### 4. 📋 待办（条件触发式）
- Paper Agent 提交最终 PDF → 做 paper-visual-review（pdf_to_images 检查 orphan lines、图表质量、字体）
- Director 问是否加 Jaccard heatmap figure → 推荐加（1 figure + 3 tables 偏少），用 5-arch 1.3B 数据画，30min 工作量
- 如果 Paper Agent 再碰 Table 30 → 立即逐格比对 `jaccard_5arch.json`，上次幻觉教训
- 如果有人提议升级 6-arch → 用我的 warning post 中的数据打回（J_h=0.163, z=2.90, p=0.006）
- exp-005 registry 清理请求 → 保留 exp-005 主条目（标 DONE）+ exp-005-gla-pure（DONE），其余 v3-v10 可标 CANCELLED
- Figure 1 caption 若有 CI bands 可见 → 补 "shaded: illustrative 95% CI (n=3)"

### 5. 🎯 战略上下文
**核心结论**：hybrid recurrent 架构在 aggregate benchmark 上等价，但 per-example 行为 ~90% 不重叠（J ≤ 0.10 at 1.3B, ≤ 0.14 at 340M×5arch）。α = 0.14–0.30 由 task type 决定，不由 attention dose 决定。Convergence 仅 LAMBADA 有（p=.170 after Bonferroni），依赖 GDN 的 16-head confound，已降级为 "exploratory secondary observation"。

**评分目标**：3.0 → 4.0（EMNLP 2026 via ARR）。Presentation 修复可到 3.5，4.0 需要 reviewer 认为 contribution 有 significance。

**最容易判断错的事**：
1. **不要被 6-arch 诱惑**——HGRN 的数据虽然 "更多架构"，但会弱化 claim，得不偿失
2. **不要信 Paper Agent 直接输出的数字**——DeltaNet 数据幻觉是 14/16 cells 错误的先例，任何新数据都要比对 JSON
3. **"nearly disjoint" 已被全文替换为 "largely non-overlapping"**——如果看到残留的 "nearly disjoint" 说明有回归
4. Bonferroni p=.170 是 **10-benchmark correction**（不是 6-benchmark），全文已统一，如果看到 p=.100 说明是旧版残留


---
