# agent / loop_5.md

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`f76e85caeb8e386b1263.json`](../../sessions/f7/f76e85caeb8e386b1263.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-15T13:45:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: autodl-5090 cuda:0-3（4×5090）。不得用其他设备
- submit_training_job 命令必须 `bash -c "..."` 包装，且在 swift 命令前显式 `CUDA_VISIBLE_DEVICES=N`（tmux wrapper 不可靠传递环境变量，2026-05-14 OOM 事故教训）
- eval 参数是 `--device cuda:0`（不是 `--gpu 0`），因为 CUDA_VISIBLE_DEVICES 已映射物理 GPU
- Vanilla 数据量 4,358 samples，TaxEI/Random 数据量 9,029 samples——不要搞混
- 所有 dose-response seed=42 实验对比 vanilla seed=42 (61.7%)，不对比 3-seed 均值 (65.3%)
- Checkpoint 路径查找必须用 `sort -V`，不要硬编码 checkpoint 号

### 2. 🖥️ 基础设施快照
- 服务器: autodl-5090, 账号 root, 工作目录 `/root/autodl-tmp/tax_error_inject_agent`
- Python: `/root/miniconda3/bin/python`，激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型: `/root/autodl-tmp/models/Qwen/Qwen3-8B`
- 数据: `data/mini_pipeline_v4/sft_{vanilla,taxei,random}_v4.jsonl`（full-scale）；`data/mini_pipeline_v4/ablation_fixed/sft_{taxei,random}_v4_fixed_inject{10,25,50}.jsonl`（dose-response）
- ms-swift 版本 4.2.0
- 论文 tex: 本地 `docs/paper/`，已同步到服务器同路径。Figure 在 `figures/paper/`
- **活跃进程（5-seed Batch 1）**:
  - vanilla seed=1: PID 154589, tmux=v4-vanilla-seed1, cuda:0（~45 min，约 14:25 UTC 完成）
  - vanilla seed=7: PID 154666, tmux=v4-vanilla-seed7, cuda:1（~45 min）
  - taxei seed=1: PID 154937, tmux=v4-taxei-seed1, cuda:2（~90 min，约 15:10 UTC 完成）
  - taxei seed=7: PID 155145, tmux=v4-taxei-seed7, cuda:3（~90 min）

### 3. 📊 当前状态
**刚完成**: D025 Wave 1 的 4 个并行任务中 3 个 CPU 任务已完成，GPU 训练在跑。

**D022 多 seed dose-response**: 全部 12 eval 完成。完整表已汇报 Director。Registry 中 D022 条目大部分丢失（只剩 v4-random-fixed-inject50-s0-eval 和 s123-eval 有 metrics），但服务器上 eval JSON 全在。

**D025 Wave 1 状态**:
| 任务 | 状态 |
|------|------|
| 5-seed 训练 Batch 1 | 🔄 RUNNING（4 GPU 占满） |
| Recovery-paired injection | ✅ 代码完成，**等 Director 审批** $15.31 API 费用 |
| Qualitative failure analysis | ✅ TaxEI loop_repetition 2.2× |
| Training dynamics | ✅ 无 per-sample loss，推荐 post-hoc forward pass |
| Figure 1 重生成 | ✅ 3-seed 版 18KB PDF |
| 论文 PDF 编译 | ✅ 7 页，缺 fig2 + fig_app placeholder |

**Recovery eval（之前 Director 指令）**: Batch 1（vanilla s0/s123 + taxei s0/s123）已提交过（PID 147731/147871/148014/148159），但 cron 从未回调，状态不明。**5-seed 训练已覆盖这些 GPU**，recovery eval 可能被终止了。需要检查结果文件是否生成。Random s0/s123 recovery eval 尚未提交。

### 4. 📋 待办（条件触发式）
- Vanilla seed=1/7 训练完成（~14:25 UTC）→ 立即在 cuda:0,1 提交 Random seed=1, seed=7 训练
- TaxEI seed=1/7 训练完成（~15:10 UTC）→ cuda:2,3 提交 6 个 clean eval（vanilla/taxei/random s1/s7，每个 ~15 min，轮流跑）
- 6 个 5-seed eval 全部完成 → 汇总 5-seed 表（5 seeds × 3 methods），更新 ROADMAP，汇报 Director
- Director 审批 recovery-paired API → spawn Worker 执行 `gen_recovery_paired.py`（$15.31）
- Director 决定是否做 post-hoc forward pass → spawn Worker 用 checkpoint 分别算 clean/injected subset loss
- Recovery eval 结果需确认：检查 `eval_results/v4_{vanilla,taxei}_recovery_eval_s{0,123}.json` 是否存在
- 缺失论文图表：需生成 `fig2_operator_gradient.pdf` 和 `fig_app_training_curves.pdf`

### 5. 🎯 战略上下文
**项目已转 long paper (D025)**：从 4 页 EMNLP workshop 短文扩展为 8 页长文。核心 narrative 是 negative result——taxonomy-guided error injection 在 embodied planning (ALFWorld) 无效。

**决策链关键节点**: D014 转 negative paper → D017 dose-response 揭示阈值效应 → D022 3-seed 验证 → D025 long paper 扩展

**核心结论（所有 pairwise 均 NS）**: Vanilla 65.3% > Random 63.1% > TaxEI 56.7%。Injection 有害但不显著。TaxEI 比 Random 更差（taxonomy 标签是额外负担）。

**易踩的坑**:
1. Registry 经常丢条目——不要信 registry 是完整的，服务器上的 eval JSON 才是 truth source
2. Cron 回调不可靠——几乎所有实验都需要手动 spawn Worker 检查完成状态
3. Worker 不能做长阻塞等待（>2 min timeout）——需要用 ssh_execute 内嵌 bash 循环或分多次 Worker
4. 5-seed 训练 Vanilla（4,358 samples）~45 min，TaxEI/Random（9,029 samples）~90 min——Vanilla 先完成，要马上用空出的 GPU 跑 Random
5. 50% injection 结果方差极大（SD ~12pp），不要对单个 seed 的 50% 结果下结论
6. `v4-vanilla-seed7` registry 条目是旧的（之前被 killed），现在重新训练，但 registry 状态是 DONE+killed——需要重置或创建新条目


---
