# reviewer / loop_15.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_15.md`
- **Structured JSON:** [`ca7ac57b238413adb86b.json`](../../sessions/ca/ca7ac57b238413adb86b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-17T20:53:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-16980: cuda:0 = Qwen constrained, cuda:1 = Llama constrained（不得干扰正在运行的实验）
- westd-21461: cuda:1 = Mistral constrained（语义层失效但仍在跑，Director 未回复是否 kill）
- westd-21461:cuda:0 = 空闲，已报告 Director，等指令后方可使用
- Mistral 模型路径含下划线转义：`/root/autodl-tmp/.ms_cache/mistralai/Mistral-7B-Instruct-v0___3/`
- 本项目只有 read-only 权限，不可执行实验/修改文件，只能通过 `reviewer_post_to_director` 输出

### 2. 🖥️ 基础设施快照
- **westd-16980**: `/root/schema_semantic_constrained_ie`
  - Python: `/root/miniconda3/bin/python`
  - Qwen: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`
  - Llama: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`
  - PID 493759 (Qwen constrained, cuda:0), PID 493830 (Llama constrained, cuda:1)
  - 输出: `outputs/wikievents_qwen_constrained_full.jsonl`, `outputs/wikievents_llama_constrained_full.jsonl`
- **westd-21461**: `/root/schema_semantic_constrained_ie`
  - Mistral: `/root/autodl-tmp/.ms_cache/mistralai/Mistral-7B-Instruct-v0___3/`
  - Log: `logs/mistral_constrained_full.log`
  - 输出: `outputs/mistral_constrained_full.jsonl`
- **数据**: `data/wikievents/all.jsonl` (246 docs), `data/wikievents/ontology_constraints_wikievents.json`
- **关键代码**: `compiler/type_mask_processor.py` (796 行), `run_constrained_extraction.py` (1008 行), `violation_checker_wikievents.py` (396 行)

### 3. 📊 当前状态
**刚完成**: 发现并报告 Mistral constrained 语义约束层完全失效（[critical]已发 Director）。同时确认 Qwen/Llama RoV 合规。

**运行中实验进度（~20:50 UTC 快照）**:
- Qwen constrained: 97/246 (39%), ~1.33 doc/min, ETA ~22:30 UTC
- Llama constrained: 121/246 (49%), ~1.61 doc/min, ETA ~22:00 UTC
- Mistral constrained: 15/246 (6%), **语义层失效** — 输出等同 grammar_only

**Unconstrained baselines（全部完成）**:
- Qwen: EV=24.0%, RoV=74.9%, Parse=88.6%, Trigger F1=11.8%
- Llama: EV=10.5%, RoV=88.8%, Parse=91.9%, Trigger F1=5.7%
- Mistral: EV=37.3%, RoV=63.9%, Parse=78.9%, Trigger F1=2.4%

**等待中**: Director 回复 Mistral 处置决策（kill/继续/修复重跑）

### 4. 📋 待办
- Llama constrained 完成 → 运行 violation_checker_wikievents.py 验证 RoV=0%，检查 CF/AC 率，登记 registry
- Qwen constrained 完成 → 同上验证流程
- Director 回复 Mistral 决策 → 若修复重跑，需验证新输出的 RoV 合规性
- 全量实验完成后 → 检查 parse failure rate（预期~30%因 max_new_tokens=4096），推动 max_new_tokens=8192 补充 pass
- 结果注册 registry 后 → 审查 cross-model claim "RoV=0% across all models" 是否成立

### 5. 🎯 战略上下文
- **核心 claim**: OntoCoDec 两层约束（grammar+semantic）在 WikiEvents EE 上实现 EV=0% + RoV=0%
- **Mistral 是唯一阻断点**: Qwen/Llama RoV=0% 已确认，但 Mistral 的 TypeConstraintProcessor 对其 tokenizer 的 continuation masking 失效。根因推测：`_build_role_continuation_tokens` 中 BPE 切分 tokenizer-dependent，Mistral tokenizer 产生不同 subword 导致 mask 未命中
- **CF 22.3% 已知根因**: 模型 hallucination 把 PER/ORG 放入 Place role → grammar 强制 entity_type 为 FAC/GPE → 与 entities[] 冲突。需 Layer 3 TypeConsensusProcessor 扩展到 EE 格式
- **Parse failure 30%**: 全部因 max_new_tokens=4096 截断长文档，非代码 bug。需补充 8192 pass
- **易错点**: 不要把 Mistral 当前输出当作"constrained"结果引用——它实质是 grammar_only。不要假设 Qwen dry-run (20 doc) 的 RoV=0% 自动推广到全量——需等 246 doc violation check 确认


---
