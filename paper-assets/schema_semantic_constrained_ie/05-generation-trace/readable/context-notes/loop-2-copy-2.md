# agent / loop_2.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`c23c370dd0e27db7e84c.json`](../../sessions/c2/c23c370dd0e27db7e84c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-14T03:20:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 cuda:0, cuda:1（westd-16980）。即使 Director 指定其他卡也必须 push back
- submit_training_job 命令必须 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 ..."` 包裹，否则 EXIT_CODE=127
- 孤儿进程清理前必须查 registry 所有 RUNNING 实验 PID 入白名单（刚因此误杀了 docred schema 实验）
- DocRED schema-informed 恢复时必须用 `--resume` 参数，不要从头跑（已有部分输出）

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980，root 账户，2× RTX PRO 6000 Blackwell (94GB each)
- 工作目录：`/root/schema_semantic_constrained_ie/`
- Python：`/root/miniconda3/bin/python3` (3.12.3, conda base)
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`
- SciERC 数据：`data/processed_data/test.json` (551 samples)
- DocRED 数据：`data/docred/dev.json` (998 docs)
- 活跃进程：PID 134202 (semantic_only, cuda:0), PID 134593 (full_s1, cuda:1)
- Cron 监控：phase2_scierc_semantic_only + phase2_scierc_full_s1（reconcile 确认均在跑）

### 3. 📊 当前状态
刚处理 mvp_phase0_docred_schema 失败回调（SIGTERM 误杀），已完成：registry 更新、飞书卡片、Director 汇报、memory.md 记录。

**RUNNING**:
- `phase2_scierc_semantic_only` (cuda:0, PID 134202) — semantic-only constrained decoding，验证 DR violation→0% 的同时 F1 损失
- `phase2_scierc_full_s1` (cuda:1, PID 134593) — grammar+semantic 双层约束 S1 单通道

**等待中**:
- Worker `diagnose:mvp_phase0_docred_schema` — 正在检查 DocRED 输出文件完成了多少 docs，回调后确定恢复起点
- Worker `emergency:kill_duplicates_and_assess` — 遗留的紧急清理 Worker
- Phase 2 两个实验的 cron 完成回调

**已完成 (success)**:
- phase2_scierc_grammar_only: rv=0%, et=0%, F1 无损（grammar 层 always-on 无代价）
- phase2_scierc_unconstrained: baseline 确认 entity_f1=0.31, relation_f1=0.08
- phase2_s2_pilot50: DR=0%, relation_f1=0.1008（S2 架构可行，F1 瓶颈在 entity span）

### 4. 📋 待办
- semantic_only 或 full_s1 cron 回调 → 按 on-experiment-done skill 处理（更新 registry + 对比 unconstrained baseline + 汇报 Director）
- diagnose Worker 回调 → 读取 docs_completed，确定 --resume 起点
- Phase 2 SciERC 某实验完成腾出 GPU → 恢复 mvp_phase0_docred_schema（`--resume`，优先级中等）
- semantic_only + full_s1 都完成 → 汇总 Phase 2 SciERC 全矩阵（unconstrained / grammar / semantic / full_s1），对比 F1 损失 vs violation 消除
- S2 bug 修复后 → 启动 phase2_scierc_full_s2（已有 pilot50 验证 DR=0%，需 551 全量）
- Phase 2 SciERC 完成 → 启动 Phase 2 DocRED (grammar_only + full_s1)
- 5/21 前：Cross-model validation (Llama-3.1-8B) if time permits

### 5. 🎯 战略上下文
- **目标**: EMNLP 2026 ARR (5/25 deadline)，AAAI 2027 后备
- **核心 story**: OntoCoDec = 编译 IE ontology schema 为解码时约束，预防 type violations。Grammar 层免费消除 rv/et，Semantic 层消除 DR violations 是核心贡献
- **决策链**: D001(EMNLP ARR 5/25) → D002(SciERC GO) → D003(MVP 通过进入 Research)
- **关键数据点已到位**: grammar_only 零代价消除 rv+et（论文 Claim 1 已证）。semantic_only 和 full_s1 是 Claim 2 的关键——如果 DR→0% 且 F1 损失 <5pp 则 story 完美
- **易错点**:
  - 不要把 S2 pilot50 的 relation_f1=0.1008 和 unconstrained 的 0.0823 直接比——pilot 只有 50 样本，需要全量跑
  - entity span 质量差（F1≈0.29）是 relation F1 低的根因（52.6% FP 是 head+tail 都错），不是 constrained decoding 的问题
  - Phase 2 实验是 retry #2（前两次因 conda 未激活 EXIT_CODE=127），当前运行正常


---
