# reviewer / loop_3.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`4ab2c406f2799860f8ac.json`](../../sessions/4a/4ab2c406f2799860f8ac.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-16T05:38:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：seed1 用 cuda:0，seed2 用 cuda:1。不可越界（D026 事故后的硬约束）
- seed2 日志有 fd offset 问题：`tail` 看不到最新输出，必须用 `grep "^Step"` 查看完整训练步
- `run_acib_eval.sh` 有致命 bug（传 ACIB checkpoint dir 给 lerobot-eval，无法加载）。**必须用 `eval_acib.py`** 做 ACIB eval
- seed2 registry 曾被 cron 误标 failed（wrapper PID 死但 python 子进程存活），已修正为 RUNNING。如果再次被误标，先检查 `/proc/&lt;PID>` 再判断
- `train_acib.py` 有 `--lambda_ent default=0.1`。seed1 的 config 无此字段（argparse 不存在时启动）。新 seed 启动必须显式传 `--lambda_ent 0`

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953(root)，代码根：`/root/acib`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 数据集：`/root/autodl-tmp/libero_dataset`
- HF cache：`/root/autodl-tmp/.hf_cache`
- wandb：WANDB_MODE=disabled/offline（无 API key）
- 活跃进程（截至 handoff）：
  - PID 682233: seed1 训练, cuda:0, 16.2GB, step ~12200/20000
  - PID 755664: seed2 训练, cuda:1, 16.2GB, step ~5600/20000
  - PID 675231: baseline_plus libero_10 eval, cuda:0, 5.3GB
  - PID 733616: baseline_std libero_10 eval, cuda:1, 5.9GB
- Checkpoints：seed1 有 checkpoint-5000 和 checkpoint-10000；seed2 有 checkpoint-5000
- Scorer analysis 产出：`/root/acib/outputs/scorer_analysis_seed1_step5000/`（JSON + 3 PNG）
- Eval 脚本：`/root/acib/scripts/eval_acib.py`（正确）、`/root/acib/scripts/run_acib_eval.sh`（有 bug 勿用）

### 3. 📊 当前状态
**刚完成**：seed2 checkpoint-5000 验证通过（scorer_std=0.439 与 seed1 的 0.441 一致）；scorer analysis v2 审查（确认 128 tokens = 2 cameras × 64，bimodality BC=0.937 在纯视觉 token 内）；eval 代码审查（发现 shell script 致命 bug）；framing 审查（建议维持 D006 framing 不升级）。

**RUNNING 实验**：
- `acib_v5_div_reg` (seed1): step 12200/20000, scorer_std=0.447, ETA ~07:45 UTC
- `acib_v5_div_reg_seed2`: step 5600/20000, scorer_std=0.441, ETA ~11:30 UTC
- `mvp1_baseline_plus_remaining`: libero_10 eval 进行中（PID 675231）
- `mvp1_baseline_std_libero10`: libero_10 eval 进行中（PID 733616）

**等待中**：cross-task probe 重跑（首次因无 CUDA 失败，需设 `CUDA_VISIBLE_DEVICES`）

### 4. 📋 待办（条件触发式）
- seed1 完成 step 20000 → 立即验证 checkpoint-20000 存在 + final scorer_std + 启动 eval（用 `eval_acib.py` 不是 shell script，seed=42 保持与 baseline 一致）
- baseline_plus/std libero_10 eval 出 `eval_info.json` → 提取 SR，补全 baseline 对比表（已有：plus spatial=81.6%, object=88.8%, goal=87.8%; std spatial=66.0%, object=67.8%, goal=76.4%）
- cross-task probe 重跑成功 → 审查 condition-dependence 结果。如果 scorer 对不同 language instruction 输出相同 mask → CRITICAL，"Action-Conditioned" claim 不成立，需降级为 "Spatial IB"
- seed2 完成 step 20000 → 验证 checkpoint + cross-seed eval 一致性
- seed1 eval 结果出来 → 对比 baseline SR。任一 suite 回退 >2% → WARNING；全部 suite 无改善 → 审查 β=0.01 是否太弱

### 5. 🎯 战略上下文
- **核心发现**：v5_div_reg 是唯一成功版本。五代迭代暴露三个独立失败模式：per-token KL 平凡解(v1/v3)、aggregate KL 常数满足(v4)、task 信号断裂(v5_stopgrad_entropy)。关键 insight：task gradient 必须流经 scorer + diversity reg 是必要的 anti-collapse 机制
- **决策链关键节点**：D006（framing 转向互补性）、D013（per-token→aggregate KL）、D015（diversity reg）、D021（stop-grad 失败确认 task gradient 必要性）、D022（MVP 标准重定义为标准 SR + scorer 分化）
- **最大风险**：scorer_std 高 ≠ eval 提升。Bimodal 权重分布（41% off, 49% on）是积极信号，但 token 选择是否 task-relevant 尚未验证（cross-task probe 失败待重跑）。per-token ratio ≈ within-sample ratio (20.2 vs 22.6) 暗示可能是固定 position prior 而非 action-conditioned selection
- **易错点**：(1) 不要用 `run_acib_eval.sh`（lerobot-eval 不能加载 ACIB checkpoint）；(2) seed2 日志用 grep 不用 tail；(3) 重复进程 bug 已发生 4+ 次——每次 Agent 启动新训练前检查 `pgrep -f train_acib`；(4) report.md 严重过时（仍显示 seed2 failed），不可信赖
- **DDL**：CoRL 2026 abstract 5/26, paper 5/29——距今 10/13 天


---
