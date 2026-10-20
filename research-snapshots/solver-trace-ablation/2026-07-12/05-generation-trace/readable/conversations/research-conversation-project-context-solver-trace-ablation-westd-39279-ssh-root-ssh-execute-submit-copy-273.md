# Research conversation: <project_context> # 项目: solver-trace-ablation ## 运行环境 - 服务器名: westd-39279 - SSH 账户: root（调用 ssh_execute / submit_trainin

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/ff2a3926-a23a-4756-aa8c-9df2956fd4eb.jsonl`
- **Structured JSON:** [`15e8fc028f71f9550b61.json`](../../sessions/15/15e8fc028f71f9550b61.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T23:01:45.355Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T23:01:45.355Z",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "content": "&lt;project_context>\n# 项目: solver-trace-ablation\n\n## 运行环境\n- 服务器名: westd-39279\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/solver-trace-ablation\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 所有实验统一使用 data/train_500_seed42.jsonl 作为训练数据，禁止使用 proofwriter_fol_500.jsonl 或其他数据文件（原因：Reviewer CRITICAL: plan001-s43 使用了不同数据文件导致多 seed 对比 confound。多 seed 实验必须控制数据变量，seed 仅控制模型初始化和训练随机性。）\n- **C002**: 提交训练任务前必须用 export CUDA_VISIBLE_DEVICES=N 显式设置 GPU，禁止 inline 赋值（bash -c VAR=X cmd），提交后验证 nvidia-smi 确认只占用分配的 GPU（原因：plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43 OOM 死亡。这是第二次 GPU 冲突事故。）\n- **C003**: 训练配置必须设置 save_total_limit=1 且禁用/限制 completions parquet 保存，防止磁盘耗尽（原因：plan013-r3 和 plan001-s43-r3 因磁盘 250G/250G 满导致 step 23/28 崩溃。根因：TRL 每实验保存 3 份模型权重（~48GB）+ completions parquet（~2.5GB）。）\n- **C004**: 跨 seed/跨 run 的 ISR 对比必须使用 eval_sta.py 统一评估，禁止引用训练日志 ISR 做跨 run 对比（不同 run 可能使用不同版本的 ISR 计算代码）（原因：Reviewer 核实发现 plan001-s42-r2 训练日志 ISR 使用 binary _fast_fn，plan001-s43-r4 使用 full STA _full_fn，同一指标名下计算方法不同导致不可比。论文中所有 ISR 数据必须来自 eval_sta.py 统一评估。）\n- **C005**: 所有 worker（含 fix/ops 类）启动任何 Python 进程前必须显式设置 CUDA_VISIBLE_DEVICES，禁止裸跑（原因：fix worker 未设 CUDA_VISIBLE_DEVICES 导致测试进程泄漏到 cuda:1（plan017 训练卡），占用 8638 MiB 显存。2026-05-14 事故。）\n- **C006**: 论文讨论 ISR 时必须区分两种语义：exec-only 的 low ISR = 冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR = metric gaming（Goodhart 效应）。不可将 ISR 差异直接等同于 reasoning 能力差异。（原因：Reviewer 发现 Prolog exec-only 生成大量重复 ground facts（如 penguin(fido). 出现 3 次），per-clause ablation 下删任一重复不影响结果，ISR=0。这是冗余不是无推理。如不区分，审稿人会误读 ISR 差异。）\n- **C007**: kill_job 后必须 nvidia-smi 确认 GPU 释放，submit 前必须 nvidia-smi 确认目标 GPU 无残留进程（原因：同一 session 两次出现 kill tmux → Python orphan → 新实验 OOM 的 pattern。kill_job 只杀 tmux session 不杀进程组，submit_on_allocated 只检查 registry 不检查实际 GPU 占用。）\n- **C008**: 所有 eval 命令必须显式指定 --data_path data/proofwriter_fol_100.jsonl，禁止依赖默认值或使用 test_100.jsonl（原因：D063: exp1 系列 eval 使用了 test_100.jsonl（与论文数据集零重叠），导致结果不可比。C004 约束的加固版。） [来自 D063]\n- **C009**: 所有 eval 命令必须显式指定 --data_path data/proofwriter_fol_100.jsonl，禁止使用默认值或 test_100.jsonl（原因：exp1 系列 eval 使用了错误的 test_100.jsonl（与 plan 系列的 proofwriter_fol_100.jsonl 零重叠），导致跨系列数据不可比。违反 C004。） [来自 D062]\n- **C010**: 磁盘清理禁止删除 conclusion=success 且标记 needs-re-eval 的 checkpoint，删前必须检查 registry 状态（原因：disk-cleanup-v2 误删了 exp1-isr-b03-s43 和 exp1-random-b03-s43 的 checkpoint，导致必须重训。这两个 checkpoint 因 D062/D063 需要用正确测试集 re-eval。）\n- **C011**: 磁盘清理禁止删除 conclusion=success 且标记 needs-re-eval 的 checkpoint 目录（原因：disk-cleanup-v2 Worker 误删 exp1_isr_b03_s43 和 exp1_random_b03_s43 checkpoint，导致必须重训。清理前必须交叉检查 registry 中 re-eval 标记。）\n- **C012**: Resume 训练时必须验证步数语义：--model_path 指向 checkpoint 时，确认 train_grpo.py 是从该 step 继续（resume）还是从 0 开始新训练。如不确定，从 base model 重新训练，不用 checkpoint。禁止第三次犯 resume 步数不对等错误。（原因：Agent 两次将 checkpoint-350 作为 model_path 启动 1000 步训练，实际训练了 1350 步（350+1000）而非 resume 到 1000 步，导致与 ISR 1000 步实验不可比。plan018-r2 数据作废。）\n- **C013**: Taxonomy 标准：genuine = proved − H7 − H1_exact − H8。H1-near 保留为 genuine 但单独标记。ISR 和 Random 两侧必须对称使用同一标准。（原因：D084 决策。H8 是退化证明必须扣除；H1-near 仍需推理步骤保留为 genuine；标准必须两侧对称以确保论文方法论一致性。） [来自 D084]\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：TeX 源文件最终校对\n\n对论文 TeX 源文件做投稿前最终校对，检查文本质量和数据一致性。\n\n### 文件位置\n论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/`\n主要 TeX 文件：`main.tex`, `experiments.tex`, `method.tex`, `conclusion.tex`, `appendix.tex`\n\n### 校对维度\n\n**1. 语言质量**\n- 语法错误、拼写错误\n- 用词不一致（同一概念在不同位置用了不同术语）\n- 缩略语首次出现是否有定义\n- 被动/主动语态一致性\n\n**2. 数字一致性**\n- 跨章节引用的数字是否一致（如 intro 提到的数字和 experiments 中的数字）\n- 表格中的数字和正文引用是否匹配\n- 百分比计算是否正确\n\n**3. 关键约束验证**\n以下是已确认的硬约束，检查论文是否严格遵守：\n- H7a（text-match tautology）是 GRPO 通用现象（非 ISR 独有），ISR 放大 5 倍\n- H7b（obfuscated tautology）是 ISR-specific\n- genuine rate ISR 6.06% vs Random 9.54%，p=0.182 不显著——不可 claim 显著差异\n- Random H7 pooled 13.7% 由 s43-r3 单 seed 贡献（38.3%），s42/s44-r2=0%——必须同时报 per-seed 和 pooled\n- premise-count-matched ISR 优势仅 1.06x（2.4x 已作废）\n- GC4-par 和 GC4-seq 不可直接对比\n- genuine = proved − |H7 ∪ H1 ∪ H8|（集合排除）\n\n**4. 引用完整性**\n- 所有 \\cite{} 是否有对应 bib 条目\n- 所有 \\ref{} / \\label{} 是否配对\n- 无 [?] 未解析标记\n\n**5. 格式检查**\n- Section/subsection 编号连续\n- Figure/Table caption 完整且信息充分\n- 脚注使用合理\n\n### 产出格式\n```\n## TeX 校对报告\n\n**检查文件数**: N\n**整体评价**: [PASS / 需修正]\n\n### 发现\n- [文件:行号] [severity] 具体问题描述\n\n### 硬约束违规（如有）\n- [文件:行号] 违反了哪条约束，当前文本 vs 正确表述\n\n### 建议修正\n- 优先级排序\n```"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T23:01:45.359Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T23:01:45.359Z",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb"
}
```

---

## Round 1

52 recorded events

### User

_source line 3 · 2026-05-15T23:01:45.397Z_

&lt;project_context>
# 项目: solver-trace-ablation

## 运行环境
- 服务器名: westd-39279
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/solver-trace-ablation

## ⚠️ 活跃约束（必须遵守）

- **C001**: 所有实验统一使用 data/train_500_seed42.jsonl 作为训练数据，禁止使用 proofwriter_fol_500.jsonl 或其他数据文件（原因：Reviewer CRITICAL: plan001-s43 使用了不同数据文件导致多 seed 对比 confound。多 seed 实验必须控制数据变量，seed 仅控制模型初始化和训练随机性。）
- **C002**: 提交训练任务前必须用 export CUDA_VISIBLE_DEVICES=N 显式设置 GPU，禁止 inline 赋值（bash -c VAR=X cmd），提交后验证 nvidia-smi 确认只占用分配的 GPU（原因：plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43 OOM 死亡。这是第二次 GPU 冲突事故。）
- **C003**: 训练配置必须设置 save_total_limit=1 且禁用/限制 completions parquet 保存，防止磁盘耗尽（原因：plan013-r3 和 plan001-s43-r3 因磁盘 250G/250G 满导致 step 23/28 崩溃。根因：TRL 每实验保存 3 份模型权重（~48GB）+ completions parquet（~2.5GB）。）
- **C004**: 跨 seed/跨 run 的 ISR 对比必须使用 eval_sta.py 统一评估，禁止引用训练日志 ISR 做跨 run 对比（不同 run 可能使用不同版本的 ISR 计算代码）（原因：Reviewer 核实发现 plan001-s42-r2 训练日志 ISR 使用 binary _fast_fn，plan001-s43-r4 使用 full STA _full_fn，同一指标名下计算方法不同导致不可比。论文中所有 ISR 数据必须来自 eval_sta.py 统一评估。）
- **C005**: 所有 worker（含 fix/ops 类）启动任何 Python 进程前必须显式设置 CUDA_VISIBLE_DEVICES，禁止裸跑（原因：fix worker 未设 CUDA_VISIBLE_DEVICES 导致测试进程泄漏到 cuda:1（plan017 训练卡），占用 8638 MiB 显存。2026-05-14 事故。）
- **C006**: 论文讨论 ISR 时必须区分两种语义：exec-only 的 low ISR = 冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR = metric gaming（Goodhart 效应）。不可将 ISR 差异直接等同于 reasoning 能力差异。（原因：Reviewer 发现 Prolog exec-only 生成大量重复 ground facts（如 penguin(fido). 出现 3 次），per-clause ablation 下删任一重复不影响结果，ISR=0。这是冗余不是无推理。如不区分，审稿人会误读 ISR 差异。）
- **C007**: kill_job 后必须 nvidia-smi 确认 GPU 释放，submit 前必须 nvidia-smi 确认目标 GPU 无残留进程（原因：同一 session 两次出现 kill tmux → Python orphan → 新实验 OOM 的 pattern。kill_job 只杀 tmux session 不杀进程组，submit_on_allocated 只检查 registry 不检查实际 GPU 占用。）
- **C008**: 所有 eval 命令必须显式指定 --data_path data/proofwriter_fol_100.jsonl，禁止依赖默认值或使用 test_100.jsonl（原因：D063: exp1 系列 eval 使用了 test_100.jsonl（与论文数据集零重叠），导致结果不可比。C004 约束的加固版。） [来自 D063]
- **C009**: 所有 eval 命令必须显式指定 --data_path data/proofwriter_fol_100.jsonl，禁止使用默认值或 test_100.jsonl（原因：exp1 系列 eval 使用了错误的 test_100.jsonl（与 plan 系列的 proofwriter_fol_100.jsonl 零重叠），导致跨系列数据不可比。违反 C004。） [来自 D062]
- **C010**: 磁盘清理禁止删除 conclusion=success 且标记 needs-re-eval 的 checkpoint，删前必须检查 registry 状态（原因：disk-cleanup-v2 误删了 exp1-isr-b03-s43 和 exp1-random-b03-s43 的 checkpoint，导致必须重训。这两个 checkpoint 因 D062/D063 需要用正确测试集 re-eval。）
- **C011**: 磁盘清理禁止删除 conclusion=success 且标记 needs-re-eval 的 checkpoint 目录（原因：disk-cleanup-v2 Worker 误删 exp1_isr_b03_s43 和 exp1_random_b03_s43 checkpoint，导致必须重训。清理前必须交叉检查 registry 中 re-eval 标记。）
- **C012**: Resume 训练时必须验证步数语义：--model_path 指向 checkpoint 时，确认 train_grpo.py 是从该 step 继续（resume）还是从 0 开始新训练。如不确定，从 base model 重新训练，不用 checkpoint。禁止第三次犯 resume 步数不对等错误。（原因：Agent 两次将 checkpoint-350 作为 model_path 启动 1000 步训练，实际训练了 1350 步（350+1000）而非 resume 到 1000 步，导致与 ISR 1000 步实验不可比。plan018-r2 数据作废。）
- **C013**: Taxonomy 标准：genuine = proved − H7 − H1_exact − H8。H1-near 保留为 genuine 但单独标记。ISR 和 Random 两侧必须对称使用同一标准。（原因：D084 决策。H8 是退化证明必须扣除；H1-near 仍需推理步骤保留为 genuine；标准必须两侧对称以确保论文方法论一致性。） [来自 D084]


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：TeX 源文件最终校对

对论文 TeX 源文件做投稿前最终校对，检查文本质量和数据一致性。

### 文件位置
论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/`
主要 TeX 文件：`main.tex`, `experiments.tex`, `method.tex`, `conclusion.tex`, `appendix.tex`

### 校对维度

**1. 语言质量**
- 语法错误、拼写错误
- 用词不一致（同一概念在不同位置用了不同术语）
- 缩略语首次出现是否有定义
- 被动/主动语态一致性

**2. 数字一致性**
- 跨章节引用的数字是否一致（如 intro 提到的数字和 experiments 中的数字）
- 表格中的数字和正文引用是否匹配
- 百分比计算是否正确

**3. 关键约束验证**
以下是已确认的硬约束，检查论文是否严格遵守：
- H7a（text-match tautology）是 GRPO 通用现象（非 ISR 独有），ISR 放大 5 倍
- H7b（obfuscated tautology）是 ISR-specific
- genuine rate ISR 6.06% vs Random 9.54%，p=0.182 不显著——不可 claim 显著差异
- Random H7 pooled 13.7% 由 s43-r3 单 seed 贡献（38.3%），s42/s44-r2=0%——必须同时报 per-seed 和 pooled
- premise-count-matched ISR 优势仅 1.06x（2.4x 已作废）
- GC4-par 和 GC4-seq 不可直接对比
- genuine = proved − |H7 ∪ H1 ∪ H8|（集合排除）

**4. 引用完整性**
- 所有 \cite{} 是否有对应 bib 条目
- 所有 \ref{} / \label{} 是否配对
- 无 [?] 未解析标记

**5. 格式检查**
- Section/subsection 编号连续
- Figure/Table caption 完整且信息充分
- 脚注使用合理

