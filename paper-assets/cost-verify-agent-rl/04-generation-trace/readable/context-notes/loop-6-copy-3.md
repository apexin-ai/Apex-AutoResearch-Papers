# reviewer / loop_6.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`04a17d04debaaf2c784a.json`](../../sessions/04/04a17d04debaaf2c784a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-15T05:19:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0, cuda:1（bjb1-17606 服务器，C001 约束）。每次审查训练实验必须核对 CUDA_VISIBLE_DEVICES。
- 数据盘 `/root/autodl-tmp/` 刚清理到 39%（153G 可用），大文件必须放这里不能放根分区。
- exp021 SFT baseline 的真实 success rate 是 **6.25%**（16ep），不是 registry/ROADMAP 中写的 25%（4ep 噪声）。任何引用 25% 的结论都需纠正。
- ssh_read_only 不支持管道符 `|`，grep 的 `\|`（正则 OR）也会被拦截。用多次单独 grep 代替。

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606 (root)，2× 97GB GPU
- 工作目录：`/root/cost-verify-agent-rl/RAGEN/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- SFT checkpoint：`/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final/`
- exp023c checkpoint：`/root/autodl-tmp/checkpoints/exp023c/global_step_5/`（8步退化后崩溃，仅供分析）
- 训练数据：`/root/autodl-tmp/expert_sft_v4/`（2546 train / 133 val）
- 日志：`/root/runs/cost-verify-agent-rl/`（标准）+ `/root/autodl-tmp/checkpoints/exp023c/train.log`（非标准）
- 活跃进程：**无**。两张 GPU 空闲（0 MiB）。无 tmux session / cron。
- 磁盘：`/root/autodl-tmp/` 98G/250G used (39%)

### 3. 📊 当前状态
**刚完成**：exp023c 崩溃后的全面审查 + ROADMAP D026 pivot 审查。

**registry 状态**：44 个实验，全部 DONE。无 RUNNING/PREPARING。exp023c 未注册 registry（已多次提醒 Agent 补注册）。

**等待中**：
- Agent 正在执行 D026 pivot：verl-agent GiGPO cherry-pick 实现（Plan C, 3-5天预估）
- 可能会有 worker_code 类 Worker 开始 verl-agent 整合代码

### 4. 📋 待办（条件触发式）
- verl-agent 整合代码 Worker 完成 → 核实 GiGPO 算法实现是否正确引入 step-independent rollout，检查是否复用了 exp021 SFT checkpoint
- 新实验启动（exp024/025 等）→ 核实 GPU C001 合规、val env_groups ≥ 16、registry 已注册
- 任何训练 Worker 完成 → 独立 `nvidia-smi` 核对 GPU 使用，`tail_training_logs` 交叉验证指标
- Agent 引用 exp021 success=25% → 立即纠正为 6.25%（16ep baseline）
- Agent 声称 "格式分布偏移" 是性能低的原因 → 已核实 SFT v4 数据与 RAGEN 格式一致，此归因不成立

### 5. 🎯 战略上下文
**核心决策链**：D021（SFT-RAGEN 格式对齐）→ D023（exp021 SFT 通过）→ D025/D026（GRPO 3/3 失败，终止 RAGEN GRPO，pivot verl-agent GiGPO）

**关键结论**：
- RAGEN + GRPO + 稀疏 reward 在 ALFWorld 上 3 次均退化（exp020b/022/023c），路线已终止
- verl-agent 论文报告同模型(Qwen3-1.7B) + GRPO 达 72.7% success，差异在于 step-independent rollout + GiGPO
- MVP 目标 success ≥ 20%，真实 baseline 6.25%，需要 ~3x 提升

**易错点**：
1. **不要信 exp021 的 25% success**——那是 4-episode 噪声。16ep 基线是 6.25%。Agent/ROADMAP 可能仍引用旧数字。
2. **不要把 action_is_valid 跨评估的波动当系统性问题**——4ep=87.5%, 8ep=48.75%, 16ep=68.75%，这是小样本方差不是 OOD。
3. **两个诊断 Worker 声称 "SFT 训练格式与 RAGEN 推理格式不一致" 是错误的**——我独立核实 SFT v4 数据包含完整 RAGEN 格式元素（Turn/State/Reward/FORMAT_PROMPT）。
4. **env.py 已有两把锁**：`_RAW_ENV_LOCK`（cache保护）+ `_TW_LOAD_LOCK`（tatsu 解析器保护）。若后续重新开启并行（parallel_friendly=true），这两把锁必须保留。
5. **config.py `score` 当前为 10.0**（已从 1.0 回退）。verl-agent 整合时注意 reward scale 是否需要调整。


---
