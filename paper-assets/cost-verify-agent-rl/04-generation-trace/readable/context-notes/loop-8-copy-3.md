# reviewer / loop_8.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`08e836e58ea9147bb132.json`](../../sessions/08/08e836e58ea9147bb132.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-15T15:26:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C001：仅 cuda:0, cuda:1 @ bjb1-17606，越界立即 critical
- Val/eval 必须 ≥16 episodes（C003），禁止基于 4-episode 结果做 pass/fail
- 所有实验必须启用 W&B（D033 教训：WANDB_MODE=disabled 导致 cron 误判）
- save_freq 必须 ≤5（D035 教训：exp026 峰值 32.81% 因 save_freq=25 无 checkpoint 可恢复）
- RAGEN eval 框架内 SFT baseline 是 6.25%（不是 eval_sft_fast 的 20%），不要混淆两个 eval 框架

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606(root)，代码根目录 /root/cost-verify-agent-rl
- Python：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- SFT checkpoint：/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4
- 基础模型：Qwen3-1.7B
- W&B entity: xiaoyucorynne-，project: cost-verify-agent-rl
- B-IAVR 代码：远程 /root/cost-verify-agent-rl/RAGEN/ragen/biavr/（2026-05-14 版本），本地 artifacts/biavr/（含 D031 修复）
- 活跃进程：exp027_stable_grpo（PID 789790 parent, WorkerDict PID 793233+793234 实际训练），tmux=exp027_stable_grpo，W&B run=y7jiibqk，双卡各 45.8GB/98GB 100% 利用率

### 3. 📊 当前状态
刚完成 worker_code_biavr_d031_warnings_fix 的审查（PASS）。两个 D031 warning 已修复：`&lt;VERIFY>` special token 注册函数 + `PreActionProfiler` 开销量化工具，代码在本地 artifacts 待 Phase B 集成。

exp027_stable_grpo RUNNING：val_before_train 完成（success=6.25%），step 1 rollout 进行中。关键参数：LR=5e-7, KL=0.005, entropy_coeff=0.01, env_groups=8（128 rollouts），save_freq=5，50 步。W&B enabled。

无其他 RUNNING 实验。无等待中的 Worker 回调。Cron 180s 监控 exp027（PID=789790, wandb=y7jiibqk）。

### 4. 📋 待办
- exp027 step 5 val 结果出来 → 按 D037/D038 判定：val<20% fail（需 pivot），20-25% weak（=SFT），≥30% proceed Phase B
- exp027 出现连续 2 步 success 归零 → 立即 critical 报告死亡螺旋（重复 exp026 pattern）
- exp027 前 5 步 KL>0.005 → registry notes 要求立即汇报，可能指示策略偏移过快
- Phase B 集成前 → 验证 `register_verify_special_token` 是否覆盖 Qwen3 tokenizer 已有 additional_special_tokens（我在审查中标注了此风险）

### 5. 🎯 战略上下文
核心决策链：RAGEN GRPO 3/3 退化（D025/D026）→ pivot 到 step-independent rollout cherry-pick（D028）→ exp026 证明 step-independent 有效但训练不稳（峰值 32.81% 后崩塌，D035/D036）→ exp027 加固版正在验证。

51 个实验全在 pipeline debugging，B-IAVR 核心选择性验证机制零实验（D030 指出）。即使 exp027 成功也只是 weak story（step-independent rollout 是 verl-agent cherry-pick 不算本项目贡献）。论文贡献必须来自 B-IAVR ablation。

**最容易判断错的事**：
- train success ≠ val success。exp026 train 32.81% 但 val 从未超 6.25%。exp023c 同样 train 29.7% vs val 6.25%。只看 train 会严重高估。
- RAGEN eval 的 6.25% baseline 和 eval_sft_fast 的 20% baseline 来自完全不同的 eval 框架，不可直接对比（D024/D038 反复讨论过）。
- D034 论文可行性标准：val≥50% 才能让 B-IAVR 的 Pareto efficiency claim 有说服力，20% MVP 只证明训练可行。


---
