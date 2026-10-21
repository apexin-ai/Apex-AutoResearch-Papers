# director / loop_10.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`15292830667aaec8c18c.json`](../../sessions/15/15292830667aaec8c18c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-21T07:21:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 rtx5090-4x 的 cuda:0-3（项目配置白名单），bjb2-12179 无 GPU 权限
- Evidence tax 必须用 matched@2048 token budget（D137 硬约束）——mismatched (no-evi@2048 vs with-evi@1024) 会产生截断伪影
- D136 "方向不稳定" claim 已 INVALIDATED，不要在任何分析或论文中引用
- **4B no-evi eval adapter 路径未验证**：cuda:0 上 d140_4b_sft_s42_no_evi_2048 使用 `/root/autodl-tmp/sft_no_evidence_output`，可能是 plan_014 模型（训练时不含 evidence 输出），不是标准 SFT s42。如果是 plan_014，结果不可用于 evidence tax 计算。**接手后第一件事确认这个 adapter 是否正确**
- eval_llama_rsft_s42_with_evidence_2048 的 registry conclusion 被诊断 Worker 误标为 failed（实际 success，ign_f1=0.5774）。Reviewer 两次确认数据有效。**接手后确认 registry 已修正为 success**

### 2. 🖥️ 基础设施快照
- **主服务器 rtx5090-4x**: connect.westd.seetacloud.com:37389，4× RTX PRO 6000 96GB
- 工作目录：/root/autodl-tmp/faith-evidence-ie/（代码）、/root/autodl-tmp/eval_results/（eval 输出）
- Python：/root/miniconda3/bin/python（conda base，不是 venv）
- 模型缓存：/root/autodl-tmp/.hf_cache/
- **bjb2-12179**: 数据源，无 GPU，SSH host `bjb2-12179`
- 活跃进程（截至 ~07:30 UTC）：
  - cuda:0: d140_4b_sft_s42_no_evi_2048 (PID 85668) — **adapter 待验证**
  - cuda:1: plan017_14b_rsft_eval_2048 (PID 70388) — 14B RSFT with-evi@2048
  - cuda:2: d140_8b_sft_s42_no_evi_2048 (PID 83650) — 8B Qwen no-evi@2048
  - cuda:3: d140_8b_sft_s42_with_evi_2048 (PID 81857) — 8B Qwen with-evi@2048

### 3. 📊 当前状态
刚完成 D140-D142 决策链：matched@2048 methodology 全面推开，LLaMA SFT 3-seed fair_tax 全部为负（mean=-5.19±5.25pp），narrative 从 "scale-dependent evidence tax" 改为 "capability-dependent amplifier"（D142）。1.7B pilot 完成（Δ_evi=-8.81pp，no-evi 截断在 2048 下仍 50%+，是模型能力问题非 token budget 问题）。

RUNNING 实验：
- plan017_14b_rsft_eval_2048: 14B RSFT with-evi@2048 验证 @1024 稳定性（预期 delta <1pp）
- d140_8b_sft_s42_with_evi_2048 + d140_8b_sft_s42_no_evi_2048: 8B Qwen matched@2048 pilot pair
- d140_4b_sft_s42_no_evi_2048: 4B no-evi@2048（adapter 正确性存疑）

等待：Agent 队列中有我的紧急消息要求验证 4B adapter 路径，尚未回复。

### 4. 📋 待办
- **4B adapter 验证结果出来 → 如果是 plan_014：kill PID 85668，用标准 SFT s42 adapter 重跑；如果正确：继续等完成**
- 14B RSFT @2048 完成 → harvest + 对比 @1024 (0.5886)，delta <1pp 确认 14B @1024 可信
- 8B Qwen with-evi + no-evi 都完成 → 计算 8B matched@2048 tax，发 Reviewer 审查
- cuda:1 释放后 → 启动 4B SFT s42 with-evi@2048（配对计算 4B tax）
- 全部 3 scale Qwen pilot 完成 → 如果全部 Δ_evi 为负 → "universal evidence benefit" 成立，更新 paper_framing.md contribution #3；任一正 → 改 "architecture-dependent"
- 全尺度 evidence effect 定稿 → 派 Paper Agent 全面 patch 论文数字 + narrative
- RSFT no-evi@2048 s42: Reviewer 建议做（RSFT 截断不对称 3.3pp），低优先级，Qwen pilot 全部完成后再排
- Test set eval: 代码已改好（test_inference.py 支持 Re-DocRED test_revised.json），等 GPU 空闲排 5 个核心 config

### 5. 🎯 战略上下文
- 目标：EMNLP 2026 Main（ARR July，~55天），Round 1 = 3.0 Findings，冲 4.0 Main
- 决策链：D137（matched@2048 必须）→ D139（Qwen 截断确认）→ D140（全尺度截断审计，P0 做 1.7B+8B+4B pilot）→ D141（fair_tax 全部为负，s42 从 +1.20 翻转为 -1.53）→ D142（narrative reframe: capability-dependent amplifier）
- 14B RSFT ign_f1=0.5886 全项目最高，RSFT gain Cohen's d=2.58，统计防御力强
- RSFT @1024 tax (-1.14±0.76pp) 已验证可信（with-evi@2048 delta=+0.60pp <1pp）
- 论文术语："evidence tax" → "evidence effect" (Δ_evi)，报告 raw + fair decomposition
- **易错点**：(1) 不要引用 D136 数据（已废弃）；(2) 旧 fair_tax_pp registry 字段全部 INVALIDATED（用了 @1024 with-evi，M026 错误），只看 matched_fair_tax_pp；(3) 4B adapter 路径 `/root/autodl-tmp/sft_no_evidence_output` 很可能是 plan_014 不是标准 SFT——这是当前最紧急的 pending 问题；(4) 1.7B matched@2048 不完全消除截断不对称（no-evi 仍 50%+ 截断），论文需加 caveat


---
