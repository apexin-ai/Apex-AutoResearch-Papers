# director / loop_3.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`4246c6e06b2cd158417f.json`](../../sessions/42/4246c6e06b2cd158417f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-15T23:09:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-27271 的 cuda:0 和 cuda:1（2× RTX PRO 6000 96GB）
- G3a (bypass-ACIS clean action_loss ratio ≤ 1.10) 是 MVP gate，不可再放宽——v7.2 的 1.91x 已确认梯度共享是真实的权重损伤
- 所有 eval metrics 必须引用 JSON 文件原始值，禁止手算/近似（D014 教训）
- dry-run 必须同时覆盖 train + eval 两种模式（D006）
- evaluate.py baseline 路径必须正确应用扰动/剪枝——v5 曾出过 imm_enabled=False 跳过的 bug（D011）

### 2. 🖥️ 基础设施快照
- 服务器：westd-27271 (connect.westd.seetacloud.com), root
- 工作目录：/root/autodl-tmp/importance_margin_vla_compress
- Python/Conda：未明确记录，Agent 连接后探测（可能是 aml-train 镜像 conda base）
- 模型：SmolVLA + LoRA（lerobot 框架）
- 数据集：aloha_sim_insertion（D005 从 LIBERO 换过来的）
- W&B：未配置
- 活跃进程：无（当前无 RUNNING 实验）

### 3. 📊 当前状态
- **刚做完**：v7.2 (λ=0.2) 全量 eval 确认 G3a=1.91x FAIL（D021/D022），与 v7 (λ=0.5, G3=3.28x) 一起确认梯度共享是根因
- **正在做**：Agent 正在实现 v8 dual detach（stop-gradient）代码，mvp_imm_anchor_v8 处于 PREPARING 状态
- **Registry**: 14 个实验，13 DONE（1 success baseline_v5, 1 negative v7.2, 10 failed earlier iterations, 1 killed），1 待处理 v8
- **等待中**：Agent 完成 v8 代码实现 → 需要 dry-run → 审批 → 训练

### 4. 📋 待办（条件触发式）
- Agent 报告 v8 代码就绪 → 要求 dry-run（train + eval 两模式）→ 审批 → allocate cuda:0 启动训练
- v8 step 2K early eval 出来 → 检查 G3a 趋势（bypass-ACIS ratio 是否朝 ≤1.10 收敛）；若 >1.5x 直接 kill
- v8 final eval → 四个 Gate 全判：G1 ≥2x, G2 ≥10pp, G3a ≤1.10, G4 <1.0；全 pass → complete_mvp()
- v8 仍 G3 FAIL → 需要决策：(a) two-stage training (先 action-only 再 freeze LoRA + train ACIS) 即 v8b，(b) 考虑 IMM 核心假设是否需要 pivot（ACIS 在 detached features 上可能学不到足够大 margins）
- v8 如果 G1/G2 大幅下降（detach 导致 ACIS 梯度信号不足）→ 考虑 partial detach / two-stage 替代方案

### 5. 🎯 战略上下文
- **核心发现**：IMM 的 margin maximization 机制本身有效（G1=64x, G2=+47pp, G4=0.323 全部强 pass），唯一问题是 margin_loss 梯度通过共享 LoRA 损伤 backbone action prediction 能力（G3a=1.91x）
- **v8 是关键赌注**：dual detach 切断梯度流向 LoRA，理论上解决 G3 但可能削弱 ACIS 学习信号（G1/G2 可能下降）——这是 v8 最大风险
- **23 条决策链 D001-D023**：从 D001 MVP 设计 → D005 换数据集 → D006-D009 debug 系列 → D010-D012 eval protocol → D013-D018 Lipschitz/metrics 修复 → D019-D023 G3 拆分+确认梯度共享根因
- **易错点**：不要把 G3a (bypass-ACIS) 和 G3b (soft-mode) / G3c (hard-mode) 混淆——G3a 是 MVP gate（纯权重损伤测试），G3b/G3c 是论文级指标
- **成功率 1/13**：前 10 次 fail 主要是环境/代码 bug 而非假设问题，v7/v7.2 才是真正的假设层面信号


---
