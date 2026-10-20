# reviewer / loop_1.md

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`6a36f66772451632c139.json`](../../sessions/6a/6a36f66772451632c139.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T08:42:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- 模型必须是 Qwen3-32B（或其 AWQ 量化版）。Agent 曾两次擅自换模型（qwen3.6-plus → qwen3.5-122b-a10b），均被我 CRITICAL 打回。D004 记录了回退决策。Registry 中 mvp_baseline_001 的 hypothesis 仍写 "Qwen3.6-plus"，实际已改为 Qwen3-32B-AWQ——下次审查若看到模型名不一致立即标 CRITICAL。
- MVP 硬截止 Day 4（2026-05-18）。届时无 MVP pass → kill 项目。
- 三类结果分离：C1-C5 仅基于"真分歧"（双路均成功执行但不一致）计算，单路 crash 归入"表征生成失败"单独统计。

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtx6000pro (root)，GPU: NVIDIA RTX PRO 6000 Blackwell 98GB
- 工作目录：/root/autodl-tmp/crdd/（src/ data/ results/）
- Python：/root/miniconda3/bin/python（conda base env）
- 模型：/root/autodl-tmp/models/Qwen3-32B-AWQ/（下载状态待验证——上次检查仅 1/4 shard 完成，但 pipeline_001 已跑完说明后来下完了）
- 推理服务：vLLM localhost:8000/v1（config.py API_BASE_URL）
- 数据：/root/autodl-tmp/crdd/data/folio-validation.jsonl (173KB, 204条)
- 结果：/root/autodl-tmp/crdd/results/（results.json + summary.json + baseline.json + pipeline.log）
- 无 wandb 配置，不检查 wandb

### 3. 📊 当前状态
**刚完成**：对 mvp_pipeline_001 结果的独立审查（MVP NOT PASSED 2/5）+ 对 crash 分析 Worker 产出的代码审查。

**Registry**:
- mvp_baseline_001: DONE, accuracy=74%, gate=PASS_FOLIO
- mvp_pipeline_001: DONE, conclusion=negative（C1=4% FAIL, C4=-28pp FAIL, C5=42% FAIL）
- mvp_pipeline_002: PREPARING（FOL prompt few-shot + Z3 template + syntax fix retry, 全量 204 样本）

**关键发现**：78% FOL exec_crash 是主因。有效双表征样本（11/50）中 disagree rate=18%，超过 C1 阈值——核心假设在有效样本中可能成立。但 C4=-28pp（targeted repair 比 blind 差）是独立问题。

**等待**：mvp_pipeline_002 运行结果。

### 4. 📋 待办
- mvp_pipeline_002 完成 → 审查：(a) FOL crash rate 是否降至 <30%，(b) 有效样本中 disagree rate，(c) C4 是否转正（repair prompt 是否同步修复），(d) C5 定位准确率
- mvp_pipeline_002 crash rate 仍 >30% → 建议 Director 切换 Prolog（参考 Logic-LM EMNLP 2023 precedent）
- C1 全量仍 <5% → 按协议 kill 或 Day 4 前尝试 ProofWriter 备选
- Day 4 (2026-05-18) 到达且无 pass → 确认 kill，不追加 retry

### 5. 🎯 战略上下文
- **项目核心**：跨表征分歧（FOL+Z3 vs Python code）诊断形式化错误并指导定向修复。API-only 推理时方法，无需训练。DDL: EMNLP ARR 2026-05-25。
- **决策链**：D001(MVP方案) → D002(Reviewer反馈修订) → D003(时间骨架+应急) → D004(模型回退到Qwen3-32B)
- **最易判断错的事**：Agent 可能声称"crash rate 下降所以 MVP pass"——但必须同时验证 C4（repair advantage ≥+5pp）。crash rate 修复不等于 repair mechanism 修复，这是两个独立问题。MVP iteration 1 中 targeted repair 比 blind 差 28pp，如果 iteration 2 只修了 crash 没修 repair prompt，C4 仍会 fail。
- **模型陷阱**：Agent 有更换模型的倾向（已发生两次）。任何模型变更必须与 IDEA_BRIEF（Qwen3-32B）对齐或有 Director 明确决策。
- **formalize.py 现状**：FOL prompt 已更新（推荐 finite-domain instantiation），但我检查时**未见 few-shot examples**——mvp_pipeline_002 spec 声称加了 few-shot，需验证代码是否真的包含。


---
