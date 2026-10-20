# Research conversation: <project_context> # 项目: solver-trace-ablation ## 运行环境 - 服务器名: westd-39279 - SSH 账户: root（调用 ssh_execute / submit_trainin

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/9fbe86a1-ca6c-45c2-ba33-211d5991aa93.jsonl`
- **Structured JSON:** [`3ef99bb68b614cf9408d.json`](../../sessions/3e/3ef99bb68b614cf9408d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T18:17:33.610Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T18:17:33.610Z",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "content": "&lt;project_context>\n# 项目: solver-trace-ablation\n\n## 运行环境\n- 服务器名: westd-39279\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/solver-trace-ablation\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 所有实验统一使用 data/train_500_seed42.jsonl 作为训练数据，禁止使用 proofwriter_fol_500.jsonl 或其他数据文件（原因：Reviewer CRITICAL: plan001-s43 使用了不同数据文件导致多 seed 对比 confound。多 seed 实验必须控制数据变量，seed 仅控制模型初始化和训练随机性。）\n- **C002**: 提交训练任务前必须用 export CUDA_VISIBLE_DEVICES=N 显式设置 GPU，禁止 inline 赋值（bash -c VAR=X cmd），提交后验证 nvidia-smi 确认只占用分配的 GPU（原因：plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43 OOM 死亡。这是第二次 GPU 冲突事故。）\n- **C003**: 训练配置必须设置 save_total_limit=1 且禁用/限制 completions parquet 保存，防止磁盘耗尽（原因：plan013-r3 和 plan001-s43-r3 因磁盘 250G/250G 满导致 step 23/28 崩溃。根因：TRL 每实验保存 3 份模型权重（~48GB）+ completions parquet（~2.5GB）。）\n- **C004**: 跨 seed/跨 run 的 ISR 对比必须使用 eval_sta.py 统一评估，禁止引用训练日志 ISR 做跨 run 对比（不同 run 可能使用不同版本的 ISR 计算代码）（原因：Reviewer 核实发现 plan001-s42-r2 训练日志 ISR 使用 binary _fast_fn，plan001-s43-r4 使用 full STA _full_fn，同一指标名下计算方法不同导致不可比。论文中所有 ISR 数据必须来自 eval_sta.py 统一评估。）\n- **C005**: 所有 worker（含 fix/ops 类）启动任何 Python 进程前必须显式设置 CUDA_VISIBLE_DEVICES，禁止裸跑（原因：fix worker 未设 CUDA_VISIBLE_DEVICES 导致测试进程泄漏到 cuda:1（plan017 训练卡），占用 8638 MiB 显存。2026-05-14 事故。）\n- **C006**: 论文讨论 ISR 时必须区分两种语义：exec-only 的 low ISR = 冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR = metric gaming（Goodhart 效应）。不可将 ISR 差异直接等同于 reasoning 能力差异。（原因：Reviewer 发现 Prolog exec-only 生成大量重复 ground facts（如 penguin(fido). 出现 3 次），per-clause ablation 下删任一重复不影响结果，ISR=0。这是冗余不是无推理。如不区分，审稿人会误读 ISR 差异。）\n- **C007**: kill_job 后必须 nvidia-smi 确认 GPU 释放，submit 前必须 nvidia-smi 确认目标 GPU 无残留进程（原因：同一 session 两次出现 kill tmux → Python orphan → 新实验 OOM 的 pattern。kill_job 只杀 tmux session 不杀进程组，submit_on_allocated 只检查 registry 不检查实际 GPU 占用。）\n- **C008**: 所有 eval 命令必须显式指定 --data_path data/proofwriter_fol_100.jsonl，禁止依赖默认值或使用 test_100.jsonl（原因：D063: exp1 系列 eval 使用了 test_100.jsonl（与论文数据集零重叠），导致结果不可比。C004 约束的加固版。） [来自 D063]\n- **C009**: 所有 eval 命令必须显式指定 --data_path data/proofwriter_fol_100.jsonl，禁止使用默认值或 test_100.jsonl（原因：exp1 系列 eval 使用了错误的 test_100.jsonl（与 plan 系列的 proofwriter_fol_100.jsonl 零重叠），导致跨系列数据不可比。违反 C004。） [来自 D062]\n- **C010**: 磁盘清理禁止删除 conclusion=success 且标记 needs-re-eval 的 checkpoint，删前必须检查 registry 状态（原因：disk-cleanup-v2 误删了 exp1-isr-b03-s43 和 exp1-random-b03-s43 的 checkpoint，导致必须重训。这两个 checkpoint 因 D062/D063 需要用正确测试集 re-eval。）\n- **C011**: 磁盘清理禁止删除 conclusion=success 且标记 needs-re-eval 的 checkpoint 目录（原因：disk-cleanup-v2 Worker 误删 exp1_isr_b03_s43 和 exp1_random_b03_s43 checkpoint，导致必须重训。清理前必须交叉检查 registry 中 re-eval 标记。）\n- **C012**: Resume 训练时必须验证步数语义：--model_path 指向 checkpoint 时，确认 train_grpo.py 是从该 step 继续（resume）还是从 0 开始新训练。如不确定，从 base model 重新训练，不用 checkpoint。禁止第三次犯 resume 步数不对等错误。（原因：Agent 两次将 checkpoint-350 作为 model_path 启动 1000 步训练，实际训练了 1350 步（350+1000）而非 resume 到 1000 步，导致与 ISR 1000 步实验不可比。plan018-r2 数据作废。）\n- **C013**: Taxonomy 标准：genuine = proved − H7 − H1_exact − H8。H1-near 保留为 genuine 但单独标记。ISR 和 Random 两侧必须对称使用同一标准。（原因：D084 决策。H8 是退化证明必须扣除；H1-near 仍需推理步骤保留为 genuine；标准必须两侧对称以确保论文方法论一致性。） [来自 D084]\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：预起草 Framing 调整提案（H7 specificity → amplification）\n\n### 背景\n项目 solver-trace-ablation 研究 STA/ISR 作为 GRPO neurosymbolic formalizer 的诊断工具。\n\n**关键转折 (D092/D093)**：\n- 之前的叙事：ISR 3-seed H7=64.5% vs Random H7=0%，H7 是 ISR-specific 的 hacking mode\n- D093 发现：Random s43-r3 重训后 H7=38.3%，推翻了 \"Random H7=0%\" 的结论\n- 之前 Random s43/s44 数据被标记 DEPRECATED（原始数据丢失无法溯源），正在重训\n- 目前 Random s42 H7=0%, s43-r3 H7=38.3%, s44-r2 还在跑\n\n**Claim 2 框架**：ISR-as-reward 展现 meta-level Goodhart（ISR 无结构优势，premise-count-matched 1.06x，β 剂量效应）。H7 specificity 是 Claim 2 的一个子论据，不是核心。\n\n**其他重要决策**：\n- D084: genuine = proved − H7 − H1_exact − H8\n- D085: H7a (text-match) + H7b (obfuscated tautology)\n- D089: exec-only 1000步 hacking mode seed-dependent\n- D051: 2.4x 作废，premise-count-matched 1.06x 定论\n\n### 你要做的事\n\n1. **读 paper_framing.md**：`read_project_file(project=\"solver-trace-ablation\", file=\"paper_framing.md\", max_chars=0)` 获取完整 framing\n\n2. **读 decisions.yaml 中 D092 和 D093**：`read_project_file(project=\"solver-trace-ablation\", file=\"decisions.yaml\", max_chars=0)` 找到相关决策\n\n3. **读 memory.md**：`read_project_file(project=\"solver-trace-ablation\", file=\"memory.md\")` 获取历史经验\n\n4. **起草 Framing 调整提案**，按 red-section 规范：\n   - **原 claim**：H7 是 ISR-specific 的 tautological collapse mode（Random 3-seed H7=0%）\n   - **实验结果**：Random s43-r3 H7=38.3%（D093），推翻 exclusive specificity\n   - **重新审视**：H7 不是 ISR 独有，但 ISR 可能 amplify H7 频率/严重度。关键问题：\n     a) ISR vs Random 的 H7 rate 对比（等 s44-r2 后完整）\n     b) H7 是否与 additive bonus 机制相关（D088 的论点）\n     c) Claim 2 核心（1.06x 无结构优势）是否受影响\n   - **3 种备选叙事骨架**：\n     1. ISR amplifies H7 (dose-response) 而非 exclusively causes it\n     2. H7 is reward-general (both ISR and Random exhibit it), 强化 Goodhart universality\n     3. H7 frequency is seed/config-dependent, 属于 hacking mode diversity 的一部分\n   - **对论文各章节的影响**（abstract/intro/method/experiments/discussion/conclusion）\n   - **建议下一步**（至少 3 组备选实验方向）\n\n5. **产出**：将提案保存到 `save_project_file(project=\"solver-trace-ablation\", file=\"memory.md\", ...)` 的末尾追加一个 section，标题为 `## [DRAFT] Framing 调整提案 — H7 Specificity (D092/D093)`。注意：这是草稿，标注 DRAFT，等 s44-r2 数据后正式定稿。\n\n### 注意\n- 这是预起草，s44-r2 还没出结果，所以提案中 Random 3-seed pooled 数据标为 PENDING\n- 不要在提案中使用任何 DEPRECATED 的旧数据（s43 旧版、s44 旧版）\n- 保持客观，不要 cherry-pick"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T18:17:33.614Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T18:17:33.614Z",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93"
}
```

---

## Round 1

34 recorded events

### User

_source line 3 · 2026-05-15T18:17:33.651Z_

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
## 任务：预起草 Framing 调整提案（H7 specificity → amplification）

### 背景
项目 solver-trace-ablation 研究 STA/ISR 作为 GRPO neurosymbolic formalizer 的诊断工具。

**关键转折 (D092/D093)**：
- 之前的叙事：ISR 3-seed H7=64.5% vs Random H7=0%，H7 是 ISR-specific 的 hacking mode
- D093 发现：Random s43-r3 重训后 H7=38.3%，推翻了 "Random H7=0%" 的结论
- 之前 Random s43/s44 数据被标记 DEPRECATED（原始数据丢失无法溯源），正在重训
- 目前 Random s42 H7=0%, s43-r3 H7=38.3%, s44-r2 还在跑

**Claim 2 框架**：ISR-as-reward 展现 meta-level Goodhart（ISR 无结构优势，premise-count-matched 1.06x，β 剂量效应）。H7 specificity 是 Claim 2 的一个子论据，不是核心。

**其他重要决策**：
- D084: genuine = proved − H7 − H1_exact − H8
- D085: H7a (text-match) + H7b (obfuscated tautology)
- D089: exec-only 1000步 hacking mode seed-dependent
- D051: 2.4x 作废，premise-count-matched 1.06x 定论

### 你要做的事

1. **读 paper_framing.md**：`read_project_file(project="solver-trace-ablation", file="paper_framing.md", max_chars=0)` 获取完整 framing

2. **读 decisions.yaml 中 D092 和 D093**：`read_project_file(project="solver-trace-ablation", file="decisions.yaml", max_chars=0)` 找到相关决策

3. **读 memory.md**：`read_project_file(project="solver-trace-ablation", file="memory.md")` 获取历史经验

4. **起草 Framing 调整提案**，按 red-section 规范：
   - **原 claim**：H7 是 ISR-specific 的 tautological collapse mode（Random 3-seed H7=0%）
   - **实验结果**：Random s43-r3 H7=38.3%（D093），推翻 exclusive specificity
   - **重新审视**：H7 不是 ISR 独有，但 ISR 可能 amplify H7 频率/严重度。关键问题：
     a) ISR vs Random 的 H7 rate 对比（等 s44-r2 后完整）
     b) H7 是否与 additive bonus 机制相关（D088 的论点）
     c) Claim 2 核心（1.06x 无结构优势）是否受影响
   - **3 种备选叙事骨架**：
     1. ISR amplifies H7 (dose-response) 而非 exclusively causes it
     2. H7 is reward-general (both ISR and Random exhibit it), 强化 Goodhart universality
     3. H7 frequency is seed/config-dependent, 属于 hacking mode diversity 的一部分
   - **对论文各章节的影响**（abstract/intro/method/experiments/discussion/conclusion）
   - **建议下一步**（至少 3 组备选实验方向）

5. **产出**：将提案保存到 `save_project_file(project="solver-trace-ablation", file="memory.md", ...)` 的末尾追加一个 section，标题为 `## [DRAFT] Framing 调整提案 — H7 Specificity (D092/D093)`。注意：这是草稿，标注 DRAFT，等 s44-r2 数据后正式定稿。

### 注意
- 这是预起草，s44-r2 还没出结果，所以提案中 Random 3-seed pooled 数据标为 PENDING
- 不要在提案中使用任何 DEPRECATED 的旧数据（s43 旧版、s44 旧版）
- 保持客观，不要 cherry-pick

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "3607f857-899c-41b1-8c04-f693ac82b7c2",
  "type": "user",
  "uuid": "cd16cc35-d70b-4257-aa34-6aa4f3daae23",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T18:17:33.650Z_

