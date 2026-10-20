# Research conversation: <agent_context> D028 决策：暂停论文写作直到核心数字一致性修复完成（至少 3 套数据源混用问题）。 关键实验： - plan-012-full: DONE/success, 11 tasks/245 eps, death — Part 2 of 2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-agent-context-d028-3-plan-012-full-done-success-11-tasks-245-eps-death.md) · [Structured JSON](../../../sessions/23/239c633bdcd23ef98ea7.json)

## Round 1

### Tool call

_source line 129 · 2026-05-14T08:01:28.870Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01JCnpMtp26F8LQsFieY4Cdv`</summary>

````json
{
  "project": "simgate-modular-routing",
  "file": "number_consistency_audit.md",
  "content": "# D028 核心数字一致性审计报告\n\n审计日期：2026-05-14\n\n---\n\n## 一、数据宇宙地图\n\n项目存在 **三套独立数据源**，数字混用是不一致的根因。\n\n| 编号 | 数据源 | Tasks | Episodes | 用途 | 可靠性 |\n|------|--------|-------|----------|------|--------|\n| **A** | plan-001b 完整版 | 11 | 245 | plan-012 decomposition 分析 | ★★★ 权威 |\n| **B** | prescreening 全集 | 30 | 249 | 早期探索性分析 | ★★ 每 task 仅 5-9 eps |\n| **C** | plan-001b 早期子集 | 11 | 194 | plan-003 baseline + SFT 训练数据 | ★★★ 权威（用途不同） |\n\n### 11 Tasks（A、C 共享任务列表）\n\nchemistry-mix, find-animal, find-non-living-thing, freeze, grow-fruit, identify-life-stages-1, identify-life-stages-2, inclined-plane-determine-angle, lifespan-longest-lived, lifespan-longest-lived-then-shortest-lived, measure-melting-point-unknown-substance\n\n---\n\n## 二、权威数字表\n\n### 2.1 Decomposition 分析（plan-012-full，数据源 A）\n\n| 指标 | 值 | 来源文件 | 验证状态 |\n|------|---|---------|---------|\n| Δ_full | **+29.60** | `results/plan_012_decomposition` (CSV) | ✅ 加权平均验算一致 |\n| Δ_nd | **+2.84** | registry plan-012-full | ✅ 与 daf 计算一致 |\n| death_avoidance_fraction | **90.41%** | = 1 - 2.84/29.60 | ✅ |\n| pearson_r | **0.9698** | registry plan-012-full | ✅ (death_rate_diff vs delta) |\n| pearson_p | **8.12e-07** | registry plan-012-full | ✅ |\n| n_tasks | **11** | CSV 行数 | ✅ |\n| n_episodes | **245** | CSV n 列求和 | ✅ (20+20+40+20+20+20+20+20+25+20+20) |\n| death_rate_int (agg) | **0.429** | registry | ✅ |\n| death_rate_det (agg) | **0.163** | registry | ✅ |\n| label_dist | det=86, int=9, no_pref=150 | CSV det_pref/int_pref/no_pref 列 | ✅ |\n\n**来源文件**：`results/plan_012_decomposition`（CSV，与 `results/death_decomposition_preliminary.csv` 内容相同）\n\n### 2.2 Baseline 评估（plan-003-baseline，数据源 C）\n\n| 策略 | continuous_score | success_rate | death_rate | sim_ratio | 验证 |\n|------|-----------------|-------------|-----------|-----------|------|\n| always-internal | **-37.16** | 12.37% | 40.72% | 0.0 | ✅ |\n| always-deterministic | **-11.64** | 23.71% | 18.56% | 1.0 | ✅ |\n| oracle | **-9.03** | 24.23% | 16.49% | 0.962 | ✅ |\n| random | **-23.75** | 16.49% | 28.35% | 0.503 | ✅ |\n| trained-router (v6) | -11.64 | 23.71% | 18.56% | 1.0 | ⚠️ 退化 |\n\n**n_episodes = 194, n_tasks = 11**\n**来源文件**：`results/plan_003_eval/overall_results.json`\n\n> ⚠️ **trained-router 完全退化**：与 always-deterministic 数字完全相同，sim_ratio=1.0 说明 router 100% 选择 deterministic。该行不可用于论文。\n\n### 2.3 Keyword Baseline（plan-011-rule-based）\n\n| 版本 | 关键词数 | Episodes | 匹配率 | 准确率 | 退化方向 |\n|------|---------|----------|--------|--------|---------|\n| v1 | 20 | 204 | 85.8% | 97.65% | → always-det（\"connect\" 假阳性） |\n| v2 | 17 | 203 | 4.9% | 1.19% | → always-internal |\n| v3 | 9 | 225 | 6.1% | 23.26% | → always-internal |\n\n**来源文件**：`results/rule_based_accuracy_v1_rerun.json`, `results/rule_based_accuracy_v2_test.json`, `results/rule_based_accuracy_v3.json`\n\n> 三版 keyword heuristic 均结构性失效。v1 \"高准确率\" 是 \"connect\" 关键词的假阳性造成（匹配 3963 次，ScienceWorld 大量 connect 动作 → 几乎所有 episode 都路由到 det）。\n\n### 2.4 SFT 训练数据\n\n| 指标 | 值 | 来源文件 | 验证 |\n|------|---|---------|------|\n| 样本数 | **2040** | `data/plan-004-implicit/implicit_sft.jsonl` | ✅ wc -l = 2040 |\n| deterministic 标签 | **1830** (89.7%) | `data/plan-004-implicit/conversion_summary.json` | ✅ |\n| internal 标签 | **210** (10.3%) | 同上 | ✅ |\n| 来源 episodes | **68** (有 preference 的) | 从 194 eps 中提取 | ✅ 与 plan-005 routing_patterns 一致 |\n| MD5 | c9b59e04de78 | 任务描述中给出 | 未重新验证 |\n\n> `data/plan-004-v3/implicit_sft.jsonl` 与上述文件完全相同（2040 行，同分布）。\n\n---\n\n## 三、不一致清单\n\n### INC-1：death_decomposition_report.json ≠ plan-012-full（严重）\n\n| | death_decomposition_report.json | plan-012-full (CSV) |\n|---|---|---|\n| Tasks | 30 | **11** ← 权威 |\n| Episodes | 249 | **245** ← 权威 |\n| Δ_full | 38.33 | **29.60** ← 权威 |\n| Δ_nd | 0.48 | **2.84** ← 权威 |\n| death_frac | 98.75% | **90.41%** ← 权威 |\n| r | 0.9864 | **0.9698** ← 权威 |\n\n**原因**：`death_decomposition_report.json` 使用的是 prescreening 30-task 数据（数据源 B），不是 plan-012-full。两者文件名容易混淆。\n\n**正确值**：论文必须引用 11 tasks / 245 episodes 的数字（plan-012-full），来源 `results/plan_012_decomposition`。\n\n### INC-2：Episode 数量差异 245 vs 194（已解释，非错误）\n\n| Task | plan-003 (C) | plan-012 (A) | 增量 |\n|------|-------------|-------------|------|\n| chemistry-mix | 20 | 20 | 0 |\n| find-animal | 15 | 20 | +5 |\n| find-non-living-thing | 35 | 40 | +5 |\n| freeze | 20 | 20 | 0 |\n| grow-fruit | 15 | 20 | +5 |\n| identify-life-stages-1 | 15 | 20 | +5 |\n| identify-life-stages-2 | 15 | 20 | +5 |\n| inclined-plane-determine-angle | 15 | 20 | +5 |\n| lifespan-longest-lived | 9 | 25 | +16 |\n| lifespan-longest-lived-then-shortest-lived | 15 | 20 | +5 |\n| measure-melting-point-unknown-substance | 20 | 20 | 0 |\n| **总计** | **194** | **245** | **+51** |\n\n**原因**：plan-001b 后续追加了 rebalance 实验（plan-001b-gpu1-rebalance 等），将 8 个 task 从 9-15 eps 扩展到 20-25 eps，使每个 task 达到最少 20 episodes。plan-003 baseline 在扩展前跑的。\n\n**影响**：\n- plan-003 baseline 数字基于 194 eps，plan-012 decomposition 基于 245 eps → 两组数字**不可直接对比**\n- SFT 训练数据（2040 samples）来自 194-episode 子集，未包含后续追加的 51 episodes\n\n### INC-3：plan005/routing_metrics.json 混合数据源\n\n该文件包含 30 tasks，但 episode 数量与 prescreening 和 plan-001b 都不完全匹配（如 find-animal=25, grow-fruit=18, mendelian-genetics-known-plant=7）。这是 prescreening + plan-001b 混合数据。**不应用于论文。**\n\n### INC-4：rule_based_accuracy 各版本 episode 数不一致\n\nv1=204, v2=203, v3=225。原因是不同版本跑在不同 task 子集上，且 v1/v2 用 prescreening+mvp 数据，v3 用 plan_c 数据。论文引用时需注明具体版本和 episode 数。\n\n### INC-5：死亡率指标命名不统一\n\n- plan-003 用 `catastrophic_failure_rate`\n- plan-012 用 `death_rate_int` / `death_rate_det`\n- decomposition report 用 `int_death_rate` / `det_death_rate`\n\n含义相同，但命名混乱。论文中统一使用 \"death rate\"。\n\n### INC-6：death_decomposition_preliminary_OLD.csv 过时数据\n\nOLD 版本 chemistry-mix 只有 10 episodes（总 235），当前版本 20 episodes（总 245）。OLD 版本已弃用。\n\n---\n\n## 四、建议：论文写作数字选择\n\n### Table 1: Baseline Comparison\n使用 **plan-003 数据（194 eps / 11 tasks）**\n\n| Strategy | Score |\n|----------|-------|\n| Always-Internal | -37.16 |\n| Always-Deterministic | -11.64 |\n| Oracle | -9.03 |\n| Random | -23.75 |\n\n注：trained-router 行删除或标注为 \"degenerate (v6)\"，不可作为有效结果呈现。\n\n### Death Decomposition Analysis\n使用 **plan-012-full 数据（245 eps / 11 tasks）**\n\n| Metric | Value |\n|--------|-------|\n| Δ_full | +29.60 |\n| Δ_nd | +2.84 |\n| Death Avoidance Fraction | 90.41% |\n| Pearson r | 0.9698 (p = 8.12e-07) |\n\n### Keyword Baseline\n使用 **plan-011 v3 数据**，报告 episode-level accuracy = 23.26%，说明结构性失效。简述 v1/v2 退化方向作为补充证据。\n\n### SFT Data Description\n- 2040 step-level samples from 68 preferenced episodes (out of 194)\n- Label distribution: 89.7% deterministic, 10.3% internal\n- 来源：`data/plan-004-implicit/implicit_sft.jsonl`\n\n### ⚠️ 绝对不引用的数字\n1. `death_decomposition_report.json` 的 30-task 数字（Δ=38.33, daf=98.75%, r=0.9864）\n2. `plan005/routing_metrics.json` 的任何数字（混合数据源）\n3. `results/plan_c_test_labels/` 下的任何文件（标签损坏）\n4. `death_decomposition_preliminary_OLD.csv`（过时，chemistry-mix n=10）\n5. trained-router 结果（退化，与 always-det 完全相同）\n\n---\n\n## 五、数据谱系图\n\n```\nplan-001b 实验执行\n├── 初始跑 → 194 episodes (11 tasks)  [数据源 C]\n│   ├── plan-003: baseline eval (always-int/det/oracle/random)\n│   ├── plan-005: routing pattern analysis → 68 episodes with preference\n│   │   └── plan-004: implicit_sft.jsonl (2040 samples)\n│   └── plan-002: explicit router training (v1-v6, all degenerate except ablation-b)\n│\n├── rebalance 追加 → +51 episodes → 245 episodes (11 tasks)  [数据源 A]\n│   └── plan-012-full: death decomposition (Δ=29.60, daf=90.41%, r=0.9698)\n│\nprescreening 实验\n└── 30 tasks × 5-9 eps → 249 episodes  [数据源 B]\n    ├── death_decomposition_report.json (Δ=38.33, daf=98.75%, r=0.9864)\n    ├── plan005/routing_metrics.json (混合版)\n    └── rule_based_accuracy 各版本\n```\n\n---\n\n## 六、遗留问题\n\n1. **plan-003 与 plan-012 的 baseline 不可直接比**：baselines 在 194 eps 上跑，decomposition 在 245 eps 上跑。论文如要在同一张表中呈现，需声明 episode 数量不同，或在 245 eps 上重跑 baselines。\n2. **SFT 数据不含追加 episodes**：2040 样本来自 194-episode 子集。如果扩展到 245 episodes，训练数据应相应更新（预计增加 ~500 step-level samples）。\n3. **trained-router 无有效结果**：plan-002-formal-v6 退化。plan-004-ablation-b 是唯一非退化模型（internal recall=51.5%，但 precision=15.9%），但未在 plan-003 框架下做 end-to-end eval。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9fe9242-e911-406b-8fd1-89de8be1a0f3",
  "isSidechain": false,
  "requestId": "req_011Cb27CuAnkzXypC9zp26Xs",
  "type": "assistant",
  "uuid": "0f52c6de-6c10-424d-b95a-986e976adb08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "64bf8e9c-9c87-47ba-adf7-bb88b4fb1455",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YY7QKsBXZPXZ7PbR7dkphq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6158,
      "cache_read_input_tokens": 107132,
      "output_tokens": 5773,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6158,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5773,
          "cache_read_input_tokens": 107132,
          "cache_creation_input_tokens": 6158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6158
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 130 · 2026-05-14T08:01:29.012Z_

<details><summary>↩ Tool result · `toolu_01JCnpMtp26F8LQsFieY4Cdv`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'number_consistency_audit.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f52c6de-6c10-424d-b95a-986e976adb08",
  "isSidechain": false,
  "promptId": "8f5e3863-8f23-4c69-a31a-63dbda3a511d",
  "type": "user",
  "uuid": "8e403883-a529-4e36-bd68-74a8367d0001",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file 'number_consistency_audit.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file 'number_consistency_audit.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "0f52c6de-6c10-424d-b95a-986e976adb08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "64bf8e9c-9c87-47ba-adf7-bb88b4fb1455",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 131 · 2026-05-14T08:01:32.914Z_

<details><summary>Logged reasoning block</summary>

```text
The file isn't in the whitelist. I need to use a different approach — either save to memory.md or use register_artifact. Let me save it as a local file and register it as an artifact.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e403883-a529-4e36-bd68-74a8367d0001",
  "isSidechain": false,
  "requestId": "req_011Cb27MUaC5pXRHVfS7rRzY",
  "type": "assistant",
  "uuid": "897e944c-e134-4962-aad9-899ed25394ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "64bf8e9c-9c87-47ba-adf7-bb88b4fb1455",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012y5bu1FDyoNddBmmXkQfSs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5860,
      "cache_read_input_tokens": 113290,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 113290,
          "cache_creation_input_tokens": 5860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5860
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 132 · 2026-05-14T08:01:33.890Z_

