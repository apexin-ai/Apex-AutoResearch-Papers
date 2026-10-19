# reviewer / loop_7.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`000f4598f93b3816cf11.json`](../../sessions/00/000f4598f93b3816cf11.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-14T14:57:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- Qwen 训练只能用 cuda:0，StarCoder 只能用 cuda:1。项目 gpu_ids=[0,1]，越界即 CRITICAL
- m2_full 训练脚本已被修复重启过一次（bash 参数缓存事件）：旧 bash PID 73554/74132 已 kill，新脚本从 s43 开始。**不要再次 kill 或重启当前训练进程链**
- TRAIN_SCRIPT 路径有两个版本：Qwen 用 `/root/structfuse-context/training/train.py`，StarCoder 用 `/root/structfuse/training/train.py`。不要混淆
- Discussion draft 有两个已知错误待修：(1) "9 seeds" 应为 "3 seeds"，(2) m1_reextract_v2 被写为 "planned" 实际是 RUNNING

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106(root)，2× RTX PRO 6000 Blackwell 96GB
- 工作目录：远程 `/root/structfuse`（代码）、`/root/autodl-tmp/structfuse`（数据/checkpoints）
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：Qwen `/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B`；StarCoder `/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b`
- wandb：offline 模式，日志 `/root/autodl-tmp/structfuse/wandb_logs/`
- 磁盘：/root/autodl-tmp 163G/250G (66%)
- 活跃进程：
  - Qwen s43 训练：PID 337271 (cuda:0)，bash 驱动 PID 337267，轮询父进程 PID 300284
  - StarCoder s42 训练：PID 76627 (cuda:1)，轮询等待进程 PID 309679 → 完成后启动 `run_m2_full_starcoder_s43plus.sh`
  - m1_reextract_v2：CodeQL 重提取（CPU），4 workers 并行，~15/82 groups done（截至 07:06 CST）
- Qwen s43 日志有双层 tee pipe buffering（`python | tee log` 内层 + `bash script | tee all.log` 外层），短期内日志文件看不到输出是正常的，不是 crash

### 3. 📊 当前状态
刚完成：
- 发现并报告 bash 脚本参数缓存问题（D026/D027 修改不生效）→ Worker 修复后我做了完整独立验证，4 项全部 PASS
- 审查 Qwen random_s42 最终结果：best R@1=0.553 @ step 1000，3 epochs 过拟合确认
- 纠正 worker_analysis_m2_full_qwen 对 s43 的误诊（"OOM/crash"实际是 pipe buffering）

Registry RUNNING：
- m2_full_qwen (ANALYZING)：s42 done，s43 刚启动（~19:24 CST），剩余 8 runs（3 strategies × 2 seeds + random_s44）
- m2_full_starcoder (RUNNING)：s42 at step 3000/4242 (~71%)，s43+ 脚本已就绪等待
- m1_reextract_v2 (RUNNING)：CodeQL 重提取，预计还需 ~10h+

### 4. 📋 待办（条件触发式）
- Qwen s43 eval@500 出现 → 验证 early stopping 逻辑是否激活（日志应显示 patience 计数器），确认 R@1 与 s42 同量级
- StarCoder s42 完成（~4242 steps）→ 验证 final eval metrics，确认 s43 以正确参数自动启动（PID 309679 轮询 → run_m2_full_starcoder_s43plus.sh）
- StarCoder eval@3500/4000 出现 → 关注 R@1/val_loss 分离趋势是否加剧（eval@2500 已出现 R@1 新高但 val_loss 恶化）
- m1_reextract_v2 完成 → 验证新增数据量（目标从 15,897→~44,173），检查数据质量
- 新 worker 完成通知 → 常规审查
- Discussion draft 修订版提交 → 核查 "9 seeds" 和 m1_reextract_v2 状态描述是否已修正

### 5. 🎯 战略上下文
- **3 Core Claims**：(1) embedding mining > random（最强，pilot+s42 一致），(2) dataflow conditional benefit mediated by encoder saturation（最弱，n=2 encoder "interaction effect"，建议降级为 observation），(3) CodeQL bounded data-flow scalable（有数据支撑）
- **关键决策链**：D017→D018→D019（go/no-go 框架）→ D024（framing 重写）→ D026（2 epochs）→ D027（early stopping）
- **Deadline**：EMNLP 2026 ARR May 25（11 天），timeline 紧但可行：M2 ~May 18-19 完成，plan_003(SWE-bench)+plan_004+plan_014 并行，写作 May 22-25
- **易错点**：
  - Worker 分析 s43 日志为空就判 crash——双层 tee pipe 会 buffer，进程活着+GPU 满载就是正常的
  - plan_017 文献对比中 StructFuse 用的是 "bounded inter-procedural data-flow analysis (2-hop call-graph scope)"，**不是** "taint tracking"——已修正过一次，别退回去
  - on_complete:m2_full_qwen 是旧 tmux exit 触发的假完成信号，全 9 runs 完成还早
  - StarCoder 的 R@1 和 val_loss 在 eval@2500 开始分离（R@1 新高但 val_loss 恶化），需要关注 dual checkpoint 策略是否正确捕获了最优模型
  - GPU budget 已严重超支（plan_002 预算 30h，实际 ~260h），但 deadline 可行性取决于 M2 何时完成，不要用 GPU-hours 超支来判 deadline 风险


---
