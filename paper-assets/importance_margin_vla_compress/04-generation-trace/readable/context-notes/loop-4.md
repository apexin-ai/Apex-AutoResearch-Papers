# director / loop_4.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`5fab924813b62d4a5480.json`](../../sessions/5f/5fab924813b62d4a5480.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-16T04:10:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-27271:cuda:0 和 westd-27271:cuda:1（项目分配的 2 张 RTX PRO 6000 96GB）
- evaluate.py 刚修完 5 处 bug（D028），任何 eval 必须用修复后版本——绝不能用旧版本跑
- G3 的 bypass 7.12x 是 co-adaptation 不是 gradient isolation 失败——不要重新排查梯度隔离代码，Reviewer 已逐行确认正确
- registry notes 中"backbone 严重受损"需改为"backbone co-adaptation with token selection"——已指令 Agent 但未确认执行

### 2. 🖥️ 基础设施快照
- 服务器：westd-27271，2× RTX PRO 6000 96GB
- 项目远程路径：execution.project_path（需从 load_project_config 获取具体路径）
- 预置镜像：aml-train（conda 环境，非 venv）
- 本地 workspace：/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/
- 活跃进程：v8.1 训练 PID 121326 on cuda:0（约 33% @ step 9950/30K，~1.8h remaining，sps=3.1）
- cuda:1：v8 re-eval 已完成释放

### 3. 📊 当前状态
刚完成 v8 re-eval（修复后 evaluate.py），结果：G3=1.344x FAIL，G1=50.2x✅ G2=+58.8pp✅ G4=0.0865✅。MVP 未通过。

Registry:
- `mvp_imm_anchor_v8` — ANALYZING，G3=1.344x FAIL（D029）
- `mvp_imm_anchor_v8_1` — RUNNING on cuda:0，λ=0.2 gradient isolation，~1.8h 剩余
- `mvp_baseline_v5` — DONE(success)，clean=0.004063

等待中：
- v8.1 训练完成回调 → 需用修复后 evaluate.py 跑 500-batch final eval
- Agent 正在处理我的最新指令（修正 notes 用词 + v8.1 后续计划）

### 4. 📋 待办
- v8.1 训练完成 → cuda:1 跑 500-batch eval（standard + bypass + pruneTrue）→ 计算 G3
- v8.1 G3 ≤1.10 → MVP PASS → complete_mvp() → 进入 research 阶段（post-mvp-kickoff skill）
- v8.1 G3 在 1.10-1.20 → 考虑 v8.2（更低 λ 或延长训练）
- v8.1 G3 >1.20 → co-adaptation 是根本瓶颈，需换方向。三个候选（Reviewer 建议）：
  1. mask ratio annealing（keep=0.9→0.5 渐进）
  2. two-stage（先训 baseline 到收敛，冻 backbone，再训 ACIS）
  3. distillation（baseline action output 做 KD）
- 用户要求严格检查实验正确性 → 已让 Reviewer 做完全管线审查（PASS，只有 eval bug），后续新实验也要保持这个标准

### 5. 🎯 战略上下文
- 决策链：D021(梯度干扰是根因) → D023(启动 v8 gradient isolation) → D028(eval 5 处 bug) → D029(co-adaptation 是新瓶颈)
- 核心转折：v7 时代的问题是"margin loss 梯度损伤 backbone"（已通过 gradient isolation 解决）；v8 时代的问题是"backbone 在训练时适应了 soft mask 后的稀疏 token 分布"（input distribution shift）——这两个机制完全不同，解法也不同
- IMM 的鲁棒性价值已确认（G1=50x, G2=+59pp），唯一卡点是 clean performance overhead
- 易错点：不要把 bypass ratio (7.12x) 当作 gradient isolation 失败去 debug——这是 co-adaptation 的自然结果，证据是 random 50% pruning (0.017) 也优于 full token (0.029)
- 用户对实验正确性有明确顾虑（"严格检查实验本身是否正确"），后续汇报要附带 Reviewer 验证结论，不要只报 Agent 自查
- 100-batch vs 500-batch 教训：小样本 eval 不可信，所有 MVP 判定必须用 500-batch


---
