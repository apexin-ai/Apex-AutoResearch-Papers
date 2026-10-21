# director / loop_3.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`9b85f481d20d72818401.json`](../../sessions/9b/9b85f481d20d72818401.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-14T01:35:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb1-45299 的 cuda:0 和 cuda:1（RTX PRO 6000 × 2），不得使用其他 GPU
- exp_008b 已被 D018 取消，替换为 exp_008c（dt=2, H=8）。不要再实现或启动 008b
- Go/No-Go 阈值：65K ≥493, 105K ≥733（baseline@105K=916，80% = 733，不是 640）
- 代码真源在远程 `/root/autodl-tmp/event-gated-adaptive-horizon`，论文/文档真源在本地 workspace

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299 (connect.bjb1.seetacloud.com)，用户 root
- 工作目录：/root/autodl-tmp/event-gated-adaptive-horizon
- 镜像：aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 活跃进程：无（两卡已清理，0% util, 0 MiB）
- 关键 commit：576ab86（gate_subsample_max_dt 参数，析因实验代码基础）
- W&B / HF cache：未配置

### 3. 📊 当前状态
D018 决策已完成，析因实验代码已就绪但 **训练未启动**（Agent 在 dry-run 阶段后空闲 180min 触发重置）。这是最紧迫的问题——两卡空闲中。

Registry:
- `exp_008a_no_subsample_dt2` — PREPARING, cuda:0: subsample OFF + dt=2 + H=15（物理覆盖 30 步）
- `exp_008c_no_subsample_dt2_h8` — PREPARING, cuda:1: subsample OFF + dt=2 + H=8（物理覆盖 16 步）

无等待中的 Worker 回调 / Cron。

### 4. 📋 待办
- **立即**：启动 exp_008a (cuda:0) + exp_008c (cuda:1) 并行训练，GPU 已空闲太久
- 65K 步到达 → 检查 eval_return：008a ≥493? 008c ≥493? 若低于阈值提前判定崩塌
- 105K 步到达 → 最终判定：008a 崩 + 008c 不崩 → compounding error 确认，H∝1/dt 是解法；都崩 → dt=2 RSSM 质量不足；008a 不崩 → Reviewer 预测错误，回查 subsample
- 008c 成功 → 考虑 008d (dt=2, H=10/12) 寻找临界点
- 训练等待期间 → pivot 调研 Worker 应已完成，读取 THICK/Options framework 设计文档

### 5. 🎯 战略上下文
**决策链**：Gumbel gate 失败(D009) → fixed dt 诊断(D010-D013) → dt=2/4 都崩(D015) → curriculum 假说被代码审计推翻(D017) → 2x2 析因设计 → Reviewer 提出 compounding error 假说 → D018 将 008b 替换为 008c(H=8)

**核心判断**：Reviewer 和崩塌分析都指向同一结论——问题不在 RSSM 世界模型（model_loss 健康），而在 imagination 物理覆盖过长导致 actor-critic 优化崩塌。exp_008c (H=8) 是关键验证。

**易错点**：
- 不要把 exp_008b 和 exp_008c 搞混——008b 已取消，当前方案是 008a + 008c
- baseline@105K = 916 不是 800，go/no-go 阈值 733 不是 640（已被 Reviewer 纠正过一次）
- CoRL DDL 2026-05-29（剩余 15 天），成功路径最快 3 天到论文初稿，但前提是析因实验今天出结果


---
