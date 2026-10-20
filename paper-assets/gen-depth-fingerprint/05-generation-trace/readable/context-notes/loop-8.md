# agent / loop_8.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`2857db325069b59ea28c.json`](../../sessions/28/2857db325069b59ea28c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-15T22:11:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 的 cuda:0/1/2/3（config `execution.gpu_ids`），不可用其他设备
- **7-gen vs 6-gen 数字禁止直接对比**（D017/Director 硬约束）：7-gen binary F1=0.768 不可与 6-gen binary F1=0.723 做 apple-to-apple 比较——训练集组成不同
- **Instruct 方向反转是长度伪影**（D019，Reviewer CRITICAL 已验证）：instruct 链不可 claim 方向反转，Discussion 只用 "method boundary" 叙事（instruct gen-1 vs gen-2+ F1 ≈ 0.5，不可检测）
- Primary metric 是 **binary LOGO F1=0.723**（gen-1 vs gen-2+，排除 gen-0 共享 seed 泄露），3-class F1=0.789 仅作 supplementary 且必须带 gen-0 caveat
- EMNLP 2026 ARR DDL: **2026-05-25**，10 天倒计时，所有实验和论文修改必须在此之前完成

### 2. 🖥️ 基础设施快照
- **服务器**: autodl-5090，account=root
- **工作目录**: /root/gen-depth-fingerprint
- **Python**: /root/miniconda3/bin/python（conda base 环境，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **模型/数据**: 在服务器 /root/gen-depth-fingerprint/ 下，具体路径需 SSH 确认
- **W&B**: 项目内实验用 W&B 追踪（部分实验无 W&B）
- **活跃进程**:
  - plan-006-paraphrastic: PID 246021, cuda:1（cron 确认 still running）
  - plan-007-cross-model: PID 241978/242205, cuda:2+cuda:3（⚠️ cron 报 "Process gone, no sentinel, no W&B — escalating to agent, miss 3/5"——可能已崩溃或完成，registry 里 conclusion=success 但 status 仍 RUNNING）
  - plan-008-multi-domain: PID 234066, cuda:0（cron 确认 still running）
- **Cron**: 3 个活跃 cron 监控上述 3 个实验

### 3. 📊 当前状态
**正在做**: Round 2 审稿修复 EMNLP 冲刺阶段。论文大部分修复已完成，剩余 abstract/intro 数字更新、related_work CI 宽度修复、P1-E ordinal 结论写入。

**Registry**: 58 个实验，49 DONE（39 success / 3 negative / 11 failed），3 RUNNING，6 PREPARING（历史遗留，不活跃）。

**RUNNING 实验**:
- plan-006-paraphrastic (cuda:1): RQ2 paraphrasing vs continuation 对比，正在跑
- plan-007-cross-model (cuda:2+3): ⚠️ **需要立即处理**——cron 报进程已消失但无 sentinel/W&B（miss 3/5）。Registry 已有 conclusion=success + metrics（3class F1=0.809, binary F1=0.764），可能是分析已完成但状态未转 DONE
- plan-008-multi-domain (cuda:0): 多域 seeds（news/scientific/creative）验证 domain robustness，正在跑

**Worker 池**: 0 个 running worker（⚠️ 违反 L1 #4，需立即派发）

**待处理论文修改** (ROADMAP 未完成项):
- abstract + intro 数字更新 → binary F1 headline
- related_work CI width 残留修复
- P1-E ordinal 结论写入论文
- Rd2-M7 bib 年份验证
- 全文数字一致性最终验证
- Round 3 review 提交

### 4. 📋 待办（条件触发式）
- **立即**: plan-007-cross-model 进程消失 → spawn worker SSH 检查日志/输出，确认是否真正完成，更新 registry 状态为 DONE
- **立即**: Worker 池 = 0 → 至少派 2 个 worker（论文修改 + plan-007 诊断）
- plan-006 cron 回调（完成） → spawn worker 分析 paraphrastic vs continuation 对比结果，更新 registry，写入论文
- plan-008 cron 回调（完成） → spawn worker 分析多域结果，确认 domain robustness，更新 registry，写入论文
- 所有 RUNNING 实验完成 → 全文数字一致性验证 → post_to_reviewer Round 3 → EMNLP 提交材料准备
- cuda:2+3 空闲（plan-007 确认完成后） → 可跑其他排队实验或复现验证

### 5. 🎯 战略上下文
**项目核心**: 递归 LLM 生成链的 depth fingerprinting——7-feature distributional ensemble 在 6 base-model generators / 3 families 上 binary LOGO F1=0.723（leak-free）。Story 是 "differential depth response"（level features drift, shape features stationary）。

**决策链关键节点**:
- D017: Primary metric 改为 binary F1（排除 gen-0 泄露）
- D019: Instruct 方向反转撤回，确认为长度伪影，改为 "method boundary" scope limitation
- D012: 恢复 EMNLP 2026 ARR 为主投（曾 D010 放弃改 AAAI，被 D012 撤回）
- Claim 3 (downstream utility) 是 negative finding——depth fingerprinting 是 diagnostic 不是 curative，已诚实报告

**易错点**:
- plan-007-cross-model 状态矛盾（RUNNING + conclusion=success + 进程消失）→ 不要假设已完成，必须 SSH 检查
- 论文里任何数字改动后必须全文 grep 一致性——之前多次出现不同 section 引用不同口径的 F1
- abstract/intro 是 "最后一英里"，改数字时必须同步改 results/conclusion 中对应描述
- bib 引用（Rd2-M7）之前出现过 LLM 幻觉作者名，必须走 reference-audit skill
- PREPARING 状态的 6 个实验是历史遗留（mvp-001 系列 + plan-001-restore + plan-004-prep），不需要处理


---
