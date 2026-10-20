# agent / loop_12.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`2dacc3f750a2afaa3f06.json`](../../sessions/2d/2dacc3f750a2afaa3f06.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-15T18:11:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-22162 cuda:0-3（RTX 6000 Pro ×4），不得使用白名单外 GPU
- GSM8K profiling 脚本必须统一 5 项参数：`run_profiling_gsm8k.py` + `gsm8k_test.json` + n=50/seed=42 + min_phase_length=10 + save_generations。之前因参数不一致被 kill 两轮
- GSM8K profiling 存在已知聚合 bug：合并目录 `analysis_output/gsm8k/` 数据不可信（ii_low=0, PPL=NaN），必须用 per-sparsity 目录 `profiling_output_gsm8k_{model}_{strategy}_s0{XX}/` 的数据
- QW rand_s030 per-sparsity 数据缺失，merged 数据有极端负值，不可用
- Appendix B G_× 已从 58-241× 更新为精确 n=500 值 21-64×，不要引用旧值
- Figure 1 caption 仍写旧 G 值 (69×-274×)、Table 1/2 标注 n=50——尚未修复，Paper Agent 需同步

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162，工作目录 `/root/autodl-tmp/pacs/`
- Python：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B` + `Qwen2.5-7B-Instruct`
- 数据：`/root/autodl-tmp/pacs/data/math500.json` (MATH-500) + `gsm8k_test.json` (1319 题 GSM8K test)
- 输出：`/root/autodl-tmp/pacs/analysis_output/` + `profiling_output_*/`
- 活跃进程：SF5 spot check 可能刚完成（worker_ops_sf5_completion_check 正在验证），无其他 GPU 进程
- Cron：sf5_asymmetric_spot（PID 259632，可能已退出待清理）

### 3. 📊 当前状态
**刚做完**：Round 7+8 审稿修复全套分析任务——N1a answer-region、W4 structural specificity、W5 LLaMA power、W6 outlier robustness、GSM8K profiling (DS+QW)、token length 分层分析、Appendix B 精确 G_×、引用验证 4 篇、Figure 1 数据源确认。

**Registry RUNNING/PREPARING**：无（全部 DONE 或等 SF5 确认）。SF5 可能刚完成，worker_ops_sf5_completion_check_20260515T181007 正在检查。

**等待中**：
- SF5 completion check Worker 回调 → 更新 registry + 汇报 Director
- Director 批准 GSM8K bug 修复方案（4 个 fix：NaN 过滤、nanmean、bootstrap 解包、bf16）→ 修复后重新聚合
- Director 安排 Paper Agent 更新 appendix.tex (G_× 21-64×) + caption/table 数据同步
- Director 决定 consistency check → Group C Round 提交时间线

### 4. 📋 待办
- SF5 Worker 回调到 → 检查成功/失败，更新 registry，汇报 Director phase gradient 方向一致性
- Director 批准 GSM8K bug fix → 派 Worker 修复 4 个 bug + 重新聚合 16 conditions 汇总表
- QW rand_s030 如需补跑 → Director 分配 GPU 后提交
- Paper Agent 完成 Phase 2+3 → Director 安排 consistency check
- 截稿 2026-05-25（距今 10 天）→ 所有分析数据已就绪，等 Paper Agent 整合 + 提交

### 5. 🎯 战略上下文
**核心结论**：Phase-gated compound sparsity severity 在 MATH-500 (n=500) 上 confirmed（DS 0.39→8.48, QW 0.07→3.16, 全部 p<1e-14）。GSM8K cross-benchmark 验证：phase gradient 复现但 strategy specificity ratio 从 15-36× 衰减至 1.1-2.2×（task-modulated, D075 决策入主文非 appendix）。

**关键决策链**：D063 random threshold story → D066/D067 审稿 action matrix → D068 N2 机制降级 → D075 GSM8K framing（task-modulated strategy specificity）

**易错点**：
- GSM8K 数据有两层：per-sparsity 目录（正确）vs 合并目录（有 bug）。永远用 per-sparsity 目录
- Cron 对非 W&B 实验频繁误报 "failed"（进程正常退出 exit code=0 但 cron 检测不到）。收到 cron failed 先 SSH 检查日志再判断
- Token length 假设在 MATH-500 成立（p<0.013）但在 GSM8K 不成立——需要 "task complexity" 作为联合解释变量，不要简单说 "length explains everything"
- G_× 精确值 (21-64×) 比校准估计 (51-183×) 低很多——n=50 方差严重高估，这是正常的不是 bug


---
