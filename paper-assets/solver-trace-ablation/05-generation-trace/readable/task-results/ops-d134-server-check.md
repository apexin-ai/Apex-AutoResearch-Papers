# ops d134 server check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d134-server-check_20260518T164650_result.json`
- **Structured JSON:** [`f1d1cec2e87ae1795288.json`](../../sessions/f1/f1d1cec2e87ae1795288.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇报如下：

---

## 诊断结果

### 1. tmux sessions
**两个 session 均存活**，服务器未重启（或重启后 session 存活于持久化层）：
- `d134-pipeline` — 创建于 May 18 18:52，正在活跃输出训练日志
- `d134-cleaner` — 创建于 May 18 20:02，pane 为空（无输出）

### 2. Random s47 训练状态
**正在训练中，step 327/500（65%）**，未中断。
- 输出目录：`/root/autodl-tmp/outputs/d134_4b_random_b01_s47/`
- 已有 `checkpoint-300`（16G）
- 无 `eval_results/` 或 `classify/`（尚未完成）
- 当前指标：reward ~0.66-1.06, prove_rate 0.625-1.0, parse_rate 1.0
- 预估剩余：~173 steps × ~14s/step ≈ 40 分钟

### 3. ISR s47-s51 状态
**全部 5 个 ISR seed 已完成训练 + eval + classify**：
- s47: 完成（19:50），模型权重保留（16G），有 eval_results.json + classify.json
- s48: 完成（20:39），checkpoint 已清理（17M），有 eval + classify
- s49: 完成（21:44），checkpoint 已清理（16M），有 eval + classify
- s50: 完成（22:31），checkpoint 已清理（16M），有 eval + classify
- s51: 完成（23:31），checkpoint 已清理（16M），有 eval + classify

d134-cleaner 已清理了 s48-s51 的模型权重，s47 的权重仍在（可能因为正在被 Random s47 参照或尚未清理）。

### 4. Random s48-s51
**均不存在**，尚未开始。Pipeline 正在顺序执行 Random s47，后续会依次训练 s48-s51。

### 5. 磁盘空间
- `/root/autodl-tmp`: 250G 用了 223G (89%)，剩余 28G
- `/root/autodl-tmp/outputs/`: 183G
- 当前 Random s47 checkpoint 占 16G，完成后 cleaner 应会清理
- **磁盘偏紧但可支撑完成 pipeline**（每个 Random 训练峰值约 16G，cleaner 会在完成后清理）

### 6. nvidia-smi
- GPU 0: RTX PRO 6000 Black，85.5G/97.9G 显存占用（88% utilization）
- PID 91314: `train_grpo.py --config configs/grpo_additive_random_b01.yaml ... --seed 47`
- 无异常进程

### 7. Pipeline/Cleaner 脚本
- Pipeline 脚本：未找到独立 `pipeline*` 文件，训练通过 tmux session `d134-pipeline` 中的 inline 命令/循环驱动
- Cleaner 脚本：未找到 `*clean*` 文件，`d134-cleaner` 通过 inline 脚本执行
- 已有脚本：`scripts/launch_extra_seeds.sh`, `scripts/launch_beta_sweep.sh`, `scripts/launch_phase1.sh`, `scripts/run_eval_after_training.sh`, `scripts/gpu_guard.sh`, `scripts/dryrun_8b.sh`, `run_1.7b_eval.sh`

### 结论
**Pipeline 未中断。** Random s47 正常训练中（65%），ISR 5 seed 全部完成。无需干预。

---
