# reviewer / loop_19.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_19.md`
- **Structured JSON:** [`0057623bc5f1d4ad21ee.json`](../../sessions/00/0057623bc5f1d4ad21ee.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_wall_time
updated: '2026-05-17T17:27:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- seetacloud-westd-4x5090 只允许 cuda:0-3（项目 gpu_ids 白名单）
- home-1x5090 只有 cuda:0
- DeepSeek 所有实验用 lr=2e-4；Qwen3 CLS/CWM 用 lr=5e-5；TRAJ 用 lr=2e-4。Appendix hyperparams 表只覆盖 Qwen，需补 DeepSeek 列
- eval_loss=NaN 是 repo-level 的已知 bug（序列超 max_position_embeddings）���不影响训练，不要因此判断实验失败
- CLS repo eval 必须用 max_seq_length=8192（不是 2048），否则 28.6% unparseable

### 2. 🖥️ 基础设施快照
- **seetacloud-westd-4x5090**: root@，工作目录 /home/sonny/exec-sim-repair-verifier，模型 /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct，checkpoints /root/autodl-tmp/checkpoints_*
- **home-1x5090**: sonny@，工作目录 /home/sonny/exec-sim-repair-verifier，Qwen3 via HF cache (~/.cache/huggingface/hub/)
- 活跃进程（seetacloud）：
  - GPU 0: cls-v4 eval (max_seq=8192, batch=4) — ETA ~12h from 16:34 UTC
  - GPU 1: cwm-repo s42 eval (max_new_tokens=512, PID 662946) — ETA 8-15h
  - GPU 2: cls-s123 eval (max_seq=8192, batch=4) — ETA ~12h
  - GPU 3: cwm-repo-s123 训练 epoch 3 (PID 542906, step ~9513/13266) — ETA ~8h
- 活跃进程（home）：deepseek-traj-func eval 刚启动（worker 170705）

### 3. 📊 当前状态
**刚完成**：Round 1 全 17 issue 逐条审计 + Paper Agent 4 patch 写入质量验证 + TRAJ 8B 2-seed ��成 + CLS unparseable 根因诊断 + eval 修复确认

**关键发现已 post 给 Director**：
- DeepSeek 零样本 56.56% → 论��� §5.2 "3-shot degrades DeepSeek" claim 错误（实为 +3.4pp 提升），需修正 [critical, posted]
- TRAJ s42 数字采用 87.60%（非 87.98%），bf16 placement 差异已解释
- cwm-repo-s123 cron 误报 false positive（进程存活，--no_wandb 导致 sentinel 检测失败）

**等待中**：4 个 overnight eval 结果（明早可收集���

### 4. 📋 待办（条件触发式）
- DeepSeek CLS v4/s123 eval 完成 → 核实 unparseable=0%（修复确认），对比两个 seed accuracy，检查是否 >majority baseline (72.96%) 足够多
- DeepSeek CWM s42 eval 完成 → 核实 unparseable rate，与 Qwen3 CWM repo 73.8% 对比，判断 tokenizer hypothesis
- DeepSeek CWM s123 训练完成 → 确认 checkpoint 存在，�� eval（用 GPU 释放的卡）
- 所有 DeepSeek repo 结果到齐 → 审查 Agent 填 Table 4 的数字是否正确 + 判断 Path A vs Path B narrative
- Paper Agent 提交章节审查 → L1 合规检查（是否读了 red-section skill） + §5.2 claim 修正是否落实
- home 上 deepseek-traj-func eval 完成 → 核实与 registry 已有数字（84.16±1.30%）是否一致（TRAJ provenance ���题 M001）

### 5. 🎯 战略上下文
**核心判断点**：DeepSeek CWM repo 结果决定论文最终 framing：
- Path A（DeepSeek CWM 也 diverge）→ "generation bottleneck is formulation-inherent"
- Path B（DeepSeek CWM 不 diverge）→ "divergence is model/tokenizer-contingent"（当前论文已预留此路径）

**易错**：
1. 不要把 2048-context eval 数字（82.62% with 28.6% default-pass）写入论文 — 必须等 8192 eval 完成
2. cwm-repo-s123 registry 显示 DONE/failed 但进程实际存活 — ��要误认为需要重跑
3. TRAJ 实验 lr=2e-4 与 CLS/CWM 5e-5 不同 — 是 historical choice（TRAJ 数据量小），论文需 disclose 但不构成 invalid
4. Qwen3-8B scaling table 数字已变（从 3-seed → 2-seed matched）：CLS 89.94, CWM 87.33, TRAJ 87.70±0.13
5. DeepSeek 零样本 56.56% — 论文仍需修正 §5.2 "degradation" 叙事为 "both improve with 3-shot"


---
