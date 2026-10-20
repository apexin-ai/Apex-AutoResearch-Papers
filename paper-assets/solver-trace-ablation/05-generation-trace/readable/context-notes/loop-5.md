# director / loop_5.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`b7c77df90598c5370081.json`](../../sessions/b7/b7c77df90598c5370081.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-15T11:30:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0 和 cuda:1（gpu_ids 白名单）
- eval 必须用 `--data_path data/proofwriter_fol_100.jsonl`（C008/C009），by_answer_type 分布必须是 34/25/41，否则数据集错误
- Resume 训练时必须验证步数语义（C012）：不确定 train_grpo.py 的 resume 行为就从 base model 重新训练，禁止第三次犯 resume 步数不对等错误
- save_total_limit=1 必须设置，磁盘 250G 已多次因 checkpoint 堆积爆满
- ISR β=0.1 s42 genuine_rate：registry 中 fraction of proved (25/81=30.9%)，不要与 fraction of total 混淆
- plan013 vs plan017 公式结构不同，不可简化为 "additive vs convex" 对照 (D027)

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/solver-trace-ablation
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base 环境）
- 模型：Qwen3-4B（base model 路径由训练脚本自动拉取）
- 数据：/root/solver-trace-ablation/data/train_500_seed42.jsonl（训练），data/proofwriter_fol_100.jsonl（eval）
- outputs：/root/autodl-tmp/outputs/（磁盘 142G used / 109G avail，57%）
- 活跃进程：
  - exp1-isr-b03-s42-1000-r2：训练已完成，eval 待出（GPU 0 空闲）
  - plan018-additive-random-b01-s42-1000-r3：RUNNING on cuda:1（约 step ~200/1000，从 base model 干净训练）

### 3. 📊 当前状态
**刚做完**：
- Wilson CI 3-seed 分析定稿：ISR β=0.1 genuine ≈ Random (17.3% vs 17.4%, p=1.0)，D073
- SFT 3-seed pooled：genuine=91.3% [79.7, 96.6]，已更新到论文全部 7 处
- ISR β=0.1 1000步 eval：H7=92.2%, genuine=3.0%，temporal Goodhart collapse 已写入 §4.2
- Paper Agent 完成多轮 patch：Wilson CI narrative + SFT 3-seed + 1000步 temporal + plan004 O(1) ablation 修正
- 磁盘爆满事故处理：清理 139GB，两实验恢复

**RUNNING**：
- plan018-additive-random-b01-s42-1000-r3（Random β=0.1, 干净 1000 步, cuda:1）— **审稿提交最后 blocker**
- exp1-isr-b03-s42-1000-r2（ISR β=0.3, 1000 步, cuda:0）— nice-to-have，训练完成 eval 待出

**等待中**：
- plan018-r3 完成 → eval → 三方 1000 步对比表 → Paper Agent patch → recompile → submit_paper_to_review
- exp1-b03-s42-1000-r2 eval 回调

### 4. 📋 待办（条件触发式）
- plan018-r3 训练完成 → eval（proofwriter_fol_100.jsonl）→ classify_h7 → 汇报 Director
- plan018-r3 eval 出来 → 构建 1000 步三方对比表（exec-only vs ISR β=0.1 vs Random β=0.1）→ Paper Agent patch §4.2 temporal section
- exp1-b03-s42-1000-r2 eval 出来 → β 剂量×时间交互数据（β=0.1 collapse at step 850 vs β=0.3 collapse at step 370）→ 如有价值 Paper Agent patch
- 两个 1000 步实验都完成 → recompile 论文 → submit_paper_to_review（用户已要求"合适时机审稿"）
- GPU 0 空闲 → 如无其他实验需求，可跑 compile worker 或等 plan018-r3 完成后释放

### 5. 🎯 战略上下文
**核心结论**：ISR 作为诊断工具有效（检测 reward hacking），但作为 reward 信号是 Goodhart 失败案例。ISR genuine rate 与 random 完全一致 (p=1.0, D073)，ISR 唯一独特效应是 H7 gaming (64.5% vs 0%)。SFT 零 gaming (91.3%) 证明 hacking 是 GRPO/RL 特异性现象。

**关键决策链**：D057(Claim 2 闭环) → D059(Claim 3 闭环) → D071/D072/D073(Wilson CI 数据完整性修正) → D074(1000步 temporal Goodhart)

**易错点**：
- Bootstrap CI p=0.637 的**结论**是对的（genuine parity），但分类器有 bug。Wilson CI p=1.0 是正确方法得到的相同结论。不要引用 bootstrap 的具体数值，用 Wilson CI 的。
- plan018-r2 是 1350 步不是 1000 步（resume 错误），不可做定量对比，只能定性参考。r3 才是干净 1000 步。
- ISR β=0.1 跨 seed H7 异质性极大（s42=16%, s43=97%, s44=87%），论文需报告 per-seed + pooled，不能只报 pooled。
- 论文 DDL 2026-05-25，剩 10 天。审稿由独立 Group C 团队处理（review_chat_id 已配置），用 submit_paper_to_review 提交。
- Paper Agent session 已活跃，直接 director_post_to_paper_agent 即可，不需要新建。


---