### 产出格式
```
## TeX 校对报告

**检查文件数**: N
**整体评价**: [PASS / 需修正]

### 发现
- [文件:行号] [severity] 具体问题描述

### 硬约束违规（如有）
- [文件:行号] 违反了哪条约束，当前文本 vs 正确表述

### 建议修正
- 优先级排序
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "type": "user",
  "uuid": "1e6ab607-5c3e-4aa9-a03b-a340f3f7b7dc",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T23:01:45.396Z_

```json
{
  "parentUuid": "1e6ab607-5c3e-4aa9-a03b-a340f3f7b7dc",
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
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "e6161238-19f4-45e7-923f-d8d60f5fb8f7",
  "timestamp": "2026-05-15T23:01:45.396Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T23:01:45.396Z_

```json
{
  "parentUuid": "e6161238-19f4-45e7-923f-d8d60f5fb8f7",
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
  "uuid": "d04e9bed-52ab-4b60-8066-1c51a7c786df",
  "timestamp": "2026-05-15T23:01:45.396Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T23:01:45.396Z_

```json
{
  "parentUuid": "d04e9bed-52ab-4b60-8066-1c51a7c786df",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4c7b0ec2-58ae-4eee-907f-17871d254412",
  "timestamp": "2026-05-15T23:01:45.396Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Final TeX proofreading for paper submission",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb"
}
```

---

### Assistant

_source line 8 · 2026-05-15T23:01:48.580Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to proofread the TeX source files for their paper before submission. I need to read all the main TeX files and check for language quality, numerical consistency, constraint violations, citation completeness, and formatting issues.

Let me start by reading all the TeX files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c7b0ec2-58ae-4eee-907f-17871d254412",
  "isSidechain": false,
  "requestId": "req_011Cb5BpAn6UkyuzB32XK6pM",
  "type": "assistant",
  "uuid": "2ca6e6fc-28a1-4b7d-baf1-7950ad65f393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tu2D8BVejKskNpKN98Mgc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14408,
      "cache_read_input_tokens": 11841,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14408
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

_source line 9 · 2026-05-15T23:01:49.125Z_

读取所有 TeX 源文件和相关数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ca6e6fc-28a1-4b7d-baf1-7950ad65f393",
  "isSidechain": false,
  "requestId": "req_011Cb5BpAn6UkyuzB32XK6pM",
  "type": "assistant",
  "uuid": "15396357-eaea-43f0-97de-88a162f09f9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tu2D8BVejKskNpKN98Mgc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14408,
      "cache_read_input_tokens": 11841,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14408
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

_source line 10 · 2026-05-15T23:01:49.820Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PzTXaH2swu6AHotdo2mbjG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15396357-eaea-43f0-97de-88a162f09f9d",
  "isSidechain": false,
  "requestId": "req_011Cb5BpAn6UkyuzB32XK6pM",
  "type": "assistant",
  "uuid": "1b194a8d-9f94-4df0-9ed4-f6bfdf1becd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tu2D8BVejKskNpKN98Mgc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14408,
      "cache_read_input_tokens": 11841,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14408
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

_source line 11 · 2026-05-15T23:01:49.831Z_

<details><summary>↩ Tool result · `toolu_01PzTXaH2swu6AHotdo2mbjG`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{limitations}
38	
39	\appendix
40	\input{appendix}
41	
42	\end{document}
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b194a8d-9f94-4df0-9ed4-f6bfdf1becd3",
  "isSidechain": false,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "type": "user",
  "uuid": "d7265f46-b81f-467c-aa69-1efbbee0bfa9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\\usepackage{enumitem}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage[protrusion=true,expansion=false]{microtype}\n\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\intextsep}{6pt plus 2pt minus 2pt}\n\\setlength{\\abovecaptionskip}{4pt}\n\\setlength{\\belowcaptionskip}{2pt}\n\n\\graphicspath{{figures/}}\n\n\\title{Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer}\n\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\input{limitations}\n\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  },
  "sourceToolAssistantUUID": "1b194a8d-9f94-4df0-9ed4-f6bfdf1becd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T23:01:50.308Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KNWXfE2Yr4ipJo6Re1naMW`</summary>

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
  "parentUuid": "d7265f46-b81f-467c-aa69-1efbbee0bfa9",
  "isSidechain": false,
  "requestId": "req_011Cb5BpAn6UkyuzB32XK6pM",
  "type": "assistant",
  "uuid": "e3968725-2a34-41fa-822f-830cf04fa670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tu2D8BVejKskNpKN98Mgc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14408,
      "cache_read_input_tokens": 11841,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14408
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

_source line 13 · 2026-05-15T23:01:50.314Z_

<details><summary>↩ Tool result · `toolu_01KNWXfE2Yr4ipJo6Re1naMW`</summary>

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
165	The eight modes (Table~\ref{tab:hacking-taxonomy}; definitions in Appendix~\ref{app:hacking-modes}) span 2 logic types and 6 reward conditions.
166	The three dominant modes---\textbf{H1} (conclusion embedding, GRPO-universal at $68$--$100\%$), \textbf{H7} (conclusion duplication, ISR-amplified ${\sim}5\times$; Fisher $p{=}1.3{\times}10^{-39}$), and \textbf{H8} (premise-subset gaming; Appendix~\ref{app:h8})---account for $>90\%$ of hacking.
167	H7 includes an obfuscated subtype \textbf{H7b} ($14/231$) that evades text-match classifiers via vacuous quantifier wrapping, simultaneously gaming execution reward, ISR, and the hacking detector (\S\ref{sec:discussion}).
168	The cross-condition pattern: \emph{reward formulation determines hacking composition but not prevalence}---all GRPO conditions show $\geq 80\%$ pooled hacking; only SFT achieves $92.3\%$ non-hacking.
169	No GRPO condition produces a high-PR, majority non-hacking run; the taxonomy is descriptive, not exhaustive (query-as-fact gaming was discovered only via functional cross-validation).
170	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3968725-2a34-41fa-822f-830cf04fa670",
  "isSidechain": false,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "type": "user",
  "uuid": "cbc706a8-dc71-414d-a827-354f19ef1265",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits meta-level Goodhart's Law (\\S\\ref{sec:goodhart}); and STA as a cross-logic protocol (\\S\\ref{sec:crosslogic}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}8$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline is trained with NLL on gold formalizations.\\footnote{All experiments use \\texttt{data/train\\_500\\_seed42.jsonl}; seeds control initialization and rollout sampling only.}\nHeld-out evaluation uses 100 FOLIO examples (\\texttt{proofwriter\\_fol\\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\\texttt{eval\\_sta.py}) so training-log ISR is never compared across runs.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary but not sufficient condition for semantic correctness.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$93\\%$\\to$96\\% while proved-only ISR falls $0.642{\\to}0.132{\\to}0.003$ over 100$\\to$500$\\to$1000 steps. By step 1000, 94.8\\% of proved samples have $\\text{ISR}{=}0$ and mean component count inflates 6.58$\\to$18.55 (contradiction explosion).}\n\\label{fig:isr-collapse}\n\\end{figure}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory execution-only evaluation would read as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (H1); by 1000 steps the embedding rate saturates at 100\\% and mean component count more than doubles ($6.58\\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.\nExtended training, lacking a structural signal, \\emph{worsens} formalization quality while improving the headline number.\n\n\\textbf{Cross-seed instability.}\nThe three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\\ref{app:detailed-results}): s42 reaches $\\text{PR}{=}93\\%$ via conclusion embedding ($\\text{H1}{=}87\\%$); s43 collapses to $\\text{PR}{=}13\\%$ via repetition (87\\% of rollouts truncated); s44 reaches $\\text{PR}{=}98\\%$ via tautological collapse ($\\text{H7}{=}100\\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44\nThe cross-seed PR variance ($\\sigma{=}47$\\,pp) shows aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).\nBy 1000 steps, all three converge to high PR ($0.95{\\pm}0.05$) but $0\\%$ non-hacking (15 samples escape text-match classifiers but are functionally degenerate; see Appendix~\\ref{app:h8} and Table~\\ref{tab:fol-detailed}), each through a different dominant mode (s42: H1 saturation; s43: H7 tautology; s44: H1+H8). %% registry: plan016-extended-1000-s42, plan001-exec-only-s43-1000-r2, plan001-exec-only-s44-1000-r2\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $\\text{PR}{=}13.0\\%$ (3-seed pooled, 1000 steps) with $\\text{H7}{=}0$, $\\text{H1}{=}7.7\\%$, $92.3\\%$ non-hacking ($n{=}39$; per-seed range 91--93\\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\nThe near-absence of hacking under identical data exposure is consistent with hacking being RL-specific.\nA 100-step RL checkpoint (Appendix~\\ref{app:100step}) at $\\text{PR}{=}32\\%$ already shows 31.2\\% hacking (vs.\\ SFT's 7.7\\%), indicating reward hacking emerges early in RL training, not merely at high PR.\n\n\\subsection{Meta-Level Goodhart's Law}\n\\label{sec:goodhart}\n\nWe now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with a matched random control, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,u)$, $u\\sim\\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.\nThe headline finding: ISR-as-reward produces \\emph{meta-level} Goodhart~\\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)\nISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 12 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}}\n\\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std of per-seed values. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ omitted for ISR $\\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\\times$ random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}). $^\\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random H7 driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}.}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-amplified gaming.}\nH7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\\sim}5\\times$: $70.6\\%$ ($163/231$) under ISR vs.\\ $13.7\\%$ ($36/262$) under random (Fisher $p{=}1.3{\\times}10^{-39}$, $\\text{OR}{=}15.05$). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nRandom H7 is highly seed-dependent: $38.3\\%$ in seed~43 vs.\\ $0\\%$ in seeds~42 and~44; ISR makes H7 near-deterministic ($2/3$ seeds at $97$--$100\\%$, Table~\\ref{tab:fol-detailed}).\nH7---a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by construction (\\S\\ref{sec:taxonomy-method})---is the canonical meta-level Goodhart move: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$100\\%$ across both conditions, and is in fact \\emph{higher} under random (pooled H1 $71\\%$ vs.\\ $18\\%$ under ISR).\nISR does not reduce hacking; it converts H1 into H7 (Figure~\\ref{fig:hacking-composition}).\nRandom also yields higher and more stable PR ($87{\\pm}8\\%$ vs.\\ $77{\\pm}14\\%$).\n\n\\textbf{Premise-count confound.}\nThe one ISR seed not dominated by H7 (s42) has raw $\\text{ISR}^{*}{=}0.415$, $3.2\\times$ its random control ($0.131$), suggesting genuine improvement.\nThis appearance is a premise-minimization artifact: ISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\\ $8.46$ for random), and ISR rises mechanically as $n$ falls---when $n{=}2$, $\\text{ISR}\\geq 0.5$ by definition.\nRestricting to non-hacking samples with $\\geq{3}$ premises (eliminating the trivial-$n$ regime) gives $\\text{ISR}^{*}{=}0.258$ for ISR vs.\\ $0.243$ for random: a $1.06\\times$ ratio, no meaningful advantage. %% D051 premise-count-matched analysis\nAfter reclassifying premise-subset gaming (H8; Appendix~\\ref{app:h8}) and correcting H7 classifier false negatives (s44, $n{=}12$; Appendix~\\ref{app:hacking-modes}), ISR $\\beta{=}0.1$ non-hacking rate ($6.06\\%$, $14/231$) is numerically lower than random ($9.5\\%$, $25/262$), but the difference is not statistically significant (Fisher $p{=}0.182$, two-sided, n.s.; Wilson 95\\% CI: ISR $[3.6\\%, 9.9\\%]$, Random $[6.5\\%, 13.7\\%]$; Appendix Table~\\ref{tab:bootstrap-ci}). %% D095 FINAL Fisher test\nThe key asymmetry is not in non-hacking rates but in gaming \\emph{composition}: ISR converts stochastic H7 into near-deterministic convergence ($2/3$ seeds ${\\geq}97\\%$), while random H7 remains seed-dependent and H1-dominated.\nThe raw $3.2\\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{Training ISR trajectories across reward conditions. ISR $\\beta{=}0.1$ seeds rise rapidly toward $\\text{ISR}{\\approx}1$ (meta-Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\\text{ISR}{\\geq}0.5$ by construction), not genuine structural quality; random $\\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\n\\textbf{Temporal collapse under ISR $\\beta{=}0.1$.}\nFigure~\\ref{fig:training-isr-curves} traces training ISR across conditions.\nExtended training (1000 steps) reveals that ISR $\\beta{=}0.1$'s genuine rate at 500 steps ($17.3\\%$, seed~42) is transient: by step 1000, H7 gaming escalates from $16.0\\%$ to $96.7\\%$ while genuine rate collapses to $2.2\\%$ ($n_{\\text{comp}}$: $5.58{\\to}2.89$).\nThe optimization converges to a fixed point where $\\text{ISR}^{*}{=}0.88$, superficially suggesting structural improvement but reflecting near-complete tautological gaming.\nThis mirrors the exec-only 1000-step trajectory (\\S\\ref{sec:diagnostic}): both converge to ${\\sim}0\\%$ genuine proofs despite opposite ISR values ($0.88$ vs.\\ $0.003$), demonstrating that ISR is gamed upward under ISR-as-reward and downward under exec-only---two paths to the same structural collapse. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\n\n\\textbf{High-dose ISR ($\\beta{=}0.3$): multi-modal Goodhart.}\nAt $\\beta{=}0.3$, ISR-as-reward produces extreme cross-seed instability ($\\text{PR}{=}66{\\pm}42\\%$, spanning 18--95\\%); each seed converges to a distinct pathway (Appendix~\\ref{app:detailed-results}). %% registry: plan002-additive-b03-s42/s43/s44\nSeed~42: \\emph{reward collapse} ($\\text{PR}{=}18\\%$), the classical pattern of~\\citep{gao-reward-overoptimization}.\nSeed~43: \\emph{H1 shortcutting} ($\\text{PR}{=}86\\%$, $\\text{H1}{=}69\\%$, only $27\\%$ non-hacking).\nSeed~44: \\emph{pure H7 meta-Goodhart} ($\\text{PR}{=}95\\%$, $\\text{H7}{=}100\\%$, $\\text{ISR}^{*}{=}0.742$, $0\\%$ non-hacking)---simultaneously gaming \\emph{both} execution and structural metrics through the same construction.\nThe random control at $\\beta{=}0.3$ is equally unstable ($\\text{PR}{=}54{\\pm}35\\%$, spanning 23--92\\%) with near-universal H1 hacking ($91\\%$, pooled) and ${\\leq}4\\%$ non-hacking per seed; high-dose proxy weighting destabilizes training regardless of signal source; ISR produces diverse failure modes (reward collapse, H1 shortcutting, H7 meta-Goodhart) while random converges to H1-dominated hacking with sporadic H7 ($7\\%$ pooled, $0$--$7$ H7a per seed) (Appendix~\\ref{app:beta03}).\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Left}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$). \\textbf{Right}: Prolog ISR-reward gaming-mode composition---all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\nWe replicate the FOL pipeline with Prolog/SWI-Prolog: (i) does ISR retain diagnostic value on a structurally different logic; (ii) does ISR-as-reward reproduce meta-level Goodhart?\nDetailed per-seed numbers are in Appendix Table~\\ref{tab:prolog-detailed}.\n\n\\textbf{Prolog exec-only: ISR catches redundancy across logics.}\nTwo of three seeds (s42, s43) show $\\text{ISR}^{*}{\\approx}0$ despite moderate-to-high PR (0.83, 0.56). %% registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3\nInspection reveals \\emph{redundant coding}: ground facts repeated multiple times (e.g., \\texttt{penguin(fido).} appearing three times), so per-clause LOO never breaks the proof.\nThis is a different failure semantics from FOL exec-only (conclusion embedding), but $\\text{ISR}^{*}$ flags both.\nWe are careful to distinguish: exec-only \\emph{low} ISR signals \\emph{redundancy}; ISR-rewarded \\emph{high} ISR signals \\emph{metric gaming} (\\S\\ref{sec:taxonomy-method})---the same number does not license the same reasoning-quality conclusion.\n\n\\textbf{Prolog ISR-as-reward: universal Goodhart.}\nThe Prolog result is stronger than FOL: 3/3 seeds reach $0\\%$ non-hacking via three distinct mechanisms (Figure~\\ref{fig:prolog-comparison}).\nSeed~42: clean H7 tautologies ($\\text{ISR}^{*}{=}1.0$, all $50/100$ proved). %% registry: plan006-prolog-sta-s42\nSeed~43: \\emph{degenerate uppercase pseudo-Prolog} (e.g., \\texttt{MARY\\_IS\\_AN\\_AVA\\-DEOTE.}); strict text-match returns $\\text{H7}{=}0$ but functional analysis shows all 38 proved samples have $n_{\\text{necessary}}{=}1$ (functionally H7). %% registry: plan006-prolog-sta-s43\nSeed~44: \\emph{query-as-fact gaming}---the model transforms the NL question into a snake-case atom asserted as both fact and query (e.g., \\texttt{is\\_the\\_dog\\_furry.} as both fact and query), with $95/97$ proved samples at $n_{\\text{necessary}}{=}1$. %% registry: plan006-prolog-sta-s44\nSeed~44 evaded our initial strict classifier (reported $100\\%$ genuine); functional cross-validation exposed it---a methodological lesson that text-match classifiers have blind spots and STA's necessity profile is the cross-check.\nWe attribute Prolog's stronger collapse to its simpler operational semantics: a broader gaming basin makes the genuine residual disappear---corroborating evidence for Claim 2.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts H1 into more extreme H7 without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nH1 embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nH7 duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nH8 prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThe eight modes (Table~\\ref{tab:hacking-taxonomy}; definitions in Appendix~\\ref{app:hacking-modes}) span 2 logic types and 6 reward conditions.\nThe three dominant modes---\\textbf{H1} (conclusion embedding, GRPO-universal at $68$--$100\\%$), \\textbf{H7} (conclusion duplication, ISR-amplified ${\\sim}5\\times$; Fisher $p{=}1.3{\\times}10^{-39}$), and \\textbf{H8} (premise-subset gaming; Appendix~\\ref{app:h8})---account for $>90\\%$ of hacking.\nH7 includes an obfuscated subtype \\textbf{H7b} ($14/231$) that evades text-match classifiers via vacuous quantifier wrapping, simultaneously gaming execution reward, ISR, and the hacking detector (\\S\\ref{sec:discussion}).\nThe cross-condition pattern: \\emph{reward formulation determines hacking composition but not prevalence}---all GRPO conditions show $\\geq 80\\%$ pooled hacking; only SFT achieves $92.3\\%$ non-hacking.\nNo GRPO condition produces a high-PR, majority non-hacking run; the taxonomy is descriptive, not exhaustive (query-as-fact gaming was discovered only via functional cross-validation).\n",
      "numLines": 170,
      "startLine": 1,
      "totalLines": 170
    }
  },
  "sourceToolAssistantUUID": "e3968725-2a34-41fa-822f-830cf04fa670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T23:01:50.811Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MBaivHxpTdCWVvQkT5n5YW`</summary>

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
  "parentUuid": "cbc706a8-dc71-414d-a827-354f19ef1265",
  "isSidechain": false,
  "requestId": "req_011Cb5BpAn6UkyuzB32XK6pM",
  "type": "assistant",
  "uuid": "0361b90d-e6ec-4372-8937-4a4f59bf85e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tu2D8BVejKskNpKN98Mgc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14408,
      "cache_read_input_tokens": 11841,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14408
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

_source line 15 · 2026-05-15T23:01:50.816Z_

<details><summary>↩ Tool result · `toolu_01MBaivHxpTdCWVvQkT5n5YW`</summary>

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
26	LOO ablation itself is standard in mutation testing, sensitivity analysis, and feature attribution~\citep{demillo1978, sundararajan-ig, lundberg-shap}; our novelty is its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
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
  "parentUuid": "0361b90d-e6ec-4372-8937-4a4f59bf85e8",
  "isSidechain": false,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "type": "user",
  "uuid": "5e5a1ed9-5c0c-4dea-aeff-ac7c133144df",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.92\\textwidth]{figures/fig1_sta_overview.pdf}\n\\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\\ as reward: when the diagnostic becomes the target, meta-level Goodhart's Law emerges.}\n\\label{fig:sta-overview}\n\\end{figure*}\n\n\\subsection{Task and GRPO Training}\n\\label{sec:task}\n\nGiven premises $P_1,\\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\\{c_1,\\ldots,c_n\\}$ verified by an external solver $S\\in\\{\\text{Prover9, SWI-Prolog}\\}$ (Figure~\\ref{fig:sta-overview}a).\nWe train with GRPO~\\citep{deepseekmath} ($K{=}8$), where each rollout receives binary execution reward $r_{\\text{exec}}(x) = \\mathbf{1}[S(F_x){=}\\textit{proved}]$.\nThis optimizes prove rate but provides no signal about \\emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.\nAll experiments draw from FOLIO~\\citep{folio}; the held-out evaluation file retains a legacy \\texttt{proofwriter\\_fol\\_*.jsonl} filename (from ProofWriter~\\citep{proofwriter}) but contains only FOLIO-derived examples.\n\n\\subsection{Solver Trace Ablation (STA)}\n\\label{sec:sta}\n\nSTA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\\ref{fig:sta-overview}b).\nGiven a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\\setminus\\{c_i\\}$ and re-runs the solver (Algorithm~\\ref{alg:sta}).\nA component is \\emph{necessary} if its removal causes proof failure.\nWhat constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.\nLOO ablation itself is standard in mutation testing, sensitivity analysis, and feature attribution~\\citep{demillo1978, sundararajan-ig, lundberg-shap}; our novelty is its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.\n\n\\begin{algorithm}[t]\n\\caption{Solver Trace Ablation (STA)}\n\\label{alg:sta}\n\\begin{algorithmic}[1]\n\\REQUIRE Proved formalization $x = \\{c_1, \\ldots, c_n\\}$, solver $S$\n\\ENSURE $\\text{ISR}(x) \\in [0, 1]$\n\\STATE $\\textit{necessary} \\gets 0$\n\\FOR{$i = 1$ to $n$}\n    \\IF{$S(x \\setminus \\{c_i\\}) = \\textit{failed}$}\n        \\STATE $\\textit{necessary} \\gets \\textit{necessary} + 1$\n    \\ENDIF\n\\ENDFOR\n\\RETURN $\\textit{necessary} \\,/\\, n$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Intensional Structural Reward.}\nISR is the fraction of necessary components:\n\\begin{equation}\n  \\text{ISR}(x) = \\frac{1}{n}\\sum_{i=1}^{n}\\mathbf{1}\\bigl[S(x\\setminus\\{c_i\\})=\\textit{failed}\\bigr]\n  \\label{eq:isr}\n\\end{equation}\nISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.\nWe report \\emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating structural quality with prove rate.\n\n\\paragraph{Limitations of ISR.}\nISR measures syntactic component necessity, not semantic faithfulness: a formalization can achieve $\\text{ISR}{=}1$ while semantically unrelated to the NL input (e.g., a single premise identical to the conclusion).\nISR is also sensitive to component count $n$: when $n{=}2$, $\\text{ISR}\\geq 0.5$ regardless of proof quality.\nWe control for this confound via premise-count-matched analysis in \\S\\ref{sec:goodhart}.\nThe $O(n)$ per-clause LOO ablation is necessary: a cheaper $O(1)$ binary variant produces near-zero ISR scores ($\\text{ISR}^*{=}0.007$) indistinguishable from exec-only, because models generate redundant premise copies whose individual removal never changes the proof outcome.\nHowever, the $O(1)$ variant includes a tautology check (conclusion provable under empty premises $\\to$ ISR${=}0$) absent from exec-only, introducing a training-time confound that depresses prove rate ($63\\%$ vs.\\ $93\\%$ exec-only); the two conditions are therefore non-equivalent in training dynamics despite producing comparable ISR signals (Appendix~\\ref{app:o1-ablation}).\n\n\\subsection{Reward Conditions and Hacking Modes}\n\\label{sec:rewards}\n\\label{sec:taxonomy-method}\n\nWe study six conditions: exec-only ($r_{\\text{exec}}$), ISR low/high-dose ($r_{\\text{exec}}\\cdot(1{+}\\beta\\,\\text{ISR})$ at $\\beta\\in\\{0.1,0.3\\}$), matched random controls ($r_{\\text{exec}}\\cdot(1{+}\\beta u)$, $u\\sim\\mathcal{U}(0,1)$), and an SFT baseline (NLL on gold formalizations).\nMultiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.\nRandom isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.\nEach RL condition uses seeds $\\{42,43,44\\}$ and identical training data.\nAn earlier convex formulation ($\\alpha r_{\\text{exec}} + \\beta r_{\\text{exec}}\\text{ISR}$, $\\alpha{+}\\beta{=}1$) was discarded because $\\text{ISR}{<}1$ always penalized relative to exec-only, collapsing PR (Appendix~\\ref{app:setup}).\n\n\\paragraph{Hacking taxonomy.}\nAcross conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\\ref{app:hacking-modes}):\n\\textbf{H1} (conclusion embedded among multiple premises),\n\\textbf{H7} (single-premise conclusion duplication, subtypes H7a standard and H7b obfuscated tautology; targets the ISR signal directly, since removing the sole premise forces $\\text{ISR}\\geq 0.5$),\n\\textbf{H8} (premise-subset gaming: each component is LOO-necessary but the premise set is a strict subset of what the problem requires, inflating ISR without faithful reasoning; Appendix~\\ref{app:h8}),\n\\textbf{tautological collapse} (minimal two-component $P{\\to}P$ without explicit ISR inflation),\n\\textbf{repetition collapse} (identical clauses repeated to inflate component count),\n\\textbf{complexity-without-utility} (elaborate but vacuous premises),\n\\textbf{contradiction explosion} (contradictory premises trivializing any conclusion via \\emph{ex falso}), and\n\\textbf{query-as-fact gaming} (Prolog-specific: emit the NL question as an atom asserted as both fact and query; evades text-match classifiers).\nModes are identified by a two-stage procedure: strict normalized text matching (H1/H7) plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution (catches modes evading text matching).\nWe report both classifications in \\S\\ref{sec:experiments}.\n\nIn interpreting ISR results we distinguish two failure semantics that share a numerical signature: an exec-only \\emph{low} ISR signals \\emph{redundancy} (e.g., repeated ground facts in Prolog), whereas an ISR-rewarded \\emph{high} ISR signals \\emph{metric gaming} (H7-style constructions).\nA bare ISR difference therefore does not translate directly into a reasoning-ability difference; the mode breakdown is what licenses such interpretation.\n",
      "numLines": 85,
      "startLine": 1,
      "totalLines": 85
    }
  },
  "sourceToolAssistantUUID": "0361b90d-e6ec-4372-8937-4a4f59bf85e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T23:01:51.306Z_

