# reviewer / loop_17.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_17.md`
- **Structured JSON:** [`ccd0254c7fc70f8044d1.json`](../../sessions/cc/ccd0254c7fc70f8044d1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_wall_time
updated: '2026-05-21T20:42:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单（C006）：bjb1 cuda:0,1；westd cuda:0,1,2,3。越界即 critical。
- exp029_seed4_v2 registry conclusion="success" 与 D113 "collapsed" 矛盾，**已报告 3 次未修正**。审查任何引用 Seed 4 结论的内容时必须按 D113 "collapsed" 处理。
- W&B entity 带尾部连字符：`xiaoyucorynne-`（不是 `xiaoyucorynne`）。
- registry filter `{"exp_id": "xxx"}` 经常返回空，改用 `{"status": "RUNNING"}` 等状态过滤。
- ssh_read_only 不支持 `-o`（find 的 OR）和 `>`、`|` 等 shell 元字符。用多次单独命令代替。

### 2. 🖥️ 基础设施快照
- **bjb1-17606** (root): 代码 `/root/cost-verify-agent-rl/RAGEN`，数据盘 `/root/autodl-tmp/`（38% used, 157 GB free），conda base `/root/miniconda3/bin/python`
- **westd-47453** (root): 代码 `/root/autodl-tmp/cost-verify-agent-rl/RAGEN`，数据盘同路径
- 模型 checkpoint: `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4`（两台都有）
- W&B: entity=`xiaoyucorynne-`, project=`cost-verify-agent-rl`
- 活跃进程（截至 handoff 时刻）：
  - **exp029_seed8**: westd cuda:2,3, PID 462991, W&B c0l6e7vd, step 9/15, **已确认崩溃**
  - **exp029_seed7_high_kl**: bjb1 cuda:0,1, PID 334159 (第3次提交), step 0-1/7, 刚重启
  - **exp029_seed7_len_penalty**: westd, **已完成** EXIT_CODE=0, GPU 0,1 空闲待分配

### 3. 📊 当前状态
本轮（第 6 个 context window）我做了：
1. 独立验证两个新 mitigation 实验（len_penalty + high_kl）的配置、代码实现、GPU 合规
2. 发现并报告 bjb1 磁盘 97% 满 → 清理 worker 释放 153 GB → 但误杀新 session → 第3次重启 high_kl
3. 独立验证 Seed 8 step 1-9 指标，确认其正在崩溃（response inflation 模式），报告崩溃率从 43% 升至 57%
4. 确认 len_penalty 完成但假设未满足（success=28.1% < 30%, resp_len=7598 >> 2000）
5. 3 次提醒 Seed 4 conclusion 矛盾未被修正

**等待中**：
- high_kl 训练进行中（bjb1），预计 ~5h 完成 7 步
- Seed 8 继续运行至 step 15（~3.5h），收集完整崩溃曲线
- Director 尚未回应 Seed 4 结论修正和 westd GPU 0,1 重分配

### 4. 📋 待办（条件触发式）
- **high_kl step 1 指标出来** → 核查 kl_loss 是否显著高于 baseline 的 0.003（应 ~10x），验证 kl_loss_coef=0.1 生效
- **high_kl step 7 完成** → 判定：resp_len < 2000 且 success > 30% = 有效；否则 KL 正则化不足以阻止崩溃
- **Seed 8 step 10/15 指标** → 确认 val step 10 是否也崩溃（val 可能好于 train 因 temp=0.4）
- **Seed 8 完成** → 最终核实 W&B 与 registry 一致，更新崩溃率统计（当前 4/7=57%）
- **westd GPU 0,1 空闲** → 提醒 Director 分配新实验（如果 ROADMAP 还有待跑的）
- **任何实验完成后** → 检查 registry status 是否更新（len_penalty 目前仍 RUNNING，应为 DONE）

### 5. 🎯 战略上下文
- **核心结论**：Episode-level GRPO 不能防止崩溃，但能让部分 seed 学习（step-level 全军覆没）。崩溃机制是 response inflation（非 entropy→0 的经典模式），根因是 kl_loss_coef=0.01 + entropy_coeff=0.001 正则化太弱。
- **D113 决策**（2026-05-21）：论文 claim 从 "avoids collapse" 调整为 "enables learning where step-level cannot" + response_length 双峰分析作为新贡献。
- **崩溃率**：D113 估 43-50%，实际已升至 57%（4/7: seeds 2,4,7,8）。存活 seeds: 1(42), 3(789), 5(456), 6(789v3)。
- **两个 mitigation 实验正在测试**：len_penalty（已完成，部分有效），high_kl（进行中）。如果 high_kl 也失败，说明仅靠 config 调参无法解决，需要架构/算法层面修改。
- **最容易判断错的事**：
  1. bjb1 上的 ray::WorkerDict 进程不一定是孤儿——先查 PPID 对应的 raylet 是否属于当前实验，我本轮就犯过这个错误
  2. W&B summary metrics 有延迟，`_step` 可能落后于实际训练 step 1-2 步
  3. `train/response_length` 和 `response_length/mean` 是两个不同指标（前者是环境报告的 episode 长度，后者是 tensor padding 后的长度），不要混淆
  4. RAGEN 的 GPU util 在 rollout 阶段和 backward 阶段交替 0%/100%，不要在 rollout 的 CPU 环节误判为 GPU 空转


---