文件名不在白名单。我将保存为 artifact 文件并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "897e944c-e134-4962-aad9-899ed25394ee",
  "isSidechain": false,
  "requestId": "req_011Cb27MUaC5pXRHVfS7rRzY",
  "type": "assistant",
  "uuid": "68ca4d9b-8d2d-4e94-bea9-ddda2783719d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "64bf8e9c-9c87-47ba-adf7-bb88b4fb1455",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012y5bu1FDyoNddBmmXkQfSs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5860,
      "cache_read_input_tokens": 113290,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 113290,
          "cache_creation_input_tokens": 5860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5860
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 133 · 2026-05-14T08:01:34.874Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HCnrSe1TT9zeRR8F3YoKBG`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68ca4d9b-8d2d-4e94-bea9-ddda2783719d",
  "isSidechain": false,
  "requestId": "req_011Cb27MUaC5pXRHVfS7rRzY",
  "type": "assistant",
  "uuid": "a90a3dc1-1645-4ad7-aeb9-afd6ac32bcda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "64bf8e9c-9c87-47ba-adf7-bb88b4fb1455",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012y5bu1FDyoNddBmmXkQfSs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5860,
      "cache_read_input_tokens": 113290,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 113290,
          "cache_creation_input_tokens": 5860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5860
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 134 · 2026-05-14T08:01:34.884Z_

<details><summary>↩ Tool result · `toolu_01HCnrSe1TT9zeRR8F3YoKBG`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a90a3dc1-1645-4ad7-aeb9-afd6ac32bcda",
  "isSidechain": false,
  "promptId": "8f5e3863-8f23-4c69-a31a-63dbda3a511d",
  "type": "user",
  "uuid": "26dbafca-c66a-47d0-8be2-b2daf3baf606",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 29
  },
  "sourceToolAssistantUUID": "a90a3dc1-1645-4ad7-aeb9-afd6ac32bcda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "64bf8e9c-9c87-47ba-adf7-bb88b4fb1455",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 135 · 2026-05-14T08:03:06.393Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01R3tUcgafEU9EgPoQ7pooHY`</summary>