<details open><summary>🔧 Tool call — Read · `toolu_013uvQr4BcZPfWEu1Yz4D1tM`</summary>

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
  "parentUuid": "5e5a1ed9-5c0c-4dea-aeff-ac7c133144df",
  "isSidechain": false,
  "requestId": "req_011Cb5BpAn6UkyuzB32XK6pM",
  "type": "assistant",
  "uuid": "fd724e54-5837-48d8-a1e9-3e67e5bdf94a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tu2D8BVejKskNpKN98Mgc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14408,
      "cache_read_input_tokens": 11841,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14408
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

_source line 17 · 2026-05-15T23:01:51.311Z_

<details><summary>↩ Tool result · `toolu_013uvQr4BcZPfWEu1Yz4D1tM`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides, while SFT localizes the failure to RL optimization (\S\ref{sec:diagnostic}).
5	Repurposed as a training signal, ISR induces meta-level Goodhart's Law: at $\beta{=}0.1$, it amplifies H7 tautological gaming ${\sim}5\times$ ($70.6\%$ vs.\ $13.7\%$ random, $p{<}10^{-38}$), and the sole apparent ISR gain vanishes ($1.06\times$) after controlling for premise count; at $\beta{=}0.3$, each seed converges to a distinct failure mode ($\text{PR}{=}66{\pm}42\%$).
6	The pattern transfers to Prolog (3/3 seeds, 0\% non-hacking) via distinct mechanisms including query-as-fact gaming that bypasses text-match classifiers (\S\ref{sec:taxonomy}).
7	ISR semantics are objective-dependent: exec-only \emph{low} ISR signals redundancy; ISR-rewarded \emph{high} ISR signals metric gaming.
8	
9	\paragraph{Classifier blind spots.}
10	H7b (obfuscated tautology) and Prolog query-as-fact gaming demonstrate that text-match classifiers have systematic blind spots exploitable by optimization.
11	In both cases, functional LOO analysis exposed gaming invisible to surface-level detection---H7b via vacuous quantifier wrapping ($10/12$ at $\text{ISR}{\geq}0.83$, triple gaming of execution, ISR, and classifier), query-as-fact via $95/97$ tautological samples the strict classifier labeled genuine (\S\ref{sec:crosslogic}).
12	Both cases argue for mandatory functional cross-validation of text-based hacking classifiers.
13	
14	\paragraph{Hacking mode switching.}
15	Under identical reward configurations, different seeds converge to qualitatively different modes (Table~\ref{tab:fol-detailed}): random $\beta{=}0.1$ ranges from H8-dominant (s44) to H7-dominant (s43) to highest non-hacking (s42); ISR $\beta{=}0.1$ similarly switches between H1-heavy (s42) and near-pure H7 (s43/s44, ${\geq}97\%$).
16	Single-seed results can therefore misrepresent a reward configuration's hacking profile; multi-seed evaluation with per-mode reporting should be standard.
17	
18	The asymmetry---reliable observer, unreliable optimizer---may generalize to other perturbation-based diagnostics; ISR and similar metrics should serve as post-hoc evaluation, with future work targeting gaming-robust rewards and broader logic types.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd724e54-5837-48d8-a1e9-3e67e5bdf94a",
  "isSidechain": false,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "type": "user",
  "uuid": "dc208c9f-eb66-4ba7-a496-bb80bf55901c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nSTA exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\\% collapse under exec-only GRPO that PR hides, while SFT localizes the failure to RL optimization (\\S\\ref{sec:diagnostic}).\nRepurposed as a training signal, ISR induces meta-level Goodhart's Law: at $\\beta{=}0.1$, it amplifies H7 tautological gaming ${\\sim}5\\times$ ($70.6\\%$ vs.\\ $13.7\\%$ random, $p{<}10^{-38}$), and the sole apparent ISR gain vanishes ($1.06\\times$) after controlling for premise count; at $\\beta{=}0.3$, each seed converges to a distinct failure mode ($\\text{PR}{=}66{\\pm}42\\%$).\nThe pattern transfers to Prolog (3/3 seeds, 0\\% non-hacking) via distinct mechanisms including query-as-fact gaming that bypasses text-match classifiers (\\S\\ref{sec:taxonomy}).\nISR semantics are objective-dependent: exec-only \\emph{low} ISR signals redundancy; ISR-rewarded \\emph{high} ISR signals metric gaming.\n\n\\paragraph{Classifier blind spots.}\nH7b (obfuscated tautology) and Prolog query-as-fact gaming demonstrate that text-match classifiers have systematic blind spots exploitable by optimization.\nIn both cases, functional LOO analysis exposed gaming invisible to surface-level detection---H7b via vacuous quantifier wrapping ($10/12$ at $\\text{ISR}{\\geq}0.83$, triple gaming of execution, ISR, and classifier), query-as-fact via $95/97$ tautological samples the strict classifier labeled genuine (\\S\\ref{sec:crosslogic}).\nBoth cases argue for mandatory functional cross-validation of text-based hacking classifiers.\n\n\\paragraph{Hacking mode switching.}\nUnder identical reward configurations, different seeds converge to qualitatively different modes (Table~\\ref{tab:fol-detailed}): random $\\beta{=}0.1$ ranges from H8-dominant (s44) to H7-dominant (s43) to highest non-hacking (s42); ISR $\\beta{=}0.1$ similarly switches between H1-heavy (s42) and near-pure H7 (s43/s44, ${\\geq}97\\%$).\nSingle-seed results can therefore misrepresent a reward configuration's hacking profile; multi-seed evaluation with per-mode reporting should be standard.\n\nThe asymmetry---reliable observer, unreliable optimizer---may generalize to other perturbation-based diagnostics; ISR and similar metrics should serve as post-hoc evaluation, with future work targeting gaming-robust rewards and broader logic types.\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  },
  "sourceToolAssistantUUID": "fd724e54-5837-48d8-a1e9-3e67e5bdf94a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T23:01:51.699Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Mj9QUJhsUnVB7fLWbaq6r2`</summary>

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
  "parentUuid": "dc208c9f-eb66-4ba7-a496-bb80bf55901c",
  "isSidechain": false,
  "requestId": "req_011Cb5BpAn6UkyuzB32XK6pM",
  "type": "assistant",
  "uuid": "df6c9525-331d-45f5-9c2a-cd45f254cfb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tu2D8BVejKskNpKN98Mgc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14408,
      "cache_read_input_tokens": 11841,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 460,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14408
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

_source line 19_

```json
{
  "type": "last-prompt",
  "leafUuid": "df6c9525-331d-45f5-9c2a-cd45f254cfb4",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Final TeX proofreading for paper submission",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb"
}
```

---

### Tool result

_source line 21 · 2026-05-15T23:01:51.974Z_

