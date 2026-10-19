# agent / loop_3.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`1a02aac9f52a9e33abe3.json`](../../sessions/1a/1a02aac9f52a9e33abe3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-16T05:55:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 westb-13953 的 cuda:0 和 cuda:1。不可用其他 GPU。
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不能假设 .venv 存在。
- Scorer conditioning bug 已确认（D030/D031）：v5 系列的 scorer 用 visual_mean 而非 language embedding 作为 condition。v5 结果保留作为 "without proper conditioning" ablation baseline，不要丢弃。
- CoRL 2026 deadline：abstract 5/26，paper 5/29。距今 10/13 天。

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953，2x RTX PRO 6000 Blackwell 96GB
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 代码：`/root/acib`（scripts/train_acib.py, scripts/eval_acib.py, scripts/eval_acib_perturbed.py）
- 数据：`/root/autodl-tmp/libero_dataset`（273K frames）
- 模型 HF cache：`/root/autodl-tmp/.hf_cache`
- 旧实验迁移到：`/root/autodl-tmp/acib_outputs/`（根分区 symlink 指向）
- 活跃进程：
  - `acib_v5_div_reg_seed2`: PID 755664, tmux, cuda:1（cron 监控中）
  - `mvp1_baseline_plus_remaining` (libero_10): PID 675231, cuda:0（cron 监控中）
  - `mvp1_baseline_std_libero10`: PID 733616, cuda:1（cron 监控中）
  - `acib_v5_div_reg_eval_ckpt10000`: PID 806823, cuda:0（cron 监控中）

### 3. 📊 当前状态
**刚发生**：acib_v5_div_reg 在 step ~12800/20000 时 EXIT_CODE=1 崩溃（原因未查）。这是 v5 主训练 seed1。checkpoint-10000 存在且已在 eval 中。

**RUNNING（4 个）**：
- `acib_v5_div_reg_seed2`：seed 2 复现，checkpoint-5000 已验证（BC=0.933），继续训练中
- `acib_v5_div_reg_eval_ckpt10000`：ckpt-10000 在 4 suite 上的 eval（libero_spatial 已开始 rollout）
- `mvp1_baseline_plus_remaining`：smolvla_libero_plus libero_10 eval，64/500 rollouts done，预计 ~09:15 UTC 完成
- `mvp1_baseline_std_libero10`：smolvla_libero libero_10 eval

**PREPARING（1 个）**：
- `acib_v6_conditioned`：修复 scorer conditioning bug，Worker 正在改代码。核心改动：condition_source 从 visual_mean 改为 language embedding。

**等待中**：
- acib_v5_div_reg 的 failed 回调已触发但尚未被处理（需要查 log 定位崩溃原因）
- v6_conditioned Worker 完成后需提交训练

### 4. 📋 待办（条件触发式）
- acib_v5_div_reg failed 回调 → spawn Worker 查 log tail 定位 EXIT_CODE=1 原因 → 如果是 OOM/偶发错误，从 checkpoint-10000 resume；如果是代码 bug，修复后重启
- acib_v5_div_reg_eval_ckpt10000 完成 → 记录 4 suite SR → 与 baseline 对比 → 这是 v5 unconditioned scorer 的唯一完整 eval 数据点
- acib_v5_div_reg_seed2 完成 → eval checkpoint-10000 和 final → 与 seed1 一致性检验
- acib_v6_conditioned Worker 代码改完 → 提交训练（cuda:0，等 baseline_plus eval 完成释放 GPU）
- mvp1_baseline_plus_remaining 完成 → 记录 libero_10 SR → 至此 smolvla_libero_plus 4 suite baseline 完整
- mvp1_baseline_std_libero10 完成 → 记录 libero_10 SR → 至此 smolvla_libero 4 suite baseline 完整
- 两个 baseline 全部完成 + v5/v6 eval 完成 → MVP pass/fail 判定

### 5. 🎯 战略上下文
**核心发现链**：v1-v4 全部 scorer collapse → v5_div_reg 首次成功（diversity reg 是关键）→ 但发现 scorer 未真正 conditioned on language（bug D030）→ v5 实际是 unconditional position prior → v6 修复 conditioning 是真正的 "action-conditioned" 验证。

**最易判断错的事**：
- v5 结果不能作为 "ACIB works" 的最终证据——scorer 没有真正 conditioned on task。v5 保留作 ablation baseline（"what if scorer is task-agnostic"）。
- v6_conditioned 才是验证核心 hypothesis 的实验。如果 v6 与 v5 结果相似，说明 conditioning 不重要（narrative 需调整）；如果 v6 显著更好，confirms the story。
- 不要把 baseline_plus（data-aug trained model）和 baseline_std 直接加减——它们是不同 checkpoint，ACIB 的 claim 是"互补性"而非替代。

**决策链关键节点**：D006（framing: 互补性而非替代）、D022（MVP 标准重定义）、D028（维持 framing 不升级）、D030/D031（scorer conditioning bug 确认）。


---