````json
{
  "name": "D028 Number Consistency Audit",
  "type": "report",
  "description": "D028 核心数字一致性审计报告：审计所有实验数据源，识别三套数据宇宙（A=245eps, B=249eps, C=194eps），发现6项不一致，生成权威数字表和论文写作建议",
  "project": "simgate-modular-routing",
  "content": "# D028 核心数字一致性审计报告\n\n审计日期：2026-05-14\n\n---\n\n## 一、数据宇宙地图\n\n项目存在 **三套独立数据源**，数字混用是不一致的根因。\n\n| 编号 | 数据源 | Tasks | Episodes | 用途 | 可靠性 |\n|------|--------|-------|----------|------|--------|\n| **A** | plan-001b 完整版 | 11 | 245 | plan-012 decomposition 分析 | ★★★ 权威 |\n| **B** | prescreening 全集 | 30 | 249 | 早期探索性分析 | ★★ 每 task 仅 5-9 eps |\n| **C** | plan-001b 早期子集 | 11 | 194 | plan-003 baseline + SFT 训练数据 | ★★★ 权威（用途不同） |\n\n### 11 Tasks（A、C 共享任务列表）\n\nchemistry-mix, find-animal, find-non-living-thing, freeze, grow-fruit, identify-life-stages-1, identify-life-stages-2, inclined-plane-determine-angle, lifespan-longest-lived, lifespan-longest-lived-then-shortest-lived, measure-melting-point-unknown-substance\n\n---\n\n## 二、权威数字表\n\n### 2.1 Decomposition 分析（plan-012-full，数据源 A）\n\n| 指标 | 值 | 来源文件 | 验证状态 |\n|------|---|---------|---------|\n| Δ_full | **+29.60** | `results/plan_012_decomposition` (CSV) | ✅ 加权平均验算一致 |\n| Δ_nd | **+2.84** | registry plan-012-full | ✅ 与 daf 计算一致 |\n| death_avoidance_fraction | **90.41%** | = 1 - 2.84/29.60 | ✅ |\n| pearson_r | **0.9698** | registry plan-012-full | ✅ (death_rate_diff vs delta) |\n| pearson_p | **8.12e-07** | registry plan-012-full | ✅ |\n| n_tasks | **11** | CSV 行数 | ✅ |\n| n_episodes | **245** | CSV n 列求和 | ✅ (20+20+40+20+20+20+20+20+25+20+20) |\n| death_rate_int (agg) | **0.429** | registry | ✅ |\n| death_rate_det (agg) | **0.163** | registry | ✅ |\n| label_dist | det=86, int=9, no_pref=150 | CSV det_pref/int_pref/no_pref 列 | ✅ |\n\n**来源文件**：`results/plan_012_decomposition`（CSV，与 `results/death_decomposition_preliminary.csv` 内容相同）\n\n#### Per-task decomposition（来源 A）\n\n| Task | n | Δ_full | Δ_nd | dr_int | dr_det | det_pref | int_pref | no_pref |\n|------|---|--------|------|--------|--------|----------|----------|---------|\n| chemistry-mix | 20 | 21.80 | 0.00 | 0.45 | 0.25 | 6 | 2 | 12 |\n| find-animal | 20 | 26.65 | 0.00 | 0.50 | 0.25 | 5 | 0 | 15 |\n| find-non-living-thing | 40 | 9.58 | 9.58 | 0.00 | 0.00 | 16 | 4 | 20 |\n| freeze | 20 | 30.50 | 0.00 | 0.55 | 0.25 | 6 | 0 | 14 |\n| grow-fruit | 20 | 25.10 | 0.00 | 0.45 | 0.20 | 6 | 1 | 13 |\n| identify-life-stages-1 | 20 | 47.50 | 0.00 | 0.55 | 0.10 | 9 | 0 | 11 |\n| identify-life-stages-2 | 20 | 30.00 | 0.00 | 0.50 | 0.20 | 6 | 0 | 14 |\n| inclined-plane-determine-angle | 20 | 36.00 | 0.00 | 0.55 | 0.20 | 7 | 0 | 13 |\n| lifespan-longest-lived | 25 | 44.00 | 0.00 | 0.56 | 0.16 | 11 | 1 | 13 |\n| lifespan-longest-lived-then-shortest-lived | 20 | 40.80 | 0.00 | 0.45 | 0.10 | 8 | 1 | 11 |\n| measure-melting-point-unknown-substance | 20 | 30.05 | 0.00 | 0.55 | 0.25 | 6 | 0 | 14 |\n\n### 2.2 Baseline 评估（plan-003-baseline，数据源 C）\n\n| 策略 | continuous_score | CI_90 | success_rate | death_rate | sim_ratio |\n|------|-----------------|-------|-------------|-----------|-----------|\n| always-internal | **-37.16** | [-43.39, -31.43] | 12.37% | 40.72% | 0.0 |\n| always-deterministic | **-11.64** | [-17.39, -6.55] | 23.71% | 18.56% | 1.0 |\n| oracle | **-9.03** | [-14.14, -4.15] | 24.23% | 16.49% | 0.962 |\n| random | **-23.75** | [-29.60, -18.11] | 16.49% | 28.35% | 0.503 |\n| trained-router (v6) | -11.64 | [-17.39, -6.55] | 23.71% | 18.56% | 1.0 |\n\n**n_episodes = 194, n_tasks = 11**\n**来源文件**：`results/plan_003_eval/overall_results.json`\n\n> ⚠️ **trained-router 完全退化**：与 always-deterministic 数字完全相同，sim_ratio=1.0 说明 router 100% 选择 deterministic。该行不可用于论文。\n\n### 2.3 Keyword Baseline（plan-011-rule-based）\n\n| 版本 | 关键词数 | Episodes | 匹配率 | Episode准确率 | 退化方向 | 来源文件 |\n|------|---------|----------|--------|-------------|---------|---------|\n| v1 | 20 | 204 | 85.8% | 97.65% | → always-det | `results/rule_based_accuracy_v1_rerun.json` |\n| v2 | 17 | 203 | 4.9% | 1.19% | → always-internal | `results/rule_based_accuracy_v2_test.json` |\n| v3 | 9 | 225 | 6.1% | 23.26% | → always-internal | `results/rule_based_accuracy_v3.json` |\n\n> 三版均结构性失效。v1 \"高准确率\" 是 \"connect\" 关键词假阳性（匹配 3963 次）。\n\n### 2.4 SFT 训练数据\n\n| 指标 | 值 | 来源文件 | 验证 |\n|------|---|---------|------|\n| 样本数 | **2040** | `data/plan-004-implicit/implicit_sft.jsonl` | ✅ wc -l = 2040 |\n| deterministic 标签 | **1830** (89.7%) | `data/plan-004-implicit/conversion_summary.json` | ✅ |\n| internal 标签 | **210** (10.3%) | 同上 | ✅ |\n| 来源 episodes | **68** (有 preference 的) | 从 194 eps 中提取 | ✅ 与 plan-005 routing_patterns 一致 |\n| 总 steps | 2040 | 来自 68 episodes 的 step-level 标签 | ✅ |\n\n> `data/plan-004-v3/implicit_sft.jsonl` 与上述文件完全相同（2040 行，同分布）。\n\n---\n\n## 三、不一致清单\n\n### INC-1：death_decomposition_report.json ≠ plan-012-full（⚠️ 严重）\n\n| | death_decomposition_report.json | plan-012-full (CSV) |\n|---|---|---|\n| Tasks | 30 | **11** ← 权威 |\n| Episodes | 249 | **245** ← 权威 |\n| Δ_full | 38.33 | **29.60** ← 权威 |\n| Δ_nd | 0.48 | **2.84** ← 权威 |\n| death_frac | 98.75% | **90.41%** ← 权威 |\n| r | 0.9864 | **0.9698** ← 权威 |\n\n**原因**：`death_decomposition_report.json` 使用 prescreening 30-task 数据（数据源 B），不是 plan-012-full。文件名极易混淆。\n\n### INC-2：Episode 数量差异 245 vs 194（已解释，非错误）\n\n| Task | plan-003 (C) | plan-012 (A) | 增量 |\n|------|-------------|-------------|------|\n| chemistry-mix | 20 | 20 | 0 |\n| find-animal | 15 | 20 | +5 |\n| find-non-living-thing | 35 | 40 | +5 |\n| freeze | 20 | 20 | 0 |\n| grow-fruit | 15 | 20 | +5 |\n| identify-life-stages-1 | 15 | 20 | +5 |\n| identify-life-stages-2 | 15 | 20 | +5 |\n| inclined-plane-determine-angle | 15 | 20 | +5 |\n| lifespan-longest-lived | 9 | 25 | +16 |\n| lifespan-longest-lived-then-shortest-lived | 15 | 20 | +5 |\n| measure-melting-point-unknown-substance | 20 | 20 | 0 |\n| **总计** | **194** | **245** | **+51** |\n\n**原因**：plan-001b 追加 rebalance 实验，将 8 个 task 扩展到 ≥20 eps。plan-003 baseline 在扩展前运行。\n\n**影响**：plan-003 baseline 与 plan-012 decomposition **不可直接对比**（不同 episode 集合）。SFT 数据（2040 samples）来自 194-episode 子集。\n\n### INC-3：plan005/routing_metrics.json 混合数据源\n\n30 tasks，episode 数量与 prescreening 和 plan-001b 都不完全匹配（如 find-animal=25, grow-fruit=18）。是混合数据源。**不应用于论文。**\n\n### INC-4：rule_based_accuracy 各版本 episode 数不一致\n\nv1=204, v2=203, v3=225。不同版本使用不同 task 子集。\n\n### INC-5：死亡率指标命名不统一\n\n- plan-003: `catastrophic_failure_rate`\n- plan-012 CSV: `death_rate_int` / `death_rate_det`\n- decomposition report: `int_death_rate` / `det_death_rate`\n\n含义相同，论文统一为 \"death rate\"。\n\n### INC-6：death_decomposition_preliminary_OLD.csv 过时\n\nOLD 版本 chemistry-mix=10 eps（总 235），当前版本=20 eps（总 245）。OLD 版本已弃用。\n\n---\n\n## 四、论文写作建议\n\n### Table 1: Baseline Comparison → 用 plan-003 (194 eps)\n\n| Strategy | Score |\n|----------|-------|\n| Always-Internal | -37.16 |\n| Always-Deterministic | -11.64 |\n| Oracle | -9.03 |\n| Random | -23.75 |\n\n> 删除 trained-router 行（退化）。\n\n### Death Decomposition → 用 plan-012-full (245 eps)\n\nΔ_full=+29.60, Δ_nd=+2.84, DAF=90.41%, r=0.9698 (p=8.12e-07)\n\n### Keyword Baseline → 用 plan-011 v3\n\nEpisode accuracy=23.26%，结构性失效。\n\n### SFT Data → 用 data/plan-004-implicit/implicit_sft.jsonl\n\n2040 samples, 89.7% det / 10.3% internal.\n\n### ⚠️ 绝对不引用\n\n1. `death_decomposition_report.json` 的 30-task 数字\n2. `plan005/routing_metrics.json`\n3. `results/plan_c_test_labels/` 下任何文件（标签损坏）\n4. `death_decomposition_preliminary_OLD.csv`\n5. trained-router 结果\n\n---\n\n## 五、数据谱系图\n\n```\nplan-001b 实验执行\n├── 初始跑 → 194 episodes (11 tasks)  [数据源 C]\n│   ├── plan-003: baseline eval (always-int/det/oracle/random)\n│   ├── plan-005: routing pattern analysis → 68 episodes with preference\n│   │   └── plan-004: implicit_sft.jsonl (2040 samples)\n│   └── plan-002: explicit router training (v1-v6, all degenerate except ablation-b)\n│\n├── rebalance 追加 → +51 episodes → 245 episodes (11 tasks)  [数据源 A]\n│   └── plan-012-full: death decomposition (Δ=29.60, daf=90.41%, r=0.9698)\n│\nprescreening 实验\n└── 30 tasks × 5-9 eps → 249 episodes  [数据源 B]\n    ├── death_decomposition_report.json (Δ=38.33, daf=98.75%, r=0.9864)\n    ├── plan005/routing_metrics.json (混合版)\n    └── rule_based_accuracy 各版本\n```\n\n---\n\n## 六、遗留问题\n\n1. **Baseline 与 decomposition 的 episode 集不匹配**：baselines (194 eps) 与 decomposition (245 eps) 不在同一 episode 集上。论文若在同一表中呈现，需声明或在 245 eps 上重跑 baselines。\n2. **SFT 数据不含追加 episodes**：2040 样本来自 194-episode 子集。扩展到 245 episodes 后训练数据未更新。\n3. **无有效 trained-router 结果**：plan-002-formal-v6 退化。plan-004-ablation-b 非退化（internal recall=51.5%）但未做 end-to-end eval。",
  "content_filename": "number_consistency_audit.md",
  "tags": [
    "D028",
    "audit",
    "consistency",
    "paper"
  ]
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26dbafca-c66a-47d0-8be2-b2daf3baf606",
  "isSidechain": false,
  "requestId": "req_011Cb27MvtyPDHRaddmw5Viw",
  "type": "assistant",
  "uuid": "7a432d0b-dd64-4eb2-8cbb-13fc6a71f1d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "64bf8e9c-9c87-47ba-adf7-bb88b4fb1455",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N2myayyLU3JETpbXSfPy9e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 795,
      "cache_read_input_tokens": 119150,
      "output_tokens": 4511,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 795,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4511,
          "cache_read_input_tokens": 119150,
          "cache_creation_input_tokens": 795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 795
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 136 · 2026-05-14T08:03:06.446Z_

<details><summary>↩ Tool result · `toolu_01R3tUcgafEU9EgPoQ7pooHY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_e311aa\", \"name\": \"D028 Number Consistency Audit\", \"type\": \"report\", \"description\": \"D028 核心数字一致性审计报告：审计所有实验数据源，识别三套数据宇宙（A=245eps, B=249eps, C=194eps），发现6项不一致，生成权威数字表和论文写作建议\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/report/number_consistency_audit.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T08:03:06.403256+00:00\", \"tags\": [\"D028\", \"audit\", \"consistency\", \"paper\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a432d0b-dd64-4eb2-8cbb-13fc6a71f1d3",
  "isSidechain": false,
  "promptId": "8f5e3863-8f23-4c69-a31a-63dbda3a511d",
  "type": "user",
  "uuid": "2f90285e-3a05-4a61-a03f-c9b5ec691fc9",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_e311aa\\\", \\\"name\\\": \\\"D028 Number Consistency Audit\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"D028 核心数字一致性审计报告：审计所有实验数据源，识别三套数据宇宙（A=245eps, B=249eps, C=194eps），发现6项不一致，生成权威数字表和论文写作建议\\\", \\\"path\\\": \\\"projects/simgate-modular-routing/artifacts/_project/report/number_consistency_audit.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"simgate-modular-routing\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T08:03:06.403256+00:00\\\", \\\"tags\\\": [\\\"D028\\\", \\\"audit\\\", \\\"consistency\\\", \\\"paper\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_e311aa\", \"name\": \"D028 Number Consistency Audit\", \"type\": \"report\", \"description\": \"D028 核心数字一致性审计报告：审计所有实验数据源，识别三套数据宇宙（A=245eps, B=249eps, C=194eps），发现6项不一致，生成权威数字表和论文写作建议\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/report/number_consistency_audit.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T08:03:06.403256+00:00\", \"tags\": [\"D028\", \"audit\", \"consistency\", \"paper\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "7a432d0b-dd64-4eb2-8cbb-13fc6a71f1d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "64bf8e9c-9c87-47ba-adf7-bb88b4fb1455",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 137_

```json
{
  "type": "last-prompt",
  "leafUuid": "2f90285e-3a05-4a61-a03f-c9b5ec691fc9",
  "sessionId": "64bf8e9c-9c87-47ba-adf7-bb88b4fb1455"
}
```

---


### Runtime record

_source line 138_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit data consistency across experiment results",
  "sessionId": "64bf8e9c-9c87-47ba-adf7-bb88b4fb1455"
}
```

---


### Assistant

_source line 139 · 2026-05-14T08:03:17.638Z_

审计完成。核心发现：

**根因**：项目存在 3 套数据源被混用——A (11 tasks/245 eps)、B (30 tasks/249 eps)、C (11 tasks/194 eps)。

**6 项不一致**：
1. **最严重**：`death_decomposition_report.json` 用的是 30-task prescreening 数据（Δ=38.33, r=0.9864），不是 plan-012-full 的 11-task 数据（Δ=29.60, r=0.9698）。文件名极易混淆。
2. 245 vs 194 episodes 差异：plan-001b 后续追加了 51 episodes（rebalance），plan-003 baseline 在追加前跑的。
3. `plan005/routing_metrics.json` 混合了 prescreening 和 plan-001b 数据。
4. rule_based_accuracy 三版本 episode 数各不相同（204/203/225）。
5. 死亡率指标命名不统一（catastrophic_failure_rate vs death_rate）。
6. trained-router 完全退化（与 always-det 完全相同）。

**论文写作建议**：decomposition 用 plan-012-full (245 eps) 数字，baselines 用 plan-003 (194 eps) 数字，但需注明两组数字基于不同 episode 集合。

报告已保存为 artifact `art_20260514_e311aa`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f90285e-3a05-4a61-a03f-c9b5ec691fc9",
  "isSidechain": false,
  "requestId": "req_011Cb27Uf7tb95kpaqA2DKEc",
  "type": "assistant",
  "uuid": "6afc2994-6aaa-422d-a3dd-7713f9da33d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "64bf8e9c-9c87-47ba-adf7-bb88b4fb1455",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSxsHrbix5qkE6S2m573N8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4834,
      "cache_read_input_tokens": 119945,
      "output_tokens": 415,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4834,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 415,
          "cache_read_input_tokens": 119945,
          "cache_creation_input_tokens": 4834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4834
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 140_

```json
{
  "type": "last-prompt",
  "leafUuid": "6afc2994-6aaa-422d-a3dd-7713f9da33d0",
  "sessionId": "64bf8e9c-9c87-47ba-adf7-bb88b4fb1455"
}
```

---


### Runtime record

_source line 141_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit data consistency across experiment results",
  "sessionId": "64bf8e9c-9c87-47ba-adf7-bb88b4fb1455"
}
```

---
