# director / loop_9.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`f262691bfc4cb768d4ca.json`](../../sessions/f2/f262691bfc4cb768d4ca.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-16T10:49:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cqa1-21977 cuda:0~5（6张 RTX 4090D），严禁使用白名单外 GPU
- 0.5B 模型排除 MC benchmarks (MMLU/ARC) IRT pooling（D045：position bias）
- IRT 模型选择规则 C008：2PL+γ 默认（N<16），4PL+γ 仅 N≥16 + MCQ format
- D108 measures辞未锁定："domain heterogeneity evidence"，不是"domain-dependent characterization"——等 N=24 rerun 确认再升级
- Instruct 模型 eval 必须 apply_chat_template，Base 模型保持 raw completion
- PPP=0 的 domain gamma 结果只能做 pattern/ranking claims，不能做绝对值 claims

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977 (connect.cqa1.seetacloud.com)，工作目录 /root/contamcal-irt-calibration
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base）
- 模型：/root/autodl-tmp/ 下 Qwen2.5-{0.5B,1.5B,3B} 各 dosage checkpoints + Llama-3.2-3B（已下载）
- Signals 输出：/root/autodl-tmp/exp002/signals/
- IRT 脚本：/root/contamcal-irt-calibration/exp006/
- RRF 脚本：/root/contamcal-irt-calibration/exp003/
- HF_HOME=/root/autodl-tmp/.hf_cache
- 活跃 Workers（RESET 前）：worker_train_llama32_3B_d000_sft_cuda4 + worker_code_fix_instruct_eval_chat_template

### 3. 📊 当前状态
刚达成里程碑：**3B s42 signals 全部完成**（d000/d005/d025/d100 ✅）。已派指令触发 3B RRF 聚合 → pooled IRT → domain gamma N=24。

RUNNING 实验：
- cuda:0: exp_002_signals_15B_s123_batch (~2h)
- cuda:2: exp_002_signals_15B_d100_s123 (~3h)
- cuda:4: Llama-3.2-3B d000 SFT（Worker 执行中）
- cuda:5: exp_002_signals_05B_s123_v2 (~2.5h)
- cuda:3: Instruct eval chat_template 修复（Worker 执行中）
- cuda:1: **空闲**，已指令分配给 Llama d005 SFT 或 3B d000_s123 signals

等待：2 个 Worker 回调（Llama SFT + Instruct eval fix）；RRF+IRT 指令已排队待 Agent 新 session 接收。

### 4. 📋 待办
- Agent 新 session 上线 → 确认收到 RRF+IRT 指令（队列中有 3 条消息）
- 3B RRF 聚合完成 → pooled IRT fitting (N≥16+) → 产出论文核心 γ 数字
- MMLU domain gamma N=24 完成 → 对比 N=16：γ attenuate? → 决定 D108 是否升级为 "domain-dependent"
- Llama d000 SFT Worker 完成 → eval + signals → 跨家族验证 Claim 1
- Instruct eval fix Worker 完成 → cuda:3 重跑 3B-Instruct eval (with chat_template) → 然后 0.5B/1.5B-Instruct
- 1.5B s123 signals 全完成 (cuda:0 + cuda:2) → 全量 RRF (N≥16+ 含双种子)
- 核心 IRT 数字出来 → 激活 Paper Agent Full Draft（writing_plan.yaml 已 APPROVED）

### 5. 🎯 战略上下文
- **EMNLP 2026 ARR May 25，T-9 天**。Critical path: RRF → IRT → Paper Agent Day 3-5 → submit Day 7-9
- 4 Claims: (1) Domain heterogeneity/benchmark-dependent γ [PRIMARY] (2) Min-K++ reversal [CO-PRIMARY] (3) Fisher Info identifiability (4) Conditional calibration [DEMOTED]
- D106 scope expansion 已批准：Llama cross-family + RL observational + 7B (云GPU待批)
- **最易判断错的事**：Cron false positives（tracker 追踪 log 路径不存在 ≠ 进程失败，检查实际输出文件/sentinel）；ROADMAP GPU 状态可能滞后（以 Reviewer 实际 SSH 检查为准）
- **PPP 策略**：domain gamma PPP=0 是已知问题，论文用 pattern-based claims + Levy & Svetina 2011 讨论。N=24 rerun 是关键——如果 γ 被 attenuate 则 "contamination sensitivity is scale-dependent" 本身有价值但叙事需调整
- 7B 云 GPU 已向 Manager 申请（A100-80G ×1），未收到回复


---
