# agent / loop_16.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_16.md`
- **Structured JSON:** [`1c56ff1d97e5d83f3228.json`](../../sessions/1c/1c56ff1d97e5d83f3228.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: idle_timeout
updated: '2026-05-17T19:05:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**：bjb1-17606 仅 cuda:0,1；westd-47453 仅 cuda:0,1,2,3。超出范围必须 push back Director
- **westd-47453 必须 `export TORCH_COMPILE_DISABLE=1`**：RTX PRO 6000 的 torch._inductor 模板冲突会导致 vLLM crash
- **WANDB_MODE 禁止 disabled**：cron 依赖 W&B heartbeat 判活，disabled 会误判实验 failed
- **eval split 已统一为 valid_unseen(134 tasks)**（D064）：所有新实验必须用 `eval_dataset: "eval_out_of_distribution"`, `env_groups: 134`
- **factorial_h2_episodeadv_seed1 已 ALLOCATED 但未提交**：需要 ~20-25 行代码改动实现 episode-level advantage mode 后才能跑（plan_018）

### 2. 🖥️ 基础设施快照
- **bjb1-17606**（2× A6000）
  - 工作目录：需 SSH 确认（RAGEN 项目目录）
  - 活跃：hsweep_h2_seed2, PID=945877, cuda:0,1
- **westd-47453**（4× RTX PRO 6000）
  - 工作目录：需 SSH 确认（RAGEN 项目目录）
  - 活跃：gae_baseline_seed1 PID=40267 cuda:0,1；gsweep_g050_h5_seed1 PID=85798 cuda:2,3
- **Cron 监控**：3 个 cron 全部 reconcile OK，均 still running
- **Python/conda**：bjb1 和 westd 用 `source /root/miniconda3/bin/activate` 方式（不依赖 .venv）
- **W&B**：project = cost-verify-agent-rl（具体 entity 需 SSH 查 config）
- **模型**：Qwen3-1.7B 系列（具体路径在各实验 config 中）

### 3. 📊 当前状态
**刚完成**：Dream review 分析 → D062 framing 调整（放弃 "contrarian" 叙事，转 "mechanistic diagnosis + factorial causal attribution"）→ 新实验 plan_018/019 加入计划。

**RUNNING（3 个实验，6 GPU 全占满）**：
- `gsweep_g050_h5_seed1`：γ=0.5 极端衰减验证崩溃加速（westd cuda:2,3）
- `gae_baseline_seed1`：REINFORCE++ baseline 对比（westd cuda:0,1）— D065 early-stop at step 10
- `hsweep_h2_seed2`：h=2 第二 seed 复现 + ADV log 收集 for plan_004（bjb1 cuda:0,1）

**ALLOCATED 未提交（1）**：
- `factorial_h2_episodeadv_seed1`：关键 factorial 实验，需先实现 episode-level advantage 代码（plan_018 ~25 行改动）

**等待中**：
- 3 个 cron 回调（实验完成时触发）
- Director 未回复 r=0.640 诊断 4 个问题（D063）
- γ-sweep 后续 3 个 γ 值（g080/g095/g100）排在 g050 完成后 chain 提交

### 4. 📋 待办（条件触发式）
- `gsweep_g050_h5_seed1` 完成 → 提交 `gsweep_g080_h5_seed1`（同 GPU cuda:2,3）
- `gae_baseline_seed1` 完成（step 10 early-stop, D065）→ 分析 vs exp029 对比，更新 report
- `hsweep_h2_seed2` 完成 → spawn Worker 分析 ADV log + 提交 `hsweep_h10_seed1`（释放的 GPU）
- Director 回复 r=0.640 Q1-Q4 → 据此调整 sign misattribution claim 精度，可能影响 paper Proposition 2
- plan_018 代码就绪（Worker 实现 episode-level advantage mode）→ 提交 `factorial_h2_episodeadv_seed1`
- 全部 γ-sweep + h-sweep 完成 → 绘制 cliff figure (fig5) + 写 Results section

### 5. 🎯 战略上下文
**核心结论链**：
- D058: step-independent h=2 崩溃（0% by step 10）= 确认
- D057: episode-level 有效（28% at step 15）= Core Claim 1 ESTABLISHED
- D062: Framing 从 "contrarian/coarser is better" 转为 "mechanistic diagnosis"（因 GAGPO 93.5% 证明 finer credit 本身没问题）
- D063: sign misattribution 成立但比 binary 假设更复杂（Type C evidence 4%）

**易错点**：
1. **不要把 episode-level 当成 "我们的方法"**——episode-level 本身是 trivial，论文贡献是**诊断**为什么 step-independent 失败 + factorial 因果归因
2. **advantage vs step_return 是同源变量**（memory.md plan_004 陷阱）——r=0.640 无诊断意义，不要再用这个数字
3. **γ 在 GRPO 算法层面不存在**，是 RAGEN step_independent 实现引入的——论文必须精确区分 "算法" vs "实现"
4. **gae_baseline 实际是 REINFORCE++**（TRL 1.1.0 移除了 value head，D060）——不要混称 GAE
5. **exp028_prereq_zeroshot_instruct / exp020d 等老实验已 deprioritized**——当前焦点是 factorial (plan_018) + sweep 数据


---
