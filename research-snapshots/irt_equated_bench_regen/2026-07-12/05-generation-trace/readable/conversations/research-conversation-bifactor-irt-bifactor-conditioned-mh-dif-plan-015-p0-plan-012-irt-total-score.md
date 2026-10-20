# Research conversation: 任务：Bifactor IRT 拟合 + Bifactor-conditioned MH-DIF（plan_015，P0 最高优先） ### 背景 plan_012 证明单维 IRT θ 与 total score 相关性 0.9986，无

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/5fffb4b4-76a3-42fd-94be-f15a5a7c83d4.jsonl`
- **Structured JSON:** [`f1ad7fa44e77c3dd561d.json`](../../sessions/f1/f1ad7fa44e77c3dd561d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T22:25:16.981Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T22:25:16.981Z",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "content": "## 任务：Bifactor IRT 拟合 + Bifactor-conditioned MH-DIF（plan_015，P0 最高优先）\n\n### 背景\nplan_012 证明单维 IRT θ 与 total score 相关性 0.9986，无法降低 temporal cohort 31% baseline FPR。Director 指示尝试 bifactor IRT 作为最后的结构性方向：用 1 general + 57 subject-specific group factors 分离学科特异性能力，用 general θ 做 MH 分层。\n\n### 总体步骤\n\n#### Step 1: Bifactor IRT 拟合\n\n**首选方案：R `mirt::bfactor()`**\n\n先检查 R 和 mirt 包是否可用：\n```python\nimport subprocess\nresult = subprocess.run(['R', '-e', 'library(mirt); cat(packageVersion(\"mirt\"), \"\\n\")'], \n                       capture_output=True, text=True)\nprint(result.stdout, result.stderr)\n```\n\n如果 R + mirt 可用，写一个 R 脚本 `fit_bifactor.R`：\n```r\nlibrary(mirt)\n\n# 加载数据（从 Python 预处理好的 CSV）\nresp <- read.csv(\"response_matrix_dense.csv\", header=FALSE)\n\n# subject mapping: 长度 12508 的整数向量，标记每个 item 的 group factor (1-57)\nsubject_map <- read.csv(\"item_subject_map.csv\")$subject_id\n\n# 拟合 bifactor\n# bfactor 利用条件独立性，比全 MHRM 快很多\nmodel <- bfactor(resp, subject_map, \n                 itemtype='2PL',\n                 TOL=0.001,           # 收敛容忍度\n                 technical=list(NCYCLES=2000))  # 最大迭代\n\n# 提取 general θ（第一个因子）\ntheta <- fscores(model, method='EAP')\ngeneral_theta <- theta[, 1]  # 第一列是 general factor\n\n# 保存\nwrite.csv(data.frame(general_theta=general_theta), \"bifactor_general_theta.csv\", row.names=FALSE)\n\n# 模型拟合指标\nsummary(model)\n```\n\n**重要：数据准备**\n- Response matrix 是 5227×12508 CSR sparse。需要转成 dense CSV 给 R\n- 但 5227×12508 dense matrix 约 500MB CSV，可能太大\n- **优化**：用 `feather` 或 `RDS` 格式传输，或用 `reticulate` 直接在 R 中读 npz\n- 或者：用 `scipy.io.savemat()` 存为 .mat，R 用 `R.matlab::readMat()` 读\n\n**计算可行性预估**：\n- bfactor 利用 bifactor 的条件独立性结构（每个 item 只加载在 general + 1 个 group factor 上），复杂度远低于全 MIRT\n- 5227 models × 12508 items × 58 factors，预估 1-4 小时\n- 如果超过 4 小时未收敛或内存不够，用 **Fallback 方案**\n\n**Fallback 方案（如果 bfactor 失败）**：\n```\n对 57 个 subjects 分别拟合 unidimensional 2PL（每个 subject ~70-1300 items，秒级完成）\n对每个 model 和每个 subject，估计 θ_subject\nDIF 检测 subject X 的 item 时，用该 model 在其他 56 个 subjects 上的加权平均 θ 作为 matching variable\n这是 leave-one-out θ 策略，避免 matching variable 包含目标 subject 的信息\n```\n\n用 Python 实现 fallback：\n```python\n# 对每个 subject 独立估计 θ\n# 简化版：logit of subject-specific proportion correct\nfor subject in subjects:\n    items_in_subject = item_metadata[item_metadata.subject == subject].index\n    subject_scores = response_matrix[:, items_in_subject].sum(axis=1)\n    subject_n = response_matrix[:, items_in_subject].getnnz(axis=1)\n    subject_p = subject_scores / subject_n\n    theta_subject[subject] = np.log((subject_p + 0.001) / (1 - subject_p + 0.001))\n\n# Leave-one-out matching: DIF 检测 subject X 时\n# matching_theta = mean(theta_subject[s] for s != X)\n```\n\n**决策逻辑**：\n1. 先尝试 R bfactor（最优）\n2. 如果 R 不可用或 bfactor 不收敛 → 用 Python fallback\n3. 无论哪种方案，产出都是：每个 model 的 general θ（或 leave-one-out θ per subject）\n\n#### Step 2: Bifactor-conditioned MH-DIF\n\n用 general θ（或 leave-one-out θ）做 MH 分层：\n- temporal cohort: ref=2023, foc=2024（model_metadata.csv 的 cohort_temporal 列）\n- 10 个 decile bins on general θ\n- 计算所有 12508 items 的 MH-DIF + ETS 分类\n- 报告: overall C%, FPR on Li-clean items, enrichment\n\n**参考代码**：`artifacts/plan_011/plan_011_analysis.py` 和 `artifacts/plan_012/plan_012_irt_theta_analysis.py` 有完整的 MH-DIF 实现。\n\n#### Step 3: Semi-synthetic 重跑\n\n在 plan_011 的 semi-synthetic 框架下用 bifactor general θ 分层：\n- 500 baseline items, 100 contaminated\n- p = [0.0, 0.5, 1.0]（只跑 3 个关键 p 值节省时间）\n- 5 seeds\n- temporal cohort only（ability cohort 在 plan_012 已证明 confounded）\n- 同时保留 external_5（plan_011 baseline）作对比\n\n报告 TPR, FPR, ΔTPR。\n\n#### Step 4: 模型拟合诊断\n\n如果用了 R bfactor：\n- 报告 RMSEA, CFI（如果 mirt 提供）\n- General factor explained variance ratio\n- 前 5 个 group factors 的 explained variance\n\n如果用了 Python fallback：\n- 报告 leave-one-out θ 与 total score 的相关性（预期应 < 0.9986）\n- 各 subject θ 之间的相关矩阵摘要\n\n### 数据文件\n所有在 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/`：\n\n1. **Response matrix**: `response_matrix.npz` — 5227×12508 CSR sparse (int8)\n   - `response_matrix_index.npz` — model_names, item_ids\n2. **Model metadata**: `model_metadata.csv` — cohort_temporal: \"2023\"/\"2024\"/\"other\"\n3. **Item metadata**: `item_metadata.csv` — subject 列标记 57 个 MMLU subjects\n4. **Li et al. labels**: `mmlu_li2024_proxy_labels.csv` — is_contaminated 列\n5. **参考代码**:\n   - `plan_011/plan_011_analysis.py` — MH-DIF + semi-synthetic injection\n   - `plan_012/plan_012_irt_theta_analysis.py` — θ-conditioned MH-DIF\n\n### 产出\n写到 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_015/`：\n\n1. `plan_015_bifactor_analysis.py` — 主 Python 脚本\n2. `fit_bifactor.R` — R 拟合脚本（如果用了 R）\n3. `bifactor_general_theta.csv` — model_name, general_theta, total_score, method (bifactor/leave-one-out)\n4. `bifactor_dif_results.csv` — temporal cohort DIF 结果（所有 items）\n5. `bifactor_dose_response.csv` — semi-synthetic dose-response\n6. `bifactor_fit_diagnostics.csv` — 模型拟合指标\n7. `plan_015_report.md` — 完整报告\n\n### 成功标准\n- temporal FPR < 0.15（从 31% 降到 15% 以下）\n- semi-synthetic TPR > 0.60 at p=0.5\n- bifactor θ 与 total score 相关性显著低于 0.9986\n\n### 执行注意\n- 这是 CPU-only 任务，可能需要 1-4 小时（bifactor 拟合）\n- 如果 R bfactor 超过 2 小时未收敛，立即切 Python fallback 并行跑\n- 优先保证有结果产出，不要卡在 bfactor 收敛上\n- 用 register_artifact 注册所有产出文件\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T22:25:16.987Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T22:25:16.987Z",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4"
}
```

---

## Round 1

47 recorded events

### User

_source line 3 · 2026-05-20T22:25:17.045Z_

## 任务：Bifactor IRT 拟合 + Bifactor-conditioned MH-DIF（plan_015，P0 最高优先）

### 背景
plan_012 证明单维 IRT θ 与 total score 相关性 0.9986，无法降低 temporal cohort 31% baseline FPR。Director 指示尝试 bifactor IRT 作为最后的结构性方向：用 1 general + 57 subject-specific group factors 分离学科特异性能力，用 general θ 做 MH 分层。

### 总体步骤

#### Step 1: Bifactor IRT 拟合

**首选方案：R `mirt::bfactor()`**

先检查 R 和 mirt 包是否可用：
```python
import subprocess
result = subprocess.run(['R', '-e', 'library(mirt); cat(packageVersion("mirt"), "\n")'], 
                       capture_output=True, text=True)
print(result.stdout, result.stderr)
```

如果 R + mirt 可用，写一个 R 脚本 `fit_bifactor.R`：
```r
library(mirt)

# 加载数据（从 Python 预处理好的 CSV）
resp <- read.csv("response_matrix_dense.csv", header=FALSE)

# subject mapping: 长度 12508 的整数向量，标记每个 item 的 group factor (1-57)
subject_map <- read.csv("item_subject_map.csv")$subject_id

# 拟合 bifactor
# bfactor 利用条件独立性，比全 MHRM 快很多
model <- bfactor(resp, subject_map, 
                 itemtype='2PL',
                 TOL=0.001,           # 收敛容忍度
                 technical=list(NCYCLES=2000))  # 最大迭代

# 提取 general θ（第一个因子）
theta <- fscores(model, method='EAP')
general_theta <- theta[, 1]  # 第一列是 general factor

# 保存
write.csv(data.frame(general_theta=general_theta), "bifactor_general_theta.csv", row.names=FALSE)

# 模型拟合指标
summary(model)
```

**重要：数据准备**
- Response matrix 是 5227×12508 CSR sparse。需要转成 dense CSV 给 R
- 但 5227×12508 dense matrix 约 500MB CSV，可能太大
- **优化**：用 `feather` 或 `RDS` 格式传输，或用 `reticulate` 直接在 R 中读 npz
- 或者：用 `scipy.io.savemat()` 存为 .mat，R 用 `R.matlab::readMat()` 读

**计算可行性预估**：
- bfactor 利用 bifactor 的条件独立性结构（每个 item 只加载在 general + 1 个 group factor 上），复杂度远低于全 MIRT
- 5227 models × 12508 items × 58 factors，预估 1-4 小时
- 如果超过 4 小时未收敛或内存不够，用 **Fallback 方案**

**Fallback 方案（如果 bfactor 失败）**：
```
对 57 个 subjects 分别拟合 unidimensional 2PL（每个 subject ~70-1300 items，秒级完成）
对每个 model 和每个 subject，估计 θ_subject
DIF 检测 subject X 的 item 时，用该 model 在其他 56 个 subjects 上的加权平均 θ 作为 matching variable
这是 leave-one-out θ 策略，避免 matching variable 包含目标 subject 的信息
```

用 Python 实现 fallback：
```python
# 对每个 subject 独立估计 θ
# 简化版：logit of subject-specific proportion correct
for subject in subjects:
    items_in_subject = item_metadata[item_metadata.subject == subject].index
    subject_scores = response_matrix[:, items_in_subject].sum(axis=1)
    subject_n = response_matrix[:, items_in_subject].getnnz(axis=1)
    subject_p = subject_scores / subject_n
    theta_subject[subject] = np.log((subject_p + 0.001) / (1 - subject_p + 0.001))

# Leave-one-out matching: DIF 检测 subject X 时
# matching_theta = mean(theta_subject[s] for s != X)
```

**决策逻辑**：
1. 先尝试 R bfactor（最优）
2. 如果 R 不可用或 bfactor 不收敛 → 用 Python fallback
3. 无论哪种方案，产出都是：每个 model 的 general θ（或 leave-one-out θ per subject）

#### Step 2: Bifactor-conditioned MH-DIF

用 general θ（或 leave-one-out θ）做 MH 分层：
- temporal cohort: ref=2023, foc=2024（model_metadata.csv 的 cohort_temporal 列）
- 10 个 decile bins on general θ
- 计算所有 12508 items 的 MH-DIF + ETS 分类
- 报告: overall C%, FPR on Li-clean items, enrichment

**参考代码**：`artifacts/plan_011/plan_011_analysis.py` 和 `artifacts/plan_012/plan_012_irt_theta_analysis.py` 有完整的 MH-DIF 实现。

#### Step 3: Semi-synthetic 重跑

在 plan_011 的 semi-synthetic 框架下用 bifactor general θ 分层：
- 500 baseline items, 100 contaminated
- p = [0.0, 0.5, 1.0]（只跑 3 个关键 p 值节省时间）
- 5 seeds
- temporal cohort only（ability cohort 在 plan_012 已证明 confounded）
- 同时保留 external_5（plan_011 baseline）作对比

报告 TPR, FPR, ΔTPR。

#### Step 4: 模型拟合诊断

如果用了 R bfactor：
- 报告 RMSEA, CFI（如果 mirt 提供）
- General factor explained variance ratio
- 前 5 个 group factors 的 explained variance

如果用了 Python fallback：
- 报告 leave-one-out θ 与 total score 的相关性（预期应 < 0.9986）
- 各 subject θ 之间的相关矩阵摘要

### 数据文件
所有在 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/`：

1. **Response matrix**: `response_matrix.npz` — 5227×12508 CSR sparse (int8)
   - `response_matrix_index.npz` — model_names, item_ids
2. **Model metadata**: `model_metadata.csv` — cohort_temporal: "2023"/"2024"/"other"
3. **Item metadata**: `item_metadata.csv` — subject 列标记 57 个 MMLU subjects
4. **Li et al. labels**: `mmlu_li2024_proxy_labels.csv` — is_contaminated 列
5. **参考代码**:
   - `plan_011/plan_011_analysis.py` — MH-DIF + semi-synthetic injection
   - `plan_012/plan_012_irt_theta_analysis.py` — θ-conditioned MH-DIF

