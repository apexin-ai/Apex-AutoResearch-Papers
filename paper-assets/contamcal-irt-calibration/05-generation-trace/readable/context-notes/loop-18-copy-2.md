# agent / loop_18.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_18.md`
- **Structured JSON:** [`56c907ad3a858da45786.json`](../../sessions/56/56c907ad3a858da45786.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_wall_time
updated: '2026-05-17T10:46:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0-5 on cqa1-21977，全部已分配给本项目
- 0.5B 模型已确认严重 position bias (A-rate 37-98%)，**禁止**再用于 IRT γ 估计——只能用于 signal failure mode 分析
- N=23 的 Math γ=0.97 是 artifact（0.5B position bias 膨胀），论文**不得**再 claim 该数值为 contamination 证据
- J=13 IRT 只有 5 个 3B 模型（缺 d000_s42, d000_s123, d005_s42），论文需说明 "3 excluded (incomplete pipeline)"
- 论文 τ=0.756 来源待核实——N=16 ContamCal MMLU τ=0.7303，0.756 更接近 Raw Acc τ=0.7559，**不要**在未核实前继续引用
- DeepSeek-R1 MMLU/ARC eval 已排除（logprob MC eval 与 CoT 不兼容），只保留 GSM8K

### 2. 🖥️ 基础设施快照
- 服务器: cqa1-21977 (别名 a6000)，6× A6000 48GB
- 工作目录: `/root/contamcal-irt-calibration/`，数据: `/root/autodl-tmp/`
- Python: `/root/miniconda3/bin/python`，CmdStan 已安装
- 模型 checkpoints: `/root/autodl-tmp/exp001/checkpoints/`
- Eval 结果: `/root/autodl-tmp/exp001/eval_results/`
- Signal 输出: `/root/autodl-tmp/exp002/signals/`
- IRT 结果: `/root/autodl-tmp/exp006/` (cross-family), `/root/contamcal-irt-calibration/exp006/mmlu_domain_irt_no05b/` (J=13 domain)
- 论文图表: `/root/contamcal-irt-calibration/figures/` (4 个 PDF 已生成)
- 本地 paper draft: `artifacts/paper_draft/`
- 活跃 cron: 无（全部已 completed）
- 活跃 tmux: 之前 fill_gpu worker 启动的 s1/s4 信号计算 sessions（需验证是否仍在跑）

### 3. 📊 当前状态
**刚完成**:
- J=13 IRT 全域 γ 结果 + θ 提取 → 已报 Director（γ 全部非显著正向，θ_3B-θ_1.5B 全域显著）
- 4 个论文图表生成（signal_heatmap, identifiability_heatmap, domain_gamma, dose_response）
- B3 Kendall τ 计算（= ContamCal for MMLU/GSM8K，ARC 差 0.003）
- Bib rebuild 38 entries 全部 WebSearch 验证
- Introduction, Abstract, Conclusion 已按 D118/D129 framing 重写

**3 个 Worker 在跑**:
1. `worker_ops_transfer_figures_to_local` — 传 4 个 figure PDF 到本地 paper 目录（turn 6, base64 传输中）
2. `worker_ops_fill_all_gpus_signals` — 填满 6 GPU 跑 pending signals
3. `worker_ops_exp009_registry_backfill` — exp-009 registry 补建

**Registry RUNNING/PREPARING**:
- exp_006_theta_extraction_j13: DONE/success（刚完成）
- exp_002_signals_15B_instruct_gsm8k_v2: PREPARING（待填 GPU）
- signals_05B_s123_batch: PREPARING（待填 GPU）
- 其他 ~10 个 PREPARING 状态的旧实验（大部分是历史遗留）

### 4. 📋 待办（条件触发式）
- `worker_ops_transfer_figures_to_local` 回调 → 通知 Director "4 figures ready in paper_draft/figures/"，Paper Agent 可开始 figure placement
- `worker_ops_fill_all_gpus_signals` 回调 → 确认 6 GPU 利用率，报 Director
- `worker_ops_exp009_registry_backfill` 回调 → 汇总已补建条目
- Director 确认 τ=0.756 来源 → 更新 Table 2（可能需要重算或修正数值）
- Director 确认 J=13 vs J=16 缺口处理方式 → 更新论文文本（"24 trained → 13 used" 的说明措辞）
- Director 决定是否修复 3 个缺失 3B 模型 pipeline 重跑 J=16 → 如果修，需 eval d000_s123 + 修 naming mismatch
- fig_dose_response 数据异常（0.5B MMLU accuracy 随 dosage 下降 0.41→0.27）→ results.tex L57 "monotonically increasing" 描述需修正
- D129 framing pivot 后 Reviewer 打分 6/10 → 可能还需进一步调整

### 5. 🎯 战略上下文
- **核心 pivot (D129)**: 论文从 "contamination detection via γ" 转为 "IRT calibration value comes from θ, not γ"。γ 是 diagnostic（exploratory），θ 是 calibration（confirmed）。这是投稿 EMNLP 2026 ARR May 25 的 framing。
- **关键证据链**: J=13 γ 全域非显著 → γ 不是 paper 的 selling point → θ 分离显著（Δθ pooled=0.50, CI excludes 0）→ calibration MAE 低（0.006-0.020）→ B3=ContamCal ranking → calibration value = IRT θ estimation itself
- **最易判断错的事**: 不要试图让 γ "work"。N=23 的显著 γ 是 0.5B position bias artifact。J=13 证实了这一点。继续在 γ 上投入是错误方向。
- **Catch-22 insight**: IRT 需要 ability variance 检测 γ，0.5B 提供 variance 但 variance 来自 position bias 不是真实能力差异。这本身是方法论贡献（论文 Section 4.4）。
- **投稿倒计时**: T-8 天 (May 25)。Paper Agent 已完成 D129 rewrite (Reviewer 6/10)。Figure placement 是下一个 blocking step。


---
