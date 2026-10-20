# director / loop_13.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_13.md`
- **Structured JSON:** [`bfd13f6399c3dd52ea33.json`](../../sessions/bf/bfd13f6399c3dd52ea33.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_messages
updated: '2026-05-21T22:17:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- D131/D132: 最后 4 天不开新 GPU 实验，所有 rebuttal 论据基于已有数据
- W4 task-level positive control 结果仅作 rebuttal 储备，不写入论文正文/附录（Reviewer WARNING: 64.7% BA 容易被误读为弱证据）
- GPU 分配已全部释放（D129），当前无分配卡，不要尝试在任何 GPU 上启动实验
- 论文 page 8 极度紧张——任何正文改动必须编译验证不超页

### 2. 🖥️ 基础设施快照
- 服务器：westd-18266（唯一注册服务器），westb-13313/westb-14838 不属于本项目
- 本地论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/`
- 产出目录：`projects/simgate-modular-routing/artifacts/`
- 无活跃进程、无 RUNNING 实验、无 cron 任务
- 曾向 Manager 申请 GPU 重新分配，未收到回复（非阻塞）

### 3. 📊 当前状态
刚完成：提交 fresh 审稿到 C 群（`apr_20260521T220006_nnjs`，pending 用户点击确认）。
论文编译状态：23 页（8 页正文 + 附录），0 errors，0 critical warnings，0 overfull hbox。
Round 25 全部 11 项修复已应用并通过 Reviewer PASS。
Rebuttal 5 个 attack 点全部准备完毕（`artifacts/rebuttal_prep.md`）。
ARR 提交表单预填项已整理（`artifacts/arr_submission_prep.md`）。
Registry 无 RUNNING/PREPARING 实验。

### 4. 📋 待办
- C 群审稿报告返回 → 按 `review-report-action` skill 处理：Holistic Pass → Per-Comment Action Matrix → 派 Agent 修复
- 用户点击审批卡确认 → 审稿流程自动启动，无需干预
- 审稿发现 critical issue → 评估是否需要改正文（注意 page 8 预算）
- DDL 2026-05-25 前 → 用户人工完成 OpenReview 提交流程（用户已明确说提交流程人工做）

### 5. 🎯 战略上下文
- 核心发现：ScienceWorld 中 78.9% 非平局路由标签来自 death asymmetry，DAF=88-90% 跨三模型家族稳定
- 论文定位：diagnostic/analysis contribution（非 method paper），EMNLP 2026 ARR，Interpretability and Analysis track
- Round 25 评分：Overall 3.0 (Findings)，Excitement 2.5/5 是瓶颈
- 易错点：不要试图在论文中加 W4 positive control 数据（已尝试→Reviewer 打回→已 revert，保持 rebuttal-only）
- Rebuttal 核心武器：Attack 4 (router positive control) 用 LOTO 一致性（LLM router 49.2% vs sklearn 50.0%）作为 convergence argument，不要突出绝对准确率 64.7%
- `review_issues.yaml` 跟踪 40+ issues 跨 rounds 13-25，新审稿报告处理时先读此文件了解历史


---
