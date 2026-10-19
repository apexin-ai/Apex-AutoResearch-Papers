# reviewer / loop_2.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`d5bd4198e277d2fa3520.json`](../../sessions/d5/d5bd4198e277d2fa3520.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-16T01:15:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目 GPU 白名单未在 constraints.yaml 中定义（文件未创建），但实际使用模式：eval 在 cuda:0/cuda:1，训练在 cuda:0 或 cuda:1。当前 v4 训练在 cuda:0，两个 eval 分别在 cuda:0 和 cuda:1
- `ps -o etime` 格式：`MM:SS` 是分秒，`HH:MM:SS` 是时分秒。**我曾把 `03:48`（3分48秒）误读为 3小时48分，导致错误 CRITICAL 报告。** 下一个"你"务必注意这个格式
- cron 监控基于 PID 存活检测。`run_remaining_suites_eval.sh` 按 suite 启动独立子进程，父 PID 退出后 cron 会误报 failed——**收到 cron:on_failed 先核实子进程再判断**，已发生 3 次
- 日志文件可能存在 inode 不一致（tmux 重建 log 导致 `/proc/PID/fd/` 指向旧 inode，磁盘文件是新 inode）。**优先从 `/proc/PID/fd/2` 读取实际输出**

### 2. 🖥️ 基础设施快照
- 服务器：`westb-13953(root)`，代码根：`/root/acib`
- Python：`/root/miniconda3/bin/python`，conda base 环境
- 数据集：`/root/autodl-tmp/libero_dataset`（LeRobot 格式，273465 frames）
- HF cache：`/root/autodl-tmp/.hf_cache`，`HF_HUB_OFFLINE=1`
- 模型：`lerobot/smolvla_libero`（std）、`lerobot/smolvla_libero_plus`（plus/mix-SFT）
- wandb：已配置 API key，project=`acib_mvp`
- 活跃进程（截至 handoff）：
  - PID 471056：baseline_plus eval，cuda:0，libero_goal 进行中
  - PID 508625：baseline_std eval，cuda:1，libero_goal 进行中
  - PID 649789：**acib_v4_agg_kl 训练**，cuda:0，step ~600/20000，tmux 启动

### 3. 📊 当前状态
刚完成 v4 训练早期监控。v4 已启动（修复 wandb 后重启），但 scorer_std 在 β=0 warmup 期间就从 0.135 快速降至 0.012——这是 task loss 自身造成的，不是 IB loss bug。已向 Director 报告 WARNING，建议观察到 step 1000+ β 升温效果。

Registry RUNNING 实验：
- `mvp1_baseline_plus_remaining`：spatial 81.6%, object 88.8% 完成，goal 进行中
- `mvp1_baseline_std_remaining`：spatial 66.0%, object 67.8% 完成，goal 进行中
- `acib_v4_agg_kl`：**registry 仍为 DONE/failed（旧 wandb 失败记录），需更新为 RUNNING, PID=649789**

### 4. 📋 待办
- v4 训练到 step 1000 → β 开始升温，**关键观察窗口**：IB loss 是否保持正值、scorer_std 是否回升（>0.05 成功，<0.01 需干预）
- v4 step 2000 时 scorer_std < 0.01 → 报 CRITICAL，建议加 diversity regularizer 或 stop-gradient
- baseline_plus/std 完成 libero_goal → 检查 eval_info.json，计算 SR，更新对照表
- baseline_plus/std 完成 libero_10（最后一个 suite） → 汇总全部 4 suite 结果给 Director
- cron:on_failed 再次触发 → 先核实子进程再判断（大概率又是 PID 变更误报）
- 新 worker_done 通知 → 审查时优先检查 registry 是否同步更新

### 5. 🎯 战略上下文
- **ACIB 核心问题已暴露**：scorer collapse 不只是 IB loss 设计 bug（v3 per-token KL），更深层是 task loss 本身不提供 token 分化信号。v4 aggregate KL 修复了 v3 的退化最小值，但可能不够——需要额外机制（diversity reg / stop-grad / temperature）
- **三代训练失败链**：v1（β=0.1 太强→即时 collapse）→ v3（β=0.01+warmup→per-token KL 退化解）→ v4（aggregate KL→task loss 自身推向均匀，待验证）
- Baseline 进度正常：plus 显著优于 std（spatial +15.6pp, object +21pp），符合 mix-SFT 增强预期
- 目标 CoRL 2026（abstract 5/26, paper 5/29），距 abstract DDL 10 天
- **最易判断错的事**：(1) etime 格式——MM:SS vs HH:MM:SS；(2) cron failed 不等于实验真失败——先查子进程；(3) scorer_std 下降不一定是 IB loss 的问题——β=0 时 IB 无梯度贡献，collapse 来自 task loss


---
