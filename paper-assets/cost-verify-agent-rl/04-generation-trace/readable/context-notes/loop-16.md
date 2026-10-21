# director / loop_16.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_16.md`
- **Structured JSON:** [`87b182a4b4f6f395b5a4.json`](../../sessions/87/87b182a4b4f6f395b5a4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_messages
updated: '2026-05-21T20:47:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-17606 cuda:0,1 + westd-47453 cuda:0,1,2,3，共 6 张，不可用其他服务器/卡
- westd 多实验并行必须 RAY_ADDRESS=local 隔离（M041/M043 教训：CUDA_VISIBLE_DEVICES 不隔离 Ray worker）
- 任何涉及 Ray/vLLM 的新进程启动前：ray stop + RAY_ADDRESS=local + CUDA_VISIBLE_DEVICES 三者缺一不可
- `qwen3_exp021_ragen_sft_v4` (SFT base model) 禁删——所有 seed 训练 + eval 依赖
- 修改 YAML config 对已运行的 verl 进程无效（启动时加载到内存）
- >10GB 删除操作需 Director 批准
- Eval 必须通过 submit_training_job 提交（避免 cron "process dead 5×" 误判，已发生 2 次）
- FSDP→HF 转换后 eval 需创建 qwen symlink（ctx_manager.py get_special_tokens 通过路径名匹配"qwen"）

### 2. 🖥️ 基础设施快照
- **bjb1-17606**: root@bjb1-17606, `/root/cost-verify-agent-rl`, 2× RTX PRO 6000 96GB, 磁盘 ~85GB free
- **westd-47453**: root@westd-47453, `/root/cost-verify-agent-rl`, 4× RTX PRO 6000 96GB, 磁盘 OK
- Python/conda: aml-train 镜像, `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- SFT checkpoint: `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4/`（两台都有）
- FSDP→HF 转换脚本: `scripts/convert_fsdp_to_hf.py`（两台都有）
- W&B project: cost-verify-agent-rl
- Watchdog: westd PID 118781, bjb1 PID 313318（step 10→删 step 5, step 15→删 step 10）
- **len_penalty 代码修改**: agent_trainer.py line 1543-1558 有 response length penalty 插入（coef=0.5, threshold=1000）。此修改对新实验有影响——如果不需要 penalty，需要 revert 或用未修改的 config

### 3. 📊 当前状态
**RUNNING 实验：**
- `exp029_seed7_high_kl` (bjb1 cuda:0,1, PID 334159, W&B d3z9u4f6): KL 10x 干预实验，step 5/7，预计 ~1h 完成。Reviewer 判断大概率也会失败（rollout resp_len=13169，val success=28.1% 零改善）
- `exp029_seed8` (westd cuda:2,3, PID 462991, W&B c0l6e7vd): step 9/15，已确认崩溃（train success 11%，resp_len 11569）。跑完收集负例数据

**空闲 GPU：**
- westd cuda:0,1: 完全空闲（len_penalty 已完成）
- 应安排 Seed 4 OOD eval（checkpoint 在 bjb1 `/root/autodl-tmp/checkpoints/exp029-seed4/global_step_15/`，需 FSDP→HF + scp 到 westd + qwen symlink + eval）

**已完成的 OOD 数据：**
- SFT baseline: 5.97% ✅
- Seed 1: 23.88% ✅
- Seed 3: 10.45% ✅
- Seed 5 (step 10): 29.10% ✅
- Seed 6: 29.10% ✅
- Seed 4: OOD 待做（collapsed seed）
- Seed 7/8: OOD 待做（collapsed seeds）

### 4. 📋 待办
- high_kl step 7 完成 → 提取 resp_len + success → 判断通过/失败 → 更新 registry + 通知用户
- high_kl 失败（大概率） → 两个 config-level mitigation 均失败，向用户汇报；考虑算法层面修改（length-normalized reward / response truncation / adaptive KL）或接受崩溃率调整论文 framing
- high_kl 成功（小概率，resp_len < 2000 且 success > 30%） → 用 kl_loss_coef=0.1 重跑崩溃 seed
- Seed 8 完成 → FSDP→HF + OOD eval（又一个 collapsed seed 数据点）
- Seed 4 OOD eval → 随时可做（westd cuda:0 空闲），需先 FSDP→HF 转换 + scp
- 所有 OOD 数据到齐 → 通知 Paper Agent 更新 Table 1 为 mean±std + 调整 claim 措辞
- 如果用户同意调整 framing → paper_framing.md 更新 + dream_simulate 验证新 framing

### 5. 🎯 战略上下文
- **论文核心**：step-independent agent RL 的双机制病理（M1 信息丢失 + M2 符号错误归因）+ episode-level 修复。目标 EMNLP 2026。
- **跨 seed 崩溃率 4/8 = 50%**（Seeds 2,4,7,8 崩溃；Seeds 1,3,5,6 成功）。崩溃机制是 response length inflation（不是 step-level 的 entropy→0 collapse）。D113 决定论文 claim 从 "avoids collapse" 调整为 "enables learning where step-level cannot" + response inflation 双峰分析作为新贡献。
- **两个 config-level 干预均失败**（D114）：len_penalty 只影响 gradient 不影响 inference；high_kl 中 actual KL 极低(0.0067) 说明 response inflation 不是策略偏移导致，而是 GRPO reward 本身奖励长 response。这本身是重要发现——标准 RL 正则化无法阻止 multi-step agent response inflation。
- **用户立场**：用户（贾瑞轩）要求先尝试修复崩溃，最后不行再调整 claim 叙事。游承松在跟进进度。
- **易错点**：(1) Seed 4 registry 曾被错标 conclusion="success"，已修正为 "negative"，如看到 "success" 再改；(2) 不要在有训练跑的服务器上启动 eval 除非严格 Ray 隔离；(3) agent_trainer.py 有 len_penalty 代码修改残留，新的训练实验如果不需要 penalty 要确认代码状态


---
