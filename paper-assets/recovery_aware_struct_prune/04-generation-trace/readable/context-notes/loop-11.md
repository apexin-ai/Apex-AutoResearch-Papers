# director / loop_11.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_11.md`
- **Structured JSON:** [`ddbb134623d9314df95b.json`](../../sessions/dd/ddbb134623d9314df95b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_messages
updated: '2026-05-16T21:05:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单（C004）：westb-23072 cuda:0/1 + westd-11672 cuda:0/1/2/3（共 6 张），严禁越界
- GRPO save_steps=100（不是 5！7B 模型每 checkpoint 25GB，save_steps=5 撑爆磁盘）
- eval_gsm8k.py 用 CUDA_VISIBLE_DEVICES 环境变量（不支持 --gpu）；sft_recovery.py 用 --gpu 参数
- Qwen Math 模型必须设 eos_token_id=[151643, 151645]
- westb↔westd 无 SSH key 互信，scp 不通
- Calibration 不一致已决定不重跑（D046）：DeepSeek cal=512, Qwen-Math cal=256，论文加 footnote
- eval_grpo_standard_25 曾加载错误模型（grpo_standard_25_qwen_math 而非 grpo_standard_25）——Reviewer 已发现，urgent 已发但 Agent 死前可能未修复，接手后第一件事验证

### 2. 🖥️ 基础设施快照
- westb-23072: connect.westb.seetacloud.com:23072, root, /root/recovery_aware_struct_prune
- westd-11672: connect.westd.seetacloud.com:11672, root, 密码 p1IO5kjrDeYv, 4×RTX PRO 6000 96GB
- Python: /root/miniconda3/bin/python（aml-train 镜像，conda base）
- 模型/数据/输出: /root/autodl-tmp/recovery_aware_struct_prune/
- HF cache: /root/autodl-tmp/.hf_cache
- grpo_rasp_25 checkpoint: westb `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25`
- grpo_standard_25 checkpoint: westd `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25` (11GB, May 17 03:15)
- wandb 日志通过 symlink 写到 /root/autodl-tmp/（根分区空间极小）
- Agent 本 session 反复死亡（idle 240min 触发 reset，共 7+ 次），处理 1-2 条消息后就停

### 3. 📊 当前状态
**应已完成（启动后 8-12h，需 SSH 确认）：**
- eval_grpo_rasp_25 (westb cuda:0, N=1319) — interim 122/1319 时 acc≈52%，应已完成
- inference speedup benchmark (westb cuda:1, plan_016) — 1 GPU-hour 任务
- alpha ablation Phase B (westd cuda:2/3) — α=0.0 done (70%), α=0.3 在做 SFT (61%训练中), α=0.5-2.0 并行部署中
- eval_pass_k8_standard_20_grpo_qwen_math (westd cuda:2)

**可能未修复：**
- eval_grpo_standard_25 (westd cuda:1) — Reviewer 发现在跑错模型，urgent 已发但 Agent 可能没执行修复

**已确认完成：**
- grpo_rasp_rlvr_20_qwen_math: reward=0.090, frac_zero=0.70, eval accuracy=71.0% (N=200)
- grpo_standard_25: reward=0.0075, near_total_collapse
- grpo_rasp_25: frac_zero=0.875, reward=0.009
- eval_sft_rasp_25: 52.99% (N=1319)
- grpo_rasp_rlvr_20 (DeepSeek, westb): OOM crash step 16, D050 决定不重跑

### 4. 📋 待办（条件触发式）
- 接手第一件事 → SSH 确认 eval_grpo_standard_25 是否跑了正确模型，如果仍在跑错的 → kill + 重启正确版本
- eval_grpo_rasp_25 结果到手（预期 ~52%） → 与 SFT 52.99% 对比确认 C1 在 25% 成立
- eval_grpo_standard_25 正确结果到手（预期 ~51%） → C1 25% 完整验证
- alpha ablation 全部完成 → 整理 α vs accuracy 曲线，写入论文（Dream Critical，0 分析 = 审稿必打回）
- 所有关键数据到齐 → paper_framing.md 大改写（align D048-D050: C1 主锚 + C2 severity gradient + C3 降级 + RLVR ablation）
- paper_framing 改写后 → director_post_to_paper_agent 发 Reframe 指令（C1 "training signal quality is uninformative of downstream performance" 为核心 claim）
- inference speedup 结果到手 → 填入论文 practical motivation

### 5. 🎯 战略上下文
- **论文定位 (D048-D050)**：solid diagnostic paper。C1 (universal reward-accuracy decoupling) 是唯一强 claim，现在有**双向证据**——collapse 不伤 accuracy（Standard: worst metrics, ok accuracy）+ 好 dynamics 不提分（RLVR: best metrics, same accuracy）。
- **C1 升级表述**："GRPO training signal quality is uninformative of downstream performance for pruned models"（比原来的 "collapse is cosmetic" 更强更 general）
- **DDL**: ARR May 25, 2026（~8 天）
- **最容易判断错的事**：
  1. Agent 报 RLVR reward=0.090 是 "成功" — 不是，accuracy 71% ≈ SFT 73% = 不提分
  2. eval_grpo_standard_25 可能跑的是 Qwen-Math 版本（63.5%）而非 DeepSeek 版本（预期 ~51%）——必须验证 model_path
  3. Alpha ablation α=0.0 accuracy=70% 是 Qwen Math N=200 post-prune（无 CKA 项 = pure importance），不是 SFT recovery 后的结果
  4. Agent 持续 idle 死亡是系统性问题，不是偶发——发消息后预期 4h 内可能需要再次 reset
  5. C2 在 DeepSeek 上成立（Standard collapse > RASP），但 Qwen-Math 上方向一致但 recovery dynamics model-dependent
- **用户态度**：已授权"你和 Reviewer 一致觉得没问题就做，并行去做"——不用逐个请示
- **Paper Agent**: Step 4 完成，等 Reframe 指令（需 paper_framing.md 先改写）


---
