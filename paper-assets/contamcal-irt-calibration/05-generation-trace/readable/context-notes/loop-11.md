# director / loop_11.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_11.md`
- **Structured JSON:** [`a7faedfa5e3717ba8210.json`](../../sessions/a7/a7faedfa5e3717ba8210.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_messages
updated: '2026-05-16T15:24:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cqa1-21977 cuda:0~5（6张 RTX 4090D），严禁使用白名单外 GPU
- 0.5B 模型排除 MC benchmarks (MMLU/ARC) IRT pooling（D045：position bias）
- IRT 模型选择 C008：2PL+γ 默认（N<16），4PL+γ 仅 N≥16 + MCQ format
- N=16 domain gamma 数字不可引用（D111：方向翻转证明不可靠），论文只用 N=24 数据
- Medical domain PPP=1.0（D112），γ不可信，论文标 model misfit
- Instruct 模型 eval 必须 apply_chat_template，Base 模型保持 raw completion
- C001：提交 GPU 任务前必须 nvidia-smi 确认无同类进程 + ls output-dir 确认无正在写入
- 3B signals 脚本 bug：`run_3B_d000_s123_signals.sh` 第6行覆盖 CUDA_VISIBLE_DEVICES，不用脚本，直接外层 export
- **Agent 系统性故障**：本 session 连续 7 次 idle 240min reset，已升级 Manager。新 session 注意队列不要积压超过 3 条

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977 (connect.cqa1.seetacloud.com)，工作目录 /root/contamcal-irt-calibration
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base）
- 模型 checkpoints：/root/autodl-tmp/ 下 Qwen2.5-{0.5B,1.5B,3B} 各 dosage + Llama-3.2-3B
- Signals 输出：/root/autodl-tmp/exp002/signals/（14+ model dirs 完成）
- IRT 脚本：/root/contamcal-irt-calibration/exp006/（run_mmlu_domain_gamma_n24.py = 正确脚本）
- RRF 脚本：/root/contamcal-irt-calibration/exp003/rrf_aggregation.py
- D108 结果：/root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24/
- HF_HOME=/root/autodl-tmp/.hf_cache
- 活跃进程（估计，4h 前确认）：Llama eval v2 (cuda:4, PID 796493), 0.5B-Instruct eval (cuda:2), cuda:0 d000_s123 s4_mmlu 最后一项, cuda:1/3 空闲

### 3. 📊 当前状态
**本 session 完成的关键工作**：
- paper_framing.md 已更新 D108 final results（STEM gradient 确认，非 STEM 标 limitation）
- 决策记录：D114（STEM-only scope）、D115（7/8 domains sufficient）、D116（Simpson's Paradox confirmed via pooled γ≈0）
- 向 Manager 升级了 Agent 系统性故障
- 向用户汇报了 D108 进展

**Registry RUNNING**（最后确认时）：
- exp_001_eval_llama32_3B_d000_s42_v2 (cuda:4) — Llama eval，GSM8K CoT 慢 ~4.5h
- exp_001_eval_05B_instruct (cuda:2) — 0.5B-Instruct eval
- exp_006_mmlu_domain_gamma_n24_v4 (CPU) — 已完成 7/8 域，"Other" crash 不重跑

**关键结果已产出但未完全整合**：
- Pooled IRT v2：GSM8K ΔMAE=+0.118（有效），MMLU 2PL+γ PPP=0.426 ΔMAE=+0.006，ARC PPP=0.002（仍失败）
- 1.5B-Instruct eval 完成：MMLU=57.75%, GSM8K=59.29%, ARC=76.54%, HumanEval=34.15%
- 1.5B-Instruct paraphrased eval 完成（baseline drop: GSM8K -10.61pp）

**等待中**：Worker 读取 exposure_scores.json 结构 + signals 覆盖情况的回调

### 4. 📋 待办（条件触发式）
- Worker 回调 exposure 结构 → 确认为什么 MMLU/ARC 只有 N=8 → 补充 signals 或修 RRF 过滤逻辑 → 重跑 pooled IRT (N≥16 目标)
- Llama eval v2 完成 → Llama signals (s1+s2+s4) → RRF 包含 Llama → 跨家族验证 Claim 1
- 0.5B-Instruct eval 完成 → 0.5B-Instruct signals → instruct vs base 对比
- ARC N≥16 达成 → 2PL+γ refit → 确认校准是否有效
- 所有核心数字就绪（pooled IRT + domain gamma + Llama） → Paper Agent Full Draft（writing_plan.yaml 已 APPROVED）
- Agent 稳定后 → Registry 修正：exp_001_eval_15B_instruct 标 success, D108 v4 标 success, Llama v2 注册 RUNNING

### 5. 🎯 战略上下文
- **EMNLP 2026 ARR May 25，T-9 天**。Critical path: N 扩大 → pooled IRT 有效 → Paper Agent Full Draft Day 3-5
- **4 Claims**: (1) Domain-differential contamination [PRIMARY, D108 confirmed] (2) Min-K++ reversal [CO-PRIMARY] (3) Fisher Info identifiability (4) Conditional calibration [DEMOTED]
- **D116 关键发现**：Pooled MMLU γ≈0 IS the Simpson's Paradox — domain 正负效应相消。这完美支撑 Claim 1。论文故事："aggregate 看不到 contamination effect，必须 domain-level analysis"
- **最易判断错的事**：(1) "pooled γ not significant" ≠ "contamination doesn't matter"——恰恰是 Simpson's Paradox 的证据 (2) 非 STEM 域的负 γ 不是"污染降低分数"——是模型失配(PPP=1.0) (3) ARC N=8 的 γ=1.51 显著性是过参数化伪影(PPP=0.000) (4) Agent 队列积压超过 3 条就会卡死——保持极简指令
- **7B 云 GPU**：已向 Manager 申请 A100-80G ×1，未收到回复


---
