---
loop: 7
reason: max_wall_time
updated: '2026-05-18T01:05:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westb-13953 的 cuda:0 和 cuda:1。`submit_training_job` 通过 CUDA_VISIBLE_DEVICES 隔离，命令里的 `--gpu 0` 指进程内可见设备（不是物理 GPU 号），spec 里的 `gpu: ["cuda:X"]` 才是物理 GPU。
- connector_only ablation 的 `--gpu 0` + spec `gpu: ["cuda:1"]` 不是 bug——CUDA_VISIBLE_DEVICES=1 后 `--gpu 0` 映射到物理 GPU 1。我之前误报过这个冲突，已澄清。
- `train_acib.py:177` 曾有 SyntaxError（`--lambda_drift` 缺闭合括号），已修复。如果 Worker 再改 argparse 区域，优先检查括号闭合。

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953(root)，代码根目录 /root/acib
- Python：/root/miniconda3/bin/python3（conda base env）
- 模型 checkpoint：/root/autodl-tmp/ 下各实验子目录
  - v7.2: /root/autodl-tmp/acib_v7.2_connector_scorer/checkpoint-20000
  - v7.3 LoRA: /root/autodl-tmp/acib_v73_connector_lora_seed42/ （训练中）
  - connector_only: /root/autodl-tmp/acib_connector_only_seed42/checkpoint-20000
  - baseline: lerobot/smolvla_libero (HF hub, cached in /root/autodl-tmp/.hf_cache)
- 数据集：/root/autodl-tmp/libero_dataset（273K frames）
- WANDB_MODE=disabled（全项目）
- 训练日志：~/runs/action_cond_info_bottleneck/
- Eval 输出：/root/autodl-tmp/v72_eval/（已完成）
- 活跃进程（截至 handoff）：PID 745668 = v7.3 LoRA 训练（GPU 0, step ~13800/20000, ~30min 完成）
- tmux sessions: v72_seed1（旧）+ 新 v7.3 的两个 session（pts/2=LoRA, pts/3=ablation已完成）

### 3. 📊 当前状态
- **v7.3 LoRA 训练** (RUNNING, PID 745668, GPU 0): step ~13800/20000, 1.8 steps/s, 预计 ~09:30 UTC 完成。训练健康——ctr loss 从 11.8 降到 1.2-1.8，scorer_std 从 0.15 升到 0.30+。
- **connector_only ablation** (DONE): Probe A cos=0.999991，证明 contrastive loss 是 spatial conditioning 必要条件 (C10 claim)。Weight drift 13.7%（v7.2 仅 0.4%）。未做 4-suite eval（GPU 1 空闲）。
- **v7.2 eval** (DONE): MVP FAIL。α=0.0 avg=61.25%(-4.85pp), α=1.0 avg=62.40%(-3.7pp)。数据已独立核实。
- **等待中**：v7.3 LoRA 完成的 cron 回调 → 将触发 Probe A + eval pipeline
- **GPU 1 空闲**：connector_only eval 未被 Agent 启动，可用于 v7.3 eval 或 connector_only 补充 eval

### 4. 📋 待办（条件触发式）
- **LoRA cron on_complete 回调** → 审查：(1) checkpoint 存在, (2) Probe A cos<0.8, (3) scorer_std, (4) registry 更新为 DONE
- **v7.3 Probe A 出结果** → 核实 cos 值是否 <0.8（至少 2/3 pairs），如 cos≈1.0 则 LoRA 未产生 spatial conditioning = CRITICAL
- **v7.3 α=0.0 eval 启动** → 审查 GPU 白名单合规，命令参数（scoring_alpha=0.0），必须验证 = baseline±1pp（这是 LoRA 结构性保证，实测不符 = 代码 bug）
- **v7.3 α=1.0 full 4-suite eval 出结果** → MVP 最终判定：avg≥64.1% = PASS，否则 FAIL。同时计算 Δ(α=1.0 - α=0.0) 判定 scenario（A/B/C）
- **Registry 仍显示 connector_only 为 DONE 但无 eval metrics** → 如果 Director 决定补跑 connector_only 4-suite eval，审查 GPU 分配和结果

### 5. 🎯 战略上下文
- **论文方向 Direction C (Hybrid)**：Method (LoRA exact baseline) + Constraint Discovery Analysis。三个 constraints: (1) gradient isolation, (2) connector participation, (3) weight preservation。
- **决策链**：D049 采纳 LoRA → D051 suite-dependent drift → D052 Direction C → D053 v7.2 MVP FAIL
- **v7.2 4-suite 完整数据**（已验证）：spatial 59.4%/61.0%, object 65.6%/66.2%, goal 78.6%/78.0%, libero_10 41.4%/44.4%（α=0.0/α=1.0）。Baseline avg=66.1%。
- **统计显著性**：仅 spatial(-6.6pp, p≈0.015) 和 libero_10(-12.8pp) 的回退是显著的。Goal +2.2pp 和 object -2.2pp 是噪声(p>0.20)。paper_framing.md C5 已据此修正。
- **易错点**：(1) α=0.0 eval 结果如果 ≠ baseline，不要急着说"scoring 有 contribution"——LoRA scale=0 = 精确 baseline 是结构性保证，不符只能是代码 bug，必须查代码而非接受结果。(2) 不要把 connector_only ablation 的 13.7% drift 和 v7.2 的 0.4% drift 直接定量比较得出"drift 线性影响性能"的结论——两者的 loss function 完全不同（task-only vs task+contrastive+IB），drift 的方向和性质不同。(3) 8h GPU 空转事件的根因是 Worker 提交后未验证进程启动——后续每次 submit 后都应检查 nvidia-smi 确认。
