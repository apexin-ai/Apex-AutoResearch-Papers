# reviewer / loop_17.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_17.md`
- **Structured JSON:** [`487eb067fe9543489948.json`](../../sessions/48/487eb067fe9543489948.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_wall_time
updated: '2026-05-17T08:12:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cuda:0 和 cuda:1（westd-39279 仅分配 2 张卡）
- CUDA_VISIBLE_DEVICES 必须通过 `export` 在 bash -c 内设置，不能依赖 submit_training_job 自动注入
- 论文数据引用必须标注来源 seed 数（3-seed / 4-seed / 5-seed），禁止混合不同 n 的数据在同一个 claim 里而不注明
- C012：resume 训练必须验证 step 语义（checkpoint-N + 500 = N+500）；当前 Wave 1 是从头训练故无此风险
- C013：genuine = proved − |H7 ∪ H1 ∪ H8|（集合排除，不双减重叠）

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279 (root)，SSH account=root
- 远程代码：`/root/solver-trace-ablation`
- 远程输出：`/root/autodl-tmp/outputs/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/`
- 论文：`projects/solver-trace-ablation/paper/` (本地)
- Python: `/root/miniconda3/bin/python3`, conda env=base
- 模型：Qwen3-4B (HF cache 自动)
- 无 W&B（所有实验 --no_wandb）
- 活跃进程（截至 handoff）：
  - Random β=0.1 s45: PID 171186 → 子进程 171186, GPU 0, ~451/500 步, ETA ~15 min
  - Random β=0.05 s42: **已完成** 500/500, checkpoint at `/root/autodl-tmp/outputs/sweep_random_b005_s42/checkpoint-500`

### 3. 📊 当前状态
**刚完成**：D120 Reframe 终稿 + 后续修复批次的审查，已 post 两轮发现给 Director。

**关键未决**：
- `sweep-random-b005-s42`: 训练完成，等待 eval + classify_h7（Agent 应很快 dispatch worker）
- `plan018-additive-random-b01-s45`: 训练 ~451/500，几分钟内完成，然后需 eval
- Registry 状态：上述两个标 RUNNING，但 b005 实际已完成

**等待中**：
- Agent dispatch eval workers → 我审查 eval 结果
- Director 对我提出的 OR=15 降级问题的决策

### 4. 📋 待办（条件触发式）
- Random β=0.05 s42 eval 完成 → 核心分析：H7 率多少？如果 H7 低 + genuine 高 → "ISR amplification at lowest dose" 成立；如果也 100% H7 → dose-response 叙事需大改
- Random β=0.1 s45 eval 完成 → 立即做 5v5 Fisher exact test（ISR vs Random H7 rate + genuine rate）→ 决定 OR=15 是否需降级
- 5v5 数据齐全 → 计算 Cliff's delta for genuine rate, 确认条件级比较是否有统计意义
- Paper Agent 修 conclusion.tex L11 (~23% bug) → 验证修复正确性
- Paper Agent 恢复 Random s46 H7=91.5% 注释 → 验证

### 5. 🎯 战略上下文
**核心叙事 (D120)**："ISR reliable as diagnostic, unreliable as optimizer at any dose; β controls timing not destiny"

**关键数据风险（下一个"你"最容易判断错的点）**：
1. **OR=15 可能不再成立**。Random s46 有 91.5% H7（极端 outlier）。4-seed Random pooled H7=34.3%（vs 3-seed 13.7%）。如果 s45 也有高 H7，5v5 OR 可能降到 2-3。论文目前报 OR=15 (3-seed)，Table 1 显示 4-seed H7=32。审稿人会发现这个矛盾。
2. **~23% 的含义**：这是 5-seed pooled（含 2 个 0% seed）。3 non-collapsed seeds pooled 实际是 ~40%。conclusion.tex L11 仍有旧 bug 未修。
3. **Random β=0.05 s42 训练 ISR≈0.21**（低，对比 ISR β=0.05 的 0.75）。这是 ISR amplification 的强信号，但需 eval 确认。
4. **Table 1 ISR β=0.1 行混合 3/5-seed 数据**。PR=77±14 和 H7=71 是 3-seed (s42/s43/s44)；N-H=23 是 5-seed。Wave 1 eval 完成后应全行更新为 5-seed。
5. **不要用人类时间直觉判断可行性**。DDL 2026-05-25，8 天，2 GPU 24/7，数据点补齐只需 hours not days。


---
