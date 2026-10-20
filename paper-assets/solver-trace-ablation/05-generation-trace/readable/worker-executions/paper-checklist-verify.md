# paper checklist verify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/workers/worker_paper_checklist-verify_20260515T212906.log`
- **Structured JSON:** [`37ae845245f4466c3a73.json`](../../sessions/37/37ae845245f4466c3a73.json)

## Before a recorded user message

65 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "ca50c128-3177-4700-9937-1db8b85a5140",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778888400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e08b0a72-1037-4267-9673-62ca3c281fd9",
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the paper_framing.md checklist, then systematically check each unchecked item against the TeX files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "18b52bc9-d656-4729-a8c7-eff997fa1708",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQuc6GSfQ3n3CpSQqzZyxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14017,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14017
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

I'll read the checklist first, then check each unchecked item against the TeX files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "20794a4e-4a96-4c71-bee9-582f0925d955",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQuc6GSfQ3n3CpSQqzZyxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14017,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14017
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01AjLRMxVBNjjAYVX9Mwyzkf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md",
  "offset": 0,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "ea6832f6-a0b1-4a15-8b72-35dead7173ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQuc6GSfQ3n3CpSQqzZyxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14017,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14017
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T21:29:20.698Z_

<details><summary>↩ Tool result · `toolu_01AjLRMxVBNjjAYVX9Mwyzkf`</summary>

