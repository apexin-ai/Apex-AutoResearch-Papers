# agent / loop_23.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_23.md`
- **Structured JSON:** [`434b1d2739711409c164.json`](../../sessions/43/434b1d2739711409c164.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 23
reason: idle_timeout
updated: '2026-05-21T03:24:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-29999 cuda:0,1,2,3 + cqa1-21977 cuda:0，共 5 张。白名单外的 GPU 即使 Director 指令也必须 push back
- evaluate.py 必须用统一版本 md5=`001a9bc23f808c47d25ef9eaeecb81f1`（37591 bytes），旧版有 mc_suffix bug 导致 +3-4pp 系统偏差
- Gemma-2 GSM8K 已正式排除（D175: catastrophic forgetting），不要再尝试
- Qwen-14B GSM8K headline 数字用 range [+5.7, +20.5pp]，不要单独引用 +20.47pp（D177: d000 baseline seed-sensitive）
- EMNLP 2026 ARR May 25 截稿，D+2/6，不能 fallback 到次级会议

### 2. 🖥️ 基础设施快照
- **westd-29999**: 4×RTX PRO 6000 96GB, /root/contamcal-irt-calibration/, conda base (/root/miniconda3/bin/python), 磁盘 427G/879G (49%)
- **cqa1-21977**: AutoDL, /root/contamcal-irt-calibration/, 磁盘根分区紧张(98%), 数据盘 1.5T/4.0T
- 模型 checkpoints: /root/autodl-tmp/exp001/checkpoints/{family}_d{dosage}_s{seed}/
- HF cache: /root/autodl-tmp/.hf_cache (AutoDL) / 默认 (westd)
- 活跃进程（reconcile 确认）:
  - sft_phi4_s0_sweep: westd cuda:0, PID 286341
  - sft_gemma2_s0_sweep: westd cuda:1, PID 314035
  - sft_qwen14b_s0_sweep: westd cuda:3, PID 311554
  - sft_qwen7b_s0_cqa1: cqa1 cuda:0, PID 313407
- **westd cuda:2 空闲**（eval_olmo2_s0_mmlu 刚完成）

### 3. 📊 当前状态
刚完成 eval_olmo2_s0_mmlu 分析并汇报 Director：
- OLMo-2 s0 MMLU: d000=55.34%, d100=56.72%, Δ=+1.38pp（确认 Benefit-sat pattern）
- Cross-seed: s42 Δ=+3.21pp (baseline 53.79%), s0 Δ=+1.38pp (baseline 55.34%), d100 绝对值收敛 ~57%（ceiling compression）
- Registry 已更新 DONE/success，memory.md 已写入 ceiling compression 洞察

RUNNING 实验（4 个 s0 sweep，都是第三颗种子用于 triple-seed bootstrap CI）:
- sft_phi4_s0_sweep: Phi-4 Immune 模式，预期 ±0.5pp
- sft_gemma2_s0_sweep: Gemma-2 Benefit 模式，预期 +3-4pp
- sft_qwen14b_s0_sweep: Qwen-14B U-collapse 模式，预期 -9pp
- sft_qwen7b_s0_cqa1: Qwen-7B V-recovery 模式，预期 V 形

等待：Director 回复 cuda:2 下一个任务（建议了 OLMo-2 s123 MMLU eval 或 s0 GSM8K eval）

### 4. 📋 待办
- Director 回复 cuda:2 任务 → 立即派 Worker 提交（OLMo-2 s123 MMLU eval 或 s0 GSM8K eval）
- sft_phi4_s0_sweep 完成 → spawn eval worker 跑 Phi-4 s0 MMLU 5-shot eval on cuda:0
- sft_gemma2_s0_sweep 完成 → spawn eval worker 跑 Gemma-2 s0 MMLU eval on cuda:1
- sft_qwen14b_s0_sweep 完成 → spawn eval worker 跑 Qwen-14B s0 MMLU eval on cuda:3
- sft_qwen7b_s0_cqa1 完成 → spawn eval worker 跑 Qwen-7B s0 MMLU eval on cqa1:0
- 所有 5 家族 s0 MMLU eval 完成 → triple-seed bootstrap CI 计算（D+3 任务）
- 各 s0 MMLU eval 完成后 → 对应 s0 GSM8K eval（除 Gemma-2）
- OLMo-2 s123 MMLU eval 缺失 — registry 里只有 s42 和 s0 的 MMLU 数据，s123 训练 checkpoints 存在（sft_qwen7b_olmo2_s123_sweep）但未跑 MMLU eval

### 5. 🎯 战略上下文
- 核心故事：5 observed dose-response profiles，方向由 baseline ability 决定（threshold 64.7%），形状由 benchmark 特性决定，跨 benchmark 迁移是 family-dependent 的
- 5 archetypes: Immune (Phi-4), U-collapse (Qwen-14B), V-recovery (Qwen-7B), Benefit (Gemma-2), Benefit-sat (OLMo-2)
- s0 是第三颗种子，用于 triple-seed bootstrap CI —— 这是论文统计可信度的关键，缺种子 = reviewer 会打回
- OLMo-2 s0 刚发现 ceiling compression 效应（高 baseline → 小 delta），论文中报告 delta 时需注意：不能简单 mean(s42, s123, s0) 的 delta，要报告 absolute 值 + CI
- 易错点：OLMo-2 s42 MMLU 数据不在独立 registry 条目中（可能在批量 eval 或直接文件中），ROADMAP 5-Pattern 表是 truth source（baseline=53.79%, Δ=+3.21pp）
- IRT fitting 已完成（25 respondents × 14042 items, γ_mean=0.025），不需要重跑
- 论文 7 页 main text 已就绪，D+3 开始 GSM8K subsection patch + triple-seed 更新


---