<details><summary>↩ Tool result · `toolu_01Mj9QUJhsUnVB7fLWbaq6r2`</summary>

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
112	\paragraph{H7 dose-response gradient.}
113	H7 tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ H7 ($36/262$ pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 H7a samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
114	The gradient---random $\beta{=}0.1$ ($13.7\%$) $\to$ random $\beta{=}0.3$ (4--7 H7a per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)---shows ISR transforms H7 from a seed-dependent GRPO tendency to a near-universal convergence direction.
115	
116	\paragraph{Meta-level Goodhart: implications.}
117	The meta-Goodhart finding extends beyond this specific system.
118	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.
119	The dose-response pattern ($\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\beta{=}0.3$: PR collapse to 18\% vs.\ 48\% random) maps onto the trajectory predicted by~\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.
120	$\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism; $\beta{=}0.3$ completes the Goodhart trajectory with outright performance collapse.
121	The practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.
122	
123	\paragraph{Single-seed unreliability.}
124	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
125	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\S\ref{sec:goodhart}).
126	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
127	
128	
129	\section{Hacking Mode Definitions}
130	\label{app:hacking-modes}
131	
132	We identify eight distinct reward hacking modes across all experiments.
133	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
134	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
135	
136	\begin{table}[h]
137	\centering
138	\small
139	\resizebox{\columnwidth}{!}{%
140	\begin{tabular}{@{}llcccc@{}}
141	\toprule
142	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
143	\midrule
144	H1 & Concl.\ in premises & 87 & 18 & 71 & 7 \\
145	H7 & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
146	H8 & Premise-subset gaming & 6 & 5 & -- & 0 \\
147	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
148	Repetition & Output degen. & $\bullet$ & -- & -- & -- \\
149	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & -- & -- & -- \\
150	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
151	Q-as-fact & Atom = fact+query & -- & -- & -- & -- \\
152	\bottomrule
153	\end{tabular}}
154	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. H7 includes subtypes H7a (text-match, $n{=}149$ ISR $+$ 36 random) and H7b (obfuscated tautology, $n{=}12$; ISR s44 only). $^\dagger$Random H7 driven by seed~43 (38.3\%); seeds~42/44: 0\%. Exec: H1${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). H8: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
155	\label{tab:hacking-taxonomy-app}
156	\end{table}
157	
158	\paragraph{Classifier Validation.}
159	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
160	H1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
161	No training data or manual annotation is used for classification.
162	
163	To estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
164	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
165	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
166	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
167	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
168	
169	\subsection{H8 --- Premise-Subset Gaming}
170	\label{app:h8}
171	
172	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (H1-style).
173	We term this \textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
174	
175	\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
176	Automated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.
177	
178	\paragraph{Audit scope and limitations.}
179	Full H8 audit was completed for ISR $\beta{=}0.1$ seed~42 only.
180	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their genuine rates may be overestimated.
181	Random $\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.
182	
183	\paragraph{H7 false-negative correction (H7b obfuscated tautology).}
184	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as genuine by the text matcher.
185	Manual inspection confirmed all 12 are logically equivalent to H7 but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
186	We classify these as \textbf{H7b} (obfuscated tautology), distinct from text-match-detectable H7a.
187	$10/12$ achieve $\text{ISR}{\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier---triple gaming (\S\ref{sec:taxonomy}).
188	After correction, ISR s44 genuine${=}0$; total H7 = H7a (77 text-match) + H7b (12 obfuscated) = 89.
189	
190	\paragraph{Impact on genuine-rate comparison.}
191	After H8 reclassification and H7 false-negative correction: ISR genuine $= 14/231 = 6.06\%$ vs.\ random genuine $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
192	The direction is consistent with ISR-amplified gaming modes (H7, H8) displacing genuine output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
193	
194	\subsection{H1 --- Conclusion Embedding}
195	
196	\paragraph{Definition.}
197	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
198	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
199	
200	\paragraph{Example (FOL).}
201	{\small\begin{verbatim}
202	Premises:
203	  all x (bird(x) -> flies(x)).
204	  bird(tweety).
205	  flies(tweety).  % conclusion embedded
206	Conclusion: flies(tweety).
207	\end{verbatim}}
208	
209	\paragraph{ISR interaction.}
210	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
211	ISR does not distinguish trivial from substantive necessity.
212	
213	\paragraph{Prevalence.}
214	Conclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\% across all RL conditions.
215	Under exec-only and Random reward, it manifests as H1 (71--93\%); under ISR reward, it shifts to H7 (70.6\% pooled).
216	
217	
218	\subsection{H7a --- Conclusion Duplication (Standard)}
219	
220	\paragraph{Definition.}
221	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
222	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
223	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
224	
225	\paragraph{Example (FOL).}
226	{\small\begin{verbatim}
227	Premises:
228	  all x ((A(x)&B(x))->(C(x)|D(x))).
229	Conclusion:
230	  all x ((A(x)&B(x))->(C(x)|D(x))).
231	\end{verbatim}}
232	
233	\paragraph{ISR interaction.}
234	ISR~$\approx 0.8$--$1.0$.
235	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
236	H7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.
237	
238	\paragraph{Prevalence.}
239	H7a (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
240	Combined H7 (H7a + H7b): 70.6\% (163/231; s43 H7a${=}59$ + H7b${=}2$; includes s44 FN correction).
241	Random~$\beta{=}0.1$ pooled: 13.7\% (36/262, all H7a; driven by seed~43 at 38.3\%, seeds~42 and~44 at 0\%).
242	
243	
244	\subsection{H7b --- Obfuscated Tautology}
245	
246	\paragraph{Definition.}
247	A single-premise formalization logically equivalent to H7a (premise = conclusion) but with surface-form differences that evade the text-match H7 classifier.
248	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
249	
250	\paragraph{Example (FOL, vacuous quantifier wrapping).}
251	{\small\begin{verbatim}
252	Premises:
253	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
254	Conclusion:
255	  all x ((A(x)&B(x))->(C(x)|D(x))).
256	\end{verbatim}}
257	The premise introduces a vacuous second quantifier variable $y$ that is immediately unified with $x$, making the formulas logically equivalent while differing textually.
258	
259	\paragraph{ISR interaction.}
260	$\text{ISR}{\geq}0.83$ ($10/12$ samples).
261	H7b simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match H7 classifier (surface-form difference evades detection).
262	This triple gaming makes H7b the most complete meta-Goodhart case we observe.
263	
264	\paragraph{Prevalence.}
265	Found exclusively in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as genuine).
266	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
267	
268	
269	\subsection{Tautological Collapse}
270	
271	\paragraph{Definition.}
272	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
273	
274	\paragraph{Example (FOL).}
275	\begin{verbatim}
276	Premises: p(a).
277	Conclusion: p(a).
278	\end{verbatim}
279	
280	\paragraph{ISR interaction.}
281	ISR~$=1.0$ (the sole premise is necessary).
282	Distinguished from H7 by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
283	
284	\paragraph{Prevalence.}
285	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% H7 by strict classifier).
286	Also observed in Prolog exec+STA seed~42 (100\% H7, PR~$=0.50$).
287	
288	
289	\subsection{Repetition Collapse}
290	
291	\paragraph{Definition.}
292	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
293	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
294	
295	\paragraph{Example (Prolog).}
296	\begin{verbatim}
297	penguin(fido).
298	penguin(fido).
299	penguin(fido).
300	... (repeated to 512 tokens)
301	query(penguin(fido)).
302	\end{verbatim}
303	
304	\paragraph{ISR interaction.}
305	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
306	ISR correctly diagnoses this degeneration.
307	
308	\paragraph{Prevalence.}
309	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
310	
311	
312	\subsection{Complexity-without-Utility}
313	
314	\paragraph{Definition.}
315	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.
316	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
317	
318	\paragraph{Example (FOL).}
319	{\small\begin{verbatim}
320	Premises:
321	  all x all y (R(x,y) ->
322	    exists z (S(x,z) & T(z,y))).
323	  all x (P(x) -> Q(x)).
324	  P(a).            % only this needed
325	Conclusion: Q(a).
326	\end{verbatim}}
327	
328	\paragraph{ISR interaction.}
329	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
330	This is the mode ISR is best calibrated for.
331	
332	\paragraph{Prevalence.}
333	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
334	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
335	
336	
337	\subsection{Contradiction Explosion}
338	
339	\paragraph{Definition.}
340	The component count grows unboundedly over training.
341	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
342	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
343	
344	\paragraph{Example (FOL, 1000-step exec-only).}
345	{\small\begin{verbatim}
346	Premises:
347	  c1. c2. c3. ... c18. % 18.55 mean
348	  % conclusion embedded among premises
349	Conclusion: Q(a).
350	\end{verbatim}}
351	
352	\paragraph{ISR interaction.}
353	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
354	
355	\paragraph{Prevalence.}
356	Observed in extended exec-only training (seed~42, 1000 steps).
357	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
358	
359	
360	\subsection{Query-as-Fact Gaming}
361	
362	\paragraph{Definition.}
363	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
364	Prolog trivially proves the query by unifying with the fact.
365	This mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.
366	
367	\paragraph{Example (Prolog).}
368	\begin{verbatim}
369	% NL: "Fido is happy."
370	% Model output:
371	fido_is_happy.
372	:- fido_is_happy.     % query = fact
373	\end{verbatim}
374	
375	\paragraph{ISR interaction.}
376	ISR~$\approx 0.9$--$1.0$.
377	The fact is necessarily necessary (its removal breaks the query), inflating ISR.
378	Functionally equivalent to H7 but with a distinct surface mechanism.
379	
380	\paragraph{Prevalence.}
381	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
382	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
383	
384	
385	\section{Per-Seed Detailed Results}
386	\label{app:detailed-results}
387	
388	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
389	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
390	ISR values are proved-only ISR$^*$.
391	
392	\begin{table*}[t]
393	\centering
394	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\S$s43-1000 raw ISR (0.531) includes ${+}12\%$ inflation from \texttt{decompose\_fol()} splitting $\exists x(\ldots)$ conclusions into quantifier + body as separate ablatable components; corrected ISR removes this artifact.}
395	\label{tab:fol-detailed}
396	\label{tab:fol-beta01-detailed}
397	\footnotesize
398	\setlength{\tabcolsep}{3pt}
399	\begin{tabular}{@{}llccccccl@{}}
400	\toprule
401	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
402	\midrule
403	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
404	Base model (no training)
405	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
406	Ground-truth FOL
407	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
408	SFT
409	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
410	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
411	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
412	\cmidrule(l){2-9}
413	  & \multicolumn{2}{l}{3-seed pooled} & \makebox[0pt][l]{$0.130$} & & \makebox[0pt][l]{$0.595$} & & \makebox[0pt][l]{\textbf{92.3}} & $n{=}39$ proved \\
414	\midrule
415	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
416	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
417	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\%$ \\
418	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
419	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
420	  & 43 & 1000 & 0.90 & 0.465$^\S$ & 100 & 0 & 0 & H7 dominant \\
421	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
422	  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & H8${=}15\%$ \\
423	\cmidrule(l){2-9}
424	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.68{\pm}0.47$} & & \makebox[0pt][l]{$0.238{\pm}0.30$} & & & 500-step \\
425	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.95{\pm}0.05$} & & \makebox[0pt][l]{$0.16{\pm}0.27$} & & \makebox[0pt][l]{$0.0{\pm}0.0$} & 1000-step \\
426	\midrule
427	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
428	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed H1+H7+H8 \\
429	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & H7a${=}59$, H7b${=}2$ \\
430	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & H7 dominant (FN corrected) \\
431	\cmidrule(l){2-9}
432	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.77{\pm}0.14$} & & \makebox[0pt][l]{$0.716{\pm}0.26$} & & & \\
433	\midrule
434	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
435	  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\
436	\midrule
437	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
438	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\
439	  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & H7a${=}36$; H8${=}1$ \\
440	  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & H8${=}16$ (H1$\cap$H8: 6) \\
441	\cmidrule(l){2-9}
442	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.87{\pm}0.08$} & & \makebox[0pt][l]{$0.117{\pm}0.042$} & & & H7 seed-dep.: 0/38/0\% \\
443	\midrule
444	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
445	  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086); $n_{\text{comp}} = 9.6$ \\
446	  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\text{genuine}}{=}3$ \\
447	  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\
448	\cmidrule(l){2-9}
449	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.54{\pm}0.35$} & & \makebox[0pt][l]{$0.09{\pm}0.09$} & & & \\
450	\bottomrule
451	\end{tabular}
452	\end{table*}
453	
454	
455	\begin{table*}[t]
456	\centering
457	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
458	\label{tab:prolog-detailed}
459	\small
460	\begin{tabular}{@{}llcccccl@{}}
461	\toprule
462	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
463	\midrule
464	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
465	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
466	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
467	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
468	\cmidrule(l){2-8}
469	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.53{\pm}0.31$} & & \makebox[0pt][l]{$0.146{\pm}0.21$} & & \\
470	\midrule
471	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
472	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & H7 tautological \\
473	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional H7$^a$ \\
474	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
475	\cmidrule(l){2-8}
476	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.62{\pm}0.31$} & & \makebox[0pt][l]{$0.699{\pm}0.45$} & & 3/3 Goodhart, 0\% non-hacking \\
477	\bottomrule
478	\end{tabular}
479	
480	\vspace{4pt}
481	{\footnotesize
482	$^a$ Strict H7 classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
483	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\
484	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
485	}
486	\end{table*}
487	
488	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
489	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
490	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
491	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.
492	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
493	
494	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
495	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
496	seed~42 produces clean H7 tautologies (single premise~$=$~conclusion),
497	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
498	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
499	The diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
500	
501	\subsection{Per-Seed Results at $\beta{=}0.3$}
502	\label{app:beta03}
503	
504	Table~\ref{tab:beta03-detailed} reports per-seed results for both ISR and Random reward at $\beta{=}0.3$.
505	The three ISR seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
506	
507	\begin{table}[h]
508	\centering
509	\caption{Per-seed results at $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H = percentage among proved samples.}
510	\label{tab:beta03-detailed}
511	\small
512	\begin{tabular}{@{}llcccccl@{}}
513	\toprule
514	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Mode} \\
515	\midrule
516	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
517	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); H8${=}3$ \\
518	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 26.7 & H1 shortcutting \\
519	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure H7 meta-Goodhart \\
520	\cmidrule(l){2-8}
521	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.66{\pm}0.42$} & & \makebox[0pt][l]{$0.39{\pm}0.31$} & & \\
522	\midrule
523	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
524	  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086) \\
525	  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\text{genuine}}{=}3$ \\
526	  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\
527	\cmidrule(l){2-8}
528	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.54{\pm}0.35$} & & \makebox[0pt][l]{$0.09{\pm}0.09$} & & \\
529	\bottomrule
530	\end{tabular}
531	\end{table}
532	
533	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
534	\label{app:100step}
535	
536	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%---higher than SFT (13.0\%, 3-seed pooled) but still early in training.
537	Of the 32 proved samples, 9 (28.1\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
538	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
539	This demonstrates that reward hacking emerges early in GRPO training---well before the prove-rate plateau---and is not simply an artifact of having more proved samples available for exploitation.
540	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
541	
542	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
543	\label{app:o1-ablation}
544	
545	To justify the per-clause LOO design (\S\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\text{fast\_ISR}(x) = 1$ if $x$ is proved \emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
546	The reward becomes $r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$.
547	After 500 steps (seed~42), this variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$---functionally zero---compared to $\text{ISR}^*{=}0.132$ under standard exec-only and $\text{ISR}^*{=}0.42$ under ISR $\beta{=}0.1$.
548	
549	\paragraph{ISR signal vs.\ training dynamics.}
550	At the \emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.
551	At the \emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.
552	This confound depresses prove rate by 30 percentage points ($63\%$ vs.\ $93\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.
553	The result confirms that the $O(n)$ per-clause ablation is necessary for ISR to carry a structural signal, while also showing that even a minimal tautology guard alters training dynamics substantially.
554	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df6c9525-331d-45f5-9c2a-cd45f254cfb4",
  "isSidechain": false,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "type": "user",
  "uuid": "11783de0-cc64-46b8-afa8-00d6e21b6c98",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 8 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\n\\section{STA Algorithm}\n\\label{app:algorithm}\n\nAlgorithm~\\ref{alg:sta} (Section~\\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.\nFor unproved samples ($S(x) \\neq \\textit{proved}$), ISR is undefined and the protocol is not applied.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures---and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness---whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$---even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}).\nThis bias is not specific to our setting---any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\n\n\\begin{table}[h]\n\\centering\n\\caption{Fisher exact tests for genuine rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ genuine rate is corrected for H8 reclassification and H7 false negatives (Appendix~\\ref{app:h8}).}\n\\label{tab:bootstrap-ci}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Genuine rate (H8+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\nISR vs.\\ Exec-only & 6.06\\% & 7.5\\% & 0.79 & 0.62 \\\\\nRandom vs.\\ Exec-only & 9.5\\% & 7.5\\% & 1.30 & 0.68 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{H7 gaming rate}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only genuine rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown.}\n\\end{table}\n\n\\paragraph{H7 dose-response gradient.}\nH7 tautology follows a dose-response pattern across reward conditions: random $\\beta{=}0.1$ produces $13.7\\%$ H7 ($36/262$ pooled; per-seed: $38.3\\%$ in s43, $0\\%$ in s42/s44), random $\\beta{=}0.3$ yields 4--7 H7a samples per seed, and ISR $\\beta{=}0.1$ reaches $70.6\\%$ ($163/231$).\nThe gradient---random $\\beta{=}0.1$ ($13.7\\%$) $\\to$ random $\\beta{=}0.3$ (4--7 H7a per seed) $\\to$ ISR $\\beta{=}0.1$ ($70.6\\%$)---shows ISR transforms H7 from a seed-dependent GRPO tendency to a near-universal convergence direction.\n\n\\paragraph{Meta-level Goodhart: implications.}\nThe meta-Goodhart finding extends beyond this specific system.\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern ($\\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\\beta{=}0.3$: PR collapse to 18\\% vs.\\ 48\\% random) maps onto the trajectory predicted by~\\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.\n$\\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism; $\\beta{=}0.3$ completes the Goodhart trajectory with outright performance collapse.\nThe practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\\S\\ref{sec:goodhart}).\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify eight distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\nTable~\\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nH1 & Concl.\\ in premises & 87 & 18 & 71 & 7 \\\\\nH7 & Single prem.\\ = concl. & $\\bullet$ & \\textbf{71} & 14$^\\dagger$ & 0 \\\\\nH8 & Premise-subset gaming & 6 & 5 & -- & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & -- & -- & -- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & -- & -- & -- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed pooled. H7 includes subtypes H7a (text-match, $n{=}149$ ISR $+$ 36 random) and H7b (obfuscated tautology, $n{=}12$; ISR s44 only). $^\\dagger$Random H7 driven by seed~43 (38.3\\%); seeds~42/44: 0\\%. Exec: H1${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). H8: premise-subset gaming (Appendix~\\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-detailed}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table}\n\n\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nH1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.\n\n\\subsection{H8 --- Premise-Subset Gaming}\n\\label{app:h8}\n\nManual audit of ISR $\\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (H1-style).\nWe term this \\textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.\n\n\\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\\text{prem}} \\leq 3$) that nonetheless achieve high ISR.\nAutomated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.\n\n\\paragraph{Audit scope and limitations.}\nFull H8 audit was completed for ISR $\\beta{=}0.1$ seed~42 only.\nISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their genuine rates may be overestimated.\nRandom $\\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.\n\n\\paragraph{H7 false-negative correction (H7b obfuscated tautology).}\nISR $\\beta{=}0.1$ seed~44 contained 12 samples with $n_{\\text{prem}}{=}1$ classified as genuine by the text matcher.\nManual inspection confirmed all 12 are logically equivalent to H7 but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).\nWe classify these as \\textbf{H7b} (obfuscated tautology), distinct from text-match-detectable H7a.\n$10/12$ achieve $\\text{ISR}{\\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier---triple gaming (\\S\\ref{sec:taxonomy}).\nAfter correction, ISR s44 genuine${=}0$; total H7 = H7a (77 text-match) + H7b (12 obfuscated) = 89.\n\n\\paragraph{Impact on genuine-rate comparison.}\nAfter H8 reclassification and H7 false-negative correction: ISR genuine $= 14/231 = 6.06\\%$ vs.\\ random genuine $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\nThe direction is consistent with ISR-amplified gaming modes (H7, H8) displacing genuine output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n\n\\subsection{H1 --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as H1 (71--93\\%); under ISR reward, it shifts to H7 (70.6\\% pooled).\n\n\n\\subsection{H7a --- Conclusion Duplication (Standard)}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nH7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.\n\n\\paragraph{Prevalence.}\nH7a (text-match detectable): 64.5\\% pooled (149/231) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\nCombined H7 (H7a + H7b): 70.6\\% (163/231; s43 H7a${=}59$ + H7b${=}2$; includes s44 FN correction).\nRandom~$\\beta{=}0.1$ pooled: 13.7\\% (36/262, all H7a; driven by seed~43 at 38.3\\%, seeds~42 and~44 at 0\\%).\n\n\n\\subsection{H7b --- Obfuscated Tautology}\n\n\\paragraph{Definition.}\nA single-premise formalization logically equivalent to H7a (premise = conclusion) but with surface-form differences that evade the text-match H7 classifier.\nThe model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).\n\n\\paragraph{Example (FOL, vacuous quantifier wrapping).}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y ((A(x)&B(y))->(C(x)|D(y))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\nThe premise introduces a vacuous second quantifier variable $y$ that is immediately unified with $x$, making the formulas logically equivalent while differing textually.\n\n\\paragraph{ISR interaction.}\n$\\text{ISR}{\\geq}0.83$ ($10/12$ samples).\nH7b simultaneously games three objectives: execution reward ($r_{\\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match H7 classifier (surface-form difference evades detection).\nThis triple gaming makes H7b the most complete meta-Goodhart case we observe.\n\n\\paragraph{Prevalence.}\nFound exclusively in ISR $\\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as genuine).\nFunctional cross-validation via $n_{\\text{necessary}}{=}1$ exposed the misclassification.\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from H7 by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% H7 by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% H7, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=13$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe fact is necessarily necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to H7 but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-beta01-detailed} and \\ref{tab:prolog-detailed} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$). $^\\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\\S$s43-1000 raw ISR (0.531) includes ${+}12\\%$ inflation from \\texttt{decompose\\_fol()} splitting $\\exists x(\\ldots)$ conclusions into quantifier + body as separate ablatable components; corrected ISR removes this artifact.}\n\\label{tab:fol-detailed}\n\\label{tab:fol-beta01-detailed}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \\textbf{92.3} & Supervised, no RL \\\\\n  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \\textbf{90.9} & \\\\\n  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \\textbf{93.3} & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed pooled} & \\makebox[0pt][l]{$0.130$} & & \\makebox[0pt][l]{$0.595$} & & \\makebox[0pt][l]{\\textbf{92.3}} & $n{=}39$ proved \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\\%$ \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.13 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Greedy ($n_{\\text{proved}}{=}13$) \\\\\n  & 43 & 1000 & 0.90 & 0.465$^\\S$ & 100 & 0 & 0 & H7 dominant \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\\ddagger$ & H8${=}15\\%$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.68{\\pm}0.47$} & & \\makebox[0pt][l]{$0.238{\\pm}0.30$} & & & 500-step \\\\\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.95{\\pm}0.05$} & & \\makebox[0pt][l]{$0.16{\\pm}0.27$} & & \\makebox[0pt][l]{$0.0{\\pm}0.0$} & 1000-step \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{17.3} & Mixed H1+H7+H8 \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{100} & 0 & 0 & H7a${=}59$, H7b${=}2$ \\\\\n  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & H7 dominant (FN corrected) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.77{\\pm}0.14$} & & \\makebox[0pt][l]{$0.716{\\pm}0.26$} & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\\\\n  & 43 & 500 & 0.94 & 0.150 & \\textbf{38.3} & 59.6 & 1.1 & H7a${=}36$; H8${=}1$ \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & H8${=}16$ (H1$\\cap$H8: 6) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.87{\\pm}0.08$} & & \\makebox[0pt][l]{$0.117{\\pm}0.042$} & & & H7 seed-dep.: 0/38/0\\% \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086); $n_{\\text{comp}} = 9.6$ \\\\\n  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\\text{genuine}}{=}3$ \\\\\n  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.54{\\pm}0.35$} & & \\makebox[0pt][l]{$0.09{\\pm}0.09$} & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.53{\\pm}0.31$} & & \\makebox[0pt][l]{$0.146{\\pm}0.21$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & H7 tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional H7$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.62{\\pm}0.31$} & & \\makebox[0pt][l]{$0.699{\\pm}0.45$} & & 3/3 Goodhart, 0\\% non-hacking \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict H7 classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Non-hacking$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: universal Goodhart via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\\% non-hacking proofs (Figure~\\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:\nseed~42 produces clean H7 tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n\n\\subsection{Per-Seed Results at $\\beta{=}0.3$}\n\\label{app:beta03}\n\nTable~\\ref{tab:beta03-detailed} reports per-seed results for both ISR and Random reward at $\\beta{=}0.3$.\nThe three ISR seeds illustrate qualitatively distinct Goodhart pathways (\\S\\ref{sec:goodhart}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results at $\\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H = percentage among proved samples.}\n\\label{tab:beta03-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); H8${=}3$ \\\\\n  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 26.7 & H1 shortcutting \\\\\n  & 44 & 0.95 & 0.742 & \\textbf{100} & 0 & 0 & Pure H7 meta-Goodhart \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.66{\\pm}0.42$} & & \\makebox[0pt][l]{$0.39{\\pm}0.31$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086) \\\\\n  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\\text{genuine}}{=}3$ \\\\\n  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.54{\\pm}0.35$} & & \\makebox[0pt][l]{$0.09{\\pm}0.09$} & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%---higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.7\\% hacking (1/13 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training---well before the prove-rate plateau---and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n\n\\subsection{$O(1)$ vs.\\ $O(n)$ ISR Ablation}\n\\label{app:o1-ablation}\n\nTo justify the per-clause LOO design (\\S\\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\\text{fast\\_ISR}(x) = 1$ if $x$ is proved \\emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.\nThe reward becomes $r = 0.5\\,r_{\\text{exec}} + 0.5\\,\\text{fast\\_ISR}$.\nAfter 500 steps (seed~42), this variant achieves $\\text{PR}{=}63\\%$ with $\\text{ISR}^*{=}0.007$---functionally zero---compared to $\\text{ISR}^*{=}0.132$ under standard exec-only and $\\text{ISR}^*{=}0.42$ under ISR $\\beta{=}0.1$.\n\n\\paragraph{ISR signal vs.\\ training dynamics.}\nAt the \\emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.\nAt the \\emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.\nThis confound depresses prove rate by 30 percentage points ($63\\%$ vs.\\ $93\\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.\nThe result confirms that the $O(n)$ per-clause ablation is necessary for ISR to carry a structural signal, while also showing that even a minimal tautology guard alters training dynamics substantially.\n",
      "numLines": 554,
      "startLine": 1,
      "totalLines": 554
    }
  },
  "sourceToolAssistantUUID": "df6c9525-331d-45f5-9c2a-cd45f254cfb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "leafUuid": "11783de0-cc64-46b8-afa8-00d6e21b6c98",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Final TeX proofreading for paper submission",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb"
}
```

---

### Assistant

_source line 24 · 2026-05-15T23:01:56.868Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also read the abstract, introduction, related work, and limitations files, as well as the references.bib to check citation completeness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11783de0-cc64-46b8-afa8-00d6e21b6c98",
  "isSidechain": false,
  "requestId": "req_011Cb5Bpew1vGeN4zHKBUMqM",
  "type": "assistant",
  "uuid": "077edd54-da0d-4a08-b4c3-53074eb86829",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015G6bgLbzAbCiKTX1DWyg33",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24753,
      "cache_read_input_tokens": 26249,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 26249,
          "cache_creation_input_tokens": 24753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24753
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

_source line 25 · 2026-05-15T23:01:57.465Z_

Now reading the remaining TeX files and references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "077edd54-da0d-4a08-b4c3-53074eb86829",
  "isSidechain": false,
  "requestId": "req_011Cb5Bpew1vGeN4zHKBUMqM",
  "type": "assistant",
  "uuid": "b96b0242-0aa3-4f1b-a279-e8c0b96d92fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015G6bgLbzAbCiKTX1DWyg33",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24753,
      "cache_read_input_tokens": 26249,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 26249,
          "cache_creation_input_tokens": 24753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24753
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

_source line 26 · 2026-05-15T23:02:00.982Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MHSKgunFzhAVi9YcxC7TPU`</summary>

