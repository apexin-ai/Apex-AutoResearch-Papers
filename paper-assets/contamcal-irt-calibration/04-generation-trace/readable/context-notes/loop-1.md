# director / loop_1.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`ac56312597421f236937.json`](../../sessions/ac/ac56312597421f236937.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-13T20:35:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 cqa1-21977 全部 6× RTX 4090D (cuda:0-5) 已分配给本项目，不要用其他服务器的 GPU
- HumanEval 已降级为 appendix case study (D009)，主实验只用 MMLU/GSM8K/ARC-Challenge 三个 benchmark
- SFT 注入用 ALL paraphrases（不过滤 QC），ConStat 信号用 QC-passed only (D010)。QC-failed 是 BLEU>0.3（太接近原文），不是语义偏移——contamination effect 反而更强
- per-benchmark γ_k 是 PRIMARY 模型，global γ 是 ABLATION（不要反过来）
- 投稿目标 EMNLP 2026 ARR May 25，12 天冲刺，用户承诺"提供足够多的资源"

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977 (connect.cqa1.seetacloud.com)，工作目录 /root/contamcal-irt-calibration
- Python：需确认（aml-train 镜像，可能 conda base）
- 数据盘：/root/autodl-tmp/（用户指定"有数据盘用数据盘"）
- HF cache：应在数据盘
- 模型：Qwen2.5-0.5B/1.5B/3B (base)，Qwen2.5-7B-Instruct (paraphrase gen)
- 活跃进程（截至 handoff）：
  - GPU 0: MMLU vLLM paraphrase PID 204758，进度不确定（19% 或 3%，口径差异）
  - GPU 1: 可能空闲（GSM8K 完成），待 Agent 执行 seed=123 0% SFT
  - GPU 2: 可能空闲（ARC 完成），待 Agent 执行 seed=123 0% SFT
  - GPU 3: 0.5B 0% SFT seed=42 PID 208938，~1.0s/step，3125 steps
  - GPU 4: 1.5B 0% SFT seed=42 PID 210121，~2.0s/step
  - GPU 5: 3B 0% SFT seed=42 PID 210671，~4.1s/step，ETA ~07:20 UTC
- Cron 监控已注册：exp_001 + exp_001_sft_0pct 各 scale，300s 间隔
- CPU 本地：exp-004 PID 219346（sim sweep，~28h total），exp-005 PID 234646（noise propagation，~40h）

### 3. 📊 当前状态
Phase 1 paraphrase: ARC+GSM8K 完成，MMLU 仍在 GPU 0 上跑（bottleneck）。Phase 2 数据准备已完成（仅 ARC+GSM8K，MMLU 待补）。0% dosage SFT 在 GPU 3-5 训练中。Agent 队列 depth=1，正在处理 Phase 2 Worker 回调，我的 "GPU 1/2 空闲填充" 指令排在后面。

Registry RUNNING: exp_001_sft_injection, exp_001_sft_0pct (×3 scales), exp_004_sim_sweep, exp_005_noise_propagation。Fisher derivation 完成（appendix.tex 6页 + 数值验证，structural/practical identifiability 定义已由 Paper Agent 补充）。

等待中：Agent 处理 GPU 1/2 seed=123 指令；MMLU paraphrase 完成 cron 回调；0% SFT cron 回调。

### 4. 📋 待办
- MMLU paraphrase 完成 → 重跑 prepare_sft_data.py 加入 MMLU → 生成最终 5 dosage SFT 数据 → 立即启动 Phase 3 contaminated SFT (5%/25%/50%/100% × 3 models)
- 0.5B 0% SFT seed=42 完成（GPU 3）→ GPU 3 加入 Phase 3 contaminated SFT 轮转
- Phase 3 全部 15 runs seed=0 完成 → 启动 Phase 4 evaluation（parallel across GPUs）→ 然后 seed=1,2
- exp-004 sim sweep 完成 → 检查 identifiability 阈值是否与 Fisher 理论一致，N=100/200 条件是否 fit time 爆炸
- exp-005 noise propagation 完成 → 检查 ME model coverage improvement
- Phase 4 eval 完成 → 启动 exp-002 signal pipeline → exp-003 RRF → exp-006 IRT calibration（主实验链）

### 5. 🎯 战略上下文
决策链：D006(DDL→EMNLP) → D007(re-dream gate) → D008(Dream D2 分析) → D009(HumanEval 降级) → D010(QC 策略)。

Fisher 推导是重大进展——Dream D2 三档都标 critical gap，现已补上（Theorem 1 + 2 Corollaries + structural/practical 定义）。论文写作 Intro/Method/Related Work/Experiments 初稿已有，Paper Agent 已完成 D2 citation patches（DIF文献、ML calibration 消歧、conformal prediction）。

易错点：
1. MMLU 进度统计有口径差异（speed-check worker 报 19% vs Phase 2 worker 报 3%），以 cron 实际监控为准
2. exp_001 曾被误判 DONE/failed 触发 on_failed hook（仅通知无破坏），registry 已回退 RUNNING，但 cron 可能再次误判——遇到类似情况先检查进程再改 registry
3. vLLM 只有 MMLU 成功用上，GSM8K/ARC 都 fallback 到 transformers（~10x 慢），后续如需重跑注意
4. QC-failed paraphrases 是"太像原文"不是"语义偏移"——Reviewer 曾搞反方向，contamination effect 不受影响
5. Phase 3 SFT 数据必须等 MMLU 完成后重新生成（dosage 计算需全部 3 benchmark 的 paraphrase pool）


---
