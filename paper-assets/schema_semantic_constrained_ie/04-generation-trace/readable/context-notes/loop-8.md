# director / loop_8.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`ed7d11678ae3d7165fe9.json`](../../sessions/ed/ed7d11678ae3d7165fe9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-17T20:25:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-16980 cuda:0,1 + westd-21461 cuda:0,1（共 4 张 RTX PRO 6000 96GB）
- westd-21461 代码曾被同步操作损坏（M007/M008）：任何跨服务器实验启动前必须 rsync 整个源码目录（不要逐文件同步），同步后验证 `wc -l compiler/type_mask_processor.py` = 796 行
- WikiEvents 实验不做 EE ablation（D043），只做 unconstrained vs full_s1
- Continuation masking v2 是所有 WikiEvents constrained 实验的默认配置（D042）
- 所有 constrained 实验命令必须包含 `--skip_on_error`（M006: Agent 两次遗漏此参数导致 Llama 崩溃）
- 目标 conference main，禁止 fallback 到 Findings（用户明确指示 D040）

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980 (connect.westd.seetacloud.com) + westd-21461 (connect.westd.seetacloud.com)
- 工作目录：`/root/schema_semantic_constrained_ie`（两台服务器相同）
- 模型缓存：HuggingFace 默认路径（Qwen3-8B, Llama-3.1-8B, Mistral-7B-v0.3）
- 数据：`/root/schema_semantic_constrained_ie/data/wikievents/`（train/dev/test.jsonl, 246 docs total）
- Ontology：`ontology_constraints_wikievents.json`（56 event types, 27 entity types, 245 constraints）
- 活跃进程（截至 handoff）：
  - westd-16980:cuda:0 — Qwen constrained full_s1 246 docs（刚启动）
  - westd-16980:cuda:1 — Llama constrained full_s1 246 docs（刚启动）
  - westd-21461:cuda:0 — Mistral unconstrained ~96/246（重启后继续）
  - westd-21461:cuda:1 — 可能在跑 constrained dry-run v2（代码修复后重跑）
- 审稿 C群：`oc_01fc90ae186a4ed432770f7601995139`

### 3. 📊 当前状态
**刚完成**：
- Qwen + Llama unconstrained baselines 全量完成（246 docs）。结果：RoV 74.9%/88.8%, EV 24.0%/10.5%
- Continuation masking v2 突破（10-doc: RoV 59.8%→0%, semantic violations ↓95.8%）
- Paper Agent 完成 §5.4 草稿 + 页数压缩（主体回到 8 页）
- Reviewer 评估 cross-task claim 完成：三层级联 Grammar→RoV→AC 比 RE 更丰富

**正在进行**：
- Qwen + Llama constrained 全量（westd-16980 双卡，预计 1-1.5h）
- Mistral unconstrained ~96/246（westd-21461:cuda:0，预计 ~2h）
- westd-21461 代码修复（type_mask_processor.py 被清空为 0 bytes，正在恢复）
- Paper Agent 可能在处理页数压缩 patch

**Registry**：WikiEvents 实验全部缺 registry 记录（Reviewer M007 发现），需在全量完成后批量注册。已注册的只有 ee_qwen/llama_wikievents_unconstrained。

### 4. 📋 待办（条件触发式）
- Qwen/Llama constrained 全量完成 → 汇报 violation rates (ET/EV/RoV/AC/CF) + F1 → 与 10-doc pilot 对比（RoV 是否保持 0%）→ 如果 argument count ↓>20% 需加 caveat
- Mistral unconstrained 完成 → 汇报结果 → 立即启动 Mistral constrained（westd-21461，确保代码已修复）
- 3 模型 constrained 全部完成 → 批量注册 registry → 派 Paper Agent patch §5.4 全量数字 → 更新 paper_framing.md
- 全量结果确认后 → 更新 Intro/Abstract/Conclusion（cross-task story 升级）→ submit_paper_to_review (Round 6)
- westd-21461 代码修复确认 → 验证 `wc -l` + `grep` → 才能在 21461 启动 constrained

### 5. 🎯 战略上下文
**核心 story**：OntoCoDec 从 RE-specific → task-agnostic IE constraint framework。RE (SciERC+DocRED, 2 models, DR↓42-99%) + EE (WikiEvents, 3 models, semantic violations ↓95.8%) 双任务验证。

**决策链**：D040(conference main) → D041(ACE05→WikiEvents) → D042(continuation v2 默认) → D043(不做 EE ablation)

**易错点**：
1. westd-21461 代码同步已失败两次（M007 遗漏文件，M008 清空文件）。下次同步必须 rsync 整个目录 + 验证。绝不信任 Agent 的 "已同步" 汇报，让 Reviewer 验证。
2. Arg F1 ≈ 0%（zero-shot EE 预期）→ §5.4 不做 F1 impact claim，聚焦 violation reduction。审稿人可能攻击 "practical value"，防线是 mechanism generalization + FT 已证明 high-F1 有效。
3. 10-doc continuation v2 argument count ↓22%。全量结果如果确认，需诚实报告为 precision-completeness tradeoff。
4. 80 个 undefined citations（Paper Agent 报告）— 可能是 bib 缺失旧条目，需在提交前修复。
5. 页数刚好 8 页，后续 patch 数字时不能膨胀。§5.4 用 inline text 不用 table。
6. DDL May 25（8 天），constrained 结果今天到 → 明天论文改写 → May 20 提交审稿 → May 23-24 定稿。时间紧但可行。


---
