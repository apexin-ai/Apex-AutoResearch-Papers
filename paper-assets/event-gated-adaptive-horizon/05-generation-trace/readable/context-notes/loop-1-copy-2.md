# agent / loop_1.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`e10d1569b0568b9560af.json`](../../sessions/e1/e10d1569b0568b9560af.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-13T18:30:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单必须查 `load_project_config` 的 `execution.gpu_ids`，当前分配 2 张（bjb1-45299 上），禁止用白名单外 GPU
- `--compile False` 必须传——PyTorch 2.10 的 torch.compile 有断言错误
- `LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6` 必须设——否则 GLIBCXX 缺失
- `CUDA_VISIBLE_DEVICES` 隔离必须用——exp_002 因未设导致 CUDA context 泄漏（D005 教训）
- Imagination dt 必须 clamp 到 effective_max_dt + logits masking——否则 train/imagine distribution mismatch 导致 return 崩塌（exp_002/exp_003 两次踩坑）
- 服务器名已从 `autodl-rtx6000` 变为 `bjb1-45299`——SSH config 和所有提交命令必须用新名

### 2. 🖥️ 基础设施快照
- 服务器：**bjb1-45299**（原 autodl-rtx6000），2× RTX PRO 6000 (96GB each)，Driver 595.58, CUDA 12.8
- 工作目录：`/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：conda base `/root/miniconda3/bin/python`，PyTorch 2.10.0+cu128
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa`
- pip 前需 `source /etc/network_turbo`
- 数据盘 250GB 可用
- 活跃进程/tmux：**未知**——Worker `worker_diagnose_exp_004_and_exp_001_20260513T152538` 正在 SSH 诊断中，尚未返回结果
- Cron：reconcile 返回 0 条活跃（所有 cron 已因 SSH 失联清理）

### 3. 📊 当前状态
**刚做完**：session-start 初始化（read_registry + reconcile_crons + 读 report/ROADMAP/memory）。收到 exp_004 失败回调后分析出根因是 AutoDL 实例名变更（autodl-rtx6000 → bjb1-45299），已派诊断 Worker。

**Registry 状态**（4 个实验全部 DONE）：
- `exp_001_baseline` [failed] — step 245K, eval_return ~920, baseline 已收敛。因 SSH 名变更被标 failed
- `exp_002_event_gated` [failed] — Phase 1 subsample 缺陷，已 kill
- `exp_003_event_gated_v2` [negative] — dt 无约束 + λ-return 索引错位，return 崩至 13%
- `exp_004_event_gated_v3` [failed] — 修复两个 bug 后重跑，step 20K 时 SSH 失联。gate_scale=0（仍在 Phase 1），fps=8.1，5.19 GPU·h

**等待中**：
- Worker `worker_diagnose_exp_004_and_exp_001_20260513T152538` 回调——SSH 到 bjb1-45299 检查进程是否仍在运行
- 尚未向 Director 汇报（等诊断结果后一并汇报）

### 4. 📋 待办
- 诊断 Worker 回调 → 根据结果分叉：
  - 进程仍在运行 → 更新 registry server 字段为 bjb1-45299，重新注册 cron 监控，向 Director 汇报"实验恢复"
  - 进程已结束（正常完成）→ 拉 metrics，更新 registry 为 success/negative，按 on-experiment-done 流程走
  - 进程已崩溃 → 读日志定位根因，更新 registry failure_reason，向 Director 汇报并建议重跑
- exp_001 baseline 若已完成 500K steps → 记录最终 metrics 作为 baseline 锚点
- exp_004 若需重跑 → 用新服务器名 bjb1-45299 + submit_training_job 提交，注意 GPU 编号从 0 开始
- 两个实验恢复/重跑后 → 重点监控 exp_004 的 step 50K-70K（Phase 2 gate 激活后 return 是否稳定，这是 MVP criterion 1 的关键验证窗口）

### 5. 🎯 战略上下文
- **项目阶段**：MVP 验证第 4 轮。核心假设是 event-gated variable-rate RSSM 能产生有意义的时间抽象且不破坏训练稳定性
- **MVP 4 个标准**：criterion 2/3/4 已在 exp_003 中 PASS（gate entropy、H_eff、dt autocorr）。**唯一未验证的是 criterion 1（return ≥ 80% baseline）**——exp_002/exp_003 两次因 bug 导致 return 崩塌，exp_004 是修复后的第一次完整验证
- **决策链**：D001(MVP 方案) → D002(量化标准) → D003(subsample curriculum) → D004(中期评估 3/4 PASS) → D005(imagination dt 无约束根因) → D006(λ-return dt 索引错位) → D007(停 Walker Walk baseline 启 Cheetah Run baseline——但 Cheetah 未见启动)
- **易踩的坑**：
  - exp_004 的 logdir 叫 `event_gated_v4_s1`（不是 v3），因为 v3 是代码版本号，v4 是 logdir 版本号
  - exp_001 baseline 的 ROADMAP 写着 step ~216K 但 registry 已到 245K（ROADMAP 未更新）
  - GPU 预算原 15h 已超，当前 ~18h consumed，Director 未正式确认新上限 30h
  - `autodl-rtx6000` 这个名字在 registry spec、ROADMAP、memory.md 中多处引用——恢复后需全面更新为 bjb1-45299


---
