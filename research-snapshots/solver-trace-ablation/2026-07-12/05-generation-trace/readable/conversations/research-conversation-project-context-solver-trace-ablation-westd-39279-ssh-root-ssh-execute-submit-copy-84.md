# Research conversation: <project_context> # 项目: solver-trace-ablation ## 运行环境 - 服务器名: westd-39279 - SSH 账户: root（调用 ssh_execute / submit_trainin

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/cd2ba71d-676c-402f-b1b9-4ca852b9e861.jsonl`
- **Structured JSON:** [`d8dd0168d15f60dd845b.json`](../../sessions/d8/d8dd0168d15f60dd845b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T18:08:08.182Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T18:08:08.182Z",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "content": "&lt;project_context>\n# 项目: solver-trace-ablation\n\n## 运行环境\n- 服务器名: westd-39279\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/solver-trace-ablation\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 所有实验统一使用 data/train_500_seed42.jsonl 作为训练数据，禁止使用 proofwriter_fol_500.jsonl 或其他数据文件（原因：Reviewer CRITICAL: plan001-s43 使用了不同数据文件导致多 seed 对比 confound。多 seed 实验必须控制数据变量，seed 仅控制模型初始化和训练随机性。）\n- **C002**: 提交训练任务前必须用 export CUDA_VISIBLE_DEVICES=N 显式设置 GPU，禁止 inline 赋值（bash -c VAR=X cmd），提交后验证 nvidia-smi 确认只占用分配的 GPU（原因：plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43 OOM 死亡。这是第二次 GPU 冲突事故。）\n- **C003**: 训练配置必须设置 save_total_limit=1 且禁用/限制 completions parquet 保存，防止磁盘耗尽（原因：plan013-r3 和 plan001-s43-r3 因磁盘 250G/250G 满导致 step 23/28 崩溃。根因：TRL 每实验保存 3 份模型权重（~48GB）+ completions parquet（~2.5GB）。）\n- **C004**: 跨 seed/跨 run 的 ISR 对比必须使用 eval_sta.py 统一评估，禁止引用训练日志 ISR 做跨 run 对比（不同 run 可能使用不同版本的 ISR 计算代码）（原因：Reviewer 核实发现 plan001-s42-r2 训练日志 ISR 使用 binary _fast_fn，plan001-s43-r4 使用 full STA _full_fn，同一指标名下计算方法不同导致不可比。论文中所有 ISR 数据必须来自 eval_sta.py 统一评估。）\n- **C005**: 所有 worker（含 fix/ops 类）启动任何 Python 进程前必须显式设置 CUDA_VISIBLE_DEVICES，禁止裸跑（原因：fix worker 未设 CUDA_VISIBLE_DEVICES 导致测试进程泄漏到 cuda:1（plan017 训练卡），占用 8638 MiB 显存。2026-05-14 事故。）\n- **C006**: 论文讨论 ISR 时必须区分两种语义：exec-only 的 low ISR = 冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA 的 high ISR = metric gaming（Goodhart 效应）。不可将 ISR 差异直接等同于 reasoning 能力差异。（原因：Reviewer 发现 Prolog exec-only 生成大量重复 ground facts（如 penguin(fido). 出现 3 次），per-clause ablation 下删任一重复不影响结果，ISR=0。这是冗余不是无推理。如不区分，审稿人会误读 ISR 差异。）\n- **C007**: kill_job 后必须 nvidia-smi 确认 GPU 释放，submit 前必须 nvidia-smi 确认目标 GPU 无残留进程（原因：同一 session 两次出现 kill tmux → Python orphan → 新实验 OOM 的 pattern。kill_job 只杀 tmux session 不杀进程组，submit_on_allocated 只检查 registry 不检查实际 GPU 占用。）\n- **C008**: 所有 eval 命令必须显式指定 --data_path data/proofwriter_fol_100.jsonl，禁止依赖默认值或使用 test_100.jsonl（原因：D063: exp1 系列 eval 使用了 test_100.jsonl（与论文数据集零重叠），导致结果不可比。C004 约束的加固版。） [来自 D063]\n- **C009**: 所有 eval 命令必须显式指定 --data_path data/proofwriter_fol_100.jsonl，禁止使用默认值或 test_100.jsonl（原因：exp1 系列 eval 使用了错误的 test_100.jsonl（与 plan 系列的 proofwriter_fol_100.jsonl 零重叠），导致跨系列数据不可比。违反 C004。） [来自 D062]\n- **C010**: 磁盘清理禁止删除 conclusion=success 且标记 needs-re-eval 的 checkpoint，删前必须检查 registry 状态（原因：disk-cleanup-v2 误删了 exp1-isr-b03-s43 和 exp1-random-b03-s43 的 checkpoint，导致必须重训。这两个 checkpoint 因 D062/D063 需要用正确测试集 re-eval。）\n- **C011**: 磁盘清理禁止删除 conclusion=success 且标记 needs-re-eval 的 checkpoint 目录（原因：disk-cleanup-v2 Worker 误删 exp1_isr_b03_s43 和 exp1_random_b03_s43 checkpoint，导致必须重训。清理前必须交叉检查 registry 中 re-eval 标记。）\n- **C012**: Resume 训练时必须验证步数语义：--model_path 指向 checkpoint 时，确认 train_grpo.py 是从该 step 继续（resume）还是从 0 开始新训练。如不确定，从 base model 重新训练，不用 checkpoint。禁止第三次犯 resume 步数不对等错误。（原因：Agent 两次将 checkpoint-350 作为 model_path 启动 1000 步训练，实际训练了 1350 步（350+1000）而非 resume 到 1000 步，导致与 ISR 1000 步实验不可比。plan018-r2 数据作废。）\n- **C013**: Taxonomy 标准：genuine = proved − H7 − H1_exact − H8。H1-near 保留为 genuine 但单独标记。ISR 和 Random 两侧必须对称使用同一标准。（原因：D084 决策。H8 是退化证明必须扣除；H1-near 仍需推理步骤保留为 genuine；标准必须两侧对称以确保论文方法论一致性。） [来自 D084]\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：整理 Random β=0.1 和 ISR β=0.1 的 3-seed 对比数据表\n\n### 背景\n项目处于论文收尾阶段，需要整理已完成实验的 cross-seed 对比数据。目前 Random s44 重训 (plan018-additive-random-b01-s44-r2) 还在跑，所以只整理已有数据。\n\n### 已有数据（从 registry 获取）\n\n**Random β=0.1**:\n- s42 (plan018-additive-random-b01-s42): PR=0.79, genuine_strict=12 (15.19%), H7=0, H1=56 (70.9%), H8=3 (3.8%)\n- s43-r3 (plan018-additive-random-b01-s43-r3): PR=0.94, genuine=1 (1.06%), H7=36 (38.3%), H1=56 (59.6%), H8=1 (1.1%)\n- s44-r2: RUNNING（暂不纳入）\n\n**ISR β=0.1**:\n- s42 (plan002-additive-b01-s42): PR=0.81, genuine=14 (17.3%), H7=13 (16%), H1=42 (51.9%), H8=12 (14.8%)\n- s43-r2 (plan002-additive-b01-s43-r2): PR=0.61, genuine=0 (0%), H7=61 (100%), H1=0, H8=0\n- s44 (plan002-additive-b01-s44): PR=0.89, genuine=0 (0%), H7=89 (100%), H1=0, H8=0\n\n### 你的任务\n1. 用 `read_registry` 读取以上 6 个实验的完整 metrics，确认数据准确\n2. 计算 ISR 3-seed pooled 统计量：\n   - pooled genuine rate = sum(genuine_count) / sum(n_proved)\n   - pooled H7 rate, H1 rate, H8 rate\n   - mean ± std of prove_rate across 3 seeds\n   - mean ± std of genuine_rate across 3 seeds\n3. 计算 Random 2-seed 临时统计量（s42 + s43-r3，s44 待补）\n4. 将结果写入 artifacts 目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_comparison_table.md`\n5. 用 `register_artifact` 注册产出\n\n### 注意\n- genuine 定义: proved − H7 − H1_exact − H8（D084 标准）\n- Random s42 的 genuine 用 strict 版本 (12, 15.19%)，不用 exact_h1 版本 (23)\n- ISR s42 的 n_proved=81，s43-r2 的 n_proved=61，s44 的 n_proved=89\n- 所有数字必须追溯到 registry，不可杜撰"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T18:08:08.185Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T18:08:08.185Z",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-15T18:08:08.224Z_

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
## 任务：整理 Random β=0.1 和 ISR β=0.1 的 3-seed 对比数据表

### 背景
项目处于论文收尾阶段，需要整理已完成实验的 cross-seed 对比数据。目前 Random s44 重训 (plan018-additive-random-b01-s44-r2) 还在跑，所以只整理已有数据。

### 已有数据（从 registry 获取）

**Random β=0.1**:
- s42 (plan018-additive-random-b01-s42): PR=0.79, genuine_strict=12 (15.19%), H7=0, H1=56 (70.9%), H8=3 (3.8%)
- s43-r3 (plan018-additive-random-b01-s43-r3): PR=0.94, genuine=1 (1.06%), H7=36 (38.3%), H1=56 (59.6%), H8=1 (1.1%)
- s44-r2: RUNNING（暂不纳入）

**ISR β=0.1**:
- s42 (plan002-additive-b01-s42): PR=0.81, genuine=14 (17.3%), H7=13 (16%), H1=42 (51.9%), H8=12 (14.8%)
- s43-r2 (plan002-additive-b01-s43-r2): PR=0.61, genuine=0 (0%), H7=61 (100%), H1=0, H8=0
- s44 (plan002-additive-b01-s44): PR=0.89, genuine=0 (0%), H7=89 (100%), H1=0, H8=0

### 你的任务
1. 用 `read_registry` 读取以上 6 个实验的完整 metrics，确认数据准确
2. 计算 ISR 3-seed pooled 统计量：
   - pooled genuine rate = sum(genuine_count) / sum(n_proved)
   - pooled H7 rate, H1 rate, H8 rate
   - mean ± std of prove_rate across 3 seeds
   - mean ± std of genuine_rate across 3 seeds
3. 计算 Random 2-seed 临时统计量（s42 + s43-r3，s44 待补）
4. 将结果写入 artifacts 目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_comparison_table.md`
5. 用 `register_artifact` 注册产出

### 注意
- genuine 定义: proved − H7 − H1_exact − H8（D084 标准）
- Random s42 的 genuine 用 strict 版本 (12, 15.19%)，不用 exact_h1 版本 (23)
- ISR s42 的 n_proved=81，s43-r2 的 n_proved=61，s44 的 n_proved=89
- 所有数字必须追溯到 registry，不可杜撰

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "db93fe6a-8875-4790-b540-188c747c78ba",
  "type": "user",
  "uuid": "fadef1d8-ecb7-4945-ae65-5bfc1968d591",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T18:08:08.223Z_

```json
{
  "parentUuid": "fadef1d8-ecb7-4945-ae65-5bfc1968d591",
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
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__update_registry"
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
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "e56fca04-4339-4bdf-a044-7b0c7b655981",
  "timestamp": "2026-05-15T18:08:08.223Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T18:08:08.223Z_

```json
{
  "parentUuid": "e56fca04-4339-4bdf-a044-7b0c7b655981",
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
  "uuid": "951224a4-c350-4799-a4a2-74ecbc8391ad",
  "timestamp": "2026-05-15T18:08:08.223Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T18:08:08.223Z_

```json
{
  "parentUuid": "951224a4-c350-4799-a4a2-74ecbc8391ad",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bd04ac82-6593-4e0a-8c89-58ed28a67871",
  "timestamp": "2026-05-15T18:08:08.223Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
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
  "aiTitle": "Organize Random and ISR β=0.1 3-seed comparison table",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861"
}
```

---

### Assistant

_source line 8 · 2026-05-15T18:08:11.208Z_

我来读取 registry 确认这些实验的完整 metrics。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd04ac82-6593-4e0a-8c89-58ed28a67871",
  "isSidechain": false,
  "requestId": "req_011Cb4oRXoC41Mxuth5svcAc",
  "type": "assistant",
  "uuid": "b8e0a53d-37d3-41d0-bf7b-70994206f831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRc3AQn9rxtvxt5TiwxaF7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13473,
      "cache_read_input_tokens": 11841,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13473,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13473,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13473
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

_source line 9 · 2026-05-15T18:08:11.438Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Q8ZpkDPtevkeQy8zHhRwvh`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8e0a53d-37d3-41d0-bf7b-70994206f831",
  "isSidechain": false,
  "requestId": "req_011Cb4oRXoC41Mxuth5svcAc",
  "type": "assistant",
  "uuid": "9bb12677-0ca0-4a0f-a324-26952f725bd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRc3AQn9rxtvxt5TiwxaF7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13473,
      "cache_read_input_tokens": 11841,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13473,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13473,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13473
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

_source line 10 · 2026-05-15T18:08:11.445Z_

<details><summary>↩ Tool result · `toolu_01Q8ZpkDPtevkeQy8zHhRwvh`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

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
  "parentUuid": "9bb12677-0ca0-4a0f-a324-26952f725bd0",
  "isSidechain": false,
  "promptId": "db93fe6a-8875-4790-b540-188c747c78ba",
  "type": "user",
  "uuid": "d2cf915b-a124-4ab8-ad14-9cc0e5d20878",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "9bb12677-0ca0-4a0f-a324-26952f725bd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-15T18:08:14.351Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the registry for the 6 experiments mentioned. I'll query them by their exp_ids.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2cf915b-a124-4ab8-ad14-9cc0e5d20878",
  "isSidechain": false,
  "requestId": "req_011Cb4oRmf8LdsWL4kRmj3as",
  "type": "assistant",
  "uuid": "5478c0c9-a54c-4b57-b31a-723001202b59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gsigq8nCW5hHBmrWd77TdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 25314,
      "output_tokens": 699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 699,
          "cache_read_input_tokens": 25314,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1082
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

_source line 12 · 2026-05-15T18:08:14.856Z_

Reading registry for all 6 experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5478c0c9-a54c-4b57-b31a-723001202b59",
  "isSidechain": false,
  "requestId": "req_011Cb4oRmf8LdsWL4kRmj3as",
  "type": "assistant",
  "uuid": "ffae9ed4-5a58-4625-b763-b625497af259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gsigq8nCW5hHBmrWd77TdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 25314,
      "output_tokens": 699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 699,
          "cache_read_input_tokens": 25314,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1082
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

_source line 13 · 2026-05-15T18:08:16.043Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_011w2gMbUyM9GG3puwTAKS1w`</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": {
    "exp_id": "plan018-additive-random-b01-s42"
  },
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffae9ed4-5a58-4625-b763-b625497af259",
  "isSidechain": false,
  "requestId": "req_011Cb4oRmf8LdsWL4kRmj3as",
  "type": "assistant",
  "uuid": "dc921498-6bdc-461e-bdd3-9e39fc114977",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gsigq8nCW5hHBmrWd77TdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 25314,
      "output_tokens": 699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 699,
          "cache_read_input_tokens": 25314,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1082
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

_source line 14 · 2026-05-15T18:08:16.416Z_

<details><summary>↩ Tool result · `toolu_011w2gMbUyM9GG3puwTAKS1w`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3533}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc921498-6bdc-461e-bdd3-9e39fc114977",
  "isSidechain": false,
  "promptId": "db93fe6a-8875-4790-b540-188c747c78ba",
  "type": "user",
  "uuid": "e3091a10-81c0-48d1-b037-4fcec192f033",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3533}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3533}}"
    }
  },
  "sourceToolAssistantUUID": "dc921498-6bdc-461e-bdd3-9e39fc114977",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T18:08:16.995Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01BCrTjvxfptvGePS7ywPv6j`</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": {
    "exp_id": "plan018-additive-random-b01-s43-r3"
  },
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3091a10-81c0-48d1-b037-4fcec192f033",
  "isSidechain": false,
  "requestId": "req_011Cb4oRmf8LdsWL4kRmj3as",
  "type": "assistant",
  "uuid": "d6cf6a52-7d43-4d38-a88b-cc6b180997fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gsigq8nCW5hHBmrWd77TdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 25314,
      "output_tokens": 699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 699,
          "cache_read_input_tokens": 25314,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1082
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

_source line 16 · 2026-05-15T18:08:17.318Z_

<details><summary>↩ Tool result · `toolu_01BCrTjvxfptvGePS7ywPv6j`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3117}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6cf6a52-7d43-4d38-a88b-cc6b180997fa",
  "isSidechain": false,
  "promptId": "db93fe6a-8875-4790-b540-188c747c78ba",
  "type": "user",
  "uuid": "9503a791-d89f-485b-a9c7-309a140626ec",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3117}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3117}}"
    }
  },
  "sourceToolAssistantUUID": "d6cf6a52-7d43-4d38-a88b-cc6b180997fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T18:08:17.422Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019DRoFf6aNR9D4DKxxU17kB`</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": {
    "exp_id": "plan002-additive-b01-s42"
  },
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9503a791-d89f-485b-a9c7-309a140626ec",
  "isSidechain": false,
  "requestId": "req_011Cb4oRmf8LdsWL4kRmj3as",
  "type": "assistant",
  "uuid": "37dc31ef-7e70-4510-ad47-f870fcea1266",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gsigq8nCW5hHBmrWd77TdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 25314,
      "output_tokens": 699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 699,
          "cache_read_input_tokens": 25314,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1082
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

_source line 18 · 2026-05-15T18:08:17.737Z_

<details><summary>↩ Tool result · `toolu_019DRoFf6aNR9D4DKxxU17kB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3056}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37dc31ef-7e70-4510-ad47-f870fcea1266",
  "isSidechain": false,
  "promptId": "db93fe6a-8875-4790-b540-188c747c78ba",
  "type": "user",
  "uuid": "c4bd28e2-011e-4aef-8763-a48818847dc2",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3056}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3056}}"
    }
  },
  "sourceToolAssistantUUID": "37dc31ef-7e70-4510-ad47-f870fcea1266",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T18:08:18.322Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01XrCxh8j2wXgPLmdS9bR6pf`</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": {
    "exp_id": "plan002-additive-b01-s43-r2"
  },
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4bd28e2-011e-4aef-8763-a48818847dc2",
  "isSidechain": false,
  "requestId": "req_011Cb4oRmf8LdsWL4kRmj3as",
  "type": "assistant",
  "uuid": "f4749aeb-75c1-4c75-8732-9c3e907785aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gsigq8nCW5hHBmrWd77TdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 25314,
      "output_tokens": 699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 699,
          "cache_read_input_tokens": 25314,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1082
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

_source line 20 · 2026-05-15T18:08:18.875Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01GdjvtYBBNmBvMzEipHdPUk`</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": {
    "exp_id": "plan002-additive-b01-s44"
  },
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4749aeb-75c1-4c75-8732-9c3e907785aa",
  "isSidechain": false,
  "requestId": "req_011Cb4oRmf8LdsWL4kRmj3as",
  "type": "assistant",
  "uuid": "e7e0be31-ec7f-4f53-8f9d-fa8f67b91a8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gsigq8nCW5hHBmrWd77TdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 25314,
      "output_tokens": 699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 699,
          "cache_read_input_tokens": 25314,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1082
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

_source line 21 · 2026-05-15T18:08:18.993Z_

<details><summary>↩ Tool result · `toolu_01XrCxh8j2wXgPLmdS9bR6pf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6473}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4749aeb-75c1-4c75-8732-9c3e907785aa",
  "isSidechain": false,
  "promptId": "db93fe6a-8875-4790-b540-188c747c78ba",
  "type": "user",
  "uuid": "f5bcabc2-1f8d-4edb-887a-a83d016a97e0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.6473}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6473}}"
    }
  },
  "sourceToolAssistantUUID": "f4749aeb-75c1-4c75-8732-9c3e907785aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T18:08:19.460Z_

<details><summary>↩ Tool result · `toolu_01GdjvtYBBNmBvMzEipHdPUk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4554}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7e0be31-ec7f-4f53-8f9d-fa8f67b91a8c",
  "isSidechain": false,
  "promptId": "db93fe6a-8875-4790-b540-188c747c78ba",
  "type": "user",
  "uuid": "468854a2-fe69-49c8-b473-cd49504ebf99",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4554}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4554}}"
    }
  },
  "sourceToolAssistantUUID": "e7e0be31-ec7f-4f53-8f9d-fa8f67b91a8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T18:08:19.616Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_017vMJBLFtMoHwfHhtcRsdJK`</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": {
    "exp_id": "plan018-additive-random-b01-s44-r2"
  },
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "468854a2-fe69-49c8-b473-cd49504ebf99",
  "isSidechain": false,
  "requestId": "req_011Cb4oRmf8LdsWL4kRmj3as",
  "type": "assistant",
  "uuid": "aca31ee0-7c82-4d64-91a5-ebfc60931338",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gsigq8nCW5hHBmrWd77TdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 25314,
      "output_tokens": 699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 699,
          "cache_read_input_tokens": 25314,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1082
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

_source line 24_

```json
{
  "type": "last-prompt",
  "leafUuid": "aca31ee0-7c82-4d64-91a5-ebfc60931338",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Organize Random and ISR β=0.1 3-seed comparison table",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861"
}
```

---

### Tool result

_source line 26 · 2026-05-15T18:08:19.949Z_

<details><summary>↩ Tool result · `toolu_017vMJBLFtMoHwfHhtcRsdJK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3225}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aca31ee0-7c82-4d64-91a5-ebfc60931338",
  "isSidechain": false,
  "promptId": "db93fe6a-8875-4790-b540-188c747c78ba",
  "type": "user",
  "uuid": "1513bcb5-e37c-4c35-8d41-c588f59bc0c9",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3225}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3225}}"
    }
  },
  "sourceToolAssistantUUID": "aca31ee0-7c82-4d64-91a5-ebfc60931338",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-15T18:08:23.207Z_

<details><summary>Logged reasoning block</summary>

```text
All queries returned 0 results. The exp_id filter might not match exactly. Let me try broader queries to find the experiments. Let me list all experiments or search with partial filters.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1513bcb5-e37c-4c35-8d41-c588f59bc0c9",
  "isSidechain": false,
  "requestId": "req_011Cb4oSPxvcebm1UMxAX6Xd",
  "type": "assistant",
  "uuid": "2dde54df-746b-4578-b078-82531b9abb1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMkBHXJ23VTBZu9tBh5HBT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 26396,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1307,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 26396,
          "cache_creation_input_tokens": 1307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1307
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

_source line 28 · 2026-05-15T18:08:24.208Z_

Exact exp_id matches returned empty. Let me search more broadly to find the correct experiment IDs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dde54df-746b-4578-b078-82531b9abb1e",
  "isSidechain": false,
  "requestId": "req_011Cb4oSPxvcebm1UMxAX6Xd",
  "type": "assistant",
  "uuid": "372d0065-622d-489a-90c6-e62086a2132f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMkBHXJ23VTBZu9tBh5HBT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 26396,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1307,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 26396,
          "cache_creation_input_tokens": 1307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1307
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