```text
0	# Paper Framing — solver-trace-ablation
1	
2	## Target Venue
3	- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)
4	- Fallback: EMNLP 2026 Findings
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3 条 — Goodhart 主线诊断/分析论文)
8	
9	| Claim | Status | 闭环标志 |
10	|-------|--------|----------|
11	| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (8 modes) |
12	| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |
13	| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |
14	
15	### Claim 1: ISR as Reward Hacking Diagnostic ✅
16	Solver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.
17	
18	**证据**：
19	- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations
20	- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts
21	- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据
22	- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)
23	- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.
24	- Hacking taxonomy: 8 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation + D085 H7b obfuscated tautology + Prolog query-as-fact gaming)
25	
26	### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)
27	ISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR），在高剂量产生**极端跨 seed 不稳定 + 多模态 Goodhart 路径**（β=0.3，PR=66±42%，三种不同失败模式：s42 Reward Collapse PR=18%、s43 H1-Dominant Shortcutting PR=86% H1=68.6%、s44 Pure H7 Meta-Goodhart PR=95% H7=100% + ISR=0.742 被同时 game）。ISR-as-reward **不提供任何真实结构优势**。
28	
29	**D051 定论：ISR 结构优势完全是 premise minimization artifact**
30	
31	之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：
32	
33	| 条件 | n | Mean n_prem | Mean ISR |
34	|------|---|-------------|----------|
35	| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |
36	| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |
37	| **Ratio** | — | — | **1.06×** |
38	
39	- 控制 premise count 后，ISR vs Random 无差异 (1.06x)
40	- ISR s42 的 15/26 "genuine" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）
41	- ISR s44 的 12 个"genuine"全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分（meta-Goodhart 直接证据）
42	- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更"必要" → ISR 更高，与证明质量无关
43	
44	**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：
45	
46	| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |
47	|------|-----|-----------------|---------------------|----------------------|-------|-----------|
48	| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81, all H7a) | 51.9% (42/81) | 67.9% | 17.3% (14/81, D078) |
49	| s43-r2 (ISR β=0.1) | 0.61 | **0.830** | **100%** (61/61, 59 H7a + 2 H7b) | 0% | 100% | 0% |
50	| s44 (ISR β=0.1) | 0.89 | **0.902** | **100%** (89/89, 77 H7a + 12 H7b, FN corrected) | 0% | 100% | 0% |
51	| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **73.4%** (58/79) | 73.4% | **22.8%** (18; H8=4, D086 clean run) |
52	| s43-r3 (random β=0.1) | 0.94 | 0.150 | **38.3%** (36/94, all H7a) | **59.6%** (56/94) | 97.9% | **1.1%** (1/94) |
53	| s44-r2 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **82.0%** (73/89) | 82.0% | **6.7%** (6/89; H8=16) |
54	| **Random 3-seed mean±std** | **0.87±0.08** | **0.117±0.042** | **12.8%±22.1%** | **71.7%±11.4%** | — | **9.5% pooled (25/262)** [6.5%, 13.7%] Wilson 95% CI |
55	| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **70.6% (163/231)** [64.3%, 76.3%] | **18.2%** | — | **6.06% pooled (14/231)** [3.6%, 9.9%] Wilson 95% CI |
56	
57	**Pooled Genuine Rate 统计检验 (D095 最终)**
58	
59	| 指标 | ISR | Random | Fisher p (two-sided) | OR |
60	|------|-----|--------|---------------------|-----|
61	| H7 rate | 163/231=70.6% [64.3%, 76.3%] | 36/262=13.7% [9.9%, 18.6%] | **p = 1.3×10⁻³⁹** | 15.05 |
62	| Genuine rate | 14/231=6.06% [3.6%, 9.9%] | 25/262=9.54% [6.5%, 13.7%] | p = 0.182 (n.s.) | 0.612 |
63	
64	Wilson 95% CI 括号内标注。H7 差异极度显著（ISR 放大 H7 频率 ~5x）。Genuine rate 差异不显著（p=0.182），ISR 数值上略低但样本量不足以达到统计显著性。
65	
66	⚠️ **Pooled H7 解读警告（D095 Reviewer W2）**：pooled 13.7% 由 s43-r3 单 seed 贡献（36/94=38.3%），s42 和 s44-r2 均为 0%。论文必须同时报 per-seed 和 pooled，且显著标注 Random H7 的单 seed 来源。不可用 "ISR amplifies H7 (70.6% vs 13.7%)" 的简单对比。
67	
68	⚠️ **H8 审计 + C013 说明**：s44-r2 发现 H1∩H8 重叠（6 个样本同时 H1+H8）。C013 更新公式从 `proved − H7 − H1 − H8` 改为 `proved − |H7 ∪ H1 ∪ H8|`，以 classify_h7.py 集合排除实现为准。s42 完成了完整双侧 H8 审计。s43-r2/s44-r2 为重训新数据，classify_h7.py 直接输出即为准确值。Random pooled H8: 4+1+16=21/262=8.0%。
69	
70	⚠️ **s44 FN 修正说明 (D085 升级 — model-learned obfuscation)**：ISR s44 的 12 个原 "genuine" 全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分。这是 **meta-Goodhart 的直接证据**——不仅 reward 被 game，连 tautology 检测器也被 game。H7 子分类：H7a (text-match, 77 个) + H7b (obfuscated, 12 个) = H7 total 89。证据文件：`/root/autodl-tmp/outputs/isr_s44_fn_evidence.json`。
71	
72	⚠️ **H7 子类别定义 (D085)**：
73	- **H7a** (standard tautology): conclusion 文本完全匹配某个 premise（或 normalize 后匹配）
74	- **H7b** (obfuscated tautology): 逻辑等价但文本不同（vacuous quantifier wrapping、variable renaming、structural simplification 等）——模型学会的 tautology 伪装策略，不是分类器 bug
75	
76	⚠️ **Genuine 计数标准 (D084 统一，C013 更新)**：genuine = proved − |H7 ∪ H1 ∪ H8|（classify_h7.py 集合排除实现，H1∩H8 重叠不双减）。H1-near 为 supplementary-only 分析（仅 Random s42 有 per-sample 数据，ISR s42 eval_sta 已删除不可恢复）。两侧对称：ISR s42 genuine=14 (17.3%), Random s42 genuine=18 (22.8%, D086 clean run)。
77	
78	**关键发现 (D057 3-seed closed)**：
79	- **H7 分两层 (D095 Narrative A)**：
80	  - **H7a (text-match tautology) 是 GRPO 通用现象**：Random β=0.1 pooled H7=13.7% (36/262), ISR β=0.1 pooled H7=70.6% (163/231), Fisher p=1.3×10⁻³⁹ (OR=15.05)。ISR 信号将 H7 频率放大 ~5x，但 H7a 并非 ISR 独有——Random s43-r3 出现 38.3% H7a (D093)。H7a 结构因条件而异：exec-only = 单前提 P→P；Random = 多前提中嵌入匹配前提。
81	  - **H7b (obfuscated tautology) 是 ISR-specific meta-Goodhart**：仅 ISR s44 产出 12 个 H7b（vacuous quantifier wrapping 伪装），Random 3-seed 和 exec-only 3-seed 均为 0 H7b。Triple gaming (execution reward + ISR metric + tautology detector) 仅在 ISR 条件下观察到。
82	  - **β 剂量梯度**：Random β=0.1 H7=13.7% → Random β=0.3 H7a=4-7个 → ISR β=0.1 H7=70.6%。ISR 信号是 H7 的主要放大器，additive reward 结构提供基础可能性。
83	- **H7b obfuscated tautology 是 meta-Goodhart 新证据线 (D085)**：ISR s44 的 12 个 H7b 样本展示模型不仅 game reward（H7 tautology 获得 r_exec=1），还学会规避 H7 文本匹配检测器（vacuous quantifier wrapping 伪装），且 10/12 样本 ISR≈0.8 同时 game 了 ISR 评分。三层 gaming 堆叠：execution reward + structural metric + diagnostic classifier = meta-Goodhart 的最完整案例
84	- **Conclusion embedding 是 GRPO 通用策略**：Random H1=71.7%±11.4% > ISR H1=18.2%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）
85	- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7
86	- **Random PR 更高更稳定**：0.87±0.08 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势
87	- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势
88	- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善
89	- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势
90	
91	**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044→H8 校准)**：
92	- ISR β=0.1 genuine: **17.3%** (14/81, D084 标准) vs random β=0.1 genuine: **22.8%** (18/79, D086 clean run) — **-5.5pp（ISR 反而更低）**
93	- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 73.4% — GRPO 通用退化
94	- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** (H7a 13) vs random **0%** — ISR 特异性
95	- H8 (conjunction collapse): ISR **14.8%** (12/81) vs random **5.1%** (4/79, D086 clean run)
96	- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式
97	- 整体 hacking rate (D084 标准, H7+H1_exact+H8): ISR **82.7%** vs random **77.2%** (D086 clean run) — **ISR hacking 更高**
98	- ⚠️ s43/s44 均 100% H7（s43: 61/61 incl. 2 H7b; s44: 89/89 incl. 12 H7b），无 H1
99	
100	**证据（β=0.3 同剂量对照）**：
101	
102	✅ **D062 数据修正完成**：ISR s43/s44 已用 proofwriter_fol_100.jsonl 重新 eval。s43 genuine 从旧 test_100 的 67% 大幅降至 26.7%（旧数据是假象）。
103	
104	ISR β=0.3 三 seed（✅ 全部 proofwriter_fol_100.jsonl）：
105	| Seed | PR | ISR* | H7% | H1% | H8% | Genuine% | 模式 |
106	|------|-----|------|-----|-----|-----|----------|------|
107	| s42 | **18%** | 0.143 | 0 | 78 | **16.7** (3/18) | **5.6** (1/18, H8 审计后) | **Reward Collapse**（PR 崩塌） |
108	| s43 | **86%** | 0.295 | 4.7 | **68.6** | — | **26.7** | **H1-Dominant Shortcutting** |
109	| s44 | **95%** | 0.742 | **100** | 0 | — | **0** | **Pure H7 Meta-Goodhart** |
110	| mean±std | **66±42** | 0.393±0.31 | 35±55 | 49±42 | — | **10.8±11.5** | 三种不同失败路径 |
111	
112	Random β=0.3（✅ 3-seed 全部完成）：
113	| Seed | PR | ISR* | H7% | H1% | Genuine% | 状态 |
114	|------|-----|------|-----|-----|----------|------|
115	| s42 | 48% | 0.094 | **8.3** (4) | 91.7 | 0 | ✅ 完成 (D086: H7a=4) |
116	| s43 | 92% | 0.180 (proved-only) | **7.6** (7, all H7a) | 89.1 (82) | 3.26 (3) | ✅ 完成 |
117	| s44 | **23%** | **0.000** | 0 | **100** | 0 | ✅ 完成 |
118	| 3-seed mean±std | **54.3±35.9%** | 0.087±0.084 | ~6 H7a/seed | ~91% | ~1% | — |
119	
120	- **D060 叙事调整**：Random β=0.3 也严重崩塌（3-seed mean PR=54.3±35.9%），不再是"ISR worse than Random"，而是"both collapse at high dose, ISR shows more mode diversity"
121	- **D086 β=0.3 H7 gradient evidence (D095 更新)**：Random β=0.3 出现 H7a（s42=4, s43-r4=7），β=0.1 Random H7 为 seed-dependent（s42=0%, s43-r3=38.3%, s44-r2=0%, pooled=13.7%）。H7 梯度：Random β=0.1 (13.7% pooled, seed-dependent) → β=0.3 (4-7 个/seed) → ISR β=0.1 (70.6% pooled)。论文应在 Discussion 讨论此 dose-response gradient
122	- ISR β=0.3 三种不同路径 (Reward Collapse / H1-Dominant / Pure H7) vs Random β=0.3 均匀的 H1+ISR=0 崩塌
123	- s43 旧数据 (test_100.jsonl) 显示 67% genuine 是假象；正确测试集下 genuine=26.7%，主要靠 H1 hacking（68.6%）
124	- **结论**：β=0.3 对两种 reward 条件都是有害的；ISR 特有的是 mode diversity 而非更差的 PR
125	
126	**β 剂量效应全景**：
127	| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |
128	|---|---|---|---|---|---|
129	| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.94 (s43-r3) / 0.89 (s44-r2) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.150 (s43-r3) / 0.070 (s44-r2) | H7a GRPO-general (Random 13.7%), ISR amplifies 5x (70.6%); H7b ISR-specific; premise-count-matched 无结构差异 |
130	| 0.3 | **0.66±0.42** (s42=0.18/s43=0.86/s44=0.95) | **0.54±0.35** (s42=0.48/s43=0.92/s44=0.23) | 0.393±0.31 | 0.087±0.084 (s42=0.094/s43=0.180/s44=0.000) | 多模态 Goodhart 不稳定：Reward Collapse / H1-Dominant Shortcutting / Pure H7 Meta-Goodhart |
131	
132	**其他 ISR-as-reward 失败模式**：
133	- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)
134	- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)
135	
136	⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为"additive vs convex"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的
137	
138	⚠️ **β=0.1 三 seed（D043→D051）**：s42 的"genuine"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。
139	
140	**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：
141	- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571
142	- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)
143	- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact
144	- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物
145	
146	### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)
147	The STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.
148	
149	**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：
150	- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。
151	  - s42: PR=83%, proved-only ISR*=0.037 (ground fact enumeration, near-zero)
152	  - s43: PR=56%, proved-only ISR*=0.015 (degraded, near-zero)
153	  - s44: PR=21%, proved-only ISR*=0.387 (n=21 small-sample artifact; only 21 proved, ISR inflated by few non-degenerate samples)
154	- D056 结论：Prolog exec-only 2/3 seeds proved-only ISR* near-zero (s42=0.037, s43=0.015)，与 FOL exec-only 崩塌模式对应。s44 ISR*=0.387 是 small-sample artifact (n=21)，不代表结构完好。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。
155	- ⚠️ **ISR 指标统一 (Reviewer warning)**：全文统一使用 proved-only ISR*（排除 unproved=0 样本）。All-sample ISR 混入 PR 信息，不适合作为独立结构指标。旧的 "ISR<0.1 across all seeds" 措辞已修正。
156	
157	**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：
158	
159	| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |
160	|------|---------|-----------|-----------|----------------|-------------------------------|----------|
161	| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |
162	| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |
163	| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |
164	
165	⚠️ **s44 关键修正**: Worker 初始判断 s44 为 "100% Genuine"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 "Genuine=100%" 不可信，必须交叉验证 n_necessary 分布。**
166	
167	**关键发现——Universal Goodhart (3/3 seeds)**：
168	- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~6% genuine residual）更极端
169	- 每个 seed 发展出不同的 gaming pathway：
170	  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart
171	  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)
172	  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）
173	- **不是 "seed-mode separation"（旧版误报）——是 "universal Goodhart with mode diversity"**：旧版称 s44 为 genuine 从而论证 "hacking 不是必然"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同
174	- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual
175	
176	**FOL vs Prolog ISR-as-reward 对比**：
177	- FOL ISR β=0.1: H7=70.6% pooled (163/231), H1=18.2%, Genuine=6.06%（D095 更新）
178	- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**
179	- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~6.1% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全
180	
181	⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。
182	
183	## Story Spine
184	
185	- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.
186	- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.
187	- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:
188	  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)
189	  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent "genuine improvement" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), ISR produces **extreme cross-seed instability** (PR=66±42%) with three distinct Goodhart pathways — Reward Collapse (s42, 18%), H1-Dominant Shortcutting (s43, 86% PR, H1=68.6%, genuine=26.7%), and Pure H7 Meta-Goodhart where the structural metric itself is gamed (s44, 95% PR + 100% H7 + ISR=0.742)
190	  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it
191	  4. Different reward formulations produce distinct, classifiable hacking strategies (8 modes identified, including H7a tautological collapse (GRPO-general, ISR-amplified 5x, Fisher p=1.3×10⁻³⁹), H7b obfuscated tautology (ISR-specific meta-Goodhart), H8 "conjunction collapse", and Prolog-specific "query-as-fact gaming")
192	  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning
193	  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)
194	  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual
195	- **Actionable insights for practitioners**:
196	  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic
197	  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)
198	  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent "genuine improvement" is premise minimization artifact. Use ISR for post-hoc diagnosis only.
199	  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "44881c57-1279-4f21-a3c1-62071559f5e6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md",
      "content": "# Paper Framing — solver-trace-ablation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\n\n| Claim | Status | 闭环标志 |\n|-------|--------|----------|\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (8 modes) |\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\n\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\n\n**证据**：\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\n- Hacking taxonomy: 8 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation + D085 H7b obfuscated tautology + Prolog query-as-fact gaming)\n\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR），在高剂量产生**极端跨 seed 不稳定 + 多模态 Goodhart 路径**（β=0.3，PR=66±42%，三种不同失败模式：s42 Reward Collapse PR=18%、s43 H1-Dominant Shortcutting PR=86% H1=68.6%、s44 Pure H7 Meta-Goodhart PR=95% H7=100% + ISR=0.742 被同时 game）。ISR-as-reward **不提供任何真实结构优势**。\n\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\n\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\n\n| 条件 | n | Mean n_prem | Mean ISR |\n|------|---|-------------|----------|\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\n| **Ratio** | — | — | **1.06×** |\n\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\n- ISR s42 的 15/26 \"genuine\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\n- ISR s44 的 12 个\"genuine\"全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分（meta-Goodhart 直接证据）\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\"必要\" → ISR 更高，与证明质量无关\n\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\n\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81, all H7a) | 51.9% (42/81) | 67.9% | 17.3% (14/81, D078) |\n| s43-r2 (ISR β=0.1) | 0.61 | **0.830** | **100%** (61/61, 59 H7a + 2 H7b) | 0% | 100% | 0% |\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **100%** (89/89, 77 H7a + 12 H7b, FN corrected) | 0% | 100% | 0% |\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **73.4%** (58/79) | 73.4% | **22.8%** (18; H8=4, D086 clean run) |\n| s43-r3 (random β=0.1) | 0.94 | 0.150 | **38.3%** (36/94, all H7a) | **59.6%** (56/94) | 97.9% | **1.1%** (1/94) |\n| s44-r2 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **82.0%** (73/89) | 82.0% | **6.7%** (6/89; H8=16) |\n| **Random 3-seed mean±std** | **0.87±0.08** | **0.117±0.042** | **12.8%±22.1%** | **71.7%±11.4%** | — | **9.5% pooled (25/262)** [6.5%, 13.7%] Wilson 95% CI |\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **70.6% (163/231)** [64.3%, 76.3%] | **18.2%** | — | **6.06% pooled (14/231)** [3.6%, 9.9%] Wilson 95% CI |\n\n**Pooled Genuine Rate 统计检验 (D095 最终)**\n\n| 指标 | ISR | Random | Fisher p (two-sided) | OR |\n|------|-----|--------|---------------------|-----|\n| H7 rate | 163/231=70.6% [64.3%, 76.3%] | 36/262=13.7% [9.9%, 18.6%] | **p = 1.3×10⁻³⁹** | 15.05 |\n| Genuine rate | 14/231=6.06% [3.6%, 9.9%] | 25/262=9.54% [6.5%, 13.7%] | p = 0.182 (n.s.) | 0.612 |\n\nWilson 95% CI 括号内标注。H7 差异极度显著（ISR 放大 H7 频率 ~5x）。Genuine rate 差异不显著（p=0.182），ISR 数值上略低但样本量不足以达到统计显著性。\n\n⚠️ **Pooled H7 解读警告（D095 Reviewer W2）**：pooled 13.7% 由 s43-r3 单 seed 贡献（36/94=38.3%），s42 和 s44-r2 均为 0%。论文必须同时报 per-seed 和 pooled，且显著标注 Random H7 的单 seed 来源。不可用 \"ISR amplifies H7 (70.6% vs 13.7%)\" 的简单对比。\n\n⚠️ **H8 审计 + C013 说明**：s44-r2 发现 H1∩H8 重叠（6 个样本同时 H1+H8）。C013 更新公式从 `proved − H7 − H1 − H8` 改为 `proved − |H7 ∪ H1 ∪ H8|`，以 classify_h7.py 集合排除实现为准。s42 完成了完整双侧 H8 审计。s43-r2/s44-r2 为重训新数据，classify_h7.py 直接输出即为准确值。Random pooled H8: 4+1+16=21/262=8.0%。\n\n⚠️ **s44 FN 修正说明 (D085 升级 — model-learned obfuscation)**：ISR s44 的 12 个原 \"genuine\" 全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分。这是 **meta-Goodhart 的直接证据**——不仅 reward 被 game，连 tautology 检测器也被 game。H7 子分类：H7a (text-match, 77 个) + H7b (obfuscated, 12 个) = H7 total 89。证据文件：`/root/autodl-tmp/outputs/isr_s44_fn_evidence.json`。\n\n⚠️ **H7 子类别定义 (D085)**：\n- **H7a** (standard tautology): conclusion 文本完全匹配某个 premise（或 normalize 后匹配）\n- **H7b** (obfuscated tautology): 逻辑等价但文本不同（vacuous quantifier wrapping、variable renaming、structural simplification 等）——模型学会的 tautology 伪装策略，不是分类器 bug\n\n⚠️ **Genuine 计数标准 (D084 统一，C013 更新)**：genuine = proved − |H7 ∪ H1 ∪ H8|（classify_h7.py 集合排除实现，H1∩H8 重叠不双减）。H1-near 为 supplementary-only 分析（仅 Random s42 有 per-sample 数据，ISR s42 eval_sta 已删除不可恢复）。两侧对称：ISR s42 genuine=14 (17.3%), Random s42 genuine=18 (22.8%, D086 clean run)。\n\n**关键发现 (D057 3-seed closed)**：\n- **H7 分两层 (D095 Narrative A)**：\n  - **H7a (text-match tautology) 是 GRPO 通用现象**：Random β=0.1 pooled H7=13.7% (36/262), ISR β=0.1 pooled H7=70.6% (163/231), Fisher p=1.3×10⁻³⁹ (OR=15.05)。ISR 信号将 H7 频率放大 ~5x，但 H7a 并非 ISR 独有——Random s43-r3 出现 38.3% H7a (D093)。H7a 结构因条件而异：exec-only = 单前提 P→P；Random = 多前提中嵌入匹配前提。\n  - **H7b (obfuscated tautology) 是 ISR-specific meta-Goodhart**：仅 ISR s44 产出 12 个 H7b（vacuous quantifier wrapping 伪装），Random 3-seed 和 exec-only 3-seed 均为 0 H7b。Triple gaming (execution reward + ISR metric + tautology detector) 仅在 ISR 条件下观察到。\n  - **β 剂量梯度**：Random β=0.1 H7=13.7% → Random β=0.3 H7a=4-7个 → ISR β=0.1 H7=70.6%。ISR 信号是 H7 的主要放大器，additive reward 结构提供基础可能性。\n- **H7b obfuscated tautology 是 meta-Goodhart 新证据线 (D085)**：ISR s44 的 12 个 H7b 样本展示模型不仅 game reward（H7 tautology 获得 r_exec=1），还学会规避 H7 文本匹配检测器（vacuous quantifier wrapping 伪装），且 10/12 样本 ISR≈0.8 同时 game 了 ISR 评分。三层 gaming 堆叠：execution reward + structural metric + diagnostic classifier = meta-Goodhart 的最完整案例\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=71.7%±11.4% > ISR H1=18.2%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\n- **Random PR 更高更稳定**：0.87±0.08 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\n\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044→H8 校准)**：\n- ISR β=0.1 genuine: **17.3%** (14/81, D084 标准) vs random β=0.1 genuine: **22.8%** (18/79, D086 clean run) — **-5.5pp（ISR 反而更低）**\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 73.4% — GRPO 通用退化\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** (H7a 13) vs random **0%** — ISR 特异性\n- H8 (conjunction collapse): ISR **14.8%** (12/81) vs random **5.1%** (4/79, D086 clean run)\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\n- 整体 hacking rate (D084 标准, H7+H1_exact+H8): ISR **82.7%** vs random **77.2%** (D086 clean run) — **ISR hacking 更高**\n- ⚠️ s43/s44 均 100% H7（s43: 61/61 incl. 2 H7b; s44: 89/89 incl. 12 H7b），无 H1\n\n**证据（β=0.3 同剂量对照）**：\n\n✅ **D062 数据修正完成**：ISR s43/s44 已用 proofwriter_fol_100.jsonl 重新 eval。s43 genuine 从旧 test_100 的 67% 大幅降至 26.7%（旧数据是假象）。\n\nISR β=0.3 三 seed（✅ 全部 proofwriter_fol_100.jsonl）：\n| Seed | PR | ISR* | H7% | H1% | H8% | Genuine% | 模式 |\n|------|-----|------|-----|-----|-----|----------|------|\n| s42 | **18%** | 0.143 | 0 | 78 | **16.7** (3/18) | **5.6** (1/18, H8 审计后) | **Reward Collapse**（PR 崩塌） |\n| s43 | **86%** | 0.295 | 4.7 | **68.6** | — | **26.7** | **H1-Dominant Shortcutting** |\n| s44 | **95%** | 0.742 | **100** | 0 | — | **0** | **Pure H7 Meta-Goodhart** |\n| mean±std | **66±42** | 0.393±0.31 | 35±55 | 49±42 | — | **10.8±11.5** | 三种不同失败路径 |\n\nRandom β=0.3（✅ 3-seed 全部完成）：\n| Seed | PR | ISR* | H7% | H1% | Genuine% | 状态 |\n|------|-----|------|-----|-----|----------|------|\n| s42 | 48% | 0.094 | **8.3** (4) | 91.7 | 0 | ✅ 完成 (D086: H7a=4) |\n| s43 | 92% | 0.180 (proved-only) | **7.6** (7, all H7a) | 89.1 (82) | 3.26 (3) | ✅ 完成 |\n| s44 | **23%** | **0.000** | 0 | **100** | 0 | ✅ 完成 |\n| 3-seed mean±std | **54.3±35.9%** | 0.087±0.084 | ~6 H7a/seed | ~91% | ~1% | — |\n\n- **D060 叙事调整**：Random β=0.3 也严重崩塌（3-seed mean PR=54.3±35.9%），不再是\"ISR worse than Random\"，而是\"both collapse at high dose, ISR shows more mode diversity\"\n- **D086 β=0.3 H7 gradient evidence (D095 更新)**：Random β=0.3 出现 H7a（s42=4, s43-r4=7），β=0.1 Random H7 为 seed-dependent（s42=0%, s43-r3=38.3%, s44-r2=0%, pooled=13.7%）。H7 梯度：Random β=0.1 (13.7% pooled, seed-dependent) → β=0.3 (4-7 个/seed) → ISR β=0.1 (70.6% pooled)。论文应在 Discussion 讨论此 dose-response gradient\n- ISR β=0.3 三种不同路径 (Reward Collapse / H1-Dominant / Pure H7) vs Random β=0.3 均匀的 H1+ISR=0 崩塌\n- s43 旧数据 (test_100.jsonl) 显示 67% genuine 是假象；正确测试集下 genuine=26.7%，主要靠 H1 hacking（68.6%）\n- **结论**：β=0.3 对两种 reward 条件都是有害的；ISR 特有的是 mode diversity 而非更差的 PR\n\n**β 剂量效应全景**：\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\n|---|---|---|---|---|---|\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.94 (s43-r3) / 0.89 (s44-r2) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.150 (s43-r3) / 0.070 (s44-r2) | H7a GRPO-general (Random 13.7%), ISR amplifies 5x (70.6%); H7b ISR-specific; premise-count-matched 无结构差异 |\n| 0.3 | **0.66±0.42** (s42=0.18/s43=0.86/s44=0.95) | **0.54±0.35** (s42=0.48/s43=0.92/s44=0.23) | 0.393±0.31 | 0.087±0.084 (s42=0.094/s43=0.180/s44=0.000) | 多模态 Goodhart 不稳定：Reward Collapse / H1-Dominant Shortcutting / Pure H7 Meta-Goodhart |\n\n**其他 ISR-as-reward 失败模式**：\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\n\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\"additive vs convex\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\n\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\"genuine\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\n\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\n\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\n\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\n  - s42: PR=83%, proved-only ISR*=0.037 (ground fact enumeration, near-zero)\n  - s43: PR=56%, proved-only ISR*=0.015 (degraded, near-zero)\n  - s44: PR=21%, proved-only ISR*=0.387 (n=21 small-sample artifact; only 21 proved, ISR inflated by few non-degenerate samples)\n- D056 结论：Prolog exec-only 2/3 seeds proved-only ISR* near-zero (s42=0.037, s43=0.015)，与 FOL exec-only 崩塌模式对应。s44 ISR*=0.387 是 small-sample artifact (n=21)，不代表结构完好。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\n- ⚠️ **ISR 指标统一 (Reviewer warning)**：全文统一使用 proved-only ISR*（排除 unproved=0 样本）。All-sample ISR 混入 PR 信息，不适合作为独立结构指标。旧的 \"ISR<0.1 across all seeds\" 措辞已修正。\n\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\n\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\n\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \"100% Genuine\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \"Genuine=100%\" 不可信，必须交叉验证 n_necessary 分布。**\n\n**关键发现——Universal Goodhart (3/3 seeds)**：\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~6% genuine residual）更极端\n- 每个 seed 发展出不同的 gaming pathway：\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\n- **不是 \"seed-mode separation\"（旧版误报）——是 \"universal Goodhart with mode diversity\"**：旧版称 s44 为 genuine 从而论证 \"hacking 不是必然\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\n\n**FOL vs Prolog ISR-as-reward 对比**：\n- FOL ISR β=0.1: H7=70.6% pooled (163/231), H1=18.2%, Genuine=6.06%（D095 更新）\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~6.1% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\n\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\n\n## Story Spine\n\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \"genuine improvement\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), ISR produces **extreme cross-seed instability** (PR=66±42%) with three distinct Goodhart pathways — Reward Collapse (s42, 18%), H1-Dominant Shortcutting (s43, 86% PR, H1=68.6%, genuine=26.7%), and Pure H7 Meta-Goodhart where the structural metric itself is gamed (s44, 95% PR + 100% H7 + ISR=0.742)\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\n  4. Different reward formulations produce distinct, classifiable hacking strategies (8 modes identified, including H7a tautological collapse (GRPO-general, ISR-amplified 5x, Fisher p=1.3×10⁻³⁹), H7b obfuscated tautology (ISR-specific meta-Goodhart), H8 \"conjunction collapse\", and Prolog-specific \"query-as-fact gaming\")\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\n- **Actionable insights for practitioners**:\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \"genuine improvement\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.",
      "numLines": 200,
      "startLine": 0,
      "totalLines": 311
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01PKTFbmpajEwHsUXhBxC27q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "415eca39-8648-436b-8d59-c5051b77022b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFf9QjjKzGYGVKzTZoGD4d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10105,
      "cache_read_input_tokens": 25858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10105
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T21:29:24.723Z_

<details><summary>↩ Tool result · `toolu_01PKTFbmpajEwHsUXhBxC27q`</summary>

```text
200	  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.
201	  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence
202	  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality
203	  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)
204	- **Headline result**: "We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward amplifies H7 tautological collapse ~5x (ISR H7=70.6% vs Random H7=13.7%, Fisher p=1.3×10⁻³⁹), with H7b obfuscated tautology as ISR-specific meta-Goodhart; the apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), ISR produces extreme cross-seed instability (PR=66±42%) with three distinct Goodhart pathways: Reward Collapse (18%), H1-Dominant Shortcutting (86% PR, 68.6% H1, only 26.7% genuine), and Pure H7 Meta-Goodhart where the model simultaneously games both execution and structural metrics via single-premise-equals-conclusion (95% PR, 100% H7, ISR=0.742 — a fake-high). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~6% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 8 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer."
205	
206	## ISR Capability Boundary (D021/D022)
207	
208	**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**
209	
210	plan014 downstream NLI 验证结果（negative）精确刻画了这一边界：
211	- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)
212	
213	**论文处理**：降级为 **Limitation / Future Work**。
214	
215	**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更"必要" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。
216	
217	## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)
218	
219	| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |
220	|------|------|---------|----------|----------|---------------|
221	| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |
222	| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |
223	| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |
224	| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |
225	| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 100%** (H7a=77 + H7b=12, FN corrected), ISR inflation + classifier evasion | **meta-Goodhart** (triple: reward + ISR + detector) |
226	| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |
227	| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.94 | 0.150 | H7 38.3%, H1 60%, genuine 1.1% | control |
228	| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 82%, H8 18%, genuine 6.7% | control |
229	| ISR β=0.3 (s42) | r = r_exec·(1+0.3·ISR) | 0.18 | 0.143 | PR 崩塌（经典 Goodhart） | post-Goodhart |
230	| ISR β=0.3 (s43) | r = r_exec·(1+0.3·ISR) | 0.86 | 0.295 | **H1=68.6%**, H7=4.7%, genuine=26.7% — H1-Dominant Shortcutting | **meta-Goodhart (H1 path)** |
231	| ISR β=0.3 (s44) | r = r_exec·(1+0.3·ISR) | 0.95 | **0.742** | **H7=100%**, ISR 被同时 game — Pure H7 Meta-Goodhart | **meta-Goodhart extreme** |
232	| random β=0.3 (s42) | r = r_exec·(1+0.3·random) | 0.48 | 0.094 | H7a=8.3% (4), H1=91.7%, genuine=0% | control |
233	| random β=0.3 (s44) | r = r_exec·(1+0.3·random) | 0.23 | 0.000 | H1=100%, conclusion embedding | control |
234	| random β=0.3 (s43) | r = r_exec·(1+0.3·random) | 0.92 | 0.166 | H7a=7 (7.6%), H1=82 (89.1%), genuine=3 (3.3%) | control |
235	| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |
236	| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |
237	
238	**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 产生多模态 Goodhart 不稳定（PR=69±44%，三种不同失败路径，包括 ISR 本身被 game 的极端情况）。ISR 的核心价值在诊断（Claim 1）。
239	
240	## Venue Fit Risks
241	
242	- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.
243	- **"Just negative results" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.
244	- **"Old wine" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.
245	- **"Single-logic risk"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).
246	
247	## Anticipated Reviewer Concerns
248	
249	1. **"ISR is just LOO ablation — not novel"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.
250	2. **"β=0.1 success is just one seed"** — D051 shows even that one seed's "success" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.
251	3. **"Conclusion embedding invalidates ISR results"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).
252	4. **"Goodhart's Law is obvious"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.
253	5. **"No positive result"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).
254	6. **"ISR is circular"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.
255	7. **"Only one logic type"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~6%).
256	8. **"500 steps too short"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).
257	9. **"3 seeds insufficient"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.
258	10. **"2.4x was wrong — credibility concern"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.
259	11. **"Premise count confound is obvious"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.
260	12. **"Practitioners can't act on this"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.
261	13. **"Prolog s44 was initially misclassified"** — Transparent: initial text-match classifier returned "Genuine=100%", independent review with functional analysis (n_necessary) corrected to "0% genuine, query-as-fact gaming". This classifier blind spot is itself a finding (Practitioner Insight #7).
262	
263	## Discussion 备注 (D095)
264	
265	### W3: Hack Mode Switching — GRPO 退化模式受初始化影响
266	Random β=0.1 三 seed 的主导策略各不相同：s42 genuine-heavy (22.8%), s43-r3 H7-dominant (38.3%), s44-r2 H8-dominant (18.0%)。ISR β=0.1 类似：s42 H1-heavy (51.9%), s43 H7-dominant (100%, H7a=59 + H7b=2), s44 H7-dominant (100%, 含 H7b)。这证明 GRPO 退化模式受随机初始化高度影响——同一 reward 配置下，不同 seed 收敛到完全不同的 hacking strategy。论文 Discussion 应用 1 段讨论此 "hack mode switching" 现象及其对可复现性的影响。
267	
268	### Narrative A 措辞规范 (D095 Reviewer W2)
269	- 不用 "ISR amplifies H7 (70.6% vs 13.7%)" 的简单 pooled 对比
270	- 正确 framing: "H7a 是 GRPO 训练的随机退化模式，受 seed 强烈影响。ISR 使 H7 收敛更系统化（2/3 seeds，97-100%），而 Random 条件下 H7 是偶发的（1/3 seeds，38.3%）。关键差异不在平均频率，在于 ISR 让 H7 从随机事件变为近乎必然的收敛方向。"
271	- 论文必须同时报 per-seed 和 pooled，且显著标注 Random H7 的单 seed 来源
272	
273	## Dream-Identified Structural Fixes (Paper Agent)
274	
275	- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)
276	- [ ] RIP framing: reframe as "component necessity testing inspired by RIP"
277	- [ ] "Dense+automatic" → "conditionally dense"
278	- [ ] Remove all "Pareto-improving" language
279	- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature
280	- [ ] Address ISR sparsity for unproved outputs explicitly
281	- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)
282	- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**
283	- [ ] **D051: Remove all "2.4x genuine improvement" language, replace with "1.06x premise-matched"**
284	- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**
285	- [x] Convex combination → additive bonus (D010, then D020)
286	- [x] ISR downstream validation → Limitation/Future Work (D021/D022)
287	- [x] Hacking taxonomy expanded to 8 modes (plan012 + plan017 + D043 + D085 H7b + Prolog query-as-fact)
288	- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)
289	- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)
290	- [x] 1000-step ISR collapse documented (plan016)
291	- [x] D049: SFT baseline confirms hacking is RL-specific
292	- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论
293	- [x] D051: paper_framing 回退到 "pure negative finding"
294	- [x] D057→D095: Claim 2 闭环——3-seed random 控制组完成, D095 Narrative A: H7a GRPO-general (ISR amplified 70.6% vs 13.7%, p<10⁻³⁹), H7b ISR-specific, genuine n.s. (p=0.182)
295	- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)
296	- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)
297	- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)
298	- [ ] **D060: β=0.3 "PR collapse" → "multi-modal Goodhart instability" — 重写 §4.3, Abstract, Table 1, Conclusion**
299	- [ ] **D060: s44 ISR co-gaming (PR=98%+H7=100%+ISR=0.742) 作为新 Goodhart 模式写入 hacking taxonomy**
300	- [ ] **D085: H7b obfuscated tautology → §4.2 新增子类别分析 + Discussion: models learn to evade diagnostic classifiers (meta-meta-Goodhart)**
301	- [ ] **D085: s44 triple gaming (reward + ISR metric + H7 detector) 作为 meta-Goodhart 最完整案例写入 §4.2/§5**
302	- [ ] **D086: β=0.3 H7 dose-response gradient (Random β=0.1: 13.7% pooled → β=0.3: 4-7/seed → ISR β=0.1: 70.6% pooled) 写入 Discussion**
303	- [ ] **D095: Narrative A — H7a GRPO-general + H7b ISR-specific; 更新 §4.2 数据表 + Discussion H7 mechanism 段**
304	- [ ] **D095/W2: Per-seed + pooled 双报要求；Random H7 单 seed 来源标注**
305	- [ ] **D095/W3: Discussion 新增 hack mode switching 段（GRPO 退化模式受初始化影响）**
306	- [ ] **C013: genuine 公式改为集合排除 proved − |H7 ∪ H1 ∪ H8|**
307	- [ ] **D095: H7 two-layer framing (H7a GRPO-general + H7b ISR-specific) — 更新 §4.2 H7 讨论, Abstract, Headline**
308	- [ ] **D093/D088 correction: H7a not additive-reward-specific (exec-only s43 = 100% H7a) — 更新 mechanism discussion**
309	- [x] D084: genuine 计数标准统一 (genuine = proved − H7 − H1_exact − H8), H1-near 降级为 supplementary-only
310	- [x] D085: H7 子类别 taxonomy 建立 (H7a text-match / H7b obfuscated), s44 验证 77+12=89
311	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "47721a90-9e3a-45bf-8772-ccaabde70f77",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md",
      "content": "  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\n- **Headline result**: \"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward amplifies H7 tautological collapse ~5x (ISR H7=70.6% vs Random H7=13.7%, Fisher p=1.3×10⁻³⁹), with H7b obfuscated tautology as ISR-specific meta-Goodhart; the apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), ISR produces extreme cross-seed instability (PR=66±42%) with three distinct Goodhart pathways: Reward Collapse (18%), H1-Dominant Shortcutting (86% PR, 68.6% H1, only 26.7% genuine), and Pure H7 Meta-Goodhart where the model simultaneously games both execution and structural metrics via single-premise-equals-conclusion (95% PR, 100% H7, ISR=0.742 — a fake-high). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~6% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 8 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\"\n\n## ISR Capability Boundary (D021/D022)\n\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\n\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\n\n**论文处理**：降级为 **Limitation / Future Work**。\n\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\"必要\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\n\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\n\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\n|------|------|---------|----------|----------|---------------|\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 100%** (H7a=77 + H7b=12, FN corrected), ISR inflation + classifier evasion | **meta-Goodhart** (triple: reward + ISR + detector) |\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.94 | 0.150 | H7 38.3%, H1 60%, genuine 1.1% | control |\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 82%, H8 18%, genuine 6.7% | control |\n| ISR β=0.3 (s42) | r = r_exec·(1+0.3·ISR) | 0.18 | 0.143 | PR 崩塌（经典 Goodhart） | post-Goodhart |\n| ISR β=0.3 (s43) | r = r_exec·(1+0.3·ISR) | 0.86 | 0.295 | **H1=68.6%**, H7=4.7%, genuine=26.7% — H1-Dominant Shortcutting | **meta-Goodhart (H1 path)** |\n| ISR β=0.3 (s44) | r = r_exec·(1+0.3·ISR) | 0.95 | **0.742** | **H7=100%**, ISR 被同时 game — Pure H7 Meta-Goodhart | **meta-Goodhart extreme** |\n| random β=0.3 (s42) | r = r_exec·(1+0.3·random) | 0.48 | 0.094 | H7a=8.3% (4), H1=91.7%, genuine=0% | control |\n| random β=0.3 (s44) | r = r_exec·(1+0.3·random) | 0.23 | 0.000 | H1=100%, conclusion embedding | control |\n| random β=0.3 (s43) | r = r_exec·(1+0.3·random) | 0.92 | 0.166 | H7a=7 (7.6%), H1=82 (89.1%), genuine=3 (3.3%) | control |\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\n\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 产生多模态 Goodhart 不稳定（PR=69±44%，三种不同失败路径，包括 ISR 本身被 game 的极端情况）。ISR 的核心价值在诊断（Claim 1）。\n\n## Venue Fit Risks\n\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\n- **\"Just negative results\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\n- **\"Old wine\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\n- **\"Single-logic risk\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\n\n## Anticipated Reviewer Concerns\n\n1. **\"ISR is just LOO ablation — not novel\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\n2. **\"β=0.1 success is just one seed\"** — D051 shows even that one seed's \"success\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\n3. **\"Conclusion embedding invalidates ISR results\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\n4. **\"Goodhart's Law is obvious\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\n5. **\"No positive result\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\n6. **\"ISR is circular\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\n7. **\"Only one logic type\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~6%).\n8. **\"500 steps too short\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\n9. **\"3 seeds insufficient\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\n10. **\"2.4x was wrong — credibility concern\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\n11. **\"Premise count confound is obvious\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\n12. **\"Practitioners can't act on this\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\n13. **\"Prolog s44 was initially misclassified\"** — Transparent: initial text-match classifier returned \"Genuine=100%\", independent review with functional analysis (n_necessary) corrected to \"0% genuine, query-as-fact gaming\". This classifier blind spot is itself a finding (Practitioner Insight #7).\n\n## Discussion 备注 (D095)\n\n### W3: Hack Mode Switching — GRPO 退化模式受初始化影响\nRandom β=0.1 三 seed 的主导策略各不相同：s42 genuine-heavy (22.8%), s43-r3 H7-dominant (38.3%), s44-r2 H8-dominant (18.0%)。ISR β=0.1 类似：s42 H1-heavy (51.9%), s43 H7-dominant (100%, H7a=59 + H7b=2), s44 H7-dominant (100%, 含 H7b)。这证明 GRPO 退化模式受随机初始化高度影响——同一 reward 配置下，不同 seed 收敛到完全不同的 hacking strategy。论文 Discussion 应用 1 段讨论此 \"hack mode switching\" 现象及其对可复现性的影响。\n\n### Narrative A 措辞规范 (D095 Reviewer W2)\n- 不用 \"ISR amplifies H7 (70.6% vs 13.7%)\" 的简单 pooled 对比\n- 正确 framing: \"H7a 是 GRPO 训练的随机退化模式，受 seed 强烈影响。ISR 使 H7 收敛更系统化（2/3 seeds，97-100%），而 Random 条件下 H7 是偶发的（1/3 seeds，38.3%）。关键差异不在平均频率，在于 ISR 让 H7 从随机事件变为近乎必然的收敛方向。\"\n- 论文必须同时报 per-seed 和 pooled，且显著标注 Random H7 的单 seed 来源\n\n## Dream-Identified Structural Fixes (Paper Agent)\n\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\n- [ ] RIP framing: reframe as \"component necessity testing inspired by RIP\"\n- [ ] \"Dense+automatic\" → \"conditionally dense\"\n- [ ] Remove all \"Pareto-improving\" language\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\n- [ ] Address ISR sparsity for unproved outputs explicitly\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\n- [ ] **D051: Remove all \"2.4x genuine improvement\" language, replace with \"1.06x premise-matched\"**\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\n- [x] Convex combination → additive bonus (D010, then D020)\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\n- [x] Hacking taxonomy expanded to 8 modes (plan012 + plan017 + D043 + D085 H7b + Prolog query-as-fact)\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\n- [x] 1000-step ISR collapse documented (plan016)\n- [x] D049: SFT baseline confirms hacking is RL-specific\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\n- [x] D051: paper_framing 回退到 \"pure negative finding\"\n- [x] D057→D095: Claim 2 闭环——3-seed random 控制组完成, D095 Narrative A: H7a GRPO-general (ISR amplified 70.6% vs 13.7%, p<10⁻³⁹), H7b ISR-specific, genuine n.s. (p=0.182)\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\n- [ ] **D060: β=0.3 \"PR collapse\" → \"multi-modal Goodhart instability\" — 重写 §4.3, Abstract, Table 1, Conclusion**\n- [ ] **D060: s44 ISR co-gaming (PR=98%+H7=100%+ISR=0.742) 作为新 Goodhart 模式写入 hacking taxonomy**\n- [ ] **D085: H7b obfuscated tautology → §4.2 新增子类别分析 + Discussion: models learn to evade diagnostic classifiers (meta-meta-Goodhart)**\n- [ ] **D085: s44 triple gaming (reward + ISR metric + H7 detector) 作为 meta-Goodhart 最完整案例写入 §4.2/§5**\n- [ ] **D086: β=0.3 H7 dose-response gradient (Random β=0.1: 13.7% pooled → β=0.3: 4-7/seed → ISR β=0.1: 70.6% pooled) 写入 Discussion**\n- [ ] **D095: Narrative A — H7a GRPO-general + H7b ISR-specific; 更新 §4.2 数据表 + Discussion H7 mechanism 段**\n- [ ] **D095/W2: Per-seed + pooled 双报要求；Random H7 单 seed 来源标注**\n- [ ] **D095/W3: Discussion 新增 hack mode switching 段（GRPO 退化模式受初始化影响）**\n- [ ] **C013: genuine 公式改为集合排除 proved − |H7 ∪ H1 ∪ H8|**\n- [ ] **D095: H7 two-layer framing (H7a GRPO-general + H7b ISR-specific) — 更新 §4.2 H7 讨论, Abstract, Headline**\n- [ ] **D093/D088 correction: H7a not additive-reward-specific (exec-only s43 = 100% H7a) — 更新 mechanism discussion**\n- [x] D084: genuine 计数标准统一 (genuine = proved − H7 − H1_exact − H8), H1-near 降级为 supplementary-only\n- [x] D085: H7 子类别 taxonomy 建立 (H7a text-match / H7b obfuscated), s44 验证 77+12=89\n",
      "numLines": 112,
      "startLine": 200,
      "totalLines": 311
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full checklist. Let me identify all unchecked `[ ]` items:

