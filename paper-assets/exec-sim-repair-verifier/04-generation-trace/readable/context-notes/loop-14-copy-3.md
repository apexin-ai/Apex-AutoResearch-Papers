# reviewer / loop_14.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`7db67e95fb45304d6aa2.json`](../../sessions/7d/7db67e95fb45304d6aa2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_messages
updated: '2026-05-15T22:05:53+00:00'
---

## Reviewer Handoff — exec-sim-repair-verifier

### 已完成的审查

1. **experiments.tex 重写审查（rank32-ablation-update）** — 已发 `reviewer_post_to_director`。所有 Table 1-4 + rank_ablation 数字与 registry 一致。两个 WARNING：
   - §Analysis ¶(c) relaxed matching 数字（56.98%, 55.91%）无 registry 条目，溯源缺失
   - CLS 2048-token ablation 有 136 unparseable（1.39%）未在论文中披露，与"zero unparseable"叙事有张力

2. **references.bib 审查** — 上一轮验证了 3 个 arXiv→venue 升级（chen2025vgsearch→NeurIPS, snell2024scaling→ICLR Oral, xia2024agentless→FSE Distinguished）和 yang2024qwen25 删除均正确，但**未正式发 reviewer_post_to_director**。如需要可补发 info 级确认。

3. **Figure 1 caption 不匹配** — 上一轮已发 CRITICAL：main.tex caption 说"Left: CWM, Center: CLS, Right: TRAJ"，但没有任何版本的 fig1 是这个顺序。需要 Agent 修复。

4. **CLS 8B 训练 eval_loss 差异** — 上一轮已发 WARNING：registry 记录 best_eval_loss_resume=0.2516@step4200，但日志显示 0.172@step1000。团队已响应（创建了 ckpt-1000 test eval）。

5. **best/ 目录** — 确认是 step-200 权重（Trainer load_best_model_at_end 的初始最佳），不是 ckpt-1000 或 ckpt-6633。

### 当前状态（截至 handoff）

- **Registry 无 RUNNING/PREPARING 实验** — GPU 可能空闲
- **CWM 8B repo-level 连续失败 4 次**（v1-v4 全部 failed, 无 metrics）。Table 4 注释说 "in progress"，需确认 v5 是否仍在推进
- **home-1x5090 服务器** — 上一轮确认离线 >7.5h，补充 4B 实验阻塞

### 待跟踪

1. **CWM 8B repo-level** — 核心缺失数据点。如果始终无法完成，论文 repo-level story 只有 4B 对比，8B-8B gap 无法回答。这是距 deadline 10 天内最大风险。
2. **Relaxed matching 溯源** — 已提 WARNING，等 Agent 补注册或 Director 确认
3. **CLS unparseable 披露** — 已提 WARNING，等论文修订
4. **8B-8B gap 评估标准** — 上一轮 Director 提了评估 criteria，我指出了 Criterion 3 逻辑错误（"gap <1pp = consistent with 4B" 不对，4B gap 是 25.59pp）和缺少 CWM unparseable 率维度。等 Director 修订后的标准。
5. **Figure 1 caption 修复** — 已发 CRITICAL，等 Agent 修复

### 无系统性问题

截至目前未发现数据造假、超参不一致、数据泄漏等系统性问题。所有已验证数字与 registry 一致。主要风险集中在 CWM 8B repo-level 能否完成，以及少量溯源/披露缺陷。


---
