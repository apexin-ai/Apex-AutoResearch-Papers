# director / loop_1.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`9ac8e4ca2a4436e3123e.json`](../../sessions/9a/9ac8e4ca2a4436e3123e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-13T21:56:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-16980 的 cuda:0 和 cuda:1，严禁使用其他设备
- 目标会议 EMNLP 2026 ARR，DDL 2026-05-25，用户明确禁止降级到其他会议
- go/no-go metric 只看 domain_range_violation_rate（不是总 violation rate），阈值 5%
- DocRED violation checker 已修复方法论缺陷（vocab vs domain_range 分离），不要回退到旧版合并计算
- S2 PositionDetector bug 未修复前，P008 (full_s2) 不能启动

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980，工作目录 `/root/schema_semantic_constrained_ie/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型：`/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B/`（16GB，5/5 shards）
- 数据集：SciERC 和 DocRED 在项目目录下
- 活跃进程（上次确认）：
  - cuda:0: DocRED schema-informed extraction (P004), PID 116365
  - cuda:1: Phase 2 SciERC sequential (grammar_only→semantic_only→full_s1), PID 123435
- 关键脚本：`run_extraction.py`(SciERC), `run_extraction_docred.py`(DocRED), `run_constrained_extraction.py`(Phase 2, 5 modes), `violation_checker.py`, `violation_checker_docred.py`
- compiler 代码：`compiler/ontology_compiler.py`, `compiler/type_mask_processor.py`, `compiler/tests/test_e2e.py`(12 tests passing)

### 3. 📊 当前状态
刚确认双 GPU 满载运行，Reviewer 最终报告 PASS。

**RUNNING 实验：**
- P004 (DocRED schema-informed, cuda:0) — ~300/998 batches，预计还需 ~2.5h
- P005→P006→P007 (SciERC grammar_only→semantic_only→full_s1, cuda:1) — 顺序执行共享模型加载，预计 3-5h 完成（~May 14 UTC 02:00-04:00）

**已完成：**
- P001: SciERC minimal DR=15.4%（1724 triples）
- P002: SciERC schema-informed DR=5.78%（-62.4%，Evaluate-for +5.8pp 回归）
- P003: DocRED minimal DR=18.7%（16540 triples，vocab=28.9%）

**等待中：** 无 pending Worker 回调，无 cron。Agent 队列空闲。

### 4. 📋 待办
- P005/P006/P007 完成回调 → 分析违规率（应为 0%）+ F1 对比 Phase 0 unconstrained baseline，F1 drop >5pp 是最大风险
- P004 DocRED schema-informed 完成 → 运行 violation_checker_docred.py 分析，更新 experiment_plan.yaml P004 结果
- Phase 2 unconstrained baseline prompt 一致性 → 验证 run_constrained_extraction.py unconstrained 模式与 Phase 0 run_extraction.py 使用相同 prompt template，不一致则修正
- S2 PositionDetector bug 修复 → 修完后启动 P008 (full_s2)，这是 Claim 4 (S1 vs S2) 的唯一证据
- 所有 SciERC Phase 2 完成 → 启动 P009/P010 (DocRED constrained decoding)
- 时间允许 → P012 (Llama-3.1-8B cross-model validation) 缓解单模型 limitation
- May 21 前实验完成 → 启动 Paper Agent 写论文

### 5. 🎯 战略上下文
- **决策链：** D001(目标 EMNLP ARR 5/25) → D002(SciERC DR=15.4% GO) → D003(MVP pass → Research phase)
- **核心发现：** 违规率由 constraint tightness 驱动（非 ontology size）；SciERC 7 rels ≈ DocRED 96 rels 的 D/R violation rate
- **最大风险：** Phase 2 constrained decoding 的 F1 如果比 unconstrained 下降 >5pp，论文降级为 Findings。S2 two-pass 是 mitigation
- **易错点：**
  - experiment_plan.yaml 中 P007 依赖已改为空（可与 P005/P006 并行），但执行上 Agent 选择了串行共享模型加载，这是合理的效率选择
  - Evaluate-for 回归（+5.8pp）已升级为"prior-constraint conflict"框架，这是论文亮点不是弱点
  - "guaranteed 0%" 措辞 Reviewer 建议软化为 "by construction eliminates"，尚未决策
  - DocRED violation checker 旧版有严重方法论缺陷（conflating vocab + domain_range），已修复，不要用旧结果


---