_source line 29 · 2026-05-15T18:08:24.757Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_011nsBUvwjnMAVoTqtWw1qXt`</summary>

```json
{
  "project": "solver-trace-ablation",
  "limit": 0,
  "fields": [
    "exp_id",
    "status",
    "conclusion",
    "metrics"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "372d0065-622d-489a-90c6-e62086a2132f",
  "isSidechain": false,
  "requestId": "req_011Cb4oSPxvcebm1UMxAX6Xd",
  "type": "assistant",
  "uuid": "d6cf7607-b595-4ede-a993-67679fa51ef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMkBHXJ23VTBZu9tBh5HBT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 26396,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1307,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 26396,
          "cache_creation_input_tokens": 1307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1307
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

_source line 30 · 2026-05-15T18:08:25.083Z_

<details><summary>↩ Tool result · `toolu_011nsBUvwjnMAVoTqtWw1qXt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan018-additive-random-b01-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.79, \"eval_mean_isr\": 0.1038, \"eval_isr_std\": 0.1369, \"eval_median_isr\": 0.0357, \"eval_proved_only_isr\": 0.1314, \"eval_n_proved\": 79, \"eval_n_problems\": 100, \"tautological_collapse\": false, \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 58, \"h1_rate\": 0.7342, \"h8_count\": 4, \"h8_rate\": 0.0506, \"genuine_count\": 18, \"genuine_rate\": 0.2278, \"taxonomy_tool\": \"classify_h7.py standard (2026-05-15)\", \"taxonomy_note\": \"Re-classified with current classify_h7.py. Old values: genuine_strict=12 (H1_exact=56, H1_near=8, H8=3). New standard: H1=58 (2 former H1-near now H1), H8=4, genuine=18. Standard definition: proved - H7 - H1 - H8.\"}}, \"plan018-additive-random-b01-s43-r3\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.94, \"n_proved\": 94, \"n_problems\": 100, \"mean_isr\": 0.1406, \"isr_std\": null, \"proved_only_isr\": 0.1495, \"h7_count\": 36, \"h7_rate\": 0.383, \"h7a_count\": 36, \"h7b_count\": 0, \"h1_count\": 56, \"h1_rate\": 0.596, \"h8_count\": 1, \"h8_rate\": 0.011, \"genuine_count\": 1, \"genuine_rate\": 0.0106, \"train_prove_rate\": 0.5825, \"train_mean_isr\": 0.1266}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s44-r2\": {\"status\": \"RUNNING\"}, \"plan002-additive-b01-s43-r2\": {\"status\": \"DONE\", \"metrics\": {\"eval_n_problems\": 100, \"eval_n_proved\": 61, \"eval_prove_rate\": 0.61, \"eval_mean_isr\": 0.5063, \"eval_isr_std\": 0.4518, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.8301, \"h7a_count\": 59, \"h7b_count\": 2, \"h7_count\": 61, \"h7_rate\": 1, \"h1_count\": 0, \"h1_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"proved_single_premise_ratio\": 1, \"content_independent_predicates\": 5, \"isr_eq_1_count\": 40, \"isr_eq_1_rate_of_proved\": 0.656, \"train_prove_rate\": 0.68775, \"train_mean_isr\": 0.5039}, \"conclusion\": \"negative\"}, \"plan001-exec-only-s43-1000-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"prove_rate\": 0.9, \"n_proved\": 90, \"n_problems\": 100, \"mean_isr\": 0.531, \"isr_std\": 0.15, \"isr_corrected\": 0.465, \"isr_artifact_note\": \"n_components=3 quantifier decomposition artifact (+0.066) + $T solver bug 5 samples (+0.025). Corrected ISR=0.465, but both values entirely from H7a tautological necessity, no reasoning quality signal.\", \"h7_count\": 90, \"h7_rate\": 1, \"h7a_count\": 90, \"h7b_count\": 0, \"h1_count\": 0, \"h1_rate\": 0, \"h8_count\": 0, \"h8_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0}}, \"plan016-extended-1000-s42\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.96, \"n_proved\": 96, \"n_problems\": 100, \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 96, \"h1_rate\": 1, \"h8_count\": 0, \"h8_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"genuine_h1_near\": 0, \"genuine_strict\": 0, \"content_independent_rate\": 1, \"single_premise_rate\": 0, \"taxonomy_audit\": \"2026-05-15\", \"taxonomy_tool\": \"classify_h7.py current version (with H8 detection)\", \"taxonomy_note\": \"Re-run with current classify_h7.py. Old value genuine=7 was incorrect (old version lacked H8 and had weaker H1 detection). All 96 proved are H1 (conclusion embedded in premises). 0 H7, 0 H8.\"}, \"conclusion\": \"success\"}, \"plan001-exec-only-s44-1000-r2\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 1, \"n_proved\": 100, \"n_problems\": 100, \"mean_isr\": 0.002, \"isr_std\": 0.0146, \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 85, \"h1_rate\": 0.85, \"h8_count\": 15, \"h8_rate\": 0.15, \"genuine_count\": 0, \"genuine_rate\": 0, \"genuine_note\": \"D091: 3 samples escape text-match classifiers but are functionally degenerate (ISR=0, disjunctive/commuted bypasses)\"}, \"conclusion\": \"success\"}, \"plan018-additive-random-b01-s42-1000-r3\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.97, \"eval_mean_isr\": 0.6892, \"eval_isr_std\": 0.2037, \"eval_median_isr\": 0.75, \"eval_proved_only_isr\": 0.7105, \"eval_n_proved\": 97, \"eval_n_problems\": 100, \"genuine_count\": 0, \"genuine_rate\": 0, \"h1_count\": 0, \"h1_rate\": 0, \"h7_count\": 97, \"h7_rate\": 1, \"tautological_collapse\": true, \"train_final_prove_rate\": 0.827, \"train_final_mean_isr\": 0.5213, \"train_loss\": 0.00671, \"train_final_entropy\": 0.003, \"train_runtime_seconds\": 5783, \"train_steps\": 1000, \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 25, \"prove_rate\": 1, \"mean_isr\": 0.7533}, \"unknown\": {\"count\": 41, \"proved\": 39, \"prove_rate\": 0.951, \"mean_isr\": 0.6565}, \"true\": {\"count\": 34, \"proved\": 33, \"prove_rate\": 0.971, \"mean_isr\": 0.6814}}, \"n_premise_distribution\": {\"1\": 97}, \"pattern_description\": \"All 97 proved: 1 premise identical to conclusion (P therefore P). D088 correction: h7=97 h1=0 (was h1=97 h7=0 pre-D086 bugfix).\"}, \"conclusion\": \"negative\"}, \"plan009-sft-baseline-s44-1000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"prove_rate\": 0.15, \"n_proved\": 15, \"n_problems\": 100, \"mean_isr\": 0.0884, \"isr_std\": 0.2268, \"median_isr\": 0, \"proved_only_mean_isr\": 0.5892, \"max_isr\": 0.8571, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.4412}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0}}, \"genuine_count\": 14, \"genuine_rate\": 0.9333, \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0667, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0667, \"content_independent_count\": 0, \"content_independent_rate\": 0, \"isr_1_count\": 0, \"isr_1_rate\": 0, \"train_final_loss\": 0.0171, \"train_avg_loss\": 0.1544, \"train_token_accuracy\": 0.995, \"train_runtime_s\": 1580.97, \"eval_elapsed_s\": 391.8}}, \"plan009-sft-baseline-s43-1000\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.11, \"n_proved\": 11, \"n_problems\": 100, \"mean_isr\": 0.0699, \"isr_std\": 0.2155, \"median_isr\": 0, \"proved_only_mean_isr\": 0.6352, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 11, \"prove_rate\": 0.3235}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0}}, \"genuine_count\": 10, \"genuine_rate\": 0.9091, \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0909, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0909, \"content_independent_count\": 0, \"content_independent_rate\": 0, \"isr_1_count\": 1, \"isr_1_rate\": 0.0909, \"train_final_loss\": 0.0167, \"train_avg_loss\": 0.1551, \"train_token_accuracy\": 0.9954, \"train_runtime_s\": 1584.79, \"eval_elapsed_s\": 326.1}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s42-1000\": {\"status\": \"DONE\", \"metrics\": {\"train_final_loss\": 0.0168, \"train_last_step_loss\": 0.0168, \"train_token_accuracy\": 0.9955, \"train_epochs\": 15.88, \"train_runtime_sec\": 1415, \"train_steps\": 1000, \"eval_prove_rate\": 0.13, \"eval_n_proved\": 13, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0738, \"eval_isr_std\": 0.2077, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5677, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"eval_output_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json\", \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0769, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 12, \"genuine_rate\": 0.9231, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0769, \"isr_1_count\": 0, \"content_independent_count\": 0, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 12, \"prove_rate\": 0.353, \"mean_isr\": 0.209}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.011}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}}}, \"conclusion\": \"success\"}, \"exp1-random-b03-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.79, \"mean_isr\": 0.1745, \"isr_std\": 0.1628, \"median_isr\": 0.1667, \"proved_only_mean_isr\": 0.2209, \"hacking_rate_strict_h7\": 0, \"hacking_rate_functional\": 0.1013, \"genuine_rate\": 0.8987, \"genuine_count\": 71, \"n_proved\": 79, \"n_problems\": 100, \"h1_conclusion_in_premise\": 0.759, \"eval_data\": \"test_100.jsonl\", \"eval_output\": \"/root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43.json\"}}, \"exp1-random-b03-s43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_step\": 500, \"prove_rate\": 0.5505, \"mean_isr\": 0.1358, \"parse_rate\": 1, \"train_loss\": 0.01365, \"train_runtime_sec\": 6161.1, \"epoch\": 2, \"eval_prove_rate\": 0.92, \"eval_mean_isr\": 0.1659, \"eval_isr_std\": 0.1147, \"eval_median_isr\": 0.1429, \"eval_proved_only_mean_isr\": 0.1803, \"eval_min_isr\": 0, \"eval_max_isr\": 0.5, \"eval_n_proved\": 92, \"eval_n_problems\": 100, \"eval_h7_strict_rate\": 0.076, \"eval_h7_strict_count\": 7, \"eval_h1_strict_rate\": 0.891, \"eval_h1_strict_count\": 82, \"eval_genuine_rate\": 0.0326, \"eval_genuine_count\": 3, \"eval_isr0_count\": 6, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 23, \"prove_rate\": 0.92, \"mean_isr\": 0.156}, \"unknown\": {\"count\": 41, \"proved\": 37, \"prove_rate\": 0.902, \"mean_isr\": 0.184}, \"true\": {\"count\": 34, \"proved\": 32, \"prove_rate\": 0.941, \"mean_isr\": 0.151}}, \"D086_correction\": \"H1 90→82, genuine 2→3 per D086 clean batch run\"}}, \"plan002-additive-b01-s42-1000\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.9, \"eval_mean_isr\": 0.7892, \"eval_isr_std\": 0.3424, \"eval_proved_only_isr\": 0.8769, \"eval_median_isr\": 1, \"eval_n_proved\": 90, \"eval_n_problems\": 100, \"eval_component_count_mean\": 2.889, \"tautological_collapse\": true, \"train_final_prove_rate\": 0.855, \"train_final_mean_isr\": 0.532, \"h7_count\": 87, \"h7_rate\": 0.9667, \"h1_count\": 0, \"h1_rate\": 0, \"h1_near_count\": 1, \"h1_near_rate\": 0.0111, \"h8_conjunction_collapse_count\": 1, \"h8_conjunction_collapse_rate\": 0.0111, \"genuine_count\": 2, \"genuine_rate\": 0.0222, \"taxonomy_standard\": \"D086 clean run = ground truth. D084 residual removed.\"}}, \"plan002-additive-b01-s44\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.89, \"eval_mean_isr\": 0.803, \"eval_isr_std\": null, \"eval_proved_only_isr\": 0.902, \"eval_n_proved\": 89, \"eval_n_problems\": 100, \"h7_count\": 89, \"h7_rate\": 1, \"h1_count\": 0, \"h1_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"component_mean\": 4.33, \"comp_2_ratio\": 0.022, \"h7_fn_correction\": \"12 former genuine reclassified as H7: all n_prem=1 false negatives (normalization mismatch prevented conclusion matching)\"}, \"conclusion\": \"negative\"}, \"plan013-random-reward-s42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 1, \"eval_mean_isr\": 0.535, \"eval_isr_std\": 0.1282, \"eval_proved_only_isr\": 0.535, \"eval_median_isr\": 0.5, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\"}}, \"plan001-exec-only-s43-r4\": {\"status\": \"DONE\", \"metrics\": {\"eval_sampling_prove_rate\": 0.14, \"eval_sampling_mean_isr\": 0, \"eval_sampling_n_proved\": 14, \"eval_sampling_temperature\": 0.7, \"eval_sampling_method\": \"do_sample=True, temperature=0.7\", \"eval_sampling_by_answer\": {\"true\": {\"count\": 34, \"proved\": 6, \"prove_rate\": 0.176}, \"false\": {\"count\": 25, \"proved\": 2, \"prove_rate\": 0.08}, \"unknown\": {\"count\": 41, \"proved\": 6, \"prove_rate\": 0.146}}, \"eval_greedy_prove_rate\": 0.13, \"eval_greedy_mean_isr\": 0, \"eval_greedy_proved_only_isr\": 0, \"eval_greedy_n_proved\": 13, \"eval_greedy_method\": \"eval_sta.py default (do_sample=False)\", \"eval_greedy_by_answer\": {\"true\": {\"count\": 34, \"proved\": 4, \"prove_rate\": 0.118}, \"false\": {\"count\": 25, \"proved\": 5, \"prove_rate\": 0.2}, \"unknown\": {\"count\": 41, \"proved\": 4, \"prove_rate\": 0.0976}}, \"eval_greedy_h7_count\": 0, \"eval_greedy_h7_rate\": 0, \"eval_greedy_h1_count\": 13, \"eval_greedy_h1_rate\": 1, \"eval_greedy_genuine_rate\": 0, \"eval_greedy_n_premises_proved_mean\": 17.92, \"eval_greedy_mean_components_proved\": 18.92, \"eval_greedy_n_premises_all_mean\": 32.67, \"eval_sampling_h1_rate\": 1, \"eval_sampling_h7_rate\": 0, \"eval_sampling_genuine_rate\": 0, \"eval_sampling_mean_components_proved\": 18.5, \"eval_greedy_vs_sampling_delta_pr\": -0.01, \"eval_method_note\": \"Greedy and sampling agree on failure profile (ISR*=0, H1=100%, components~18.5-18.9). s43 collapse is decoding-invariant.\"}, \"conclusion\": \"negative\"}, \"plan001-exec-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan017-additive-random-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.48, \"eval_mean_isr\": 0.0453, \"eval_isr_std\": 0.0759, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2857, \"eval_proved_only_isr\": 0.0943, \"eval_n_proved\": 48, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 9.6, \"eval_component_count_2_ratio\": 0, \"tautological_collapse\": false, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 1, \"h1_count\": 48, \"genuine_rate\": 0, \"genuine_count\": 0}}, \"plan002-additive-b01-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.81, \"eval_mean_isr\": 0.3365, \"eval_isr_std\": 0.3227, \"eval_proved_only_isr\": 0.4154, \"eval_median_isr\": 0.2, \"eval_n_proved\": 81, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 5.58, \"h7_rate\": 0.16, \"h7_count\": 13, \"h1_rate\": 0.519, \"h1_count\": 42, \"h8_conjunction_collapse_count\": 12, \"h8_conjunction_collapse_rate\": 0.148, \"genuine_rate\": 0.173, \"genuine_count\": 14, \"tautological_collapse\": false, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse audit completed. 12/81 proved samples are H8. Genuine 26→14 (32.1%→17.3%). H8 JSON at /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json\"}}, \"plan002-additive-b01-s43\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.61, \"eval_n_proved\": 61, \"eval_n_problems\": 100, \"eval_proved_only_isr\": 0.83, \"h7_count\": 59, \"h7_rate\": 0.9672, \"h1_count\": 0, \"h1_rate\": 0, \"h1_near_count\": 0, \"h1_near_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 2, \"genuine_rate\": 0.0328, \"proved_single_premise_ratio\": 1, \"taxonomy_note\": \"structurally determined: proved_single_premise_ratio=1.0, all taxonomy categories except H7 are zero by construction. eval file lost but classification derivable from structure.\"}, \"conclusion\": \"negative\"}, \"exp1-isr-b03-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.91, \"mean_isr\": 0.2575, \"isr_std\": 0.2363, \"median_isr\": 0.3333, \"proved_only_mean_isr\": 0.283, \"hacking_rate_strict_h7\": 0.022, \"hacking_rate_functional\": 0.3297, \"genuine_rate\": 0.6703, \"genuine_count\": 61, \"n_proved\": 91, \"n_problems\": 100, \"h1_conclusion_in_premise\": 0.747, \"eval_data\": \"test_100.jsonl\", \"eval_output\": \"/root/autodl-tmp/outputs/eval_sta_exp1_isr_b03_s43.json\"}}, \"plan009-sft-baseline-s44-1000-r3\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.15, \"eval_n_proved\": 15, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0884, \"eval_isr_std\": 0.2268, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5892, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 1, \"h1_rate\": 0.0667, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 14, \"genuine_rate\": 0.9333, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.441, \"mean_isr\": 0.26}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}}}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s44\": {\"status\": \"DONE\", \"metrics\": {\"train_final_loss\": 0.2397, \"train_last_step_loss\": 0.0328, \"train_token_accuracy\": 0.9928, \"train_epochs\": 7.94, \"train_runtime_sec\": 729.05, \"train_steps\": 500, \"eval_prove_rate\": 0.17, \"eval_n_proved\": 17, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0974, \"eval_isr_std\": 0.2409, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5729, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"eval_output_path\": \"/root/autodl-tmp/outputs/eval_sta_plan009_sft_s44.json\", \"eval_tautological_collapse\": false, \"eval_h7_count\": 0, \"eval_h7_rate\": 0, \"eval_h1_count\": 2, \"eval_h1_rate\": 0.118, \"eval_genuine_count\": 15, \"eval_genuine_rate\": 0.882, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.441, \"mean_isr\": 0.257}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.027}, \"unknown\": {\"count\": 41, \"proved\": 1, \"prove_rate\": 0.024, \"mean_isr\": 0.008}}, \"eval_correction_note\": \"Corrected 2026-05-15: previous eval used test_100.jsonl (50/44/6 distribution), re-evaled with proofwriter_fol_100.jsonl (34/25/41)\"}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s43\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.2391, \"train_token_accuracy\": 0.9938, \"train_epochs\": 7.94, \"train_runtime_sec\": 677.14, \"train_steps\": 500, \"eval_prove_rate\": 0.15, \"eval_mean_isr\": 0.0895, \"eval_isr_std\": 0.2338, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5967, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 1, \"h1_rate\": 0.067, \"genuine_count\": 14, \"genuine_rate\": 0.933, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"prove_rate\": 0.382, \"mean_isr\": 0.234}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.027}, \"unknown\": {\"count\": 41, \"proved\": 1, \"prove_rate\": 0.024, \"mean_isr\": 0.008}}, \"eval_data_path\": \"data/proofwriter_fol_100.jsonl\", \"eval_output_path\": \"/root/autodl-tmp/outputs/eval_sta_plan009_sft_s43.json\"}, \"conclusion\": \"success\"}, \"plan001-exec-only-s44-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan009-sft-baseline-s44-1000-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan002-additive-b03-s42\": {\"status\": \"DONE\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"last100_prove_rate\": 0.5525, \"eval_prove_rate\": 0.18, \"eval_mean_isr\": 0.0257, \"eval_isr_std\": 0.0742, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.1427, \"eval_n_proved\": 18, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.778, \"h1_count\": 14, \"h8_conjunction_collapse_count\": 3, \"h8_conjunction_collapse_rate\": 0.1667, \"genuine_rate\": 0.0556, \"genuine_count\": 1, \"eval_by_type_false_pr\": 0.12, \"eval_by_type_false_isr\": 0.0102, \"eval_by_type_unknown_pr\": 0.195, \"eval_by_type_unknown_isr\": 0.0422, \"eval_by_type_true_pr\": 0.206, \"eval_by_type_true_isr\": 0.0172, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine 4→1.\"}, \"conclusion\": \"negative\"}, \"plan001-exec-only-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.93, \"eval_mean_isr\": 0.1232, \"eval_isr_std\": 0.1887, \"eval_proved_only_isr\": 0.1324, \"eval_median_isr\": 0, \"eval_n_proved\": 93, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.871, \"h1_count\": 81, \"h8_conjunction_collapse_count\": 6, \"h8_conjunction_collapse_rate\": 0.0645, \"genuine_rate\": 0.0753, \"genuine_count\": 7, \"genuine_mean_isr\": 0.3141, \"h1_mean_isr\": 0.1055, \"conclusion_embedding_total\": 0.871, \"content_independent_predicates_count\": 1, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine 12→7.\"}}, \"plan004-o1-ablation-s42\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.63, \"mean_isr\": 0.0072, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 63, \"h1_rate\": 1, \"h8_conjunction_collapse_count\": 2, \"h8_conjunction_collapse_rate\": 0.0317, \"genuine_count\": 0, \"genuine_rate\": 0, \"content_independent_predicates_count\": 3, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine unchanged (0).\"}, \"conclusion\": \"negative\"}, \"exp1-isr-b03-s42-1000-r2\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.95, \"eval_mean_isr\": 0.734, \"eval_isr_std\": 0.2575, \"eval_median_isr\": 0.6, \"eval_proved_only_isr\": 0.7726, \"eval_n_proved\": 95, \"eval_n_problems\": 100, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 25, \"prove_rate\": 1, \"mean_isr\": 0.824}, \"unknown\": {\"count\": 41, \"proved\": 38, \"prove_rate\": 0.927, \"mean_isr\": 0.673}, \"true\": {\"count\": 34, \"proved\": 32, \"prove_rate\": 0.941, \"mean_isr\": 0.741}}, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 54, \"h1_rate\": 0.568, \"genuine_count\": 0, \"genuine_rate\": 0, \"tautological_collapse\": true, \"isr_1_count\": 41, \"isr_1_rate\": 0.432, \"single_premise_count\": 0, \"train_final_prove_rate\": 0.829, \"train_final_mean_isr\": 0.727, \"train_loss\": 0.0041, \"train_runtime_seconds\": 6280, \"train_final_entropy\": 9e-06, \"completions_mean_length\": 47, \"h8_conjunction_collapse_count\": 41, \"h8_conjunction_collapse_rate\": 0.432, \"content_independent_predicates\": true}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s42-1000-r2\": {\"status\": \"DONE\", \"metrics\": {\"train_final_prove_rate\": 0.989, \"train_final_mean_isr\": 0.353, \"train_final_reward\": 1.062, \"train_steps\": 1000, \"train_runtime_seconds\": 2957, \"eval_prove_rate\": 1, \"eval_mean_isr\": 0.3333, \"eval_isr_std\": 0, \"eval_median_isr\": 0.3333, \"eval_proved_only_isr\": 0.3333, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_component_count_mean\": 3, \"genuine_rate\": 0, \"genuine_count\": 0, \"tautological_collapse\": true, \"h7_rate\": null, \"h7_count\": null, \"h1_rate\": null, \"h1_count\": null}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s42-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp1-isr-b03-s42-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s44\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.98, \"eval_mean_isr\": 0.57, \"eval_isr_std\": 0.2013, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.5816, \"eval_n_proved\": 98, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 2.04, \"eval_component_count_2\": 94, \"eval_component_count_3\": 4, \"tautological_collapse\": true, \"h7_rate\": 1, \"h7_count\": 97, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"conclusion_embedding_total\": 1}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s43-r2\": {\"status\": \"DONE\", \"metrics\": {\"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 93.2, \"h1_count\": 82, \"genuine_rate\": 6.8, \"genuine_count\": 6, \"eval_prove_rate\": 0.88, \"eval_mean_isr\": 0.058}, \"conclusion\": \"negative\"}, \"exp1-random-b03-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.23, \"eval_proved_only_mean_isr\": 0, \"eval_mean_isr\": 0, \"eval_isr_std\": 0, \"eval_median_isr\": 0, \"eval_n_proved\": 23, \"eval_n_problems\": 100, \"eval_h7_strict_rate\": 0, \"eval_h7_strict_count\": 0, \"eval_h1_strict_rate\": 1, \"eval_h1_strict_count\": 23, \"eval_genuine_rate\": 0, \"eval_genuine_count\": 0, \"eval_data\": \"proofwriter_fol_100.jsonl\"}}, \"exp1-isr-b03-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_step\": 500, \"prove_rate\": 0.56125, \"mean_isr\": 0.1515, \"parse_rate\": 1, \"train_loss\": 0.0176, \"train_runtime_sec\": 4153.6, \"epoch\": 2, \"eval_prove_rate\": 0.86, \"eval_mean_isr\": 0.2535, \"eval_isr_std\": 0.2406, \"eval_median_isr\": 0.3333, \"eval_proved_only_mean_isr\": 0.2948, \"eval_min_isr\": 0, \"eval_max_isr\": 0.75, \"eval_n_proved\": 86, \"eval_n_problems\": 100, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_h7_strict_rate\": 0.047, \"eval_h7_strict_count\": 4, \"eval_h1_strict_rate\": 0.686, \"eval_h1_strict_count\": 59, \"eval_conclusion_in_premise_rate\": 0.733, \"eval_conclusion_in_premise_count\": 63, \"eval_genuine_rate\": 0.267, \"eval_genuine_count\": 23, \"eval_single_premise_rate\": 0.058, \"eval_single_premise_count\": 5, \"eval_isr_1_count\": 0, \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 23, \"prove_rate\": 0.92, \"mean_isr\": 0.334}, \"unknown\": {\"count\": 41, \"proved\": 35, \"prove_rate\": 0.854, \"mean_isr\": 0.199}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.26}}}}, \"exp1-random-b03-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan015-linear-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp1-isr-b03-s43-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp1-random-b03-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp1-isr-b03-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"prove_rate\": 0.95, \"mean_isr\": 0.705, \"isr_std\": 0.172, \"proved_only_isr\": 0.7421, \"n_proved\": 95, \"n_problems\": 100, \"h7_rate\": 1, \"h7_count\": 95, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"single_premise_rate\": 1, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"Re-eval with correct test set (D062). Previous test_100.jsonl results invalidated.\"}}, \"exp1-random-b03-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp1-isr-b03-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp1-isr-b03-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp2-exec-s43-greedy\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp4-100step-h1h7\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan006-prolog-sta-s44\": {\"status\": \"DONE\", \"metrics\": {\"pass_rate\": 0.97, \"isr_mean\": 0.885, \"isr_n_cl_ge3\": \"N/A (0 samples)\", \"n_clauses_dist\": \"78/100 single-clause, 22/100 two-clause\", \"h7_functional_rate\": 0.979, \"genuine_rate\": 0, \"premise_count_analysis\": \"100% artifact - zero samples with n_clauses>=3, model exclusively generates 1-2 clause programs\", \"failure_mode\": \"query-as-fact gaming (total H7 collapse)\"}, \"conclusion\": \"negative\"}, \"plan006-prolog-sta-s43\": {\"status\": \"DONE\", \"metrics\": {\"train\": {\"final_prove_rate\": 0.769, \"final_mean_isr\": 0.129, \"final_loss\": 0.0155, \"final_entropy\": 0.09, \"final_reward\": 0.573, \"completion_length_mean\": 143, \"train_runtime_seconds\": 5095, \"train_runtime_minutes\": 84.9}, \"eval\": {\"n_problems\": 100, \"n_proved\": 38, \"prove_rate\": 0.38, \"mean_isr\": 0.0704, \"isr_std\": 0.1263, \"median_isr\": 0, \"proved_only_mean_isr\": 0.1853, \"min_isr\": 0, \"max_isr\": 1, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 11, \"prove_rate\": 0.44, \"mean_isr\": 0.1003}, \"unknown\": {\"count\": 41, \"proved\": 11, \"prove_rate\": 0.268, \"mean_isr\": 0.0394}, \"true\": {\"count\": 34, \"proved\": 16, \"prove_rate\": 0.471, \"mean_isr\": 0.0859}}}, \"h7_classification\": {\"h7_strict\": 0, \"h7_rate\": 0, \"h1_strict\": 37, \"h1_rate\": 0.974, \"conclusion_in_premise_total\": 37, \"conclusion_in_premise_rate\": 0.974, \"genuine_count\": 0, \"genuine_rate\": 0, \"isr_1_count\": 1, \"note\": \"1 pseudo-genuine sample (folio_1415) has query embedded in single mega-clause; all 38/38 proved samples are tautological\"}}, \"conclusion\": \"negative\"}, \"plan006-prolog-sta-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"cumulative_prove_rate\": 0.848, \"cumulative_mean_isr\": 0.787, \"final_prove_rate\": 1, \"final_isr\": 1, \"final_reward\": 1, \"saturation_onset_step\": 100, \"train_loss\": 0.00716, \"training_hours\": 0.78, \"final_entropy\": 0.01, \"final_completion_length\": 27, \"initial_completion_length\": 120, \"steps_at_perfect_reward\": 400, \"train_runtime_sec\": 2791, \"eval_prove_rate\": 0.5, \"eval_mean_isr\": 0.5, \"eval_proved_only_isr\": 1, \"eval_h7_rate\": 1, \"eval_h7_count\": 50, \"eval_proved_count\": 50, \"eval_total_count\": 100, \"eval_n_clauses_mean\": 1, \"eval_isr_distribution\": \"binary: 50x0 + 50x1\"}}, \"plan006-prolog-exec-s44\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.21, \"eval_mean_isr\": 0.0812, \"eval_isr_std\": 0.2343, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.3866, \"eval_min_isr\": 0, \"eval_max_isr\": 1, \"eval_n_proved\": 21, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 683.9, \"eval_by_type_false_pr\": 0.04, \"eval_by_type_false_isr\": 0.04, \"eval_by_type_unknown_pr\": 0.317, \"eval_by_type_unknown_isr\": 0.099, \"eval_by_type_true_pr\": 0.206, \"eval_by_type_true_isr\": 0.09, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\"}, \"plan009-sft-baseline-s42-r4\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.14, \"eval_mean_isr\": 0.08, \"eval_isr_std\": 0.214, \"eval_median_isr\": 0, \"eval_max_isr\": 0.833, \"eval_proved_only_isr\": 0.571, \"eval_n_proved\": 14, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"train_final_loss\": 0.0287, \"train_token_accuracy\": 0.9935, \"train_epochs\": 7.94, \"train_runtime_sec\": 789.6, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"pr\": 0.382, \"isr\": 0.226}, \"unknown\": {\"count\": 41, \"proved\": 1, \"pr\": 0.024, \"isr\": 0.008}, \"false\": {\"count\": 25, \"proved\": 0, \"pr\": 0, \"isr\": 0}}, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.071, \"h1_count\": 1, \"genuine_rate\": 0.929, \"genuine_count\": 13, \"hacking_patterns\": \"near-zero (1/14 H1, 0 H7, 92.9% genuine)\", \"tautological_collapse\": false}, \"conclusion\": \"success\"}, \"plan006-prolog-exec-s43-r3\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.56, \"eval_mean_isr\": 0.0084, \"eval_isr_std\": 0.0221, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.015, \"eval_min_isr\": 0, \"eval_max_isr\": 0.1, \"eval_n_proved\": 56, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 868.2, \"eval_by_type_false_pr\": 0.48, \"eval_by_type_false_isr\": 0.0043, \"eval_by_type_unknown_pr\": 0.6585, \"eval_by_type_unknown_isr\": 0.0114, \"eval_by_type_true_pr\": 0.5, \"eval_by_type_true_isr\": 0.0078, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s44\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.89, \"mean_isr\": 0.0619, \"isr_std\": 0.1756, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0695, \"n_proved\": 89, \"n_problems\": 100, \"max_isr\": 1, \"min_isr\": 0, \"isr_pr_ratio\": 0.0695, \"isr_zero_count\": 72, \"isr_one_count\": 2, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 21, \"prove_rate\": 0.84, \"mean_isr\": 0.0533}, \"unknown\": {\"count\": 41, \"proved\": 40, \"prove_rate\": 0.976, \"mean_isr\": 0.0892}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.0353}}, \"elapsed_seconds\": 1012.7, \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\"}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan006-prolog-exec-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan006-prolog-exec-s42\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.83, \"eval_mean_isr\": 0.031, \"eval_proved_only_isr\": 0.037, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2, \"eval_isr_std\": 0.0534, \"h7_rate\": 0, \"h1_rate\": 0, \"isr_1_rate\": 0, \"single_premise_rate\": 0, \"by_answer_type\": {\"true\": {\"proved\": 37, \"count\": 40, \"pr\": 0.925, \"isr\": 0.037}, \"false\": {\"proved\": 21, \"count\": 29, \"pr\": 0.724, \"isr\": 0.038}, \"unknown\": {\"proved\": 25, \"count\": 31, \"pr\": 0.806, \"isr\": 0.016}}}, \"conclusion\": \"negative\"}, \"plan006-prolog-exec-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan009-sft-baseline-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan009-sft-baseline-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan018-additive-random-b01-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan012-hacking-taxonomy\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"isr_b01_genuine_rate\": 0.259, \"random_b01_genuine_rate\": 0.177, \"genuine_rate_delta_pp\": 8.2, \"isr_b01_conclusion_embedding_rate\": 0.728, \"random_b01_conclusion_embedding_rate\": 0.785, \"isr_b01_genuine_mean_isr\": 0.6723, \"random_b01_genuine_mean_isr\": 0.3427, \"isr_b01_complexity_wo_utility_rate\": 0, \"random_b01_complexity_wo_utility_rate\": 0.038, \"isr_b01_hacking_rate\": 0.741, \"random_b01_hacking_rate\": 0.823}}, \"plan005-sta-low-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 71, \"parse_rate\": 1, \"overall_prove_rate\": 0.5657, \"overall_isr\": 0.1682, \"last50_prove_rate\": 0.77, \"last50_isr\": 0.2559, \"last100_prove_rate\": 0.7725, \"last100_isr\": 0.2299, \"last100_loss\": 0.022752, \"overall_loss\": 0.017296, \"last100_isr_pr_ratio\": 0.298, \"last100_isr_lt_pr_count\": \"99/100\", \"first_rolling10_pr_ge_0.8\": 178, \"first_rolling10_pr_ge_0.9\": 439, \"max_rolling10_pr\": 0.9375, \"max_rolling10_isr\": 0.3282, \"windowed\": {\"1-50\": {\"pr\": 0.1775, \"isr\": 0.0906}, \"51-100\": {\"pr\": 0.1775, \"isr\": 0.0835}, \"101-200\": {\"pr\": 0.5062, \"isr\": 0.1463}, \"201-300\": {\"pr\": 0.6713, \"isr\": 0.1791}, \"301-400\": {\"pr\": 0.7013, \"isr\": 0.1984}, \"401-500\": {\"pr\": 0.7725, \"isr\": 0.2299}}}}, \"plan014-downstream-nli-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_accuracy\": 0.341, \"proved_rate\": 0.915, \"proved_count\": 732, \"total_generations\": 800, \"parse_errors\": 0, \"accuracy_by_label\": {\"true\": 0.912, \"false\": 0, \"unknown\": 0.076}, \"spearman_rho\": -0.049, \"spearman_p\": 0.187, \"mann_whitney_U\": 17202, \"mann_whitney_p\": 0.288, \"bon_isr_accuracy\": 0.35, \"bon_random_accuracy\": 0.341, \"bon_oracle_accuracy\": 0.44, \"bon_prove_first_accuracy\": 0.35, \"isr_bucket_high_acc\": 0.75, \"isr_bucket_mid_acc\": 0.377, \"isr_bucket_low_acc\": 0.327, \"runtime_inference_s\": 408.8, \"runtime_eval_s\": 13.6}}, \"plan001-exec-only-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan003-eval-exec-only-r5\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.32, \"mean_isr\": 0.2055, \"isr_std\": 0.3194, \"proved_only_isr\": 0.6423, \"isr_by_type\": {\"true\": 0.3598, \"false\": 0.1723, \"unknown\": 0.0979}, \"total_samples\": 100, \"proved_count\": 32, \"runtime_s\": 251.7}, \"conclusion\": \"success\"}, \"plan001-exec-only-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta-r5\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1, \"mean_isr\": 0.04347, \"last20_prove_rate\": 0.15, \"last20_isr_mean\": 0.04956, \"first20_prove_rate\": 0.08125, \"first20_isr_mean\": 0.05182, \"overall_reward_mean\": 0.07174, \"last20_reward_mean\": 0.09978, \"training_steps\": 100, \"training_minutes\": 16.9, \"step_time_s\": 10.13, \"isr_pr_ratio_overall\": 0.43, \"isr_pr_ratio_last20\": 0.33, \"K\": 8}, \"conclusion\": \"negative\"}, \"sta-phase1-exec-only-r5\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_prove_rate\": 0.11875, \"first20_isr_mean\": 0.11875, \"overall_reward_mean\": 0.15125, \"last20_reward_mean\": 0.2, \"training_steps\": 100, \"training_minutes\": 15.7, \"step_time_s\": 9.44, \"isr_pr_ratio_last20\": 1, \"K\": 8}, \"conclusion\": \"success\"}, \"sta-phase1-exec-sta-r4\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1575, \"mean_isr\": 0.1525, \"last20_prove_rate\": 0.2125, \"last20_isr_mean\": 0.2125, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"conclusion\": \"negative\"}, \"sta-phase1-exec-only-r4\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"conclusion\": \"negative\"}, \"sta-phase1-exec-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-only\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-gt-isr-baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gt_prove_rate\": 0.18, \"gt_mean_isr\": 0.5588, \"gt_isr_std\": 0.2582, \"gt_isr_median\": 0.6125, \"solver_execution_rate\": 1, \"true_prove_rate\": 0.5, \"true_mean_isr\": 0.5833}}, \"sta-phase0-baseline\": {\"status\": \"DONE\", \"metrics\": {\"mean_isr\": 0.0641, \"isr_std\": 0.1983, \"median_isr\": 0, \"isr_range\": [0, 0.889], \"prove_rate\": 0.12, \"proved_count\": 12, \"total_samples\": 100, \"xor_affected_samples\": 34, \"effective_prove_rate_no_xor\": 0.182, \"avg_time_per_sample_s\": 3.4, \"total_runtime_s\": 336, \"isr_by_answer\": {\"true\": {\"n\": 34, \"proved\": 9, \"prove_rate\": 0.265, \"mean_isr\": 0.1345}, \"false\": {\"n\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.024}, \"unknown\": {\"n\": 41, \"proved\": 2, \"prove_rate\": 0.049, \"mean_isr\": 0.0302}}}, \"conclusion\": \"success\"}}, \"count\": 86, \"total\": 86, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3107}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6cf7607-b595-4ede-a993-67679fa51ef3",
  "isSidechain": false,
  "promptId": "db93fe6a-8875-4790-b540-188c747c78ba",
  "type": "user",
  "uuid": "048dc8bf-9821-4d1b-8ed0-ed6f7dcb9342",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"plan018-additive-random-b01-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.79, \\\"eval_mean_isr\\\": 0.1038, \\\"eval_isr_std\\\": 0.1369, \\\"eval_median_isr\\\": 0.0357, \\\"eval_proved_only_isr\\\": 0.1314, \\\"eval_n_proved\\\": 79, \\\"eval_n_problems\\\": 100, \\\"tautological_collapse\\\": false, \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h7a_count\\\": 0, \\\"h7b_count\\\": 0, \\\"h1_count\\\": 58, \\\"h1_rate\\\": 0.7342, \\\"h8_count\\\": 4, \\\"h8_rate\\\": 0.0506, \\\"genuine_count\\\": 18, \\\"genuine_rate\\\": 0.2278, \\\"taxonomy_tool\\\": \\\"classify_h7.py standard (2026-05-15)\\\", \\\"taxonomy_note\\\": \\\"Re-classified with current classify_h7.py. Old values: genuine_strict=12 (H1_exact=56, H1_near=8, H8=3). New standard: H1=58 (2 former H1-near now H1), H8=4, genuine=18. Standard definition: proved - H7 - H1 - H8.\\\"}}, \\\"plan018-additive-random-b01-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.94, \\\"n_proved\\\": 94, \\\"n_problems\\\": 100, \\\"mean_isr\\\": 0.1406, \\\"isr_std\\\": null, \\\"proved_only_isr\\\": 0.1495, \\\"h7_count\\\": 36, \\\"h7_rate\\\": 0.383, \\\"h7a_count\\\": 36, \\\"h7b_count\\\": 0, \\\"h1_count\\\": 56, \\\"h1_rate\\\": 0.596, \\\"h8_count\\\": 1, \\\"h8_rate\\\": 0.011, \\\"genuine_count\\\": 1, \\\"genuine_rate\\\": 0.0106, \\\"train_prove_rate\\\": 0.5825, \\\"train_mean_isr\\\": 0.1266}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan018-additive-random-b01-s44-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"plan002-additive-b01-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_n_problems\\\": 100, \\\"eval_n_proved\\\": 61, \\\"eval_prove_rate\\\": 0.61, \\\"eval_mean_isr\\\": 0.5063, \\\"eval_isr_std\\\": 0.4518, \\\"eval_median_isr\\\": 0.5, \\\"eval_proved_only_isr\\\": 0.8301, \\\"h7a_count\\\": 59, \\\"h7b_count\\\": 2, \\\"h7_count\\\": 61, \\\"h7_rate\\\": 1, \\\"h1_count\\\": 0, \\\"h1_rate\\\": 0, \\\"h8_conjunction_collapse_count\\\": 0, \\\"h8_conjunction_collapse_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"proved_single_premise_ratio\\\": 1, \\\"content_independent_predicates\\\": 5, \\\"isr_eq_1_count\\\": 40, \\\"isr_eq_1_rate_of_proved\\\": 0.656, \\\"train_prove_rate\\\": 0.68775, \\\"train_mean_isr\\\": 0.5039}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan001-exec-only-s43-1000-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.9, \\\"n_proved\\\": 90, \\\"n_problems\\\": 100, \\\"mean_isr\\\": 0.531, \\\"isr_std\\\": 0.15, \\\"isr_corrected\\\": 0.465, \\\"isr_artifact_note\\\": \\\"n_components=3 quantifier decomposition artifact (+0.066) + $T solver bug 5 samples (+0.025). Corrected ISR=0.465, but both values entirely from H7a tautological necessity, no reasoning quality signal.\\\", \\\"h7_count\\\": 90, \\\"h7_rate\\\": 1, \\\"h7a_count\\\": 90, \\\"h7b_count\\\": 0, \\\"h1_count\\\": 0, \\\"h1_rate\\\": 0, \\\"h8_count\\\": 0, \\\"h8_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0}}, \\\"plan016-extended-1000-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.96, \\\"n_proved\\\": 96, \\\"n_problems\\\": 100, \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h7a_count\\\": 0, \\\"h7b_count\\\": 0, \\\"h1_count\\\": 96, \\\"h1_rate\\\": 1, \\\"h8_count\\\": 0, \\\"h8_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"genuine_h1_near\\\": 0, \\\"genuine_strict\\\": 0, \\\"content_independent_rate\\\": 1, \\\"single_premise_rate\\\": 0, \\\"taxonomy_audit\\\": \\\"2026-05-15\\\", \\\"taxonomy_tool\\\": \\\"classify_h7.py current version (with H8 detection)\\\", \\\"taxonomy_note\\\": \\\"Re-run with current classify_h7.py. Old value genuine=7 was incorrect (old version lacked H8 and had weaker H1 detection). All 96 proved are H1 (conclusion embedded in premises). 0 H7, 0 H8.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan001-exec-only-s44-1000-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 1, \\\"n_proved\\\": 100, \\\"n_problems\\\": 100, \\\"mean_isr\\\": 0.002, \\\"isr_std\\\": 0.0146, \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h7a_count\\\": 0, \\\"h7b_count\\\": 0, \\\"h1_count\\\": 85, \\\"h1_rate\\\": 0.85, \\\"h8_count\\\": 15, \\\"h8_rate\\\": 0.15, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"genuine_note\\\": \\\"D091: 3 samples escape text-match classifiers but are functionally degenerate (ISR=0, disjunctive/commuted bypasses)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan018-additive-random-b01-s42-1000-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.97, \\\"eval_mean_isr\\\": 0.6892, \\\"eval_isr_std\\\": 0.2037, \\\"eval_median_isr\\\": 0.75, \\\"eval_proved_only_isr\\\": 0.7105, \\\"eval_n_proved\\\": 97, \\\"eval_n_problems\\\": 100, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"h1_count\\\": 0, \\\"h1_rate\\\": 0, \\\"h7_count\\\": 97, \\\"h7_rate\\\": 1, \\\"tautological_collapse\\\": true, \\\"train_final_prove_rate\\\": 0.827, \\\"train_final_mean_isr\\\": 0.5213, \\\"train_loss\\\": 0.00671, \\\"train_final_entropy\\\": 0.003, \\\"train_runtime_seconds\\\": 5783, \\\"train_steps\\\": 1000, \\\"eval_by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 25, \\\"prove_rate\\\": 1, \\\"mean_isr\\\": 0.7533}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 39, \\\"prove_rate\\\": 0.951, \\\"mean_isr\\\": 0.6565}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 33, \\\"prove_rate\\\": 0.971, \\\"mean_isr\\\": 0.6814}}, \\\"n_premise_distribution\\\": {\\\"1\\\": 97}, \\\"pattern_description\\\": \\\"All 97 proved: 1 premise identical to conclusion (P therefore P). D088 correction: h7=97 h1=0 (was h1=97 h7=0 pre-D086 bugfix).\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan009-sft-baseline-s44-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.15, \\\"n_proved\\\": 15, \\\"n_problems\\\": 100, \\\"mean_isr\\\": 0.0884, \\\"isr_std\\\": 0.2268, \\\"median_isr\\\": 0, \\\"proved_only_mean_isr\\\": 0.5892, \\\"max_isr\\\": 0.8571, \\\"by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 15, \\\"prove_rate\\\": 0.4412}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 0, \\\"prove_rate\\\": 0}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 0, \\\"prove_rate\\\": 0}}, \\\"genuine_count\\\": 14, \\\"genuine_rate\\\": 0.9333, \\\"h7_strict_count\\\": 0, \\\"h7_strict_rate\\\": 0, \\\"h1_strict_count\\\": 1, \\\"h1_strict_rate\\\": 0.0667, \\\"h8_conjunction_collapse_count\\\": 0, \\\"h8_conjunction_collapse_rate\\\": 0, \\\"conclusion_in_premise_count\\\": 1, \\\"conclusion_in_premise_rate\\\": 0.0667, \\\"content_independent_count\\\": 0, \\\"content_independent_rate\\\": 0, \\\"isr_1_count\\\": 0, \\\"isr_1_rate\\\": 0, \\\"train_final_loss\\\": 0.0171, \\\"train_avg_loss\\\": 0.1544, \\\"train_token_accuracy\\\": 0.995, \\\"train_runtime_s\\\": 1580.97, \\\"eval_elapsed_s\\\": 391.8}}, \\\"plan009-sft-baseline-s43-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.11, \\\"n_proved\\\": 11, \\\"n_problems\\\": 100, \\\"mean_isr\\\": 0.0699, \\\"isr_std\\\": 0.2155, \\\"median_isr\\\": 0, \\\"proved_only_mean_isr\\\": 0.6352, \\\"by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 11, \\\"prove_rate\\\": 0.3235}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 0, \\\"prove_rate\\\": 0}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 0, \\\"prove_rate\\\": 0}}, \\\"genuine_count\\\": 10, \\\"genuine_rate\\\": 0.9091, \\\"h7_strict_count\\\": 0, \\\"h7_strict_rate\\\": 0, \\\"h1_strict_count\\\": 1, \\\"h1_strict_rate\\\": 0.0909, \\\"h8_conjunction_collapse_count\\\": 0, \\\"h8_conjunction_collapse_rate\\\": 0, \\\"conclusion_in_premise_count\\\": 1, \\\"conclusion_in_premise_rate\\\": 0.0909, \\\"content_independent_count\\\": 0, \\\"content_independent_rate\\\": 0, \\\"isr_1_count\\\": 1, \\\"isr_1_rate\\\": 0.0909, \\\"train_final_loss\\\": 0.0167, \\\"train_avg_loss\\\": 0.1551, \\\"train_token_accuracy\\\": 0.9954, \\\"train_runtime_s\\\": 1584.79, \\\"eval_elapsed_s\\\": 326.1}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan009-sft-baseline-s42-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_final_loss\\\": 0.0168, \\\"train_last_step_loss\\\": 0.0168, \\\"train_token_accuracy\\\": 0.9955, \\\"train_epochs\\\": 15.88, \\\"train_runtime_sec\\\": 1415, \\\"train_steps\\\": 1000, \\\"eval_prove_rate\\\": 0.13, \\\"eval_n_proved\\\": 13, \\\"eval_n_problems\\\": 100, \\\"eval_mean_isr\\\": 0.0738, \\\"eval_isr_std\\\": 0.2077, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.5677, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_output_path\\\": \\\"/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json\\\", \\\"h7_strict_count\\\": 0, \\\"h7_strict_rate\\\": 0, \\\"h1_strict_count\\\": 1, \\\"h1_strict_rate\\\": 0.0769, \\\"h8_conjunction_collapse_count\\\": 0, \\\"h8_conjunction_collapse_rate\\\": 0, \\\"genuine_count\\\": 12, \\\"genuine_rate\\\": 0.9231, \\\"conclusion_in_premise_count\\\": 1, \\\"conclusion_in_premise_rate\\\": 0.0769, \\\"isr_1_count\\\": 0, \\\"content_independent_count\\\": 0, \\\"eval_by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 12, \\\"prove_rate\\\": 0.353, \\\"mean_isr\\\": 0.209}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 1, \\\"prove_rate\\\": 0.04, \\\"mean_isr\\\": 0.011}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 0, \\\"prove_rate\\\": 0, \\\"mean_isr\\\": 0}}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp1-random-b03-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.79, \\\"mean_isr\\\": 0.1745, \\\"isr_std\\\": 0.1628, \\\"median_isr\\\": 0.1667, \\\"proved_only_mean_isr\\\": 0.2209, \\\"hacking_rate_strict_h7\\\": 0, \\\"hacking_rate_functional\\\": 0.1013, \\\"genuine_rate\\\": 0.8987, \\\"genuine_count\\\": 71, \\\"n_proved\\\": 79, \\\"n_problems\\\": 100, \\\"h1_conclusion_in_premise\\\": 0.759, \\\"eval_data\\\": \\\"test_100.jsonl\\\", \\\"eval_output\\\": \\\"/root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43.json\\\"}}, \\\"exp1-random-b03-s43-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_step\\\": 500, \\\"prove_rate\\\": 0.5505, \\\"mean_isr\\\": 0.1358, \\\"parse_rate\\\": 1, \\\"train_loss\\\": 0.01365, \\\"train_runtime_sec\\\": 6161.1, \\\"epoch\\\": 2, \\\"eval_prove_rate\\\": 0.92, \\\"eval_mean_isr\\\": 0.1659, \\\"eval_isr_std\\\": 0.1147, \\\"eval_median_isr\\\": 0.1429, \\\"eval_proved_only_mean_isr\\\": 0.1803, \\\"eval_min_isr\\\": 0, \\\"eval_max_isr\\\": 0.5, \\\"eval_n_proved\\\": 92, \\\"eval_n_problems\\\": 100, \\\"eval_h7_strict_rate\\\": 0.076, \\\"eval_h7_strict_count\\\": 7, \\\"eval_h1_strict_rate\\\": 0.891, \\\"eval_h1_strict_count\\\": 82, \\\"eval_genuine_rate\\\": 0.0326, \\\"eval_genuine_count\\\": 3, \\\"eval_isr0_count\\\": 6, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 23, \\\"prove_rate\\\": 0.92, \\\"mean_isr\\\": 0.156}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 37, \\\"prove_rate\\\": 0.902, \\\"mean_isr\\\": 0.184}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 32, \\\"prove_rate\\\": 0.941, \\\"mean_isr\\\": 0.151}}, \\\"D086_correction\\\": \\\"H1 90→82, genuine 2→3 per D086 clean batch run\\\"}}, \\\"plan002-additive-b01-s42-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.9, \\\"eval_mean_isr\\\": 0.7892, \\\"eval_isr_std\\\": 0.3424, \\\"eval_proved_only_isr\\\": 0.8769, \\\"eval_median_isr\\\": 1, \\\"eval_n_proved\\\": 90, \\\"eval_n_problems\\\": 100, \\\"eval_component_count_mean\\\": 2.889, \\\"tautological_collapse\\\": true, \\\"train_final_prove_rate\\\": 0.855, \\\"train_final_mean_isr\\\": 0.532, \\\"h7_count\\\": 87, \\\"h7_rate\\\": 0.9667, \\\"h1_count\\\": 0, \\\"h1_rate\\\": 0, \\\"h1_near_count\\\": 1, \\\"h1_near_rate\\\": 0.0111, \\\"h8_conjunction_collapse_count\\\": 1, \\\"h8_conjunction_collapse_rate\\\": 0.0111, \\\"genuine_count\\\": 2, \\\"genuine_rate\\\": 0.0222, \\\"taxonomy_standard\\\": \\\"D086 clean run = ground truth. D084 residual removed.\\\"}}, \\\"plan002-additive-b01-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.89, \\\"eval_mean_isr\\\": 0.803, \\\"eval_isr_std\\\": null, \\\"eval_proved_only_isr\\\": 0.902, \\\"eval_n_proved\\\": 89, \\\"eval_n_problems\\\": 100, \\\"h7_count\\\": 89, \\\"h7_rate\\\": 1, \\\"h1_count\\\": 0, \\\"h1_rate\\\": 0, \\\"h8_conjunction_collapse_count\\\": 0, \\\"h8_conjunction_collapse_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"component_mean\\\": 4.33, \\\"comp_2_ratio\\\": 0.022, \\\"h7_fn_correction\\\": \\\"12 former genuine reclassified as H7: all n_prem=1 false negatives (normalization mismatch prevented conclusion matching)\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan013-random-reward-s42-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 1, \\\"eval_mean_isr\\\": 0.535, \\\"eval_isr_std\\\": 0.1282, \\\"eval_proved_only_isr\\\": 0.535, \\\"eval_median_isr\\\": 0.5, \\\"eval_n_proved\\\": 100, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_note\\\": \\\"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\\\"}}, \\\"plan001-exec-only-s43-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_sampling_prove_rate\\\": 0.14, \\\"eval_sampling_mean_isr\\\": 0, \\\"eval_sampling_n_proved\\\": 14, \\\"eval_sampling_temperature\\\": 0.7, \\\"eval_sampling_method\\\": \\\"do_sample=True, temperature=0.7\\\", \\\"eval_sampling_by_answer\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 6, \\\"prove_rate\\\": 0.176}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 2, \\\"prove_rate\\\": 0.08}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 6, \\\"prove_rate\\\": 0.146}}, \\\"eval_greedy_prove_rate\\\": 0.13, \\\"eval_greedy_mean_isr\\\": 0, \\\"eval_greedy_proved_only_isr\\\": 0, \\\"eval_greedy_n_proved\\\": 13, \\\"eval_greedy_method\\\": \\\"eval_sta.py default (do_sample=False)\\\", \\\"eval_greedy_by_answer\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 4, \\\"prove_rate\\\": 0.118}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 5, \\\"prove_rate\\\": 0.2}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 4, \\\"prove_rate\\\": 0.0976}}, \\\"eval_greedy_h7_count\\\": 0, \\\"eval_greedy_h7_rate\\\": 0, \\\"eval_greedy_h1_count\\\": 13, \\\"eval_greedy_h1_rate\\\": 1, \\\"eval_greedy_genuine_rate\\\": 0, \\\"eval_greedy_n_premises_proved_mean\\\": 17.92, \\\"eval_greedy_mean_components_proved\\\": 18.92, \\\"eval_greedy_n_premises_all_mean\\\": 32.67, \\\"eval_sampling_h1_rate\\\": 1, \\\"eval_sampling_h7_rate\\\": 0, \\\"eval_sampling_genuine_rate\\\": 0, \\\"eval_sampling_mean_components_proved\\\": 18.5, \\\"eval_greedy_vs_sampling_delta_pr\\\": -0.01, \\\"eval_method_note\\\": \\\"Greedy and sampling agree on failure profile (ISR*=0, H1=100%, components~18.5-18.9). s43 collapse is decoding-invariant.\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan001-exec-only-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan017-additive-random-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.48, \\\"eval_mean_isr\\\": 0.0453, \\\"eval_isr_std\\\": 0.0759, \\\"eval_median_isr\\\": 0, \\\"eval_max_isr\\\": 0.2857, \\\"eval_proved_only_isr\\\": 0.0943, \\\"eval_n_proved\\\": 48, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_component_count_mean\\\": 9.6, \\\"eval_component_count_2_ratio\\\": 0, \\\"tautological_collapse\\\": false, \\\"h7_rate\\\": 0, \\\"h7_count\\\": 0, \\\"h1_rate\\\": 1, \\\"h1_count\\\": 48, \\\"genuine_rate\\\": 0, \\\"genuine_count\\\": 0}}, \\\"plan002-additive-b01-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.81, \\\"eval_mean_isr\\\": 0.3365, \\\"eval_isr_std\\\": 0.3227, \\\"eval_proved_only_isr\\\": 0.4154, \\\"eval_median_isr\\\": 0.2, \\\"eval_n_proved\\\": 81, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_component_count_mean\\\": 5.58, \\\"h7_rate\\\": 0.16, \\\"h7_count\\\": 13, \\\"h1_rate\\\": 0.519, \\\"h1_count\\\": 42, \\\"h8_conjunction_collapse_count\\\": 12, \\\"h8_conjunction_collapse_rate\\\": 0.148, \\\"genuine_rate\\\": 0.173, \\\"genuine_count\\\": 14, \\\"tautological_collapse\\\": false, \\\"h8_audit_note\\\": \\\"2026-05-15: H8 conjunction collapse audit completed. 12/81 proved samples are H8. Genuine 26→14 (32.1%→17.3%). H8 JSON at /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json\\\"}}, \\\"plan002-additive-b01-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.61, \\\"eval_n_proved\\\": 61, \\\"eval_n_problems\\\": 100, \\\"eval_proved_only_isr\\\": 0.83, \\\"h7_count\\\": 59, \\\"h7_rate\\\": 0.9672, \\\"h1_count\\\": 0, \\\"h1_rate\\\": 0, \\\"h1_near_count\\\": 0, \\\"h1_near_rate\\\": 0, \\\"h8_conjunction_collapse_count\\\": 0, \\\"h8_conjunction_collapse_rate\\\": 0, \\\"genuine_count\\\": 2, \\\"genuine_rate\\\": 0.0328, \\\"proved_single_premise_ratio\\\": 1, \\\"taxonomy_note\\\": \\\"structurally determined: proved_single_premise_ratio=1.0, all taxonomy categories except H7 are zero by construction. eval file lost but classification derivable from structure.\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp1-isr-b03-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.91, \\\"mean_isr\\\": 0.2575, \\\"isr_std\\\": 0.2363, \\\"median_isr\\\": 0.3333, \\\"proved_only_mean_isr\\\": 0.283, \\\"hacking_rate_strict_h7\\\": 0.022, \\\"hacking_rate_functional\\\": 0.3297, \\\"genuine_rate\\\": 0.6703, \\\"genuine_count\\\": 61, \\\"n_proved\\\": 91, \\\"n_problems\\\": 100, \\\"h1_conclusion_in_premise\\\": 0.747, \\\"eval_data\\\": \\\"test_100.jsonl\\\", \\\"eval_output\\\": \\\"/root/autodl-tmp/outputs/eval_sta_exp1_isr_b03_s43.json\\\"}}, \\\"plan009-sft-baseline-s44-1000-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.15, \\\"eval_n_proved\\\": 15, \\\"eval_n_problems\\\": 100, \\\"eval_mean_isr\\\": 0.0884, \\\"eval_isr_std\\\": 0.2268, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.5892, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h1_count\\\": 1, \\\"h1_rate\\\": 0.0667, \\\"h8_conjunction_collapse_count\\\": 0, \\\"h8_conjunction_collapse_rate\\\": 0, \\\"genuine_count\\\": 14, \\\"genuine_rate\\\": 0.9333, \\\"eval_by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 15, \\\"prove_rate\\\": 0.441, \\\"mean_isr\\\": 0.26}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 0, \\\"prove_rate\\\": 0, \\\"mean_isr\\\": 0}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 0, \\\"prove_rate\\\": 0, \\\"mean_isr\\\": 0}}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan009-sft-baseline-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_final_loss\\\": 0.2397, \\\"train_last_step_loss\\\": 0.0328, \\\"train_token_accuracy\\\": 0.9928, \\\"train_epochs\\\": 7.94, \\\"train_runtime_sec\\\": 729.05, \\\"train_steps\\\": 500, \\\"eval_prove_rate\\\": 0.17, \\\"eval_n_proved\\\": 17, \\\"eval_n_problems\\\": 100, \\\"eval_mean_isr\\\": 0.0974, \\\"eval_isr_std\\\": 0.2409, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.5729, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_output_path\\\": \\\"/root/autodl-tmp/outputs/eval_sta_plan009_sft_s44.json\\\", \\\"eval_tautological_collapse\\\": false, \\\"eval_h7_count\\\": 0, \\\"eval_h7_rate\\\": 0, \\\"eval_h1_count\\\": 2, \\\"eval_h1_rate\\\": 0.118, \\\"eval_genuine_count\\\": 15, \\\"eval_genuine_rate\\\": 0.882, \\\"eval_by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 15, \\\"prove_rate\\\": 0.441, \\\"mean_isr\\\": 0.257}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 1, \\\"prove_rate\\\": 0.04, \\\"mean_isr\\\": 0.027}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 1, \\\"prove_rate\\\": 0.024, \\\"mean_isr\\\": 0.008}}, \\\"eval_correction_note\\\": \\\"Corrected 2026-05-15: previous eval used test_100.jsonl (50/44/6 distribution), re-evaled with proofwriter_fol_100.jsonl (34/25/41)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan009-sft-baseline-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.2391, \\\"train_token_accuracy\\\": 0.9938, \\\"train_epochs\\\": 7.94, \\\"train_runtime_sec\\\": 677.14, \\\"train_steps\\\": 500, \\\"eval_prove_rate\\\": 0.15, \\\"eval_mean_isr\\\": 0.0895, \\\"eval_isr_std\\\": 0.2338, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.5967, \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h1_count\\\": 1, \\\"h1_rate\\\": 0.067, \\\"genuine_count\\\": 14, \\\"genuine_rate\\\": 0.933, \\\"by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 13, \\\"prove_rate\\\": 0.382, \\\"mean_isr\\\": 0.234}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 1, \\\"prove_rate\\\": 0.04, \\\"mean_isr\\\": 0.027}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 1, \\\"prove_rate\\\": 0.024, \\\"mean_isr\\\": 0.008}}, \\\"eval_data_path\\\": \\\"data/proofwriter_fol_100.jsonl\\\", \\\"eval_output_path\\\": \\\"/root/autodl-tmp/outputs/eval_sta_plan009_sft_s43.json\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan001-exec-only-s44-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan001-exec-only-s43-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan009-sft-baseline-s44-1000-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan002-additive-b03-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_steps\\\": 500, \\\"duration_min\\\": 56.7, \\\"overall_prove_rate\\\": 0.34025, \\\"overall_isr\\\": 0.11527, \\\"last100_prove_rate\\\": 0.5525, \\\"eval_prove_rate\\\": 0.18, \\\"eval_mean_isr\\\": 0.0257, \\\"eval_isr_std\\\": 0.0742, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.1427, \\\"eval_n_proved\\\": 18, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"h7_rate\\\": 0, \\\"h7_count\\\": 0, \\\"h1_rate\\\": 0.778, \\\"h1_count\\\": 14, \\\"h8_conjunction_collapse_count\\\": 3, \\\"h8_conjunction_collapse_rate\\\": 0.1667, \\\"genuine_rate\\\": 0.0556, \\\"genuine_count\\\": 1, \\\"eval_by_type_false_pr\\\": 0.12, \\\"eval_by_type_false_isr\\\": 0.0102, \\\"eval_by_type_unknown_pr\\\": 0.195, \\\"eval_by_type_unknown_isr\\\": 0.0422, \\\"eval_by_type_true_pr\\\": 0.206, \\\"eval_by_type_true_isr\\\": 0.0172, \\\"h8_audit_note\\\": \\\"2026-05-15: H8 conjunction collapse added. genuine 4→1.\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan001-exec-only-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.93, \\\"eval_mean_isr\\\": 0.1232, \\\"eval_isr_std\\\": 0.1887, \\\"eval_proved_only_isr\\\": 0.1324, \\\"eval_median_isr\\\": 0, \\\"eval_n_proved\\\": 93, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"h7_rate\\\": 0, \\\"h7_count\\\": 0, \\\"h1_rate\\\": 0.871, \\\"h1_count\\\": 81, \\\"h8_conjunction_collapse_count\\\": 6, \\\"h8_conjunction_collapse_rate\\\": 0.0645, \\\"genuine_rate\\\": 0.0753, \\\"genuine_count\\\": 7, \\\"genuine_mean_isr\\\": 0.3141, \\\"h1_mean_isr\\\": 0.1055, \\\"conclusion_embedding_total\\\": 0.871, \\\"content_independent_predicates_count\\\": 1, \\\"h8_audit_note\\\": \\\"2026-05-15: H8 conjunction collapse added. genuine 12→7.\\\"}}, \\\"plan004-o1-ablation-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.63, \\\"mean_isr\\\": 0.0072, \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h1_count\\\": 63, \\\"h1_rate\\\": 1, \\\"h8_conjunction_collapse_count\\\": 2, \\\"h8_conjunction_collapse_rate\\\": 0.0317, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"content_independent_predicates_count\\\": 3, \\\"h8_audit_note\\\": \\\"2026-05-15: H8 conjunction collapse added. genuine unchanged (0).\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp1-isr-b03-s42-1000-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.95, \\\"eval_mean_isr\\\": 0.734, \\\"eval_isr_std\\\": 0.2575, \\\"eval_median_isr\\\": 0.6, \\\"eval_proved_only_isr\\\": 0.7726, \\\"eval_n_proved\\\": 95, \\\"eval_n_problems\\\": 100, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 25, \\\"prove_rate\\\": 1, \\\"mean_isr\\\": 0.824}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 38, \\\"prove_rate\\\": 0.927, \\\"mean_isr\\\": 0.673}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 32, \\\"prove_rate\\\": 0.941, \\\"mean_isr\\\": 0.741}}, \\\"h7_count\\\": 0, \\\"h7_rate\\\": 0, \\\"h1_count\\\": 54, \\\"h1_rate\\\": 0.568, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"tautological_collapse\\\": true, \\\"isr_1_count\\\": 41, \\\"isr_1_rate\\\": 0.432, \\\"single_premise_count\\\": 0, \\\"train_final_prove_rate\\\": 0.829, \\\"train_final_mean_isr\\\": 0.727, \\\"train_loss\\\": 0.0041, \\\"train_runtime_seconds\\\": 6280, \\\"train_final_entropy\\\": 9e-06, \\\"completions_mean_length\\\": 47, \\\"h8_conjunction_collapse_count\\\": 41, \\\"h8_conjunction_collapse_rate\\\": 0.432, \\\"content_independent_predicates\\\": true}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan018-additive-random-b01-s42-1000-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_final_prove_rate\\\": 0.989, \\\"train_final_mean_isr\\\": 0.353, \\\"train_final_reward\\\": 1.062, \\\"train_steps\\\": 1000, \\\"train_runtime_seconds\\\": 2957, \\\"eval_prove_rate\\\": 1, \\\"eval_mean_isr\\\": 0.3333, \\\"eval_isr_std\\\": 0, \\\"eval_median_isr\\\": 0.3333, \\\"eval_proved_only_isr\\\": 0.3333, \\\"eval_n_proved\\\": 100, \\\"eval_n_problems\\\": 100, \\\"eval_component_count_mean\\\": 3, \\\"genuine_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"tautological_collapse\\\": true, \\\"h7_rate\\\": null, \\\"h7_count\\\": null, \\\"h1_rate\\\": null, \\\"h1_count\\\": null}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan018-additive-random-b01-s42-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp1-isr-b03-s42-1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan001-exec-only-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.98, \\\"eval_mean_isr\\\": 0.57, \\\"eval_isr_std\\\": 0.2013, \\\"eval_median_isr\\\": 0.5, \\\"eval_proved_only_isr\\\": 0.5816, \\\"eval_n_proved\\\": 98, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_component_count_mean\\\": 2.04, \\\"eval_component_count_2\\\": 94, \\\"eval_component_count_3\\\": 4, \\\"tautological_collapse\\\": true, \\\"h7_rate\\\": 1, \\\"h7_count\\\": 97, \\\"h1_rate\\\": 0, \\\"h1_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"conclusion_embedding_total\\\": 1}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan018-additive-random-b01-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"h7_rate\\\": 0, \\\"h7_count\\\": 0, \\\"h1_rate\\\": 93.2, \\\"h1_count\\\": 82, \\\"genuine_rate\\\": 6.8, \\\"genuine_count\\\": 6, \\\"eval_prove_rate\\\": 0.88, \\\"eval_mean_isr\\\": 0.058}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp1-random-b03-s44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.23, \\\"eval_proved_only_mean_isr\\\": 0, \\\"eval_mean_isr\\\": 0, \\\"eval_isr_std\\\": 0, \\\"eval_median_isr\\\": 0, \\\"eval_n_proved\\\": 23, \\\"eval_n_problems\\\": 100, \\\"eval_h7_strict_rate\\\": 0, \\\"eval_h7_strict_count\\\": 0, \\\"eval_h1_strict_rate\\\": 1, \\\"eval_h1_strict_count\\\": 23, \\\"eval_genuine_rate\\\": 0, \\\"eval_genuine_count\\\": 0, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\"}}, \\\"exp1-isr-b03-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_step\\\": 500, \\\"prove_rate\\\": 0.56125, \\\"mean_isr\\\": 0.1515, \\\"parse_rate\\\": 1, \\\"train_loss\\\": 0.0176, \\\"train_runtime_sec\\\": 4153.6, \\\"epoch\\\": 2, \\\"eval_prove_rate\\\": 0.86, \\\"eval_mean_isr\\\": 0.2535, \\\"eval_isr_std\\\": 0.2406, \\\"eval_median_isr\\\": 0.3333, \\\"eval_proved_only_mean_isr\\\": 0.2948, \\\"eval_min_isr\\\": 0, \\\"eval_max_isr\\\": 0.75, \\\"eval_n_proved\\\": 86, \\\"eval_n_problems\\\": 100, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_h7_strict_rate\\\": 0.047, \\\"eval_h7_strict_count\\\": 4, \\\"eval_h1_strict_rate\\\": 0.686, \\\"eval_h1_strict_count\\\": 59, \\\"eval_conclusion_in_premise_rate\\\": 0.733, \\\"eval_conclusion_in_premise_count\\\": 63, \\\"eval_genuine_rate\\\": 0.267, \\\"eval_genuine_count\\\": 23, \\\"eval_single_premise_rate\\\": 0.058, \\\"eval_single_premise_count\\\": 5, \\\"eval_isr_1_count\\\": 0, \\\"eval_by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 23, \\\"prove_rate\\\": 0.92, \\\"mean_isr\\\": 0.334}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 35, \\\"prove_rate\\\": 0.854, \\\"mean_isr\\\": 0.199}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 28, \\\"prove_rate\\\": 0.824, \\\"mean_isr\\\": 0.26}}}}, \\\"exp1-random-b03-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan015-linear-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp1-isr-b03-s43-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp1-random-b03-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp1-isr-b03-s44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.95, \\\"mean_isr\\\": 0.705, \\\"isr_std\\\": 0.172, \\\"proved_only_isr\\\": 0.7421, \\\"n_proved\\\": 95, \\\"n_problems\\\": 100, \\\"h7_rate\\\": 1, \\\"h7_count\\\": 95, \\\"h1_rate\\\": 0, \\\"h1_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"genuine_count\\\": 0, \\\"single_premise_rate\\\": 1, \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_note\\\": \\\"Re-eval with correct test set (D062). Previous test_100.jsonl results invalidated.\\\"}}, \\\"exp1-random-b03-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp1-isr-b03-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp1-isr-b03-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp2-exec-s43-greedy\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp4-100step-h1h7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan006-prolog-sta-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"pass_rate\\\": 0.97, \\\"isr_mean\\\": 0.885, \\\"isr_n_cl_ge3\\\": \\\"N/A (0 samples)\\\", \\\"n_clauses_dist\\\": \\\"78/100 single-clause, 22/100 two-clause\\\", \\\"h7_functional_rate\\\": 0.979, \\\"genuine_rate\\\": 0, \\\"premise_count_analysis\\\": \\\"100% artifact - zero samples with n_clauses>=3, model exclusively generates 1-2 clause programs\\\", \\\"failure_mode\\\": \\\"query-as-fact gaming (total H7 collapse)\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan006-prolog-sta-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train\\\": {\\\"final_prove_rate\\\": 0.769, \\\"final_mean_isr\\\": 0.129, \\\"final_loss\\\": 0.0155, \\\"final_entropy\\\": 0.09, \\\"final_reward\\\": 0.573, \\\"completion_length_mean\\\": 143, \\\"train_runtime_seconds\\\": 5095, \\\"train_runtime_minutes\\\": 84.9}, \\\"eval\\\": {\\\"n_problems\\\": 100, \\\"n_proved\\\": 38, \\\"prove_rate\\\": 0.38, \\\"mean_isr\\\": 0.0704, \\\"isr_std\\\": 0.1263, \\\"median_isr\\\": 0, \\\"proved_only_mean_isr\\\": 0.1853, \\\"min_isr\\\": 0, \\\"max_isr\\\": 1, \\\"by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 11, \\\"prove_rate\\\": 0.44, \\\"mean_isr\\\": 0.1003}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 11, \\\"prove_rate\\\": 0.268, \\\"mean_isr\\\": 0.0394}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 16, \\\"prove_rate\\\": 0.471, \\\"mean_isr\\\": 0.0859}}}, \\\"h7_classification\\\": {\\\"h7_strict\\\": 0, \\\"h7_rate\\\": 0, \\\"h1_strict\\\": 37, \\\"h1_rate\\\": 0.974, \\\"conclusion_in_premise_total\\\": 37, \\\"conclusion_in_premise_rate\\\": 0.974, \\\"genuine_count\\\": 0, \\\"genuine_rate\\\": 0, \\\"isr_1_count\\\": 1, \\\"note\\\": \\\"1 pseudo-genuine sample (folio_1415) has query embedded in single mega-clause; all 38/38 proved samples are tautological\\\"}}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan006-prolog-sta-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"cumulative_prove_rate\\\": 0.848, \\\"cumulative_mean_isr\\\": 0.787, \\\"final_prove_rate\\\": 1, \\\"final_isr\\\": 1, \\\"final_reward\\\": 1, \\\"saturation_onset_step\\\": 100, \\\"train_loss\\\": 0.00716, \\\"training_hours\\\": 0.78, \\\"final_entropy\\\": 0.01, \\\"final_completion_length\\\": 27, \\\"initial_completion_length\\\": 120, \\\"steps_at_perfect_reward\\\": 400, \\\"train_runtime_sec\\\": 2791, \\\"eval_prove_rate\\\": 0.5, \\\"eval_mean_isr\\\": 0.5, \\\"eval_proved_only_isr\\\": 1, \\\"eval_h7_rate\\\": 1, \\\"eval_h7_count\\\": 50, \\\"eval_proved_count\\\": 50, \\\"eval_total_count\\\": 100, \\\"eval_n_clauses_mean\\\": 1, \\\"eval_isr_distribution\\\": \\\"binary: 50x0 + 50x1\\\"}}, \\\"plan006-prolog-exec-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.21, \\\"eval_mean_isr\\\": 0.0812, \\\"eval_isr_std\\\": 0.2343, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.3866, \\\"eval_min_isr\\\": 0, \\\"eval_max_isr\\\": 1, \\\"eval_n_proved\\\": 21, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_elapsed_seconds\\\": 683.9, \\\"eval_by_type_false_pr\\\": 0.04, \\\"eval_by_type_false_isr\\\": 0.04, \\\"eval_by_type_unknown_pr\\\": 0.317, \\\"eval_by_type_unknown_isr\\\": 0.099, \\\"eval_by_type_true_pr\\\": 0.206, \\\"eval_by_type_true_isr\\\": 0.09, \\\"solver\\\": \\\"PrologSolver\\\", \\\"logic_type\\\": \\\"prolog\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan009-sft-baseline-s42-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.14, \\\"eval_mean_isr\\\": 0.08, \\\"eval_isr_std\\\": 0.214, \\\"eval_median_isr\\\": 0, \\\"eval_max_isr\\\": 0.833, \\\"eval_proved_only_isr\\\": 0.571, \\\"eval_n_proved\\\": 14, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"train_final_loss\\\": 0.0287, \\\"train_token_accuracy\\\": 0.9935, \\\"train_epochs\\\": 7.94, \\\"train_runtime_sec\\\": 789.6, \\\"by_answer_type\\\": {\\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 13, \\\"pr\\\": 0.382, \\\"isr\\\": 0.226}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 1, \\\"pr\\\": 0.024, \\\"isr\\\": 0.008}, \\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 0, \\\"pr\\\": 0, \\\"isr\\\": 0}}, \\\"h7_rate\\\": 0, \\\"h7_count\\\": 0, \\\"h1_rate\\\": 0.071, \\\"h1_count\\\": 1, \\\"genuine_rate\\\": 0.929, \\\"genuine_count\\\": 13, \\\"hacking_patterns\\\": \\\"near-zero (1/14 H1, 0 H7, 92.9% genuine)\\\", \\\"tautological_collapse\\\": false}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan006-prolog-exec-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.56, \\\"eval_mean_isr\\\": 0.0084, \\\"eval_isr_std\\\": 0.0221, \\\"eval_median_isr\\\": 0, \\\"eval_proved_only_isr\\\": 0.015, \\\"eval_min_isr\\\": 0, \\\"eval_max_isr\\\": 0.1, \\\"eval_n_proved\\\": 56, \\\"eval_n_problems\\\": 100, \\\"eval_method\\\": \\\"eval_sta.py full STA\\\", \\\"eval_data\\\": \\\"proofwriter_fol_100.jsonl\\\", \\\"eval_elapsed_seconds\\\": 868.2, \\\"eval_by_type_false_pr\\\": 0.48, \\\"eval_by_type_false_isr\\\": 0.0043, \\\"eval_by_type_unknown_pr\\\": 0.6585, \\\"eval_by_type_unknown_isr\\\": 0.0114, \\\"eval_by_type_true_pr\\\": 0.5, \\\"eval_by_type_true_isr\\\": 0.0078, \\\"solver\\\": \\\"PrologSolver\\\", \\\"logic_type\\\": \\\"prolog\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan018-additive-random-b01-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.89, \\\"mean_isr\\\": 0.0619, \\\"isr_std\\\": 0.1756, \\\"median_isr\\\": 0, \\\"proved_only_mean_isr\\\": 0.0695, \\\"n_proved\\\": 89, \\\"n_problems\\\": 100, \\\"max_isr\\\": 1, \\\"min_isr\\\": 0, \\\"isr_pr_ratio\\\": 0.0695, \\\"isr_zero_count\\\": 72, \\\"isr_one_count\\\": 2, \\\"by_answer_type\\\": {\\\"false\\\": {\\\"count\\\": 25, \\\"proved\\\": 21, \\\"prove_rate\\\": 0.84, \\\"mean_isr\\\": 0.0533}, \\\"unknown\\\": {\\\"count\\\": 41, \\\"proved\\\": 40, \\\"prove_rate\\\": 0.976, \\\"mean_isr\\\": 0.0892}, \\\"true\\\": {\\\"count\\\": 34, \\\"proved\\\": 28, \\\"prove_rate\\\": 0.824, \\\"mean_isr\\\": 0.0353}}, \\\"elapsed_seconds\\\": 1012.7, \\\"eval_method\\\": \\\"eval_sta.py with Prover9Solver, FOL\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan009-sft-baseline-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"plan006-prolog-exec-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan006-prolog-exec-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_prove_rate\\\": 0.83, \\\"eval_mean_isr\\\": 0.031, \\\"eval_proved_only_isr\\\": 0.037, \\\"eval_median_isr\\\": 0, \\\"eval_max_isr\\\": 0.2, \\\"eval_isr_std\\\": 0.0534, \\\"h7_rate\\\": 0, \\\"h1_rate\\\": 0, \\\"isr_1_rate\\\": 0, \\\"single_premise_rate\\\": 0, \\\"by_answer_type\\\": {\\\"true\\\": {\\\"proved\\\": 37, \\\"count\\\": 40, \\\"pr\\\": 0.925, \\\"isr\\\": 0.037}, \\\"false\\\": {\\\"proved\\\": 21, \\\"count\\\": 29, \\\"pr\\\": 0.724, \\\"isr\\\": 0.038}, \\\"unknown\\\": {\\\"proved\\\": 25, \\\"count\\\": 31, \\\"pr\\\": 0.806, \\\"isr\\\": 0.016}}}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"plan006-prolog-exec-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"plan009-sft-baseline-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan009-sft-baseline-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan018-additive-random-b01-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan012-hacking-taxonomy\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"isr_b01_genuine_rate\\\": 0.259, \\\"random_b01_genuine_rate\\\": 0.177, \\\"genuine_rate_delta_pp\\\": 8.2, \\\"isr_b01_conclusion_embedding_rate\\\": 0.728, \\\"random_b01_conclusion_embedding_rate\\\": 0.785, \\\"isr_b01_genuine_mean_isr\\\": 0.6723, \\\"random_b01_genuine_mean_isr\\\": 0.3427, \\\"isr_b01_complexity_wo_utility_rate\\\": 0, \\\"random_b01_complexity_wo_utility_rate\\\": 0.038, \\\"isr_b01_hacking_rate\\\": 0.741, \\\"random_b01_hacking_rate\\\": 0.823}}, \\\"plan005-sta-low-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"total_steps\\\": 500, \\\"duration_min\\\": 71, \\\"parse_rate\\\": 1, \\\"overall_prove_rate\\\": 0.5657, \\\"overall_isr\\\": 0.1682, \\\"last50_prove_rate\\\": 0.77, \\\"last50_isr\\\": 0.2559, \\\"last100_prove_rate\\\": 0.7725, \\\"last100_isr\\\": 0.2299, \\\"last100_loss\\\": 0.022752, \\\"overall_loss\\\": 0.017296, \\\"last100_isr_pr_ratio\\\": 0.298, \\\"last100_isr_lt_pr_count\\\": \\\"99/100\\\", \\\"first_rolling10_pr_ge_0.8\\\": 178, \\\"first_rolling10_pr_ge_0.9\\\": 439, \\\"max_rolling10_pr\\\": 0.9375, \\\"max_rolling10_isr\\\": 0.3282, \\\"windowed\\\": {\\\"1-50\\\": {\\\"pr\\\": 0.1775, \\\"isr\\\": 0.0906}, \\\"51-100\\\": {\\\"pr\\\": 0.1775, \\\"isr\\\": 0.0835}, \\\"101-200\\\": {\\\"pr\\\": 0.5062, \\\"isr\\\": 0.1463}, \\\"201-300\\\": {\\\"pr\\\": 0.6713, \\\"isr\\\": 0.1791}, \\\"301-400\\\": {\\\"pr\\\": 0.7013, \\\"isr\\\": 0.1984}, \\\"401-500\\\": {\\\"pr\\\": 0.7725, \\\"isr\\\": 0.2299}}}}, \\\"plan014-downstream-nli-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"overall_accuracy\\\": 0.341, \\\"proved_rate\\\": 0.915, \\\"proved_count\\\": 732, \\\"total_generations\\\": 800, \\\"parse_errors\\\": 0, \\\"accuracy_by_label\\\": {\\\"true\\\": 0.912, \\\"false\\\": 0, \\\"unknown\\\": 0.076}, \\\"spearman_rho\\\": -0.049, \\\"spearman_p\\\": 0.187, \\\"mann_whitney_U\\\": 17202, \\\"mann_whitney_p\\\": 0.288, \\\"bon_isr_accuracy\\\": 0.35, \\\"bon_random_accuracy\\\": 0.341, \\\"bon_oracle_accuracy\\\": 0.44, \\\"bon_prove_first_accuracy\\\": 0.35, \\\"isr_bucket_high_acc\\\": 0.75, \\\"isr_bucket_mid_acc\\\": 0.377, \\\"isr_bucket_low_acc\\\": 0.327, \\\"runtime_inference_s\\\": 408.8, \\\"runtime_eval_s\\\": 13.6}}, \\\"plan001-exec-only-s43-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan013-random-reward-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan001-exec-only-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan013-random-reward-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan013-random-reward-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan001-exec-only-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan003-eval-exec-only-r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"prove_rate\\\": 0.32, \\\"mean_isr\\\": 0.2055, \\\"isr_std\\\": 0.3194, \\\"proved_only_isr\\\": 0.6423, \\\"isr_by_type\\\": {\\\"true\\\": 0.3598, \\\"false\\\": 0.1723, \\\"unknown\\\": 0.0979}, \\\"total_samples\\\": 100, \\\"proved_count\\\": 32, \\\"runtime_s\\\": 251.7}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan001-exec-only-s42-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-sta-r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.1, \\\"mean_isr\\\": 0.04347, \\\"last20_prove_rate\\\": 0.15, \\\"last20_isr_mean\\\": 0.04956, \\\"first20_prove_rate\\\": 0.08125, \\\"first20_isr_mean\\\": 0.05182, \\\"overall_reward_mean\\\": 0.07174, \\\"last20_reward_mean\\\": 0.09978, \\\"training_steps\\\": 100, \\\"training_minutes\\\": 16.9, \\\"step_time_s\\\": 10.13, \\\"isr_pr_ratio_overall\\\": 0.43, \\\"isr_pr_ratio_last20\\\": 0.33, \\\"K\\\": 8}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"sta-phase1-exec-only-r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.15125, \\\"mean_isr\\\": 0.1475, \\\"last20_prove_rate\\\": 0.2, \\\"last20_isr_mean\\\": 0.2, \\\"first20_prove_rate\\\": 0.11875, \\\"first20_isr_mean\\\": 0.11875, \\\"overall_reward_mean\\\": 0.15125, \\\"last20_reward_mean\\\": 0.2, \\\"training_steps\\\": 100, \\\"training_minutes\\\": 15.7, \\\"step_time_s\\\": 9.44, \\\"isr_pr_ratio_last20\\\": 1, \\\"K\\\": 8}, \\\"conclusion\\\": \\\"success\\\"}, \\\"sta-phase1-exec-sta-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.1575, \\\"mean_isr\\\": 0.1525, \\\"last20_prove_rate\\\": 0.2125, \\\"last20_isr_mean\\\": 0.2125, \\\"first20_reward_mean\\\": 0.119, \\\"training_steps\\\": 100, \\\"training_minutes\\\": 15}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"sta-phase1-exec-only-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"parse_rate\\\": 1, \\\"prove_rate\\\": 0.15125, \\\"mean_isr\\\": 0.1475, \\\"last20_prove_rate\\\": 0.2, \\\"last20_isr_mean\\\": 0.2, \\\"first20_reward_mean\\\": 0.119, \\\"training_steps\\\": 100, \\\"training_minutes\\\": 15}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"sta-phase1-exec-only-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-sta-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-sta-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-only-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-sta\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-phase1-exec-only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sta-gt-isr-baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gt_prove_rate\\\": 0.18, \\\"gt_mean_isr\\\": 0.5588, \\\"gt_isr_std\\\": 0.2582, \\\"gt_isr_median\\\": 0.6125, \\\"solver_execution_rate\\\": 1, \\\"true_prove_rate\\\": 0.5, \\\"true_mean_isr\\\": 0.5833}}, \\\"sta-phase0-baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"mean_isr\\\": 0.0641, \\\"isr_std\\\": 0.1983, \\\"median_isr\\\": 0, \\\"isr_range\\\": [0, 0.889], \\\"prove_rate\\\": 0.12, \\\"proved_count\\\": 12, \\\"total_samples\\\": 100, \\\"xor_affected_samples\\\": 34, \\\"effective_prove_rate_no_xor\\\": 0.182, \\\"avg_time_per_sample_s\\\": 3.4, \\\"total_runtime_s\\\": 336, \\\"isr_by_answer\\\": {\\\"true\\\": {\\\"n\\\": 34, \\\"proved\\\": 9, \\\"prove_rate\\\": 0.265, \\\"mean_isr\\\": 0.1345}, \\\"false\\\": {\\\"n\\\": 25, \\\"proved\\\": 1, \\\"prove_rate\\\": 0.04, \\\"mean_isr\\\": 0.024}, \\\"unknown\\\": {\\\"n\\\": 41, \\\"proved\\\": 2, \\\"prove_rate\\\": 0.049, \\\"mean_isr\\\": 0.0302}}}, \\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 86, \\\"total\\\": 86, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3107}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan018-additive-random-b01-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.79, \"eval_mean_isr\": 0.1038, \"eval_isr_std\": 0.1369, \"eval_median_isr\": 0.0357, \"eval_proved_only_isr\": 0.1314, \"eval_n_proved\": 79, \"eval_n_problems\": 100, \"tautological_collapse\": false, \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 58, \"h1_rate\": 0.7342, \"h8_count\": 4, \"h8_rate\": 0.0506, \"genuine_count\": 18, \"genuine_rate\": 0.2278, \"taxonomy_tool\": \"classify_h7.py standard (2026-05-15)\", \"taxonomy_note\": \"Re-classified with current classify_h7.py. Old values: genuine_strict=12 (H1_exact=56, H1_near=8, H8=3). New standard: H1=58 (2 former H1-near now H1), H8=4, genuine=18. Standard definition: proved - H7 - H1 - H8.\"}}, \"plan018-additive-random-b01-s43-r3\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.94, \"n_proved\": 94, \"n_problems\": 100, \"mean_isr\": 0.1406, \"isr_std\": null, \"proved_only_isr\": 0.1495, \"h7_count\": 36, \"h7_rate\": 0.383, \"h7a_count\": 36, \"h7b_count\": 0, \"h1_count\": 56, \"h1_rate\": 0.596, \"h8_count\": 1, \"h8_rate\": 0.011, \"genuine_count\": 1, \"genuine_rate\": 0.0106, \"train_prove_rate\": 0.5825, \"train_mean_isr\": 0.1266}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s44-r2\": {\"status\": \"RUNNING\"}, \"plan002-additive-b01-s43-r2\": {\"status\": \"DONE\", \"metrics\": {\"eval_n_problems\": 100, \"eval_n_proved\": 61, \"eval_prove_rate\": 0.61, \"eval_mean_isr\": 0.5063, \"eval_isr_std\": 0.4518, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.8301, \"h7a_count\": 59, \"h7b_count\": 2, \"h7_count\": 61, \"h7_rate\": 1, \"h1_count\": 0, \"h1_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"proved_single_premise_ratio\": 1, \"content_independent_predicates\": 5, \"isr_eq_1_count\": 40, \"isr_eq_1_rate_of_proved\": 0.656, \"train_prove_rate\": 0.68775, \"train_mean_isr\": 0.5039}, \"conclusion\": \"negative\"}, \"plan001-exec-only-s43-1000-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"prove_rate\": 0.9, \"n_proved\": 90, \"n_problems\": 100, \"mean_isr\": 0.531, \"isr_std\": 0.15, \"isr_corrected\": 0.465, \"isr_artifact_note\": \"n_components=3 quantifier decomposition artifact (+0.066) + $T solver bug 5 samples (+0.025). Corrected ISR=0.465, but both values entirely from H7a tautological necessity, no reasoning quality signal.\", \"h7_count\": 90, \"h7_rate\": 1, \"h7a_count\": 90, \"h7b_count\": 0, \"h1_count\": 0, \"h1_rate\": 0, \"h8_count\": 0, \"h8_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0}}, \"plan016-extended-1000-s42\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.96, \"n_proved\": 96, \"n_problems\": 100, \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 96, \"h1_rate\": 1, \"h8_count\": 0, \"h8_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"genuine_h1_near\": 0, \"genuine_strict\": 0, \"content_independent_rate\": 1, \"single_premise_rate\": 0, \"taxonomy_audit\": \"2026-05-15\", \"taxonomy_tool\": \"classify_h7.py current version (with H8 detection)\", \"taxonomy_note\": \"Re-run with current classify_h7.py. Old value genuine=7 was incorrect (old version lacked H8 and had weaker H1 detection). All 96 proved are H1 (conclusion embedded in premises). 0 H7, 0 H8.\"}, \"conclusion\": \"success\"}, \"plan001-exec-only-s44-1000-r2\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 1, \"n_proved\": 100, \"n_problems\": 100, \"mean_isr\": 0.002, \"isr_std\": 0.0146, \"h7_count\": 0, \"h7_rate\": 0, \"h7a_count\": 0, \"h7b_count\": 0, \"h1_count\": 85, \"h1_rate\": 0.85, \"h8_count\": 15, \"h8_rate\": 0.15, \"genuine_count\": 0, \"genuine_rate\": 0, \"genuine_note\": \"D091: 3 samples escape text-match classifiers but are functionally degenerate (ISR=0, disjunctive/commuted bypasses)\"}, \"conclusion\": \"success\"}, \"plan018-additive-random-b01-s42-1000-r3\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.97, \"eval_mean_isr\": 0.6892, \"eval_isr_std\": 0.2037, \"eval_median_isr\": 0.75, \"eval_proved_only_isr\": 0.7105, \"eval_n_proved\": 97, \"eval_n_problems\": 100, \"genuine_count\": 0, \"genuine_rate\": 0, \"h1_count\": 0, \"h1_rate\": 0, \"h7_count\": 97, \"h7_rate\": 1, \"tautological_collapse\": true, \"train_final_prove_rate\": 0.827, \"train_final_mean_isr\": 0.5213, \"train_loss\": 0.00671, \"train_final_entropy\": 0.003, \"train_runtime_seconds\": 5783, \"train_steps\": 1000, \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 25, \"prove_rate\": 1, \"mean_isr\": 0.7533}, \"unknown\": {\"count\": 41, \"proved\": 39, \"prove_rate\": 0.951, \"mean_isr\": 0.6565}, \"true\": {\"count\": 34, \"proved\": 33, \"prove_rate\": 0.971, \"mean_isr\": 0.6814}}, \"n_premise_distribution\": {\"1\": 97}, \"pattern_description\": \"All 97 proved: 1 premise identical to conclusion (P therefore P). D088 correction: h7=97 h1=0 (was h1=97 h7=0 pre-D086 bugfix).\"}, \"conclusion\": \"negative\"}, \"plan009-sft-baseline-s44-1000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"prove_rate\": 0.15, \"n_proved\": 15, \"n_problems\": 100, \"mean_isr\": 0.0884, \"isr_std\": 0.2268, \"median_isr\": 0, \"proved_only_mean_isr\": 0.5892, \"max_isr\": 0.8571, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.4412}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0}}, \"genuine_count\": 14, \"genuine_rate\": 0.9333, \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0667, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0667, \"content_independent_count\": 0, \"content_independent_rate\": 0, \"isr_1_count\": 0, \"isr_1_rate\": 0, \"train_final_loss\": 0.0171, \"train_avg_loss\": 0.1544, \"train_token_accuracy\": 0.995, \"train_runtime_s\": 1580.97, \"eval_elapsed_s\": 391.8}}, \"plan009-sft-baseline-s43-1000\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.11, \"n_proved\": 11, \"n_problems\": 100, \"mean_isr\": 0.0699, \"isr_std\": 0.2155, \"median_isr\": 0, \"proved_only_mean_isr\": 0.6352, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 11, \"prove_rate\": 0.3235}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0}}, \"genuine_count\": 10, \"genuine_rate\": 0.9091, \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0909, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0909, \"content_independent_count\": 0, \"content_independent_rate\": 0, \"isr_1_count\": 1, \"isr_1_rate\": 0.0909, \"train_final_loss\": 0.0167, \"train_avg_loss\": 0.1551, \"train_token_accuracy\": 0.9954, \"train_runtime_s\": 1584.79, \"eval_elapsed_s\": 326.1}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s42-1000\": {\"status\": \"DONE\", \"metrics\": {\"train_final_loss\": 0.0168, \"train_last_step_loss\": 0.0168, \"train_token_accuracy\": 0.9955, \"train_epochs\": 15.88, \"train_runtime_sec\": 1415, \"train_steps\": 1000, \"eval_prove_rate\": 0.13, \"eval_n_proved\": 13, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0738, \"eval_isr_std\": 0.2077, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5677, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"eval_output_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json\", \"h7_strict_count\": 0, \"h7_strict_rate\": 0, \"h1_strict_count\": 1, \"h1_strict_rate\": 0.0769, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 12, \"genuine_rate\": 0.9231, \"conclusion_in_premise_count\": 1, \"conclusion_in_premise_rate\": 0.0769, \"isr_1_count\": 0, \"content_independent_count\": 0, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 12, \"prove_rate\": 0.353, \"mean_isr\": 0.209}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.011}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}}}, \"conclusion\": \"success\"}, \"exp1-random-b03-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.79, \"mean_isr\": 0.1745, \"isr_std\": 0.1628, \"median_isr\": 0.1667, \"proved_only_mean_isr\": 0.2209, \"hacking_rate_strict_h7\": 0, \"hacking_rate_functional\": 0.1013, \"genuine_rate\": 0.8987, \"genuine_count\": 71, \"n_proved\": 79, \"n_problems\": 100, \"h1_conclusion_in_premise\": 0.759, \"eval_data\": \"test_100.jsonl\", \"eval_output\": \"/root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43.json\"}}, \"exp1-random-b03-s43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_step\": 500, \"prove_rate\": 0.5505, \"mean_isr\": 0.1358, \"parse_rate\": 1, \"train_loss\": 0.01365, \"train_runtime_sec\": 6161.1, \"epoch\": 2, \"eval_prove_rate\": 0.92, \"eval_mean_isr\": 0.1659, \"eval_isr_std\": 0.1147, \"eval_median_isr\": 0.1429, \"eval_proved_only_mean_isr\": 0.1803, \"eval_min_isr\": 0, \"eval_max_isr\": 0.5, \"eval_n_proved\": 92, \"eval_n_problems\": 100, \"eval_h7_strict_rate\": 0.076, \"eval_h7_strict_count\": 7, \"eval_h1_strict_rate\": 0.891, \"eval_h1_strict_count\": 82, \"eval_genuine_rate\": 0.0326, \"eval_genuine_count\": 3, \"eval_isr0_count\": 6, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 23, \"prove_rate\": 0.92, \"mean_isr\": 0.156}, \"unknown\": {\"count\": 41, \"proved\": 37, \"prove_rate\": 0.902, \"mean_isr\": 0.184}, \"true\": {\"count\": 34, \"proved\": 32, \"prove_rate\": 0.941, \"mean_isr\": 0.151}}, \"D086_correction\": \"H1 90→82, genuine 2→3 per D086 clean batch run\"}}, \"plan002-additive-b01-s42-1000\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.9, \"eval_mean_isr\": 0.7892, \"eval_isr_std\": 0.3424, \"eval_proved_only_isr\": 0.8769, \"eval_median_isr\": 1, \"eval_n_proved\": 90, \"eval_n_problems\": 100, \"eval_component_count_mean\": 2.889, \"tautological_collapse\": true, \"train_final_prove_rate\": 0.855, \"train_final_mean_isr\": 0.532, \"h7_count\": 87, \"h7_rate\": 0.9667, \"h1_count\": 0, \"h1_rate\": 0, \"h1_near_count\": 1, \"h1_near_rate\": 0.0111, \"h8_conjunction_collapse_count\": 1, \"h8_conjunction_collapse_rate\": 0.0111, \"genuine_count\": 2, \"genuine_rate\": 0.0222, \"taxonomy_standard\": \"D086 clean run = ground truth. D084 residual removed.\"}}, \"plan002-additive-b01-s44\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.89, \"eval_mean_isr\": 0.803, \"eval_isr_std\": null, \"eval_proved_only_isr\": 0.902, \"eval_n_proved\": 89, \"eval_n_problems\": 100, \"h7_count\": 89, \"h7_rate\": 1, \"h1_count\": 0, \"h1_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 0, \"genuine_rate\": 0, \"component_mean\": 4.33, \"comp_2_ratio\": 0.022, \"h7_fn_correction\": \"12 former genuine reclassified as H7: all n_prem=1 false negatives (normalization mismatch prevented conclusion matching)\"}, \"conclusion\": \"negative\"}, \"plan013-random-reward-s42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 1, \"eval_mean_isr\": 0.535, \"eval_isr_std\": 0.1282, \"eval_proved_only_isr\": 0.535, \"eval_median_isr\": 0.5, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\"}}, \"plan001-exec-only-s43-r4\": {\"status\": \"DONE\", \"metrics\": {\"eval_sampling_prove_rate\": 0.14, \"eval_sampling_mean_isr\": 0, \"eval_sampling_n_proved\": 14, \"eval_sampling_temperature\": 0.7, \"eval_sampling_method\": \"do_sample=True, temperature=0.7\", \"eval_sampling_by_answer\": {\"true\": {\"count\": 34, \"proved\": 6, \"prove_rate\": 0.176}, \"false\": {\"count\": 25, \"proved\": 2, \"prove_rate\": 0.08}, \"unknown\": {\"count\": 41, \"proved\": 6, \"prove_rate\": 0.146}}, \"eval_greedy_prove_rate\": 0.13, \"eval_greedy_mean_isr\": 0, \"eval_greedy_proved_only_isr\": 0, \"eval_greedy_n_proved\": 13, \"eval_greedy_method\": \"eval_sta.py default (do_sample=False)\", \"eval_greedy_by_answer\": {\"true\": {\"count\": 34, \"proved\": 4, \"prove_rate\": 0.118}, \"false\": {\"count\": 25, \"proved\": 5, \"prove_rate\": 0.2}, \"unknown\": {\"count\": 41, \"proved\": 4, \"prove_rate\": 0.0976}}, \"eval_greedy_h7_count\": 0, \"eval_greedy_h7_rate\": 0, \"eval_greedy_h1_count\": 13, \"eval_greedy_h1_rate\": 1, \"eval_greedy_genuine_rate\": 0, \"eval_greedy_n_premises_proved_mean\": 17.92, \"eval_greedy_mean_components_proved\": 18.92, \"eval_greedy_n_premises_all_mean\": 32.67, \"eval_sampling_h1_rate\": 1, \"eval_sampling_h7_rate\": 0, \"eval_sampling_genuine_rate\": 0, \"eval_sampling_mean_components_proved\": 18.5, \"eval_greedy_vs_sampling_delta_pr\": -0.01, \"eval_method_note\": \"Greedy and sampling agree on failure profile (ISR*=0, H1=100%, components~18.5-18.9). s43 collapse is decoding-invariant.\"}, \"conclusion\": \"negative\"}, \"plan001-exec-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan017-additive-random-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.48, \"eval_mean_isr\": 0.0453, \"eval_isr_std\": 0.0759, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2857, \"eval_proved_only_isr\": 0.0943, \"eval_n_proved\": 48, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 9.6, \"eval_component_count_2_ratio\": 0, \"tautological_collapse\": false, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 1, \"h1_count\": 48, \"genuine_rate\": 0, \"genuine_count\": 0}}, \"plan002-additive-b01-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.81, \"eval_mean_isr\": 0.3365, \"eval_isr_std\": 0.3227, \"eval_proved_only_isr\": 0.4154, \"eval_median_isr\": 0.2, \"eval_n_proved\": 81, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 5.58, \"h7_rate\": 0.16, \"h7_count\": 13, \"h1_rate\": 0.519, \"h1_count\": 42, \"h8_conjunction_collapse_count\": 12, \"h8_conjunction_collapse_rate\": 0.148, \"genuine_rate\": 0.173, \"genuine_count\": 14, \"tautological_collapse\": false, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse audit completed. 12/81 proved samples are H8. Genuine 26→14 (32.1%→17.3%). H8 JSON at /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json\"}}, \"plan002-additive-b01-s43\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.61, \"eval_n_proved\": 61, \"eval_n_problems\": 100, \"eval_proved_only_isr\": 0.83, \"h7_count\": 59, \"h7_rate\": 0.9672, \"h1_count\": 0, \"h1_rate\": 0, \"h1_near_count\": 0, \"h1_near_rate\": 0, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 2, \"genuine_rate\": 0.0328, \"proved_single_premise_ratio\": 1, \"taxonomy_note\": \"structurally determined: proved_single_premise_ratio=1.0, all taxonomy categories except H7 are zero by construction. eval file lost but classification derivable from structure.\"}, \"conclusion\": \"negative\"}, \"exp1-isr-b03-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.91, \"mean_isr\": 0.2575, \"isr_std\": 0.2363, \"median_isr\": 0.3333, \"proved_only_mean_isr\": 0.283, \"hacking_rate_strict_h7\": 0.022, \"hacking_rate_functional\": 0.3297, \"genuine_rate\": 0.6703, \"genuine_count\": 61, \"n_proved\": 91, \"n_problems\": 100, \"h1_conclusion_in_premise\": 0.747, \"eval_data\": \"test_100.jsonl\", \"eval_output\": \"/root/autodl-tmp/outputs/eval_sta_exp1_isr_b03_s43.json\"}}, \"plan009-sft-baseline-s44-1000-r3\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.15, \"eval_n_proved\": 15, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0884, \"eval_isr_std\": 0.2268, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5892, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 1, \"h1_rate\": 0.0667, \"h8_conjunction_collapse_count\": 0, \"h8_conjunction_collapse_rate\": 0, \"genuine_count\": 14, \"genuine_rate\": 0.9333, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.441, \"mean_isr\": 0.26}, \"false\": {\"count\": 25, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}, \"unknown\": {\"count\": 41, \"proved\": 0, \"prove_rate\": 0, \"mean_isr\": 0}}}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s44\": {\"status\": \"DONE\", \"metrics\": {\"train_final_loss\": 0.2397, \"train_last_step_loss\": 0.0328, \"train_token_accuracy\": 0.9928, \"train_epochs\": 7.94, \"train_runtime_sec\": 729.05, \"train_steps\": 500, \"eval_prove_rate\": 0.17, \"eval_n_proved\": 17, \"eval_n_problems\": 100, \"eval_mean_isr\": 0.0974, \"eval_isr_std\": 0.2409, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5729, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_method\": \"eval_sta.py full STA\", \"eval_output_path\": \"/root/autodl-tmp/outputs/eval_sta_plan009_sft_s44.json\", \"eval_tautological_collapse\": false, \"eval_h7_count\": 0, \"eval_h7_rate\": 0, \"eval_h1_count\": 2, \"eval_h1_rate\": 0.118, \"eval_genuine_count\": 15, \"eval_genuine_rate\": 0.882, \"eval_by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 15, \"prove_rate\": 0.441, \"mean_isr\": 0.257}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.027}, \"unknown\": {\"count\": 41, \"proved\": 1, \"prove_rate\": 0.024, \"mean_isr\": 0.008}}, \"eval_correction_note\": \"Corrected 2026-05-15: previous eval used test_100.jsonl (50/44/6 distribution), re-evaled with proofwriter_fol_100.jsonl (34/25/41)\"}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s43\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.2391, \"train_token_accuracy\": 0.9938, \"train_epochs\": 7.94, \"train_runtime_sec\": 677.14, \"train_steps\": 500, \"eval_prove_rate\": 0.15, \"eval_mean_isr\": 0.0895, \"eval_isr_std\": 0.2338, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.5967, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 1, \"h1_rate\": 0.067, \"genuine_count\": 14, \"genuine_rate\": 0.933, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"prove_rate\": 0.382, \"mean_isr\": 0.234}, \"false\": {\"count\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.027}, \"unknown\": {\"count\": 41, \"proved\": 1, \"prove_rate\": 0.024, \"mean_isr\": 0.008}}, \"eval_data_path\": \"data/proofwriter_fol_100.jsonl\", \"eval_output_path\": \"/root/autodl-tmp/outputs/eval_sta_plan009_sft_s43.json\"}, \"conclusion\": \"success\"}, \"plan001-exec-only-s44-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan009-sft-baseline-s44-1000-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan002-additive-b03-s42\": {\"status\": \"DONE\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"last100_prove_rate\": 0.5525, \"eval_prove_rate\": 0.18, \"eval_mean_isr\": 0.0257, \"eval_isr_std\": 0.0742, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.1427, \"eval_n_proved\": 18, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.778, \"h1_count\": 14, \"h8_conjunction_collapse_count\": 3, \"h8_conjunction_collapse_rate\": 0.1667, \"genuine_rate\": 0.0556, \"genuine_count\": 1, \"eval_by_type_false_pr\": 0.12, \"eval_by_type_false_isr\": 0.0102, \"eval_by_type_unknown_pr\": 0.195, \"eval_by_type_unknown_isr\": 0.0422, \"eval_by_type_true_pr\": 0.206, \"eval_by_type_true_isr\": 0.0172, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine 4→1.\"}, \"conclusion\": \"negative\"}, \"plan001-exec-only-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.93, \"eval_mean_isr\": 0.1232, \"eval_isr_std\": 0.1887, \"eval_proved_only_isr\": 0.1324, \"eval_median_isr\": 0, \"eval_n_proved\": 93, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.871, \"h1_count\": 81, \"h8_conjunction_collapse_count\": 6, \"h8_conjunction_collapse_rate\": 0.0645, \"genuine_rate\": 0.0753, \"genuine_count\": 7, \"genuine_mean_isr\": 0.3141, \"h1_mean_isr\": 0.1055, \"conclusion_embedding_total\": 0.871, \"content_independent_predicates_count\": 1, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine 12→7.\"}}, \"plan004-o1-ablation-s42\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.63, \"mean_isr\": 0.0072, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 63, \"h1_rate\": 1, \"h8_conjunction_collapse_count\": 2, \"h8_conjunction_collapse_rate\": 0.0317, \"genuine_count\": 0, \"genuine_rate\": 0, \"content_independent_predicates_count\": 3, \"h8_audit_note\": \"2026-05-15: H8 conjunction collapse added. genuine unchanged (0).\"}, \"conclusion\": \"negative\"}, \"exp1-isr-b03-s42-1000-r2\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.95, \"eval_mean_isr\": 0.734, \"eval_isr_std\": 0.2575, \"eval_median_isr\": 0.6, \"eval_proved_only_isr\": 0.7726, \"eval_n_proved\": 95, \"eval_n_problems\": 100, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 25, \"prove_rate\": 1, \"mean_isr\": 0.824}, \"unknown\": {\"count\": 41, \"proved\": 38, \"prove_rate\": 0.927, \"mean_isr\": 0.673}, \"true\": {\"count\": 34, \"proved\": 32, \"prove_rate\": 0.941, \"mean_isr\": 0.741}}, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 54, \"h1_rate\": 0.568, \"genuine_count\": 0, \"genuine_rate\": 0, \"tautological_collapse\": true, \"isr_1_count\": 41, \"isr_1_rate\": 0.432, \"single_premise_count\": 0, \"train_final_prove_rate\": 0.829, \"train_final_mean_isr\": 0.727, \"train_loss\": 0.0041, \"train_runtime_seconds\": 6280, \"train_final_entropy\": 9e-06, \"completions_mean_length\": 47, \"h8_conjunction_collapse_count\": 41, \"h8_conjunction_collapse_rate\": 0.432, \"content_independent_predicates\": true}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s42-1000-r2\": {\"status\": \"DONE\", \"metrics\": {\"train_final_prove_rate\": 0.989, \"train_final_mean_isr\": 0.353, \"train_final_reward\": 1.062, \"train_steps\": 1000, \"train_runtime_seconds\": 2957, \"eval_prove_rate\": 1, \"eval_mean_isr\": 0.3333, \"eval_isr_std\": 0, \"eval_median_isr\": 0.3333, \"eval_proved_only_isr\": 0.3333, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_component_count_mean\": 3, \"genuine_rate\": 0, \"genuine_count\": 0, \"tautological_collapse\": true, \"h7_rate\": null, \"h7_count\": null, \"h1_rate\": null, \"h1_count\": null}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s42-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp1-isr-b03-s42-1000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s44\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.98, \"eval_mean_isr\": 0.57, \"eval_isr_std\": 0.2013, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.5816, \"eval_n_proved\": 98, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 2.04, \"eval_component_count_2\": 94, \"eval_component_count_3\": 4, \"tautological_collapse\": true, \"h7_rate\": 1, \"h7_count\": 97, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"conclusion_embedding_total\": 1}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s43-r2\": {\"status\": \"DONE\", \"metrics\": {\"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 93.2, \"h1_count\": 82, \"genuine_rate\": 6.8, \"genuine_count\": 6, \"eval_prove_rate\": 0.88, \"eval_mean_isr\": 0.058}, \"conclusion\": \"negative\"}, \"exp1-random-b03-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.23, \"eval_proved_only_mean_isr\": 0, \"eval_mean_isr\": 0, \"eval_isr_std\": 0, \"eval_median_isr\": 0, \"eval_n_proved\": 23, \"eval_n_problems\": 100, \"eval_h7_strict_rate\": 0, \"eval_h7_strict_count\": 0, \"eval_h1_strict_rate\": 1, \"eval_h1_strict_count\": 23, \"eval_genuine_rate\": 0, \"eval_genuine_count\": 0, \"eval_data\": \"proofwriter_fol_100.jsonl\"}}, \"exp1-isr-b03-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_step\": 500, \"prove_rate\": 0.56125, \"mean_isr\": 0.1515, \"parse_rate\": 1, \"train_loss\": 0.0176, \"train_runtime_sec\": 4153.6, \"epoch\": 2, \"eval_prove_rate\": 0.86, \"eval_mean_isr\": 0.2535, \"eval_isr_std\": 0.2406, \"eval_median_isr\": 0.3333, \"eval_proved_only_mean_isr\": 0.2948, \"eval_min_isr\": 0, \"eval_max_isr\": 0.75, \"eval_n_proved\": 86, \"eval_n_problems\": 100, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_h7_strict_rate\": 0.047, \"eval_h7_strict_count\": 4, \"eval_h1_strict_rate\": 0.686, \"eval_h1_strict_count\": 59, \"eval_conclusion_in_premise_rate\": 0.733, \"eval_conclusion_in_premise_count\": 63, \"eval_genuine_rate\": 0.267, \"eval_genuine_count\": 23, \"eval_single_premise_rate\": 0.058, \"eval_single_premise_count\": 5, \"eval_isr_1_count\": 0, \"eval_by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 23, \"prove_rate\": 0.92, \"mean_isr\": 0.334}, \"unknown\": {\"count\": 41, \"proved\": 35, \"prove_rate\": 0.854, \"mean_isr\": 0.199}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.26}}}}, \"exp1-random-b03-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan015-linear-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp1-isr-b03-s43-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp1-random-b03-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp1-isr-b03-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"prove_rate\": 0.95, \"mean_isr\": 0.705, \"isr_std\": 0.172, \"proved_only_isr\": 0.7421, \"n_proved\": 95, \"n_problems\": 100, \"h7_rate\": 1, \"h7_count\": 95, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"single_premise_rate\": 1, \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"Re-eval with correct test set (D062). Previous test_100.jsonl results invalidated.\"}}, \"exp1-random-b03-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp1-isr-b03-s44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp1-isr-b03-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp2-exec-s43-greedy\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp4-100step-h1h7\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan006-prolog-sta-s44\": {\"status\": \"DONE\", \"metrics\": {\"pass_rate\": 0.97, \"isr_mean\": 0.885, \"isr_n_cl_ge3\": \"N/A (0 samples)\", \"n_clauses_dist\": \"78/100 single-clause, 22/100 two-clause\", \"h7_functional_rate\": 0.979, \"genuine_rate\": 0, \"premise_count_analysis\": \"100% artifact - zero samples with n_clauses>=3, model exclusively generates 1-2 clause programs\", \"failure_mode\": \"query-as-fact gaming (total H7 collapse)\"}, \"conclusion\": \"negative\"}, \"plan006-prolog-sta-s43\": {\"status\": \"DONE\", \"metrics\": {\"train\": {\"final_prove_rate\": 0.769, \"final_mean_isr\": 0.129, \"final_loss\": 0.0155, \"final_entropy\": 0.09, \"final_reward\": 0.573, \"completion_length_mean\": 143, \"train_runtime_seconds\": 5095, \"train_runtime_minutes\": 84.9}, \"eval\": {\"n_problems\": 100, \"n_proved\": 38, \"prove_rate\": 0.38, \"mean_isr\": 0.0704, \"isr_std\": 0.1263, \"median_isr\": 0, \"proved_only_mean_isr\": 0.1853, \"min_isr\": 0, \"max_isr\": 1, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 11, \"prove_rate\": 0.44, \"mean_isr\": 0.1003}, \"unknown\": {\"count\": 41, \"proved\": 11, \"prove_rate\": 0.268, \"mean_isr\": 0.0394}, \"true\": {\"count\": 34, \"proved\": 16, \"prove_rate\": 0.471, \"mean_isr\": 0.0859}}}, \"h7_classification\": {\"h7_strict\": 0, \"h7_rate\": 0, \"h1_strict\": 37, \"h1_rate\": 0.974, \"conclusion_in_premise_total\": 37, \"conclusion_in_premise_rate\": 0.974, \"genuine_count\": 0, \"genuine_rate\": 0, \"isr_1_count\": 1, \"note\": \"1 pseudo-genuine sample (folio_1415) has query embedded in single mega-clause; all 38/38 proved samples are tautological\"}}, \"conclusion\": \"negative\"}, \"plan006-prolog-sta-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"cumulative_prove_rate\": 0.848, \"cumulative_mean_isr\": 0.787, \"final_prove_rate\": 1, \"final_isr\": 1, \"final_reward\": 1, \"saturation_onset_step\": 100, \"train_loss\": 0.00716, \"training_hours\": 0.78, \"final_entropy\": 0.01, \"final_completion_length\": 27, \"initial_completion_length\": 120, \"steps_at_perfect_reward\": 400, \"train_runtime_sec\": 2791, \"eval_prove_rate\": 0.5, \"eval_mean_isr\": 0.5, \"eval_proved_only_isr\": 1, \"eval_h7_rate\": 1, \"eval_h7_count\": 50, \"eval_proved_count\": 50, \"eval_total_count\": 100, \"eval_n_clauses_mean\": 1, \"eval_isr_distribution\": \"binary: 50x0 + 50x1\"}}, \"plan006-prolog-exec-s44\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.21, \"eval_mean_isr\": 0.0812, \"eval_isr_std\": 0.2343, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.3866, \"eval_min_isr\": 0, \"eval_max_isr\": 1, \"eval_n_proved\": 21, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 683.9, \"eval_by_type_false_pr\": 0.04, \"eval_by_type_false_isr\": 0.04, \"eval_by_type_unknown_pr\": 0.317, \"eval_by_type_unknown_isr\": 0.099, \"eval_by_type_true_pr\": 0.206, \"eval_by_type_true_isr\": 0.09, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\"}, \"plan009-sft-baseline-s42-r4\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.14, \"eval_mean_isr\": 0.08, \"eval_isr_std\": 0.214, \"eval_median_isr\": 0, \"eval_max_isr\": 0.833, \"eval_proved_only_isr\": 0.571, \"eval_n_proved\": 14, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"train_final_loss\": 0.0287, \"train_token_accuracy\": 0.9935, \"train_epochs\": 7.94, \"train_runtime_sec\": 789.6, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"pr\": 0.382, \"isr\": 0.226}, \"unknown\": {\"count\": 41, \"proved\": 1, \"pr\": 0.024, \"isr\": 0.008}, \"false\": {\"count\": 25, \"proved\": 0, \"pr\": 0, \"isr\": 0}}, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.071, \"h1_count\": 1, \"genuine_rate\": 0.929, \"genuine_count\": 13, \"hacking_patterns\": \"near-zero (1/14 H1, 0 H7, 92.9% genuine)\", \"tautological_collapse\": false}, \"conclusion\": \"success\"}, \"plan006-prolog-exec-s43-r3\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.56, \"eval_mean_isr\": 0.0084, \"eval_isr_std\": 0.0221, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.015, \"eval_min_isr\": 0, \"eval_max_isr\": 0.1, \"eval_n_proved\": 56, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 868.2, \"eval_by_type_false_pr\": 0.48, \"eval_by_type_false_isr\": 0.0043, \"eval_by_type_unknown_pr\": 0.6585, \"eval_by_type_unknown_isr\": 0.0114, \"eval_by_type_true_pr\": 0.5, \"eval_by_type_true_isr\": 0.0078, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s44\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.89, \"mean_isr\": 0.0619, \"isr_std\": 0.1756, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0695, \"n_proved\": 89, \"n_problems\": 100, \"max_isr\": 1, \"min_isr\": 0, \"isr_pr_ratio\": 0.0695, \"isr_zero_count\": 72, \"isr_one_count\": 2, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 21, \"prove_rate\": 0.84, \"mean_isr\": 0.0533}, \"unknown\": {\"count\": 41, \"proved\": 40, \"prove_rate\": 0.976, \"mean_isr\": 0.0892}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.0353}}, \"elapsed_seconds\": 1012.7, \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\"}, \"conclusion\": \"success\"}, \"plan009-sft-baseline-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan006-prolog-exec-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan006-prolog-exec-s42\": {\"status\": \"DONE\", \"metrics\": {\"eval_prove_rate\": 0.83, \"eval_mean_isr\": 0.031, \"eval_proved_only_isr\": 0.037, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2, \"eval_isr_std\": 0.0534, \"h7_rate\": 0, \"h1_rate\": 0, \"isr_1_rate\": 0, \"single_premise_rate\": 0, \"by_answer_type\": {\"true\": {\"proved\": 37, \"count\": 40, \"pr\": 0.925, \"isr\": 0.037}, \"false\": {\"proved\": 21, \"count\": 29, \"pr\": 0.724, \"isr\": 0.038}, \"unknown\": {\"proved\": 25, \"count\": 31, \"pr\": 0.806, \"isr\": 0.016}}}, \"conclusion\": \"negative\"}, \"plan006-prolog-exec-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan009-sft-baseline-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan009-sft-baseline-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan018-additive-random-b01-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan012-hacking-taxonomy\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"isr_b01_genuine_rate\": 0.259, \"random_b01_genuine_rate\": 0.177, \"genuine_rate_delta_pp\": 8.2, \"isr_b01_conclusion_embedding_rate\": 0.728, \"random_b01_conclusion_embedding_rate\": 0.785, \"isr_b01_genuine_mean_isr\": 0.6723, \"random_b01_genuine_mean_isr\": 0.3427, \"isr_b01_complexity_wo_utility_rate\": 0, \"random_b01_complexity_wo_utility_rate\": 0.038, \"isr_b01_hacking_rate\": 0.741, \"random_b01_hacking_rate\": 0.823}}, \"plan005-sta-low-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 71, \"parse_rate\": 1, \"overall_prove_rate\": 0.5657, \"overall_isr\": 0.1682, \"last50_prove_rate\": 0.77, \"last50_isr\": 0.2559, \"last100_prove_rate\": 0.7725, \"last100_isr\": 0.2299, \"last100_loss\": 0.022752, \"overall_loss\": 0.017296, \"last100_isr_pr_ratio\": 0.298, \"last100_isr_lt_pr_count\": \"99/100\", \"first_rolling10_pr_ge_0.8\": 178, \"first_rolling10_pr_ge_0.9\": 439, \"max_rolling10_pr\": 0.9375, \"max_rolling10_isr\": 0.3282, \"windowed\": {\"1-50\": {\"pr\": 0.1775, \"isr\": 0.0906}, \"51-100\": {\"pr\": 0.1775, \"isr\": 0.0835}, \"101-200\": {\"pr\": 0.5062, \"isr\": 0.1463}, \"201-300\": {\"pr\": 0.6713, \"isr\": 0.1791}, \"301-400\": {\"pr\": 0.7013, \"isr\": 0.1984}, \"401-500\": {\"pr\": 0.7725, \"isr\": 0.2299}}}}, \"plan014-downstream-nli-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_accuracy\": 0.341, \"proved_rate\": 0.915, \"proved_count\": 732, \"total_generations\": 800, \"parse_errors\": 0, \"accuracy_by_label\": {\"true\": 0.912, \"false\": 0, \"unknown\": 0.076}, \"spearman_rho\": -0.049, \"spearman_p\": 0.187, \"mann_whitney_U\": 17202, \"mann_whitney_p\": 0.288, \"bon_isr_accuracy\": 0.35, \"bon_random_accuracy\": 0.341, \"bon_oracle_accuracy\": 0.44, \"bon_prove_first_accuracy\": 0.35, \"isr_bucket_high_acc\": 0.75, \"isr_bucket_mid_acc\": 0.377, \"isr_bucket_low_acc\": 0.327, \"runtime_inference_s\": 408.8, \"runtime_eval_s\": 13.6}}, \"plan001-exec-only-s43-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan013-random-reward-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan001-exec-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan003-eval-exec-only-r5\": {\"status\": \"DONE\", \"metrics\": {\"prove_rate\": 0.32, \"mean_isr\": 0.2055, \"isr_std\": 0.3194, \"proved_only_isr\": 0.6423, \"isr_by_type\": {\"true\": 0.3598, \"false\": 0.1723, \"unknown\": 0.0979}, \"total_samples\": 100, \"proved_count\": 32, \"runtime_s\": 251.7}, \"conclusion\": \"success\"}, \"plan001-exec-only-s42-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta-r5\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1, \"mean_isr\": 0.04347, \"last20_prove_rate\": 0.15, \"last20_isr_mean\": 0.04956, \"first20_prove_rate\": 0.08125, \"first20_isr_mean\": 0.05182, \"overall_reward_mean\": 0.07174, \"last20_reward_mean\": 0.09978, \"training_steps\": 100, \"training_minutes\": 16.9, \"step_time_s\": 10.13, \"isr_pr_ratio_overall\": 0.43, \"isr_pr_ratio_last20\": 0.33, \"K\": 8}, \"conclusion\": \"negative\"}, \"sta-phase1-exec-only-r5\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_prove_rate\": 0.11875, \"first20_isr_mean\": 0.11875, \"overall_reward_mean\": 0.15125, \"last20_reward_mean\": 0.2, \"training_steps\": 100, \"training_minutes\": 15.7, \"step_time_s\": 9.44, \"isr_pr_ratio_last20\": 1, \"K\": 8}, \"conclusion\": \"success\"}, \"sta-phase1-exec-sta-r4\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1575, \"mean_isr\": 0.1525, \"last20_prove_rate\": 0.2125, \"last20_isr_mean\": 0.2125, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"conclusion\": \"negative\"}, \"sta-phase1-exec-only-r4\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"conclusion\": \"negative\"}, \"sta-phase1-exec-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta-r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-sta\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-phase1-exec-only\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sta-gt-isr-baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gt_prove_rate\": 0.18, \"gt_mean_isr\": 0.5588, \"gt_isr_std\": 0.2582, \"gt_isr_median\": 0.6125, \"solver_execution_rate\": 1, \"true_prove_rate\": 0.5, \"true_mean_isr\": 0.5833}}, \"sta-phase0-baseline\": {\"status\": \"DONE\", \"metrics\": {\"mean_isr\": 0.0641, \"isr_std\": 0.1983, \"median_isr\": 0, \"isr_range\": [0, 0.889], \"prove_rate\": 0.12, \"proved_count\": 12, \"total_samples\": 100, \"xor_affected_samples\": 34, \"effective_prove_rate_no_xor\": 0.182, \"avg_time_per_sample_s\": 3.4, \"total_runtime_s\": 336, \"isr_by_answer\": {\"true\": {\"n\": 34, \"proved\": 9, \"prove_rate\": 0.265, \"mean_isr\": 0.1345}, \"false\": {\"n\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.024}, \"unknown\": {\"n\": 41, \"proved\": 2, \"prove_rate\": 0.049, \"mean_isr\": 0.0302}}}, \"conclusion\": \"success\"}}, \"count\": 86, \"total\": 86, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3107}}"
    }
  },
  "sourceToolAssistantUUID": "d6cf7607-b595-4ede-a993-67679fa51ef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-15T18:08:25.091Z_

```json
{
  "parentUuid": "048dc8bf-9821-4d1b-8ed0-ed6f7dcb9342",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "afb3715a-5101-46a4-82d6-9dcf175bf431",
  "timestamp": "2026-05-15T18:08:25.091Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "leafUuid": "afb3715a-5101-46a4-82d6-9dcf175bf431",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Organize Random and ISR β=0.1 3-seed comparison table",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861"
}
```

---

### Assistant

_source line 34 · 2026-05-15T18:09:52.217Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the registry data. Let me extract the relevant experiments and verify the numbers.

**Random β=0.1 experiments:**

1. **plan018-additive-random-b01-s42**: 
   - PR = 0.79, n_proved = 79
   - taxonomy_note: "Re-classified with current classify_h7.py. Old values: genuine_strict=12 (H1_exact=56, H1_near=8, H8=3). New standard: H1=58 (2 former H1-near now H1), H8=4, genuine=18. 

I'm noticing a discrepancy here—the registry now shows genuine=18 after reclassification, but the user specifically requested the strict version with genuine_strict=12 (15.19%). The taxonomy tool was updated on 2026-05-15, which changed how these categories are defined. I see there's a discrepancy between the user's provided numbers and what's currently in the registry. The registry was updated today with new classification logic, so the values they gave me (H1=56, H8=3, genuine=12) are outdated. Since the user explicitly stated all numbers must be traced back to the registry without fabrication, I should use the current registry values instead. Let me pull the actual current data for plan018-additive-random-b01-s42: n_proved=79, n_problems=100, PR=0.79, with H7=0. I see there's a discrepancy between the old strict definition (genuine_strict=12 with H1_exact=56, H1_near=8, H8=3) and the current registry showing genuine=18 under a different standard where H1 includes both exact and near matches. Looking at the C013 taxonomy standard, genuine should equal proved minus H7, H1_exact, and H8, with H1_near kept separate but still counted as genuine—so I need to reconcile which standard the registry is actually using now. I'm working through the calculation differences—it looks like genuine_strict counts all H1 variants (both exact and near) as exclusions, giving 79 - 0 - 64 - 3 = 12, while the exact_h1 version only subtracts H1_exact, yielding 79 - 0 - 56 = 23.

According to the registry reclassification, H1_near got merged into H1, so the new totals are H1=58 and H8=4, which should give genuine = 79 - 0 - 58 - 4 = 17, but the registry shows 18—there's a discrepancy of 1 that I need to account for.

Rather than get stuck on this mismatch, I should just pull the current registry numbers for all 6 experiments and work with those values directly.

Now I'm compiling the registry data for each experiment—the second random seed run shows a much higher proof rate at 0.94 with mostly H1 classifications, while the ISR variant at the same beta has a lower proof rate of 0.81 with a more balanced distribution across categories. Now I'm verifying the metrics for plan002-additive-b01-s42 against the registry data—H7 at 16%, H1 at 52%, H8 conjunction collapse at 15%, and genuine proofs at 17%—which all check out. The s44 variant shows perfect H7 performance at 100% with no other proof types, and I'm cross-referencing the s43-r2 results as well.

The key issue emerging is with plan018-additive-random-b01-s42, where the user's original taxonomy numbers don't match what the registry now shows after reclassification.  The user explicitly instructed me to use the strict version of genuine (12) and to source all numbers from the registry, but the registry has been updated since those instructions were written. I need to flag this discrepancy and clarify which values to use, especially since the registry notes show both the old taxonomy (genuine_strict=12) and the new standard (H1=58 with reclassified values).

Now I'm compiling the statistics table for the ISR results... Now I'm looking at the per-seed performance rates and calculating the standard deviation more carefully—the PR rates vary from 0.61 to 0.89 with a mean around 0.77, while the genuine rates are much lower and more sparse across the seeds. Now I'm looking at the results for the random β=0.1 condition across two seeds, comparing the registry values against what the user specified. I notice there's a discrepancy with s42's genuine_strict value and I'm wondering if s43-r3 has similar taxonomy issues in the registry. Looking at the different classification standards, I'm seeing inconsistencies in how the genuine count is calculated depending on which definition I apply. The current registry shows genuine=18 for s42, but when I work through the D084 standard (proved minus H7, H1_exact, and H8), I get either 19 or 20 depending on whether I use the old or new H8 value—none of which match the registry's 18.

Rather than trying to resolve this discrepancy, I'll just use the registry values as they are and make sure to flag this inconsistency clearly to the user. Now let me compute the results using the current registry data.

Looking at the random β=0.1 results across both seeds, I'm pooling the proved samples to get overall rates: 173 total proved instances, with genuine cases making up about 11%, H7 around 21%, H1 roughly 66%, and H8 at about 3%. The per-seed proof rates are 0.79 and 0.94, averaging around 0.865, and the genuine rates vary from about 23% down to 1% across the two seeds.

With only two seeds, calculating standard deviation feels less informative, so I'm thinking it makes more sense to just report both individual values rather than trying to summarize with mean and standard deviation.

Now I'm verifying the background numbers against the registry—s42 has n_proved=81, s43-r2 has 61, and s44 has 89, which all check out. The ISR results with β=0.1 match expectations too. There's that reclassification issue with Random s42 that I'll need to flag, but I'm ready to build out the comprehensive table now.

Generating markdown table...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afb3715a-5101-46a4-82d6-9dcf175bf431",
  "isSidechain": false,
  "requestId": "req_011Cb4oSmtJ2T2R9919uLVf8",
  "type": "assistant",
  "uuid": "463b9774-24d8-476a-bf68-e121d249b183",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XShe42mBo9GWxxEThKjtQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18491,
      "cache_read_input_tokens": 27703,
      "output_tokens": 5640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18491,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5640,
          "cache_read_input_tokens": 27703,
          "cache_creation_input_tokens": 18491,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18491
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

_source line 35 · 2026-05-15T18:09:52.679Z_

Registry loaded. Key discrepancy: **plan018-additive-random-b01-s42** was reclassified on 2026-05-15 — registry now shows H1=58, H8=4, genuine=18 (was H1=56, H8=3, genuine_strict=12). I'll use current registry values and note this.

Let me compute and write the table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "463b9774-24d8-476a-bf68-e121d249b183",
  "isSidechain": false,
  "requestId": "req_011Cb4oSmtJ2T2R9919uLVf8",
  "type": "assistant",
  "uuid": "fa0d2b29-10e1-4539-a8cd-733e5192adfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XShe42mBo9GWxxEThKjtQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18491,
      "cache_read_input_tokens": 27703,
      "output_tokens": 5640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18491,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5640,
          "cache_read_input_tokens": 27703,
          "cache_creation_input_tokens": 18491,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18491
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

_source line 36 · 2026-05-15T18:09:54.171Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MZtB4DNeG18iYm758mZXdR`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa0d2b29-10e1-4539-a8cd-733e5192adfc",
  "isSidechain": false,
  "requestId": "req_011Cb4oSmtJ2T2R9919uLVf8",
  "type": "assistant",
  "uuid": "7a5d68f0-9bd2-4fa4-879e-1eb1c3689812",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XShe42mBo9GWxxEThKjtQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18491,
      "cache_read_input_tokens": 27703,
      "output_tokens": 5640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18491,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5640,
          "cache_read_input_tokens": 27703,
          "cache_creation_input_tokens": 18491,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18491
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

_source line 37 · 2026-05-15T18:09:54.501Z_

<details><summary>↩ Tool result · `toolu_01MZtB4DNeG18iYm758mZXdR`</summary>

```text
_deprecated
_project
analysis_random_vs_isr_b01_interim.md
bootstrap_ci_results.json
claim_coverage_audit.md
component_count_analysis.md
data_consistency_report.md
diagnose_phase1_r3.md
dream_reports
evidence_chain_status.md
evidence_tables_d051.md
figure_quality_report.md
genuine_isr_crosscheck.md
grpo_exec_only.yaml
grpo_exec_sta.yaml
hacking_characterization_report.md
hacking_taxonomy.md
hacking_taxonomy_comparison.md
inc05_literature_linkage.md
launch_phase1.sh
literature_goodhart.md
literature_map.yaml
manifest.yaml
paper-audit
paper_compile_audit.md
paper_consistency_audit.md
paper_figures
paper_number_audit.md
paper_number_audit_2026-05-15.json
paper_review_r1.md
paper_table1_evidence.md
paper_tables
paper_tables_draft.md
phase1_r2_diagnosis.md
plan001-exec-only-s43-1000-r2
plan001-exec-only-s43-r4
plan001-exec-only-s44
plan002-additive-b01-s42
plan002-additive-b01-s42-1000
plan002-additive-b01-s43
plan002-additive-b01-s43-r2
plan005_negative_literature.md
plan006
plan006_eval_compatibility.md
plan006_readiness.md
plan006_readiness_report.md
plan012
plan013-random-reward-s42-r4
plan013_analysis.md
plan014_design.md
plan016-extended-1000-s42
plan017-additive-random-s42
plan018
plan018-additive-random-b01-s42
plan018-additive-random-b01-s42-1000-r3
plan018-additive-random-b01-s42-1000-r3_analysis.json
preflight_prolog_sta_eval.md
prolog_sta_literature_linkage.md
prolog_sta_premise_count_analysis.md
reference_audit_report.md
reference_final_audit.md
registry_extract.json
review_issues.yaml
review_reports
s43_1000_n_components_investigation.md
section_4_3_1000step_draft.md
seed44_readiness.md
sft_3seed_pooled_ci.json
sta-phase0-baseline
stats_recalc_checklist.md
table1_comparison.md
table1_data.json
table1_draft.md
table2_draft.md
table2_hacking_taxonomy.csv
table2_hacking_taxonomy.tex
table_data.json
table_data_compilation.md
table_drafts_v2.md
tables_draft_v1.md
tex_number_audit_20260515.md
train_grpo.py
training_progress_check.md
wilson_ci.py
wilson_ci_complete.csv
wilson_ci_complete.json
wilson_ci_complete.py
wilson_ci_results.csv
wilson_ci_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a5d68f0-9bd2-4fa4-879e-1eb1c3689812",
  "isSidechain": false,
  "promptId": "db93fe6a-8875-4790-b540-188c747c78ba",
  "type": "user",
  "uuid": "86e963a6-d240-496a-9a02-7c736b1cad39",
  "toolUseResult": {
    "stdout": "_deprecated\n_project\nanalysis_random_vs_isr_b01_interim.md\nbootstrap_ci_results.json\nclaim_coverage_audit.md\ncomponent_count_analysis.md\ndata_consistency_report.md\ndiagnose_phase1_r3.md\ndream_reports\nevidence_chain_status.md\nevidence_tables_d051.md\nfigure_quality_report.md\ngenuine_isr_crosscheck.md\ngrpo_exec_only.yaml\ngrpo_exec_sta.yaml\nhacking_characterization_report.md\nhacking_taxonomy.md\nhacking_taxonomy_comparison.md\ninc05_literature_linkage.md\nlaunch_phase1.sh\nliterature_goodhart.md\nliterature_map.yaml\nmanifest.yaml\npaper-audit\npaper_compile_audit.md\npaper_consistency_audit.md\npaper_figures\npaper_number_audit.md\npaper_number_audit_2026-05-15.json\npaper_review_r1.md\npaper_table1_evidence.md\npaper_tables\npaper_tables_draft.md\nphase1_r2_diagnosis.md\nplan001-exec-only-s43-1000-r2\nplan001-exec-only-s43-r4\nplan001-exec-only-s44\nplan002-additive-b01-s42\nplan002-additive-b01-s42-1000\nplan002-additive-b01-s43\nplan002-additive-b01-s43-r2\nplan005_negative_literature.md\nplan006\nplan006_eval_compatibility.md\nplan006_readiness.md\nplan006_readiness_report.md\nplan012\nplan013-random-reward-s42-r4\nplan013_analysis.md\nplan014_design.md\nplan016-extended-1000-s42\nplan017-additive-random-s42\nplan018\nplan018-additive-random-b01-s42\nplan018-additive-random-b01-s42-1000-r3\nplan018-additive-random-b01-s42-1000-r3_analysis.json\npreflight_prolog_sta_eval.md\nprolog_sta_literature_linkage.md\nprolog_sta_premise_count_analysis.md\nreference_audit_report.md\nreference_final_audit.md\nregistry_extract.json\nreview_issues.yaml\nreview_reports\ns43_1000_n_components_investigation.md\nsection_4_3_1000step_draft.md\nseed44_readiness.md\nsft_3seed_pooled_ci.json\nsta-phase0-baseline\nstats_recalc_checklist.md\ntable1_comparison.md\ntable1_data.json\ntable1_draft.md\ntable2_draft.md\ntable2_hacking_taxonomy.csv\ntable2_hacking_taxonomy.tex\ntable_data.json\ntable_data_compilation.md\ntable_drafts_v2.md\ntables_draft_v1.md\ntex_number_audit_20260515.md\ntrain_grpo.py\ntraining_progress_check.md\nwilson_ci.py\nwilson_ci_complete.csv\nwilson_ci_complete.json\nwilson_ci_complete.py\nwilson_ci_results.csv\nwilson_ci_results.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7a5d68f0-9bd2-4fa4-879e-1eb1c3689812",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "leafUuid": "86e963a6-d240-496a-9a02-7c736b1cad39",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Organize Random and ISR β=0.1 3-seed comparison table",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861"
}
```

---

### Assistant

_source line 40 · 2026-05-15T18:10:36.388Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me compute the statistics and write the table.

**ISR β=0.1 (3 seeds):**

| Seed | exp_id | n_proved | PR | H7 | H1 | H8 | genuine |
|------|--------|----------|------|------|------|------|---------|
| s42 | plan002-additive-b01-s42 | 81 | 0.81 | 13 (16.0%) | 42 (51.9%) | 12 (14.8%) | 14 (17.3%) |


| s43-r2 | plan002-additive-b01-s43-r2 | 61 | 0.61 | 61 (100%) | 0 (0%) | 0 (0%) | 0 (0%) |
| s44 | plan002-additive-b01-s44 | 89 | 0.89 | 89 (100%) | 0 (0%) | 0 (0%) | 0 (0%) |

Generating markdown table... I'm finishing the standard deviation calculation at 0.1442, then looking at the genuine rate statistics which show much lower values with a standard deviation of 0.0998. Now I'm examining the results from the random β=0.1 experiments across two seeds, compiling the performance metrics into a registry table. Now I'm calculating the mean metrics across the two seeds: the pooled prove rate comes to 0.865, and the genuine rate averages around 0.1192. But I'm noticing a discrepancy in the registry data—the counts for one configuration don't quite add up to the total proved, so I need to investigate that more carefully. Looking at the breakdown of how the 79 proved problems are classified: H1 accounts for 58, H8 for 4, and genuine for 18, which aligns with the taxonomy note showing how the classification was updated using the current script.

But when I add these up—58 plus 4 plus 18—I get 80, not 79. And the rates themselves (0.7342 + 0.0506 + 0.2278) sum to over 1, which confirms there's an overlap or double-counting issue somewhere. One sample is likely being counted in multiple categories. I should flag this data quality concern but proceed with the registry values as given.

Actually, looking at the formula "proved - H7 - H1 - H8" = 79 - 0 - 58 - 4, that gives 17 for genuine, not 18. So there's an internal inconsistency in how the numbers were recorded. I'll note both the recorded value of 18 and the formula-derived value of 17, flag the discrepancy, and let the user decide which to use.

Now I'll create the artifact with this caveat included.

Checking the arithmetic across the other samples — s43-r3 adds up correctly at 94, ISR s42 checks out at 81, ISR s43-r2 is consistent at 61, and ISR s44 also balances at 89.

The only discrepancy is in Random s42, where the individual counts sum to 80 but n_proved is listed as 79. Looking deeper into the registry values, eval_prove_rate is 0.79 with eval_n_proved=79 out of 100 problems, which should mean 79 proved cases. The individual rates for h1, h8, and genuine all check out against this 79 denominator, but when I add those rates together they exceed 1.0, suggesting one sample might be double-classified or there's a stale artifact in the h8_count that should be 3 instead of 4.

Now I'm calculating the H7 and H1 rate statistics across seeds for ISR β=0.1, computing the means and standard deviations to see how much variation there is between the different random seeds.

Generating markdown table...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86e963a6-d240-496a-9a02-7c736b1cad39",
  "isSidechain": false,
  "requestId": "req_011Cb4oZNBibcJo2V6N9bDeM",
  "type": "assistant",
  "uuid": "9e3049a3-dc29-47fc-8bf6-6e58049a1b65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UXgUtRLiCLaKtc67tDFWDf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6440,
      "cache_read_input_tokens": 46194,
      "output_tokens": 4704,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6440,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4704,
          "cache_read_input_tokens": 46194,
          "cache_creation_input_tokens": 6440,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6440
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

_source line 41 · 2026-05-15T18:11:00.045Z_

<details open><summary>🔧 Tool call — Write · `toolu_016sRF1brHuuEWsZ8er1kRiT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_comparison_table.md",
  "content": "# Random β=0.1 vs ISR β=0.1: Cross-Seed Comparison Table\n\nGenerated: 2026-05-15 | Source: project registry (solver-trace-ablation)\n\n## Data Quality Note\n\n**plan018-additive-random-b01-s42** was reclassified on 2026-05-15 with updated classify_h7.py.\n- Old values: H7=0, H1_exact=56, H1_near=8, H8=3, genuine_strict=12\n- New values: H7=0, H1=58, H8=4, genuine=18\n- **Consistency issue**: H7+H1+H8+genuine = 0+58+4+18 = 80 ≠ n_proved=79. One sample double-counted. Needs investigation.\n\nAll other experiments sum correctly (H7+H1+H8+genuine = n_proved).\n\n---\n\n## ISR β=0.1 — Per-Seed Results (3 seeds)\n\n| Metric | s42 | s43-r2 | s44 |\n|--------|-----|--------|-----|\n| exp_id | plan002-additive-b01-s42 | plan002-additive-b01-s43-r2 | plan002-additive-b01-s44 |\n| Prove Rate | 0.81 | 0.61 | 0.89 |\n| n_proved | 81 | 61 | 89 |\n| H7 | 13 (16.0%) | 61 (100%) | 89 (100%) |\n| H1 | 42 (51.9%) | 0 (0%) | 0 (0%) |\n| H8 | 12 (14.8%) | 0 (0%) | 0 (0%) |\n| genuine | 14 (17.3%) | 0 (0%) | 0 (0%) |\n| mean ISR | 0.3365 | 0.5063 | 0.803 |\n\n### ISR β=0.1 — Pooled Statistics\n\n| Metric | Value |\n|--------|-------|\n| total n_proved | 231 |\n| mean PR ± std | 0.770 ± 0.144 |\n| pooled genuine | 14/231 = 6.06% |\n| pooled H7 | 163/231 = 70.56% |\n| pooled H1 | 42/231 = 18.18% |\n| pooled H8 | 12/231 = 5.19% |\n| mean genuine_rate ± std | 5.77% ± 9.99% |\n\nPer-seed genuine rates: 17.3%, 0%, 0% — high variance driven by s42.\n\n**Key pattern**: 2/3 seeds (s43, s44) collapsed to 100% H7 tautology. Only s42 retained genuine proofs.\n\n---\n\n## Random β=0.1 — Per-Seed Results (2 seeds; s44-r2 RUNNING)\n\n| Metric | s42 | s43-r3 |\n|--------|-----|--------|\n| exp_id | plan018-additive-random-b01-s42 | plan018-additive-random-b01-s43-r3 |\n| Prove Rate | 0.79 | 0.94 |\n| n_proved | 79 | 94 |\n| H7 | 0 (0%) | 36 (38.3%) |\n| H1 | 58 (73.4%) | 56 (59.6%) |\n| H8 | 4 (5.1%) | 1 (1.1%) |\n| genuine | 18 (22.8%)* | 1 (1.1%) |\n| mean ISR | 0.1038 | 0.1406 |\n\n*See data quality note above. Old genuine_strict=12 (15.19%) before reclassification.\n\n### Random β=0.1 — Pooled Statistics (2-seed, provisional)\n\n| Metric | Value |\n|--------|-------|\n| total n_proved | 173 |\n| mean PR | 0.865 (range: 0.79–0.94) |\n| pooled genuine | 19/173 = 10.98% |\n| pooled H7 | 36/173 = 20.81% |\n| pooled H1 | 114/173 = 65.90% |\n| pooled H8 | 5/173 = 2.89% |\n| per-seed genuine rates | 22.8%, 1.1% |\n\n**Key pattern**: Both seeds dominated by H1 (conclusion-in-premise). s42 has 0% H7 while s43-r3 has 38.3% H7. High inter-seed variance.\n\n---\n\n## Side-by-Side Comparison\n\n| Metric | ISR β=0.1 (3-seed) | Random β=0.1 (2-seed) |\n|--------|--------------------|-----------------------|\n| mean PR | 0.770 ± 0.144 | 0.865 |\n| pooled genuine rate | 6.06% (14/231) | 10.98% (19/173) |\n| pooled H7 rate | 70.56% (163/231) | 20.81% (36/173) |\n| pooled H1 rate | 18.18% (42/231) | 65.90% (114/173) |\n| pooled H8 rate | 5.19% (12/231) | 2.89% (5/173) |\n| dominant failure mode | H7 tautology | H1 conclusion embedding |\n| seeds with genuine=0 | 2/3 | 0/2 |\n\n### Interpretation\n\n1. **ISR reward amplifies H7 tautology**: 70.6% pooled H7 vs 20.8% for Random. ISR incentivizes maximizing indispensability → model discovers tautological shortcut (single-premise = conclusion).\n2. **Random reward amplifies H1 embedding**: 65.9% pooled H1 vs 18.2% for ISR. Without ISR pressure, model defaults to embedding conclusion in premises.\n3. **Neither method produces reliable genuine proofs**: ISR pooled genuine 6.1%, Random pooled genuine 11.0%. Both far below SFT baseline (~93% genuine).\n4. **Both show extreme inter-seed variance**: ISR ranges 0%–17.3% genuine; Random ranges 1.1%–22.8%. Single-seed results unreliable.\n\n---\n\n## Pending\n\n- [ ] Random s44-r2 (plan018-additive-random-b01-s44-r2): RUNNING. Add to table when complete.\n- [ ] Investigate s42 reclassification sum mismatch (80 vs 79).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e3049a3-dc29-47fc-8bf6-6e58049a1b65",
  "isSidechain": false,
  "requestId": "req_011Cb4oZNBibcJo2V6N9bDeM",
  "type": "assistant",
  "uuid": "d3f0cb62-acb5-49ee-8c8a-8e6fee644b38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UXgUtRLiCLaKtc67tDFWDf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6440,
      "cache_read_input_tokens": 46194,
      "output_tokens": 4704,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6440,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4704,
          "cache_read_input_tokens": 46194,
          "cache_creation_input_tokens": 6440,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6440
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

_source line 42 · 2026-05-15T18:11:00.078Z_

<details><summary>↩ Tool result · `toolu_016sRF1brHuuEWsZ8er1kRiT`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_comparison_table.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3f0cb62-acb5-49ee-8c8a-8e6fee644b38",
  "isSidechain": false,
  "promptId": "db93fe6a-8875-4790-b540-188c747c78ba",
  "type": "user",
  "uuid": "83078868-cd29-412c-8c90-f4ae9686ac28",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_comparison_table.md",
    "content": "# Random β=0.1 vs ISR β=0.1: Cross-Seed Comparison Table\n\nGenerated: 2026-05-15 | Source: project registry (solver-trace-ablation)\n\n## Data Quality Note\n\n**plan018-additive-random-b01-s42** was reclassified on 2026-05-15 with updated classify_h7.py.\n- Old values: H7=0, H1_exact=56, H1_near=8, H8=3, genuine_strict=12\n- New values: H7=0, H1=58, H8=4, genuine=18\n- **Consistency issue**: H7+H1+H8+genuine = 0+58+4+18 = 80 ≠ n_proved=79. One sample double-counted. Needs investigation.\n\nAll other experiments sum correctly (H7+H1+H8+genuine = n_proved).\n\n---\n\n## ISR β=0.1 — Per-Seed Results (3 seeds)\n\n| Metric | s42 | s43-r2 | s44 |\n|--------|-----|--------|-----|\n| exp_id | plan002-additive-b01-s42 | plan002-additive-b01-s43-r2 | plan002-additive-b01-s44 |\n| Prove Rate | 0.81 | 0.61 | 0.89 |\n| n_proved | 81 | 61 | 89 |\n| H7 | 13 (16.0%) | 61 (100%) | 89 (100%) |\n| H1 | 42 (51.9%) | 0 (0%) | 0 (0%) |\n| H8 | 12 (14.8%) | 0 (0%) | 0 (0%) |\n| genuine | 14 (17.3%) | 0 (0%) | 0 (0%) |\n| mean ISR | 0.3365 | 0.5063 | 0.803 |\n\n### ISR β=0.1 — Pooled Statistics\n\n| Metric | Value |\n|--------|-------|\n| total n_proved | 231 |\n| mean PR ± std | 0.770 ± 0.144 |\n| pooled genuine | 14/231 = 6.06% |\n| pooled H7 | 163/231 = 70.56% |\n| pooled H1 | 42/231 = 18.18% |\n| pooled H8 | 12/231 = 5.19% |\n| mean genuine_rate ± std | 5.77% ± 9.99% |\n\nPer-seed genuine rates: 17.3%, 0%, 0% — high variance driven by s42.\n\n**Key pattern**: 2/3 seeds (s43, s44) collapsed to 100% H7 tautology. Only s42 retained genuine proofs.\n\n---\n\n## Random β=0.1 — Per-Seed Results (2 seeds; s44-r2 RUNNING)\n\n| Metric | s42 | s43-r3 |\n|--------|-----|--------|\n| exp_id | plan018-additive-random-b01-s42 | plan018-additive-random-b01-s43-r3 |\n| Prove Rate | 0.79 | 0.94 |\n| n_proved | 79 | 94 |\n| H7 | 0 (0%) | 36 (38.3%) |\n| H1 | 58 (73.4%) | 56 (59.6%) |\n| H8 | 4 (5.1%) | 1 (1.1%) |\n| genuine | 18 (22.8%)* | 1 (1.1%) |\n| mean ISR | 0.1038 | 0.1406 |\n\n*See data quality note above. Old genuine_strict=12 (15.19%) before reclassification.\n\n### Random β=0.1 — Pooled Statistics (2-seed, provisional)\n\n| Metric | Value |\n|--------|-------|\n| total n_proved | 173 |\n| mean PR | 0.865 (range: 0.79–0.94) |\n| pooled genuine | 19/173 = 10.98% |\n| pooled H7 | 36/173 = 20.81% |\n| pooled H1 | 114/173 = 65.90% |\n| pooled H8 | 5/173 = 2.89% |\n| per-seed genuine rates | 22.8%, 1.1% |\n\n**Key pattern**: Both seeds dominated by H1 (conclusion-in-premise). s42 has 0% H7 while s43-r3 has 38.3% H7. High inter-seed variance.\n\n---\n\n## Side-by-Side Comparison\n\n| Metric | ISR β=0.1 (3-seed) | Random β=0.1 (2-seed) |\n|--------|--------------------|-----------------------|\n| mean PR | 0.770 ± 0.144 | 0.865 |\n| pooled genuine rate | 6.06% (14/231) | 10.98% (19/173) |\n| pooled H7 rate | 70.56% (163/231) | 20.81% (36/173) |\n| pooled H1 rate | 18.18% (42/231) | 65.90% (114/173) |\n| pooled H8 rate | 5.19% (12/231) | 2.89% (5/173) |\n| dominant failure mode | H7 tautology | H1 conclusion embedding |\n| seeds with genuine=0 | 2/3 | 0/2 |\n\n### Interpretation\n\n1. **ISR reward amplifies H7 tautology**: 70.6% pooled H7 vs 20.8% for Random. ISR incentivizes maximizing indispensability → model discovers tautological shortcut (single-premise = conclusion).\n2. **Random reward amplifies H1 embedding**: 65.9% pooled H1 vs 18.2% for ISR. Without ISR pressure, model defaults to embedding conclusion in premises.\n3. **Neither method produces reliable genuine proofs**: ISR pooled genuine 6.1%, Random pooled genuine 11.0%. Both far below SFT baseline (~93% genuine).\n4. **Both show extreme inter-seed variance**: ISR ranges 0%–17.3% genuine; Random ranges 1.1%–22.8%. Single-seed results unreliable.\n\n---\n\n## Pending\n\n- [ ] Random s44-r2 (plan018-additive-random-b01-s44-r2): RUNNING. Add to table when complete.\n- [ ] Investigate s42 reclassification sum mismatch (80 vs 79).\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "d3f0cb62-acb5-49ee-8c8a-8e6fee644b38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T18:11:04.815Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_012vLCF6DxrW3tHsUiBRa7wX`</summary>

```json
{
  "name": "3seed_comparison_table",
  "type": "report",
  "description": "Random β=0.1 vs ISR β=0.1 cross-seed comparison table with pooled statistics. ISR 3-seed complete, Random 2-seed provisional (s44-r2 running).",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_comparison_table.md",
  "tags": [
    "cross-seed",
    "comparison",
    "random-vs-isr",
    "beta-0.1",
    "taxonomy"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83078868-cd29-412c-8c90-f4ae9686ac28",
  "isSidechain": false,
  "requestId": "req_011Cb4oeCfsAgd9NswrWKMo2",
  "type": "assistant",
  "uuid": "3afd2272-d59f-4f2c-87a1-9310f881ad6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DeDXD9wy3VkhsUhraDBkU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4755,
      "cache_read_input_tokens": 52634,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4755,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 270,
          "cache_read_input_tokens": 52634,
          "cache_creation_input_tokens": 4755,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4755
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

_source line 44 · 2026-05-15T18:11:05.022Z_

<details><summary>↩ Tool result · `toolu_012vLCF6DxrW3tHsUiBRa7wX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_c00dd1\", \"name\": \"3seed_comparison_table\", \"type\": \"report\", \"description\": \"Random β=0.1 vs ISR β=0.1 cross-seed comparison table with pooled statistics. ISR 3-seed complete, Random 2-seed provisional (s44-r2 running).\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/report/3seed_comparison_table.md\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T18:11:04.822618+00:00\", \"tags\": [\"cross-seed\", \"comparison\", \"random-vs-isr\", \"beta-0.1\", \"taxonomy\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3afd2272-d59f-4f2c-87a1-9310f881ad6b",
  "isSidechain": false,
  "promptId": "db93fe6a-8875-4790-b540-188c747c78ba",
  "type": "user",
  "uuid": "b388dc5b-226e-47a0-bd6b-4bc749e855dd",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_c00dd1\\\", \\\"name\\\": \\\"3seed_comparison_table\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Random β=0.1 vs ISR β=0.1 cross-seed comparison table with pooled statistics. ISR 3-seed complete, Random 2-seed provisional (s44-r2 running).\\\", \\\"path\\\": \\\"projects/solver-trace-ablation/artifacts/_project/report/3seed_comparison_table.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"solver-trace-ablation\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T18:11:04.822618+00:00\\\", \\\"tags\\\": [\\\"cross-seed\\\", \\\"comparison\\\", \\\"random-vs-isr\\\", \\\"beta-0.1\\\", \\\"taxonomy\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_c00dd1\", \"name\": \"3seed_comparison_table\", \"type\": \"report\", \"description\": \"Random β=0.1 vs ISR β=0.1 cross-seed comparison table with pooled statistics. ISR 3-seed complete, Random 2-seed provisional (s44-r2 running).\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/report/3seed_comparison_table.md\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T18:11:04.822618+00:00\", \"tags\": [\"cross-seed\", \"comparison\", \"random-vs-isr\", \"beta-0.1\", \"taxonomy\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "3afd2272-d59f-4f2c-87a1-9310f881ad6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-15T18:11:10.723Z_

产出已写入并注册。

**发现一个数据问题**：plan018-additive-random-b01-s42 在 2026-05-15 被重新分类，registry 当前值 (H1=58, H8=4, genuine=18) 与你提供的旧值 (H1=56, H8=3, genuine_strict=12) 不一致。且新值存在内部矛盾：H7+H1+H8+genuine = 80 ≠ n_proved=79，有一个 sample 被重复计数。需要排查。

**核心结论**：
- ISR pooled genuine 6.06% (14/231), dominant failure = H7 tautology (70.6%)
- Random pooled genuine 10.98% (19/173, 2-seed provisional), dominant failure = H1 embedding (65.9%)
- 两种方法的 genuine rate 都远低于 SFT baseline (~93%)，且 inter-seed variance 极大

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b388dc5b-226e-47a0-bd6b-4bc749e855dd",
  "isSidechain": false,
  "requestId": "req_011Cb4oeZdBkdMgD2w7HYSTJ",
  "type": "assistant",
  "uuid": "ae48f637-da9f-4b87-975a-e15a807f8eba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFtT3zgVkSK6dCnjyuzd4p",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 578,
      "cache_read_input_tokens": 57389,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 57389,
          "cache_creation_input_tokens": 578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 578
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

_source line 46_

```json
{
  "type": "last-prompt",
  "leafUuid": "ae48f637-da9f-4b87-975a-e15a807f8eba",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Organize Random and ISR β=0.1 3-seed comparison table",
  "sessionId": "cd2ba71d-676c-402f-b1b9-4ca852b9e861"
}
```

---
