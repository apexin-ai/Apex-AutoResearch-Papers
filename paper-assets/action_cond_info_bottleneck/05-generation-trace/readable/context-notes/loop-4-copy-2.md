# agent / loop_4.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`52b5446b5ece57f3c03d.json`](../../sessions/52/52b5446b5ece57f3c03d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-16T13:44:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-13953 上只能用 cuda:0 和 cuda:1，绝对不能用其他设备号
- smolvla_libero_plus 是 mandatory baseline（D022），不能跳过
- scorer conditioning bug 已确认（D030/D031）：v5 系列 scorer 用 visual_mean 而非 language embedding，v5 结果只能作为 "without proper conditioning" ablation baseline，不能作为主实验
- libero_10 eval 的 cron 监控有结构性问题：eval 脚本按 suite 启动独立子进程，父 PID 退出会触发 cron 误报。已发生 3+ 次。下次提交 eval 必须确保 cron 监控的是实际 eval 子进程 PID，不是 wrapper

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953，account=root，工作目录 /root/acib
- Python：/root/miniconda3/bin/python（conda base），激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：lerobot/smolvla_libero + lerobot/smolvla_libero_plus（HF hub 直接加载）
- 数据集：/root/autodl-tmp/libero_dataset（273K 样本）
- HF cache：/root/autodl-tmp/.hf_cache
- 输出目录：/root/acib/outputs/
- W&B：大部分实验 WANDB_MODE=disabled（auth 问题未解决）
- 活跃进程：mvp1_baseline_std_libero10 PID 733616 cuda:1（lerobot-eval libero_10 for std model）
- 活跃 cron：mvp1_baseline_std_libero10（刚 reconcile 确认 still running）

### 3. 📊 当前状态
**刚做完**：收到 mvp1_baseline_plus_remaining 失败回调，已派 Worker（worker_diagnose_mvp1_baseline_plus_remaining_20260516T094137）去 SSH 诊断实际状态。该 Worker 尚未返回。

**Registry 关键实验**：
- `mvp1_baseline_std_libero10` RUNNING cuda:1 — std model libero_10 eval，PID 733616
- `mvp1_baseline_plus_remaining` DONE(failed) — cron 误报可能性大，spatial/object/goal 三个 suite 已有结果（81.6%/88.8%/87.8%），libero_10 子进程 PID 675231 可能仍在跑或已完成
- `acib_v6_conditioned` DONE(failed) — session recovery 标记，实际上是修复 conditioning bug 的关键训练，需要重跑
- `acib_v5_div_reg` / `acib_v5_div_reg_seed2` DONE(failed) — EXIT_CODE=1，但已产出有价值的分析结论（scorer 是 position prior 不是 action-conditioned）
- `acib_v3_train` ANALYZING — IB loss collapse 已确认，killed，作为 baseline 参考

**等待中**：
- Worker 诊断回调（mvp1_baseline_plus_remaining 实际状态）
- mvp1_baseline_std_libero10 cron 完成回调

### 4. 📋 待办
- 诊断 Worker 回调到 → 如果 libero_10 plus eval 已完成：提取结果更新 registry，将 conclusion 改为 success；如果未完成/进程已死：在 cuda:0 上重跑 libero_10 eval for plus model
- mvp1_baseline_std_libero10 完成回调 → 提取 std libero_10 SR，汇总 4 suite baseline（spatial=66.0%, object=67.8%, goal=76.4%, libero_10=?）
- 两个 baseline 全部就绪 → 更新 baseline metrics 到 registry，汇报 Director
- cuda:0 空闲确认后 → 重跑 acib_v6_conditioned（修复了 conditioning bug 的版本，condition_source=language），这是当前最高优先级训练
- v6_conditioned 训练完成 → cross-task probe 验证 conditioning 生效（期望 cos < 0.95），然后 eval
- Director 未决策项：v5 negative 结果的 framing 调整提案尚未提交（v5 scorer=position prior 的发现需要更新 narrative）

### 5. 🎯 战略上下文
- **核心发现**：v5_div_reg 的 diversity regularizer 成功防止了 scorer collapse（scorer_std=0.44, bimodal 分布），但 cross-task probe（D029-D031）证明 scorer 学到的是 spatial position prior 而非 action-conditioned selection。根因：scorer 的 condition 输入是 visual_mean 而非 language embedding（实现 bug）
- **决策链**：v3 per-token KL collapse → v4 aggregate KL 无分化 → v5 diversity reg 防 collapse 但 conditioning 无效 → v6 修复 conditioning（condition_source=language）是当前关键实验
- **v6 是 make-or-break**：如果 language conditioning 后 scorer 仍然是 position prior → 方法可能有根本问题；如果 probe cos < 0.95 → 继续 eval pipeline
- **CoRL 2026 deadline**：abstract 5/26（10天），paper 5/29（13天）。MVP 验证仍未通过。时间极紧
- **易错点**：
  - 不要把 v5 的 eval 数字当作 ACIB 有效的证据——v5 scorer 没有真正 conditioning
  - eval 脚本（eval_acib.py）有 dtype mismatch bug（scorer fp32 vs base bf16），perturbed eval dryrun 已修复但 eval_acib.py 可能还没 patch
  - WANDB auth 一直有问题，多数实验用 WANDB_MODE=disabled，指标只能从 log/checkpoint 提取


---
