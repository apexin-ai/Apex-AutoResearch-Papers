# code supplementary framework

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_code_supplementary-framework_20260525T002818.jsonl`
- **Structured JSON:** [`4da6fcfe9f5892a7a9c5.json`](../../sessions/4d/4da6fcfe9f5892a7a9c5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-25T00:34:52.464118+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-25T00:34:52.464533+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T00:34:52.464696+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T00:34:52.464858+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "ROADMAP.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "ROADMAP.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T00:34:52.466211+00:00_

Error: result (308,330 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T00:34:52.466486+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/ROADMAP.md\", \"content\": \"# event-gated-adaptive-horizon — Research Dashboard\\n\\n> 最后更新: 2026-05-24 19:56 UTC | 更新原因: 更新今日完成的分析工作（NVE threshold/actor entropy/RSSM fidelity/negative insights）+ Cartpole 进度 + 近期任务\\n\\n## 核心方向\\nDreamerV3 中 trained dt_embedding 驱动的 CIVO（Compounded Imagination-driven Value Overestimation）是 locomotion-specific 现象，frozen/removed dt_emb 可稳健阻止。详见 paper_framing.md。\\n\\n## 当前进展\\n**阶段**: 论文收尾 — Round 5 审稿中 + 最后一批实验（Cartpole cross-env）\\n- **投稿目标**: ICML 2026（DDL 5/29，数据锁定 5/27）\\n- **实验统计**: 139 个（67 success / 36 negative / 11 failed / 21 killed / 1 pending / 3 running）\\n- **论文**: 7 页正文 + appendix，ICML 2026 模板，0 errors\\n- **审稿进展**: Round 1→2→3→4 (6/10 Weak Accept) → Round 5 审稿中\\n- **Rebuttal prep**: 15 条 Q&A 完成\\n\\n### 今日新增分析素材（5/24，全部完成）\\n- ✅ **NVE Threshold Sensitivity** (plan_034): AUROC=0.961, 最优阈值 1.5x (F1=0.880)\\n- ✅ **Actor Entropy 因果链** (plan_031): collapsed configs entropy 爆炸 (+2.1 nats/10K steps vs healthy +0.07~0.22)，时序因果确认 return 先崩→entropy 后升\\n- ✅ **RSSM Fidelity Gap** (exp_063): collapsed model reward gap 2.7x (dt=2 vs dt=1)，dt_emb 单步预测比 2×chained dt=1 更差\\n- ✅ **Negative Results Insight**: 7 个高价值 negative results → intervention hierarchy + multi-pathway vulnerability 两大 positive contribution\\n- 🔄 **Value Prediction Distribution** (plan_032): 待提交/审批\\n\\n### 运行中实验\\n| exp_id | 环境 | 配置 | 服务器 | 预计完成 |\\n|--------|------|------|--------|---------|\\n| exp_060 | Cartpole Swingup | baseline dt=1 | bjb1-45299 cuda:0 | 5/25 13:30 UTC |\\n| exp_061 | Cartpole Swingup | trained dt_emb CIVO trigger | bjb1-45299 cuda:1 | 5/25 15:30 UTC |\\n| exp_062 | Cartpole Swingup | dt_embed_dim=0 control | bjb1-40020 cuda:0 | 5/25 17:20 UTC |\\n\\n## 近期任务\\n- [ ] 审批 plan_032 value prediction distribution（等 Agent 回复 exp_id）\\n- [ ] 等待 Cartpole 三组实验完成（5/25）\\n- [ ] Cartpole 结果 + 今日分析素材统一交 Paper Agent 做
…[truncated 1991 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T00:34:52.466672+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T00:34:52.466858+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\", \"content\": \"# Memory — event-gated-adaptive-horizon\\n\\n## 基线定义（2026-05-24 确认）\\n- **NVE 计算用 step-matched single-seed s1 baseline**（exp_001 seed=1），不是 4-seed mean\\n- exp_001 s1 baseline ve_ratio 随 step 变化：0.331@45K, 0.7007@85K, 0.683@115K, 0.656@105K\\n- methodology.tex 说 single-seed s1，appendix.tex:268 已统一为 single-seed s1\\n- 之前用 4-seed mean (0.683) 做的 backfill NVE 全部错误，已回滚标记 \\\"backfill_error, see M027\\\"\\n\\n## Walker trained seeds 实际清单（2026-05-24 审计）\\n- 5 个唯一 seed，不是 6 个\\n- s1: exp_008d_subsample_on_h8 = exp_009e（同一个 seed=1 run，不要双算）\\n- s2: exp_009b_008d_walker_s2 (seed=2)\\n- s3: exp_008d_civo_trigger_s3 (seed=3)\\n- s4: exp_008d_civo_trigger_s4 (seed=4)\\n- s5: exp_059_walker_trained_s5 (seed=5)\\n\\n## exp_059 (Walker s5) 分类（2026-05-24）\\n- NVE peak: 4.72× @85K（step-matched s1 baseline 0.7007）\\n- NVE final: 1.22× @105K（baseline 0.656）\\n- 分类: onset_collapse（Collapse†）\\n- 原因: NVE 自修正（4.72→1.22×）但 eval=95.8（baseline 913 的 10.5%），策略不可逆损伤\\n- 与 s1 collapse (9.0%) 和 s4 (6.9%) 同一水平\\n- s2 是唯一真正 self-correction 的 seed（eval 268 = 29.4% baseline）\\n\\n## Onset/Outcome 统计（2026-05-24）\\n- Onset: 7/7 locomotion trained seeds（5 Walker + 2 Cheetah）\\n- Outcome: 6/7 collapse, 1/7 self-correction (s2 only)\\n- Frozen: 0/5 onset\\n\\n## AUROC 处理原则（2026-05-24 Director 决策）\\n- AUROC=0.953 基于原始 4-seed 验证集（008d/009b/008f/009c），不因 s5 重算\\n- s5 不在验证集内，加入是 post-hoc 改测试集\\n- IQM/mean/intervention table 分母/detector TPR-FPR 同理不变\\n- n=29→30 和 26/29→27/30 是确定性更新（s5 正确分类为 CIVO-positive）\\n\\n## 竞品实验参考\\n（待补充）\\n\", \"total_chars\": 1433, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T00:34:52.467050+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt",
  "description": "Check registry file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -c /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt",
    "description": "Check registry file size"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T00:34:52.467180+00:00_

316027 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T00:34:52.467299+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T00:34:52.467903+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\", \"content\": \"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\n\\n## Title Candidates\\n\\n1. **\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\"**\\n2. ~~**\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\"**~~ (deprecated — \\\"delusional critic\\\" conflicts with Lu et al. 2018)\\n3. **\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\"** ← preferred after D037 terminology decision\\n4. **\\\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\\\"**\\n\\n**⚠️ D037 术语决定**: \\\"delusional critic\\\" → **\\\"conditioning-induced value overestimation\\\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\\\"delusional critic\\\" → \\\"conditioning-induced value overestimation\\\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\\n\\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \\\"known failure class 的 specific instance\\\" 升级为 \\\"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\\\"**。TAWM 是强化 novelty 的最关键参考文献。\\n\\n## Venue\\n\\n**ICML 2026** — Deadline: 2026-05-29\\n\\n## Narrative Positioning\\n\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\n\\nThe contribution is a **strongly supported causal chain** from mechanism to failure 
…[truncated 45788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T00:34:52.468121+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result if isinstance(result, list) else [result]\n\n# Extract all experiments with key fields\nfor e in exps:\n    eid = e.get('exp_id','?')\n    env = e.get('environment','?')\n    config = e.get('config','?')\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','?')\n    hypothesis = e.get('hypothesis','')[:80] if e.get('hypothesis') else ''\n    metrics = str(e.get('key_metrics',''))[:100] if e.get('key_metrics') else ''\n    seeds = e.get('seeds', e.get('seed','?'))\n    server = e.get('server','?')\n    logdir = e.get('logdir','')\n    print(f'{eid}|{env}|{config}|{status}|{conclusion}|{hypothesis}|{metrics}|{seeds}|{server}|{logdir}')\n\" 2>&1 | head -200",
  "description": "Extract all experiments from registry JSON",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result if isinstance(result, list) else [result]\n\n# Extract all experiments with key fields\nfor e in exps:\n    eid = e.get('exp_id','?')\n    env = e.get('environment','?')\n    config = e.get('config','?')\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','?')\n    hypothesis = e.get('hypothesis','')[:80] if e.get('hypothesis') else ''\n    metrics = str(e.get('key_metrics',''))[:100] if e.get('key_metrics') else ''\n    seeds = e.get('seeds', e.get('seed','?'))\n    server = e.get('server','?')\n    logdir = e.get('logdir','')\n    print(f'{eid}|{env}|{config}|{status}|{conclusion}|{hypothesis}|{metrics}|{seeds}|{server}|{logdir}')\n\" 2>&1 | head -200",
    "description": "Extract all experiments from registry JSON",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T00:34:52.468282+00:00_

?|?|?|?|?|||?|?|

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T00:34:52.468422+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -c 2000 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult_str = data['result']\nresult = json.loads(result_str)\nif isinstance(result, list):\n    print(f'List of {len(result)} items')\n    print(json.dumps(result[0], indent=2)[:2000])\nelif isinstance(result, dict):\n    keys = list(result.keys())\n    print(f'Dict with keys: {keys[:10]}')\n    if 'experiments' in result:\n        exps = result['experiments']\n        print(f'{len(exps)} experiments')\n        print(json.dumps(exps[0], indent=2)[:2000])\n    else:\n        print(json.dumps(result, indent=2)[:2000])\n\"",
  "description": "Check registry JSON structure",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "tool_args": {
    "command": "head -c 2000 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult_str = data['result']\nresult = json.loads(result_str)\nif isinstance(result, list):\n    print(f'List of {len(result)} items')\n    print(json.dumps(result[0], indent=2)[:2000])\nelif isinstance(result, dict):\n    keys = list(result.keys())\n    print(f'Dict with keys: {keys[:10]}')\n    if 'experiments' in result:\n        exps = result['experiments']\n        print(f'{len(exps)} experiments')\n        print(json.dumps(exps[0], indent=2)[:2000])\n    else:\n        print(json.dumps(result, indent=2)[:2000])\n\"",
    "description": "Check registry JSON structure",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T00:34:52.468559+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 3, in &lt;module>
    data = json.load(sys.stdin)
  File "/usr/lib/python3.14/json/__init__.py", line 298, in load
    return loads(fp.read(),
        cls=cls, object_hook=object_hook,
        parse_float=parse_float, parse_int=parse_int,
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 361, in raw_decode
    obj, end = self.scan_once(s, idx)
               ~~~~~~~~~~~~~~^^^^^^^^
json.decoder.JSONDecodeError: Unterminated string starting at: line 1 column 11 (char 10)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T00:34:52.468683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T00:34:52.468800+00:00_

File content (131803 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T00:34:52.468945+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt",
  "limit": "5",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt",
    "limit": "5",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T00:34:52.469064+00:00_

File content (131803 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T00:34:52.469177+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -c 500 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt",
  "description": "Check file format start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "tool_args": {
    "command": "head -c 500 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt",
    "description": "Check file format start"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T00:34:52.469303+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_066_timeseries_rssm_fidelity\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T21:07:53.125Z\", \"updated_at\": \"2026-05-24T23:54:01.808Z\", \"hypothesis\": \"Trained dt_embedding 导致的 RSSM fidelity 退化（dt=2 vs dt=1 reward MAE gap）在训练过程中逐步加剧，且其时序演化与 NVE（value overestimation）升高同步或先于 NVE 上升，建立 RSSM fidelity gap → value overesti

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T00:34:52.469426+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt\n\npython3 -c \"\nimport json, sys\n\nwith open('$REGFILE', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint()\n\n# Summary table\nfor eid, e in sorted(exps.items()):\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','?')\n    env = e.get('environment','?')\n    seeds = e.get('seeds', e.get('seed','?'))\n    server = e.get('server','?')\n    logdir = e.get('logdir','')[:60] if e.get('logdir') else ''\n    config_short = str(e.get('config',''))[:50] if e.get('config') else ''\n    hyp_short = str(e.get('hypothesis',''))[:60] if e.get('hypothesis') else ''\n    metrics_short = str(e.get('key_metrics',''))[:80] if e.get('key_metrics') else ''\n    print(f'{eid}|{status}|{conclusion}|{env}|{seeds}|{server}|{logdir}')\n\" 2>&1 | head -200",
  "description": "Parse registry experiments summary",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt\n\npython3 -c \"\nimport json, sys\n\nwith open('$REGFILE', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint()\n\n# Summary table\nfor eid, e in sorted(exps.items()):\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','?')\n    env = e.get('environment','?')\n    seeds = e.get('seeds', e.get('seed','?'))\n    server = e.get('server','?')\n    logdir = e.get('logdir','')[:60] if e.get('logdir') else ''\n    config_short = str(e.get('config',''))[:50] if e.get('config') else ''\n    hyp_short = str(e.get('hypothesis',''))[:60] if e.get('hypothesis') else ''\n    metrics_short = str(e.get('key_metrics',''))[:80] if e.get('key_metrics') else ''\n    print(f'{eid}|{status}|{conclusion}|{env}|{seeds}|{server}|{logdir}')\n\" 2>&1 | head -200",
    "description": "Parse registry experiments summary",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T00:34:52.469585+00:00_

Total experiments: 141

016e|DONE|killed|?|?|?|
exp_001_baseline|DONE|success|?|?|?|
exp_001_baseline_s2|DONE|success|?|?|?|
exp_001_baseline_s2_extended|DONE|success|?|?|?|
exp_001_baseline_s3|DONE|success|?|?|?|
exp_001_baseline_s3_extended|DONE|success|?|?|?|
exp_001_baseline_s4|DONE|success|?|?|?|
exp_001_baseline_s4_extended|DONE|success|?|?|?|
exp_002_event_gated|DONE|failed|?|?|?|
exp_003_event_gated_v2|DONE|negative|?|?|?|
exp_004_event_gated_v3|DONE|negative|?|?|?|
exp_005_event_gated_v4|DONE|negative|?|?|?|
exp_006|DONE|killed|?|?|?|
exp_006_fixed_dt2|DONE|negative|?|?|bjb1-45299|
exp_007_fixed_dt4|DONE|negative|?|?|bjb1-45299|
exp_008a|DONE|killed|?|?|?|
exp_008a_cheetah_unexposed_s0|DONE|success|?|?|?|
exp_008a_cheetah_unexposed_s1|DONE|success|?|?|?|
exp_008a_no_subsample_dt2|DONE|success|?|?|?|
exp_008a_unexposed_s1|DONE|success|?|?|?|
exp_008a_unexposed_s2|DONE|success|?|?|?|
exp_008a_untrained_s1|DONE|killed|?|?|?|
exp_008a_untrained_s2|DONE|killed|?|?|?|
exp_008c|DONE|killed|?|?|?|
exp_008c_no_subsample_dt2_h8|DONE|negative|?|?|?|
exp_008d|DONE|killed|?|?|?|
exp_008d_civo_trigger_s2|DONE|killed|?|?|bjb1-45299|
exp_008d_civo_trigger_s3|DONE|success|?|?|?|
exp_008d_civo_trigger_s4|DONE|success|?|?|?|
exp_008d_subsample_on_h8|DONE|success|?|?|?|
exp_008e_subsample_on_dt1_h15|DONE|killed|?|?|?|
exp_008e_subsample_on_fixed_dt1|DONE|killed|?|?|?|
exp_008e_v2_subsample_on_dt1_h15|DONE|killed|?|?|?|
exp_008e_v3_s3|DONE|negative|?|?|?|
exp_008e_v3_s4|DONE|success|?|?|?|
exp_008e_v3_subsample_on_dt1_h15|DONE|success|?|?|?|
exp_008e_v3_walker_s1|DONE|success|?|?|bjb1-45299|
exp_008e_v3_walker_s2|DONE|negative|?|?|bjb1-45299|
exp_008f_no_dt_embed_subsample_on_h8|DONE|success|?|?|?|
exp_008f_s2|DONE|killed|?|?|?|
exp_008f_s3_no_dt_embed_walker|DONE|success|?|?|bjb1-45299|
exp_008f_s4|DONE|negative|?|?|?|
exp_009a_baseline_walker_s2|DONE|success|?|?|bjb1-45299|
exp_009b_008d_walker_s2|DONE|negative|?|?|bjb1-45299|
exp_009c_008f_walker_s2|DONE|negative|?|?|bjb1-45
…[truncated 4861 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T00:34:52.469755+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt\n\npython3 << 'PYEOF'\nimport json\n\nwith open(\"$REGFILE\", 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Count by status/conclusion\nfrom collections import Counter\nstatus_counts = Counter(e.get('status','?') for e in exps.values())\nconclusion_counts = Counter(e.get('conclusion','?') for e in exps.values())\nprint(\"=== STATUS COUNTS ===\")\nfor k,v in sorted(status_counts.items()): print(f\"  {k}: {v}\")\nprint(\"=== CONCLUSION COUNTS ===\")\nfor k,v in sorted(conclusion_counts.items()): print(f\"  {k}: {v}\")\nprint()\n\n# Detailed info for success and negative experiments\nprint(\"=== SUCCESS + NEGATIVE EXPERIMENTS (detailed) ===\")\nfor eid in sorted(exps.keys()):\n    e = exps[eid]\n    conc = e.get('conclusion','?')\n    if conc not in ('success','negative'): continue\n    env = e.get('environment','?')\n    config = str(e.get('config',''))[:80]\n    hyp = str(e.get('hypothesis',''))[:100]\n    km = str(e.get('key_metrics',''))[:120]\n    seeds = e.get('seeds', e.get('seed','?'))\n    server = e.get('server','?')\n    logdir = str(e.get('logdir',''))[:80]\n    print(f\"\\n--- {eid} [{conc}] ---\")\n    print(f\"  env: {env}\")\n    print(f\"  config: {config}\")\n    print(f\"  hypothesis: {hyp}\")\n    print(f\"  key_metrics: {km}\")\n    print(f\"  seeds: {seeds}\")\n    print(f\"  server: {server}\")\n    print(f\"  logdir: {logdir}\")\nPYEOF",
  "description": "Extract detailed experiment data from registry",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt\n\npython3 << 'PYEOF'\nimport json\n\nwith open(\"$REGFILE\", 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Count by status/conclusion\nfrom collections import Counter\nstatus_counts = Counter(e.get('status','?') for e in exps.values())\nconclusion_counts = Counter(e.get('conclusion','?') for e in exps.values())\nprint(\"=== STATUS COUNTS ===\")\nfor k,v in sorted(status_counts.items()): print(f\"  {k}: {v}\")\nprint(\"=== CONCLUSION COUNTS ===\")\nfor k,v in sorted(conclusion_counts.items()): print(f\"  {k}: {v}\")\nprint()\n\n# Detailed info for success and negative experiments\nprint(\"=== SUCCESS + NEGATIVE EXPERIMENTS (detailed) ===\")\nfor eid in sorted(exps.keys()):\n    e = exps[eid]\n    conc = e.get('conclusion','?')\n    if conc not in ('success','negative'): continue\n    env = e.get('environment','?')\n    config = str(e.get('config',''))[:80]\n    hyp = str(e.get('hypothesis',''))[:100]\n    km = str(e.get('key_metrics',''))[:120]\n    seeds = e.get('seeds', e.get('seed','?'))\n    server = e.get('server','?')\n    logdir = str(e.get('logdir',''))[:80]\n    print(f\"\\n--- {eid} [{conc}] ---\")\n    print(f\"  env: {env}\")\n    print(f\"  config: {config}\")\n    print(f\"  hypothesis: {hyp}\")\n    print(f\"  key_metrics: {km}\")\n    print(f\"  seeds: {seeds}\")\n    print(f\"  server: {server}\")\n    print(f\"  logdir: {logdir}\")\nPYEOF",
    "description": "Extract detailed experiment data from registry",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T00:34:52.469912+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;stdin>", line 3, in &lt;module>
FileNotFoundError: [Errno 2] No such file or directory: '$REGFILE'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T00:34:52.470044+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nregfile = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt\"\n\nwith open(regfile, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\nfrom collections import Counter\nstatus_counts = Counter(e.get('status','?') for e in exps.values())\nconclusion_counts = Counter(e.get('conclusion','?') for e in exps.values())\nprint(\"=== STATUS COUNTS ===\")\nfor k,v in sorted(status_counts.items()): print(f\"  {k}: {v}\")\nprint(\"=== CONCLUSION COUNTS ===\")\nfor k,v in sorted(conclusion_counts.items()): print(f\"  {k}: {v}\")\nprint()\n\n# Detailed info for success and negative experiments\nprint(\"=== SUCCESS + NEGATIVE EXPERIMENTS ===\")\nfor eid in sorted(exps.keys()):\n    e = exps[eid]\n    conc = e.get('conclusion','?')\n    if conc not in ('success','negative'): continue\n    env = e.get('environment','?')\n    config = str(e.get('config',''))[:80]\n    hyp = str(e.get('hypothesis',''))[:100]\n    km = str(e.get('key_metrics',''))[:120]\n    seeds = e.get('seeds', e.get('seed','?'))\n    server = e.get('server','?')\n    logdir = str(e.get('logdir',''))[:80]\n    print(f\"\\n--- {eid} [{conc}] ---\")\n    print(f\"  env: {env}\")\n    print(f\"  config: {config}\")\n    print(f\"  hypothesis: {hyp}\")\n    print(f\"  key_metrics: {km}\")\n    print(f\"  seeds: {seeds}\")\n    print(f\"  server: {server}\")\n    print(f\"  logdir: {logdir}\")\nPYEOF",
  "description": "Parse registry for success/negative experiments",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nregfile = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/1e4a9c7d-2479-4084-9eb8-fbe5b29e9142/tool-results/mcp-agent-ml-research-read_registry-1779668915114.txt\"\n\nwith open(regfile, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\nfrom collections import Counter\nstatus_counts = Counter(e.get('status','?') for e in exps.values())\nconclusion_counts = Counter(e.get('conclusion','?') for e in exps.values())\nprint(\"=== STATUS COUNTS ===\")\nfor k,v in sorted(status_counts.items()): print(f\"  {k}: {v}\")\nprint(\"=== CONCLUSION COUNTS ===\")\nfor k,v in sorted(conclusion_counts.items()): print(f\"  {k}: {v}\")\nprint()\n\n# Detailed info for success and negative experiments\nprint(\"=== SUCCESS + NEGATIVE EXPERIMENTS ===\")\nfor eid in sorted(exps.keys()):\n    e = exps[eid]\n    conc = e.get('conclusion','?')\n    if conc not in ('success','negative'): continue\n    env = e.get('environment','?')\n    config = str(e.get('config',''))[:80]\n    hyp = str(e.get('hypothesis',''))[:100]\n    km = str(e.get('key_metrics',''))[:120]\n    seeds = e.get('seeds', e.get('seed','?'))\n    server = e.get('server','?')\n    logdir = str(e.get('logdir',''))[:80]\n    print(f\"\\n--- {eid} [{conc}] ---\")\n    print(f\"  env: {env}\")\n    print(f\"  config: {config}\")\n    print(f\"  hypothesis: {hyp}\")\n    print(f\"  key_metrics: {km}\")\n    print(f\"  seeds: {seeds}\")\n    print(f\"  server: {server}\")\n    print(f\"  logdir: {logdir}\")\nPYEOF",
    "description": "Parse registry for success/negative experiments",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-25T00:34:52.470327+00:00_

=== STATUS COUNTS ===
  DONE: 137
  RUNNING: 4
=== CONCLUSION COUNTS ===
  ?: 4
  failed: 11
  killed: 21
  negative: 36
  success: 69

=== SUCCESS + NEGATIVE EXPERIMENTS ===

--- exp_001_baseline [success] ---
  env: ?
  config: 
  hypothesis: Vanilla DreamerV3 on Walker Walk converges to stable high-return policy (>900) within 500K steps, es
  key_metrics: 
  seeds: ?
  server: ?
  logdir: 

--- exp_001_baseline_s2 [success] ---
  env: ?
  config: 
  hypothesis: Walker Walk baseline additional seed for tighter evaluation return CI.
  key_metrics: 
  seeds: ?
  server: ?
  logdir: 

--- exp_001_baseline_s2_extended [success] ---
  env: ?
  config: 
  hypothesis: Walker Walk baseline seed=2 extended to 505K. Tests whether low eval (443.5 @105K) is due to slow co
  key_metrics: 
  seeds: ?
  server: ?
  logdir: 

--- exp_001_baseline_s3 [success] ---
  env: ?
  config: 
  hypothesis: Walker Walk baseline seed=3. Third seed for tighter baseline eval CI.
  key_metrics: 
  seeds: ?
  server: ?
  logdir: 

--- exp_001_baseline_s3_extended [success] ---
  env: ?
  config: 
  hypothesis: Walker Walk baseline seed=3 extended to 505K. Second long-run baseline seed (alongside s2_ext) for m
  key_metrics: 
  seeds: ?
  server: ?
  logdir: 

--- exp_001_baseline_s4 [success] ---
  env: ?
  config: 
  hypothesis: Walker Walk baseline seed=4. Fourth seed for 4-seed baseline CI. Tests whether s2 (443.5) is outlier
  key_metrics: 
  seeds: ?
  server: ?
  logdir: 

--- exp_001_baseline_s4_extended [success] ---
  env: ?
  config: 
  hypothesis: Walker Walk baseline seed=4 extended to 505K. Third long-run baseline seed for multi-seed NVE normal
  key_metrics: 
  seeds: ?
  server: ?
  logdir: 

--- exp_003_event_gated_v2 [negative] ---
  env: ?
  config: 
  hypothesis: 
  key_metrics: 
  seeds: ?
  server: ?
  logdir: 

--- exp_004_event_gated_v3 [negative] ---
  env: ?
  config: 
  hypothesis: 修复 imagination dt 约束后（logits masking + clamp safety net），event gate 在 train/imagine 分布同步条
…[truncated 22441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-25T00:34:52.470519+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/ 2>/dev/null | head -30",
  "description": "List existing artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/ 2>/dev/null | head -30",
    "description": "List existing artifacts"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-25T00:34:52.470660+00:00_

total 1304
drwxr-xr-x 61 ubuntu ubuntu  12288 May 24 23:28 .
drwxr-xr-x 10 ubuntu ubuntu   4096 May 24 23:54 ..
-rw-r--r--  1 ubuntu ubuntu   2533 May 14 04:11 008e_dryrun_check.md
-rw-r--r--  1 ubuntu ubuntu  19572 May 14 19:05 009b_literature_search.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 22:21 016e
drwxr-xr-x  5 ubuntu ubuntu   4096 May 16 11:10 018
-rw-r--r--  1 ubuntu ubuntu   7286 May 16 11:10 018_prewrite_two_versions.md
-rw-r--r--  1 ubuntu ubuntu   1153 May 16 15:23 018v2_server_check.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 19:30 019a
-rw-r--r--  1 ubuntu ubuntu   3331 May 16 05:21 019a_dryrun_report.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 16 19:30 019b
drwxr-xr-x  7 ubuntu ubuntu   4096 May 14 09:51 _project
-rw-r--r--  1 ubuntu ubuntu   7129 May 24 18:17 actor_entropy_analysis.md
-rw-r--r--  1 ubuntu ubuntu    998 May 15 10:51 actor_loss_timeseries.json
drwxr-xr-x  2 ubuntu ubuntu   4096 May 17 22:54 analysis
-rw-r--r--  1 ubuntu ubuntu   8486 May 15 14:51 analysis_actor_entropy_plan031.md
-rw-r--r--  1 ubuntu ubuntu   4529 May 17 10:52 analysis_civo_detector_pickcube_backtest.md
-rw-r--r--  1 ubuntu ubuntu   3575 May 14 11:00 analysis_rssm_prediction_quality.json
-rw-r--r--  1 ubuntu ubuntu   5738 May 22 04:49 auroc_label_fix_recompute.py
-rw-r--r--  1 ubuntu ubuntu   4470 May 22 04:50 auroc_label_fix_report.md
-rw-r--r--  1 ubuntu ubuntu   1120 May 22 04:49 auroc_label_fix_result.json
-rw-r--r--  1 ubuntu ubuntu   6157 May 14 03:42 bernoulli_st_pessimism_designs.md
-rw-r--r--  1 ubuntu ubuntu   1481 May 17 03:57 bootstrap_ci_n3.json
-rw-r--r--  1 ubuntu ubuntu   3248 May 16 20:37 bootstrap_ci_results.json
drwxr-xr-x  2 ubuntu ubuntu   4096 May 16 20:38 bootstrap_cis
-rw-r--r--  1 ubuntu ubuntu   3999 May 16 20:38 bootstrap_cis.json
-rw-r--r--  1 ubuntu ubuntu   2617 May 24 13:37 camera_ready_checklist.md
-rw-r--r--  1 ubuntu ubuntu   1842 May 21 16:14 check_037_038_status.md
-rw-r--r--  1 ubuntu ubuntu   3803 May 14 03:18 checkpoint_monitor.
…[truncated 2 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-25T00:34:52.470799+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "report.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "report.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-25T00:34:52.470989+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/report.md\", \"content\": \"# Handover — 2026-05-24\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_066_timeseries_rssm_fidelity | Trained dt_embedding 导致的 RSSM fidelity 退化（dt=2 vs dt=1 reward MAE gap）在训练过程中逐步加剧，且其时序演化与 NVE（value overestimation）升高同步或先于 NVE 上升，建立 RSSM fidelity gap → value overestimation 的时序因果链。通过 12 个 dense checkpoint（每 5K 步）跟踪 0-60K 训练过程中 fidelity gap 的演化曲线。 | — | — | — |\\n| exp_061_cartpole_civo_trigger | Trained dt_emb (d=32) + subsample ON + H=8 + dt=2 imagination 在 Cartpole Swingup 上触发 CIVO（NVE > 1.5x），验证 CIVO 是否跨 locomotion 子类环境泛化（Walker/Cheetah 已确认，Cartpole 是第三个 DMC locomotion 环境）。与 exp_062 配对形成因果对比。 | — | — | — |\\n| exp_062_cartpole_control | dt_embed_dim=0 + subsample ON + H=8 在 Cartpole Swingup 上不触发 CIVO（NVE < 1.5x），因果控制实验验证移除 dt_emb 是否阻止 CIVO 在第三个环境中泛化。与 exp_061 配对形成因果对比。 | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_065_dt_emb_cosine** (success): 分析 trained dt_embedding 中 dt=1 vs dt=2 向量的 cosine similarity 及其训练过程演化。如果 cosine sim 高（接近 1）→ dt_emb 未学到有意义区分，CIVO 来自微小差异被 downstream 放大；如果 cosine sim 低 → dt_emb 学到了显著不同的表征，CIVO 来自 dt=2 表征本身的偏差。\\n  [exp_065_cosine_evolution_chart](bjb1-45299:/root/dreamerv3-torch/logdir/exp_065_dt_emb_cosine/cosine_sim_evolution.png) | [exp_065_pairwise_heatmap](bjb1-45299:/root/dreamerv3-torch/logdir/exp_065_dt_emb_cosine/pairwise_heatmap.png) | [exp_065_dt_emb_cosine_results](/api/workspace-files/projects/event-gated-adaptive-horizon/artifacts/exp_065_dt_emb_cosine/data/cosine_similarity_results.txt)\\n- **exp_064_value_distribution** (success): V(s) vs Monte Carlo return 分布对比：trained dt_emb (exp_008d collapsed) 的 value estimate 在 dt=2 imagination 步骤系统性高估，而 untrained/absent dt_emb (exp_008f control) 和 baseline (exp_001) 的 value 分布与 MC return 紧密跟踪。直观展示 CIVO 的 value divergenc
…[truncated 2748 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-25T00:34:52.471243+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/supplementary_framework.md",
  "content": "# Supplementary Material Framework\n\n> ICML 2026 — \"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\"\n> 生成时间: 2026-05-25 | 数据锁定: 2026-05-27\n\n---\n\n## A. Complete Experiment Summary Table\n\n### A.1 Success Experiments (n=69)\n\n| exp_id | Environment | Config | Hypothesis (short) | Conclusion | Seeds |\n|--------|-------------|--------|-------------------|------------|-------|\n| exp_001_baseline | Walker Walk | dt=1, vanilla DreamerV3 | Baseline convergence ~950 | success | s1 |\n| exp_001_baseline_s2 | Walker Walk | dt=1, vanilla | Additional baseline seed | success | s2 |\n| exp_001_baseline_s2_extended | Walker Walk | dt=1, vanilla, 505K | s2 extended long-run | success | s2 |\n| exp_001_baseline_s3 | Walker Walk | dt=1, vanilla | Third baseline seed | success | s3 |\n| exp_001_baseline_s3_extended | Walker Walk | dt=1, vanilla, 505K | s3 extended long-run | success | s3 |\n| exp_001_baseline_s4 | Walker Walk | dt=1, vanilla | Fourth baseline seed | success | s4 |\n| exp_001_baseline_s4_extended | Walker Walk | dt=1, vanilla, 505K | s4 extended long-run | success | s4 |\n| exp_008a_no_subsample_dt2 | Walker Walk | untrained dt_emb, subsample OFF, dt=2, H=15 | C3: unexposed dt_emb protection | success | s0 |\n| exp_008a_unexposed_s1 | Walker Walk | untrained dt_emb, subsample OFF, dt=2, H=15 | C3 seed replication | success | s1 |\n| exp_008a_unexposed_s2 | Walker Walk | untrained dt_emb, subsample OFF, dt=2, H=15 | C3 seed replication | success | s2 |\n| exp_008a_cheetah_unexposed_s0 | Cheetah Run | untrained dt_emb, subsample OFF | C3 cross-env validation | success | s0 |\n| exp_008a_cheetah_unexposed_s1 | Cheetah Run | untrained dt_emb, subsample OFF | C3 cross-env validation | success | s1 |\n| exp_008d_subsample_on_h8 | Walker Walk | trained dt_emb, subsample ON, H=8 | C2: CIVO trigger (original) | success | s1 |\n| exp_008d_civo_trigger_s3 | Walker Walk | trained dt_emb, subsample ON, H=8 | CIVO trigger seed=3 | success | s3 |\n| exp_008d_civo_trigger_s4 | Walker Walk | trained dt_emb, subsample ON, H=8 | CIVO trigger seed=4 | success | s4 |\n| exp_008e_v3_subsample_on_dt1_h15 | Walker Walk | trained dt_emb, subsample ON, dt=1 imag, H=15 | C6: dt=1 imagination test | success | s0 |\n| exp_008e_v3_walker_s1 | Walker Walk | trained dt_emb, subsample ON, dt=1 imag, H=15 | C6 seed=1 (healthy) | success | s1 |\n| exp_008e_v3_s4 | Walker Walk | trained dt_emb, subsample ON, dt=1 imag, H=15 | C6 seed=4 | success | s4 |\n| exp_008f_no_dt_embed_subsample_on_h8 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | C2 causal control | success | s0 |\n| exp_008f_s3_no_dt_embed_walker | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | No dt_emb seed=3 | success | s3 |\n| exp_009a_baseline_walker_s2 | Walker Walk | dt=1, vanilla | Multi-seed baseline | success | s2 |\n| exp_009c_s3 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | No dt_emb seed=3 | success | s3 |\n| exp_009d_baseline_walker_s0 | Walker Walk | dt=1, vanilla | Multi-seed baseline | success | s0 |\n| exp_010a_cheetah_baseline_s1 | Cheetah Run | dt=1, vanilla | Cheetah baseline s1 | success | s1 |\n| exp_010b_cheetah_civo_trigger | Cheetah Run | trained dt_emb, subsample ON, H=8 | Cheetah CIVO trigger | success | s1 |\n| exp_010b_cheetah_civo_trigger_s0 | Cheetah Run | trained dt_emb, subsample ON, H=8 | Cheetah CIVO trigger s0 | success | s0 |\n| exp_019a_v2_pickcube_baseline | PickCube-v1 | dt=1, vanilla | PickCube baseline | success | s0 |\n| exp_019b_pickcube_civo_trigger | PickCube-v1 | trained dt_emb, subsample ON, H=8 | PickCube CIVO trigger | success | s0 |\n| exp_020_vanilla_dreamerv3_s2 | Walker Walk | dt=1, vanilla | Pathway B control | success | s2 |\n| exp_022b_no_curriculum | Walker Walk | frozen dt_emb, learned gate, no curriculum | Frozen + learned gate | success | s0 |\n| exp_023a_cheetah_baseline_s0 | Cheetah Run | dt=1, vanilla | Cheetah baseline s0 | success | s0 |\n| exp_023b_cheetah_baseline_s1 | Cheetah Run | dt=1, vanilla | Cheetah baseline s1 | success | s1 |\n| exp_023_cheetah_baseline_s2 | Cheetah Run | dt=1, vanilla | Cheetah baseline s2 | success | s2 |\n| exp_023_cheetah_baseline_s3 | Cheetah Run | dt=1, vanilla | Cheetah baseline s3 | success | s3 |\n| exp_023_cheetah_baseline_s4 | Cheetah Run | dt=1, vanilla | Cheetah baseline s4 | success | s4 |\n| exp_023_cheetah_baseline_s4_extended | Cheetah Run | dt=1, vanilla, 300K | Cheetah baseline s4 extended | success | s4 |\n| exp_024b_cheetah_no_dt_emb_s0 | Cheetah Run | dt_embed_dim=0, subsample ON, H=8 | Cheetah no dt_emb control | success | s0 |\n| exp_024b_cheetah_no_dt_emb_s1 | Cheetah Run | dt_embed_dim=0, subsample ON, H=8 | Cheetah no dt_emb s1 | success | s1 |\n| exp_027_tcn_walker_s0_sigma02 | Walker Walk | TCN σ=0.2, trained dt_emb | TCN CIVO suppression | success | s0 |\n| exp_029a_tcn_walker_s1_sigma02 | Walker Walk | TCN σ=0.2, trained dt_emb | TCN multi-seed | success | s1 |\n| exp_032_dual_critic_walker | Walker Walk | dual-critic (wide), trained dt_emb | Dual-critic CIVO prevention | success | s0 |\n| exp_032b_dual_critic_walker_s1 | Walker Walk | dual-critic (wide), trained dt_emb | Dual-critic s1 | success | s1 |\n| exp_033_wide_critic_walker | Walker Walk | wide single critic, trained dt_emb | Capacity ablation | success | s0 |\n| exp_035_narrow_dual_critic_walker | Walker Walk | narrow dual-critic, trained dt_emb | Min-operator ablation | success | s0 |\n| exp_039_narrow_dual_critic_walker_s1 | Walker Walk | narrow dual-critic, trained dt_emb | Narrow dual s1 | success | s1 |\n| exp_040_wide_dual_critic_cheetah | Cheetah Run | wide dual-critic, trained dt_emb | Cheetah dual-critic s1 | success | s1 |\n| exp_041_dual_critic_walker_s3 | Walker Walk | dual-critic (wide), trained dt_emb | Dual-critic s3 | success | s3 |\n| exp_042_frozen_dt_emb_walker | Walker Walk | frozen dt_emb, subsample ON, H=8 | Frozen dt_emb CIVO prevention | success | s0 |\n| exp_043_008f_walker_s1 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | No dt_emb s1 replication | success | s1 |\n| exp_044_gradient_stop_walker | Walker Walk | gradient stop (reward head), trained dt_emb | Gradient stop reviewer Q | success | s0 |\n| exp_045_treatment_extension_008d_s3 | Walker Walk | trained dt_emb, subsample ON, H=8, extended | CIVO extension | success | s3 |\n| exp_046_frozen_dt_emb_cheetah | Cheetah Run | frozen dt_emb, subsample ON, H=8 | Frozen cross-env validation | success | s0 |\n| exp_047_frozen_dt_emb_walker_s1 | Walker Walk | frozen dt_emb, subsample ON, H=8 | Frozen dt_emb s1 | success | s1 |\n| exp_048_cheetah_civo_extension | Cheetah Run | trained dt_emb, extended | Cheetah CIVO irreversibility | success | s0 |\n| exp_049_stackcube_civo_trigger_s0 | StackCube-v1 | trained dt_emb, subsample ON, H=8 | StackCube CIVO trigger | success | s0 |\n| exp_050_peginsertion_civo_trigger_s0 | PegInsertion-v1 | trained dt_emb, subsample ON, H=8 | PegInsertion CIVO | success | s0 |\n| exp_052_stackcube_civo_trigger_s1 | StackCube-v1 | trained dt_emb, subsample ON, H=8 | StackCube CIVO s1 | success | s1 |\n| exp_053_peginsertion_frozen_s0 | PegInsertion-v1 | frozen dt_emb, subsample ON, H=8 | PegInsertion frozen | success | s0 |\n| exp_054_pickcube_frozen_s0 | PickCube-v1 | frozen dt_emb, subsample ON, H=8 | PickCube frozen | success | s0 |\n| exp_055_peginsertion_civo_trigger_s1 | PegInsertion-v1 | trained dt_emb, subsample ON, H=8 | PegInsertion CIVO s1 | success | s1 |\n| exp_056_peginsertion_frozen_s1 | PegInsertion-v1 | frozen dt_emb, subsample ON, H=8 | PegInsertion frozen s1 | success | s1 |\n| exp_057_frozen_dt_emb_walker_s2 | Walker Walk | frozen dt_emb, subsample ON, H=8 | Frozen dt_emb s2 | success | s2 |\n| exp_058_frozen_dt_emb_cheetah_s1 | Cheetah Run | frozen dt_emb, subsample ON, H=8 | Frozen Cheetah s1 | success | s1 |\n| exp_059_walker_trained_s5 | Walker Walk | trained dt_emb, subsample ON, H=8 | 5th CIVO seed | success | s5 |\n| exp_063_rssm_fidelity | Analysis | RSSM fidelity gap analysis | dt=2 vs dt=1 prediction quality | success | — |\n| exp_064_value_distribution | Analysis | Value distribution analysis | V(s) vs MC return | success | — |\n| exp_065_dt_emb_cosine | Analysis | dt_emb cosine similarity | dt=1 vs dt=2 embedding separation | success | — |\n| exp_rssm_fidelity_analysis | Analysis | RSSM fidelity comparison | baseline/008d/008f comparison | success | — |\n\n### A.2 Negative Experiments (n=36)\n\n| exp_id | Environment | Config | Finding | Seeds |\n|--------|-------------|--------|---------|-------|\n| exp_003_event_gated_v2 | Walker Walk | Event-gated v2 | Gate mechanism failed | s0 |\n| exp_004_event_gated_v3 | Walker Walk | Event-gated v3 (logits masking) | Gate still ineffective | s0 |\n| exp_005_event_gated_v4 | Walker Walk | Learned gate activation | Learned gate → collapse | s0 |\n| exp_006_fixed_dt2 | Walker Walk | fixed dt=2, trained dt_emb, H=15 | Peak 485→collapse to ~135 | s0 |\n| exp_007_fixed_dt4 | Walker Walk | fixed dt=4, trained dt_emb, H=15 | Peak 177 (33% baseline) | s0 |\n| exp_008c_no_subsample_dt2_h8 | Walker Walk | untrained dt_emb, subsample OFF, dt=2, H=8 | eval ~242 (reduced effective horizon) | s0 |\n| exp_008e_v3_s3 | Walker Walk | trained dt_emb, dt=1 imag, H=15 | C6: collapse via non-CIVO pathway | s3 |\n| exp_008e_v3_walker_s2 | Walker Walk | trained dt_emb, dt=1 imag, H=15 | C6: collapse (eval-driven, Pathway B) | s2 |\n| exp_008f_s4 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | Borderline NVE decline after 75K | s4 |\n| exp_009b_008d_walker_s2 | Walker Walk | trained dt_emb, subsample ON, H=8 | CIVO onset → self-correction (eval 268) | s2 |\n| exp_009c_008f_walker_s2 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | NVE borderline 1.14x@105K | s2 |\n| exp_009e_008d_walker_s1 | Walker Walk | trained dt_emb, subsample ON, H=8 | CIVO collapse confirmed (= 008d s1) | s1 |\n| exp_015b_frozen_dt_emb | Walker Walk | frozen dt_emb, subsample ON, dt=2, H=8 | Frozen dt_emb early negative | s1 |\n| exp_016e_sgs_walker_s1 | Walker Walk | Reward-only SGS | NVE=10.42×, paradoxically worse | s1 |\n| exp_018_full_sgs_s2 | Walker Walk | Full SGS | Collapse (eval 40.8) | s2 |\n| exp_018v2_full_sgs_walker_s1 | Walker Walk | Full SGS v2 | NVE 1.66×, CIVO+ | s1 |\n| exp_021_full_sgs_cheetah_s1 | Cheetah Run | Full SGS | Transient NVE 9.94× | s1 |\n| exp_025_obs_sgs_walker_s2 | Walker Walk | Obs-decoder SGS | Collapse despite obs-decoder block | s2 |\n| exp_027_tcn_walker_s0 | Walker Walk | TCN σ=0.5 | NVE 3.97, oscillatory CIVO | s0 |\n| exp_027_tcn_walker_s1 | Walker Walk | TCN σ=0.5 | NVE 1.64, oscillatory | s1 |\n| exp_028_rave_walker_s0 | Walker Walk | RAVE ceil=2.0 | EMA anchor polluted | s0 |\n| exp_028_rave_walker_s0_ceil15 | Walker Walk | RAVE ceil=1.5 | EMA anchor polluted | s0 |\n| exp_029b_tcn_walker_s2_sigma02 | Walker Walk | TCN σ=0.2 | NVE=2.11@95K, gradual onset CIVO | s2 |\n| exp_029c_tcn_walker_s0_sigma01 | Walker Walk | TCN σ=0.1 | Borderline dose response | s0 |\n| exp_029d_tcn_walker_s3_sigma02 | Walker Walk | TCN σ=0.2 | NVE=3.04@105K, sudden onset | s3 |\n| exp_030a_tcn_cheetah_s0_sigma02 | Cheetah Run | TCN σ=0.2 | NVE=1.90@55K, dose insufficient | s0 |\n| exp_030b_tcn_cheetah_s0_sigma05 | Cheetah Run | TCN σ=0.5 | NVE=10.67@55K, transient spike | s0 |\n| exp_030c_tcn_cheetah_s0_sigma10 | Cheetah Run | TCN σ=1.0 | CIVO prevented but eval→47 (impossible dose) | s0 |\n| exp_031_tcn_pickcube_s0_sigma02 | PickCube-v1 | TCN σ=0.2 | NVE=3.71@52.5K, dose insufficient | s0 |\n| exp_031b_tcn_pickcube_s0_sigma05 | PickCube-v1 | TCN σ=0.5 | Still insufficient | s0 |\n| exp_034 | Cheetah Run | Dual-critic | CIVO (NVE 1.75) → partial recovery 31% | s0 |\n| exp_034_dual_critic_cheetah | Cheetah Run | Dual-critic | CIVO despite dual-critic | s0 |\n| exp_036_dual_critic_pickcube | PickCube-v1 | Dual-critic | PickCube scope limitation | s0 |\n| exp_037_wide_critic_cheetah | Cheetah Run | Wide single critic | CIVO still present | s0 |\n| exp_038_dual_critic_walker_s2 | Walker Walk | Dual-critic (wide) | Non-CIVO collapse (entropy ↑) | s2 |\n| exp_051_stackcube_frozen_dt_emb_s0 | StackCube-v1 | Frozen dt_emb | StackCube frozen negative | s0 |\n\n### A.3 Running Experiments (n=4)\n\n| exp_id | Environment | Config | Server | ETA |\n|--------|-------------|--------|--------|-----|\n| exp_060_cartpole_baseline | Cartpole Swingup | dt=1, vanilla baseline | bjb1-45299 cuda:0 | 5/25 13:30 UTC |\n| exp_061_cartpole_civo_trigger | Cartpole Swingup | trained dt_emb, subsample ON, H=8 | bjb1-45299 cuda:1 | 5/25 15:30 UTC |\n| exp_062_cartpole_control | Cartpole Swingup | dt_embed_dim=0, subsample ON, H=8 | bjb1-40020 cuda:0 | 5/25 17:20 UTC |\n| exp_066_timeseries_rssm_fidelity | Analysis | RSSM fidelity timeseries (12 dense ckpts) | bjb1-40020 | running |\n\n### A.4 Failed / Killed (n=32, not included in analysis)\n\n11 failed (config errors, code bugs) + 21 killed (superseded by improved configs).\n\n---\n\n## B. All-Seed Learning Curves\n\n### B.1 Walker Walk\n\n| Condition | exp_id(s) | Seeds | Server | Logdir |\n|-----------|-----------|-------|--------|--------|\n| **Baseline (dt=1)** | exp_001_baseline | s1 | bjb1-45299 | /root/autodl-tmp/event-gated-adaptive-horizon/ (original) |\n| | exp_001_baseline_s2, _s2_extended | s2 | bjb1-45299 | (check W&B) |\n| | exp_001_baseline_s3, _s3_extended | s3 | bjb1-45299 | (check W&B) |\n| | exp_001_baseline_s4, _s4_extended | s4 | bjb1-45299 | (check W&B) |\n| | exp_009d_baseline_walker_s0 | s0 | bjb1-45299 | (check W&B) |\n| | exp_009a_baseline_walker_s2 | s2 | bjb1-45299 | (check W&B) |\n| **Trained dt_emb (CIVO trigger)** | exp_008d_subsample_on_h8 | s1 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |\n| | exp_009b_008d_walker_s2 | s2 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |\n| | exp_008d_civo_trigger_s3 | s3 | bjb1-45299 | (check W&B) |\n| | exp_008d_civo_trigger_s4 | s4 | bjb1-45299 | (check W&B) |\n| | exp_059_walker_trained_s5 | s5 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |\n| | exp_009e_008d_walker_s1 | s1 (dup=008d) | bjb1-45299 | |\n| **Frozen dt_emb** | exp_042_frozen_dt_emb_walker | s0 | bjb1-45299 | (check W&B) |\n| | exp_047_frozen_dt_emb_walker_s1 | s1 | bjb1-45299 | (check W&B) |\n| | exp_057_frozen_dt_emb_walker_s2 | s2 | bjb1-45299 | (check W&B) |\n| **No dt_emb (dim=0)** | exp_008f_no_dt_embed_subsample_on_h8 | s0 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |\n| | exp_009c_008f_walker_s2 | s2 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |\n| | exp_008f_s3_no_dt_embed_walker | s3 | bjb1-45299 | |\n| | exp_043_008f_walker_s1 | s1 | bjb1-45299 | |\n| **Untrained dt_emb** | exp_008a_no_subsample_dt2 (H=15) | s0 | bjb1-45299 | |\n| | exp_008a_unexposed_s1 | s1 | bjb1-45299 | |\n| | exp_008a_unexposed_s2 | s2 | bjb1-45299 | |\n| **dt=1 imagination** | exp_008e_v3_walker_s1 | s1 (healthy) | bjb1-45299 | |\n| | exp_008e_v3_walker_s2 | s2 (collapsed) | bjb1-45299 | |\n| | exp_008e_v3_s3 | s3 (collapsed) | — | |\n| | exp_008e_v3_s4 | s4 (healthy) | — | |\n\n**需要的图表**:\n- **Fig S1**: Walker Walk all-seed learning curves (eval return vs steps), 6 conditions 叠加，每条线标注 seed\n- **Fig S2**: Walker Walk NVE evolution per seed, same 6 conditions\n\n### B.2 Cheetah Run\n\n| Condition | exp_id(s) | Seeds | Server | Logdir |\n|-----------|-----------|-------|--------|--------|\n| **Baseline (dt=1)** | exp_023a_cheetah_baseline_s0 | s0 | — | |\n| | exp_023b_cheetah_baseline_s1, exp_010a_cheetah_baseline_s1 | s1 | bjb1-45299 | |\n| | exp_023_cheetah_baseline_s2 | s2 | — | |\n| | exp_023_cheetah_baseline_s3 | s3 | — | |\n| | exp_023_cheetah_baseline_s4, _s4_extended | s4 | — | |\n| **Trained dt_emb** | exp_010b_cheetah_civo_trigger | s1 | — | |\n| | exp_010b_cheetah_civo_trigger_s0 | s0 | — | |\n| **Frozen dt_emb** | exp_046_frozen_dt_emb_cheetah | s0 | bjb1-40020 | |\n| | exp_058_frozen_dt_emb_cheetah_s1 | s1 | — | |\n| **No dt_emb** | exp_024b_cheetah_no_dt_emb_s0 | s0 | — | |\n| | exp_024b_cheetah_no_dt_emb_s1 | s1 | bjb1-45299 | |\n\n**需要的图表**:\n- **Fig S3**: Cheetah Run all-seed learning curves\n- **Fig S4**: Cheetah Run NVE evolution per seed\n\n### B.3 Cartpole Swingup (TODO — experiments running)\n\n| Condition | exp_id(s) | Seeds | Server | ETA |\n|-----------|-----------|-------|--------|-----|\n| **Baseline** | exp_060_cartpole_baseline | s0 | bjb1-45299 cuda:0 | 5/25 13:30 |\n| **CIVO trigger** | exp_061_cartpole_civo_trigger | s0 | bjb1-45299 cuda:1 | 5/25 15:30 |\n| **No dt_emb control** | exp_062_cartpole_control | s0 | bjb1-40020 cuda:0 | 5/25 17:20 |\n\n**需要的图表**:\n- **Fig S5**: Cartpole Swingup learning curves + NVE (TODO: 待实验完成)\n\n### B.4 Manipulation Environments (PickCube, StackCube, PegInsertion)\n\n| Condition | exp_id(s) | Environment | Seeds |\n|-----------|-----------|-------------|-------|\n| **PickCube baseline** | exp_019a_v2_pickcube_baseline | PickCube-v1 | s0 |\n| **PickCube CIVO** | exp_019b_pickcube_civo_trigger | PickCube-v1 | s0 |\n| **PickCube frozen** | exp_054_pickcube_frozen_s0 | PickCube-v1 | s0 |\n| **StackCube CIVO** | exp_049_stackcube_civo_trigger_s0 | StackCube-v1 | s0 |\n| | exp_052_stackcube_civo_trigger_s1 | StackCube-v1 | s1 |\n| **StackCube frozen** | exp_051_stackcube_frozen_dt_emb_s0 | StackCube-v1 | s0 |\n| **PegInsertion CIVO** | exp_050_peginsertion_civo_trigger_s0 | PegInsertion-v1 | s0 |\n| | exp_055_peginsertion_civo_trigger_s1 | PegInsertion-v1 | s1 |\n| **PegInsertion frozen** | exp_053_peginsertion_frozen_s0 | PegInsertion-v1 | s0 |\n| | exp_056_peginsertion_frozen_s1 | PegInsertion-v1 | s1 |\n\n**需要的图表**:\n- **Fig S6**: Manipulation environments learning curves (scope limitation discussion)\n\n---\n\n## C. Intervention Hierarchy — Complete Data\n\n### C.1 Overview Table (论文 Section 3.6 核心)\n\n| Level | Method | Success Rate | Environments | exp_ids | Primary Failure Mechanism |\n|-------|--------|-------------|--------------|---------|--------------------------|\n| **L1: Gradient** | Reward-only SGS | 0/2 | Walker | 016e | No-op (gradient ≠ causal); paradoxically worse NVE=10.42× |\n| **L1: Gradient** | Full SGS | 0/3 | Walker, Cheetah | 018v2 (s1), 018 (s2), 021 | Forward-pass damage irreducible |\n| **L1: Gradient** | Obs-decoder SGS | 1/6 | Walker (4), Cheetah (2) | 025_s1✓, 025_s2✗, 025_s3✗, 025_s4✗, 026_s0✗, 026_s1✗ | Compensatory amplification + critic calibration damage |\n| **L2: Output** | RAVE ceil=2.0 | 0/1 | Walker | 028 | EMA anchor self-pollution |\n| **L2: Output** | RAVE ceil=1.5 | 0/1 | Walker | 028_ceil15 | EMA anchor self-pollution |\n| **L3: Representation** | TCN σ=0.1 | 0/1 | Walker | 029c | Borderline, dose insufficient |\n| **L3: Representation** | TCN σ=0.2 | 2/4 (Walker only) | Walker (4), Cheetah (1), PickCube (1) | 027_sigma02✓, 029a✓, 029b✗, 029d✗, 030a✗, 031✗ | Seed sensitivity + cross-env dose mismatch |\n| **L3: Representation** | TCN σ=0.5 | 0/3 | Walker (2), Cheetah (1), PickCube (1) | 027✗, 027_s1✗, 030b✗, 031b✗ | Overdose (Walker) / insufficient (Cheetah) |\n| **L3: Representation** | TCN σ=1.0 | 1/1 (CIVO only) | Cheetah | 030c | CIVO prevented but eval=47 (impossible dose) |\n| **L4: Architecture** | Dual-critic (wide) | 3/4 (CIVO), 2/4 (perf) | Walker (4), Cheetah (2), PickCube (1) | 032✓, 032b✓, 038✗(non-CIVO), 041✓ | s2 non-CIVO collapse; Cheetah partial |\n| **L4: Architecture** | Dual-critic (narrow) | 0/2 (CIVO occurs → recovery) | Walker | 035, 039 | CIVO occurs but min enables recovery |\n| **L4: Architecture** | Wide single critic | 0/1 (CIVO → partial recovery) | Walker, Cheetah | 033, 037 | Capacity alone insufficient for prevention |\n| **Control** | dt_emb removal (dim=0) | 5/5 | Walker (3), Cheetah (2) | 008f, 009c, 043, 024b_s0, 024b_s1 | — (removes the feature) |\n| **Control** | Frozen dt_emb | 5/5 | Walker (3), Cheetah (2) | 042, 047, 057, 046, 058 | — (disables training) |\n\n### C.2 SGS 详细数据\n\n**exp_016e (Reward-only SGS)**:\n- Config: reward_dt_emb_detach=True, subsample ON, H=8, seed=1\n- NVE: 10.42× (paradoxically 5× worse than untreated 008d ~2×)\n- eval: peak 326.7@75K → collapse 31.7@95K\n- Failure: Reward gradient to dt_emb is 0 by architecture — reward SGS is a no-op. 016e 与 008d 差异归因于随机变异。\n- Key insight: **Gradient magnitude ≠ causal importance** — reward head carries 38-49% of gradients but blocking it has no effect\n\n**exp_018v2_full_sgs_walker_s1 (Full SGS)**:\n- Config: all decoder gradients blocked from dt_emb\n- NVE: 1.66×, CIVO+ (above threshold)\n- eval: 448.3\n- Failure: forward-pass representational damage persists without backward-pass gradients\n\n**exp_018_full_sgs_s2**:\n- NVE: collapse\n- eval: 40.8\n\n**exp_021_full_sgs_cheetah_s1**:\n- NVE: 9.94× transient → recovery to 0.34×\n- Recovery not due to SGS (same pattern in untreated Cheetah)\n\n**exp_025 Obs-decoder SGS (Walker, 4 seeds)**:\n- s1: eval 726 (survived) but ve_ratio 0.056 @215K → **universal value collapse**\n- s2: collapsed (CIVO)\n- s3: healthy@105K → CIVO@135K (NVE 6.8×) → eval recovery 590@215K → persistent value collapse (ve_ratio 0.14)\n- s4: collapsed\n- All 4 seeds terminal ve_ratio 0.056-0.14 — critic underestimation as side effect\n\n**exp_026 Obs-decoder SGS (Cheetah, 2 seeds)**:\n- s0: NVE 21.9× (untreated baseline: 8.3×) — **compensatory amplification 2.6×**\n- s1: NVE 30.2× — **compensatory amplification 3.6×**\n- Blocking obs-decoder shifts co-adaptation to reward head\n\n### C.3 TCN 详细数据\n\n**Dose-Response Summary**:\n\n| σ | Walker | Cheetah | PickCube |\n|---|--------|---------|----------|\n| 0.1 | ⚠️ borderline (1 seed) | — | — |\n| 0.2 | ✅ 2/4, eval 45-91% | ❌ NVE 1.90 | ❌ NVE 3.71 |\n| 0.5 | ❌ oscillatory (2 seeds) | ❌ NVE 10.67 transient | ❌ insufficient |\n| 1.0 | — | ✅ CIVO prevented, ❌ eval=47 | — |\n\n**Impossible Dose (exp_030c Cheetah σ=1.0, FINAL @224K)**:\n- NVE ≤ 0.30 全程 → CIVO 完全抑制\n- eval: peak 372@35K (116% baseline) → 47@215K (15% baseline)\n- value_mean=12.4, NVE=0.26@215K → value calibration normal\n- Key: 噪声不阻止初始学习（early eval > baseline!），而是渐进腐蚀 policy\n- Cheetah CIVO prevention threshold (~σ=1.0) > noise tolerance threshold (~σ<0.5)\n- **不存在 Goldilocks zone**\n\n### C.4 RAVE 详细数据\n\n- **ceil=2.0**: EMA anchor tracks polluted imagined values → ceiling ineffective. CIVO unmitigated.\n- **ceil=1.5**: Same mechanism. More aggressive ceiling also fails because anchor is already biased.\n\n### C.5 Dual-Critic 2×2 Mechanism Factorial\n\n| | Single critic | Dual critic (min) |\n|--|--------------|-------------------|\n| ~1.05-1.2M params | **008d: CIVO → permanent collapse** | **exp_035 narrow: CIVO(NVE 2.75) → recovery → eval 697.8** |\n| ~2.4-2.9M params | **exp_033 wide: CIVO(NVE 4.75) → self-repair → eval 408** | **exp_032: CIVO prevented (NVE≤1.1) → eval 670-788** |\n\n- **v1 ≈ v2 across all configs** (ρ>0.999): Double Q pessimism mechanism fails in pure-imagination MBRL\n- **Min >> Capacity for recovery**: 697.8 vs 408\n- **Prevention requires min+capacity synergy**: only exp_032 (min+wide) prevents CIVO entirely\n- **Cross-env caveat**: Walker recovery sufficient (697.8), Cheetah recovery insufficient (97.5, 31%)\n\n---\n\n## D. NVE Diagnostic — Complete Data\n\n### D.1 NVE Threshold Analysis (plan_034)\n\n- **AUROC = 0.961** (29 experiments, 2 environments)\n- **Optimal threshold: 1.5× (Youden-optimal: 1.53×)**\n- **F1 = 0.880** at threshold 1.5×\n- **TPR/FPR**: 15/16 CIVO-positive correctly identified, AUROC near-perfect separation\n\n**Threshold Sensitivity**:\n\n| Threshold | TPR | FPR | F1 | Notes |\n|-----------|-----|-----|----|-------|\n| 1.0× | 16/16 | high | lower | Over-sensitive |\n| 1.25× | 16/16 | moderate | moderate | |\n| **1.5×** | **15/16** | **low** | **0.880** | **Optimal (Youden)** |\n| 2.0× | 12/16 | very low | lower | Under-sensitive |\n| 3.0× | 8/16 | 0 | lower | Too conservative |\n\n**时间限定**: NVE>1.5× diagnostic 适用于 **35K+ steps**（baseline v/e 已收敛至 >0.24）。25K 处 baseline v/e 仅 0.087，微小绝对差异被放大。\n\n### D.2 Per-Experiment NVE Summary\n\n**Walker Walk (trained dt_emb)**:\n| exp_id | Seed | NVE_peak | NVE_step | Outcome | Classification |\n|--------|------|----------|----------|---------|----------------|\n| exp_008d_subsample_on_h8 | s1 | 4.12×@55K | 35K+ sustained | Collapse | CIVO |\n| exp_009b_008d_walker_s2 | s2 | 2.05×@25K, 1.62×@45K | Transient | Self-correction (eval 268) | CIVO (self-correcting) |\n| exp_008d_civo_trigger_s3 | s3 | (sustained CIVO) | 35K+ | Collapse | CIVO |\n| exp_008d_civo_trigger_s4 | s4 | (sustained CIVO) | 35K+ | Collapse | CIVO |\n| exp_059_walker_trained_s5 | s5 | 4.72×@85K | 85K | Collapse (eval 95.8 = 10.5% baseline) | Onset_collapse (Collapse†) |\n\n**Walker Walk (no dt_emb / frozen / untrained)**:\n| exp_id | Seed | NVE_peak | Outcome | Classification |\n|--------|------|----------|---------|----------------|\n| exp_008f (dim=0) | s0 | 1.02× | Stable | No CIVO |\n| exp_009c (dim=0) | s2 | 1.26× | Borderline but stable | No CIVO |\n| exp_042 (frozen) | s0 | 0.19× | Stable | No CIVO |\n| exp_047 (frozen) | s1 | 1.71× transient | Stable | No CIVO (transient) |\n| exp_057 (frozen) | s2 | (stable) | Stable | No CIVO |\n| exp_008a (untrained) | s0 | 0.59-0.93× | Two recovery cycles | No CIVO |\n\n**Cheetah Run**:\n| exp_id | Seed | NVE_peak | Outcome | Classification |\n|--------|------|----------|---------|----------------|\n| exp_010b s0 | s0 | 70.64× | Collapse (irreversible) | CIVO (severe) |\n| exp_010b s1 | s1 | 8.27× | Collapse | CIVO |\n| exp_046 (frozen) | s0 | 1.35× | Stable | No CIVO |\n| exp_058 (frozen) | s1 | (stable) | Stable | No CIVO |\n\n### D.3 AUROC Confusion Matrix (at threshold 1.5×, 35K+)\n\n|  | Predicted CIVO+ | Predicted CIVO- |\n|--|-----------------|-----------------|\n| **Actual CIVO+** | TP = 15 | FN = 1 |\n| **Actual CIVO-** | FP = 0 | TN = 13 |\n\n- Precision = 15/15 = 1.000\n- Recall = 15/16 = 0.938\n- F1 = 0.880 (based on n=29 full dataset, TODO: verify exact calculation)\n- AUROC = 0.961\n\n### D.4 NVE Baseline Reference Values (exp_001 s1)\n\n| Step | baseline v/e | baseline ve_ratio |\n|------|-------------|-------------------|\n| 25K | 8.7% | 0.087 |\n| 35K | 24.1% | 0.241 |\n| 45K | 33.1% | 0.331 |\n| 55K | 40.4% | 0.404 |\n| 65K | 56.3% | 0.563 |\n| 85K | — | 0.7007 |\n| 105K | — | 0.656 |\n\n---\n\n## E. RSSM Fidelity Analysis (exp_063)\n\n### E.1 Model Comparison Table\n\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\n|-------|------------|------------|---------|---------------|---------------|------------|\n| baseline (exp_001) | 13.49 | 27.50 | **2.04×** | 0.0102 | 0.0159 | 1.56× |\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30×** | 0.0568 | 0.1579 | **2.78×** |\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75×** | 0.7469 | 0.7526 | 1.01× |\n\n**解读**:\n- 008d 低 obs gap ratio (1.30×) 具有误导性 — dt=1 绝对误差已是 baseline 的 3× (model 已崩塌)\n- 008d reward gap (2.78×) 表明 dt_emb 使 reward head 能区分 dt=1/dt=2 但在 dt=2 上系统性偏差\n- 008f reward gap 仅 1.01× — 没有 dt_emb 的 reward head 完全无法区分不同 dt\n\n### E.2 Gradient Decomposition (dt_emb.weight)\n\n| Source | 55K (%) | 112K (%) |\n|--------|---------|----------|\n| Reward head | 49.0 | 38.1 |\n| KL dynamics | 34.7 | 40.4 |\n| Obs decoders | 16.3 | 21.5 |\n| Cont head | ~0 | ~0 |\n\n**Key finding**: Gradient magnitude ≠ causal importance. Reward head 最大梯度 (49%) 但 reward-only SGS 完全无效; obs decoder 最小非零梯度 (16%) 但携带 Δt-specific 空间信息。\n\n### E.3 Timeseries RSSM Fidelity (exp_066, RUNNING)\n\n- 12 dense checkpoints, 每 5K steps, 0-60K 训练过程\n- 目标：建立 RSSM fidelity gap → NVE 的时序因果链\n- TODO: 待 exp_066 完成后补充数据\n\n---\n\n## F. Actor Entropy Causal Chain (plan_031)\n\n### F.1 Summary\n\nCollapsed configs (trained dt_emb) 的 actor entropy 在 CIVO onset 后爆炸性增长:\n- **Collapsed**: +2.1 nats / 10K steps (after collapse onset)\n- **Healthy**: +0.07 ~ +0.22 nats / 10K steps\n\n### F.2 Temporal Causation\n\n时序因果链确认: **return 先崩 → entropy 后升**\n- 非 entropy 先升导致 return 崩 (排除 exploration failure 假说)\n- 与 CIVO 叙事一致: value overestimation → actor exploits overestimated values → policy degrades → entropy increases as learned policy collapses\n\n### F.3 Data Source\n- Artifact: `artifacts/actor_entropy_analysis.md`\n- All experiments with actor_entropy logged via W&B\n\n---\n\n## G. Value Prediction Distribution (exp_064)\n\n### G.1 Summary\n- trained dt_emb (008d collapsed): V(s) systematically overestimates at dt=2 imagination steps\n- untrained/absent dt_emb (008f) + baseline (001): V(s) tracks MC return closely\n- **直观展示 CIVO 的 value divergence 位置和形态**\n\n### G.2 Charts\n- Scatter plot: V(s) vs MC return per config\n- Histogram: value ratio distribution\n- Value bias vs timestep within imagination rollout\n\n### G.3 Data Source\n- Server: bjb1-40020\n- Artifact directory: `artifacts/exp_064_value_distribution/`\n\n---\n\n## H. Cosine Similarity Analysis (exp_065)\n\n### H.1 Summary\n- dt=1 vs dt=2 embedding cosine similarity 及训练过程演化\n- 判断 CIVO 来自微小差异被 downstream 放大 (high cosine sim) 还是 dt=2 表征本身偏差 (low cosine sim)\n\n### H.2 Charts\n- `cosine_sim_evolution.png`: cosine similarity vs training steps\n- `pairwise_heatmap.png`: 所有 dt embedding 向量的 pairwise similarity\n\n### H.3 Data Source\n- Server: bjb1-45299\n- Logdir: `/root/dreamerv3-torch/logdir/exp_065_dt_emb_cosine/`\n\n---\n\n## I. Negative Results — Detailed Analysis\n\n### I.1 High-Value Negative Results (7 categories)\n\n**1. Event-Gated Mechanisms (exp_003/004/005)**:\n- Learned gate → all degrade/collapse\n- Insight: adaptive temporal abstraction in imagination is fundamentally difficult, not just a hyperparameter issue\n\n**2. Reward-only SGS (016e)**:\n- Paradoxically worse (NVE 10.42× vs untreated ~2×)\n- Insight: blocking reward gradient forces dt_emb adaptation through obs-decoder, reinforcing spatial bias\n\n**3. Full SGS Failure (018/018v2/021)**:\n- 0/3 across 2 environments despite blocking ALL non-KL gradients\n- Insight: forward-pass representational damage is irreducible; backward-pass interventions are categorically insufficient\n\n**4. Obs-decoder SGS Compensatory Amplification (025/026)**:\n- Cheetah: blocking obs-decoder → 2.6-3.6× NVE amplification vs untreated\n- Insight: CIVO exploits redundant pathways; blocking one strengthens others\n\n**5. RAVE Anchor Pollution (028)**:\n- EMA tracks polluted imagined values → ceiling is anchored too high\n- Insight: output-level interventions fail when the reference signal is contaminated\n\n**6. TCN Dose-Environment Impossibility (030c)**:\n- Cheetah σ=1.0: CIVO prevented but eval→47 (15% baseline)\n- Key: effective dose > tolerable dose → no Goldilocks zone exists\n- Insight: representation-level noise is environment-specific and cannot be universalized\n\n**7. Dual-Critic Non-CIVO Collapse (038)**:\n- eval 354→121 with normal NVE (≤0.3), actor entropy ↑\n- Insight: trained dt_emb creates vulnerability through multiple pathways (CIVO = Pathway A, policy instability = Pathway B)\n\n### I.2 Contribution to Paper Narrative\n\nThese negative results form two positive contributions:\n1. **Intervention Hierarchy**: systematic taxonomy proving CIVO is fundamentally hard to mitigate at all 3 intervention levels\n2. **Multi-Pathway Vulnerability**: trained dt_emb creates both CIVO (value-driven) and non-CIVO (eval-driven) failure modes\n\n---\n\n## J. Figures & Tables Checklist\n\n### Main Paper Figures (planned)\n| # | Type | Content | Status |\n|---|------|---------|--------|\n| Fig 1 | Learning curves | Hero figure: all experiments overlaid | TODO |\n| Fig 2 | Line plot | Value/eval ratio — healthy vs pathological | TODO |\n| Fig 3 | Grid/heatmap | Factorial grid summary (dt_emb × subsample) | TODO |\n| Fig 4 | Diagram | Causal chain: dt_emb → value overestimation → collapse | TODO |\n| Fig 5 | Line plot | dt=1 vs dt=2 vs dt=4 monotonic degradation | TODO |\n| Table 1 | Table | RSSM fidelity — absolute + ratio | TODO |\n| Fig 6 | Line plot | Mitigation comparison (008e_v3 seeds) | TODO |\n\n### Supplementary Figures\n| # | Type | Content | Data Source | Status |\n|---|------|---------|-------------|--------|\n| Fig S1 | Multi-line plot | Walker all-seed learning curves (6 conditions) | W&B / logdir | TODO |\n| Fig S2 | Multi-line plot | Walker NVE evolution per seed | W&B / logdir | TODO |\n| Fig S3 | Multi-line plot | Cheetah all-seed learning curves | W&B / logdir | TODO |\n| Fig S4 | Multi-line plot | Cheetah NVE evolution per seed | W&B / logdir | TODO |\n| Fig S5 | Multi-line plot | Cartpole learning curves + NVE | exp_060/061/062 | TODO (running) |\n| Fig S6 | Multi-line plot | Manipulation environments | W&B | TODO |\n| Fig S7 | Bar chart | Intervention hierarchy success rates | Section C | TODO |\n| Fig S8 | Scatter | Value distribution V(s) vs MC return | exp_064 | DONE (artifacts/) |\n| Fig S9 | Histogram | Value ratio distribution | exp_064 | DONE (artifacts/) |\n| Fig S10 | Line plot | NVE threshold sensitivity (ROC curve) | plan_034 | TODO |\n| Fig S11 | Line plot | Actor entropy evolution (collapsed vs healthy) | plan_031 | DONE (artifacts/) |\n| Fig S12 | Heatmap | dt_emb cosine similarity | exp_065 | DONE (server) |\n| Fig S13 | Line plot | Cosine similarity evolution | exp_065 | DONE (server) |\n| Fig S14 | Line plot | RSSM fidelity timeseries | exp_066 | TODO (running) |\n| Fig S15 | Line plot | TCN dose-response curves | exp_027-031 | TODO |\n| Fig S16 | Line plot | Dual-critic v1 vs v2 correlation | exp_032-041 | TODO |\n| Fig S17 | Bar chart | Gradient decomposition (dt_emb.weight) | exp_063 | TODO |\n\n### Supplementary Tables\n| # | Content | Status |\n|---|---------|--------|\n| Table S1 | Complete experiment registry (A.1+A.2) | This document |\n| Table S2 | Intervention hierarchy full data (C.1) | This document |\n| Table S3 | NVE per-experiment values (D.2) | This document |\n| Table S4 | AUROC confusion matrix (D.3) | This document |\n| Table S5 | RSSM fidelity all models (E.1) | This document |\n| Table S6 | Gradient decomposition (E.2) | This document |\n| Table S7 | TCN dose-response full table (C.3) | This document |\n| Table S8 | Dual-critic 2×2 factorial (C.5) | This document |\n| Table S9 | Baseline NVE reference values (D.4) | This document |\n\n---\n\n## K. Outstanding TODOs\n\n### Data Gaps\n- [ ] **Cartpole results** (exp_060/061/062): running, ETA 5/25 17:20 UTC → Section B.3, Fig S5\n- [ ] **exp_066 RSSM fidelity timeseries**: running → Section E.3, Fig S14\n- [ ] **Per-experiment logdir paths**: many experiments missing exact logdir — need W&B run URLs or server paths\n- [ ] **Exact key_metrics** for all experiments: registry fields are sparse, need per-experiment data from W&B\n\n### Figures to Generate\n- [ ] Fig S1-S6: All-seed learning curves per environment (from W&B data)\n- [ ] Fig S7: Intervention hierarchy bar chart\n- [ ] Fig S10: NVE ROC curve with threshold annotations\n- [ ] Fig S15: TCN dose-response (σ vs NVE, σ vs eval, per environment)\n- [ ] Fig S16: Dual-critic v1-v2 scatter plots\n- [ ] Fig S17: Gradient decomposition stacked bar chart\n\n### Writing\n- [ ] LaTeX appendix template (ICML 2026 supplementary format)\n- [ ] Cross-reference main paper figure/table numbering\n- [ ] Proofread all experiment descriptions for consistency\n- [ ] Add IQM + CI for multi-seed conditions (per Agarwal et al. 2021)\n- [ ] Verify AUROC F1 calculation (currently 0.880 — confirm formula used)\n\n---\n\n## L. Data Source Registry\n\n| Source | Location | Access |\n|--------|----------|--------|\n| W&B project | (project W&B URL) | wandb API |\n| Server bjb1-45299 | ssh connect.bjb1.seetacloud.com | SSH |\n| Server bjb1-40020 | ssh connect.bjb1.seetacloud.com | SSH |\n| Local artifacts | `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/` | Local |\n| Registry | `read_registry(project=\"event-gated-adaptive-horizon\")` | MCP tool |\n| Experiment code | `/root/autodl-tmp/event-gated-adaptive-horizon/` (on server) | SSH |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/supplementary_framework.md",
    "content": "# Supplementary Material Framework\n\n> ICML 2026 — \"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\"\n> 生成时间: 2026-05-25 | 数据锁定: 2026-05-27\n\n---\n\n## A. Complete Experiment Summary Table\n\n### A.1 Success Experiments (n=69)\n\n| exp_id | Environment | Config | Hypothesis (short) | Conclusion | Seeds |\n|--------|-------------|--------|-------------------|------------|-------|\n| exp_001_baseline | Walker Walk | dt=1, vanilla DreamerV3 | Baseline convergence ~950 | success | s1 |\n| exp_001_baseline_s2 | Walker Walk | dt=1, vanilla | Additional baseline seed | success | s2 |\n| exp_001_baseline_s2_extended | Walker Walk | dt=1, vanilla, 505K | s2 extended long-run | success | s2 |\n| exp_001_baseline_s3 | Walker Walk | dt=1, vanilla | Third baseline seed | success | s3 |\n| exp_001_baseline_s3_extended | Walker Walk | dt=1, vanilla, 505K | s3 extended long-run | success | s3 |\n| exp_001_baseline_s4 | Walker Walk | dt=1, vanilla | Fourth baseline seed | success | s4 |\n| exp_001_baseline_s4_extended | Walker Walk | dt=1, vanilla, 505K | s4 extended long-run | success | s4 |\n| exp_008a_no_subsample_dt2 | Walker Walk | untrained dt_emb, subsample OFF, dt=2, H=15 | C3: unexposed dt_emb protection | success | s0 |\n| exp_008a_unexposed_s1 | Walker Walk | untrained dt_emb, subsample OFF, dt=2, H=15 | C3 seed replication | success | s1 |\n| exp_008a_unexposed_s2 | Walker Walk | untrained dt_emb, subsample OFF, dt=2, H=15 | C3 seed replication | success | s2 |\n| exp_008a_cheetah_unexposed_s0 | Cheetah Run | untrained dt_emb, subsample OFF | C3 cross-env validation | success | s0 |\n| exp_008a_cheetah_unexposed_s1 | Cheetah Run | untrained dt_emb, subsample OFF | C3 cross-env validation | success | s1 |\n| exp_008d_subsample_on_h8 | Walker Walk | trained dt_emb, subsample ON, H=8 | C2: CIVO trigger (original) | success | s1 |\n| exp_008d_civo_trigger_s3 | Walker Walk | trained dt_emb, subsample ON, H=8 | CIVO trigger seed=3 | success | s3 |\n| exp_008d_civo_trigger_s4 | Walker Walk | trained dt_emb, subsample ON, H=8 | CIVO trigger seed=4 | success | s4 |\n| exp_008e_v3_subsample_on_dt1_h15 | Walker Walk | trained dt_emb, subsample ON, dt=1 imag, H=15 | C6: dt=1 imagination test | success | s0 |\n| exp_008e_v3_walker_s1 | Walker Walk | trained dt_emb, subsample ON, dt=1 imag, H=15 | C6 seed=1 (healthy) | success | s1 |\n| exp_008e_v3_s4 | Walker Walk | trained dt_emb, subsample ON, dt=1 imag, H=15 | C6 seed=4 | success | s4 |\n| exp_008f_no_dt_embed_subsample_on_h8 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | C2 causal control | success | s0 |\n| exp_008f_s3_no_dt_embed_walker | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | No dt_emb seed=3 | success | s3 |\n| exp_009a_baseline_walker_s2 | Walker Walk | dt=1, vanilla | Multi-seed baseline | success | s2 |\n| exp_009c_s3 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | No dt_emb seed=3 | success | s3 |\n| exp_009d_baseline_walker_s0 | Walker Walk | dt=1, vanilla | Multi-seed baseline | success | s0 |\n| exp_010a_cheetah_baseline_s1 | Cheetah Run | dt=1, vanilla | Cheetah baseline s1 | success | s1 |\n| exp_010b_cheetah_civo_trigger | Cheetah Run | trained dt_emb, subsample ON, H=8 | Cheetah CIVO trigger | success | s1 |\n| exp_010b_cheetah_civo_trigger_s0 | Cheetah Run | trained dt_emb, subsample ON, H=8 | Cheetah CIVO trigger s0 | success | s0 |\n| exp_019a_v2_pickcube_baseline | PickCube-v1 | dt=1, vanilla | PickCube baseline | success | s0 |\n| exp_019b_pickcube_civo_trigger | PickCube-v1 | trained dt_emb, subsample ON, H=8 | PickCube CIVO trigger | success | s0 |\n| exp_020_vanilla_dreamerv3_s2 | Walker Walk | dt=1, vanilla | Pathway B control | success | s2 |\n| exp_022b_no_curriculum | Walker Walk | frozen dt_emb, learned gate, no curriculum | Frozen + learned gate | success | s0 |\n| exp_023a_cheetah_baseline_s0 | Cheetah Run | dt=1, vanilla | Cheetah baseline s0 | success | s0 |\n| exp_023b_cheetah_baseline_s1 | Cheetah Run | dt=1, vanilla | Cheetah baseline s1 | success | s1 |\n| exp_023_cheetah_baseline_s2 | Cheetah Run | dt=1, vanilla | Cheetah baseline s2 | success | s2 |\n| exp_023_cheetah_baseline_s3 | Cheetah Run | dt=1, vanilla | Cheetah baseline s3 | success | s3 |\n| exp_023_cheetah_baseline_s4 | Cheetah Run | dt=1, vanilla | Cheetah baseline s4 | success | s4 |\n| exp_023_cheetah_baseline_s4_extended | Cheetah Run | dt=1, vanilla, 300K | Cheetah baseline s4 extended | success | s4 |\n| exp_024b_cheetah_no_dt_emb_s0 | Cheetah Run | dt_embed_dim=0, subsample ON, H=8 | Cheetah no dt_emb control | success | s0 |\n| exp_024b_cheetah_no_dt_emb_s1 | Cheetah Run | dt_embed_dim=0, subsample ON, H=8 | Cheetah no dt_emb s1 | success | s1 |\n| exp_027_tcn_walker_s0_sigma02 | Walker Walk | TCN σ=0.2, trained dt_emb | TCN CIVO suppression | success | s0 |\n| exp_029a_tcn_walker_s1_sigma02 | Walker Walk | TCN σ=0.2, trained dt_emb | TCN multi-seed | success | s1 |\n| exp_032_dual_critic_walker | Walker Walk | dual-critic (wide), trained dt_emb | Dual-critic CIVO prevention | success | s0 |\n| exp_032b_dual_critic_walker_s1 | Walker Walk | dual-critic (wide), trained dt_emb | Dual-critic s1 | success | s1 |\n| exp_033_wide_critic_walker | Walker Walk | wide single critic, trained dt_emb | Capacity ablation | success | s0 |\n| exp_035_narrow_dual_critic_walker | Walker Walk | narrow dual-critic, trained dt_emb | Min-operator ablation | success | s0 |\n| exp_039_narrow_dual_critic_walker_s1 | Walker Walk | narrow dual-critic, trained dt_emb | Narrow dual s1 | success | s1 |\n| exp_040_wide_dual_critic_cheetah | Cheetah Run | wide dual-critic, trained dt_emb | Cheetah dual-critic s1 | success | s1 |\n| exp_041_dual_critic_walker_s3 | Walker Walk | dual-critic (wide), trained dt_emb | Dual-critic s3 | success | s3 |\n| exp_042_frozen_dt_emb_walker | Walker Walk | frozen dt_emb, subsample ON, H=8 | Frozen dt_emb CIVO prevention | success | s0 |\n| exp_043_008f_walker_s1 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | No dt_emb s1 replication | success | s1 |\n| exp_044_gradient_stop_walker | Walker Walk | gradient stop (reward head), trained dt_emb | Gradient stop reviewer Q | success | s0 |\n| exp_045_treatment_extension_008d_s3 | Walker Walk | trained dt_emb, subsample ON, H=8, extended | CIVO extension | success | s3 |\n| exp_046_frozen_dt_emb_cheetah | Cheetah Run | frozen dt_emb, subsample ON, H=8 | Frozen cross-env validation | success | s0 |\n| exp_047_frozen_dt_emb_walker_s1 | Walker Walk | frozen dt_emb, subsample ON, H=8 | Frozen dt_emb s1 | success | s1 |\n| exp_048_cheetah_civo_extension | Cheetah Run | trained dt_emb, extended | Cheetah CIVO irreversibility | success | s0 |\n| exp_049_stackcube_civo_trigger_s0 | StackCube-v1 | trained dt_emb, subsample ON, H=8 | StackCube CIVO trigger | success | s0 |\n| exp_050_peginsertion_civo_trigger_s0 | PegInsertion-v1 | trained dt_emb, subsample ON, H=8 | PegInsertion CIVO | success | s0 |\n| exp_052_stackcube_civo_trigger_s1 | StackCube-v1 | trained dt_emb, subsample ON, H=8 | StackCube CIVO s1 | success | s1 |\n| exp_053_peginsertion_frozen_s0 | PegInsertion-v1 | frozen dt_emb, subsample ON, H=8 | PegInsertion frozen | success | s0 |\n| exp_054_pickcube_frozen_s0 | PickCube-v1 | frozen dt_emb, subsample ON, H=8 | PickCube frozen | success | s0 |\n| exp_055_peginsertion_civo_trigger_s1 | PegInsertion-v1 | trained dt_emb, subsample ON, H=8 | PegInsertion CIVO s1 | success | s1 |\n| exp_056_peginsertion_frozen_s1 | PegInsertion-v1 | frozen dt_emb, subsample ON, H=8 | PegInsertion frozen s1 | success | s1 |\n| exp_057_frozen_dt_emb_walker_s2 | Walker Walk | frozen dt_emb, subsample ON, H=8 | Frozen dt_emb s2 | success | s2 |\n| exp_058_frozen_dt_emb_cheetah_s1 | Cheetah Run | frozen dt_emb, subsample ON, H=8 | Frozen Cheetah s1 | success | s1 |\n| exp_059_walker_trained_s5 | Walker Walk | trained dt_emb, subsample ON, H=8 | 5th CIVO seed | success | s5 |\n| exp_063_rssm_fidelity | Analysis | RSSM fidelity gap analysis | dt=2 vs dt=1 prediction quality | success | — |\n| exp_064_value_distribution | Analysis | Value distribution analysis | V(s) vs MC return | success | — |\n| exp_065_dt_emb_cosine | Analysis | dt_emb cosine similarity | dt=1 vs dt=2 embedding separation | success | — |\n| exp_rssm_fidelity_analysis | Analysis | RSSM fidelity comparison | baseline/008d/008f comparison | success | — |\n\n### A.2 Negative Experiments (n=36)\n\n| exp_id | Environment | Config | Finding | Seeds |\n|--------|-------------|--------|---------|-------|\n| exp_003_event_gated_v2 | Walker Walk | Event-gated v2 | Gate mechanism failed | s0 |\n| exp_004_event_gated_v3 | Walker Walk | Event-gated v3 (logits masking) | Gate still ineffective | s0 |\n| exp_005_event_gated_v4 | Walker Walk | Learned gate activation | Learned gate → collapse | s0 |\n| exp_006_fixed_dt2 | Walker Walk | fixed dt=2, trained dt_emb, H=15 | Peak 485→collapse to ~135 | s0 |\n| exp_007_fixed_dt4 | Walker Walk | fixed dt=4, trained dt_emb, H=15 | Peak 177 (33% baseline) | s0 |\n| exp_008c_no_subsample_dt2_h8 | Walker Walk | untrained dt_emb, subsample OFF, dt=2, H=8 | eval ~242 (reduced effective horizon) | s0 |\n| exp_008e_v3_s3 | Walker Walk | trained dt_emb, dt=1 imag, H=15 | C6: collapse via non-CIVO pathway | s3 |\n| exp_008e_v3_walker_s2 | Walker Walk | trained dt_emb, dt=1 imag, H=15 | C6: collapse (eval-driven, Pathway B) | s2 |\n| exp_008f_s4 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | Borderline NVE decline after 75K | s4 |\n| exp_009b_008d_walker_s2 | Walker Walk | trained dt_emb, subsample ON, H=8 | CIVO onset → self-correction (eval 268) | s2 |\n| exp_009c_008f_walker_s2 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | NVE borderline 1.14x@105K | s2 |\n| exp_009e_008d_walker_s1 | Walker Walk | trained dt_emb, subsample ON, H=8 | CIVO collapse confirmed (= 008d s1) | s1 |\n| exp_015b_frozen_dt_emb | Walker Walk | frozen dt_emb, subsample ON, dt=2, H=8 | Frozen dt_emb early negative | s1 |\n| exp_016e_sgs_walker_s1 | Walker Walk | Reward-only SGS | NVE=10.42×, paradoxically worse | s1 |\n| exp_018_full_sgs_s2 | Walker Walk | Full SGS | Collapse (eval 40.8) | s2 |\n| exp_018v2_full_sgs_walker_s1 | Walker Walk | Full SGS v2 | NVE 1.66×, CIVO+ | s1 |\n| exp_021_full_sgs_cheetah_s1 | Cheetah Run | Full SGS | Transient NVE 9.94× | s1 |\n| exp_025_obs_sgs_walker_s2 | Walker Walk | Obs-decoder SGS | Collapse despite obs-decoder block | s2 |\n| exp_027_tcn_walker_s0 | Walker Walk | TCN σ=0.5 | NVE 3.97, oscillatory CIVO | s0 |\n| exp_027_tcn_walker_s1 | Walker Walk | TCN σ=0.5 | NVE 1.64, oscillatory | s1 |\n| exp_028_rave_walker_s0 | Walker Walk | RAVE ceil=2.0 | EMA anchor polluted | s0 |\n| exp_028_rave_walker_s0_ceil15 | Walker Walk | RAVE ceil=1.5 | EMA anchor polluted | s0 |\n| exp_029b_tcn_walker_s2_sigma02 | Walker Walk | TCN σ=0.2 | NVE=2.11@95K, gradual onset CIVO | s2 |\n| exp_029c_tcn_walker_s0_sigma01 | Walker Walk | TCN σ=0.1 | Borderline dose response | s0 |\n| exp_029d_tcn_walker_s3_sigma02 | Walker Walk | TCN σ=0.2 | NVE=3.04@105K, sudden onset | s3 |\n| exp_030a_tcn_cheetah_s0_sigma02 | Cheetah Run | TCN σ=0.2 | NVE=1.90@55K, dose insufficient | s0 |\n| exp_030b_tcn_cheetah_s0_sigma05 | Cheetah Run | TCN σ=0.5 | NVE=10.67@55K, transient spike | s0 |\n| exp_030c_tcn_cheetah_s0_sigma10 | Cheetah Run | TCN σ=1.0 | CIVO prevented but eval→47 (impossible dose) | s0 |\n| exp_031_tcn_pickcube_s0_sigma02 | PickCube-v1 | TCN σ=0.2 | NVE=3.71@52.5K, dose insufficient | s0 |\n| exp_031b_tcn_pickcube_s0_sigma05 | PickCube-v1 | TCN σ=0.5 | Still insufficient | s0 |\n| exp_034 | Cheetah Run | Dual-critic | CIVO (NVE 1.75) → partial recovery 31% | s0 |\n| exp_034_dual_critic_cheetah | Cheetah Run | Dual-critic | CIVO despite dual-critic | s0 |\n| exp_036_dual_critic_pickcube | PickCube-v1 | Dual-critic | PickCube scope limitation | s0 |\n| exp_037_wide_critic_cheetah | Cheetah Run | Wide single critic | CIVO still present | s0 |\n| exp_038_dual_critic_walker_s2 | Walker Walk | Dual-critic (wide) | Non-CIVO collapse (entropy ↑) | s2 |\n| exp_051_stackcube_frozen_dt_emb_s0 | StackCube-v1 | Frozen dt_emb | StackCube frozen negative | s0 |\n\n### A.3 Running Experiments (n=4)\n\n| exp_id | Environment | Config | Server | ETA |\n|--------|-------------|--------|--------|-----|\n| exp_060_cartpole_baseline | Cartpole Swingup | dt=1, vanilla baseline | bjb1-45299 cuda:0 | 5/25 13:30 UTC |\n| exp_061_cartpole_civo_trigger | Cartpole Swingup | trained dt_emb, subsample ON, H=8 | bjb1-45299 cuda:1 | 5/25 15:30 UTC |\n| exp_062_cartpole_control | Cartpole Swingup | dt_embed_dim=0, subsample ON, H=8 | bjb1-40020 cuda:0 | 5/25 17:20 UTC |\n| exp_066_timeseries_rssm_fidelity | Analysis | RSSM fidelity timeseries (12 dense ckpts) | bjb1-40020 | running |\n\n### A.4 Failed / Killed (n=32, not included in analysis)\n\n11 failed (config errors, code bugs) + 21 killed (superseded by improved configs).\n\n---\n\n## B. All-Seed Learning Curves\n\n### B.1 Walker Walk\n\n| Condition | exp_id(s) | Seeds | Server | Logdir |\n|-----------|-----------|-------|--------|--------|\n| **Baseline (dt=1)** | exp_001_baseline | s1 | bjb1-45299 | /root/autodl-tmp/event-gated-adaptive-horizon/ (original) |\n| | exp_001_baseline_s2, _s2_extended | s2 | bjb1-45299 | (check W&B) |\n| | exp_001_baseline_s3, _s3_extended | s3 | bjb1-45299 | (check W&B) |\n| | exp_001_baseline_s4, _s4_extended | s4 | bjb1-45299 | (check W&B) |\n| | exp_009d_baseline_walker_s0 | s0 | bjb1-45299 | (check W&B) |\n| | exp_009a_baseline_walker_s2 | s2 | bjb1-45299 | (check W&B) |\n| **Trained dt_emb (CIVO trigger)** | exp_008d_subsample_on_h8 | s1 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |\n| | exp_009b_008d_walker_s2 | s2 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |\n| | exp_008d_civo_trigger_s3 | s3 | bjb1-45299 | (check W&B) |\n| | exp_008d_civo_trigger_s4 | s4 | bjb1-45299 | (check W&B) |\n| | exp_059_walker_trained_s5 | s5 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |\n| | exp_009e_008d_walker_s1 | s1 (dup=008d) | bjb1-45299 | |\n| **Frozen dt_emb** | exp_042_frozen_dt_emb_walker | s0 | bjb1-45299 | (check W&B) |\n| | exp_047_frozen_dt_emb_walker_s1 | s1 | bjb1-45299 | (check W&B) |\n| | exp_057_frozen_dt_emb_walker_s2 | s2 | bjb1-45299 | (check W&B) |\n| **No dt_emb (dim=0)** | exp_008f_no_dt_embed_subsample_on_h8 | s0 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |\n| | exp_009c_008f_walker_s2 | s2 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |\n| | exp_008f_s3_no_dt_embed_walker | s3 | bjb1-45299 | |\n| | exp_043_008f_walker_s1 | s1 | bjb1-45299 | |\n| **Untrained dt_emb** | exp_008a_no_subsample_dt2 (H=15) | s0 | bjb1-45299 | |\n| | exp_008a_unexposed_s1 | s1 | bjb1-45299 | |\n| | exp_008a_unexposed_s2 | s2 | bjb1-45299 | |\n| **dt=1 imagination** | exp_008e_v3_walker_s1 | s1 (healthy) | bjb1-45299 | |\n| | exp_008e_v3_walker_s2 | s2 (collapsed) | bjb1-45299 | |\n| | exp_008e_v3_s3 | s3 (collapsed) | — | |\n| | exp_008e_v3_s4 | s4 (healthy) | — | |\n\n**需要的图表**:\n- **Fig S1**: Walker Walk all-seed learning curves (eval return vs steps), 6 conditions 叠加，每条线标注 seed\n- **Fig S2**: Walker Walk NVE evolution per seed, same 6 conditions\n\n### B.2 Cheetah Run\n\n| Condition | exp_id(s) | Seeds | Server | Logdir |\n|-----------|-----------|-------|--------|--------|\n| **Baseline (dt=1)** | exp_023a_cheetah_baseline_s0 | s0 | — | |\n| | exp_023b_cheetah_baseline_s1, exp_010a_cheetah_baseline_s1 | s1 | bjb1-45299 | |\n| | exp_023_cheetah_baseline_s2 | s2 | — | |\n| | exp_023_cheetah_baseline_s3 | s3 | — | |\n| | exp_023_cheetah_baseline_s4, _s4_extended | s4 | — | |\n| **Trained dt_emb** | exp_010b_cheetah_civo_trigger | s1 | — | |\n| | exp_010b_cheetah_civo_trigger_s0 | s0 | — | |\n| **Frozen dt_emb** | exp_046_frozen_dt_emb_cheetah | s0 | bjb1-40020 | |\n| | exp_058_frozen_dt_emb_cheetah_s1 | s1 | — | |\n| **No dt_emb** | exp_024b_cheetah_no_dt_emb_s0 | s0 | — | |\n| | exp_024b_cheetah_no_dt_emb_s1 | s1 | bjb1-45299 | |\n\n**需要的图表**:\n- **Fig S3**: Cheetah Run all-seed learning curves\n- **Fig S4**: Cheetah Run NVE evolution per seed\n\n### B.3 Cartpole Swingup (TODO — experiments running)\n\n| Condition | exp_id(s) | Seeds | Server | ETA |\n|-----------|-----------|-------|--------|-----|\n| **Baseline** | exp_060_cartpole_baseline | s0 | bjb1-45299 cuda:0 | 5/25 13:30 |\n| **CIVO trigger** | exp_061_cartpole_civo_trigger | s0 | bjb1-45299 cuda:1 | 5/25 15:30 |\n| **No dt_emb control** | exp_062_cartpole_control | s0 | bjb1-40020 cuda:0 | 5/25 17:20 |\n\n**需要的图表**:\n- **Fig S5**: Cartpole Swingup learning curves + NVE (TODO: 待实验完成)\n\n### B.4 Manipulation Environments (PickCube, StackCube, PegInsertion)\n\n| Condition | exp_id(s) | Environment | Seeds |\n|-----------|-----------|-------------|-------|\n| **PickCube baseline** | exp_019a_v2_pickcube_baseline | PickCube-v1 | s0 |\n| **PickCube CIVO** | exp_019b_pickcube_civo_trigger | PickCube-v1 | s0 |\n| **PickCube frozen** | exp_054_pickcube_frozen_s0 | PickCube-v1 | s0 |\n| **StackCube CIVO** | exp_049_stackcube_civo_trigger_s0 | StackCube-v1 | s0 |\n| | exp_052_stackcube_civo_trigger_s1 | StackCube-v1 | s1 |\n| **StackCube frozen** | exp_051_stackcube_frozen_dt_emb_s0 | StackCube-v1 | s0 |\n| **PegInsertion CIVO** | exp_050_peginsertion_civo_trigger_s0 | PegInsertion-v1 | s0 |\n| | exp_055_peginsertion_civo_trigger_s1 | PegInsertion-v1 | s1 |\n| **PegInsertion frozen** | exp_053_peginsertion_frozen_s0 | PegInsertion-v1 | s0 |\n| | exp_056_peginsertion_frozen_s1 | PegInsertion-v1 | s1 |\n\n**需要的图表**:\n- **Fig S6**: Manipulation environments learning curves (scope limitation discussion)\n\n---\n\n## C. Intervention Hierarchy — Complete Data\n\n### C.1 Overview Table (论文 Section 3.6 核心)\n\n| Level | Method | Success Rate | Environments | exp_ids | Primary Failure Mechanism |\n|-------|--------|-------------|--------------|---------|--------------------------|\n| **L1: Gradient** | Reward-only SGS | 0/2 | Walker | 016e | No-op (gradient ≠ causal); paradoxically worse NVE=10.42× |\n| **L1: Gradient** | Full SGS | 0/3 | Walker, Cheetah | 018v2 (s1), 018 (s2), 021 | Forward-pass damage irreducible |\n| **L1: Gradient** | Obs-decoder SGS | 1/6 | Walker (4), Cheetah (2) | 025_s1✓, 025_s2✗, 025_s3✗, 025_s4✗, 026_s0✗, 026_s1✗ | Compensatory amplification + critic calibration damage |\n| **L2: Output** | RAVE ceil=2.0 | 0/1 | Walker | 028 | EMA anchor self-pollution |\n| **L2: Output** | RAVE ceil=1.5 | 0/1 | Walker | 028_ceil15 | EMA anchor self-pollution |\n| **L3: Representation** | TCN σ=0.1 | 0/1 | Walker | 029c | Borderline, dose insufficient |\n| **L3: Representation** | TCN σ=0.2 | 2/4 (Walker only) | Walker (4), Cheetah (1), PickCube (1) | 027_sigma02✓, 029a✓, 029b✗, 029d✗, 030a✗, 031✗ | Seed sensitivity + cross-env dose mismatch |\n| **L3: Representation** | TCN σ=0.5 | 0/3 | Walker (2), Cheetah (1), PickCube (1) | 027✗, 027_s1✗, 030b✗, 031b✗ | Overdose (Walker) / insufficient (Cheetah) |\n| **L3: Representation** | TCN σ=1.0 | 1/1 (CIVO only) | Cheetah | 030c | CIVO prevented but eval=47 (impossible dose) |\n| **L4: Architecture** | Dual-critic (wide) | 3/4 (CIVO), 2/4 (perf) | Walker (4), Cheetah (2), PickCube (1) | 032✓, 032b✓, 038✗(non-CIVO), 041✓ | s2 non-CIVO collapse; Cheetah partial |\n| **L4: Architecture** | Dual-critic (narrow) | 0/2 (CIVO occurs → recovery) | Walker | 035, 039 | CIVO occurs but min enables recovery |\n| **L4: Architecture** | Wide single critic | 0/1 (CIVO → partial recovery) | Walker, Cheetah | 033, 037 | Capacity alone insufficient for prevention |\n| **Control** | dt_emb removal (dim=0) | 5/5 | Walker (3), Cheetah (2) | 008f, 009c, 043, 024b_s0, 024b_s1 | — (removes the feature) |\n| **Control** | Frozen dt_emb | 5/5 | Walker (3), Cheetah (2) | 042, 047, 057, 046, 058 | — (disables training) |\n\n### C.2 SGS 详细数据\n\n**exp_016e (Reward-only SGS)**:\n- Config: reward_dt_emb_detach=True, subsample ON, H=8, seed=1\n- NVE: 10.42× (paradoxically 5× worse than untreated 008d ~2×)\n- eval: peak 326.7@75K → collapse 31.7@95K\n- Failure: Reward gradient to dt_emb is 0 by architecture — reward SGS is a no-op. 016e 与 008d 差异归因于随机变异。\n- Key insight: **Gradient magnitude ≠ causal importance** — reward head carries 38-49% of gradients but blocking it has no effect\n\n**exp_018v2_full_sgs_walker_s1 (Full SGS)**:\n- Config: all decoder gradients blocked from dt_emb\n- NVE: 1.66×, CIVO+ (above threshold)\n- eval: 448.3\n- Failure: forward-pass representational damage persists without backward-pass gradients\n\n**exp_018_full_sgs_s2**:\n- NVE: collapse\n- eval: 40.8\n\n**exp_021_full_sgs_cheetah_s1**:\n- NVE: 9.94× transient → recovery to 0.34×\n- Recovery not due to SGS (same pattern in untreated Cheetah)\n\n**exp_025 Obs-decoder SGS (Walker, 4 seeds)**:\n- s1: eval 726 (survived) but ve_ratio 0.056 @215K → **universal value collapse**\n- s2: collapsed (CIVO)\n- s3: healthy@105K → CIVO@135K (NVE 6.8×) → eval recovery 590@215K → persistent value collapse (ve_ratio 0.14)\n- s4: collapsed\n- All 4 seeds terminal ve_ratio 0.056-0.14 — critic underestimation as side effect\n\n**exp_026 Obs-decoder SGS (Cheetah, 2 seeds)**:\n- s0: NVE 21.9× (untreated baseline: 8.3×) — **compensatory amplification 2.6×**\n- s1: NVE 30.2× — **compensatory amplification 3.6×**\n- Blocking obs-decoder shifts co-adaptation to reward head\n\n### C.3 TCN 详细数据\n\n**Dose-Response Summary**:\n\n| σ | Walker | Cheetah | PickCube |\n|---|--------|---------|----------|\n| 0.1 | ⚠️ borderline (1 seed) | — | — |\n| 0.2 | ✅ 2/4, eval 45-91% | ❌ NVE 1.90 | ❌ NVE 3.71 |\n| 0.5 | ❌ oscillatory (2 seeds) | ❌ NVE 10.67 transient | ❌ insufficient |\n| 1.0 | — | ✅ CIVO prevented, ❌ eval=47 | — |\n\n**Impossible Dose (exp_030c Cheetah σ=1.0, FINAL @224K)**:\n- NVE ≤ 0.30 全程 → CIVO 完全抑制\n- eval: peak 372@35K (116% baseline) → 47@215K (15% baseline)\n- value_mean=12.4, NVE=0.26@215K → value calibration normal\n- Key: 噪声不阻止初始学习（early eval > baseline!），而是渐进腐蚀 policy\n- Cheetah CIVO prevention threshold (~σ=1.0) > noise tolerance threshold (~σ<0.5)\n- **不存在 Goldilocks zone**\n\n### C.4 RAVE 详细数据\n\n- **ceil=2.0**: EMA anchor tracks polluted imagined values → ceiling ineffective. CIVO unmitigated.\n- **ceil=1.5**: Same mechanism. More aggressive ceiling also fails because anchor is already biased.\n\n### C.5 Dual-Critic 2×2 Mechanism Factorial\n\n| | Single critic | Dual critic (min) |\n|--|--------------|-------------------|\n| ~1.05-1.2M params | **008d: CIVO → permanent collapse** | **exp_035 narrow: CIVO(NVE 2.75) → recovery → eval 697.8** |\n| ~2.4-2.9M params | **exp_033 wide: CIVO(NVE 4.75) → self-repair → eval 408** | **exp_032: CIVO prevented (NVE≤1.1) → eval 670-788** |\n\n- **v1 ≈ v2 across all configs** (ρ>0.999): Double Q pessimism mechanism fails in pure-imagination MBRL\n- **Min >> Capacity for recovery**: 697.8 vs 408\n- **Prevention requires min+capacity synergy**: only exp_032 (min+wide) prevents CIVO entirely\n- **Cross-env caveat**: Walker recovery sufficient (697.8), Cheetah recovery insufficient (97.5, 31%)\n\n---\n\n## D. NVE Diagnostic — Complete Data\n\n### D.1 NVE Threshold Analysis (plan_034)\n\n- **AUROC = 0.961** (29 experiments, 2 environments)\n- **Optimal threshold: 1.5× (Youden-optimal: 1.53×)**\n- **F1 = 0.880** at threshold 1.5×\n- **TPR/FPR**: 15/16 CIVO-positive correctly identified, AUROC near-perfect separation\n\n**Threshold Sensitivity**:\n\n| Threshold | TPR | FPR | F1 | Notes |\n|-----------|-----|-----|----|-------|\n| 1.0× | 16/16 | high | lower | Over-sensitive |\n| 1.25× | 16/16 | moderate | moderate | |\n| **1.5×** | **15/16** | **low** | **0.880** | **Optimal (Youden)** |\n| 2.0× | 12/16 | very low | lower | Under-sensitive |\n| 3.0× | 8/16 | 0 | lower | Too conservative |\n\n**时间限定**: NVE>1.5× diagnostic 适用于 **35K+ steps**（baseline v/e 已收敛至 >0.24）。25K 处 baseline v/e 仅 0.087，微小绝对差异被放大。\n\n### D.2 Per-Experiment NVE Summary\n\n**Walker Walk (trained dt_emb)**:\n| exp_id | Seed | NVE_peak | NVE_step | Outcome | Classification |\n|--------|------|----------|----------|---------|----------------|\n| exp_008d_subsample_on_h8 | s1 | 4.12×@55K | 35K+ sustained | Collapse | CIVO |\n| exp_009b_008d_walker_s2 | s2 | 2.05×@25K, 1.62×@45K | Transient | Self-correction (eval 268) | CIVO (self-correcting) |\n| exp_008d_civo_trigger_s3 | s3 | (sustained CIVO) | 35K+ | Collapse | CIVO |\n| exp_008d_civo_trigger_s4 | s4 | (sustained CIVO) | 35K+ | Collapse | CIVO |\n| exp_059_walker_trained_s5 | s5 | 4.72×@85K | 85K | Collapse (eval 95.8 = 10.5% baseline) | Onset_collapse (Collapse†) |\n\n**Walker Walk (no dt_emb / frozen / untrained)**:\n| exp_id | Seed | NVE_peak | Outcome | Classification |\n|--------|------|----------|---------|----------------|\n| exp_008f (dim=0) | s0 | 1.02× | Stable | No CIVO |\n| exp_009c (dim=0) | s2 | 1.26× | Borderline but stable | No CIVO |\n| exp_042 (frozen) | s0 | 0.19× | Stable | No CIVO |\n| exp_047 (frozen) | s1 | 1.71× transient | Stable | No CIVO (transient) |\n| exp_057 (frozen) | s2 | (stable) | Stable | No CIVO |\n| exp_008a (untrained) | s0 | 0.59-0.93× | Two recovery cycles | No CIVO |\n\n**Cheetah Run**:\n| exp_id | Seed | NVE_peak | Outcome | Classification |\n|--------|------|----------|---------|----------------|\n| exp_010b s0 | s0 | 70.64× | Collapse (irreversible) | CIVO (severe) |\n| exp_010b s1 | s1 | 8.27× | Collapse | CIVO |\n| exp_046 (frozen) | s0 | 1.35× | Stable | No CIVO |\n| exp_058 (frozen) | s1 | (stable) | Stable | No CIVO |\n\n### D.3 AUROC Confusion Matrix (at threshold 1.5×, 35K+)\n\n|  | Predicted CIVO+ | Predicted CIVO- |\n|--|-----------------|-----------------|\n| **Actual CIVO+** | TP = 15 | FN = 1 |\n| **Actual CIVO-** | FP = 0 | TN = 13 |\n\n- Precision = 15/15 = 1.000\n- Recall = 15/16 = 0.938\n- F1 = 0.880 (based on n=29 full dataset, TODO: verify exact calculation)\n- AUROC = 0.961\n\n### D.4 NVE Baseline Reference Values (exp_001 s1)\n\n| Step | baseline v/e | baseline ve_ratio |\n|------|-------------|-------------------|\n| 25K | 8.7% | 0.087 |\n| 35K | 24.1% | 0.241 |\n| 45K | 33.1% | 0.331 |\n| 55K | 40.4% | 0.404 |\n| 65K | 56.3% | 0.563 |\n| 85K | — | 0.7007 |\n| 105K | — | 0.656 |\n\n---\n\n## E. RSSM Fidelity Analysis (exp_063)\n\n### E.1 Model Comparison Table\n\n| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |\n|-------|------------|------------|---------|---------------|---------------|------------|\n| baseline (exp_001) | 13.49 | 27.50 | **2.04×** | 0.0102 | 0.0159 | 1.56× |\n| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30×** | 0.0568 | 0.1579 | **2.78×** |\n| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75×** | 0.7469 | 0.7526 | 1.01× |\n\n**解读**:\n- 008d 低 obs gap ratio (1.30×) 具有误导性 — dt=1 绝对误差已是 baseline 的 3× (model 已崩塌)\n- 008d reward gap (2.78×) 表明 dt_emb 使 reward head 能区分 dt=1/dt=2 但在 dt=2 上系统性偏差\n- 008f reward gap 仅 1.01× — 没有 dt_emb 的 reward head 完全无法区分不同 dt\n\n### E.2 Gradient Decomposition (dt_emb.weight)\n\n| Source | 55K (%) | 112K (%) |\n|--------|---------|----------|\n| Reward head | 49.0 | 38.1 |\n| KL dynamics | 34.7 | 40.4 |\n| Obs decoders | 16.3 | 21.5 |\n| Cont head | ~0 | ~0 |\n\n**Key finding**: Gradient magnitude ≠ causal importance. Reward head 最大梯度 (49%) 但 reward-only SGS 完全无效; obs decoder 最小非零梯度 (16%) 但携带 Δt-specific 空间信息。\n\n### E.3 Timeseries RSSM Fidelity (exp_066, RUNNING)\n\n- 12 dense checkpoints, 每 5K steps, 0-60K 训练过程\n- 目标：建立 RSSM fidelity gap → NVE 的时序因果链\n- TODO: 待 exp_066 完成后补充数据\n\n---\n\n## F. Actor Entropy Causal Chain (plan_031)\n\n### F.1 Summary\n\nCollapsed configs (trained dt_emb) 的 actor entropy 在 CIVO onset 后爆炸性增长:\n- **Collapsed**: +2.1 nats / 10K steps (after collapse onset)\n- **Healthy**: +0.07 ~ +0.22 nats / 10K steps\n\n### F.2 Temporal Causation\n\n时序因果链确认: **return 先崩 → entropy 后升**\n- 非 entropy 先升导致 return 崩 (排除 exploration failure 假说)\n- 与 CIVO 叙事一致: value overestimation → actor exploits overestimated values → policy degrades → entropy increases as learned policy collapses\n\n### F.3 Data Source\n- Artifact: `artifacts/actor_entropy_analysis.md`\n- All experiments with actor_entropy logged via W&B\n\n---\n\n## G. Value Prediction Distribution (exp_064)\n\n### G.1 Summary\n- trained dt_emb (008d collapsed): V(s) systematically overestimates at dt=2 imagination steps\n- untrained/absent dt_emb (008f) + baseline (001): V(s) tracks MC return closely\n- **直观展示 CIVO 的 value divergence 位置和形态**\n\n### G.2 Charts\n- Scatter plot: V(s) vs MC return per config\n- Histogram: value ratio distribution\n- Value bias vs timestep within imagination rollout\n\n### G.3 Data Source\n- Server: bjb1-40020\n- Artifact directory: `artifacts/exp_064_value_distribution/`\n\n---\n\n## H. Cosine Similarity Analysis (exp_065)\n\n### H.1 Summary\n- dt=1 vs dt=2 embedding cosine similarity 及训练过程演化\n- 判断 CIVO 来自微小差异被 downstream 放大 (high cosine sim) 还是 dt=2 表征本身偏差 (low cosine sim)\n\n### H.2 Charts\n- `cosine_sim_evolution.png`: cosine similarity vs training steps\n- `pairwise_heatmap.png`: 所有 dt embedding 向量的 pairwise similarity\n\n### H.3 Data Source\n- Server: bjb1-45299\n- Logdir: `/root/dreamerv3-torch/logdir/exp_065_dt_emb_cosine/`\n\n---\n\n## I. Negative Results — Detailed Analysis\n\n### I.1 High-Value Negative Results (7 categories)\n\n**1. Event-Gated Mechanisms (exp_003/004/005)**:\n- Learned gate → all degrade/collapse\n- Insight: adaptive temporal abstraction in imagination is fundamentally difficult, not just a hyperparameter issue\n\n**2. Reward-only SGS (016e)**:\n- Paradoxically worse (NVE 10.42× vs untreated ~2×)\n- Insight: blocking reward gradient forces dt_emb adaptation through obs-decoder, reinforcing spatial bias\n\n**3. Full SGS Failure (018/018v2/021)**:\n- 0/3 across 2 environments despite blocking ALL non-KL gradients\n- Insight: forward-pass representational damage is irreducible; backward-pass interventions are categorically insufficient\n\n**4. Obs-decoder SGS Compensatory Amplification (025/026)**:\n- Cheetah: blocking obs-decoder → 2.6-3.6× NVE amplification vs untreated\n- Insight: CIVO exploits redundant pathways; blocking one strengthens others\n\n**5. RAVE Anchor Pollution (028)**:\n- EMA tracks polluted imagined values → ceiling is anchored too high\n- Insight: output-level interventions fail when the reference signal is contaminated\n\n**6. TCN Dose-Environment Impossibility (030c)**:\n- Cheetah σ=1.0: CIVO prevented but eval→47 (15% baseline)\n- Key: effective dose > tolerable dose → no Goldilocks zone exists\n- Insight: representation-level noise is environment-specific and cannot be universalized\n\n**7. Dual-Critic Non-CIVO Collapse (038)**:\n- eval 354→121 with normal NVE (≤0.3), actor entropy ↑\n- Insight: trained dt_emb creates vulnerability through multiple pathways (CIVO = Pathway A, policy instability = Pathway B)\n\n### I.2 Contribution to Paper Narrative\n\nThese negative results form two positive contributions:\n1. **Intervention Hierarchy**: systematic taxonomy proving CIVO is fundamentally hard to mitigate at all 3 intervention levels\n2. **Multi-Pathway Vulnerability**: trained dt_emb creates both CIVO (value-driven) and non-CIVO (eval-driven) failure modes\n\n---\n\n## J. Figures & Tables Checklist\n\n### Main Paper Figures (planned)\n| # | Type | Content | Status |\n|---|------|---------|--------|\n| Fig 1 | Learning curves | Hero figure: all experiments overlaid | TODO |\n| Fig 2 | Line plot | Value/eval ratio — healthy vs pathological | TODO |\n| Fig 3 | Grid/heatmap | Factorial grid summary (dt_emb × subsample) | TODO |\n| Fig 4 | Diagram | Causal chain: dt_emb → value overestimation → collapse | TODO |\n| Fig 5 | Line plot | dt=1 vs dt=2 vs dt=4 monotonic degradation | TODO |\n| Table 1 | Table | RSSM fidelity — absolute + ratio | TODO |\n| Fig 6 | Line plot | Mitigation comparison (008e_v3 seeds) | TODO |\n\n### Supplementary Figures\n| # | Type | Content | Data Source | Status |\n|---|------|---------|-------------|--------|\n| Fig S1 | Multi-line plot | Walker all-seed learning curves (6 conditions) | W&B / logdir | TODO |\n| Fig S2 | Multi-line plot | Walker NVE evolution per seed | W&B / logdir | TODO |\n| Fig S3 | Multi-line plot | Cheetah all-seed learning curves | W&B / logdir | TODO |\n| Fig S4 | Multi-line plot | Cheetah NVE evolution per seed | W&B / logdir | TODO |\n| Fig S5 | Multi-line plot | Cartpole learning curves + NVE | exp_060/061/062 | TODO (running) |\n| Fig S6 | Multi-line plot | Manipulation environments | W&B | TODO |\n| Fig S7 | Bar chart | Intervention hierarchy success rates | Section C | TODO |\n| Fig S8 | Scatter | Value distribution V(s) vs MC return | exp_064 | DONE (artifacts/) |\n| Fig S9 | Histogram | Value ratio distribution | exp_064 | DONE (artifacts/) |\n| Fig S10 | Line plot | NVE threshold sensitivity (ROC curve) | plan_034 | TODO |\n| Fig S11 | Line plot | Actor entropy evolution (collapsed vs healthy) | plan_031 | DONE (artifacts/) |\n| Fig S12 | Heatmap | dt_emb cosine similarity | exp_065 | DONE (server) |\n| Fig S13 | Line plot | Cosine similarity evolution | exp_065 | DONE (server) |\n| Fig S14 | Line plot | RSSM fidelity timeseries | exp_066 | TODO (running) |\n| Fig S15 | Line plot | TCN dose-response curves | exp_027-031 | TODO |\n| Fig S16 | Line plot | Dual-critic v1 vs v2 correlation | exp_032-041 | TODO |\n| Fig S17 | Bar chart | Gradient decomposition (dt_emb.weight) | exp_063 | TODO |\n\n### Supplementary Tables\n| # | Content | Status |\n|---|---------|--------|\n| Table S1 | Complete experiment registry (A.1+A.2) | This document |\n| Table S2 | Intervention hierarchy full data (C.1) | This document |\n| Table S3 | NVE per-experiment values (D.2) | This document |\n| Table S4 | AUROC confusion matrix (D.3) | This document |\n| Table S5 | RSSM fidelity all models (E.1) | This document |\n| Table S6 | Gradient decomposition (E.2) | This document |\n| Table S7 | TCN dose-response full table (C.3) | This document |\n| Table S8 | Dual-critic 2×2 factorial (C.5) | This document |\n| Table S9 | Baseline NVE reference values (D.4) | This document |\n\n---\n\n## K. Outstanding TODOs\n\n### Data Gaps\n- [ ] **Cartpole results** (exp_060/061/062): running, ETA 5/25 17:20 UTC → Section B.3, Fig S5\n- [ ] **exp_066 RSSM fidelity timeseries**: running → Section E.3, Fig S14\n- [ ] **Per-experiment logdir paths**: many experiments missing exact logdir — need W&B run URLs or server paths\n- [ ] **Exact key_metrics** for all experiments: registry fields are sparse, need per-experiment data from W&B\n\n### Figures to Generate\n- [ ] Fig S1-S6: All-seed learning curves per environment (from W&B data)\n- [ ] Fig S7: Intervention hierarchy bar chart\n- [ ] Fig S10: NVE ROC curve with threshold annotations\n- [ ] Fig S15: TCN dose-response (σ vs NVE, σ vs eval, per environment)\n- [ ] Fig S16: Dual-critic v1-v2 scatter plots\n- [ ] Fig S17: Gradient decomposition stacked bar chart\n\n### Writing\n- [ ] LaTeX appendix template (ICML 2026 supplementary format)\n- [ ] Cross-reference main paper figure/table numbering\n- [ ] Proofread all experiment descriptions for consistency\n- [ ] Add IQM + CI for multi-seed conditions (per Agarwal et al. 2021)\n- [ ] Verify AUROC F1 calculation (currently 0.880 — confirm formula used)\n\n---\n\n## L. Data Source Registry\n\n| Source | Location | Access |\n|--------|----------|--------|\n| W&B project | (project W&B URL) | wandb API |\n| Server bjb1-45299 | ssh connect.bjb1.seetacloud.com | SSH |\n| Server bjb1-40020 | ssh connect.bjb1.seetacloud.com | SSH |\n| Local artifacts | `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/` | Local |\n| Registry | `read_registry(project=\"event-gated-adaptive-horizon\")` | MCP tool |\n| Experiment code | `/root/autodl-tmp/event-gated-adaptive-horizon/` (on server) | SSH |\n"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-25T00:34:52.471837+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/supplementary_framework.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-25T00:34:52.471998+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "supplementary_framework",
  "type": "report",
  "description": "ICML 2026 supplementary material framework — complete appendix structure with experiment tables, intervention hierarchy data, NVE diagnostics, figure/table checklist, and TODO tracking",
  "project": "event-gated-adaptive-horizon",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/supplementary_framework.md",
  "tags": "['supplementary', 'icml2026', 'appendix', 'framework']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "supplementary_framework",
    "type": "report",
    "description": "ICML 2026 supplementary material framework — complete appendix structure with experiment tables, intervention hierarchy data, NVE diagnostics, figure/table checklist, and TODO tracking",
    "project": "event-gated-adaptive-horizon",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/supplementary_framework.md",
    "tags": "['supplementary', 'icml2026', 'appendix', 'framework']"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-25T00:34:52.472169+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260525_3f4736\", \"name\": \"supplementary_framework\", \"type\": \"report\", \"description\": \"ICML 2026 supplementary material framework — complete appendix structure with experiment tables, intervention hierarchy data, NVE diagnostics, figure/table checklist, and TODO tracking\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/report/supplementary_framework.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-25T00:34:38.238917+00:00\", \"tags\": [\"supplementary\", \"icml2026\", \"appendix\", \"framework\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_supplementary-framework_20260525T002818",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-25T00:34:52.472354+00:00_

文档已生成并注册。结构概览：

**12 个 Section (A-L)**:

| Section | 内容 | 状态 |
|---------|------|------|
| A | 完整实验表 (69 success + 36 negative + 4 running) | ✅ |
| B | 全 seed 学习曲线清单 (Walker/Cheetah/Cartpole/Manipulation) | ✅ 框架，Cartpole 待实验完成 |
| C | Intervention Hierarchy 完整数据 (SGS/TCN/RAVE/Dual-critic) | ✅ |
| D | NVE Diagnostic (AUROC=0.961, confusion matrix, per-exp NVE) | ✅ |
| E | RSSM Fidelity + Gradient Decomposition | ✅，exp_066 timeseries 待完成 |
| F | Actor Entropy 因果链 | ✅ |
| G | Value Prediction Distribution | ✅ |
| H | Cosine Similarity Analysis | ✅ |
| I | 7 类 Negative Results 详细分析 | ✅ |
| J | 17 张 Supplementary Figures + 9 张 Tables checklist | ✅ |
| K | Outstanding TODOs | ✅ |
| L | Data Source Registry | ✅ |

**主要 TODO**: Cartpole 实验结果 (5/25 完成)、exp_066 RSSM timeseries、17 张待生成图表、LaTeX 排版。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_supplementary-framework_20260525T002818"
}
```

</details>

---
