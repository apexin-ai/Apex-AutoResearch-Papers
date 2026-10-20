# director / loop_3.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`9a57945e9ea75ffae151.json`](../../sessions/9a/9a57945e9ea75ffae151.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-14T02:33:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- **C001**: 所有实验统一使用 `data/train_500_seed42.jsonl`，禁止 `proofwriter_fol_500.jsonl` 或其他数据文件（多 seed 对比 confound 事故）
- **C002**: 提交训练前必须 `export CUDA_VISIBLE_DEVICES=N` 显式设置，禁止 inline 赋值 `bash -c VAR=X cmd`，提交后 `nvidia-smi` 验证（两次 GPU 越界事故）
- **C003**: 训练配置必须 `save_total_limit=1` + 限制 completions parquet，磁盘只有 250G（plan013-r3 和 plan001-s43-r3 磁盘满崩溃）
- GPU 只能用 cuda:0 和 cuda:1（westd-39279 分配内）

### 2. 🖥️ 基础设施快照
- 服务器：`westd-39279` (connect.westd.seetacloud.com)，2× RTX PRO 6000 96GB
- 工作目录：`/root/solver-trace-ablation`
- 弹性 GPU 未启用，W&B 未配置，Git 未配置
- 活跃进程：plan002-additive-b03-s42（应在 cuda 上）、plan001-exec-only-s43-r4（应在另一张 cuda 上）——但 Agent 已 idle 180min，需要 SSH 确认这两个实验是否仍在跑或已结束未回调

### 3. 📊 当前状态
- **阶段**: Research + 审稿进行中（review_chat_id 已配置）
- **RUNNING (2)**: plan002-additive-b03-s42（additive bonus β=0.3）、plan001-exec-only-s43-r4（exec-only baseline 第4次重试）
- **关键完成实验**: plan_003 消歧完成（Interpretation B confirmed: 50/50 STA = penalty effect）、plan_005 低权重 STA negative、plan_013 random reward baseline success
- **总计**: 26 实验，6 success / 4 negative / 14 failed / 2 running
- **Agent idle 180min**: 两个 RUNNING 实验可能已完成但未回调，新 Agent 启动后首要任务是检查这两个实验状态
- **DDL**: EMNLP ARR 2026-05-25（剩 11 天）

### 4. 📋 待办（条件触发式）
- plan001-exec-only-s43-r4 完成 → 分析 prove_rate/ISR，如果终于成功则 exec-only baseline 确立
- plan002-additive-b03-s42 完成 → 对比 exec-only baseline，验证 additive bonus 公式是否优于凸组合
- 两者都完成 → 启动 plan_003 式 held-out eval 对比两个 checkpoint
- plan_001 若第4次仍 failed → 紧急诊断，考虑是否 pipeline 有根本问题（kill criteria D004: 3-seed mean PR <25% AND slope ≤ 0）
- 两张 GPU 空闲时 → 立即铺 plan_014（downstream validation，打破 ISR circularity）或 plan_006（Prolog 扩展）
- Paper Agent 待指令：related work 扩充 + RIP reframing + story 转向（STA as metric + proper integration）

### 5. 🎯 战略上下文
- **核心 story 转向 (D008-D011)**: "STA detects hacking" → "STA as principled structural metric + proper integration"。50/50 凸组合已证明是 penalty（D007-D008），新方向是 additive bonus `r = r_exec · (1 + β·ISR)`
- **Dream 审稿 5 个结构性问题**: (1) related work 不足 6→25+ (2) RIP framing 过度 (3) ISR circularity (4) single-seed (5) ISR sparsity/"dense+automatic" 不成立。这些是跨三档一致问题，必须全部解决
- **最容易判断错的事**: plan_001 已 failed 3 次（之前因数据不一致 C001、GPU 越界 C002、磁盘满 C003），第4次如果还 fail 不要轻易放弃——先确认是基础设施问题还是真的 pipeline 问题
- **决策链**: D001(MVP)→D002(调整)→D003(full STA)→D004(penalty发现)→D005-D006(消歧)→D007-D008(Dream+Interpretation B)→D009(约束)→D010-D011(framing转向+Narrative A+C)→D012(additive random对照)
- **14/24 实验 failed**: 大部分是基础设施问题（数据 confound、GPU 冲突、磁盘满），不是方法论失败。三个约束 C001-C003 已修复这些问题


---
