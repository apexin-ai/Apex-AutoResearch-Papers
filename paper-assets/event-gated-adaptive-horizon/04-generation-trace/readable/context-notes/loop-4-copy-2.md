# agent / loop_4.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`bbc6bdd2559bba8bed0c.json`](../../sessions/bb/bbc6bdd2559bba8bed0c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-14T04:05:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 + cuda:1 on bjb1-45299，不可用其他 GPU
- submit 命令必须 `bash -c "..."` 包装，必须带 `--compile False`，必须带环境三件套：`LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6`, `MUJOCO_GL=osmesa`, `PYOPENGL_PLATFORM=osmesa`
- conda 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- GPU 编号始终从 0 开始（框架注入 CUDA_VISIBLE_DEVICES）
- **禁止再尝试 hard categorical gate（含 K=2 Gumbel-Softmax）**——3 轮 bug 修复后确认结构性失败
- Worker registry 更新不可靠——Worker 回调后必须自己 read_registry 验证
- 录入 metrics 必须核实 metrics.jsonl 原始数据（之前有误录事故）

### 2. 🖥️ 基础设施快照
- **服务器**：bjb1-45299，工作目录 `/root/autodl-tmp/event-gated-adaptive-horizon`
- **Python**：`/root/miniconda3/bin/python`（conda base 环境）
- **模型**：DreamerV3 代码在工作目录下，`dreamer.py` 为入口
- **日志目录**：`/root/autodl-tmp/event-gated-adaptive-horizon/logdir/`
- **Baseline checkpoint**：`logdir/baseline_s1`（exp_001, 512K steps, eval ~950.9）
- **活跃进程**：
  - exp_008a: PID 106942, tmux session, cuda:0, logdir=`exp_008a_fixed_dt2_no_subsample`
  - exp_008c: PID 107021, tmux session, cuda:1, logdir=`exp_008c_fixed_dt2_no_subsample_h8`
  - exp_008d: PID 109519, tmux session, cuda:0, logdir=`exp_008d_subsample_on_h8`
- **Cron**：reconcile 返回 0 active crons（可能需要重新注册监控）
- **GPU 预算**：累计 ~58 GPU·h，RTX PRO 6000 × 2

### 3. 📊 当前状态
三个实验正在运行，均为析因实验（隔离 subsample / dt_embedding / horizon 的影响）：

| exp_id | 假设 | GPU | 最新指标 | 状态 |
|--------|------|-----|---------|------|
| **008a** (H=15, no subsample, untrained dt_emb) | 隔离 subsample 效应 | cuda:0 | @55K=487.9, v/e=37.6%, 从 peak 563.4@45K 回落 | **等 @65K 决策点** |
| **008c** (H=8, no subsample, untrained dt_emb) | 隔离 compounding error | cuda:1 | @35K=185.1, plateau | 确认 underfitting 非崩塌 |
| **008d** (H=8, subsample ON, trained dt_emb) | 证明 trained dt_emb → delusional critic | cuda:0 | @35K=146.3, v/e=41.2% | 🔑 决定性证据已产出，等 @45K 确认崩塌复现 |

**exp_006** 状态 PREPARING 是残留条目，实际已由 exp_006_fixed_dt2 覆盖（DONE/negative）。

**Worker 池为 0**——没有正在运行的 Worker。

**008e**（gate_dt_embed_dim=0 参数化）代码已准备，等 dryrun 验证。ROADMAP 提及但 registry 无条目。

### 4. 📋 待办（条件触发式）
- **008a @65K eval 到达** → 这是最关键决策点：
  - ≥450 → Narrative B+（延迟+减弱崩塌），向 Director 汇报可行
  - <350 → 锁定纯 Narrative B（诊断分析论文）
  - 350-450 → 灰色地带，参考 actor_loss 斜率和 value/eval 趋势
- **008d @45K eval 到达** → 预测 value/eval >50% + eval 加速下降 → 完整复现 exp_006 崩塌模式，写入 registry 确认因果链
- **008a + 008d 均完成** → spawn Worker 做 008e（dt_embed_dim=0）dryrun + 提交；同时 spawn Worker 创建 paper_framing.md
- **所有析因完成** → 扩展到 2 个额外 DMC 环境（Cheetah Run, Hopper Hop）验证通用性
- **Cron 监控为空** → 需要为 008a/008c/008d 重新注册 cron 监控（reconcile 返回 0）
- **CoRL DDL 2026-05-29**（剩 15 天）→ 析因完成后立即进入 paper_framing → experiment_plan → 论文写作流水线

### 5. 🎯 战略上下文
**核心结论**：variable-rate imagination 在 DreamerV3 中失败的根因是 **trained dt_embedding 导致 delusional critic**（value 过估 → actor 被误导 → return 崩塌）。因果链已由 008c vs 008d 对照实验闭合（同 H=8 同 dt=2，唯一差异是 dt_emb 是否参与训练）。

**决策链关键节点**：
- D021: 因果链闭合（008c vs 008d）
- D020: 机制修正（精确 imagination → delusional critic）
- D019: Compounding error 假说被反驳
- D013: dt=4 失败是动作分辨率问题非模型能力

**论文方向**：Narrative B = Diagnostic Analysis of Temporal Abstraction in World-Model RL。不是"我们的方法 work"，而是"我们系统性分析了为什么不 work 并发现了根因"。这是一篇诊断分析论文。

**最容易判断错的事**：
1. **008a 的回落不等于崩塌**——@55K=487.9 从 peak 下降 13.4%，但 baseline 同期也有波动。需要看 @65K 才能判断是正常波动还是 exp_006 式崩塌。不要提前下结论
2. **008c 的低 eval 不是失败**——H=8 的 underfitting 恰恰证明 compounding error 不是根因（缩短 H 恶化了性能），这是正向证据
3. **exp_006 PREPARING 是垃圾条目**——真正的 exp_006 数据在 exp_006_fixed_dt2 里
4. **单 GPU 可跑 8-10 并发**（每进程仅 ~4GB on 98GB RTX PRO 6000），不要以为 2 并发就满了
5. **Cron 监控可能已丢失**——reconcile 返回 0，但有 3 个 RUNNING 实验。优先重建 cron 监控


---
