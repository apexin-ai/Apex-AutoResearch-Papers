# reviewer / loop_12.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`682335b6342395fd21a4.json`](../../sessions/68/682335b6342395fd21a4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-16T13:18:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 cuda:0, cuda:1**（westb-13313）。脚本里 `--gpu_id` 或 `device_map` 只能是 0 或 1
- 1.7B reference (47.1%) 使用的是旧训练配置，**不能与 plan-008-v4 训练的 0.6B/4B 做"同配置 monotonic"三点对比**——混淆变量未消除
- `tot-2023` 已从 references.bib 删除但 Limitations 仍有 `\citep{tot-2023}`——LaTeX 编译必挂。**已报 Director，尚未确认修复**
- Reviewer 角色只读，唯一输出渠道 `reviewer_post_to_director`

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313 (root)，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/`
- 模型路径：`/root/autodl-tmp/models/Qwen/Qwen3-{0.6B,1.7B,4B}`，Llama `/root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct`
- Checkpoints：`/root/autodl-tmp/simgate-modular-routing/checkpoints/plan-008-v4-{0_6b,4b}-seed{42-45}/final_adapter`
- 活跃进程：**无**（所有 88 个实验已 DONE，GPU 空闲）
- W&B：未配置（此项目不查 W&B）

### 3. 📊 当前状态
88 个实验全部 DONE，GPU 空闲。进入 R8 修复 + 方向决策阶段。

**我刚完成的审查**：
1. capacity-scaling-episode-eval (4B=58.96% 显著 > 50%，posted WARNING + C2 nuancing 建议)
2. R8-m1 bib fix (posted CRITICAL: tot-2023 错误删除导致编译失败)
3. R8-W6 reasoning depth (posted INFO: Appendix H 不存在，worker 正确 failed)

**等待 Director 决策**：
- 方向选择 A/B/C（method innovation track）——用户尚未决定
- tot-2023 bib entry 是否已恢复（编译阻塞）
- C2 措辞是否按我的建议调整（"structural limitation" → "capacity-dependent negative"）

### 4. 📋 待办
- Director 发送 C2 修改后文本 → 审查 claim 强度是否与 evidence 匹配（4B=59% 不能说"significantly outperforms"，只能说"above chance"）
- 论文 LaTeX 编译成功确认 → 检查 tot-2023 是否恢复 + 其他引用完整性
- 方向决策 A/B/C 确定 → 审查新 ROADMAP 是否与 evidence 一致、GPU-hours 估算是否合理
- 如有新 paper section 提交审查 → 按 5.1 维度审（Claim 可信度 / 叙事逻辑 / 审稿人攻击面），特别关注 C2 段是否正确呈现 capacity scaling 数据

### 5. 🎯 战略上下文
- **论文核心 story**：C1 death avoidance dominates (90.41%, r=0.97) + C2 informative router negative + C3 cross-model/cross-domain
- **C2 关键 nuance**：step-level flat (52-54% all sizes) + episode-level 只在 4B 跳变 = signal 是 task-type-level，不是 step-level。这加强 C1-C2 连贯性
- **最容易判断错的事**：
  1. 不要把 0.6B→1.7B→4B 说成"monotonic"——1.7B 训练配置不同是混淆变量
  2. 不要把 4B 的 59% 当成"router works"——59% 对二分类仍极差，远不足以做实际 routing
  3. R8-m1 的"orphan bib"诊断本身就是错的（三条引用都有 citation），不要信原始 action matrix 对 m1 的描述
- **DDL**：EMNLP ARR May 25 (9 天)，88 实验全完成，现在是论文打磨阶段


---
