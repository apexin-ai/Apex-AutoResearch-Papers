# director / loop_2.md

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`5a7d297f0785600b2828.json`](../../sessions/5a/5a7d297f0785600b2828.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-21T17:54:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-48145:cuda:0（唯一分配的 GPU）
- Observational study：使用 Wang et al. 2025 预训练模型，不自己训练。只能跑 eval-only 实验
- HellaSwag 必须用 acc_norm（不是 acc），之前因此出过 M012 critical bug
- GPU 已由 Reviewer 书面确认不再使用（D021），提交前无需跑任何实验
- EMNLP 2026 主文限 8 页（当前 7 页），references/appendix 不限

### 2. 🖥️ 基础设施快照
- 服务器：westb-48145 (connect.westb.seetacloud.com)，root 用户
- 工作目录：/root/entrainment_gated_ft
- 论文目录（本地）：projects/entrainment_gated_ft/docs/paper/
- Artifacts（本地）：projects/entrainment_gated_ft/artifacts/paper_data/（bootstrap_ci_alpha.json, 340m_lambada_per_example.json, subsample_sensitivity.json）
- 无活跃进程/tmux/cron——全系统空闲，GPU idle

### 3. 📊 当前状态
论文全部打磨完成，等用户批准 Round 6 审稿卡片 `apr_20260521T100110_w6db`。

自上次 Round 5 审稿（Overall 3.0）以来完成：
- Round 5 全部 9 项审稿意见修复（W1-W9）
- M012 HellaSwag acc→acc_norm 数据修正 + 全文级联更新
- 3 项新分析整合：Bootstrap CI on α / 340M per-example / Subsample sensitivity
- Introduction multiplicity-first 重写 + Abstract/Conclusion 叙事同步
- Contribution list 明确区分 seed-driven vs architecture-driven
- Proofreading（hurt ES 0.062→0.047 / CI 格式统一 / author_response §4.5→§4.4, Round 3→6）
- author_response.tex 最终更新（5 项 overview 补充 + 3 处回应增强）
- Hostile review 模拟完成，预期 3.0-3.25

Registry: 无 RUNNING/PREPARING。Paper Agent 正在清理 42 个 orphan bib entries（最后一个任务）。
Reviewer 确认 related work 覆盖完整，无遗漏。

### 4. 📋 待办
- 用户批准审稿卡片 → Round 6 Review Director 自动启动审稿（推荐 continue 模式）
- Round 6 审稿报告回来 → 按 review-report-action skill 处理（Holistic Pass → Action Matrix）
- Paper Agent orphan bib 清理完成 → 重新编译 PDF 确认
- 如果 Round 6 评分 ≥3.25 → 准备 ARR May 最终提交
- 如果 Round 6 仍有 critical → 修复后再提交一轮

### 5. 🎯 战略上下文
- 核心决策链：D014(审稿策略) → D015(扩展 per-example) → D018(4-benchmark confirmed) → D019(直接执行 Action Matrix) → D020(W3 format confound 成功) → D021(GPU 最终确认不再使用 + multiplicity-first framing)
- C2 (convergence) 是最弱 claim：Bonferroni p=.100，单 benchmark (LAMBADA)，结构性限制无法解决。论文已将 C1 (multiplicity) 定位为 central contribution，C2 降级为 secondary
- 易错点：(1) 不要试图用 GPU 跑更多实验补强 C2——Reviewer 已确认结构性限制，浪费时间；(2) author_response.tex 刚做了大量更新，别再引用旧版内容；(3) check_paper_consistency 的 orphan bib 可能包含 author_response.tex 引用的条目（如 mccoy2020berts），清理时要确认
- 42 orphan bib entries 中部分可能被 author_response.tex 引用，Paper Agent 已被提醒检查


---
