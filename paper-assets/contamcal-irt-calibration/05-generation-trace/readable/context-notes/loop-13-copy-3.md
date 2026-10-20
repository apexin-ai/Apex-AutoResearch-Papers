# reviewer / loop_13.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`dff6d47062082739ccbf.json`](../../sessions/df/dff6d47062082739ccbf.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-16T10:13:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：项目使用 cuda:0-5 全部 6 张卡，但各进程必须显式 `CUDA_VISIBLE_DEVICES=X`，不允许隐式占用
- lora_alpha=16 已被 D076 blacklist，所有实验必须 alpha=32, lr=5e-5
- S3 信号（perplexity）已被 D098 排除，不进入 RRF/IRT，仅保留 S1(embedding)/S2(Min-K++)/S4(self-critique)
- Cron on_failed 多为误报（wrapper PID 退出触发），不要直接标 critical——先检查子进程是否正常完成 + "ALL DONE" 标志

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-21977`，工作目录 `/root/contamcal-irt-calibration`
- 数据盘：`/root/autodl-tmp/`（模型 checkpoints、signals 输出、eval 结果）
- Python：conda base `/root/miniconda3/bin/python`
- 关键路径：
  - 训练 checkpoints: `/root/autodl-tmp/exp001/checkpoints/`
  - 信号输出: `/root/autodl-tmp/exp002/signals/`
  - RRF 输出: `/root/autodl-tmp/exp003/rrf_05B_15B/`
  - Eval 结果: `/root/autodl-tmp/exp001/eval_results/`
  - IRT 脚本: `/root/contamcal-irt-calibration/exp006/`
  - MMLU domain gamma 输出: `/root/autodl-tmp/exp006/results_mmlu_domain_gamma/`
- 活跃进程（截至 handoff）：
  - cuda:1 — 3B d100 signals（PID 未记录，预计 1-2h）
  - cuda:2 — 1.5B d100_s123 signals（PID 746777/746785，日志 `exp002/run_15B_d100_s123_cuda2.log`）
  - cuda:4 — 3B d000 signals（预计 1-2h）
  - cuda:0 — batch 信号进程（当前在 d025，后续到 d100 会 skip 已有）
  - cuda:3 — 3B-Instruct eval（可能已完成）
  - cuda:5 — 0.5B 双进程

### 3. 📊 当前状态
刚完成审查：
- `worker_run_arc_2pl_gamma_05b_15b`：ARC 2PL+γ PPP=0.000，确认问题是 N vs items 不平衡 + 多维性，非模型选择问题。已 post [info] 给 Director。
- `worker_ops_diag_signals_3B_d005_a32_s42`：正常完成，cuda:2 释放。
- `worker_ops_allocate_cuda2_next_task`：cuda:2 分配给 1.5B d100_s123 signals。
- `cron:on_failed:exp_002_signals_3B_d005_a32_s42`：又一个 cron 误报，先前 worker 已确认正常完成。

等待中：
- 3B signals 完成（cuda:1/4，预计 1-2h）→ 3B 加入 pooled IRT 后 N 可达 ~16
- 1.5B d100_s123 signals 完成 → 1.5B s123 全系列告捷
- 3B eval 全部完成 → 可跑 scale-stratified IRT（0.5B/1.5B/3B 分层）

### 4. 📋 待办
- 3B signals 全部完成 + 3B eval 全部完成 → 审查 scale-stratified IRT 结果（关注 PPP 是否改善、γ 方向是否与 raw dose-response 一致）
- N≥16 pooled IRT 重跑 → 这是 paper 可引用的最终版，严格审查 GSM8K γ≈0 是否仍成立（若是，需要论文解释 format confound D044）
- ARC IRT 若 N≥12 后 PPP 仍=0 → 建议 paper 排除 ARC IRT 或仅报 raw calibration
- Llama-3.2-3B 跨架构验证完成 → 审查是否引入新 confound（不同 tokenizer/chat template）
- 任何 paper 章节写作提交 → 切换到模式 B 对抗审查

### 5. 🎯 战略上下文
- **核心发现**：GSM8K contamination 有显著 dose-response（14%→70%），但 IRT pooled γ≈0——矛盾来源可能是 0.5B 模型 GSM8K 全面低分（format 问题）拉平了 pooled signal。Scale-stratified 分析是关键。
- **D044 format confound**：d000 SFT 破坏 GSM8K 生成格式，contamination 部分恢复格式而非真正提升能力。这是本项目最大叙事风险——paper 必须诚实处理。
- **Cross-seed variance**：GSM8K s42 vs s123 差 21.6pp（同 dosage），论文需 acknowledge。
- **MMLU domain gamma 异质性**：STEM_Math 负 γ（-0.55, 差 PPP），Other/Humanities 正 γ。说明 contamination effect 非均匀，支持 domain-specific 分析 narrative。
- **易错点**：Worker 曾错误声称"contamination 仅针对 GSM8K"——实际所有 benchmark 均等 5% contamination，差异效果来自 format sensitivity 而非 targeting。审查时注意类似因果混淆。
- **Paper target**：EMNLP 2026 ARR May 25（T-9 days）。


---
