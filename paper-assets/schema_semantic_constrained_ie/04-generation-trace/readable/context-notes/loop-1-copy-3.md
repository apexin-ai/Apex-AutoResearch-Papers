# reviewer / loop_1.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`f1543ccaa01c856b2df7.json`](../../sessions/f1/f1543ccaa01c856b2df7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-13T21:56:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1（westd-16980 仅两张 RTX PRO 6000 96GB）。之前 DocRED 实验有过 spec 写 cuda:0 但实际跑 cuda:1 的不一致，已修正。
- 模型路径：`/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`。旧路径 `/root/autodl-tmp/models/Qwen3-8B/` 已被清理（释放 7.7GB）。不要用旧路径。
- Phase 2 脚本 `run_constrained_extraction.py` 用 `CUDA_VISIBLE_DEVICES=N` 映射后脚本内写 `cuda:0`。审查时注意区分物理 GPU ID 和逻辑 device。
- S2 (full_s2) 模式有已知 bug：TypeConstraintProcessor 的 PositionDetector 不支持 relation-only JSON 格式，dry-run 50% violation 泄漏。**S2 实验数据在 bug 修复前不可信，不能用于论文**。

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980 (root)，工作目录 `/root/schema_semantic_constrained_ie`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 数据集：SciERC `/root/schema_semantic_constrained_ie/data/scierc/test.json`，DocRED `/root/schema_semantic_constrained_ie/data/docred/dev.json`
- 约束文件：`/root/schema_semantic_constrained_ie/ontology_constraints.json`（SciERC 6 types × 7 rels + DocRED 6 types × 96 rels）
- 输出目录：`/root/schema_semantic_constrained_ie/outputs/`
- Phase 2 日志：`/root/schema_semantic_constrained_ie/outputs/phase2_batch.log`
- 无 wandb 配置，不检查 wandb
- 活跃进程（截至 handoff）：
  - PID 116365 — cuda:0, DocRED schema-informed extraction（23.6GB, ~3.7MB output 增长中）
  - PID 123435 — cuda:1, Phase 2 SciERC 顺序执行 grammar_only→semantic_only→full_s1（16.5GB，刚启动 grammar_only）

### 3. 📊 当前状态
**已完成审查并发送报告的 worker：**
- Phase 0：SciERC minimal (DR=15.4%) ✅, SciERC schema-informed (DR=5.78%) ✅, DocRED minimal (DR=18.7%) ✅
- Phase 1 compiler: 24 unit + 12 e2e tests 全通过 ✅
- Phase 2 代码审查: run_constrained_extraction.py 652 行，S1 路径 PASS，S2 路径 WARNING（PositionDetector bug）✅
- Literature survey: 40+ 篇，novelty confirmed，4 篇 citation spot-checked ✅
- ROADMAP 审查: WARNING（cuda:1 空闲 → 已解决；P007 依赖链保守；缺 unconstrained baseline）✅

**正在运行的实验：**
- `mvp_phase0_docred_schema` — DocRED schema-informed, cuda:0, registry RUNNING
- Phase 2 SciERC batch — cuda:1, 3 个实验顺序执行，预计 5/14 02:00-04:00 UTC 完成

**Registry 需更新：** `mvp_phase0_scierc_schema` 仍显示 RUNNING，实际已完成（551/551）

### 4. 📋 待办（条件触发式）
- DocRED schema-informed 完成 → 跑 violation analysis + 与 DocRED minimal 对比（McNemar） → 验证 schema-informed 在 DocRED 上的降 violation 效果 → 更新 C2 evidence
- Phase 2 SciERC grammar_only 完成 → 检查 violation_checker 输出：grammar_only 应消除 JSON 格式错误和 vocab violation，但 D/R violation 应与 unconstrained 相同
- Phase 2 SciERC full_s1 完成 → **核心验证**：D/R violation 是否降至 0%？如果 >0% 说明 TypeConstraintProcessor 有 bug，C3 claim 不成立
- Phase 2 SciERC semantic_only 完成 → 与 grammar_only 对比，确认语义层独立贡献
- S2 bug 修复 worker 完成 → 重新审查 PositionDetector 对 relation-only JSON 的行为 + 要求补 e2e 测试
- Phase 2 全部完成 → 审查 F1 指标：constrained 相比 unconstrained F1 降幅是否 <5pp（最高风险 flag）
- 论文章节提交审查 → 按 §5 写作对抗审查维度执行，注意 C3 "guaranteed 0%" 措辞

### 5. 🎯 战略上下文
- **决策链**：D001（目标 EMNLP ARR 5/25，后备 AAAI 2027）→ D002（SciERC GO）→ D003（MVP 通过，进 Research）
- **论文叙事三层**：violation landscape（Phase 0 完成）→ prompt insufficiency（SciERC 完成，DocRED 进行中）→ guaranteed compliance（Phase 2 关键路径，尚未有数据）
- **最大风险**：Phase 2 constrained decoding 降 F1 >5pp。如果发生，S2 two-pass 是 mitigation 手段——但 S2 有 bug。如果 S1 降 F1 严重且 S2 修不好，论文 story 会很弱。
- **容易判断错的事**：
  1. Phase 0 的 unconstrained baseline 和 Phase 2 的 unconstrained 模式使用**不同 prompt 模板**（Phase 0 用 `run_violation_analysis.py` 的 prompt，Phase 2 用 `run_constrained_extraction.py` 的 `SCIERC_SYSTEM`）。对比必须用 Phase 2 自身的 unconstrained 输出，不能直接引用 Phase 0 数据作为 baseline。
  2. DocRED 的 28.9% relation vocab violation 不是 D/R violation——violation_checker 正确分开计算，D/R violation 只算 valid relation type 的 triples。论文引用时不要混淆。
  3. Dry-run 估算偏差大（DocRED 14.4% vs 全量 18.7%），后续不要信 dry-run 数字写论文。
  4. `experiment_plan.yaml` 的 `read_experiment_plan_with_status` API 返回空——YAML 格式可能与 API 期望不匹配，但文件本身内容完整（12 个实验），直接 Read 文件即可。


---
