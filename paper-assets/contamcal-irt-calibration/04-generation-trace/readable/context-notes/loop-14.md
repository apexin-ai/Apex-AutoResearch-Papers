# director / loop_14.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_14.md`
- **Structured JSON:** [`206827503a3c8e9b69a5.json`](../../sessions/20/206827503a3c8e9b69a5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_messages
updated: '2026-05-16T19:46:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cqa1-21977 cuda:0~5（6张 RTX 4090D），严禁使用白名单外 GPU
- 0.5B 模型排除 MC benchmarks (MMLU/ARC) IRT pooling（D045：position bias）
- IRT 模型选择 C008：2PL+γ 默认（N<16），4PL+γ 仅 N≥16 + MCQ format
- N=16 domain gamma 数字不可引用（D111：方向翻转证明不可靠），论文只用 N=24 数据
- ARC pooled gamma 显著但 PPP=0.003 → 走 gating criterion 报 raw scores（D118）——不可作为可靠 contamination 证据引用
- D119：论文不能用 "Simpson's Paradox" 叙事，改用 "dilution masking"
- Non-STEM 域负 gamma 不可 claim（PPP=1.0 模型失配，D117）
- Agent 系统性故障：连续 18 次 idle 240min reset，已两次升级 Manager。指令极简化

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977 (connect.cqa1.seetacloud.com)，工作目录 /root/contamcal-irt-calibration
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base）
- 模型 checkpoints：/root/autodl-tmp/exp001/checkpoints/ 下 Llama-3.2-3B_{d000,d005,d025,d100}_s42/
- Qwen models：/root/autodl-tmp/ 下 Qwen2.5-{0.5B,1.5B,3B} 各 dosage
- Signals 输出：/root/autodl-tmp/exp002/signals/
- RRF 输出：/root/autodl-tmp/exp002/signals/rrf/（exposure_scores.json 509K行，全模型）
- IRT 脚本：/root/contamcal-irt-calibration/exp006/
- Pooled IRT 结果：/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/
- HF_HOME=/root/autodl-tmp/.hf_cache
- 磁盘：~35G 可用（需监控）
- 最后确认活跃进程（Agent 刚报告 kill 成功后）：
  - cuda:0: Llama d005 eval (PID 825638)
  - cuda:1: Llama d000 MMLU signals (PID 830115, 僵尸已清理)
  - cuda:2: 空闲
  - cuda:3: Llama d025 eval (PID 822390)
  - cuda:4: Llama d005 signals mmlu (PID 842929, 刚启动)
  - cuda:5: Llama d100 eval (PID 831033)

### 3. 📊 当前状态
**本 session 完成的关键工作**：
- D120 决策：Pooled IRT 2PL+γ N=24 结果确认（ARC γ=0.73 走 gating, MMLU NS, GSM8K ΔMAE=16pp 来自 ability estimation）
- 1.5B-Instruct RRF aggregation 完成（全模型 signals root 聚合）
- 3B signals 全部确认完整（s42+s123 ×4 dosages ×3 benchmarks）
- GPU 1 僵尸进程终于被 kill（第 5 次上报后）
- Reviewer reset（4h41m/87消息）
- 向用户发送 pooled IRT 结果 + 再次催确认 Option B
- 向 Manager 升级 Agent 系统性故障（第 2 次）

**Registry RUNNING**：Llama d005 eval, d025 eval, d100 eval, d000 MMLU signals, d005 signals mmlu
**冗余实验需取消**：exp_002_signals_15B_instruct_mmlu_v2, exp_002_signals_llama32_3B_d000_gsm8k_v2（PREPARING 状态，数据已存在无需重跑）

### 4. 📋 待办（条件触发式）
- 用户确认 Option B + 双 seed → 激活 Paper Agent 启动 reframe（含 D119 dilution masking + D120 calibration value decomposition）
- 用户拒绝双 seed → 单 seed N=4 + "exploratory" 标注
- Llama d005/d025/d100 eval 全完成 → 启动各 dosage signals → Llama RRF → cross-family pooled IRT (N≥20+)
- Llama d000 MMLU signals (PID 830115) 完成 → d000 全 3 benchmark signals 就绪 → 可单独做 d000 RRF
- cuda:2 空闲 → 填充 Llama d025 signals（如 d025 eval 已完成）或等 eval 完成
- 取消 gsm8k_v2 和 15B_instruct_mmlu_v2（冗余 PREPARING）
- Fisher Info N×identifiability heatmap（W4）→ CPU 任务，低优先级
- Agent 基础设施修复后 → 批量推进积压任务

### 5. 🎯 战略上下文
- **EMNLP 2026 ARR May 25，T-9 天（写 handoff 时）**。审稿 Weak Reject，revision 阶段。
- **Paper 新 framing (D118+D119+D120)**："Domain-Differential Contamination Effects"——Math γ=0.97 + Science γ=0.95 是正面发现；pooled γ≈0 是 dilution masking；GSM8K ΔMAE=16pp 来自 IRT ability estimation 而非 γ（calibration value decomposition）
- **最易判断错的事**：
  1. ARC γ=0.73 看似显著但 PPP=0.003 → 不可引用为可靠结论（Reviewer 两次 critical）
  2. pooled gamma 不显著 ≠ 方法失败，是 dilution 的证据
  3. Agent 系统性 idle——18 次 reset，Manager 已知但未修复。新 session 只派最简单指令
  4. exp_002_signals_llama32_3B_d000_gsm8k 在 registry 标 failed 但磁盘数据完整可用
  5. Llama evals 预计早已完成（ETA 05:00 UTC），但因 Agent idle 无法确认
- **Reviewers 共识论文最强牌**：Min-K++ reversal (Cohen's d = -1.55~-1.98, 跨家族复制)
- **用户待回复**：Option B framing 确认 + Llama 双 seed 决策（已催两次）


---
