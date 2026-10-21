# director / loop_17.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_17.md`
- **Structured JSON:** [`0c903aacc269d4df564d.json`](../../sessions/0c/0c903aacc269d4df564d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_messages
updated: '2026-05-21T23:53:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd cuda:0-3（4× RTX PRO 6000），westb cuda:0-1（2× RTX PRO 6000），共 6 张
- westb-westd 之间无直连网络，模型 checkpoint 不能 rsync/scp 跨服务器传输
- westb 磁盘紧张（清理后 ~37G），大模型操作优先用 westd
- eval_gsm8k.py 必须加 --max_new_tokens 2048，否则无 EOS 样本会 stall 6min+、VRAM 膨胀到 29GB。submit_training_job 包装器有 cron monitor 干扰 nohup 进程，复杂 eval 用 nohup 绕过
- C1 decoupling 判定标准已锁定（D101）：|Δ|≤2pp=universal, 2-5pp=predominant, >5pp=conditional

### 2. 🖥️ 基础设施快照
- **westd-29022**: connect.westd.seetacloud.com, /root/recovery_aware_struct_prune, aml-train 镜像（conda base）
- **westb-23072**: connect.westb.seetacloud.com, /root/recovery_aware_struct_prune, aml-train 镜像（conda base）
- Python: /root/miniconda3/bin/python（conda base，不用 venv）
- 模型 checkpoint 主要在 westd:/root/recovery_aware_struct_prune/outputs/ 下各子目录
- HF cache: /root/autodl-tmp/.hf_cache（两台都有）
- 活跃进程（reset 前快照）：
  - westd:0 — eval_gsm8k_sft_alpha4_20_v4 PID 426306（应已完成或接近完成，~23:27 UTC 预估）
  - westd:1 — eval_math500_grpo_random_20_v2（484/500，应已完成）
  - westd:2 — eval_math500_grpo_alpha4_20（~55% → 预计 ~01:00 UTC）
  - westd:3 — eval_math500_sft_random_20（206/500，预计 ~00:30 UTC）
  - westb:0 — 空闲（磁盘已清理到 37G）
  - westb:1 — eval_math500_sft_standard_25 PID 104592（跑了 7h40m）+ eval_math500_sft_cka_only_20_v6 PID 118095（206/500）

### 3. 📊 当前状态
**刚做完**：
- D101 决策：C1 decoupling 初步确认为 universal（α=4.0 Δ=-0.16pp @550/750 samples）
- CKA-only 25% MATH-500 从 log 恢复：SFT=19.2%, GRPO=18.4%
- GPU 碰撞修复（westd:0 误提交 standard_20 被 kill）
- westb 磁盘清理（14G→37G）
- D099 narrative shift：从 "CKA-only best" 到 "CKA diversity is key signal, CKA-only most robust"

**RUNNING/PREPARING**：
- eval_gsm8k_sft_alpha4_20_v4 — RUNNING，D100 critical，应快完成
- eval_math500_grpo_alpha4_20 — RUNNING，α=4.0 MATH-500 interim 27.2%
- eval_math500_sft_random_20 — RUNNING
- eval_gsm8k_grpo_alpha4_20_v2 — PREPARING，等 westd:0 空出提交（timeout=8h, --max_new_tokens 2048）
- eval_math500_grpo_standard_20_fair_2048 — PREPARING，等 westd:1 空出提交（P0 数据缺口）

**等待中**：Agent 刚 reset，需要新 session 接手上述任务调度

### 4. 📋 待办（条件触发式）
- eval_gsm8k_sft_alpha4_20_v4 完成 → 读取 full N=1319 accuracy，与 GRPO 62.93% 比较，确认 C1 universal → westd:0 立即提交 eval_gsm8k_grpo_alpha4_20_v2
- westd:1 空出（random GRPO 应已完成）→ 立即提交 eval_math500_grpo_standard_20_fair_2048
- 全部 MATH-500 eval 完成 → 汇总 20%/25% × SFT/GRPO × 5 criteria 的完整表格 → dispatch Paper Agent MATH-500 table patch
- α=4.0 GSM8K 全量结果确认 → dispatch Paper Agent 综合 RASP paragraph rewrite（D099 narrative + α sensitivity + C1 universal）
- 所有 patch 完成 → submit_paper_to_review Round 6
- westb:0 空闲 → 查 westb 本地有哪些 checkpoint，安排可用 eval 填空

### 5. 🎯 战略上下文
- **DDL**: EMNLP 2026 ARR May 25（~3 天）
- **核心发现演变**：CKA-only >> others → CKA-only ≈ RASP(α=4.0) >> Standard >> RASP(α=1.0) >> Random。α 是 dose-response 变量，提供准因果证据
- **C1 Decoupling**（D101 初步 universal）：所有 pruning criteria × sparsity 的 |GRPO-SFT| < 2pp。论文可用 "universal" 表述
- **Paper Agent D098**：Round 5 审稿 15 个 issue（N1-N2 critical, W1-W5 warning），大部分 in_progress。selfhealing2025 bib 已修复。Round 6 需要等 MATH-500 + α=4.0 narrative patch 后提交
- **易错点**：
  1. eval_gsm8k.py 不加 --max_new_tokens 会 stall，已踩坑 3 次（v1/v2/v3 都因此失败或超时）
  2. westb-westd 不通网，别尝试跨服务器传模型
  3. Registry 容易漂移（状态不对），处理 worker:done 后验证 registry 状态
  4. Round 4 审稿 approval (apr_20260521T145013_qbke) 仍 pending 用户审批
  5. review_issues.yaml 有 Round 5 的 15 个 issue 需要随修复进度更新状态


---
