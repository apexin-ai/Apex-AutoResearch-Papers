# director / loop_14.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_14.md`
- **Structured JSON:** [`ce5c1f7c3afa73a8af6e.json`](../../sessions/ce/ce5c1f7c3afa73a8af6e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_messages
updated: '2026-05-19T11:02:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-41312 cuda:0-3, westd-30476 cuda:0-3（全部空闲，实验已全部完成）
- 论文定位 Findings Track（D091），禁止 claim Main Conference 水准
- 统计报告：N=3 禁止 p-value / bootstrap / permutation test / Cohen's d，只用 directional consistency + per-seed paired differences
- W2 distribution matching 是第 2 个 analytical contribution（D093），不是 limitation
- ρ=0.6 grid 数据标注 single-seed preliminary（D092 决定不跑 3-seed）
- 1.7B 结果表述为 "no evidence of improvement or degradation"，不能 claim scale transfer

### 2. 🖥️ 基础设施快照
- 服务器：westd-41312 + westd-30476，各 4× RTX PRO 6000 96GB
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/`
- 最新 PDF：`artifacts/paper_draft_20260519_v2.pdf`（15 pages, 464KB，已上传用户）
- 无活跃进程（实验全部完成，纯等审稿阶段）
- 无 RUNNING cron 与论文写作相关

### 3. 📊 当前状态
刚完成 review_issues.yaml 全量更新——Round 5 所有已修复 issue 从 open → resolved（约 30 项），含 resolution 描述。

Registry：176 个实验全部 DONE，无 RUNNING/PREPARING。

等待中：
- Round 6 审稿卡片 `apr_20260519T080115_rrrh`（continue mode）待用户批准
- 批准后 Review Director 会执行 Round 6 审稿，报告以 `[审稿报告]` 注入

### 4. 📋 待办
- 用户批准 Round 6 审稿卡片 → 等待审稿报告返回
- 收到 `[审稿报告]` → Read `review-report-action.skill.md` → Holistic Pass → Per-Comment Action Matrix → 派 Paper Agent 修复
- Round 6 无 critical → 编译最终 PDF → `feishu_upload_file` 发用户 → 准备 ARR May 25 提交
- 用户未批准 / 长时间无响应 → 当前 v2 PDF 即为提交版本，可直接使用

### 5. 🎯 战略上下文
- 核心决策链：D084(n-gram负向) → D087(GPT-2负向) → D088(epoch confound确认) → D089(实验收尾) → D090(1.7B撤回) → D091(reframe analytical study) → D092(ρ=0.6不跑) → D093(W2整合)
- 论文 4 个 contribution：(1) Epoch confound (2) Distribution matching (3) Mechanism+detector type (4) Adaptive b* tool
- Round 5 评分 3.0/5 weak accept (Findings)，从 Round 3-4 weak reject 提升，方向正确
- DDL: EMNLP 2026 ARR May 25（~6 天）
- 易错点：review_issues.yaml 刚全量更新过，所有 Round 5 item 已 resolved——下一轮审稿如果 re-raise 同一 issue，需要检查是否真的 regressed 还是审稿人在看旧版
- M035 教训：Table 1 数据必须从 registry 精确值拉取，不能混用 paper_framing.md 的近似值


---
