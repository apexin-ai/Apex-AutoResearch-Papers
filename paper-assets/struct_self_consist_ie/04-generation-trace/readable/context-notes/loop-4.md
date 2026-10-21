# director / loop_4.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`f88469abcf2c693ec68f.json`](../../sessions/f8/f88469abcf2c693ec68f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-15T12:37:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 autodl-5090 的 4× RTX 5090（项目配置 gpu_ids），不得使用其他项目的卡
- exp-019 (supervised verifier) 已被 D073 决策 SKIP——Reviewer 建议 DDL 风险 + scope creep，不要重新启动
- OOD 对比禁止使用 "in-domain avg ρ=0.335" 这个数字——来源不明，Reviewer 已 flag。论文中改为逐信号列举并溯源到 Table 1
- exp_011_ood_conll_to_scierc registry conclusion 仍为 "success"，需改为 "negative"——这个修正指令已发过两次但 Agent 可能未执行（两次都被 RESET 打断）

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (connect.bjb1.seetacloud.com)，用户 root
- 工作目录：/root/autodl-tmp/struct_self_consist_ie
- Python/conda：aml-train 镜像，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：Qwen3-8B fine-tuned (scierc-merged-v2 + conll), LLaMA-3.1-8B fine-tuned (scierc + conll)
- 活跃进程：无。全部实验完成，无 RUNNING/Worker/Cron

### 3. 📊 当前状态
纯论文修订阶段。全部 75 个实验 DONE (47 success / 19 negative / 1 failed + 8 killed)。

**Paper Agent 已独立完成**：
- D072 patch（title "Do Not" + abstract + intro + discussion + conclusion 修订）
- 补充 patch：OOD 数据集成（逐信号溯源）、N-scaling 3 张 appendix 表格、model name 修正、CoNLL→SciERC 排除原因精确化
- 编译通过：21 页（主体 8 + 附录 13），0 critical warnings

**未完成**：
- Registry 修正 exp_011_ood_conll_to_scierc（conclusion "success"→"negative" + 补 metrics）——指令发了但 Agent 两次 RESET 前可能未执行
- Round 7 提交（Paper Agent patches 完成后 → submit_paper_to_review）
- FK excess agreement Reviewer warning：P_e 不是 "由数据集决定"（CoNLL 上 Qwen 0.238 vs LLaMA 0.068 差 3.5x），论文如引用需改为 "受数据集和模型双重影响"

### 4. 📋 待办
- Agent 新 session 启动 → 立即重发 registry 修正指令（exp_011_ood_conll_to_scierc conclusion→negative + metrics）
- Paper Agent 报告 D072 patch 全部完成 → submit_paper_to_review 启动 Round 7
- Round 7 审稿报告回来 → Read `review-report-action.skill.md`，走 Holistic Pass + Per-Comment Action Matrix
- Reviewer 或 Round 7 发现需要补充数据 → 4× RTX 5090 待命，可立即启动补充实验
- FK P_e claim 如果要进论文 → 确保用 Reviewer 修正后的表述（数据集+模型双重影响）

### 5. 🎯 战略上下文
- **核心结论**：universal correlation-selection gap——所有 5 类置信信号（SJ/FK/VC/EM/LP）都能排序但无法有效选择，free-form ablation (exp-018) 证明这不是 constrained decoding artifact 而是 model/task intrinsic
- **决策链**：D070(narrative restructure) → D071(根本重定位) → D072(universal gap framing) → D073(skip exp-019) → D074(LP flip 保留 Section 5 不升级) → D075(title "Cannot"→"Do Not")
- **DDL**：EMNLP 2026 Findings，2026-05-25（约 10 天）
- **易错点**：
  1. 不要重启 exp-019——已被 D073 明确 SKIP
  2. 不要建议降级投稿目标（EMNLP Findings 已是目标，禁止 fallback）
  3. registry exp_011_ood_conll_to_scierc 标记错误是遗留债务，第一件事修掉
  4. Paper Agent 是独立角色，写作由它负责，Agent 不参与论文写作


---
