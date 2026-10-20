# director / loop_9.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`3e8f50c8058ed867671a.json`](../../sessions/3e/3e8f50c8058ed867671a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-16T16:26:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单（C004）：westb-23072 cuda:0/1 + westd-11672 cuda:0/1/2/3（共 6 张）
- RASP-RLVR 是全项目最高优先级实验（用户明确指示）
- Calibration 不一致已决定不重跑（D046）：DeepSeek cal=512, Qwen-Math cal=256，论文加 footnote
- eval_gsm8k.py 用 CUDA_VISIBLE_DEVICES 而非 --gpu 参数；sft_recovery.py 用 --gpu 参数
- Qwen Math 模型必须设 eos_token_id=[151643, 151645]（eval 脚本已硬编码修复，generation_config.json 也需要改）
- GRPO save_steps=100（不是 5！7B 模型每 checkpoint 25GB，save_steps=5 会撑爆磁盘）
- wandb 日志通过 symlink 写到 /root/autodl-tmp/（根分区空间极小）
- westb↔westd 无 SSH key 互信，scp 不通

### 2. 🖥️ 基础设施快照
- westb-23072: connect.westb.seetacloud.com:23072, root, /root/recovery_aware_struct_prune
- westd-11672: connect.westd.seetacloud.com:11672, root, 密码 p1IO5kjrDeYv, 4×RTX PRO 6000 96GB, 500GB 数据盘
- Python: /root/miniconda3/bin/python（aml-train 镜像，conda base）
- 模型/数据/输出: /root/autodl-tmp/recovery_aware_struct_prune/
- HF cache: /root/autodl-tmp/.hf_cache
- 磁盘: westb 212/250GB (85%), westd 268/750GB (36%)
- 活跃进程（截至 handoff）：
  - westb cuda:0: eval_sft_rasp_25 (PID 602990, N=1319, 接近完成)
  - westb cuda:1: eval_sft_rasp_rlvr_20 (PID 625453, N=1319, ~353/1319 27%, acc interim 60.57%)
  - westd cuda:0-3: post-GRPO eval ×4 (Qwen Math, N=200, 即将完成) → cuda:0 接 RLVR pipeline

### 3. 📊 当前状态
- **Dream 已完成并分析**：best=4/6, median=3/6, worst=3/6。#1 致命弱点是 pass@k 缺失，#2 是 RLVR 未完成
- **pass@k 脚本已开发完成**（eval_gsm8k.py 支持 --pass_k --num_samples_per_prompt），等 GPU 释放后跑
- **Qwen Math GRPO 全部完成**：20% 双方 collapse（Standard 更严重），25% RASP 稳定 vs Standard KL 爆炸(4M)
- **Post-GRPO eval 初步结果**：C1 decoupling 跨模型确认（GRPO 既没帮也没伤，SFT→GRPO accuracy 无变化）
- **关键发现**：collapse 方向是 model-dependent（DeepSeek: RASP 更差; Qwen Math: Standard 更差），RASP-RLVR 是 tiebreaker
- **Paper Agent**：Step 4 完成，预写了 RLVR 框架，等数据 Patch 后进 Step 5
- Agent 队列已清空，RESET_BOTH 已批准

### 4. 📋 待办（条件触发式）
- eval_sft_rasp_rlvr_20 完成 → 记录 accuracy → **立即启动 grpo_rasp_rlvr_20**（westb cuda:1, save_steps=100, 同 DeepSeek GRPO 参数）→ 这决定论文是 "diagnosis only"(3/6) 还是 "diagnosis + remedy"(5/6)
- eval_sft_rasp_25 完成 → 记录 25% RASP full accuracy → 对比 Standard 25% (已出 51.25%)，更新 paper_framing.md evidence table
- post-GRPO eval ×4 完成 → 记录结果 → westd cuda:0 启动 Qwen Math RLVR pipeline（prune rasp-rlvr → SFT → eval → GRPO）
- westd cuda:1-3 释放 → 立即跑 pass@k=8（N=200, temp=0.7）：cuda:1 unpruned post-GRPO, cuda:2 RASP 20% post-SFT, cuda:3 RASP 20% post-GRPO → 对比回答 Dream Q1
- grpo_rasp_rlvr_20 完成 → **关键判断点**：collapse onset > step 60? → 论文升级 "diagnosis + remedy"；collapse 仍早 → 重新评估贡献 viability
- 所有 RLVR + pass@k 数据到齐 → 更新 paper_framing.md → 通知 Paper Agent Patch（一次性：25% + RLVR + Qwen Math + pass@k）→ 进 Step 5 Refinement
- DeepSeek 25% GRPO (grpo_rasp_25 + grpo_standard_25)：这波完成后重新提交到 westd

### 5. 🎯 战略上下文
- **核心叙事演化**：从 "RASP > Standard" 简单对比 → 升级为 "Redundancy-Stability Threshold Framework"。不同模型需要不同量的冗余保护；RASP-RLVR 是 universal remedy
- **Dream 路径到 5/6**：需要 (a) RLVR 成功防止 collapse, (b) pass@k 证明 decoupling 不是 greedy artifact, (c) 多 seed / 更长 GRPO（200-500 步）, (d) 收窄 "universal" claim
- **eval_sft_rasp_rlvr_20 interim 60.57%**：与 RASP(61.49%) 和 Standard(59.29%) 在同一水平，SFT 恢复正常。真正的测试是 GRPO 阶段
- **最容易判断错的事**：(1) eval_sft_rasp_25 速度极慢（模型生成长 response），不是 bug 不要 kill; (2) Qwen Math 模型 EOS 问题已修（eval 脚本 + generation_config），但新模型仍需检查; (3) Agent 之前多次混淆 bash wrapper PID vs Python PID，kill 时用 `kill -9` 或确认实际 python 进程
- **DDL**：ARR May 25, 2026（~9 天），时间充裕但 RLVR 是 critical path
- **用户态度**：已授权"你和 Reviewer 一致觉得没问题就做，并行去做，保证质量提高效率"——不用逐个请示


---
