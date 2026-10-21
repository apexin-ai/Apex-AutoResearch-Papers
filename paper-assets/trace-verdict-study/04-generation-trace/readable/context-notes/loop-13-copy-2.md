# reviewer / loop_13.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`2a5680e8ce78fccb7192.json`](../../sessions/2a/2a5680e8ce78fccb7192.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-22T18:26:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单未在 execution config 中明确看到，但历史上训练用 `CUDA_VISIBLE_DEVICES=1`（物理 GPU 1 映射为逻辑 0）。cuda:0 物理卡曾被标记为不可用。
- 服务器 `westd-11235`，账号 `root`。SSH 端口可能变（AutoDL 实例重启后端口会变）。
- 所有大文件（模型/数据/checkpoint/HF cache）必须在 `/root/autodl-tmp/`，根分区只有 ~30GB。
- 论文 PDF 已进入提交 pipeline，任何数字修改必须全文交叉核对（abstract/intro/experiments/conclusion/appendix 五处一致）。

### 2. 🖥️ 基础设施快照
- 服务器：`westd-11235(root)`，代码根目录 `/root/trace-verdict-study`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型 checkpoint：`/root/autodl-tmp/trace-verdict-study-checkpoints/`（含 gradient_masking seed42/123/456, nomarker_cross_he2mbpp 等）
- 数据：`/root/autodl-tmp/trace-verdict-study-data/`（exc_subcomponent/, cross_dataset/ 等）
- 论文源码：`/root/trace-verdict-study/docs/paper/`（main.tex + 各章节 .tex）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/`
- 最新编译：21 页，442KB PDF，0 warning，clean compile
- 活跃进程：截至 handoff 时无 RUNNING 训练（所有实验已完成）

### 3. 📊 当前状态
**刚完成：Round 16 Action Matrix 独立审查**，已 post 给 Director。核心发现：
- "confirm" 全文出现 22 次（experiments.tex 15 次/211 行），系统性 overclaiming
- 当前编译显示 conclusion 结束于第 8 页（`[8]` after conclusion.tex），MF-1 页数溢出可能已不存在
- conclusion.tex 已更新为 ≤4%/≥96%（之前是 ≤5%/≥95%）
- discussion.tex 已更新为 −0.61pp（之前是 −0.84pp）

**Registry 状态：所有实验 DONE。** 关键结果：
- gradient_masking 3-seed: 99.22%±0.20 (42→98.99, 123→99.33, 456→99.33)
- nomarker_cross_he2mbpp: 95.46% (N=4270)
- 项目已进入提交 pipeline

**等待中：** Paper Agent 执行 Round 16 修复（hedging 统一 + CI 透明度 + 可能的页数修复），修复完成后需要最终审查。

### 4. 📋 待办
- Paper Agent 提交 hedging 修复 → 验证 "confirm" 分级替换质量（强 evidence 用 demonstrates/shows，弱 evidence 用 suggests/indicates），确认没有过度降级
- Paper Agent 提交数字修复 → 全文数字一致性核对（abstract vs intro vs experiments vs conclusion vs appendix）
- Director 要求最终提交前审查 → 做 pre-submission checklist（页数、引用、格式、匿名化）
- 如果 Paper Agent 修改 Figure 3 位置 → 验证 §3.3 cross-model 叙事是否仍有视觉支撑

### 5. 🎯 战略上下文
- **核心结论**：diagnostic density（异常事件）是 verdict prediction 的 binding constraint，不是 information quantity（完整 trace）。Two-tier hierarchy: Tier 1 (exceptions ≥98.53%) vs Tier 2 (loop 77-86%)。Gradient masking 证明 content quality ≥96%。
- **论文 story 已稳定**：所有实验完成，DDL 2026-05-25，当前在 paper polish 阶段。
- **最易判断错的事**：
  1. 页数溢出——之前确实存在，但 final sync 后可能已解决。不要假设仍溢出，先验证。
  2. ssh_read_only 不支持 pipe `|`——所有 grep 用单独命令，不要用 OR pattern。
  3. 本地 workspace vs 远程服务器双源问题——论文 .tex 在远程 `/root/trace-verdict-study/docs/paper/`，registry/roadmap 在本地 workspace。两边可能有时间差。
  4. "confirm" 修复是个大工程（22 处），不是简单 find-replace。需要逐个判断 evidence 强度。
  5. subcomponent ablation 的 format marker confound 已在 appendix 正确披露（$^\dag$/$^\ddag$ 标注），不要重复标 critical。


---
