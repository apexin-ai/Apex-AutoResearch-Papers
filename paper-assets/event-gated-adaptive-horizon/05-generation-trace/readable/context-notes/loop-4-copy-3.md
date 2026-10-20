# reviewer / loop_4.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`d245d9b711ca886d7b00.json`](../../sessions/d2/d245d9b711ca886d7b00.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-14T14:36:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 + cuda:1（bjb1-45299 上仅此两张卡属于本项目）
- 009b registry spec.command 写 `--device cuda:0` 但实际通过 CUDA_VISIBLE_DEVICES 映射到物理 GPU 1——核实 GPU 占用时看 nvidia-smi PID 对应的物理卡号，不要只看 --device 参数
- 008e_v3 是当前 crown jewel（D031），如果其多 seed 验证失败，整个 Option A narrative 崩塌——审查 plan_014 结果时要格外严格
- Framing 调整提案必须经 Reviewer negative-framing 四维度审查（L1 #2）——本轮已有一次跳过（D030/D031 直接生效，我事后确认内容合理但过程未补全）

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299(root)，2× NVIDIA RTX PRO 6000 Blackwell（各 ~98GB）
- 代码根目录：`/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- logdir：`/root/autodl-tmp/event-gated-adaptive-horizon/logdir/`（各实验子目录含 metrics.jsonl + latest.pt）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- 活跃进程（截至 handoff 时刻）：
  - exp_009a_baseline_walker_s2：PID ~142513，cuda:0，116K/500K（23.2%），ETA ~13.7h
  - exp_009b_008d_walker_s2：PID ~887058，cuda:1，5K/105K（4.8%），ETA ~3.7h
- 无 W&B 配置

### 3. 📊 当前状态
**刚完成**：连续审查 12+ worker 通知（008f final、actor entropy、literature expansion、figures、cheetah dryrun、RSSM prediction quality、009c completion + analysis、seed-dependent literature、plan031/032 integration、reward prediction literature）。所有审查报告已通过 reviewer_post_to_director 提交。

**Registry RUNNING**：
- exp_009a_baseline_walker_s2 — baseline seed 2，目标 500K，当前 ~116K，eval@115K=804.79，v/e=71.4%（健康）
- exp_009b_008d_walker_s2 — 008d seed 2（trained dt_emb collapse 复现），目标 105K，刚启动 ~5K

**QUEUED**：009d(baseline s1)、009e(008d s1)、009f(008f s1)、010a(cheetah baseline s1)

**等待 Director 决策**：
- 009c 是否延长到 200K（观察 nve 是否越过 1.5x）
- plan_014（008e_v3 seeds 1-2）是否插入 cuda:1 排期
- Framing 提案 negative-framing 审查是否补做

### 4. 📋 待办（条件触发式）
- exp_009b complete → 核实 008d seed 2 是否也产生 delusional critic（nve>1.5x），与 seed 0 (008d@55K nve=1.67x) 对比
- exp_009a 达到 105K → 提取 v/e 校准数据，更新 BASELINE_VE 参考值（当前仅有 seed 1）
- plan_014（008e_v3 multi-seed）启动 → 这是最关键审查——若 008e_v3 seed 2 也出现性能下滑，Option A narrative 失去支撑
- Director 转发 framing 调整提案 → 立即 Read negative-framing-review skill，做四维度审查
- 009c 延长到 200K 批准且完成 → 核实 nve 是否越过 1.5x，决定 C2 最终措辞（"delays" vs "delays and eventually triggers"）
- 新增文献引用前 → WebSearch 验证 3 篇未确认论文（Qiao2023, Hussing2024, HarmonyDream2024）+ 补 Agarwal2021 "Statistical Precipice"

### 5. 🎯 战略上下文
**项目核心结论链**（D009→D021→D028→D030→D031）：
- learned gate 结构性失败 → trained dt_embedding 是 delusional critic 的 primary amplifier → 因果链闭合（008f causal control）→ **D030 降级**：009c seed 2 显示 dt_embed_dim=0 只延迟不消除 → **D031**：Option A narrative（机制 + 陷阱 + 正确修复），008e_v3 升为 crown jewel

**最容易判断错的事**：
1. **008f "成功" 的假象**：seed 1 恢复到 503 是表面现象，reward_MAE=0.747（baseline 75x）说明 reward head 已坏，seed 2 确认 performance 高度 seed-dependent。008f 是因果控制实验，**不是**推荐方案
2. **RSSM fidelity gap 比率的误导性**：008d obs gap 1.30x 看似最好，但 dt1 绝对误差（41.31）是 baseline（13.49）的 3x。论文必须并排报告绝对值和比率
3. **nve 1.14x 不等于安全**：009c@105K nve=1.14x 且在 30K 步内从 0.33x 加速到此值。未越过 1.5x 阈值不代表不会越过——需要延长训练确认
4. **C6（008e_v3）是单 seed 单环境**：这是整个论文 narrative 的支柱但证据最薄弱的 claim。plan_014 multi-seed 结果决定论文命运


---