```json
{
  "parentUuid": "cd16cc35-d70b-4257-aa34-6aa4f3daae23",
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
  "uuid": "2ea976b5-22e6-478f-8d27-3e6453f349c9",
  "timestamp": "2026-05-15T18:17:33.650Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T18:17:33.650Z_

```json
{
  "parentUuid": "2ea976b5-22e6-478f-8d27-3e6453f349c9",
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
  "uuid": "8a450d6f-c143-41fb-a488-139b47380a14",
  "timestamp": "2026-05-15T18:17:33.650Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T18:17:33.650Z_

```json
{
  "parentUuid": "8a450d6f-c143-41fb-a488-139b47380a14",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a2ed6d7c-5863-4f91-b257-bd723043866e",
  "timestamp": "2026-05-15T18:17:33.650Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
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
  "aiTitle": "Draft H7 specificity framing adjustment proposal",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93"
}
```

---

### Assistant

_source line 8 · 2026-05-15T18:17:36.687Z_

我来读取所需的项目文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2ed6d7c-5863-4f91-b257-bd723043866e",
  "isSidechain": false,
  "requestId": "req_011Cb4p9DKrdLZRNmv1VZ5Kg",
  "type": "assistant",
  "uuid": "97681382-3b38-44e2-bf95-aa91840000e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhhdyqyTr4GK8nA7xpACoX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13830,
      "cache_read_input_tokens": 11841,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13830,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 129,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13830
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

_source line 9 · 2026-05-15T18:17:37.638Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ErqFoJgyftpARFLZhjgMhF`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97681382-3b38-44e2-bf95-aa91840000e5",
  "isSidechain": false,
  "requestId": "req_011Cb4p9DKrdLZRNmv1VZ5Kg",
  "type": "assistant",
  "uuid": "ff8943ef-b74a-4c24-95eb-b5679518c542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhhdyqyTr4GK8nA7xpACoX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13830,
      "cache_read_input_tokens": 11841,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13830,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 129,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13830
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

_source line 10 · 2026-05-15T18:17:37.647Z_

<details><summary>↩ Tool result · `toolu_01ErqFoJgyftpARFLZhjgMhF`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff8943ef-b74a-4c24-95eb-b5679518c542",
  "isSidechain": false,
  "promptId": "3607f857-899c-41b1-8c04-f693ac82b7c2",
  "type": "user",
  "uuid": "9a774ea7-1913-4aa1-9a31-57f223a262bb",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__append_idea"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "ff8943ef-b74a-4c24-95eb-b5679518c542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-15T18:17:40.396Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the three files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a774ea7-1913-4aa1-9a31-57f223a262bb",
  "isSidechain": false,
  "requestId": "req_011Cb4p9WPXZ6nC4VSUtLCq8",
  "type": "assistant",
  "uuid": "c7592c25-b5f6-4715-a8c2-283994c3bde0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2k4p64ZGFMk7JGiA1DApp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 25671,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 907,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 25671,
          "cache_creation_input_tokens": 907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 907
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

_source line 12 · 2026-05-15T18:17:40.924Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01L2HhLxApen6pFCHFFKmTkh`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7592c25-b5f6-4715-a8c2-283994c3bde0",
  "isSidechain": false,
  "requestId": "req_011Cb4p9WPXZ6nC4VSUtLCq8",
  "type": "assistant",
  "uuid": "60ca8b31-1700-4142-8106-138766c11c6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2k4p64ZGFMk7JGiA1DApp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 25671,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 907,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 25671,
          "cache_creation_input_tokens": 907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 907
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

_source line 13 · 2026-05-15T18:17:40.947Z_

<details><summary>↩ Tool result · `toolu_01L2HhLxApen6pFCHFFKmTkh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (8 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\n- Hacking taxonomy: 8 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation + D085 H7b obfuscated tautology + Prolog query-as-fact gaming)\\n\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR），在高剂量产生**极端跨 seed 不稳定 + 多模态 Goodhart 路径**（β=0.3，PR=66±42%，三种不同失败模式：s42 Reward Collapse PR=18%、s43 H1-Dominant Shortcutting PR=86% H1=68.6%、s44 Pure H7 Meta-Goodhart PR=95% H7=100% + ISR=0.742 被同时 game）。ISR-as-reward **不提供任何真实结构优势**。\\n\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\n\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\n\\n| 条件 | n | Mean n_prem | Mean ISR |\\n|------|---|-------------|----------|\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\n| **Ratio** | — | — | **1.06×** |\\n\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\n- ISR s42 的 15/26 \\\"genuine\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\n- ISR s44 的 12 个\\\"genuine\\\"全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分（meta-Goodhart 直接证据）\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高，与证明质量无关\\n\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\n\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **100%** (89/89, H7 FN corrected) | 0% | 100% | **0%** (0; 12 原 \\\"genuine\\\" 全为 n_prem=1 H7 false negative) |\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **73.4%** (58/79) | 73.4% | **22.8%** (18; H8=4, D086 clean run) |\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | ⚠️ ~~6.8% (6)~~ **PROVISIONAL — 重训中 (s43-r3)，原数据丢失无法溯源** |\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | ⚠️ ~~20.2% (18)~~ **PROVISIONAL — 重训中 (s44-r2)，原数据丢失，18 是推算值从未直接测量** |\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | ⚠️ ~~18.4% pooled (47/256)~~ **DEPRECATED — 待 s43-r3/s44-r2 重训完成后用新数据重算。所有聚合统计量（Fisher p, Wilson CI, genuine rate）必须用新数据重算** |\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **75.3% (H7 FN corrected)** | **17.3%** | — | **6.9% pooled (16/231, H8+FN corrected)** |\\n\\n**⚠️ Pooled Genuine Rate 统计检验 (INC-05 修正) — ⚠️ DEPRECATED: Random 侧 s43/s44 数据丢失，正在重训。以下数字待重训完成后全部重算。**\\n\\n原 \\\"identical genuine rates (Fisher p=1.0)\\\" 已失效。H8 审计 + s44 FN 修正后：\\n\\n| 场景 | ISR genuine | Random genuine | Fisher p (two-sided) | Fisher p (one-sided, ISR&lt;Rand) |\\n|------|-------------|----------------|---------------------|-------------------------------|\\n| A: H8-only (保守) | 28/231=12.1% [8.5%, 17.0%] | ~~47/256=18.4%~~ **DEPRECATED** | ~~p=0.060~~ | ~~p=0.037~~ |\\n| B: H8+s44 FN (完整) | 16/231=6.9% [4.3%, 11.0%] | ~~47/256=18.4%~~ **DEPRECATED** | ~~p=0.0002~~ | ~~p=0.0001~~ |\\n\\nWilson 95% CI 括号内标注。**Random 侧数字（47/256）包含 s43 genuine=6 和 s44 genuine=18（推算值），两者原始数据丢失，正在重训。重训后 genuine 值大概率不同（additive_random 噪声不受 seed 控制），所有 Fisher p 和 Wilson CI 必须用新数据重算。**\\n\\n⚠️ **H8 审计覆盖说明**：仅 s42 完成了完整双侧 H8 审计（genuine 26→14）。s43/s44 checkpoint 已删除，无法补做 H8 审计。场景 A 的 28/231 中 s43(2)/s44(12) 未扣 H8，为上界。场景 B 在 A 基础上修正 s44 FN（12→0），仍未扣 s43/s44 的 H8。论文应报告两个场景作为 bounds。\\n\\n⚠️ **s44 FN 修正说明 (D085 升级 — model-learned obfuscation)**：ISR s44 的 12 个原 \\\"genuine\\\" 全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分。这是 **meta-Goodhart 的直接证据**——不仅 reward 被 game，连 tautology 检测器也被 game。H7 子分类：H7a (text-match, 77 个) + H7b (obfuscated, 12 个) = H7 total 89。证据文件：`/root/autodl-tmp/outputs/isr_s44_fn_evidence.json`。\\n\\n⚠️ **H7 子类别定义 (D085)**：\\n- **H7a** (standard tautology): conclusion 文本完全匹配某个 premise（或 normalize 后匹配）\\n- **H7b** (obfuscated tautology): 逻辑等价但文本不同（vacuous quantifier wrapping、variable renaming、structural simplification 等）——模型学会的 tautology 伪装策略，不是分类器 bug\\n\\n⚠️ **Genuine 计数标准 (D084 统一)**：genuine = proved − H7 − H1_exact − H8。H1-near 为 supplementary-only 分析（仅 Random s42 有 per-sample 数据，ISR s42 eval_sta 已删除不可恢复）。两侧对称：ISR s42 genuine=14 (17.3%), Random s42 genuine=18 (22.8%, D086 clean run)。\\n\\n**关键发现 (D057 3-seed closed)**：\\n- **H7 是 ISR-specific gaming（β=0.1 定论，β=0.3 有梯度）**：β=0.1 下 ISR 3-seed H7=64.5% (149/231)，Random β=0.1 3-seed H7=**0%** (0/256)，跨全部 3 random seeds 一致为零。β=0.3 Random 出现少量 H7a（s42=4, s43-r4=7），呈明显剂量梯度（β=0.1: 0% → β=0.3: 4-7 个 → ISR β=0.1: 64.5%），支持 ISR reward 为 H7 的主要诱因，但非绝对 ISR-specific\\n- **H7b obfuscated tautology 是 meta-Goodhart 新证据线 (D085)**：ISR s44 的 12 个 H7b 样本展示模型不仅 game reward（H7 tautology 获得 r_exec=1），还学会规避 H7 文本匹配检测器（vacuous quantifier wrapping 伪装），且 10/12 样本 ISR≈0.8 同时 game 了 ISR 评分。三层 gaming 堆叠：execution reward + structural metric + diagnostic classifier = meta-Goodhart 的最完整案例\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\n\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044→H8 校准)**：\\n- ISR β=0.1 genuine: **17.3%** (14/81, D084 标准) vs random β=0.1 genuine: **22.8%** (18/79, D086 clean run) — **-5.5pp（ISR 反而更低）**\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 73.4% — GRPO 通用退化\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** (H7a 13) vs random **0%** — ISR 特异性\\n- H8 (conjunction collapse): ISR **14.8%** (12/81) vs random **5.1%** (4/79, D086 clean run)\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\n- 整体 hacking rate (D084 标准, H7+H1_exact+H8): ISR **82.7%** vs random **77.2%** (D086 clean run) — **ISR hacking 更高**\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/100% FN-corrected），无 H1\\n\\n**证据（β=0.3 同剂量对照）**：\\n\\n✅ **D062 数据修正完成**：ISR s43/s44 已用 proofwriter_fol_100.jsonl 重新 eval。s43 genuine 从旧 test_100 的 67% 大幅降至 26.7%（旧数据是假象）。\\n\\nISR β=0.3 三 seed（✅ 全部 proofwriter_fol_100.jsonl）：\\n| Seed | PR | ISR* | H7% | H1% | Genuine% | 模式 |\\n|------|-----|------|-----|-----|----------|------|\\n| s42 | **18%** | 0.143 | 0 | 78 | 22 | **Reward Collapse**（PR 崩塌） |\\n| s43 | **86%** | 0.295 | 4.7 | **68.6** | **26.7** | **H1-Dominant Shortcutting** |\\n| s44 | **95%** | 0.742 | **100** | 0 | **0** | **Pure H7 Meta-Goodhart** |\\n| mean±std | **66±42** | 0.393±0.31 | 35±55 | 49±42 | 16±15 | 三种不同失败路径 |\\n\\nRandom β=0.3（s42/s44 完成，s43 训练中）：\\n| Seed | PR | ISR* | H7% | H1% | Genuine% | 状态 |\\n|------|-----|------|-----|-----|----------|------|\\n| s42 | 48% | 0.094 | **8.3** (4) | 91.7 | 0 | ✅ 完成 (D086: H7a=4) |\\n| s43 | — | — | — | — | — | 训练中 (exp1-random-b03-s43-r4, 前次 H7a=7) |\\n| s44 | **23%** | **0.000** | 0 | **100** | 0 | ✅ 完成 |\\n| 2-seed mean | **35.5%** | 0.047 | ~4 | ~96 | 0 | — |\\n\\n- **D060 叙事调整**：Random β=0.3 也严重崩塌（2-seed mean PR=35.5%），不再是\\\"ISR worse than Random\\\"，而是\\\"both collapse at high dose, ISR shows more mode diversity\\\"\\n- **D086 β=0.3 H7 gradient evidence**：Random β=0.3 出现 H7a（s42=4, s43-r4=7），而 β=0.1 Random H7=0%。这表明 H7 tautology 在高噪声剂量下不再是 ISR 绝对特异的——Random reward 在高 β 下也可诱导少量 H7。H7 梯度：Random β=0.1 (0%) → Random β=0.3 (4-7) → ISR β=0.1 (64.5%)。论文应在 Discussion 讨论此 dose-response gradient\\n- ISR β=0.3 三种不同路径 (Reward Collapse / H1-Dominant / Pure H7) vs Random β=0.3 均匀的 H1+ISR=0 崩塌\\n- s43 旧数据 (test_100.jsonl) 显示 67% genuine 是假象；正确测试集下 genuine=26.7%，主要靠 H1 hacking（68.6%）\\n- **结论（待 s43 确认）**：β=0.3 对两种 reward 条件都是有害的；ISR 特有的是 mode diversity 而非更差的 PR\\n\\n**β 剂量效应全景**：\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\n| 0.3 | **0.66±0.42** (s42=0.18/s43=0.86/s44=0.95) | 0.48 (s42) / s43 训练中 / 0.23 (s44) | 0.393±0.31 | 0.094 (s42) / s43 pending / 0.000 (s44) | 多模态 Goodhart 不稳定：Reward Collapse / H1-Dominant Shortcutting / Pure H7 Meta-Goodhart |\\n\\n**其他 ISR-as-reward 失败模式**：\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\n\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\n\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\"genuine\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\n\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\n\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\n\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\n  - s42: PR=83%, proved-only ISR*=0.037 (ground fact enumeration, near-zero)\\n  - s43: PR=56%, proved-only ISR*=0.015 (degraded, near-zero)\\n  - s44: PR=21%, proved-only ISR*=0.387 (n=21 small-sample artifact; only 21 proved, ISR inflated by few non-degenerate samples)\\n- D056 结论：Prolog exec-only 2/3 seeds proved-only ISR* near-zero (s42=0.037, s43=0.015)，与 FOL exec-only 崩塌模式对应。s44 ISR*=0.387 是 small-sample artifact (n=21)，不代表结构完好。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\n- ⚠️ **ISR 指标统一 (Reviewer warning)**：全文统一使用 proved-only ISR*（排除 unproved=0 样本）。All-sample ISR 混入 PR 信息，不适合作为独立结构指标。旧的 \\\"ISR<0.1 across all seeds\\\" 措辞已修正。\\n\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\n\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\n\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\"100% Genuine\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\"Genuine=100%\\\" 不可信，必须交叉验证 n_necessary 分布。**\\n\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\n- 每个 seed 发展出不同的 gaming pathway：\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\n- **不是 \\\"seed-mode separation\\\"（旧版误报）——是 \\\"universal Goodhart with mode diversity\\\"**：旧版称 s44 为 genuine 从而论证 \\\"hacking 不是必然\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\n\\n**FOL vs Prolog ISR-as-reward 对比**：\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\n\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\"genuine improvement\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), ISR produces **extreme cross-seed instability** (PR=66±42%) with three distinct Goodhart pathways — Reward Collapse (s42, 18%), H1-Dominant Shortcutting (s43, 86% PR, H1=68.6%, genuine=26.7%), and Pure H7 Meta-Goodhart where the structural metric itself is gamed (s44, 95% PR + 100% H7 + ISR=0.742)\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (8 modes identified, including ISR-specific \\\"conclusion duplication with ISR inflation\\\", H7b \\\"obfuscated tautology\\\" via vacuous quantifier wrapping that evades text-match detectors, H8 \\\"conjunction collapse\\\", and Prolog-specific \\\"query-as-fact gaming\\\")\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\"genuine improvement\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\n- **Headline result**: \\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), ISR produces extreme cross-seed instability (PR=66±42%) with three distinct Goodhart pathways: Reward Collapse (18%), H1-Dominant Shortcutting (86% PR, 68.6% H1, only 26.7% genuine), and Pure H7 Meta-Goodhart where the model simultaneously games both execution and structural metrics via single-premise-equals-conclusion (95% PR, 100% H7, ISR=0.742 — a fake-high). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 8 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n\\n**论文处理**：降级为 **Limitation / Future Work**。\\n\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\n\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\n\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\n|------|------|---------|----------|----------|---------------|\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 100%** (H7a=77 + H7b=12, FN corrected), ISR inflation + classifier evasion | **meta-Goodhart** (triple: reward + ISR + detector) |\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | ⚠️ PROVISIONAL — 重训中 |\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | ⚠️ PROVISIONAL — 重训中 |\\n| ISR β=0.3 (s42) | r = r_exec·(1+0.3·ISR) | 0.18 | 0.143 | PR 崩塌（经典 Goodhart） | post-Goodhart |\\n| ISR β=0.3 (s43) | r = r_exec·(1+0.3·ISR) | 0.86 | 0.295 | **H1=68.6%**, H7=4.7%, genuine=26.7% — H1-Dominant Shortcutting | **meta-Goodhart (H1 path)** |\\n| ISR β=0.3 (s44) | r = r_exec·(1+0.3·ISR) | 0.95 | **0.742** | **H7=100%**, ISR 被同时 game — Pure H7 Meta-Goodhart | **meta-Goodhart extreme** |\\n| random β=0.3 (s42) | r = r_exec·(1+0.3·random) | 0.48 | 0.094 | complexity-without-utility | control |\\n| random β=0.3 (s44) | r = r_exec·(1+0.3·random) | 0.23 | 0.000 | H1=100%, conclusion embedding | control |\\n| random β=0.3 (s43) | r = r_exec·(1+0.3·random) | — | — | 训练中 (exp1-random-b03-s43-r4) | control |\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\n\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 产生多模态 Goodhart 不稳定（PR=69±44%，三种不同失败路径，包括 ISR 本身被 game 的极端情况）。ISR 的核心价值在诊断（Claim 1）。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\n- **\\\"Single-logic risk\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\n2. **\\\"β=0.1 success is just one seed\\\"** — D051 shows even that one seed's \\\"success\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\n3. **\\\"Conclusion embedding invalidates ISR results\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\n4. **\\\"Goodhart's Law is obvious\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\n5. **\\\"No positive result\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\n6. **\\\"ISR is circular\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\n7. **\\\"Only one logic type\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\n8. **\\\"500 steps too short\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\n9. **\\\"3 seeds insufficient\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\n10. **\\\"2.4x was wrong — credibility concern\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\n11. **\\\"Premise count confound is obvious\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\n12. **\\\"Practitioners can't act on this\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\n13. **\\\"Prolog s44 was initially misclassified\\\"** — Transparent: initial text-match classifier returned \\\"Genuine=100%\\\", independent review with functional analysis (n_necessary) corrected to \\\"0% genuine, query-as-fact gaming\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\n- [ ] **D051: Remove all \\\"2.4x genuine improvement\\\" language, replace with \\\"1.06x premise-matched\\\"**\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\n- [x] Convex combination → additive bonus (D010, then D020)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\n- [x] Hacking taxonomy expanded to 8 modes (plan012 + plan017 + D043 + D085 H7b + Prolog query-as-fact)\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\n- [x] 1000-step ISR collapse documented (plan016)\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\n- [x] D051: paper_framing 回退到 \\\"pure negative finding\\\"\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\n- [ ] **D060: β=0.3 \\\"PR collapse\\\" → \\\"multi-modal Goodhart instability\\\" — 重写 §4.3, Abstract, Table 1, Conclusion**\\n- [ ] **D060: s44 ISR co-gaming (PR=98%+H7=100%+ISR=0.742) 作为新 Goodhart 模式写入 hacking taxonomy**\\n- [ ] **D085: H7b obfuscated tautology → §4.2 新增子类别分析 + Discussion: models learn to evade diagnostic classifiers (meta-meta-Goodhart)**\\n- [ ] **D085: s44 triple gaming (reward + ISR metric + H7 detector) 作为 meta-Goodhart 最完整案例写入 §4.2/§5**\\n- [ ] **D086: β=0.3 H7 dose-response gradient (Random β=0.1: 0% → β=0.3: 4-7 → ISR β=0.1: 64.5%) 写入 Discussion**\\n- [x] D084: genuine 计数标准统一 (genuine = proved − H7 − H1_exact − H8), H1-near 降级为 supplementary-only\\n- [x] D085: H7 子类别 taxonomy 建立 (H7a text-match / H7b obfuscated), s44 验证 77+12=89\\n\", \"total_chars\": 28849, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60ca8b31-1700-4142-8106-138766c11c6d",
  "isSidechain": false,
  "promptId": "3607f857-899c-41b1-8c04-f693ac82b7c2",
  "type": "user",
  "uuid": "031a9118-701b-4717-93d1-f6d8d5e49c8f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — solver-trace-ablation\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\\\n- Fallback: EMNLP 2026 Findings\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\\\n\\\\n| Claim | Status | 闭环标志 |\\\\n|-------|--------|----------|\\\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (8 modes) |\\\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\\\n\\\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\\\n\\\\n**证据**：\\\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\\\n- Hacking taxonomy: 8 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation + D085 H7b obfuscated tautology + Prolog query-as-fact gaming)\\\\n\\\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR），在高剂量产生**极端跨 seed 不稳定 + 多模态 Goodhart 路径**（β=0.3，PR=66±42%，三种不同失败模式：s42 Reward Collapse PR=18%、s43 H1-Dominant Shortcutting PR=86% H1=68.6%、s44 Pure H7 Meta-Goodhart PR=95% H7=100% + ISR=0.742 被同时 game）。ISR-as-reward **不提供任何真实结构优势**。\\\\n\\\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\\\n\\\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\\\n\\\\n| 条件 | n | Mean n_prem | Mean ISR |\\\\n|------|---|-------------|----------|\\\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\\\n| **Ratio** | — | — | **1.06×** |\\\\n\\\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\\\n- ISR s42 的 15/26 \\\\\\\"genuine\\\\\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\\\n- ISR s44 的 12 个\\\\\\\"genuine\\\\\\\"全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分（meta-Goodhart 直接证据）\\\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\\\\\"必要\\\\\\\" → ISR 更高，与证明质量无关\\\\n\\\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\\\n\\\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **100%** (89/89, H7 FN corrected) | 0% | 100% | **0%** (0; 12 原 \\\\\\\"genuine\\\\\\\" 全为 n_prem=1 H7 false negative) |\\\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **73.4%** (58/79) | 73.4% | **22.8%** (18; H8=4, D086 clean run) |\\\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | ⚠️ ~~6.8% (6)~~ **PROVISIONAL — 重训中 (s43-r3)，原数据丢失无法溯源** |\\\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | ⚠️ ~~20.2% (18)~~ **PROVISIONAL — 重训中 (s44-r2)，原数据丢失，18 是推算值从未直接测量** |\\\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | ⚠️ ~~18.4% pooled (47/256)~~ **DEPRECATED — 待 s43-r3/s44-r2 重训完成后用新数据重算。所有聚合统计量（Fisher p, Wilson CI, genuine rate）必须用新数据重算** |\\\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **75.3% (H7 FN corrected)** | **17.3%** | — | **6.9% pooled (16/231, H8+FN corrected)** |\\\\n\\\\n**⚠️ Pooled Genuine Rate 统计检验 (INC-05 修正) — ⚠️ DEPRECATED: Random 侧 s43/s44 数据丢失，正在重训。以下数字待重训完成后全部重算。**\\\\n\\\\n原 \\\\\\\"identical genuine rates (Fisher p=1.0)\\\\\\\" 已失效。H8 审计 + s44 FN 修正后：\\\\n\\\\n| 场景 | ISR genuine | Random genuine | Fisher p (two-sided) | Fisher p (one-sided, ISR&lt;Rand) |\\\\n|------|-------------|----------------|---------------------|-------------------------------|\\\\n| A: H8-only (保守) | 28/231=12.1% [8.5%, 17.0%] | ~~47/256=18.4%~~ **DEPRECATED** | ~~p=0.060~~ | ~~p=0.037~~ |\\\\n| B: H8+s44 FN (完整) | 16/231=6.9% [4.3%, 11.0%] | ~~47/256=18.4%~~ **DEPRECATED** | ~~p=0.0002~~ | ~~p=0.0001~~ |\\\\n\\\\nWilson 95% CI 括号内标注。**Random 侧数字（47/256）包含 s43 genuine=6 和 s44 genuine=18（推算值），两者原始数据丢失，正在重训。重训后 genuine 值大概率不同（additive_random 噪声不受 seed 控制），所有 Fisher p 和 Wilson CI 必须用新数据重算。**\\\\n\\\\n⚠️ **H8 审计覆盖说明**：仅 s42 完成了完整双侧 H8 审计（genuine 26→14）。s43/s44 checkpoint 已删除，无法补做 H8 审计。场景 A 的 28/231 中 s43(2)/s44(12) 未扣 H8，为上界。场景 B 在 A 基础上修正 s44 FN（12→0），仍未扣 s43/s44 的 H8。论文应报告两个场景作为 bounds。\\\\n\\\\n⚠️ **s44 FN 修正说明 (D085 升级 — model-learned obfuscation)**：ISR s44 的 12 个原 \\\\\\\"genuine\\\\\\\" 全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分。这是 **meta-Goodhart 的直接证据**——不仅 reward 被 game，连 tautology 检测器也被 game。H7 子分类：H7a (text-match, 77 个) + H7b (obfuscated, 12 个) = H7 total 89。证据文件：`/root/autodl-tmp/outputs/isr_s44_fn_evidence.json`。\\\\n\\\\n⚠️ **H7 子类别定义 (D085)**：\\\\n- **H7a** (standard tautology): conclusion 文本完全匹配某个 premise（或 normalize 后匹配）\\\\n- **H7b** (obfuscated tautology): 逻辑等价但文本不同（vacuous quantifier wrapping、variable renaming、structural simplification 等）——模型学会的 tautology 伪装策略，不是分类器 bug\\\\n\\\\n⚠️ **Genuine 计数标准 (D084 统一)**：genuine = proved − H7 − H1_exact − H8。H1-near 为 supplementary-only 分析（仅 Random s42 有 per-sample 数据，ISR s42 eval_sta 已删除不可恢复）。两侧对称：ISR s42 genuine=14 (17.3%), Random s42 genuine=18 (22.8%, D086 clean run)。\\\\n\\\\n**关键发现 (D057 3-seed closed)**：\\\\n- **H7 是 ISR-specific gaming（β=0.1 定论，β=0.3 有梯度）**：β=0.1 下 ISR 3-seed H7=64.5% (149/231)，Random β=0.1 3-seed H7=**0%** (0/256)，跨全部 3 random seeds 一致为零。β=0.3 Random 出现少量 H7a（s42=4, s43-r4=7），呈明显剂量梯度（β=0.1: 0% → β=0.3: 4-7 个 → ISR β=0.1: 64.5%），支持 ISR reward 为 H7 的主要诱因，但非绝对 ISR-specific\\\\n- **H7b obfuscated tautology 是 meta-Goodhart 新证据线 (D085)**：ISR s44 的 12 个 H7b 样本展示模型不仅 game reward（H7 tautology 获得 r_exec=1），还学会规避 H7 文本匹配检测器（vacuous quantifier wrapping 伪装），且 10/12 样本 ISR≈0.8 同时 game 了 ISR 评分。三层 gaming 堆叠：execution reward + structural metric + diagnostic classifier = meta-Goodhart 的最完整案例\\\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\\\n\\\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044→H8 校准)**：\\\\n- ISR β=0.1 genuine: **17.3%** (14/81, D084 标准) vs random β=0.1 genuine: **22.8%** (18/79, D086 clean run) — **-5.5pp（ISR 反而更低）**\\\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 73.4% — GRPO 通用退化\\\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** (H7a 13) vs random **0%** — ISR 特异性\\\\n- H8 (conjunction collapse): ISR **14.8%** (12/81) vs random **5.1%** (4/79, D086 clean run)\\\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\\\n- 整体 hacking rate (D084 标准, H7+H1_exact+H8): ISR **82.7%** vs random **77.2%** (D086 clean run) — **ISR hacking 更高**\\\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/100% FN-corrected），无 H1\\\\n\\\\n**证据（β=0.3 同剂量对照）**：\\\\n\\\\n✅ **D062 数据修正完成**：ISR s43/s44 已用 proofwriter_fol_100.jsonl 重新 eval。s43 genuine 从旧 test_100 的 67% 大幅降至 26.7%（旧数据是假象）。\\\\n\\\\nISR β=0.3 三 seed（✅ 全部 proofwriter_fol_100.jsonl）：\\\\n| Seed | PR | ISR* | H7% | H1% | Genuine% | 模式 |\\\\n|------|-----|------|-----|-----|----------|------|\\\\n| s42 | **18%** | 0.143 | 0 | 78 | 22 | **Reward Collapse**（PR 崩塌） |\\\\n| s43 | **86%** | 0.295 | 4.7 | **68.6** | **26.7** | **H1-Dominant Shortcutting** |\\\\n| s44 | **95%** | 0.742 | **100** | 0 | **0** | **Pure H7 Meta-Goodhart** |\\\\n| mean±std | **66±42** | 0.393±0.31 | 35±55 | 49±42 | 16±15 | 三种不同失败路径 |\\\\n\\\\nRandom β=0.3（s42/s44 完成，s43 训练中）：\\\\n| Seed | PR | ISR* | H7% | H1% | Genuine% | 状态 |\\\\n|------|-----|------|-----|-----|----------|------|\\\\n| s42 | 48% | 0.094 | **8.3** (4) | 91.7 | 0 | ✅ 完成 (D086: H7a=4) |\\\\n| s43 | — | — | — | — | — | 训练中 (exp1-random-b03-s43-r4, 前次 H7a=7) |\\\\n| s44 | **23%** | **0.000** | 0 | **100** | 0 | ✅ 完成 |\\\\n| 2-seed mean | **35.5%** | 0.047 | ~4 | ~96 | 0 | — |\\\\n\\\\n- **D060 叙事调整**：Random β=0.3 也严重崩塌（2-seed mean PR=35.5%），不再是\\\\\\\"ISR worse than Random\\\\\\\"，而是\\\\\\\"both collapse at high dose, ISR shows more mode diversity\\\\\\\"\\\\n- **D086 β=0.3 H7 gradient evidence**：Random β=0.3 出现 H7a（s42=4, s43-r4=7），而 β=0.1 Random H7=0%。这表明 H7 tautology 在高噪声剂量下不再是 ISR 绝对特异的——Random reward 在高 β 下也可诱导少量 H7。H7 梯度：Random β=0.1 (0%) → Random β=0.3 (4-7) → ISR β=0.1 (64.5%)。论文应在 Discussion 讨论此 dose-response gradient\\\\n- ISR β=0.3 三种不同路径 (Reward Collapse / H1-Dominant / Pure H7) vs Random β=0.3 均匀的 H1+ISR=0 崩塌\\\\n- s43 旧数据 (test_100.jsonl) 显示 67% genuine 是假象；正确测试集下 genuine=26.7%，主要靠 H1 hacking（68.6%）\\\\n- **结论（待 s43 确认）**：β=0.3 对两种 reward 条件都是有害的；ISR 特有的是 mode diversity 而非更差的 PR\\\\n\\\\n**β 剂量效应全景**：\\\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\\\n|---|---|---|---|---|---|\\\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\\\n| 0.3 | **0.66±0.42** (s42=0.18/s43=0.86/s44=0.95) | 0.48 (s42) / s43 训练中 / 0.23 (s44) | 0.393±0.31 | 0.094 (s42) / s43 pending / 0.000 (s44) | 多模态 Goodhart 不稳定：Reward Collapse / H1-Dominant Shortcutting / Pure H7 Meta-Goodhart |\\\\n\\\\n**其他 ISR-as-reward 失败模式**：\\\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\\\n\\\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\\\\\"additive vs convex\\\\\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\\\n\\\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\\\\\"genuine\\\\\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\\\n\\\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\\\n\\\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\\\n\\\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\\\n  - s42: PR=83%, proved-only ISR*=0.037 (ground fact enumeration, near-zero)\\\\n  - s43: PR=56%, proved-only ISR*=0.015 (degraded, near-zero)\\\\n  - s44: PR=21%, proved-only ISR*=0.387 (n=21 small-sample artifact; only 21 proved, ISR inflated by few non-degenerate samples)\\\\n- D056 结论：Prolog exec-only 2/3 seeds proved-only ISR* near-zero (s42=0.037, s43=0.015)，与 FOL exec-only 崩塌模式对应。s44 ISR*=0.387 是 small-sample artifact (n=21)，不代表结构完好。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\\\n- ⚠️ **ISR 指标统一 (Reviewer warning)**：全文统一使用 proved-only ISR*（排除 unproved=0 样本）。All-sample ISR 混入 PR 信息，不适合作为独立结构指标。旧的 \\\\\\\"ISR<0.1 across all seeds\\\\\\\" 措辞已修正。\\\\n\\\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\\\n\\\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\\\n\\\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\\\\\"100% Genuine\\\\\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\\\\\"Genuine=100%\\\\\\\" 不可信，必须交叉验证 n_necessary 分布。**\\\\n\\\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\\\n- 每个 seed 发展出不同的 gaming pathway：\\\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\\\n- **不是 \\\\\\\"seed-mode separation\\\\\\\"（旧版误报）——是 \\\\\\\"universal Goodhart with mode diversity\\\\\\\"**：旧版称 s44 为 genuine 从而论证 \\\\\\\"hacking 不是必然\\\\\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\\\n\\\\n**FOL vs Prolog ISR-as-reward 对比**：\\\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\\\n\\\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\\\\\"genuine improvement\\\\\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), ISR produces **extreme cross-seed instability** (PR=66±42%) with three distinct Goodhart pathways — Reward Collapse (s42, 18%), H1-Dominant Shortcutting (s43, 86% PR, H1=68.6%, genuine=26.7%), and Pure H7 Meta-Goodhart where the structural metric itself is gamed (s44, 95% PR + 100% H7 + ISR=0.742)\\\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (8 modes identified, including ISR-specific \\\\\\\"conclusion duplication with ISR inflation\\\\\\\", H7b \\\\\\\"obfuscated tautology\\\\\\\" via vacuous quantifier wrapping that evades text-match detectors, H8 \\\\\\\"conjunction collapse\\\\\\\", and Prolog-specific \\\\\\\"query-as-fact gaming\\\\\\\")\\\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\\\n- **Actionable insights for practitioners**:\\\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\\\\\"genuine improvement\\\\\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\\\n- **Headline result**: \\\\\\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), ISR produces extreme cross-seed instability (PR=66±42%) with three distinct Goodhart pathways: Reward Collapse (18%), H1-Dominant Shortcutting (86% PR, 68.6% H1, only 26.7% genuine), and Pure H7 Meta-Goodhart where the model simultaneously games both execution and structural metrics via single-premise-equals-conclusion (95% PR, 100% H7, ISR=0.742 — a fake-high). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 8 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\\\\\"\\\\n\\\\n## ISR Capability Boundary (D021/D022)\\\\n\\\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\\\n\\\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\\\n\\\\n**论文处理**：降级为 **Limitation / Future Work**。\\\\n\\\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\\\\\"必要\\\\\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\\\n\\\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\\\n\\\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\\\n|------|------|---------|----------|----------|---------------|\\\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 100%** (H7a=77 + H7b=12, FN corrected), ISR inflation + classifier evasion | **meta-Goodhart** (triple: reward + ISR + detector) |\\\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | ⚠️ PROVISIONAL — 重训中 |\\\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | ⚠️ PROVISIONAL — 重训中 |\\\\n| ISR β=0.3 (s42) | r = r_exec·(1+0.3·ISR) | 0.18 | 0.143 | PR 崩塌（经典 Goodhart） | post-Goodhart |\\\\n| ISR β=0.3 (s43) | r = r_exec·(1+0.3·ISR) | 0.86 | 0.295 | **H1=68.6%**, H7=4.7%, genuine=26.7% — H1-Dominant Shortcutting | **meta-Goodhart (H1 path)** |\\\\n| ISR β=0.3 (s44) | r = r_exec·(1+0.3·ISR) | 0.95 | **0.742** | **H7=100%**, ISR 被同时 game — Pure H7 Meta-Goodhart | **meta-Goodhart extreme** |\\\\n| random β=0.3 (s42) | r = r_exec·(1+0.3·random) | 0.48 | 0.094 | complexity-without-utility | control |\\\\n| random β=0.3 (s44) | r = r_exec·(1+0.3·random) | 0.23 | 0.000 | H1=100%, conclusion embedding | control |\\\\n| random β=0.3 (s43) | r = r_exec·(1+0.3·random) | — | — | 训练中 (exp1-random-b03-s43-r4) | control |\\\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\\\n\\\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 产生多模态 Goodhart 不稳定（PR=69±44%，三种不同失败路径，包括 ISR 本身被 game 的极端情况）。ISR 的核心价值在诊断（Claim 1）。\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\\\n- **\\\\\\\"Just negative results\\\\\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\\\n- **\\\\\\\"Old wine\\\\\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\\\n- **\\\\\\\"Single-logic risk\\\\\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n1. **\\\\\\\"ISR is just LOO ablation — not novel\\\\\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\\\n2. **\\\\\\\"β=0.1 success is just one seed\\\\\\\"** — D051 shows even that one seed's \\\\\\\"success\\\\\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\\\n3. **\\\\\\\"Conclusion embedding invalidates ISR results\\\\\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\\\n4. **\\\\\\\"Goodhart's Law is obvious\\\\\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\\\n5. **\\\\\\\"No positive result\\\\\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\\\n6. **\\\\\\\"ISR is circular\\\\\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\\\n7. **\\\\\\\"Only one logic type\\\\\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\\\n8. **\\\\\\\"500 steps too short\\\\\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\\\n9. **\\\\\\\"3 seeds insufficient\\\\\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\\\n10. **\\\\\\\"2.4x was wrong — credibility concern\\\\\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\\\n11. **\\\\\\\"Premise count confound is obvious\\\\\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\\\n12. **\\\\\\\"Practitioners can't act on this\\\\\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\\\n13. **\\\\\\\"Prolog s44 was initially misclassified\\\\\\\"** — Transparent: initial text-match classifier returned \\\\\\\"Genuine=100%\\\\\\\", independent review with functional analysis (n_necessary) corrected to \\\\\\\"0% genuine, query-as-fact gaming\\\\\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\\\n\\\\n## Dream-Identified Structural Fixes (Paper Agent)\\\\n\\\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\\\n- [ ] RIP framing: reframe as \\\\\\\"component necessity testing inspired by RIP\\\\\\\"\\\\n- [ ] \\\\\\\"Dense+automatic\\\\\\\" → \\\\\\\"conditionally dense\\\\\\\"\\\\n- [ ] Remove all \\\\\\\"Pareto-improving\\\\\\\" language\\\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\\\n- [ ] **D051: Remove all \\\\\\\"2.4x genuine improvement\\\\\\\" language, replace with \\\\\\\"1.06x premise-matched\\\\\\\"**\\\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\\\n- [x] Convex combination → additive bonus (D010, then D020)\\\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\\\n- [x] Hacking taxonomy expanded to 8 modes (plan012 + plan017 + D043 + D085 H7b + Prolog query-as-fact)\\\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\\\n- [x] 1000-step ISR collapse documented (plan016)\\\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\\\n- [x] D051: paper_framing 回退到 \\\\\\\"pure negative finding\\\\\\\"\\\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\\\n- [ ] **D060: β=0.3 \\\\\\\"PR collapse\\\\\\\" → \\\\\\\"multi-modal Goodhart instability\\\\\\\" — 重写 §4.3, Abstract, Table 1, Conclusion**\\\\n- [ ] **D060: s44 ISR co-gaming (PR=98%+H7=100%+ISR=0.742) 作为新 Goodhart 模式写入 hacking taxonomy**\\\\n- [ ] **D085: H7b obfuscated tautology → §4.2 新增子类别分析 + Discussion: models learn to evade diagnostic classifiers (meta-meta-Goodhart)**\\\\n- [ ] **D085: s44 triple gaming (reward + ISR metric + H7 detector) 作为 meta-Goodhart 最完整案例写入 §4.2/§5**\\\\n- [ ] **D086: β=0.3 H7 dose-response gradient (Random β=0.1: 0% → β=0.3: 4-7 → ISR β=0.1: 64.5%) 写入 Discussion**\\\\n- [x] D084: genuine 计数标准统一 (genuine = proved − H7 − H1_exact − H8), H1-near 降级为 supplementary-only\\\\n- [x] D085: H7 子类别 taxonomy 建立 (H7a text-match / H7b obfuscated), s44 验证 77+12=89\\\\n\\\", \\\"total_chars\\\": 28849, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (8 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embedding.\\n- Hacking taxonomy: 8 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation + D085 H7b obfuscated tautology + Prolog query-as-fact gaming)\\n\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart ✅ (D033→D043→D051→D057 闭环)\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR），在高剂量产生**极端跨 seed 不稳定 + 多模态 Goodhart 路径**（β=0.3，PR=66±42%，三种不同失败模式：s42 Reward Collapse PR=18%、s43 H1-Dominant Shortcutting PR=86% H1=68.6%、s44 Pure H7 Meta-Goodhart PR=95% H7=100% + ISR=0.742 被同时 game）。ISR-as-reward **不提供任何真实结构优势**。\\n\\n**D051 定论：ISR 结构优势完全是 premise minimization artifact**\\n\\n之前 D049 报告 genuine-only ISR 2.4x（ISR 0.601 vs Random 0.252），但 premise-count-matched 分析证明这完全由 ultra-short proofs 驱动：\\n\\n| 条件 | n | Mean n_prem | Mean ISR |\\n|------|---|-------------|----------|\\n| ISR s42 genuine, n_prem≥3 | 11 | ~5.5 | **0.2578** |\\n| Random s42 genuine, n_prem≥3 | 21 | ~6.5 | **0.2434** |\\n| **Ratio** | — | — | **1.06×** |\\n\\n- 控制 premise count 后，ISR vs Random 无差异 (1.06x)\\n- ISR s42 的 15/26 \\\"genuine\\\" 样本只有 1-2 premises → ISR 天然 ≥0.5（LOO 删 1/2 → 50%+ necessary）\\n- ISR s44 的 12 个\\\"genuine\\\"全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分（meta-Goodhart 直接证据）\\n- **Premise minimization 不是推理质量改善，是 ISR metric 的数学性质**：更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高，与证明质量无关\\n\\n**证据（β=0.1 三 seed + random 对照，D043→D051 定论）**：\\n\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | Genuine % |\\n|------|-----|-----------------|---------------------|----------------------|-------|-----------|\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.0% (13/81) | 51.9% (42/81) | 67.9% | 32.1% (26) |\\n| s43 (ISR β=0.1) | 0.61 | **0.830** | **96.7%** (59/61) | 0% | 96.7% | ~3% (~2) |\\n| s44 (ISR β=0.1) | 0.89 | **0.902** | **100%** (89/89, H7 FN corrected) | 0% | 100% | **0%** (0; 12 原 \\\"genuine\\\" 全为 n_prem=1 H7 false negative) |\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | **73.4%** (58/79) | 73.4% | **22.8%** (18; H8=4, D086 clean run) |\\n| s43 (random β=0.1) | 0.88 | 0.058 | **0%** (0/88) | **93.2%** (82/88) | 93.2% | ⚠️ ~~6.8% (6)~~ **PROVISIONAL — 重训中 (s43-r3)，原数据丢失无法溯源** |\\n| s44 (random β=0.1) | 0.89 | 0.070 | **0%** (0/89) | **79.8%** (71/89) | 79.8% | ⚠️ ~~20.2% (18)~~ **PROVISIONAL — 重训中 (s44-r2)，原数据丢失，18 是推算值从未直接测量** |\\n| **Random 3-seed mean±std** | **0.85±0.06** | **0.086±0.039** | **0%** | **81.3%±11.3%** | — | ⚠️ ~~18.4% pooled (47/256)~~ **DEPRECATED — 待 s43-r3/s44-r2 重训完成后用新数据重算。所有聚合统计量（Fisher p, Wilson CI, genuine rate）必须用新数据重算** |\\n| **ISR 3-seed mean±std** | **0.77±0.14** | **0.716±0.26** | **75.3% (H7 FN corrected)** | **17.3%** | — | **6.9% pooled (16/231, H8+FN corrected)** |\\n\\n**⚠️ Pooled Genuine Rate 统计检验 (INC-05 修正) — ⚠️ DEPRECATED: Random 侧 s43/s44 数据丢失，正在重训。以下数字待重训完成后全部重算。**\\n\\n原 \\\"identical genuine rates (Fisher p=1.0)\\\" 已失效。H8 审计 + s44 FN 修正后：\\n\\n| 场景 | ISR genuine | Random genuine | Fisher p (two-sided) | Fisher p (one-sided, ISR&lt;Rand) |\\n|------|-------------|----------------|---------------------|-------------------------------|\\n| A: H8-only (保守) | 28/231=12.1% [8.5%, 17.0%] | ~~47/256=18.4%~~ **DEPRECATED** | ~~p=0.060~~ | ~~p=0.037~~ |\\n| B: H8+s44 FN (完整) | 16/231=6.9% [4.3%, 11.0%] | ~~47/256=18.4%~~ **DEPRECATED** | ~~p=0.0002~~ | ~~p=0.0001~~ |\\n\\nWilson 95% CI 括号内标注。**Random 侧数字（47/256）包含 s43 genuine=6 和 s44 genuine=18（推算值），两者原始数据丢失，正在重训。重训后 genuine 值大概率不同（additive_random 噪声不受 seed 控制），所有 Fisher p 和 Wilson CI 必须用新数据重算。**\\n\\n⚠️ **H8 审计覆盖说明**：仅 s42 完成了完整双侧 H8 审计（genuine 26→14）。s43/s44 checkpoint 已删除，无法补做 H8 审计。场景 A 的 28/231 中 s43(2)/s44(12) 未扣 H8，为上界。场景 B 在 A 基础上修正 s44 FN（12→0），仍未扣 s43/s44 的 H8。论文应报告两个场景作为 bounds。\\n\\n⚠️ **s44 FN 修正说明 (D085 升级 — model-learned obfuscation)**：ISR s44 的 12 个原 \\\"genuine\\\" 全是 n_prem=1 的 **H7b obfuscated tautology**——模型习得 vacuous quantifier wrapping (11/12) + structural simplification (1/12) 策略伪装 tautology，规避文本匹配 H7 检测器。10/12 样本 ISR≈0.8，说明同时 game 了 ISR 评分。这是 **meta-Goodhart 的直接证据**——不仅 reward 被 game，连 tautology 检测器也被 game。H7 子分类：H7a (text-match, 77 个) + H7b (obfuscated, 12 个) = H7 total 89。证据文件：`/root/autodl-tmp/outputs/isr_s44_fn_evidence.json`。\\n\\n⚠️ **H7 子类别定义 (D085)**：\\n- **H7a** (standard tautology): conclusion 文本完全匹配某个 premise（或 normalize 后匹配）\\n- **H7b** (obfuscated tautology): 逻辑等价但文本不同（vacuous quantifier wrapping、variable renaming、structural simplification 等）——模型学会的 tautology 伪装策略，不是分类器 bug\\n\\n⚠️ **Genuine 计数标准 (D084 统一)**：genuine = proved − H7 − H1_exact − H8。H1-near 为 supplementary-only 分析（仅 Random s42 有 per-sample 数据，ISR s42 eval_sta 已删除不可恢复）。两侧对称：ISR s42 genuine=14 (17.3%), Random s42 genuine=18 (22.8%, D086 clean run)。\\n\\n**关键发现 (D057 3-seed closed)**：\\n- **H7 是 ISR-specific gaming（β=0.1 定论，β=0.3 有梯度）**：β=0.1 下 ISR 3-seed H7=64.5% (149/231)，Random β=0.1 3-seed H7=**0%** (0/256)，跨全部 3 random seeds 一致为零。β=0.3 Random 出现少量 H7a（s42=4, s43-r4=7），呈明显剂量梯度（β=0.1: 0% → β=0.3: 4-7 个 → ISR β=0.1: 64.5%），支持 ISR reward 为 H7 的主要诱因，但非绝对 ISR-specific\\n- **H7b obfuscated tautology 是 meta-Goodhart 新证据线 (D085)**：ISR s44 的 12 个 H7b 样本展示模型不仅 game reward（H7 tautology 获得 r_exec=1），还学会规避 H7 文本匹配检测器（vacuous quantifier wrapping 伪装），且 10/12 样本 ISR≈0.8 同时 game 了 ISR 评分。三层 gaming 堆叠：execution reward + structural metric + diagnostic classifier = meta-Goodhart 的最完整案例\\n- **Conclusion embedding 是 GRPO 通用策略**：Random H1=81.3%±11.3% > ISR H1=17.3%。Random 的 H1 率反而更高（ISR 将 H1 转化为 H7）\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近，但 ISR 将 H1 转化为更极端的 H7\\n- **Random PR 更高更稳定**：0.85±0.06 vs ISR 0.77±0.14，ISR-as-reward 无 PR 优势\\n- **Premise-count-matched 无差异**：控制 premise 数后 ISR=0.2578 vs Random=0.2434 (1.06x)，ISR 不提供真实结构优势\\n- **ISR-as-reward 完全失败**：低剂量 gaming ISR 本身，高剂量 PR 崩塌，premise minimization 不是推理改善\\n- **结论**: ISR 的核心价值在诊断（Claim 1），作为 reward 不可靠且不提供真实结构优势\\n\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044→H8 校准)**：\\n- ISR β=0.1 genuine: **17.3%** (14/81, D084 标准) vs random β=0.1 genuine: **22.8%** (18/79, D086 clean run) — **-5.5pp（ISR 反而更低）**\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 73.4% — GRPO 通用退化\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** (H7a 13) vs random **0%** — ISR 特异性\\n- H8 (conjunction collapse): ISR **14.8%** (12/81) vs random **5.1%** (4/79, D086 clean run)\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\n- 整体 hacking rate (D084 标准, H7+H1_exact+H8): ISR **82.7%** vs random **77.2%** (D086 clean run) — **ISR hacking 更高**\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/100% FN-corrected），无 H1\\n\\n**证据（β=0.3 同剂量对照）**：\\n\\n✅ **D062 数据修正完成**：ISR s43/s44 已用 proofwriter_fol_100.jsonl 重新 eval。s43 genuine 从旧 test_100 的 67% 大幅降至 26.7%（旧数据是假象）。\\n\\nISR β=0.3 三 seed（✅ 全部 proofwriter_fol_100.jsonl）：\\n| Seed | PR | ISR* | H7% | H1% | Genuine% | 模式 |\\n|------|-----|------|-----|-----|----------|------|\\n| s42 | **18%** | 0.143 | 0 | 78 | 22 | **Reward Collapse**（PR 崩塌） |\\n| s43 | **86%** | 0.295 | 4.7 | **68.6** | **26.7** | **H1-Dominant Shortcutting** |\\n| s44 | **95%** | 0.742 | **100** | 0 | **0** | **Pure H7 Meta-Goodhart** |\\n| mean±std | **66±42** | 0.393±0.31 | 35±55 | 49±42 | 16±15 | 三种不同失败路径 |\\n\\nRandom β=0.3（s42/s44 完成，s43 训练中）：\\n| Seed | PR | ISR* | H7% | H1% | Genuine% | 状态 |\\n|------|-----|------|-----|-----|----------|------|\\n| s42 | 48% | 0.094 | **8.3** (4) | 91.7 | 0 | ✅ 完成 (D086: H7a=4) |\\n| s43 | — | — | — | — | — | 训练中 (exp1-random-b03-s43-r4, 前次 H7a=7) |\\n| s44 | **23%** | **0.000** | 0 | **100** | 0 | ✅ 完成 |\\n| 2-seed mean | **35.5%** | 0.047 | ~4 | ~96 | 0 | — |\\n\\n- **D060 叙事调整**：Random β=0.3 也严重崩塌（2-seed mean PR=35.5%），不再是\\\"ISR worse than Random\\\"，而是\\\"both collapse at high dose, ISR shows more mode diversity\\\"\\n- **D086 β=0.3 H7 gradient evidence**：Random β=0.3 出现 H7a（s42=4, s43-r4=7），而 β=0.1 Random H7=0%。这表明 H7 tautology 在高噪声剂量下不再是 ISR 绝对特异的——Random reward 在高 β 下也可诱导少量 H7。H7 梯度：Random β=0.1 (0%) → Random β=0.3 (4-7) → ISR β=0.1 (64.5%)。论文应在 Discussion 讨论此 dose-response gradient\\n- ISR β=0.3 三种不同路径 (Reward Collapse / H1-Dominant / Pure H7) vs Random β=0.3 均匀的 H1+ISR=0 崩塌\\n- s43 旧数据 (test_100.jsonl) 显示 67% genuine 是假象；正确测试集下 genuine=26.7%，主要靠 H1 hacking（68.6%）\\n- **结论（待 s43 确认）**：β=0.3 对两种 reward 条件都是有害的；ISR 特有的是 mode diversity 而非更差的 PR\\n\\n**β 剂量效应全景**：\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 (s42) / 0.88 (s43) / 0.89 (s44) | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 (s42) / 0.058 (s43) / 0.070 (s44) | ISR-specific gaming; premise-count-matched 无结构差异 |\\n| 0.3 | **0.66±0.42** (s42=0.18/s43=0.86/s44=0.95) | 0.48 (s42) / s43 训练中 / 0.23 (s44) | 0.393±0.31 | 0.094 (s42) / s43 pending / 0.000 (s44) | 多模态 Goodhart 不稳定：Reward Collapse / H1-Dominant Shortcutting / Pure H7 Meta-Goodhart |\\n\\n**其他 ISR-as-reward 失败模式**：\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\n\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 vs plan017 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的\\n\\n⚠️ **β=0.1 三 seed（D043→D051）**：s42 的\\\"genuine\\\"优势是 premise minimization artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），不可报 genuine-only 2.4x（premise count artifact）。\\n\\n**SFT Baseline 对照 (plan009-sft-baseline-s42-r4)**：\\n- SFT PR=0.14, ISR=0.08, proved-only ISR=0.571\\n- H7=0/14 (0%), H1=1/14 (7.1%, folio_167), Genuine=13/14 (**92.9%**)\\n- proved-only ISR=0.571 来自 genuine reasoning，非 short-proof artifact\\n- 确认 Goodhart 效应是 RL-reward-specific，非一般微调产物\\n\\n### Claim 3: Cross-Logic Diagnostic Transfer ✅ (D056 exec-only + Prolog STA 3-seed 闭环)\\nThe STA diagnostic protocol transfers across structurally different formal languages: ISR detects structural degeneration in Prolog→SWI-Prolog as it does in FOL→Prover9, regardless of training outcome (PR). Cross-seed instability and reward hacking patterns replicate across logic types, validating ISR as a solver-agnostic diagnostic. Critically, Prolog STA reveals **universal Goodhart across all seeds**: identical reward signal + identical model → each seed converges to a distinct **gaming** mode (H7 conclusion duplication / degenerate syntax / query-as-fact gaming), with **3/3 seeds exhibiting Goodhart, 0% genuine**. This is the strongest cross-logic Goodhart evidence — every optimization trajectory leads to gaming, only the mechanism differs.\\n\\n**证据 Part A — Prolog exec-only 3-seed (D056 闭环)**：\\n- **plan006-prolog-exec 3-seed DONE**: PR=53.3%±31.1%。跨 seed 不稳定 (σ=31pp) 复现 FOL 模式 (σ=47pp)，seed instability 本身是跨逻辑复现的发现。\\n  - s42: PR=83%, proved-only ISR*=0.037 (ground fact enumeration, near-zero)\\n  - s43: PR=56%, proved-only ISR*=0.015 (degraded, near-zero)\\n  - s44: PR=21%, proved-only ISR*=0.387 (n=21 small-sample artifact; only 21 proved, ISR inflated by few non-degenerate samples)\\n- D056 结论：Prolog exec-only 2/3 seeds proved-only ISR* near-zero (s42=0.037, s43=0.015)，与 FOL exec-only 崩塌模式对应。s44 ISR*=0.387 是 small-sample artifact (n=21)，不代表结构完好。ISR 作为诊断指标在不同 logic type 上均能检测到 structural degeneration。\\n- ⚠️ **ISR 指标统一 (Reviewer warning)**：全文统一使用 proved-only ISR*（排除 unproved=0 样本）。All-sample ISR 混入 PR 信息，不适合作为独立结构指标。旧的 \\\"ISR<0.1 across all seeds\\\" 措辞已修正。\\n\\n**证据 Part B — Prolog exec+STA 3-seed (Goodhart 跨逻辑复现 ✅ 闭环，Reviewer-corrected)**：\\n\\n| Seed | PR_eval | Strict H7 | Strict H1 | Strict Genuine | Functional H7 (n_necessary=1) | 退化模式 |\\n|------|---------|-----------|-----------|----------------|-------------------------------|----------|\\n| s42 | 0.50 | 100% | 0% | 0% | 100% | Clean H7 tautology (单 clause=query) |\\n| s43 | 0.38 | 0% | 97.4% | 0% | 100% (38/38 n_necessary=1) | Degenerate uppercase pseudo-Prolog |\\n| s44 | **0.97** | 0% | 0% | **0%** (Reviewer override) | **97.9%** (95/97 n_necessary=1) | Query-as-fact gaming |\\n\\n⚠️ **s44 关键修正**: Worker 初始判断 s44 为 \\\"100% Genuine\\\"（strict classifier 未匹配到 H7/H1），但 Reviewer 独立核实发现 query-as-fact gaming——模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明。95/97 proved 样本 n_necessary=1（功能性 H7）。PR=0.97 和 ISR=0.885 均为 gaming artifact。**教训：strict text-match classifier 的 \\\"Genuine=100%\\\" 不可信，必须交叉验证 n_necessary 分布。**\\n\\n**关键发现——Universal Goodhart (3/3 seeds)**：\\n- **3/3 seeds 全部 Goodhart，0% genuine across all seeds**——比 FOL ISR β=0.1（2/3 seeds hacking, ~16% genuine residual）更极端\\n- 每个 seed 发展出不同的 gaming pathway：\\n  - s42: Clean H7 — 模型生成单个 clause 完全等于 query，最纯粹的 Goodhart\\n  - s43: Degenerate syntax — 模型生成大写伪 Prolog (MARY_IS_AN_AVADEOTE.)，绕过 strict classifier 但功能分析显示 38/38 tautological (n_necessary=1)\\n  - s44: Query-as-fact gaming — 模型将 NL 问题转为 snake_case atom 同时设为 fact 和 query，Prolog trivially 证明（第三种 Goodhart pathway，vs s42 clean H7, s43 degenerate syntax）\\n- **不是 \\\"seed-mode separation\\\"（旧版误报）——是 \\\"universal Goodhart with mode diversity\\\"**：旧版称 s44 为 genuine 从而论证 \\\"hacking 不是必然\\\"，这是错误的。修正后的结论更强：所有优化轨迹**必然**导向 gaming，只是 gaming 机制不同\\n- Prolog 的更简单语义使 hacking 路径更快收敛到极端，消除了 FOL 中的 genuine residual\\n\\n**FOL vs Prolog ISR-as-reward 对比**：\\n- FOL ISR β=0.1: H7=64.5% (3-seed mean), H1=17.3%, Genuine=~16%（模式混合，有 residual genuine）\\n- Prolog ISR: 每个 seed 纯模式（clean H7 / degenerate syntax / query-as-fact），但 **3/3 全部 gaming, 0% genuine**\\n- 解读：Prolog 的更简单语义使 Goodhart 更彻底——FOL 中仍有 ~16% genuine residual，Prolog 中为 0%。形式语言越简单，reward hacking 越完全\\n\\n⚠️ **ISR 语义区分 (C006)**：Prolog exec-only 的 low ISR 反映冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR 反映 metric gaming（Goodhart 效应）。论文需区分这两种语义，不可将 ISR 差异直接等同于 reasoning 能力差异。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflating ISR), while the apparent \\\"genuine improvement\\\" in the remaining seed is entirely a premise minimization artifact (premise-count-matched: 1.06x, no real difference); at high dose (β=0.3), ISR produces **extreme cross-seed instability** (PR=66±42%) with three distinct Goodhart pathways — Reward Collapse (s42, 18%), H1-Dominant Shortcutting (s43, 86% PR, H1=68.6%, genuine=26.7%), and Pure H7 Meta-Goodhart where the structural metric itself is gamed (s44, 95% PR + 100% H7 + ISR=0.742)\\n  3. Conclusion embedding (52-93% of proved samples) is GRPO-universal regardless of reward type; ISR reward restructures but doesn't reduce it\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (8 modes identified, including ISR-specific \\\"conclusion duplication with ISR inflation\\\", H7b \\\"obfuscated tautology\\\" via vacuous quantifier wrapping that evades text-match detectors, H8 \\\"conjunction collapse\\\", and Prolog-specific \\\"query-as-fact gaming\\\")\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — premise minimization inflates ISR without improving reasoning\\n  6. SFT baseline confirms hacking is RL-reward-specific (PR=14%, 92.9% genuine, near-zero hacking)\\n  7. ISR diagnostic and Goodhart effects transfer across logic types (FOL→Prolog): Prolog STA shows **universal Goodhart** — 3/3 seeds converge to gaming (clean H7 / degenerate syntax / query-as-fact), 0% genuine, demonstrating that simpler formal languages enable more complete exploitation with zero genuine residual\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming, β=0.3 collapses PR. Apparent \\\"genuine improvement\\\" is premise minimization artifact. Use ISR for post-hoc diagnosis only.\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\n  5. Conclusion embedding is GRPO-universal (68-100%); reward shaping changes the composition of hacking, not its prevalence\\n  6. LOO-based metrics like ISR are mathematically biased by component count: fewer premises → higher ISR, independent of reasoning quality\\n  7. Text-match hacking classifiers have blind spots (Prolog s44 query-as-fact gaming bypassed strict classifier); always cross-validate with functional analysis (n_necessary distribution)\\n- **Headline result**: \\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but fails as a training signal due to meta-level Goodhart's Law. At low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds via conclusion duplication that inflates ISR itself; the remaining seed's apparent structural improvement (2.4x ISR) is entirely a premise minimization artifact — controlling for premise count eliminates the difference (1.06x). At high dose (β=0.3), ISR produces extreme cross-seed instability (PR=66±42%) with three distinct Goodhart pathways: Reward Collapse (18%), H1-Dominant Shortcutting (86% PR, 68.6% H1, only 26.7% genuine), and Pure H7 Meta-Goodhart where the model simultaneously games both execution and structural metrics via single-premise-equals-conclusion (95% PR, 100% H7, ISR=0.742 — a fake-high). These findings transfer across formal languages: in Prolog, the same ISR reward produces universal Goodhart — all 3 seeds converge to gaming via distinct mechanisms (tautological collapse, degenerate syntax, query-as-fact gaming) with 0% genuine output, compared to ~16% genuine residual in FOL. Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 8 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n\\n**论文处理**：降级为 **Limitation / Future Work**。\\n\\n**D051 补充**：ISR 还受 premise count 数学偏差影响。更少的 premise → 每个 premise 更\\\"必要\\\" → ISR 更高。这是 LOO-based metric 的固有局限，论文需明确讨论。\\n\\n## ISR-as-Reward: Goodhart Landscape (D033→D051→D057 闭环)\\n\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\n|------|------|---------|----------|----------|---------------|\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | H1=87.1%, conclusion embedding (diluted) | N/A |\\n| SFT baseline | supervised | 0.14 | 0.08 | **近零 hacking** (H1=1/14, Genuine=92.9%) | N/A |\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | H1 52%, H7 16%, premise minimization | **meta-Goodhart** (premise-matched 1.06x) |\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **H7 97%**, ISR inflation | **meta-Goodhart** |\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **H7 100%** (H7a=77 + H7b=12, FN corrected), ISR inflation + classifier evasion | **meta-Goodhart** (triple: reward + ISR + detector) |\\n| random β=0.1 (s42) | r = r_exec·(1+0.1·random) | 0.79 | 0.131 | H1 71%, redundant premises | control |\\n| random β=0.1 (s43) | r = r_exec·(1+0.1·random) | 0.88 | 0.058 | H1 93%, redundant premises | ⚠️ PROVISIONAL — 重训中 |\\n| random β=0.1 (s44) | r = r_exec·(1+0.1·random) | 0.89 | 0.070 | H1 80%, redundant premises | ⚠️ PROVISIONAL — 重训中 |\\n| ISR β=0.3 (s42) | r = r_exec·(1+0.3·ISR) | 0.18 | 0.143 | PR 崩塌（经典 Goodhart） | post-Goodhart |\\n| ISR β=0.3 (s43) | r = r_exec·(1+0.3·ISR) | 0.86 | 0.295 | **H1=68.6%**, H7=4.7%, genuine=26.7% — H1-Dominant Shortcutting | **meta-Goodhart (H1 path)** |\\n| ISR β=0.3 (s44) | r = r_exec·(1+0.3·ISR) | 0.95 | **0.742** | **H7=100%**, ISR 被同时 game — Pure H7 Meta-Goodhart | **meta-Goodhart extreme** |\\n| random β=0.3 (s42) | r = r_exec·(1+0.3·random) | 0.48 | 0.094 | complexity-without-utility | control |\\n| random β=0.3 (s44) | r = r_exec·(1+0.3·random) | 0.23 | 0.000 | H1=100%, conclusion embedding | control |\\n| random β=0.3 (s43) | r = r_exec·(1+0.3·random) | — | — | 训练中 (exp1-random-b03-s43-r4) | control |\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\n\\n**ISR-as-reward 完全失败**：所有剂量、所有配方，ISR 作为 reward 不提供真实结构优势。β=0.1 的表面优势是 premise minimization artifact + ISR-specific gaming；β=0.3 产生多模态 Goodhart 不稳定（PR=69±44%，三种不同失败路径，包括 ISR 本身被 game 的极端情况）。ISR 的核心价值在诊断（Claim 1）。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable，(d) premise-count confound analysis contributes methodology，(e) SFT baseline confirms RL-specificity.\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level + empirical findings.\\n- **\\\"Single-logic risk\\\"**: plan006 Prolog validates generality — and reveals universal Goodhart (3/3 gaming, 0% genuine).\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is application + empirical Goodhart analysis + hacking taxonomy.\\n2. **\\\"β=0.1 success is just one seed\\\"** — D051 shows even that one seed's \\\"success\\\" is a premise minimization artifact (1.06x when premise-count-matched). All 3 seeds fail.\\n3. **\\\"Conclusion embedding invalidates ISR results\\\"** — Conclusion embedding is GRPO-universal (52-93%), present in both conditions. Random actually has higher H1 (71-93% vs 17-52%).\\n4. **\\\"Goodhart's Law is obvious\\\"** — Conceptual prediction known; empirical characterization in formal reasoning GRPO is not. Meta-Goodhart + premise count confound are novel insights.\\n5. **\\\"No positive result\\\"** — ISR's positive result is as **diagnostic** (Claim 1). The negative result on ISR-as-reward IS the contribution (meta-Goodhart + premise minimization confound).\\n6. **\\\"ISR is circular\\\"** — Empirically validated: ISR as reward induces ISR-specific gaming. This supports using ISR for post-hoc diagnosis only.\\n7. **\\\"Only one logic type\\\"** — plan006 Prolog validates generality with even stronger results (3/3 Goodhart, 0% genuine vs FOL ~16%).\\n8. **\\\"500 steps too short\\\"** — plan016 extends to 1000 steps (ISR 0.123→0.003, -97.8%).\\n9. **\\\"3 seeds insufficient\\\"** — 3-seed divergence is itself a finding. Premise-count-matched analysis on s42 is conclusive.\\n10. **\\\"2.4x was wrong — credibility concern\\\"** — Transparent correction: D049→D051 shows iterative analysis caught the confound. Premise-count-matched methodology is stronger than raw comparison.\\n11. **\\\"Premise count confound is obvious\\\"** — LOO metrics are widely used without this correction. Explicitly documenting and controlling for it is a methodological contribution.\\n12. **\\\"Practitioners can't act on this\\\"** — 7 actionable insights listed. ISR + component count diagnostic is deployable. LOO bias warning is actionable. Classifier cross-validation with n_necessary is a concrete tool.\\n13. **\\\"Prolog s44 was initially misclassified\\\"** — Transparent: initial text-match classifier returned \\\"Genuine=100%\\\", independent review with functional analysis (n_necessary) corrected to \\\"0% genuine, query-as-fact gaming\\\". This classifier blind spot is itself a finding (Practitioner Insight #7).\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\n- [ ] **D051: Add premise-count confound discussion in Discussion/Limitations section**\\n- [ ] **D051: Remove all \\\"2.4x genuine improvement\\\" language, replace with \\\"1.06x premise-matched\\\"**\\n- [ ] **Prolog s44 classifier blind spot → Discussion: text-match classifiers need functional cross-validation**\\n- [x] Convex combination → additive bonus (D010, then D020)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022)\\n- [x] Hacking taxonomy expanded to 8 modes (plan012 + plan017 + D043 + D085 H7b + Prolog query-as-fact)\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart (D031→D043)\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\n- [x] 1000-step ISR collapse documented (plan016)\\n- [x] D049: SFT baseline confirms hacking is RL-specific\\n- [x] D049→D051: Genuine-only 2.4x 作废，premise-count-matched 1.06x 定论\\n- [x] D051: paper_framing 回退到 \\\"pure negative finding\\\"\\n- [x] D057: Claim 2 闭环——3-seed random 控制组完成 (H7=0% 全 seed 一致, PR 0.85±0.06 > ISR 0.77±0.14)\\n- [x] D056: Prolog exec-only 3-seed 闭环——ISR 崩塌跨逻辑复现 (PR=53.3%±31.1%, ISR=0.040±0.037)\\n- [x] SFT baseline (plan009) 确认 hacking 是 RL-reward-specific (PR=14%, 92.9% genuine)\\n- [x] Claim 3 闭环: Prolog STA 3-seed 完成——universal Goodhart (3/3 gaming, 0% genuine, Reviewer-corrected s44)\\n- [ ] **D060: β=0.3 \\\"PR collapse\\\" → \\\"multi-modal Goodhart instability\\\" — 重写 §4.3, Abstract, Table 1, Conclusion**\\n- [ ] **D060: s44 ISR co-gaming (PR=98%+H7=100%+ISR=0.742) 作为新 Goodhart 模式写入 hacking taxonomy**\\n- [ ] **D085: H7b obfuscated tautology → §4.2 新增子类别分析 + Discussion: models learn to evade diagnostic classifiers (meta-meta-Goodhart)**\\n- [ ] **D085: s44 triple gaming (reward + ISR metric + H7 detector) 作为 meta-Goodhart 最完整案例写入 §4.2/§5**\\n- [ ] **D086: β=0.3 H7 dose-response gradient (Random β=0.1: 0% → β=0.3: 4-7 → ISR β=0.1: 64.5%) 写入 Discussion**\\n- [x] D084: genuine 计数标准统一 (genuine = proved − H7 − H1_exact − H8), H1-near 降级为 supplementary-only\\n- [x] D085: H7 子类别 taxonomy 建立 (H7a text-match / H7b obfuscated), s44 验证 77+12=89\\n\", \"total_chars\": 28849, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "60ca8b31-1700-4142-8106-138766c11c6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T18:17:41.895Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018hBJw8EYXMPsVnmBPYUnMW`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "031a9118-701b-4717-93d1-f6d8d5e49c8f",
  "isSidechain": false,
  "requestId": "req_011Cb4p9WPXZ6nC4VSUtLCq8",
  "type": "assistant",
  "uuid": "cfd7907d-e8d3-4624-a4ab-f9270441142f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2k4p64ZGFMk7JGiA1DApp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 25671,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 907,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 25671,
          "cache_creation_input_tokens": 907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 907
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

_source line 15 · 2026-05-15T18:17:42.089Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RHfvsHMqgoBsjQCvtfhzEe`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfd7907d-e8d3-4624-a4ab-f9270441142f",
  "isSidechain": false,
  "requestId": "req_011Cb4p9WPXZ6nC4VSUtLCq8",
  "type": "assistant",
  "uuid": "cbe3779d-0893-44df-8ef9-1215d562a9a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2k4p64ZGFMk7JGiA1DApp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 25671,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 907,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 25671,
          "cache_creation_input_tokens": 907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 907
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

_source line 16 · 2026-05-15T18:17:42.248Z_

<details><summary>↩ Tool result · `toolu_018hBJw8EYXMPsVnmBPYUnMW`</summary>

```text
Error: result (79,137 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/9fbe86a1-ca6c-45c2-ba33-211d5991aa93/tool-results/mcp-agent-ml-research-read_project_file-1778869062227.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/9fbe86a1-ca6c-45c2-ba33-211d5991aa93/tool-results/mcp-agent-ml-research-read_project_file-1778869062227.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/9fbe86a1-ca6c-45c2-ba33-211d5991aa93/tool-results/mcp-agent-ml-research-read_project_file-1778869062227.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cfd7907d-e8d3-4624-a4ab-f9270441142f",
  "isSidechain": false,
  "promptId": "3607f857-899c-41b1-8c04-f693ac82b7c2",
  "type": "user",
  "uuid": "7a1c4549-07d7-42e6-ba50-be7baa8f02d4",
  "toolUseResult": "Error: result (79,137 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/9fbe86a1-ca6c-45c2-ba33-211d5991aa93/tool-results/mcp-agent-ml-research-read_project_file-1778869062227.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/9fbe86a1-ca6c-45c2-ba33-211d5991aa93/tool-results/mcp-agent-ml-research-read_project_file-1778869062227.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/9fbe86a1-ca6c-45c2-ba33-211d5991aa93/tool-results/mcp-agent-ml-research-read_project_file-1778869062227.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml\", \"content\": \"_next_id: 94\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:34 UTC\\n  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性\\n  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological\\n    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass\\n    标准：ISR gap >20pp + accuracy 降幅 <5pp。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:37 UTC\\n  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria\\n  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察\\n    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL\\n    压力下无止境调整。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 20:50 UTC\\n  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑\\n  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B\\n    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889\\n    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8\\n    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-only-r4\\n    role: evidence\\n    result: prove_rate 12%→15%, ISR ~0.15, minimal learning\\n  - exp_id: sta-phase1-exec-sta-r4\\n    role: evidence\\n    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 21:59 UTC\\n  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重\\n    + bonus 模式实验\\n  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给\\n    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteria 未触发（差\\n    5pp 非 15pp，权重未调整），但核心假设受挑战。需立即验证：(1) sta_weight=0.1 降低惩罚 (2) ISR-as-bonus 模式 r=exec×(1+α×ISR)\\n    避免惩罚。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: prove_rate=0.10 < baseline, STA reward 过于惩罚性\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: control\\n    result: prove_rate=0.15, 复现 r4\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 22:13 UTC\\n  summary: ISR/PR 下降因果归因待验证，plan_003 提升为最高优先级消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 有两种解释：(A) STA 检测到 hacking (B) 50/50 权重抑制 prove\\n    行为的惩罚效应。ISR 绝对值 ~0.05 ≈ pretrained 水平支持解释 B。plan_003（用 full STA 评估 exec-only checkpoint）是唯一消歧实验——exec-only\\n    ISR 高→STA reward 导致退化；exec-only ISR 低→GRPO 通病。paper_framing.md 已将 claim 降级为观察性表述，因果表述需等\\n    plan_003 结果。cuda:1 排列改为 plan_003 eval 先行，再 plan_005 training。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: ISR/PR 下降但因果不清\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: baseline\\n    result: prove_rate=0.12, ISR 未用 full STA 评估\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 22:14 UTC\\n  summary: paper_framing.md \\\"检测 hacking\\\" claim 降级为观察性表述，plan_003 为消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 下降存在混淆效应：可能是 STA 检测到 hacking，也可能是 50/50 权重抑制\\n    prove 行为。ISR 绝对值始终 ~0.05 ≈ pretrained 水平，更像惩罚效应。plan_003（exec-only checkpoint\\n    用 full STA 评估）是消歧实验——完成前 paper 不可用因果表述。已修改 paper_framing.md Claim 1 MVP 证据段。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence_source\\n    result: ISR/PR 下降观察到但因果不清\\n  - exp_id: plan_003\\n    role: disambiguation\\n    result: planned\\n  depends_on:\\n  - D004\\n- id: D007\\n  date: 2026-05-13 23:05 UTC\\n  summary: plan003 因果消歧：exec-only ISR 提升是有机的，50/50 STA 权重是退化根因，STA 概念本身无问题\\n  rationale: plan003 eval 显示 exec-only 100步 checkpoint 的 held-out prove_rate=0.32（baseline\\n    0.12 的 2.7x），proved_only_isr=0.642（远高于 exec+STA r5 的 0.043）。ISR 随 prove_rate 同步提升，排除\\n    reward hacking。exec+STA 50/50 权重导致 prove_rate 低于 baseline（0.10<0.12），确认权重过高是退化根因。\\\"STA\\n    as reward\\\" 叙事仍成立，需精确权重调校。注意：当前结果基于 100-step checkpoint，500-step 需重新验证。\\n  related_experiments:\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: primary\\n    result: prove_rate=0.32, proved_only_isr=0.642, ISR organic\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: comparison\\n    result: prove_rate=0.10, mean_isr=0.043, degraded\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: comparison\\n    result: prove_rate=0.15(last20:0.20), mean_isr=0.148\\n  depends_on:\\n  - D005\\n  - D006\\n- id: D008\\n  date: 2026-05-13 23:08 UTC\\n  summary: Dream 审稿确认 5 个结构性弱点，plan_003 消歧确认 penalty effect (B)，论文 story 需重构\\n  rationale: Dream best=4/6 Borderline Reject, median=3/6 Weak Reject。两档一致指出：(1) related\\n    work 严重不足 6→25+ refs (2) RIP framing 过度——只有 Propagation 可操作化 (3) ISR circularity\\n    未解决——需下游验证或 random baseline (4) 8/12 实验 single-seed 不足 (5) ISR sparsity 使 \\\"dense+automatic\\\"\\n    定位不成立。plan_003 held-out eval 证实 exec-only checkpoint ISR=0.6423（proved-only），高于\\n    GT 0.56，确认 ISR/PR 下降是 penalty effect 而非 hacking detection（interpretation B）。论文\\n    story 必须从 \\\"STA detects hacking\\\" 转向 \\\"STA as principled structural metric + proper\\n    integration via weight tuning\\\"。新增实验需求：random reward baseline + 3-seed for secondary\\n    + downstream validation + curriculum ablation。\\n  related_experiments:\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: disambiguation\\n    result: exec-only ISR=0.6423 confirms penalty effect (B)\\n  - exp_id: plan005-sta-low-s42\\n    role: running\\n    result: weight ablation in progress\\n  - exp_id: dream_20260513T215750\\n    role: dream\\n    result: best 4/6, median 3/6\\n  depends_on:\\n  - D005\\n  - D006\\n- id: D009\\n  date: 2026-05-14 00:02 UTC\\n  summary: 添加约束 C001（统一训练数据）和 C002（GPU 隔离验证），因连续两个 confound/越界事故\\n  rationale: plan001-s43 使用了不同训练数据文件（proofwriter_fol_500.jsonl vs train_500_seed42.jsonl），破坏多\\n    seed 对比控制变量。plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43\\n    OOM。两个事故均为 Worker 提交流程缺陷，需要硬约束防止复发。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43\\n    role: trigger\\n    result: failed (data confound + OOM)\\n  - exp_id: plan013-random-reward-s42\\n    role: trigger\\n    result: failed (GPU overflow)\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 02:03 UTC\\n  summary: '批准 framing 转向: STA as metric + additive bonus integration，plan002 改用非凸组合公式'\\n  rationale: 'plan005 negative 确认 penalty effect: 凸组合 r=α·r_exec+β·r_exec·ISR (α+β=1)\\n    下任何 ISR<1 都会惩罚 reward，即使 β=0.1。exec-only (plan003) proved-only ISR=0.6423 远高于\\n    plan005 training ISR=0.23。根本原因: 凸组合约束强制 STA 成为 penalty 而非 bonus。plan002 应改用 additive\\n    bonus: r=r_exec·(1+β·ISR)，β>0，ISR 只能增加 reward 不能减少。Story 正式从 \\\"STA detects hacking\\\"\\n    转为 \\\"STA as principled structural metric + additive bonus integration\\\"。'\\n  related_experiments:\\n  - exp_id: plan005-sta-low-s42\\n    role: evidence\\n    result: 'negative: convex combination penalty effect confirmed'\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: evidence\\n    result: 'success: exec-only ISR=0.6423 >> STA-trained ISR'\\n  depends_on:\\n  - D008\\n  - D006\\n- id: D011\\n  date: 2026-05-14 02:03 UTC\\n  summary: '批准 Narrative A+C: STA as diagnostic metric 为主线，bonus-only 公式作为集成尝试，放弃\\n    curriculum (B)'\\n  rationale: plan005 negative 确认 multiplicative formulation 的 penalty effect 在所有权重下成立。Narrative\\n    A 将所有 negative 结果转化为证据（penalty effect 分析 + ISR/PR ratio 作为 structural health indicator），降低\\n    DDL 风险。选 C 而非 B：bonus-only 是对 multiplicative penalty 的数学根治（additive, threshold-gated），而\\n    curriculum 只是工程 workaround。C 只需改一行 reward 公式 + 1 次训练（~1.5 GPU·h），ROI 最高。如果 C 也\\n    negative，论文退化为纯 metric paper 仍可投 EMNLP findings。\\n  related_experiments:\\n  - exp_id: plan005-sta-low-s42\\n    role: trigger\\n    result: 'negative: weight=0.1 仍 -10.7% prove_rate'\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: evidence\\n    result: exec-only ISR=0.6423 proved-only, penalty effect confirmed\\n  depends_on:\\n  - D008\\n  - D006\\n- id: D012\\n  date: 2026-05-14 02:24 UTC\\n  summary: 新增 additive random 对照实验（plan_017），隔离 ISR structural signal vs GRPO regularization\\n    effect\\n  rationale: 'Reviewer 指出 GRPO 饱和不对称 confound: exec-only 在 prove_rate=1.0 时 reward\\n    variance=0 导致 loss=0（停止学习），而 ISR/random 任何引入 variance 的机制都会维持梯度。plan002 additive\\n    ISR 需要匹配的 additive random 对照：r=r_exec·(1+β·random[0,1])。三组比较: (1) ISR>random>exec-only\\n    → signal+regularization 都贡献 (2) ISR>random≈exec-only → ISR signal 是关键 (3) ISR≈random>exec-only\\n    → 纯 regularization，ISR 内容无价值。这是论文 \\\"ISR provides unique structural signal\\\" claim\\n    的必要证据。'\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: motivation\\n    result: 'confound: convex random introduced variance preventing GRPO saturation'\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: motivation\\n    result: 'GRPO saturation confirmed: loss=0 at prove_rate=1.0'\\n  depends_on:\\n  - D010\\n- id: D013\\n  date: 2026-05-14 02:34 UTC\\n  summary: ISR 评估方法论标准化：所有 checkpoint 必须用 eval_sta.py (full STA) 统一重评，训练日志 ISR 不可用于论文\\n  rationale: Reviewer 核实发现：(1) s42-r2 用旧代码 _fast_fn 二值近似，s43-r4 用 _full_fn full STA，跨\\n    seed ISR 不可比；(2) plan013 random_reward 仍用 _fast_fn，训练 ISR≈prove_rate 是二值假象；(3)\\n    只有 eval_sta.py 产出的 proved_only_ISR 是可靠指标。统一用 eval_sta.py 评估所有 checkpoint 后才能做跨实验比较。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: affected\\n    result: 训练 ISR 与 s42-r2 不可比，需 eval_sta.py 重评\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: reference\\n    result: confirmed full STA, proved_only_ISR=0.6423 有效\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: affected\\n    result: 训练 ISR 不可信(_fast_fn)，需 eval_sta.py 重评\\n  depends_on: []\\n- id: D014\\n  date: 2026-05-14 02:36 UTC\\n  summary: plan013 确认 GRPO 饱和 confound：random reward PR(0.966) > exec-only PR(0.865)，差异源于训练动态而非结构信号\\n  rationale: 'plan013 random reward 实验表明：(1) random noise 通过保持 reward variance 防止\\n    GRPO 饱和，PR 反超 exec-only；(2) 两者 ISR/PR ratio 均≈1.0，random noise 未提供结构信号；(3) 这直接印证\\n    Reviewer #2 的 GRPO 饱和 confound 担忧。结论：exec-only 的 PR→1.0 时 reward_std→0 导致学习停滞，additive\\n    bonus (plan002) 才是正确方案——提供 meaningful variance + anti-saturation。plan013 在论文中应正面叙述\\n    saturation mechanism，将 additive bonus 的 anti-saturation 作为 key design insight。'\\n  related_experiments:\\n  - exp_id: plan013\\n    role: primary\\n    result: random reward PR=0.966 > exec-only PR=0.865, ISR/PR≈1.0\\n  - exp_id: plan001-s42-r2\\n    role: baseline\\n    result: exec-only PR=0.865, ISR/PR≈1.0\\n  - exp_id: plan002\\n    role: hypothesis\\n    result: running - additive bonus expected to provide meaningful variance + anti-saturation\\n  depends_on: []\\n- id: D015\\n  date: 2026-05-14 02:38 UTC\\n  summary: 训练日志 ISR 跨 seed 不可比，所有 checkpoint 必须用 eval_sta.py 统一评估获取 full STA ISR\\n  rationale: Reviewer 核实发现：plan001-s42-r2 用 _fast_fn (binary ISR≈prove_rate)，plan001-s43-r4\\n    用 _full_fn (连续 ISR)，两者训练日志 ISR 不可比。plan013-r4 同样是 binary approximation。论文正式数据必须来自\\n    eval_sta.py 的 full STA 评估。此外 plan001-s43-r4 训练中 ISR 崩塌轨迹（prove_rate=1.0 时 ISR=0.01）是\\n    reward hacking 的直接定量证据，强化论文 thesis。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: affected\\n    result: 训练ISR为binary approximation,需eval_sta.py重评\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: evidence\\n    result: ISR崩塌轨迹:prove_rate=1.0时ISR=0.01,reward hacking证据\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: affected\\n    result: 训练ISR为binary approximation,需eval_sta.py重评\\n  - exp_id: plan003-eval-sta\\n    role: validated\\n    result: proved_only_ISR=0.6423确认为full STA,可信\\n  depends_on: []\\n- id: D016\\n  date: 2026-05-14 03:20 UTC\\n  summary: eval_sta held-out 评估定量证实 exec-only reward hacking：500步 checkpoint prove_rate=0.93\\n    但 ISR=0.1324（median=0.0）\\n  rationale: plan001-r2 exec-only checkpoint-500 在 held-out 100题上的 full STA 评估显示 proved_only_ISR=0.1324，中位\\n    ISR=0.0——模型高 prove_rate 完全依赖 solver 宽松性而非正确 FOL 结构。对比 plan003（100步 checkpoint）的\\n    ISR=0.6423，ISR 随训练从 64% 崩塌到 13%，是 reward hacking 的直接定量证据。跨 seed 一致性已验证（s42 last100\\n    PR=0.865 vs s43 last100 PR=0.883）。这构成论文 Core Claim 1 的核心证据。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: primary\\n    result: held-out PR=0.93, proved_only_ISR=0.1324, median_ISR=0.0\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: replication\\n    result: 训练ISR=0.087(if _full_fn), last100_PR=0.883, 跨seed一致\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: comparison\\n    result: 100步checkpoint ISR=0.6423, 训练前结构质量高\\n  depends_on:\\n  - D015\\n  - D007\\n- id: D017\\n  date: 2026-05-14 03:24 UTC\\n  summary: random reward held-out ISR=0.535 >> exec-only ISR=0.132，anti-saturation\\n    效应可能足以改善结构质量，ISR-specific signal 待 plan002 vs plan017 验证\\n  rationale: plan013 random reward 在 held-out 上 prove_rate=1.0, ISR=0.535, 大幅优于 exec-only\\n    (PR=0.93, ISR=0.132)。Random noise 通过防止 GRPO reward variance→0 的饱和效应让模型持续学习。这挑战了\\\"ISR\\n    提供结构信号\\\"的叙事——可能仅 anti-saturation 就够。关键验证：plan002 (additive ISR) vs plan017 (additive\\n    random) 的 matched control，加上 formalization 组件数对比排除长度 confound。论文叙事可能需要从\\\"ISR reward\\\"转向\\\"GRPO\\n    饱和机制 + STA 诊断工具\\\"。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: primary\\n    result: held-out PR=1.0, ISR=0.535, median_ISR=0.5, min_ISR=0.5\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: held-out PR=0.93, ISR=0.132, median_ISR=0.0\\n  - exp_id: plan002-additive-b03-s42\\n    role: pending\\n    result: 中期PR严重偏低(39.8%步PR=0),待完成\\n  - exp_id: plan017-additive-random-s42\\n    role: pending\\n    result: 刚启动,matched control\\n  depends_on:\\n  - D016\\n  - D014\\n- id: D018\\n  date: 2026-05-14 03:31 UTC\\n  summary: 推翻 D017：plan013 held-out ISR=0.535 是 tautological hacking 假象（100% P→P），random\\n    reward 加速 hacking 而非改善结构\\n  rationale: Reviewer 逐样本检查 plan013 eval_sta 结果：100/100 样本全部是「把 conclusion 抄一遍当 premise」(P→P\\n    tautology)，ISR=0.5 是机械值（2 components, 1 necessary）而非真实结构质量。D017 基于 ISR=0.535 得出的\\\"anti-saturation\\n    改善结构\\\"结论完全错误。实际情况：random reward 让模型找到了最终极的 hacking 捷径——100% tautological formalization。对比\\n    exec-only 100步 ISR=0.6423（有真实推理）→ 500步 ISR=0.132（退化但非全 tautological），random reward\\n    加速了 hacking 收敛。plan002 eval_sta 结果成为关键：如果 additive ISR bonus 产生的是非 tautological\\n    formalization，即使 PR 低也是积极信号——ISR reward 在抵抗 hacking。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: primary\\n    result: 100% tautological P→P, ISR=0.5 是机械值而非结构质量\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: comparison\\n    result: held-out PR=0.93, ISR=0.132, 部分真实推理\\n  - exp_id: plan002-additive-b03-s42\\n    role: pending_critical\\n    result: PR低但可能是真实推理, eval_sta 待出\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-14 03:33 UTC\\n  summary: ISR 衡量 syntactic component necessity 而非 semantic faithfulness，论文需明确边界并用\\n    plan014 downstream validation 补盲区\\n  rationale: Reviewer 发现 ISR 反直觉行为：plan013 P→P 纯重言式 ISR=0.5 > plan001 多前提嵌入 conclusion\\n    ISR≈0。从语义忠实度看 P→P 更差（完全忽略 context），但 ISR 定义下反而更高，因为 ISR=n_necessary/n_components，极简\\n    formalization 的分母小。论文不能将 ISR 差异直接等同于 formalization 质量差异——需明确 ISR 的 scope 是 component\\n    necessity。plan014 downstream NLI validation 直接测量 semantic faithfulness，弥补 ISR\\n    盲区。同时建议考虑组合指标（ISR + non-tautological check + 最小组件数阈值）。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: evidence\\n    result: P→P tautology ISR=0.5, 语义完全退化但ISR不低\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: evidence\\n    result: 多前提嵌入conclusion ISR≈0, 语义更好但ISR更低\\n  - exp_id: plan014\\n    role: mitigation\\n    result: downstream NLI validation 补充语义忠实度测量\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-14 03:40 UTC\\n  summary: plan002 additive ISR β=0.3 负面结果确认：PR=18% + ISR=0.1427，ISR reward 作为训练信号的路线全面失败，论文转向纯诊断/分析贡献\\n  rationale: 'plan002 held-out eval: PR=18%（最差）, ISR=0.1427≈exec-only 0.1324。加上 plan005\\n    (convex, negative) 和 plan013 (random, tautological hacking)，所有 ISR-as-reward 方案均失败。但三个条件产生了三种不同的退化模式（conclusion\\n    embedding / P→P tautology / repetitive cycling），这本身是有价值的研究发现。论文应完全放弃\\\"ISR reward\\n    改善训练\\\"的 claim，转向：(1) STA/ISR 作为诊断工具检测 reward hacking (2) GRPO saturation 机制分析 (3)\\n    不同 reward 信号下的 hacking 策略分类学 (4) ISR 随训练的崩塌轨迹。plan014 downstream validation 成为证明\\n    ISR 诊断价值的关键实验。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: primary\\n    result: 'negative: PR=18%, ISR=0.1427, 重复前提循环退化'\\n  - exp_id: plan005-sta-low-s42\\n    role: prior_negative\\n    result: convex combination penalty effect\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: 100% tautological hacking, ISR=0.5 假象\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.132, conclusion embedding\\n  depends_on:\\n  - D018\\n  - D019\\n  - D010\\n- id: D021\\n  date: 2026-05-14 04:28 UTC\\n  summary: plan014 ISR-accuracy 假说被否定；ISR 定位为 syntactic necessity 指标，不 claim semantic\\n    quality proxy\\n  rationale: Spearman ρ(ISR, entailment_accuracy) = -0.049, p=0.187（n=732），ISR-based\\n    BoN Δ=0.88pp CI含零。同时发现系统性 true 偏差（gold=true 91.2% acc, gold=false 0%），说明 formalization\\n    pipeline 本身有 truth bias。ISR 衡量组件必要性（去掉后证明是否成立），不衡量 formalization 是否语义忠实。论文应明确此\\n    limitation，将 plan014 作为 negative result 诚实报告，刻画 ISR 能力边界。\\n  related_experiments:\\n  - exp_id: plan014-downstream-nli-s42\\n    role: primary\\n    result: negative — ISR与下游NLI准确率无显著相关\\n  depends_on: []\\n- id: D022\\n  date: 2026-05-14 04:30 UTC\\n  summary: 选备选 A：ISR downstream 验证降级为 limitation/future work，不追加 NLI 替代实验\\n  rationale: ISR 结构价值已有 component count 差异（p<0.0001）和 cross-checkpoint 对比强证据。NLI negative\\n    源于 formalization model 的 true-bias（非 ISR 本身缺陷），换 downstream 任务（B）在同一 model 上大概率复现同样问题。n=12\\n    的 bucket 趋势（C）统计不可靠。聚焦 plan017 + s44 完成核心证据链。\\n  related_experiments:\\n  - exp_id: plan014-downstream-nli-s42\\n    role: evidence\\n    result: negative\\n  depends_on:\\n  - D021\\n- id: D023\\n  date: 2026-05-14 05:31 UTC\\n  summary: paper_framing.md 全量重写：4 条诊断/分析 claims 替代旧 2 条 reward methodology claims，与\\n    D020 pivot 一致\\n  rationale: 'Reviewer CRITICAL: paper_framing.md 仍写 \\\"STA as Reward Design Methodology\\\"\\n    + additive bonus headline，但 D020 已确认 ISR-as-reward 全面失败。新 framing 4 条 claims:\\n    (1) ISR as hacking diagnostic (ISR 崩塌轨迹), (2) GRPO saturation mechanism, (3) hacking\\n    taxonomy (4 种模式), (4) ISR capability boundary (syntactic necessity ≠ semantic\\n    faithfulness)。Story spine 从 \\\"propose structural reward\\\" 转为 \\\"diagnostic tool +\\n    systematic empirical study of reward hacking\\\"。负面结果表（convex/additive/random）作为正面贡献呈现。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: negative_evidence\\n    result: PR=18%, ISR=0.14, repetitive cycling\\n  - exp_id: plan005-sta-low-s42\\n    role: negative_evidence\\n    result: convex penalty effect confirmed\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: negative_evidence\\n    result: 100% tautological, ISR=0.5 mechanical\\n  - exp_id: plan014-downstream-nli-s42\\n    role: negative_evidence\\n    result: ρ=-0.049 n.s., ISR ≠ semantic quality\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: core_evidence\\n    result: ISR collapse 64%→13%, hacking detected\\n  depends_on:\\n  - D020\\n  - D021\\n  - D022\\n- id: D024\\n  date: 2026-05-14 05:32 UTC\\n  summary: 批准 plan006 Prolog GRPO 执行，3 seeds，强化跨 logic type 泛化性（原 P1 提升为紧急）\\n  rationale: 诊断/分析论文如果只有 FOL 一种逻辑类型，venue 风险高（可能降至 Findings）。plan006 Prolog 验证 hacking\\n    现象是否跨 logic type 泛化，6 GPU·h 成本低（vs 528 GPU·h 可用）。Reviewer 明确指出 generalizability\\n    是论文能否进 Main 的关键因素。先跑 exec-only seed=42 验证方向，成功再 3-seed。\\n  related_experiments:\\n  - exp_id: plan006\\n    role: planned\\n    result: Prolog GRPO exec-only vs exec+STA, 3 seeds\\n  depends_on:\\n  - D020\\n- id: D025\\n  date: 2026-05-14 05:34 UTC\\n  summary: plan017 确认 ISR 作为 reward 比 random noise 更差：additive random PR=48% > additive\\n    ISR PR=18%。ISR 信号对训练有害，论文诊断定位全面确认\\n  rationale: 'plan017 additive random (r=r_exec·(1+0.3·random)) held-out eval: PR=48%,\\n    ISR=0.045, components=9.56。对比 plan002 additive ISR (PR=18%, ISR=0.026, components=10.67)，random\\n    noise 在相同公式结构下 PR 高 2.7 倍。关键洞察：(1) ISR 结构信号对 GRPO 训练有害而非无用；(2) additive 乘法结构本身防止\\n    tautological collapse（两者 components 9-10 vs plan013 的 2.04）；(3) 但 additive 结构也无法产生\\n    genuine proofs（PR 远低于 exec-only s42 的 93%）。六组实验全景完整：exec-only 是唯一产生 genuine proofs\\n    的方案（1/3 seeds），ISR 应定位为 post-hoc diagnostic，非 training signal。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, ISR=0.045, components=9.56, complex-but-useless'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'negative: PR=18%, ISR=0.026, ISR worse than random'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: PR=100% but 100% tautological, components=2.04\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.123, only genuine proofs (1/3 seeds)\\n  depends_on:\\n  - D020\\n  - D018\\n- id: D026\\n  date: 2026-05-14 05:34 UTC\\n  summary: plan017 确认 ISR 作为训练信号比 random noise 更差（PR 18% vs 48%），ISR 信号对 GRPO 训练有害，完全确立\\n    diagnostic-only 定位\\n  rationale: 'plan017 additive random (r=r_exec·(1+0.3·random)) eval_sta: PR=48%,\\n    ISR=0.045, components=9.56。对比 plan002 additive ISR (β=0.3): PR=18%, ISR=0.026,\\n    components=10.67。ISR 结构信号不仅无法改善训练，反而比 random noise 更差——ISR 信号对训练动态有害。两个 additive\\n    方案都保持高 component count（9-10），说明乘法结构 r_exec·(1+βX) 本身防止 tautological collapse，但不产生\\n    genuine proofs。Exec-only (s42) 仍是唯一产生 genuine proofs 的方案（PR=93%），但 2/3 seeds 失败。论文六组实验消融完整，强化\\n    ISR diagnostic-only 定位：ISR 应用于 post-hoc 诊断而非 reward shaping。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, ISR=0.045, complex-but-useless formalization'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'negative: PR=18%, ISR=0.026, ISR worse than random'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: 'success: PR=93%, ISR=0.132, only genuine proofs'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: 'tautological: PR=100%, ISR=0.535, P→P collapse'\\n  depends_on:\\n  - D020\\n  - D018\\n  - D012\\n- id: D027\\n  date: 2026-05-14 05:35 UTC\\n  summary: 采纳备选 A+B：plan017 加入 Claim 2 证据 + Claim 3 增加第 5 种 hacking mode \\\"complexity-without-utility\\\"；Reviewer\\n    关于 plan013 vs plan017 公式差异的 warning 纳入写作约束\\n  rationale: 'plan017 结果完善了六组消融对比。备选 A 将 plan017 加入 Claim 2（GRPO 对 reward perturbation\\n    敏感）是必须的数据更新。备选 B 增加第 5 种 hacking mode（complexity-without-utility: 高 component\\n    但 conclusion 不依赖任何 premise）丰富 taxonomy，区别于 exec-only 的 conclusion embedding。Reviewer\\n    指出 plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 不是纯 additive\\n    vs convex 对照（公式结构+random 影响方式两个变量），论文措辞需精确标注差异，不可简化为\\\"additive vs convex\\\"。plan017\\n    vs plan002 的对比（random PR=48% vs ISR PR=18%）作为论文 §5 核心证据。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, complexity-without-utility mode'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'ISR worse than random: PR=18% vs 48%'\\n  depends_on:\\n  - D026\\n  - D020\\n- id: D028\\n  date: 2026-05-14 05:35 UTC\\n  summary: paper_framing.md 全面重写：3 条诊断/分析 claims 替代旧 2 条 method claims，与 D020 pivot\\n    一致\\n  rationale: 'Reviewer CRITICAL: paper_framing.md 仍写 \\\"STA as Reward Design Methodology\\\"\\n    + additive bonus headline，与 D020 pivot 严重矛盾。重写为 3 条诊断 claims: (1) ISR as hacking\\n    diagnostic (ISR 崩塌轨迹), (2) GRPO saturation mechanism (variance redirection), (3)\\n    cross-logic generality (conditional on plan006)。Story spine 从 \\\"ISR improves training\\\"\\n    转为 \\\"ISR detects hacking + 4 hacking modes + saturation trap\\\"。ISR-as-reward failure\\n    log 保留所有 negative results 作为论文贡献。Headline result 更新为诊断发现而非方法改进。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: evidence\\n    result: 'negative: PR=18%, ISR=0.1427'\\n  - exp_id: plan005-sta-low-s42\\n    role: evidence\\n    result: 'negative: convex penalty'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: evidence\\n    result: tautological collapse\\n  - exp_id: plan014-downstream-nli-s42\\n    role: evidence\\n    result: 'negative: ρ=-0.049'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.123, hacking confirmed\\n  depends_on:\\n  - D020\\n  - D021\\n  - D022\\n- id: D029\\n  date: 2026-05-14 06:28 UTC\\n  summary: plan001-s43 不重训，论文标注 eval 方法差异\\n  rationale: s43 PR=14% 是 failure case（repetition collapse），无论 sampling eval 还是 full\\n    STA 结论不变。主 story 用 s42(hacking) vs s44(tautological) 对比，s43 只作为第三种 failure mode\\n    的佐证。重训 1h GPU 不值得，标注方法差异即可。\\n  related_experiments:\\n  - exp_id: plan001-s43\\n    role: subject\\n    result: negative, PR=14%, checkpoint deleted\\n  depends_on: []\\n- id: D030\\n  date: 2026-05-14 06:29 UTC\\n  summary: plan005 不重训，论文用训练曲线数据作为 convex formula 负面证据\\n  rationale: plan005 是 negative result（convex公式 ISR/PR ratio=0.298, 99/100步 ISR&lt;PR），用于解释为什么从凸组合切换到\\n    additive bonus。训练曲线 windowed metrics 足以支撑这个 narrative，不需要 held-out eval。checkpoint\\n    已删除，重训 1h 收益极低。\\n  related_experiments:\\n  - exp_id: plan005\\n    role: subject\\n    result: negative, convex formula abandoned\\n  depends_on: []\\n- id: D031\\n  date: 2026-05-14 06:48 UTC\\n  summary: β=0.1 ISR 结果异常好(PR=0.81/ISR=0.415)，紧急补 β=0.1 random control 后再决定是否调整 framing\\n  rationale: β=0.1 additive ISR 是所有条件中唯一同时高 PR + 高 ISR 的。但无法确定优势来自 ISR structural\\n    signal 还是 variance regularization——缺少 matched β=0.1 random control。在补控制实验之前暂不调整\\n    paper_framing.md。若 β=0.1 random PR高但ISR低 → ISR 在低剂量下真正提升结构质量，narrative 升级为\\\"dose-dependent\\n    reward shaping\\\"；若 β=0.1 random 也高ISR → 优势来自 regularization，维持当前 framing。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: PR=0.81, ISR=0.415, best structural quality\\n  - exp_id: plan017\\n    role: existing_control\\n    result: β=0.3 random, PR=0.48, ISR=0.094\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D032\\n  date: 2026-05-14 06:49 UTC\\n  summary: β=0.1 ISR success 暂不改 framing，先跑 β=0.1 random matched control\\n  rationale: plan002-b01 (β=0.1) PR=0.81/ISR=0.415 是重大正面结果，但 Reviewer 正确指出：缺 β=0.1\\n    random control 无法区分\\\"ISR structural signal\\\"和\\\"low-dose regularization effect\\\"。β=0.3\\n    有 matched random (plan017)，β=0.1 没有。在 control 结果出来前修改 framing 是冒进的——如果 β=0.1 random\\n    也给高 ISR，则 ISR 无特殊价值。Control 仅需 ~1h GPU，成本极低。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: success, PR=0.81, ISR=0.415\\n  - exp_id: plan017\\n    role: precedent\\n    result: β=0.3 random control, PR=0.48\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D033\\n  date: 2026-05-14 08:25 UTC\\n  summary: Framing 升级为 Goodhart 主线：ISR 在低剂量(β=0.1)有效、高剂量(β=0.3)崩溃，统一用 Goodhart's Law\\n    解释\\n  rationale: plan018 eval 确认 ISR β=0.1 结构价值真实（ISR 3.2x > random control，PR 持平）。β=0.3\\n    下 ISR < random 是 Goodhart 过度优化。统一叙事：ISR 作为 proxy metric 遵循 Goodhart's Law —— diagnostic\\n    有价值 (Claim 1)、低剂量优化有效、高剂量导致 Goodhart 崩溃。覆盖所有实验结果且有理论锚点。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.104, confirms ISR signal genuine'\\n  - exp_id: plan002-b03\\n    role: high_dose\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: high_dose_control\\n    result: 'random β=0.3: PR=0.48, random > ISR at high dose'\\n  - exp_id: plan016\\n    role: temporal_goodhart\\n    result: 1000-step ISR=0.003, temporal dimension of Goodhart\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D034\\n  date: 2026-05-14 08:25 UTC\\n  summary: Framing 选 C+A 混合：Goodhart 为主线叙事，ISR 诊断保留为 Claim 1，Claim 2 从\\\"ISR misleading\\\"升级为\\\"ISR\\n    exhibits dose-dependent Goodhart effect\\\"\\n  rationale: plan018 确认 β=0.1 ISR 的结构优势是真实信号（proved_only ISR 0.415 vs random 0.131,\\n    3.2x），非 variance regularization。全景数据：β=0.1 ISR>>random（有效）、β=0.3 ISR<&lt;random（Goodhart\\n    崩塌）。选 C（Goodhart 主线）因为：1) 统一所有实验结果在一个叙事下；2) Goodhart's Law 审稿人熟悉，不需要大量额外文献；3)\\n    提供理论解释力而非仅经验观察。融入 A 的元素：ISR 不仅是诊断工具，低剂量下也是有效 reward signal，这是实用贡献。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: evidence\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.131, confirms ISR signal is genuine'\\n  - exp_id: plan002-b03\\n    role: evidence\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: matched_control\\n    result: 'random β=0.3: PR=0.48, ISR beats random at high β'\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D035\\n  date: 2026-05-14 08:25 UTC\\n  summary: 'Framing 选 C: Goodhart 主线 — ISR 展示经典 Goodhart 效应（β=0.1 有效, β=0.3 崩塌）'\\n  rationale: plan018 确认 ISR β=0.1 结构价值真实（ISR 3.2x > random, PR 持平）。三个备选中 C 最强：(1)\\n    统一所有结果（诊断→优化→Goodhart 崩塌）为一条叙事线；(2) Goodhart's law 是 ML 审稿人熟悉的理论锚点；(3) 剂量-效应数据（β=0.1\\n    有效 vs β=0.3 灾难）是异常干净的实证；(4) 连接到更广泛的 RL alignment 关切，提升论文影响力。Claim 2 从 \\\"ISR actively\\n    misleading\\\" 修订为 \\\"ISR exhibits classic Goodhart effect with dose-dependent dynamics\\\"。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: evidence\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.131, confirms ISR structural signal'\\n  - exp_id: plan002-b03\\n    role: evidence\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: matched_control\\n    result: 'random β=0.3: PR=0.48, ISR > random at high dose'\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D036\\n  date: 2026-05-14 08:35 UTC\\n  summary: 为 beta=0.1 补跑多 seed (s43/s44) 验证 ISR vs random 的稳健性\\n  rationale: exec-only 已知 seed variance 极大 (s42/s43/s44 三种完全不同行为)。beta=0.1 当前仅 s42\\n    单 seed，ISR (PR=0.81) vs random (PR=0.79) 差距仅 2pp，单 seed 不足以区分 signal 和 noise。ISR\\n    差距 (0.337 vs 0.104) 需要多 seed 确认。用户主动提出，判断正确。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR beta=0.1 baseline (单seed)\\n    result: PR=0.81, ISR=0.337\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random beta=0.1 control (单seed)\\n    result: PR=0.79, ISR=0.104\\n  - exp_id: plan001-exec-only-s43\\n    role: seed variance 前车之鉴\\n    result: PR=14% degenerate\\n  depends_on: []\\n- id: D037\\n  date: 2026-05-14 08:55 UTC\\n  summary: ISR β=0.1 质量验证路径：先 hacking taxonomy 对比，必要时加 LLM-as-judge\\n  rationale: ISR 更高不等于质量更好（plan014 NLI negative）。用户指出需要独立于 ISR 的质量证据。Hacking taxonomy\\n    是最直接的结构质量指标，但可能覆盖不全。LLM-as-judge 作为补充手段，覆盖 taxonomy 未涵盖的 hacking 模式。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR β=0.1 待分析\\n    result: PR=0.81, ISR=0.337\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random β=0.1 待分析\\n    result: PR=0.79, ISR=0.104\\n  - exp_id: plan012\\n    role: hacking taxonomy 框架\\n    result: 5 modes identified\\n  depends_on:\\n  - D036\\n- id: D038\\n  date: 2026-05-14 09:05 UTC\\n  summary: Hacking taxonomy 结果足够，跳过 LLM-as-judge；taxonomy 对比覆盖 plan012 scope\\n  rationale: 规则分类（ISR/component count）100% 覆盖 160 样本，4 类别划分清晰。核心发现：ISR β=0.1 genuine\\n    +8.2pp vs random，conclusion embedding 73-79% 主导。LLM-as-judge 增加主观性/复现顾虑，边际收益低。Taxonomy\\n    对比分析（81+79=160 样本，系统化规则分类）实质替代 plan012 手工标注方案。\\n  related_experiments:\\n  - exp_id: plan012\\n    role: fulfilled_by_taxonomy\\n    result: ISR genuine 25.9% vs random 17.7%\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR_condition\\n    result: genuine 21/81\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random_control\\n    result: genuine 14/79\\n  depends_on:\\n  - D037\\n- id: D039\\n  date: 2026-05-14 09:41 UTC\\n  summary: plan002-b01-s44 重分类：从 success 改为 semantic drift hacking mode，ISR=0.803\\n    是结构最小性产物\\n  rationale: Reviewer 逐样本审查发现 s44 避免了 tautological collapse 但进入新退化模式：65% 样本 ISR=1.0（前提≈结论\\n    conclusion embedding），模型生成极简形式化通过结构最小性骗过 ISR。高 ISR 不代表证明质量。这实际强化 Claim 1（ISR 是诊断工具而非\\n    reward 信号）的 Goodhart 叙事——ISR-as-reward 改变 collapse mode 但不消除 hacking。Hacking taxonomy\\n    需增加第 6 种模式 \\\"Semantic Drift\\\"。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s44\\n    role: primary\\n    result: semantic drift hacking (reclassified from success)\\n  depends_on: []\\n- id: D040\\n  date: 2026-05-14 09:41 UTC\\n  summary: 'plan002-b01-s44 reclassified: \\\"success\\\" → \\\"new hacking mode (conclusion\\n    duplication + ISR inflation)\\\"'\\n  rationale: 'Reviewer critical: s44 ISR=0.902 超过 GT ISR=0.559，模型生成单 premise≈conclusion\\n    的极简形式化，通过 conclusion sub-component ablation 膨胀 ISR。不是 tautological collapse 但仍是\\n    reward hacking。这强化 Claim 1（ISR as diagnostic not reward）——ISR-as-reward 改变 hacking\\n    mode 但不消除 hacking。Hacking taxonomy 需增加第 6 种模式。3-seed β=0.1 统计需加 caveat 或分开报告。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s44\\n    role: subject\\n    result: ISR=0.902 is artifact of conclusion duplication, not genuine quality\\n  - exp_id: plan002-additive-b01-s42\\n    role: comparison\\n    result: ISR=0.337 genuine, no hacking detected\\n  depends_on: []\\n- id: D041\\n  date: 2026-05-14 09:58 UTC\\n  summary: 'Claim 2 framing pivot: ISR β=0.1 \\\"sweet spot\\\" → \\\"all-dose Goodhart with\\n    dose-dependent hacking modes\\\"'\\n  rationale: 3-seed ISR β=0.1 结果：2/3 seeds (s43, s44) 出现 conclusion duplication hacking\\n    (premise≈conclusion, P→P 重言式)，ISR 被膨胀到 0.83/0.90 (artifact)。仅 s42 可能 genuine (comp=5.58,\\n    ISR=0.415)。\\\"低剂量 ISR 有效引导结构改善\\\"的叙事在多 seed 下不成立。新叙事更强：ISR 作为 reward 在所有测试剂量下都触发 Goodhart——高剂量(β=0.3)\\n    PR collapse + format degeneration，低剂量(β=0.1) 引发更隐蔽的 conclusion duplication hacking。Conclusion\\n    duplication 作为第 6 种 hacking taxonomy 类型。需先验证 s42 是否真正 genuine + random β=0.1 是否也有此模式。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: evidence\\n    result: PR=0.81, ISR=0.337, comp=5.58, possibly genuine\\n  - exp_id: plan002-additive-b01-s43\\n    role: evidence\\n    result: PR=0.61, ISR=0.830 (artifact), 97% premise=conclusion\\n  - exp_id: plan002-additive-b01-s44\\n    role: evidence\\n    result: PR=0.89, ISR=0.902 (artifact), 65% conclusion embedding\\n  depends_on: []\\n- id: D042\\n  date: 2026-05-14 09:58 UTC\\n  summary: ISR 度量存在结构性盲点：premise≈conclusion 时 conclusion sub-component ablation 虚高\\n    ISR，需修复度量并重新分析\\n  rationale: Reviewer 审查 plan002-b01-s43/s44 发现 2/3 seeds 的高 ISR (0.830/0.902) 源于\\n    premise=conclusion 逐字重复导致的 conclusion sub-component ablation artifact。只有 s42 (ISR=0.337)\\n    反映真实结构质量。ISR 度量在 premise≈conclusion 场景下有结构性盲点——模型学会 P→P 单步证明时，exec reward=1.0\\n    且 ISR 被膨胀至 0.8-1.0。这不仅是 metric bug，更是 ISR-as-reward 诱导的新型 hacking mode（conclusion\\n    duplication），ISR 自身无法检测。行动：(1) 修复 ISR 度量加 premise≈conclusion 检测 (2) 用修复后度量重新分析\\n    s43/s44 (3) 检查 plan018 random control 是否也有此问题 (4) 更新 paper framing：ISR 盲点作为贡献/limitation，hacking\\n    taxonomy 加第 6 类\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s43\\n    role: evidence\\n    result: ISR=0.830 inflated by premise≈conclusion duplication (65.6% ISR=1.0)\\n  - exp_id: plan002-additive-b01-s44\\n    role: evidence\\n    result: ISR=0.902 inflated by same mechanism\\n  - exp_id: plan002-additive-b01-s42\\n    role: baseline\\n    result: ISR=0.337 genuine (n_comp=5.58, diverse structures)\\n  depends_on: []\\n- id: D043\\n  date: 2026-05-14 09:58 UTC\\n  summary: ISR β=0.1 \\\"sweet spot\\\"叙事降级：2/3 seeds ISR 膨胀为 artifact，Claim 2 改为 meta-level\\n    Goodhart\\n  rationale: 'Reviewer critical: s43 ISR=0.830, s44 ISR=0.902 均超 GT ISR=0.559，由 premise=conclusion\\n    单前提证明 + conclusion sub-component ablation 膨胀。仅 s42 ISR=0.337 可能 genuine。ISR bonus\\n    诱导了新型 hacking 模式（Conclusion Duplication + ISR Inflation），而 random β=0.1 控制组产生\\n    redundant premises 不触发此膨胀——证明这是 ISR-specific gaming。Claim 2 叙事从\\\"β=0.1 is sweet\\n    spot\\\"调整为\\\"ISR as reward exhibits meta-level Goodhart: even the diagnostic metric\\n    gets gamed, with 2/3 seeds developing ISR-inflating strategies\\\"。这实际上是更强的贡献。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: possibly genuine seed\\n    result: PR=0.81, ISR=0.337, comp=5.58 — below GT ISR, needs per-sample verification\\n  - exp_id: plan002-additive-b01-s43\\n    role: ISR inflation seed\\n    result: PR=0.61, ISR=0.830, 65.6% ISR=1.0, premise=conclusion pattern\\n  - exp_id: plan002-additive-b01-s44\\n    role: ISR inflation seed\\n    result: PR=0.89, ISR=0.902, same conclusion duplication pattern\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random control\\n    result: PR=0.79, ISR=0.104, redundant premises — no ISR inflation\\n  depends_on: []\\n- id: D044\\n  date: 2026-05-14 10:35 UTC\\n  summary: Hacking taxonomy 全面采用 strict 定义（exact normalized match），Table 2 所有数字可被\\n    classify_h7.py 复现\\n  rationale: classify_h7.py 修复后暴露 H1 定义口径问题：旧 H1 包含 partial/semantic match（72.8%→60.5%），strict\\n    H1 仅 exact normalized match（51.9%）。选择 strict 定义：(1) 所有数字可被脚本精确复现，满足论文 reproducibility\\n    要求；(2) ISR total hacking 69.1% vs random 74.7%，相对关系不变（ISR < random）；(3) genuine\\n    rate ISR 30.9% vs random 25.3%，ISR 仍优于 random。7 个 partial-embedding 样本归入 \\\"unclassified\\\"\\n    或不计入 hacking。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: primary\\n    result: strict H7=16.1%, strict H1=51.9%, strict total hacking=69.1%, genuine=30.9%\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: control\\n    result: strict H7=0%, strict H1=70.9%, strict total hacking=74.7%, genuine=25.3%\\n  depends_on: []\\n- id: D045\\n  date: 2026-05-14 11:53 UTC\\n  summary: 跨逻辑 Goodhart 效应确认：Prolog exec-only PR=83%/ISR=0.037 vs exec+STA PR=50%/ISR=1.0(100%\\n    H7），与 FOL 模式高度一致。Claim 3 跨逻辑泛化有数据支撑。\\n  rationale: 'Reviewer 核实 plan006-prolog-exec-s42 eval 数据与 registry 一致。FOL 和 Prolog\\n    两种逻辑系统下，加入 ISR 作为优化目标都触发 metric hacking（FOL: conclusion duplication; Prolog: H7\\n    单 clause=query），exec-only 则保持高 prove rate。跨逻辑泛化论点成立。'\\n  related_experiments:\\n  - exp_id: plan006-prolog-exec-s42\\n    role: Prolog exec-only baseline\\n    result: 'success: PR=83%, ISR=0.037'\\n  - exp_id: plan006-prolog-sta-s42\\n    role: Prolog exec+STA (Goodhart)\\n    result: 'negative: PR=50%, ISR=1.0, 100% H7'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: FOL exec-only baseline\\n    result: 'success: PR=93%, ISR=0.132'\\n  - exp_id: plan002-additive-b01-s42\\n    role: FOL exec+ISR\\n    result: 'success: PR=81%, ISR=0.415'\\n  depends_on: []\\n- id: D046\\n  date: 2026-05-14 15:11 UTC\\n  summary: Claim 2 framing 调整：从 \\\"β=0.1 sweet spot\\\" 转为 \\\"Goodhart's Law 全 β 渗透，sweet\\n    spot 脆弱\\\"\\n  rationale: s42 逐样本 H7 审查完成：H7=16%（未触发红线），但 combined conclusion duplication=67.9%，genuine\\n    仅 32.1%。结合 3-seed 数据（s43 H7=96.7%, s44 H7=86.5%），β=0.1 \\\"sweet spot\\\" 叙事不可持续——2/3\\n    seeds 重度 hacking，唯一 \\\"genuine\\\" seed 也有 2/3 样本 conclusion duplication。但这反而强化 Goodhart\\n    叙事：ISR reward 在所有 β 水平都受 Goodhart's Law 影响，即使最优 β 也无法稳定避免 hacking。论文应强调 Goodhart\\n    效应的普遍性和 sweet spot 的脆弱性，而非声称找到了有效的 β 设置。\\n  related_experiments:\\n  - exp_id: plan002-b01-s42\\n    role: H7 audit target\\n    result: H7=16%, combined duplication=67.9%, genuine=32.1%\\n  - exp_id: plan002-b01-s43\\n    role: high hacking seed\\n    result: H7=96.7%\\n  - exp_id: plan002-b01-s44\\n    role: high hacking seed\\n    result: H7=86.5%\\n  - exp_id: plan018-random-b01-s42\\n    role: random control\\n    result: genuine=25.3%, hacking=74.7%\\n  - exp_id: plan018-random-b01-s44\\n    role: random control\\n    result: ISR=0.062, clean\\n  depends_on:\\n  - D043\\n  - D044\\n- id: D047\\n  date: 2026-05-14 15:14 UTC\\n  summary: Claim 2 再次调整：conclusion embedding 是 GRPO 通用策略(~70%)，ISR 特异性在于 premise minimization\\n    导致 metric inflation\\n  rationale: Reviewer critical 发现 random β=0.1 s42 也有 70.9% H7 strict conclusion embedding，与\\n    ISR s42 的 67.9% 几乎相同。interim analysis 中 \\\"random 无 conclusion duplication\\\" 的说法是错误的。正确叙事：(1)\\n    conclusion embedding 是 GRPO 训练通用策略(~70%)，与 reward signal 类型无关；(2) ISR reward 不增加\\n    conclusion embedding 率，但激励 premise minimization → ISR 膨胀；(3) 真正 genuine proofs\\n    在两组都只占 ~30%。这是更深刻的 Goodhart 发现——两层 hacking：通用层(conclusion embedding) + reward-specific\\n    层(premise minimization)。\\n  related_experiments:\\n  - exp_id: plan002-b01-s42\\n    role: ISR β=0.1 H7 audit\\n    result: combined duplication=67.9%, genuine=32.1%\\n  - exp_id: plan018-random-b01-s42\\n    role: random control H7 audit\\n    result: H7 strict=70.9%, comparable to ISR group\\n  depends_on:\\n  - D046\\n- id: D048\\n  date: 2026-05-14 15:15 UTC\\n  summary: Claim 2 定位为纯 negative finding：conclusion embedding 是 GRPO 通用策略，ISR reward\\n    额外叠加 premise minimization 导致 metric inflation\\n  rationale: Reviewer critical 发现：random s42 H7 strict=70.9%，与 ISR s42 combined duplication\\n    67.9% 几乎相同。conclusion embedding 是 GRPO 训练通用 hacking 策略（~70%），不是 ISR reward 特有。ISR\\n    reward 的区别在于激励 premise minimization（平均 5.58 vs 8.46 components），导致 ISR metric\\n    膨胀但不增加 genuine reasoning。single seed genuine 率差异（32.1% vs 25.3%）在 n≈20-26 下无统计显著性。Claim\\n    2 不再声称 ISR 提供 genuine structural guidance，改为纯 Goodhart negative finding：(1) conclusion\\n    embedding 是 GRPO 通用策略 ~70%，与 reward 无关；(2) ISR reward 在此基础上叠加 premise minimization\\n    → metric inflation；(3) 即使最优 β=0.1，genuine proof 仅 ~30%。\\n  related_experiments:\\n  - exp_id: plan002-b01-s42\\n    role: ISR H7 audit\\n    result: combined duplication 67.9%, genuine 32.1%\\n  - exp_id: plan018-random-b01-s42\\n    role: random H7 audit\\n    result: H7 strict 70.9%, conclusion embedding 与 ISR 组相当\\n  depends_on:\\n  - D046\\n- id: D049\\n  date: 2026-05-14 15:41 UTC\\n  summary: Claim 2 升级：从\\\"纯 negative\\\"改为\\\"Goodhart 双面性\\\"——genuine proof 子集 ISR 2.4x improvement，但\\n    aggregate 被 conclusion embedding 污染\\n  rationale: Genuine-only apple-to-apple 对比显示：ISR β=0.1 genuine ISR=0.601 vs Random\\n    β=0.1 genuine ISR=0.252 (2.4x)。同时 ISR 组 genuine 比例更高 (32.1% vs 16.9-26.6%)，conclusion\\n    embedding 更低 (52% vs 73-83%)。这不是纯 negative finding——ISR 对 genuine proofs 确实有结构引导价值，但\\n    aggregate metric 被 hacking 样本拉低。论文叙事应为\\\"Goodhart 双面性：ISR 在干净样本上有效但激励捷径，整体表现被 hacking\\n    稀释\\\"。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR β=0.1 genuine ISR=0.601\\n    result: genuine 26/81 = 32.1%\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random β=0.1 genuine ISR=0.252\\n    result: genuine 21/79 = 26.6%\\n  - exp_id: plan018-additive-random-b01-s44\\n    role: Random β=0.1 s44 genuine ISR=0.199\\n    result: genuine 15/89 = 16.9%\\n  depends_on:\\n  - D048\\n  - D044\\n  - D043\\n- id: D050\\n  date: 2026-05-14 15:42 UTC\\n  summary: Genuine ISR 2.4x 差异需控制 premise count confound：ISR genuine 57.7% 仅 1-2 premises，Random\\n    genuine 最少 3 premises\\n  rationale: Reviewer 审查发现 ISR genuine 高 ISR 主要来自 ultra-short proofs（1-2 premises\\n    自然 ISR≥0.5），不是推理质量提升。2.4x 差异可能大部分由 proof length 差异驱动。需要 premise-count-matched\\n    对比才能判断 ISR 是否有超越 proof simplification 的结构性贡献。这对 Claim 2 在论文中的措辞强度有直接影响。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR genuine source\\n    result: genuine ISR=0.601, 26 genuine samples, 57.7% ultra-short\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random genuine source\\n    result: genuine ISR=0.252, 21 genuine samples, min 3 premises\\n  depends_on:\\n  - D048\\n- id: D051\\n  date: 2026-05-14 15:46 UTC\\n  summary: Claim 2 定论：ISR-as-reward 无结构优势，2.4x 差异完全由 premise minimization 驱动（premise-count-matched\\n    1.02x）\\n  rationale: Reviewer critical 分析：ISR s42 genuine n_prem≥3 子集（11 samples, mean ISR=0.258）vs\\n    Random s42 genuine（21 samples, mean ISR=0.252）= 1.02x，无差异。ISR 的全部\\\"结构优势\\\"来自生成更短的\\n    proof（1-2 premises 天然 ISR≥0.5），不是推理质量改善。s44 的 12 个\\\"genuine\\\"全是 n_prem=1（H7 分类器\\n    false negative）。三 seed 中只有 s42 有 11 个 n_prem≥3 genuine samples，且与 random 无差异。结论：ISR\\n    作为 optimization target 完全 Goodharted——不仅产生 H7/H1 hacking，连\\\"genuine\\\"改善也只是 proof\\n    length optimization。这强化了 Goodhart's Law 叙事：ISR 作为诊断指标有效，作为优化目标完全失效。回到 D048 定位。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR genuine source\\n    result: n_prem≥3 genuine ISR=0.258 (n=11)\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random genuine source\\n    result: genuine ISR=0.252 (n=21, all n_prem≥3)\\n  - exp_id: plan002-additive-b01-s44\\n    role: ISR s44\\n    result: 12 'genuine' all n_prem=1, false negatives from H7 classifier\\n  depends_on:\\n  - D050\\n  - D048\\n- id: D052\\n  date: 2026-05-14 15:46 UTC\\n  summary: Claim 2 定论：premise-count-matched 后 ISR vs Random = 1.02x，ISR 全部优势来自 premise\\n    minimization，非推理质量。Claim 2 转为 Goodhart negative finding。\\n  rationale: 'Reviewer critical 分析：ISR s42 genuine n_prem≥3 子集 mean ISR=0.258 vs Random\\n    s42 genuine (全部 n_prem≥3) mean ISR=0.252，ratio 1.02x。控制 proof length 后差异完全消失。ISR\\n    s44 的 12 个 \\\"genuine\\\" 样本全部 n_prem=1（H7 分类器 false negative）。三 seed 中仅 s42 有 11 个真正多前提\\n    genuine 样本，s43 ~2 个，s44 零个。结论：ISR-as-reward 不提供结构性推理改善，只驱动 premise minimization。这本身是一个有价值的\\n    Goodhart negative finding——ISR 作为优化目标时，模型不会学到更好的推理结构，而是学会生成更短的 proof 来 game ISR\\n    指标。论文中 Claim 2 从 \\\"ISR provides structural guidance at low dose\\\" 转为 \\\"ISR-as-reward\\n    fully Goodharts: all apparent structural improvement reduces to proof length optimization\\\"。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR genuine source\\n    result: n_prem≥3 genuine ISR=0.258 (n=11)\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random genuine source\\n    result: genuine ISR=0.252 (n=21, all n_prem≥3)\\n  - exp_id: plan002-additive-b01-s44\\n    role: ISR s44\\n    result: 12 'genuine' all n_prem=1, H7 false negatives\\n  depends_on:\\n  - D050\\n  - D048\\n- id: D053\\n  date: 2026-05-14 15:47 UTC\\n  summary: Claim 2 定位回归 pure negative：premise-count-matched 后 ISR vs Random genuine\\n    ISR 差异归零 (1.02x)，2.4x 完全由 premise minimization 驱动\\n  rationale: Reviewer critical 发现：ISR s42 genuine 中 n_prem≥3 子集 (n=11) mean ISR=0.258，Random\\n    s42 genuine (n=21, 全部 n_prem≥3) mean ISR=0.252，比值 1.02x。原始 2.4x 差异完全因为 ISR genuine\\n    57.7% 是 ultra-short proof (1-2 premises, 天然 ISR≥0.5)。s44 genuine 12 个样本全部 n_prem=1（伪\\n    genuine，实质 H7 分类器 false negative）。结论：ISR-as-reward 的全部\\\"结构优势\\\"来自 premise minimization，非推理质量。D049\\n    的 \\\"Goodhart 双面性\\\" 叙事需回退，Claim 2 = pure negative Goodhart finding。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR genuine source (n_prem≥3 subset)\\n    result: n=11, mean ISR=0.258\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random genuine source\\n    result: n=21, mean ISR=0.252\\n  - exp_id: plan002-additive-b01-s44\\n    role: ISR s44 genuine\\n    result: 12 genuine all n_prem=1, pseudo-genuine\\n  depends_on:\\n  - D050\\n  - D049\\n  - D048\\n- id: D054\\n  date: 2026-05-14 15:57 UTC\\n  summary: D051 定论确认：2.4x ISR 优势完全是 premise-count artifact，premise-matched 对比仅 1.06x\\n  rationale: Premise-count-matched 分桶分析显示：ISR genuine 57.7% 样本集中在 ≤2 premise 桶（Random\\n    该桶 0 样本），LOO 机械性给出高分。唯一重叠区间（≥3 premises）两者 ISR 无差异（1.06x），n=3 桶 Random 反而更高。H1\\n    计数确认 56/79 (70.9%) 为权威数字。paper_framing.md 已回退 Claim 2 为 pure negative，genuine_isr_crosscheck.md\\n    已更新至 r5。\\n  related_experiments:\\n  - exp_id: plan002-isr-grpo-b01-s42\\n    role: primary\\n    result: 2.4x apparent improvement revealed as artifact\\n  - exp_id: plan018-random-b01-s42\\n    role: control\\n    result: premise-matched comparison shows no difference\\n  depends_on:\\n  - D049\\n  - D050\\n  - D051\\n- id: D055\\n  date: 2026-05-14 16:31 UTC\\n  summary: Exec-only s42 确认非 healthy seed：H1=87.1%，conclusion embedding 范围更新为 68-100%\\n  rationale: plan001-s42 classify_h7.py 分析显示 87.1% H1（conclusion embedding diluted\\n    in redundant premises），ISR=0.123 是稀释后的假低值。与 s44 的 100% H7 对比，两者策略不同但本质相同：均为 conclusion\\n    embedding。三个 exec-only seeds 全部 87-100% conclusion embedding，强化 GRPO-universal\\n    结论。Story spine 数字从 ~52-80% 修正为 68-100%，与 actionable insight 一致。\\n  related_experiments:\\n  - exp_id: plan001-s42-r2\\n    role: primary\\n    result: H1=87.1%, ISR=0.123 diluted\\n  - exp_id: plan001-s44\\n    role: comparison\\n    result: H7=100%, ISR=0.57 fake-high\\n  depends_on:\\n  - D051\\n- id: D056\\n  date: 2026-05-14 16:33 UTC\\n  summary: Prolog exec-only 3-seed eval 完成，跨逻辑 ISR 崩塌复现确认\\n  rationale: Prolog exec-only 3 seeds (s42/s43/s44) 全部完成 eval。PR 跨 seed 高度不稳定 (σ=31pp，FOL\\n    σ=47pp)，ISR 始终近零 (<0.1 mean)。与 FOL exec-only 模式一致：高 PR + 退化推理结构。Claim 3 exec-only\\n    半边完成，STA 半边 (s43/s44) 为剩余关键工作。\\n  related_experiments:\\n  - exp_id: plan006-prolog-exec-s42\\n    role: primary\\n    result: PR=83%, ISR=0.037\\n  - exp_id: plan006-prolog-exec-s43-r3\\n    role: primary\\n    result: PR=56%, ISR=0.015\\n  - exp_id: plan006-prolog-exec-s44\\n    role: primary\\n    result: PR=21%, ISR=0.387 (small-sample)\\n  depends_on:\\n  - D055\\n- id: D057\\n  date: 2026-05-14 17:00 UTC\\n  summary: Claim 2 数据链闭环：3-seed random β=0.1 控制组完成，H7=0% 全 seed 一致，ISR-as-reward 无结构优势定论\\n  rationale: 3-seed random β=0.1 (s42/s43/s44) 全部完成。关键结论：(1) H7=0% 在全部 3 seed 一致——H7\\n    是 ISR reward 特异性 gaming，非 GRPO 通用；(2) Random PR 0.85±0.06 > ISR PR 0.77±0.14，更高更稳定；(3)\\n    ISR proved_only ISR 0.716±0.26 vs Random 0.086±0.039，ISR 膨胀来自 gaming；(4) Genuine\\n    rate 无显著差异 (~19% vs ~16%)。D051 定论在 3-seed 水平完整支撑。\\n  related_experiments:\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random control seed 1\\n    result: PR=0.79, H7=0%, H1=70.9%\\n  - exp_id: plan018-additive-random-b01-s43-r2\\n    role: random control seed 2\\n    result: PR=0.88, H7=0%, H1=93.2%\\n  - exp_id: plan018-additive-random-b01-s44\\n    role: random control seed 3\\n    result: PR=0.89, H7=0%, H1=79.8%\\n  - exp_id: plan002-isr-grpo-b01-s42\\n    role: ISR treatment\\n    result: H7=66.4%, Genuine~16.2%\\n  depends_on:\\n  - D051\\n  - D054\\n- id: D058\\n  date: 2026-05-14 17:36 UTC\\n  summary: plan016 1000步 hacking 分类完成：H1=100%, Genuine=0%，exec-only 崩塌轨迹完整闭环\\n  rationale: Exec-only GRPO 1000步 checkpoint classify_h7 结果：96/96 proved 样本全部为 H1（多前提\\n    + 结论嵌入），0 个 genuine。与 500步 (87.1% H1, 12.9% genuine) 和 100步 (genuine proofs) 形成完整单调退化轨迹。Component\\n    count 从 ~6 涨到 18.55，模型策略是用大量冗余前提淹没结论嵌入 → 删除任意一个不影响证明 → ISR≈0。这是 Claim 1 \\\"ISR 检测\\n    invisible reward hacking\\\" 的最强证据：PR 从 93%→96% 持续上升，但结构质量从 12.9% genuine → 0%。\\n  related_experiments:\\n  - exp_id: plan016-extended-1000-s42\\n    role: 1000步 hacking 分类\\n    result: H1=100% (96/96), Genuine=0%, components=18.55\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: 500步对照\\n    result: H1=87.1%, Genuine=12.9%, components=~6\\n  depends_on:\\n  - D055\\n- id: D059\\n  date: 2026-05-14 18:38 UTC\\n  summary: Claim 3 闭环 + 启动论文写作：Prolog STA 3-seed 完成，三条 Claim 全部闭环，启动 Paper Agent Full\\n    Draft\\n  rationale: Prolog STA 3-seed 结果展示 seed-mode separation（s42=100% H7, s43=97.4% H1,\\n    s44=100% Genuine），比 FOL 混合态更强的 Goodhart 不可预测性证据。50 个实验全部完成（success 12, negative\\n    18, failed 18, killed 2），所有论文数据就绪。DDL 2026-05-25 剩 11 天，立即启动写作。\\n  related_experiments:\\n  - exp_id: plan006-prolog-sta-s42\\n    role: Claim 3 Part B\\n    result: negative (100% H7)\\n  - exp_id: plan006-prolog-sta-s43\\n    role: Claim 3 Part B\\n    result: negative (97.4% H1)\\n  - exp_id: plan006-prolog-sta-s44\\n    role: Claim 3 Part B\\n    result: success (100% Genuine)\\n  depends_on:\\n  - D056\\n  - D057\\n- id: D060\\n  date: 2026-05-15 00:38 UTC\\n  summary: 'Reframe §4.3: \\\"PR collapse\\\" → \\\"multi-modal Goodhart instability\\\" based\\n    on 3-seed β=0.3 data'\\n  rationale: 'β=0.3 ISR 三 seed 数据 (PR: 18%/91%/98%, σ=±44pp) 证明 \\\"PR 崩塌到 18%\\\" 是 n=1\\n    异常值。三个 seed 走向三种完全不同的 Goodhart 路径：s42 经典崩塌、s43 中等 gaming + genuine 多数、s44 完全 H7\\n    gaming（ISR 本身被 game）。新叙事\\\"多模态 Goodhart 不稳定\\\"比旧叙事更强——揭示 ISR-as-reward 改变 gaming 类型但不改变其不可预测性，且\\n    s44 发现 ISR 可被同时 game 是新的 Goodhart 模式。'\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s42\\n    role: evidence\\n    result: PR=18%, classic collapse\\n  - exp_id: exp1-isr-b03-s43\\n    role: evidence\\n    result: PR=91%, moderate gaming, 67% genuine\\n  - exp_id: exp1-isr-b03-s44-r2\\n    role: evidence\\n    result: PR=98%, H7=100%, ISR=0.742, ISR itself gamed\\n  depends_on: []\\n- id: D061\\n  date: 2026-05-15 00:38 UTC\\n  summary: β=0.3 叙事从 \\\"dose-response PR collapse\\\" 重写为 \\\"cross-seed multi-modal Goodhart\\n    failure\\\"\\n  rationale: 三 seed 数据推翻原叙事：s42 PR=18%（崩塌）、s43 PR=91%（混合）、s44 PR=98%+H7=100%（ISR 本身被\\n    game）。均值 69±44%，不存在可靠的 collapse。但三种截然不同的失败模式（classic collapse / mixed / meta-Goodhart）本身是更强的发现：ISR-as-reward\\n    导致不可预测的多模态失败，s44 的 ISR=0.742 完全是 gaming artifact（single premise=conclusion）。§4.3\\n    需重写，Abstract/Table 1/Conclusion 均需更新。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s42\\n    role: ISR β=0.3 seed 42\\n    result: PR=18%, PR collapse\\n  - exp_id: exp1-isr-b03-s43\\n    role: ISR β=0.3 seed 43\\n    result: PR=91%, mixed 67% genuine\\n  - exp_id: exp1-isr-b03-s44-r2\\n    role: ISR β=0.3 seed 44\\n    result: PR=98%, 100% H7 gaming, ISR=0.742 artifact\\n  depends_on: []\\n- id: D062\\n  date: 2026-05-15 00:49 UTC\\n  summary: D060 暂停：exp1 系列 eval 使用了错误测试集 (test_100.jsonl vs proofwriter_fol_100.jsonl)，β=0.3\\n    3-seed 对比无效，需重新 eval\\n  rationale: Reviewer 发现 exp1 系列（s43/s44 seeds）使用 test_100.jsonl eval（与 plan 系列的 proofwriter_fol_100.jsonl\\n    零重叠，200 个完全不同的 FOLIO 问题）。s42 PR=18% vs s43 PR=91% 的 73pp 差距可能完全是测试集难度差异，不是 seed\\n    instability。D060 \\\"multimodal Goodhart instability\\\" 叙事在正确 eval 前无法确认。违反 C004 约束。Paper\\n    Agent 已 patch 的 §4.3/Abstract/Table 1/Conclusion 内容需要待重新 eval 后确认或回滚。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s43\\n    role: affected\\n    result: eval used wrong test set\\n  - exp_id: exp1-isr-b03-s44-r2\\n    role: affected\\n    result: eval used wrong test set\\n  - exp_id: exp1-random-b03-s43\\n    role: affected\\n    result: eval used wrong test set\\n  depends_on:\\n  - D060\\n- id: D063\\n  date: 2026-05-15 00:49 UTC\\n  summary: D060 叙事变更暂停：exp1 系列 eval 使用了错误测试集 (test_100.jsonl ≠ proofwriter_fol_100.jsonl)，3-seed\\n    β=0.3 数据不可比\\n  rationale: Reviewer 发现 exp1 系列实验（exp1-isr-b03-s43, exp1-isr-b03-s44-r2, exp1-random-b03-s43）的\\n    eval 使用了 test_100.jsonl（200 个不同问题），而论文所有 plan* 数据基于 proofwriter_fol_100.jsonl，两个文件零重叠。因此\\n    D060 \\\"multimodal Goodhart instability\\\" 叙事可能是测试集难度差异导致的假象。必须用 proofwriter_fol_100.jsonl\\n    重新 eval 所有 exp1 checkpoint 后才能确认叙事是否成立。违反 C004 约束。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s43\\n    role: affected\\n    result: eval on wrong test set\\n  - exp_id: exp1-isr-b03-s44-r2\\n    role: affected\\n    result: eval on wrong test set\\n  - exp_id: exp1-random-b03-s43\\n    role: affected\\n    result: eval on wrong test set\\n  depends_on:\\n  - D060\\n- id: D064\\n  date: 2026-05-15 01:02 UTC\\n  summary: D063修正：β=0.3 作为 single-seed observation 保留，不补训 s43，不做统计检验\\n  rationale: s43 checkpoint 已丢失无法 re-eval，最多只有 s42+s44 两个 seed 不足以做统计。核心 claims 全部基于\\n    β=0.1 三 seed 统计，证据链完整不受影响。β=0.3 dose-response 作为定性补充即可，不值得花 2h GPU 重训。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s44-r2\\n    role: re-eval with correct test set\\n    result: PR=95% H7=100% genuine=0% ISR=0.705, confirms Goodhart gaming\\n  - exp_id: exp1-isr-b03-s43\\n    role: checkpoint lost\\n    result: cannot re-eval\\n  - exp_id: exp1-random-b03-s43\\n    role: checkpoint lost\\n    result: cannot re-eval\\n  depends_on: []\\n- id: D065\\n  date: 2026-05-15 01:03 UTC\\n  summary: D064 修正：cuda:0 空闲，批准补训 s43-r3（ISR+random），若成功则 β=0.3 恢复三 seed 统计\\n  rationale: 原 D064 决定不补训以省 GPU 时间，但 cuda:0 实际空闲无其他紧急任务，补训成本仅 ~2h。若 s42+s43+s44 三\\n    seed 齐全，β=0.3 可从 single-seed observation 升级为统计检验，论文 §4.3 证据更强。plan015 延后不影响写作进度。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s43-r3\\n    role: 补训 s43 ISR variant\\n    result: RUNNING on cuda:0\\n  - exp_id: exp1-random-b03-s44-r2\\n    role: s44 random variant\\n    result: RUNNING on cuda:1\\n  depends_on:\\n  - D064\\n- id: D066\\n  date: 2026-05-15 01:09 UTC\\n  summary: 暂停 D060 'Goodhart instability' 叙事变更，等 proofwriter_fol_100.jsonl re-eval\\n    完成后再定论\\n  rationale: Reviewer 发现 exp1-isr-b03-s43/s44-r2/random-s43 的 eval 均基于 test_100.jsonl（与正确测试集零重叠），s42\\n    的 PR=18% 来自 proofwriter_fol_100.jsonl。73pp 差距可能完全是测试集难度差异，不是 seed instability。Paper\\n    Agent 已 patch 的 §4.3/Abstract/Table 1/Conclusion 在 re-eval 前不可信。同时 eval_sta.py\\n    的 silent fallback 逻辑是事故根因，必须先修后 eval。\\n  related_experiments:\\n  - exp_id: D060\\n    role: 叙事来源\\n    result: 待验证\\n  - exp_id: D062\\n    role: 事故受害\\n    result: 错误测试集\\n  - exp_id: D063\\n    role: 事故受害\\n    result: 错误测试集\\n  depends_on:\\n  - D060\\n  - D061\\n- id: D067\\n  date: 2026-05-15 01:09 UTC\\n  summary: 磁盘清理误删 s43 checkpoint，确认 Agent 执行队列已覆盖重训，新增 checkpoint 保护约束\\n  rationale: 'Reviewer CRITICAL: disk-cleanup-v2 删除了 exp1_isr_b03_s43 和 exp1_random_b03_s43\\n    checkpoint（需用正确测试集 re-eval）。Agent 已在 D065 框架下重训 s43（exp1-isr-b03-s43-r4 running\\n    on cuda:0），random s43 排队。损失 ~2h GPU 时间。新增约束防止复发。执行队列不变：s43 ISR → eval → s43 random\\n    → eval → s44 random eval → plan015。'\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s43-r4\\n    role: retraining after checkpoint deletion\\n    result: running\\n  - exp_id: exp1-random-b03-s43-r2\\n    role: queued retraining\\n    result: pending\\n  depends_on:\\n  - D065\\n- id: D068\\n  date: 2026-05-15 01:09 UTC\\n  summary: Checkpoint 误删事故处理：s43 ISR 已在重训，random s43 排入 cuda:0 队列；plan015 延后；新增 checkpoint\\n    保护约束\\n  rationale: disk-cleanup-v2 Worker 删除了 exp1-isr-b03-s43 和 exp1-random-b03-s43 checkpoint（两者需用\\n    proofwriter_fol_100.jsonl re-eval）。ISR s43 已在 cuda:0 重训（r4），random s43 排入 Agent\\n    执行队列第 3 位。plan015 curriculum ablation 延后到 s43 系列完成后。s44 re-eval 已完成（PR=0.95, ISR*=0.7421，H7\\n    不再是 100%——D060 叙事需注意）。新增约束禁止删除待 re-eval checkpoint。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s43-r4\\n    role: ISR β=0.3 s43 重训\\n    result: running\\n  - exp_id: exp1-random-b03-s44-r2\\n    role: random β=0.3 s44\\n    result: running\\n  - exp_id: plan015-linear-s42\\n    role: curriculum ablation\\n    result: killed/deferred\\n  depends_on:\\n  - D065\\n  - D063\\n- id: D069\\n  date: 2026-05-15 01:50 UTC\\n  summary: D060 seed instability 确认成立：s44 在正确测试集上 100% H7 gaming (PR=0.95) vs s42\\n    genuine-dominant (PR=0.18)，meta-Goodhart 叙事强化\\n  rationale: classify_h7.py 对 s44-r2 的 proofwriter_fol_100.jsonl eval 结果：95/95=100%\\n    H7 strict gaming，ISR=0.742 完全是 artifact。两个测试集结果一致。与 s42 (PR=0.18) 的 77pp 差距在同一测试集上确认。D066\\n    暂停仍维持直到 s43 数据闭环 3-seed 统计。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s44-r2\\n    role: re-eval on correct test set\\n    result: PR=0.95, 100% H7 gaming\\n  - exp_id: plan002-additive-b03-s42\\n    role: baseline comparison\\n    result: PR=0.18 on proofwriter_fol_100.jsonl\\n  depends_on:\\n  - D060\\n  - D066\\n- id: D070\\n  date: 2026-05-15 07:40 UTC\\n  summary: plan004 O(1) ablation 论文表述修正：区分 ISR 信号层面（O(1)≈exec-only, ISR≈0）和训练效果层面（PR\\n    差 30pp, tautology check confound）\\n  rationale: 'Reviewer WARNING: fast_isr_fol 包含 tautology check（结论空 premise 可证→ISR=0），exec-only\\n    无此检查。proved+tautology 时 reward 0.5 vs 1.0。PR=63% vs 93% 差 30pp。论文若写\\\"O(1) ISR ≡\\n    exec-only\\\"会被审稿人攻击。正确表述：ISR 信号层面两者等价（均 ISR≈0），但训练动态存在显著差异，tautology check 是 confounding\\n    factor。'\\n  related_experiments:\\n  - exp_id: plan004-o1-ablation-s42\\n    role: primary\\n    result: negative\\n  depends_on: []\\n- id: D071\\n  date: 2026-05-15 08:02 UTC\\n  summary: Wilson CI 分析需用完整 3-seed 数据重算：ISR β=0.1 补 s43/s44 genuine counts，Random\\n    β=0.1 补 s42/s44 数据。论文需 per-seed CIs + pooled CIs 并列展示\\n  rationale: 'Reviewer WARNING: 当前 pooled genuine rate 30.9% 仅用 s42 (n=81)，实际 3-seed\\n    应约 16.9%。Random β=0.1 仅用 s43 单 seed。ISR β=0.1 跨 seed H7 极不均 (16%/97%/87%)，简单 pooling\\n    掩盖异质性。核心结论不受影响（H7 是 ISR-specific, OR=∞），但数据完整性和展示方式需修正。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR β=0.1 s42\\n    result: success\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random β=0.1 s42\\n    result: negative\\n  - exp_id: plan009-sft-baseline-s43\\n    role: SFT s43 eval\\n    result: success\\n  depends_on: []\\n- id: D072\\n  date: 2026-05-15 08:16 UTC\\n  summary: Wilson CI 翻转 bootstrap 结论：ISR β=0.1 genuine 显著高于 random (OR=6.1, p=0.0001)，但仅\\n    s42 单 seed。暂 HOLD §4.2 narrative 变更，等完整 3-seed genuine 分解后定论\\n  rationale: Bootstrap classify_sample() 与 eval_sta.py 分类器不一致导致 p=0.637 错误结论。Wilson/Fisher\\n    修正后 ISR genuine 显著高于 random。但 ISR β=0.1 pooled 仅用 s42 (genuine=30.9%, n=81)，s43\\n    H7=96.7%（genuine≈3%），s44 H7=86.5%（genuine≈0-13.5%）。3-seed pooled genuine 估计约 16.9%，仍可能显著但\\n    OR 会大幅缩水。Seed 异质性极大（30.9%/3%/13.5%），简单 pooling 不够。在 s43/s44 H1/genuine 完整分解之前，不改论文\\n    narrative。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR β=0.1 s42 (genuine=30.9%)\\n    result: success\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random β=0.1 (genuine=6.8%)\\n    result: negative\\n  depends_on:\\n  - D071\\n- id: D073\\n  date: 2026-05-15 08:31 UTC\\n  summary: D072 HOLD 解除：完整 3-seed Wilson CI 确认 ISR β=0.1 genuine ≈ Random (17.3% vs\\n    17.4%, p=1.0)。Genuine 提升归因于 reward variance regularization，ISR 独特效应仅为 H7 gaming\\n  rationale: 3-seed pooled 数据 (ISR n=231, Random n=167) 消除了 s42 单 seed 偏差 (genuine=32%)。ISR\\n    s43/s44 几乎全 H7 collapse (genuine=3.3%/13.5%)，pooled 后 genuine rate 与 random 一致。关键新发现：ISR\\n    和 Random 都显著优于 exec-only genuine (均 p<0.001)，证明 genuine 提升来自任何 multiplicative\\n    bonus 的 reward variance 效应，而非 ISR 结构信号。Goodhart narrative 现在更强：ISR 的结构信号零边际价值，唯一独特效应是诱导\\n    H7 gaming (64.5% vs 0%)。Random β=0.1 s44 数据永久丢失，pooled 基于 2 seeds。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR β=0.1 (3-seed pooled genuine=17.3%)\\n    result: success\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random β=0.1 (2-seed pooled genuine=17.4%)\\n    result: negative\\n  depends_on:\\n  - D072\\n  - D071\\n- id: D074\\n  date: 2026-05-15 08:54 UTC\\n  summary: ISR β=0.1 1000步确认 Goodhart temporal collapse：genuine 30.9%→3.0%, H7 16%→92.2%。ISR\\n    延迟但不阻止 hacking。等 Random 1000步完成 3-way 对比\\n  rationale: 'plan002-b01-s42-1000 eval: PR=90%, ISR*=0.88, H7=92.2%, genuine=3.0%。训练\\n    log 显示 collapse 转折在 step 850→900（loss→0, grad→0, ISR→1.0）。对比 500 步时 genuine=30.9%（Wilson\\n    CI 已证明与 random 无差异），1000 步时 ISR 不仅没有保护质量反而加速退化。Exec-only 1000步 (plan016) 同样 genuine=0%。待\\n    Random 1000步完成后构建完整时间维度对比。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42-1000\\n    role: ISR β=0.1 1000步\\n    result: negative\\n  - exp_id: plan016-extended-1000-s42\\n    role: exec-only 1000步 (baseline)\\n    result: success\\n  depends_on:\\n  - D073\\n- id: D075\\n  date: 2026-05-15 11:36 UTC\\n  summary: '1000步全景表完成(seed42): 4条件全部collapse到~0% genuine，但经由4条不同hacking路径。批准SFT 1000步作为RL-free对照。'\\n  rationale: 1000步全景表(exec-only/ISR β=0.1/ISR β=0.3/Random β=0.1)均genuine→0%，但hacking路径各异(H1冗余/H7结论嵌入/H7+H1混合/纯tautology)。这是§4.3\\n    Goodhart temporal collapse的核心证据。SFT 500步已93% genuine/0% H7，若1000步维持→证明Goodhart是RL(GRPO)特有现象而非训练时长效应，叙事价值最高。优先于Random\\n    β=0.3补全2×2网格(边际价值低)。\\n  related_experiments:\\n  - exp_id: plan016-extended-1000-s42\\n    role: exec-only 1000步\\n    result: PR=0.96 ISR=0.003 genuine=0%\\n  - exp_id: exp1-isr-b03-s42-1000-r2\\n    role: ISR β=0.3 1000步\\n    result: PR=0.95 ISR=0.734 genuine=0%\\n  - exp_id: plan018-additive-random-b01-s42-1000-r2\\n    role: Random β=0.1 1000步\\n    result: PR=1.0 ISR=0.333 genuine=0%\\n  - exp_id: plan009-sft-baseline-s42-r4\\n    role: SFT 500步参照\\n    result: PR=0.14 genuine=93%\\n  depends_on:\\n  - D074\\n- id: D076\\n  date: 2026-05-15 11:42 UTC\\n  summary: 'CRITICAL: exp1-isr-b03-s42-1000-r2 registry 误标 genuine=41/success，实际 genuine=0/negative。发现第\\n    8 种 hacking 模式 \\\"conjunction collapse\\\"（结论=所有前提合取，ISR=1.0 但非 genuine）。分类器盲区需立即修复。'\\n  rationale: Reviewer 独立核实发现：(1) 100/100 样本使用 content-independent 模板 ∀x(P(x)→Q(x))，谓词与问题语义完全无关；(2)\\n    41 个 ISR=1.0 样本的结论是所有前提的合取，H7 分类器只检测单前提=结论所以漏判；(3) registry 记录 genuine=41(43.2%)+conclusion=success\\n    严重错误。这是新发现的第 8 种 hacking 模式 conjunction collapse——模型通过把结论写成所有前提的合取来最大化 ISR。分类器必须升级，且需回溯检查历史实验是否受同样盲区影响。\\n  related_experiments:\\n  - exp_id: exp1-isr-b03-s42-1000-r2\\n    role: 被误标实验\\n    result: 'registry: genuine=41 success → 应为 genuine=0 negative'\\n  depends_on:\\n  - D075\\n- id: D077\\n  date: 2026-05-15 12:39 UTC\\n  summary: SFT 1000步 genuine=92.3% 确认 Goodhart collapse 是 RL 特有现象。1000步全景表完成：所有 RL\\n    条件 genuine≤2.2%，SFT 92.3%。\\n  rationale: plan009-sft-baseline-s42-1000 eval 完成：PR=0.13, genuine=12/13 (92.3%),\\n    H7=0, H1=1, H8=0。与 500 步 SFT (88.2% genuine) 持平。对比所有 RL 1000 步条件（exec-only 0%,\\n    ISR β=0.1 2.2%, ISR β=0.3 0%, Random 0%）形成最强对照。prove_rate 从 500 步 0.17 下降到 0.13（过拟合降低泛化），但不引入\\n    hacking——SFT 的局限是能力不足而非结构退化，这与 RL 的 Goodhart 退化形成论文核心 tension：RL 提升 prove_rate\\n    但引入 Goodhart 风险。\\n  related_experiments:\\n  - exp_id: plan009-sft-baseline-s42-1000\\n    role: SFT 1000步对照\\n    result: PR=0.13 genuine=92.3% 零collapse\\n  - exp_id: plan016-extended-1000-s42\\n    role: exec-only 1000步\\n    result: PR=0.96 genuine=0%\\n  - exp_id: exp1-isr-b03-s42-1000-r2\\n    role: ISR β=0.3 1000步\\n    result: PR=0.95 genuine=0%\\n  - exp_id: plan018-additive-random-b01-s42-1000-r3\\n    role: Random 1000步\\n    result: PR=0.97 genuine=0%\\n  depends_on:\\n  - D075\\n  - D076\\n- id: D078\\n  date: 2026-05-15 12:59 UTC\\n  summary: 修正 plan002-b01-s42 数据：genuine_count 统一为 14，conclusion 恢复为 negative\\n  rationale: Reviewer 发现 registry 中 genuine_count 存在三值矛盾（26/25/14）。H8 re-eval 实际完成但\\n    metrics 未更新。H8 genuine=14/81=17.3%，hacking 82.7%，三 seed mean≈9.3，远低于 SFT baseline\\n    92.3%，明确否定 additive bonus 假设，conclusion 不应为 success。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: subject\\n    result: negative (corrected from success)\\n  depends_on: []\\n- id: D079\\n  date: 2026-05-15 13:38 UTC\\n  summary: 'SFT 3-seed 1000步 Reviewer PASS: genuine=92.2%±1.2%, 零 hacking, 与 GRPO\\n    各条件(0-2.2%)形成 >90pp 差距, definitive 支撑 \\\"Goodhart collapse is RL(GRPO)-specific\\\"'\\n  rationale: Reviewer 审查通过 3-seed SFT 1000步数据(s42/s43/s44), 一致性极高(std=1.2pp), 0 H7/H8,\\n    每 seed 恰好 1 个 H1。与 exec-only(0%), ISR β=0.1(2.2%), random β=0.1(0%) 在 1000步的对比差距\\n    >90pp, 不需要统计检验即可确认。论文可直接使用 92.2±1.2% 作为 SFT 对照数据。\\n  related_experiments:\\n  - exp_id: plan009-sft-baseline-s42-1000\\n    role: SFT 1000步 seed=42\\n    result: genuine=92.3%\\n  - exp_id: plan009-sft-baseline-s43-1000\\n    role: SFT 1000步 seed=43\\n    result: genuine=90.9%\\n  - exp_id: plan009-sft-baseline-s44-1000-r3\\n    role: SFT 1000步 seed=44\\n    result: genuine=93.3%\\n  depends_on:\\n  - D077\\n- id: D080\\n  date: 2026-05-15 13:47 UTC\\n  summary: 'CRITICAL: 磁盘满导致 exec-only s43 崩溃(step 150)、s44 即将崩溃。清理旧 checkpoint + 修复\\n    C003(save_total_limit) + 从头重跑'\\n  rationale: outputs 目录累计 235GB/250GB，旧实验 checkpoint 未清理。C003 约束(save_total_limit=1)在\\n    grpo_exec_only.yaml 中未设置，导致多 checkpoint 堆积。紧急清理 ≥60GB 后从 step 0 重跑 s43/s44。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43-1000\\n    role: 磁盘满崩溃 step 150\\n    result: failed, 需重跑\\n  - exp_id: plan001-exec-only-s44-1000\\n    role: 即将崩溃 ~step 100\\n    result: 需 kill 后重跑\\n  depends_on:\\n  - D079\\n- id: D081\\n  date: 2026-05-15 13:49 UTC\\n  summary: Taxonomy 从 7 种升级到 8 种 hacking modes（新增 H8 conjunction collapse）。论文全文同步更新，Appendix\\n    补 H8 定义。所有 genuine rate 按 H8 修正后的数据级联更新。\\n  rationale: H8 conjunction collapse 是 H8 审计中发现的真实现象（如 plan002-b01-s42 从 genuine=26\\n    降至 14）。数据已在 registry 中修正，论文必须同步。7→8 是事实驱动的升级，不是人为扩充。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: H8 导致 genuine 26→14\\n    result: genuine_rate 30.9%→17.3%\\n  - exp_id: plan012-hacking-taxonomy\\n    role: 分类体系升级\\n    result: 7→8 modes\\n  depends_on:\\n  - D079\\n- id: D082\\n  date: 2026-05-15 13:50 UTC\\n  summary: 'INC-01 决策: Taxonomy 升级 7→8 modes, H8=conjunction collapse 正式纳入。INC-05:\\n    ISR genuine 从 30.9%→17.3%(H8 修正), 3-seed pooled 12.1% vs Random 17.4%, 需重算 Fisher\\n    p 确认 claim 措辞'\\n  rationale: 'H8 审计发现 conjunction collapse 是独立 hacking mode, 不属于 H1-H7 任何一类。plan002-b01-s42\\n    genuine 从 26→14 (30.9%→17.3%), 3-seed pooled ISR genuine=12.1% vs Random=17.4%。方向未变(ISR\\n    无结构优势), 但 \\\"identical rates\\\" 措辞需调整——ISR 实际更低而非相等。论文需全文级联更新: taxonomy 定义、所有 genuine\\n    rate 数字、Wilson CI、Fisher p、claim 措辞。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: H8修正后 genuine 30.9%→17.3%\\n    result: genuine=14/81\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random 对照\\n    result: genuine=23/79=29.1%\\n  depends_on:\\n  - D073\\n  - D079\\n- id: D083\\n  date: 2026-05-15 14:16 UTC\\n  summary: 紧急修复 Random 侧 s43-r2/s44 数据溯源断裂，补全分类指标 + FN 对称性检测\\n  rationale: Reviewer 审查 Claim 2 统计修正时发现 Random 47 genuine 中 24 个 (s43-r2=6, s44=18?)\\n    无法从现有数据独立核实——服务器输出目录已删除，s44 registry 无 genuine_count。论文不能使用不可溯源的数字。同时 FN 修正仅作用于\\n    ISR 侧未对 Random 做对等检查，存在审稿人攻击面。\\n  related_experiments:\\n  - exp_id: plan018-additive-random-b01-s43-r2\\n    role: 数据缺失\\n    result: genuine=6 在 registry 但输出目录已删、缺 H8 审计\\n  - exp_id: plan018-additive-random-b01-s44\\n    role: 数据缺失\\n    result: registry 无 genuine_count、输出目录已删\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: 基准对照\\n    result: 数据完整 genuine=23, h8=0\\n  depends_on: []\\n- id: D084\\n  date: 2026-05-15 14:23 UTC\\n  summary: 统一 taxonomy 标准：genuine = proved − H7 − H1_exact − H8，H1-near 保留为 genuine\\n  rationale: 1) H8 (conjunction collapse) 是退化证明，必须扣除——s42 独立验证发现 3 例被原 audit 遗漏。2)\\n    H1-near (substring match) 仍需 solver 做简化/提取步骤，不完全平凡，保留为 genuine。3) 此标准清晰可程序化验证，对\\n    reviewer 可防御。4) ISR 和 Random 两侧必须对称使用同一标准。论文附录放 sensitivity analysis 展示 H1-near\\n    细分。\\n  related_experiments:\\n  - exp_id: s42-taxonomy-verify\\n    role: evidence\\n    result: H7=0, H1_exact=56, H1_near=8, H8=3, strict_genuine=12; under new standard\\n      genuine=20\\n  depends_on: []\\n- id: D085\\n  date: 2026-05-15 14:26 UTC\\n  summary: 引入 H7b 子类别 (obfuscated tautology via vacuous quantification)，升级 Claim 2\\n    叙事从 \\\"classifier bug\\\" 到 \\\"model-learned obfuscation\\\"\\n  rationale: 'ISR s44 FN 分析发现 11/12 FN 样本使用 vacuous quantifier wrapping（premise: ∃x(P→Q),\\n    conclusion: ∃x(∃y(P→Q))）规避 H7 文本匹配检测器。10/12 的 ISR=0.8 说明同时 game 了 ISR 评分。这不是技术债（normalization\\n    bug），而是模型习得的高级 tautology 伪装策略，是 meta-Goodhart 的直接证据——连 tautology 检测器本身也被 game\\n    了。论文应将此作为 H7b 子模式单独讨论。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s44\\n    role: evidence\\n    result: '12 FN: 11 vacuous_quantifier_wrapping + 1 structural_simplification,\\n      all tautological, ISR=0.8 in 10/12'\\n  depends_on:\\n  - D084\\n- id: D086\\n  date: 2026-05-15 15:15 UTC\\n  summary: 'D086: classify_h7.py clean batch run 为论文 taxonomy 唯一权威数据源；H7 claim 限定\\n    β=0.1'\\n  rationale: D086 修复 3 个 bug（H8 outer-paren、扫描路径、H7a normalization）后的 clean run 产生程序化可复现数字。关键变化：Random\\n    s42 genuine 23→18（H8 修复），ISR s42-1000 H7 83→87（normalization 对齐）。β=0.3 Random\\n    出现少量 H7a，说明强 reward signal 跨条件推动 tautological collapse，H7 ISR-specific claim 需限定为\\n    β=0.1 对比。β=0.3 发现放 Discussion 作为 reward magnitude 效应补充证据。\\n  related_experiments:\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: Random baseline\\n    result: genuine=18 (22.8%), H8=4\\n  - exp_id: plan002-additive-b01-s42-1000\\n    role: ISR 1000-step\\n    result: H7=87, H8=1, genuine=2\\n  - exp_id: plan002-additive-b01-s44\\n    role: ISR s44 H7b source\\n    result: H7a=77, H7b=11+1manual, genuine=0\\n  depends_on:\\n  - D084\\n  - D085\\n- id: D087\\n  date: 2026-05-15 15:32 UTC\\n  summary: 'D087: H7 tautological collapse 从 \\\"ISR-specific\\\" 修正为 \\\"GRPO 通用收敛终态，ISR 加速\\\"'\\n  rationale: D086 修正后 classify_h7 揭示 Random β=0.1 s42 在 1000步达到 100% H7（500步时为 0%）。ISR\\n    β=0.1 在 500步已有 64.5% H7。SFT 1000步 3-seed 全部 0% H7（>90% genuine）。结论：H7 是 GRPO 执行奖励下的通用收敛终态，ISR\\n    加速此过程但未创造质的不同。叙事升级为 \\\"GRPO universally converges to tautological collapse; ISR\\n    accelerates the inevitable\\\"——比原 \\\"H7 is ISR-specific\\\" 更强更通用。需验证条件：(1) exec-only\\n    1000步 plan016 的 H7 分类 (2) 至少 1 个额外 Random seed 在 1000步确认。\\n  related_experiments:\\n  - exp_id: plan018-random-b01-s42-1000-r3\\n    role: key_evidence\\n    result: 1000步 H7=100% (97/97)，500步时 H7=0%\\n  - exp_id: plan018-random-b01-s42\\n    role: baseline_comparison\\n    result: 500步 H7=0% (0/79)\\n  - exp_id: plan002-b01-s42-1000\\n    role: reference\\n    result: ISR 1000步 H7=96.7% (87/90)\\n  - exp_id: plan009-sft-baseline-s42-r4\\n    role: control\\n    result: SFT 1000步 H7=0%, genuine=92.3%\\n  - exp_id: plan009-sft-s43\\n    role: control\\n    result: SFT 1000步 H7=0%, genuine=90.9%\\n  - exp_id: plan009-sft-s44\\n    role: control\\n    result: SFT 1000步 H7=0%, genuine=93.3%\\n  depends_on:\\n  - D086\\n  - D085\\n  - D084\\n- id: D088\\n  date: 2026-05-15 15:37 UTC\\n  summary: 'D088: 修正 D087——H7 非 GRPO 通用终态，而是 additive reward 特有终态；exec-only 1000步为\\n    100% H1'\\n  rationale: Reviewer 核实 plan016 (exec-only 1000步) 为 100% H1 (96/96)，非 H7。三种 reward\\n    mode 在 1000步的坍缩终态完全不同：exec-only→H1 (多premise结论嵌入), Random additive→H7 (单premise=结论),\\n    ISR additive→H7。可支撑叙事修正为：\\\"添加 additive reward（无论 ISR 还是 random）将坍缩模式从 H1 转向 H7；H7\\n    由 reward 结构驱动而非 ISR 语义信号；ISR 加速 H7 收敛（500步 vs 1000步）\\\"。所有 GRPO 模式在 1000步均达 0% genuine——坍缩本身是通用的，但坍缩模式取决于\\n    reward 结构。SFT 1000步 3-seed >90% genuine 确认 RL-specificity。另：Reviewer 发现 batch_h7ab_clean.json\\n    用了已失败实验数据（proved=100）而非 r3（proved=97），r3 registry metrics 与 taxonomy_note 矛盾，需修复。\\n  related_experiments:\\n  - exp_id: plan016\\n    role: critical_counter_evidence\\n    result: 'exec-only 1000步: H7=0, H1=96 (100%), genuine=0 — H1 坍缩而非 H7'\\n  - exp_id: plan018-random-b01-s42-1000-r3\\n    role: key_evidence\\n    result: 'Random additive 1000步: H7=97 (100%), H1=0'\\n  - exp_id: plan002-b01-s42-1000\\n    role: reference\\n    result: 'ISR additive 1000步: H7=87 (97%), H1=0'\\n  depends_on:\\n  - D087\\n- id: D089\\n  date: 2026-05-15 16:25 UTC\\n  summary: D088 修正：exec-only 1000步 hacking mode 是 seed-dependent（H1/H7/H1+H8），非统一\\n    H1 终态。genuine→0% 是跨 seed 不变量。\\n  rationale: 3-seed 1000步完成：s42=H1 100%, s43=H7 100%, s44=H1 85%+H8 15%。genuine 分别为\\n    0%/0%/3%（mean=1.0%±1.7%）。原 D088 结论\\\"exec-only 保持 H1 不转 H7\\\"基于单 seed s42，现被 s43 反例否定。但更强的结论成立：hacking\\n    mode 随 seed 变化（多路径），但 genuine collapse 是系统性的（invariant endpoint）。论文叙事从\\\"特定 hacking\\n    mode\\\"升级为\\\"Goodhart collapse 系统性不可避免\\\"。\\n  related_experiments:\\n  - exp_id: plan016-extended-1000-s42\\n    role: evidence\\n    result: H1=100%, genuine=0%\\n  - exp_id: plan001-exec-only-s43-1000-r2\\n    role: evidence\\n    result: H7=100%, genuine=0%\\n  - exp_id: plan001-exec-only-s44-1000-r2\\n    role: evidence\\n    result: H1=85%+H8=15%, genuine=3%\\n  depends_on:\\n  - D088\\n- id: D090\\n  date: 2026-05-15 16:39 UTC\\n  summary: 'D090: Exec-only GRPO 3-seed 1000步完成，Goodhart collapse 3-seed 统计确认'\\n  rationale: 3 seeds (s42/s43/s44) 一致收敛到 near-zero genuine (1.0%±1.7%)，PR=0.95±0.05。与\\n    SFT 92.2%±1.2% 形成 >91pp 差距。Hacking mode seed-dependent (s42=H1, s43=H7, s44=H1+H8)，但\\n    genuine collapse 是 seed-invariant。ISR 高方差 (0.002-0.531) 反映不同 hacking 策略对 intermediate\\n    steps 保留差异。Goodhart collapse 是 RL(GRPO) 特有现象，证据链最后一块拼图就位。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43-1000-r2\\n    role: exec-only s43 1000步\\n    result: PR=0.90, ISR=0.531, genuine=0%, H7=100%\\n  - exp_id: plan001-exec-only-s44-1000-r2\\n    role: exec-only s44 1000步\\n    result: PR=1.00, ISR=0.002, genuine=3%, H1=85%+H8=15%\\n  - exp_id: plan016-extended-1000-s42\\n    role: exec-only s42 1000步\\n    result: PR=0.96, ISR=0.003, genuine=0%, H1=100%\\n  depends_on:\\n  - D089\\n  - D079\\n- id: D091\\n  date: 2026-05-15 16:54 UTC\\n  summary: 'D091: s44-1000 genuine 3%→0%，exec-only 3-seed 真实 genuine=0.0%±0.0%'\\n  rationale: 'Reviewer + registry audit 确认 s44-1000 的 3 个 \\\"genuine\\\" 样本（folio_1296/1428/1051）全部\\n    ISR=0，功能退化（disjunctive conclusions 绕过 H8、commuted/instantiated premise variants\\n    绕过 H1 text-match）。非真正推理。exec-only 3-seed 1000步实际 genuine: s42=0%, s43=0%, s44=0%，mean=0.0%±0.0%。比\\n    D090 的 1.0%±1.7% 更强——所有 GRPO exec-only 优化轨迹在 1000步后 genuinely 归零。论文 \\\"≤3% non-hacking\\\"\\n    改为 \\\"0% genuine (3 samples escape classifiers but are functionally degenerate,\\n    see Appendix)\\\"。'\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s44-1000-r2\\n    role: s44 genuine reclassified\\n    result: 3 samples ISR=0, all functionally degenerate → genuine=0%\\n  depends_on:\\n  - D090\\n- id: D092\\n  date: 2026-05-15 18:11 UTC\\n  summary: 暂停 H7 ISR-specific claim，等 Random 三 seed 全貌后调整 framing\\n  rationale: 'Reviewer critical: Random β=0.1 s43-r3 出现 H7=36 (38.3%)，直接否定 \\\"Random\\n    H7=0%\\\" claim (C136/C192)。H7 不再是 ISR-specific。需等 s44-r2 完成后根据三 seed H7 分布决定新叙事方向（ISR\\n    amplification vs seed-dependent stochastic behavior）。核心 Claim 1/2/3 不受影响。'\\n  related_experiments:\\n  - exp_id: plan018-additive-random-b01-s43-r3\\n    role: evidence\\n    result: H7=36 (38.3%), genuine=1/94 (1.1%)\\n  depends_on: []\\n- id: D093\\n  date: 2026-05-15 18:13 UTC\\n  summary: H7 非 ISR 独有：Random s43-r3 H7=38.3%，\\\"Random H7=0%\\\" 定论作废，转向 \\\"ISR amplifies\\n    H7\\\" 叙事\\n  rationale: Reviewer CRITICAL 报告：plan018-additive-random-b01-s43-r3 taxonomy 显示 H7a=36/94=38.3%，而\\n    s42 H7=0%。同一 classify_h7.py 版本下的 apple-to-apple 比较。这意味着：(1) H7 tautology 非 ISR\\n    独有，GRPO 训练动态本身可在 Random 条件下产生 H7；(2) 跨 seed 方差极大（0% vs 38.3%），单 seed 结论不可推广；(3)\\n    但 ISR pooled H7~70% >> 预计 Random pooled~15-25%，\\\"ISR 显著放大 H7\\\" 的方向仍成立。新叙事更 nuanced\\n    也更有说服力。等 s44-r2 完成后确定 Random pooled H7 rate，再做最终 framing 修订。\\n  related_experiments:\\n  - exp_id: plan018-additive-random-b01-s43-r3\\n    role: evidence\\n    result: H7=36/94=38.3%, genuine=1/94=1.1%\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: reference\\n    result: H7=0/79=0%, genuine=18/79=22.8%\\n  - exp_id: plan018-additive-random-b01-s44-r2\\n    role: pending\\n    result: 训练中，决定 Random pooled H7 rate\\n  depends_on: []\\n\", \"total_chars\": 74872, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "cfd7907d-e8d3-4624-a4ab-f9270441142f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "leafUuid": "e7878ba3-abf6-49bf-917a-578701bcd07b",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Draft H7 specificity framing adjustment proposal",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93"
}
```

---

### Tool result

_source line 19 · 2026-05-15T18:17:42.267Z_

<details><summary>↩ Tool result · `toolu_01RHfvsHMqgoBsjQCvtfhzEe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\", \"content\": \"# Memory — solver-trace-ablation\\n\\n## 决策与经验\\n\\n### Exec-only 3-seed 1000步 hacking mode 是 seed-dependent (D089, 2026-05-15)\\n- s42: 全 H1 (conclusion-in-premise), ISR≈0.003\\n- s43: 全 H7 (tautological collapse), ISR≈0.531\\n- s44: H1 85% + H8 15%, ISR≈0.002, 3 genuine 幸存\\n- **启示**: 不同随机初始化导致 GRPO 收敛到不同 hacking 策略，但 genuine rate 均趋向 0%。H7 策略保留 intermediate steps（高 ISR），H1 策略丢弃 steps（低 ISR）。ISR 作为诊断指标对 H7 有效但对 H1 无法区分\\n- **论文影响**: 可 claim \\\"universally collapses regardless of hacking mode\\\"，比限定单一 mode 更强\\n\\n### SFT 不产生 Goodhart collapse (D079, 2026-05-15)\\n- 3-seed SFT 1000步 genuine=92.2%±1.2%，零 H7/H8 hacking\\n- SFT 过拟合（loss 0.017）但不退化 genuine reasoning\\n- **原因**: SFT 无 reward optimization，不触发 Goodhart 效应\\n\\n### GPU 物理编号 vs 逻辑编号 (踩坑记录)\\n- SFT 脚本 `--gpu N` 是物理 GPU 编号，不是逻辑编号\\n- GRPO 脚本通过 CUDA_VISIBLE_DEVICES 映射，脚本内不需要 `--gpu`\\n- plan009-sft-baseline-s44-1000 前两次 OOM 就是因为 `--gpu 0` 撞了已占的 cuda:0\\n\\n### Config 文件命名陷阱\\n- ISR additive bonus 的 config 是 `grpo_additive_bonus_b01.yaml`，不是 `grpo_additive_b01.yaml`\\n- plan002 重训曾因 config 名错误失败\\n\\n### eval_sta.py 没有 --gpu 参数\\n- 必须通过 `CUDA_VISIBLE_DEVICES=N` 环境变量指定 GPU\\n- 直接跑默认用 cuda:0，可能与训练进程冲突\\n\\n### D078: plan002-additive-b01-s42 genuine_count 统一为 14\\n- 不要用旧值，以 D078 修正为准\\n\\n### Taxonomy 标准 (D082/D084/D086, 2026-05-15)\\n- **8 种 hacking modes**（H1-H7 + H8 conjunction collapse），D082 从 7 升级到 8\\n- genuine = proved − H7 − H1_exact − H8\\n- classify_h7.py D086 版本是 ground truth，之前版本有 bug\\n- Prolog STA 3/3 seeds 为 gaming（D059 Reviewer 修正）\\n\\n### Bootstrap CI 结论\\n- genuine rate parity: p=0.637 (n.s.) — ISR 与 random 无显著差异\\n- H7 gaming: p=0.0004 (***) — H7 在 additive 条件显著高于 random\\n- ISR* inflation: p<0.001 (***) — ISR 优化显著抬高 ISR*\\n\\n### D051: 2.4x 倍率作废\\n- premise-count-matched 分析得 1.06x，无结构优势\\n- 论文中不可引用 2.4x\\n\\n### Random s43/s44 旧统计量 DEPRECATED (2026-05-15)\\n- 原始数据丢失，s43-r3 正在重训、s44-r2 待提交\\n- paper_framing.md 中 s43 genuine=6.8% 和 s44 genuine=20.2% 为 PROVISIONAL 推算值\\n- Fisher p、Wilson CI、genuine rate 聚合数字必须等新数据重算\\n- **绝对不能**将旧数字当作已验证数据写入论文\\n\\n### AutoDL 网络注意事项\\n- pip install 前 `source /etc/network_turbo`\\n- HF 下载设 `HF_HUB_DISABLE_XET=1`\\n- SSL 证书: 设 `REQUESTS_CA_BUNDLE` 和 `SSL_CERT_FILE`\\n\", \"total_chars\": 2089, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbe3779d-0893-44df-8ef9-1215d562a9a3",
  "isSidechain": false,
  "promptId": "3607f857-899c-41b1-8c04-f693ac82b7c2",
  "type": "user",
  "uuid": "e7878ba3-abf6-49bf-917a-578701bcd07b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\\\", \\\"content\\\": \\\"# Memory — solver-trace-ablation\\\\n\\\\n## 决策与经验\\\\n\\\\n### Exec-only 3-seed 1000步 hacking mode 是 seed-dependent (D089, 2026-05-15)\\\\n- s42: 全 H1 (conclusion-in-premise), ISR≈0.003\\\\n- s43: 全 H7 (tautological collapse), ISR≈0.531\\\\n- s44: H1 85% + H8 15%, ISR≈0.002, 3 genuine 幸存\\\\n- **启示**: 不同随机初始化导致 GRPO 收敛到不同 hacking 策略，但 genuine rate 均趋向 0%。H7 策略保留 intermediate steps（高 ISR），H1 策略丢弃 steps（低 ISR）。ISR 作为诊断指标对 H7 有效但对 H1 无法区分\\\\n- **论文影响**: 可 claim \\\\\\\"universally collapses regardless of hacking mode\\\\\\\"，比限定单一 mode 更强\\\\n\\\\n### SFT 不产生 Goodhart collapse (D079, 2026-05-15)\\\\n- 3-seed SFT 1000步 genuine=92.2%±1.2%，零 H7/H8 hacking\\\\n- SFT 过拟合（loss 0.017）但不退化 genuine reasoning\\\\n- **原因**: SFT 无 reward optimization，不触发 Goodhart 效应\\\\n\\\\n### GPU 物理编号 vs 逻辑编号 (踩坑记录)\\\\n- SFT 脚本 `--gpu N` 是物理 GPU 编号，不是逻辑编号\\\\n- GRPO 脚本通过 CUDA_VISIBLE_DEVICES 映射，脚本内不需要 `--gpu`\\\\n- plan009-sft-baseline-s44-1000 前两次 OOM 就是因为 `--gpu 0` 撞了已占的 cuda:0\\\\n\\\\n### Config 文件命名陷阱\\\\n- ISR additive bonus 的 config 是 `grpo_additive_bonus_b01.yaml`，不是 `grpo_additive_b01.yaml`\\\\n- plan002 重训曾因 config 名错误失败\\\\n\\\\n### eval_sta.py 没有 --gpu 参数\\\\n- 必须通过 `CUDA_VISIBLE_DEVICES=N` 环境变量指定 GPU\\\\n- 直接跑默认用 cuda:0，可能与训练进程冲突\\\\n\\\\n### D078: plan002-additive-b01-s42 genuine_count 统一为 14\\\\n- 不要用旧值，以 D078 修正为准\\\\n\\\\n### Taxonomy 标准 (D082/D084/D086, 2026-05-15)\\\\n- **8 种 hacking modes**（H1-H7 + H8 conjunction collapse），D082 从 7 升级到 8\\\\n- genuine = proved − H7 − H1_exact − H8\\\\n- classify_h7.py D086 版本是 ground truth，之前版本有 bug\\\\n- Prolog STA 3/3 seeds 为 gaming（D059 Reviewer 修正）\\\\n\\\\n### Bootstrap CI 结论\\\\n- genuine rate parity: p=0.637 (n.s.) — ISR 与 random 无显著差异\\\\n- H7 gaming: p=0.0004 (***) — H7 在 additive 条件显著高于 random\\\\n- ISR* inflation: p<0.001 (***) — ISR 优化显著抬高 ISR*\\\\n\\\\n### D051: 2.4x 倍率作废\\\\n- premise-count-matched 分析得 1.06x，无结构优势\\\\n- 论文中不可引用 2.4x\\\\n\\\\n### Random s43/s44 旧统计量 DEPRECATED (2026-05-15)\\\\n- 原始数据丢失，s43-r3 正在重训、s44-r2 待提交\\\\n- paper_framing.md 中 s43 genuine=6.8% 和 s44 genuine=20.2% 为 PROVISIONAL 推算值\\\\n- Fisher p、Wilson CI、genuine rate 聚合数字必须等新数据重算\\\\n- **绝对不能**将旧数字当作已验证数据写入论文\\\\n\\\\n### AutoDL 网络注意事项\\\\n- pip install 前 `source /etc/network_turbo`\\\\n- HF 下载设 `HF_HUB_DISABLE_XET=1`\\\\n- SSL 证书: 设 `REQUESTS_CA_BUNDLE` 和 `SSL_CERT_FILE`\\\\n\\\", \\\"total_chars\\\": 2089, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\", \"content\": \"# Memory — solver-trace-ablation\\n\\n## 决策与经验\\n\\n### Exec-only 3-seed 1000步 hacking mode 是 seed-dependent (D089, 2026-05-15)\\n- s42: 全 H1 (conclusion-in-premise), ISR≈0.003\\n- s43: 全 H7 (tautological collapse), ISR≈0.531\\n- s44: H1 85% + H8 15%, ISR≈0.002, 3 genuine 幸存\\n- **启示**: 不同随机初始化导致 GRPO 收敛到不同 hacking 策略，但 genuine rate 均趋向 0%。H7 策略保留 intermediate steps（高 ISR），H1 策略丢弃 steps（低 ISR）。ISR 作为诊断指标对 H7 有效但对 H1 无法区分\\n- **论文影响**: 可 claim \\\"universally collapses regardless of hacking mode\\\"，比限定单一 mode 更强\\n\\n### SFT 不产生 Goodhart collapse (D079, 2026-05-15)\\n- 3-seed SFT 1000步 genuine=92.2%±1.2%，零 H7/H8 hacking\\n- SFT 过拟合（loss 0.017）但不退化 genuine reasoning\\n- **原因**: SFT 无 reward optimization，不触发 Goodhart 效应\\n\\n### GPU 物理编号 vs 逻辑编号 (踩坑记录)\\n- SFT 脚本 `--gpu N` 是物理 GPU 编号，不是逻辑编号\\n- GRPO 脚本通过 CUDA_VISIBLE_DEVICES 映射，脚本内不需要 `--gpu`\\n- plan009-sft-baseline-s44-1000 前两次 OOM 就是因为 `--gpu 0` 撞了已占的 cuda:0\\n\\n### Config 文件命名陷阱\\n- ISR additive bonus 的 config 是 `grpo_additive_bonus_b01.yaml`，不是 `grpo_additive_b01.yaml`\\n- plan002 重训曾因 config 名错误失败\\n\\n### eval_sta.py 没有 --gpu 参数\\n- 必须通过 `CUDA_VISIBLE_DEVICES=N` 环境变量指定 GPU\\n- 直接跑默认用 cuda:0，可能与训练进程冲突\\n\\n### D078: plan002-additive-b01-s42 genuine_count 统一为 14\\n- 不要用旧值，以 D078 修正为准\\n\\n### Taxonomy 标准 (D082/D084/D086, 2026-05-15)\\n- **8 种 hacking modes**（H1-H7 + H8 conjunction collapse），D082 从 7 升级到 8\\n- genuine = proved − H7 − H1_exact − H8\\n- classify_h7.py D086 版本是 ground truth，之前版本有 bug\\n- Prolog STA 3/3 seeds 为 gaming（D059 Reviewer 修正）\\n\\n### Bootstrap CI 结论\\n- genuine rate parity: p=0.637 (n.s.) — ISR 与 random 无显著差异\\n- H7 gaming: p=0.0004 (***) — H7 在 additive 条件显著高于 random\\n- ISR* inflation: p<0.001 (***) — ISR 优化显著抬高 ISR*\\n\\n### D051: 2.4x 倍率作废\\n- premise-count-matched 分析得 1.06x，无结构优势\\n- 论文中不可引用 2.4x\\n\\n### Random s43/s44 旧统计量 DEPRECATED (2026-05-15)\\n- 原始数据丢失，s43-r3 正在重训、s44-r2 待提交\\n- paper_framing.md 中 s43 genuine=6.8% 和 s44 genuine=20.2% 为 PROVISIONAL 推算值\\n- Fisher p、Wilson CI、genuine rate 聚合数字必须等新数据重算\\n- **绝对不能**将旧数字当作已验证数据写入论文\\n\\n### AutoDL 网络注意事项\\n- pip install 前 `source /etc/network_turbo`\\n- HF 下载设 `HF_HUB_DISABLE_XET=1`\\n- SSL 证书: 设 `REQUESTS_CA_BUNDLE` 和 `SSL_CERT_FILE`\\n\", \"total_chars\": 2089, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "cbe3779d-0893-44df-8ef9-1215d562a9a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-15T18:17:46.324Z_

<details><summary>Logged reasoning block</summary>

```text
I have paper_framing.md and memory.md content. The decisions.yaml was too large and saved to a file. Let me extract D092 and D093 from it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7878ba3-abf6-49bf-917a-578701bcd07b",
  "isSidechain": false,
  "requestId": "req_011Cb4p9qzVk6Va7e6gcenN5",
  "type": "assistant",
  "uuid": "751915af-72cd-4ad5-98e7-17b6a4674d9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAVXQWVdDBQdsiZrWNNfQm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15911,
      "cache_read_input_tokens": 26578,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 410,
          "cache_read_input_tokens": 26578,
          "cache_creation_input_tokens": 15911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15911
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

_source line 21 · 2026-05-15T18:17:46.325Z_

decisions.yaml 太大，需要提取 D092 和 D093。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "751915af-72cd-4ad5-98e7-17b6a4674d9b",
  "isSidechain": false,
  "requestId": "req_011Cb4p9qzVk6Va7e6gcenN5",
  "type": "assistant",
  "uuid": "2ff5abf6-61bc-434d-864a-a8f367203dc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAVXQWVdDBQdsiZrWNNfQm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15911,
      "cache_read_input_tokens": 26578,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 410,
          "cache_read_input_tokens": 26578,
          "cache_creation_input_tokens": 15911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15911
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

_source line 22 · 2026-05-15T18:17:49.467Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01H3h1MnXwDSgkBLe3RrXb29`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/9fbe86a1-ca6c-45c2-ba33-211d5991aa93/tool-results/mcp-agent-ml-research-read_project_file-1778869062227.txt | python3 -c \"\nimport json, sys, yaml\nraw = json.loads(sys.stdin.read())\ndata = json.loads(raw['result'])\ncontent = data['data']['content']\ndecisions = yaml.safe_load(content)\nfor d in decisions:\n    if d.get('id') in ('D092', 'D093', 'D088', 'D086', 'D085', 'D084'):\n        print(f'=== {d[\\\"id\\\"]} ===')\n        print(yaml.dump(d, allow_unicode=True, default_flow_style=False))\n        print()\n\"",
  "description": "Extract D092, D093, D088, D086, D085, D084 from decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ff5abf6-61bc-434d-864a-a8f367203dc1",
  "isSidechain": false,
  "requestId": "req_011Cb4p9qzVk6Va7e6gcenN5",
  "type": "assistant",
  "uuid": "18dc75c8-a7bb-4763-9765-f37db324f10e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAVXQWVdDBQdsiZrWNNfQm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15911,
      "cache_read_input_tokens": 26578,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 410,
          "cache_read_input_tokens": 26578,
          "cache_creation_input_tokens": 15911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15911
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

_source line 23 · 2026-05-15T18:17:50.328Z_

<details><summary>↩ Tool result · reported error · `toolu_01H3h1MnXwDSgkBLe3RrXb29`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    if d.get('id') in ('D092', 'D093', 'D088', 'D086', 'D085', 'D084'):
       ^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18dc75c8-a7bb-4763-9765-f37db324f10e",
  "isSidechain": false,
  "promptId": "3607f857-899c-41b1-8c04-f693ac82b7c2",
  "type": "user",
  "uuid": "8c497eb2-e074-4a4e-8561-70180d2a87d4",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 8, in &lt;module>\n    if d.get('id') in ('D092', 'D093', 'D088', 'D086', 'D085', 'D084'):\n       ^^^^^\nAttributeError: 'str' object has no attribute 'get'",
  "sourceToolAssistantUUID": "18dc75c8-a7bb-4763-9765-f37db324f10e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T18:17:55.712Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014DYNbMTTRAtN5i93ap91SJ`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/9fbe86a1-ca6c-45c2-ba33-211d5991aa93/tool-results/mcp-agent-ml-research-read_project_file-1778869062227.txt | python3 -c \"\nimport json, sys\nraw = json.loads(sys.stdin.read())\ndata = json.loads(raw['result'])\ncontent = data['data']['content']\n# Find D092 and D093 sections\nimport re\nfor did in ['D092', 'D093', 'D088']:\n    pattern = rf'(- id: {did}\\b.*?)(?=\\n- id: D\\d|$)'\n    m = re.search(pattern, content, re.DOTALL)\n    if m:\n        print(f'=== {did} ===')\n        print(m.group(1)[:3000])\n        print()\n    else:\n        print(f'{did}: NOT FOUND')\n        print()\n\"",
  "description": "Extract D092, D093, D088 from decisions.yaml using regex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c497eb2-e074-4a4e-8561-70180d2a87d4",
  "isSidechain": false,
  "requestId": "req_011Cb4pASZNPAYR1LVcem44q",
  "type": "assistant",
  "uuid": "54f5d924-1301-4554-a4f1-6e0d675eee88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5aoocZcCPgfZiQ38CpGDV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 519,
      "cache_read_input_tokens": 42489,
      "output_tokens": 359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 519,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 359,
          "cache_read_input_tokens": 42489,
          "cache_creation_input_tokens": 519,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 519
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

_source line 25 · 2026-05-15T18:17:55.872Z_

<details><summary>↩ Tool result · `toolu_014DYNbMTTRAtN5i93ap91SJ`</summary>

```text
=== D092 ===
- id: D092
  date: 2026-05-15 18:11 UTC
  summary: 暂停 H7 ISR-specific claim，等 Random 三 seed 全貌后调整 framing
  rationale: 'Reviewer critical: Random β=0.1 s43-r3 出现 H7=36 (38.3%)，直接否定 "Random
    H7=0%" claim (C136/C192)。H7 不再是 ISR-specific。需等 s44-r2 完成后根据三 seed H7 分布决定新叙事方向（ISR
    amplification vs seed-dependent stochastic behavior）。核心 Claim 1/2/3 不受影响。'
  related_experiments:
  - exp_id: plan018-additive-random-b01-s43-r3
    role: evidence
    result: H7=36 (38.3%), genuine=1/94 (1.1%)
  depends_on: []

=== D093 ===
- id: D093
  date: 2026-05-15 18:13 UTC
  summary: H7 非 ISR 独有：Random s43-r3 H7=38.3%，"Random H7=0%" 定论作废，转向 "ISR amplifies
    H7" 叙事
  rationale: Reviewer CRITICAL 报告：plan018-additive-random-b01-s43-r3 taxonomy 显示 H7a=36/94=38.3%，而
    s42 H7=0%。同一 classify_h7.py 版本下的 apple-to-apple 比较。这意味着：(1) H7 tautology 非 ISR
    独有，GRPO 训练动态本身可在 Random 条件下产生 H7；(2) 跨 seed 方差极大（0% vs 38.3%），单 seed 结论不可推广；(3)
    但 ISR pooled H7~70% >> 预计 Random pooled~15-25%，"ISR 显著放大 H7" 的方向仍成立。新叙事更 nuanced
    也更有说服力。等 s44-r2 完成后确定 Random pooled H7 rate，再做最终 framing 修订。
  related_experiments:
  - exp_id: plan018-additive-random-b01-s43-r3
    role: evidence
    result: H7=36/94=38.3%, genuine=1/94=1.1%
  - exp_id: plan018-additive-random-b01-s42
    role: reference
    result: H7=0/79=0%, genuine=18/79=22.8%
  - exp_id: plan018-additive-random-b01-s44-r2
    role: pending
    result: 训练中，决定 Random pooled H7 rate
  depends_on: []

=== D088 ===
- id: D088
  date: 2026-05-15 15:37 UTC
  summary: 'D088: 修正 D087——H7 非 GRPO 通用终态，而是 additive reward 特有终态；exec-only 1000步为
    100% H1'
  rationale: Reviewer 核实 plan016 (exec-only 1000步) 为 100% H1 (96/96)，非 H7。三种 reward
    mode 在 1000步的坍缩终态完全不同：exec-only→H1 (多premise结论嵌入), Random additive→H7 (单premise=结论),
    ISR additive→H7。可支撑叙事修正为："添加 additive reward（无论 ISR 还是 random）将坍缩模式从 H1 转向 H7；H7
    由 reward 结构驱动而非 ISR 语义信号；ISR 加速 H7 收敛（500步 vs 1000步）"。所有 GRPO 模式在 1000步均达 0% genuine——坍缩本身是通用的，但坍缩模式取决于
    reward 结构。SFT 1000步 3-seed >90% genuine 确认 RL-specificity。另：Reviewer 发现 batch_h7ab_clean.json
    用了已失败实验数据（proved=100）而非 r3（proved=97），r3 registry metrics 与 taxonomy_note 矛盾，需修复。
  related_experiments:
  - exp_id: plan016
    role: critical_counter_evidence
    result: 'exec-only 1000步: H7=0, H1=96 (100%), genuine=0 — H1 坍缩而非 H7'
  - exp_id: plan018-random-b01-s42-1000-r3
    role: key_evidence
    result: 'Random additive 1000步: H7=97 (100%), H1=0'
  - exp_id: plan002-b01-s42-1000
    role: reference
    result: 'ISR additive 1000步: H7=87 (97%), H1=0'
  depends_on:
  - D087
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54f5d924-1301-4554-a4f1-6e0d675eee88",
  "isSidechain": false,
  "promptId": "3607f857-899c-41b1-8c04-f693ac82b7c2",
  "type": "user",
  "uuid": "1832036c-2102-4a89-8be6-c65deb00d400",
  "toolUseResult": {
    "stdout": "=== D092 ===\n- id: D092\n  date: 2026-05-15 18:11 UTC\n  summary: 暂停 H7 ISR-specific claim，等 Random 三 seed 全貌后调整 framing\n  rationale: 'Reviewer critical: Random β=0.1 s43-r3 出现 H7=36 (38.3%)，直接否定 \"Random\n    H7=0%\" claim (C136/C192)。H7 不再是 ISR-specific。需等 s44-r2 完成后根据三 seed H7 分布决定新叙事方向（ISR\n    amplification vs seed-dependent stochastic behavior）。核心 Claim 1/2/3 不受影响。'\n  related_experiments:\n  - exp_id: plan018-additive-random-b01-s43-r3\n    role: evidence\n    result: H7=36 (38.3%), genuine=1/94 (1.1%)\n  depends_on: []\n\n=== D093 ===\n- id: D093\n  date: 2026-05-15 18:13 UTC\n  summary: H7 非 ISR 独有：Random s43-r3 H7=38.3%，\"Random H7=0%\" 定论作废，转向 \"ISR amplifies\n    H7\" 叙事\n  rationale: Reviewer CRITICAL 报告：plan018-additive-random-b01-s43-r3 taxonomy 显示 H7a=36/94=38.3%，而\n    s42 H7=0%。同一 classify_h7.py 版本下的 apple-to-apple 比较。这意味着：(1) H7 tautology 非 ISR\n    独有，GRPO 训练动态本身可在 Random 条件下产生 H7；(2) 跨 seed 方差极大（0% vs 38.3%），单 seed 结论不可推广；(3)\n    但 ISR pooled H7~70% >> 预计 Random pooled~15-25%，\"ISR 显著放大 H7\" 的方向仍成立。新叙事更 nuanced\n    也更有说服力。等 s44-r2 完成后确定 Random pooled H7 rate，再做最终 framing 修订。\n  related_experiments:\n  - exp_id: plan018-additive-random-b01-s43-r3\n    role: evidence\n    result: H7=36/94=38.3%, genuine=1/94=1.1%\n  - exp_id: plan018-additive-random-b01-s42\n    role: reference\n    result: H7=0/79=0%, genuine=18/79=22.8%\n  - exp_id: plan018-additive-random-b01-s44-r2\n    role: pending\n    result: 训练中，决定 Random pooled H7 rate\n  depends_on: []\n\n=== D088 ===\n- id: D088\n  date: 2026-05-15 15:37 UTC\n  summary: 'D088: 修正 D087——H7 非 GRPO 通用终态，而是 additive reward 特有终态；exec-only 1000步为\n    100% H1'\n  rationale: Reviewer 核实 plan016 (exec-only 1000步) 为 100% H1 (96/96)，非 H7。三种 reward\n    mode 在 1000步的坍缩终态完全不同：exec-only→H1 (多premise结论嵌入), Random additive→H7 (单premise=结论),\n    ISR additive→H7。可支撑叙事修正为：\"添加 additive reward（无论 ISR 还是 random）将坍缩模式从 H1 转向 H7；H7\n    由 reward 结构驱动而非 ISR 语义信号；ISR 加速 H7 收敛（500步 vs 1000步）\"。所有 GRPO 模式在 1000步均达 0% genuine——坍缩本身是通用的，但坍缩模式取决于\n    reward 结构。SFT 1000步 3-seed >90% genuine 确认 RL-specificity。另：Reviewer 发现 batch_h7ab_clean.json\n    用了已失败实验数据（proved=100）而非 r3（proved=97），r3 registry metrics 与 taxonomy_note 矛盾，需修复。\n  related_experiments:\n  - exp_id: plan016\n    role: critical_counter_evidence\n    result: 'exec-only 1000步: H7=0, H1=96 (100%), genuine=0 — H1 坍缩而非 H7'\n  - exp_id: plan018-random-b01-s42-1000-r3\n    role: key_evidence\n    result: 'Random additive 1000步: H7=97 (100%), H1=0'\n  - exp_id: plan002-b01-s42-1000\n    role: reference\n    result: 'ISR additive 1000步: H7=87 (97%), H1=0'\n  depends_on:\n  - D087",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "54f5d924-1301-4554-a4f1-6e0d675eee88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-15T18:18:09.322Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the key data. Let me synthesize:

**Key facts for the framing proposal:**

1. **D092**: Pause H7 ISR-specific claim, wait for Random 3-seed full picture
2. **D093**: H7 not ISR-exclusive. Random s43-r3 H7=38.3%, "Random H7=0%" is invalidated. Shift to "ISR amplifies H7" narrative
3. **D088**: H7 is additive-reward-specific endpoint (not GRPO-universal). 

The Random baseline shows H7 emerging at 38.3% with additive rewards, while ISR dramatically accelerates convergence to near-perfect H7 performance—reaching 96.7% and 100% at the same step counts where Random barely hits 38%. This validates the amplification narrative rather than exclusivity. I'm ready to finalize the proposal and add it to memory.md, pulling in the current content and appending the new framing section about H7's role across ISR and random conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1832036c-2102-4a89-8be6-c65deb00d400",
  "isSidechain": false,
  "requestId": "req_011Cb4pArEejFhMwSrKKKpz3",
  "type": "assistant",
  "uuid": "033d656d-abd7-4edc-8ea2-972e940cf2ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTcgGULfcF6fxLtt8Qvcqq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 43008,
      "output_tokens": 6083,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1775,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6083,
          "cache_read_input_tokens": 43008,
          "cache_creation_input_tokens": 1775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1775
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

_source line 27 · 2026-05-15T18:18:11.194Z_

所有数据已收集。现在起草 framing 调整提案并追加到 memory.md。

关键数据汇总：
- D092: 暂停 H7 ISR-specific claim
- D093: Random s43-r3 H7=38.3%，推翻 "Random H7=0%"，转向 "ISR amplifies H7"
- D088: H7 是 additive reward 特有终态（非 GRPO 通用），exec-only 1000步→100% H1

现有 H7 分布：
- ISR β=0.1: s42=16.0%, s43=96.7%, s44=100% → pooled 64.5%
- Random β=0.1: s42=0%, s43-r3=38.3%, s44-r2=**PENDING**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "033d656d-abd7-4edc-8ea2-972e940cf2ad",
  "isSidechain": false,
  "requestId": "req_011Cb4pArEejFhMwSrKKKpz3",
  "type": "assistant",
  "uuid": "2dff6410-1590-4554-895b-34dc2ecfdb6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTcgGULfcF6fxLtt8Qvcqq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 43008,
      "output_tokens": 6083,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1775,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6083,
          "cache_read_input_tokens": 43008,
          "cache_creation_input_tokens": 1775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1775
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

_source line 28 · 2026-05-15T18:19:44.689Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01GXdzxnUiF8X9ENPtuLb7XY`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "memory.md",
  "content": "# Memory — solver-trace-ablation\n\n## 决策与经验\n\n### Exec-only 3-seed 1000步 hacking mode 是 seed-dependent (D089, 2026-05-15)\n- s42: 全 H1 (conclusion-in-premise), ISR≈0.003\n- s43: 全 H7 (tautological collapse), ISR≈0.531\n- s44: H1 85% + H8 15%, ISR≈0.002, 3 genuine 幸存\n- **启示**: 不同随机初始化导致 GRPO 收敛到不同 hacking 策略，但 genuine rate 均趋向 0%。H7 策略保留 intermediate steps（高 ISR），H1 策略丢弃 steps（低 ISR）。ISR 作为诊断指标对 H7 有效但对 H1 无法区分\n- **论文影响**: 可 claim \"universally collapses regardless of hacking mode\"，比限定单一 mode 更强\n\n### SFT 不产生 Goodhart collapse (D079, 2026-05-15)\n- 3-seed SFT 1000步 genuine=92.2%±1.2%，零 H7/H8 hacking\n- SFT 过拟合（loss 0.017）但不退化 genuine reasoning\n- **原因**: SFT 无 reward optimization，不触发 Goodhart 效应\n\n### GPU 物理编号 vs 逻辑编号 (踩坑记录)\n- SFT 脚本 `--gpu N` 是物理 GPU 编号，不是逻辑编号\n- GRPO 脚本通过 CUDA_VISIBLE_DEVICES 映射，脚本内不需要 `--gpu`\n- plan009-sft-baseline-s44-1000 前两次 OOM 就是因为 `--gpu 0` 撞了已占的 cuda:0\n\n### Config 文件命名陷阱\n- ISR additive bonus 的 config 是 `grpo_additive_bonus_b01.yaml`，不是 `grpo_additive_b01.yaml`\n- plan002 重训曾因 config 名错误失败\n\n### eval_sta.py 没有 --gpu 参数\n- 必须通过 `CUDA_VISIBLE_DEVICES=N` 环境变量指定 GPU\n- 直接跑默认用 cuda:0，可能与训练进程冲突\n\n### D078: plan002-additive-b01-s42 genuine_count 统一为 14\n- 不要用旧值，以 D078 修正为准\n\n### Taxonomy 标准 (D082/D084/D086, 2026-05-15)\n- **8 种 hacking modes**（H1-H7 + H8 conjunction collapse），D082 从 7 升级到 8\n- genuine = proved − H7 − H1_exact − H8\n- classify_h7.py D086 版本是 ground truth，之前版本有 bug\n- Prolog STA 3/3 seeds 为 gaming（D059 Reviewer 修正）\n\n### Bootstrap CI 结论\n- genuine rate parity: p=0.637 (n.s.) — ISR 与 random 无显著差异\n- H7 gaming: p=0.0004 (***) — H7 在 additive 条件显著高于 random\n- ISR* inflation: p<0.001 (***) — ISR 优化显著抬高 ISR*\n\n### D051: 2.4x 倍率作废\n- premise-count-matched 分析得 1.06x，无结构优势\n- 论文中不可引用 2.4x\n\n### Random s43/s44 旧统计量 DEPRECATED (2026-05-15)\n- 原始数据丢失，s43-r3 正在重训、s44-r2 待提交\n- paper_framing.md 中 s43 genuine=6.8% 和 s44 genuine=20.2% 为 PROVISIONAL 推算值\n- Fisher p、Wilson CI、genuine rate 聚合数字必须等新数据重算\n- **绝对不能**将旧数字当作已验证数据写入论文\n\n### AutoDL 网络注意事项\n- pip install 前 `source /etc/network_turbo`\n- HF 下载设 `HF_HUB_DISABLE_XET=1`\n- SSL 证书: 设 `REQUESTS_CA_BUNDLE` 和 `SSL_CERT_FILE`\n\n## [DRAFT] Framing 调整提案 — H7 Specificity (D092/D093)\n\n> **状态**: DRAFT — 等 s44-r2 数据后定稿\n> **触发**: D093 (2026-05-15) — Random s43-r3 H7=38.3% 推翻 \"Random H7=0%\"\n> **影响范围**: Claim 2 子论据，不影响 Claim 1/2 核心和 Claim 3\n\n### 1. 原 Claim 与实验结果\n\n**原 claim (paper_framing.md, D057)**:\n> \"H7 是 ISR-specific gaming — β=0.1 下 ISR 3-seed H7=64.5%, Random β=0.1 3-seed H7=**0%** (0/256), 跨全部 3 random seeds 一致为零\"\n\n**实验结果 (D093)**:\n- Random β=0.1 s42: H7=0/79 (0%) ✅\n- Random β=0.1 s43-r3: H7=36/94 (**38.3%**) ← 推翻 \"一致为零\"\n- Random β=0.1 s44-r2: **PENDING**\n- ISR β=0.1 pooled: H7=149/231 (64.5%)\n\n**结论**: \"Random H7=0%\" 定论作废。H7 tautological collapse 非 ISR 独有，GRPO+additive reward 训练动态本身可在 Random 条件下产生 H7。\n\n### 2. 背景约束\n\n已确认不受影响的核心论据：\n- **Claim 2 核心**: premise-count-matched 1.06x 无结构优势 (D051) — 不依赖 H7 specificity\n- **β 剂量效应**: β=0.1→β=0.3 多模态 Goodhart 不稳定 — 不依赖 H7 specificity\n- **H7b obfuscated tautology** (D085): meta-Goodhart 证据 — ISR s44 triple gaming 独立于 Random 是否有 H7\n- **D088 关键发现**: H7 是 additive reward 特有终态（exec-only 1000步→100% H1，additive→H7），说明 H7 由 reward 结构（additive bonus）驱动而非 ISR 语义信号\n\n### 3. 三种备选叙事骨架\n\n#### 叙事 A: ISR Amplifies H7 (Dose-Response)\n\n**核心主张**: H7 tautological collapse 是 additive reward 结构的产物（D088），ISR 信号显著放大 H7 频率和收敛速度，但非绝对排他。\n\n**H7 rate 梯度**:\n| 条件 | H7 Rate | 证据 |\n|------|---------|------|\n| Exec-only 500步 (s42) | 0% | plan001 |\n| Exec-only 1000步 (s42) | 0% (100% H1) | plan016, D088 |\n| Random β=0.1 s42 | 0% | plan018 |\n| Random β=0.1 s43-r3 | 38.3% | D093 |\n| Random β=0.1 s44-r2 | **PENDING** | — |\n| Random β=0.3 s42 | 8.3% (4个) | D086 |\n| Random β=0.3 s43-r4 | ~7个 | D086 |\n| ISR β=0.1 s42 | 16.0% | plan002 |\n| ISR β=0.1 s43 | 96.7% | plan002 |\n| ISR β=0.1 s44 | 100% (H7a+H7b) | plan002, D085 |\n| ISR β=0.1 pooled | **64.5%** | D057 |\n\n**叙事逻辑**: Additive bonus 引入 H7 可能性 (D088: exec-only 不产生 H7)，ISR 信号放大 H7 频率（64.5% vs Random PENDING）。ISR 加速 H7 收敛（ISR 500步已现 H7，Random 需更多步/更高 β）。\n\n**优点**: 与 D088 完全一致，保留 \"ISR 有 specific effect\" 但降级为 amplification 而非 exclusivity。比原叙事更 nuanced 更抗攻击。\n**缺点**: 需 s44-r2 确认 Random pooled H7 rate，如果 s44-r2 也高 H7 则 amplification 幅度可能不够大。\n\n#### 叙事 B: H7 is Reward-General (Goodhart Universality)\n\n**核心主张**: H7 tautological collapse 在 ISR 和 Random reward 条件下均出现，强化 Goodhart 效应的普遍性——任何 additive reward bonus 都可能导致 H7，不需要 ISR 的语义信号。\n\n**叙事逻辑**: H7 是 additive reward 结构性质的产物 (D088)，不依赖 bonus 的语义内容。ISR 和 Random 的差异不在 H7 有无，而在 hacking mode 的分布/composition：\n- ISR: H7-dominant (64.5%), 低 H1\n- Random: H1-dominant (81.3%), H7 seed-dependent (0%–38.3%)\n\n这支持 Claim 2 核心论点：ISR 改变 hacking composition 而非总量，不提供结构优势。\n\n**优点**: 最强化 \"Goodhart universality\" 叙事，与 Claim 2 核心完全协调。不依赖 Random 3-seed H7 pooled rate 的具体值。\n**缺点**: 放弃了 ISR amplification 的 specific effect，可能被审稿人认为 \"ISR 和 Random 没区别那研究 ISR 干嘛\"——需强调 ISR 的价值在诊断 (Claim 1) 而非 reward。\n\n#### 叙事 C: H7 is Seed/Config-Dependent (Hacking Mode Diversity)\n\n**核心主张**: H7 频率高度依赖随机初始化和训练配置，属于 hacking mode diversity 的一部分。不同 seed 收敛到不同 hacking 策略（H1 vs H7 vs H8），这本身是 GRPO 不稳定性的体现。\n\n**叙事逻辑**: \n- ISR: s42=16%, s43=97%, s44=100% — 跨 seed 方差极大\n- Random: s42=0%, s43-r3=38.3%, s44-r2=PENDING — 同样高方差\n- Exec-only 1000步: s42=100% H1, s43=100% H7 (D089) — seed-dependent 在所有条件下复现\n\n核心发现不是 \"哪种条件产生 H7\"，而是 \"GRPO 训练的 hacking mode 高度随机，单 seed 结论不可推广\"。这支持 Practitioner Insight #2 (single-seed unreliable)。\n\n**优点**: 最保守、最难被攻击。将注意力从 H7 specificity 转移到 seed instability（已是强发现）。\n**缺点**: 削弱了对 ISR 特异性的任何论述，可能使论文缺乏 mechanism-level insight。\n\n### 4. 推荐方向\n\n**推荐叙事 A 为主线，B 为补充论述，C 作为 robustness discussion。**\n\n理由：\n1. D088 明确区分了 exec-only (无 H7) 和 additive (有 H7)，为 \"additive reward 引入 H7 可能性\" 提供 mechanism\n2. ISR pooled 64.5% vs Random (即使含 s43-r3 的 38.3%) 仍有显著差距，amplification 有数据支撑\n3. 叙事 A 保留 paper 的 mechanistic depth 而不过度依赖 exclusivity claim\n4. 叙事 B 的 universality 论点作为 Discussion 中的解读自然嵌入\n5. 叙事 C 的 seed-dependence 已在 Claim 1/Claim 3 中充分讨论\n\n### 5. 对论文各章节的影响\n\n**Abstract**:\n- 删除 \"ISR-specific H7\" 措辞\n- 改为 \"ISR reward amplifies tautological collapse (H7) frequency relative to random baseline, though H7 is not exclusive to ISR — it emerges from the additive reward structure itself\"\n- 核心 headline (\"ISR as diagnostic succeeds, as reward fails due to meta-Goodhart\") 不变\n\n**Introduction**:\n- 调整 contribution bullet: \"ISR reward amplifies specific hacking modes (H7 tautological collapse)\" 而非 \"exclusively causes\"\n- 保留 additive bonus 的 mechanism 讨论\n\n**Method (§3)**:\n- H7 定义和 STA 方法论不变\n- H7a/H7b 子分类不变\n\n**Experiments (§4)**:\n- §4.2 (ISR β=0.1): 更新 Random 对照数据为新数据（s42=0%, s43-r3=38.3%, s44-r2=PENDING）\n- 删除 \"Random 3-seed H7=0%\" 一致性论述\n- 替换为 H7 rate 对比表（ISR pooled vs Random pooled），标注 amplification 幅度\n- §4.3 (β dose): D086 的 β=0.3 H7 梯度证据 (Random β=0.1: 0-38% → β=0.3: 4-7个 → ISR β=0.1: 64.5%) 保留，调整解读\n\n**Discussion (§5)**:\n- 新增/重写 H7 mechanism 小节：\n  - H7 由 additive reward 结构驱动 (D088: exec-only 无 H7)\n  - ISR 信号放大 H7 频率（amplification, not exclusivity）\n  - 跨 seed 高方差 (0%-100%) 是 GRPO 不稳定性的体现\n  - H7b obfuscated tautology 仍为 ISR-specific meta-Goodhart 证据（Random 未观察到 H7b）\n- D086 dose-response gradient 保留\n\n**Conclusion**:\n- 核心结论 (\"ISR: diagnostic yes, reward no\") 不变\n- 调整措辞: \"H7 tautological collapse is amplified by ISR reward but can emerge under random additive reward, suggesting the phenomenon is driven by reward structure rather than ISR's semantic signal\"\n\n### 6. 建议下一步\n\n**必须等 s44-r2 完成后才能做的**:\n1. **计算 Random pooled H7 rate 和 Fisher exact test**: ISR pooled 149/231 vs Random pooled (0 + 36 + s44-r2)/N。确定 amplification 是否统计显著 (p<0.05)。这决定叙事 A 的强度。\n2. **重算所有 Random 侧聚合统计量**: genuine rate, Wilson CI, Fisher p — 按 memory.md 约束，必须用新数据重算。\n\n**可立即执行的**:\n3. **检查 H7b 在 Random 侧是否存在**: Random s43-r3 的 36 个 H7 是 H7a 还是 H7b？如果全是 H7a，则 H7b (obfuscated tautology) 仍为 ISR-specific，meta-Goodhart triple gaming 论据不受影响。用 classify_h7.py 跑 Random s43-r3 的 H7 子类别。\n4. **D088 机制验证**: 确认 exec-only 3-seed 1000步均无 H7（D089 记录 s43 有 H7），如果 exec-only s43 也有 H7，则 H7 不仅限于 additive reward 结构。需核实 D089 s43 的 \"全 H7\" 是 exec-only 还是其他条件。\n5. **H7 收敛速度对比**: ISR 何时出现 H7（100步? 350步? 500步?） vs Random s43-r3 何时出现 H7。如果 ISR 更早出现 H7，支持 \"ISR accelerates H7 convergence\" 的 amplification 叙事。\n\n**论文写作准备**:\n6. **预写 Discussion H7 mechanism 段落**: 基于叙事 A 框架，留 placeholder 给 s44-r2 数据。等数据到后填入具体数字。\n\n### 7. 风险评估\n\n| 风险 | 概率 | 影响 | 应对 |\n|------|------|------|------|\n| s44-r2 也高 H7 (>30%) | 中 | Random pooled H7 可能接近 25-30%，削弱 amplification 叙事但不推翻 | 叙事 A 仍成立（64.5% vs 25-30% 仍显著），同时强化叙事 B |\n| s44-r2 H7=0% | 中 | Random pooled H7 ≈ 13-15%，amplification 叙事很强 | 叙事 A 最佳情景 |\n| D089 exec-only s43 的 \"全 H7\" 确认 | 需核实 | 如确认，H7 不仅限于 additive reward，影响 D088 结论 | 调整为 \"additive reward amplifies H7\" 而非 \"exclusively enables H7\" |\n| Random s43-r3 的 H7 中含 H7b | 低 | 如果 Random 也有 H7b，meta-Goodhart triple gaming 不再 ISR-specific | 降级 H7b 为 \"advanced hacking mode\" 而非 \"ISR-specific meta-Goodhart\" |\n\n---\n*Draft date: 2026-05-15. Pending: s44-r2 data, H7 subtype analysis on Random s43-r3.*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dff6410-1590-4554-895b-34dc2ecfdb6f",
  "isSidechain": false,
  "requestId": "req_011Cb4pArEejFhMwSrKKKpz3",
  "type": "assistant",
  "uuid": "3ab91662-c75c-4dc6-b4c1-403d67868d16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTcgGULfcF6fxLtt8Qvcqq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 43008,
      "output_tokens": 6083,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1775,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6083,
          "cache_read_input_tokens": 43008,
          "cache_creation_input_tokens": 1775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1775
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

_source line 29 · 2026-05-15T18:19:44.735Z_

<details><summary>↩ Tool result · `toolu_01GXdzxnUiF8X9ENPtuLb7XY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ab91662-c75c-4dc6-b4c1-403d67868d16",
  "isSidechain": false,
  "promptId": "3607f857-899c-41b1-8c04-f693ac82b7c2",
  "type": "user",
  "uuid": "4bb9c86a-7924-4c66-9005-a8e9f172dcbb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "3ab91662-c75c-4dc6-b4c1-403d67868d16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-15T18:19:44.740Z_

```json
{
  "parentUuid": "4bb9c86a-7924-4c66-9005-a8e9f172dcbb",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6cb883a6-18ff-43ab-93a7-ae216311bd7c",
  "timestamp": "2026-05-15T18:19:44.740Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "leafUuid": "6cb883a6-18ff-43ab-93a7-ae216311bd7c",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Draft H7 specificity framing adjustment proposal",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93"
}
```

---

### Assistant

_source line 33 · 2026-05-15T18:19:47.552Z_

<details><summary>Logged reasoning block</summary>

```text
The proposal has been saved. Let me summarize what was done.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cb883a6-18ff-43ab-93a7-ae216311bd7c",
  "isSidechain": false,
  "requestId": "req_011Cb4pJscyLwUHpBooFwqqf",
  "type": "assistant",
  "uuid": "46d79f8f-815f-490e-bf09-70b52cf58961",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZDBQzzhQbS3RC78Y1eM3X",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6268,
      "cache_read_input_tokens": 44783,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 404,
          "cache_read_input_tokens": 44783,
          "cache_creation_input_tokens": 6268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6268
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

_source line 34 · 2026-05-15T18:19:53.848Z_

Framing 调整提案已保存到 memory.md 末尾，标题 `## [DRAFT] Framing 调整提案 — H7 Specificity (D092/D093)`。

提案核心：

**三种备选叙事**：
- **A (推荐主线)**: ISR amplifies H7 — additive reward 结构引入 H7 可能性 (D088)，ISR 信号放大频率（64.5% vs Random PENDING）
- **B (补充)**: H7 is reward-general — 强化 Goodhart universality，ISR 改变 hacking composition 而非总量
- **C (robustness)**: seed/config-dependent — 高方差本身是发现

**对 Claim 2 核心无影响** — 1.06x premise-count-matched 和 β 剂量效应均不依赖 H7 specificity。

**关键待定项**：
1. s44-r2 数据 → Random pooled H7 rate → 决定 amplification 幅度
2. Random s43-r3 的 H7 子类别（H7a vs H7b）→ meta-Goodhart triple gaming 是否仍 ISR-specific
3. D089 exec-only s43 "全 H7" 需核实是否影响 D088 "additive-only H7" 结论

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46d79f8f-815f-490e-bf09-70b52cf58961",
  "isSidechain": false,
  "requestId": "req_011Cb4pJscyLwUHpBooFwqqf",
  "type": "assistant",
  "uuid": "34a936b1-10a3-4f41-9e55-df2b8d6b30d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZDBQzzhQbS3RC78Y1eM3X",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6268,
      "cache_read_input_tokens": 44783,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 404,
          "cache_read_input_tokens": 44783,
          "cache_creation_input_tokens": 6268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6268
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

_source line 35_

```json
{
  "type": "last-prompt",
  "leafUuid": "34a936b1-10a3-4f41-9e55-df2b8d6b30d1",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Draft H7 specificity framing adjustment proposal",
  "sessionId": "9fbe86a1-ca6c-45c2-ba33-211d5991aa93"
}
```

---
