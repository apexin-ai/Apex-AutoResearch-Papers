# feishu dm oc 29920c6324d3f42ddec91e372c2eca18 briefer

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/feishu_dm_oc_29920c6324d3f42ddec91e372c2eca18_briefer.jsonl`
- **Structured JSON:** [`f98bd1da234b52eddd7b.json`](../../sessions/f9/f98bd1da234b52eddd7b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-14T10:58:59.134159+00:00_

[飞书用户 孙震 (ou_9fc1091793795f5e111c3db748a5482e)]: 这篇在讲自迭代过程中，选出其中比较多样性的数据继续训练，可以减缓崩塌这个结论是错的，实际上是加速崩塌。我想问的是前人工作真的有提出这种方式可以减缓崩塌吗？我们是不是在虚空画靶？如果我们的结论是真的，那岂不是前人的数据在造假？这个有好好做过调研吗？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "source": "feishu:oc_29920c6324d3f42ddec91e372c2eca18"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T10:59:11.194044+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T10:59:11.866250+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "ToolSearch",
  "elapsed_ms": 672
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T10:59:14.627898+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "div_cal_verify",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "div_cal_verify",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T10:59:15.301389+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/memory.md\", \"content\": \"# Memory\\n\\n## GPT2-Medium 355M Scaling 关键发现 (2026-05-14)\\n\\n355M 上 RGDS vs Uncurated 排序与 125M **相反**：\\n- 125M: RGDS (74.29) >> Uncurated (47.04) — RGDS 最差\\n- 355M: RGDS (82.84) < Uncurated (91.66) — RGDS 反而优于 Uncurated\\n\\n**原因**：355M 的 baseline collapse 极度严重（Uncurated +245%），50% 数据裁剪的正则化效应足以抵消 alignment gap 损害。\\n\\n**但 C3 仍成立**：RGDS (82.84) > Random 50% (70.25)，alignment gap 相对于同 budget random 仍有害（+18%）。\\n\\n**355M 四方法完整排序 (seed=42)**：Random (70.25) < External (77.74) < RGDS (82.84) < Uncurated (91.66)\\n\\n**论文叙事影响**：不能简单说\\\"RGDS 是最差的\\\"——需要按 scale 区分。核心 claim 应锚定在\\\"同 budget 内 RGDS 劣于 Random\\\"（C3），而非 RGDS vs Uncurated 的绝对排序。\\n\\n## 355M 统计检验方法论 (2026-05-14)\\n\\nBootstrap CI (10000 resamples) 是 2-seed 阶段的主要统计工具（配对 t-test 需 ≥3 seed）。关键发现：\\n- RGDS vs Random-50 (+15.15, CI 排除零) 和 RGDS vs External (+7.90, CI 排除零) 在 2-seed 下已显著\\n- RGDS vs Uncurated (-2.81, CI 含零) 在 355M 不显著——这是 scaling narrative 的统计基础\\n- **不对称 gap 收窄**量化：125M→355M 收窄 57-109%，所有 CI 排除零，是论文 scaling 论证的核心证据\\n\\n## tmux chain 最佳实践 (2026-05-14)\\n\\n**教训**：tmux send-keys 方式不可靠。chain_cuda1 session 退出后 send-keys 无目标，导致 cuda:1 空闲 ~1h。\\n\\n**正确做法**：所有 chain 用单个 bash 脚本串行执行（`script1.sh && script2.sh`），不用 send-keys 追加命令。跨 GPU 调度用 flag 文件 + while loop 等待机制。\\n\\n## 训练超参一致性 (2026-05-13)\\n\\n所有实验（125M 和 355M）使用完全相同的训练超参：lr=5e-5, AdamW, batch=4, grad_accum=8 (effective 32), max_len=512, 3 epochs/gen, 500K tokens/gen。不同方法之间唯一变量是 selection_method。\\n\", \"total_chars\": 1367, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 673
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T10:59:15.301730+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "div_cal_verify"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "div_cal_verify"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T10:59:15.916917+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/ROADMAP.md\", \"content\": \"# div_cal_verify — Research Dashboard\\n\\n> 最后更新: 2026-05-14 07:28 UTC | 更新原因: seed=456 两卡并行部署确认，修正时间线从 02:15→22:30 CST\\n\\n> 最后更新: 2026-05-14 | 更新原因: seed=456 两卡并行部署确认，修正时间线\\n\\n## 核心方向\\n迭代自训练中，模型内部嵌入的几何多样性与内容多样性系统性失对齐（Embedding Alignment Gap），导致基于内部表征的 diversity selection 灾难性加速 model collapse。详见 paper_framing.md (D014 revised)。\\n\\n## 当前进展\\n- **阶段**: Research + 审稿进行中（Group C 独立处理）\\n- **MVP**: PASS (D009)\\n- **Core claims**: C1 (ratio 退化) 强 ✅ | C3 (RGDS > Random 同 budget) 强 ✅ 跨 scale | C2-revised (内部嵌入特异性) 定性强 ✅\\n- **125M 完成**: 4 方法 × 3 seed 完整，3-seed t-test 就绪\\n- **355M 进展**: seed=42 四方法完成 ✅ | seed=123 运行中（2/4完成，2卡并行）| seed=456 脚本就绪+两卡chain部署完毕\\n- **355M seed=42 完整排序**: Random 70.25 < External 77.74 < RGDS 82.84 < Uncurated 91.66 → C3 成立\\n- **Scaling narrative (D020)**: 双假说共存（表征冗余缓冲 + ceiling effect），ratio 作为鉴别指标，已加 limitation 句\\n- **论文写作**: Results 355M + Discussion scaling narrative 已完成（D020 patch）。全文 Provenance 18/19。\\n\\n## 运行中实验\\n| 实验 | GPU | 状态 | 预计完成 |\\n|------|-----|------|----------|\\n| medium_random50_seed123 | cuda:0 | Gen 3/7 训练中 | ~16:15 CST |\\n| medium_external_seed456 | cuda:1 | Gen 0/7 训练中 | ~16:45 CST |\\n\\n## 自动衔接（两卡并行）\\n- cuda:0: random50_seed123 (~16:15) → chain_cuda0_seed456: **uncurated→rgds** (~6-7h → ~22:30 CST)\\n- cuda:1: external_seed456 (~16:45) → chain_cuda1_seed456: **random50** (~3h → ~19:45 CST)\\n- **seed=456 全部完成：~22:30 CST（两卡并行，比单卡串行提前 ~4h）**\\n\\n## 近期任务\\n- [x] seed=456 脚本准备（4 方法 + 2 chain 脚本 + registry 预注册）\\n- [x] seed=456 两卡并行 chain 部署（cuda:0: uncurated→rgds, cuda:1: random50）\\n- [x] Paper Agent Results 355M + Discussion 深化（seed=42 数据）\\n- [x] 因果性语言修正（D017 降级 S3 相关表述）\\n- [x] paper_framing.md 同步：S3 降级 (D017) + External scaling nuance + scaling narrative (D020)\\n- [x] Scaling narrative 定稿：双假说共存框架 (D020)\\n- [ ] seed=123 剩余两方法完成（random50 ~16:15, externa
…[truncated 1939 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 615
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T10:59:15.917289+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "div_cal_verify",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "div_cal_verify",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T10:59:16.541203+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/paper_framing.md\", \"content\": \"# Paper Framing — Embedding Alignment Gap\\n\\n## Target Venue\\nEMNLP 2026 ARR (deadline: May 25, 2026) — Findings full paper (8 pages)\\n\\n## Title (working)\\n\\\"The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training\\\"\\n\\n## Core Insight\\nIn iterative self-training (student-as-generator feedback loop), the geometric diversity of a model's internal embeddings becomes systematically misaligned with content diversity (measured by rare n-gram survival). This \\\"alignment gap\\\" shows an overall declining trend across generations (with a transient early rebound at Gen 1-3 before accelerating decline from Gen 4), causing diversity-based data selection using internal representations to **accelerate** rather than prevent model collapse. All methods that do not rely on degrading internal embeddings — including frozen external embeddings, random selection, and no selection — avoid this catastrophic failure mode.\\n\\n## Core Claims\\n\\n### C1: Alignment Gap Exists and Worsens Progressively\\n- Internal embedding diversity selection ratio degrades from ~1.04 (Gen 0) to ~0.52 (Gen 7)\\n- Overall declining trend with transient early rebound (Gen 1-3: 0.91→0.93→0.94) before accelerating decline from Gen 4\\n- The model increasingly selects vocabulary-poor samples when using its own representations for diversity scoring\\n- Evidence: Phase 2 RGDS selection diagnostics (GPT2-125M, WikiText-103, self-iterate)\\n\\n### C2-revised: The Failure Is Specific to Internal Embeddings (D013/D014/D015)\\n- RGDS is the **only** method showing catastrophic performance degradation\\n- {random_50, external_only, uncurated} form a \\\"normal cluster\\\" (gen7 PPL range: 43-50), while RGDS is a catastrophic outlier (gen7 PPL 75-82)\\n- External selection ratio stabl
…[truncated 10748 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 623
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T10:59:22.666496+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "div_cal_verify",
  "file": "literature_map.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "div_cal_verify",
    "file": "literature_map.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T10:59:23.118949+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'div_cal_verify'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T10:59:23.169517+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "div_cal_verify",
  "file": "decisions.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "div_cal_verify",
    "file": "decisions.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T10:59:23.220608+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/decisions.yaml\", \"content\": \"_next_id: 25\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: MVP 验证方案：3 方法 × 4 代 × WikiText-103，验证 window of advantage 假设\\n  rationale: 核心假设是模型内部表征在迭代训练早期提供优于外部嵌入的多样性信号。MVP 用最小规模（1 数据集、3 方法、4 代）验证此假设是否成立。EMNLP\\n    ARR DDL 仅 13 天，MVP 需在 2-3 天内完成以留出研究和写作时间。选择 WikiText-103 因为它是标准崩塌基准且内容异质性强，预期产生更快崩塌。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 09:59 UTC\\n  summary: 修正 MVP gate：删除 SOFT PASS，二元 PASS/FAIL，N=1 + ≥5% downstream perplexity 相对改善\\n  rationale: Reviewer 指出两个问题：(1) N=1 下 ≥2% 阈值不可靠，提高到 ≥5% 接受 false negative 风险换取速度；(2)\\n    SOFT PASS 与 Human Review Note 第 4 条（删除 dual-outcome hedge）矛盾，统一为二元 gate。如果 RGDS\\n    ≈ RGDS-external-only 则为 FAIL，考虑 pivot 或转 AAAI 2027。主指标明确为 held-out downstream\\n    perplexity 相对改善。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-12 14:41 UTC\\n  summary: 识别 MVP 训练强度不足风险：每代仅 ~250K tokens 对 1.7B 模型几乎无影响，可能导致 PASS(a) 不成立\\n  rationale: Gen 0-2 数据显示 RankMe 仅降 1.7%（983→966）且 gen 2 反弹，k-NN 完全不变（0.991）。每代训练\\n    488×512≈250K tokens 对 1.7B 模型是极轻 fine-tuning。决定：(1) 让当前 3 方法跑完用于对比（~6h）；(2) 如果\\n    3 方法对比均无显著崩塌，立即跑高强度变体（增大生成量到 5-10M tokens/代，多 epoch，或提高 LR）。负 rank correlation\\n    (-0.37~-0.38) 是非预期发现，需进一步分析。\\n  related_experiments:\\n  - exp_id: mvp_rgds_v3\\n    role: evidence\\n    result: 'gen 0-2: RankMe -1.7%, kNN stable 0.991, PPL 16.63→16.35'\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 20:04 UTC\\n  summary: MVP FAIL — 训练强度不足导致前提未触发，启动高强度验证（D003 contingency）\\n  rationale: MVP 结果：RGDS PPL 16.46 vs External-only 16.15，External 反而更优 1.9%，远未达 ≥5%\\n    改善门槛。RankMe 4 代仅降 1.5%（983→968），k-NN 不变（0.991）。根本原因：每代仅 ~250K tokens 对 1.7B 模型影响微乎其微（~0.01\\n    epoch），崩塌前提未被触发。D003 已预判此风险。决定：(1) 快速验证崩塌可诱导：GPT2-125M 极端设置（~2h）；(2) 高强度 Qwen3-1.7B/4B（5M\\n    tokens/gen, 3 epochs）；(3)
…[truncated 10932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T10:59:31.228410+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/related_work_references*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/related_work_references*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T10:59:31.894696+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/artifacts/_project/report/related_work_references.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/artifacts/related_work_references.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "Glob",
  "elapsed_ms": 666
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T10:59:34.812588+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/artifacts/related_work_references.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/artifacts/related_work_references.md"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T10:59:35.472042+00:00_

1	# Related Work References — div_cal_verify
2	
3	> 36 篇经过 WebSearch 验证的引用，覆盖 8 个子领域
4	
5	## 1. Concept Drift / Embedding Drift
6	
7	1. **Lu et al. (2019)** "Learning under Concept Drift: A Review" — *IEEE Transactions on Knowledge and Data Engineering*, Vol. 31, No. 12, pp. 2346–2363
8	   - 作者: Jie Lu, Anjin Liu, Fan Dong, Feng Gu, João Gama, Guangquan Zhang
9	   - 关联: 建立了 drift 检测与适应的分类体系，为理解自训练中嵌入空间几何漂移提供了概念框架
10	
11	2. **Gama et al. (2014)** "A Survey on Concept Drift Adaptation" — *ACM Computing Surveys*, Vol. 46, No. 4, Article 44
12	   - 作者: João Gama, Indrė Žliobaitė, Albert Bifet, Mykola Pechenizkiy, Abdelhamid Bouchachia
13	   - 关联: 阐述分布漂移下决策边界退化的机制，为嵌入表征在自训练伪标签分布漂移时的失对齐提供理论基础
14	
15	3. **Caccia et al. (2022)** "New Insights on Reducing Abrupt Representation Change in Online Continual Learning" — *ICLR 2022*
16	   - 作者: Lucas Caccia, Rahaf Aljundi, Nader Asadi, Tinne Tuytelaars, Joëlle Pineau, Eugene Belilovsky
17	   - 关联: 直接量化了序贯训练中内部表征的突变幅度，其度量框架与自训练循环中嵌入对齐间隙的观测高度类似
18	
19	4. **Davari et al. (2022)** "Probing Representation Forgetting in Supervised and Unsupervised Continual Learning" — *CVPR 2022*, pp. 16712–16721
20	   - 作者: MohammadReza Davari, Nader Asadi, Sudhir Mudur, Rahaf Aljundi, Eugene Belilovsky
21	   - 关联: 表明表征层面的遗忘和漂移独立于任务性能衰退，与本文发现的嵌入几何多样性与语义内容多样性脱耦现象直接对应
22	
23	## 2. Active Learning under Distribution Shift
24	
25	5. **Ash et al. (2020)** "Deep Batch Active Learning by Diverse, Uncertain Gradient Lower Bounds" — *ICLR 2020*
26	   - 作者: Jordan T. Ash, Chicheng Zhang, Akshay Krishnamurthy, John Langford, Alekh Agarwal
27	   - 关联: BADGE 使用梯度嵌入上的 k-means++ 选择多样性批次——正是本文研究其在表征漂移下失效的嵌入多样性选择机制
28	
29	6. **Kirsch et al. (2019)** "BatchBALD: Efficient and Diverse Batch Acquisition for Deep Bayesian Active Learning" — *NeurIPS 2019*
30	   - 作者: Andreas Kirsch, Joost van Amersfoort, Yarin Gal
31	   - 关联: 通过联合最大化互信息实现多样性批次选择，依赖稳定表征的假设与本文对嵌入漂移的发现形成对照
32	
33	7. **Kothawade et al. (2021)** "SIMILAR: Submodular Information Measures Based Active Learning I
…[truncated 8553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer",
  "tool": "Read",
  "elapsed_ms": 659
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-14T11:00:28.099157+00:00_

这是一个关键的方法论问题。基于我读到的项目文档，以下是事实：

## 前人工作到底说了什么

项目引用的相关文献分两类，但**没有交集**：

1. **数据选择/多样性文献** — SemDeDup (Abbas 2023)、D4 (Tirumala 2023)、DSIR (Xie 2023)、BADGE (Ash 2020)、次模选择 (Wei 2015, Mirzasoleiman 2020) 等。这些方法全部在**静态（非迭代）**场景下工作，证明多样性选择有效。**没有一篇将其应用到迭代自训练场景并声称能减缓崩塌。**

2. **模型崩塌文献** — Shumailov 2024 (Nature)、Alemohammad 2024、Dohmatob 2025 等。这些文献记录了崩塌现象，但**同样没有提出用多样性选择来缓解**。

## 论文实际在打什么靶

从 paper_framing.md 的叙事弧可以看到，论文的逻辑是：

> "迭代自训练导致模型崩塌（已知）→ 多样性数据筛选是一个**自然的缓解思路**（natural mitigation idea）→ 我们发现用内部嵌入做多样性选择反而加速崩塌"

关键词是 **"natural mitigation idea"** — 这是一个**直觉推断**，不是在反驳某篇具体论文的具体实验结论。

## 回答你的三个问题

**1. 前人有没有提出这种方式可以减缓崩塌？**
据我在项目文献列表中看到的 36 篇引用，**没有**。多样性选择文献做的是静态场景，崩塌文献没有测试多样性选择。论文在打的靶是"读者的直觉推断"，不是某篇具体工作的 claim。

**2. 是不是虚空画靶？**
有这个风险。论文的贡献是测试了一个"看似合理但实际没人做过的 extension"并发现它失败。这在学术上叫 **testing a natural hypothesis**，是合法的贡献，但确实弱于反驳一个已发表的具体 claim。如果 framing 写成"前人提出X能减缓崩塌，我们发现不行"，那就是在 misrepresent prior work。

**3. 前人数据在造假吗？**
不存在这个问题。前人的多样性选择方法在**非迭代**设置下确实有效，与本项目的迭代设置是不同场景，两者不矛盾。

## 建议

这个问题的严重程度取决于论文 Related Work 和 Introduction 的措辞。如果论文把"diversity selection reduces collapse"归因到了某些具体前人工作上，那就是虚假引用，需要立刻修正。如果只是说"a natural hypothesis"或"an intuitive approach"，那 framing 本身是诚实的，只是 contribution 力度偏弱。

我只能读项目文档，没有论文最终稿的文字。如果你想确认论文 Intro 中具体怎么描述前人工作的，需要去看 artifacts 目录下的论文源文件，但这个验证操作我这边做不了执行类的事，你可以在官方讨论群里提出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:dm:oc_29920c6324d3f42ddec91e372c2eca18:briefer"
}
```

</details>

---
