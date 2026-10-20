# reviewer / loop_1.md

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`36398c5559b6e4e9b290.json`](../../sessions/36/36398c5559b6e4e9b290.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T08:31:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 cuda:0-3（constraints.yaml C001）。训练/评测进程必须在此范围内，越界立即 CRITICAL
- 轨迹收集进程 PID 11045 正在运行，不要 kill 或干扰
- API endpoint `http://47.94.22.126/v1` 余额有限，不要发起非必要 API 调用
- `&lt;injection_detected>` 标签策略尚未由 Director 决策，不要擅自改动 `_serialize_record()` 中的 recovery observation 格式

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090（root），工作目录 `/root/autodl-tmp/tax_error_inject_agent`
- Python：`/root/miniconda3/bin/python`（conda base 环境），PyTorch 2.10.0+cu128
- 模型：Qwen3-8B 已下载完成（路径未确认，需 SSH 查）
- 数据：`data/trajectories/successful_trajectories.jsonl`（收集中，~122/500）、`data/trajectories/failed_trajectories.jsonl`（~37 条）
- 注入 dry-run 输出：`data/injected_dryrun/injected_variants.jsonl`（96 条，旧格式）
- SFT dry-run：`data/sft_dryrun_taxei.jsonl` + `sft_dryrun_vanilla.jsonl`（修复前旧版，两文件相同，待重跑）
- 活跃进程：PID 11045（轨迹收集，nohup，日志 `/tmp/collect_500.log`）
- 第二台服务器 gpu-5090-4x-3 存在但本阶段未使用

### 3. 📊 当前状态
- **刚完成审查**：`fix-injection-format` 和 `fix-formatter-field` 两个 worker。核心格式兼容 bug 已修复（`_serialize_record()` 转换层 + formatter 双字段名），但修复后未重跑 dry-run 验证
- **Registry RUNNING**：`traj_collect_500`（GPT-5.2 收集 500 条成功轨迹，~122/500，成功率 ~76%，预计还需 ~3-4h）
- **等待 Director 决策**：`&lt;injection_detected>` 标签是否替换为真实 observation（training-eval 分布不匹配问题）
- **等待 Worker**：dry-run 重跑验证（确认 TaxEI 和 vanilla SFT 文件行数不同）

### 4. 📋 待办
- `traj_collect_500` 完成通知到达 → 验证 500 条质量 + 任务类型分布（重点关注 pick_clean ≥30 条）+ 确认 token 长度分布
- dry-run 重跑验证通知到达 → 检查 TaxEI SFT 行数 > vanilla SFT 行数，抽检注入数据格式
- 注入 pipeline 正式运行完成 → Gate 1 审查：注入合法率 ≥80%
- recovery demo 生成完成 → Gate 2 审查：抽检 60 条质量 ≥75%
- SFT 训练启动 → **立即核对 GPU 在 cuda:0-3 范围内**（L1 红线 #4，nvidia-smi 独立验证）
- 评测完成 → Gate 3（TaxEI vs vanilla +5pp, McNemar p<0.05）+ Gate 4（clean task 回归 <2pp）

### 5. 🎯 战略上下文
- **核心科学问题**：taxonomy-guided injection 能否从 tool error（PALADIN 已验证）迁移到 planning/context error。MVP 用 4 个算子（P1/P2/C1/C4）在 ALFWorld 上验证
- **关键数据偏差**：GPT-5.2 在 clean（50%）和 cool（60%）任务上成功率远低于 simple（94%），训练数据系统性偏向简单任务。不影响 TaxEI vs vanilla 对照公平性，但论文必须报告 per-type 分布，eval 结果需按任务类型分解
- **易错点 1**：formatter.py 的 `task_desc` vs `task_description` 字段问题已修复，但 boilerplate "I'll help with this task" 现在会加到所有轨迹上——如果有人质疑这个冗余首轮，需要知道这是为了原始/注入数据格式一致性做的 tradeoff
- **易错点 2**：verl-agent 无显式 plan state，P1/P2 注入的是 "corrupted history" 而非 "corrupted plan"——论文写作时必须用前者表述
- **易错点 3**：注入步范围固定在 2-6（margin=2），只覆盖早期轨迹。MVP 可接受但 full study 需扩展。不要误认为覆盖了全轨迹
- **决策链**：Teacher 从 GPT-4o 改为 GPT-5.2（API endpoint 限制）→ 已记录在 ROADMAP 关键风险 #3


---
