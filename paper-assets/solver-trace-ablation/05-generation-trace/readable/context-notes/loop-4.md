# director / loop_4.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`fb596329dca50ab3b04e.json`](../../sessions/fb/fb596329dca50ab3b04e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-14T05:21:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-39279 的 cuda:0 和 cuda:1（C002/C005: 任何 Python 进程启动前必须 `export CUDA_VISIBLE_DEVICES=N`，禁止 inline 赋值，否则会越界占用另一张卡）
- 训练数据统一 `data/train_500_seed42.jsonl`（C001），禁止用 proofwriter_fol_500.jsonl
- 训练配置必须 `save_total_limit=1` + 限制 completions parquet（C003，磁盘只有 250G）
- 跨 seed/跨 run ISR 对比必须用 eval_sta.py 统一评估（C004），禁止引用训练日志 ISR
- DDL: ARR May 25, 2026（剩 11 天）

### 2. 🖥️ 基础设施快照
- 服务器: westd-39279 (connect.westd.seetacloud.com)，账号 root
- 工作目录: /root/solver-trace-ablation
- GPU: 2 × RTX PRO 6000 96GB（cuda:0, cuda:1）
- 当前两卡均空闲，无 RUNNING 实验
- 模型/数据在服务器本地，HF cache 未配置 wandb
- 活跃进程: 无（plan017-additive-random-s42 状态 ANALYZING，无活跃 PID）

### 3. 📊 当前状态
**29 个实验：success 6, negative 8, failed 14, analyzing 1**

本 session 完成的关键工作：
- **plan001 exec-only 3-seed 全部完成**: s42 PR=93%/ISR=0.64, s43 PR=14%/ISR=0, s44 PR=14%/ISR=0.21 → 跨 seed 极不稳定，s42 是 outlier
- **plan002 additive β=0.3 negative**: PR=18%, ISR=0.12 — additive bonus 没有帮助
- **plan013 random reward success（但 degenerate）**: held-out ISR=0.535 是 trivial 2-component proof 的 artifact
- **plan014 downstream NLI negative**: ISR 与 NLI accuracy 无相关（ρ=-0.049）→ ISR 降级为 syntactic metric，downstream 降级为 limitation
- **plan017 additive random control**: ANALYZING 状态，实际可能还没跑或正在等处理

**两张 GPU 空闲，违反"禁止空卡 >10min"红线，必须立即派实验。**

### 4. 📋 待办（条件触发式）
- plan017 ANALYZING 完成 → 对比 additive-random vs plan002 additive-ISR vs plan001 exec-only，判断 ISR signal 是否 > random noise
- 两卡空闲 → 立即从 planned 实验中选取派发（plan004 O(1) ablation / plan015 curriculum / plan016 extended training / plan006 Prolog 都可选）
- 如果 plan017 也 negative → 需要评估整个 additive bonus story 是否成立，可能需要第三次 framing pivot
- 论文审稿团队（Group C）在并行工作，注意 `submit_paper_to_review` 的时机

### 5. 🎯 战略上下文
**核心危机：P0 实验大面积 negative，论文 story 已 pivot 两次。**

决策链：
- D008: 50/50 凸组合是 penalty effect → 废弃旧公式
- D010/D011: framing 从 "STA detects hacking" → "STA as diagnostic + additive bonus"
- D014: GRPO 饱和 confound — random reward 也达高 PR
- D018: plan013 ISR=0.535 是 tautological artifact，不是真实信号
- D019-D022: ISR 重新定位为 syntactic component necessity，downstream 降级为 limitation

**最容易判断错的事**：
1. 不要被 plan001-s42 的 93% PR 误导——s43/s44 只有 13-14%，跨 seed 极不稳定，3-seed mean 才是真实水平
2. plan013 random reward 的 ISR=0.535 不代表 random reward 产生了好 formalization——是 trivial 2-component proof 的 artifact（mean components=2.04 vs exec-only mean=6.58）
3. additive bonus 公式 r=r_exec·(1+β·ISR) 看起来 sound 但 plan002 实际效果是 negative（PR=18%）——不要假设公式正确就一定 work
4. 11 天 DDL + 两卡空闲 = 必须立即行动，不能等 plan017 分析完再排下一批


---
