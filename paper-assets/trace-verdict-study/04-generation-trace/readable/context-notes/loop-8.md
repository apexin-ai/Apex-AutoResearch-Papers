# director / loop_8.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`a4dc61dacd5c8a47bfa1.json`](../../sessions/a4/a4dc61dacd5c8a47bfa1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-17T18:17:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-11235 的 cuda:0 和 cuda:1，不可使用其他服务器/GPU
- 论文远程路径：`/root/trace-verdict-study/docs/paper/`，本地 artifacts：`projects/trace-verdict-study/artifacts/`
- 模型权重在 `/root/autodl-tmp/models/` 下，不要删除（磁盘紧张但仍需保留）
- Reviewer 本轮一直 API Error 400（"Could not process image"），完全无法工作——已提交 RESET_BOTH，新 session 应该恢复正常

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235 (connect.westd.seetacloud.com)，账号 root
- 工作目录：`/root/trace-verdict-study`
- 模型路径：`/root/autodl-tmp/models/` (Qwen2.5-Coder-7B-Instruct, Qwen2.5-Coder-1.5B-Instruct, deepseek-coder-6.7b-instruct-v1.5, CodeLlama-13b-Instruct-hf)
- 数据：`/root/trace-verdict-study/data/` (full_trace_head/tail conditions 已生成)
- 磁盘：系统盘 6.2G/30G (80%), 数据盘 42G/250G (84%), checkpoints=73G
- 活跃进程：deepseek_full_trace_head2048_seed42 (cuda:0, ~2h), qwen15b_full_trace_head2048_seed42 (cuda:1, ~45min)

### 3. 📊 当前状态
刚完成本轮核心工作：5 级 baseline 递进整合 + cross-model tail-2048 验证。Paper Agent 已完成全部 5 轮 Patch。

RUNNING 实验：
- `deepseek_full_trace_head2048_seed42` — DeepSeek head-2048 截断，预期 ~80-85%
- `qwen15b_full_trace_head2048_seed42` — Qwen-1.5B head-2048 截断，预期 ~75-82%

等待中：
- Round 6 审稿审批卡 (apr_20260517T175602_17p3) pending 用户确认
- head-2048 实验完成后 cron 自动回调

### 4. 📋 待办
- head-2048 实验完成 → 收割结果，计算 tail vs head gap（DeepSeek/Qwen-1.5B），派 Paper Agent 补入论文
- Round 6 审稿用户批准 → Review Director 接手，等审稿报告回来后按 review-report-action skill 处理
- 审稿报告回来后 → 如有 critical issue 需补实验，在双卡上立即启动
- 所有 head-2048 + 审稿都完成 → 更新 ROADMAP（已 10h 未更新）

### 5. 🎯 战略上下文
- 核心论文 story："exception trace 诊断信号集中在 trace 末尾 256-512 token 窗口，exception_only（median 150 tokens）是最优提取方式，SFT 将跨架构 42pp zero-shot 方差压缩到 <1pp"
- 已有 54 个成功实验，证据极其充分：4 模型 × 3 架构 × 2 scale + 5 级 baseline + 8-point budget curve + tail/head cross-model
- DDL：2026-05-25 ARR（约 7 天），时间充裕但需要审稿反馈来确定最后修改
- 易错点：Paper Agent patch 后论文可能有 orphan bib keys（3 个已知 warning），不影响编译但最终提交前需清理
- 易错点：zero-shot 结果中 Qwen-1.5B (93.45%) > Qwen-7B (89.08%)，叙事是 "cross-architecture normalization" 不是 "scale normalization"——不要在任何地方暗示更大模型 zero-shot 更好
- 已知 limitation（论文已承认）：只有 Java/Defects4J 数据集，无 Python/real-world CI 数据


---
