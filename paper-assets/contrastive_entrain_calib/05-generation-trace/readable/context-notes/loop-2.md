# director / loop_2.md

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`bc4337ed28b8e202275a.json`](../../sessions/bc/bc4337ed28b8e202275a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-22T18:50:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- **28034 RTX 5090 32GB 不能跑任何 Qwen3-8B GRPO 实验**（M026/M027）。只能跑 SFT 和 eval。GRPO 需要 ≥48GB（29046 96GB 卡）
- **启动训练前必须 `pgrep -f &lt;script>` 检查现有进程**——已两次出现重复进程（M025 ACT s2, M027 gs8），导致 checkpoint 污染和 step time 暴涨
- GPU 白名单：westd-29046 cuda:0/1, westd-28034 cuda:0/1/2/3。不要用其他服务器的卡
- **DDL: EMNLP 2026 ARR May 25**。所有决策以此为锚

### 2. 🖥️ 基础设施快照
- **29046** (2x 96GB): 工作目录 `/root/contrastive_entrain_calib`
  - cuda:0: exp-003-gs8 训练（PID 516696, ~step 200+/8000, 24.5s/step）
  - cuda:1: exp-004-s2-v2 ACT s2 训练（step ~4800/8000, 9.1s/step, ~May 23 02:00 完成）
- **28034** (4x 32GB RTX 5090): 工作目录 `/root/contrastive_entrain_calib`
  - cuda:1: exp-004-reduced-lora SFT 训练（~step 10/8000, 7.2s/step, ~May 23 09:00 完成）
  - cuda:0/2/3: ACT s2 eval pipeline 轮流跑（ckpt-5000 在 GPU0 eval 中）
- **westb-13953**: 认证失败，不可用，Agent 正在检查连通性
- 论文路径：`projects/contrastive_entrain_calib/docs/paper/main.tex`（11 页，正文 8 页）
- Eval preset: D027 unified preset

### 3. 📊 当前状态
**刚完成：**
- Paper Agent Batch 10: R3-only s2 完整数据 + reliability gap 更新（4/28=14.3% vs ACT 24/24=100%）
- R3-only s2 16/16 eval 全部完成（1/16 > vanilla = 6.3%）
- Kill 28034 上两个 OOM 实验（exp-003-len512, exp-003-s3）
- Kill 29046 GPU0 上 duplicate gs8 进程 + eval 争 compute 进程

**RUNNING 实验：**
- exp-003-gs8: gs=8 R₃-only GRPO（29046 cuda:0, step ~200/8000）— THE decisive experiment
- exp-004-s2-v2: ACT seed 2 训练恢复（29046 cuda:1, step ~4800/8000）
- exp-004-reduced-lora: ACT reduced LoRA 控制实验（28034 cuda:1, step ~10/8000）

**等待中：**
- ACT s2 ckpt-5000 eval Worker 回调（28034 GPU0）
- westb-13953 连通性检查 Worker 回调
- 用户回复：是否提供额外 96GB GPU 服务器（用于 len512 和 s3）
- gs8 ckpt-500 eval 约 ~2h 后可用

### 4. 📋 待办
- gs8 ckpt-500 出来 → 立即 eval，对比 gs=2 ckpt-500（0.105-0.116）。如果明显不同 → 强证据，如果相似 → 等 ckpt-1000+
- exp-004-s2-v2 完成（~May 23 02:00）→ 29046 cuda:1 释放 → 立即启动 exp-003-len512（mcl=512 R₃-only）
- exp-003-gs8 完成或足够 checkpoints → 29046 cuda:0 释放 → 启动 exp-003-s3（seed 3）
- 用户提供新 96GB 服务器 → 立即在新卡上并行启动 len512 + s3
- exp-004-reduced-lora 完成（~May 23 09:00）→ eval all checkpoints → 如果 reduced-LoRA ACT 也成功 → supervision granularity（per-token SFT）是关键因素，不是 LoRA capacity
- gs8 + reduced-lora 数据都到 → Paper Agent Batch 11 集成 + 标题加 scope qualifier → 编译 → Round 6 submit_paper_to_review

### 5. 🎯 战略上下文
- **论文核心 story**: d_syc 有高 discriminability（AUROC 0.827）但作为训练 reward 失败。C2（Probe Reward Trap）是 primary contribution（SFT 设定，独立于 GRPO confound），C1（GRPO failures）是 conditional observation
- **5 轮审稿分数轨迹**: 2.5 → 3.0 → 3.0 → 3.0 → 3.0。纯文本/framing 修复已到 ceiling，突破需要数据
- **gs=8 是 THE pivotal experiment**: 如果 gs=8 也失败 → d_syc 作为 GRPO reward 确实不行（C1 成立）；如果 gs=8 成功 → gs=2 是 confound（C1 需大改但 C2 不受影响）
- **review_issues.yaml 20+ issues tracked**。Round 5 文本修复大部分由 Batch 9/10 完成，标题 scope qualifier 待 gs8 数据后修
- **易错点**: (1) 不要在 32GB 卡上启动 GRPO (2) 启动训练前必须检查无重复进程 (3) eval 不要和训练跑在同一张 GPU 上（会 2.6x 减速）(4) 论文的 "4/27" 已全部更新为 "4/28"，不要回退
- **决策链**: D055(取消 ablation) → D056(C2 primary pivot) → D057(gs=8) → D058(len512+reduced-lora+s3) → D059(重定向 GRPO 到 96GB)


---
