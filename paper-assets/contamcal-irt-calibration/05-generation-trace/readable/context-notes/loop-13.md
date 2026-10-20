# director / loop_13.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_13.md`
- **Structured JSON:** [`2515fc6b7855f0ab1dcc.json`](../../sessions/25/2515fc6b7855f0ab1dcc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_messages
updated: '2026-05-16T18:56:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cqa1-21977 cuda:0~5（6张 RTX 4090D），严禁使用白名单外 GPU
- 0.5B 模型排除 MC benchmarks (MMLU/ARC) IRT pooling（D045：position bias）
- IRT 模型选择 C008：2PL+γ 默认（N<16），4PL+γ 仅 N≥16 + MCQ format
- N=16 domain gamma 数字不可引用（D111：方向翻转证明不可靠），论文只用 N=24 数据
- Medical domain PPP=1.0（D112），γ不可信；Non-STEM 域负 gamma 不可 claim（PPP=1.0 模型失配，D117）
- CS/Eng domain gamma 不显著（N=21/23 时 0.20~0.31），不能归入"STEM 全部显著"
- ARC pooled gamma 显著但 PPP=0.003 → 走 gating criterion 报 raw scores（D118）
- D119：论文不能用 "Simpson's Paradox" 叙事（无可靠负向域），改用 "dilution masking"
- Instruct 模型 eval 必须 apply_chat_template，Base 模型保持 raw completion
- Agent 系统性故障：连续 12 次 idle 240min reset，已升级 Manager。新 session 指令极简化，不超过 2 条排队

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977 (connect.cqa1.seetacloud.com)，工作目录 /root/contamcal-irt-calibration
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base）
- 模型 checkpoints：/root/autodl-tmp/exp001/checkpoints/ 下 Llama-3.2-3B_{d000,d005,d025,d100}_s42/
- Qwen models：/root/autodl-tmp/ 下 Qwen2.5-{0.5B,1.5B,3B} 各 dosage
- Signals 输出：/root/autodl-tmp/exp002/signals/
- IRT 脚本：/root/contamcal-irt-calibration/exp006/
- RRF 脚本：/root/contamcal-irt-calibration/exp003/rrf_aggregation.py
- HF_HOME=/root/autodl-tmp/.hf_cache
- 磁盘：/root/autodl-tmp/ 169G 总量，~35G 可用（本 session 清理了 43GB）
- 活跃进程（本 session 最后确认 18:28 UTC）：
  - cuda:0: Llama d005 eval (PID 825638)
  - cuda:1: Llama d000 MMLU signals (PID 830115)
  - cuda:2: 空闲（1.5B ARC signals 已确认早期完成）
  - cuda:3: Llama d025 eval (PID 822390)
  - cuda:4: Llama d000 ARC signals (PID 831353)
  - cuda:5: Llama d100 eval (PID 831033)

### 3. 📊 当前状态
**本 session 完成的关键工作**：
- Data Freeze 三条件全部满足（2PL ablation + Llama d000 eval v3 + 1.5B GSM8K signals）
- D119 决策：Simpson's Paradox → dilution masking（Reviewer 审查后修正）
- 磁盘满危机处理：清理 43GB，d005 merge 成功
- GPU 5/2 重复进程清理（多次 kill duplicate）
- 向用户发送 Data Freeze milestone + 催确认 Option B / 双 seed
- Llama d000 eval v3 确认成功：MMLU 45.5%, GSM8K 19.2%, ARC 60.1%, HumanEval 4.3%
- 1.5B-Instruct signals 全部完成（MMLU+ARC+GSM8K）

**Registry RUNNING**：Llama d005 eval, d025 eval, d100 eval, d000 MMLU signals, d000 ARC signals

**等待中**：用户确认 Option B framing + Llama 双 seed；实验完成后 CRON 回调

### 4. 📋 待办（条件触发式）
- 用户确认 Option B + 双 seed → 激活 Paper Agent 启动 reframe（含 D119 dilution masking 修正）
- 用户拒绝双 seed → 单 seed N=4 + "exploratory" 标注 + pooled N=28 定位
- Llama d005/d025/d100 eval 全完成 → 启动各 dosage signals 计算 → RRF → pooled IRT (N≥20 含 Llama)
- 1.5B-Instruct RRF aggregation 待执行（CPU，signals 全齐但 Agent idle 未跑）
- cuda:2 空闲 → 填充 Llama d000 GSM8K signals 或其他
- Fisher Info N×identifiability heatmap（W4）→ CPU 任务，用 exp-004 simulation 代码
- method_notes.md ARC 方向已修正（本 session Agent 确认）
- Eckerly (2017) 引用验证 → WebSearch 确认 ProQuest Iowa thesis

### 5. 🎯 战略上下文
- **EMNLP 2026 ARR May 25，T-9 天**。审稿完成（Weak Reject），现在是 revision 阶段。
- **Paper 新 framing (D118+D119)**："Domain-Differential Contamination Effects"——Math γ=0.97 + Science γ=0.95 是正面发现，pooled γ≈0 是 dilution masking（不是 Simpson's Paradox），不是失败。
- **最易判断错的事**：
  1. pooled gamma 不显著 ≠ 方法失败，是 dilution 的证据
  2. non-STEM 负 gamma 不可信（PPP=1.0），不能 claim "contamination hurts non-STEM"
  3. "Simpson's Paradox" 已被 D119 降级——论文中不能再用此术语，改 "dilution masking"
  4. Agent 系统性 idle（第 12 次）——指令极简化，一次只派一个任务
  5. 磁盘只剩 ~35G，大操作前检查空间
- **Reviewers 共识论文最强牌**：Min-K++ reversal (Cohen's d = -1.55~-1.98, 跨家族复制)。Reframe 时必须突出。
- **7B 云 GPU**：已向 Manager 申请 A100-80G ×1，无回复。7B 实验不在 critical path。


---
