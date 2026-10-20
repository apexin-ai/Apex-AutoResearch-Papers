# director / loop_19.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_19.md`
- **Structured JSON:** [`842a57df638e263115a6.json`](../../sessions/84/842a57df638e263115a6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_messages
updated: '2026-05-17T20:19:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- seetacloud GPU 仅限 cuda:0/1/2/3，不可占用其他项目的卡
- DeepSeek CLS repo eval 必须用 max_seq_length=8192（M003：2048 导致 28.6% 截断）
- DeepSeek CWM repo eval 必须用 max_new_tokens=512（M003：128 导致截断不可比）
- DeepSeek CWM repo checkpoint 选择：用 last-epoch checkpoint（eval_loss=NaN 无法 val-select）
- 论文数字更新前必须 Reviewer 确认（M002：cross-model baseline 错误用了不同模型 zero-shot 做 delta）
- M004 教训：在任何 GPU 上启动新进程前必须先 nvidia-smi + ps 确认无活跃训练进程，registry 状态不可信（--no_wandb false positive）
- 跨模型 delta 计算必须用同模型 baseline

### 2. 🖥️ 基础设施快照
- **seetacloud**: connect.westd.seetacloud.com，工作目录 /home/sonny/exec-sim-repair-verifier，checkpoint 在 /root/autodl-tmp/
- **home-1x5090**: 1 张 RTX 5090，当前空闲
- **本地 paper 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/
- **活跃进程（seetacloud）**:
  - GPU 0: CLS v4 eval (PID 664774), checkpoint-4422, seq8192 — ETA ~5h → 完成后启动 CLS v5 retrain
  - GPU 1: CWM s42 eval (PID 662946), checkpoint-13266 (epoch 3, last-epoch, 已 MD5 验证), tokens512 — ETA ~23h
  - GPU 2: CLS s123 eval (PID 665019), best checkpoint, seq8192 — ETA ~5h → 完成后启动 CWM s42 epoch 2 eval
  - GPU 3: CWM s123 eval (PID 668680), checkpoint-8844 (epoch 2, 训练被杀只有这个), tokens512 — ETA ~26h
- **cron**: cls-v4 和 cls-s123 各有 10min 间隔 cron 监控

### 3. 📊 当前状态
**刚做完**: D122 Path AB narrative 确认、D123 过拟合假说（已被 D124 修正）、D124 安排 CWM s42 epoch 2 eval 解耦过拟合 vs seed 差异、Paper Agent 完成预更新 Patch（few-shot baseline + Table 4 占位 + Path AB narrative）、Paper Agent 被通知暂缓 CWM 定稿

**Running accuracy（稳定中）**:
- CLS s123: 73.9%（2040/9784, 20.8%）— 稳定
- CLS v4 s42: 69.9%（~1000/9784）— 不可用（只有 2/3 epoch training），eval 完后 GPU 0 重训
- CWM s42 (epoch 3): 58.7%（1014/9784, 10.4%）— 稳定
- CWM s123 (epoch 2): 63.6%（670/9784, 6.8%）— 稳定，与 s42 有 5pp gap

**等待中**: 4 个 eval 完成的 cron 回调

### 4. 📋 待办
- **CLS v4 eval 完成（GPU 0，~5h）** → 记录最终数字（预期 ~70% 不可用） → 立即提交 CLS v5 retrain（命令已准备好，exp_id=deepseek-cls-repo-v5，从零训练 3 epoch seed 42，output_dir=checkpoints_deepseek_cls_repo_v5/）
- **CLS s123 eval 完成（GPU 2，~5h）** → 记录最终 accuracy（预期 ~74%） → 立即启动 CWM s42 epoch 2 eval（checkpoint-8844，D124 实验，解耦过拟合 vs seed 差异）
- **CWM s42 epoch 2 eval 跑到 ~1000 samples** → 如果 ~63%（与 s123 一致）→ 过拟合确认，checkpoint sensitivity 写入论文作为 CWM 额外劣势；如果 ~59%（与 s42 epoch 3 一致）→ seed 差异，报告均值
- **CWM s42/s123 eval 全部完成（~23-26h）** → 收集最终数字 + unparseable rate → 填 Table 4 确定值
- **所有 DeepSeek 数字到手** → Paper Agent 最终 Patch（替换 preliminary 数字 + CWM narrative 定稿）→ 解决 R1-N1/R1-N2/R2-W1 → 提交 Round 2 审稿
- **CLS v5 retrain 完成（~22h after start）** → eval seq8192 → 提供 R1-N1 需要的 CLS repo multi-seed

### 5. 🎯 战略上下文
- **D116 framing**: "Design space characterization"（中性），不是 CLS advocacy
- **D122 Path AB**: formulation-inherent × model-contingent 双因素交互。Qwen3 CLS ~5pp/CWM ~22pp drop vs DeepSeek CLS ~13pp/CWM ~27pp drop
- **D124 悬而未决**: CWM s42 epoch 3 (58.7%) vs s123 epoch 2 (63.6%) 有 5pp gap。成因待定（过拟合 or seed）。CWM s42 epoch 2 eval 是关键判定实验。无论哪条路 C2 claim 都成立（最小 gap 10.7pp）
- **Paper Agent 状态**: 预更新完成（few-shot + Table 4 占位 + Path AB），CWM 数字标为 preliminary，已通知暂缓定稿
- **Review issues**: 15/18 resolved，剩余 R1-N1（CLS multi-seed → CLS v5 retrain）、R1-N2（CWM repo → eval 中）、R2-W1（新颖性 → DeepSeek 跨模型验证 + Path AB）
- **DDL**: EMNLP ARR May 25，剩 8 天。关键路径：CWM eval ~23-26h → Paper 更新 → Round 2 审稿 → May 20-21 完成
- **易错点**: (1) CWM checkpoint 必须用 last-epoch 不是 val-best；(2) CLS v4 s42 69.9% 不可用于论文（incomplete training）；(3) Paper Agent 的 CWM ~25pp drop 需更新为 ~27pp（58.7% 而非 60%）；(4) few-shot baseline 68.78% 已完成，不需要再跑


---