1. Related work: 6→25+ references
2. RIP framing: reframe as "component necessity testing inspired by RIP"
3. "Dense+automatic" → "conditionally dense"
4. Remove all "Pareto-improving" language
5. Acknowledge ISR = LOO ablation, cite feature attribution literature


6. Address ISR sparsity for unproved outputs explicitly
7. Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)
8. Add premise-count confound discussion in Discussion/Limitations section
9. Remove all "2.4x genuine improvement" language, replace with "1.06x premise-matched"
10. Move Prolog s44 classifier blind spot to Discussion
11. Reframe β=0.3 "PR collapse" as "multi-modal Goodhart instability" across §4.3, Abstract, Table 1, and Conclusion

Now I'm working through the Goodhart taxonomy revisions: treating s44 ISR co-gaming as a distinct mode, adding the obfuscated tautology subcategory for H7b with supporting analysis, and framing s44's triple gaming as a meta-Goodhart case. I need to incorporate the β=0.3 H7 dose-response gradient into the Discussion, restructure the H7 narrative to separate GRPO-general effects from ISR-specific ones with updated data tables, and implement dual reporting for both per-seed and pooled results with random seed source annotations. I'm also refining the genuine improvement formula as a set exclusion calculation and applying the two-layer H7 framing throughout the relevant sections.

Now I need to verify that H7a isn't being characterized as additive-reward-specific in the mechanism discussion, then systematically check all the TeX files to ensure each revision is properly implemented.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "aa18ade7-671c-4f37-ab67-3c6a67f4d12f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MGGE4eP2PBGoqtcN8fSJNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5157,
      "cache_read_input_tokens": 35963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5157
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 11_

Now let me identify the TeX files and start checking each unchecked item in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "b13d5d17-c35e-48f9-8055-4d0107953f69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MGGE4eP2PBGoqtcN8fSJNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5157,
      "cache_read_input_tokens": 35963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5157
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_016tsWrk5JxozTgSybXW7NmD`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "cceea12c-7b89-41d8-84e0-9aa98847a38d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MGGE4eP2PBGoqtcN8fSJNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5157,
      "cache_read_input_tokens": 35963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5157
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T21:29:35.668Z_

<details><summary>↩ Tool result · `toolu_016tsWrk5JxozTgSybXW7NmD`</summary>

```text
paper/limitations.tex
paper/abstract.tex
paper/method.tex
paper/conclusion.tex
paper/main.tex
paper/introduction.tex
paper/related_work.tex
paper/appendix.tex
paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "25c47ead-b5a9-498d-afab-e77ecfae4040",
  "tool_use_result": {
    "filenames": [
      "paper/limitations.tex",
      "paper/abstract.tex",
      "paper/method.tex",
      "paper/conclusion.tex",
      "paper/main.tex",
      "paper/introduction.tex",
      "paper/related_work.tex",
      "paper/appendix.tex",
      "paper/experiments.tex"
    ],
    "durationMs": 26,
    "numFiles": 9,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 14_

Let me read all the TeX files and search for key terms in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "5465246f-0e23-4b63-aa2e-019911a8569c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYNqnySrdyi75vhanCcS4R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 765,
      "cache_read_input_tokens": 41120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 765
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01UbKhj8vYCbsCFThPCWixDA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "ee287cca-88dd-49a1-9723-583cfcf43a7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYNqnySrdyi75vhanCcS4R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 765,
      "cache_read_input_tokens": 41120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 765
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T21:29:39.397Z_

<details><summary>↩ Tool result · `toolu_01UbKhj8vYCbsCFThPCWixDA`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}: \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
10	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
11	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
12	The shared lesson across these approaches is that reward augmentation introduces proxy risk---our contribution is demonstrating the \emph{meta}-level variant where the diagnostic itself becomes the target.
13	
14	\paragraph{Reward hacking and Goodhart's Law.}
15	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
16	\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.
17	Recent work further documents spurious reward signals in RLVR~\citep{spurious-rewards} and reward hacking in frontier models~\citep{metr-reward-hacking}.
18	Our setting differs in three ways: ISR is deterministic and solver-derived rather than learned; gaming \emph{emerges during RL training} rather than at inference time; and the effect operates at a \emph{meta} level---the diagnostic for gaming itself becomes gamed when optimized---a phenomenon, to our knowledge, not previously documented.
19	
20	\paragraph{Mutation testing.}
21	STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "2d9e82d8-b5b3-49a3-9f28-33857e93dcd6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.\nWe use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Process rewards and reward shaping.}\nLearned PRMs~\\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\\citep{processbench}: \\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \\emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.\nSymbolic feedback approaches~\\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.\nRubric-grounded GRPO~\\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.\nThe shared lesson across these approaches is that reward augmentation introduces proxy risk---our contribution is demonstrating the \\emph{meta}-level variant where the diagnostic itself becomes the target.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \\emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.\nRecent work further documents spurious reward signals in RLVR~\\citep{spurious-rewards} and reward hacking in frontier models~\\citep{metr-reward-hacking}.\nOur setting differs in three ways: ISR is deterministic and solver-derived rather than learned; gaming \\emph{emerges during RL training} rather than at inference time; and the effect operates at a \\emph{meta} level---the diagnostic for gaming itself becomes gamed when optimized---a phenomenon, to our knowledge, not previously documented.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01JEcSxcs6YUNz66BqqRAHbn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "00ba113e-f1c1-4bb0-b33f-704453d188f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYNqnySrdyi75vhanCcS4R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 765,
      "cache_read_input_tokens": 41120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 765
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T21:29:40.434Z_

<details><summary>↩ Tool result · `toolu_01JEcSxcs6YUNz66BqqRAHbn`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: when the diagnostic becomes the target, meta-level Goodhart's Law emerges.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with GRPO~\citep{deepseekmath} ($K{=}8$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is standard in mutation testing and feature attribution; our novelty is its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
27	
28	\begin{algorithm}[t]
29	\caption{Solver Trace Ablation (STA)}
30	\label{alg:sta}
31	\begin{algorithmic}[1]
32	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
33	\ENSURE $\text{ISR}(x) \in [0, 1]$
34	\STATE $\textit{necessary} \gets 0$
35	\FOR{$i = 1$ to $n$}
36	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
37	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
38	    \ENDIF
39	\ENDFOR
40	\RETURN $\textit{necessary} \,/\, n$
41	\end{algorithmic}
42	\end{algorithm}
43	
44	\paragraph{Intensional Structural Reward.}
45	ISR is the fraction of necessary components:
46	\begin{equation}
47	  \text{ISR}(x) = \frac{1}{n}\sum_{i=1}^{n}\mathbf{1}\bigl[S(x\setminus\{c_i\})=\textit{failed}\bigr]
48	  \label{eq:isr}
49	\end{equation}
50	ISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.
51	We report \emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating structural quality with prove rate.
52	
53	\paragraph{Limitations of ISR.}
54	ISR measures syntactic component necessity, not semantic faithfulness: a formalization can achieve $\text{ISR}{=}1$ while semantically unrelated to the NL input (e.g., a single premise identical to the conclusion).
55	ISR is also sensitive to component count $n$: when $n{=}2$, $\text{ISR}\geq 0.5$ regardless of proof quality.
56	We control for this confound via premise-count-matched analysis in \S\ref{sec:goodhart}.
57	The $O(n)$ per-clause LOO ablation is necessary: a cheaper $O(1)$ binary variant produces near-zero ISR scores ($\text{ISR}^*{=}0.007$) indistinguishable from exec-only, because models generate redundant premise copies whose individual removal never changes the proof outcome.
58	However, the $O(1)$ variant includes a tautology check (conclusion provable under empty premises $\to$ ISR${=}0$) absent from exec-only, introducing a training-time confound that depresses prove rate ($63\%$ vs.\ $93\%$ exec-only); the two conditions are therefore non-equivalent in training dynamics despite producing comparable ISR signals (Appendix~\ref{app:o1-ablation}).
59	
60	\subsection{Reward Conditions and Hacking Modes}
61	\label{sec:rewards}
62	\label{sec:taxonomy-method}
63	
64	We study six conditions: exec-only ($r_{\text{exec}}$), ISR low/high-dose ($r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta\in\{0.1,0.3\}$), matched random controls ($r_{\text{exec}}\cdot(1{+}\beta u)$, $u\sim\mathcal{U}(0,1)$), and an SFT baseline (NLL on gold formalizations).
65	Multiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.
66	Random isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.
67	Each RL condition uses seeds $\{42,43,44\}$ and identical training data.
68	An earlier convex formulation ($\alpha r_{\text{exec}} + \beta r_{\text{exec}}\text{ISR}$, $\alpha{+}\beta{=}1$) was discarded because $\text{ISR}{<}1$ always penalized relative to exec-only, collapsing PR (Appendix~\ref{app:setup}).
69	
70	\paragraph{Hacking taxonomy.}
71	Across conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\ref{app:hacking-modes}):
72	\textbf{H1} (conclusion embedded among multiple premises),
73	\textbf{H7} (single-premise conclusion duplication, subtypes H7a standard and H7b obfuscated tautology; targets the ISR signal directly, since removing the sole premise forces $\text{ISR}\geq 0.5$),
74	\textbf{H8} (premise-subset gaming: each component is LOO-necessary but the premise set is a strict subset of what the problem requires, inflating ISR without faithful reasoning; Appendix~\ref{app:h8}),
75	\textbf{tautological collapse} (minimal two-component $P{\to}P$ without explicit ISR inflation),
76	\textbf{repetition collapse} (identical clauses repeated to inflate component count),
77	\textbf{complexity-without-utility} (elaborate but vacuous premises),
78	\textbf{contradiction explosion} (contradictory premises trivializing any conclusion via \emph{ex falso}), and
79	\textbf{query-as-fact gaming} (Prolog-specific: emit the NL question as an atom asserted as both fact and query; evades text-match classifiers).
80	Modes are identified by a two-stage procedure: strict normalized text matching (H1/H7) plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution (catches modes evading text matching).
81	We report both classifications in \S\ref{sec:experiments}.
82	
83	In interpreting ISR results we distinguish two failure semantics that share a numerical signature: an exec-only \emph{low} ISR signals \emph{redundancy} (e.g., repeated ground facts in Prolog), whereas an ISR-rewarded \emph{high} ISR signals \emph{metric gaming} (H7-style constructions).
84	A bare ISR difference therefore does not translate directly into a reasoning-ability difference; the mode breakdown is what licenses such interpretation.
85	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "3863ba8f-27ca-4aca-8b3d-86cdbe122df0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth]{figures/fig1_sta_overview.pdf}\n\\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\\ as reward: when the diagnostic becomes the target, meta-level Goodhart's Law emerges.}\n\\label{fig:sta-overview}\n\\end{figure*}\n\n\\subsection{Task and GRPO Training}\n\\label{sec:task}\n\nGiven premises $P_1,\\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\\{c_1,\\ldots,c_n\\}$ verified by an external solver $S\\in\\{\\text{Prover9, SWI-Prolog}\\}$ (Figure~\\ref{fig:sta-overview}a).\nWe train with GRPO~\\citep{deepseekmath} ($K{=}8$), where each rollout receives binary execution reward $r_{\\text{exec}}(x) = \\mathbf{1}[S(F_x){=}\\textit{proved}]$.\nThis optimizes prove rate but provides no signal about \\emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.\nAll experiments draw from FOLIO~\\citep{folio}; the held-out evaluation file retains a legacy \\texttt{proofwriter\\_fol\\_*.jsonl} filename (from ProofWriter~\\citep{proofwriter}) but contains only FOLIO-derived examples.\n\n\\subsection{Solver Trace Ablation (STA)}\n\\label{sec:sta}\n\nSTA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\\ref{fig:sta-overview}b).\nGiven a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\\setminus\\{c_i\\}$ and re-runs the solver (Algorithm~\\ref{alg:sta}).\nA component is \\emph{necessary} if its removal causes proof failure.\nWhat constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.\nLOO ablation itself is standard in mutation testing and feature attribution; our novelty is its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.\n\n\\begin{algorithm}[t]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\REQUIRE Proved formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $S$\n\\ENSURE $\\text{ISR}(x) \\in [0, 1]$\n\\STATE $\\textit{necessary} \\gets 0$\n\\FOR{$i = 1$ to $n$}\n    \\IF{$S(x \\setminus \\{c_i\\}) = \\textit{failed}$}\n        \\STATE $\\textit{necessary} \\gets \\textit{necessary} + 1$\n    \\ENDIF\n\\ENDFOR\n\\RETURN $\\textit{necessary} \\,/\\, n$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Intensional Structural Reward.}\nISR is the fraction of necessary components:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n}\\sum_{i=1}^{n}\\mathbf{1}\\bigl[S(x\\setminus\\{c_i\\})=\\textit{failed}\\bigr]\n  \\label{eq:isr}\n\\end{equation}\nISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.\nWe report \\emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating structural quality with prove rate.\n\n\\paragraph{Limitations of ISR.}\nISR measures syntactic component necessity, not semantic faithfulness: a formalization can achieve $\\text{ISR}{=}1$ while semantically unrelated to the NL input (e.g., a single premise identical to the conclusion).\nISR is also sensitive to component count $n$: when $n{=}2$, $\\text{ISR}\\geq 0.5$ regardless of proof quality.\nWe control for this confound via premise-count-matched analysis in \\S\\ref{sec:goodhart}.\nThe $O(n)$ per-clause LOO ablation is necessary: a cheaper $O(1)$ binary variant produces near-zero ISR scores ($\\text{ISR}^*{=}0.007$) indistinguishable from exec-only, because models generate redundant premise copies whose individual removal never changes the proof outcome.\nHowever, the $O(1)$ variant includes a tautology check (conclusion provable under empty premises $\\to$ ISR${=}0$) absent from exec-only, introducing a training-time confound that depresses prove rate ($63\\%$ vs.\\ $93\\%$ exec-only); the two conditions are therefore non-equivalent in training dynamics despite producing comparable ISR signals (Appendix~\\ref{app:o1-ablation}).\n\n\\subsection{Reward Conditions and Hacking Modes}\n\\label{sec:rewards}\n\\label{sec:taxonomy-method}\n\nWe study six conditions: exec-only ($r_{\\text{exec}}$), ISR low/high-dose ($r_{\\text{exec}}\\cdot(1{+}\\beta\\,\\text{ISR})$ at $\\beta\\in\\{0.1,0.3\\}$), matched random controls ($r_{\\text{exec}}\\cdot(1{+}\\beta u)$, $u\\sim\\mathcal{U}(0,1)$), and an SFT baseline (NLL on gold formalizations).\nMultiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.\nRandom isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.\nEach RL condition uses seeds $\\{42,43,44\\}$ and identical training data.\nAn earlier convex formulation ($\\alpha r_{\\text{exec}} + \\beta r_{\\text{exec}}\\text{ISR}$, $\\alpha{+}\\beta{=}1$) was discarded because $\\text{ISR}{<}1$ always penalized relative to exec-only, collapsing PR (Appendix~\\ref{app:setup}).\n\n\\paragraph{Hacking taxonomy.}\nAcross conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\\ref{app:hacking-modes}):\n\\textbf{H1} (conclusion embedded among multiple premises),\n\\textbf{H7} (single-premise conclusion duplication, subtypes H7a standard and H7b obfuscated tautology; targets the ISR signal directly, since removing the sole premise forces $\\text{ISR}\\geq 0.5$),\n\\textbf{H8} (premise-subset gaming: each component is LOO-necessary but the premise set is a strict subset of what the problem requires, inflating ISR without faithful reasoning; Appendix~\\ref{app:h8}),\n\\textbf{tautological collapse} (minimal two-component $P{\\to}P$ without explicit ISR inflation),\n\\textbf{repetition collapse} (identical clauses repeated to inflate component count),\n\\textbf{complexity-without-utility} (elaborate but vacuous premises),\n\\textbf{contradiction explosion} (contradictory premises trivializing any conclusion via \\emph{ex falso}), and\n\\textbf{query-as-fact gaming} (Prolog-specific: emit the NL question as an atom asserted as both fact and query; evades text-match classifiers).\nModes are identified by a two-stage procedure: strict normalized text matching (H1/H7) plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution (catches modes evading text matching).\nWe report both classifications in \\S\\ref{sec:experiments}.\n\nIn interpreting ISR results we distinguish two failure semantics that share a numerical signature: an exec-only \\emph{low} ISR signals \\emph{redundancy} (e.g., repeated ground facts in Prolog), whereas an ISR-rewarded \\emph{high} ISR signals \\emph{metric gaming} (H7-style constructions).\nA bare ISR difference therefore does not translate directly into a reasoning-ability difference; the mode breakdown is what licenses such interpretation.\n",
      "numLines": 85,
      "startLine": 1,
      "totalLines": 85
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_011gabVc2gJehzAm6FTjR7hQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "c6383975-ec57-46d3-a150-b70ece67e4fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYNqnySrdyi75vhanCcS4R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 765,
      "cache_read_input_tokens": 41120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 765
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T21:29:40.449Z_

<details><summary>↩ Tool result · `toolu_011gabVc2gJehzAm6FTjR7hQ`</summary>

