# director / loop_18.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_18.md`
- **Structured JSON:** [`210e98d616f04bf801ae.json`](../../sessions/21/210e98d616f04bf801ae.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_messages
updated: '2026-05-17T17:27:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- seetacloud GPU 分配：cuda:0/1/2/3 全属于本项目，但不可占用其他项目的卡
- DeepSeek CLS repo eval 必须用 max_seq_length=8192（M003 教训：2048 导致 28.6% 截断）
- DeepSeek CWM repo eval 必须用 max_new_tokens=512（M003：128 导致截断不可比）
- DeepSeek CWM repo checkpoint 选择：统一用 last-epoch checkpoint（eval_loss=NaN 导致无法 val-select）
- 论文数字更新前必须 Reviewer 确认——之前出过 M002（cross-model baseline 错误用了不同模型的 zero-shot 做 delta）
- cwm-repo-s123 (cuda:3) 训练可能仍在跑（cron 曾误报 failed），操作前先确认 PID 存活

### 2. 🖥️ 基础设施快照
- **seetacloud**: connect.westd.seetacloud.com，工作目录 /home/sonny/exec-sim-repair-verifier，checkpoint 在 /root/autodl-tmp/
- **home-1x5090**: home 服务器，1 张 RTX 5090
- **本地 paper 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/
- **Overnight 进程（seetacloud）**:
  - cuda:0: DeepSeek CLS v4 (s42) eval, checkpoint-4422, seq8192, tmux session 待确认
  - cuda:1: DeepSeek CWM (s42) eval, best checkpoint, tokens512, PID 662946
  - cuda:2: DeepSeek CLS (s123) eval, best checkpoint, seq8192
  - cuda:3: DeepSeek CWM (s123) 训练 ~72%, PID 542906（cron 标记 failed 但可能仍存活）
- **home GPU**: 空闲，Agent 被派去跑 M001 TRAJ 重验证但 Agent session 出错未返回

### 3. 📊 当前状态
**刚做完**: 修复 DeepSeek eval 配置（CLS seq8192 + CWM tokens512），重启 4 个 eval，确认 0% unparseable。Table 2 新增 TRAJ column（方案 B: 2 matched seeds）。Review issues 15/18 resolved。

**RUNNING**: 4 个 seetacloud overnight eval（预计 8-15h，明早出结果）

**等待中**:
- 4 个 DeepSeek repo eval 结果（blocking Table 4 + C2 narrative + 剩余 3 个 review issues）
- Agent session 出错需重试（最后一条 "Agent 未返回任何回复"）
- Home GPU 上 M001 TRAJ 重验证可能未启动（因 Agent 出错）

### 4. 📋 待办
- **DeepSeek CLS eval 完成** → 收集 accuracy + unparseable rate → 确认 ~80%（running acc） → post_to_reviewer 审查
- **DeepSeek CWM eval 完成** → 收集 accuracy + unparseable rate + parseable-only accuracy → 这是 Path A/B 决定性数据：如果 CWM unparseable 高 + accuracy 低 → Path A (tokenizer-specific divergence)；如果 CWM 表现尚可 → Path B (model-agnostic)
- **4 个结果齐全** → 填 Table 4 DeepSeek 行 → Paper Agent 更新 Abstract/Intro/Conclusion → 提交 Round 2 审稿
- **Home GPU 空闲** → 安排 M001 TRAJ 重验证（DeepSeek TRAJ func-level，确认 84.16±1.30%）
- **cwm-repo-s123 训练完成** → 用 last-epoch checkpoint eval（与 s42 策略一致）
- **所有结果到手 + paper 更新完** → submit_paper_to_review 提交 Round 2

### 5. 🎯 战略上下文
- **D116 framing**: "Design space characterization"（中性），不是 CLS advocacy
- **C2 claim**: complexity-dependent CWM divergence。Qwen3 已证实（repo-level CWM 58-65% vs CLS 83-85%）。DeepSeek 结果决定是 tokenizer-specific (Path A) 还是 model-agnostic (Path B)。两条路都能写，但叙事力度不同
- **Table 2 已改为方案 B**（2 matched seeds 42/123 across all 3 formulations）。数字：CLS +1.27pp, CWM -0.03pp, TRAJ +1.70pp。CWM 是唯一不 scale 的 formulation
- **易错点**: (1) DeepSeek eval 参数必须与 Qwen3 对齐——已出过 M003；(2) CWM repo checkpoint 选择用 last-epoch 不是 val-best；(3) seetacloud 有进程被系统 kill 的历史（cls-v4 epoch 3 eval 被杀，cwm-s123 cron 误报）；(4) 跨模型 delta 计算必须用同模型 baseline（M002 教训）
- **DDL**: EMNLP ARR May 25，剩 8 天。DeepSeek 结果是唯一 blocker


---
