# reviewer / loop_5.md

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`87cfbab78e0360592d37.json`](../../sessions/87/87cfbab78e0360592d37.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-21T01:33:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-33183 的 cuda:0（RTX PRO 6000 98GB），无其他 GPU 分配
- 论文主文严格 8 页（EMNLP 2026 ARR），Limitations/Ethics/References/Appendix 不计入
- tab:e2e 和 tab:frozen_verify 使用不同 checkpoint（main experiment vs plan_002），数字不同是 intentional——不要标为 inconsistency
- exp16 qwen_test 指标已废弃（数据泄漏，D048），不要引用该指标

### 2. 🖥️ 基础设施快照
- 服务器：westd-33183(root)，工作目录 /root/persuasion_turn_jailbreak_detect
- Python：系统 Python 或 venv（未详细探查，Worker 负责环境）
- HF cache：/root/autodl-tmp/hf_cache
- Checkpoints：/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints_archive/plan_002{,_seed123,_seed456}/
- 数据：/root/persuasion_turn_jailbreak_detect/data/（plan_002_splits/, generated/, wildchat_benign_226.jsonl）
- 本地论文：/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/
- 活跃进程：无（GPU 空闲，~89 GPU-hours remaining）
- 无 wandb 配置（本项目不用 wandb）

### 3. 📊 当前状态
**论文处于可提交状态**，等待 Round 5 审稿用户审批（review mode: apr_20260520T020101_ay8q）。

我刚完成：
1. 全文 pre-submission 终审（figures/story arc/checklist 全通过）
2. exp37 审查（turn-count confound 否定：benign truncation FPR=0%；AA padding collapse 作为 limitation 写入）
3. Patch 27 确认（exp37 写入 Appendix §Z + Limitations 更新）
4. EMNLP 评分预估从 3.5 上调至 3.5-3.75
5. 回应 Director 的"推向 4.0"提问：推荐候选 1（WildChat threshold calibration，<0.5h），不推荐候选 2/3

Registry: 全部 DONE（104 总实验，51+ 成功，20 负向）。无 RUNNING/PREPARING。

等待中：Director 可能决定是否跑 WildChat threshold calibration 实验（我推荐了但 Director 尚未决策）。

### 4. 📋 待办
- Director 审批 WildChat calibration 实验 → 审查 exp38 结果（纯推理实验，关注 calibrated FPR@TPR=0.95 和 ROC 曲线合理性）
- Round 5 审稿用户审批 → 可能有新的审稿意见需要审查
- 如果 Paper Agent 提交新 Patch → 做增量审查（重点看新增内容是否与已有 story arc 一致）
- 如果新实验启动 → 核查 CUDA_VISIBLE_DEVICES=0 合规

### 5. 🎯 战略上下文
**核心结论链**：D049（claim 重构："classification DAPT most robust across conditions"）→ D057（实验关闭）→ D058（turn-count confound 否定）。论文 story 从"domain exposure suffices"演化为"adaptation mechanism matters"，有 exp16 mixed-LLM MLM collapse 作为关键证据。

**决策链中容易判断错的事**：
- 3.75→4.0 的差距是 significance/novelty 固有限制，不是 soundness 问题——不要被推去跑大型补充实验（DeBERTa-v3-large 等），ROI 不对称
- WildChat FPR 68.1% 是 domain shift 驱动（exp37 Part 1 证实），不是 length shortcut——下一个审稿人如果攻击 FPR，用 exp37 数据回应
- ToxicChat hierarchy reversal（MLM > 9-class）是 condition-dependent effect 的一部分，不是 bug——论文已诚实披露
- Part 3 AA padding collapse（-57.9pp）定位为 BiGRU aggregator limitation，不是 DAPT 表征问题（DD 仅 -2.5pp 证明表征 robust）
- 论文本地文件是权威版本（remote 可能 stale）——审查论文内容时读本地 paper/ 目录


---
