# agent / loop_2.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`2756f8752527680f670a.json`](../../sessions/27/2756f8752527680f670a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-16T02:47:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 westb-13953 的 cuda:0 和 cuda:1，不可用其他设备
- acib_v5_stopgrad_entropy 已确认 negative（p→0 trivial collapse），不要重试 stop-grad 路线——task gradient 不可省略是已验证结论
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- mvp1_baseline_std_remaining 标记 failed 但实际是 cron 误报（eval 子进程模式），libero_goal 和 libero_10 数据可能不完整，需 SSH 验证 eval_info.json 是否存在再定结论
- CoRL 2026 deadline：abstract 5/26（10天），paper 5/29（13天），时间极紧

### 2. 🖥️ 基础设施快照
- **服务器**: westb-13953，2× RTX PRO 6000 Blackwell 96GB
- **工作目录**: /root/acib
- **Python**: /root/miniconda3/bin/python（conda base 环境，非 venv）
- **数据集**: /root/autodl-tmp/libero_dataset（273K frames，LIBERO 全套）
- **模型**: lerobot/smolvla_libero + lerobot/smolvla_libero_plus（HF cache）
- **输出目录**: /root/acib/outputs/（各实验子目录）
- **活跃进程**:
  - acib_v5_div_reg: PID 682233, tmux session, cuda:0, 22.8GB/96GB, ~0.8 steps/s，预计 ~08:00 UTC 完成
  - mvp1_baseline_plus_remaining: 子进程 PID 675231, cuda:0, 跑 libero_10 eval（父 PID 471056 已退出）
  - acib_v5_stopgrad_entropy: PID 694348, cuda:1——已确认 negative，应 kill 释放 GPU
- **活跃 Worker**: worker_code_prepare-v5-eval（正在准备 v5 eval 脚本）
- **Cron**: reconcile 返回 0 个活跃 cron（可能已清理）

### 3. 📊 当前状态
**刚做完**: v5 双路对比实验的 step 500 checkpoint 分析。v5_div_reg 首次成功压制 scorer collapse（scorer_std=0.379，远超 0.05 阈值），v5_stopgrad_entropy 失败（p→0 collapse）。已向 Director 汇报（D020/D021）。已派 Worker 准备 v5 eval 代码。

**Registry 活跃实验**:
| exp_id | status | 摘要 |
|--------|--------|------|
| acib_v5_div_reg | RUNNING | ✅ 突破性进展，scorer_std=0.42 稳定，预计 08:00 UTC 完成 20K steps |
| acib_v5_stopgrad_entropy | PREPARING | ❌ negative，待 kill |
| mvp1_baseline_plus_remaining | RUNNING | libero_10 eval 进行中（spatial=81.6%, object=88.8%, goal=87.8% 已完成）|
| acib_v3_train | ANALYZING | killed，作为 per-token KL 失败的 baseline 记录 |

**等待中**:
- Worker `worker_code_prepare-v5-eval` 回调（准备 eval 脚本）
- v5_div_reg 训练完成 cron 回调（~08:00 UTC）
- baseline_plus_remaining libero_10 完成
- mvp1_baseline_std_remaining 的 goal/libero_10 数据需要 SSH 验证（cron 误报 failed）

### 4. 📋 待办（条件触发式）
- **v5_stopgrad_entropy 未 kill** → 立即 spawn Worker kill PID 694348 释放 cuda:1，update_registry status=DONE conclusion=negative
- **Worker prepare-v5-eval 回调到达** → 检查 eval 脚本就绪，等 v5_div_reg 训练完成后立即提交 eval
- **v5_div_reg 训练完成（cron 回调）** → spawn Worker 在 cuda:0+cuda:1 并行跑 4 suite eval（libero_spatial/object/goal/10），对比 baseline 判断 MVP pass/fail
- **baseline_plus_remaining libero_10 完成** → 汇总 4 suite baseline_plus 完整结果，update_registry
- **baseline_std_remaining 数据验证** → SSH 检查 /root/acib/outputs/baseline_std_v3/ 下 libero_goal/libero_10 的 eval_info.json 是否存在；若缺失需重跑
- **MVP pass（v5_div_reg eval ≥2/4 维度 ≥5pp 提升）** → 启动 ACIB-H@k=0.8 训练 + smolvla_libero_plus 上叠加 ACIB-S（互补性验证）
- **MVP fail** → 产出 Framing 调整提案，不默默跑下一个

### 5. 🎯 战略上下文
**核心发现链**: v1(β太高) → v3(per-token KL 退化) → v4(aggregate KL 无分化激励) → v5_stopgrad(task gradient 不可省) → **v5_div_reg(✅ diversity reg 成功)**。五代迭代确认：(1) task gradient 必须保留 (2) diversity reg (-λ*std) 是有效 anti-collapse 机制 (3) β warmup + diversity reg 共存可行。

**论文 story**: ACIB 是 data-aug 的互补正则化器（不是替代品）。关键实验是 ACIB-S on top of smolvla_libero_plus（互补性验证）。

**最容易判断错的事**:
- baseline_std_remaining 的 "failed" 是 cron 误报历史（eval 子进程模式），不要直接信 failure_reason，SSH 看实际文件
- cuda:0 上同时有 v5_div_reg 和 baseline_plus_remaining 两个进程，注意 GPU 内存竞争（v5_div_reg 用 22.8GB，baseline eval 用 ~6GB，96GB 卡够用）
- v5_div_reg 的 WANDB_MODE=disabled，指标只在 stdout log 里，分析时要 tail log 而非查 W&B
- acib_deploy_westb13953 和 acib_v3_train 是历史实验（killed/queued），不需要处理


---
