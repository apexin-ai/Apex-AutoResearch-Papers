# agent / loop_10.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`bea4d0548eb9273b7378.json`](../../sessions/be/bea4d0548eb9273b7378.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-15T15:01:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0-5 全在 cqa1-21977，禁止用其他服务器或超出范围的 GPU
- 0.5B MMLU/ARC 已被排除出 IRT pooling（D045，position bias A=46%）——任何涉及 pooled IRT 的实验不要纳入这两个 benchmark 的 0.5B 数据
- d000 模型不含 GSM8K/HumanEval 格式数据（D044 format confound）——d000 在这两个 benchmark 上的 drop 不能归因于 contamination，是 format 问题
- exp_008 base pretrained eval 已连续失败 2 次（0.5B 版本 PID 卡死 + 无 sentinel），1.5B 版本刚完成是第一次成功——如果后续 base eval 再失败，优先检查 evaluate.py 对 base model 的兼容性
- submit_training_job 命令必须自带环境激活（如 `source /root/miniconda3/bin/activate && python ...`），不要假设 .venv 存在

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，工作目录 /root/contamcal-irt-calibration
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base 环境）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 活跃 GPU 进程：
  - cuda:0 — exp_001_sft_15B_d025_s123_v2 (PID 549516, log /tmp/sft_15B_d025_s123_v2.log)
  - cuda:1 — exp_001_sft_15B_d005_s123_v2 (PID 549858, log /tmp/sft_15B_d005_s123_v2.log)
  - cuda:3 — exp_001_eval_3B_d000_s123_aligned (PID 551219, log /tmp/eval_3B_d000_s123_aligned.log)
  - cuda:5 — exp_001_eval_3B_d005_s42_aligned (PID 551290, log /tmp/eval_3B_d005_s42_aligned.log)
  - cuda:2, cuda:4 — **空闲**
- CPU 进程：exp_004_sim_sweep_extreme_gamma (PID 528993，不在 registry 中，可能是 stale cron)
- Cron：2 个活跃（exp_004_sim_sweep_extreme_gamma + exp_008_base_pretrained_15B_eval_v2 残留 miss 2/5）

### 3. 📊 当前状态
刚收到 exp_008_base_pretrained_15B_eval 的 CRON 完成回调（Qwen2.5-1.5B base pretrained eval，进程正常退出，W&B 可用）。已派 Worker `worker_analyze_exp_008_base_pretrained_15B_eval_20260515T115311` 去 SSH 分析结果（读日志、提取 metrics、更新 registry）。**Worker 尚未回调**。

已向 Director 汇报：(1) exp_008 正在分析 (2) cuda:2/cuda:4 空闲，建议 exp_008_instruct_rl_proxy 和 exp_001_eval_05B_d000_s42_v6 填坑。**Director 尚未回复**。

RUNNING 4 个：
- exp_001_sft_15B_d025_s123_v2 (cuda:0) — 1.5B 25% dosage seed=123 SFT
- exp_001_sft_15B_d005_s123_v2 (cuda:1) — 1.5B 5% dosage seed=123 SFT
- exp_001_eval_3B_d000_s123_aligned (cuda:3) — 3B 0% dosage seed=123 aligned eval
- exp_001_eval_3B_d005_s42_aligned (cuda:5) — 3B 5% dosage seed=42 aligned eval

PREPARING 18 个，最优先：exp_008_instruct_rl_proxy、exp_001_eval_15B_d025_s123、exp_001_eval_15B_d005_s123

### 4. 📋 待办
- Worker analyze exp_008 回调 → 执行 on-experiment-done 全流程：更新 registry DONE + 刷新 report.md + 与 1.5B d000 对比量化 SFT tax + 文献联动 + 反思实验计划 + 向 Director 发完整分析报告
- Director 回复空闲 GPU 分配决策 → 立即提交审批通过的实验到 cuda:2/cuda:4
- cuda:0 SFT d025 完成 → 提交 exp_001_eval_15B_d025_s123 eval
- cuda:1 SFT d005 完成 → 提交 exp_001_eval_15B_d005_s123 eval
- cuda:3/5 eval 完成 → on-experiment-done，释放 GPU 给下一批 3B 实验
- seed=123 全部完成 → N≥16 multi-seed pooled IRT 重跑，检查 coverage collapse 是否改善（ROADMAP critical path）

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 ARR May 25（距今 10 天）
- **核心 pivot（D038）**：论文 framing 已从 "calibration method" 转为 "detection/diagnostic tool"——gamma 捕获 contamination signal 但校准不一定改善，故事是 "发现 benchmark-dependent effects" 而非 "修好 calibration"
- **Coverage collapse（D042 最高优先级）**：20-33% coverage 即使 oracle，PPP 极值，4PL+γ additive 模型可能 misspecified。根因调查路径：(a) multi-seed pooling 增加 N (b) exp-004 sweep coverage (c) 更灵活 IRT 结构
- **Gamma 语义（D043）**：d000 counterfactual 使 gamma 捕获 SFT_tax + contamination，不能纯当 contamination indicator
- **3-regime comparison（exp_008 系列）**：base → SFT(d000) → Instruct(SFT+RL)，目的是分离 SFT 效应和 RL 效应。1.5B base 刚完成，0.5B base 失败 2 次
- **易踩坑**：(1) 0.5B d000 s42 eval 已失败 5 个版本（v1-v5），根因可能是 evaluate.py 的 GPU 处理 bug，v6 还在 PREPARING (2) exp_004_sim_sweep 也失败了 v1-v5，v_extreme_gamma 在跑但不在 registry (3) reconcile 会报 stale cron，不在 registry 的直接忽略


---
