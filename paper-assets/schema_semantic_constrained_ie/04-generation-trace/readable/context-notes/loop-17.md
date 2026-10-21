# agent / loop_17.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_17.md`
- **Structured JSON:** [`d91a0682aaab846765c0.json`](../../sessions/d9/d91a0682aaab846765c0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_wall_time
updated: '2026-05-17T20:28:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-16980 cuda:0,1 + westd-21461 cuda:0,1。其他 GPU 禁用
- westd-21461 启动任何实验前必须先验证 `wc -l compiler/type_mask_processor.py` = 796 行（此文件曾被截断为 0 bytes）
- 跨服务器代码同步必须 rsync 整个目录，禁止逐文件 scp（D044 硬规则，已有截断事故）
- 所有 constrained 实验命令必须包含 `--skip_on_error`（parsed 可能返回 list 而非 dict）
- WikiEvents 只做 unconstrained vs full_s1，不做 EE ablation（D043）
- Continuation masking v2 是所有 WikiEvents constrained 实验的默认配置（D042）

### 2. 🖥️ 基础设施快照
- **westd-16980**: 工作目录 `/root/schema_semantic_constrained_ie/`，Python 系统默认，HF cache 已有 Qwen3-8B + Llama-3.1-8B-Instruct
- **westd-21461**: 同路径，HF cache 有 Mistral-7B-Instruct-v0.3 + Qwen3-8B（通过 hf-mirror.com 下载，需 `HF_HUB_OFFLINE=1` + 本地路径启动）
- 数据集：`data/wikievents/all.jsonl` (246 docs), `test.jsonl` (20 docs)
- Ontology：`data/wikievents/ontology_constraints_wikievents.json` (56 event types, 27 entity types, 80 roles, 245 constraints)
- 活跃 tmux sessions（最后已知状态，需 SSH 确认）：
  - westd-16980: `qwen_constrained_full` (cuda:0), `llama_constrained_full` (cuda:1) — 启动时 5/246 和 11/246
  - westd-21461: `mistral_restart` (cuda:0, unconstrained ~96/246), `constrained_dryrun_v2` (cuda:1, Qwen dry-run)
- Worker 运行中：`worker_code_wikievents_full_status_check_and_launch_20260517T202659` — 正在检查所有实验状态、收集已完成结果、启动 Mistral constrained

### 3. 📊 当前状态
**刚做完：** Qwen + Llama unconstrained baseline 全量完成并注册 registry（ee_qwen/llama_wikievents_unconstrained, DONE）。Qwen + Llama constrained 全量已在 westd-16980 启动。westd-21461 type_mask_processor.py 修复完成（796 行确认）。

**Registry RUNNING：**
- `ee_qwen_wikievents_constrained` — Qwen3-8B full_s1 × 246 docs, westd-16980:cuda:0
- `ee_llama_wikievents_constrained` — Llama-3.1-8B full_s1 × 246 docs, westd-16980:cuda:1
- Mistral unconstrained 未注册 registry（在 tmux 中跑，~96/246 重启后）

**等待中：**
- Worker `full_status_check_and_launch` 回调 — 会带回所有实验进度 + 已完成的 violation rates + F1，以及可能已启动的 Mistral constrained
- Constrained dry-run v2 结果（westd-21461:cuda:1，验证 continuation masking v2 在修复后代码上的效果）

**Unconstrained baseline 结果（已有）：**

| | Qwen | Llama | Mistral |
|---|---|---|---|
| Parse | 88.6% | 91.9% | 待完成 |
| EV | 24.0% | 10.5% | 待完成 |
| RoV | 74.9% | 88.8% | 待完成 |
| Trigger F1 | 0.118 | 0.057 | 待完成 |

### 4. 📋 待办（条件触发式）
- `full_status_check_and_launch` worker 回调 → 读取结果，注册 Mistral unconstrained 到 registry，汇报 Director 完整三模型表
- Qwen/Llama constrained 完成 → 运行 violation_checker + eval，注册 registry (conclusion+metrics)，对比 unconstrained（EV→0%? RoV→0%?），汇报 Director
- Mistral unconstrained 完成 → 收集 violation rates，注册 registry，启动 Mistral constrained on westd-21461:cuda:0
- Mistral constrained 完成 → 收集结果，完整 3×2 对比表（unconstrained vs constrained × 3 models），汇报 Director
- 全部 6 个实验完成 → 更新 report.md，spawn Worker 写论文 §5.4 Event Extraction section
- Constrained dry-run v2 (20 docs) 完成 → 验证 continuation masking v2 有效性（RoV 应近 0%），如果无效需要 debug

### 5. 🎯 战略上下文
- **目标**：EMNLP 2026 ARR May 25 提交。WikiEvents EE 扩展是 conference main 升级的关键（从 short paper → main paper）
- **核心 story**：OntoCoDec 跨任务泛化 — 同一框架 zero-code 从 RE 切换到 EE，自动编译 KAIROS ontology 为 token-level constraints
- **WikiEvents 特殊性**：tightness=0.33%（348 valid triples / 106K 理论空间），比 SciERC/DocRED 紧得多。RoV 是压倒性主要违规（75-89%），而 RE 中 RV 只有 1-12%。这完美展示 semantic layer 在更复杂 schema 上的价值
- **Continuation masking v2**：解决 EE 中 80 个 role 有 25 个 first-token collision 的问题。10-doc pilot 证明 RoV 从 28.6%→0%。全量是否保持是关键验证点
- **易错点**：
  - westd-21461 的 HF 模型需要 `HF_HUB_OFFLINE=1` + 本地路径（网络不通 HF hub）
  - `parsed` 可能是 list（模型输出 JSON array），必须有 isinstance 守卫
  - Entity F1=0 是 prompt 设计问题（zero-shot 不引导 entity extraction），不是 bug
  - Constrained decoding 比 unconstrained 慢 ~3-5x（每 doc 30-60s vs 5-15s）
- **决策链**：D040(升级main) → D041(WikiEvents替代ACE05) → D042(continuation v2为默认) → D043(不做EE ablation) → D044(rsync整目录)


---
