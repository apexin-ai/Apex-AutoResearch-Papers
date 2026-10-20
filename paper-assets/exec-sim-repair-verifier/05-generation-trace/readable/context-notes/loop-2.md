# director / loop_2.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`62985df83bdcc8b1b238.json`](../../sessions/62/62985df83bdcc8b1b238.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-12T14:32:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：seetacloud cuda:0/1/2/3 + home cuda:0。westd-48478 是 seetacloud 的另一个 SSH 入口（同一台物理机），不是额外 GPU
- seetacloud 训练脚本中 **禁止** `os.environ["CUDA_VISIBLE_DEVICES"] = ...` 覆盖（已踩坑两次导致 OOM）。GPU 分配只通过 shell 层 CUDA_VISIBLE_DEVICES
- seetacloud 上 Qwen3-4B 本地路径：`/root/.cache/huggingface/hub/Qwen/Qwen3-4B`（不是 `/root/autodl-tmp/.hf_cache/` 下）。8B 在 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`
- 统计检验：论文只用 clustered bootstrap（D019），禁止引用 Welch's t-test "per-test 优于 traj" 结论（苹果比橘子）
- repo-level 训练 max_seq_length=4096（不是 2048），val 截断率 15.1% 已知但暂不处理

### 2. 🖥️ 基础设施快照
- **seetacloud-westd-4x5090**: connect.westd.seetacloud.com:48478 [root]，工作目录 /root/exec-sim-repair-verifier
  - Python: /root/miniconda3/bin/python (conda base)
  - 数据: /root/exec-sim-repair-verifier/data/swebench_full/ (89,867 records, 250 instances)
  - repo-level split: train 70,748 / val 9,335 (184/22/25 instances, class weights fail=1.66/pass=0.34)
- **home-1x5090**: implicit5638.xyfu.me [sonny]，工作目录 /home/sonny/exec-sim-repair-verifier
- 活跃进程（需 SSH 验证，session 间隔较长）：
  - repo-level-cls: seetacloud cuda:0（实际在物理 GPU 0，因历史 CUDA_VISIBLE_DEVICES bug）, ~1150/6633 steps
  - cwm8b-seed456: seetacloud cuda:2, PID 47236
  - repo-level-cwm: **被 SIGTERM 杀死** (EXIT_CODE=143, step 694/6633)，需重提交 cuda:3
  - cls8b-seed456: home cuda:0, PID 2810143，可能已完成（进入 eval 阶段）

### 3. 📊 当前状态
**刚做完**：5-paired CLS vs CWM bootstrap（seed-level p=0.0506 two-sided, sign test p=0.031, CI [+0.46, +2.04]）。5-paired CLS vs TRAJ TOST 等价通过 (p=0.007)。paper_framing.md 已更新 Claim 2 为 "Diagnostic Granularity At Equivalent Accuracy"。

**RUNNING**: repo-level-cls, cwm8b-seed456, cls8b-seed456（可能已完成）
**需重提交**: repo-level-cwm（被 kill，cuda:3 空闲）
**空闲 GPU**: seetacloud cuda:1（cwm-seed789 完成后未分配）, cuda:3（repo-level-cwm 死后）

**Agent 队列**: depth=5，包含我的 urgent 消息（repo-level-cwm 重提交 + GPU 空闲处理）和多个 Worker done 回调

### 4. 📋 待办
- repo-level-cwm 重提交到 cuda:3 → 检查有无 checkpoint 可 resume，确认 CUDA_VISIBLE_DEVICES=3
- cls8b-seed456 完成 → 更新 registry，释放 home cuda:0 → 分配新实验或待命
- cwm8b-seed456 完成 → 3-paired 8B scaling 分析（4B gap 1.25pp → 8B gap 预期 ~2.6pp）
- repo-level-cls + repo-level-cwm 都完成 → **Pillar 1 go/no-go 决策**：cls > cwm 则核心假设成立，否则 pivot 到 efficiency framing
- Reviewer 建议补 per-instance CWM predictions + clustered bootstrap → 加强 Claim 1（当前 two-sided p=0.0506 可被审稿人质疑）
- 所有实验完成后 → 更新 ROADMAP，评估是否进入写作阶段

### 5. 🎯 战略上下文
**三大 Pillar**：(1) Complexity-dependent advantage: cls scales better than CWM, 4B gap 1.25pp → 8B gap 2.60pp, repo-level 待验证; (2) Diagnostic granularity at equivalent accuracy: TOST p=0.007 已证明; (3) Oracle frontier: per-test advantage 集中在 T≥2 instances (31%)
**决策链**：D016 repo-level 训练 → D018 variant-level 等价发现 → D019 只用 clustered bootstrap → D020 TOST 通过恢复 "equivalent"
**最易判断错的事**：(1) per-test vs traj 的 2pp gap 是粒度假象，variant-level 等价，不要再 claim accuracy advantage; (2) seetacloud 上 4B 和 8B 模型路径不同，别搞混; (3) CWM 4B 有天花板效应 (std=0.37pp)，CLS 方差更大 (std=0.78pp)——4B gap 的不稳定性来自 CLS 不是 CWM
**repo-level 是决胜实验**：如果 repo-level cls > cwm，Pillar 1 成立，论文 story 完整。如果 null，需要 pivot 到 efficiency framing（same accuracy, 1-token vs N-token inference）


---