```json
{
  "description": "Read remaining TeX files",
  "subagent_type": "Explore",
  "prompt": "Read these files in full and report their complete contents:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex\n\nReport the full text of each file."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b96b0242-0aa3-4f1b-a279-e8c0b96d92fc",
  "isSidechain": false,
  "requestId": "req_011Cb5Bpew1vGeN4zHKBUMqM",
  "type": "assistant",
  "uuid": "5b55a961-866d-4858-8145-971486b5aa8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015G6bgLbzAbCiKTX1DWyg33",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24753,
      "cache_read_input_tokens": 26249,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 26249,
          "cache_creation_input_tokens": 24753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24753
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

_source line 27 · 2026-05-15T23:02:04.687Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016yUAKGoKduRBRQYjDgjXpo`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && grep -c '\\\\\\\\cite{' main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex conclusion.tex appendix.tex limitations.tex 2>/dev/null; echo \"---\"; grep -oP '\\\\\\\\cite\\{[^}]+\\}' abstract.tex introduction.tex related_work.tex method.tex experiments.tex conclusion.tex appendix.tex limitations.tex 2>/dev/null | sort -u; echo \"---BIBS---\"; grep -oP '@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//' | sed 's/,$//' | sort",
  "description": "Extract all cite keys and bib entries for cross-check"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b55a961-866d-4858-8145-971486b5aa8d",
  "isSidechain": false,
  "requestId": "req_011Cb5Bpew1vGeN4zHKBUMqM",
  "type": "assistant",
  "uuid": "eb75ff1b-d643-411f-843d-779da0693a7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015G6bgLbzAbCiKTX1DWyg33",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24753,
      "cache_read_input_tokens": 26249,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 26249,
          "cache_creation_input_tokens": 24753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24753
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

_source line 28 · 2026-05-15T23:02:06.098Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UNMY9gFetpdGTqFg65XRKt`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && grep -oP '\\\\\\\\(ref|label)\\{[^}]+\\}' abstract.tex introduction.tex related_work.tex method.tex experiments.tex conclusion.tex appendix.tex limitations.tex 2>/dev/null | sort | uniq -c | sort -rn",
  "description": "Extract all ref/label pairs for cross-check"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb75ff1b-d643-411f-843d-779da0693a7a",
  "isSidechain": false,
  "requestId": "req_011Cb5Bpew1vGeN4zHKBUMqM",
  "type": "assistant",
  "uuid": "f32689cb-f507-46b8-ab40-73c3fe353b8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015G6bgLbzAbCiKTX1DWyg33",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24753,
      "cache_read_input_tokens": 26249,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 26249,
          "cache_creation_input_tokens": 24753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24753
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

_source line 29 · 2026-05-15T23:02:07.798Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01G5bNoBBgRCjw9bTczKatuz`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && grep -n '\\[?\\]' main.log 2>/dev/null | head -20; echo \"---WARNINGS---\"; grep -n 'Warning.*undefined\\|Warning.*multiply' main.log 2>/dev/null | head -30",
  "description": "Check LaTeX log for undefined references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f32689cb-f507-46b8-ab40-73c3fe353b8a",
  "isSidechain": false,
  "requestId": "req_011Cb5Bpew1vGeN4zHKBUMqM",
  "type": "assistant",
  "uuid": "063e537b-6554-495f-9bb8-a5bc27afeb7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015G6bgLbzAbCiKTX1DWyg33",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24753,
      "cache_read_input_tokens": 26249,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 26249,
          "cache_creation_input_tokens": 24753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24753
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

_source line 30 · 2026-05-15T23:02:43.150Z_

<details><summary>↩ Tool result · `toolu_01MHSKgunFzhAVi9YcxC7TPU`</summary>

````text
Here are the complete contents of all four files:

## 1. abstract.tex

```
\begin{abstract}
GRPO-trained neurosymbolic formalizers achieve high prove rates---93\% on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.
We introduce \emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.
The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.
ISR is uncorrelated with downstream NLI accuracy ($\rho{=}{-}0.049$), confirming it measures structural---not semantic---integrity.
As a diagnostic, ISR exposes a collapse trajectory hidden from PR: over 100--1000 GRPO steps (Qwen3-4B), ISR falls $0.642{\to}0.003$ while PR rises $32\%{\to}96\%$; an SFT baseline reaches 92.3\% non-hacking on identical data (3-seed pooled), localizing the failure to RL.
As a reward, $r = r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta{=}0.1$ induces \emph{meta-level Goodhart's Law}: 70.6\% conclusion duplication (H7) versus 13.7\% under matched random (Fisher $p{=}1.3{\times}10^{-39}$; random H7 is seed-dependent, driven by one of three seeds); ISR amplifies H7 frequency ${\sim}5{\times}$ rather than exclusively causing it; the sole apparent ISR improvement reduces to $1.06\times$ after controlling for a premise-count confound; $\beta{=}0.3$ destabilizes training regardless of signal source (ISR: PR $66{\pm}42\%$; random: $54{\pm}35\%$), with individual seeds collapsing to as low as $18\%$.
Cross-logic transfer to Prolog yields universal Goodhart: 3/3 seeds gaming via distinct mechanisms, 0\% non-hacking.
Across 6 reward conditions, 2 logic types, 3 seeds, we catalog 8 hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
\end{abstract}
```

## 2. introduction.tex

```
\section{Introduction}
\label{sec:introduction}

A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.

\paragraph{The execution-only blind spot.}
Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but gives no gradient on structural quality.
Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
A separate line documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.

\paragraph{Component necessity testing.}
We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\ref{fig:sta-overview}).
For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR), with $\text{ISR}{=}1$ indicating full necessity and $\text{ISR}{=}0$ complete redundancy.
LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
ISR captures structural rather than semantic integrity (downstream NLI: $\rho{=}{-}0.049$, $p{=}0.187$).

\paragraph{ISR as diagnostic.}
As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\text{ISR}^{*}{:}\,0.642\to 0.132\to 0.003$ over 100--1000 steps (99.5\% degradation) while PR rises $32\%{\to}96\%$.
Three seeds diverge radically (PR $\sigma{=}47\,pp$), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.
An SFT baseline on identical data reaches $\text{PR}{=}13.0\%$ with 92.3\% non-hacking (3-seed pooled, 1000 steps), localizing the failure to RL optimization, not data or capacity.

\paragraph{Meta-level Goodhart.}
Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR is gamed at its own definition---\emph{meta-level Goodhart's Law}~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.
At $\beta{=}0.1$, 70.6\% of proved samples exhibit conclusion duplication (H7)---versus 13.7\% under matched random (Fisher $p{<}10^{-38}$; random H7 is highly seed-dependent), showing ISR amplifies tautological collapse by ${\sim}5{\times}$; the one seed with non-trivial residual reduces to $1.06\times$ random after controlling for a premise-count confound.
At $\beta{=}0.3$, both ISR and random produce extreme cross-seed instability (PR $66{\pm}42\%$ and $54{\pm}35\%$ respectively), confirming high-dose proxy weighting is harmful regardless of signal content; ISR seeds diverge into three distinct pathways (reward collapse, shortcut dominance, pure metric gaming) while random converges uniformly to H1.
The effect transfers and intensifies in Prolog: 3/3 seeds yield 0\% non-hacking via distinct mechanisms, including \emph{query-as-fact gaming} that bypasses text-match classifiers.
ISR's asymmetry is the central finding: \emph{reliable as observer, unreliable as optimizer.}

\paragraph{Contributions.}
Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 steps, we contribute: (\textbf{C1}) ISR as a diagnostic for GRPO reward hacking, with a 99.5\% collapse trajectory invisible to PR and an SFT control localizing the failure to RL (\S\ref{sec:diagnostic}); (\textbf{C2}) empirical meta-level Goodhart, with a random control showing ISR amplifies H7 gaming ${\sim}5{\times}$ (70.6\% vs.\ 13.7\%, Fisher $p{<}10^{-38}$; random H7 is seed-dependent) and a premise-count-matched analysis showing the sole apparent gain is an LOO artifact (\S\ref{sec:goodhart}); (\textbf{C3}) cross-logic transfer to Prolog with universal Goodhart (\S\ref{sec:crosslogic}); (\textbf{C4}) an eight-mode hacking taxonomy including query-as-fact gaming and obfuscated tautology, motivating functional cross-validation of diagnostics (\S\ref{sec:taxonomy}).
These are cautionary results for any work treating a structural proxy as a training signal.
```

## 3. related_work.tex

```
\section{Related Work}
\label{sec:related-work}

\paragraph{Neurosymbolic reasoning.}
LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.

\paragraph{Process rewards and reward shaping.}
Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}: \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
The shared lesson across these approaches is that reward augmentation introduces proxy risk---our contribution is demonstrating the \emph{meta}-level variant where the diagnostic itself becomes the target.

\paragraph{Reward hacking and Goodhart's Law.}
Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.
Recent work further documents spurious reward signals in RLVR~\citep{spurious-rewards} and reward hacking in frontier models~\citep{metr-reward-hacking}.
Our setting differs in three ways: ISR is deterministic and solver-derived rather than learned; gaming \emph{emerges during RL training} rather than at inference time; and the effect operates at a \emph{meta} level---the diagnostic for gaming itself becomes gamed when optimized---a phenomenon, to our knowledge, not previously documented.

\paragraph{Mutation testing.}
STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
```

## 4. limitations.tex

