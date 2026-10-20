# director / loop_10.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`3de1e27f10a09e6cac1f.json`](../../sessions/3d/3de1e27f10a09e6cac1f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-16T14:16:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cqa1-21977 cuda:0~5（6张 RTX 4090D），严禁使用白名单外 GPU
- 0.5B 模型排除 MC benchmarks (MMLU/ARC) IRT pooling（D045：position bias）
- IRT 模型选择规则 C008：2PL+γ 默认（N<16），4PL+γ 仅 N≥16 + MCQ format
- N=16 domain gamma 数字**不可引用**（D111：STEM_Math 方向翻转证明 N=16 不可靠），论文只用 N=24 数据
- Medical domain PPP=1.0���D112），γ=-0.20 不可信，论文中标为 model misfit
- Instruct 模型 eval 必须 apply_chat_template，Base 模型保持 raw completion
- PPP=0 的 domain gamma 结果只能做 pattern/ranking claims，不能做绝对值 claims
- C001 反复违规：提交 GPU 任务前**必须** `nvidia-smi --query-compute-apps` 确认无同类进程 + `ls output-dir` 确认无正在写入文件。本 session 4 次违规。
- 3B signals 脚本 bug：`run_3B_d000_s123_signals.sh` 第 6 行 `export CUDA_VISIBLE_DEVICES=${1}` 会覆盖外层设置。不要传 gpu_id 作为脚本参数，直接外层 export。

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977 (connect.cqa1.seetacloud.com)，工作目录 /root/contamcal-irt-calibration
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base）
- 模型 checkpoints：/root/autodl-tmp/ 下 Qwen2.5-{0.5B,1.5B,3B} 各 dosage + Llama-3.2-3B
- Signals 输出：/root/autodl-tmp/exp002/signals/
- IRT 脚本：/root/contamcal-irt-calibration/exp006/（**注意区分 run_mmlu_domain_gamma.py (旧N=16) vs run_mmlu_domain_gamma_n24.py (正确N=24)**）
- RRF 脚本：/root/contamcal-irt-calibration/exp003/
- D108 结果目录：/root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24/
- HF_HOME=/root/autodl-tmp/.hf_cache
- 活跃进程（RESET 前）：D108 v4 (PID 789935, CPU Stan), 3B signals (cuda:2 PID 790564), Llama eval (cuda:4 PID 785955), 1.5B-Instruct eval (cuda:5 PID 786898), 0.5B-Instruct signals (cuda:1 PID 780591), 冗余 3B s4 (cuda:0 PID 780943 应 kill)

### 3. 📊 ��前状态
**刚完成的里程碑**：
- Pooled IRT N=23 (2PL+γ) ✅ — γ 全部不显著，GSM8K ΔMAE=0.155 校准改善显著 (D109)
- D108 前 3 好域：STEM_Math γ=+0.97(sig), STEM_Science γ=+0.84(sig), STEM_CS_Eng γ≈0(null) — domain heterogeneity 确认
- 0.5B s123 signals ✅ 全部完成、1.5B s123 signals ✅ 全部完成
- 3B-Instruct eval v2 ✅ 成功（MMLU=60.5%, GSM8K=76%, HumanEval=50%）(D113)
- Llama-3.2-3B d000 SFT ✅ 成功，merged checkpoint 就绪
- Scale-stratified IRT ✅ negative result，作为 ablation (D110)

**RUNNING/等待中**：
- exp_006_mmlu_domain_gamma_n24_v4 — 正确脚本跑剩余 4 域 (Humanities/Social_Sciences/Business_Law/Other)，PID 789935，CPU Stan
- exp_002_signals_3B_d000_s123_cuda2 — 刚收到 cron 回调（退出），需诊断
- Llama eval (cuda:4 PID 785955) — 应该接近完成
- 1.5B-Instruct eval (cuda:5 PID 786898) — 运行中
- 0.5B-Instruct signals (cuda:1 PID 780591) — 运行中
- cuda:0 PID 780943 — 冗余进程，应 kill

**Registry 待修正**：
- exp_001_eval_3B_instruct_v2 → 改 success（当前标 failed）
- exp_002_signals_3B_d000_s123_cuda2 → 需诊断后更新
- exp_006_pooled_irt_n25 → 改 DONE/success（进程已死，结果文件在）

### 4. 📋 待办（条件触发式）
- D108 v4 完成（8 域全齐）→ 汇总全 8 域 γ/CI/PPP 表格 → 更新 paper_framing.md 的 D108 措辞（从 "Simpson's Paradox opposing directions" 改为 "domain-differential susceptibility"）→ 通知用户 → 激活 Paper Agent Full Draft
- Llama eval 完成 → 跑 Llama signals → 跨家族验证 Claim 1
- 1.5B-Instruct eval 完成 → cuda:5 跑 0.5B-Instruct eval 或 3B d025_s123 signals
- cuda:0 kill 冗余后释放 → 3B d100_s123 signals
- 全量 RRF N=20+ 完成 → 新 pooled IRT（应已完成，Reviewer 确认结果文件存在）
- 所有核心 IRT 数字就绪 → Paper Agent Full Draft（writing_plan.yaml 已 APPROVED）

### 5. 🎯 战略上下文
- **EMNLP 2026 ARR May 25，T-9 天**。Critical path: D108 8域完成 → paper_framing 更新 → Paper Agent Day 3-5 → submit Day 7-9
- 4 Claims: (1) Domain-differential contamination susceptibility [PRIMARY, D108] (2) Min-K++ reversal [CO-PRIMARY] (3) Fisher Info identifiability (4) Conditional calibration [DEMOTED]
- **论文 story 已演变**：从"提出 IRT 方法"到"用 IRT 揭示 contamination 的 domain-differential 特性"。Method 是工具，empirical finding 是主卖点（用户已知悉并未反对）
- **D108 叙事修正 (D111)**：N=16 时"正负方向对立"是假象；N=24 实际是"知识密集型 domain γ≈0.9 vs 推理型 γ≈0"——更有解释力
- **最易判断错的事**：(1) Cron false positives — signals/Stan 类任务不写 W&B，cron 永远误判，必须检查 log 和输出文件 (2) run_mmlu_domain_gamma.py vs run_mmlu_domain_gamma_n24.py — 用错脚本（v3 血的教训）(3) CUDA_VISIBLE_DEVICES 脚本覆盖 bug (4) Agent 反复卡死 — 可能是 session 层面问题，queue 不要积太深
- **7B 云 GPU**：已向 Manager 申请（A100-80G ×1），未收到回复


---
