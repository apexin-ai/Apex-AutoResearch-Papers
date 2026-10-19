# director / loop_5.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`c44f3c5ff0305b1bc6ec.json`](../../sessions/c4/c44f3c5ff0305b1bc6ec.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-17T17:21:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-13953 的 cuda:0 和 cuda:1，严禁使用其他设备
- Eval 结果只在日志出现 suite 级 `pc_success` 汇总后才报告给用户——之前多次把 per-task 数据误报为 suite 级结论（M001）
- paper_framing.md 当前版本与 v7.2 实际数据矛盾（"without corrupting" 是错的），不要基于当前版本启动正式论文写作（M002）
- Registry 中 v7.2 eval 的 `libero_spatial_sr: 0.76` 是误标（实际 59.4%/61.0%），不可引用

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953 (connect.westb.seetacloud.com)，用户 root
- 代码目录：`/root/acib/`（config.py, acib_policy.py, train_acib.py, eval_acib.py, cross_task_probe.py）
- Checkpoints：`/root/autodl-tmp/` 下各版本目录
  - v7.2: `acib_v7.2_connector_scorer/checkpoint-20000`, `_seed2/checkpoint-20000`
  - v7.3 LoRA: `acib_v73_connector_lora/`（待训练）
  - connector-only: `acib_connector_only/`（待训练）
  - baseline: `lerobot/smolvla_libero`（HF cache）
- 活跃进程：PID 40598 (v7.2 eval α=0.0, cuda:0), PID 44022 (v7.2 eval α=1.0, cuda:1)，约 50-60% 完成，预计 ~3h 后结束
- 无 W&B 配置，无 conda env（直接用系统 Python）

### 3. 📊 当前状态
**v7.2 4-suite eval 在跑**（~50-60% 完成）。libero_spatial 已出 suite 级结果：α=0.0=59.4%(-6.6pp), α=1.0=61.0%(-5.0pp)，MVP gate FAIL。剩余 3 suites (object/goal/libero_10) 预计 ~3h 后出。

**v7.3 connector LoRA 代码全部就绪**（D049），等 GPU 空闲立即启动：
- cuda:0: v7.3 LoRA 训练 (`run_v73_connector_lora.sh`, λ_drift=0.0)
- cuda:1: connector-only ablation (`run_connector_only.sh`)

**已完成的代码准备**：v7.3 LoRA 实现 + eval/probe 兼容性修复 + λ_drift sweep 脚本(fallback) + contrastive_grad_scale 代码(降优先级) + connector-only ablation 代码 + 文献调研 16 篇 → literature_map.yaml + paper_framing.md 初稿

### 4. 📋 待办
- v7.2 eval 完成（cron 回调）→ 记录 4-suite 结果 → 立即启动 v7.3 LoRA + connector-only 并行训练
- v7.3 训练完成（~3h after start）→ Probe A (cos<0.8 + spatial) → α=0.0 sanity (spatial only, 应精确=baseline) → α=1.0 full 4-suite eval
- connector-only 训练完成 → α=0.0 4-suite eval → 判定 connector 是否可 fine-tune
- connector-only 结果出来后：如果也回退 → connector 根本不可碰，LoRA 是唯一出路；如果保持 baseline → 问题在 ACIB losses 的梯度方向
- v7.3 Probe A PASS + α=0.0 = baseline + α=1.0 ≥ 64% → **MVP PASS** → 全面修订 paper_framing.md → 启动 Paper Agent
- v7.3 也 FAIL → 考虑增大 LoRA rank (16/32) 或 scorer 容量增强方案

### 5. 🎯 战略上下文
**项目核心发现链**：v7 joint training 梯度污染(-7.8pp, D038) → v7.1 scorer-only 仅 global bias(D041) → v7.2 connector+scorer spatial conditioning 成功但 connector 极度敏感(0.4% drift→-6.6pp, D046/D048) → v7.3 LoRA 结构性隔离(D049，α=0.0 精确恢复 baseline)

**最易判断错的事**：
1. 不要相信 per-task 中间数据——必须等 `pc_success` suite 级汇总
2. v7.2 的 Probe A 是 PASS 的（cos=0.593 seed2），问题不在 spatial conditioning 而在 connector damage
3. λ_drift sweep 大概率无效（connector 已仅偏移 0.4%，增大 λ 无意义）——LoRA 才是正道
4. literature_map.yaml 中部分论文（DeepVision-VLA 等 2026 年论文）可能是 LLM 幻觉，写 Related Work 前必须 WebSearch 验证 arxiv ID
5. CoRL abstract DDL 5/26（9天），paper DDL 5/29（12天）。v7.3 如果一次通过，时间可行但无余量

**Reviewer 判定框架**（已对齐）：4-suite avg Δ(α=1.0 - α=0.0) ≥ +2pp → Scenario A（强 claim）；-2pp~+2pp → Scenario B（interpretability + efficiency）；≤ -2pp → Scenario C（需 reframe）。v7.3 的 α=0.0 应精确=baseline，所以判定简化为 α=1.0 vs baseline。


---
