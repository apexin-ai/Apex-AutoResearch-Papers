# agent / loop_6.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`f102ad9e282ec3c5b791.json`](../../sessions/f1/f102ad9e282ec3c5b791.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-15T16:03:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-11235 的 cuda:0 + cuda:1（gpu_ids 白名单）
- DeepSeek 组实验使用旧代码版本（`load_best_model_at_end` 已注释为 TEMP_DISABLED），组内必须保持一致，不要给 DeepSeek 组后续实验启用该功能
- exception_only 的 headline 数字是 epoch 1 的 99.83%（非 final epoch 的 99.33%），DeepSeek 也是 epoch 1 最优——汇报时标明 checkpoint 来源
- vota_seed123 因 OOM 失败 2 次（cuda:1 被其他进程占用），已放弃；VOTA seed robustness 降优先级（D017 决策：exception_only 才是 primary claim 核心证据）
- ae_only 的 fallback locals 行不构成 data leakage（D013 裁定），不要重新质疑

### 2. 🖥️ 基础设施快照
- **服务器**: westd-11235，工作目录 `/root/trace-verdict-study`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **模型路径**: Qwen → 默认 HF cache `/root/autodl-tmp/.hf_cache`；DeepSeek → `/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct`
- **数据**: `/root/autodl-tmp/trace-verdict-study-data/{condition}_{train,test}.jsonl`（train 4720 / test 1190）
- **Checkpoints**: `/root/autodl-tmp/trace-verdict-study-checkpoints/{condition}/final/`
- **W&B**: project=`trace-verdict-study`
- **活跃进程**:
  - `deepseek_full_trace_seed42`: PID 112289, tmux session, cuda:0（提交于 13:47 UTC，约 2h 训练 + eval）
  - `exception_only_seed123`: PID 124197, tmux session, cuda:1（提交于 15:54 UTC，约 2h）
- **Cron**: 上述两个实验各有一个 cron 监控

### 3. 📊 当前状态
**刚做完**: DeepSeek 4 条件中 3 条已出（no_trace 73.4% / VOTA 84.5% / exception_only 99.3%），calibration analysis 完成（ECE 数据已入 registry），exception_only seed123 (Qwen) 已提交。

**RUNNING（2 个，双卡满载）**:
- `deepseek_full_trace_seed42` (cuda:0) — DeepSeek 组最后一条，预计很快完成
- `exception_only_seed123` (cuda:1) — Qwen exception_only seed robustness 第一跑

**PREPARING（3 个，等 GPU 释放）**:
- `exception_only_seed456` — Qwen exception_only 第二个种子
- `deepseek_exception_only_seed123` — DeepSeek exception_only 第二个种子
- `vota_seed456` — 已被 Director 降优先级

**等待中**: 无 Worker 回调待处理。两个 cron 在跑。无 Director 未决决策。

### 4. 📋 待办（条件触发式）
- `deepseek_full_trace_seed42` cron 回调到 → 分析结果 + 完成 DeepSeek 4 条件对比表 + 更新 report.md + 汇报 Director（DeepSeek 组全部完成）→ cuda:0 空出后提交 `deepseek_exception_only_seed123`
- `exception_only_seed123` cron 回调到 → 分析 seed robustness（与 seed42 的 99.83% 对比）→ cuda:1 空出后提交 `exception_only_seed456`
- 两个 seed robustness 都完成 → 计算 mean ± std → 更新 paper_framing.md 中 Claim 1 的 evidence
- DeepSeek 全部完成 + seed robustness 有初步结果 → 正式更新 framing → 汇报 Director 启动 Paper Agent（ROADMAP 5/16 里程碑）
- GPU 空窗时 → 考虑 `vota_seed456`（低优先级）或 plan_005 DebugBench（如时间允许）

### 5. 🎯 战略上下文
**核心发现**: Exception signal 是 universal 诊断信号。Qwen 99.83% / DeepSeek 99.33%——跨模型 gap = 0pp（最佳 checkpoint 下）。VOTA 的价值不在压缩本身，而在隔离 exception 这一关键信号。

**Claim 结构已转向**（D016/D017）:
- Claim 1: Exception events 是 near-perfect fault indicator（不再是 "VOTA compression"）
- Claim 2: Full trace 性能受限来自 gradient dilution (26%) + info overload (74%)
- Claim 3: Two-tier hierarchy: exception (99.8%) >>> loop (85.6%) >> ae (redundant)

**关键决策链**: D008(ae无关) → D009(gradient dilution minor) → D010-D011(exception主导) → D013(ae_only不是leak) → D014-D016(DeepSeek确认exception universal) → D017(seed robustness优先exception_only)

**易错点**:
- DeepSeek VOTA 只有 84.5%（vs Qwen 99.4%），不要把 VOTA 当 universal claim——只有 exception_only 跨模型稳定
- epoch 1 vs final accuracy 解耦：Qwen 和 DeepSeek 都是 epoch 1 最优，continued training 可能过拟合——汇报时必须说明是哪个 checkpoint
- `vota_seed123` 已失败 2 次不要再试（OOM），VOTA seed robustness 用 `vota_seed456` 但优先级低
- DDL 是 5/25 ARR，还有 10 天，论文写作应在 seed robustness 初步结果后尽快启动


---
