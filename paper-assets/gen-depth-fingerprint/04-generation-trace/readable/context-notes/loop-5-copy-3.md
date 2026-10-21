# reviewer / loop_5.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`0ffc6bd065b647020215.json`](../../sessions/0f/0ffc6bd065b647020215.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-15T22:06:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 `gpu_ids` 白名单配置（constraints.yaml 未创建），但当前 4 张 5090 全部被占用，新实验必须等 GPU 释放
- Registry spec 模型名不一致已报告但未修：`review-sampling-ablation` spec 写 Pythia-2.8B，实际数据是 Qwen3-1.7B
- 论文 binary F1 的 primary metric 是 **gen-1 vs gen-2+**（排除 gen-0），不是 gen-0 vs gen-2+。审查新实验时务必核对用的是哪个定义
- `artifacts/_project/paper/` 和 `docs/paper/` 是两份副本，审查 paper 变更时**两边都要查**，不要只看一边就下结论

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-5090`（root），代码根目录 `/root/gen-depth-fingerprint`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/`
- 模型路径：`/root/autodl-tmp/models/`（pythia-410m/1b/2.8b, olmo-2-1b, qwen3-0.6b/1.7b/8b）
- 数据路径：`/root/gen-depth-fingerprint/data/`，结果：`/root/gen-depth-fingerprint/results/`
- 无 W&B 配置（不检查 W&B）
- 活跃进程（截至 handoff）：
  - PID 234066 cuda:0 — plan-008 multi-domain seeds（news+scientific done, creative ~70%）
  - PID 246026 cuda:1 — plan-006 paraphrastic chains（generate 阶段，ETA ~2h total）
  - PID 241983 cuda:2 — plan-007 cross-model shard 0（depth 3/4，ETA ~60min from 21:23 UTC）
  - PID 242210 cuda:3 — plan-007 cross-model shard 1（同上）

### 3. 📊 当前状态
**刚完成的审查**：
- plan-010 human-edit 实验完成，结果已验证（baseline F1=0.789, random 5-20% graceful degradation, llm_rephrase binary F1 降 6.3pp）。Registry 仍显示 RUNNING，需 Agent 更新为 DONE
- consistency audit 发现 **CRITICAL**：results.tex 5-gen→6-gen 改进写 +1.1pp，registry 实际是 +0.83pp；table2.tex surface-only 组误含 entropy_min。已报告 Director
- bib audit 第二轮：`model_collapse_avoidable` venue 应为 COLM 2024（非 ICML），已报告
- plan-007 eval-fix 已确认修复 binary F1 指标定义
- plan-006 paraphrastic chains 刚启动，flagged repetition_penalty=1.3 confound

**Registry RUNNING**：
- `plan-008-multi-domain` — multi-domain seeds generation+extract+evaluate，cuda:0
- `plan-007-cross-model` — cross-model chains generation，cuda:2/3
- `plan-010-human-edit` — **实际已完成但 registry 未更新**

### 4. 📋 待办（条件触发式）
- plan-007 generation 完成 → 核实 extract + evaluate 阶段启动，验证 gen-1 vs gen-2+ binary F1 是否正确计算
- plan-008 multi-domain 完成 → 核实 dedup 是否运行（之前 3 重复进程导致数据重复，dedup_generations.py 已创建但未执行），验证结果数字
- plan-006 paraphrastic 完成 → 核查 continuation vs paraphrase 对比结论，关注 repetition_penalty confound 是否影响结论
- consistency audit 修复 worker 完成 → 重新核对 5-gen/6-gen 数字链（0.802→0.810, +0.8pp）和 table2 surface feature 分组
- plan-010 registry 更新 → 确认 metrics 和 conclusion 写入正确

### 5. 🎯 战略上下文
- **核心贡献**：7 个分布特征（5 reference + 2 surface）可区分 gen-0/gen-1/gen-2+，6-gen LOGO F1=0.789，binary F1=0.723
- **关键限定**：仅 base model generators（instruct 模型 depth signal 退化严重）；sampling robustness 仅限 moderate variation（高温 T=1.0 崩溃）；llm_rephrase 保住 3-class 但损 binary
- **最容易判断错的事**：
  1. Qwen3-0.6B instruct 的 partial ρ 值在 registry 中找不到支撑（之前报过 WARNING），如果论文仍保留这些数字要追问来源
  2. plan-008 multi-domain 数据可能仍有重复（之前 3 进程同写一个文件），必须确认 dedup 已执行再信任结果
  3. "robust" 的定义在不同实验中不一致——sampling ablation 说 robust=false，human_edit 说 llm_rephrase_robust=true，但后者 binary F1 降了 6.3pp。论文 robustness claim 需要仔细限定


---