```
\section{Limitations}
\label{sec:limitations}

Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
Three seeds demonstrate qualitative divergence but limit statistical power.
STA requires solvers supporting component-level input manipulation.

\paragraph{Data scale.}
Our experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\citep{folio}.
The training subset is selected via stratified sampling (seed 42) and held constant across all conditions.
While our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.
```
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "5b55a961-866d-4858-8145-971486b5aa8d",
  "isSidechain": false,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "type": "user",
  "uuid": "47db79c9-93ed-444a-8fb9-558a8962d786",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Read these files in full and report their complete contents:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex\n\nReport the full text of each file.",
    "agentId": "a62a755bf7232a081",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Here are the complete contents of all four files:\n\n## 1. abstract.tex\n\n```\n\\begin{abstract}\nGRPO-trained neurosymbolic formalizers achieve high prove rates---93\\% on FOLIO---yet 87\\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.\nWe introduce \\emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.\nThe fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.\nISR is uncorrelated with downstream NLI accuracy ($\\rho{=}{-}0.049$), confirming it measures structural---not semantic---integrity.\nAs a diagnostic, ISR exposes a collapse trajectory hidden from PR: over 100--1000 GRPO steps (Qwen3-4B), ISR falls $0.642{\\to}0.003$ while PR rises $32\\%{\\to}96\\%$; an SFT baseline reaches 92.3\\% non-hacking on identical data (3-seed pooled), localizing the failure to RL.\nAs a reward, $r = r_{\\text{exec}}\\cdot(1{+}\\beta\\,\\text{ISR})$ at $\\beta{=}0.1$ induces \\emph{meta-level Goodhart's Law}: 70.6\\% conclusion duplication (H7) versus 13.7\\% under matched random (Fisher $p{=}1.3{\\times}10^{-39}$; random H7 is seed-dependent, driven by one of three seeds); ISR amplifies H7 frequency ${\\sim}5{\\times}$ rather than exclusively causing it; the sole apparent ISR improvement reduces to $1.06\\times$ after controlling for a premise-count confound; $\\beta{=}0.3$ destabilizes training regardless of signal source (ISR: PR $66{\\pm}42\\%$; random: $54{\\pm}35\\%$), with individual seeds collapsing to as low as $18\\%$.\nCross-logic transfer to Prolog yields universal Goodhart: 3/3 seeds gaming via distinct mechanisms, 0\\% non-hacking.\nAcross 6 reward conditions, 2 logic types, 3 seeds, we catalog 8 hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\\footnote{Code and data: \\url{[anonymized]}}\n\\end{abstract}\n```\n\n## 2. introduction.tex\n\n```\n\\section{Introduction}\n\\label{sec:introduction}\n\nA GRPO-trained formalizer achieves a 93\\% prove rate on first-order logic problems---yet 87\\% of its proved outputs embed the conclusion verbatim among the premises.\nThe solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.\nThis structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.\n\n\\paragraph{The execution-only blind spot.}\nProve rate---the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nRecent work applies GRPO~\\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but gives no gradient on structural quality.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.\nA separate line documents that LLMs already game logical formalization at inference time~\\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \\emph{diagnostic} for structural integrity in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic applying \\emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\\ref{fig:sta-overview}).\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR), with $\\text{ISR}{=}1$ indicating full necessity and $\\text{ISR}{=}0$ complete redundancy.\nLOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.\nISR captures structural rather than semantic integrity (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\n\n\\paragraph{ISR as diagnostic.}\nAs a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\\text{ISR}^{*}{:}\\,0.642\\to 0.132\\to 0.003$ over 100--1000 steps (99.5\\% degradation) while PR rises $32\\%{\\to}96\\%$.\nThree seeds diverge radically (PR $\\sigma{=}47\\,pp$), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.\nAn SFT baseline on identical data reaches $\\text{PR}{=}13.0\\%$ with 92.3\\% non-hacking (3-seed pooled, 1000 steps), localizing the failure to RL optimization, not data or capacity.\n\n\\paragraph{Meta-level Goodhart.}\nRepurposed as a training signal, $r = r_{\\text{exec}} \\cdot (1 + \\beta\\,\\text{ISR})$, ISR is gamed at its own definition---\\emph{meta-level Goodhart's Law}~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.\nAt $\\beta{=}0.1$, 70.6\\% of proved samples exhibit conclusion duplication (H7)---versus 13.7\\% under matched random (Fisher $p{<}10^{-38}$; random H7 is highly seed-dependent), showing ISR amplifies tautological collapse by ${\\sim}5{\\times}$; the one seed with non-trivial residual reduces to $1.06\\times$ random after controlling for a premise-count confound.\nAt $\\beta{=}0.3$, both ISR and random produce extreme cross-seed instability (PR $66{\\pm}42\\%$ and $54{\\pm}35\\%$ respectively), confirming high-dose proxy weighting is harmful regardless of signal content; ISR seeds diverge into three distinct pathways (reward collapse, shortcut dominance, pure metric gaming) while random converges uniformly to H1.\nThe effect transfers and intensifies in Prolog: 3/3 seeds yield 0\\% non-hacking via distinct mechanisms, including \\emph{query-as-fact gaming} that bypasses text-match classifiers.\nISR's asymmetry is the central finding: \\emph{reliable as observer, unreliable as optimizer.}\n\n\\paragraph{Contributions.}\nAcross 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 steps, we contribute: (\\textbf{C1}) ISR as a diagnostic for GRPO reward hacking, with a 99.5\\% collapse trajectory invisible to PR and an SFT control localizing the failure to RL (\\S\\ref{sec:diagnostic}); (\\textbf{C2}) empirical meta-level Goodhart, with a random control showing ISR amplifies H7 gaming ${\\sim}5{\\times}$ (70.6\\% vs.\\ 13.7\\%, Fisher $p{<}10^{-38}$; random H7 is seed-dependent) and a premise-count-matched analysis showing the sole apparent gain is an LOO artifact (\\S\\ref{sec:goodhart}); (\\textbf{C3}) cross-logic transfer to Prolog with universal Goodhart (\\S\\ref{sec:crosslogic}); (\\textbf{C4}) an eight-mode hacking taxonomy including query-as-fact gaming and obfuscated tautology, motivating functional cross-validation of diagnostics (\\S\\ref{sec:taxonomy}).\nThese are cautionary results for any work treating a structural proxy as a training signal.\n```\n\n## 3. related_work.tex\n\n```\n\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.\nWe use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Process rewards and reward shaping.}\nLearned PRMs~\\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\\citep{processbench}: \\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \\emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.\nSymbolic feedback approaches~\\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.\nRubric-grounded GRPO~\\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.\nThe shared lesson across these approaches is that reward augmentation introduces proxy risk---our contribution is demonstrating the \\emph{meta}-level variant where the diagnostic itself becomes the target.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \\emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.\nRecent work further documents spurious reward signals in RLVR~\\citep{spurious-rewards} and reward hacking in frontier models~\\citep{metr-reward-hacking}.\nOur setting differs in three ways: ISR is deterministic and solver-derived rather than learned; gaming \\emph{emerges during RL training} rather than at inference time; and the effect operates at a \\emph{meta} level---the diagnostic for gaming itself becomes gamed when optimized---a phenomenon, to our knowledge, not previously documented.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\n```\n\n## 4. limitations.tex\n\n```\n\\section{Limitations}\n\\label{sec:limitations}\n\nExperiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.\nISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\\ref{app:extended-discussion}).\nThree seeds demonstrate qualitative divergence but limit statistical power.\nSTA requires solvers supporting component-level input manipulation.\n\n\\paragraph{Data scale.}\nOur experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\\citep{folio}.\nThe training subset is selected via stratified sampling (seed 42) and held constant across all conditions.\nWhile our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.\n```"
      }
    ],
    "totalDurationMs": 42158,
    "totalTokens": 23430,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4609,
      "cache_read_input_tokens": 15560,
      "output_tokens": 3254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4609
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3254,
          "cache_read_input_tokens": 15560,
          "cache_creation_input_tokens": 4609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4609,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "5b55a961-866d-4858-8145-971486b5aa8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "leafUuid": "47db79c9-93ed-444a-8fb9-558a8962d786",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Final TeX proofreading for paper submission",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb"
}
```

---

### Tool result

_source line 33 · 2026-05-15T23:02:43.469Z_

<details><summary>↩ Tool result · `toolu_016yUAKGoKduRBRQYjDgjXpo`</summary>

```text
main.tex:0
abstract.tex:0
introduction.tex:0
related_work.tex:0
method.tex:0
experiments.tex:0
conclusion.tex:0
appendix.tex:0
limitations.tex:0
---
---BIBS---
bondarenko-spec-gaming
deepseek-prover-v15
deepseekmath
demillo1978
folio
fover-pei2025
gao-effective-rl-reward
gao-reward-overoptimization
jia-harman-survey
karwowski-goodhart-rl
kim-game-formalization
kwa-catastrophic-goodhart
lightman-verify-step
linc
logic-lm
logic-rl
lorp
lundberg-shap
manheim-goodhart-taxonomy
math-shepherd
mellgren-prolog-grpo
metr-reward-hacking
processbench
proofwriter
qwen3
reward-hacking-survey
rlsf
rubric-grpo
satlm
skalse-reward-hacking
spurious-rewards
sundararajan-ig
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb75ff1b-d643-411f-843d-779da0693a7a",
  "isSidechain": false,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "type": "user",
  "uuid": "e6b8cd83-2162-4ff2-88ac-c8fcb275b943",
  "toolUseResult": {
    "stdout": "main.tex:0\nabstract.tex:0\nintroduction.tex:0\nrelated_work.tex:0\nmethod.tex:0\nexperiments.tex:0\nconclusion.tex:0\nappendix.tex:0\nlimitations.tex:0\n---\n---BIBS---\nbondarenko-spec-gaming\ndeepseek-prover-v15\ndeepseekmath\ndemillo1978\nfolio\nfover-pei2025\ngao-effective-rl-reward\ngao-reward-overoptimization\njia-harman-survey\nkarwowski-goodhart-rl\nkim-game-formalization\nkwa-catastrophic-goodhart\nlightman-verify-step\nlinc\nlogic-lm\nlogic-rl\nlorp\nlundberg-shap\nmanheim-goodhart-taxonomy\nmath-shepherd\nmellgren-prolog-grpo\nmetr-reward-hacking\nprocessbench\nproofwriter\nqwen3\nreward-hacking-survey\nrlsf\nrubric-grpo\nsatlm\nskalse-reward-hacking\nspurious-rewards\nsundararajan-ig",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "eb75ff1b-d643-411f-843d-779da0693a7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T23:02:43.647Z_

<details><summary>↩ Tool result · `toolu_01G5bNoBBgRCjw9bTczKatuz`</summary>

```text
---WARNINGS---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "063e537b-6554-495f-9bb8-a5bc27afeb7d",
  "isSidechain": false,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "type": "user",
  "uuid": "517fc5d8-33eb-490e-ab2f-26fff2ab24ad",
  "toolUseResult": {
    "stdout": "---WARNINGS---",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "063e537b-6554-495f-9bb8-a5bc27afeb7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T23:02:43.656Z_

<details><summary>↩ Tool result · `toolu_01UNMY9gFetpdGTqFg65XRKt`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f32689cb-f507-46b8-ab40-73c3fe353b8a",
  "isSidechain": false,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "type": "user",
  "uuid": "e13c4972-ab01-46eb-92ed-bdfcaa55c202",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f32689cb-f507-46b8-ab40-73c3fe353b8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-15T23:02:43.662Z_

```json
{
  "parentUuid": "e13c4972-ab01-46eb-92ed-bdfcaa55c202",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "08658aa2-a32b-494a-9c90-ca2521b805ea",
  "timestamp": "2026-05-15T23:02:43.662Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 37 · 2026-05-15T23:02:46.456Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also check the LaTeX log more carefully and cross-check refs vs labels.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08658aa2-a32b-494a-9c90-ca2521b805ea",
  "isSidechain": false,
  "requestId": "req_011Cb5BtTrsRo4sD1AQ8swyo",
  "type": "assistant",
  "uuid": "17950dfa-6d02-41a4-9007-9bfcd408b8c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UmLtue3HffJ4HiNBGKTem4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 35,
      "cache_creation_input_tokens": 4578,
      "cache_read_input_tokens": 51002,
      "output_tokens": 690,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 35,
          "output_tokens": 690,
          "cache_read_input_tokens": 51002,
          "cache_creation_input_tokens": 4578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4578
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

_source line 38 · 2026-05-15T23:02:47.001Z_

Let me cross-check ref/label pairs and verify some specific numerical claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17950dfa-6d02-41a4-9007-9bfcd408b8c3",
  "isSidechain": false,
  "requestId": "req_011Cb5BtTrsRo4sD1AQ8swyo",
  "type": "assistant",
  "uuid": "466cb7e2-d8bd-4198-832d-cea6cdfb866a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UmLtue3HffJ4HiNBGKTem4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 35,
      "cache_creation_input_tokens": 4578,
      "cache_read_input_tokens": 51002,
      "output_tokens": 690,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 35,
          "output_tokens": 690,
          "cache_read_input_tokens": 51002,
          "cache_creation_input_tokens": 4578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4578
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

_source line 39 · 2026-05-15T23:02:48.944Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JKd1gD2sQBoxBZbF1S2J6U`</summary>

```json
{
  "command": "echo \"=== LABELS ===\" && grep -oP '\\\\label\\{[^}]+\\}' abstract.tex introduction.tex related_work.tex method.tex experiments.tex conclusion.tex appendix.tex limitations.tex 2>/dev/null | sed 's/\\\\label{//;s/}//' | sort; echo \"=== REFS ===\" && grep -oP '\\\\ref\\{[^}]+\\}' abstract.tex introduction.tex related_work.tex method.tex experiments.tex conclusion.tex appendix.tex limitations.tex 2>/dev/null | sed 's/\\\\ref{//;s/}//' | sort -u",
  "description": "Cross-check labels vs refs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "466cb7e2-d8bd-4198-832d-cea6cdfb866a",
  "isSidechain": false,
  "requestId": "req_011Cb5BtTrsRo4sD1AQ8swyo",
  "type": "assistant",
  "uuid": "0d2c6a0c-1491-4311-8de2-45e3afdd38ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UmLtue3HffJ4HiNBGKTem4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 35,
      "cache_creation_input_tokens": 4578,
      "cache_read_input_tokens": 51002,
      "output_tokens": 690,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 35,
          "output_tokens": 690,
          "cache_read_input_tokens": 51002,
          "cache_creation_input_tokens": 4578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4578
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

_source line 40 · 2026-05-15T23:02:53.315Z_

<details><summary>↩ Tool result · `toolu_01HUKkz1UJSVZGQnmcZqRKk2`</summary>

```text
239:Package: rerunfilecheck 2025-06-21 v1.11 Rerun checks for auxiliary files (HO)
1014:LaTeX Warning: `h' float specifier changed to `ht'.
1101:LaTeX Warning: `h' float specifier changed to `ht'.
1179:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
1183:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
1187:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
1196:LaTeX Warning: `h' float specifier changed to `ht'.
1200:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
1204:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
1208:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
1212:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbb5877e-ced6-4207-b493-32e46fdfa186",
  "isSidechain": false,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "type": "user",
  "uuid": "359a639f-39ad-4d1d-bd8f-3f641a10f7c6",
  "toolUseResult": {
    "stdout": "239:Package: rerunfilecheck 2025-06-21 v1.11 Rerun checks for auxiliary files (HO)\n1014:LaTeX Warning: `h' float specifier changed to `ht'.\n1101:LaTeX Warning: `h' float specifier changed to `ht'.\n1179:Package hyperref Warning: Token not allowed in a PDF string (Unicode):\n1183:Package hyperref Warning: Token not allowed in a PDF string (Unicode):\n1187:Package hyperref Warning: Token not allowed in a PDF string (Unicode):\n1196:LaTeX Warning: `h' float specifier changed to `ht'.\n1200:Package hyperref Warning: Token not allowed in a PDF string (Unicode):\n1204:Package hyperref Warning: Token not allowed in a PDF string (Unicode):\n1208:Package hyperref Warning: Token not allowed in a PDF string (Unicode):\n1212:Package hyperref Warning: Token not allowed in a PDF string (Unicode):",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fbb5877e-ced6-4207-b493-32e46fdfa186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T23:02:49.032Z_

<details><summary>↩ Tool result · `toolu_01JKd1gD2sQBoxBZbF1S2J6U`</summary>

```text
=== LABELS ===
appendix.tex:app:100step
appendix.tex:app:algorithm
appendix.tex:app:beta03
appendix.tex:app:detailed-results
appendix.tex:app:extended-discussion
appendix.tex:app:h8
appendix.tex:app:hacking-modes
appendix.tex:app:o1-ablation
appendix.tex:app:setup
appendix.tex:tab:beta03-detailed
appendix.tex:tab:bootstrap-ci
appendix.tex:tab:fol-beta01-detailed
appendix.tex:tab:fol-detailed
appendix.tex:tab:hacking-taxonomy-app
appendix.tex:tab:hyperparams
appendix.tex:tab:prolog-detailed
conclusion.tex:sec:discussion
experiments.tex:fig:hacking-composition
experiments.tex:fig:isr-collapse
experiments.tex:fig:prolog-comparison
experiments.tex:fig:training-isr-curves
experiments.tex:sec:crosslogic
experiments.tex:sec:diagnostic
experiments.tex:sec:experiments
experiments.tex:sec:goodhart
experiments.tex:sec:setup
experiments.tex:sec:taxonomy
experiments.tex:tab:goodhart-landscape
experiments.tex:tab:hacking-taxonomy
introduction.tex:sec:introduction
limitations.tex:sec:limitations
method.tex:alg:sta
method.tex:eq:isr
method.tex:fig:sta-overview
method.tex:sec:method
method.tex:sec:rewards
method.tex:sec:sta
method.tex:sec:task
method.tex:sec:taxonomy-method
related_work.tex:sec:related-work
=== REFS ===
appendix.tex:alg:sta
appendix.tex:app:h8
appendix.tex:app:hacking-modes
appendix.tex:fig:prolog-comparison
appendix.tex:sec:crosslogic
appendix.tex:sec:diagnostic
appendix.tex:sec:goodhart
appendix.tex:sec:sta
appendix.tex:sec:taxonomy
appendix.tex:tab:beta03-detailed
appendix.tex:tab:fol-beta01-detailed
appendix.tex:tab:fol-detailed
appendix.tex:tab:goodhart-landscape
appendix.tex:tab:hacking-taxonomy-app
appendix.tex:tab:hyperparams
appendix.tex:tab:prolog-detailed
conclusion.tex:sec:crosslogic
conclusion.tex:sec:diagnostic
conclusion.tex:sec:taxonomy
conclusion.tex:tab:fol-detailed
experiments.tex:app:100step
experiments.tex:app:beta03
experiments.tex:app:detailed-results
experiments.tex:app:h8
experiments.tex:app:hacking-modes
experiments.tex:fig:hacking-composition
experiments.tex:fig:isr-collapse
experiments.tex:fig:prolog-comparison
experiments.tex:fig:training-isr-curves
experiments.tex:sec:crosslogic
experiments.tex:sec:diagnostic
experiments.tex:sec:discussion
experiments.tex:sec:goodhart
experiments.tex:sec:taxonomy
experiments.tex:sec:taxonomy-method
experiments.tex:tab:bootstrap-ci
experiments.tex:tab:fol-detailed
experiments.tex:tab:hacking-taxonomy
experiments.tex:tab:prolog-detailed
introduction.tex:fig:sta-overview
introduction.tex:sec:crosslogic
introduction.tex:sec:diagnostic
introduction.tex:sec:goodhart
introduction.tex:sec:taxonomy
limitations.tex:app:extended-discussion
method.tex:alg:sta
method.tex:app:h8
method.tex:app:hacking-modes
method.tex:app:o1-ablation
method.tex:app:setup
method.tex:fig:sta-overview
method.tex:sec:experiments
method.tex:sec:goodhart
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d2c6a0c-1491-4311-8de2-45e3afdd38ae",
  "isSidechain": false,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "type": "user",
  "uuid": "ada86e58-d7f8-4abd-bbcc-4e63ad34f607",
  "toolUseResult": {
    "stdout": "=== LABELS ===\nappendix.tex:app:100step\nappendix.tex:app:algorithm\nappendix.tex:app:beta03\nappendix.tex:app:detailed-results\nappendix.tex:app:extended-discussion\nappendix.tex:app:h8\nappendix.tex:app:hacking-modes\nappendix.tex:app:o1-ablation\nappendix.tex:app:setup\nappendix.tex:tab:beta03-detailed\nappendix.tex:tab:bootstrap-ci\nappendix.tex:tab:fol-beta01-detailed\nappendix.tex:tab:fol-detailed\nappendix.tex:tab:hacking-taxonomy-app\nappendix.tex:tab:hyperparams\nappendix.tex:tab:prolog-detailed\nconclusion.tex:sec:discussion\nexperiments.tex:fig:hacking-composition\nexperiments.tex:fig:isr-collapse\nexperiments.tex:fig:prolog-comparison\nexperiments.tex:fig:training-isr-curves\nexperiments.tex:sec:crosslogic\nexperiments.tex:sec:diagnostic\nexperiments.tex:sec:experiments\nexperiments.tex:sec:goodhart\nexperiments.tex:sec:setup\nexperiments.tex:sec:taxonomy\nexperiments.tex:tab:goodhart-landscape\nexperiments.tex:tab:hacking-taxonomy\nintroduction.tex:sec:introduction\nlimitations.tex:sec:limitations\nmethod.tex:alg:sta\nmethod.tex:eq:isr\nmethod.tex:fig:sta-overview\nmethod.tex:sec:method\nmethod.tex:sec:rewards\nmethod.tex:sec:sta\nmethod.tex:sec:task\nmethod.tex:sec:taxonomy-method\nrelated_work.tex:sec:related-work\n=== REFS ===\nappendix.tex:alg:sta\nappendix.tex:app:h8\nappendix.tex:app:hacking-modes\nappendix.tex:fig:prolog-comparison\nappendix.tex:sec:crosslogic\nappendix.tex:sec:diagnostic\nappendix.tex:sec:goodhart\nappendix.tex:sec:sta\nappendix.tex:sec:taxonomy\nappendix.tex:tab:beta03-detailed\nappendix.tex:tab:fol-beta01-detailed\nappendix.tex:tab:fol-detailed\nappendix.tex:tab:goodhart-landscape\nappendix.tex:tab:hacking-taxonomy-app\nappendix.tex:tab:hyperparams\nappendix.tex:tab:prolog-detailed\nconclusion.tex:sec:crosslogic\nconclusion.tex:sec:diagnostic\nconclusion.tex:sec:taxonomy\nconclusion.tex:tab:fol-detailed\nexperiments.tex:app:100step\nexperiments.tex:app:beta03\nexperiments.tex:app:detailed-results\nexperiments.tex:app:h8\nexperiments.tex:app:hacking-modes\nexperiments.tex:fig:hacking-composition\nexperiments.tex:fig:isr-collapse\nexperiments.tex:fig:prolog-comparison\nexperiments.tex:fig:training-isr-curves\nexperiments.tex:sec:crosslogic\nexperiments.tex:sec:diagnostic\nexperiments.tex:sec:discussion\nexperiments.tex:sec:goodhart\nexperiments.tex:sec:taxonomy\nexperiments.tex:sec:taxonomy-method\nexperiments.tex:tab:bootstrap-ci\nexperiments.tex:tab:fol-detailed\nexperiments.tex:tab:hacking-taxonomy\nexperiments.tex:tab:prolog-detailed\nintroduction.tex:fig:sta-overview\nintroduction.tex:sec:crosslogic\nintroduction.tex:sec:diagnostic\nintroduction.tex:sec:goodhart\nintroduction.tex:sec:taxonomy\nlimitations.tex:app:extended-discussion\nmethod.tex:alg:sta\nmethod.tex:app:h8\nmethod.tex:app:hacking-modes\nmethod.tex:app:o1-ablation\nmethod.tex:app:setup\nmethod.tex:fig:sta-overview\nmethod.tex:sec:experiments\nmethod.tex:sec:goodhart",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0d2c6a0c-1491-4311-8de2-45e3afdd38ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T23:02:52.200Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LRRJY84kC8LnStZCFw9FG1`</summary>

```json
{
  "command": "echo \"=== CITE KEYS USED ===\" && grep -oP '\\\\cite[tp]?\\{[^}]+\\}' abstract.tex introduction.tex related_work.tex method.tex experiments.tex conclusion.tex appendix.tex limitations.tex 2>/dev/null | grep -oP '\\{[^}]+\\}' | sed 's/[{}]//g' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u; echo \"=== BIB KEYS ===\" && grep -oP '@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u",
  "description": "Cross-check cite keys vs bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ada86e58-d7f8-4abd-bbcc-4e63ad34f607",
  "isSidechain": false,
  "requestId": "req_011Cb5BtTrsRo4sD1AQ8swyo",
  "type": "assistant",
  "uuid": "5d28e426-aee0-45f4-b47b-aa8d34562305",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UmLtue3HffJ4HiNBGKTem4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 35,
      "cache_creation_input_tokens": 4578,
      "cache_read_input_tokens": 51002,
      "output_tokens": 690,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 35,
          "output_tokens": 690,
          "cache_read_input_tokens": 51002,
          "cache_creation_input_tokens": 4578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4578
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

_source line 43 · 2026-05-15T23:02:52.294Z_

<details><summary>↩ Tool result · `toolu_01LRRJY84kC8LnStZCFw9FG1`</summary>

```text
=== CITE KEYS USED ===
bondarenko-spec-gaming
deepseek-prover-v15
deepseekmath
demillo1978
folio
fover-pei2025
gao-effective-rl-reward
gao-reward-overoptimization
jia-harman-survey
karwowski-goodhart-rl
kim-game-formalization
kwa-catastrophic-goodhart
lightman-verify-step
linc
logic-lm
logic-rl
lorp
lundberg-shap
manheim-goodhart-taxonomy
math-shepherd
mellgren-prolog-grpo
metr-reward-hacking
processbench
proofwriter
qwen3
reward-hacking-survey
rlsf
rubric-grpo
satlm
skalse-reward-hacking
spurious-rewards
sundararajan-ig
=== BIB KEYS ===
bondarenko-spec-gaming
deepseek-prover-v15
deepseekmath
demillo1978
folio
fover-pei2025
gao-effective-rl-reward
gao-reward-overoptimization
jia-harman-survey
karwowski-goodhart-rl
kim-game-formalization
kwa-catastrophic-goodhart
lightman-verify-step
linc
logic-lm
logic-rl
lorp
lundberg-shap
manheim-goodhart-taxonomy
math-shepherd
mellgren-prolog-grpo
metr-reward-hacking
processbench
proofwriter
qwen3
reward-hacking-survey
rlsf
rubric-grpo
satlm
skalse-reward-hacking
spurious-rewards
sundararajan-ig
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d28e426-aee0-45f4-b47b-aa8d34562305",
  "isSidechain": false,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "type": "user",
  "uuid": "b579f8c9-c2b9-44d0-b30b-4adf4321e4e2",
  "toolUseResult": {
    "stdout": "=== CITE KEYS USED ===\nbondarenko-spec-gaming\ndeepseek-prover-v15\ndeepseekmath\ndemillo1978\nfolio\nfover-pei2025\ngao-effective-rl-reward\ngao-reward-overoptimization\njia-harman-survey\nkarwowski-goodhart-rl\nkim-game-formalization\nkwa-catastrophic-goodhart\nlightman-verify-step\nlinc\nlogic-lm\nlogic-rl\nlorp\nlundberg-shap\nmanheim-goodhart-taxonomy\nmath-shepherd\nmellgren-prolog-grpo\nmetr-reward-hacking\nprocessbench\nproofwriter\nqwen3\nreward-hacking-survey\nrlsf\nrubric-grpo\nsatlm\nskalse-reward-hacking\nspurious-rewards\nsundararajan-ig\n=== BIB KEYS ===\nbondarenko-spec-gaming\ndeepseek-prover-v15\ndeepseekmath\ndemillo1978\nfolio\nfover-pei2025\ngao-effective-rl-reward\ngao-reward-overoptimization\njia-harman-survey\nkarwowski-goodhart-rl\nkim-game-formalization\nkwa-catastrophic-goodhart\nlightman-verify-step\nlinc\nlogic-lm\nlogic-rl\nlorp\nlundberg-shap\nmanheim-goodhart-taxonomy\nmath-shepherd\nmellgren-prolog-grpo\nmetr-reward-hacking\nprocessbench\nproofwriter\nqwen3\nreward-hacking-survey\nrlsf\nrubric-grpo\nsatlm\nskalse-reward-hacking\nspurious-rewards\nsundararajan-ig",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5d28e426-aee0-45f4-b47b-aa8d34562305",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T23:02:53.264Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HUKkz1UJSVZGQnmcZqRKk2`</summary>

```json
{
  "command": "grep -n 'Warning\\|Rerun\\|undefined\\|multiply\\|multiply-defined' main.log 2>/dev/null | head -40",
  "description": "Check LaTeX log for warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b579f8c9-c2b9-44d0-b30b-4adf4321e4e2",
  "isSidechain": false,
  "requestId": "req_011Cb5BtTrsRo4sD1AQ8swyo",
  "type": "assistant",
  "uuid": "fbb5877e-ced6-4207-b493-32e46fdfa186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UmLtue3HffJ4HiNBGKTem4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 35,
      "cache_creation_input_tokens": 4578,
      "cache_read_input_tokens": 51002,
      "output_tokens": 690,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 35,
          "output_tokens": 690,
          "cache_read_input_tokens": 51002,
          "cache_creation_input_tokens": 4578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4578
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

_source line 45 · 2026-05-15T23:11:08.847Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now systematically analyze the findings:

1. **Citation completeness**: All cite keys match bib entries exactly — 32 cite keys, 32 bib entries, perfect match. No [?] warnings in log.

2. **Reference completeness**: All \ref targets have matching \label definitions. Let me verify by diff.

3. **LaTeX warnings**: Only float specifier `h` → `ht` changes and hyperref PDF string warnings (cosmetic). No undefined references or multiply-defined labels.

4. **Label duplication**: method.tex has both `\label{sec:rewards}` and `\label{sec:taxonomy-method}` on the same line (line 62). 

Both labels are actually used in the document, so that's fine. Now I'm checking the numerical consistency between the abstract and body text — verifying that the percentages and metrics cited in the abstract match what's reported in the experiments section. The abstract claims 93% on FOLIO, 87% for embedded conclusions, and specific ISR values, and I'm cross-referencing these against the actual experimental results. I'm continuing to verify the abstract claims against the experimental results, checking that the introduction statistics also align with the body text findings. I'm verifying the table values against the text—the exec-only condition shows PR at 93% and ISR at 0.132, which aligns with the cited numbers, and the ISR β=0.1 row matches the 70.6% H7 metric mentioned earlier (the table rounds to 71%). Now checking the random baseline condition where PR is 87±8 with ISR at 0.117±0.04 against the corresponding text reference. Now I'm checking the appendix table against the main text—the Exec-only condition with 500 steps shows 87.1% for H1, which matches what's stated in the paper, and the 7.5% non-hacking rate rounds up to 8% in Table 1, so that's consistent. Moving on to verify the ISR β=0.1 condition with its performance metrics.

For the pooled results across the three seeds, I'm calculating the mean PR as 0.77 and checking the standard deviation calculation to confirm the reported 77±14 range.

Now I'm working through the H7 percentages for the ISR β=0.1 condition by pooling the proved instances across all three seeds, which gives me 163 out of 231 total, or about 70.6%.

Moving on to the Random β=0.1 results, I'm seeing notably different performance patterns where the PR values are higher but the ISR* scores are much lower, and the distribution across H7, H1, and N-H categories shifts significantly compared to ISR.

For the pooled Random β=0.1 data, I'm calculating the mean PR across the three seeds as 0.87, and verifying this matches Table 1's reported value of 87±8 by computing the standard deviation from the individual seed values.

Now I'm working through the H7 percentages across seeds—pooling them gives 36 out of 262 total, which is about 13.74%. For N-H, I'm getting roughly 25 cases across the three seeds, totaling about 9.54% of 262, which aligns with the text's reported 9.5% and Table 1's rounded 10%.

Comparing the genuine rates, ISR at β=0.1 shows 6.06% while Random shows 9.54%, confirming the ISR approach has a lower false positive rate.

Now I'm checking the H7 subtypes section, where the text mentions H7b as an obfuscated variant.  There's a discrepancy between what Table 2 says (n=14 for H7b) and what the appendix claims (n=12), so I need to trace through the exact numbers more carefully to figure out which is correct. = 2 (s43) + 12 (s44) = 14, which aligns with Table 2's caption. The appendix line 188 appears to be discussing s44 in isolation: H7a of 77 text-matches plus H7b of 12 obfuscated samples totals 89 proved samples for s44 alone. Since s44 shows 100% H7 classification, all 89 samples fall into the H7 category, confirming the arithmetic of 77 + 12 = 89.

Now looking at line 240, which gives the combined H7 breakdown across all three seeds: s42 contributes 13 H7a samples (16% of 81), s43 has 59 H7a and 2 H7b for a total of 61, and s44 has 77 H7a and 12 H7b totaling 89. Adding these up: 13 + 61 + 89 = 163 out of 231 samples, which gives exactly 70.6%. The H7b counts also check out at 0 + 2 + 12 = 14, matching the caption. This means the total H7a across all seeds is 13 + 59 + 77 = 149.

But I need to clarify what the caption's n=149 actually represents. The caption mentions "H7a (text-match, n=149)" but doesn't specify whether this is ISR-only or includes the random condition. Looking at line 241, the random condition pooled across seeds shows 13.7% (36/262) with all 36 being H7a, driven primarily by seed 43 at 38.3% while seeds 42 and 44 contribute 0%. So the n=149 appears to be the ISR-only H7a count, separate from the random condition's 36 H7a samples. So the n=149 for H7a is ISR-only, which makes sense given that H7b references ISR-specific seeds. The caption is implicitly scoped to ISR, which is reasonable since that's where the H7 subtype discussion centers. Now let me verify the hard constraint about H7a being GRPO-universal with ISR amplifying it roughly 5×...

checking the math: 70.6% divided by 13.7% gives 5.15×, so the "~5×" claim holds up. For the total conclusion embedding across GRPO conditions, I'm seeing 85-89% for β=0.1 and 87% for exec-only, so I need to dig into the per-seed breakdown to see if the "68-100%" range is accurate.

Looking at individual seeds, the H1+H7 percentages range from 67.9% up to 100%, which validates the "68–100%" claim. Now I'm checking whether H7b is truly ISR-specific—the text mentions it appears exclusively in ISR β=0.1 seed 44, so I need to verify this constraint holds across the data.

But I'm noticing a discrepancy: the appendix shows H7b samples in both seed 43 and seed 44, not just seed 44 as the text claims. This is a contradiction I need to flag. Meanwhile, the genuine rate comparison between ISR (6.06%) and random (9.54%) shows no significant difference at p=0.182, which is an important null result to track. I'm checking the remaining constraints and terminology consistency. The paper correctly describes N-H as the residual of proved samples that don't match any of the eight cataloged patterns, which aligns with the genuine definition. I need to verify that ISR terminology is used consistently throughout.

Looking at the H7 naming conventions across the document, I notice it's referred to as "conclusion duplication," "tautological collapse," and "duplicate" in different sections. The "tautological collapse" phrasing in the experiments section appears to describe the phenomenon itself rather than just the mode name, and there's also a separate "tautological collapse" mode mentioned for exec-only results in the appendix, so the terminology isn't actually inconsistent—just applied in different contexts. Looking at the appendix section on "Tautological Collapse," I see it describes two-component formalizations where premise and conclusion are identical, and notes that the exec-only seed 44 is classified as 100% H7 by the strict classifier. But this creates a contradiction in Table 2 — if seed 44 is entirely H7, why does the "H7 duplicate" row show 0 for that seed while the "Tautological" row shows s44? Looking at the distinction more carefully, it seems H7 captures text-match detection where a single premise equals the conclusion, while "Tautological" in the table refers to a specific pattern that happens to be caught by that classifier—like Prolog s42, which shows up in the Tautological row with an H7 classification. The naming is a bit muddled, but it's not fundamentally inconsistent. Now checking the exec-only H7 results: Table 1 shows exec-only H7 at 0, which aligns with what I'm seeing in the detailed breakdown where exec-only s42 also has H7=0.

For the 1000-step runs, the text mentions that by this point all three seeds converge to high performance but with 0% non-hacking solutions, with 15 samples still escaping the text-match classifiers despite being functionally degenerate. Looking at the detailed metrics, s42 and s43 both hit 100% on their respective classifiers with no non-hacking solutions, while s44 shows 85% on H1 with those 15 samples being the ones that slip through. I'm seeing a discrepancy here—the text claims 15 samples escape text-match classifiers, but tracing through the detailed table, only 3 from s44-1000 actually escape, and the other seeds show N-H=0. Either the number 15 is incorrect, or there's something about how the samples are being counted across different classifier versions (H1/H8) that I'm missing from what's visible in the table. I'm realizing the 15 samples that escape text-match classification are the H8 cases from s44-1000, which get caught by manual inspection instead—so they're still accounted for in the "0% non-hacking" result across all three seeds, even though text-match classifiers alone wouldn't catch them. Looking at the breakdown across all three samples: s42-1000 caught all 96 by text-match, s43-1000 caught all 90 by text-match, and s44-1000 caught 85 of 100 by text-match, leaving 15 that escape—so the total count of samples escaping text-match detection is accumulating across these three datasets.

Now I'm verifying the "214× collapse" claim by checking the ratio 0.642/0.003, which confirms the calculation. Moving on to the SFT pooled statistics, I'm cross-referencing the reported PR=13.0% figure against the detailed per-seed breakdown to validate the numbers. Now I'm verifying the SFT ISR values—the table reports 0.595, and when I average the per-seed results of 0.568, 0.635, and 0.589, I get 0.597, which is close enough to the reported figure.

Actually, looking at the pooled row in the detailed table, it also shows 0.595, so it must be weighted by the number of proved instances per seed rather than a simple average. Computing it that way—(0.568×13 + 0.635×11 + 0.589×15) divided by 39 total proved instances—gives exactly 0.595. ✓

Now I'm checking the language and formatting in the experiments file, starting with the FOLIO citation and the legacy filename notation.

Looking through the abbreviations, I see STA and ISR are both defined in the abstract, and PR gets formally introduced in the experiments section. But GRPO appears in the abstract without expansion—it's cited in the method section and mentioned in the introduction, but the first use in the abstract doesn't spell it out. practice is to expand acronyms at first use. LOO is properly defined in the introduction when discussing component necessity testing, so that's fine. NLI appears in the abstract without expansion—it's common enough in NLP circles but still a minor oversight. FOL gets used in method descriptions and figure captions without being formally introduced in the text, which is another small gap to address.

Looking at the other abbreviations, SFT appears throughout the paper without expansion despite being used in the introduction and methods—it should be introduced as Supervised Fine-Tuning at first mention. Similarly, NLL shows up in the methods section describing the SFT baseline but never gets spelled out as Negative Log-Likelihood. These are all relatively minor issues since they're standard terms in the field, but the paper should still follow the convention of expanding them on first use.

The voice stays consistently active with "we" throughout, and I'm not catching any spelling problems. The ISR semantics distinction is properly maintained across all three sections where it appears. Now I need to check the taxonomy standards mentioned in the constraint.

Looking at how N-H is defined as the residual of proved samples that don't match any of the eight cataloged patterns—this aligns with the formula genuine = proved − all hacking modes. But when I examine the appendix section on H7b more closely, I'm noticing some inconsistencies in the data. The text says H7b appears exclusively in seed 44, yet the detailed table shows H7b=2 for s43 as well, and there's a mention of s44 having false negatives that complicates the picture. The table caption in experiments.tex acknowledges H7b is "primarily s44," which means the appendix's claim of "exclusively" is the inconsistency—it should say "primarily" instead. Let me verify the numbers: s44 has 12 H7b samples and s43 has 2, totaling 14, which matches. Now checking the appendix H7b section around line 188, which mentions the corrected ISR s44 count and total H7 breakdown. I'm verifying the statistical claims in the conclusion—the p-value of 1.3×10^{-39} is indeed less than the stated p<10^{-38}, and the ISR gain after controlling for premise count checks out at 1.06×. Now I'm looking at the H7b discussion around vacuous quantifier wrapping, where 10 out of 12 cases occur at ISR≥0.83, representing a triple gaming effect across execution, ISR, and classifier dimensions. Looking at the appendix data more carefully, the ISR≥0.83 metric of 10/12 samples is specifically for the s44 H7b group, while the full H7b category actually includes 14 samples total when accounting for the 2 s43 samples. The appendix frames this as s44-exclusive, which creates an inconsistency since those 2 s43 samples weren't characterized for ISR scores. Now I'm checking the random β=0.3 baseline data from Table 1 and the detailed appendix breakdown to see how the performance metrics compare across the different sample groups. Now I'm verifying the H7 calculation by breaking down each sample's contribution—s42 gives 4, s43 gives 7, and s44 contributes 0, totaling 11 out of 163 cases which rounds to 7%. For H1, I'm summing the weighted values across all three samples to get the pooled percentage.

Checking the remaining categories: the N-H pooled count comes to 3 cases (1.84%, matching the table's 2%), and I'm calculating the pooled ISR mean and standard deviation across the samples.

Now I'm verifying the claims in Experiments.tex about the random condition—the 7% pooled H7 rate checks out, and the per-seed H7a counts range from 0 to 7 as stated. Moving into the ISR β=0.3 results, I'm cross-referencing the pooled metrics from Table 1 against the detailed per-seed breakdowns. Now I'm verifying the pooled percentages across the three samples. For H7, the weighted total comes to about 50%, H1 to roughly 37%, and N-H to around 12%, which all check out against the table values.

For the ISR calculations, the mean across the three samples gives approximately 0.39, and when I look at the β=0.1 scenario, the H1 pooled percentage is about 18%, while the N-H pooled percentage matches the table's 6% value.

Now I'm trying to reconcile the raw N-H counts before and after the H8 correction—the per-seed breakdown shows 14 total N-H cases across all samples, which gives 6.06% when pooled, but I need to verify whether the table's caption about H7 inclusion affects how these numbers should be interpreted. I'm trying to reconcile the percentages in the table for s42—the individual category percentages don't seem to add up cleanly, which suggests there might be overlapping classifications or rounding issues I need to account for. The key question is whether the H8 percentage refers to 5.2% of the total 81 samples or some other subset, and how the "Mixed H1+H7+H8" label affects the count. The numbers check out across the different seed tables. Now I'm looking at the H7 footnote in Table 1, which mentions corrections for H7 classifier false negatives in s44 and H8 premise-subset gaming in s42 at 5.2%.

The ¶ symbol appears on H7 in the ISR row, so the 71% figure (which is 163 out of 231 samples) already incorporates both the H7a and H7b corrections. The footnote's mention of H8 is a bit confusing since it's attached to the H7 note, but I think it's clarifying that the ISR row's values reflect corrections for both H8 reclassification and H7 false negatives—the H8 correction primarily affects the N-H category by moving some samples there, rather than directly impacting H7.

For the introduction line about ISR amplifying tautological collapse by ~5×, the math checks out: 70.6% of proved samples show conclusion duplication versus 13.7% under matched random conditions (Fisher p<10^{-38}), which gives us 70.6/13.7 ≈ 5.15. Now I'm verifying that all cross-references have matching labels defined and that nothing's been left dangling. I'm checking which references were actually used in the document—most of the sections and figures I listed are getting marked as referenced, though I notice some duplicates in the verification list and a few entries that got cut off at the end. Continuing through the reference checks, I'm verifying that all the remaining citations match their corresponding labels. Now I'm examining some duplicate labels in the appendix and method files—there are a couple of tables and sections with multiple labels pointing to the same content, which is actually fine since it just means different references can point to the same element. Everything checks out so far.

Moving through Table 1, I'm confirming the SFT results show PR=13 with the footnote matching the detailed table breakdown, and the base model shows PR=12 which aligns with the detailed results. I'm also spot-checking the random β=0.3 condition where the non-hacking rates across seeds stay under that 4% threshold. Now I'm looking at the 100-step analysis in the appendix to verify those numbers as well. I'm noticing the 100-step checkpoint data appears in the appendix rather than the main detailed table, which explains why those H7 and H1 percentages don't show up in the line 416 reference I was checking.

Now I'm verifying the O(1) ablation numbers — the text rounds ISR* values to 0.42 and 0.132, which match the actual data from the s42 runs, so that checks out.

Looking at the H8 breakdown for the Random baseline in Table 2, I need to reconcile the individual seed results with the reported aggregate. The seeds show H8 counts of 4, 1, and 16 across the three runs, but there's overlap with H1 cases that complicates the total — I'm trying to figure out whether Table 2's H8=8 represents a percentage or raw count and how the overlaps factor in. So if H8 includes those overlaps—4 plus 1 plus 16 equals 21, which is 8% of 262—that matches what Table 2 shows. Since some H8 samples overlap with H1 (6 from s44), the union of H1 and H8 would be 186 plus 21 minus 6, giving 201. Adding in H7's 36 cases and accounting for the known overlaps, the total coverage across all three groups reaches 237 out of 262.

That leaves 25 samples unaccounted for, or about 9.5%—which checks out. So Table 2's categories aren't mutually exclusive; they can overlap, and N-H represents what's left over. This aligns with the formula that genuine cases equal proved minus the union of H7, H1, and H8.

But looking at the per-seed breakdown, there's a rounding issue. For s42, the numbers don't quite add up cleanly—22.8% of 79 should be 18, and 73.4% of 79 should be 58, but the percentages are slightly off when I work through the actual counts. ≈ 58. 0+58+4 = 62. 79-62 = 17. But N-H = 18. Off by 1.

This could be a rounding issue. 73.4% of 79 = 57.986. If that's actually 58 H1 samples, then 79-0-58-4 = 17, not 18. But if some H1 and H8 overlap, then |H1 ∪ H8| < 58+4. If there's 1 overlap, |H1 ∪ H8| = 61, and 79-61 = 18. 

OK, this is getting into very fine-grained counting. The per-seed percentages in the detailed table are computed from integer counts, so rounding to one decimal place can cause apparent inconsistencies. I'll note this as a very minor issue.

Now I'm checking the experiments.tex file more carefully. I notice "SFT pooled ISR*" appears twice in Table 1, both showing 0.595, which matches the pooled row in the detailed table. The layout is a bit confusing since ISR* and PR share the same column position, so let me trace through the detailed table format to understand the structure better. I'm working through the column alignment in this LaTeX table row. The pooled row uses `\makebox` commands with zero width to position values, and I need to verify which columns the PR value (0.130) and ISR* value (0.595) actually occupy by counting the `&` separators carefully. The final part shows the N-H% column contains 92.3 in bold, followed by a note about 39 proved cases. I'm parsing through the LaTeX table row to map each value to its correct column. The multicolumn directive spans Seed and Steps, then PR gets 0.130, ISR* is empty, and H7% should get 0.595 — but that value seems too high for a percentage metric in that context, so something's off with how I'm reading the column alignment.

Looking at the individual SFT row for reference, I can see the expected pattern: Seed, Steps, PR, ISR*, H7%, H1%, and N-H%. The zero-width box formatting in the pooled row is creating visual overflow across column boundaries, which is making it harder to track where each value actually belongs.

Now examining the pooled row structure, the multicolumn spans the first two columns for the label, then the PR value uses the zero-width box trick. The next empty column should be ISR*, followed by another zero-width box that appears to contain the 0.595 value. This formatting is intentionally placing values outside their strict column boundaries for visual alignment purposes. I see that the \makebox[0pt][l] technique is being used intentionally throughout the pooled rows — it's a clever LaTeX formatting trick that places content at the column start without consuming width, making it appear visually correct even though it's technically in a different column position. This is a deliberate layout choice, not an error. Now I'm checking the remaining experimental data, starting with the ISR β=0.3 seed 43 entry. The numbers for the 1000-step ISR run (H7 gaming at 96.7%, genuine rate dropping to 2.2%) aren't in the appendix tables, but that's acceptable since they're from actual experiments. I'm also noting that ISR*=0.88 is cited for this same configuration. Now I'm finding an internal inconsistency in appendix.tex where the H7b section claims it appears exclusively in ISR β=0.1 seed 44, but the detailed table shows seed 43 also has H7b=2, so the language should say "primarily" instead to match what's stated elsewhere.

Beyond that, I'm spotting several abbreviations that never get properly introduced: GRPO, FOL, SFT, and NLL all appear throughout the paper without their full expansions being defined. There's also a potential naming confusion where "tautological collapse" is used both as a description of H7 behavior and as the name of a separate hacking mode in the appendix, which could be clarified by using different terminology like "tautological gaming" instead.

Let me verify the PR variance calculation for those three samples—the standard deviation of 47 percentage points checks out mathematically.

Now I'm checking the claim about total conclusion embedding across conditions. The numbers show H1+H7 pooled rates are 85% under random conditions versus 89% under ISR, so the statement that embedding is "higher under random" appears to be incorrect—ISR actually shows slightly higher total embedding. I see the core issue now: the sentence structure creates ambiguity about what "is in fact higher under random" actually refers to. The grammatical subject appears to be the H1+H7 total (which would make the claim false, since ISR is 89% vs random's 85%), but the numbers cited (71% vs 18%) are only for H1 alone (where random is indeed higher). So either the sentence is factually wrong about the aggregate, or it's misleading by attaching H1-specific numbers to a statement about H1+H7.

The fix is straightforward: restructure it to make clear that the H1 comparison is what's being highlighted, something like "H1 is in fact higher under random (71% vs 18% under ISR)" rather than letting readers misinterpret it as a claim about the combined metric.

Now I'm verifying the specific claims in the conclusion against the detailed results. The random β=0.3 case checks out—H7a counts across seeds sum to 11 with a range of 0–7, and the appendix reference is valid. For the β=0.1 conclusion, I'm confirming that s42 does show the highest non-hacking rate at 22.8%, s43 peaks in H7 dominance at 38.3%, and s44 is H8-dominant, so that characterization is accurate. I see the issue now—s44 has H1 at 82% and H8 at 18%, so calling it "H8-dominant" is inaccurate. It's actually H1-dominant with the highest H8 rate among the samples. The terminology should be "highest H8" or "H8-enriched" to be precise about what s44 represents.

Now I'm checking the experiments.tex claim about s44 reaching PR=98% with H7=100% and mean n=2.04. The table confirms PR=0.98 and H7=100%, but ISR*=0.582 seems inconsistent with pure H7 collapse—if all samples are single-premise conclusions, ISR should be much higher.

Looking at the appendix, it mentions ISR=1.0 for the sole premise being necessary, yet the detailed metrics show ISR*=0.582. The discrepancy might stem from how ISR is aggregated across the two-component formalizations (1 premise + 1 conclusion per sample), where the ISR calculation spans all n components rather than just the premise-conclusion pair.

Now I'm working through the STA ablation logic: if both premise and conclusion are treated as removable components, then removing the premise causes proof failure (marking it necessary), but removing the conclusion is trickier since in a tautological case where the premise equals the conclusion, the conclusion can't be independently derived. This suggests the ISR calculation might be averaging across different ablation outcomes rather than treating the entire formalization as a single unit. other premise works differently—removing it might not break the proof, so that component contributes 0 to ISR. This gives ISR = 1/2 = 0.5 for those cases, which aligns with the observed ISR* ≈ 0.582 when accounting for samples with both premises necessary or more than two components. The numbers check out. Now looking at the exec-only 100-step result cited in the abstract—s42 shows ISR* = 0.642, which matches. And the limitations section properly references the extended discussion appendix. Let me verify the conclusion section mentions H7b with the vacuous quantifier wrapping result. I'm checking the definition of non-hacking rate—it's the proportion of samples that don't match any of the eight cataloged hacking patterns. The phrasing "necessary but not sufficient condition for semantic correctness" makes sense: a semantically correct proof must be non-hacking, but being non-hacking alone doesn't guarantee semantic correctness. That checks out. I also verified the ISR* value of 0.007 for the binary variant against the appendix, which matches.

Now looking at why the O(1) variant achieves near-zero ISR scores—the explanation is that models generate redundant premise copies, and since the O(1) variant uses a binary check during training rather than per-clause ablation, these redundant copies still pass through. When the O(1)-trained model's outputs are evaluated using standard STA evaluation, they show ISR* of 0.007, indicating the model still produces redundant formalizations despite the simplified training signal. I'm noticing the paper claims ISR*=0.007 is "indistinguishable from exec-only," but exec-only shows 0.132 at 500 steps and appears to drop to around 0.003 at 1000 steps—so the comparison depends heavily on which exec-only baseline we're looking at. The language in method.tex seems imprecise about what "indistinguishable" means here. Both 0.007 and 0.132 fall into the same low-ISR regime indicating structural degeneration, so "indistinguishable" refers to them being in the same category rather than numerically identical—a somewhat loose but defensible characterization. Now I'm verifying the reported ranges: the SFT N-H seeds of 92.3%, 90.9%, and 93.3% do round to the reported 91–93% range, and I'm double-checking the Random β=0.1 N-H values across the paper. Now I'm checking the H1 percentages across the seeds for Random β=0.1, which total to 71.4% and round to 71% in the table. But I'm noticing a discrepancy in the s42 breakdown—the N-H percentage is 22.8%, and with H7 at 0% and H1 at 73.4%, the remaining "other hacking" should be around 3.8%, which doesn't quite match the H8 note of 4 samples (5.1% of 79).

I think H1 and H8 might be overlapping categories, so some of those 4 H8 instances could be counted within the H1 group as well. If I account for that overlap—say 1 H8 overlaps with H1—then the unique contributions would be H1-only at 57, H8-only at 3, and the overlap at 1, which brings the total back to 79.

But looking at the data more carefully, there's a rounding discrepancy: 73.4% of 79 should be about 58, and if I add up H7=0, H1=58, H8=4, and N-H=18, I get 80, which is one too many. The percentages might be slightly off due to rounding—58/79 is actually 73.42%, not 73.4%.

Let me reconsider the breakdown. If complexity-without-utility is around 3.8% of 79, that's roughly 3 cases, but Table 2 shows cwu=4 for the random sample. Adding that in gives 0+58+4+3+18=83, which overshoots 79 even more. Without access to the raw data and exact overlap details between categories, I can't fully reconcile these counts—the percentages in the table are likely computed from actual counts with some rounding involved.

I think I've done enough verification here. Let me wrap this up and compile my findings.

Looking at the seven constraints I identified, none appear to be violated. The paper correctly reports that H7a is universal across GRPO with a 5× amplification from ISR, H7b is ISR-specific, the genuine rate shows no significance at p=0.182, the per-seed breakdown for random H7 is provided, the 1.06× multiplier is used for premise-count matching, GC4-par and GC4-seq aren't directly compared, and set exclusion is properly applied for the genuine category.

However, I did spot a few issues worth noting. There's a medium-severity problem where the appendix incorrectly claims H7b is "exclusive" to s44 when s43 also contains two instances, and the experimental section has ambiguous wording that could mislead readers into thinking the combined H1+H7 effect is stronger under random conditions when really only H1 shows that pattern. Beyond that, there are some minor documentation gaps—GRPO, FOL, SFT, and NLL are never formally expanded as abbreviations, and the conclusion mislabels s44's random results as "H8-dominant" when H1 actually accounts for 82% of the effect.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "359a639f-39ad-4d1d-bd8f-3f641a10f7c6",
  "isSidechain": false,
  "requestId": "req_011Cb5BuB8Zucy7fPRyRnP6A",
  "type": "assistant",
  "uuid": "5c35ec1a-d478-4fff-9f17-9ca890071142",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UEwkEcZV9Yqy8Zbkrc6vT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2324,
      "cache_read_input_tokens": 55580,
      "output_tokens": 26325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 26325,
          "cache_read_input_tokens": 55580,
          "cache_creation_input_tokens": 2324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2324
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

_source line 46 · 2026-05-15T23:11:08.850Z_

Now let me verify a couple more specific number claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c35ec1a-d478-4fff-9f17-9ca890071142",
  "isSidechain": false,
  "requestId": "req_011Cb5BuB8Zucy7fPRyRnP6A",
  "type": "assistant",
  "uuid": "42e21e84-d193-414b-a6b8-c8720224f947",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UEwkEcZV9Yqy8Zbkrc6vT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2324,
      "cache_read_input_tokens": 55580,
      "output_tokens": 26325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 26325,
          "cache_read_input_tokens": 55580,
          "cache_creation_input_tokens": 2324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2324
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

_source line 47 · 2026-05-15T23:11:21.912Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013XhTaft3juHhsNEGvtfux9`</summary>

```json
{
  "command": "python3 -c \"\n# Verify key numerical claims\nimport math\n\n# 1. ISR collapse ratio\nprint('=== ISR collapse ===')\nprint(f'0.642/0.003 = {0.642/0.003:.0f}x (claimed 214x)')\n\n# 2. H7 amplification\nprint('=== H7 amplification ===')\nprint(f'70.6/13.7 = {70.6/13.7:.1f}x (claimed ~5x)')\n\n# 3. Exec-only PR std across seeds (500-step)\nseeds = [93, 13, 98]\nmean = sum(seeds)/3\nstd = math.sqrt(sum((x-mean)**2 for x in seeds)/(len(seeds)-1))\nprint(f'Exec-only PR: mean={mean:.0f}, std={std:.1f}pp (claimed sigma=47pp)')\n\n# 4. ISR b01 PR mean/std\nisr_pr = [81, 61, 89]\nm = sum(isr_pr)/3\ns = math.sqrt(sum((x-m)**2 for x in isr_pr)/(len(isr_pr)-1))\nprint(f'ISR b01 PR: mean={m:.0f}, std={s:.0f} (claimed 77+-14)')\n\n# 5. Random b01 PR mean/std\nrnd_pr = [79, 94, 89]\nm = sum(rnd_pr)/3\ns = math.sqrt(sum((x-m)**2 for x in rnd_pr)/(len(rnd_pr)-1))\nprint(f'Rnd b01 PR: mean={m:.0f}, std={s:.0f} (claimed 87+-8)')\n\n# 6. ISR b03 PR mean/std\nisr03 = [18, 86, 95]\nm = sum(isr03)/3\ns = math.sqrt(sum((x-m)**2 for x in isr03)/(len(isr03)-1))\nprint(f'ISR b03 PR: mean={m:.0f}, std={s:.0f} (claimed 66+-42)')\n\n# 7. Rnd b03 PR mean/std\nrnd03 = [48, 92, 23]\nm = sum(rnd03)/3\ns = math.sqrt(sum((x-m)**2 for x in rnd03)/(len(rnd03)-1))\nprint(f'Rnd b03 PR: mean={m:.0f}, std={s:.0f} (claimed 54+-35)')\n\n# 8. Pooled genuine rates\nprint('=== Genuine rates ===')\nprint(f'ISR genuine: 14/231 = {14/231*100:.2f}% (claimed 6.06%)')\nprint(f'Rnd genuine: 25/262 = {25/262*100:.2f}% (claimed 9.54%/9.5%)')\n\n# 9. Pooled H7\nprint(f'ISR H7: 163/231 = {163/231*100:.1f}% (claimed 70.6%)')\nprint(f'Rnd H7: 36/262 = {36/262*100:.1f}% (claimed 13.7%)')\n\n# 10. SFT pooled\nprint(f'SFT PR: 39/300 = {39/300*100:.1f}% (claimed 13%)')\nprint(f'SFT NH: 36/39 = {36/39*100:.1f}% (claimed 92.3%)')\n\n# 11. SFT ISR weighted\nisr_w = (0.568*13 + 0.635*11 + 0.589*15)/39\nprint(f'SFT ISR* weighted: {isr_w:.3f} (claimed 0.595)')\n\"\n",
  "description": "Verify all key numerical claims computationally"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42e21e84-d193-414b-a6b8-c8720224f947",
  "isSidechain": false,
  "requestId": "req_011Cb5BuB8Zucy7fPRyRnP6A",
  "type": "assistant",
  "uuid": "89078909-ade6-4ebd-a588-e12a00ed7bde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012UEwkEcZV9Yqy8Zbkrc6vT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2324,
      "cache_read_input_tokens": 55580,
      "output_tokens": 26325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2324,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 26325,
          "cache_read_input_tokens": 55580,
          "cache_creation_input_tokens": 2324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2324
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

_source line 48 · 2026-05-15T23:11:22.003Z_

<details><summary>↩ Tool result · `toolu_013XhTaft3juHhsNEGvtfux9`</summary>

```text
=== ISR collapse ===
0.642/0.003 = 214x (claimed 214x)
=== H7 amplification ===
70.6/13.7 = 5.2x (claimed ~5x)
Exec-only PR: mean=68, std=47.7pp (claimed sigma=47pp)
ISR b01 PR: mean=77, std=14 (claimed 77+-14)
Rnd b01 PR: mean=87, std=8 (claimed 87+-8)
ISR b03 PR: mean=66, std=42 (claimed 66+-42)
Rnd b03 PR: mean=54, std=35 (claimed 54+-35)
=== Genuine rates ===
ISR genuine: 14/231 = 6.06% (claimed 6.06%)
Rnd genuine: 25/262 = 9.54% (claimed 9.54%/9.5%)
ISR H7: 163/231 = 70.6% (claimed 70.6%)
Rnd H7: 36/262 = 13.7% (claimed 13.7%)
SFT PR: 39/300 = 13.0% (claimed 13%)
SFT NH: 36/39 = 92.3% (claimed 92.3%)
SFT ISR* weighted: 0.595 (claimed 0.595)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89078909-ade6-4ebd-a588-e12a00ed7bde",
  "isSidechain": false,
  "promptId": "169bea34-34c4-423a-9946-976e7f30e506",
  "type": "user",
  "uuid": "f929bace-136c-41d7-8765-b6c4cef259be",
  "toolUseResult": {
    "stdout": "=== ISR collapse ===\n0.642/0.003 = 214x (claimed 214x)\n=== H7 amplification ===\n70.6/13.7 = 5.2x (claimed ~5x)\nExec-only PR: mean=68, std=47.7pp (claimed sigma=47pp)\nISR b01 PR: mean=77, std=14 (claimed 77+-14)\nRnd b01 PR: mean=87, std=8 (claimed 87+-8)\nISR b03 PR: mean=66, std=42 (claimed 66+-42)\nRnd b03 PR: mean=54, std=35 (claimed 54+-35)\n=== Genuine rates ===\nISR genuine: 14/231 = 6.06% (claimed 6.06%)\nRnd genuine: 25/262 = 9.54% (claimed 9.54%/9.5%)\nISR H7: 163/231 = 70.6% (claimed 70.6%)\nRnd H7: 36/262 = 13.7% (claimed 13.7%)\nSFT PR: 39/300 = 13.0% (claimed 13%)\nSFT NH: 36/39 = 92.3% (claimed 92.3%)\nSFT ISR* weighted: 0.595 (claimed 0.595)",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "89078909-ade6-4ebd-a588-e12a00ed7bde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 49_

```json
{
  "type": "last-prompt",
  "leafUuid": "f929bace-136c-41d7-8765-b6c4cef259be",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "Final TeX proofreading for paper submission",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb"
}
```

---

### Assistant

_source line 51 · 2026-05-15T23:11:24.424Z_

<details><summary>Logged reasoning block</summary>

```text
All numerical claims check out. Now let me compile the final report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f929bace-136c-41d7-8765-b6c4cef259be",
  "isSidechain": false,
  "requestId": "req_011Cb5CYfywU3r4Eyx2se27Y",
  "type": "assistant",
  "uuid": "8f72f915-31ef-47eb-9a60-1d0606718ae6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYuhmK2Vyd5RdsS5iX21Mg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26618,
      "cache_read_input_tokens": 57904,
      "output_tokens": 1554,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1554,
          "cache_read_input_tokens": 57904,
          "cache_creation_input_tokens": 26618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26618
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

_source line 52 · 2026-05-15T23:11:57.478Z_

## TeX 校对报告

**检查文件数**: 9 (main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex, limitations.tex)
**整体评价**: 需修正（2处中等问题，5处低优先级）

---

### 发现

#### 中等优先级

1. **[appendix.tex:265] 内部不一致 — H7b 排他性声明错误**
   当前文本: `"Found exclusively in ISR β=0.1 seed 44 (12/89 proved samples)"`
   但 appendix.tex:240 和 appendix.tex:429 均显示 s43 也有 H7b=2 样本。experiments.tex:161 表格 caption 正确使用了 `"primarily s44"`。应改 `exclusively` → `primarily` 或 `"found in ISR β=0.1 seeds 43 (n=2) and 44 (n=12)"`。

2. **[experiments.tex:72] 语法歧义导致数字误读**
   当前文本: `"Total conclusion embedding (H1+H7) is GRPO-universal at 68–100% across both conditions, and is in fact \emph{higher} under random (pooled H1 71% vs. 18% under ISR)."`
   语法主语是 "Total conclusion embedding (H1+H7)"，但 H1+H7 pooled 实际是 ISR 89% > Random 85%，并非 random 更高。括号中的 71% vs 18% 仅指 H1。建议拆句：`"...across both conditions. H1 alone is higher under random (pooled 71\% vs.\ 18\% under ISR)---ISR converts H1 into H7 rather than reducing total embedding."`

#### 低优先级

3. **[全文] 缩略语 GRPO 未展开**
   从 abstract 开始使用 GRPO，全文未出现 "Group Relative Policy Optimization (GRPO)"。建议在 abstract 或 method.tex:15 首次使用处展开。

4. **[全文] 缩略语 FOL 未正式引入**
   Introduction 写 "first-order logic problems"，但后续直接使用 FOL 未做 "(FOL)" 定义。建议在 method.tex:13 或 introduction 中加 "first-order logic (FOL)"。

5. **[全文] SFT 未展开**
   全文未出现 "Supervised Fine-Tuning (SFT)"。建议在 method.tex:64 首次出处展开。

6. **[method.tex:64] NLL 未展开**
   `"SFT baseline (NLL on gold formalizations)"` 中 NLL 未定义为 "negative log-likelihood"。

7. **[conclusion.tex:15] "H8-dominant" 用词不准**
   `"random β=0.1 ranges from H8-dominant (s44) to..."` — s44 实际 H1=82%, H8=18%，H1 才是主导模式。建议改为 `"H8-enriched"` 或 `"highest-H8"`。

---

### 硬约束违规

**无违规。** 七条硬约束全部满足：
- H7a GRPO-universal + ISR amplifies ~5x: experiments.tex:69 正确 (5.15x) ✓
- H7b ISR-specific: 仅出现在 ISR seeds ✓
- genuine rate p=0.182 n.s., 未 claim 显著差异: experiments.tex:80 ✓
- Random H7 per-seed 分解 (38.3%/0%/0%): experiments.tex:70 + Table 1 caption ✓
- premise-count-matched 1.06x: experiments.tex:79 ✓
- ISR 双语义区分 (redundancy vs gaming): experiments.tex:121, conclusion.tex:7, method.tex:83 ✓
- genuine = proved − hacking (set排除): experiments.tex:11 ✓

---

### 引用完整性

- **\cite{}**: 32 个 cite key 与 references.bib 32 条 entry **完全匹配**，无遗漏无多余 ✓
- **\ref{}/\label{}**: 所有 ref 目标均有对应 label，无悬挂引用 ✓
- **LaTeX log**: 无 undefined reference 或 multiply-defined label 警告 ✓（仅有 float `h`→`ht` 和 hyperref PDF string 警告，均为 cosmetic）

---

### 数字一致性

所有关键数字经交叉验证正确：214x collapse ✓, ~5x amplification (5.15x) ✓, σ=47pp ✓, 所有 mean±std ✓, 所有 pooled 百分比 ✓, Fisher p 值 ✓, SFT weighted ISR*=0.595 ✓。

---

### 建议修正（按优先级）

1. **appendix.tex:265** — `exclusively` → `primarily` （与 experiments.tex:161 保持一致）
2. **experiments.tex:72** — 拆句避免 H1+H7 vs H1-only 歧义
3. **method.tex 或 abstract** — 展开 GRPO/FOL/SFT/NLL 缩略语（4 处）
4. **conclusion.tex:15** — `H8-dominant` → `H8-enriched`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f72f915-31ef-47eb-9a60-1d0606718ae6",
  "isSidechain": false,
  "requestId": "req_011Cb5CYfywU3r4Eyx2se27Y",
  "type": "assistant",
  "uuid": "12a73b38-f341-4b44-84ab-6dd39b5f9693",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYuhmK2Vyd5RdsS5iX21Mg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26618,
      "cache_read_input_tokens": 57904,
      "output_tokens": 1554,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1554,
          "cache_read_input_tokens": 57904,
          "cache_creation_input_tokens": 26618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26618
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

_source line 53_

```json
{
  "type": "last-prompt",
  "leafUuid": "12a73b38-f341-4b44-84ab-6dd39b5f9693",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Final TeX proofreading for paper submission",
  "sessionId": "ff2a3926-a23a-4756-aa8c-9df2956fd4eb"
}
```

---
