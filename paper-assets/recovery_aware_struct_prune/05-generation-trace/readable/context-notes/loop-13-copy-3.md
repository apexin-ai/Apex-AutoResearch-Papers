# reviewer / loop_13.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`818a74ca55f985e90fbd.json`](../../sessions/81/818a74ca55f985e90fbd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-17T18:00:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- westb GPU 白名单: cuda:0, cuda:1 只允许这两张卡
- westd GPU 白名单: cuda:0, cuda:1, cuda:2, cuda:3
- GRPO checkpoint 不公平问题 (D051): Standard 用 checkpoint-50 (max_steps=100, post-peak), RASP 用 v9 final (max_steps=30, collapsed)。**所有 GRPO 对比 claim 必须注明此 confound**，不可作为公平对比引用
- HumanEval 所有 @512 结果已废弃（truncation artifact: unpruned@512=1.83% vs @2048=45.12%），只用 @2048 数据
- eval_humaneval_grpo_rasp_20_2048 的 EXIT_CODE=129 是误报，数据有效（pass@1=14.63%，结果文件已保存）

### 2. 🖥️ 基础设施快照
- **westb-23072** (root): 代码 `/root/recovery_aware_struct_prune`，模型/结果 `/root/autodl-tmp/recovery_aware_struct_prune/`
- **westd-11672** (root): 同上路径结构，模型复制在 westd 本地
- Python: `/root/miniconda3/bin/python` (两台都是)
- wandb project: `recovery_aware_struct_prune` (user: xiaoyucorynne-)
- **westb 活跃进程**:
  - GRPO cka_only training: step ~26/100, ~415s/step, wandb=li451oi4, cuda:0 (~93GB)
  - GRPO random training: step ~35/100, ~450s/step, cuda:1 (~73GB)
- **westd 活跃进程**:
  - GRPO Standard MATH-500: PID 14556, cuda:1, ~130/500, ~17h remaining, 无 timeout
  - MATH-500 GRPO RASP v3: PID 31706, cuda:3, timeout=604800s (7d), 刚开始 ~3h
  - cuda:0 和 cuda:2 刚完成 eval，可能已被重新分配（检查 nvidia-smi）

### 3. 📊 当前状态
**刚完成**: HumanEval@2048 五模型矩阵全部完成 + GRPO cka_only/random step 20 数据分析 + claim 强度预审提交

**关键发现已报 Director**:
1. CKA-only GRPO 极其稳定 (reward=0.253, frac_zero_std=0.175 at step 10) — 完全推翻 "Redundancy-Stability Tradeoff" 预测
2. 稳定性梯度: CKA-only > Random > Standard > RASP（与预测方向相反）
3. HumanEval@2048: GRPO RASP 14.63% > SFT Standard 11.59% ≈ SFT RASP 10.37% = GRPO Standard 10.37%
4. 跨 benchmark 无方法一致占优（GSM8K 收敛，HumanEval RASP 领先，MATH-500 Standard 领先）
5. 论文整体预估 Findings 级别 (2.5-3.0)，升 Main 最需公平 GRPO 对比

**等待中**:
- GRPO cka_only step 30 数据 (~15 min)
- GRPO random 继续监控到 step 50+
- MATH-500 两个 eval (Standard ~17h, RASP v3 ~13h)
- Director 对 claim 预审 + narrative reframe 的决策
- paper method-results draft worker 完成，可能触发章节审查

### 4. 📋 待办
- cka_only step 30 出数据 → 对比 step 10/20 趋势，如 frac_zero_std 仍 <0.3 则确认 "representational diversity = RL stability"
- cka_only frac_zero_std 突然 >0.5 → 降级为 "delayed collapse"，重新评估 narrative
- Random grad_norm 再次 spike → 标 warning，可能需要 early stopping
- MATH-500 RASP v3 / Standard 完成 → 交叉验证 interim 数据，更新 C1/C3 评估
- Director 转发论文章节审查 → 执行模式 B 审查 (claim 可信度 + 叙事逻辑 + 攻击面)
- westd cuda:0/cuda:2 空闲 → 检查是否被合理分配新任务

### 5. 🎯 战略上下文
**核心转折**: CKA-only GRPO 数据推翻了原始 "去冗余导致不稳定" 假设。实际是 "保留表征多样性 = RL 稳定性"。这比原假设更 interesting 也更 counter-intuitive，但需要 step 50+ 数据确认趋势持续。

**最容易判断错的事**:
1. 不要把 GRPO RASP vs GRPO Standard 当公平对比——config 完全不同 (max_steps 30 vs 100, 不同 checkpoint)
2. 不要信 "multiseed 显示 RASP > Standard"——seed 123 方向翻转 (Standard 64.5% > RASP 60.5%)
3. eval_math500_grpo_rasp_20_v2 FAILED (timeout)，interim 数据 N=150 acc=30.67% 只能做参考不能做 claim
4. 所有 HumanEval@512 数据已废弃，只用 @2048
5. CKA-only step 10/20 数据很漂亮但只有 20 步——可能后期 collapse，不要过早下结论

**决策链**: D051 = checkpoint 不公平审查 → 影响所有 GRPO 对比的可信度


---