```text
1	\begin{abstract}
2	GRPO-trained neurosymbolic formalizers achieve high prove rates---93\% on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.
4	The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.
5	ISR is uncorrelated with downstream NLI accuracy ($\rho{=}{-}0.049$), confirming it measures structural---not semantic---integrity.
6	As a diagnostic, ISR exposes a collapse trajectory hidden from PR: over 100--1000 GRPO steps (Qwen3-4B), ISR falls $0.642{\to}0.003$ while PR rises $32\%{\to}96\%$; an SFT baseline reaches 92.3\% non-hacking on identical data (3-seed pooled), localizing the failure to RL.
7	As a reward, $r = r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta{=}0.1$ induces \emph{meta-level Goodhart's Law}: 70.6\% conclusion duplication (H7) versus 13.7\% under matched random (Fisher $p{=}1.3{\times}10^{-39}$; random H7 is seed-dependent, driven by one of three seeds); ISR amplifies H7 frequency ${\sim}5{\times}$ rather than exclusively causing it; the sole apparent ISR improvement reduces to $1.06\times$ after controlling for a premise-count confound; $\beta{=}0.3$ destabilizes training regardless of signal source (ISR: PR $66{\pm}42\%$; random: $54{\pm}35\%$), with individual seeds collapsing to as low as $18\%$.
8	Cross-logic transfer to Prolog yields universal Goodhart: 3/3 seeds gaming via distinct mechanisms, 0\% non-hacking.
9	Across 6 reward conditions, 2 logic types, 3 seeds, we catalog 8 hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
10	\end{abstract}
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "94ac3188-37cd-4bb7-8a5f-2ecb8dd29408",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex",
      "content": "\\begin{abstract}\nGRPO-trained neurosymbolic formalizers achieve high prove rates---93\\% on FOLIO---yet 87\\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.\nWe introduce \\emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.\nThe fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.\nISR is uncorrelated with downstream NLI accuracy ($\\rho{=}{-}0.049$), confirming it measures structural---not semantic---integrity.\nAs a diagnostic, ISR exposes a collapse trajectory hidden from PR: over 100--1000 GRPO steps (Qwen3-4B), ISR falls $0.642{\\to}0.003$ while PR rises $32\\%{\\to}96\\%$; an SFT baseline reaches 92.3\\% non-hacking on identical data (3-seed pooled), localizing the failure to RL.\nAs a reward, $r = r_{\\text{exec}}\\cdot(1{+}\\beta\\,\\text{ISR})$ at $\\beta{=}0.1$ induces \\emph{meta-level Goodhart's Law}: 70.6\\% conclusion duplication (H7) versus 13.7\\% under matched random (Fisher $p{=}1.3{\\times}10^{-39}$; random H7 is seed-dependent, driven by one of three seeds); ISR amplifies H7 frequency ${\\sim}5{\\times}$ rather than exclusively causing it; the sole apparent ISR improvement reduces to $1.06\\times$ after controlling for a premise-count confound; $\\beta{=}0.3$ destabilizes training regardless of signal source (ISR: PR $66{\\pm}42\\%$; random: $54{\\pm}35\\%$), with individual seeds collapsing to as low as $18\\%$.\nCross-logic transfer to Prolog yields universal Goodhart: 3/3 seeds gaming via distinct mechanisms, 0\\% non-hacking.\nAcross 6 reward conditions, 2 logic types, 3 seeds, we catalog 8 hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\\footnote{Code and data: \\url{[anonymized]}}\n\\end{abstract}\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01Cj6nRJ2SNHyoq7Km1JwxcJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "a94fee0b-26af-44b9-a0f8-bf60932d8e54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYNqnySrdyi75vhanCcS4R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 765,
      "cache_read_input_tokens": 41120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 765
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T21:29:40.800Z_

<details><summary>↩ Tool result · `toolu_01Cj6nRJ2SNHyoq7Km1JwxcJ`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
6	Three seeds demonstrate qualitative divergence but limit statistical power.
7	STA requires solvers supporting component-level input manipulation.
8	
9	\paragraph{Data scale.}
10	Our experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\citep{folio}.
11	The training subset is selected via stratified sampling (seed 42) and held constant across all conditions.
12	While our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "eb4adb00-f945-457c-b8ea-a4e4798cb317",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex",
      "content": "\\section{Limitations}\n\\label{sec:limitations}\n\nExperiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.\nISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\\ref{app:extended-discussion}).\nThree seeds demonstrate qualitative divergence but limit statistical power.\nSTA requires solvers supporting component-level input manipulation.\n\n\\paragraph{Data scale.}\nOur experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\\citep{folio}.\nThe training subset is selected via stratified sampling (seed 42) and held constant across all conditions.\nWhile our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_017ASQY5ZcuCDD7qqFXigWbN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "4d9e6ea7-df15-4507-9a18-89f7120522af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYNqnySrdyi75vhanCcS4R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 765,
      "cache_read_input_tokens": 41120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 765
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T21:29:41.272Z_

<details><summary>↩ Tool result · `toolu_017ASQY5ZcuCDD7qqFXigWbN`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	Solver Trace Ablation (STA) exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides; an SFT baseline with 92.3\% non-hacking (3-seed pooled) localizes the failure to RL optimization (\S\ref{sec:diagnostic}).
5	Repurposed as a training signal, ISR induces meta-level Goodhart's Law: the diagnostic for gaming becomes itself the target of gaming.
6	At $\beta{=}0.1$, conclusion duplication exploits the LOO definition (70.6\% vs.\ 13.7\% under matched random (Fisher $p{<}10^{-38}$); random H7 is seed-dependent (38.3\% in one seed, 0\% in two others), so ISR amplifies rather than exclusively causes H7), and the sole apparent ISR gain reduces to $1.06\times$ random once a premise-count confound is controlled; at $\beta{=}0.3$, cross-seed instability is extreme ($\text{PR}{=}66{\pm}42\%$, random $54{\pm}35\%$), each seed converging to a distinct failure mode.
7	The pattern transfers to Prolog, where ISR-as-reward yields universal gaming (3/3 seeds, 0\% non-hacking) via three distinct mechanisms including query-as-fact gaming, which bypasses text-match classifiers (\S\ref{sec:taxonomy}).
8	ISR semantics depend on objective: exec-only \emph{low} ISR signals redundancy; ISR-rewarded \emph{high} ISR signals metric gaming.
9	
10	\paragraph{Classifier blind spots and functional cross-validation.}
11	H7b (obfuscated tautology) demonstrates that text-match classifiers have systematic blind spots: the model learns vacuous quantifier wrapping to disguise tautologies, evading detection while simultaneously gaming ISR ($10/12$ samples at $\text{ISR}{\approx}0.8$).
12	This triple gaming---execution reward, structural metric, and diagnostic classifier---is the most complete meta-Goodhart case we observe.
13	Query-as-fact gaming in Prolog (\S\ref{sec:crosslogic}) independently confirms the blind spot: our strict classifier reported $100\%$ genuine before functional LOO analysis revealed $95/97$ samples tautological.
14	Both cases argue for mandatory functional cross-validation of any text-based hacking classifier.
15	
16	\paragraph{H7 dose-response gradient.}
17	H7 tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ H7 ($36/262$, pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 H7a samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
18	The gradient---random $\beta{=}0.1$ ($13.7\%$, pooled) $\to$ random $\beta{=}0.3$ (4--7 H7a per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)---shows ISR transforms H7 from a seed-dependent GRPO tendency to a near-universal convergence direction.
19	
20	\paragraph{Hacking mode switching.}
21	The dominant hacking strategy is not reward-determined: under identical reward configurations, different seeds converge to qualitatively different modes (Appendix Table~\ref{tab:fol-detailed}).
22	Random $\beta{=}0.1$ seeds illustrate this starkly: s42 shows the highest non-hacking rate ($22.8\%$), s43 is H7-dominant ($38.3\%$), and s44 is H8-dominant.
23	ISR $\beta{=}0.1$ shows analogous switching: s42 is H1-heavy, while s43 and s44 are near-pure H7 (${\geq}97\%$).
24	This seed-dependent mode selection implies that GRPO hacking patterns are sensitive to random initialization, and single-seed results can misrepresent the hacking profile of a reward configuration.
25	Multi-seed evaluation with per-mode reporting should be standard practice.
26	
27	The asymmetry---reliable observer, unreliable optimizer---may generalize to other perturbation-based diagnostics; ISR and structurally similar metrics should be used as post-hoc evaluation, with future work targeting gaming-robust rewards and broader logic types.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "046471c7-124d-4877-8b85-6b1a83ae29e8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nSolver Trace Ablation (STA) exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\\% collapse under exec-only GRPO that PR hides; an SFT baseline with 92.3\\% non-hacking (3-seed pooled) localizes the failure to RL optimization (\\S\\ref{sec:diagnostic}).\nRepurposed as a training signal, ISR induces meta-level Goodhart's Law: the diagnostic for gaming becomes itself the target of gaming.\nAt $\\beta{=}0.1$, conclusion duplication exploits the LOO definition (70.6\\% vs.\\ 13.7\\% under matched random (Fisher $p{<}10^{-38}$); random H7 is seed-dependent (38.3\\% in one seed, 0\\% in two others), so ISR amplifies rather than exclusively causes H7), and the sole apparent ISR gain reduces to $1.06\\times$ random once a premise-count confound is controlled; at $\\beta{=}0.3$, cross-seed instability is extreme ($\\text{PR}{=}66{\\pm}42\\%$, random $54{\\pm}35\\%$), each seed converging to a distinct failure mode.\nThe pattern transfers to Prolog, where ISR-as-reward yields universal gaming (3/3 seeds, 0\\% non-hacking) via three distinct mechanisms including query-as-fact gaming, which bypasses text-match classifiers (\\S\\ref{sec:taxonomy}).\nISR semantics depend on objective: exec-only \\emph{low} ISR signals redundancy; ISR-rewarded \\emph{high} ISR signals metric gaming.\n\n\\paragraph{Classifier blind spots and functional cross-validation.}\nH7b (obfuscated tautology) demonstrates that text-match classifiers have systematic blind spots: the model learns vacuous quantifier wrapping to disguise tautologies, evading detection while simultaneously gaming ISR ($10/12$ samples at $\\text{ISR}{\\approx}0.8$).\nThis triple gaming---execution reward, structural metric, and diagnostic classifier---is the most complete meta-Goodhart case we observe.\nQuery-as-fact gaming in Prolog (\\S\\ref{sec:crosslogic}) independently confirms the blind spot: our strict classifier reported $100\\%$ genuine before functional LOO analysis revealed $95/97$ samples tautological.\nBoth cases argue for mandatory functional cross-validation of any text-based hacking classifier.\n\n\\paragraph{H7 dose-response gradient.}\nH7 tautology follows a dose-response pattern across reward conditions: random $\\beta{=}0.1$ produces $13.7\\%$ H7 ($36/262$, pooled; per-seed: $38.3\\%$ in s43, $0\\%$ in s42/s44), random $\\beta{=}0.3$ yields 4--7 H7a samples per seed, and ISR $\\beta{=}0.1$ reaches $70.6\\%$ ($163/231$).\nThe gradient---random $\\beta{=}0.1$ ($13.7\\%$, pooled) $\\to$ random $\\beta{=}0.3$ (4--7 H7a per seed) $\\to$ ISR $\\beta{=}0.1$ ($70.6\\%$)---shows ISR transforms H7 from a seed-dependent GRPO tendency to a near-universal convergence direction.\n\n\\paragraph{Hacking mode switching.}\nThe dominant hacking strategy is not reward-determined: under identical reward configurations, different seeds converge to qualitatively different modes (Appendix Table~\\ref{tab:fol-detailed}).\nRandom $\\beta{=}0.1$ seeds illustrate this starkly: s42 shows the highest non-hacking rate ($22.8\\%$), s43 is H7-dominant ($38.3\\%$), and s44 is H8-dominant.\nISR $\\beta{=}0.1$ shows analogous switching: s42 is H1-heavy, while s43 and s44 are near-pure H7 (${\\geq}97\\%$).\nThis seed-dependent mode selection implies that GRPO hacking patterns are sensitive to random initialization, and single-seed results can misrepresent the hacking profile of a reward configuration.\nMulti-seed evaluation with per-mode reporting should be standard practice.\n\nThe asymmetry---reliable observer, unreliable optimizer---may generalize to other perturbation-based diagnostics; ISR and structurally similar metrics should be used as post-hoc evaluation, with future work targeting gaming-robust rewards and broader logic types.\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01LxU5i84zXxns97ZscCtWqC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "edac10b2-c59d-4a4c-8ee3-47f432764944",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYNqnySrdyi75vhanCcS4R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 765,
      "cache_read_input_tokens": 41120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 765
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T21:29:41.654Z_

<details><summary>↩ Tool result · `toolu_01LxU5i84zXxns97ZscCtWqC`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but gives no gradient on structural quality.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\ref{fig:sta-overview}).
16	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR), with $\text{ISR}{=}1$ indicating full necessity and $\text{ISR}{=}0$ complete redundancy.
17	LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
18	ISR captures structural rather than semantic integrity (downstream NLI: $\rho{=}{-}0.049$, $p{=}0.187$).
19	
20	\paragraph{ISR as diagnostic.}
21	As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\text{ISR}^{*}{:}\,0.642\to 0.132\to 0.003$ over 100--1000 steps (99.5\% degradation) while PR rises $32\%{\to}96\%$.
22	Three seeds diverge radically (PR $\sigma{=}47$\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.
23	An SFT baseline on identical data reaches $\text{PR}{=}13.0\%$ with 92.3\% non-hacking (3-seed pooled, 1000 steps), localizing the failure to RL optimization, not data or capacity.
24	
25	\paragraph{Meta-level Goodhart.}
26	Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR is gamed at its own definition---\emph{meta-level Goodhart's Law}~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.
27	At $\beta{=}0.1$, 70.6\% of proved samples exhibit conclusion duplication (H7)---versus 13.7\% under matched random (Fisher $p{<}10^{-38}$; random H7 is highly seed-dependent), showing ISR amplifies tautological collapse by ${\sim}5{\times}$; the one seed with non-trivial residual reduces to $1.06\times$ random after controlling for a premise-count confound.
28	At $\beta{=}0.3$, both ISR and random produce extreme cross-seed instability (PR $66{\pm}42\%$ and $54{\pm}35\%$ respectively), confirming high-dose proxy weighting is harmful regardless of signal content; ISR seeds diverge into three distinct pathways (reward collapse, shortcut dominance, pure metric gaming) while random converges uniformly to H1.
29	The effect transfers and intensifies in Prolog: 3/3 seeds yield 0\% non-hacking via distinct mechanisms, including \emph{query-as-fact gaming} that bypasses text-match classifiers.
30	ISR's asymmetry is the central finding: \emph{reliable as observer, unreliable as optimizer.}
31	
32	\paragraph{Contributions.}
33	Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 steps, we contribute: (\textbf{C1}) ISR as a diagnostic for GRPO reward hacking, with a 99.5\% collapse trajectory invisible to PR and an SFT control localizing the failure to RL (\S\ref{sec:diagnostic}); (\textbf{C2}) empirical meta-level Goodhart, with a random control showing ISR amplifies H7 gaming ${\sim}5{\times}$ (70.6\% vs.\ 13.7\%, Fisher $p{<}10^{-38}$; random H7 is seed-dependent) and a premise-count-matched analysis showing the sole apparent gain is an LOO artifact (\S\ref{sec:goodhart}); (\textbf{C3}) cross-logic transfer to Prolog with universal Goodhart (\S\ref{sec:crosslogic}); (\textbf{C4}) an eight-mode hacking taxonomy including query-as-fact gaming and obfuscated tautology, motivating functional cross-validation of diagnostics (\S\ref{sec:taxonomy}).
34	These are cautionary results for any work treating a structural proxy as a training signal.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "89a32569-87a1-49ad-94d7-a427a585d3cf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nA GRPO-trained formalizer achieves a 93\\% prove rate on first-order logic problems---yet 87\\% of its proved outputs embed the conclusion verbatim among the premises.\nThe solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.\nThis structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.\n\n\\paragraph{The execution-only blind spot.}\nProve rate---the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nRecent work applies GRPO~\\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but gives no gradient on structural quality.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.\nA separate line documents that LLMs already game logical formalization at inference time~\\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \\emph{diagnostic} for structural integrity in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic applying \\emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\\ref{fig:sta-overview}).\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR), with $\\text{ISR}{=}1$ indicating full necessity and $\\text{ISR}{=}0$ complete redundancy.\nLOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.\nISR captures structural rather than semantic integrity (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\n\n\\paragraph{ISR as diagnostic.}\nAs a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\\text{ISR}^{*}{:}\\,0.642\\to 0.132\\to 0.003$ over 100--1000 steps (99.5\\% degradation) while PR rises $32\\%{\\to}96\\%$.\nThree seeds diverge radically (PR $\\sigma{=}47$\\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.\nAn SFT baseline on identical data reaches $\\text{PR}{=}13.0\\%$ with 92.3\\% non-hacking (3-seed pooled, 1000 steps), localizing the failure to RL optimization, not data or capacity.\n\n\\paragraph{Meta-level Goodhart.}\nRepurposed as a training signal, $r = r_{\\text{exec}} \\cdot (1 + \\beta\\,\\text{ISR})$, ISR is gamed at its own definition---\\emph{meta-level Goodhart's Law}~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.\nAt $\\beta{=}0.1$, 70.6\\% of proved samples exhibit conclusion duplication (H7)---versus 13.7\\% under matched random (Fisher $p{<}10^{-38}$; random H7 is highly seed-dependent), showing ISR amplifies tautological collapse by ${\\sim}5{\\times}$; the one seed with non-trivial residual reduces to $1.06\\times$ random after controlling for a premise-count confound.\nAt $\\beta{=}0.3$, both ISR and random produce extreme cross-seed instability (PR $66{\\pm}42\\%$ and $54{\\pm}35\\%$ respectively), confirming high-dose proxy weighting is harmful regardless of signal content; ISR seeds diverge into three distinct pathways (reward collapse, shortcut dominance, pure metric gaming) while random converges uniformly to H1.\nThe effect transfers and intensifies in Prolog: 3/3 seeds yield 0\\% non-hacking via distinct mechanisms, including \\emph{query-as-fact gaming} that bypasses text-match classifiers.\nISR's asymmetry is the central finding: \\emph{reliable as observer, unreliable as optimizer.}\n\n\\paragraph{Contributions.}\nAcross 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 steps, we contribute: (\\textbf{C1}) ISR as a diagnostic for GRPO reward hacking, with a 99.5\\% collapse trajectory invisible to PR and an SFT control localizing the failure to RL (\\S\\ref{sec:diagnostic}); (\\textbf{C2}) empirical meta-level Goodhart, with a random control showing ISR amplifies H7 gaming ${\\sim}5{\\times}$ (70.6\\% vs.\\ 13.7\\%, Fisher $p{<}10^{-38}$; random H7 is seed-dependent) and a premise-count-matched analysis showing the sole apparent gain is an LOO artifact (\\S\\ref{sec:goodhart}); (\\textbf{C3}) cross-logic transfer to Prolog with universal Goodhart (\\S\\ref{sec:crosslogic}); (\\textbf{C4}) an eight-mode hacking taxonomy including query-as-fact gaming and obfuscated tautology, motivating functional cross-validation of diagnostics (\\S\\ref{sec:taxonomy}).\nThese are cautionary results for any work treating a structural proxy as a training signal.\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01BWUG1iwphn1aCqkK76xQvH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "acdffcf4-2894-42dc-af20-de57817a580e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ztV7vGNKknzzG1kEULSet",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7626,
      "cache_read_input_tokens": 41885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7626
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T21:29:45.553Z_

<details><summary>↩ Tool result · `toolu_01BWUG1iwphn1aCqkK76xQvH`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits meta-level Goodhart's Law (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}8$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with NLL on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
10	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so training-log ISR is never compared across runs.
11	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary but not sufficient condition for semantic correctness.
12	
13	\subsection{ISR as Diagnostic}
14	\label{sec:diagnostic}
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
19	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples have $\text{ISR}{=}0$ and mean component count inflates 6.58$\to$18.55 (contradiction explosion).}
20	\label{fig:isr-collapse}
21	\end{figure}
22	
23	\textbf{Collapse trajectory.}
24	Figure~\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.
25	PR rises $32\%\to93\%\to96\%$, a trajectory execution-only evaluation would read as successful optimization; $\text{ISR}^*$ tells the opposite story, $0.642\to0.132\to0.003$ (214$\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
26	By 500 steps, 87.1\% of proved samples embed the conclusion (H1); by 1000 steps the embedding rate saturates at 100\% and mean component count more than doubles ($6.58\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.
27	Extended training, lacking a structural signal, \emph{worsens} formalization quality while improving the headline number.
28	
29	\textbf{Cross-seed instability.}
30	The three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\ref{app:detailed-results}): s42 reaches $\text{PR}{=}93\%$ via conclusion embedding ($\text{H1}{=}87\%$); s43 collapses to $\text{PR}{=}13\%$ via repetition (87\% of rollouts truncated); s44 reaches $\text{PR}{=}98\%$ via tautological collapse ($\text{H7}{=}100\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44
31	The cross-seed PR variance ($\sigma{=}47$\,pp) shows aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).
32	By 1000 steps, all three converge to high PR ($0.95{\pm}0.05$) but $0\%$ non-hacking (15 samples escape text-match classifiers but are functionally degenerate; see Appendix~\ref{app:h8} and Table~\ref{tab:fol-detailed}), each through a different dominant mode (s42: H1 saturation; s43: H7 tautology; s44: H1+H8). %% registry: plan016-extended-1000-s42, plan001-exec-only-s43-1000-r2, plan001-exec-only-s44-1000-r2
33	
34	\textbf{SFT baseline.}
35	SFT on gold formalizations reaches $\text{PR}{=}13.0\%$ (3-seed pooled, 1000 steps) with $\text{H7}{=}0$, $\text{H1}{=}7.7\%$, $92.3\%$ non-hacking ($n{=}39$; per-seed range 91--93\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
36	The near-absence of hacking under identical data exposure is consistent with hacking being RL-specific.
37	A 100-step RL checkpoint (Appendix~\ref{app:100step}) at $\text{PR}{=}32\%$ already shows 31.2\% hacking (vs.\ SFT's 7.7\%), indicating reward hacking emerges early in RL training, not merely at high PR.
38	
39	\subsection{Meta-Level Goodhart's Law}
40	\label{sec:goodhart}
41	
42	We now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with a matched random control, $r = r_{\text{exec}}\cdot(1 + \beta\,u)$, $u\sim\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.
43	The headline finding: ISR-as-reward produces \emph{meta-level} Goodhart~\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming.
44	
45	\begin{table}[t]
46	\centering
47	\small
48	\resizebox{\columnwidth}{!}{%
49	\begin{tabular}{lcccccc}
50	\toprule
51	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} \\
52	\midrule
53	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
54	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
55	\midrule
56	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)
57	ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
58	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 71 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
59	\midrule
60	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 12 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled)
61	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)
62	\bottomrule
63	\end{tabular}}
64	\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\pm$std of per-seed values. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ omitted for ISR $\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\times$ random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}). $^\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). $^\S$Random H7 driven by seed~43 (38.3\%); seeds~42 and~44: 0\%. Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}.}
65	\label{tab:goodhart-landscape}
66	\end{table}
67	
68	\textbf{Low-dose ISR ($\beta{=}0.1$): ISR-amplified gaming.}
69	H7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\sim}5\times$: $70.6\%$ ($163/231$) under ISR vs.\ $13.7\%$ ($36/262$) under random (Fisher $p{=}1.3{\times}10^{-39}$, $\text{OR}{=}15.05$). %% registry: plan002 vs plan018 all seeds; D095 FINAL
70	Random H7 is highly seed-dependent: $38.3\%$ in seed~43 vs.\ $0\%$ in seeds~42 and~44; ISR makes H7 near-deterministic ($2/3$ seeds at $97$--$100\%$, Table~\ref{tab:fol-detailed}).
71	H7---a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by construction (\S\ref{sec:taxonomy-method})---is the canonical meta-level Goodhart move: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.
72	Total conclusion embedding ($\text{H1}+\text{H7}$) is GRPO-universal at $68$--$100\%$ across both conditions, and is in fact \emph{higher} under random (pooled H1 $71\%$ vs.\ $18\%$ under ISR).
73	ISR does not reduce hacking; it converts H1 into H7 (Figure~\ref{fig:hacking-composition}).
74	Random also yields higher and more stable PR ($87{\pm}8\%$ vs.\ $77{\pm}14\%$).
75	
76	\textbf{Premise-count confound.}
77	The one ISR seed not dominated by H7 (s42) has raw $\text{ISR}^{*}{=}0.415$, $3.2\times$ its random control ($0.131$), suggesting genuine improvement.
78	This appearance is a premise-minimization artifact: ISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\ $8.46$ for random), and ISR rises mechanically as $n$ falls---when $n{=}2$, $\text{ISR}\geq 0.5$ by definition.
79	Restricting to non-hacking samples with $\geq{3}$ premises (eliminating the trivial-$n$ regime) gives $\text{ISR}^{*}{=}0.258$ for ISR vs.\ $0.243$ for random: a $1.06\times$ ratio, no meaningful advantage. %% D051 premise-count-matched analysis
80	After reclassifying premise-subset gaming (H8; Appendix~\ref{app:h8}) and correcting H7 classifier false negatives (s44, $n{=}12$; Appendix~\ref{app:hacking-modes}), ISR $\beta{=}0.1$ non-hacking rate ($6.06\%$, $14/231$) is numerically lower than random ($9.5\%$, $25/262$), but the difference is not statistically significant (Fisher $p{=}0.182$, two-sided, n.s.; Wilson 95\% CI: ISR $[3.6\%, 9.9\%]$, Random $[6.5\%, 13.7\%]$; Appendix Table~\ref{tab:bootstrap-ci}). %% D095 FINAL Fisher test
81	The key asymmetry is not in non-hacking rates but in gaming \emph{composition}: ISR converts stochastic H7 into near-deterministic convergence ($2/3$ seeds ${\geq}97\%$), while random H7 remains seed-dependent and H1-dominated.
82	The raw $3.2\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification
83	
84	\begin{figure}[t]
85	\centering
86	\includegraphics[width=0.95\columnwidth]{figures/fig5_training_isr_curves.pdf}
87	\caption{Training ISR trajectories across reward conditions. ISR $\beta{=}0.1$ seeds rise rapidly toward $\text{ISR}{\approx}1$ (meta-Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\text{ISR}{\geq}0.5$ by construction), not genuine structural quality; random $\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}
88	\label{fig:training-isr-curves}
89	\end{figure}
90	
91	\textbf{Temporal collapse under ISR $\beta{=}0.1$.}
92	Figure~\ref{fig:training-isr-curves} traces training ISR across conditions.
93	Extended training (1000 steps) reveals that ISR $\beta{=}0.1$'s genuine rate at 500 steps ($17.3\%$, seed~42) is transient: by step 1000, H7 gaming escalates from $16.0\%$ to $96.7\%$ while genuine rate collapses to $2.2\%$ ($n_{\text{comp}}$: $5.58{\to}2.89$).
94	The optimization converges to a fixed point where $\text{ISR}^{*}{=}0.88$, superficially suggesting structural improvement but reflecting near-complete tautological gaming.
95	This mirrors the exec-only 1000-step trajectory (\S\ref{sec:diagnostic}): both converge to ${\sim}0\%$ genuine proofs despite opposite ISR values ($0.88$ vs.\ $0.003$), demonstrating that ISR is gamed upward under ISR-as-reward and downward under exec-only---two paths to the same structural collapse. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
96	
97	\textbf{High-dose ISR ($\beta{=}0.3$): multi-modal Goodhart.}
98	At $\beta{=}0.3$, ISR-as-reward produces extreme cross-seed instability ($\text{PR}{=}66{\pm}42\%$, spanning 18--95\%); each seed converges to a distinct pathway (Appendix~\ref{app:detailed-results}). %% registry: plan002-additive-b03-s42/s43/s44
99	Seed~42: \emph{reward collapse} ($\text{PR}{=}18\%$), the classical pattern of~\citep{gao-reward-overoptimization}.
100	Seed~43: \emph{H1 shortcutting} ($\text{PR}{=}86\%$, $\text{H1}{=}69\%$, only $27\%$ non-hacking).
101	Seed~44: \emph{pure H7 meta-Goodhart} ($\text{PR}{=}95\%$, $\text{H7}{=}100\%$, $\text{ISR}^{*}{=}0.742$, $0\%$ non-hacking)---simultaneously gaming \emph{both} execution and structural metrics through the same construction.
102	The random control at $\beta{=}0.3$ is equally unstable ($\text{PR}{=}54{\pm}35\%$, spanning 23--92\%) with near-universal H1 hacking ($91\%$, pooled) and ${\leq}4\%$ non-hacking per seed; high-dose proxy weighting destabilizes training regardless of signal source; ISR produces diverse failure modes (reward collapse, H1 shortcutting, H7 meta-Goodhart) while random converges to H1-dominated hacking with sporadic H7 ($7\%$ pooled, $0$--$7$ H7a per seed) (Appendix~\ref{app:beta03}).
103	
104	\subsection{Cross-Logic Diagnostic Transfer}
105	\label{sec:crosslogic}
106	
107	\begin{figure}[t]
108	\centering
109	\includegraphics[width=0.95\columnwidth]{figures/fig4_prolog_comparison.pdf}
110	\caption{Cross-logic results. \textbf{Left}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$). \textbf{Right}: Prolog ISR-reward gaming-mode composition---all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
111	\label{fig:prolog-comparison}
112	\end{figure}
113	
114	We replicate the FOL pipeline with Prolog/SWI-Prolog: (i) does ISR retain diagnostic value on a structurally different logic; (ii) does ISR-as-reward reproduce meta-level Goodhart?
115	Detailed per-seed numbers are in Appendix Table~\ref{tab:prolog-detailed}.
116	
117	\textbf{Prolog exec-only: ISR catches redundancy across logics.}
118	Two of three seeds (s42, s43) show $\text{ISR}^{*}{\approx}0$ despite moderate-to-high PR (0.83, 0.56). %% registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3
119	Inspection reveals \emph{redundant coding}: ground facts repeated multiple times (e.g., \texttt{penguin(fido).} appearing three times), so per-clause LOO never breaks the proof.
120	This is a different failure semantics from FOL exec-only (conclusion embedding), but $\text{ISR}^{*}$ flags both.
121	We are careful to distinguish: exec-only \emph{low} ISR signals \emph{redundancy}; ISR-rewarded \emph{high} ISR signals \emph{metric gaming} (\S\ref{sec:taxonomy-method})---the same number does not license the same reasoning-quality conclusion.
122	
123	\textbf{Prolog ISR-as-reward: universal Goodhart.}
124	The Prolog result is stronger than FOL: 3/3 seeds reach $0\%$ non-hacking via three distinct mechanisms (Figure~\ref{fig:prolog-comparison}).
125	Seed~42: clean H7 tautologies ($\text{ISR}^{*}{=}1.0$, all $50/100$ proved). %% registry: plan006-prolog-sta-s42
126	Seed~43: \emph{degenerate uppercase pseudo-Prolog} (e.g., \texttt{MARY\_IS\_AN\_AVA\-DEOTE.}); strict text-match returns $\text{H7}{=}0$ but functional analysis shows all 38 proved samples have $n_{\text{necessary}}{=}1$ (functionally H7). %% registry: plan006-prolog-sta-s43
127	Seed~44: \emph{query-as-fact gaming}---the model transforms the NL question into a snake-case atom asserted as both fact and query (e.g., \texttt{is\_the\_dog\_furry.} as both fact and query), with $95/97$ proved samples at $n_{\text{necessary}}{=}1$. %% registry: plan006-prolog-sta-s44
128	Seed~44 evaded our initial strict classifier (reported $100\%$ genuine); functional cross-validation exposed it---a methodological lesson that text-match classifiers have blind spots and STA's necessity profile is the cross-check.
129	We attribute Prolog's stronger collapse to its simpler operational semantics: a broader gaming basin makes the genuine residual disappear---corroborating evidence for Claim 2.
130	
131	\subsection{Hacking Taxonomy}
132	\label{sec:taxonomy}
133	
134	\begin{figure}[t]
135	\centering
136	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
137	\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR converts H1 into more extreme H7 without reducing total hacking; SFT shows near-zero hacking.}
138	\label{fig:hacking-composition}
139	\end{figure}
140	
141	\begin{table}[t]
142	\centering
143	\small
144	\resizebox{\columnwidth}{!}{%
145	\begin{tabular}{lccccc}
146	\toprule
147	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} \\
148	\midrule
149	H1 embed       & 87 & 18 & 71 & 7 & 0$^\sharp$ \\
150	H7 duplicate   & 0  & 71 & 14 & 0 & 100$^\sharp$ \\
151	H8 prem-subset & 6  & 5  & 8   & 0 & --- \\
152	Tautological   & --- & --- & --- & --- & s42 \\
153	Repetition     & s43 & --- & --- & --- & --- \\
154	Contradiction  & 1k & --- & --- & --- & --- \\
155	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- \\
156	Query-as-fact  & --- & --- & --- & --- & s44 \\
157	\midrule
158	\textbf{Non-hacking} & 8  & 6  & 10 & \textbf{92} & \textbf{0} \\
159	\bottomrule
160	\end{tabular}}
161	\caption{Eight hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}).}
162	\label{tab:hacking-taxonomy}
163	\end{table}
164	
165	The eight modes (Table~\ref{tab:hacking-taxonomy}; full definitions in Appendix~\ref{app:hacking-modes}) span the studied conditions.
166	Three are quantifiable across conditions: \textbf{H1} (conclusion embedding) is GRPO-universal at $68$--$100\%$ regardless of reward type; \textbf{H7} (conclusion duplication) occurs under both ISR and random but ISR amplifies it ${\sim}5\times$ ($70.6\%$ vs.\ $13.7\%$ under random; Fisher $p{=}1.3{\times}10^{-39}$), with random H7 concentrated in a single seed (s43: $38.3\%$; s42, s44: $0\%$); \textbf{H8} (premise-subset gaming) appears under both exec-only ($6\%$) and ISR ($5\%$) conditions (Appendix~\ref{app:h8}).
167	H7 splits into \textbf{H7a} (standard, text-match detectable; $64.5\%$ of ISR proved, $149/231$) and \textbf{H7b} (obfuscated tautology; $6.06\%$, $14/231$): H7b samples use vacuous quantifier wrapping or structural simplification to evade the text-match classifier while remaining logically equivalent (s44: $11/12$ quantifier wrapping, $1/12$ structural; s43: $2$), with $10/12$ (s44) achieving $\text{ISR}{\approx}0.8$---simultaneously gaming execution reward, ISR metric, and hacking detector.
168	The remaining five appear in specific cells: tautological collapse (exec-only s44, Prolog ISR s42), repetition (exec-only s43), contradiction explosion (exec-only at 1000 steps), complexity-without-utility (random $\beta{=}0.1$ residual), and query-as-fact gaming (Prolog ISR s44).
169	
170	The cross-condition pattern is consistent with \S\ref{sec:goodhart}: \emph{reward formulation determines hacking composition but not hacking prevalence.}
171	Exec-only, ISR, and random conditions all show $\geq 80\%$ pooled hacking among proved samples; only SFT shows $92.3\%$ non-hacking.
172	Across 2 logic types, 6 reward conditions, 3 seeds, and up to 1000 steps, no GRPO condition we tested produces a high-PR run that is also majority non-hacking; the closest is random $\beta{=}0.1$ s42 at $\text{PR}{=}79\%$, $22.8\%$ non-hacking, and ISR $\beta{=}0.1$ s42 at $\text{PR}{=}81\%$, $17.3\%$ non-hacking---both residuals are the premise-minimization artifact analyzed above.
173	Query-as-fact gaming was found only when we cross-validated the strict classifier against $n_{\text{necessary}}$ distributions, suggesting the taxonomy is descriptive, not exhaustive.
174	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "3a43bc26-d2f4-475b-bd96-37976605d63b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits meta-level Goodhart's Law (\\S\\ref{sec:goodhart}); and STA as a cross-logic protocol (\\S\\ref{sec:crosslogic}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}8$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline is trained with NLL on gold formalizations.\\footnote{All experiments use \\texttt{data/train\\_500\\_seed42.jsonl}; seeds control initialization and rollout sampling only.}\nHeld-out evaluation uses 100 FOLIO examples (\\texttt{proofwriter\\_fol\\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\\texttt{eval\\_sta.py}) so training-log ISR is never compared across runs.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary but not sufficient condition for semantic correctness.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$93\\%$\\to$96\\% while proved-only ISR falls $0.642{\\to}0.132{\\to}0.003$ over 100$\\to$500$\\to$1000 steps. By step 1000, 94.8\\% of proved samples have $\\text{ISR}{=}0$ and mean component count inflates 6.58$\\to$18.55 (contradiction explosion).}\n\\label{fig:isr-collapse}\n\\end{figure}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory execution-only evaluation would read as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (H1); by 1000 steps the embedding rate saturates at 100\\% and mean component count more than doubles ($6.58\\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.\nExtended training, lacking a structural signal, \\emph{worsens} formalization quality while improving the headline number.\n\n\\textbf{Cross-seed instability.}\nThe three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\\ref{app:detailed-results}): s42 reaches $\\text{PR}{=}93\\%$ via conclusion embedding ($\\text{H1}{=}87\\%$); s43 collapses to $\\text{PR}{=}13\\%$ via repetition (87\\% of rollouts truncated); s44 reaches $\\text{PR}{=}98\\%$ via tautological collapse ($\\text{H7}{=}100\\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44\nThe cross-seed PR variance ($\\sigma{=}47$\\,pp) shows aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).\nBy 1000 steps, all three converge to high PR ($0.95{\\pm}0.05$) but $0\\%$ non-hacking (15 samples escape text-match classifiers but are functionally degenerate; see Appendix~\\ref{app:h8} and Table~\\ref{tab:fol-detailed}), each through a different dominant mode (s42: H1 saturation; s43: H7 tautology; s44: H1+H8). %% registry: plan016-extended-1000-s42, plan001-exec-only-s43-1000-r2, plan001-exec-only-s44-1000-r2\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $\\text{PR}{=}13.0\\%$ (3-seed pooled, 1000 steps) with $\\text{H7}{=}0$, $\\text{H1}{=}7.7\\%$, $92.3\\%$ non-hacking ($n{=}39$; per-seed range 91--93\\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\nThe near-absence of hacking under identical data exposure is consistent with hacking being RL-specific.\nA 100-step RL checkpoint (Appendix~\\ref{app:100step}) at $\\text{PR}{=}32\\%$ already shows 31.2\\% hacking (vs.\\ SFT's 7.7\\%), indicating reward hacking emerges early in RL training, not merely at high PR.\n\n\\subsection{Meta-Level Goodhart's Law}\n\\label{sec:goodhart}\n\nWe now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with a matched random control, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,u)$, $u\\sim\\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.\nThe headline finding: ISR-as-reward produces \\emph{meta-level} Goodhart~\\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)\nISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 12 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}}\n\\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std of per-seed values. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ omitted for ISR $\\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\\times$ random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}). $^\\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random H7 driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}.}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-amplified gaming.}\nH7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\\sim}5\\times$: $70.6\\%$ ($163/231$) under ISR vs.\\ $13.7\\%$ ($36/262$) under random (Fisher $p{=}1.3{\\times}10^{-39}$, $\\text{OR}{=}15.05$). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nRandom H7 is highly seed-dependent: $38.3\\%$ in seed~43 vs.\\ $0\\%$ in seeds~42 and~44; ISR makes H7 near-deterministic ($2/3$ seeds at $97$--$100\\%$, Table~\\ref{tab:fol-detailed}).\nH7---a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by construction (\\S\\ref{sec:taxonomy-method})---is the canonical meta-level Goodhart move: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$100\\%$ across both conditions, and is in fact \\emph{higher} under random (pooled H1 $71\\%$ vs.\\ $18\\%$ under ISR).\nISR does not reduce hacking; it converts H1 into H7 (Figure~\\ref{fig:hacking-composition}).\nRandom also yields higher and more stable PR ($87{\\pm}8\\%$ vs.\\ $77{\\pm}14\\%$).\n\n\\textbf{Premise-count confound.}\nThe one ISR seed not dominated by H7 (s42) has raw $\\text{ISR}^{*}{=}0.415$, $3.2\\times$ its random control ($0.131$), suggesting genuine improvement.\nThis appearance is a premise-minimization artifact: ISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\\ $8.46$ for random), and ISR rises mechanically as $n$ falls---when $n{=}2$, $\\text{ISR}\\geq 0.5$ by definition.\nRestricting to non-hacking samples with $\\geq{3}$ premises (eliminating the trivial-$n$ regime) gives $\\text{ISR}^{*}{=}0.258$ for ISR vs.\\ $0.243$ for random: a $1.06\\times$ ratio, no meaningful advantage. %% D051 premise-count-matched analysis\nAfter reclassifying premise-subset gaming (H8; Appendix~\\ref{app:h8}) and correcting H7 classifier false negatives (s44, $n{=}12$; Appendix~\\ref{app:hacking-modes}), ISR $\\beta{=}0.1$ non-hacking rate ($6.06\\%$, $14/231$) is numerically lower than random ($9.5\\%$, $25/262$), but the difference is not statistically significant (Fisher $p{=}0.182$, two-sided, n.s.; Wilson 95\\% CI: ISR $[3.6\\%, 9.9\\%]$, Random $[6.5\\%, 13.7\\%]$; Appendix Table~\\ref{tab:bootstrap-ci}). %% D095 FINAL Fisher test\nThe key asymmetry is not in non-hacking rates but in gaming \\emph{composition}: ISR converts stochastic H7 into near-deterministic convergence ($2/3$ seeds ${\\geq}97\\%$), while random H7 remains seed-dependent and H1-dominated.\nThe raw $3.2\\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{Training ISR trajectories across reward conditions. ISR $\\beta{=}0.1$ seeds rise rapidly toward $\\text{ISR}{\\approx}1$ (meta-Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\\text{ISR}{\\geq}0.5$ by construction), not genuine structural quality; random $\\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\n\\textbf{Temporal collapse under ISR $\\beta{=}0.1$.}\nFigure~\\ref{fig:training-isr-curves} traces training ISR across conditions.\nExtended training (1000 steps) reveals that ISR $\\beta{=}0.1$'s genuine rate at 500 steps ($17.3\\%$, seed~42) is transient: by step 1000, H7 gaming escalates from $16.0\\%$ to $96.7\\%$ while genuine rate collapses to $2.2\\%$ ($n_{\\text{comp}}$: $5.58{\\to}2.89$).\nThe optimization converges to a fixed point where $\\text{ISR}^{*}{=}0.88$, superficially suggesting structural improvement but reflecting near-complete tautological gaming.\nThis mirrors the exec-only 1000-step trajectory (\\S\\ref{sec:diagnostic}): both converge to ${\\sim}0\\%$ genuine proofs despite opposite ISR values ($0.88$ vs.\\ $0.003$), demonstrating that ISR is gamed upward under ISR-as-reward and downward under exec-only---two paths to the same structural collapse. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\n\n\\textbf{High-dose ISR ($\\beta{=}0.3$): multi-modal Goodhart.}\nAt $\\beta{=}0.3$, ISR-as-reward produces extreme cross-seed instability ($\\text{PR}{=}66{\\pm}42\\%$, spanning 18--95\\%); each seed converges to a distinct pathway (Appendix~\\ref{app:detailed-results}). %% registry: plan002-additive-b03-s42/s43/s44\nSeed~42: \\emph{reward collapse} ($\\text{PR}{=}18\\%$), the classical pattern of~\\citep{gao-reward-overoptimization}.\nSeed~43: \\emph{H1 shortcutting} ($\\text{PR}{=}86\\%$, $\\text{H1}{=}69\\%$, only $27\\%$ non-hacking).\nSeed~44: \\emph{pure H7 meta-Goodhart} ($\\text{PR}{=}95\\%$, $\\text{H7}{=}100\\%$, $\\text{ISR}^{*}{=}0.742$, $0\\%$ non-hacking)---simultaneously gaming \\emph{both} execution and structural metrics through the same construction.\nThe random control at $\\beta{=}0.3$ is equally unstable ($\\text{PR}{=}54{\\pm}35\\%$, spanning 23--92\\%) with near-universal H1 hacking ($91\\%$, pooled) and ${\\leq}4\\%$ non-hacking per seed; high-dose proxy weighting destabilizes training regardless of signal source; ISR produces diverse failure modes (reward collapse, H1 shortcutting, H7 meta-Goodhart) while random converges to H1-dominated hacking with sporadic H7 ($7\\%$ pooled, $0$--$7$ H7a per seed) (Appendix~\\ref{app:beta03}).\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Left}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$). \\textbf{Right}: Prolog ISR-reward gaming-mode composition---all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\nWe replicate the FOL pipeline with Prolog/SWI-Prolog: (i) does ISR retain diagnostic value on a structurally different logic; (ii) does ISR-as-reward reproduce meta-level Goodhart?\nDetailed per-seed numbers are in Appendix Table~\\ref{tab:prolog-detailed}.\n\n\\textbf{Prolog exec-only: ISR catches redundancy across logics.}\nTwo of three seeds (s42, s43) show $\\text{ISR}^{*}{\\approx}0$ despite moderate-to-high PR (0.83, 0.56). %% registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3\nInspection reveals \\emph{redundant coding}: ground facts repeated multiple times (e.g., \\texttt{penguin(fido).} appearing three times), so per-clause LOO never breaks the proof.\nThis is a different failure semantics from FOL exec-only (conclusion embedding), but $\\text{ISR}^{*}$ flags both.\nWe are careful to distinguish: exec-only \\emph{low} ISR signals \\emph{redundancy}; ISR-rewarded \\emph{high} ISR signals \\emph{metric gaming} (\\S\\ref{sec:taxonomy-method})---the same number does not license the same reasoning-quality conclusion.\n\n\\textbf{Prolog ISR-as-reward: universal Goodhart.}\nThe Prolog result is stronger than FOL: 3/3 seeds reach $0\\%$ non-hacking via three distinct mechanisms (Figure~\\ref{fig:prolog-comparison}).\nSeed~42: clean H7 tautologies ($\\text{ISR}^{*}{=}1.0$, all $50/100$ proved). %% registry: plan006-prolog-sta-s42\nSeed~43: \\emph{degenerate uppercase pseudo-Prolog} (e.g., \\texttt{MARY\\_IS\\_AN\\_AVA\\-DEOTE.}); strict text-match returns $\\text{H7}{=}0$ but functional analysis shows all 38 proved samples have $n_{\\text{necessary}}{=}1$ (functionally H7). %% registry: plan006-prolog-sta-s43\nSeed~44: \\emph{query-as-fact gaming}---the model transforms the NL question into a snake-case atom asserted as both fact and query (e.g., \\texttt{is\\_the\\_dog\\_furry.} as both fact and query), with $95/97$ proved samples at $n_{\\text{necessary}}{=}1$. %% registry: plan006-prolog-sta-s44\nSeed~44 evaded our initial strict classifier (reported $100\\%$ genuine); functional cross-validation exposed it---a methodological lesson that text-match classifiers have blind spots and STA's necessity profile is the cross-check.\nWe attribute Prolog's stronger collapse to its simpler operational semantics: a broader gaming basin makes the genuine residual disappear---corroborating evidence for Claim 2.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts H1 into more extreme H7 without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nH1 embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nH7 duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nH8 prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThe eight modes (Table~\\ref{tab:hacking-taxonomy}; full definitions in Appendix~\\ref{app:hacking-modes}) span the studied conditions.\nThree are quantifiable across conditions: \\textbf{H1} (conclusion embedding) is GRPO-universal at $68$--$100\\%$ regardless of reward type; \\textbf{H7} (conclusion duplication) occurs under both ISR and random but ISR amplifies it ${\\sim}5\\times$ ($70.6\\%$ vs.\\ $13.7\\%$ under random; Fisher $p{=}1.3{\\times}10^{-39}$), with random H7 concentrated in a single seed (s43: $38.3\\%$; s42, s44: $0\\%$); \\textbf{H8} (premise-subset gaming) appears under both exec-only ($6\\%$) and ISR ($5\\%$) conditions (Appendix~\\ref{app:h8}).\nH7 splits into \\textbf{H7a} (standard, text-match detectable; $64.5\\%$ of ISR proved, $149/231$) and \\textbf{H7b} (obfuscated tautology; $6.06\\%$, $14/231$): H7b samples use vacuous quantifier wrapping or structural simplification to evade the text-match classifier while remaining logically equivalent (s44: $11/12$ quantifier wrapping, $1/12$ structural; s43: $2$), with $10/12$ (s44) achieving $\\text{ISR}{\\approx}0.8$---simultaneously gaming execution reward, ISR metric, and hacking detector.\nThe remaining five appear in specific cells: tautological collapse (exec-only s44, Prolog ISR s42), repetition (exec-only s43), contradiction explosion (exec-only at 1000 steps), complexity-without-utility (random $\\beta{=}0.1$ residual), and query-as-fact gaming (Prolog ISR s44).\n\nThe cross-condition pattern is consistent with \\S\\ref{sec:goodhart}: \\emph{reward formulation determines hacking composition but not hacking prevalence.}\nExec-only, ISR, and random conditions all show $\\geq 80\\%$ pooled hacking among proved samples; only SFT shows $92.3\\%$ non-hacking.\nAcross 2 logic types, 6 reward conditions, 3 seeds, and up to 1000 steps, no GRPO condition we tested produces a high-PR run that is also majority non-hacking; the closest is random $\\beta{=}0.1$ s42 at $\\text{PR}{=}79\\%$, $22.8\\%$ non-hacking, and ISR $\\beta{=}0.1$ s42 at $\\text{PR}{=}81\\%$, $17.3\\%$ non-hacking---both residuals are the premise-minimization artifact analyzed above.\nQuery-as-fact gaming was found only when we cross-validated the strict classifier against $n_{\\text{necessary}}$ distributions, suggesting the taxonomy is descriptive, not exhaustive.\n",
      "numLines": 174,
      "startLine": 1,
      "totalLines": 174
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01JrRrcVjHHXwzwd7Ua9MkZ3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "0d0e109e-4e9a-49c5-a96d-3089318acfe9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bcf7w5nUYFNozXfnsFmSay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7696,
      "cache_read_input_tokens": 49511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7696
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T21:29:49.865Z_

<details><summary>↩ Tool result · `toolu_01JrRrcVjHHXwzwd7Ua9MkZ3`</summary>

```text
1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 8 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
55	
56	
57	\section{STA Algorithm}
58	\label{app:algorithm}
59	
60	Algorithm~\ref{alg:sta} (Section~\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.
61	For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.
62	
63	
64	\section{Extended Discussion}
65	\label{app:extended-discussion}
66	
67	\paragraph{What ISR measures---and what it does not.}
68	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
69	This is strictly weaker than semantic faithfulness---whether the formalization accurately captures the natural-language meaning.
70	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
71	ISR and downstream task performance are uncorrelated.
72	ISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
73	
74	Critically, low ISR carries different semantics depending on the training objective.
75	Under exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\S\ref{sec:crosslogic}).
76	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
77	ISR values must always be interpreted relative to the optimization objective that produced them.
78	
79	\paragraph{The premise-count confound.}
80	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
81	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$---even though the latter encodes richer reasoning.
82	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
83	Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:fol-beta01-detailed}).
84	This bias is not specific to our setting---any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
85	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
86	
87	\begin{table}[h]
88	\centering
89	\caption{Fisher exact tests for genuine rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ genuine rate is corrected for H8 reclassification and H7 false negatives (Appendix~\ref{app:h8}).}
90	\label{tab:bootstrap-ci}
91	\small
92	\begin{tabular}{@{}lcccc@{}}
93	\toprule
94	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
95	\midrule
96	\multicolumn{5}{@{}l}{\textit{Genuine rate (H8+FN corrected)}} \\
97	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
98	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
99	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
100	\midrule
101	\multicolumn{5}{@{}l}{\textit{H7 gaming rate}} \\
102	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
103	\midrule
104	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only genuine rate}} \\
105	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
106	\bottomrule
107	\end{tabular}
108	\\[2pt]
109	{\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
110	\end{table}
111	
112	\paragraph{Meta-level Goodhart: implications.}
113	The meta-Goodhart finding extends beyond this specific system.
114	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.
115	The dose-response pattern ($\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\beta{=}0.3$: PR collapse to 18\% vs.\ 48\% random) maps onto the trajectory predicted by~\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.
116	$\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism; $\beta{=}0.3$ completes the Goodhart trajectory with outright performance collapse.
117	The practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.
118	
119	\paragraph{Single-seed unreliability.}
120	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
121	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\S\ref{sec:goodhart}).
122	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
123	
124	
125	\section{Hacking Mode Definitions}
126	\label{app:hacking-modes}
127	
128	We identify eight distinct reward hacking modes across all experiments.
129	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
130	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
131	
132	\begin{table}[h]
133	\centering
134	\small
135	\resizebox{\columnwidth}{!}{%
136	\begin{tabular}{@{}llcccc@{}}
137	\toprule
138	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
139	\midrule
140	H1 & Concl.\ in premises & 87 & 18 & 71 & 7 \\
141	H7 & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
142	H8 & Premise-subset gaming & 6 & 5 & -- & 0 \\
143	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
144	Repetition & Output degen. & $\bullet$ & -- & -- & -- \\
145	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & -- & -- & -- \\
146	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
147	Q-as-fact & Atom = fact+query & -- & -- & -- & -- \\
148	\bottomrule
149	\end{tabular}}
150	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. H7 includes subtypes H7a (text-match, $n{=}149$ ISR $+$ 36 random) and H7b (obfuscated tautology, $n{=}12$; ISR s44 only). $^\dagger$Random H7 driven by seed~43 (38.3\%); seeds~42/44: 0\%. Exec: H1${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). H8: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
151	\label{tab:hacking-taxonomy-app}
152	\end{table}
153	
154	\paragraph{Classifier Validation.}
155	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
156	H1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
157	No training data or manual annotation is used for classification.
158	
159	To estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
160	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
161	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
162	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
163	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
164	
165	\subsection{H8 --- Premise-Subset Gaming}
166	\label{app:h8}
167	
168	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (H1-style).
169	We term this \textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
170	
171	\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
172	Automated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.
173	
174	\paragraph{Audit scope and limitations.}
175	Full H8 audit was completed for ISR $\beta{=}0.1$ seed~42 only.
176	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their genuine rates may be overestimated.
177	Random $\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.
178	
179	\paragraph{H7 false-negative correction (H7b obfuscated tautology).}
180	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as genuine by the text matcher.
181	Manual inspection confirmed all 12 are logically equivalent to H7 but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
182	We classify these as \textbf{H7b} (obfuscated tautology), distinct from text-match-detectable H7a.
183	$10/12$ achieve $\text{ISR}{\approx}0.8$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier---triple gaming (\S\ref{sec:taxonomy}).
184	After correction, ISR s44 genuine${=}0$; total H7 = H7a (77 text-match) + H7b (12 obfuscated) = 89.
185	
186	\paragraph{Impact on genuine-rate comparison.}
187	After H8 reclassification and H7 false-negative correction: ISR genuine $= 14/231 = 6.06\%$ vs.\ random genuine $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
188	The direction is consistent with ISR-amplified gaming modes (H7, H8) displacing genuine output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
189	
190	\subsection{H1 --- Conclusion Embedding}
191	
192	\paragraph{Definition.}
193	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
194	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
195	
196	\paragraph{Example (FOL).}
197	{\small\begin{verbatim}
198	Premises:
199	  all x (bird(x) -> flies(x)).
200	  bird(tweety).
201	  flies(tweety).  % conclusion embedded
202	Conclusion: flies(tweety).
203	\end{verbatim}}
204	
205	\paragraph{ISR interaction.}
206	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
207	ISR does not distinguish trivial from substantive necessity.
208	
209	\paragraph{Prevalence.}
210	Conclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\% across all RL conditions.
211	Under exec-only and Random reward, it manifests as H1 (71--93\%); under ISR reward, it shifts to H7 (70.6\% pooled).
212	
213	
214	\subsection{H7a --- Conclusion Duplication (Standard)}
215	
216	\paragraph{Definition.}
217	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
218	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
219	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
220	
221	\paragraph{Example (FOL).}
222	{\small\begin{verbatim}
223	Premises:
224	  all x ((A(x)&B(x))->(C(x)|D(x))).
225	Conclusion:
226	  all x ((A(x)&B(x))->(C(x)|D(x))).
227	\end{verbatim}}
228	
229	\paragraph{ISR interaction.}
230	ISR~$\approx 0.8$--$1.0$.
231	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
232	H7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.
233	
234	\paragraph{Prevalence.}
235	H7a (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
236	Combined H7 (H7a + H7b): 70.6\% (163/231; s43 H7a${=}59$ + H7b${=}2$; includes s44 FN correction).
237	Random~$\beta{=}0.1$ pooled: 13.7\% (36/262, all H7a; driven by seed~43 at 38.3\%, seeds~42 and~44 at 0\%).
238	
239	
240	\subsection{H7b --- Obfuscated Tautology}
241	
242	\paragraph{Definition.}
243	A single-premise formalization logically equivalent to H7a (premise = conclusion) but with surface-form differences that evade the text-match H7 classifier.
244	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
245	
246	\paragraph{Example (FOL, vacuous quantifier wrapping).}
247	{\small\begin{verbatim}
248	Premises:
249	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
250	Conclusion:
251	  all x ((A(x)&B(x))->(C(x)|D(x))).
252	\end{verbatim}}
253	The premise introduces a vacuous second quantifier variable $y$ that is immediately unified with $x$, making the formulas logically equivalent while differing textually.
254	
255	\paragraph{ISR interaction.}
256	ISR~$\approx 0.8$ ($10/12$ samples).
257	H7b simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match H7 classifier (surface-form difference evades detection).
258	This triple gaming makes H7b the most complete meta-Goodhart case we observe.
259	
260	\paragraph{Prevalence.}
261	Found exclusively in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as genuine).
262	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
263	
264	
265	\subsection{Tautological Collapse}
266	
267	\paragraph{Definition.}
268	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
269	
270	\paragraph{Example (FOL).}
271	\begin{verbatim}
272	Premises: p(a).
273	Conclusion: p(a).
274	\end{verbatim}
275	
276	\paragraph{ISR interaction.}
277	ISR~$=1.0$ (the sole premise is necessary).
278	Distinguished from H7 by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
279	
280	\paragraph{Prevalence.}
281	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% H7 by strict classifier).
282	Also observed in Prolog exec+STA seed~42 (100\% H7, PR~$=0.50$).
283	
284	
285	\subsection{Repetition Collapse}
286	
287	\paragraph{Definition.}
288	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
289	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
290	
291	\paragraph{Example (Prolog).}
292	\begin{verbatim}
293	penguin(fido).
294	penguin(fido).
295	penguin(fido).
296	... (repeated to 512 tokens)
297	query(penguin(fido)).
298	\end{verbatim}
299	
300	\paragraph{ISR interaction.}
301	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
302	ISR correctly diagnoses this degeneration.
303	
304	\paragraph{Prevalence.}
305	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
306	
307	
308	\subsection{Complexity-without-Utility}
309	
310	\paragraph{Definition.}
311	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.
312	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
313	
314	\paragraph{Example (FOL).}
315	{\small\begin{verbatim}
316	Premises:
317	  all x all y (R(x,y) ->
318	    exists z (S(x,z) & T(z,y))).
319	  all x (P(x) -> Q(x)).
320	  P(a).            % only this needed
321	Conclusion: Q(a).
322	\end{verbatim}}
323	
324	\paragraph{ISR interaction.}
325	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
326	This is the mode ISR is best calibrated for.
327	
328	\paragraph{Prevalence.}
329	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
330	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
331	
332	
333	\subsection{Contradiction Explosion}
334	
335	\paragraph{Definition.}
336	The component count grows unboundedly over training.
337	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
338	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
339	
340	\paragraph{Example (FOL, 1000-step exec-only).}
341	{\small\begin{verbatim}
342	Premises:
343	  c1. c2. c3. ... c18. % 18.55 mean
344	  % conclusion embedded among premises
345	Conclusion: Q(a).
346	\end{verbatim}}
347	
348	\paragraph{ISR interaction.}
349	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
350	
351	\paragraph{Prevalence.}
352	Observed in extended exec-only training (seed~42, 1000 steps).
353	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
354	
355	
356	\subsection{Query-as-Fact Gaming}
357	
358	\paragraph{Definition.}
359	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
360	Prolog trivially proves the query by unifying with the fact.
361	This mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.
362	
363	\paragraph{Example (Prolog).}
364	\begin{verbatim}
365	% NL: "Fido is happy."
366	% Model output:
367	fido_is_happy.
368	:- fido_is_happy.     % query = fact
369	\end{verbatim}
370	
371	\paragraph{ISR interaction.}
372	ISR~$\approx 0.9$--$1.0$.
373	The fact is necessarily necessary (its removal breaks the query), inflating ISR.
374	Functionally equivalent to H7 but with a distinct surface mechanism.
375	
376	\paragraph{Prevalence.}
377	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
378	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
379	
380	
381	\section{Per-Seed Detailed Results}
382	\label{app:detailed-results}
383	
384	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
385	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
386	ISR values are proved-only ISR$^*$.
387	
388	\begin{table*}[t]
389	\centering
390	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\S$s43-1000 raw ISR (0.531) includes ${+}12\%$ inflation from \texttt{decompose\_fol()} splitting $\exists x(\ldots)$ conclusions into quantifier + body as separate ablatable components; corrected ISR removes this artifact.}
391	\label{tab:fol-detailed}
392	\label{tab:fol-beta01-detailed}
393	\footnotesize
394	\setlength{\tabcolsep}{3pt}
395	\begin{tabular}{@{}llccccccl@{}}
396	\toprule
397	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
398	\midrule
399	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
400	Base model (no training)
401	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
402	Ground-truth FOL
403	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
404	SFT
405	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
406	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
407	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
408	\cmidrule(l){2-9}
409	  & \multicolumn{2}{l}{3-seed pooled} & \makebox[0pt][l]{$0.130$} & & \makebox[0pt][l]{$0.595$} & & \makebox[0pt][l]{\textbf{92.3}} & $n{=}39$ proved \\
410	\midrule
411	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
412	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
413	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\%$ \\
414	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
415	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
416	  & 43 & 1000 & 0.90 & 0.465$^\S$ & 100 & 0 & 0 & H7 dominant \\
417	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
418	  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & H8${=}15\%$ \\
419	\cmidrule(l){2-9}
420	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.68{\pm}0.47$} & & \makebox[0pt][l]{$0.238{\pm}0.30$} & & & 500-step \\
421	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.95{\pm}0.05$} & & \makebox[0pt][l]{$0.16{\pm}0.27$} & & \makebox[0pt][l]{$0.0{\pm}0.0$} & 1000-step \\
422	\midrule
423	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
424	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed H1+H7+H8 \\
425	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & H7a${=}59$, H7b${=}2$ \\
426	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & H7 dominant (FN corrected) \\
427	\cmidrule(l){2-9}
428	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.77{\pm}0.14$} & & \makebox[0pt][l]{$0.716{\pm}0.26$} & & & \\
429	\midrule
430	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
431	  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\
432	\midrule
433	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
434	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\
435	  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & H7a${=}36$; H8${=}1$ \\
436	  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & H8${=}16$ (H1$\cap$H8: 6) \\
437	\cmidrule(l){2-9}
438	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.87{\pm}0.08$} & & \makebox[0pt][l]{$0.117{\pm}0.042$} & & & H7 seed-dep.: 0/38/0\% \\
439	\midrule
440	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
441	  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086); $n_{\text{comp}} = 9.6$ \\
442	  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\text{genuine}}{=}3$ \\
443	  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\
444	\cmidrule(l){2-9}
445	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.54{\pm}0.35$} & & \makebox[0pt][l]{$0.09{\pm}0.09$} & & & \\
446	\bottomrule
447	\end{tabular}
448	\end{table*}
449	
450	
451	\begin{table*}[t]
452	\centering
453	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
454	\label{tab:prolog-detailed}
455	\small
456	\begin{tabular}{@{}llcccccl@{}}
457	\toprule
458	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
459	\midrule
460	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
461	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
462	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
463	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
464	\cmidrule(l){2-8}
465	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.53{\pm}0.31$} & & \makebox[0pt][l]{$0.146{\pm}0.21$} & & \\
466	\midrule
467	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
468	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & H7 tautological \\
469	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional H7$^a$ \\
470	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
471	\cmidrule(l){2-8}
472	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.62{\pm}0.31$} & & \makebox[0pt][l]{$0.699{\pm}0.45$} & & 3/3 Goodhart, 0\% non-hacking \\
473	\bottomrule
474	\end{tabular}
475	
476	\vspace{4pt}
477	{\footnotesize
478	$^a$ Strict H7 classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
479	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\
480	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
481	}
482	\end{table*}
483	
484	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
485	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
486	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
487	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.
488	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
489	
490	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
491	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
492	seed~42 produces clean H7 tautologies (single premise~$=$~conclusion),
493	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
494	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
495	The diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
496	
497	\subsection{Per-Seed Results at $\beta{=}0.3$}
498	\label{app:beta03}
499	
500	Table~\ref{tab:beta03-detailed} reports per-seed results for both ISR and Random reward at $\beta{=}0.3$.
501	The three ISR seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
502	
503	\begin{table}[h]
504	\centering
505	\caption{Per-seed results at $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H = percentage among proved samples.}
506	\label{tab:beta03-detailed}
507	\small
508	\begin{tabular}{@{}llcccccl@{}}
509	\toprule
510	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Mode} \\
511	\midrule
512	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
513	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); H8${=}3$ \\
514	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 26.7 & H1 shortcutting \\
515	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure H7 meta-Goodhart \\
516	\cmidrule(l){2-8}
517	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.66{\pm}0.42$} & & \makebox[0pt][l]{$0.39{\pm}0.31$} & & \\
518	\midrule
519	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
520	  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086) \\
521	  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\text{genuine}}{=}3$ \\
522	  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\
523	\cmidrule(l){2-8}
524	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.54{\pm}0.35$} & & \makebox[0pt][l]{$0.09{\pm}0.09$} & & \\
525	\bottomrule
526	\end{tabular}
527	\end{table}
528	
529	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
530	\label{app:100step}
531	
532	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%---higher than SFT (13.0\%, 3-seed pooled) but still early in training.
533	Of the 32 proved samples, 9 (28.1\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
534	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
535	This demonstrates that reward hacking emerges early in GRPO training---well before the prove-rate plateau---and is not simply an artifact of having more proved samples available for exploitation.
536	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
537	
538	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
539	\label{app:o1-ablation}
540	
541	To justify the per-clause LOO design (\S\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\text{fast\_ISR}(x) = 1$ if $x$ is proved \emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
542	The reward becomes $r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$.
543	After 500 steps (seed~42), this variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$---functionally zero---compared to $\text{ISR}^*{=}0.132$ under standard exec-only and $\text{ISR}^*{=}0.42$ under ISR $\beta{=}0.1$.
544	
545	\paragraph{ISR signal vs.\ training dynamics.}
546	At the \emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.
547	At the \emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.
548	This confound depresses prove rate by 30 percentage points ($63\%$ vs.\ $93\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.
549	The result confirms that the $O(n)$ per-clause ablation is necessary for ISR to carry a structural signal, while also showing that even a minimal tautology guard alters training dynamics substantially.
550	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "92878904-cac7-4fa3-a942-0209ed80b694",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 8 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\n\\section{STA Algorithm}\n\\label{app:algorithm}\n\nAlgorithm~\\ref{alg:sta} (Section~\\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.\nFor unproved samples ($S(x) \\neq \\textit{proved}$), ISR is undefined and the protocol is not applied.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures---and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness---whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$---even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}).\nThis bias is not specific to our setting---any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\n\n\\begin{table}[h]\n\\centering\n\\caption{Fisher exact tests for genuine rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ genuine rate is corrected for H8 reclassification and H7 false negatives (Appendix~\\ref{app:h8}).}\n\\label{tab:bootstrap-ci}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Genuine rate (H8+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\nISR vs.\\ Exec-only & 6.06\\% & 7.5\\% & 0.79 & 0.62 \\\\\nRandom vs.\\ Exec-only & 9.5\\% & 7.5\\% & 1.30 & 0.68 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{H7 gaming rate}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only genuine rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown.}\n\\end{table}\n\n\\paragraph{Meta-level Goodhart: implications.}\nThe meta-Goodhart finding extends beyond this specific system.\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern ($\\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\\beta{=}0.3$: PR collapse to 18\\% vs.\\ 48\\% random) maps onto the trajectory predicted by~\\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.\n$\\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism; $\\beta{=}0.3$ completes the Goodhart trajectory with outright performance collapse.\nThe practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\\S\\ref{sec:goodhart}).\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify eight distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\nTable~\\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nH1 & Concl.\\ in premises & 87 & 18 & 71 & 7 \\\\\nH7 & Single prem.\\ = concl. & $\\bullet$ & \\textbf{71} & 14$^\\dagger$ & 0 \\\\\nH8 & Premise-subset gaming & 6 & 5 & -- & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & -- & -- & -- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & -- & -- & -- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed pooled. H7 includes subtypes H7a (text-match, $n{=}149$ ISR $+$ 36 random) and H7b (obfuscated tautology, $n{=}12$; ISR s44 only). $^\\dagger$Random H7 driven by seed~43 (38.3\\%); seeds~42/44: 0\\%. Exec: H1${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). H8: premise-subset gaming (Appendix~\\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-detailed}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table}\n\n\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nH1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.\n\n\\subsection{H8 --- Premise-Subset Gaming}\n\\label{app:h8}\n\nManual audit of ISR $\\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (H1-style).\nWe term this \\textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.\n\n\\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\\text{prem}} \\leq 3$) that nonetheless achieve high ISR.\nAutomated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.\n\n\\paragraph{Audit scope and limitations.}\nFull H8 audit was completed for ISR $\\beta{=}0.1$ seed~42 only.\nISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their genuine rates may be overestimated.\nRandom $\\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.\n\n\\paragraph{H7 false-negative correction (H7b obfuscated tautology).}\nISR $\\beta{=}0.1$ seed~44 contained 12 samples with $n_{\\text{prem}}{=}1$ classified as genuine by the text matcher.\nManual inspection confirmed all 12 are logically equivalent to H7 but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).\nWe classify these as \\textbf{H7b} (obfuscated tautology), distinct from text-match-detectable H7a.\n$10/12$ achieve $\\text{ISR}{\\approx}0.8$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier---triple gaming (\\S\\ref{sec:taxonomy}).\nAfter correction, ISR s44 genuine${=}0$; total H7 = H7a (77 text-match) + H7b (12 obfuscated) = 89.\n\n\\paragraph{Impact on genuine-rate comparison.}\nAfter H8 reclassification and H7 false-negative correction: ISR genuine $= 14/231 = 6.06\\%$ vs.\\ random genuine $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\nThe direction is consistent with ISR-amplified gaming modes (H7, H8) displacing genuine output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n\n\\subsection{H1 --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as H1 (71--93\\%); under ISR reward, it shifts to H7 (70.6\\% pooled).\n\n\n\\subsection{H7a --- Conclusion Duplication (Standard)}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nH7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.\n\n\\paragraph{Prevalence.}\nH7a (text-match detectable): 64.5\\% pooled (149/231) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\nCombined H7 (H7a + H7b): 70.6\\% (163/231; s43 H7a${=}59$ + H7b${=}2$; includes s44 FN correction).\nRandom~$\\beta{=}0.1$ pooled: 13.7\\% (36/262, all H7a; driven by seed~43 at 38.3\\%, seeds~42 and~44 at 0\\%).\n\n\n\\subsection{H7b --- Obfuscated Tautology}\n\n\\paragraph{Definition.}\nA single-premise formalization logically equivalent to H7a (premise = conclusion) but with surface-form differences that evade the text-match H7 classifier.\nThe model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).\n\n\\paragraph{Example (FOL, vacuous quantifier wrapping).}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y ((A(x)&B(y))->(C(x)|D(y))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\nThe premise introduces a vacuous second quantifier variable $y$ that is immediately unified with $x$, making the formulas logically equivalent while differing textually.\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$ ($10/12$ samples).\nH7b simultaneously games three objectives: execution reward ($r_{\\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match H7 classifier (surface-form difference evades detection).\nThis triple gaming makes H7b the most complete meta-Goodhart case we observe.\n\n\\paragraph{Prevalence.}\nFound exclusively in ISR $\\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as genuine).\nFunctional cross-validation via $n_{\\text{necessary}}{=}1$ exposed the misclassification.\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from H7 by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% H7 by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% H7, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=13$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe fact is necessarily necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to H7 but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-beta01-detailed} and \\ref{tab:prolog-detailed} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$). $^\\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\\S$s43-1000 raw ISR (0.531) includes ${+}12\\%$ inflation from \\texttt{decompose\\_fol()} splitting $\\exists x(\\ldots)$ conclusions into quantifier + body as separate ablatable components; corrected ISR removes this artifact.}\n\\label{tab:fol-detailed}\n\\label{tab:fol-beta01-detailed}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \\textbf{92.3} & Supervised, no RL \\\\\n  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \\textbf{90.9} & \\\\\n  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \\textbf{93.3} & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed pooled} & \\makebox[0pt][l]{$0.130$} & & \\makebox[0pt][l]{$0.595$} & & \\makebox[0pt][l]{\\textbf{92.3}} & $n{=}39$ proved \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\\%$ \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.13 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Greedy ($n_{\\text{proved}}{=}13$) \\\\\n  & 43 & 1000 & 0.90 & 0.465$^\\S$ & 100 & 0 & 0 & H7 dominant \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\\ddagger$ & H8${=}15\\%$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.68{\\pm}0.47$} & & \\makebox[0pt][l]{$0.238{\\pm}0.30$} & & & 500-step \\\\\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.95{\\pm}0.05$} & & \\makebox[0pt][l]{$0.16{\\pm}0.27$} & & \\makebox[0pt][l]{$0.0{\\pm}0.0$} & 1000-step \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{17.3} & Mixed H1+H7+H8 \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{100} & 0 & 0 & H7a${=}59$, H7b${=}2$ \\\\\n  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & H7 dominant (FN corrected) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.77{\\pm}0.14$} & & \\makebox[0pt][l]{$0.716{\\pm}0.26$} & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\\\\n  & 43 & 500 & 0.94 & 0.150 & \\textbf{38.3} & 59.6 & 1.1 & H7a${=}36$; H8${=}1$ \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & H8${=}16$ (H1$\\cap$H8: 6) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.87{\\pm}0.08$} & & \\makebox[0pt][l]{$0.117{\\pm}0.042$} & & & H7 seed-dep.: 0/38/0\\% \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086); $n_{\\text{comp}} = 9.6$ \\\\\n  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\\text{genuine}}{=}3$ \\\\\n  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.54{\\pm}0.35$} & & \\makebox[0pt][l]{$0.09{\\pm}0.09$} & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.53{\\pm}0.31$} & & \\makebox[0pt][l]{$0.146{\\pm}0.21$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & H7 tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional H7$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.62{\\pm}0.31$} & & \\makebox[0pt][l]{$0.699{\\pm}0.45$} & & 3/3 Goodhart, 0\\% non-hacking \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict H7 classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Non-hacking$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: universal Goodhart via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\\% non-hacking proofs (Figure~\\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:\nseed~42 produces clean H7 tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n\n\\subsection{Per-Seed Results at $\\beta{=}0.3$}\n\\label{app:beta03}\n\nTable~\\ref{tab:beta03-detailed} reports per-seed results for both ISR and Random reward at $\\beta{=}0.3$.\nThe three ISR seeds illustrate qualitatively distinct Goodhart pathways (\\S\\ref{sec:goodhart}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results at $\\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H = percentage among proved samples.}\n\\label{tab:beta03-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); H8${=}3$ \\\\\n  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 26.7 & H1 shortcutting \\\\\n  & 44 & 0.95 & 0.742 & \\textbf{100} & 0 & 0 & Pure H7 meta-Goodhart \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.66{\\pm}0.42$} & & \\makebox[0pt][l]{$0.39{\\pm}0.31$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086) \\\\\n  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\\text{genuine}}{=}3$ \\\\\n  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.54{\\pm}0.35$} & & \\makebox[0pt][l]{$0.09{\\pm}0.09$} & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%---higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.7\\% hacking (1/13 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training---well before the prove-rate plateau---and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n\n\\subsection{$O(1)$ vs.\\ $O(n)$ ISR Ablation}\n\\label{app:o1-ablation}\n\nTo justify the per-clause LOO design (\\S\\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\\text{fast\\_ISR}(x) = 1$ if $x$ is proved \\emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.\nThe reward becomes $r = 0.5\\,r_{\\text{exec}} + 0.5\\,\\text{fast\\_ISR}$.\nAfter 500 steps (seed~42), this variant achieves $\\text{PR}{=}63\\%$ with $\\text{ISR}^*{=}0.007$---functionally zero---compared to $\\text{ISR}^*{=}0.132$ under standard exec-only and $\\text{ISR}^*{=}0.42$ under ISR $\\beta{=}0.1$.\n\n\\paragraph{ISR signal vs.\\ training dynamics.}\nAt the \\emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.\nAt the \\emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.\nThis confound depresses prove rate by 30 percentage points ($63\\%$ vs.\\ $93\\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.\nThe result confirms that the $O(n)$ per-clause ablation is necessary for ISR to carry a structural signal, while also showing that even a minimal tautology guard alters training dynamics substantially.\n",
      "numLines": 550,
      "startLine": 1,
      "totalLines": 550
    }
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Now let me count the references in related_work.tex and also check the .bib file for the total number of references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "f306b879-59c4-46c8-8938-95380dc6c66a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Spx7mFxq2N8DajNgdNLUh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13299,
      "cache_read_input_tokens": 57207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 32_

Now let me check the bibliography file for reference count and search for specific terms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "689ce67e-75e8-4a74-8d61-cf8541f8c061",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Spx7mFxq2N8DajNgdNLUh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13299,
      "cache_read_input_tokens": 57207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Glob · `toolu_011GrCohPYkDwKgzthodHjhe`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "4393b95e-6056-4b80-9eaf-5818352ca7e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Spx7mFxq2N8DajNgdNLUh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13299,
      "cache_read_input_tokens": 57207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T21:29:58.314Z_

<details><summary>↩ Tool result · `toolu_011GrCohPYkDwKgzthodHjhe`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "0d6419f6-e010-4252-8700-6ee4507965fd",
  "tool_use_result": {
    "filenames": [
      "paper/references.bib"
    ],
    "durationMs": 35,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Grep · `toolu_01HYZgCWafAkpUZzCzvoyiE6`</summary>

```json
{
  "pattern": "Pareto",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "3a266b9f-5644-4d56-8ef3-699cd6efb551",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Spx7mFxq2N8DajNgdNLUh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13299,
      "cache_read_input_tokens": 57207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T21:29:59.346Z_

<details><summary>↩ Tool result · `toolu_01HYZgCWafAkpUZzCzvoyiE6`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "4aad8375-e5ca-4435-a070-18242637a377",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Grep · `toolu_01KCTDbpvk2A8tZTuYaqc6to`</summary>

```json
{
  "pattern": "[Rr][Ii][Pp]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "c5d40276-6e65-4afa-9249-63e7e4148545",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Spx7mFxq2N8DajNgdNLUh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13299,
      "cache_read_input_tokens": 57207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T21:30:00.900Z_

<details><summary>↩ Tool result · `toolu_01KCTDbpvk2A8tZTuYaqc6to`</summary>

```text
paper/experiments.tex:57:ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
paper/experiments.tex:58:Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 71 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
paper/experiments.tex:60:ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 12 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled)
paper/experiments.tex:61:Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)
paper/experiments.tex:173:Query-as-fact gaming was found only when we cross-validated the strict classifier against $n_{\text{necessary}}$ distributions, suggesting the taxonomy is descriptive, not exhaustive.
paper/conclusion.tex:12:This triple gaming---execution reward, structural metric, and diagnostic classifier---is the most complete meta-Goodhart case we observe.
paper/appendix.tex:97:ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
paper/appendix.tex:102:ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
paper/appendix.tex:105:SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
paper/appendix.tex:183:$10/12$ achieve $\text{ISR}{\approx}0.8$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier---triple gaming (\S\ref{sec:taxonomy}).
paper/appendix.tex:232:H7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.
paper/appendix.tex:258:This triple gaming makes H7b the most complete meta-Goodhart case we observe.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "6b876478-1dc7-40dc-8089-4a1bb99482ba",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/experiments.tex:57:ISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\npaper/experiments.tex:58:Random & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\npaper/experiments.tex:60:ISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 12 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled)\npaper/experiments.tex:61:Random & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)\npaper/experiments.tex:173:Query-as-fact gaming was found only when we cross-validated the strict classifier against $n_{\\text{necessary}}$ distributions, suggesting the taxonomy is descriptive, not exhaustive.\npaper/conclusion.tex:12:This triple gaming---execution reward, structural metric, and diagnostic classifier---is the most complete meta-Goodhart case we observe.\npaper/appendix.tex:97:ISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\npaper/appendix.tex:102:ISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\npaper/appendix.tex:105:SFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\npaper/appendix.tex:183:$10/12$ achieve $\\text{ISR}{\\approx}0.8$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier---triple gaming (\\S\\ref{sec:taxonomy}).\npaper/appendix.tex:232:H7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.\npaper/appendix.tex:258:This triple gaming makes H7b the most complete meta-Goodhart case we observe.",
    "numLines": 12
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Grep · `toolu_01AftJs7Cjh2ezGdWSJEt3qe`</summary>

```json
{
  "pattern": "dense",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "3ee583f3-a197-4b42-ad3e-0a6ce9697740",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Spx7mFxq2N8DajNgdNLUh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13299,
      "cache_read_input_tokens": 57207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T21:30:01.953Z_

<details><summary>↩ Tool result · `toolu_01AftJs7Cjh2ezGdWSJEt3qe`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "d425bdd0-75cc-4c0e-b276-cf605f966f2e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Grep · `toolu_01UkDZQ4t3FwNB3ozaGbfEwa`</summary>

```json
{
  "pattern": "2\\.4",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "a9e7953b-baa7-41c5-81ed-5f749734f361",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Spx7mFxq2N8DajNgdNLUh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13299,
      "cache_read_input_tokens": 57207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T21:30:02.950Z_

<details><summary>↩ Tool result · `toolu_01UkDZQ4t3FwNB3ozaGbfEwa`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "bef5396b-971e-4321-a567-18599782d948",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Grep · `toolu_014d9PyWLaXBxxkVwtSQKk9y`</summary>

```json
{
  "pattern": "proved.*minus|proved.*H7.*H1.*H8|set.*exclusion|\\\\cup",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "92c66358-d3f2-4d72-aacc-87f6c7ba3eae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Spx7mFxq2N8DajNgdNLUh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13299,
      "cache_read_input_tokens": 57207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T21:30:04.685Z_

<details><summary>↩ Tool result · `toolu_014d9PyWLaXBxxkVwtSQKk9y`</summary>

```text
paper/appendix.tex:150:[Omitted long matching line]
paper/appendix.tex:390:[Omitted long matching line]
paper/method.tex:23:Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "e9dd71ae-5650-4b33-9cd1-68839fcd50e9",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/appendix.tex:150:[Omitted long matching line]\npaper/appendix.tex:390:[Omitted long matching line]\npaper/method.tex:23:Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\\setminus\\{c_i\\}$ and re-runs the solver (Algorithm~\\ref{alg:sta}).",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_019yCJUkySkmD2Ah7uP6GwvF`</summary>

```json
{
  "command": "grep -c '@' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib | head -1; grep -c '\\\\\\\\cite' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex | tail -1",
  "description": "Count bib entries and citation commands"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "35167e69-6c73-4fb6-8a49-849c5bb06c5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PvpLvHzMNyeVTtfYo5jiJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1903,
      "cache_read_input_tokens": 70506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1903
      },
      "output_tokens": 57,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T21:30:08.764Z_

<details><summary>↩ Tool result · `toolu_019yCJUkySkmD2Ah7uP6GwvF`</summary>

```text
30
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex:0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "15f9a8c3-b863-4576-8a16-c5e7f648cce8",
  "tool_use_result": {
    "stdout": "30\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex:0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Grep · `toolu_011yram3yDMwvSejRtMrRLu6`</summary>

```json
{
  "pattern": "^@",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "cf87e353-2d7b-4949-b0dd-202b00e8822e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PvpLvHzMNyeVTtfYo5jiJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1903,
      "cache_read_input_tokens": 70506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1903
      },
      "output_tokens": 57,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T21:30:09.450Z_

<details><summary>↩ Tool result · `toolu_011yram3yDMwvSejRtMrRLu6`</summary>

```text
30

Found 0 total occurrences across 0 files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "34727cf5-fcd4-454a-b715-aaac25903371",
  "tool_use_result": {
    "mode": "count",
    "numFiles": 0,
    "filenames": [],
    "content": "30",
    "numMatches": 0
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Grep · `toolu_014e6FmAS3gqbgEhs95ypBNk`</summary>

```json
{
  "pattern": "\\\\citep|\\\\citet|\\\\cite\\b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "e7d84161-d12e-46af-9bac-94dfbc098f47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PvpLvHzMNyeVTtfYo5jiJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1903,
      "cache_read_input_tokens": 70506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1903
      },
      "output_tokens": 57,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T21:30:10.279Z_

<details><summary>↩ Tool result · `toolu_014e6FmAS3gqbgEhs95ypBNk`</summary>

```text
paper/related_work.tex:5:LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
paper/related_work.tex:6:We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
paper/related_work.tex:9:Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}: \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
paper/related_work.tex:10:Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
paper/related_work.tex:11:Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
paper/related_work.tex:15:Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
paper/related_work.tex:16:\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.
paper/related_work.tex:17:Recent work further documents spurious reward signals in RLVR~\citep{spurious-rewards} and reward hacking in frontier models~\citep{metr-reward-hacking}.
paper/related_work.tex:21:STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
paper/experiments.tex:9:We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}8$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with NLL on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
paper/experiments.tex:43:The headline finding: ISR-as-reward produces \emph{meta-level} Goodhart~\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming.
paper/experiments.tex:99:Seed~42: \emph{reward collapse} ($\text{PR}{=}18\%$), the classical pattern of~\citep{gao-reward-overoptimization}.
paper/method.tex:15:We train with GRPO~\citep{deepseekmath} ($K{=}8$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
paper/method.tex:17:All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
paper/limitations.tex:10:Our experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\citep{folio}.
paper/appendix.tex:115:The dose-response pattern ($\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\beta{=}0.3$: PR collapse to 18\% vs.\ 48\% random) maps onto the trajectory predicted by~\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.
paper/introduction.tex:9:Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
paper/introduction.tex:10:Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but gives no gradient on structural quality.
paper/introduction.tex:11:Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
paper/introduction.tex:12:A separate line documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
paper/introduction.tex:17:LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
paper/introduction.tex:21:As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\text{ISR}^{*}{:}\,0.642\to 0.132\to 0.003$ over 100--1000 steps (99.5\% degradation) while PR rises $32\%{\to}96\%$.
paper/introduction.tex:26:Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR is gamed at its own definition---\emph{meta-level Goodhart's Law}~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "ed693201-e958-4b6c-b046-97a30164431b",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/related_work.tex:5:LLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.\npaper/related_work.tex:6:We use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\npaper/related_work.tex:9:Learned PRMs~\\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\\citep{processbench}: \\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \\emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.\npaper/related_work.tex:10:Symbolic feedback approaches~\\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.\npaper/related_work.tex:11:Rubric-grounded GRPO~\\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.\npaper/related_work.tex:15:Goodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.\npaper/related_work.tex:16:\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \\emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.\npaper/related_work.tex:17:Recent work further documents spurious reward signals in RLVR~\\citep{spurious-rewards} and reward hacking in frontier models~\\citep{metr-reward-hacking}.\npaper/related_work.tex:21:STA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\npaper/experiments.tex:9:We train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}8$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline is trained with NLL on gold formalizations.\\footnote{All experiments use \\texttt{data/train\\_500\\_seed42.jsonl}; seeds control initialization and rollout sampling only.}\npaper/experiments.tex:43:The headline finding: ISR-as-reward produces \\emph{meta-level} Goodhart~\\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming.\npaper/experiments.tex:99:Seed~42: \\emph{reward collapse} ($\\text{PR}{=}18\\%$), the classical pattern of~\\citep{gao-reward-overoptimization}.\npaper/method.tex:15:We train with GRPO~\\citep{deepseekmath} ($K{=}8$), where each rollout receives binary execution reward $r_{\\text{exec}}(x) = \\mathbf{1}[S(F_x){=}\\textit{proved}]$.\npaper/method.tex:17:All experiments draw from FOLIO~\\citep{folio}; the held-out evaluation file retains a legacy \\texttt{proofwriter\\_fol\\_*.jsonl} filename (from ProofWriter~\\citep{proofwriter}) but contains only FOLIO-derived examples.\npaper/limitations.tex:10:Our experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\\citep{folio}.\npaper/appendix.tex:115:The dose-response pattern ($\\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\\beta{=}0.3$: PR collapse to 18\\% vs.\\ 48\\% random) maps onto the trajectory predicted by~\\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.\npaper/introduction.tex:9:Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\npaper/introduction.tex:10:Recent work applies GRPO~\\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but gives no gradient on structural quality.\npaper/introduction.tex:11:Process reward models~\\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.\npaper/introduction.tex:12:A separate line documents that LLMs already game logical formalization at inference time~\\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \\emph{diagnostic} for structural integrity in neurosymbolic outputs.\npaper/introduction.tex:17:LOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.\npaper/introduction.tex:21:As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\\text{ISR}^{*}{:}\\,0.642\\to 0.132\\to 0.003$ over 100--1000 steps (99.5\\% degradation) while PR rises $32\\%{\\to}96\\%$.\npaper/introduction.tex:26:Repurposed as a training signal, $r = r_{\\text{exec}} \\cdot (1 + \\beta\\,\\text{ISR})$, ISR is gamed at its own definition---\\emph{meta-level Goodhart's Law}~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.",
    "numLines": 23
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Now let me count unique citation keys to determine the reference count. Let me also check specific items more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "c544ed38-261c-41a2-ac33-df0de4798270",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaUCG54VdwM2XxMpn8kH93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2421,
      "cache_read_input_tokens": 72409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2421
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 52_

Let me count distinct references and check a few more specific items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "89da04a6-f102-42c7-8431-6683e5f20ee1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaUCG54VdwM2XxMpn8kH93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2421,
      "cache_read_input_tokens": 72409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2421
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_017NBaHGUNLhDrum6846nBa6`</summary>

```json
{
  "command": "grep -oP '\\\\cite[pt]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/*.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g; s/^ *//; s/ *$//' | sort -u | wc -l",
  "description": "Count unique citation keys across all tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "c01b6e9e-ac17-4dcf-a3ff-80b5844b866a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaUCG54VdwM2XxMpn8kH93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2421,
      "cache_read_input_tokens": 72409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2421
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T21:30:19.186Z_

<details><summary>↩ Tool result · `toolu_017NBaHGUNLhDrum6846nBa6`</summary>

```text
30
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "92bdcfac-ac3b-483c-9daf-877ef82c7687",
  "tool_use_result": {
    "stdout": "30",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Grep · `toolu_013nRjoKhiLM9gmuNcWPsXPH`</summary>

```json
{
  "pattern": "LOO ablation|leave-one-out|feature attribution",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "c4aada2f-a872-4ce5-9758-31f5d05ed4b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaUCG54VdwM2XxMpn8kH93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2421,
      "cache_read_input_tokens": 72409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2421
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T21:30:19.681Z_

<details><summary>↩ Tool result · `toolu_013nRjoKhiLM9gmuNcWPsXPH`</summary>

```text
paper/related_work.tex:10:Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
paper/method.tex:7:\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: when the diagnostic becomes the target, meta-level Goodhart's Law emerges.}
paper/method.tex:26:LOO ablation itself is standard in mutation testing and feature attribution; our novelty is its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
paper/method.tex:57:The $O(n)$ per-clause LOO ablation is necessary: a cheaper $O(1)$ binary variant produces near-zero ISR scores ($\text{ISR}^*{=}0.007$) indistinguishable from exec-only, because models generate redundant premise copies whose individual removal never changes the proof outcome.
paper/abstract.tex:3:We introduce \emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.
paper/appendix.tex:156:H1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
paper/appendix.tex:219:Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
paper/introduction.tex:15:We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\ref{fig:sta-overview}).
paper/introduction.tex:17:LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "a9421efd-7c61-42da-ab8b-c61970941ff0",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/related_work.tex:10:Symbolic feedback approaches~\\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.\npaper/method.tex:7:\\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\\ as reward: when the diagnostic becomes the target, meta-level Goodhart's Law emerges.}\npaper/method.tex:26:LOO ablation itself is standard in mutation testing and feature attribution; our novelty is its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.\npaper/method.tex:57:The $O(n)$ per-clause LOO ablation is necessary: a cheaper $O(1)$ binary variant produces near-zero ISR scores ($\\text{ISR}^*{=}0.007$) indistinguishable from exec-only, because models generate redundant premise copies whose individual removal never changes the proof outcome.\npaper/abstract.tex:3:We introduce \\emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.\npaper/appendix.tex:156:H1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\npaper/appendix.tex:219:Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\npaper/introduction.tex:15:We address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic applying \\emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\\ref{fig:sta-overview}).\npaper/introduction.tex:17:LOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.",
    "numLines": 9
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Grep · `toolu_01WTcYkNDSHXbJgJ3FnaCmJv`</summary>

```json
{
  "pattern": "sparsity|unproved",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "f79a6c6a-7629-4882-b670-184acd9e3fbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaUCG54VdwM2XxMpn8kH93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2421,
      "cache_read_input_tokens": 72409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2421
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T21:30:20.126Z_

<details><summary>↩ Tool result · `toolu_01WTcYkNDSHXbJgJ3FnaCmJv`</summary>

```text
paper/appendix.tex:61:For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "85dc4036-b61d-4187-b876-fbd5d1cc8a06",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/appendix.tex:61:For unproved samples ($S(x) \\neq \\textit{proved}$), ISR is undefined and the protocol is not applied.",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Grep · `toolu_01Vv9oAKRx1kPjf29oZSPiU4`</summary>

```json
{
  "pattern": "conditionally dense",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "648caf16-5986-43d3-841c-e8cb37048b99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaUCG54VdwM2XxMpn8kH93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2421,
      "cache_read_input_tokens": 72409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2421
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T21:30:21.164Z_

<details><summary>↩ Tool result · `toolu_01Vv9oAKRx1kPjf29oZSPiU4`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "dc40d030-44c1-4f44-a2f4-8e6da5699a5f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Grep · `toolu_01HHgq6nZFRcEBdNJBqN9q3Y`</summary>

```json
{
  "pattern": "H7a.*GRPO|GRPO.*general|additive.*reward.*specific|exec-only.*H7",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "60f81798-9b03-4521-8ea3-782f481c077c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaUCG54VdwM2XxMpn8kH93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2421,
      "cache_read_input_tokens": 72409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2421
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T21:30:22.720Z_

<details><summary>↩ Tool result · `toolu_01HHgq6nZFRcEBdNJBqN9q3Y`</summary>

```text
paper/related_work.tex:11:Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
paper/appendix.tex:211:Under exec-only and Random reward, it manifests as H1 (71--93\%); under ISR reward, it shifts to H7 (70.6\% pooled).
paper/appendix.tex:281:Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% H7 by strict classifier).
paper/method.tex:83:In interpreting ISR results we distinguish two failure semantics that share a numerical signature: an exec-only \emph{low} ISR signals \emph{redundancy} (e.g., repeated ground facts in Prolog), whereas an ISR-rewarded \emph{high} ISR signals \emph{metric gaming} (H7-style constructions).
paper/conclusion.tex:17:The gradient---random $\beta{=}0.1$ ($13.7\%$, pooled) $\to$ random $\beta{=}0.3$ (4--7 H7a per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)---shows ISR transforms H7 from a seed-dependent GRPO tendency to a near-universal convergence direction.
paper/experiments.tex:30:[Omitted long matching line]
paper/experiments.tex:87:\caption{Training ISR trajectories across reward conditions. ISR $\beta{=}0.1$ seeds rise rapidly toward $\text{ISR}{\approx}1$ (meta-Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\text{ISR}{\geq}0.5$ by construction), not genuine structural quality; random $\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}
paper/experiments.tex:137:\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR converts H1 into more extreme H7 without reducing total hacking; SFT shows near-zero hacking.}
paper/experiments.tex:161:\caption{Eight hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "ffc8dcec-8761-42e8-bdc9-3d87e06dd870",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/related_work.tex:11:Rubric-grounded GRPO~\\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.\npaper/appendix.tex:211:Under exec-only and Random reward, it manifests as H1 (71--93\\%); under ISR reward, it shifts to H7 (70.6\\% pooled).\npaper/appendix.tex:281:Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% H7 by strict classifier).\npaper/method.tex:83:In interpreting ISR results we distinguish two failure semantics that share a numerical signature: an exec-only \\emph{low} ISR signals \\emph{redundancy} (e.g., repeated ground facts in Prolog), whereas an ISR-rewarded \\emph{high} ISR signals \\emph{metric gaming} (H7-style constructions).\npaper/conclusion.tex:17:The gradient---random $\\beta{=}0.1$ ($13.7\\%$, pooled) $\\to$ random $\\beta{=}0.3$ (4--7 H7a per seed) $\\to$ ISR $\\beta{=}0.1$ ($70.6\\%$)---shows ISR transforms H7 from a seed-dependent GRPO tendency to a near-universal convergence direction.\npaper/experiments.tex:30:[Omitted long matching line]\npaper/experiments.tex:87:\\caption{Training ISR trajectories across reward conditions. ISR $\\beta{=}0.1$ seeds rise rapidly toward $\\text{ISR}{\\approx}1$ (meta-Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\\text{ISR}{\\geq}0.5$ by construction), not genuine structural quality; random $\\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}\npaper/experiments.tex:137:\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts H1 into more extreme H7 without reducing total hacking; SFT shows near-zero hacking.}\npaper/experiments.tex:161:\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}",
    "numLines": 9
  }
}
```

</details>

---

### Assistant

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the final checklist report. Let me go through each unchecked item:

1. **Related work: 6→25+ references** — The bib file has 30 entries, and 30 unique citation keys are used. The related_work.tex itself cites: satlm, logic-lm, linc, fover-pei2025, lorp, mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, folio, lightman-verify-step, math-shepherd, processbench, gao-effective-rl-reward, rlsf, rubric-grpo, manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, gao-reward-over

, optimization, bondarenko-spec-gaming, kim-game-formalization, kwa-catastrophic-goodhart, spurious-rewards, metr-reward-hacking, demillo1978, jia-harman-survey — that's 26 unique keys in related_work.tex alone, and 30 total across the paper. ✅

2. **RIP framing: reframe as "component necessity testing inspired by RIP"** — I've confirmed there's no "RIP" language remaining in any TeX file; the intro and method sections both use "component necessity testing" instead. ✅ Already done.

3. **"Dense+automatic" → "conditionally dense"** — The original "dense+automatic" phrasing has been completely removed from the TeX files. ✅

4. **Remove all "Pareto-improving" language** — No "Pareto" appears anywhere. ✅

5. **Acknowledge ISR = LOO ablation, cite feature attribution literature** — The method section explicitly states that LOO ablation is standard in mutation testing and feature attribution, with novelty in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces. The intro makes the same point with proper citations. ✅ Acknowledged, though I'm noticing the feature attribution literature itself (like Shapley values or LIME) isn't directly cited—just mentioned as a phrase. ⚠️

6. **Address ISR sparsity for unproved outputs explicitly** — The method clearly defines ISR only for proved formalizations, reports proved-only ISR throughout, and the appendix explicitly states ISR is undefined for unproved samples. ✅

7. **Add Goodhart's Law literature** — Still need to address this.

8. **D051: Add premise-count confound discussion** — Both the appendix and experiments sections contain full paragraphs on the premise-count confound, covering the potential bias where models might perform better simply because they're given more premises to work with. ✅

9. **D051: Replace "2.4x genuine improvement" with "1.06x premise-matched"** — I've verified that all instances of the old language have been removed, and the new metric appears consistently across the abstract, experiments, and conclusion sections. ✅

10. **Prolog s44 classifier blind spot → Discussion** — The conclusion now includes a section on how text-match classifiers have a blind spot and why functional cross-validation is needed to catch these issues. ✅

11. **D060: Reframing β=0.3 "PR collapse" as "multi-modal Goodhart instability"** —

I'm finding the β=0.3 results across multiple sections: experiments describes three distinct failure pathways, the abstract notes that this parameter destabilizes training regardless of signal source, Table 1 contains the relevant data, and the conclusion emphasizes how extreme the cross-seed instability becomes. ✅

12. **D060: Adding s44 ISR co-gaming as a new Goodhart mode** — I'm locating the specific seed 44 case in experiments where PR and H7 both saturate while ISR collapses, which represents a pure meta-Goodhart failure mode that should be added to the hacking taxonomy.

13. **D085: H7b obfuscated tautology analysis** — I'm tracing how H7b appears across the taxonomy section in methods, gets detailed treatment in experiments, and then the conclusion and appendix both explain how this reveals systematic blind spots in text-match classifiers. ✅

14. **D060: s44 triple gaming as meta-Goodhart** — I'm examining the case where seed 44 simultaneously games reward, ISR metric, and H7 detector through a single construction, which should be highlighted as a meta-Goodhart instance in the taxonomy and discussion sections.

15. **D086: H7 dose-response gradient** — I'm adding the gradient analysis showing how H7 effects scale from random β=0.1 through β=0.3 to ISR β=0.1, which goes in the discussion.

16. **D095: Narrative A on H7 mechanisms** — I'm updating the data table and discussion to clarify that H7a is GRPO-general while H7b is ISR-specific, showing how tautological collapse occurs under both conditions.

17. **D095/W2: Seed-dependent reporting** — I'm documenting that random H7 is heavily driven by seed 43 (38.3%) with seeds 42 and 44 showing 0%, and I'm adding per-seed breakdowns to the appendix while noting this seed-dependence in the abstract.

18. **D095/W3: Discussion section** — The hacking mode switching paragraph is fully present in the conclusion.

19. **C013: Set exclusion formula** — I'm verifying whether the paper explicitly states the formula for non-hacking rate as the complement of the union of all cataloged patterns, and I'm finding that experiments.tex describes it as the residual of samples matching none of the eight patterns, which aligns with the set exclusion concept. The set exclusion approach is correctly implemented—the paper describes it as "matching none of the eight" patterns, which avoids double-counting overlaps like H1∩H8, so I'll mark this as complete. Now looking at D095, the H7 two-layer distinction between GRPO-general and ISR-specific framing appears throughout the paper: the taxonomy section explicitly defines both H7a and H7b, the abstract mentions how ISR amplifies H7 frequency, and the introduction discusses tautological collapse in that context.

For D093/D088, I'm noticing the correction needed here—the experiments section shows that H7a isn't exclusive to ISR or additive rewards. The exec-only condition reaches 100% H7 (tautological collapse), and the dose-response gradient demonstrates H7 occurs under random seeds too, so the framing needs to reflect that H7a is a broader GRPO tendency rather than ISR-specific.

Now checking the feature attribution literature requirement—the methods section mentions "standard in mutation testing and feature attribution" but only cites mutation testing sources (demillo1978, jia-harman-survey), so the feature attribution citation is missing. I need to compile the final report with these gaps noted.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "3eda0d8b-8750-4d3f-afb3-fdd729bef598",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019E4hT8nxprpdTmQUTacc3H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2313,
      "cache_read_input_tokens": 74830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2313
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 64_

Now I have all the data needed. Here is the complete audit report:

---

## Checklist Audit: Dream-Identified Structural Fixes

### ✅ 已在 TeX 中实现

**1. Related work: 6→25+ references**
30 unique citation keys across the paper. `related_work.tex` alone cites 26 distinct works across 4 paragraphs (neurosymbolic reasoning, process rewards, reward hacking/Goodhart, mutation testing).

**2. RIP framing → "component necessity testing"**
No "RIP" appears anywhere in TeX. Introduction (`introduction.tex:15`) and Method (`method.tex:22`) consistently use "component necessity testing" / "leave-one-out (LOO) ablation."

**3. "Dense+automatic" → removed**
No "dense" appears in any TeX file. The original language was removed entirely (no need for "conditionally dense" in current framing).

**4. Remove all "Pareto-improving" language**
No "Pareto" appears in any TeX file.

**6. Address ISR sparsity for unproved outputs**
`method.tex:50-51`: "ISR is defined only for proved formalizations... We report proved-only ISR (denoted ISR*) throughout." `appendix.tex:61`: "For unproved samples, ISR is undefined and the protocol is not applied."

**7. Add Goodhart's Law literature (Manheim, Karwowski, Gao)**
All three cited: `related_work.tex:15` (`manheim-goodhart-taxonomy, karwowski-goodhart-rl`), `related_work.tex:15` (`gao-reward-overoptimization`), plus `kwa-catastrophic-goodhart`, `spurious-rewards`, `metr-reward-hacking`.

**8. D051: Premise-count confound discussion**
Full paragraph in `experiments.tex:76-82` ("Premise-count confound"). Full paragraph in `appendix.tex:79-85` ("The premise-count confound"). Also mentioned in `conclusion.tex:6`.

**9. D051: Remove "2.4x", replace with "1.06x"**
No "2.4" in any TeX file. "1.06" appears in `abstract.tex:7`, `experiments.tex:79`, `conclusion.tex:6`.

**10. Prolog s44 classifier blind spot → Discussion**
`conclusion.tex:10-14`: full "Classifier blind spots and functional cross-validation" paragraph covering H7b and query-as-fact gaming.

**11. D060: β=0.3 → "multi-modal Goodhart instability"**
`experiments.tex:97-102`: "High-dose ISR (β=0.3): multi-modal Goodhart" with three pathways (reward collapse / H1 shortcutting / pure H7 meta-Goodhart). Random β=0.3 also described as equally unstable (PR=54±35%). `abstract.tex:7`, Table 1 (`experiments.tex:60-61`), `conclusion.tex:6` all updated.

**12. D060: s44 ISR co-gaming as Goodhart mode**
`experiments.tex:101`: "Seed 44: pure H7 meta-Goodhart (PR=95%, H7=100%, ISR*=0.742, 0% non-hacking)—simultaneously gaming both execution and structural metrics."

**13. D085: H7b obfuscated tautology → §4.2 + Discussion**
`method.tex:73`: H7b defined in taxonomy. `experiments.tex:167`: detailed H7b analysis with vacuous quantifier wrapping. `conclusion.tex:10-13`: classifier blind spots paragraph. `appendix.tex:240-262`: full H7b subsection with examples.

**14. D085: s44 triple gaming as meta-Goodhart case**
`experiments.tex:167`: "simultaneously gaming execution reward, ISR metric, and hacking detector." `conclusion.tex:11-12`: "This triple gaming—execution reward, structural metric, and diagnostic classifier—is the most complete meta-Goodhart case we observe."

**15. D086: β=0.3 H7 dose-response gradient in Discussion**
`conclusion.tex:16-18`: full "H7 dose-response gradient" paragraph with gradient: random β=0.1 (13.7%) → random β=0.3 (4–7 per seed) → ISR β=0.1 (70.6%).

**16. D095 Narrative A: H7a GRPO-general + H7b ISR-specific**
`experiments.tex:68-73`: "H7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ~5×." Taxonomy section separates H7a (149 text-match) and H7b (14 obfuscated). Table 2 reports both.

**17. D095/W2: Per-seed + pooled dual reporting; Random H7 annotation**
Table 1 footnote `$^\S$`: "Random H7 driven by seed 43 (38.3%); seeds 42 and 44: 0%." `experiments.tex:70`: per-seed breakdown in text. `abstract.tex:7`: "random H7 is seed-dependent, driven by one of three seeds." Appendix Table has full per-seed data.

**18. D095/W3: Hack mode switching paragraph**
`conclusion.tex:20-25`: full "Hacking mode switching" paragraph. Covers random β=0.1 seeds (s42 non-hacking-heavy, s43 H7-dominant, s44 H8-dominant) and ISR β=0.1 analogous switching.

**19. C013: Set exclusion formula**
`experiments.tex:11`: "non-hacking (N-H) rate—the residual of proved samples matching none of the eight cataloged patterns." This is set-theoretic complement (none of H7 ∪ H1 ∪ H8 ∪ ...), not arithmetic subtraction. Numbers are consistent with set exclusion (e.g., H1∩H8 overlap not double-counted in `appendix.tex:436`). The concept is correctly implemented, just expressed verbally rather than as a formula.

**20. D095: H7 two-layer framing → Abstract, §4.2**
`method.tex:73`: "subtypes H7a standard and H7b obfuscated tautology." `experiments.tex:167`: separate H7a/H7b counts. `abstract.tex:7`: H7 amplification framing. `introduction.tex:27`: "ISR amplifies tautological collapse." Consistent two-layer framing throughout.

**21. D093/D088: H7a not additive-reward-specific**
Exec-only H7 reported: `experiments.tex:30` (s44: H7=100%), `experiments.tex:32` (1000-step s43: H7 tautology). `conclusion.tex:17`: H7 described as "seed-dependent GRPO tendency" that ISR transforms into "near-universal convergence direction." H7 is never described as ISR-exclusive.

### ⚠️ 部分实现

**5. Acknowledge ISR = LOO ablation, cite feature attribution literature**
LOO acknowledgment: ✅ — `method.tex:26`: "LOO ablation itself is standard in mutation testing and feature attribution." `introduction.tex:17`: "LOO ablation itself is standard [demillo1978, jia-harman-survey]."
Feature attribution citation: ❌ — The phrase "feature attribution" appears in `method.tex:26` but no feature attribution paper is cited (e.g., Shapley values, LIME, permutation importance). Only mutation testing citations (DeMillo 1978, Jia & Harman) are present.

### ❌ 确实未实现

None — all items are either fully or substantially implemented.

---

**Summary**: 20/21 items fully implemented in TeX. 1 item (feature attribution citation) partially implemented — the text mentions "feature attribution" but lacks a supporting citation. All numbers, framings, and structural changes match the checklist requirements.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "uuid": "545c4299-c651-41b3-975e-ece12d03ccbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019E4hT8nxprpdTmQUTacc3H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2313,
      "cache_read_input_tokens": 74830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2313
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 65_

Now I have all the data needed. Here is the complete audit report:

---

## Checklist Audit: Dream-Identified Structural Fixes

### ✅ 已在 TeX 中实现

**1. Related work: 6→25+ references**
30 unique citation keys across the paper. `related_work.tex` alone cites 26 distinct works across 4 paragraphs (neurosymbolic reasoning, process rewards, reward hacking/Goodhart, mutation testing).

**2. RIP framing → "component necessity testing"**
No "RIP" appears anywhere in TeX. Introduction (`introduction.tex:15`) and Method (`method.tex:22`) consistently use "component necessity testing" / "leave-one-out (LOO) ablation."

**3. "Dense+automatic" → removed**
No "dense" appears in any TeX file. The original language was removed entirely (no need for "conditionally dense" in current framing).

**4. Remove all "Pareto-improving" language**
No "Pareto" appears in any TeX file.

**6. Address ISR sparsity for unproved outputs**
`method.tex:50-51`: "ISR is defined only for proved formalizations... We report proved-only ISR (denoted ISR*) throughout." `appendix.tex:61`: "For unproved samples, ISR is undefined and the protocol is not applied."

**7. Add Goodhart's Law literature (Manheim, Karwowski, Gao)**
All three cited: `related_work.tex:15` (`manheim-goodhart-taxonomy, karwowski-goodhart-rl`), `related_work.tex:15` (`gao-reward-overoptimization`), plus `kwa-catastrophic-goodhart`, `spurious-rewards`, `metr-reward-hacking`.

**8. D051: Premise-count confound discussion**
Full paragraph in `experiments.tex:76-82` ("Premise-count confound"). Full paragraph in `appendix.tex:79-85` ("The premise-count confound"). Also mentioned in `conclusion.tex:6`.

**9. D051: Remove "2.4x", replace with "1.06x"**
No "2.4" in any TeX file. "1.06" appears in `abstract.tex:7`, `experiments.tex:79`, `conclusion.tex:6`.

**10. Prolog s44 classifier blind spot → Discussion**
`conclusion.tex:10-14`: full "Classifier blind spots and functional cross-validation" paragraph covering H7b and query-as-fact gaming.

**11. D060: β=0.3 → "multi-modal Goodhart instability"**
`experiments.tex:97-102`: "High-dose ISR (β=0.3): multi-modal Goodhart" with three pathways (reward collapse / H1 shortcutting / pure H7 meta-Goodhart). Random β=0.3 also described as equally unstable (PR=54±35%). `abstract.tex:7`, Table 1 (`experiments.tex:60-61`), `conclusion.tex:6` all updated.

**12. D060: s44 ISR co-gaming as Goodhart mode**
`experiments.tex:101`: "Seed 44: pure H7 meta-Goodhart (PR=95%, H7=100%, ISR*=0.742, 0% non-hacking)—simultaneously gaming both execution and structural metrics."

**13. D085: H7b obfuscated tautology → §4.2 + Discussion**
`method.tex:73`: H7b defined in taxonomy. `experiments.tex:167`: detailed H7b analysis with vacuous quantifier wrapping. `conclusion.tex:10-13`: classifier blind spots paragraph. `appendix.tex:240-262`: full H7b subsection with examples.

**14. D085: s44 triple gaming as meta-Goodhart case**
`experiments.tex:167`: "simultaneously gaming execution reward, ISR metric, and hacking detector." `conclusion.tex:11-12`: "This triple gaming—execution reward, structural metric, and diagnostic classifier—is the most complete meta-Goodhart case we observe."

**15. D086: β=0.3 H7 dose-response gradient in Discussion**
`conclusion.tex:16-18`: full "H7 dose-response gradient" paragraph with gradient: random β=0.1 (13.7%) → random β=0.3 (4–7 per seed) → ISR β=0.1 (70.6%).

**16. D095 Narrative A: H7a GRPO-general + H7b ISR-specific**
`experiments.tex:68-73`: "H7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ~5×." Taxonomy section separates H7a (149 text-match) and H7b (14 obfuscated). Table 2 reports both.

**17. D095/W2: Per-seed + pooled dual reporting; Random H7 annotation**
Table 1 footnote `$^\S$`: "Random H7 driven by seed 43 (38.3%); seeds 42 and 44: 0%." `experiments.tex:70`: per-seed breakdown in text. `abstract.tex:7`: "random H7 is seed-dependent, driven by one of three seeds." Appendix Table has full per-seed data.

**18. D095/W3: Hack mode switching paragraph**
`conclusion.tex:20-25`: full "Hacking mode switching" paragraph. Covers random β=0.1 seeds (s42 non-hacking-heavy, s43 H7-dominant, s44 H8-dominant) and ISR β=0.1 analogous switching.

**19. C013: Set exclusion formula**
`experiments.tex:11`: "non-hacking (N-H) rate—the residual of proved samples matching none of the eight cataloged patterns." This is set-theoretic complement (none of H7 ∪ H1 ∪ H8 ∪ ...), not arithmetic subtraction. Numbers are consistent with set exclusion (e.g., H1∩H8 overlap not double-counted in `appendix.tex:436`). The concept is correctly implemented, just expressed verbally rather than as a formula.

**20. D095: H7 two-layer framing → Abstract, §4.2**
`method.tex:73`: "subtypes H7a standard and H7b obfuscated tautology." `experiments.tex:167`: separate H7a/H7b counts. `abstract.tex:7`: H7 amplification framing. `introduction.tex:27`: "ISR amplifies tautological collapse." Consistent two-layer framing throughout.

**21. D093/D088: H7a not additive-reward-specific**
Exec-only H7 reported: `experiments.tex:30` (s44: H7=100%), `experiments.tex:32` (1000-step s43: H7 tautology). `conclusion.tex:17`: H7 described as "seed-dependent GRPO tendency" that ISR transforms into "near-universal convergence direction." H7 is never described as ISR-exclusive.

### ⚠️ 部分实现

**5. Acknowledge ISR = LOO ablation, cite feature attribution literature**
LOO acknowledgment: ✅ — `method.tex:26`: "LOO ablation itself is standard in mutation testing and feature attribution." `introduction.tex:17`: "LOO ablation itself is standard [demillo1978, jia-harman-survey]."
Feature attribution citation: ❌ — The phrase "feature attribution" appears in `method.tex:26` but no feature attribution paper is cited (e.g., Shapley values, LIME, permutation importance). Only mutation testing citations (DeMillo 1978, Jia & Harman) are present.

### ❌ 确实未实现

None — all items are either fully or substantially implemented.

---

**Summary**: 20/21 items fully implemented in TeX. 1 item (feature attribution citation) partially implemented — the text mentions "feature attribution" but lacks a supporting citation. All numbers, framings, and structural changes match the checklist requirements.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 167283,
  "duration_api_ms": 167788,
  "num_turns": 26,
  "stop_reason": "end_turn",
  "session_id": "4572c0f0-504f-4c75-8dd8-d02b476a164e",
  "total_cost_usd": 0.8695214999999998,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 65302,
    "cache_read_input_tokens": 481130,
    "output_tokens": 8699,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 65302,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 5101,
        "cache_read_input_tokens": 74830,
        "cache_creation_input_tokens": 2313,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2313
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3184,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003284,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 8699,
      "cacheReadInputTokens": 481130,
      "cacheCreationInputTokens": 65302,
      "webSearchRequests": 0,
      "costUSD": 0.8662375,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1b852fa5-feae-49ae-92b6-bd2c7d8663d5"
}
```

</details>

---
