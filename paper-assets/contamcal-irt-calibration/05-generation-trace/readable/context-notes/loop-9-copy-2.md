# agent / loop_9.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`9119359741cf0ffcadd1.json`](../../sessions/91/9119359741cf0ffcadd1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-15T11:40:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cqa1-21977 的 cuda:0~cuda:5（共 6 张），不可用白名单外 GPU
- train_sft.py 有已知 `--gpu` 死代码 bug（args.gpu 解析但未实际使用），ROADMAP 已记录待修复。提交 SFT 训练时注意此问题
- 模型/数据/HF cache 必须放 `/root/autodl-tmp/`，根分区只有 ~30GB
- seed=123 系列实验是为 multi-seed pooling 准备的（与 seed=42 配对），不可随意改 seed
- 本项目 framing 已从 "calibration method" pivot 到 "detection diagnostics"（D038），所有论文相关工作必须对齐新 framing

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977（AutoDL），工作目录 `/root/contamcal-irt-calibration/`
- Python：`/root/miniconda3/bin/python`，conda base 环境（不是 venv）
- 激活命令：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型路径：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-{0.5B,1.5B,3B}`
- SFT 数据：`/root/autodl-tmp/exp001/sft_data/sft_dosage_{000,005,025,100}.jsonl`
- Checkpoints：`/root/autodl-tmp/exp001/checkpoints/`
- 日志：`~/runs/contamcal-irt-calibration/`
- 代码 commit：`dd81ae283e12a247f768b6ae72e67b085a874bd1`
- 活跃进程（reconcile 确认）：
  - exp_001_eval_3B_d000_s42_v3: PID 513826（有 cron 监控）
  - exp_001_eval_15B_d000_s123_aligned: PID 521608（有 cron 监控）
  - exp_001_eval_05B_d000_s123_aligned: PID 521689（有 cron 监控）

### 3. 📊 当前状态
**刚做完**：收到 exp_001_sft_15B_d005_s123 的 CRON 失败回调（EXIT_CODE=2，25 秒即死）。已完成 session-start 初始化（registry + reconcile + ROADMAP）。已派 Worker `worker_diagnose_exp_001_sft_15B_d005_s123_20260515T083802` SSH 诊断日志。已向 Director 汇报失败 + 资源缺口。

**RUNNING（3 个 eval）**：
- exp_001_eval_3B_d000_s42_v3 — 3B baseline eval v3（cuda:? PID 513826）
- exp_001_eval_15B_d000_s123_aligned — 1.5B d000 s123 eval（cuda:5）
- exp_001_eval_05B_d000_s123_aligned — 0.5B d000 s123 eval（cuda:1）

**PREPARING（17 个）**：exp_001_sft_15B_d025_s123, exp_008 系列, exp_003_mmlu, exp_006_irt_05B_v2 等

**空闲 GPU**：cuda:0, cuda:2, cuda:4（3/6 空闲 = 违规状态）

**等待中**：
- Worker 诊断回调（exp_001_sft_15B_d005_s123 日志分析）
- Director 对资源缺口汇报的回复

### 4. 📋 待办（条件触发式）
- 诊断 Worker 回调 → 读诊断报告 → 如果是 --gpu 死代码 bug：派 Worker 修复 train_sft.py → 重提交 d005 s123 到 cuda:0；如果是其他原因：按诊断结果修复
- Director 回复资源分配 → 从 PREPARING 队列填 cuda:2 和 cuda:4（优先 seed=123 SFT 以推进 multi-seed pooling）
- eval_3B_d000_s42_v3 完成回调 → 走 on-experiment-done 流程，结果入 pooled IRT
- eval_15B_d000_s123_aligned / eval_05B_d000_s123_aligned 完成回调 → 同上
- 所有 seed=123 eval 完成 → N≥16 multi-seed pooled IRT 重跑 → 检查 coverage collapse 是否改善

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 ARR May 25（距今 10 天）
- **核心发现（D036-D043）**：ARC gamma 负方向 confirmed；coverage collapse 20-33%（PPP 极值，疑似 model misspecification）；跨种子方差 7pp → multi-seed pooling 是必要条件
- **Framing pivot（D038）**：从 "calibration method" 转为 "detection diagnostics"——4PL+γ 的价值不在校准本身，而在诊断 benchmark-dependent contamination effects
- **Critical path**：coverage collapse 根因 > seed=123 补全 > pooled IRT N≥16 > 论文
- **易错点**：
  - 不要把 oracle（N=15 models）和 RRF（N=8）直接比——N 不匹配，需 matched N=8 重跑
  - GSM8K gamma=+3.77 显著但校准更差（D037），ARC gamma 负向（D036）——benchmark-dependent 是关键 narrative
  - exp-004 sim sweep 已失败 5 次（v1-v5），如果需要重跑务必先查历史失败原因
  - 3 张 GPU 空闲是当前最紧迫的资源问题，诊断完成后必须立即填满


---
