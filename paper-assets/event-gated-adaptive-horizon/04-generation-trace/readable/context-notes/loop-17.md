# agent / loop_17.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_17.md`
- **Structured JSON:** [`cf7f65a4ba6d5fc1d838.json`](../../sessions/cf/cf7f65a4ba6d5fc1d838.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: idle_timeout
updated: '2026-05-16T18:46:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 cuda:0 + cuda:1（bjb1-45299），禁止用其他卡
- 所有训练命令必须带 `LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl`
- MUJOCO_EGL_DEVICE_ID 必须与物理 GPU 对应（cuda:0→EGL_DEVICE_ID=0, cuda:1→EGL_DEVICE_ID=1），脚本内始终 `--device cuda:0`
- 018v2 NVE 裁决（D068）：两次 transient 超 1.5×（35K:1.61）不算 sustained CIVO，结论仍为"CIVO 消除"
- 016e 是 architectural no-op（reward gradient=0），不能声称 SGS delays collapse——该解读已撤回（D061）
- CoRL DDL 2026-05-29，剩余 13 天，不允许 fallback 到次级会议

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299，2×RTX PRO 6000
- 工作目录：`/root/autodl-tmp/event-gated-adaptive-horizon/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 日志目录：`~/runs/event-gated-adaptive-horizon/`
- logdir（metrics.jsonl）：`/root/autodl-tmp/event-gated-adaptive-horizon/logdir/&lt;exp_id>/`
- 代码 commit：`3328f53cb32cda27e85b099d560256aeb01db998`
- 活跃进程：
  - exp_020_vanilla_dreamerv3_s2: PID 596344, tmux session, cuda:0, cron 监控中
  - exp_008f_s3_no_dt_embed_walker: PID 601233, tmux session, cuda:1, cron 监控中

### 3. 📊 当前状态
两卡满载运行：
- **exp_020_vanilla_dreamerv3_s2** (cuda:0): Pathway B 控制实验——vanilla DreamerV3 seed 2，验证 008e_v3_s2 的 collapse 是否需要 trained dt_emb。提交于 16:45 UTC，105K steps。
- **exp_008f_s3_no_dt_embed_walker** (cuda:1): no_dt_emb 第 3 seed，闭合 bootstrap CI（当前 n=2 需 ≥3）。提交于 17:21 UTC，105K steps。

无等待中的 Worker 回调。2 个 cron 在监控上述实验（reconcile 确认 still running）。

排队实验：019b PickCube CIVO trigger（等 GPU 释放）。

### 4. 📋 待办（条件触发式）
- exp_020 完成 → 分析：若 vanilla s2 稳定（无 collapse）→ C6 成立（trained dt_emb 是 Pathway B 必要条件），更新论文 claim；若也崩溃 → Pathway B 是 DreamerV3 inherent fragility，需 limitation 讨论
- exp_008f_s3 完成 → 计算 3-seed bootstrap CI for no_dt_emb condition，更新 art_20260516_2b21be artifact
- 两卡释放后 → 立即提交 019b PickCube CIVO trigger（cuda:0）+ 追加 seed 实验或 019c StackCube（cuda:1）
- D064 非 GPU 任务（随时可铺）：Related work 扩展到 20+ refs、claim 语言审计（去 "necessary and sufficient"）、gradient decomposition methodology section 写作
- Bootstrap CIs 追加计算（010b Cheetah 数据已有，可 0-GPU 完成）

### 5. 🎯 战略上下文
- **核心结论链**：Trained dt_emb → CIVO (gradient-level: 93% obs decoder gradient)。018 Full-SGS 消除 CIVO (NVE 1.00×)。010b 跨环境验证 (Cheetah NVE 8.63×)。
- **论文 Framing B**：诊断论文 + SGS informative negative + Full-SGS proof-of-concept intervention
- **D064 Dream 审稿**：6 项结构性问题，018 已解决 D5/D7 部分，剩余 D1(seeds)/D3(language)/D4(refs)/D6(020 running)/D7(methodology)/D8(CIs)
- **易错点**：
  - 016e NVE 用 normalized 10.42×，不是 raw 6.59×
  - 009b peak 是 278.5@95K 不是 268.3@105K
  - 008a 是 "trained but unexposed"，不是 "untrained"——与 plan_017 相同，017 已取消
  - Gradient decomposition 随训练演化（55K: obs=25.8% → 105K: obs=93%），不能只报单一 step
  - NVE>1.5× 不是 CIVO 专属指标（008e_v3_s2 是 Imagination-Reality Divergence，AUROC 降为 7/8）


---
