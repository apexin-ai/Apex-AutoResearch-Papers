# reviewer / loop_2.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`1beee72c5c30e29f8e4e.json`](../../sessions/1b/1beee72c5c30e29f8e4e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T02:18:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（westd-39279 只有两张卡，项目配置允许两张）
- 训练数据必须用 `/root/solver-trace-ablation/data/train_500_seed42.jsonl`（484867 bytes, 500 lines）做多 seed 对比。`proofwriter_fol_500.jsonl` 是不同数据集（485044 bytes），混用会引入 data confound（plan001-s43-r1 踩过此坑）
- CUDA_VISIBLE_DEVICES 必须用 `export CUDA_VISIBLE_DEVICES=N &&` 而非 inline 赋值，否则 PyTorch 看到所有 GPU → OOM 溢出（plan013-r1 踩过）
- TRL GRPOTrainer 每个实验存 ~48GB（3 份 checkpoint），必须设 `save_total_limit=1, log_completions=False`，否则磁盘爆满（r3 踩过）

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279(root)，项目目录 `/root/solver-trace-ablation`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 模型：`/root/autodl-tmp/models/Qwen3-4B`
- 数据盘：`/root/autodl-tmp/`（250G，截至 handoff 时 56% 使用 139G/250G）
- 输出目录：`/root/autodl-tmp/outputs/plan{NNN}_{name}/`
- W&B：未配置（不检查 W&B）
- 活跃进程（handoff 时刻）：
  - plan013-random-reward-s42-r4：PID 136261, tmux, cuda:0, step ~455/500（即将完成）
  - plan001-exec-only-s43-r4：PID 136339, tmux, cuda:1, step ~219/500（预计还需 ~45 分钟）

### 3. 📊 当前状态
刚发送实验中期审查报告给 Director，核心发现：

1. **ISR 日志方法不一致**：isr-monitoring-fix 导致 exec-only 用 `_full_fn`（真实 ISR, O(n)），random_reward 仍用 `_fast_fn`（二值 ISR, O(1)）。plan001-s42-r2 的 ISR=0.86 是旧代码二值近似（≈prove_rate），**不是真实结构质量**。
2. **plan001-s43 真实 ISR 极低**：prove_rate=1.0 时 ISR=0.05-0.19，是 exec-only reward hacking 的直接证据。
3. **GRPO 饱和不对称**：exec-only 在 PR=1.0 时 loss=0（无梯度），random_reward 因随机分量保持 reward variance 仍有梯度。

Registry 状态：
- RUNNING：plan013-random-reward-s42-r4, plan001-exec-only-s43-r4
- DONE（成功）：plan001-exec-only-s42-r2, plan005-sta-low-s42, plan003-eval-exec-only-r5, sta-gt-isr-baseline, sta-phase0-baseline
- plan005 spec 已修复（model_name/data_path 均正确）

### 4. 📋 待办
- plan013 完成 → 核查最终 metrics，特别关注 prove_rate 轨迹。如果 PR 与 exec-only 持平，random 未提供独特信号 → 需要 eval_sta.py 对 checkpoint 做真实 ISR 评估才能下结论
- plan001-s43 完成 → 对比 s42-r2 的 prove_rate 轨迹，确认多 seed 可复现性。注意两者 ISR 日志不可比（不同代码版本）
- 两个实验都完成后 → 催促 Agent 统一跑 eval_sta.py 和 eval_downstream.py，获得可比较的真实 ISR
- additive_bonus（plan002）提交后 → 核查：(1) 用 `_full_fn`，(2) beta=0.3，(3) GPU 合规，(4) 也会有 3-4x 速度瓶颈
- Prolog 实验准备 → proofwriter_prolog_500.jsonl 尚不存在，configs 需要改 weights 0.9/0.1, steps 500

### 5. 🎯 战略上下文
- 决策链：D001→D008（penalty effect 确认）→D010（additive bonus pivot）→D011（Narrative A+C 批准）
- 论文 framing 已从"STA detects hacking"转向"STA as principled structural metric + additive bonus integration"
- **最容易判断错的事**：
  1. 不要把 registry 中 plan001-s42-r2 的 ISR=0.86 当作真实结构质量——那是二值近似（≈prove_rate）。真实 ISR 需要 eval_sta.py 重新评估
  2. plan013 日志中 ISR=1.0 也不是真实 ISR——是 fast_isr 二值近似。跨实验 ISR 比较只能用 eval_sta.py 统一评估后的数据
  3. random_reward 的 anti-saturation 效应（random 分量维持 reward variance）是 exec-only 所没有的——如果 plan013 结果与 exec-only 不同，不能简单归因于"random vs ISR"，需讨论训练动态差异
  4. Dream review 给出 best 4/6 Borderline Reject，5 个结构弱点，其中 M2/W7（random reward 对照）= plan013 正在做的实验


---
