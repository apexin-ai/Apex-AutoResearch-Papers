# agent / loop_11.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`0b2bcbcdb595f5241da9.json`](../../sessions/0b/0b2bcbcdb595f5241da9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-15T12:01:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-22162 GPU 白名单：gpu_ids 需查 `get_project_status`，当前 4 张卡全被 sensitivity 分析占用
- SF5 asymmetric 代码已改好（run_profiling.py 加了 --head_sparsity/--kv_sparsity），但 **未启动**——必须等 GPU 空闲才能跑，不能抢占正在运行的 sensitivity 进程
- Crossover claim 限定："across all sparsity levels" 仅对 DeepSeek 成立；Qwen 无 crossover（random 在两个 phase 都更差），论文中不能写 "both models show crossover"
- Bonferroni 用 k=4 family-wise（不是 k=48），BH-FDR 做全局补充。之前 k=48 已被 Director 明确否决
- paper_provenance.yaml 中 random masking 叙事必须用 D063 threshold narrative（s015/s020 NS, s025+ significant but 3-39× smaller），禁止写 "random 0/8 significant"

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162，4× A100-80GB
- Python：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 项目代码：`/root/autodl-tmp/pacs/`（run_profiling.py 在 `pacs/profiling/`）
- 分析脚本：`/root/autodl-tmp/pacs_analysis/`
- n=500 profiling 数据：`/root/autodl-tmp/pacs/profiling_output_n500_bf16_{ds,qw}_{imp,rand}_s{015,020,025,030}/profiling_results.json`
- 模型：DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（路径在 profiling 脚本内 hardcoded）
- 活跃进程（截至 handoff）：
  - PID 218877: seg_sensitivity_v2.py --model deepseek, GPU 0, 160/500 ~2.4h remaining
  - PID 219130: seg_sensitivity_v2.py --model qwen, GPU 2, **可能已完成**（ETA 早于 handoff）
  - PID 220988: mpl_sensitivity.py --model deepseek, GPU 1, 80/500 ~5h
  - PID 221265: mpl_sensitivity.py --model qwen, GPU 3, 80/500 ~4.6h
- 本地 artifacts：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_analysis/`

### 3. 📊 当前状态
**刚完成**：Round 6 审稿数据提取三项（N2a Gini baseline、N1 Table 2 n=500 替换数字、W7 引用验证），已汇报 Director。

**等待中的 Worker**：
- `worker_ops_compile_pdf` — 编译论文 PDF 并下载到本地（用户紧急请求）
- Qwen seg spot fill 已完成（segmentation_sensitivity.csv 已扩充为 24 行双模型数据）

**Registry 关键条目**：
- `sf5_asymmetric_spot`: PREPARING — 代码就绪，等 GPU 空闲启动。配置：(h=0.20,kv=0.30) + (h=0.30,kv=0.20)，n=50 DS only
- `c2_n500_deepseek`: DONE/success
- `c2_qw_n500_r3`: DONE/success

**服务器上 sensitivity 分析**：seg_sensitivity_v2（全量 n=500 tercile/quartile/quintile）和 mpl_sensitivity（n=500 mpl=5/10/20）仍在跑，完成后需要：更新本地 CSV、注册 artifact、汇报 Director。这些进程没有 cron 监控，需要手动检查。

### 4. 📋 待办（条件触发式）
- PDF compile worker 回调 → 汇报 Director PDF 路径，通知用户
- seg_sensitivity_v2 QW 完成（可能已完成）→ 合并双模型全量 n=500 segmentation 数据到本地 CSV
- seg_sensitivity_v2 DS 完成 → 同上，更新 tercile 行为 n=500 全量数据（当前 tercile 行已是 n=500，quartile/quintile 是 n=50 spot check）
- mpl_sensitivity DS+QW 完成（~4-5h）→ 更新 min_phase_length_sensitivity.csv 为 n=500 全量数据
- 任一 GPU 空闲 → 立即用 submit_training_job 启动 sf5_asymmetric_spot（命令在 run_profiling.py --head_sparsity X --kv_sparsity Y）
- SF5 完成 → 按 on-experiment-done skill 处理：D>0 方向一致写 appendix "robust to asymmetry"；方向反转写 limitations
- Director 对 Qwen crossover framing 决策 → 更新 paper_framing.md 和 provenance

### 5. 🎯 战略上下文
- **目标**：EMNLP 2026 ARR，deadline May 25。Round 1 Weak Reject，正在做 D066 审稿修复
- **核心结论**：importance-based KV cache eviction 产生 phase-dependent compound interaction（II_low >> II_high），效应随 sparsity 单调递增（dose-response），random masking 无此效应（D063 threshold narrative）
- **决策链关键**：D063（random threshold narrative）、D064（d_z variance at n=50 resolved）、D066（审稿修复综合指令）
- **最容易判断错的事**：
  1. Qwen 的 crossover 结论——Qwen 没有 crossover，但主效应（D = II_low - II_high > 0）在两个模型都成立。不要混淆 crossover（策略排名反转）和 phase-gating（低相位 II 大于高相位 II）
  2. n=475 vs n=496——Qwen 有效 n=475（mid-phase null 45.2%），DeepSeek n=496。D gradient 只需 low+high phases 所以不受影响，但报告数字时必须用正确的 n
  3. sensitivity 分析进程没有 cron——需要手动 SSH 检查是否完成，不会有自动回调
  4. G ratio narrative——importance masking G=7-80×（远离 1），random G=0.5-1.3×（接近 1 但 6/8 conditions CI exclude 1）。说 random "practically negligible" 是对的，但不能说 "CI overlap 1"


---