### 产出
写到 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_015/`：

1. `plan_015_bifactor_analysis.py` — 主 Python 脚本
2. `fit_bifactor.R` — R 拟合脚本（如果用了 R）
3. `bifactor_general_theta.csv` — model_name, general_theta, total_score, method (bifactor/leave-one-out)
4. `bifactor_dif_results.csv` — temporal cohort DIF 结果（所有 items）
5. `bifactor_dose_response.csv` — semi-synthetic dose-response
6. `bifactor_fit_diagnostics.csv` — 模型拟合指标
7. `plan_015_report.md` — 完整报告

### 成功标准
- temporal FPR < 0.15（从 31% 降到 15% 以下）
- semi-synthetic TPR > 0.60 at p=0.5
- bifactor θ 与 total score 相关性显著低于 0.9986

### 执行注意
- 这是 CPU-only 任务，可能需要 1-4 小时（bifactor 拟合）
- 如果 R bfactor 超过 2 小时未收敛，立即切 Python fallback 并行跑
- 优先保证有结果产出，不要卡在 bfactor 收敛上
- 用 register_artifact 注册所有产出文件


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "type": "user",
  "uuid": "967c3b5c-fa97-4ebe-bcca-15b93da18161",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T22:25:17.044Z_

```json
{
  "parentUuid": "967c3b5c-fa97-4ebe-bcca-15b93da18161",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "cd41d598-9c32-4a36-b292-549b46edf5df",
  "timestamp": "2026-05-20T22:25:17.044Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T22:25:17.044Z_

```json
{
  "parentUuid": "cd41d598-9c32-4a36-b292-549b46edf5df",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "6e4dd00f-2429-4449-89ad-789615cab8ad",
  "timestamp": "2026-05-20T22:25:17.044Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T22:25:17.044Z_

```json
{
  "parentUuid": "6e4dd00f-2429-4449-89ad-789615cab8ad",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f8f4b659-d84b-4d92-9694-5fc016805ef9",
  "timestamp": "2026-05-20T22:25:17.044Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Bifactor IRT fitting with MH-DIF analysis",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4"
}
```

---

### Assistant

_source line 8 · 2026-05-20T22:25:21.218Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this task. It's a complex ML research task involving:

1. Bifactor IRT fitting (using R's mirt::bfactor() or Python fallback)
2. Bifactor-conditioned MH-DIF analysis
3. Semi-synthetic re-run
4. Model fit diagnostics

Let me start by understanding the current state of the project - checking what files exist, whether R is available, and understanding the existing code.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8f4b659-d84b-4d92-9694-5fc016805ef9",
  "isSidechain": false,
  "requestId": "req_011CbEc5S9p9zqZkESh5tRci",
  "type": "assistant",
  "uuid": "53ad3ce3-f6ed-4018-98f4-2407d2899cdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFLGkfhBgczSCMLpZ2Lqpr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 11841,
      "output_tokens": 852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 852,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
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

_source line 9 · 2026-05-20T22:25:22.274Z_

开始执行 plan_015。先探测环境和数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53ad3ce3-f6ed-4018-98f4-2407d2899cdc",
  "isSidechain": false,
  "requestId": "req_011CbEc5S9p9zqZkESh5tRci",
  "type": "assistant",
  "uuid": "f336c66d-17b1-4af6-bfe8-381bd3070e72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFLGkfhBgczSCMLpZ2Lqpr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 11841,
      "output_tokens": 852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 852,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
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

_source line 10 · 2026-05-20T22:25:23.303Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UntUtZu9bfkHYRWNrwJRT2`</summary>

```json
{
  "command": "R -e 'library(mirt); cat(packageVersion(\"mirt\"), \"\\n\")' 2>&1 | tail -5",
  "description": "Check R and mirt package availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f336c66d-17b1-4af6-bfe8-381bd3070e72",
  "isSidechain": false,
  "requestId": "req_011CbEc5S9p9zqZkESh5tRci",
  "type": "assistant",
  "uuid": "e669e138-79fb-4042-831e-6155ca37843f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFLGkfhBgczSCMLpZ2Lqpr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 11841,
      "output_tokens": 852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 852,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
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

_source line 11 · 2026-05-20T22:25:23.613Z_

<details><summary>↩ Tool result · `toolu_01UntUtZu9bfkHYRWNrwJRT2`</summary>

```text
/bin/bash: line 1: R: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e669e138-79fb-4042-831e-6155ca37843f",
  "isSidechain": false,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "type": "user",
  "uuid": "a6a7c5cd-d3b2-455d-ad72-61cce195723c",
  "toolUseResult": {
    "stdout": "/bin/bash: line 1: R: command not found",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e669e138-79fb-4042-831e-6155ca37843f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T22:25:24.788Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0135R7cj7rphFckjSerBXskc`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | head -30",
  "description": "List artifact directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6a7c5cd-d3b2-455d-ad72-61cce195723c",
  "isSidechain": false,
  "requestId": "req_011CbEc5S9p9zqZkESh5tRci",
  "type": "assistant",
  "uuid": "2f4dad2f-e7e2-48d7-894c-d0a65be8e911",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFLGkfhBgczSCMLpZ2Lqpr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 11841,
      "output_tokens": 852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 852,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
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

_source line 13 · 2026-05-20T22:25:24.920Z_

<details><summary>↩ Tool result · `toolu_0135R7cj7rphFckjSerBXskc`</summary>

```text
__pycache__
_project
build_response_matrix.py
dif_diagnostic.py
dif_diagnostic_output.log
dif_diagnostic_pvalue_dist.pdf
dif_diagnostic_tpr_comparison.csv
dif_phase2_param_distribution.pdf
dif_phase2_power_curves.pdf
dif_phase2_results.csv
dif_phase2_simulation.py
dif_power_curves.pdf
dif_power_results.csv
dif_power_simulation.py
dream_reports
irt_scale_analysis.json
irt_scale_analysis.md
item_metadata.csv
manifest.yaml
metabench_cohort_analysis.csv
metabench_ctt_stats.csv
metabench_data
metabench_data_summary.md
metabench_explore.py
metabench_model_accuracy.csv
metabench_model_list.txt
metabench_rl_models.csv
metabench_subject_stats.csv
metabench_summary.json
mmlu_cf_analysis.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f4dad2f-e7e2-48d7-894c-d0a65be8e911",
  "isSidechain": false,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "type": "user",
  "uuid": "2e25db99-8aab-4aca-aae7-b129d055b197",
  "toolUseResult": {
    "stdout": "__pycache__\n_project\nbuild_response_matrix.py\ndif_diagnostic.py\ndif_diagnostic_output.log\ndif_diagnostic_pvalue_dist.pdf\ndif_diagnostic_tpr_comparison.csv\ndif_phase2_param_distribution.pdf\ndif_phase2_power_curves.pdf\ndif_phase2_results.csv\ndif_phase2_simulation.py\ndif_power_curves.pdf\ndif_power_results.csv\ndif_power_simulation.py\ndream_reports\nirt_scale_analysis.json\nirt_scale_analysis.md\nitem_metadata.csv\nmanifest.yaml\nmetabench_cohort_analysis.csv\nmetabench_ctt_stats.csv\nmetabench_data\nmetabench_data_summary.md\nmetabench_explore.py\nmetabench_model_accuracy.csv\nmetabench_model_list.txt\nmetabench_rl_models.csv\nmetabench_subject_stats.csv\nmetabench_summary.json\nmmlu_cf_analysis.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2f4dad2f-e7e2-48d7-894c-d0a65be8e911",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T22:25:30.274Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01T22c4ygSYChc7rsTGyB8sT`</summary>

```json
{
  "command": "python3 -c \"\nimport scipy.sparse, numpy as np, pandas as pd\nrm = scipy.sparse.load_npz('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix.npz')\nidx = np.load('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix_index.npz', allow_pickle=True)\nprint('Response matrix:', rm.shape, rm.dtype, rm.nnz)\nprint('Model names:', len(idx['model_names']), idx['model_names'][:3])\nprint('Item IDs:', len(idx['item_ids']), idx['item_ids'][:3])\nmeta = pd.read_csv('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv')\nprint('Model metadata:', meta.shape)\nprint('Cohort temporal:', meta['cohort_temporal'].value_counts().to_dict())\nitems = pd.read_csv('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/item_metadata.csv')\nprint('Item metadata:', items.shape)\nprint('Subjects:', items['subject'].nunique(), 'items per subject range:', items.groupby('subject').size().min(), '-', items.groupby('subject').size().max())\nli = pd.read_csv('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mmlu_li2024_proxy_labels.csv')\nprint('Li labels:', li.shape, 'contaminated:', li['is_contaminated'].sum())\n\"",
  "description": "Inspect data files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e25db99-8aab-4aca-aae7-b129d055b197",
  "isSidechain": false,
  "requestId": "req_011CbEc5S9p9zqZkESh5tRci",
  "type": "assistant",
  "uuid": "43e4d37c-bee0-4b35-8de7-d16b2ffaf1eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFLGkfhBgczSCMLpZ2Lqpr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13143,
      "cache_read_input_tokens": 11841,
      "output_tokens": 852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 852,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13143
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

_source line 15 · 2026-05-20T22:25:32.809Z_

<details><summary>↩ Tool result · `toolu_01T22c4ygSYChc7rsTGyB8sT`</summary>

```text
Response matrix: (5227, 12508) int8 38654082
Model names: 5227 ['0-hero/Matter-0.1-7B' '0-hero/Matter-0.1-7B-DPO-preview'
 '0-hero/Matter-0.1-7B-boost']
Item IDs: 12508 ['abstract_algebra.1' 'abstract_algebra.10' 'abstract_algebra.100']
Model metadata: (5227, 8)
Cohort temporal: {'other': 3340, '2023': 1080, '2024': 807}
Item metadata: (12508, 7)
Subjects: 57 items per subject range: 72 - 1331
Li labels: (12508, 6) contaminated: 3645
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43e4d37c-bee0-4b35-8de7-d16b2ffaf1eb",
  "isSidechain": false,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "type": "user",
  "uuid": "97028c20-c035-4d0b-96f4-e131f11c2a17",
  "toolUseResult": {
    "stdout": "Response matrix: (5227, 12508) int8 38654082\nModel names: 5227 ['0-hero/Matter-0.1-7B' '0-hero/Matter-0.1-7B-DPO-preview'\n '0-hero/Matter-0.1-7B-boost']\nItem IDs: 12508 ['abstract_algebra.1' 'abstract_algebra.10' 'abstract_algebra.100']\nModel metadata: (5227, 8)\nCohort temporal: {'other': 3340, '2023': 1080, '2024': 807}\nItem metadata: (12508, 7)\nSubjects: 57 items per subject range: 72 - 1331\nLi labels: (12508, 6) contaminated: 3645",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "43e4d37c-bee0-4b35-8de7-d16b2ffaf1eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## 任务：Bifactor IRT 拟合 + Bifactor-conditioned MH-DIF（plan_015，P0 最高优先）  ### 背景 plan_012 证明单维 IRT θ 与 total score 相关性 0.9986，无法降低 temporal cohort 31% baseline FPR。Director 指示尝试 bifactor IRT 作为最后的结构性方向：用…",
  "leafUuid": "97028c20-c035-4d0b-96f4-e131f11c2a17",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Bifactor IRT fitting with MH-DIF analysis",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4"
}
```

---

### Assistant

_source line 18 · 2026-05-20T22:25:35.804Z_

R 不可用，直接走 Python fallback 方案（leave-one-out θ）。先看参考代码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97028c20-c035-4d0b-96f4-e131f11c2a17",
  "isSidechain": false,
  "requestId": "req_011CbEc6bYtg8HDrtjd6iK3y",
  "type": "assistant",
  "uuid": "3b39e6d0-82b9-46c8-902e-69783e20f485",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sjb2NGsWwTRN8yza2nJZ4m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 24984,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 275,
          "cache_read_input_tokens": 24984,
          "cache_creation_input_tokens": 1408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1408
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

_source line 19 · 2026-05-20T22:25:39.720Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01YTqBcbHiyhpgdmyLT5wgSG`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Read reference analysis scripts",
  "prompt": "Read the following files in full and report their complete contents:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py\n2. /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012/plan_012_irt_theta_analysis.py\n\nI need to understand the MH-DIF implementation, semi-synthetic injection framework, and IRT theta estimation code. Report back the full code of both files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b39e6d0-82b9-46c8-902e-69783e20f485",
  "isSidechain": false,
  "requestId": "req_011CbEc6bYtg8HDrtjd6iK3y",
  "type": "assistant",
  "uuid": "de0701fb-50ec-4873-985d-37b2cfbae375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sjb2NGsWwTRN8yza2nJZ4m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 24984,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 275,
          "cache_read_input_tokens": 24984,
          "cache_creation_input_tokens": 1408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1408
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

_source line 20 · 2026-05-20T22:25:58.120Z_

<details><summary>↩ Tool result · `toolu_01YTqBcbHiyhpgdmyLT5wgSG`</summary>

````text
Perfect! I've successfully read both files. Here's a complete summary of what these scripts implement:

## File 1: plan_011_analysis.py — Semi-Synthetic DIF Validation

**Purpose**: Validates the MH-DIF methodology by injecting known differential contamination into real MMLU response data and testing detection capability.

**Key Components**:

1. **MH-DIF Core Function** (`mh_dif_subset`):
   - Implements purified Mantel-Haenszel DIF detection for all items
   - Supports 3 stratification strategies:
     - Standard: total score on all items minus current item
     - Anchor: total score on known-clean items only (oracle knowledge)
     - External: total score on full 12,508-item original matrix (best matching precision)
   - Computes alpha (log-odds ratio), delta (ETS DIF parameter), chi-square tests, p-values
   - Classifies items as ETS A, B, or C based on |delta| threshold (1.0) and p < 0.05

2. **Semi-Synthetic Injection Framework**:
   - Selects 500 baseline items (clean + ETS A classification)
   - Creates two cohorts: ability (Q1-2 vs Q4-5) and temporal (2023 vs 2024)
   - Injects differential contamination into N_CONTAMINATED=100 items per run
   - Injection probability varies: p ∈ [0.0, 0.3, 0.5, 0.7, 1.0]
   - Uses 5 random seeds per configuration
   - Flips 0→1 responses probabilistically in focal group

3. **Performance Metrics**:
   - TPR (True Positive Rate): proportion of contaminated items detected as ETS C
   - FPR (False Positive Rate): proportion of clean items falsely marked as ETS C
   - Fisher's exact test OR and p-values for statistical significance
   - Dose-response curves across injection probabilities

4. **Output**:
   - injection_results.csv: All runs (250 rows: 5 p × 5 seeds × 2 cohorts × 5 variants)
   - dose_response_summary.csv: Aggregated statistics
   - per_item_results.csv: Per-item delta/p-value for anchor variant
   - plan_011_report.md: Full analysis report

**Key Findings Structure**:
- Compares 3 MH variants to identify matching variable contamination (when standard FPR is high but external FPR is low)
- Distinguishes differential vs non-differential contamination detection capability

---

## File 2: plan_012_irt_theta_analysis.py — IRT θ-Conditioning MH-DIF

**Purpose**: Tests whether IRT-based ability estimates reduce the high baseline FPR from plan_011 while maintaining detection power.

**Key Components**:

1. **IRT θ Estimation** (Lines 179-199):
   - Method: Logit of proportion correct with Laplace smoothing
   ```python
   θ = log((total + 0.5) / (J_full + 1 - total - 0.5))
   ```
   - Applied to full 12,508-item matrix for all 5,227 models
   - Produces θ range and correlation with raw total scores (~0.999+)

2. **MH-DIF with Stratification Variants**:
   - `theta_eq_K`: Equal-width bins on θ scale (respects IRT metric)
   - `theta_qt_K`: Quantile bins on θ (equal-count strata)
   - K ∈ [10, 15, 20] to test strata count effects
   - `external_5`: 5-quantile bins on full-matrix total score (plan_011 baseline)

3. **Core MH Computation** (`_compute_mh_item` and `mh_dif_with_bins`):
   - Separates stratification from per-item calculation
   - Pre-computes bin assignments once, applies to all items
   - Same MH statistics (alpha, delta, chi2, p-value, ETS class) as plan_011

4. **Semi-Synthetic Injection**:
   - Identical setup to plan_011 (same 500 baseline items, cohorts, injection scheme)
   - Tests all MH variants against same contamination patterns
   - Measures baseline FPR and dose-response curves

5. **Real Data Enrichment Analysis** (Lines 410-485):
   - Applies all MH variants to Li et al. contamination labels (no injection)
   - Computes enrichment: rate(contaminated flagged) / rate(clean flagged)
   - Tests whether θ-conditioning improves detection against real contamination

6. **Output**:
   - theta_estimates.csv: All models' θ and total score
   - injection_results.csv: All semi-synthetic runs
   - dose_response_theta.csv: Aggregated semi-synthetic results
   - enrichment_theta.csv: Real-data enrichment rates by variant
   - plan_012_report.md: Full analysis with success criteria evaluation

**Key Distinctions from plan_011**:
- Replaces total-score stratification with IRT θ
- Tests multiple strata counts (10, 15, 20) vs fixed 5
- Evaluates whether finer ability matching reduces FPR while preserving TPR
- Includes enrichment analysis on real contamination labels for practical validation

Both scripts follow the same semi-synthetic injection methodology but test different MH-DIF conditioning strategies to identify the optimal approach for contamination detection in LLM evaluation benchmarks.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "de0701fb-50ec-4873-985d-37b2cfbae375",
  "isSidechain": false,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "type": "user",
  "uuid": "2c53c60a-dad3-4ccc-877f-2df9e7a5c017",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Read the following files in full and report their complete contents:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py\n2. /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012/plan_012_irt_theta_analysis.py\n\nI need to understand the MH-DIF implementation, semi-synthetic injection framework, and IRT theta estimation code. Report back the full code of both files.",
    "agentId": "afcf9a07bab716d8b",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I've successfully read both files. Here's a complete summary of what these scripts implement:\n\n## File 1: plan_011_analysis.py — Semi-Synthetic DIF Validation\n\n**Purpose**: Validates the MH-DIF methodology by injecting known differential contamination into real MMLU response data and testing detection capability.\n\n**Key Components**:\n\n1. **MH-DIF Core Function** (`mh_dif_subset`):\n   - Implements purified Mantel-Haenszel DIF detection for all items\n   - Supports 3 stratification strategies:\n     - Standard: total score on all items minus current item\n     - Anchor: total score on known-clean items only (oracle knowledge)\n     - External: total score on full 12,508-item original matrix (best matching precision)\n   - Computes alpha (log-odds ratio), delta (ETS DIF parameter), chi-square tests, p-values\n   - Classifies items as ETS A, B, or C based on |delta| threshold (1.0) and p < 0.05\n\n2. **Semi-Synthetic Injection Framework**:\n   - Selects 500 baseline items (clean + ETS A classification)\n   - Creates two cohorts: ability (Q1-2 vs Q4-5) and temporal (2023 vs 2024)\n   - Injects differential contamination into N_CONTAMINATED=100 items per run\n   - Injection probability varies: p ∈ [0.0, 0.3, 0.5, 0.7, 1.0]\n   - Uses 5 random seeds per configuration\n   - Flips 0→1 responses probabilistically in focal group\n\n3. **Performance Metrics**:\n   - TPR (True Positive Rate): proportion of contaminated items detected as ETS C\n   - FPR (False Positive Rate): proportion of clean items falsely marked as ETS C\n   - Fisher's exact test OR and p-values for statistical significance\n   - Dose-response curves across injection probabilities\n\n4. **Output**:\n   - injection_results.csv: All runs (250 rows: 5 p × 5 seeds × 2 cohorts × 5 variants)\n   - dose_response_summary.csv: Aggregated statistics\n   - per_item_results.csv: Per-item delta/p-value for anchor variant\n   - plan_011_report.md: Full analysis report\n\n**Key Findings Structure**:\n- Compares 3 MH variants to identify matching variable contamination (when standard FPR is high but external FPR is low)\n- Distinguishes differential vs non-differential contamination detection capability\n\n---\n\n## File 2: plan_012_irt_theta_analysis.py — IRT θ-Conditioning MH-DIF\n\n**Purpose**: Tests whether IRT-based ability estimates reduce the high baseline FPR from plan_011 while maintaining detection power.\n\n**Key Components**:\n\n1. **IRT θ Estimation** (Lines 179-199):\n   - Method: Logit of proportion correct with Laplace smoothing\n   ```python\n   θ = log((total + 0.5) / (J_full + 1 - total - 0.5))\n   ```\n   - Applied to full 12,508-item matrix for all 5,227 models\n   - Produces θ range and correlation with raw total scores (~0.999+)\n\n2. **MH-DIF with Stratification Variants**:\n   - `theta_eq_K`: Equal-width bins on θ scale (respects IRT metric)\n   - `theta_qt_K`: Quantile bins on θ (equal-count strata)\n   - K ∈ [10, 15, 20] to test strata count effects\n   - `external_5`: 5-quantile bins on full-matrix total score (plan_011 baseline)\n\n3. **Core MH Computation** (`_compute_mh_item` and `mh_dif_with_bins`):\n   - Separates stratification from per-item calculation\n   - Pre-computes bin assignments once, applies to all items\n   - Same MH statistics (alpha, delta, chi2, p-value, ETS class) as plan_011\n\n4. **Semi-Synthetic Injection**:\n   - Identical setup to plan_011 (same 500 baseline items, cohorts, injection scheme)\n   - Tests all MH variants against same contamination patterns\n   - Measures baseline FPR and dose-response curves\n\n5. **Real Data Enrichment Analysis** (Lines 410-485):\n   - Applies all MH variants to Li et al. contamination labels (no injection)\n   - Computes enrichment: rate(contaminated flagged) / rate(clean flagged)\n   - Tests whether θ-conditioning improves detection against real contamination\n\n6. **Output**:\n   - theta_estimates.csv: All models' θ and total score\n   - injection_results.csv: All semi-synthetic runs\n   - dose_response_theta.csv: Aggregated semi-synthetic results\n   - enrichment_theta.csv: Real-data enrichment rates by variant\n   - plan_012_report.md: Full analysis with success criteria evaluation\n\n**Key Distinctions from plan_011**:\n- Replaces total-score stratification with IRT θ\n- Tests multiple strata counts (10, 15, 20) vs fixed 5\n- Evaluates whether finer ability matching reduces FPR while preserving TPR\n- Includes enrichment analysis on real contamination labels for practical validation\n\nBoth scripts follow the same semi-synthetic injection methodology but test different MH-DIF conditioning strategies to identify the optimal approach for contamination detection in LLM evaluation benchmarks."
      }
    ],
    "totalDurationMs": 18385,
    "totalTokens": 43000,
    "totalToolUseCount": 2,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 23119,
      "cache_read_input_tokens": 18502,
      "output_tokens": 1372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23119
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1372,
          "cache_read_input_tokens": 18502,
          "cache_creation_input_tokens": 23119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23119,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "de0701fb-50ec-4873-985d-37b2cfbae375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 21 · 2026-05-20T22:26:01.799Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Gd3WfoycgkE72SHekyrwFS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012/plan_012_irt_theta_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c53c60a-dad3-4ccc-877f-2df9e7a5c017",
  "isSidechain": false,
  "requestId": "req_011CbEc8TtKsHxyfm23i7SSD",
  "type": "assistant",
  "uuid": "30ffd594-8221-46f6-b126-2ea67216ad1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tq5P2bgMfqE2fQvzqjkBJ1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1655,
      "cache_read_input_tokens": 26392,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1655,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 26392,
          "cache_creation_input_tokens": 1655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1655
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

_source line 22 · 2026-05-20T22:26:02.102Z_

<details><summary>↩ Tool result · `toolu_01Gd3WfoycgkE72SHekyrwFS`</summary>

````text
1	#!/usr/bin/env python3
2	"""
3	plan_012_irt_theta_analysis.py — IRT θ-Conditioning MH-DIF Analysis
4	
5	Uses IRT-based θ estimates (logit of proportion correct) instead of raw total
6	scores for MH-DIF stratification. Tests whether finer ability matching reduces
7	the high baseline FPR from plan_011 (temporal ~31%, ability ~49%) while
8	preserving detection power for differential contamination.
9	
10	Variants tested:
11	  - theta_eq_K   : equal-width bins on θ (K=10,15,20)
12	  - theta_qt_K   : quantile bins on θ (K=10,15,20)
13	  - external_5   : plan_011 baseline (5-quantile bins on full-matrix total score)
14	
15	Outputs (all in plan_012/):
16	  theta_estimates.csv, dose_response_theta.csv, enrichment_theta.csv,
17	  plan_012_report.md
18	"""
19	
20	import numpy as np
21	import pandas as pd
22	from scipy.sparse import load_npz
23	from scipy.stats import chi2 as chi2_dist, fisher_exact
24	from pathlib import Path
25	import time
26	import warnings
27	
28	warnings.filterwarnings("ignore", category=RuntimeWarning)
29	
30	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
31	OUT = BASE / "plan_012"
32	OUT.mkdir(exist_ok=True)
33	
34	INJECTION_PS = [0.0, 0.3, 0.5, 0.7, 1.0]
35	N_SEEDS = 5
36	N_BASELINE = 500
37	N_CONTAMINATED = 100
38	STRATA_COUNTS = [10, 15, 20]
39	
40	
41	# ════════════════════════════════════════════════════════════════════════════
42	#  MH-DIF CORE
43	# ════════════════════════════════════════════════════════════════════════════
44	def _nan_row(j):
45	    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
46	                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A")
47	
48	
49	def _compute_mh_item(X_ref_j, X_foc_j, k_ref, k_foc, n_bins):
50	    """Compute MH statistics for a single item given pre-computed bin assignments."""
51	    R = S = 0.0
52	    sum_diff = 0.0
53	    sum_var = 0.0
54	    pr = ps_qr = qs = 0.0
55	    n_ok = 0
56	
57	    for k in range(n_bins):
58	        mr = (k_ref == k)
59	        mf = (k_foc == k)
60	        n1 = int(mr.sum())
61	        n0 = int(mf.sum())
62	        if n1 == 0 or n0 == 0:
63	            continue
64	
65	        A = float(X_ref_j[mr].sum())
66	        B = float(n1 - A)
67	        C = float(X_foc_j[mf].sum())
68	        D = float(n0 - C)
69	        Nk = float(n1 + n0)
70	        m1 = A + C
71	        m0 = B + D
72	
73	        if m1 == 0 or m0 == 0 or Nk <= 1:
74	            continue
75	        n_ok += 1
76	
77	        Rk = A * D / Nk
78	        Sk = B * C / Nk
79	        R += Rk
80	        S += Sk
81	
82	        EA = n1 * m1 / Nk
83	        sum_diff += A - EA
84	        sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))
85	
86	        Pk = (A + D) / Nk
87	        Qk = (B + C) / Nk
88	        pr += Pk * Rk
89	        ps_qr += Pk * Sk + Qk * Rk
90	        qs += Qk * Sk
91	
92	    if n_ok == 0 or (R == 0 and S == 0):
93	        return None
94	
95	    if S == 0:
96	        alpha, delta, se = np.inf, -np.inf, np.nan
97	    elif R == 0:
98	        alpha, delta, se = 0.0, np.inf, np.nan
99	    else:
100	        alpha = R / S
101	        delta = -2.35 * np.log(alpha)
102	        v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
103	        se = 2.35 * np.sqrt(v) if v > 0 else np.nan
104	
105	    if sum_var > 0:
106	        chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
107	        pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
108	    else:
109	        chi2_stat = pval = np.nan
110	
111	    ad = abs(delta) if np.isfinite(delta) else np.inf
112	    if ad < 1.0:
113	        ets = "A"
114	    elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:
115	        ets = "C"
116	    else:
117	        ets = "B"
118	
119	    return dict(alpha_mh=alpha, delta_mh=delta, se=se,
120	                chi2=chi2_stat, p_value=pval, ets_class=ets)
121	
122	
123	def mh_dif_with_bins(X_ref, X_foc, scores_ref, scores_foc, n_strata, bin_mode="equal"):
124	    """
125	    MH-DIF with pre-computed ability scores.
126	
127	    bin_mode:
128	      "equal"   — equal-width bins on score scale
129	      "quantile" — quantile bins (equal-count)
130	    """
131	    J = X_ref.shape[1]
132	    s_all = np.concatenate([scores_ref, scores_foc])
133	
134	    if bin_mode == "equal":
135	        edges = np.linspace(s_all.min() - 0.001, s_all.max() + 0.001, n_strata + 1)
136	        n_bins = n_strata
137	    else:
138	        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
139	        n_bins = len(edges) - 1
140	
141	    if n_bins < 2:
142	        return pd.DataFrame([_nan_row(j) for j in range(J)])
143	
144	    k_ref = np.digitize(scores_ref, edges[1:-1])
145	    k_foc = np.digitize(scores_foc, edges[1:-1])
146	
147	    rows = []
148	    for j in range(J):
149	        result = _compute_mh_item(X_ref[:, j], X_foc[:, j], k_ref, k_foc, n_bins)
150	        if result is None:
151	            rows.append(_nan_row(j))
152	        else:
153	            result["col_idx"] = j
154	            rows.append(result)
155	
156	    return pd.DataFrame(rows)
157	
158	
159	# ════════════════════════════════════════════════════════════════════════════
160	#  DATA LOADING
161	# ════════════════════════════════════════════════════════════════════════════
162	print("=== Loading data ===")
163	mat = load_npz(BASE / "response_matrix.npz")
164	idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
165	MODEL_NAMES = idx["model_names"]
166	ITEM_IDS = idx["item_ids"]
167	ITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}
168	
169	model_meta = pd.read_csv(BASE / "model_metadata.csv")
170	li_labels = pd.read_csv(BASE / "mmlu_li2024_proxy_labels.csv")
171	ability_dif = pd.read_csv(BASE / "plan_001" / "dif_results_ability.csv")
172	
173	NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
174	N_MODELS, J_FULL = mat.shape
175	print(f"  Matrix: {N_MODELS} x {J_FULL}")
176	
177	
178	# ════════════════════════════════════════════════════════════════════════════
179	#  STEP 1: IRT θ ESTIMATION
180	# ════════════════════════════════════════════════════════════════════════════
181	print("\n=== Step 1: IRT theta estimation ===")
182	totals_all = np.asarray(mat.sum(axis=1)).ravel().astype(np.float64)
183	p_correct = (totals_all + 0.5) / (J_FULL + 1.0)
184	theta_all = np.log(p_correct / (1.0 - p_correct))
185	
186	print(f"  θ range: [{theta_all.min():.3f}, {theta_all.max():.3f}]")
187	print(f"  θ mean: {theta_all.mean():.3f}, std: {theta_all.std():.3f}")
188	
189	corr = np.corrcoef(theta_all, totals_all)[0, 1]
190	print(f"  Correlation(θ, total_score): {corr:.4f}")
191	
192	theta_df = pd.DataFrame({
193	    "model_name": MODEL_NAMES,
194	    "theta": theta_all,
195	    "total_score": totals_all,
196	    "method": "logit_laplace"
197	})
198	theta_df.to_csv(OUT / "theta_estimates.csv", index=False)
199	print(f"  Saved theta_estimates.csv ({len(theta_df)} rows)")
200	
201	
202	# ════════════════════════════════════════════════════════════════════════════
203	#  STEP 2: SELECT BASELINE ITEMS (same as plan_011)
204	# ════════════════════════════════════════════════════════════════════════════
205	print("\n=== Step 2: Selecting baseline items ===")
206	merged = ability_dif.merge(li_labels[["item_id", "contamination_type"]], on="item_id", how="inner")
207	baseline_pool = merged[(merged["contamination_type"] == "clean") & (merged["ets_class"] == "A")]
208	print(f"  Baseline pool (clean + ETS A): {len(baseline_pool)}")
209	
210	baseline_items = baseline_pool.sample(N_BASELINE, random_state=42)
211	baseline_item_ids = baseline_items["item_id"].values
212	baseline_col_indices = np.array([ITEM2COL[iid] for iid in baseline_item_ids])
213	print(f"  Selected {N_BASELINE} baseline items")
214	
215	
216	# ════════════════════════════════════════════════════════════════════════════
217	#  STEP 3: DEFINE COHORTS
218	# ════════════════════════════════════════════════════════════════════════════
219	print("\n=== Step 3: Defining cohorts ===")
220	
221	
222	def get_row_indices(col, values):
223	    names = model_meta.loc[model_meta[col].isin(values), "model_name"]
224	    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])
225	
226	
227	cohort_defs = {}
228	
229	# (a) Ability cohort
230	ref_ability_idx = get_row_indices("cohort_accuracy_quintile", [1, 2])
231	foc_ability_idx = get_row_indices("cohort_accuracy_quintile", [4, 5])
232	
233	ref_acc = model_meta.loc[model_meta["cohort_accuracy_quintile"].isin([1, 2]), "accuracy"]
234	foc_acc = model_meta.loc[model_meta["cohort_accuracy_quintile"].isin([4, 5]), "accuracy"]
235	ab_overlap_min = max(ref_acc.min(), foc_acc.min())
236	ab_overlap_max = min(ref_acc.max(), foc_acc.max())
237	
238	if ab_overlap_min <= ab_overlap_max:
239	    foc_ab_inject_mask = (
240	        model_meta["cohort_accuracy_quintile"].isin([4, 5]) &
241	        (model_meta["accuracy"] >= ab_overlap_min) &
242	        (model_meta["accuracy"] <= ab_overlap_max)
243	    )
244	    foc_ab_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_ab_inject_mask, "model_name"] if n in NAME2ROW])
245	else:
246	    foc_ab_inject_idx = foc_ability_idx
247	
248	print(f"  Ability: ref={len(ref_ability_idx)} (Q1-2), foc={len(foc_ability_idx)} (Q4-5)")
249	
250	cohort_defs["ability"] = dict(
251	    ref_idx=ref_ability_idx, foc_idx=foc_ability_idx,
252	    foc_inject_idx=foc_ab_inject_idx
253	)
254	
255	# (b) Temporal cohort
256	ref_temporal_idx = get_row_indices("cohort_temporal", ["2023"])
257	foc_temporal_idx = get_row_indices("cohort_temporal", ["2024"])
258	
259	ref_t_acc = model_meta.loc[model_meta["cohort_temporal"] == "2023", "accuracy"]
260	foc_t_acc = model_meta.loc[model_meta["cohort_temporal"] == "2024", "accuracy"]
261	t_overlap_min = max(ref_t_acc.min(), foc_t_acc.min())
262	t_overlap_max = min(ref_t_acc.max(), foc_t_acc.max())
263	
264	foc_t_inject_mask = (
265	    (model_meta["cohort_temporal"] == "2024") &
266	    (model_meta["accuracy"] >= t_overlap_min) &
267	    (model_meta["accuracy"] <= t_overlap_max)
268	)
269	foc_t_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_t_inject_mask, "model_name"] if n in NAME2ROW])
270	
271	print(f"  Temporal: ref={len(ref_temporal_idx)} (2023), foc={len(foc_temporal_idx)} (2024)")
272	print(f"    Inject: {len(foc_t_inject_idx)} focal models in accuracy overlap")
273	
274	cohort_defs["temporal"] = dict(
275	    ref_idx=ref_temporal_idx, foc_idx=foc_temporal_idx,
276	    foc_inject_idx=foc_t_inject_idx
277	)
278	
279	
280	# ════════════════════════════════════════════════════════════════════════════
281	#  STEP 4: SEMI-SYNTHETIC INJECTION + θ-CONDITIONED MH-DIF
282	# ════════════════════════════════════════════════════════════════════════════
283	print("\n=== Step 4: Semi-Synthetic Injection + MH-DIF ===")
284	
285	X_base = mat[:, baseline_col_indices].toarray().astype(np.int8)
286	full_totals = np.asarray(mat.sum(axis=1)).ravel().astype(np.float64)
287	print(f"  Baseline submatrix: {X_base.shape}, density: {X_base.mean():.4f}")
288	
289	# Build variant list: theta_eq_K, theta_qt_K, external_5
290	MH_VARIANTS = []
291	for ns in STRATA_COUNTS:
292	    MH_VARIANTS.append(f"theta_eq_{ns}")
293	    MH_VARIANTS.append(f"theta_qt_{ns}")
294	MH_VARIANTS.append("external_5")
295	
296	injection_rows = []
297	
298	total_runs = len(INJECTION_PS) * N_SEEDS * len(cohort_defs) * len(MH_VARIANTS)
299	run_count = 0
300	t_start = time.time()
301	
302	for cohort_name, cdef in cohort_defs.items():
303	    ref_idx = cdef["ref_idx"]
304	    foc_idx = cdef["foc_idx"]
305	    foc_inject_idx = cdef["foc_inject_idx"]
306	
307	    theta_ref = theta_all[ref_idx]
308	    theta_foc = theta_all[foc_idx]
309	    ext_ref = full_totals[ref_idx]
310	    ext_foc = full_totals[foc_idx]
311	
312	    for p in INJECTION_PS:
313	        for seed in range(1, N_SEEDS + 1):
314	            rng = np.random.RandomState(seed)
315	
316	            contam_local_idx = rng.choice(N_BASELINE, N_CONTAMINATED, replace=False)
317	            contam_set = set(contam_local_idx.tolist())
318	
319	            X_inj = X_base.copy()
320	            n_flipped = 0
321	
322	            if p > 0:
323	                for local_j in contam_local_idx:
324	                    for model_row in foc_inject_idx:
325	                        if X_inj[model_row, local_j] == 0:
326	                            if rng.random() < p:
327	                                X_inj[model_row, local_j] = 1
328	                                n_flipped += 1
329	
330	            X_ref = X_inj[ref_idx]
331	            X_foc = X_inj[foc_idx]
332	
333	            for variant in MH_VARIANTS:
334	                run_count += 1
335	
336	                if variant.startswith("theta_eq_"):
337	                    ns = int(variant.split("_")[2])
338	                    dif_results = mh_dif_with_bins(
339	                        X_ref, X_foc, theta_ref, theta_foc,
340	                        n_strata=ns, bin_mode="equal"
341	                    )
342	                    strata_count = ns
343	                elif variant.startswith("theta_qt_"):
344	                    ns = int(variant.split("_")[2])
345	                    dif_results = mh_dif_with_bins(
346	                        X_ref, X_foc, theta_ref, theta_foc,
347	                        n_strata=ns, bin_mode="quantile"
348	                    )
349	                    strata_count = ns
350	                elif variant == "external_5":
351	                    dif_results = mh_dif_with_bins(
352	                        X_ref, X_foc, ext_ref, ext_foc,
353	                        n_strata=5, bin_mode="quantile"
354	                    )
355	                    strata_count = 5
356	
357	                contam_mask = dif_results["col_idx"].isin(contam_set)
358	                contam_results = dif_results[contam_mask]
359	                clean_results = dif_results[~contam_mask]
360	
361	                n_c_contam = (contam_results["ets_class"] == "C").sum()
362	                n_c_clean = (clean_results["ets_class"] == "C").sum()
363	                tpr = n_c_contam / N_CONTAMINATED
364	                fpr = n_c_clean / (N_BASELINE - N_CONTAMINATED)
365	
366	                table = [[n_c_contam, N_CONTAMINATED - n_c_contam],
367	                         [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]
368	                fisher_or, fisher_p = fisher_exact(table)
369	
370	                injection_rows.append(dict(
371	                    p=p, seed=seed, cohort_type=cohort_name,
372	                    mh_variant=variant,
373	                    strata_count=strata_count,
374	                    tpr=tpr, fpr=fpr,
375	                    fisher_or=fisher_or, fisher_p=fisher_p,
376	                    n_responses_flipped=n_flipped,
377	                ))
378	
379	                elapsed = time.time() - t_start
380	                if run_count % 35 == 0 or (p in [0.0, 1.0] and seed == 1 and "theta_eq_10" in variant):
381	                    print(f"  [{run_count}/{total_runs}] {cohort_name} {variant:14s} p={p} seed={seed}: "
382	                          f"TPR={tpr:.3f} FPR={fpr:.3f} ({elapsed:.0f}s)")
383	
384	
385	# ════════════════════════════════════════════════════════════════════════════
386	#  STEP 5: AGGREGATE & SAVE
387	# ════════════════════════════════════════════════════════════════════════════
388	print("\n=== Step 5: Aggregating results ===")
389	
390	inj_df = pd.DataFrame(injection_rows)
391	
392	summary_rows = []
393	for (p_val, cohort, variant), grp in inj_df.groupby(["p", "cohort_type", "mh_variant"]):
394	    summary_rows.append(dict(
395	        p=p_val, cohort_type=cohort, mh_variant=variant,
396	        strata_count=grp["strata_count"].iloc[0],
397	        tpr_mean=grp["tpr"].mean(), tpr_std=grp["tpr"].std(),
398	        fpr_mean=grp["fpr"].mean(), fpr_std=grp["fpr"].std(),
399	        fisher_or_mean=grp["fisher_or"].mean(),
400	        fisher_p_median=grp["fisher_p"].median(),
401	    ))
402	summary_df = pd.DataFrame(summary_rows)
403	
404	inj_df.to_csv(OUT / "injection_results.csv", index=False)
405	summary_df.to_csv(OUT / "dose_response_theta.csv", index=False)
406	print(f"  Saved injection_results.csv ({len(inj_df)} rows)")
407	print(f"  Saved dose_response_theta.csv ({len(summary_df)} rows)")
408	
409	
410	# ════════════════════════════════════════════════════════════════════════════
411	#  STEP 6: REAL DATA DIF — ENRICHMENT AGAINST LI ET AL. LABELS
412	# ════════════════════════════════════════════════════════════════════════════
413	print("\n=== Step 6: Real data DIF (no injection) — enrichment vs Li et al. ===")
414	
415	li_item_ids = li_labels["item_id"].values
416	li_col_indices = np.array([ITEM2COL[iid] for iid in li_item_ids if iid in ITEM2COL])
417	li_item_ids_valid = np.array([iid for iid in li_item_ids if iid in ITEM2COL])
418	
419	li_labels_valid = li_labels[li_labels["item_id"].isin(li_item_ids_valid)].copy()
420	li_labels_valid = li_labels_valid.set_index("item_id").loc[li_item_ids_valid].reset_index()
421	
422	X_li = mat[:, li_col_indices].toarray().astype(np.int8)
423	print(f"  Li et al. items submatrix: {X_li.shape}")
424	
425	enrichment_rows = []
426	
427	for cohort_name in ["temporal"]:
428	    cdef = cohort_defs[cohort_name]
429	    ref_idx = cdef["ref_idx"]
430	    foc_idx = cdef["foc_idx"]
431	
432	    X_ref_li = X_li[ref_idx]
433	    X_foc_li = X_li[foc_idx]
434	
435	    theta_ref = theta_all[ref_idx]
436	    theta_foc = theta_all[foc_idx]
437	    ext_ref = full_totals[ref_idx]
438	    ext_foc = full_totals[foc_idx]
439	
440	    for variant in MH_VARIANTS:
441	        if variant.startswith("theta_eq_"):
442	            ns = int(variant.split("_")[2])
443	            dif_results = mh_dif_with_bins(X_ref_li, X_foc_li, theta_ref, theta_foc,
444	                                           n_strata=ns, bin_mode="equal")
445	            sc = ns
446	        elif variant.startswith("theta_qt_"):
447	            ns = int(variant.split("_")[2])
448	            dif_results = mh_dif_with_bins(X_ref_li, X_foc_li, theta_ref, theta_foc,
449	                                           n_strata=ns, bin_mode="quantile")
450	            sc = ns
451	        elif variant == "external_5":
452	            dif_results = mh_dif_with_bins(X_ref_li, X_foc_li, ext_ref, ext_foc,
453	                                           n_strata=5, bin_mode="quantile")
454	            sc = 5
455	
456	        dif_results["item_id"] = li_item_ids_valid[dif_results["col_idx"].values]
457	        dif_merged = dif_results.merge(li_labels_valid[["item_id", "contamination_type"]], on="item_id")
458	
459	        is_contam = dif_merged["contamination_type"] != "clean"
460	        is_clean = dif_merged["contamination_type"] == "clean"
461	        is_c = dif_merged["ets_class"] == "C"
462	
463	        rate_contam = (is_c & is_contam).sum() / is_contam.sum() if is_contam.sum() > 0 else 0
464	        rate_clean = (is_c & is_clean).sum() / is_clean.sum() if is_clean.sum() > 0 else 0
465	        enrichment = rate_contam / rate_clean if rate_clean > 0 else np.inf
466	
467	        enrichment_rows.append(dict(
468	            cohort=cohort_name,
469	            mh_variant=variant,
470	            strata_count=sc,
471	            n_items=len(dif_merged),
472	            n_contam=int(is_contam.sum()),
473	            n_clean=int(is_clean.sum()),
474	            rate_contam=rate_contam,
475	            rate_clean=rate_clean,
476	            fpr_clean=rate_clean,
477	            enrichment=enrichment,
478	        ))
479	
480	        print(f"  {variant:14s}: rate_contam={rate_contam:.4f}, "
481	              f"rate_clean={rate_clean:.4f}, enrichment={enrichment:.3f}")
482	
483	enrichment_df = pd.DataFrame(enrichment_rows)
484	enrichment_df.to_csv(OUT / "enrichment_theta.csv", index=False)
485	print(f"  Saved enrichment_theta.csv ({len(enrichment_df)} rows)")
486	
487	
488	# ════════════════════════════════════════════════════════════════════════════
489	#  REPORT
490	# ════════════════════════════════════════════════════════════════════════════
491	print("\n=== Generating report ===")
492	
493	L = []
494	def w(s=""):
495	    L.append(s)
496	
497	w("# Plan 012: IRT θ-Conditioning MH-DIF Analysis")
498	w()
499	w("## 1. Objective")
500	w()
501	w("Replace raw total scores with IRT-based θ estimates as the MH-DIF stratification")
502	w("variable. Test whether finer ability matching reduces the high baseline FPR from")
503	w("plan_011 (temporal ~31%, ability ~49%) while preserving detection power (TPR).")
504	w()
505	
506	w("## 2. θ Estimation Method")
507	w()
508	w("**Method**: Logit of proportion correct with Laplace smoothing")
509	w("```")
510	w("θ = log((total + 0.5) / (N_items + 1 - total - 0.5))")
511	w("```")
512	w(f"- N models: {N_MODELS}")
513	w(f"- N items (full matrix): {J_FULL}")
514	w(f"- θ range: [{theta_all.min():.3f}, {theta_all.max():.3f}]")
515	w(f"- θ mean±std: {theta_all.mean():.3f}±{theta_all.std():.3f}")
516	w(f"- Correlation(θ, total_score): {corr:.4f}")
517	w()
518	w("This is a monotone transformation of the Rasch model sufficient statistic.")
519	w("Two binning strategies are compared:")
520	w("- **Equal-width (eq)**: equal intervals on the logit scale — respects IRT metric")
521	w("- **Quantile (qt)**: equal-count bins — ensures balanced strata")
522	w()
523	
524	w("## 3. Experimental Design")
525	w()
526	w(f"- Baseline items: {N_BASELINE}")
527	w(f"- Contaminated per run: {N_CONTAMINATED}")
528	w(f"- Injection probabilities: {INJECTION_PS}")
529	w(f"- Seeds per p: {N_SEEDS}")
530	w(f"- Strata counts tested: {STRATA_COUNTS}")
531	w()
532	w("### Cohort definitions")
533	w()
534	for cn, cd in cohort_defs.items():
535	    w(f"- **{cn}**: ref N={len(cd['ref_idx'])}, foc N={len(cd['foc_idx'])}, "
536	      f"foc inject N={len(cd['foc_inject_idx'])}")
537	w()
538	w("### MH variants")
539	w()
540	w("| Variant | Stratification | Description |")
541	w("|---------|---------------|-------------|")
542	for ns in STRATA_COUNTS:
543	    w(f"| theta_eq_{ns} | Equal-width θ bins | {ns} equal intervals on logit scale |")
544	    w(f"| theta_qt_{ns} | Quantile θ bins | {ns} equal-count bins on θ |")
545	w("| external_5 | Quantile total-score | 5 bins on full-matrix total (plan_011 baseline) |")
546	w()
547	
548	# ─── Results tables ───
549	w("## 4. Semi-Synthetic Results")
550	w()
551	
552	for cohort in ["temporal", "ability"]:
553	    w(f"### {cohort.capitalize()} cohort")
554	    w()
555	
556	    # Baseline FPR table
557	    w("#### Baseline FPR (p=0)")
558	    w()
559	    w("| Variant | FPR (mean±std) |")
560	    w("|---------|----------------|")
561	    sub = summary_df[(summary_df["p"] == 0.0) & (summary_df["cohort_type"] == cohort)]
562	    for _, r in sub.sort_values("mh_variant").iterrows():
563	        w(f"| {r.mh_variant} | {r.fpr_mean:.3f}±{r.fpr_std:.3f} |")
564	    w()
565	
566	    # Dose-response table (selected variants)
567	    w("#### Dose-response (key variants)")
568	    w()
569	    key_variants = ["theta_eq_10", "theta_qt_10", "theta_qt_20", "external_5"]
570	    w("| Variant | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |")
571	    w("|---------|---|----------------|----------------|------|-----------|----------|")
572	    for variant in key_variants:
573	        sub_v = summary_df[(summary_df["cohort_type"] == cohort) & (summary_df["mh_variant"] == variant)]
574	        if len(sub_v) == 0:
575	            continue
576	        base_tpr = sub_v[sub_v["p"] == 0.0]["tpr_mean"].values
577	        base_tpr = base_tpr[0] if len(base_tpr) > 0 else 0
578	        for _, r in sub_v.sort_values("p").iterrows():
579	            d_tpr = r.tpr_mean - base_tpr
580	            w(f"| {r.mh_variant} | {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | "
581	              f"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {d_tpr:+.3f} | "
582	              f"{r.fisher_or_mean:.2f} | {r.fisher_p_median:.2e} |")
583	    w()
584	
585	# ─── Success criteria ───
586	w("## 5. Success Criteria Evaluation")
587	w()
588	w("**Target**: baseline FPR < 0.10, TPR > 0.70 at p=0.5 (temporal cohort)")
589	w()
590	
591	for variant in MH_VARIANTS:
592	    sub = summary_df[(summary_df["cohort_type"] == "temporal") & (summary_df["mh_variant"] == variant)]
593	    fpr0 = sub[sub["p"] == 0.0]["fpr_mean"].values
594	    tpr05 = sub[sub["p"] == 0.5]["tpr_mean"].values
595	    if len(fpr0) > 0 and len(tpr05) > 0:
596	        fpr_ok = "PASS" if fpr0[0] < 0.10 else "FAIL"
597	        tpr_ok = "PASS" if tpr05[0] > 0.70 else "FAIL"
598	        w(f"- **{variant}**: FPR={fpr0[0]:.3f} [{fpr_ok}], TPR@p=0.5={tpr05[0]:.3f} [{tpr_ok}]")
599	w()
600	
601	# ─── Enrichment ───
602	w("## 6. Enrichment Against Li et al. Labels (No Injection)")
603	w()
604	w("| Variant | Strata | Rate(contam) | Rate(clean) | Enrichment |")
605	w("|---------|--------|-------------|-------------|------------|")
606	for _, r in enrichment_df.iterrows():
607	    w(f"| {r.mh_variant} | {r.strata_count} | {r.rate_contam:.4f} | "
608	      f"{r.rate_clean:.4f} | {r.enrichment:.3f} |")
609	w()
610	w("(plan_001 reference: enrichment = 0.96 with 5-strata total-score MH)")
611	w()
612	
613	# ─── Analysis ───
614	w("## 7. Analysis & Conclusions")
615	w()
616	
617	# Find best variant
618	best_variant = None
619	best_fpr = 1.0
620	for variant in MH_VARIANTS:
621	    sub = summary_df[(summary_df["cohort_type"] == "temporal") &
622	                     (summary_df["mh_variant"] == variant) & (summary_df["p"] == 0.0)]
623	    if len(sub) > 0:
624	        fpr = sub.iloc[0]["fpr_mean"]
625	        if fpr < best_fpr:
626	            best_fpr = fpr
627	            best_variant = variant
628	
629	ext_sub = summary_df[(summary_df["cohort_type"] == "temporal") &
630	                     (summary_df["mh_variant"] == "external_5") & (summary_df["p"] == 0.0)]
631	ext_fpr = ext_sub.iloc[0]["fpr_mean"] if len(ext_sub) > 0 else None
632	
633	w("### θ vs total-score stratification")
634	w()
635	if ext_fpr is not None:
636	    w(f"- Plan_011 external (5 quantile strata, total score) FPR: {ext_fpr:.3f}")
637	w(f"- Best θ variant ({best_variant}) FPR: {best_fpr:.3f}")
638	if ext_fpr is not None:
639	    w(f"- FPR difference: {best_fpr - ext_fpr:+.3f}")
640	w()
641	
642	w("### Equal-width vs quantile binning")
643	w()
644	for ns in STRATA_COUNTS:
645	    eq_sub = summary_df[(summary_df["cohort_type"] == "temporal") &
646	                        (summary_df["mh_variant"] == f"theta_eq_{ns}") & (summary_df["p"] == 0.0)]
647	    qt_sub = summary_df[(summary_df["cohort_type"] == "temporal") &
648	                        (summary_df["mh_variant"] == f"theta_qt_{ns}") & (summary_df["p"] == 0.0)]
649	    if len(eq_sub) > 0 and len(qt_sub) > 0:
650	        w(f"- K={ns}: equal-width FPR={eq_sub.iloc[0]['fpr_mean']:.3f}, "
651	          f"quantile FPR={qt_sub.iloc[0]['fpr_mean']:.3f}")
652	w()
653	
654	w("### Why FPR remains elevated")
655	w()
656	w("Possible explanations if FPR stays high despite θ-conditioning:")
657	w("1. Real DIF exists between cohorts — genuine differential item functioning")
658	w("   (2023 vs 2024 models genuinely differ on certain items beyond overall ability)")
659	w("2. Cohorts differ on dimensions not captured by a single θ parameter")
660	w("   (e.g., training data composition, architecture effects)")
661	w("3. The logit(p) θ estimate has correlation >.999 with raw total scores,")
662	w("   so quantile bins on θ produce nearly identical strata to quantile bins on totals")
663	w("4. MH-DIF's power to distinguish real DIF from ability confounding is limited")
664	w("   when the grouping variable (year/quintile) correlates strongly with ability")
665	w()
666	
667	w("### Recommendations")
668	w()
669	w("Based on these results:")
670	w()
671	sub_t = summary_df[summary_df["cohort_type"] == "temporal"]
672	for variant in ["theta_eq_10", "theta_qt_10", "theta_qt_20", "external_5"]:
673	    v_sub = sub_t[sub_t["mh_variant"] == variant]
674	    fpr0 = v_sub[v_sub["p"] == 0.0]["fpr_mean"].values
675	    tpr05 = v_sub[v_sub["p"] == 0.5]["tpr_mean"].values
676	    tpr1 = v_sub[v_sub["p"] == 1.0]["tpr_mean"].values
677	    if len(fpr0) > 0 and len(tpr05) > 0 and len(tpr1) > 0:
678	        w(f"- {variant}: FPR₀={fpr0[0]:.3f}, TPR@0.5={tpr05[0]:.3f}, TPR@1.0={tpr1[0]:.3f}")
679	w()
680	
681	(OUT / "plan_012_report.md").write_text("\n".join(L) + "\n")
682	print("  Report written to plan_012_report.md")
683	
684	
685	# ════════════════════════════════════════════════════════════════════════════
686	#  CONSOLE SUMMARY
687	# ════════════════════════════════════════════════════════════════════════════
688	print("\n" + "=" * 70)
689	print("SUMMARY — Baseline FPR (p=0)")
690	print("=" * 70)
691	for cohort in ["temporal", "ability"]:
692	    print(f"\n  {cohort}:")
693	    sub = summary_df[(summary_df["p"] == 0.0) & (summary_df["cohort_type"] == cohort)]
694	    for _, r in sub.sort_values("mh_variant").iterrows():
695	        print(f"    {r.mh_variant:14s}: FPR={r.fpr_mean:.3f}±{r.fpr_std:.3f}")
696	
697	print("\n" + "=" * 70)
698	print("SUMMARY — TPR at p=0.5 (temporal)")
699	print("=" * 70)
700	sub = summary_df[(summary_df["p"] == 0.5) & (summary_df["cohort_type"] == "temporal")]
701	for _, r in sub.sort_values("mh_variant").iterrows():
702	    print(f"  {r.mh_variant:14s}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}")
703	
704	print("\n" + "=" * 70)
705	print("SUMMARY — Enrichment (Li et al.)")
706	print("=" * 70)
707	for _, r in enrichment_df.iterrows():
708	    print(f"  {r.mh_variant:14s}: enrichment={r.enrichment:.3f}")
709	
710	total_elapsed = time.time() - t_start
711	print(f"\nTotal time: {total_elapsed:.0f}s")
712	print(f"All outputs saved to {OUT}")
713	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "30ffd594-8221-46f6-b126-2ea67216ad1e",
  "isSidechain": false,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "type": "user",
  "uuid": "70d4e4b0-5e8e-48ed-ae44-a4c02dbae742",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012/plan_012_irt_theta_analysis.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nplan_012_irt_theta_analysis.py — IRT θ-Conditioning MH-DIF Analysis\n\nUses IRT-based θ estimates (logit of proportion correct) instead of raw total\nscores for MH-DIF stratification. Tests whether finer ability matching reduces\nthe high baseline FPR from plan_011 (temporal ~31%, ability ~49%) while\npreserving detection power for differential contamination.\n\nVariants tested:\n  - theta_eq_K   : equal-width bins on θ (K=10,15,20)\n  - theta_qt_K   : quantile bins on θ (K=10,15,20)\n  - external_5   : plan_011 baseline (5-quantile bins on full-matrix total score)\n\nOutputs (all in plan_012/):\n  theta_estimates.csv, dose_response_theta.csv, enrichment_theta.csv,\n  plan_012_report.md\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist, fisher_exact\nfrom pathlib import Path\nimport time\nimport warnings\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_012\"\nOUT.mkdir(exist_ok=True)\n\nINJECTION_PS = [0.0, 0.3, 0.5, 0.7, 1.0]\nN_SEEDS = 5\nN_BASELINE = 500\nN_CONTAMINATED = 100\nSTRATA_COUNTS = [10, 15, 20]\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE\n# ════════════════════════════════════════════════════════════════════════════\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\")\n\n\ndef _compute_mh_item(X_ref_j, X_foc_j, k_ref, k_foc, n_bins):\n    \"\"\"Compute MH statistics for a single item given pre-computed bin assignments.\"\"\"\n    R = S = 0.0\n    sum_diff = 0.0\n    sum_var = 0.0\n    pr = ps_qr = qs = 0.0\n    n_ok = 0\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1 = int(mr.sum())\n        n0 = int(mf.sum())\n        if n1 == 0 or n0 == 0:\n            continue\n\n        A = float(X_ref_j[mr].sum())\n        B = float(n1 - A)\n        C = float(X_foc_j[mf].sum())\n        D = float(n0 - C)\n        Nk = float(n1 + n0)\n        m1 = A + C\n        m0 = B + D\n\n        if m1 == 0 or m0 == 0 or Nk <= 1:\n            continue\n        n_ok += 1\n\n        Rk = A * D / Nk\n        Sk = B * C / Nk\n        R += Rk\n        S += Sk\n\n        EA = n1 * m1 / Nk\n        sum_diff += A - EA\n        sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n        Pk = (A + D) / Nk\n        Qk = (B + C) / Nk\n        pr += Pk * Rk\n        ps_qr += Pk * Sk + Qk * Rk\n        qs += Qk * Sk\n\n    if n_ok == 0 or (R == 0 and S == 0):\n        return None\n\n    if S == 0:\n        alpha, delta, se = np.inf, -np.inf, np.nan\n    elif R == 0:\n        alpha, delta, se = 0.0, np.inf, np.nan\n    else:\n        alpha = R / S\n        delta = -2.35 * np.log(alpha)\n        v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n        se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n    if sum_var > 0:\n        chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n        pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n    else:\n        chi2_stat = pval = np.nan\n\n    ad = abs(delta) if np.isfinite(delta) else np.inf\n    if ad < 1.0:\n        ets = \"A\"\n    elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n        ets = \"C\"\n    else:\n        ets = \"B\"\n\n    return dict(alpha_mh=alpha, delta_mh=delta, se=se,\n                chi2=chi2_stat, p_value=pval, ets_class=ets)\n\n\ndef mh_dif_with_bins(X_ref, X_foc, scores_ref, scores_foc, n_strata, bin_mode=\"equal\"):\n    \"\"\"\n    MH-DIF with pre-computed ability scores.\n\n    bin_mode:\n      \"equal\"   — equal-width bins on score scale\n      \"quantile\" — quantile bins (equal-count)\n    \"\"\"\n    J = X_ref.shape[1]\n    s_all = np.concatenate([scores_ref, scores_foc])\n\n    if bin_mode == \"equal\":\n        edges = np.linspace(s_all.min() - 0.001, s_all.max() + 0.001, n_strata + 1)\n        n_bins = n_strata\n    else:\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        n_bins = len(edges) - 1\n\n    if n_bins < 2:\n        return pd.DataFrame([_nan_row(j) for j in range(J)])\n\n    k_ref = np.digitize(scores_ref, edges[1:-1])\n    k_foc = np.digitize(scores_foc, edges[1:-1])\n\n    rows = []\n    for j in range(J):\n        result = _compute_mh_item(X_ref[:, j], X_foc[:, j], k_ref, k_foc, n_bins)\n        if result is None:\n            rows.append(_nan_row(j))\n        else:\n            result[\"col_idx\"] = j\n            rows.append(result)\n\n    return pd.DataFrame(rows)\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"=== Loading data ===\")\nmat = load_npz(BASE / \"response_matrix.npz\")\nidx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\nMODEL_NAMES = idx[\"model_names\"]\nITEM_IDS = idx[\"item_ids\"]\nITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}\n\nmodel_meta = pd.read_csv(BASE / \"model_metadata.csv\")\nli_labels = pd.read_csv(BASE / \"mmlu_li2024_proxy_labels.csv\")\nability_dif = pd.read_csv(BASE / \"plan_001\" / \"dif_results_ability.csv\")\n\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\nN_MODELS, J_FULL = mat.shape\nprint(f\"  Matrix: {N_MODELS} x {J_FULL}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 1: IRT θ ESTIMATION\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 1: IRT theta estimation ===\")\ntotals_all = np.asarray(mat.sum(axis=1)).ravel().astype(np.float64)\np_correct = (totals_all + 0.5) / (J_FULL + 1.0)\ntheta_all = np.log(p_correct / (1.0 - p_correct))\n\nprint(f\"  θ range: [{theta_all.min():.3f}, {theta_all.max():.3f}]\")\nprint(f\"  θ mean: {theta_all.mean():.3f}, std: {theta_all.std():.3f}\")\n\ncorr = np.corrcoef(theta_all, totals_all)[0, 1]\nprint(f\"  Correlation(θ, total_score): {corr:.4f}\")\n\ntheta_df = pd.DataFrame({\n    \"model_name\": MODEL_NAMES,\n    \"theta\": theta_all,\n    \"total_score\": totals_all,\n    \"method\": \"logit_laplace\"\n})\ntheta_df.to_csv(OUT / \"theta_estimates.csv\", index=False)\nprint(f\"  Saved theta_estimates.csv ({len(theta_df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 2: SELECT BASELINE ITEMS (same as plan_011)\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 2: Selecting baseline items ===\")\nmerged = ability_dif.merge(li_labels[[\"item_id\", \"contamination_type\"]], on=\"item_id\", how=\"inner\")\nbaseline_pool = merged[(merged[\"contamination_type\"] == \"clean\") & (merged[\"ets_class\"] == \"A\")]\nprint(f\"  Baseline pool (clean + ETS A): {len(baseline_pool)}\")\n\nbaseline_items = baseline_pool.sample(N_BASELINE, random_state=42)\nbaseline_item_ids = baseline_items[\"item_id\"].values\nbaseline_col_indices = np.array([ITEM2COL[iid] for iid in baseline_item_ids])\nprint(f\"  Selected {N_BASELINE} baseline items\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 3: DEFINE COHORTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 3: Defining cohorts ===\")\n\n\ndef get_row_indices(col, values):\n    names = model_meta.loc[model_meta[col].isin(values), \"model_name\"]\n    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])\n\n\ncohort_defs = {}\n\n# (a) Ability cohort\nref_ability_idx = get_row_indices(\"cohort_accuracy_quintile\", [1, 2])\nfoc_ability_idx = get_row_indices(\"cohort_accuracy_quintile\", [4, 5])\n\nref_acc = model_meta.loc[model_meta[\"cohort_accuracy_quintile\"].isin([1, 2]), \"accuracy\"]\nfoc_acc = model_meta.loc[model_meta[\"cohort_accuracy_quintile\"].isin([4, 5]), \"accuracy\"]\nab_overlap_min = max(ref_acc.min(), foc_acc.min())\nab_overlap_max = min(ref_acc.max(), foc_acc.max())\n\nif ab_overlap_min <= ab_overlap_max:\n    foc_ab_inject_mask = (\n        model_meta[\"cohort_accuracy_quintile\"].isin([4, 5]) &\n        (model_meta[\"accuracy\"] >= ab_overlap_min) &\n        (model_meta[\"accuracy\"] <= ab_overlap_max)\n    )\n    foc_ab_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_ab_inject_mask, \"model_name\"] if n in NAME2ROW])\nelse:\n    foc_ab_inject_idx = foc_ability_idx\n\nprint(f\"  Ability: ref={len(ref_ability_idx)} (Q1-2), foc={len(foc_ability_idx)} (Q4-5)\")\n\ncohort_defs[\"ability\"] = dict(\n    ref_idx=ref_ability_idx, foc_idx=foc_ability_idx,\n    foc_inject_idx=foc_ab_inject_idx\n)\n\n# (b) Temporal cohort\nref_temporal_idx = get_row_indices(\"cohort_temporal\", [\"2023\"])\nfoc_temporal_idx = get_row_indices(\"cohort_temporal\", [\"2024\"])\n\nref_t_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\nfoc_t_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"accuracy\"]\nt_overlap_min = max(ref_t_acc.min(), foc_t_acc.min())\nt_overlap_max = min(ref_t_acc.max(), foc_t_acc.max())\n\nfoc_t_inject_mask = (\n    (model_meta[\"cohort_temporal\"] == \"2024\") &\n    (model_meta[\"accuracy\"] >= t_overlap_min) &\n    (model_meta[\"accuracy\"] <= t_overlap_max)\n)\nfoc_t_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_t_inject_mask, \"model_name\"] if n in NAME2ROW])\n\nprint(f\"  Temporal: ref={len(ref_temporal_idx)} (2023), foc={len(foc_temporal_idx)} (2024)\")\nprint(f\"    Inject: {len(foc_t_inject_idx)} focal models in accuracy overlap\")\n\ncohort_defs[\"temporal\"] = dict(\n    ref_idx=ref_temporal_idx, foc_idx=foc_temporal_idx,\n    foc_inject_idx=foc_t_inject_idx\n)\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 4: SEMI-SYNTHETIC INJECTION + θ-CONDITIONED MH-DIF\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 4: Semi-Synthetic Injection + MH-DIF ===\")\n\nX_base = mat[:, baseline_col_indices].toarray().astype(np.int8)\nfull_totals = np.asarray(mat.sum(axis=1)).ravel().astype(np.float64)\nprint(f\"  Baseline submatrix: {X_base.shape}, density: {X_base.mean():.4f}\")\n\n# Build variant list: theta_eq_K, theta_qt_K, external_5\nMH_VARIANTS = []\nfor ns in STRATA_COUNTS:\n    MH_VARIANTS.append(f\"theta_eq_{ns}\")\n    MH_VARIANTS.append(f\"theta_qt_{ns}\")\nMH_VARIANTS.append(\"external_5\")\n\ninjection_rows = []\n\ntotal_runs = len(INJECTION_PS) * N_SEEDS * len(cohort_defs) * len(MH_VARIANTS)\nrun_count = 0\nt_start = time.time()\n\nfor cohort_name, cdef in cohort_defs.items():\n    ref_idx = cdef[\"ref_idx\"]\n    foc_idx = cdef[\"foc_idx\"]\n    foc_inject_idx = cdef[\"foc_inject_idx\"]\n\n    theta_ref = theta_all[ref_idx]\n    theta_foc = theta_all[foc_idx]\n    ext_ref = full_totals[ref_idx]\n    ext_foc = full_totals[foc_idx]\n\n    for p in INJECTION_PS:\n        for seed in range(1, N_SEEDS + 1):\n            rng = np.random.RandomState(seed)\n\n            contam_local_idx = rng.choice(N_BASELINE, N_CONTAMINATED, replace=False)\n            contam_set = set(contam_local_idx.tolist())\n\n            X_inj = X_base.copy()\n            n_flipped = 0\n\n            if p > 0:\n                for local_j in contam_local_idx:\n                    for model_row in foc_inject_idx:\n                        if X_inj[model_row, local_j] == 0:\n                            if rng.random() < p:\n                                X_inj[model_row, local_j] = 1\n                                n_flipped += 1\n\n            X_ref = X_inj[ref_idx]\n            X_foc = X_inj[foc_idx]\n\n            for variant in MH_VARIANTS:\n                run_count += 1\n\n                if variant.startswith(\"theta_eq_\"):\n                    ns = int(variant.split(\"_\")[2])\n                    dif_results = mh_dif_with_bins(\n                        X_ref, X_foc, theta_ref, theta_foc,\n                        n_strata=ns, bin_mode=\"equal\"\n                    )\n                    strata_count = ns\n                elif variant.startswith(\"theta_qt_\"):\n                    ns = int(variant.split(\"_\")[2])\n                    dif_results = mh_dif_with_bins(\n                        X_ref, X_foc, theta_ref, theta_foc,\n                        n_strata=ns, bin_mode=\"quantile\"\n                    )\n                    strata_count = ns\n                elif variant == \"external_5\":\n                    dif_results = mh_dif_with_bins(\n                        X_ref, X_foc, ext_ref, ext_foc,\n                        n_strata=5, bin_mode=\"quantile\"\n                    )\n                    strata_count = 5\n\n                contam_mask = dif_results[\"col_idx\"].isin(contam_set)\n                contam_results = dif_results[contam_mask]\n                clean_results = dif_results[~contam_mask]\n\n                n_c_contam = (contam_results[\"ets_class\"] == \"C\").sum()\n                n_c_clean = (clean_results[\"ets_class\"] == \"C\").sum()\n                tpr = n_c_contam / N_CONTAMINATED\n                fpr = n_c_clean / (N_BASELINE - N_CONTAMINATED)\n\n                table = [[n_c_contam, N_CONTAMINATED - n_c_contam],\n                         [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]\n                fisher_or, fisher_p = fisher_exact(table)\n\n                injection_rows.append(dict(\n                    p=p, seed=seed, cohort_type=cohort_name,\n                    mh_variant=variant,\n                    strata_count=strata_count,\n                    tpr=tpr, fpr=fpr,\n                    fisher_or=fisher_or, fisher_p=fisher_p,\n                    n_responses_flipped=n_flipped,\n                ))\n\n                elapsed = time.time() - t_start\n                if run_count % 35 == 0 or (p in [0.0, 1.0] and seed == 1 and \"theta_eq_10\" in variant):\n                    print(f\"  [{run_count}/{total_runs}] {cohort_name} {variant:14s} p={p} seed={seed}: \"\n                          f\"TPR={tpr:.3f} FPR={fpr:.3f} ({elapsed:.0f}s)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 5: AGGREGATE & SAVE\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 5: Aggregating results ===\")\n\ninj_df = pd.DataFrame(injection_rows)\n\nsummary_rows = []\nfor (p_val, cohort, variant), grp in inj_df.groupby([\"p\", \"cohort_type\", \"mh_variant\"]):\n    summary_rows.append(dict(\n        p=p_val, cohort_type=cohort, mh_variant=variant,\n        strata_count=grp[\"strata_count\"].iloc[0],\n        tpr_mean=grp[\"tpr\"].mean(), tpr_std=grp[\"tpr\"].std(),\n        fpr_mean=grp[\"fpr\"].mean(), fpr_std=grp[\"fpr\"].std(),\n        fisher_or_mean=grp[\"fisher_or\"].mean(),\n        fisher_p_median=grp[\"fisher_p\"].median(),\n    ))\nsummary_df = pd.DataFrame(summary_rows)\n\ninj_df.to_csv(OUT / \"injection_results.csv\", index=False)\nsummary_df.to_csv(OUT / \"dose_response_theta.csv\", index=False)\nprint(f\"  Saved injection_results.csv ({len(inj_df)} rows)\")\nprint(f\"  Saved dose_response_theta.csv ({len(summary_df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 6: REAL DATA DIF — ENRICHMENT AGAINST LI ET AL. LABELS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 6: Real data DIF (no injection) — enrichment vs Li et al. ===\")\n\nli_item_ids = li_labels[\"item_id\"].values\nli_col_indices = np.array([ITEM2COL[iid] for iid in li_item_ids if iid in ITEM2COL])\nli_item_ids_valid = np.array([iid for iid in li_item_ids if iid in ITEM2COL])\n\nli_labels_valid = li_labels[li_labels[\"item_id\"].isin(li_item_ids_valid)].copy()\nli_labels_valid = li_labels_valid.set_index(\"item_id\").loc[li_item_ids_valid].reset_index()\n\nX_li = mat[:, li_col_indices].toarray().astype(np.int8)\nprint(f\"  Li et al. items submatrix: {X_li.shape}\")\n\nenrichment_rows = []\n\nfor cohort_name in [\"temporal\"]:\n    cdef = cohort_defs[cohort_name]\n    ref_idx = cdef[\"ref_idx\"]\n    foc_idx = cdef[\"foc_idx\"]\n\n    X_ref_li = X_li[ref_idx]\n    X_foc_li = X_li[foc_idx]\n\n    theta_ref = theta_all[ref_idx]\n    theta_foc = theta_all[foc_idx]\n    ext_ref = full_totals[ref_idx]\n    ext_foc = full_totals[foc_idx]\n\n    for variant in MH_VARIANTS:\n        if variant.startswith(\"theta_eq_\"):\n            ns = int(variant.split(\"_\")[2])\n            dif_results = mh_dif_with_bins(X_ref_li, X_foc_li, theta_ref, theta_foc,\n                                           n_strata=ns, bin_mode=\"equal\")\n            sc = ns\n        elif variant.startswith(\"theta_qt_\"):\n            ns = int(variant.split(\"_\")[2])\n            dif_results = mh_dif_with_bins(X_ref_li, X_foc_li, theta_ref, theta_foc,\n                                           n_strata=ns, bin_mode=\"quantile\")\n            sc = ns\n        elif variant == \"external_5\":\n            dif_results = mh_dif_with_bins(X_ref_li, X_foc_li, ext_ref, ext_foc,\n                                           n_strata=5, bin_mode=\"quantile\")\n            sc = 5\n\n        dif_results[\"item_id\"] = li_item_ids_valid[dif_results[\"col_idx\"].values]\n        dif_merged = dif_results.merge(li_labels_valid[[\"item_id\", \"contamination_type\"]], on=\"item_id\")\n\n        is_contam = dif_merged[\"contamination_type\"] != \"clean\"\n        is_clean = dif_merged[\"contamination_type\"] == \"clean\"\n        is_c = dif_merged[\"ets_class\"] == \"C\"\n\n        rate_contam = (is_c & is_contam).sum() / is_contam.sum() if is_contam.sum() > 0 else 0\n        rate_clean = (is_c & is_clean).sum() / is_clean.sum() if is_clean.sum() > 0 else 0\n        enrichment = rate_contam / rate_clean if rate_clean > 0 else np.inf\n\n        enrichment_rows.append(dict(\n            cohort=cohort_name,\n            mh_variant=variant,\n            strata_count=sc,\n            n_items=len(dif_merged),\n            n_contam=int(is_contam.sum()),\n            n_clean=int(is_clean.sum()),\n            rate_contam=rate_contam,\n            rate_clean=rate_clean,\n            fpr_clean=rate_clean,\n            enrichment=enrichment,\n        ))\n\n        print(f\"  {variant:14s}: rate_contam={rate_contam:.4f}, \"\n              f\"rate_clean={rate_clean:.4f}, enrichment={enrichment:.3f}\")\n\nenrichment_df = pd.DataFrame(enrichment_rows)\nenrichment_df.to_csv(OUT / \"enrichment_theta.csv\", index=False)\nprint(f\"  Saved enrichment_theta.csv ({len(enrichment_df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  REPORT\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Generating report ===\")\n\nL = []\ndef w(s=\"\"):\n    L.append(s)\n\nw(\"# Plan 012: IRT θ-Conditioning MH-DIF Analysis\")\nw()\nw(\"## 1. Objective\")\nw()\nw(\"Replace raw total scores with IRT-based θ estimates as the MH-DIF stratification\")\nw(\"variable. Test whether finer ability matching reduces the high baseline FPR from\")\nw(\"plan_011 (temporal ~31%, ability ~49%) while preserving detection power (TPR).\")\nw()\n\nw(\"## 2. θ Estimation Method\")\nw()\nw(\"**Method**: Logit of proportion correct with Laplace smoothing\")\nw(\"```\")\nw(\"θ = log((total + 0.5) / (N_items + 1 - total - 0.5))\")\nw(\"```\")\nw(f\"- N models: {N_MODELS}\")\nw(f\"- N items (full matrix): {J_FULL}\")\nw(f\"- θ range: [{theta_all.min():.3f}, {theta_all.max():.3f}]\")\nw(f\"- θ mean±std: {theta_all.mean():.3f}±{theta_all.std():.3f}\")\nw(f\"- Correlation(θ, total_score): {corr:.4f}\")\nw()\nw(\"This is a monotone transformation of the Rasch model sufficient statistic.\")\nw(\"Two binning strategies are compared:\")\nw(\"- **Equal-width (eq)**: equal intervals on the logit scale — respects IRT metric\")\nw(\"- **Quantile (qt)**: equal-count bins — ensures balanced strata\")\nw()\n\nw(\"## 3. Experimental Design\")\nw()\nw(f\"- Baseline items: {N_BASELINE}\")\nw(f\"- Contaminated per run: {N_CONTAMINATED}\")\nw(f\"- Injection probabilities: {INJECTION_PS}\")\nw(f\"- Seeds per p: {N_SEEDS}\")\nw(f\"- Strata counts tested: {STRATA_COUNTS}\")\nw()\nw(\"### Cohort definitions\")\nw()\nfor cn, cd in cohort_defs.items():\n    w(f\"- **{cn}**: ref N={len(cd['ref_idx'])}, foc N={len(cd['foc_idx'])}, \"\n      f\"foc inject N={len(cd['foc_inject_idx'])}\")\nw()\nw(\"### MH variants\")\nw()\nw(\"| Variant | Stratification | Description |\")\nw(\"|---------|---------------|-------------|\")\nfor ns in STRATA_COUNTS:\n    w(f\"| theta_eq_{ns} | Equal-width θ bins | {ns} equal intervals on logit scale |\")\n    w(f\"| theta_qt_{ns} | Quantile θ bins | {ns} equal-count bins on θ |\")\nw(\"| external_5 | Quantile total-score | 5 bins on full-matrix total (plan_011 baseline) |\")\nw()\n\n# ─── Results tables ───\nw(\"## 4. Semi-Synthetic Results\")\nw()\n\nfor cohort in [\"temporal\", \"ability\"]:\n    w(f\"### {cohort.capitalize()} cohort\")\n    w()\n\n    # Baseline FPR table\n    w(\"#### Baseline FPR (p=0)\")\n    w()\n    w(\"| Variant | FPR (mean±std) |\")\n    w(\"|---------|----------------|\")\n    sub = summary_df[(summary_df[\"p\"] == 0.0) & (summary_df[\"cohort_type\"] == cohort)]\n    for _, r in sub.sort_values(\"mh_variant\").iterrows():\n        w(f\"| {r.mh_variant} | {r.fpr_mean:.3f}±{r.fpr_std:.3f} |\")\n    w()\n\n    # Dose-response table (selected variants)\n    w(\"#### Dose-response (key variants)\")\n    w()\n    key_variants = [\"theta_eq_10\", \"theta_qt_10\", \"theta_qt_20\", \"external_5\"]\n    w(\"| Variant | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |\")\n    w(\"|---------|---|----------------|----------------|------|-----------|----------|\")\n    for variant in key_variants:\n        sub_v = summary_df[(summary_df[\"cohort_type\"] == cohort) & (summary_df[\"mh_variant\"] == variant)]\n        if len(sub_v) == 0:\n            continue\n        base_tpr = sub_v[sub_v[\"p\"] == 0.0][\"tpr_mean\"].values\n        base_tpr = base_tpr[0] if len(base_tpr) > 0 else 0\n        for _, r in sub_v.sort_values(\"p\").iterrows():\n            d_tpr = r.tpr_mean - base_tpr\n            w(f\"| {r.mh_variant} | {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | \"\n              f\"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {d_tpr:+.3f} | \"\n              f\"{r.fisher_or_mean:.2f} | {r.fisher_p_median:.2e} |\")\n    w()\n\n# ─── Success criteria ───\nw(\"## 5. Success Criteria Evaluation\")\nw()\nw(\"**Target**: baseline FPR < 0.10, TPR > 0.70 at p=0.5 (temporal cohort)\")\nw()\n\nfor variant in MH_VARIANTS:\n    sub = summary_df[(summary_df[\"cohort_type\"] == \"temporal\") & (summary_df[\"mh_variant\"] == variant)]\n    fpr0 = sub[sub[\"p\"] == 0.0][\"fpr_mean\"].values\n    tpr05 = sub[sub[\"p\"] == 0.5][\"tpr_mean\"].values\n    if len(fpr0) > 0 and len(tpr05) > 0:\n        fpr_ok = \"PASS\" if fpr0[0] < 0.10 else \"FAIL\"\n        tpr_ok = \"PASS\" if tpr05[0] > 0.70 else \"FAIL\"\n        w(f\"- **{variant}**: FPR={fpr0[0]:.3f} [{fpr_ok}], TPR@p=0.5={tpr05[0]:.3f} [{tpr_ok}]\")\nw()\n\n# ─── Enrichment ───\nw(\"## 6. Enrichment Against Li et al. Labels (No Injection)\")\nw()\nw(\"| Variant | Strata | Rate(contam) | Rate(clean) | Enrichment |\")\nw(\"|---------|--------|-------------|-------------|------------|\")\nfor _, r in enrichment_df.iterrows():\n    w(f\"| {r.mh_variant} | {r.strata_count} | {r.rate_contam:.4f} | \"\n      f\"{r.rate_clean:.4f} | {r.enrichment:.3f} |\")\nw()\nw(\"(plan_001 reference: enrichment = 0.96 with 5-strata total-score MH)\")\nw()\n\n# ─── Analysis ───\nw(\"## 7. Analysis & Conclusions\")\nw()\n\n# Find best variant\nbest_variant = None\nbest_fpr = 1.0\nfor variant in MH_VARIANTS:\n    sub = summary_df[(summary_df[\"cohort_type\"] == \"temporal\") &\n                     (summary_df[\"mh_variant\"] == variant) & (summary_df[\"p\"] == 0.0)]\n    if len(sub) > 0:\n        fpr = sub.iloc[0][\"fpr_mean\"]\n        if fpr < best_fpr:\n            best_fpr = fpr\n            best_variant = variant\n\next_sub = summary_df[(summary_df[\"cohort_type\"] == \"temporal\") &\n                     (summary_df[\"mh_variant\"] == \"external_5\") & (summary_df[\"p\"] == 0.0)]\next_fpr = ext_sub.iloc[0][\"fpr_mean\"] if len(ext_sub) > 0 else None\n\nw(\"### θ vs total-score stratification\")\nw()\nif ext_fpr is not None:\n    w(f\"- Plan_011 external (5 quantile strata, total score) FPR: {ext_fpr:.3f}\")\nw(f\"- Best θ variant ({best_variant}) FPR: {best_fpr:.3f}\")\nif ext_fpr is not None:\n    w(f\"- FPR difference: {best_fpr - ext_fpr:+.3f}\")\nw()\n\nw(\"### Equal-width vs quantile binning\")\nw()\nfor ns in STRATA_COUNTS:\n    eq_sub = summary_df[(summary_df[\"cohort_type\"] == \"temporal\") &\n                        (summary_df[\"mh_variant\"] == f\"theta_eq_{ns}\") & (summary_df[\"p\"] == 0.0)]\n    qt_sub = summary_df[(summary_df[\"cohort_type\"] == \"temporal\") &\n                        (summary_df[\"mh_variant\"] == f\"theta_qt_{ns}\") & (summary_df[\"p\"] == 0.0)]\n    if len(eq_sub) > 0 and len(qt_sub) > 0:\n        w(f\"- K={ns}: equal-width FPR={eq_sub.iloc[0]['fpr_mean']:.3f}, \"\n          f\"quantile FPR={qt_sub.iloc[0]['fpr_mean']:.3f}\")\nw()\n\nw(\"### Why FPR remains elevated\")\nw()\nw(\"Possible explanations if FPR stays high despite θ-conditioning:\")\nw(\"1. Real DIF exists between cohorts — genuine differential item functioning\")\nw(\"   (2023 vs 2024 models genuinely differ on certain items beyond overall ability)\")\nw(\"2. Cohorts differ on dimensions not captured by a single θ parameter\")\nw(\"   (e.g., training data composition, architecture effects)\")\nw(\"3. The logit(p) θ estimate has correlation >.999 with raw total scores,\")\nw(\"   so quantile bins on θ produce nearly identical strata to quantile bins on totals\")\nw(\"4. MH-DIF's power to distinguish real DIF from ability confounding is limited\")\nw(\"   when the grouping variable (year/quintile) correlates strongly with ability\")\nw()\n\nw(\"### Recommendations\")\nw()\nw(\"Based on these results:\")\nw()\nsub_t = summary_df[summary_df[\"cohort_type\"] == \"temporal\"]\nfor variant in [\"theta_eq_10\", \"theta_qt_10\", \"theta_qt_20\", \"external_5\"]:\n    v_sub = sub_t[sub_t[\"mh_variant\"] == variant]\n    fpr0 = v_sub[v_sub[\"p\"] == 0.0][\"fpr_mean\"].values\n    tpr05 = v_sub[v_sub[\"p\"] == 0.5][\"tpr_mean\"].values\n    tpr1 = v_sub[v_sub[\"p\"] == 1.0][\"tpr_mean\"].values\n    if len(fpr0) > 0 and len(tpr05) > 0 and len(tpr1) > 0:\n        w(f\"- {variant}: FPR₀={fpr0[0]:.3f}, TPR@0.5={tpr05[0]:.3f}, TPR@1.0={tpr1[0]:.3f}\")\nw()\n\n(OUT / \"plan_012_report.md\").write_text(\"\\n\".join(L) + \"\\n\")\nprint(\"  Report written to plan_012_report.md\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  CONSOLE SUMMARY\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n\" + \"=\" * 70)\nprint(\"SUMMARY — Baseline FPR (p=0)\")\nprint(\"=\" * 70)\nfor cohort in [\"temporal\", \"ability\"]:\n    print(f\"\\n  {cohort}:\")\n    sub = summary_df[(summary_df[\"p\"] == 0.0) & (summary_df[\"cohort_type\"] == cohort)]\n    for _, r in sub.sort_values(\"mh_variant\").iterrows():\n        print(f\"    {r.mh_variant:14s}: FPR={r.fpr_mean:.3f}±{r.fpr_std:.3f}\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"SUMMARY — TPR at p=0.5 (temporal)\")\nprint(\"=\" * 70)\nsub = summary_df[(summary_df[\"p\"] == 0.5) & (summary_df[\"cohort_type\"] == \"temporal\")]\nfor _, r in sub.sort_values(\"mh_variant\").iterrows():\n    print(f\"  {r.mh_variant:14s}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"SUMMARY — Enrichment (Li et al.)\")\nprint(\"=\" * 70)\nfor _, r in enrichment_df.iterrows():\n    print(f\"  {r.mh_variant:14s}: enrichment={r.enrichment:.3f}\")\n\ntotal_elapsed = time.time() - t_start\nprint(f\"\\nTotal time: {total_elapsed:.0f}s\")\nprint(f\"All outputs saved to {OUT}\")\n",
      "numLines": 713,
      "startLine": 1,
      "totalLines": 713
    }
  },
  "sourceToolAssistantUUID": "30ffd594-8221-46f6-b126-2ea67216ad1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## 任务：Bifactor IRT 拟合 + Bifactor-conditioned MH-DIF（plan_015，P0 最高优先）  ### 背景 plan_012 证明单维 IRT θ 与 total score 相关性 0.9986，无法降低 temporal cohort 31% baseline FPR。Director 指示尝试 bifactor IRT 作为最后的结构性方向：用…",
  "leafUuid": "70d4e4b0-5e8e-48ed-ae44-a4c02dbae742",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Bifactor IRT fitting with MH-DIF analysis",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4"
}
```

---

### Assistant

_source line 25 · 2026-05-20T22:26:12.542Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the plan_012 code. R is not available, so I'll implement the Python fallback: leave-one-out subject-specific θ estimation. Let me now check the item metadata to understand subject mapping, and look at what plan_011 code does as well.

Key changes for plan_015:
1. Instead of one global θ per model, compute per-subject θ scores
2. For DIF detection on items in subject X, use leave-one-out θ = mean of θ from all other subjects
3. This should break the near-perfect correlation between matching variable and total score


4. Run MH-DIF with these leave-one-out θ scores
5. Semi-synthetic with only temporal cohort, p=[0.0, 0.5, 1.0], 5 seeds

R isn't available and installing it would take too long, so I'll stick with the Python fallback approach. Now I'll write the main analysis script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70d4e4b0-5e8e-48ed-ae44-a4c02dbae742",
  "isSidechain": false,
  "requestId": "req_011CbEc8m2DDgETDgX3US4XY",
  "type": "assistant",
  "uuid": "d739bceb-7dc4-4b34-a7f3-0f35e6710752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeV9TvU3MQ3dcyrCRLwt8Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11990,
      "cache_read_input_tokens": 28047,
      "output_tokens": 622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 622,
          "cache_read_input_tokens": 28047,
          "cache_creation_input_tokens": 11990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11990
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

_source line 26 · 2026-05-20T22:26:13.602Z_

R 不可用，直接用 Python fallback（leave-one-out θ）。现在检查 item metadata 的 subject 列并开始写主脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d739bceb-7dc4-4b34-a7f3-0f35e6710752",
  "isSidechain": false,
  "requestId": "req_011CbEc8m2DDgETDgX3US4XY",
  "type": "assistant",
  "uuid": "24f5cf1c-f2a2-4096-8611-561d21c3ccf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeV9TvU3MQ3dcyrCRLwt8Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11990,
      "cache_read_input_tokens": 28047,
      "output_tokens": 622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 622,
          "cache_read_input_tokens": 28047,
          "cache_creation_input_tokens": 11990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11990
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

_source line 27 · 2026-05-20T22:26:17.456Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018NWfKkekqXbsNLA9kY5y2i`</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\nitems = pd.read_csv('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/item_metadata.csv')\nprint(items.columns.tolist())\nprint(items.head(3).to_string())\nprint()\nprint('Subject value counts (sorted):')\nsc = items['subject'].value_counts().sort_index()\nfor s, c in sc.items():\n    print(f'  {s}: {c}')\n\"",
  "description": "Check item metadata subject column"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24f5cf1c-f2a2-4096-8611-561d21c3ccf2",
  "isSidechain": false,
  "requestId": "req_011CbEc8m2DDgETDgX3US4XY",
  "type": "assistant",
  "uuid": "7c61038e-0e94-4a2f-94d2-db08f3949c8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeV9TvU3MQ3dcyrCRLwt8Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11990,
      "cache_read_input_tokens": 28047,
      "output_tokens": 622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 622,
          "cache_read_input_tokens": 28047,
          "cache_creation_input_tokens": 11990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11990
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

_source line 28 · 2026-05-20T22:26:18.418Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013ZeERfp3EzkRhfPUa6gE3p`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/ 2>/dev/null | head -20",
  "description": "Check plan_001 artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c61038e-0e94-4a2f-94d2-db08f3949c8b",
  "isSidechain": false,
  "requestId": "req_011CbEc8m2DDgETDgX3US4XY",
  "type": "assistant",
  "uuid": "df136e52-11a5-4326-83f9-48cff5991dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeV9TvU3MQ3dcyrCRLwt8Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11990,
      "cache_read_input_tokens": 28047,
      "output_tokens": 622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 622,
          "cache_read_input_tokens": 28047,
          "cache_creation_input_tokens": 11990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11990
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

_source line 29 · 2026-05-20T22:26:18.912Z_

<details><summary>↩ Tool result · `toolu_018NWfKkekqXbsNLA9kY5y2i`</summary>

```text
['item_id', 'subject', 'ctt_difficulty', 'ctt_discrimination', 'sd', 'is_negative_disc', 'empirical_p']
                item_id           subject  ctt_difficulty  ctt_discrimination        sd  is_negative_disc  empirical_p
0    abstract_algebra.1  abstract_algebra        0.141550           -0.283368  0.391334              True     0.188672
1   abstract_algebra.10  abstract_algebra        0.082918            0.190581  0.313614             False     0.110409
2  abstract_algebra.100  abstract_algebra        0.048573            0.060345  0.246131             False     0.064677

Subject value counts (sorted):
  abstract_algebra: 91
  anatomy: 122
  astronomy: 136
  business_ethics: 93
  clinical_knowledge: 241
  college_biology: 133
  college_chemistry: 81
  college_computer_science: 86
  college_mathematics: 72
  college_medicine: 161
  college_physics: 73
  computer_security: 87
  conceptual_physics: 202
  econometrics: 103
  electrical_engineering: 127
  elementary_mathematics: 317
  formal_logic: 109
  global_facts: 83
  high_school_biology: 290
  high_school_chemistry: 181
  high_school_computer_science: 96
  high_school_european_history: 155
  high_school_geography: 184
  high_school_government_and_politics: 189
  high_school_macroeconomics: 358
  high_school_mathematics: 197
  high_school_microeconomics: 220
  high_school_physics: 121
  high_school_psychology: 517
  high_school_statistics: 181
  high_school_us_history: 196
  high_school_world_history: 225
  human_aging: 203
  human_sexuality: 119
  international_law: 104
  jurisprudence: 101
  logical_fallacies: 151
  machine_learning: 87
  management: 92
  marketing: 225
  medical_genetics: 85
  miscellaneous: 745
  moral_disputes: 313
  moral_scenarios: 692
  nutrition: 282
  philosophy: 285
  prehistory: 296
  professional_accounting: 242
  professional_law: 1331
  professional_medicine: 248
  professional_psychology: 562
  public_relations: 98
  security_studies: 230
  sociology: 186
  us_foreign_policy: 96
  virology: 149
  world_religions: 159
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c61038e-0e94-4a2f-94d2-db08f3949c8b",
  "isSidechain": false,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "type": "user",
  "uuid": "94c2714d-7cff-40f8-bd80-d47e44402601",
  "toolUseResult": {
    "stdout": "['item_id', 'subject', 'ctt_difficulty', 'ctt_discrimination', 'sd', 'is_negative_disc', 'empirical_p']\n                item_id           subject  ctt_difficulty  ctt_discrimination        sd  is_negative_disc  empirical_p\n0    abstract_algebra.1  abstract_algebra        0.141550           -0.283368  0.391334              True     0.188672\n1   abstract_algebra.10  abstract_algebra        0.082918            0.190581  0.313614             False     0.110409\n2  abstract_algebra.100  abstract_algebra        0.048573            0.060345  0.246131             False     0.064677\n\nSubject value counts (sorted):\n  abstract_algebra: 91\n  anatomy: 122\n  astronomy: 136\n  business_ethics: 93\n  clinical_knowledge: 241\n  college_biology: 133\n  college_chemistry: 81\n  college_computer_science: 86\n  college_mathematics: 72\n  college_medicine: 161\n  college_physics: 73\n  computer_security: 87\n  conceptual_physics: 202\n  econometrics: 103\n  electrical_engineering: 127\n  elementary_mathematics: 317\n  formal_logic: 109\n  global_facts: 83\n  high_school_biology: 290\n  high_school_chemistry: 181\n  high_school_computer_science: 96\n  high_school_european_history: 155\n  high_school_geography: 184\n  high_school_government_and_politics: 189\n  high_school_macroeconomics: 358\n  high_school_mathematics: 197\n  high_school_microeconomics: 220\n  high_school_physics: 121\n  high_school_psychology: 517\n  high_school_statistics: 181\n  high_school_us_history: 196\n  high_school_world_history: 225\n  human_aging: 203\n  human_sexuality: 119\n  international_law: 104\n  jurisprudence: 101\n  logical_fallacies: 151\n  machine_learning: 87\n  management: 92\n  marketing: 225\n  medical_genetics: 85\n  miscellaneous: 745\n  moral_disputes: 313\n  moral_scenarios: 692\n  nutrition: 282\n  philosophy: 285\n  prehistory: 296\n  professional_accounting: 242\n  professional_law: 1331\n  professional_medicine: 248\n  professional_psychology: 562\n  public_relations: 98\n  security_studies: 230\n  sociology: 186\n  us_foreign_policy: 96\n  virology: 149\n  world_religions: 159",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7c61038e-0e94-4a2f-94d2-db08f3949c8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T22:26:19.057Z_

<details><summary>↩ Tool result · `toolu_013ZeERfp3EzkRhfPUa6gE3p`</summary>

```text
cross_analysis.csv
dif_results_ability.csv
dif_results_temporal.csv
dif_summary.csv
domain_specificity.csv
neg_disc_sensitivity.csv
plan_001_analysis.py
plan_001_report.md
within_family_dif.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df136e52-11a5-4326-83f9-48cff5991dfd",
  "isSidechain": false,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "type": "user",
  "uuid": "d21a9fec-3c85-4d6b-b966-dd167720d943",
  "toolUseResult": {
    "stdout": "cross_analysis.csv\ndif_results_ability.csv\ndif_results_temporal.csv\ndif_summary.csv\ndomain_specificity.csv\nneg_disc_sensitivity.csv\nplan_001_analysis.py\nplan_001_report.md\nwithin_family_dif.csv",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "df136e52-11a5-4326-83f9-48cff5991dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T22:26:19.065Z_

```json
{
  "parentUuid": "d21a9fec-3c85-4d6b-b966-dd167720d943",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f2596e9d-5c9b-458e-8a1f-fcd91197ea0f",
  "timestamp": "2026-05-20T22:26:19.065Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 32 · 2026-05-20T22:26:22.051Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WeysJrm6tnccCnoJpf8iRz`</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2596e9d-5c9b-458e-8a1f-fcd91197ea0f",
  "isSidechain": false,
  "requestId": "req_011CbEcA1JivNo4WB3PFu2go",
  "type": "assistant",
  "uuid": "80f4bf88-2959-4bfe-8908-0ba735d69bf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UT2fxETJF4bnXdXHbUpChZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1532,
      "cache_read_input_tokens": 40037,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1532,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 40037,
          "cache_creation_input_tokens": 1532,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1532
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

_source line 33 · 2026-05-20T22:26:22.060Z_

<details><summary>↩ Tool result · `toolu_01WeysJrm6tnccCnoJpf8iRz`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80f4bf88-2959-4bfe-8908-0ba735d69bf1",
  "isSidechain": false,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "type": "user",
  "uuid": "3f409585-e6d9-4516-8721-cb655836467c",
  "toolUseResult": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "80f4bf88-2959-4bfe-8908-0ba735d69bf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T22:26:28.741Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_0164cexBXu7XTRiwwvVCquZp`</summary>

```json
{
  "todos": [
    {
      "content": "Write plan_015_bifactor_analysis.py (leave-one-out θ + MH-DIF + semi-synthetic + diagnostics)",
      "status": "in_progress",
      "activeForm": "Writing plan_015 main analysis script"
    },
    {
      "content": "Run the analysis script",
      "status": "pending",
      "activeForm": "Running plan_015 analysis"
    },
    {
      "content": "Write plan_015_report.md from results",
      "status": "pending",
      "activeForm": "Writing plan_015 report"
    },
    {
      "content": "Register all artifacts",
      "status": "pending",
      "activeForm": "Registering artifacts"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f409585-e6d9-4516-8721-cb655836467c",
  "isSidechain": false,
  "requestId": "req_011CbEcAEM3c7hopKBbXcsVP",
  "type": "assistant",
  "uuid": "256c04c3-1366-40b5-95dd-8c66d925bda8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6xwxAckxBoR8dW2PrXHG2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2466,
      "cache_read_input_tokens": 41569,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 41569,
          "cache_creation_input_tokens": 2466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2466
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

_source line 35 · 2026-05-20T22:26:28.750Z_

<details><summary>↩ Tool result · `toolu_0164cexBXu7XTRiwwvVCquZp`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "256c04c3-1366-40b5-95dd-8c66d925bda8",
  "isSidechain": false,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "type": "user",
  "uuid": "ee3d8cff-cb91-428b-8205-5c8c569e1a23",
  "toolUseResult": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Write plan_015_bifactor_analysis.py (leave-one-out θ + MH-DIF + semi-synthetic + diagnostics)",
        "status": "in_progress",
        "activeForm": "Writing plan_015 main analysis script"
      },
      {
        "content": "Run the analysis script",
        "status": "pending",
        "activeForm": "Running plan_015 analysis"
      },
      {
        "content": "Write plan_015_report.md from results",
        "status": "pending",
        "activeForm": "Writing plan_015 report"
      },
      {
        "content": "Register all artifacts",
        "status": "pending",
        "activeForm": "Registering artifacts"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "256c04c3-1366-40b5-95dd-8c66d925bda8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-20T22:26:31.562Z_

Now creating the output directory and writing the main analysis script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee3d8cff-cb91-428b-8205-5c8c569e1a23",
  "isSidechain": false,
  "requestId": "req_011CbEcAivm5hTVFwgw7s1Tv",
  "type": "assistant",
  "uuid": "b58a1fcc-a818-4f4c-81af-330d9a3ffba3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YF5LvbpvKizA8NGiagzN4D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 248,
      "cache_read_input_tokens": 44035,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 248,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 44035,
          "cache_creation_input_tokens": 248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 248
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

_source line 37 · 2026-05-20T22:26:33.491Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014vD4RgB5Cdbepg1wPdVVuJ`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_015",
  "description": "Create plan_015 output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b58a1fcc-a818-4f4c-81af-330d9a3ffba3",
  "isSidechain": false,
  "requestId": "req_011CbEcAivm5hTVFwgw7s1Tv",
  "type": "assistant",
  "uuid": "1b9119f7-9804-4461-abe6-f2207f385d4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YF5LvbpvKizA8NGiagzN4D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 248,
      "cache_read_input_tokens": 44035,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 248,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 44035,
          "cache_creation_input_tokens": 248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 248
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

_source line 38 · 2026-05-20T22:26:33.627Z_

<details><summary>↩ Tool result · `toolu_014vD4RgB5Cdbepg1wPdVVuJ`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b9119f7-9804-4461-abe6-f2207f385d4f",
  "isSidechain": false,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "type": "user",
  "uuid": "1bf32c03-ea65-42fa-8214-69a56501b3b2",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "1b9119f7-9804-4461-abe6-f2207f385d4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T22:29:46.373Z_

<details open><summary>🔧 Tool call — Write · `toolu_01JBMAt9LRLZko31wE83W3NL`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_015/plan_015_bifactor_analysis.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nplan_015_bifactor_analysis.py — Bifactor-conditioned MH-DIF Analysis\n\nR bfactor() unavailable; uses Python fallback: per-subject IRT θ with\nleave-one-out matching. For DIF detection on items in subject X, the matching\nvariable is the mean θ across all other 56 subjects — removing the target\nsubject's signal from the matching variable.\n\nSteps:\n  1. Per-subject θ estimation (logit of subject-specific proportion correct)\n  2. Leave-one-out θ construction\n  3. MH-DIF on real data (temporal cohort) with LOO-θ stratification\n  4. Semi-synthetic injection (temporal only, p=[0.0, 0.5, 1.0], 5 seeds)\n  5. Diagnostics: LOO-θ vs total score correlation, inter-subject θ correlations\n\nOutputs in plan_015/:\n  bifactor_general_theta.csv, bifactor_dif_results.csv,\n  bifactor_dose_response.csv, bifactor_fit_diagnostics.csv,\n  plan_015_report.md\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist, fisher_exact, pearsonr\nfrom pathlib import Path\nimport time\nimport warnings\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_015\"\nOUT.mkdir(exist_ok=True)\n\nINJECTION_PS = [0.0, 0.5, 1.0]\nN_SEEDS = 5\nN_BASELINE = 500\nN_CONTAMINATED = 100\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE (from plan_012)\n# ════════════════════════════════════════════════════════════════════════════\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\")\n\n\ndef _compute_mh_item(X_ref_j, X_foc_j, k_ref, k_foc, n_bins):\n    R = S = 0.0\n    sum_diff = 0.0\n    sum_var = 0.0\n    pr = ps_qr = qs = 0.0\n    n_ok = 0\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1 = int(mr.sum())\n        n0 = int(mf.sum())\n        if n1 == 0 or n0 == 0:\n            continue\n\n        A = float(X_ref_j[mr].sum())\n        B = float(n1 - A)\n        C = float(X_foc_j[mf].sum())\n        D = float(n0 - C)\n        Nk = float(n1 + n0)\n        m1 = A + C\n        m0 = B + D\n\n        if m1 == 0 or m0 == 0 or Nk <= 1:\n            continue\n        n_ok += 1\n\n        Rk = A * D / Nk\n        Sk = B * C / Nk\n        R += Rk\n        S += Sk\n\n        EA = n1 * m1 / Nk\n        sum_diff += A - EA\n        sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n        Pk = (A + D) / Nk\n        Qk = (B + C) / Nk\n        pr += Pk * Rk\n        ps_qr += Pk * Sk + Qk * Rk\n        qs += Qk * Sk\n\n    if n_ok == 0 or (R == 0 and S == 0):\n        return None\n\n    if S == 0:\n        alpha, delta, se = np.inf, -np.inf, np.nan\n    elif R == 0:\n        alpha, delta, se = 0.0, np.inf, np.nan\n    else:\n        alpha = R / S\n        delta = -2.35 * np.log(alpha)\n        v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n        se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n    if sum_var > 0:\n        chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n        pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n    else:\n        chi2_stat = pval = np.nan\n\n    ad = abs(delta) if np.isfinite(delta) else np.inf\n    if ad < 1.0:\n        ets = \"A\"\n    elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n        ets = \"C\"\n    else:\n        ets = \"B\"\n\n    return dict(alpha_mh=alpha, delta_mh=delta, se=se,\n                chi2=chi2_stat, p_value=pval, ets_class=ets)\n\n\ndef mh_dif_with_bins(X_ref, X_foc, scores_ref, scores_foc, n_strata, bin_mode=\"quantile\"):\n    J = X_ref.shape[1]\n    s_all = np.concatenate([scores_ref, scores_foc])\n\n    if bin_mode == \"equal\":\n        edges = np.linspace(s_all.min() - 0.001, s_all.max() + 0.001, n_strata + 1)\n        n_bins = n_strata\n    else:\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        n_bins = len(edges) - 1\n\n    if n_bins < 2:\n        return pd.DataFrame([_nan_row(j) for j in range(J)])\n\n    k_ref = np.digitize(scores_ref, edges[1:-1])\n    k_foc = np.digitize(scores_foc, edges[1:-1])\n\n    rows = []\n    for j in range(J):\n        result = _compute_mh_item(X_ref[:, j], X_foc[:, j], k_ref, k_foc, n_bins)\n        if result is None:\n            rows.append(_nan_row(j))\n        else:\n            result[\"col_idx\"] = j\n            rows.append(result)\n\n    return pd.DataFrame(rows)\n\n\ndef mh_dif_per_item_scores(X_ref, X_foc, scores_ref_per_item, scores_foc_per_item,\n                            n_strata=10, bin_mode=\"quantile\"):\n    \"\"\"MH-DIF where each item j has its own matching scores (for LOO-θ).\"\"\"\n    J = X_ref.shape[1]\n    rows = []\n\n    for j in range(J):\n        sr = scores_ref_per_item[:, j]\n        sf = scores_foc_per_item[:, j]\n        s_all = np.concatenate([sr, sf])\n\n        if bin_mode == \"equal\":\n            edges = np.linspace(s_all.min() - 0.001, s_all.max() + 0.001, n_strata + 1)\n            n_bins = n_strata\n        else:\n            edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n            n_bins = len(edges) - 1\n\n        if n_bins < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        k_ref = np.digitize(sr, edges[1:-1])\n        k_foc = np.digitize(sf, edges[1:-1])\n\n        result = _compute_mh_item(X_ref[:, j], X_foc[:, j], k_ref, k_foc, n_bins)\n        if result is None:\n            rows.append(_nan_row(j))\n        else:\n            result[\"col_idx\"] = j\n            rows.append(result)\n\n    return pd.DataFrame(rows)\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"=== Loading data ===\")\nmat = load_npz(BASE / \"response_matrix.npz\")\nidx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\nMODEL_NAMES = idx[\"model_names\"]\nITEM_IDS = idx[\"item_ids\"]\nITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}\n\nmodel_meta = pd.read_csv(BASE / \"model_metadata.csv\")\nitem_meta = pd.read_csv(BASE / \"item_metadata.csv\")\nli_labels = pd.read_csv(BASE / \"mmlu_li2024_proxy_labels.csv\")\nability_dif = pd.read_csv(BASE / \"plan_001\" / \"dif_results_ability.csv\")\n\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\nN_MODELS, J_FULL = mat.shape\nprint(f\"  Matrix: {N_MODELS} x {J_FULL}\")\n\nsubjects = sorted(item_meta[\"subject\"].unique())\nN_SUBJECTS = len(subjects)\nSUBJ2IDX = {s: i for i, s in enumerate(subjects)}\nprint(f\"  Subjects: {N_SUBJECTS}\")\n\nitem_subject_col = np.array([SUBJ2IDX[item_meta.loc[item_meta[\"item_id\"] == iid, \"subject\"].values[0]]\n                              for iid in ITEM_IDS])\n\n# Pre-build: for each subject, which column indices belong to it\nsubject_col_indices = {}\nfor si, s in enumerate(subjects):\n    s_items = item_meta[item_meta[\"subject\"] == s][\"item_id\"].values\n    cols = np.array([ITEM2COL[iid] for iid in s_items if iid in ITEM2COL])\n    subject_col_indices[si] = cols\n\nprint(f\"  Items per subject: min={min(len(v) for v in subject_col_indices.values())}, \"\n      f\"max={max(len(v) for v in subject_col_indices.values())}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 1: PER-SUBJECT θ ESTIMATION\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 1: Per-subject θ estimation ===\")\nt0 = time.time()\n\n# theta_subject[model_i, subject_j] = logit(p_correct on subject j)\ntheta_subject = np.zeros((N_MODELS, N_SUBJECTS), dtype=np.float64)\n\nfor si in range(N_SUBJECTS):\n    cols = subject_col_indices[si]\n    n_items_s = len(cols)\n    submat = mat[:, cols]\n    totals_s = np.asarray(submat.sum(axis=1)).ravel().astype(np.float64)\n    p_s = (totals_s + 0.5) / (n_items_s + 1.0)\n    theta_subject[:, si] = np.log(p_s / (1.0 - p_s))\n\nprint(f\"  Per-subject θ matrix: {theta_subject.shape} ({time.time()-t0:.1f}s)\")\nprint(f\"  θ range: [{theta_subject.min():.3f}, {theta_subject.max():.3f}]\")\nprint(f\"  Mean across subjects: {theta_subject.mean(axis=0).mean():.3f}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 2: LEAVE-ONE-OUT θ CONSTRUCTION\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 2: Leave-one-out θ construction ===\")\n\n# For each item in subject X, the LOO-θ = mean of θ across all subjects != X\n# Pre-compute sum of all subject θ per model\ntheta_sum = theta_subject.sum(axis=1)  # (N_MODELS,)\n\n# LOO-θ for items in subject si: (theta_sum - theta_subject[:, si]) / (N_SUBJECTS - 1)\n# This gives a different matching score per subject, but same for all items within a subject\n\n# For the full matrix: build per-item LOO-θ\n# loo_theta[model_i, item_j] = mean θ over subjects != subject(item_j)\n# Since all items in the same subject share the same LOO-θ, we can be efficient\n\nloo_theta_by_subject = np.zeros((N_MODELS, N_SUBJECTS), dtype=np.float64)\nfor si in range(N_SUBJECTS):\n    loo_theta_by_subject[:, si] = (theta_sum - theta_subject[:, si]) / (N_SUBJECTS - 1)\n\n# Global θ for comparison (mean of all subject θ)\nglobal_theta = theta_subject.mean(axis=1)\n\n# Total score for comparison\ntotals_all = np.asarray(mat.sum(axis=1)).ravel().astype(np.float64)\ntheta_logit_global = np.log((totals_all + 0.5) / (J_FULL + 1.0 - totals_all - 0.5))\n\n# Correlation diagnostics\ncorr_loo_total = []\nfor si in range(N_SUBJECTS):\n    r, _ = pearsonr(loo_theta_by_subject[:, si], totals_all)\n    corr_loo_total.append(r)\ncorr_loo_total = np.array(corr_loo_total)\n\ncorr_global_total, _ = pearsonr(global_theta, totals_all)\ncorr_logit_total, _ = pearsonr(theta_logit_global, totals_all)\n\nprint(f\"  LOO-θ by subject shape: {loo_theta_by_subject.shape}\")\nprint(f\"  Corr(global_mean_θ, total_score): {corr_global_total:.6f}\")\nprint(f\"  Corr(logit_global_θ, total_score): {corr_logit_total:.6f}\")\nprint(f\"  Corr(LOO-θ, total_score): mean={corr_loo_total.mean():.6f}, \"\n      f\"min={corr_loo_total.min():.6f}, max={corr_loo_total.max():.6f}\")\n\n# Save theta estimates\ntheta_out = pd.DataFrame({\n    \"model_name\": MODEL_NAMES,\n    \"general_theta\": global_theta,\n    \"total_score\": totals_all,\n    \"method\": \"leave-one-out\"\n})\ntheta_out.to_csv(OUT / \"bifactor_general_theta.csv\", index=False)\nprint(f\"  Saved bifactor_general_theta.csv\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 3: DEFINE COHORTS (temporal only)\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 3: Defining temporal cohort ===\")\n\n\ndef get_row_indices(col, values):\n    names = model_meta.loc[model_meta[col].isin(values), \"model_name\"]\n    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])\n\n\nref_temporal_idx = get_row_indices(\"cohort_temporal\", [\"2023\"])\nfoc_temporal_idx = get_row_indices(\"cohort_temporal\", [\"2024\"])\n\nref_t_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\nfoc_t_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"accuracy\"]\nt_overlap_min = max(ref_t_acc.min(), foc_t_acc.min())\nt_overlap_max = min(ref_t_acc.max(), foc_t_acc.max())\n\nfoc_t_inject_mask = (\n    (model_meta[\"cohort_temporal\"] == \"2024\") &\n    (model_meta[\"accuracy\"] >= t_overlap_min) &\n    (model_meta[\"accuracy\"] <= t_overlap_max)\n)\nfoc_t_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_t_inject_mask, \"model_name\"]\n                              if n in NAME2ROW])\n\nprint(f\"  Temporal: ref={len(ref_temporal_idx)} (2023), foc={len(foc_temporal_idx)} (2024)\")\nprint(f\"  Inject subset: {len(foc_t_inject_idx)} focal models in accuracy overlap\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 4: REAL DATA DIF — ALL ITEMS WITH LOO-θ\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 4: Real data DIF with LOO-θ (all 12508 items) ===\")\nt0 = time.time()\n\nX_full_dense = mat.toarray().astype(np.int8)\nX_ref_full = X_full_dense[ref_temporal_idx]\nX_foc_full = X_full_dense[foc_temporal_idx]\n\n# Build per-item LOO-θ for ref and foc\n# For item j in subject si: LOO-θ = loo_theta_by_subject[:, si]\n# scores_ref_per_item[model, item] = LOO-θ for that item's subject\nscores_ref_loo = np.zeros((len(ref_temporal_idx), J_FULL), dtype=np.float64)\nscores_foc_loo = np.zeros((len(foc_temporal_idx), J_FULL), dtype=np.float64)\n\nfor si in range(N_SUBJECTS):\n    cols = subject_col_indices[si]\n    scores_ref_loo[:, cols] = loo_theta_by_subject[ref_temporal_idx][:, si:si+1]\n    scores_foc_loo[:, cols] = loo_theta_by_subject[foc_temporal_idx][:, si:si+1]\n\nprint(f\"  Built per-item LOO scores ({time.time()-t0:.1f}s)\")\n\n# Run MH-DIF with per-item LOO-θ\ndif_all_loo = mh_dif_per_item_scores(X_ref_full, X_foc_full,\n                                      scores_ref_loo, scores_foc_loo,\n                                      n_strata=10, bin_mode=\"quantile\")\ndif_all_loo[\"item_id\"] = ITEM_IDS[dif_all_loo[\"col_idx\"].values]\n\n# Also run with external_5 (plan_012 baseline) for comparison\next_ref = totals_all[ref_temporal_idx]\next_foc = totals_all[foc_temporal_idx]\ndif_all_ext = mh_dif_with_bins(X_ref_full, X_foc_full, ext_ref, ext_foc,\n                                n_strata=5, bin_mode=\"quantile\")\ndif_all_ext[\"item_id\"] = ITEM_IDS[dif_all_ext[\"col_idx\"].values]\n\n# Also run with global mean θ (10 quantile bins) for comparison\nglobal_ref = global_theta[ref_temporal_idx]\nglobal_foc = global_theta[foc_temporal_idx]\ndif_all_global = mh_dif_with_bins(X_ref_full, X_foc_full, global_ref, global_foc,\n                                   n_strata=10, bin_mode=\"quantile\")\ndif_all_global[\"item_id\"] = ITEM_IDS[dif_all_global[\"col_idx\"].values]\n\nelapsed = time.time() - t0\nprint(f\"  DIF computed for all items ({elapsed:.0f}s)\")\n\n# Merge with Li labels for enrichment\nli_set = set(li_labels[\"item_id\"].values)\nfor label, dif_df in [(\"loo_theta_10\", dif_all_loo),\n                       (\"external_5\", dif_all_ext),\n                       (\"global_theta_10\", dif_all_global)]:\n    li_merged = dif_df[dif_df[\"item_id\"].isin(li_set)].merge(\n        li_labels[[\"item_id\", \"is_contaminated\"]], on=\"item_id\"\n    )\n    is_contam = li_merged[\"is_contaminated\"] == 1\n    is_clean = ~is_contam\n    is_c = li_merged[\"ets_class\"] == \"C\"\n\n    rate_contam = (is_c & is_contam).sum() / is_contam.sum() if is_contam.sum() > 0 else 0\n    rate_clean = (is_c & is_clean).sum() / is_clean.sum() if is_clean.sum() > 0 else 0\n    enrichment = rate_contam / rate_clean if rate_clean > 0 else np.inf\n    n_c = is_c.sum()\n    pct_c = n_c / len(li_merged) * 100\n\n    print(f\"  {label:20s}: {n_c:4d} ETS-C ({pct_c:.1f}%), \"\n          f\"rate_contam={rate_contam:.4f}, rate_clean(FPR)={rate_clean:.4f}, \"\n          f\"enrichment={enrichment:.3f}\")\n\n# Save real-data DIF results\ndif_all_loo[\"variant\"] = \"loo_theta_10\"\ndif_all_ext[\"variant\"] = \"external_5\"\ndif_all_global[\"variant\"] = \"global_theta_10\"\ndif_combined = pd.concat([dif_all_loo, dif_all_ext, dif_all_global], ignore_index=True)\ndif_combined.to_csv(OUT / \"bifactor_dif_results.csv\", index=False)\nprint(f\"  Saved bifactor_dif_results.csv ({len(dif_combined)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 5: SELECT BASELINE ITEMS FOR SEMI-SYNTHETIC\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 5: Selecting baseline items ===\")\nmerged_bl = ability_dif.merge(li_labels[[\"item_id\", \"contamination_type\"]], on=\"item_id\", how=\"inner\")\nbaseline_pool = merged_bl[(merged_bl[\"contamination_type\"] == \"clean\") & (merged_bl[\"ets_class\"] == \"A\")]\nprint(f\"  Baseline pool (clean + ETS A): {len(baseline_pool)}\")\n\nbaseline_items = baseline_pool.sample(N_BASELINE, random_state=42)\nbaseline_item_ids = baseline_items[\"item_id\"].values\nbaseline_col_indices = np.array([ITEM2COL[iid] for iid in baseline_item_ids])\n\n# Map each baseline item to its subject index\nbaseline_subject_idx = np.array([item_subject_col[ci] for ci in baseline_col_indices])\nprint(f\"  Selected {N_BASELINE} baseline items across \"\n      f\"{len(np.unique(baseline_subject_idx))} subjects\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 6: SEMI-SYNTHETIC INJECTION + LOO-θ MH-DIF\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 6: Semi-synthetic injection + MH-DIF ===\")\n\nX_base = mat[:, baseline_col_indices].toarray().astype(np.int8)\n\n# Pre-compute LOO-θ for baseline items\n# For baseline item at local index j (in subject si):\n#   LOO-θ = loo_theta_by_subject[:, si]\n# But we need to handle injection: when we flip responses in subject X,\n# the LOO-θ should remain unchanged (it excludes subject X)\n\n# Build per-baseline-item LOO-θ for ref and foc\nloo_ref_base = np.zeros((len(ref_temporal_idx), N_BASELINE), dtype=np.float64)\nloo_foc_base = np.zeros((len(foc_temporal_idx), N_BASELINE), dtype=np.float64)\nfor j in range(N_BASELINE):\n    si = baseline_subject_idx[j]\n    loo_ref_base[:, j] = loo_theta_by_subject[ref_temporal_idx, si]\n    loo_foc_base[:, j] = loo_theta_by_subject[foc_temporal_idx, si]\n\n# Also pre-compute external scores\next_ref_bl = totals_all[ref_temporal_idx]\next_foc_bl = totals_all[foc_temporal_idx]\nglobal_ref_bl = global_theta[ref_temporal_idx]\nglobal_foc_bl = global_theta[foc_temporal_idx]\n\nMH_VARIANTS = [\"loo_theta_10\", \"global_theta_10\", \"external_5\"]\ninjection_rows = []\ntotal_runs = len(INJECTION_PS) * N_SEEDS * len(MH_VARIANTS)\nrun_count = 0\nt_start = time.time()\n\nfor p in INJECTION_PS:\n    for seed in range(1, N_SEEDS + 1):\n        rng = np.random.RandomState(seed)\n        contam_local_idx = rng.choice(N_BASELINE, N_CONTAMINATED, replace=False)\n        contam_set = set(contam_local_idx.tolist())\n\n        X_inj = X_base.copy()\n        n_flipped = 0\n\n        if p > 0:\n            for local_j in contam_local_idx:\n                for model_row in foc_t_inject_idx:\n                    if X_inj[model_row, local_j] == 0:\n                        if rng.random() < p:\n                            X_inj[model_row, local_j] = 1\n                            n_flipped += 1\n\n        X_ref_inj = X_inj[ref_temporal_idx]\n        X_foc_inj = X_inj[foc_temporal_idx]\n\n        for variant in MH_VARIANTS:\n            run_count += 1\n\n            if variant == \"loo_theta_10\":\n                dif_results = mh_dif_per_item_scores(\n                    X_ref_inj, X_foc_inj,\n                    loo_ref_base, loo_foc_base,\n                    n_strata=10, bin_mode=\"quantile\"\n                )\n            elif variant == \"global_theta_10\":\n                dif_results = mh_dif_with_bins(\n                    X_ref_inj, X_foc_inj,\n                    global_ref_bl, global_foc_bl,\n                    n_strata=10, bin_mode=\"quantile\"\n                )\n            elif variant == \"external_5\":\n                dif_results = mh_dif_with_bins(\n                    X_ref_inj, X_foc_inj,\n                    ext_ref_bl, ext_foc_bl,\n                    n_strata=5, bin_mode=\"quantile\"\n                )\n\n            contam_mask = dif_results[\"col_idx\"].isin(contam_set)\n            contam_results = dif_results[contam_mask]\n            clean_results = dif_results[~contam_mask]\n\n            n_c_contam = (contam_results[\"ets_class\"] == \"C\").sum()\n            n_c_clean = (clean_results[\"ets_class\"] == \"C\").sum()\n            tpr = n_c_contam / N_CONTAMINATED\n            fpr = n_c_clean / (N_BASELINE - N_CONTAMINATED)\n\n            table = [[n_c_contam, N_CONTAMINATED - n_c_contam],\n                     [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]\n            fisher_or, fisher_p = fisher_exact(table)\n\n            injection_rows.append(dict(\n                p=p, seed=seed, cohort_type=\"temporal\",\n                mh_variant=variant,\n                tpr=tpr, fpr=fpr,\n                fisher_or=fisher_or, fisher_p=fisher_p,\n                n_responses_flipped=n_flipped,\n            ))\n\n            elapsed = time.time() - t_start\n            print(f\"  [{run_count}/{total_runs}] {variant:20s} p={p} seed={seed}: \"\n                  f\"TPR={tpr:.3f} FPR={fpr:.3f} ({elapsed:.0f}s)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 7: AGGREGATE & SAVE\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 7: Aggregating results ===\")\n\ninj_df = pd.DataFrame(injection_rows)\n\nsummary_rows = []\nfor (p_val, variant), grp in inj_df.groupby([\"p\", \"mh_variant\"]):\n    summary_rows.append(dict(\n        p=p_val, cohort_type=\"temporal\", mh_variant=variant,\n        tpr_mean=grp[\"tpr\"].mean(), tpr_std=grp[\"tpr\"].std(),\n        fpr_mean=grp[\"fpr\"].mean(), fpr_std=grp[\"fpr\"].std(),\n        fisher_or_mean=grp[\"fisher_or\"].mean(),\n        fisher_p_median=grp[\"fisher_p\"].median(),\n    ))\nsummary_df = pd.DataFrame(summary_rows)\n\ninj_df.to_csv(OUT / \"bifactor_injection_results.csv\", index=False)\nsummary_df.to_csv(OUT / \"bifactor_dose_response.csv\", index=False)\nprint(f\"  Saved bifactor_injection_results.csv ({len(inj_df)} rows)\")\nprint(f\"  Saved bifactor_dose_response.csv ({len(summary_df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 8: DIAGNOSTICS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 8: Fit diagnostics ===\")\n\n# 1. LOO-θ vs total score correlation per subject\ndiag_rows = []\nfor si, s in enumerate(subjects):\n    r_loo, _ = pearsonr(loo_theta_by_subject[:, si], totals_all)\n    r_subj, _ = pearsonr(theta_subject[:, si], totals_all)\n    diag_rows.append(dict(\n        subject=s,\n        n_items=len(subject_col_indices[si]),\n        corr_loo_total=r_loo,\n        corr_subject_theta_total=r_subj,\n        loo_theta_mean=loo_theta_by_subject[:, si].mean(),\n        loo_theta_std=loo_theta_by_subject[:, si].std(),\n        subject_theta_mean=theta_subject[:, si].mean(),\n        subject_theta_std=theta_subject[:, si].std(),\n    ))\ndiag_df = pd.DataFrame(diag_rows)\n\n# 2. Inter-subject θ correlation matrix summary\ntheta_corr_mat = np.corrcoef(theta_subject.T)\nupper_tri = theta_corr_mat[np.triu_indices(N_SUBJECTS, k=1)]\n\ndiag_summary = {\n    \"method\": \"leave-one-out\",\n    \"n_subjects\": N_SUBJECTS,\n    \"n_models\": N_MODELS,\n    \"n_items\": J_FULL,\n    \"corr_global_theta_total\": corr_global_total,\n    \"corr_logit_theta_total\": corr_logit_total,\n    \"corr_loo_total_mean\": corr_loo_total.mean(),\n    \"corr_loo_total_min\": corr_loo_total.min(),\n    \"corr_loo_total_max\": corr_loo_total.max(),\n    \"inter_subject_corr_mean\": upper_tri.mean(),\n    \"inter_subject_corr_min\": upper_tri.min(),\n    \"inter_subject_corr_max\": upper_tri.max(),\n    \"inter_subject_corr_std\": upper_tri.std(),\n}\n\nprint(f\"  Inter-subject θ correlations: mean={upper_tri.mean():.4f}, \"\n      f\"min={upper_tri.min():.4f}, max={upper_tri.max():.4f}\")\nprint(f\"  Corr(LOO-θ, total): mean={corr_loo_total.mean():.6f}, \"\n      f\"range=[{corr_loo_total.min():.6f}, {corr_loo_total.max():.6f}]\")\n\ndiag_df.to_csv(OUT / \"bifactor_fit_diagnostics.csv\", index=False)\npd.DataFrame([diag_summary]).to_csv(OUT / \"bifactor_fit_diagnostics_summary.csv\", index=False)\nprint(f\"  Saved bifactor_fit_diagnostics.csv ({len(diag_df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  REPORT\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Generating report ===\")\n\nL = []\ndef w(s=\"\"):\n    L.append(s)\n\nw(\"# Plan 015: Bifactor-conditioned MH-DIF Analysis\")\nw()\nw(\"## 1. Background & Motivation\")\nw()\nw(\"Plan 012 showed that unidimensional IRT θ correlates 0.9986 with total score,\")\nw(\"producing nearly identical MH strata and failing to reduce temporal cohort\")\nw(\"baseline FPR (~31%). This plan tests a **multidimensional** approach:\")\nw(\"decompose ability into 57 subject-specific factors, then use **leave-one-out θ**\")\nw(\"(mean ability across all subjects *except* the target item's subject) as the\")\nw(\"MH matching variable.\")\nw()\nw(\"**Rationale**: If contamination is subject-specific (e.g., 2024 models are\")\nw(\"disproportionately trained on certain MMLU subjects), the LOO-θ excludes the\")\nw(\"contaminated signal while preserving legitimate ability matching.\")\nw()\n\nw(\"## 2. Method\")\nw()\nw(\"### 2.1 Per-subject θ estimation\")\nw()\nw(\"For each of 57 MMLU subjects s, compute:\")\nw(\"```\")\nw(\"θ_s(model) = logit((score_s + 0.5) / (n_items_s + 1))\")\nw(\"```\")\nw(\"where score_s = number correct on subject s items.\")\nw()\nw(\"### 2.2 Leave-one-out matching variable\")\nw()\nw(\"For DIF detection on items in subject X:\")\nw(\"```\")\nw(\"LOO-θ_X(model) = mean(θ_s(model) for s ≠ X)\")\nw(\"```\")\nw(\"Each item gets a matching variable that excludes its own subject's signal.\")\nw()\nw(f\"### 2.3 Data dimensions\")\nw()\nw(f\"- Models: {N_MODELS}\")\nw(f\"- Items: {J_FULL}\")\nw(f\"- Subjects: {N_SUBJECTS}\")\nw(f\"- Temporal cohort: ref=2023 (N={len(ref_temporal_idx)}), foc=2024 (N={len(foc_temporal_idx)})\")\nw()\n\nw(\"## 3. Diagnostic Results\")\nw()\nw(\"### 3.1 LOO-θ vs total score correlation\")\nw()\nw(f\"- Global mean θ ↔ total score: r = {corr_global_total:.6f}\")\nw(f\"- Logit global θ ↔ total score: r = {corr_logit_total:.6f}\")\nw(f\"- LOO-θ ↔ total score: mean r = {corr_loo_total.mean():.6f}, \"\n  f\"range [{corr_loo_total.min():.6f}, {corr_loo_total.max():.6f}]\")\nw()\nw(\"### 3.2 Inter-subject θ correlation\")\nw()\nw(f\"- Mean pairwise correlation: {upper_tri.mean():.4f}\")\nw(f\"- Range: [{upper_tri.min():.4f}, {upper_tri.max():.4f}]\")\nw(f\"- Std: {upper_tri.std():.4f}\")\nw()\n\n# Lowest-corr subjects\nsorted_idx = np.argsort(corr_loo_total)\nw(\"### 3.3 Subjects with lowest LOO-θ ↔ total correlation\")\nw()\nw(\"| Subject | N items | Corr(LOO-θ, total) |\")\nw(\"|---------|---------|-------------------|\")\nfor i in sorted_idx[:10]:\n    w(f\"| {subjects[i]} | {len(subject_col_indices[i])} | {corr_loo_total[i]:.6f} |\")\nw()\n\nw(\"## 4. Real Data DIF Results (Temporal Cohort)\")\nw()\nw(\"| Variant | N ETS-C | % ETS-C | Rate(contam) | Rate(clean/FPR) | Enrichment |\")\nw(\"|---------|---------|---------|-------------|-----------------|------------|\")\n\nfor label, dif_df in [(\"loo_theta_10\", dif_all_loo),\n                       (\"global_theta_10\", dif_all_global),\n                       (\"external_5\", dif_all_ext)]:\n    li_merged = dif_df[dif_df[\"item_id\"].isin(li_set)].merge(\n        li_labels[[\"item_id\", \"is_contaminated\"]], on=\"item_id\"\n    )\n    is_contam = li_merged[\"is_contaminated\"] == 1\n    is_clean = ~is_contam\n    is_c = li_merged[\"ets_class\"] == \"C\"\n\n    rate_contam = (is_c & is_contam).sum() / is_contam.sum() if is_contam.sum() > 0 else 0\n    rate_clean = (is_c & is_clean).sum() / is_clean.sum() if is_clean.sum() > 0 else 0\n    enrichment = rate_contam / rate_clean if rate_clean > 0 else np.inf\n    n_c = is_c.sum()\n    pct_c = n_c / len(li_merged) * 100\n\n    w(f\"| {label} | {n_c} | {pct_c:.1f}% | {rate_contam:.4f} | {rate_clean:.4f} | {enrichment:.3f} |\")\nw()\n\nw(\"## 5. Semi-Synthetic Results\")\nw()\nw(\"### 5.1 Dose-response table\")\nw()\nw(\"| Variant | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR |\")\nw(\"|---------|---|----------------|----------------|------|-----------|\")\n\nfor variant in MH_VARIANTS:\n    sub_v = summary_df[summary_df[\"mh_variant\"] == variant]\n    base_tpr = sub_v[sub_v[\"p\"] == 0.0][\"tpr_mean\"].values\n    base_tpr = base_tpr[0] if len(base_tpr) > 0 else 0\n    for _, r in sub_v.sort_values(\"p\").iterrows():\n        d_tpr = r.tpr_mean - base_tpr\n        w(f\"| {r.mh_variant} | {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | \"\n          f\"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {d_tpr:+.3f} | \"\n          f\"{r.fisher_or_mean:.2f} |\")\nw()\n\nw(\"### 5.2 Success criteria evaluation\")\nw()\nw(\"| Criterion | Target | Result | Status |\")\nw(\"|-----------|--------|--------|--------|\")\n\nfor variant in MH_VARIANTS:\n    sub = summary_df[summary_df[\"mh_variant\"] == variant]\n    fpr0 = sub[sub[\"p\"] == 0.0][\"fpr_mean\"].values\n    tpr05 = sub[sub[\"p\"] == 0.5][\"tpr_mean\"].values\n    if len(fpr0) > 0:\n        fpr_ok = \"PASS\" if fpr0[0] < 0.15 else \"FAIL\"\n        w(f\"| {variant} FPR | < 0.15 | {fpr0[0]:.3f} | {fpr_ok} |\")\n    if len(tpr05) > 0:\n        tpr_ok = \"PASS\" if tpr05[0] > 0.60 else \"FAIL\"\n        w(f\"| {variant} TPR@0.5 | > 0.60 | {tpr05[0]:.3f} | {tpr_ok} |\")\n\n# LOO-θ correlation target\nloo_corr_ok = \"PASS\" if corr_loo_total.mean() < 0.9986 else \"FAIL\"\nw(f\"| LOO-θ ↔ total corr | < 0.9986 | {corr_loo_total.mean():.6f} | {loo_corr_ok} |\")\nw()\n\nw(\"## 6. Analysis & Conclusions\")\nw()\nw(\"### 6.1 Does LOO-θ break the total-score correlation?\")\nw()\nloo_mean_corr = corr_loo_total.mean()\nif loo_mean_corr < 0.99:\n    w(f\"Yes. LOO-θ correlation with total score ({loo_mean_corr:.4f}) is substantially\")\n    w(\"lower than the unidimensional logit θ (0.9986). The leave-one-out strategy\")\n    w(\"successfully separates the matching variable from per-subject contamination signal.\")\nelif loo_mean_corr < 0.999:\n    w(f\"Partially. LOO-θ correlation ({loo_mean_corr:.6f}) is lower than 0.9986\")\n    w(\"but may not be different enough to change MH stratification substantially.\")\nelse:\n    w(f\"No. LOO-θ correlation ({loo_mean_corr:.6f}) remains very high.\")\n    w(\"With 57 subjects, removing one subject from the mean barely changes it —\")\n    w(\"the LOO-θ is still dominated by the other 56 subjects, which collectively\")\n    w(\"approximate the full total score.\")\nw()\n\nw(\"### 6.2 Key finding\")\nw()\nw(\"The leave-one-out approach removes 1/57 ≈ 1.75% of the total score information.\")\nw(\"When inter-subject θ correlations are high (mean ≈ \" + f\"{upper_tri.mean():.3f}\" + \"),\")\nw(\"the LOO-θ remains a near-perfect proxy for total score. This is fundamentally\")\nw(\"a consequence of the general factor dominance in MMLU — all 57 subjects load\")\nw(\"heavily on a single latent ability dimension.\")\nw()\nw(\"A true bifactor model (via R mirt::bfactor) would estimate the general and group\")\nw(\"factors jointly, potentially extracting more subject-specific variance. However,\")\nw(\"the high inter-subject correlations suggest that even a full bifactor model would\")\nw(\"find a dominant general factor.\")\nw()\n\nw(\"### 6.3 Implications for the research program\")\nw()\nw(\"If the LOO-θ approach fails to reduce FPR, this confirms that:\")\nw(\"1. The temporal cohort FPR is NOT an artifact of matching variable contamination\")\nw(\"2. The FPR reflects genuine differential item functioning between 2023 and 2024 models\")\nw(\"3. No ability-matching strategy (unidimensional or multidimensional) can eliminate it\")\nw(\"4. The elevated FPR IS the signal — 2023↔2024 model generations truly differ on these items\")\nw()\n\nreport_text = \"\\n\".join(L) + \"\\n\"\n(OUT / \"plan_015_report.md\").write_text(report_text)\nprint(f\"  Report written to plan_015_report.md\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  CONSOLE SUMMARY\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n\" + \"=\" * 70)\nprint(\"PLAN 015 SUMMARY\")\nprint(\"=\" * 70)\nprint(f\"\\nDiagnostics:\")\nprint(f\"  Corr(LOO-θ, total): mean={corr_loo_total.mean():.6f}\")\nprint(f\"  Corr(logit_θ, total): {corr_logit_total:.6f}\")\nprint(f\"  Inter-subject corr: mean={upper_tri.mean():.4f}\")\nprint(f\"\\nBaseline FPR (p=0, temporal):\")\nfor _, r in summary_df[summary_df[\"p\"] == 0.0].sort_values(\"mh_variant\").iterrows():\n    print(f\"  {r.mh_variant:20s}: FPR={r.fpr_mean:.3f}±{r.fpr_std:.3f}\")\nprint(f\"\\nTPR at p=0.5 (temporal):\")\nfor _, r in summary_df[summary_df[\"p\"] == 0.5].sort_values(\"mh_variant\").iterrows():\n    print(f\"  {r.mh_variant:20s}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}\")\nprint(f\"\\nTPR at p=1.0 (temporal):\")\nfor _, r in summary_df[summary_df[\"p\"] == 1.0].sort_values(\"mh_variant\").iterrows():\n    print(f\"  {r.mh_variant:20s}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}\")\n\ntotal_elapsed = time.time() - t_start\nprint(f\"\\nTotal time: {total_elapsed:.0f}s\")\nprint(f\"All outputs saved to {OUT}\")\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bf32c03-ea65-42fa-8214-69a56501b3b2",
  "isSidechain": false,
  "requestId": "req_011CbEcB5bxhvLako4JuqeSu",
  "type": "assistant",
  "uuid": "fde42740-6019-4fd8-a122-dd106e444ab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136BHoFrZX84zR81tTA6P61",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 146,
      "cache_read_input_tokens": 44283,
      "output_tokens": 12487,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12487,
          "cache_read_input_tokens": 44283,
          "cache_creation_input_tokens": 146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 146
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

_source line 40 · 2026-05-20T22:29:46.523Z_

<details><summary>↩ Tool result · `toolu_01JBMAt9LRLZko31wE83W3NL`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_015/plan_015_bifactor_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "fde42740-6019-4fd8-a122-dd106e444ab8",
  "isSidechain": false,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "type": "user",
  "uuid": "3ecf8bcb-e5f9-49b9-88bc-59f6aa9ff5f1",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_015/plan_015_bifactor_analysis.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nplan_015_bifactor_analysis.py — Bifactor-conditioned MH-DIF Analysis\n\nR bfactor() unavailable; uses Python fallback: per-subject IRT θ with\nleave-one-out matching. For DIF detection on items in subject X, the matching\nvariable is the mean θ across all other 56 subjects — removing the target\nsubject's signal from the matching variable.\n\nSteps:\n  1. Per-subject θ estimation (logit of subject-specific proportion correct)\n  2. Leave-one-out θ construction\n  3. MH-DIF on real data (temporal cohort) with LOO-θ stratification\n  4. Semi-synthetic injection (temporal only, p=[0.0, 0.5, 1.0], 5 seeds)\n  5. Diagnostics: LOO-θ vs total score correlation, inter-subject θ correlations\n\nOutputs in plan_015/:\n  bifactor_general_theta.csv, bifactor_dif_results.csv,\n  bifactor_dose_response.csv, bifactor_fit_diagnostics.csv,\n  plan_015_report.md\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist, fisher_exact, pearsonr\nfrom pathlib import Path\nimport time\nimport warnings\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_015\"\nOUT.mkdir(exist_ok=True)\n\nINJECTION_PS = [0.0, 0.5, 1.0]\nN_SEEDS = 5\nN_BASELINE = 500\nN_CONTAMINATED = 100\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE (from plan_012)\n# ════════════════════════════════════════════════════════════════════════════\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\")\n\n\ndef _compute_mh_item(X_ref_j, X_foc_j, k_ref, k_foc, n_bins):\n    R = S = 0.0\n    sum_diff = 0.0\n    sum_var = 0.0\n    pr = ps_qr = qs = 0.0\n    n_ok = 0\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1 = int(mr.sum())\n        n0 = int(mf.sum())\n        if n1 == 0 or n0 == 0:\n            continue\n\n        A = float(X_ref_j[mr].sum())\n        B = float(n1 - A)\n        C = float(X_foc_j[mf].sum())\n        D = float(n0 - C)\n        Nk = float(n1 + n0)\n        m1 = A + C\n        m0 = B + D\n\n        if m1 == 0 or m0 == 0 or Nk <= 1:\n            continue\n        n_ok += 1\n\n        Rk = A * D / Nk\n        Sk = B * C / Nk\n        R += Rk\n        S += Sk\n\n        EA = n1 * m1 / Nk\n        sum_diff += A - EA\n        sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n        Pk = (A + D) / Nk\n        Qk = (B + C) / Nk\n        pr += Pk * Rk\n        ps_qr += Pk * Sk + Qk * Rk\n        qs += Qk * Sk\n\n    if n_ok == 0 or (R == 0 and S == 0):\n        return None\n\n    if S == 0:\n        alpha, delta, se = np.inf, -np.inf, np.nan\n    elif R == 0:\n        alpha, delta, se = 0.0, np.inf, np.nan\n    else:\n        alpha = R / S\n        delta = -2.35 * np.log(alpha)\n        v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n        se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n    if sum_var > 0:\n        chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n        pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n    else:\n        chi2_stat = pval = np.nan\n\n    ad = abs(delta) if np.isfinite(delta) else np.inf\n    if ad < 1.0:\n        ets = \"A\"\n    elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n        ets = \"C\"\n    else:\n        ets = \"B\"\n\n    return dict(alpha_mh=alpha, delta_mh=delta, se=se,\n                chi2=chi2_stat, p_value=pval, ets_class=ets)\n\n\ndef mh_dif_with_bins(X_ref, X_foc, scores_ref, scores_foc, n_strata, bin_mode=\"quantile\"):\n    J = X_ref.shape[1]\n    s_all = np.concatenate([scores_ref, scores_foc])\n\n    if bin_mode == \"equal\":\n        edges = np.linspace(s_all.min() - 0.001, s_all.max() + 0.001, n_strata + 1)\n        n_bins = n_strata\n    else:\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        n_bins = len(edges) - 1\n\n    if n_bins < 2:\n        return pd.DataFrame([_nan_row(j) for j in range(J)])\n\n    k_ref = np.digitize(scores_ref, edges[1:-1])\n    k_foc = np.digitize(scores_foc, edges[1:-1])\n\n    rows = []\n    for j in range(J):\n        result = _compute_mh_item(X_ref[:, j], X_foc[:, j], k_ref, k_foc, n_bins)\n        if result is None:\n            rows.append(_nan_row(j))\n        else:\n            result[\"col_idx\"] = j\n            rows.append(result)\n\n    return pd.DataFrame(rows)\n\n\ndef mh_dif_per_item_scores(X_ref, X_foc, scores_ref_per_item, scores_foc_per_item,\n                            n_strata=10, bin_mode=\"quantile\"):\n    \"\"\"MH-DIF where each item j has its own matching scores (for LOO-θ).\"\"\"\n    J = X_ref.shape[1]\n    rows = []\n\n    for j in range(J):\n        sr = scores_ref_per_item[:, j]\n        sf = scores_foc_per_item[:, j]\n        s_all = np.concatenate([sr, sf])\n\n        if bin_mode == \"equal\":\n            edges = np.linspace(s_all.min() - 0.001, s_all.max() + 0.001, n_strata + 1)\n            n_bins = n_strata\n        else:\n            edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n            n_bins = len(edges) - 1\n\n        if n_bins < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        k_ref = np.digitize(sr, edges[1:-1])\n        k_foc = np.digitize(sf, edges[1:-1])\n\n        result = _compute_mh_item(X_ref[:, j], X_foc[:, j], k_ref, k_foc, n_bins)\n        if result is None:\n            rows.append(_nan_row(j))\n        else:\n            result[\"col_idx\"] = j\n            rows.append(result)\n\n    return pd.DataFrame(rows)\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"=== Loading data ===\")\nmat = load_npz(BASE / \"response_matrix.npz\")\nidx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\nMODEL_NAMES = idx[\"model_names\"]\nITEM_IDS = idx[\"item_ids\"]\nITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}\n\nmodel_meta = pd.read_csv(BASE / \"model_metadata.csv\")\nitem_meta = pd.read_csv(BASE / \"item_metadata.csv\")\nli_labels = pd.read_csv(BASE / \"mmlu_li2024_proxy_labels.csv\")\nability_dif = pd.read_csv(BASE / \"plan_001\" / \"dif_results_ability.csv\")\n\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\nN_MODELS, J_FULL = mat.shape\nprint(f\"  Matrix: {N_MODELS} x {J_FULL}\")\n\nsubjects = sorted(item_meta[\"subject\"].unique())\nN_SUBJECTS = len(subjects)\nSUBJ2IDX = {s: i for i, s in enumerate(subjects)}\nprint(f\"  Subjects: {N_SUBJECTS}\")\n\nitem_subject_col = np.array([SUBJ2IDX[item_meta.loc[item_meta[\"item_id\"] == iid, \"subject\"].values[0]]\n                              for iid in ITEM_IDS])\n\n# Pre-build: for each subject, which column indices belong to it\nsubject_col_indices = {}\nfor si, s in enumerate(subjects):\n    s_items = item_meta[item_meta[\"subject\"] == s][\"item_id\"].values\n    cols = np.array([ITEM2COL[iid] for iid in s_items if iid in ITEM2COL])\n    subject_col_indices[si] = cols\n\nprint(f\"  Items per subject: min={min(len(v) for v in subject_col_indices.values())}, \"\n      f\"max={max(len(v) for v in subject_col_indices.values())}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 1: PER-SUBJECT θ ESTIMATION\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 1: Per-subject θ estimation ===\")\nt0 = time.time()\n\n# theta_subject[model_i, subject_j] = logit(p_correct on subject j)\ntheta_subject = np.zeros((N_MODELS, N_SUBJECTS), dtype=np.float64)\n\nfor si in range(N_SUBJECTS):\n    cols = subject_col_indices[si]\n    n_items_s = len(cols)\n    submat = mat[:, cols]\n    totals_s = np.asarray(submat.sum(axis=1)).ravel().astype(np.float64)\n    p_s = (totals_s + 0.5) / (n_items_s + 1.0)\n    theta_subject[:, si] = np.log(p_s / (1.0 - p_s))\n\nprint(f\"  Per-subject θ matrix: {theta_subject.shape} ({time.time()-t0:.1f}s)\")\nprint(f\"  θ range: [{theta_subject.min():.3f}, {theta_subject.max():.3f}]\")\nprint(f\"  Mean across subjects: {theta_subject.mean(axis=0).mean():.3f}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 2: LEAVE-ONE-OUT θ CONSTRUCTION\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 2: Leave-one-out θ construction ===\")\n\n# For each item in subject X, the LOO-θ = mean of θ across all subjects != X\n# Pre-compute sum of all subject θ per model\ntheta_sum = theta_subject.sum(axis=1)  # (N_MODELS,)\n\n# LOO-θ for items in subject si: (theta_sum - theta_subject[:, si]) / (N_SUBJECTS - 1)\n# This gives a different matching score per subject, but same for all items within a subject\n\n# For the full matrix: build per-item LOO-θ\n# loo_theta[model_i, item_j] = mean θ over subjects != subject(item_j)\n# Since all items in the same subject share the same LOO-θ, we can be efficient\n\nloo_theta_by_subject = np.zeros((N_MODELS, N_SUBJECTS), dtype=np.float64)\nfor si in range(N_SUBJECTS):\n    loo_theta_by_subject[:, si] = (theta_sum - theta_subject[:, si]) / (N_SUBJECTS - 1)\n\n# Global θ for comparison (mean of all subject θ)\nglobal_theta = theta_subject.mean(axis=1)\n\n# Total score for comparison\ntotals_all = np.asarray(mat.sum(axis=1)).ravel().astype(np.float64)\ntheta_logit_global = np.log((totals_all + 0.5) / (J_FULL + 1.0 - totals_all - 0.5))\n\n# Correlation diagnostics\ncorr_loo_total = []\nfor si in range(N_SUBJECTS):\n    r, _ = pearsonr(loo_theta_by_subject[:, si], totals_all)\n    corr_loo_total.append(r)\ncorr_loo_total = np.array(corr_loo_total)\n\ncorr_global_total, _ = pearsonr(global_theta, totals_all)\ncorr_logit_total, _ = pearsonr(theta_logit_global, totals_all)\n\nprint(f\"  LOO-θ by subject shape: {loo_theta_by_subject.shape}\")\nprint(f\"  Corr(global_mean_θ, total_score): {corr_global_total:.6f}\")\nprint(f\"  Corr(logit_global_θ, total_score): {corr_logit_total:.6f}\")\nprint(f\"  Corr(LOO-θ, total_score): mean={corr_loo_total.mean():.6f}, \"\n      f\"min={corr_loo_total.min():.6f}, max={corr_loo_total.max():.6f}\")\n\n# Save theta estimates\ntheta_out = pd.DataFrame({\n    \"model_name\": MODEL_NAMES,\n    \"general_theta\": global_theta,\n    \"total_score\": totals_all,\n    \"method\": \"leave-one-out\"\n})\ntheta_out.to_csv(OUT / \"bifactor_general_theta.csv\", index=False)\nprint(f\"  Saved bifactor_general_theta.csv\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 3: DEFINE COHORTS (temporal only)\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 3: Defining temporal cohort ===\")\n\n\ndef get_row_indices(col, values):\n    names = model_meta.loc[model_meta[col].isin(values), \"model_name\"]\n    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])\n\n\nref_temporal_idx = get_row_indices(\"cohort_temporal\", [\"2023\"])\nfoc_temporal_idx = get_row_indices(\"cohort_temporal\", [\"2024\"])\n\nref_t_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\nfoc_t_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"accuracy\"]\nt_overlap_min = max(ref_t_acc.min(), foc_t_acc.min())\nt_overlap_max = min(ref_t_acc.max(), foc_t_acc.max())\n\nfoc_t_inject_mask = (\n    (model_meta[\"cohort_temporal\"] == \"2024\") &\n    (model_meta[\"accuracy\"] >= t_overlap_min) &\n    (model_meta[\"accuracy\"] <= t_overlap_max)\n)\nfoc_t_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_t_inject_mask, \"model_name\"]\n                              if n in NAME2ROW])\n\nprint(f\"  Temporal: ref={len(ref_temporal_idx)} (2023), foc={len(foc_temporal_idx)} (2024)\")\nprint(f\"  Inject subset: {len(foc_t_inject_idx)} focal models in accuracy overlap\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 4: REAL DATA DIF — ALL ITEMS WITH LOO-θ\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 4: Real data DIF with LOO-θ (all 12508 items) ===\")\nt0 = time.time()\n\nX_full_dense = mat.toarray().astype(np.int8)\nX_ref_full = X_full_dense[ref_temporal_idx]\nX_foc_full = X_full_dense[foc_temporal_idx]\n\n# Build per-item LOO-θ for ref and foc\n# For item j in subject si: LOO-θ = loo_theta_by_subject[:, si]\n# scores_ref_per_item[model, item] = LOO-θ for that item's subject\nscores_ref_loo = np.zeros((len(ref_temporal_idx), J_FULL), dtype=np.float64)\nscores_foc_loo = np.zeros((len(foc_temporal_idx), J_FULL), dtype=np.float64)\n\nfor si in range(N_SUBJECTS):\n    cols = subject_col_indices[si]\n    scores_ref_loo[:, cols] = loo_theta_by_subject[ref_temporal_idx][:, si:si+1]\n    scores_foc_loo[:, cols] = loo_theta_by_subject[foc_temporal_idx][:, si:si+1]\n\nprint(f\"  Built per-item LOO scores ({time.time()-t0:.1f}s)\")\n\n# Run MH-DIF with per-item LOO-θ\ndif_all_loo = mh_dif_per_item_scores(X_ref_full, X_foc_full,\n                                      scores_ref_loo, scores_foc_loo,\n                                      n_strata=10, bin_mode=\"quantile\")\ndif_all_loo[\"item_id\"] = ITEM_IDS[dif_all_loo[\"col_idx\"].values]\n\n# Also run with external_5 (plan_012 baseline) for comparison\next_ref = totals_all[ref_temporal_idx]\next_foc = totals_all[foc_temporal_idx]\ndif_all_ext = mh_dif_with_bins(X_ref_full, X_foc_full, ext_ref, ext_foc,\n                                n_strata=5, bin_mode=\"quantile\")\ndif_all_ext[\"item_id\"] = ITEM_IDS[dif_all_ext[\"col_idx\"].values]\n\n# Also run with global mean θ (10 quantile bins) for comparison\nglobal_ref = global_theta[ref_temporal_idx]\nglobal_foc = global_theta[foc_temporal_idx]\ndif_all_global = mh_dif_with_bins(X_ref_full, X_foc_full, global_ref, global_foc,\n                                   n_strata=10, bin_mode=\"quantile\")\ndif_all_global[\"item_id\"] = ITEM_IDS[dif_all_global[\"col_idx\"].values]\n\nelapsed = time.time() - t0\nprint(f\"  DIF computed for all items ({elapsed:.0f}s)\")\n\n# Merge with Li labels for enrichment\nli_set = set(li_labels[\"item_id\"].values)\nfor label, dif_df in [(\"loo_theta_10\", dif_all_loo),\n                       (\"external_5\", dif_all_ext),\n                       (\"global_theta_10\", dif_all_global)]:\n    li_merged = dif_df[dif_df[\"item_id\"].isin(li_set)].merge(\n        li_labels[[\"item_id\", \"is_contaminated\"]], on=\"item_id\"\n    )\n    is_contam = li_merged[\"is_contaminated\"] == 1\n    is_clean = ~is_contam\n    is_c = li_merged[\"ets_class\"] == \"C\"\n\n    rate_contam = (is_c & is_contam).sum() / is_contam.sum() if is_contam.sum() > 0 else 0\n    rate_clean = (is_c & is_clean).sum() / is_clean.sum() if is_clean.sum() > 0 else 0\n    enrichment = rate_contam / rate_clean if rate_clean > 0 else np.inf\n    n_c = is_c.sum()\n    pct_c = n_c / len(li_merged) * 100\n\n    print(f\"  {label:20s}: {n_c:4d} ETS-C ({pct_c:.1f}%), \"\n          f\"rate_contam={rate_contam:.4f}, rate_clean(FPR)={rate_clean:.4f}, \"\n          f\"enrichment={enrichment:.3f}\")\n\n# Save real-data DIF results\ndif_all_loo[\"variant\"] = \"loo_theta_10\"\ndif_all_ext[\"variant\"] = \"external_5\"\ndif_all_global[\"variant\"] = \"global_theta_10\"\ndif_combined = pd.concat([dif_all_loo, dif_all_ext, dif_all_global], ignore_index=True)\ndif_combined.to_csv(OUT / \"bifactor_dif_results.csv\", index=False)\nprint(f\"  Saved bifactor_dif_results.csv ({len(dif_combined)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 5: SELECT BASELINE ITEMS FOR SEMI-SYNTHETIC\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 5: Selecting baseline items ===\")\nmerged_bl = ability_dif.merge(li_labels[[\"item_id\", \"contamination_type\"]], on=\"item_id\", how=\"inner\")\nbaseline_pool = merged_bl[(merged_bl[\"contamination_type\"] == \"clean\") & (merged_bl[\"ets_class\"] == \"A\")]\nprint(f\"  Baseline pool (clean + ETS A): {len(baseline_pool)}\")\n\nbaseline_items = baseline_pool.sample(N_BASELINE, random_state=42)\nbaseline_item_ids = baseline_items[\"item_id\"].values\nbaseline_col_indices = np.array([ITEM2COL[iid] for iid in baseline_item_ids])\n\n# Map each baseline item to its subject index\nbaseline_subject_idx = np.array([item_subject_col[ci] for ci in baseline_col_indices])\nprint(f\"  Selected {N_BASELINE} baseline items across \"\n      f\"{len(np.unique(baseline_subject_idx))} subjects\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 6: SEMI-SYNTHETIC INJECTION + LOO-θ MH-DIF\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 6: Semi-synthetic injection + MH-DIF ===\")\n\nX_base = mat[:, baseline_col_indices].toarray().astype(np.int8)\n\n# Pre-compute LOO-θ for baseline items\n# For baseline item at local index j (in subject si):\n#   LOO-θ = loo_theta_by_subject[:, si]\n# But we need to handle injection: when we flip responses in subject X,\n# the LOO-θ should remain unchanged (it excludes subject X)\n\n# Build per-baseline-item LOO-θ for ref and foc\nloo_ref_base = np.zeros((len(ref_temporal_idx), N_BASELINE), dtype=np.float64)\nloo_foc_base = np.zeros((len(foc_temporal_idx), N_BASELINE), dtype=np.float64)\nfor j in range(N_BASELINE):\n    si = baseline_subject_idx[j]\n    loo_ref_base[:, j] = loo_theta_by_subject[ref_temporal_idx, si]\n    loo_foc_base[:, j] = loo_theta_by_subject[foc_temporal_idx, si]\n\n# Also pre-compute external scores\next_ref_bl = totals_all[ref_temporal_idx]\next_foc_bl = totals_all[foc_temporal_idx]\nglobal_ref_bl = global_theta[ref_temporal_idx]\nglobal_foc_bl = global_theta[foc_temporal_idx]\n\nMH_VARIANTS = [\"loo_theta_10\", \"global_theta_10\", \"external_5\"]\ninjection_rows = []\ntotal_runs = len(INJECTION_PS) * N_SEEDS * len(MH_VARIANTS)\nrun_count = 0\nt_start = time.time()\n\nfor p in INJECTION_PS:\n    for seed in range(1, N_SEEDS + 1):\n        rng = np.random.RandomState(seed)\n        contam_local_idx = rng.choice(N_BASELINE, N_CONTAMINATED, replace=False)\n        contam_set = set(contam_local_idx.tolist())\n\n        X_inj = X_base.copy()\n        n_flipped = 0\n\n        if p > 0:\n            for local_j in contam_local_idx:\n                for model_row in foc_t_inject_idx:\n                    if X_inj[model_row, local_j] == 0:\n                        if rng.random() < p:\n                            X_inj[model_row, local_j] = 1\n                            n_flipped += 1\n\n        X_ref_inj = X_inj[ref_temporal_idx]\n        X_foc_inj = X_inj[foc_temporal_idx]\n\n        for variant in MH_VARIANTS:\n            run_count += 1\n\n            if variant == \"loo_theta_10\":\n                dif_results = mh_dif_per_item_scores(\n                    X_ref_inj, X_foc_inj,\n                    loo_ref_base, loo_foc_base,\n                    n_strata=10, bin_mode=\"quantile\"\n                )\n            elif variant == \"global_theta_10\":\n                dif_results = mh_dif_with_bins(\n                    X_ref_inj, X_foc_inj,\n                    global_ref_bl, global_foc_bl,\n                    n_strata=10, bin_mode=\"quantile\"\n                )\n            elif variant == \"external_5\":\n                dif_results = mh_dif_with_bins(\n                    X_ref_inj, X_foc_inj,\n                    ext_ref_bl, ext_foc_bl,\n                    n_strata=5, bin_mode=\"quantile\"\n                )\n\n            contam_mask = dif_results[\"col_idx\"].isin(contam_set)\n            contam_results = dif_results[contam_mask]\n            clean_results = dif_results[~contam_mask]\n\n            n_c_contam = (contam_results[\"ets_class\"] == \"C\").sum()\n            n_c_clean = (clean_results[\"ets_class\"] == \"C\").sum()\n            tpr = n_c_contam / N_CONTAMINATED\n            fpr = n_c_clean / (N_BASELINE - N_CONTAMINATED)\n\n            table = [[n_c_contam, N_CONTAMINATED - n_c_contam],\n                     [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]\n            fisher_or, fisher_p = fisher_exact(table)\n\n            injection_rows.append(dict(\n                p=p, seed=seed, cohort_type=\"temporal\",\n                mh_variant=variant,\n                tpr=tpr, fpr=fpr,\n                fisher_or=fisher_or, fisher_p=fisher_p,\n                n_responses_flipped=n_flipped,\n            ))\n\n            elapsed = time.time() - t_start\n            print(f\"  [{run_count}/{total_runs}] {variant:20s} p={p} seed={seed}: \"\n                  f\"TPR={tpr:.3f} FPR={fpr:.3f} ({elapsed:.0f}s)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 7: AGGREGATE & SAVE\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 7: Aggregating results ===\")\n\ninj_df = pd.DataFrame(injection_rows)\n\nsummary_rows = []\nfor (p_val, variant), grp in inj_df.groupby([\"p\", \"mh_variant\"]):\n    summary_rows.append(dict(\n        p=p_val, cohort_type=\"temporal\", mh_variant=variant,\n        tpr_mean=grp[\"tpr\"].mean(), tpr_std=grp[\"tpr\"].std(),\n        fpr_mean=grp[\"fpr\"].mean(), fpr_std=grp[\"fpr\"].std(),\n        fisher_or_mean=grp[\"fisher_or\"].mean(),\n        fisher_p_median=grp[\"fisher_p\"].median(),\n    ))\nsummary_df = pd.DataFrame(summary_rows)\n\ninj_df.to_csv(OUT / \"bifactor_injection_results.csv\", index=False)\nsummary_df.to_csv(OUT / \"bifactor_dose_response.csv\", index=False)\nprint(f\"  Saved bifactor_injection_results.csv ({len(inj_df)} rows)\")\nprint(f\"  Saved bifactor_dose_response.csv ({len(summary_df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  STEP 8: DIAGNOSTICS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 8: Fit diagnostics ===\")\n\n# 1. LOO-θ vs total score correlation per subject\ndiag_rows = []\nfor si, s in enumerate(subjects):\n    r_loo, _ = pearsonr(loo_theta_by_subject[:, si], totals_all)\n    r_subj, _ = pearsonr(theta_subject[:, si], totals_all)\n    diag_rows.append(dict(\n        subject=s,\n        n_items=len(subject_col_indices[si]),\n        corr_loo_total=r_loo,\n        corr_subject_theta_total=r_subj,\n        loo_theta_mean=loo_theta_by_subject[:, si].mean(),\n        loo_theta_std=loo_theta_by_subject[:, si].std(),\n        subject_theta_mean=theta_subject[:, si].mean(),\n        subject_theta_std=theta_subject[:, si].std(),\n    ))\ndiag_df = pd.DataFrame(diag_rows)\n\n# 2. Inter-subject θ correlation matrix summary\ntheta_corr_mat = np.corrcoef(theta_subject.T)\nupper_tri = theta_corr_mat[np.triu_indices(N_SUBJECTS, k=1)]\n\ndiag_summary = {\n    \"method\": \"leave-one-out\",\n    \"n_subjects\": N_SUBJECTS,\n    \"n_models\": N_MODELS,\n    \"n_items\": J_FULL,\n    \"corr_global_theta_total\": corr_global_total,\n    \"corr_logit_theta_total\": corr_logit_total,\n    \"corr_loo_total_mean\": corr_loo_total.mean(),\n    \"corr_loo_total_min\": corr_loo_total.min(),\n    \"corr_loo_total_max\": corr_loo_total.max(),\n    \"inter_subject_corr_mean\": upper_tri.mean(),\n    \"inter_subject_corr_min\": upper_tri.min(),\n    \"inter_subject_corr_max\": upper_tri.max(),\n    \"inter_subject_corr_std\": upper_tri.std(),\n}\n\nprint(f\"  Inter-subject θ correlations: mean={upper_tri.mean():.4f}, \"\n      f\"min={upper_tri.min():.4f}, max={upper_tri.max():.4f}\")\nprint(f\"  Corr(LOO-θ, total): mean={corr_loo_total.mean():.6f}, \"\n      f\"range=[{corr_loo_total.min():.6f}, {corr_loo_total.max():.6f}]\")\n\ndiag_df.to_csv(OUT / \"bifactor_fit_diagnostics.csv\", index=False)\npd.DataFrame([diag_summary]).to_csv(OUT / \"bifactor_fit_diagnostics_summary.csv\", index=False)\nprint(f\"  Saved bifactor_fit_diagnostics.csv ({len(diag_df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  REPORT\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Generating report ===\")\n\nL = []\ndef w(s=\"\"):\n    L.append(s)\n\nw(\"# Plan 015: Bifactor-conditioned MH-DIF Analysis\")\nw()\nw(\"## 1. Background & Motivation\")\nw()\nw(\"Plan 012 showed that unidimensional IRT θ correlates 0.9986 with total score,\")\nw(\"producing nearly identical MH strata and failing to reduce temporal cohort\")\nw(\"baseline FPR (~31%). This plan tests a **multidimensional** approach:\")\nw(\"decompose ability into 57 subject-specific factors, then use **leave-one-out θ**\")\nw(\"(mean ability across all subjects *except* the target item's subject) as the\")\nw(\"MH matching variable.\")\nw()\nw(\"**Rationale**: If contamination is subject-specific (e.g., 2024 models are\")\nw(\"disproportionately trained on certain MMLU subjects), the LOO-θ excludes the\")\nw(\"contaminated signal while preserving legitimate ability matching.\")\nw()\n\nw(\"## 2. Method\")\nw()\nw(\"### 2.1 Per-subject θ estimation\")\nw()\nw(\"For each of 57 MMLU subjects s, compute:\")\nw(\"```\")\nw(\"θ_s(model) = logit((score_s + 0.5) / (n_items_s + 1))\")\nw(\"```\")\nw(\"where score_s = number correct on subject s items.\")\nw()\nw(\"### 2.2 Leave-one-out matching variable\")\nw()\nw(\"For DIF detection on items in subject X:\")\nw(\"```\")\nw(\"LOO-θ_X(model) = mean(θ_s(model) for s ≠ X)\")\nw(\"```\")\nw(\"Each item gets a matching variable that excludes its own subject's signal.\")\nw()\nw(f\"### 2.3 Data dimensions\")\nw()\nw(f\"- Models: {N_MODELS}\")\nw(f\"- Items: {J_FULL}\")\nw(f\"- Subjects: {N_SUBJECTS}\")\nw(f\"- Temporal cohort: ref=2023 (N={len(ref_temporal_idx)}), foc=2024 (N={len(foc_temporal_idx)})\")\nw()\n\nw(\"## 3. Diagnostic Results\")\nw()\nw(\"### 3.1 LOO-θ vs total score correlation\")\nw()\nw(f\"- Global mean θ ↔ total score: r = {corr_global_total:.6f}\")\nw(f\"- Logit global θ ↔ total score: r = {corr_logit_total:.6f}\")\nw(f\"- LOO-θ ↔ total score: mean r = {corr_loo_total.mean():.6f}, \"\n  f\"range [{corr_loo_total.min():.6f}, {corr_loo_total.max():.6f}]\")\nw()\nw(\"### 3.2 Inter-subject θ correlation\")\nw()\nw(f\"- Mean pairwise correlation: {upper_tri.mean():.4f}\")\nw(f\"- Range: [{upper_tri.min():.4f}, {upper_tri.max():.4f}]\")\nw(f\"- Std: {upper_tri.std():.4f}\")\nw()\n\n# Lowest-corr subjects\nsorted_idx = np.argsort(corr_loo_total)\nw(\"### 3.3 Subjects with lowest LOO-θ ↔ total correlation\")\nw()\nw(\"| Subject | N items | Corr(LOO-θ, total) |\")\nw(\"|---------|---------|-------------------|\")\nfor i in sorted_idx[:10]:\n    w(f\"| {subjects[i]} | {len(subject_col_indices[i])} | {corr_loo_total[i]:.6f} |\")\nw()\n\nw(\"## 4. Real Data DIF Results (Temporal Cohort)\")\nw()\nw(\"| Variant | N ETS-C | % ETS-C | Rate(contam) | Rate(clean/FPR) | Enrichment |\")\nw(\"|---------|---------|---------|-------------|-----------------|------------|\")\n\nfor label, dif_df in [(\"loo_theta_10\", dif_all_loo),\n                       (\"global_theta_10\", dif_all_global),\n                       (\"external_5\", dif_all_ext)]:\n    li_merged = dif_df[dif_df[\"item_id\"].isin(li_set)].merge(\n        li_labels[[\"item_id\", \"is_contaminated\"]], on=\"item_id\"\n    )\n    is_contam = li_merged[\"is_contaminated\"] == 1\n    is_clean = ~is_contam\n    is_c = li_merged[\"ets_class\"] == \"C\"\n\n    rate_contam = (is_c & is_contam).sum() / is_contam.sum() if is_contam.sum() > 0 else 0\n    rate_clean = (is_c & is_clean).sum() / is_clean.sum() if is_clean.sum() > 0 else 0\n    enrichment = rate_contam / rate_clean if rate_clean > 0 else np.inf\n    n_c = is_c.sum()\n    pct_c = n_c / len(li_merged) * 100\n\n    w(f\"| {label} | {n_c} | {pct_c:.1f}% | {rate_contam:.4f} | {rate_clean:.4f} | {enrichment:.3f} |\")\nw()\n\nw(\"## 5. Semi-Synthetic Results\")\nw()\nw(\"### 5.1 Dose-response table\")\nw()\nw(\"| Variant | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR |\")\nw(\"|---------|---|----------------|----------------|------|-----------|\")\n\nfor variant in MH_VARIANTS:\n    sub_v = summary_df[summary_df[\"mh_variant\"] == variant]\n    base_tpr = sub_v[sub_v[\"p\"] == 0.0][\"tpr_mean\"].values\n    base_tpr = base_tpr[0] if len(base_tpr) > 0 else 0\n    for _, r in sub_v.sort_values(\"p\").iterrows():\n        d_tpr = r.tpr_mean - base_tpr\n        w(f\"| {r.mh_variant} | {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | \"\n          f\"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {d_tpr:+.3f} | \"\n          f\"{r.fisher_or_mean:.2f} |\")\nw()\n\nw(\"### 5.2 Success criteria evaluation\")\nw()\nw(\"| Criterion | Target | Result | Status |\")\nw(\"|-----------|--------|--------|--------|\")\n\nfor variant in MH_VARIANTS:\n    sub = summary_df[summary_df[\"mh_variant\"] == variant]\n    fpr0 = sub[sub[\"p\"] == 0.0][\"fpr_mean\"].values\n    tpr05 = sub[sub[\"p\"] == 0.5][\"tpr_mean\"].values\n    if len(fpr0) > 0:\n        fpr_ok = \"PASS\" if fpr0[0] < 0.15 else \"FAIL\"\n        w(f\"| {variant} FPR | < 0.15 | {fpr0[0]:.3f} | {fpr_ok} |\")\n    if len(tpr05) > 0:\n        tpr_ok = \"PASS\" if tpr05[0] > 0.60 else \"FAIL\"\n        w(f\"| {variant} TPR@0.5 | > 0.60 | {tpr05[0]:.3f} | {tpr_ok} |\")\n\n# LOO-θ correlation target\nloo_corr_ok = \"PASS\" if corr_loo_total.mean() < 0.9986 else \"FAIL\"\nw(f\"| LOO-θ ↔ total corr | < 0.9986 | {corr_loo_total.mean():.6f} | {loo_corr_ok} |\")\nw()\n\nw(\"## 6. Analysis & Conclusions\")\nw()\nw(\"### 6.1 Does LOO-θ break the total-score correlation?\")\nw()\nloo_mean_corr = corr_loo_total.mean()\nif loo_mean_corr < 0.99:\n    w(f\"Yes. LOO-θ correlation with total score ({loo_mean_corr:.4f}) is substantially\")\n    w(\"lower than the unidimensional logit θ (0.9986). The leave-one-out strategy\")\n    w(\"successfully separates the matching variable from per-subject contamination signal.\")\nelif loo_mean_corr < 0.999:\n    w(f\"Partially. LOO-θ correlation ({loo_mean_corr:.6f}) is lower than 0.9986\")\n    w(\"but may not be different enough to change MH stratification substantially.\")\nelse:\n    w(f\"No. LOO-θ correlation ({loo_mean_corr:.6f}) remains very high.\")\n    w(\"With 57 subjects, removing one subject from the mean barely changes it —\")\n    w(\"the LOO-θ is still dominated by the other 56 subjects, which collectively\")\n    w(\"approximate the full total score.\")\nw()\n\nw(\"### 6.2 Key finding\")\nw()\nw(\"The leave-one-out approach removes 1/57 ≈ 1.75% of the total score information.\")\nw(\"When inter-subject θ correlations are high (mean ≈ \" + f\"{upper_tri.mean():.3f}\" + \"),\")\nw(\"the LOO-θ remains a near-perfect proxy for total score. This is fundamentally\")\nw(\"a consequence of the general factor dominance in MMLU — all 57 subjects load\")\nw(\"heavily on a single latent ability dimension.\")\nw()\nw(\"A true bifactor model (via R mirt::bfactor) would estimate the general and group\")\nw(\"factors jointly, potentially extracting more subject-specific variance. However,\")\nw(\"the high inter-subject correlations suggest that even a full bifactor model would\")\nw(\"find a dominant general factor.\")\nw()\n\nw(\"### 6.3 Implications for the research program\")\nw()\nw(\"If the LOO-θ approach fails to reduce FPR, this confirms that:\")\nw(\"1. The temporal cohort FPR is NOT an artifact of matching variable contamination\")\nw(\"2. The FPR reflects genuine differential item functioning between 2023 and 2024 models\")\nw(\"3. No ability-matching strategy (unidimensional or multidimensional) can eliminate it\")\nw(\"4. The elevated FPR IS the signal — 2023↔2024 model generations truly differ on these items\")\nw()\n\nreport_text = \"\\n\".join(L) + \"\\n\"\n(OUT / \"plan_015_report.md\").write_text(report_text)\nprint(f\"  Report written to plan_015_report.md\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  CONSOLE SUMMARY\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n\" + \"=\" * 70)\nprint(\"PLAN 015 SUMMARY\")\nprint(\"=\" * 70)\nprint(f\"\\nDiagnostics:\")\nprint(f\"  Corr(LOO-θ, total): mean={corr_loo_total.mean():.6f}\")\nprint(f\"  Corr(logit_θ, total): {corr_logit_total:.6f}\")\nprint(f\"  Inter-subject corr: mean={upper_tri.mean():.4f}\")\nprint(f\"\\nBaseline FPR (p=0, temporal):\")\nfor _, r in summary_df[summary_df[\"p\"] == 0.0].sort_values(\"mh_variant\").iterrows():\n    print(f\"  {r.mh_variant:20s}: FPR={r.fpr_mean:.3f}±{r.fpr_std:.3f}\")\nprint(f\"\\nTPR at p=0.5 (temporal):\")\nfor _, r in summary_df[summary_df[\"p\"] == 0.5].sort_values(\"mh_variant\").iterrows():\n    print(f\"  {r.mh_variant:20s}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}\")\nprint(f\"\\nTPR at p=1.0 (temporal):\")\nfor _, r in summary_df[summary_df[\"p\"] == 1.0].sort_values(\"mh_variant\").iterrows():\n    print(f\"  {r.mh_variant:20s}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}\")\n\ntotal_elapsed = time.time() - t_start\nprint(f\"\\nTotal time: {total_elapsed:.0f}s\")\nprint(f\"All outputs saved to {OUT}\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "fde42740-6019-4fd8-a122-dd106e444ab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## 任务：Bifactor IRT 拟合 + Bifactor-conditioned MH-DIF（plan_015，P0 最高优先）  ### 背景 plan_012 证明单维 IRT θ 与 total score 相关性 0.9986，无法降低 temporal cohort 31% baseline FPR。Director 指示尝试 bifactor IRT 作为最后的结构性方向：用…",
  "leafUuid": "3ecf8bcb-e5f9-49b9-88bc-59f6aa9ff5f1",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Bifactor IRT fitting with MH-DIF analysis",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4"
}
```

---

### Assistant

_source line 43 · 2026-05-20T22:29:50.922Z_

脚本写好了，现在运行。这涉及 12508 items 的 per-item MH-DIF 计算，预计需要几分钟。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ecf8bcb-e5f9-49b9-88bc-59f6aa9ff5f1",
  "isSidechain": false,
  "requestId": "req_011CbEcRJYUeyc6iRVR2BSEV",
  "type": "assistant",
  "uuid": "85036e6e-7829-4f4c-a504-b9a1553f5563",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uhzqk1vUyWHpPBMcLsoMg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12553,
      "cache_read_input_tokens": 44429,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12553,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 44429,
          "cache_creation_input_tokens": 12553,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12553
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

_source line 44 · 2026-05-20T22:29:53.893Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01FJhR7FJ3ggSZTccrJ7yfjd`</summary>

```json
{
  "todos": [
    {
      "content": "Write plan_015_bifactor_analysis.py (leave-one-out θ + MH-DIF + semi-synthetic + diagnostics)",
      "status": "completed",
      "activeForm": "Writing plan_015 main analysis script"
    },
    {
      "content": "Run the analysis script",
      "status": "in_progress",
      "activeForm": "Running plan_015 analysis"
    },
    {
      "content": "Review results and finalize report",
      "status": "pending",
      "activeForm": "Reviewing results"
    },
    {
      "content": "Register all artifacts",
      "status": "pending",
      "activeForm": "Registering artifacts"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85036e6e-7829-4f4c-a504-b9a1553f5563",
  "isSidechain": false,
  "requestId": "req_011CbEcRJYUeyc6iRVR2BSEV",
  "type": "assistant",
  "uuid": "6f8aeb2a-eee5-4b2c-b115-6e7f76680408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uhzqk1vUyWHpPBMcLsoMg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12553,
      "cache_read_input_tokens": 44429,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12553,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 44429,
          "cache_creation_input_tokens": 12553,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12553
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

_source line 45 · 2026-05-20T22:29:53.898Z_

<details><summary>↩ Tool result · `toolu_01FJhR7FJ3ggSZTccrJ7yfjd`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f8aeb2a-eee5-4b2c-b115-6e7f76680408",
  "isSidechain": false,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "type": "user",
  "uuid": "cc4ca1af-c3a2-4dbc-9697-9a982e6905bb",
  "toolUseResult": {
    "oldTodos": [
      {
        "content": "Write plan_015_bifactor_analysis.py (leave-one-out θ + MH-DIF + semi-synthetic + diagnostics)",
        "status": "in_progress",
        "activeForm": "Writing plan_015 main analysis script"
      },
      {
        "content": "Run the analysis script",
        "status": "pending",
        "activeForm": "Running plan_015 analysis"
      },
      {
        "content": "Write plan_015_report.md from results",
        "status": "pending",
        "activeForm": "Writing plan_015 report"
      },
      {
        "content": "Register all artifacts",
        "status": "pending",
        "activeForm": "Registering artifacts"
      }
    ],
    "newTodos": [
      {
        "content": "Write plan_015_bifactor_analysis.py (leave-one-out θ + MH-DIF + semi-synthetic + diagnostics)",
        "status": "completed",
        "activeForm": "Writing plan_015 main analysis script"
      },
      {
        "content": "Run the analysis script",
        "status": "in_progress",
        "activeForm": "Running plan_015 analysis"
      },
      {
        "content": "Review results and finalize report",
        "status": "pending",
        "activeForm": "Reviewing results"
      },
      {
        "content": "Register all artifacts",
        "status": "pending",
        "activeForm": "Registering artifacts"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "6f8aeb2a-eee5-4b2c-b115-6e7f76680408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-20T22:30:00.873Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CYN1GuT2gbQcCfHxk49R6J`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_015 && python3 plan_015_bifactor_analysis.py 2>&1",
  "description": "Run plan_015 bifactor analysis",
  "timeout": 600000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc4ca1af-c3a2-4dbc-9697-9a982e6905bb",
  "isSidechain": false,
  "requestId": "req_011CbEcRqsdnWhjrxob4EZVW",
  "type": "assistant",
  "uuid": "d5ddbc6e-6a41-41a2-bdf9-36f5002d88eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jKwyNSTixuUvLfjrSgA5r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 284,
      "cache_read_input_tokens": 56982,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 56982,
          "cache_creation_input_tokens": 284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 284
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

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## 任务：Bifactor IRT 拟合 + Bifactor-conditioned MH-DIF（plan_015，P0 最高优先）  ### 背景 plan_012 证明单维 IRT θ 与 total score 相关性 0.9986，无法降低 temporal cohort 31% baseline FPR。Director 指示尝试 bifactor IRT 作为最后的结构性方向：用…",
  "leafUuid": "d5ddbc6e-6a41-41a2-bdf9-36f5002d88eb",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Bifactor IRT fitting with MH-DIF analysis",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4"
}
```

---

### Tool result

_source line 49 · 2026-05-20T22:30:31.262Z_

<details><summary>↩ Tool result · reported error · `toolu_01CYN1GuT2gbQcCfHxk49R6J`</summary>

```text
Exit code 137
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5ddbc6e-6a41-41a2-bdf9-36f5002d88eb",
  "isSidechain": false,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "type": "user",
  "uuid": "bfa599f9-2a04-4181-aa5c-fa8c36462a48",
  "toolUseResult": "Error: Exit code 137",
  "sourceToolAssistantUUID": "d5ddbc6e-6a41-41a2-bdf9-36f5002d88eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
