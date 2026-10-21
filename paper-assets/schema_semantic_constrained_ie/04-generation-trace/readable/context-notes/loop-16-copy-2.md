# reviewer / loop_16.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_16.md`
- **Structured JSON:** [`7aba769382262d466860.json`](../../sessions/7a/7aba769382262d466860.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-18T01:40:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-16980: [cuda:0, cuda:1]，westd-21461: [cuda:0, cuda:1]。无其他卡可用。
- Qwen retry (PID 502110) 在 westd-16980:cuda:0 仍在运行（238/246），不要 kill。
- Llama 16k retry (PID 507848) 在 westd-16980:cuda:1 刚启动（max_new_tokens=16384），不要 kill。
- Mistral v2 (PID 40830) 在 westd-21461:cuda:0 运行中（209/246），这是修复后代码的唯一有效 Mistral 运行，不要 kill。
- westd-21461 上旧 Mistral 进程（PID 37038, cuda:1）已自然结束，其输出 `mistral_constrained_full.jsonl` 是旧代码结果（RoV=54.8%），仅作 grammar-only baseline 参考。

### 2. 🖥️ 基础设施快照
- westd-16980: `/root/schema_semantic_constrained_ie`，Python: `/root/miniconda3/bin/python`
  - 模型: Qwen `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`，Llama `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`
- westd-21461: `/root/schema_semantic_constrained_ie`，Python: `/root/miniconda3/bin/python`
  - 模型: Mistral `/root/autodl-tmp/.ms_cache/mistralai/Mistral-7B-Instruct-v0___3/`
  - 需 `HF_HUB_OFFLINE=1` 前缀
- 数据: `data/wikievents/all.jsonl` (246 docs)，约束: `data/wikievents/ontology_constraints_wikievents.json`
- 评估脚本: `violation_checker_wikievents.py`（violation rates），`eval_event_extraction.py`（F1）
- 活跃进程：Qwen PID 502110 (cuda:0, 16980)，Llama PID 507848 (cuda:1, 16980)，Mistral PID 40830 (cuda:0, 21461)

### 3. 📊 当前状态
**刚完成：**
- Qwen RoV=0.4% 根因分析 → 确认是旧代码+截断伪影，非系统性问题
- "Win-win" claim 可行性评估 → 推荐 Level 3 分层 claim（RE=non-degradation，EE=format compliance bonus）
- Grammar-only ablation 升级评估 → 推荐 Intro 轻提 + §5.4 保持主体
- D044 Mistral tokenizer fix 独立验证 → 4/4 PASS

**Registry RUNNING：**
- `ee_mistral_wikievents_constrained_v2`: Mistral 修复后 full_s1，209/246 docs
- `ee_mistral_wikievents_constrained`: 已改标为 DONE（旧代码 grammar-only baseline, RoV=54.8%）

**Registry DONE 但需更新：**
- `ee_qwen_wikievents_constrained`: 仍为旧数据（RoV=0.4%），新运行 238/246 未完成
- `ee_llama_wikievents_constrained`: 已更新为 215/246 (87.4%)，RoV=0%。Worker 又启动了 16k retry

### 4. 📋 待办（条件触发式）
- Qwen retry 完成 → 跑 `violation_checker_wikievents.py` + `eval_event_extraction.py` → 验证 RoV 是否归零 → 更新 registry
- Llama 16k retry 完成 → 检查 parse rate 提升幅度（215→?/246）→ 更新 registry
- Mistral v2 完成 → 跑 violation checker → **关键验证**：RoV 是否从 54.8%（旧代码）→ 0%（修复后）→ 更新 registry
- 三模型全部完成 → 交叉验证 "RoV≈0% across all models" claim → 若成立，通知 Director 可以写论文 EE 数据
- 若 Qwen 新运行 RoV 仍 >0% → 深入排查 Qwen tiktoken 特有 edge case

### 5. 🎯 战略上下文
- **核心结论链**：OntoCoDec two-layer constrained decoding 跨任务（RE→EE）泛化验证中。RE 已成熟（SciERC/DocRED，3 模型×多 ablation），EE（WikiEvents）是新战场。
- **D044 是关键决策**：Mistral SentencePiece tokenizer 有 BPE context-dependency bug，修复采用 vocab-wide scan 替代 encode-then-check。修复已验证（dry-run RoV=0%），全量验证中。
- **最易判断错的事**：
  1. Qwen 用 tiktoken（非 SentencePiece），D044 修复不直接影响 Qwen。Qwen RoV=0.4% 的原因是旧 run 截断伪影，不是 tokenizer bug。
  2. --resume 保留旧 docs，不重新处理。Llama 的 215 docs 中有 212 来自旧代码（但 Llama 旧代码 RoV=0%，所以不影响结论）。
  3. 论文 F1 提升（EE 中 entity_f1: 0→18%）的机制是 **format compliance**（约束迫使合法输出格式→evaluation parser 能提取）。**不是** semantic understanding 提升。论文 claim 必须诚实 frame 这个机制，否则审稿人会攻击 overclaiming。推荐 Level 3 claim 措辞（见之前提交的报告）。
  4. 两个 cuda:1 GPU 可能被 Worker 占用做新实验——检查前先看 ps/nvidia-smi，不要假设空闲。


---
