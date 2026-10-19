# agent / loop_5.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`d474bd54303b10a5a597.json`](../../sessions/d4/d474bd54303b10a5a597.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-16T19:49:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-13953 的 cuda:0 和 cuda:1（`get_project_resource_usage` 白名单）
- 根分区只有 ~30GB，所有 outputs/checkpoints 必须写 `/root/autodl-tmp/` 或通过 symlink（v7 已因根分区满崩溃过一次）
- v7 训练命令必须指定 `--output_dir /root/acib/outputs/acib_v7_contrastive`（这是 symlink 到数据盘）
- conda 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- 训练脚本 GPU 参数始终 `--gpu 0`（框架通过 CUDA_VISIBLE_DEVICES 映射物理卡）

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953，2× NVIDIA RTX PRO 6000 Blackwell 96GB
- 工作目录：`/root/acib/`
- Python：`/root/miniconda3/bin/python3`（conda base 环境）
- 模型：`lerobot/smolvla_libero`（HF hub，已缓存）
- 数据集：`/root/autodl-tmp/libero_dataset`（273465 samples）
- HF cache：`/root/autodl-tmp/.hf_cache`
- W&B：项目 `acib_mvp`，部分实验 WANDB_MODE=disabled
- Outputs：`/root/acib/outputs/`（symlink 到 `/root/autodl-tmp/`）
- 活跃进程：**未确认**——诊断 Worker 正在查（见第 3 节）

### 3. 📊 当前状态
收到 CRON 回调：`acib_v7_contrastive` EXIT_CODE=129 (SIGHUP) 失败。已派 Worker `worker_diagnose_acib_v7_contrastive_fail_20260516T134642` 去服务器诊断（查日志尾、磁盘、GPU、checkpoint、seed2 进程状态）。**Worker 尚未回调。**

Registry 关键状态：
- `acib_v7_contrastive`: DONE/failed — 最有价值实验，step 5000 时 Probe A cos [0.476, 0.894]，训练从 step 0 重启后在某个 step 被 SIGHUP kill
- `acib_v7_seed2`: PREPARING — 有 PID 27422，是否存活待诊断 Worker 确认
- `acib_v8_film`: PREPARING/暂缓 — 500 步 sweep Probe A cos≈1.0 无效，v7 contrastive 更优先
- 两张 GPU 均空闲，零 Worker 在跑 ⚠️

### 4. 📋 待办
- 诊断 Worker 回调到达 → 根据根因决定：
  - 若磁盘满再次 → 清理空间 + 从最新 checkpoint resume（`--resume_from`）
  - 若外部 kill/SSH 断连 → 直接从 checkpoint resume 重启
  - 若 OOM → 降 batch_size 或 gradient accumulation
- v7 恢复后 → 确认 v7_seed2 状态，若 dead 也重启（cuda:1）
- 两实验稳定 RUNNING 后 → 汇报 Director（附 [资源] 行）
- v7 完成 20000 步 → 跑 4-suite eval（libero_spatial/object/goal/libero_10，50 eps/task）
- eval 完成 → 与 baseline 对比（std: avg=66.1%, plus: avg=81.4%）

### 5. 🎯 战略上下文
**核心突破**：v7 log-barrier contrastive loss 解决了 v5/v6 的 scorer collapse 和 conditioning 退化问题。Probe A cos 从 v5 的 1.0 / v6 的 0.9999 降到 v7 的 [0.476, 0.894]——scorer 终于依赖 language 了。

**决策链**：v3(IB collapse) → v4(agg-KL 无分化) → v5(div-reg 有效但 position-only) → v6(language conditioning 训练退化) → v7(contrastive 成功强制 language-dependence) → 当前目标: 完成 20k 步全训练 + eval

**CoRL 2026 deadline**：abstract 5/26（距今 10 天），paper 5/29（13 天）。时间极紧。

**易错点**：
- Cron EXIT_CODE=129 不一定是程序 bug，常见是 SSH 断连或 tmux 异常导致 SIGHUP
- v7 之前因根分区满崩溃过，重启时从 step 0 开始而非 resume——检查这次是否有 checkpoint 可 resume
- `acib_v7_seed2` 虽然 registry 显示 PREPARING，但有 PID 且走了 submit_training_job，可能实际在跑（registry 状态未正确推进到 RUNNING）
- v8_film 已确认在无 contrastive loss 情况下无效，不要再投入 GPU 时间


---
