---
loop: 6
reason: max_messages
updated: '2026-05-18T01:05:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-13953 的 cuda:0 和 cuda:1，严禁使用其他设备
- Eval 结果只在日志出现 suite 级 `pc_success` 汇总后才报告给用户——之前多次把 per-task 数据误报为 suite 级结论（M001）
- paper_framing.md 已修订但仍含 PENDING claims——v7.3 结果出来前不可启动正式论文写作
- Registry 中 v7.2 eval 的 `libero_spatial_sr: 0.76` 是历史误标（实际 59.4%/61.0%），不可引用
- LIBERO eval 时 GPU utilization 报 0% 是正常的（CPU 密集型仿真，M003）——判断进程存活用 PID + 日志时间戳，不要信 nvidia-smi utilization
- 训练提交后必须 2min 内验证进程存活（M004：v7.3 首次提交因 SyntaxError 崩溃，GPU 空转 8h 未被发现）
- Goal suite +2.2pp 不显著（p=0.20），不可作为 claim（D052）

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953 (connect.westb.seetacloud.com)，用户 root
- 代码目录：`/root/acib/`（train_acib.py, acib_policy.py, config.py, eval_acib.py, cross_task_probe.py）
- Checkpoints：`/root/autodl-tmp/` 下各版本目录
  - v7.2: `acib_v7.2_connector_scorer/checkpoint-20000` (seed1/seed2)
  - v7.3 LoRA: `acib_v73_connector_lora/`（训练中）
  - connector-only: `acib_v73_connector_only_ablation/`（训练完成，eval 在跑）
  - baseline: `lerobot/smolvla_libero`（HF cache）
- 活跃进程：
  - PID 745668: v7.3 LoRA 训练 cuda:0（step ~13600/20000, ~1h 剩余, 预计 ~10:10 UTC）
  - PID 759162: connector-only eval α=0.0 cuda:1（刚启动，~8h）
- 无 W&B，无 conda env（直接系统 Python），磁盘 5% 用（396GB 可用）

### 3. 📊 当前状态
v7.2 4-suite eval **完成，MVP FAIL**（D053）：α=0.0 avg=61.25%(-4.85pp), α=1.0 avg=62.40%(-3.7pp)。Scorer 信号一致正向(+1.15pp avg)，与任务难度正相关(libero_10 +3.0pp)。

v7.3 LoRA 训练中（cuda:0, ~1h 剩余）。Connector-only ablation 训练已完成（Probe A cos≈1.0，确认 contrastive loss 是 spatial conditioning 的必要条件），其 eval 刚启动在 cuda:1。

Registry RUNNING：acib_v73_connector_lora（训练）, acib_v73_connector_only_ablation（eval）。Cron 监控两个实验。

### 4. 📋 待办
- v7.3 LoRA 训练完成（~10:10 UTC）→ Probe A（cos<0.8?）→ α=0.0 spatial sanity（must=baseline 66.0%±1pp）→ α=1.0 full 4-suite eval
- v7.3 Probe A PASS + α=0.0=baseline + α=1.0≥64.1% → **MVP PASS** → 全面修订 paper_framing.md PENDING claims → 启动 Paper Agent（Direction C）
- v7.3 α=1.0 结果出来后按 D052 分支：≥baseline+1pp→method 为主；±1pp→analysis 为主；<baseline-2pp→纯 analysis paper
- connector-only eval 完成（~8h）→ 收集 4-suite 数据 → 填 ablation table（13.7% drift vs v7.2 的 0.4% drift 性能对比）
- v7.3 也 FAIL → contingency：α sweep(0.1/0.3/0.5)、additive modulation、LoRA rank 16/32

### 5. 🎯 战略上下文
**项目核心发现链**：v7 joint training 梯度污染(-7.8pp, D038) → v7.1 scorer-only 仅 global bias(D041) → v7.2 connector+scorer spatial conditioning 成功但 connector 敏感(0.4% drift→-4.85pp avg, D046/D048/D053) → connector-only ablation 确认 contrastive loss 是 spatial conditioning 必要条件(cos≈1.0) → v7.3 LoRA 结构性隔离(D049，训练中)

**论文方向：Direction C Hybrid（D052）**——Method arm (LoRA exact baseline) + Analysis arm (three constraint discovery)。v7.3 结果决定两条腿的权重。统计纪律：只 claim p<0.05 的结果，goal +2.2pp(p=0.20) 不可做 claim。正文呈现 3 个核心 constraint (v7/v7.1/v7.2)，v1-v6 放 Appendix（D050）。

**最易判断错的事**：
1. GPU utilization 0% ≠ 进程崩溃（LIBERO eval 是 CPU 密集型）——检查 PID 存活
2. 训练 submit 成功 ≠ 训练在跑——必须 2min 内验证日志有输出
3. v7.2 scorer 增量 +1.15pp 不能直接预测 v7.3——v7.2 是在 drift-damaged baseline 上测的，混杂了交互效应
4. CoRL abstract DDL 5/26（8天），paper DDL 5/29（11天）。v7.3 如果一次通过，时间可行但已因 M004 延迟 8h
5. 10 negatives 不是问题——它们是 constraint discovery story 的核心素材，但不要在 Introduction 提"10 experiments"
