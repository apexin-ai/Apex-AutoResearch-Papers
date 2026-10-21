# reviewer / loop_3.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`d1d0b8774c827e966363.json`](../../sessions/d1/d1d0b8774c827e966363.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T06:00:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `westd-16980`，GPU 0/1 分别跑 DocRED grammar_only 和 full_s1，**不得 kill 这两个进程**
- 输出文件名为 `docred_grammar_only.jsonl` 和 `docred_full_s1.jsonl`（不在子目录里，直接在 `/root/schema_semantic_constrained_ie/outputs/`）
- `ssh_read_only` 不支持 `|`（pipe）和 `>`（redirect），用独立 grep 命令
- Section 4 用 "grammar-first fallback"（不是 "invariant"），Section 3 用 "engineering robustness mechanism"（不是 "formal guarantee"）——这是经审查确认的措辞规范

### 2. 🖥️ 基础设施快照
- 服务器：`westd-16980(root)`，代码根 `/root/schema_semantic_constrained_ie`
- 模型：Qwen3-8B（主实验），Llama-3.1-8B-Instruct（cross-model 已 dry-run 通过，未正式跑）
- 数据集：SciERC 551 samples（Phase 2 全部 DONE），DocRED 998 docs（Phase 2 进行中）
- GPU 0: DocRED grammar_only，85% util，600/998 完成
- GPU 1: DocRED full_s1，84% util，461/998 完成
- 本地 artifacts：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/`
- 无 wandb 配置，不检查 W&B

### 3. 📊 当前状态
**刚完成的审查轮次**（本 Loop 审查了 6 个 section draft + 多项修复）：
- `section4_composition_draft.tex` — PASS（warning: "S(t) defined only over G(t)" 不精确，已报）
- `section5_scierc_draft.tex` — WARNING（Evaluate-for 遗漏 + "not statistically significant" 无检验证据）
- `section6_related_work.tex` — 初版 CRITICAL（9 must-cite 缺失）→ 修订版 PASS
- `section1_introduction_draft.tex` — WARNING → 修复版已确认（62% 歧义、CF trade-off 披露等）
- `section3_method_draft.tex` — WARNING → 修复版已确认（head type masking fallback、decidability 去重）
- Llama cross-model prep — 代码修改已验证（`_chat_template_kwargs` 替换硬编码 `enable_thinking=False`）
- Reference audit — 4 篇可疑引用全部验证真实

**Registry RUNNING**：
- `phase2_docred_grammar_only` — 600/998
- `phase2_docred_full_s1` — 461/998（含 τ_g 预检查修复，0 次 assertion fallback）

### 4. 📋 待办
- DocRED grammar_only 完成 → 核对 DR/RV/ET 数字，对比 SciERC grammar_only 模式
- DocRED full_s1 完成 → **重点审查**：(a) DR 降幅是否接近 SciERC 的 94%，(b) CF 率，(c) fallback 触发计数（需加 counter 或 grep 验证），(d) cross-dataset Table 4 的 TBD 填充是否准确
- Section 3 第 143 行 "triggers once (0.1%)" → DocRED 完成后验证此声明（目前无计量证据，已报 warning）
- Section 5 "not statistically significant" → 确认是否跑了 bootstrap CI，未跑则要求改措辞
- Section 4 "S(t) is defined only over G(t)" → 确认是否已修正为 "takes effect only within"

### 5. 🎯 战略上下文
**核心结论链**：
- D007: S2 无优势，降级为 ablation，S1 为主配置
- Core claim: DR 15.37→0.93% (↓94%) at zero F1 cost（F1-neutral，不是 improvement）
- CF 从 0.08→9.90% 是 semantic layer 引入的 trade-off，**必须在 intro 和 discussion 中诚实披露**
- Enabling dependency = grammar 是 semantic 的前提条件（不是 synergy/amplification）

**易错点**：
1. **不要说 "statistically significant"**——没跑 bootstrap CI，只能说 "within noise"
2. **不要说 "guaranteed"**——用 "near-complete"（0.93% 残留）
3. **DocRED 数据还没出来**——任何 cross-dataset generalization claim 都是 premature
4. **τ_g 预检查没有 logging**——`_apply_type_mask` 中 `any_allowed_valid=False` 时静默 return，无法统计触发次数。Section 3 第 143 行的 "triggers once" 声明无证据支撑
5. **literature_map.yaml 有 16 篇 must-cite**——Related Work 已全覆盖，但新增段落的 bib key 需确保 .bib 文件中有对应条目


---
