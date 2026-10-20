# reviewer / loop_3.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`f9a30c9e536ca480f84c.json`](../../sessions/f9/f9a30c9e536ca480f84c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T09:34:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 bjb1-45299 只有 2 张 GPU（cuda:0, cuda:1），项目未设 constraints.yaml，但所有实验均在这两张卡上跑，不得越界
- exp_009c 命令里 `--device cuda:0` 但实际通过 CUDA_VISIBLE_DEVICES 映射到物理 GPU 1——不要看到 `cuda:0` 就以为在 GPU 0 上
- cheetah 脚本已修复（加了 `defaults` config + `--compile False`），但尚未实际跑过——首次启动 cheetah 实验时务必验证能正常启动
- 008f 的 registry metrics 结构被 analysis worker 改过格式（eval_checkpoints 嵌套 dict），与其他实验的扁平 metrics 不一致——读 008f 指标时注意路径

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299(root)，工作目录 `/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`，conda env = base（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 代码 commit：`09876d7` (008f analysis worker 时的版本)
- Logdir：`/root/autodl-tmp/event-gated-adaptive-horizon/logdir/`（所有实验输出）
- Scripts：`/root/autodl-tmp/event-gated-adaptive-horizon/scripts/`（multi_seed_runs.sh, cheetah_run_experiments.sh, mvp_eval.py）
- W&B：未配置（本项目不检查 W&B）
- 活跃进程：009c (PID ~140985, GPU 1, tmux)。GPU 0 空闲。008f 刚完成（ANALYZING→等 DONE）

### 3. 📊 当前状态
**刚完成审查**：008f（C2 因果实验）和 008e_v3（B+ confound control）均已完成。008f 的 analysis worker 刚跑完，registry 可能还在 ANALYZING 状态等更新为 DONE。

**RUNNING**：
- exp_009c_008f_walker_s2（GPU 1, seed 2 复现 008f no-dt-embed 稳定性）

**ALLOCATED/QUEUED（未启动）**：
- exp_009a_baseline_walker_s2（GPU 0 已空，可立即启动）
- exp_009b_008d_walker_s2（QUEUED，008d 崩塌复现 seed 2）
- exp_010a_cheetah_baseline_s1（QUEUED，跨环境验证）

**等待**：008f analysis worker 完成 → registry 更新为 DONE。GPU 0 空闲 → Agent 应启动 009a 或 009b。

### 4. 📋 待办
- 008f registry 更新为 DONE → 核实最终 metrics 与 conclusion 是否准确（特别是 v/e 轨迹：峰值 39.1%@55K → 19.5%@105K）
- 009a/009b 启动 → 确认 GPU 分配 + PID 正确
- 009c 到 35K/45K → 关键检查点：v/e 是否与 008f seed 1 一致（无崩塌），seed 间方差大小
- 009b（008d seed 2）启动后到 45K → 确认崩塌是否在 seed 2 复现（v/e > 50%）
- 任何实验完成 → 常规审查（数据一致性 + GPU 合规 + 结论合理性）

### 5. 🎯 战略上下文
**核心因果链（已确认）**：
- C2 CONFIRMED：dt_embedding conditioning 是 delusional critic collapse 的直接原因（008d 崩塌 vs 008f 无崩塌，唯一差异 = gate_dt_embed_dim）
- B+ CONFIRMED：subsample ON（混合 dt 训练数据）本身不是问题（008e_v3 = 95% baseline）
- 问题不在 replay buffer 混合，而在 imagination 时 dt_embedding 误导 value function

**关键数值参考**：
| 实验 | eval@105K | v/e@峰值 | 结论 |
|------|-----------|---------|------|
| baseline | 916 | ~66%(稳定) | 参考 |
| 008a(no subsample,H15) | 778(85%) | 53.6%@75K | success |
| 008e_v3(subsample,dt1,H15) | 870(95%) | 52.3%@75K | success |
| 008d(subsample,dt2,H8,dt_embed) | 141@45K | 69.3%@45K↑ | 崩塌 |
| 008f(subsample,dt2,H8,NO dt_embed) | 503(55%) | 39.1%@55K↓ | 无崩塌 |

**易错点**：
- 008f 绝对性能差（55% baseline）不等于实验失败——它是因果控制实验，目标是证明 dt_embedding 是崩塌原因，不是追求高 return
- 不要把 008f 的"无崩塌"解读为"去掉 dt_embedding 是解决方案"——正确方向是修复 dt_embedding 在 imagination 中的使用方式
- 多 seed 实验（009 系列）才 1 个在跑，统计显著性声明要等 seed 2/3 数据


---
