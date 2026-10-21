# reviewer / loop_2.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`7b4fd6c8168847024fdf.json`](../../sessions/7b/7b4fd6c8168847024fdf.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T12:46:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- autodl-5090 有 4 张 RTX 5090，gpu-5090-4x-2 有 4 张 RTX 5090。两台服务器均为本项目独占，无 gpu_ids 白名单限制，但需确认无其他项目抢占
- `run_mvp_pilot.py` 默认 `--num_test 200`！必须显式传 `--num_test 551`（SciERC）或 `--num_test 99999`（CoNLL/WNUT），否则只跑 200 实例。已踩坑：exp001_seed123/456 和 exp008 全部只跑了 200 实例而非目标 551
- Registry 更新滞后是常态：Worker 经常 launch tmux 后退出报 done，但训练/推理仍在跑。必须 ssh_read_only 独立验证实际状态，不信 worker_done 通知
- pilot script 的 logprob AUROC 在 median_f1=1.0（如 CoNLL）时输出 0.5000（bug），需用 5-signal 分析脚本的 AUROC 值

### 2. 🖥️ 基础设施快照
- **autodl-5090**: `/root/autodl-tmp/struct_self_consist_ie`，conda base (`/root/miniconda3/bin/python`)
  - 模型: `checkpoints/qwen3-8b-scierc-merged-v2` (SciERC), `checkpoints/qwen3-8b-conll2003-merged` (CoNLL), `checkpoints/qwen3-8b-wnut17-lora` (训练中)
  - 数据: `data/scierc/processed_data` (551), `data/conll2003/` (3453), `data/wnut17/` (~3400)
  - HF cache: `/root/autodl-tmp/.hf_cache`
  - 活跃: exp_003 WNUT 训练 cuda:1 (~25% 完成于 12:30 UTC, ETA ~24min 后)
- **gpu-5090-4x-2**: 同路径结构，代码通过 git sync
  - cuda:1 有 vLLM 进程 (PID 58518) + python (PID 55644)，可能是残留需清理
  - exp007 LLaMA 下载/fine-tune 计划在 cuda:3
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/`
- 无 wandb 配置（项目不用 wandb）

### 3. 📊 当前状态
刚完成 exp_002 CoNLL-2003 pilot 审查。**关键发现：EM > SJ 在 CoNLL 上统计显著（Δρ=-0.015, CI 不跨零）**，与 SciERC 排名完全相反。已提交 critical 报告给 Director，建议论文叙事调整为"SJ 优势与任务难度正相关"。

同时发现 gpu-5090-4x-2 上 3 个实验（seed123/456/exp008）**全部只跑了 200 实例**（非目标 551），已报 critical。

Registry 状态:
- **DONE**: exp_002 (CoNLL pilot, 关键正面结果), exp_016 (ensemble, mixed), exp_008/seed123/seed456 (200 实例, 需重跑全集), exp_001~005/012~015 (CPU 分析)
- **RUNNING**: exp_003 (WNUT 训练, ~25% → 预计 12:55 UTC 完成), exp_001_n16_seed123/456 (registry RUNNING 但实际已完成)
- **QUEUED**: exp_007 (LLaMA-3.1-8B SciERC, gpu-5090-4x-2 cuda:3)
- **未启动**: exp_001 全集重跑 (T=1.0 551 实例 N=16), exp_008 全集重跑

等待: exp_003 训练完成 → merge → pilot → 5-signal 分析。Director 可能基于我的 Action Matrix 审查做出叙事决策。

### 4. 📋 待办
- exp_003 WNUT 训练完成 → 审查 merge + pilot 结果（注意 `--num_test` 必须指定全集！）→ 验证 SJ vs logprob 在第三个数据集上是否一致
- exp_007 LLaMA 开始训练 → 核实 GPU 设备 + 进程 PID + 训练进度
- exp_001/exp_008 全集重跑（551 实例）启动 → 核实 `--num_test 551` 参数
- 若 Director 回应 Action Matrix 审查 → 关注 W1 (exp-016 ensemble 叙事调整) 和 R4 (best-of-N 不 beat greedy 的应对)
- exp_002 CoNLL EM > SJ 结果 → 关注 Director 是否更新 paper_framing.md Claim 1 措辞

### 5. 🎯 战略上下文
**决策链核心**: D001→D011 (Dream 1 暴露缺 baseline) → D012 (SJ >> logprob confirmed) → D013 (voting_conf ≈ SJ, structural family) → D014 (SJ ρ 数据源不一致) → D017 (Dream 2 全 3/6, presentation 是瓶颈)

**论文最大风险不是实验不够，是叙事一致性**:
1. paper_framing.md 预设 "SJ > EM always"，但 CoNLL EM > SJ。叙事必须改为条件性结论
2. exp-016 best-of-N selection 不 beat greedy on NER。如果论文定位为 test-time scaling improvement，数据不支持。应转向 confidence estimation / selective prediction
3. headline result template 里的 "+Zpp F1 via best-of-N selection" 需要删除或大幅降调

**最容易判断错的事**:
- 不要把 exp001 原始结果（T=0.7, 200 实例）和 exp008/seed 结果（T=1.0, 200 实例）混为一谈。温度和 N 不同
- exp_012 和 pilot_004 的 SJ ρ 不一致（0.357 vs 0.383）是已知问题（D014），根因是 exp_012 重新采样。论文数字统一用 exp_015（从 pilot_004 原始数据重算全指标）
- gpu-5090-4x-2 上残留进程可能占 GPU 内存但不做计算，nvidia-smi 看到 25GB 占用不等于在跑实验
- DDL 2026-05-25（11 天），Paper Agent 是关键路径，不是更多 GPU 实验


---
