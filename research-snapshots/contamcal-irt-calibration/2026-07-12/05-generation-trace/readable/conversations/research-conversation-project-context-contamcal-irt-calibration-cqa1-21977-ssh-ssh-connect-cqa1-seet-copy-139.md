# Research conversation: <project_context> # 项目: contamcal-irt-calibration ## 运行环境 - 服务器名: cqa1-21977 - SSH 连接命令: ssh connect.cqa1.seetacloud.com

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/e6028e88-e01b-4b8d-a6df-b73d9e802fc1.jsonl`
- **Structured JSON:** [`f30637834995ded09a23.json`](../../sessions/f3/f30637834995ded09a23.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T04:08:11.223Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T04:08:11.223Z",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "content": "&lt;project_context>\n# 项目: contamcal-irt-calibration\n\n## 运行环境\n- 服务器名: cqa1-21977\n- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/contamcal-irt-calibration\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 提交实验前必须检查目标 GPU 上是否已有同类进程（nvidia-smi 查 PID + 对比 output dir），有则不提交（原因：GPU 2 因重复提交导致 4 次进程冲突和数据污染。on_failed hook 触发的 worker 和手动提交都不做查重。）\n- **C002**: 提交 GPU 任务前必须用 nvidia-smi 确认目标 GPU 空闲，不得仅依赖 get_project_resource_usage 判断（原因：resource_usage 工具因 PID/tmux 不匹配严重误报（cuda:0/2/3 活跃但报 idle），已导致调度风险。Reviewer 2026-05-14 确认。）\n- **C003**: 标记实验为 failed 时必须同时 kill 所有关联 GPU 进程；submit 新任务到 GPU 前必须先 nvidia-smi + ps 确认该 GPU 无残留进程（原因：GPU 2 两次出现\"标 failed 不 kill 进程\"导致新旧进程冲突、数据腐败风险。v3 标 failed 但 2 个子进程存活，v4 提交时未检查，造成三进程竞争同一 output-dir。）\n- **C004**: 提交 GPU 实验时必须在命令中显式设置 CUDA_VISIBLE_DEVICES=N，不依赖默认行为（原因：已两次出现声明 cuda:3 实际跑在 cuda:0 的事故（PID 498153、PID 513900/513826），根因是 tmux/nohup 启动时未显式传递 CUDA_VISIBLE_DEVICES。）\n- **C005**: 禁止在 cuda:4 有 SFT 训练运行时提交 compute_signals 任务到 cuda:4；signals_3B 任务必须等目标 GPU 独占空闲后再提交（原因：cuda:4 三次出现未授权 compute_signals 进程与 d000_v3 SFT 抢显存（PID 590509, 605267, 607648）。来源疑为旧 session Worker 或 auto-loop 触发的 signals 批量任务。必须杜绝 signals 任务与 SFT 训练共享 GPU。）\n- **C006**: 禁止在 alpha=16 checkpoint 上启动任何任务（训练/eval/信号计算）。废弃目录黑名单：Qwen2.5-3B_d000_s42, Qwen2.5-3B_d000_v2_s42, Qwen2.5-3B_d005_s42, Qwen2.5-3B_d025_s42, Qwen2.5-3B_d100_s42（不含 _v3/_v2 等 alpha=32 重训版本）。启动前必须 cat adapter_config.json | grep lora_alpha 确认 =32。（原因：D055/D076 决定全部标准化到 alpha=32 + lr=5e-5。本 session 已 4 次发现 Worker 在废弃 alpha=16 checkpoint 上启动信号计算，每次 kill 后又重启新进程，累计浪费 10+ GPU-hours。根因是 Worker prompt 中缺少废弃 checkpoint 黑名单。） [来自 D055]\n- **C007**: GPU 释放后优先级：0.5B s123 signals > 1.5B s123 signals > d100_a32_s123 signals > 其他。0.5B/1.5B s123 全部完成前不分配 GPU 给低优先级信号任务。（原因：0.5B/1.5B s123 合计 +8 respondents 是达到 N≥16 IRT 门槛的最高 ROI 路径，d100 仅 +1。Reviewer 第三次确认优先级倒挂风险。）\n- **C008**: IRT 模型选择规则：2PL+γ 为默认（robust，N<16 可用）；4PL+γ 仅当 N≥16 且 benchmark 为 MCQ format 时使用。N<16 时 4PL 的 c/d 参数不可识别，会导致 PPP=0 和校准恶化。（原因：ARC N=5 使用 4PL+γ 导致 PPP=0.000、MAE 从 0.004 恶化到 0.068（过参数化）。Director 指令要求建立模型选择规则供后续所有 IRT fitting 使用。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：重写 Method section (§3)\n\n### 目标\n基于现有两个版本（method.tex + method.md），按 writing_plan 的 outline 重构 Method section。输出完整 LaTeX .tex 文件内容（不含 preamble，只有 \\section{Method} 开始的正文）。\n\n### 重要：先读取写作规范\n执行前必须 `Read /home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md` 和 `Read /home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n\n### 现有文件位置\n- 当前 method.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex`\n- 较新 method.md: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/method.md`\n- references.bib: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib`\n\n### 目标结构（来自 writing_plan）\n\n**Word budget: 1100 words**\n\n3.1 Problem Formulation\n- Given model j, benchmark k with items i\n- Goal: diagnose contamination effects at domain level + estimate θ_j^clean\n- Three IRT adaptations (from educational measurement to LLM evaluation)\n\n3.2 Stage 1: Multi-Signal Exposure Mapping\n- 4 signals (S1-S4), RRF aggregation\n- Meta-circularity argument for training-free fusion\n- Note S2/S4 failure modes (detailed analysis in §5.2)\n\n3.3 Stage 2: Contamination-Augmented IRT\n- **KEY CHANGE**: 2PL+γ is PRIMARY model: P(y=1) = σ(a_i(θ_j - b_i + γ_k·e_ij))\n- Per-domain γ_k WITHIN benchmark (e.g., MMLU has 8 domains, each with own γ)\n- 4PL extension for MC benchmarks (ARC/MMLU) adds c_i, d_i asymptotes\n- Stan NUTS inference, convergence diagnostics\n- Calibrated score = counterfactual (e_ij=0)\n\n3.4 Fisher Information and Identifiability\n- Derive I(γ) dependence on signal quality (exposure variance)\n- AUC=0.55 structural lower bound (lowest tested), N≥50 practical threshold\n- CI width ∝ N^{-0.48}\n- Domain-method mismatch: LLM eval N=8-30 vs required N≥50\n\n3.5 Calibration Value Decomposition (D120/D121)\n- CRITICAL FRAMING: vanilla 2PL ≈ 2PL+γ on calibration MAE (ALL benchmarks)\n- Numbers: GSM8K 0.0063 vs 0.0062; MMLU 0.0068 vs 0.0070; ARC 0.0158 vs 0.0201\n- Calibration benefit ENTIRELY from IRT ability estimation (θ separation from noise)\n- γ provides DIAGNOSTIC value only (which domains inflated/deflated, direction, magnitude)\n- This STRENGTHENS diagnostic framing: γ reveals hidden structure that aggregate metrics miss\n\n### 关键改动（相对现有 method.tex）\n1. **2PL+γ 为 PRIMARY**：主方程用 2PL，4PL 作为 MC extension（一段话）\n2. **Per-domain γ_k**：明确说 MMLU 等有 domain 结构的 benchmark 可以 fit per-domain γ\n3. **Fisher Info 正文精简**：只保留关键结论（AUC=0.55, N≥50, scaling law），完整推导引用 Appendix A\n4. **§3.5 独立段落**：明确区分 calibration value (θ) vs diagnostic value (γ)，用具体数字\n\n### 写作约束\n- 禁止 em-dash (—) 和解释性 en-dash (–)\n- 禁止 -ing 短语结尾\n- 禁止 \"Furthermore\" / \"Moreover\" / \"Additionally\" 连续使用\n- 禁止 \"delve into\" / \"leverage\" / \"utilize\"\n- 定量声明必须有证据来源标注（e.g., from exp-004 simulation）\n- LaTeX 数学公式必须 numbered (\\begin{equation})\n- 用 \\citep{} / \\citet{} 引用，key 必须在 references.bib 中存在\n- 不超过 1100 words\n\n### 输出\n将完整 .tex 内容写入：\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex`\n\n完成后打印 word count 确认在 budget 内。"
}
```

---

### Runtime record

_source line 2 · 2026-05-17T04:08:11.235Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T04:08:11.235Z",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-17T04:08:11.365Z_

&lt;project_context>
# 项目: contamcal-irt-calibration

## 运行环境
- 服务器名: cqa1-21977
- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/contamcal-irt-calibration

## ⚠️ 活跃约束（必须遵守）

- **C001**: 提交实验前必须检查目标 GPU 上是否已有同类进程（nvidia-smi 查 PID + 对比 output dir），有则不提交（原因：GPU 2 因重复提交导致 4 次进程冲突和数据污染。on_failed hook 触发的 worker 和手动提交都不做查重。）
- **C002**: 提交 GPU 任务前必须用 nvidia-smi 确认目标 GPU 空闲，不得仅依赖 get_project_resource_usage 判断（原因：resource_usage 工具因 PID/tmux 不匹配严重误报（cuda:0/2/3 活跃但报 idle），已导致调度风险。Reviewer 2026-05-14 确认。）
- **C003**: 标记实验为 failed 时必须同时 kill 所有关联 GPU 进程；submit 新任务到 GPU 前必须先 nvidia-smi + ps 确认该 GPU 无残留进程（原因：GPU 2 两次出现"标 failed 不 kill 进程"导致新旧进程冲突、数据腐败风险。v3 标 failed 但 2 个子进程存活，v4 提交时未检查，造成三进程竞争同一 output-dir。）
- **C004**: 提交 GPU 实验时必须在命令中显式设置 CUDA_VISIBLE_DEVICES=N，不依赖默认行为（原因：已两次出现声明 cuda:3 实际跑在 cuda:0 的事故（PID 498153、PID 513900/513826），根因是 tmux/nohup 启动时未显式传递 CUDA_VISIBLE_DEVICES。）
- **C005**: 禁止在 cuda:4 有 SFT 训练运行时提交 compute_signals 任务到 cuda:4；signals_3B 任务必须等目标 GPU 独占空闲后再提交（原因：cuda:4 三次出现未授权 compute_signals 进程与 d000_v3 SFT 抢显存（PID 590509, 605267, 607648）。来源疑为旧 session Worker 或 auto-loop 触发的 signals 批量任务。必须杜绝 signals 任务与 SFT 训练共享 GPU。）
- **C006**: 禁止在 alpha=16 checkpoint 上启动任何任务（训练/eval/信号计算）。废弃目录黑名单：Qwen2.5-3B_d000_s42, Qwen2.5-3B_d000_v2_s42, Qwen2.5-3B_d005_s42, Qwen2.5-3B_d025_s42, Qwen2.5-3B_d100_s42（不含 _v3/_v2 等 alpha=32 重训版本）。启动前必须 cat adapter_config.json | grep lora_alpha 确认 =32。（原因：D055/D076 决定全部标准化到 alpha=32 + lr=5e-5。本 session 已 4 次发现 Worker 在废弃 alpha=16 checkpoint 上启动信号计算，每次 kill 后又重启新进程，累计浪费 10+ GPU-hours。根因是 Worker prompt 中缺少废弃 checkpoint 黑名单。） [来自 D055]
- **C007**: GPU 释放后优先级：0.5B s123 signals > 1.5B s123 signals > d100_a32_s123 signals > 其他。0.5B/1.5B s123 全部完成前不分配 GPU 给低优先级信号任务。（原因：0.5B/1.5B s123 合计 +8 respondents 是达到 N≥16 IRT 门槛的最高 ROI 路径，d100 仅 +1。Reviewer 第三次确认优先级倒挂风险。）
- **C008**: IRT 模型选择规则：2PL+γ 为默认（robust，N<16 可用）；4PL+γ 仅当 N≥16 且 benchmark 为 MCQ format 时使用。N<16 时 4PL 的 c/d 参数不可识别，会导致 PPP=0 和校准恶化。（原因：ARC N=5 使用 4PL+γ 导致 PPP=0.000、MAE 从 0.004 恶化到 0.068（过参数化）。Director 指令要求建立模型选择规则供后续所有 IRT fitting 使用。）


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：重写 Method section (§3)

### 目标
基于现有两个版本（method.tex + method.md），按 writing_plan 的 outline 重构 Method section。输出完整 LaTeX .tex 文件内容（不含 preamble，只有 \section{Method} 开始的正文）。

### 重要：先读取写作规范
执行前必须 `Read /home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md` 和 `Read /home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`

### 现有文件位置
- 当前 method.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex`
- 较新 method.md: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/method.md`
- references.bib: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib`

### 目标结构（来自 writing_plan）

**Word budget: 1100 words**

3.1 Problem Formulation
- Given model j, benchmark k with items i
- Goal: diagnose contamination effects at domain level + estimate θ_j^clean
- Three IRT adaptations (from educational measurement to LLM evaluation)

3.2 Stage 1: Multi-Signal Exposure Mapping
- 4 signals (S1-S4), RRF aggregation
- Meta-circularity argument for training-free fusion
- Note S2/S4 failure modes (detailed analysis in §5.2)

3.3 Stage 2: Contamination-Augmented IRT
- **KEY CHANGE**: 2PL+γ is PRIMARY model: P(y=1) = σ(a_i(θ_j - b_i + γ_k·e_ij))
- Per-domain γ_k WITHIN benchmark (e.g., MMLU has 8 domains, each with own γ)
- 4PL extension for MC benchmarks (ARC/MMLU) adds c_i, d_i asymptotes
- Stan NUTS inference, convergence diagnostics
- Calibrated score = counterfactual (e_ij=0)

3.4 Fisher Information and Identifiability
- Derive I(γ) dependence on signal quality (exposure variance)
- AUC=0.55 structural lower bound (lowest tested), N≥50 practical threshold
- CI width ∝ N^{-0.48}
- Domain-method mismatch: LLM eval N=8-30 vs required N≥50

3.5 Calibration Value Decomposition (D120/D121)
- CRITICAL FRAMING: vanilla 2PL ≈ 2PL+γ on calibration MAE (ALL benchmarks)
- Numbers: GSM8K 0.0063 vs 0.0062; MMLU 0.0068 vs 0.0070; ARC 0.0158 vs 0.0201
- Calibration benefit ENTIRELY from IRT ability estimation (θ separation from noise)
- γ provides DIAGNOSTIC value only (which domains inflated/deflated, direction, magnitude)
- This STRENGTHENS diagnostic framing: γ reveals hidden structure that aggregate metrics miss

### 关键改动（相对现有 method.tex）
1. **2PL+γ 为 PRIMARY**：主方程用 2PL，4PL 作为 MC extension（一段话）
2. **Per-domain γ_k**：明确说 MMLU 等有 domain 结构的 benchmark 可以 fit per-domain γ
3. **Fisher Info 正文精简**：只保留关键结论（AUC=0.55, N≥50, scaling law），完整推导引用 Appendix A
4. **§3.5 独立段落**：明确区分 calibration value (θ) vs diagnostic value (γ)，用具体数字

### 写作约束
- 禁止 em-dash (—) 和解释性 en-dash (–)
- 禁止 -ing 短语结尾
- 禁止 "Furthermore" / "Moreover" / "Additionally" 连续使用
- 禁止 "delve into" / "leverage" / "utilize"
- 定量声明必须有证据来源标注（e.g., from exp-004 simulation）
- LaTeX 数学公式必须 numbered (\begin{equation})
- 用 \citep{} / \citet{} 引用，key 必须在 references.bib 中存在
- 不超过 1100 words

### 输出
将完整 .tex 内容写入：
`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex`

完成后打印 word count 确认在 budget 内。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a6e775ec-3f10-4982-9c94-8b07992debf7",
  "type": "user",
  "uuid": "f01bbd1a-ab3b-45db-8cc8-a7df46188481",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T04:08:11.364Z_

```json
{
  "parentUuid": "f01bbd1a-ab3b-45db-8cc8-a7df46188481",
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
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
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
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "d9a79afe-a37b-4361-9b80-f0f2eb64fe83",
  "timestamp": "2026-05-17T04:08:11.364Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T04:08:11.364Z_

```json
{
  "parentUuid": "d9a79afe-a37b-4361-9b80-f0f2eb64fe83",
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
  "uuid": "b6d75a0f-8be7-424b-9c5e-129e44b49215",
  "timestamp": "2026-05-17T04:08:11.364Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-17T04:08:11.364Z_

```json
{
  "parentUuid": "b6d75a0f-8be7-424b-9c5e-129e44b49215",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9911e3d5-0699-40ad-acba-102c0c1bafe9",
  "timestamp": "2026-05-17T04:08:11.364Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
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
  "aiTitle": "Rewrite Method section with 2PL+γ primary model",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1"
}
```

---

### Assistant

_source line 8 · 2026-05-17T04:08:16.273Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the required files to understand the context and existing content before writing the new method section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9911e3d5-0699-40ad-acba-102c0c1bafe9",
  "isSidechain": false,
  "requestId": "req_011Cb7UzPutt6RJSXTeJY8Ha",
  "type": "assistant",
  "uuid": "73f08016-2608-4df0-b1eb-7b9a389986c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDy1fJJDbUVEjCHkGTETF4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15108,
      "cache_read_input_tokens": 11841,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15108
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

_source line 9 · 2026-05-17T04:08:16.667Z_

I'll read the required reference files and existing drafts to write the Method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73f08016-2608-4df0-b1eb-7b9a389986c9",
  "isSidechain": false,
  "requestId": "req_011Cb7UzPutt6RJSXTeJY8Ha",
  "type": "assistant",
  "uuid": "7be66099-0e42-406d-908a-5de9c3239e9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDy1fJJDbUVEjCHkGTETF4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15108,
      "cache_read_input_tokens": 11841,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15108
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

_source line 10 · 2026-05-17T04:08:17.129Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HucCmhyc1nTykPjgaETUWP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7be66099-0e42-406d-908a-5de9c3239e9a",
  "isSidechain": false,
  "requestId": "req_011Cb7UzPutt6RJSXTeJY8Ha",
  "type": "assistant",
  "uuid": "8452ef23-7ff5-4bdc-95a3-5fa8aef4f2e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDy1fJJDbUVEjCHkGTETF4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15108,
      "cache_read_input_tokens": 11841,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15108
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

_source line 11 · 2026-05-17T04:08:17.140Z_

<details><summary>↩ Tool result · `toolu_01HucCmhyc1nTykPjgaETUWP`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages. Stage~1 (\S\ref{sec:stage1}) estimates per-item contamination exposure by fusing multiple detection signals into a single score. Stage~2 (\S\ref{sec:stage2}--\S\ref{sec:calibrated}) embeds these scores as covariates in a contamination-augmented IRT model, performing Bayesian inference to produce calibrated benchmark scores with credible intervals.
5	
6	\subsection{Stage 1: Multi-Signal Provenance Mapping}
7	\label{sec:stage1}
8	
9	For each model~$i$ and benchmark item~$j$, we compute four complementary detection signals that capture different facets of contamination evidence.
10	
11	\paragraph{Embedding-based near-duplicate retrieval.}
12	We embed both training corpus segments and benchmark items using a sentence transformer encoder and build a FAISS index over training embeddings for efficient retrieval. The signal $s_1(i,j)$ is the maximum cosine similarity between item~$j$ and the top-$K$ retrieved training segments for model~$i$'s training corpus, capturing semantic overlap that survives paraphrasing and surface-level reformulation.
13	
14	\paragraph{Min-K\%++ membership inference.}
15	Following \citet{duan2025minkpp}, we compute the average log-probability of the $k\%$ least-likely tokens in each benchmark item under model~$i$, z-scored against a reference (clean) model. Contaminated items yield systematically higher (less negative) Min-K\%++ scores, as the model assigns elevated probability to tokens it has memorized during training. The signal $s_2(i,j)$ is the resulting membership inference statistic. We use a simplified variant that z-normalizes per-item against a single reference model's mean and standard deviation, rather than the per-token z-scoring of the original formulation; since the downstream RRF aggregation operates on ranks rather than raw scores, this simplification preserves signal ordering while reducing computational cost.
16	
17	\paragraph{ConStat performance gap.}
18	For each benchmark item, we generate a semantically equivalent paraphrased variant using an independent rewriter model. The signal $s_3(i,j)$ is the accuracy gap between model~$i$'s performance on the original item versus its paraphrased counterpart \citep{dekoninck2024constat}. A model that has memorized the original surface form but genuinely understands the underlying concept should perform comparably on both versions; a large gap indicates surface-level memorization rather than robust capability.
19	
20	\paragraph{Self-Critique entropy collapse.}
21	When model~$i$ is prompted to evaluate the correctness of its own response to item~$j$, contaminated items elicit low-entropy self-evaluation distributions---the model exhibits overconfidence in its assessment of memorized content \citep{wust2025selfcritique}. The signal $s_4(i,j)$ is the negative entropy of the self-critique distribution. This signal is particularly valuable because it operates at the meta-cognitive level and exhibits greater robustness to RL post-training than signals relying on token-level statistics (\S\ref{sec:signal_survival}).
22	
23	\paragraph{Signal survival analysis.}
24	\label{sec:signal_survival}
25	Prior work suggests that detection signals do not degrade uniformly across training regimes. \citet{wang2025fragility} demonstrate that RL post-training with GRPO substantially degrades probability-based detection signals (Min-K\%++, ConStat), while entropy-based approaches such as Self-Critique retain greater robustness by exploiting policy collapse rather than probability gaps. This motivates our inclusion of Self-Critique alongside probability-based signals: if the signal~$\times$~regime interaction is confirmed in our controlled experiments, it has two practical consequences. First, exposure estimates for RL-trained models would carry higher uncertainty, which the measurement error model in Stage~2 propagates into appropriately wider credible intervals. Second, a cliff-like (rather than gradual) degradation pattern would imply that RL fundamentally restructures the model's relationship to memorized content, rather than merely attenuating detection signals. We systematically evaluate signal survival across training regimes in \S\ref{sec:experiments}.% TODO: fill in quantitative AUC values from exp-008 results
26	
27	\paragraph{RRF aggregation.}
28	We aggregate the four signals via reciprocal rank fusion \citep{cormack2009}. For each model~$i$, items are ranked independently by each signal~$s$, and the fused exposure score is:
29	\begin{equation}
30	\label{eq:rrf}
31	    e_{ij} = \sum_{s=1}^{4} \frac{1}{k + r_{s,i}(j)},
32	\end{equation}
33	where $r_{s,i}(j)$ is the rank of item~$j$ under signal~$s$ for model~$i$, and $k = 60$ is the standard RRF smoothing constant. RRF is a deliberate design choice over learned aggregation (\emph{e.g.}, logistic regression over signal scores). A learned aggregator requires labeled training data indicating which items are truly contaminated---but ground-truth contamination labels are precisely what we lack, and the aggregator's training data may itself be contaminated, creating meta-circularity. RRF avoids this by requiring no training, providing a robust, parameter-free fusion baseline.
34	
35	We note that KDS \citep{xu2025kds} provides a complementary detection signal based on knowledge distillation signatures, but requires per-model LoRA fine-tuning at $O(N^2)$ computational cost. We include KDS in ablation experiments but exclude it from the default pipeline for scalability.
36	
37	\subsection{Stage 2: Contamination-Augmented 4PL IRT}
38	\label{sec:stage2}
39	
40	\paragraph{Model specification.}
41	We augment the standard four-parameter logistic (4PL) IRT model \citep{lord1980} with a contamination covariate. The probability that model~$i$ correctly answers item~$j$ is:
42	\begin{equation}
43	\label{eq:4pl}
44	    P(y_{ij} = 1 \mid \boldsymbol{\psi}) = c_j + (d_j - c_j)\,\sigma\!\bigl(a_j(\theta_i - b_j) + \gamma \cdot \tau_{ij}\bigr),
45	\end{equation}
46	where $\sigma(\cdot)$ denotes the logistic function, $y_{ij} \in \{0,1\}$ is the binary response, and $\boldsymbol{\psi}$ collects all parameters. The standard IRT parameters are: $\theta_i \in \mathbb{R}$ (ability of model~$i$), $a_j > 0$ (discrimination of item~$j$), $b_j \in \mathbb{R}$ (difficulty of item~$j$), $c_j \in [0,1]$ (guessing/lower asymptote), and $d_j \in [0,1]$ (upper asymptote/slip parameter). The contamination-specific parameters are: $\gamma \in \mathbb{R}$ (global contamination effect) and $\tau_{ij} \geq 0$ (latent true exposure of model~$i$ to item~$j$).
47	
48	The additive structure $a_j(\theta_i - b_j) + \gamma \cdot \tau_{ij}$ admits a natural interpretation: contamination exposure shifts the effective ability of a model on a given item by $\gamma \cdot \tau_{ij} / a_j$ units on the ability scale. When $\tau_{ij} = 0$ (no contamination), Eq.~\eqref{eq:4pl} reduces to the standard 4PL model. A positive~$\gamma$ indicates that contamination inflates performance, as expected.
49	
50	\paragraph{Measurement error model.}
51	The latent exposure $\tau_{ij}$ is not directly observed; we observe the noisy RRF-derived estimate $e_{ij}$ from Stage~1. We model this relationship as:
52	\begin{equation}
53	\label{eq:measurement_error}
54	    \tau_{ij} \sim \mathcal{N}(e_{ij},\, \sigma_e^2),
55	\end{equation}
56	where $\sigma_e^2$ is the measurement error variance, estimated jointly with other model parameters. This formulation treats the observed exposure scores as noisy proxies for latent contamination and has two critical consequences. First, uncertainty in the detection signals is automatically propagated into the posterior over ability~$\theta_i$ and contamination effect~$\gamma$, yielding appropriately wider credible intervals when signals are unreliable. Second, under RL post-training---where signal degradation is severe (\S\ref{sec:signal_survival})---the posterior distribution of~$\tau_{ij}$ becomes more diffuse, producing wider credible intervals that honestly reflect our reduced ability to distinguish contaminated from clean items.
57	
58	\paragraph{Prior specification.}
59	We assign the following priors:
60	\begin{align}
61	    \theta_i &\sim \mathcal{N}(0, 1), \label{eq:prior_theta} \\
62	    a_j &\sim \text{LogNormal}(0, 0.5), \label{eq:prior_a} \\
63	    b_j &\sim \mathcal{N}(0, 1), \label{eq:prior_b} \\
64	    c_j &\sim \text{Beta}(5, 20), \label{eq:prior_c} \\
65	    d_j &\sim \text{Beta}(20, 5), \label{eq:prior_d} \\
66	    \gamma &\sim \mathcal{N}(0, 1). \label{eq:prior_gamma}
67	\end{align}
68	The $\text{Beta}(5, 20)$ prior on~$c_j$ encodes the expectation that guessing rates are low (mean $\approx 0.2$) but non-negligible for multiple-choice items. The $\text{Beta}(20, 5)$ prior on~$d_j$ reflects the expectation that upper asymptotes are high (mean $\approx 0.8$) but not necessarily unity, allowing for careless errors or ambiguous items. The $\text{LogNormal}(0, 0.5)$ prior on~$a_j$ constrains discrimination to be positive with moderate magnitude (median $= 1$). The weakly informative $\mathcal{N}(0, 1)$ prior on~$\gamma$ permits both positive and negative contamination effects; we conduct sensitivity analyses under $\mathcal{N}(0, 0.5)$ and $\mathcal{N}(0, 2)$ to assess robustness to this specification (\S\ref{sec:experiments}).
69	
70	\paragraph{Connection to item compromise IRT.}
71	Equation~\eqref{eq:4pl} extends the item compromise IRT tradition \citep{eckerly2017,sinharay2017} with three structural adaptations for the LLM evaluation setting.
72	
73	\emph{Adaptation~1: Independent examinees $\to$ shared item pool.} In educational testing, each examinee independently samples from a population ability distribution. In LLM evaluation, a single model responds to all items, and its responses are correlated through shared model parameters. This alters the local independence assumption: conditional on~$\theta_i$, item responses within a single model may remain correlated through model-specific idiosyncrasies not captured by the scalar ability parameter \citep{mislevy1986,sanmartin2009}. We mitigate this by fitting IRT models per-benchmark---reducing the scope of potential violations---and empirically assessing residual correlations via posterior predictive checks (\S\ref{sec:experiments}).
74	
75	\emph{Adaptation~2: Binary leakage $\to$ continuous exposure.} Classical item compromise models use binary indicators $e_{ij} \in \{0, 1\}$ \citep{sinharay2017}. We generalize to continuous exposure scores $\tau_{ij} \in \mathbb{R}^+$ derived from noisy detection signals, which is standard in explanatory IRT \citep{deboeck2004} but necessitates the measurement error formulation of Eq.~\eqref{eq:measurement_error} to prevent attenuation bias from regression dilution \citep{maris2009}.
76	
77	\emph{Adaptation~3: Stable ability $\to$ regime-conditional ability.} An examinee's ability is typically assumed stable across test items. For LLMs, the training regime (SFT vs.\ RL) qualitatively changes both the model's ability profile and the reliability of detection signals. We handle this through the signal survival analysis (\S\ref{sec:signal_survival}), which informs the measurement error variance, rather than through regime-specific ability parameters---preserving model parsimony while acknowledging regime effects through the uncertainty channel.
78	
79	\subsection{Bayesian Inference}
80	\label{sec:inference}
81	
82	We perform full Bayesian inference using the No-U-Turn Sampler \citep[NUTS;][]{hoffman2014} implemented in CmdStanPy \citep{carpenter2017}. We run four independent Markov chains and assess convergence via three diagnostics: split-$\hat{R} < 1.01$ for all parameters, effective sample size $\text{ESS} > 400$ per parameter, and fewer than 0.1\% divergent transitions. The target acceptance probability is set to $\texttt{adapt\_delta} = 0.95$ to reduce divergences in the high-curvature posterior geometry induced by the 4PL model's bounded response function.
83	
84	\paragraph{Per-benchmark fitting.}
85	Rather than fitting a single IRT model jointly across all benchmarks, we fit separate models per benchmark. This design choice reduces the scope of local independence violations: within a single benchmark, items share a common knowledge domain, making the conditional independence assumption more defensible than across heterogeneous benchmarks encompassing knowledge recall, mathematical reasoning, and code generation \citep{sanmartin2009}. Per-benchmark fitting also naturally yields benchmark-specific contamination effects~$\gamma_k$ (\S\ref{sec:calibrated}), the primary specification in our framework.
86	
87	\paragraph{Few-examinee regime.}
88	Standard IRT applications assume large examinee populations ($N > 200$), but current LLM evaluation studies may include as few as 20--50 models. In this low-$N$ regime, item parameter estimation becomes unstable without informative priors. We address this by incorporating empirical Bayes priors for item parameters derived from the Growing Pains study \citep{polo2026growing}, which provides item parameter estimates from a pool of 400+ models. Specifically, the item difficulty and discrimination priors are centered at the Growing Pains point estimates with moderately inflated variances, serving as a regularizing anchor while permitting data-driven updating. We validate this prior transfer procedure via simulation-based calibration \citep[SBC;][]{talts2018sbc}, confirming that posteriors are well-calibrated under the specified priors across a range of sample sizes (\S\ref{sec:experiments}). Automatic differentiation variational inference \citep[ADVI;][]{ulitzsch2022} is explored as a scalability option for larger item pools in the appendix, though preliminary results indicate ADVI may fail to converge for the 4PL specification due to the bounded response function's multimodal posterior geometry; we include the comparison for completeness.
89	
90	\subsection{Calibrated Score Computation}
91	\label{sec:calibrated}
92	
93	Given the posterior distribution over all parameters, we compute the calibrated (decontaminated) accuracy for model~$i$ on benchmark~$B$ by setting exposure to zero and marginalizing over posterior uncertainty:
94	\begin{equation}
95	\label{eq:calibrated}
96	    \text{Acc}_{i}^{\text{cal}} = \frac{1}{|B|} \sum_{j \in B}\, \mathbb{E}_{\boldsymbol{\psi} \sim p(\boldsymbol{\psi} \mid \mathbf{y})} \!\left[ c_j + (d_j - c_j)\,\sigma\!\bigl(a_j(\theta_i - b_j)\bigr) \right],
97	\end{equation}
98	where the expectation is taken over posterior draws of~$\boldsymbol{\psi}$ and the contamination term $\gamma \cdot \tau_{ij}$ has been removed. This counterfactual quantity answers: \emph{what would model~$i$'s expected accuracy be on benchmark~$B$ had it never been exposed to any test items during training?}
99	
100	In practice, we approximate Eq.~\eqref{eq:calibrated} by averaging over $L$ posterior draws $\{\boldsymbol{\psi}^{(\ell)}\}_{\ell=1}^{L}$:
101	\begin{equation}
102	\label{eq:calibrated_mc}
103	    \widehat{\text{Acc}}_{i}^{\text{cal}} = \frac{1}{L} \sum_{\ell=1}^{L} \frac{1}{|B|} \sum_{j \in B} \left[ c_j^{(\ell)} + (d_j^{(\ell)} - c_j^{(\ell)})\,\sigma\!\bigl(a_j^{(\ell)}(\theta_i^{(\ell)} - b_j^{(\ell)})\bigr) \right].
104	\end{equation}
105	Credible intervals at level~$\alpha$ are obtained from the empirical quantiles of $\{\text{Acc}_{i}^{\text{cal},(\ell)}\}_{\ell=1}^{L}$. We report 50\%, 80\%, and 95\% intervals. By construction, models with higher exposure scores and noisier detection signals---whose $\tau_{ij}$ posteriors are more diffuse---receive wider credible intervals, encoding the principle that calibration is only as reliable as its inputs.
106	
107	\paragraph{Per-benchmark contamination effects.}
108	Since we fit independent models per benchmark (\S\ref{sec:inference}), each benchmark naturally yields its own contamination effect parameter~$\gamma_k$:
109	\begin{equation}
110	\label{eq:per_benchmark_gamma}
111	    P(y_{ij} = 1 \mid \boldsymbol{\psi}_k) = c_j + (d_j - c_j)\,\sigma\!\bigl(a_j(\theta_i - b_j) + \gamma_k \cdot \tau_{ij}\bigr),
112	\end{equation}
113	where $\gamma_k$ is the contamination effect specific to benchmark~$k$, with independent priors $\gamma_k \sim \mathcal{N}(0, 1)$. This is the primary specification, permitting heterogeneous contamination effects across benchmarks.
114	
115	\paragraph{Calibration value decomposition.}
116	The calibrated score in Eq.~\eqref{eq:calibrated} depends on the ability estimate~$\theta_i$, not on $\gamma_k$ directly. Two distinct mechanisms contribute to calibration quality: (a)~the IRT ability estimation itself, which separates stable model capability from item-specific noise regardless of the contamination model; and (b)~the explicit $\gamma_k$ correction, which reweights items based on exposure during the joint estimation of~$\theta_i$. In principle, including $\gamma_k$ should yield better $\theta_i$ estimates by absorbing contamination variance. In practice, we compare calibration MAE between the full model (2PL+$\gamma$) and vanilla 2PL ($\gamma\!=\!0$) to quantify the marginal calibration contribution of the contamination covariate (\S\ref{sec:results}). The $\gamma_k$ parameters serve a complementary diagnostic role: they reveal which domains or benchmarks exhibit inflation, deflation, or model misfit, providing actionable characterization that aggregate calibration metrics cannot deliver.
117	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8452ef23-7ff5-4bdc-95a3-5fa8aef4f2e3",
  "isSidechain": false,
  "promptId": "a6e775ec-3f10-4982-9c94-8b07992debf7",
  "type": "user",
  "uuid": "e9d6a776-9e26-49c2-90d0-6f350e3fefda",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nContamCal operates in two stages. Stage~1 (\\S\\ref{sec:stage1}) estimates per-item contamination exposure by fusing multiple detection signals into a single score. Stage~2 (\\S\\ref{sec:stage2}--\\S\\ref{sec:calibrated}) embeds these scores as covariates in a contamination-augmented IRT model, performing Bayesian inference to produce calibrated benchmark scores with credible intervals.\n\n\\subsection{Stage 1: Multi-Signal Provenance Mapping}\n\\label{sec:stage1}\n\nFor each model~$i$ and benchmark item~$j$, we compute four complementary detection signals that capture different facets of contamination evidence.\n\n\\paragraph{Embedding-based near-duplicate retrieval.}\nWe embed both training corpus segments and benchmark items using a sentence transformer encoder and build a FAISS index over training embeddings for efficient retrieval. The signal $s_1(i,j)$ is the maximum cosine similarity between item~$j$ and the top-$K$ retrieved training segments for model~$i$'s training corpus, capturing semantic overlap that survives paraphrasing and surface-level reformulation.\n\n\\paragraph{Min-K\\%++ membership inference.}\nFollowing \\citet{duan2025minkpp}, we compute the average log-probability of the $k\\%$ least-likely tokens in each benchmark item under model~$i$, z-scored against a reference (clean) model. Contaminated items yield systematically higher (less negative) Min-K\\%++ scores, as the model assigns elevated probability to tokens it has memorized during training. The signal $s_2(i,j)$ is the resulting membership inference statistic. We use a simplified variant that z-normalizes per-item against a single reference model's mean and standard deviation, rather than the per-token z-scoring of the original formulation; since the downstream RRF aggregation operates on ranks rather than raw scores, this simplification preserves signal ordering while reducing computational cost.\n\n\\paragraph{ConStat performance gap.}\nFor each benchmark item, we generate a semantically equivalent paraphrased variant using an independent rewriter model. The signal $s_3(i,j)$ is the accuracy gap between model~$i$'s performance on the original item versus its paraphrased counterpart \\citep{dekoninck2024constat}. A model that has memorized the original surface form but genuinely understands the underlying concept should perform comparably on both versions; a large gap indicates surface-level memorization rather than robust capability.\n\n\\paragraph{Self-Critique entropy collapse.}\nWhen model~$i$ is prompted to evaluate the correctness of its own response to item~$j$, contaminated items elicit low-entropy self-evaluation distributions---the model exhibits overconfidence in its assessment of memorized content \\citep{wust2025selfcritique}. The signal $s_4(i,j)$ is the negative entropy of the self-critique distribution. This signal is particularly valuable because it operates at the meta-cognitive level and exhibits greater robustness to RL post-training than signals relying on token-level statistics (\\S\\ref{sec:signal_survival}).\n\n\\paragraph{Signal survival analysis.}\n\\label{sec:signal_survival}\nPrior work suggests that detection signals do not degrade uniformly across training regimes. \\citet{wang2025fragility} demonstrate that RL post-training with GRPO substantially degrades probability-based detection signals (Min-K\\%++, ConStat), while entropy-based approaches such as Self-Critique retain greater robustness by exploiting policy collapse rather than probability gaps. This motivates our inclusion of Self-Critique alongside probability-based signals: if the signal~$\\times$~regime interaction is confirmed in our controlled experiments, it has two practical consequences. First, exposure estimates for RL-trained models would carry higher uncertainty, which the measurement error model in Stage~2 propagates into appropriately wider credible intervals. Second, a cliff-like (rather than gradual) degradation pattern would imply that RL fundamentally restructures the model's relationship to memorized content, rather than merely attenuating detection signals. We systematically evaluate signal survival across training regimes in \\S\\ref{sec:experiments}.% TODO: fill in quantitative AUC values from exp-008 results\n\n\\paragraph{RRF aggregation.}\nWe aggregate the four signals via reciprocal rank fusion \\citep{cormack2009}. For each model~$i$, items are ranked independently by each signal~$s$, and the fused exposure score is:\n\\begin{equation}\n\\label{eq:rrf}\n    e_{ij} = \\sum_{s=1}^{4} \\frac{1}{k + r_{s,i}(j)},\n\\end{equation}\nwhere $r_{s,i}(j)$ is the rank of item~$j$ under signal~$s$ for model~$i$, and $k = 60$ is the standard RRF smoothing constant. RRF is a deliberate design choice over learned aggregation (\\emph{e.g.}, logistic regression over signal scores). A learned aggregator requires labeled training data indicating which items are truly contaminated---but ground-truth contamination labels are precisely what we lack, and the aggregator's training data may itself be contaminated, creating meta-circularity. RRF avoids this by requiring no training, providing a robust, parameter-free fusion baseline.\n\nWe note that KDS \\citep{xu2025kds} provides a complementary detection signal based on knowledge distillation signatures, but requires per-model LoRA fine-tuning at $O(N^2)$ computational cost. We include KDS in ablation experiments but exclude it from the default pipeline for scalability.\n\n\\subsection{Stage 2: Contamination-Augmented 4PL IRT}\n\\label{sec:stage2}\n\n\\paragraph{Model specification.}\nWe augment the standard four-parameter logistic (4PL) IRT model \\citep{lord1980} with a contamination covariate. The probability that model~$i$ correctly answers item~$j$ is:\n\\begin{equation}\n\\label{eq:4pl}\n    P(y_{ij} = 1 \\mid \\boldsymbol{\\psi}) = c_j + (d_j - c_j)\\,\\sigma\\!\\bigl(a_j(\\theta_i - b_j) + \\gamma \\cdot \\tau_{ij}\\bigr),\n\\end{equation}\nwhere $\\sigma(\\cdot)$ denotes the logistic function, $y_{ij} \\in \\{0,1\\}$ is the binary response, and $\\boldsymbol{\\psi}$ collects all parameters. The standard IRT parameters are: $\\theta_i \\in \\mathbb{R}$ (ability of model~$i$), $a_j > 0$ (discrimination of item~$j$), $b_j \\in \\mathbb{R}$ (difficulty of item~$j$), $c_j \\in [0,1]$ (guessing/lower asymptote), and $d_j \\in [0,1]$ (upper asymptote/slip parameter). The contamination-specific parameters are: $\\gamma \\in \\mathbb{R}$ (global contamination effect) and $\\tau_{ij} \\geq 0$ (latent true exposure of model~$i$ to item~$j$).\n\nThe additive structure $a_j(\\theta_i - b_j) + \\gamma \\cdot \\tau_{ij}$ admits a natural interpretation: contamination exposure shifts the effective ability of a model on a given item by $\\gamma \\cdot \\tau_{ij} / a_j$ units on the ability scale. When $\\tau_{ij} = 0$ (no contamination), Eq.~\\eqref{eq:4pl} reduces to the standard 4PL model. A positive~$\\gamma$ indicates that contamination inflates performance, as expected.\n\n\\paragraph{Measurement error model.}\nThe latent exposure $\\tau_{ij}$ is not directly observed; we observe the noisy RRF-derived estimate $e_{ij}$ from Stage~1. We model this relationship as:\n\\begin{equation}\n\\label{eq:measurement_error}\n    \\tau_{ij} \\sim \\mathcal{N}(e_{ij},\\, \\sigma_e^2),\n\\end{equation}\nwhere $\\sigma_e^2$ is the measurement error variance, estimated jointly with other model parameters. This formulation treats the observed exposure scores as noisy proxies for latent contamination and has two critical consequences. First, uncertainty in the detection signals is automatically propagated into the posterior over ability~$\\theta_i$ and contamination effect~$\\gamma$, yielding appropriately wider credible intervals when signals are unreliable. Second, under RL post-training---where signal degradation is severe (\\S\\ref{sec:signal_survival})---the posterior distribution of~$\\tau_{ij}$ becomes more diffuse, producing wider credible intervals that honestly reflect our reduced ability to distinguish contaminated from clean items.\n\n\\paragraph{Prior specification.}\nWe assign the following priors:\n\\begin{align}\n    \\theta_i &\\sim \\mathcal{N}(0, 1), \\label{eq:prior_theta} \\\\\n    a_j &\\sim \\text{LogNormal}(0, 0.5), \\label{eq:prior_a} \\\\\n    b_j &\\sim \\mathcal{N}(0, 1), \\label{eq:prior_b} \\\\\n    c_j &\\sim \\text{Beta}(5, 20), \\label{eq:prior_c} \\\\\n    d_j &\\sim \\text{Beta}(20, 5), \\label{eq:prior_d} \\\\\n    \\gamma &\\sim \\mathcal{N}(0, 1). \\label{eq:prior_gamma}\n\\end{align}\nThe $\\text{Beta}(5, 20)$ prior on~$c_j$ encodes the expectation that guessing rates are low (mean $\\approx 0.2$) but non-negligible for multiple-choice items. The $\\text{Beta}(20, 5)$ prior on~$d_j$ reflects the expectation that upper asymptotes are high (mean $\\approx 0.8$) but not necessarily unity, allowing for careless errors or ambiguous items. The $\\text{LogNormal}(0, 0.5)$ prior on~$a_j$ constrains discrimination to be positive with moderate magnitude (median $= 1$). The weakly informative $\\mathcal{N}(0, 1)$ prior on~$\\gamma$ permits both positive and negative contamination effects; we conduct sensitivity analyses under $\\mathcal{N}(0, 0.5)$ and $\\mathcal{N}(0, 2)$ to assess robustness to this specification (\\S\\ref{sec:experiments}).\n\n\\paragraph{Connection to item compromise IRT.}\nEquation~\\eqref{eq:4pl} extends the item compromise IRT tradition \\citep{eckerly2017,sinharay2017} with three structural adaptations for the LLM evaluation setting.\n\n\\emph{Adaptation~1: Independent examinees $\\to$ shared item pool.} In educational testing, each examinee independently samples from a population ability distribution. In LLM evaluation, a single model responds to all items, and its responses are correlated through shared model parameters. This alters the local independence assumption: conditional on~$\\theta_i$, item responses within a single model may remain correlated through model-specific idiosyncrasies not captured by the scalar ability parameter \\citep{mislevy1986,sanmartin2009}. We mitigate this by fitting IRT models per-benchmark---reducing the scope of potential violations---and empirically assessing residual correlations via posterior predictive checks (\\S\\ref{sec:experiments}).\n\n\\emph{Adaptation~2: Binary leakage $\\to$ continuous exposure.} Classical item compromise models use binary indicators $e_{ij} \\in \\{0, 1\\}$ \\citep{sinharay2017}. We generalize to continuous exposure scores $\\tau_{ij} \\in \\mathbb{R}^+$ derived from noisy detection signals, which is standard in explanatory IRT \\citep{deboeck2004} but necessitates the measurement error formulation of Eq.~\\eqref{eq:measurement_error} to prevent attenuation bias from regression dilution \\citep{maris2009}.\n\n\\emph{Adaptation~3: Stable ability $\\to$ regime-conditional ability.} An examinee's ability is typically assumed stable across test items. For LLMs, the training regime (SFT vs.\\ RL) qualitatively changes both the model's ability profile and the reliability of detection signals. We handle this through the signal survival analysis (\\S\\ref{sec:signal_survival}), which informs the measurement error variance, rather than through regime-specific ability parameters---preserving model parsimony while acknowledging regime effects through the uncertainty channel.\n\n\\subsection{Bayesian Inference}\n\\label{sec:inference}\n\nWe perform full Bayesian inference using the No-U-Turn Sampler \\citep[NUTS;][]{hoffman2014} implemented in CmdStanPy \\citep{carpenter2017}. We run four independent Markov chains and assess convergence via three diagnostics: split-$\\hat{R} < 1.01$ for all parameters, effective sample size $\\text{ESS} > 400$ per parameter, and fewer than 0.1\\% divergent transitions. The target acceptance probability is set to $\\texttt{adapt\\_delta} = 0.95$ to reduce divergences in the high-curvature posterior geometry induced by the 4PL model's bounded response function.\n\n\\paragraph{Per-benchmark fitting.}\nRather than fitting a single IRT model jointly across all benchmarks, we fit separate models per benchmark. This design choice reduces the scope of local independence violations: within a single benchmark, items share a common knowledge domain, making the conditional independence assumption more defensible than across heterogeneous benchmarks encompassing knowledge recall, mathematical reasoning, and code generation \\citep{sanmartin2009}. Per-benchmark fitting also naturally yields benchmark-specific contamination effects~$\\gamma_k$ (\\S\\ref{sec:calibrated}), the primary specification in our framework.\n\n\\paragraph{Few-examinee regime.}\nStandard IRT applications assume large examinee populations ($N > 200$), but current LLM evaluation studies may include as few as 20--50 models. In this low-$N$ regime, item parameter estimation becomes unstable without informative priors. We address this by incorporating empirical Bayes priors for item parameters derived from the Growing Pains study \\citep{polo2026growing}, which provides item parameter estimates from a pool of 400+ models. Specifically, the item difficulty and discrimination priors are centered at the Growing Pains point estimates with moderately inflated variances, serving as a regularizing anchor while permitting data-driven updating. We validate this prior transfer procedure via simulation-based calibration \\citep[SBC;][]{talts2018sbc}, confirming that posteriors are well-calibrated under the specified priors across a range of sample sizes (\\S\\ref{sec:experiments}). Automatic differentiation variational inference \\citep[ADVI;][]{ulitzsch2022} is explored as a scalability option for larger item pools in the appendix, though preliminary results indicate ADVI may fail to converge for the 4PL specification due to the bounded response function's multimodal posterior geometry; we include the comparison for completeness.\n\n\\subsection{Calibrated Score Computation}\n\\label{sec:calibrated}\n\nGiven the posterior distribution over all parameters, we compute the calibrated (decontaminated) accuracy for model~$i$ on benchmark~$B$ by setting exposure to zero and marginalizing over posterior uncertainty:\n\\begin{equation}\n\\label{eq:calibrated}\n    \\text{Acc}_{i}^{\\text{cal}} = \\frac{1}{|B|} \\sum_{j \\in B}\\, \\mathbb{E}_{\\boldsymbol{\\psi} \\sim p(\\boldsymbol{\\psi} \\mid \\mathbf{y})} \\!\\left[ c_j + (d_j - c_j)\\,\\sigma\\!\\bigl(a_j(\\theta_i - b_j)\\bigr) \\right],\n\\end{equation}\nwhere the expectation is taken over posterior draws of~$\\boldsymbol{\\psi}$ and the contamination term $\\gamma \\cdot \\tau_{ij}$ has been removed. This counterfactual quantity answers: \\emph{what would model~$i$'s expected accuracy be on benchmark~$B$ had it never been exposed to any test items during training?}\n\nIn practice, we approximate Eq.~\\eqref{eq:calibrated} by averaging over $L$ posterior draws $\\{\\boldsymbol{\\psi}^{(\\ell)}\\}_{\\ell=1}^{L}$:\n\\begin{equation}\n\\label{eq:calibrated_mc}\n    \\widehat{\\text{Acc}}_{i}^{\\text{cal}} = \\frac{1}{L} \\sum_{\\ell=1}^{L} \\frac{1}{|B|} \\sum_{j \\in B} \\left[ c_j^{(\\ell)} + (d_j^{(\\ell)} - c_j^{(\\ell)})\\,\\sigma\\!\\bigl(a_j^{(\\ell)}(\\theta_i^{(\\ell)} - b_j^{(\\ell)})\\bigr) \\right].\n\\end{equation}\nCredible intervals at level~$\\alpha$ are obtained from the empirical quantiles of $\\{\\text{Acc}_{i}^{\\text{cal},(\\ell)}\\}_{\\ell=1}^{L}$. We report 50\\%, 80\\%, and 95\\% intervals. By construction, models with higher exposure scores and noisier detection signals---whose $\\tau_{ij}$ posteriors are more diffuse---receive wider credible intervals, encoding the principle that calibration is only as reliable as its inputs.\n\n\\paragraph{Per-benchmark contamination effects.}\nSince we fit independent models per benchmark (\\S\\ref{sec:inference}), each benchmark naturally yields its own contamination effect parameter~$\\gamma_k$:\n\\begin{equation}\n\\label{eq:per_benchmark_gamma}\n    P(y_{ij} = 1 \\mid \\boldsymbol{\\psi}_k) = c_j + (d_j - c_j)\\,\\sigma\\!\\bigl(a_j(\\theta_i - b_j) + \\gamma_k \\cdot \\tau_{ij}\\bigr),\n\\end{equation}\nwhere $\\gamma_k$ is the contamination effect specific to benchmark~$k$, with independent priors $\\gamma_k \\sim \\mathcal{N}(0, 1)$. This is the primary specification, permitting heterogeneous contamination effects across benchmarks.\n\n\\paragraph{Calibration value decomposition.}\nThe calibrated score in Eq.~\\eqref{eq:calibrated} depends on the ability estimate~$\\theta_i$, not on $\\gamma_k$ directly. Two distinct mechanisms contribute to calibration quality: (a)~the IRT ability estimation itself, which separates stable model capability from item-specific noise regardless of the contamination model; and (b)~the explicit $\\gamma_k$ correction, which reweights items based on exposure during the joint estimation of~$\\theta_i$. In principle, including $\\gamma_k$ should yield better $\\theta_i$ estimates by absorbing contamination variance. In practice, we compare calibration MAE between the full model (2PL+$\\gamma$) and vanilla 2PL ($\\gamma\\!=\\!0$) to quantify the marginal calibration contribution of the contamination covariate (\\S\\ref{sec:results}). The $\\gamma_k$ parameters serve a complementary diagnostic role: they reveal which domains or benchmarks exhibit inflation, deflation, or model misfit, providing actionable characterization that aggregate calibration metrics cannot deliver.\n",
      "numLines": 117,
      "startLine": 1,
      "totalLines": 117
    }
  },
  "sourceToolAssistantUUID": "8452ef23-7ff5-4bdc-95a3-5fa8aef4f2e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T04:08:18.060Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B665hMFzCNouWYc99o5uUa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/method.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9d6a776-9e26-49c2-90d0-6f350e3fefda",
  "isSidechain": false,
  "requestId": "req_011Cb7UzPutt6RJSXTeJY8Ha",
  "type": "assistant",
  "uuid": "bf50c362-62e3-4d6e-a09f-17409f85911b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDy1fJJDbUVEjCHkGTETF4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15108,
      "cache_read_input_tokens": 11841,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15108
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

_source line 13 · 2026-05-17T04:08:18.066Z_

<details><summary>↩ Tool result · `toolu_01B665hMFzCNouWYc99o5uUa`</summary>

```text
1	## 3 Method
2	
3	ContamCal is a two-stage framework that maps observed item responses and contamination exposure signals to calibrated ability estimates. Stage 1 produces per-item exposure scores from multiple detection signals via training-free fusion. Stage 2 fits a contamination-augmented IRT model that decomposes observed performance into latent ability and contamination effects.
4	
5	### 3.1 Problem Formulation
6	
7	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model $j$ ($j=1,\ldots,J$) to item $i$ ($i=1,\ldots,I_k$) on benchmark $k$. Standard IRT models assume $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ are item parameters. When training data contains benchmark items, observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
8	
9	Our goal is to estimate $\theta_j^{\text{clean}}$, the decontaminated ability---what model $j$'s performance would be had it never encountered the test items during training. We approach this through contamination-augmented IRT, drawing on item compromise IRT (Eckerly, 2017; Sinharay, 2017) and explanatory IRT (De Boeck & Wilson, 2004). Adapting these frameworks to LLM evaluation requires three structural modifications:
10	
11	**(a) Independent examinees $\to$ shared item distribution.** Classical IRT assumes independent test-takers. In LLM evaluation, a single model produces all item responses, and items are fixed across models. We treat the model ensemble as the examinee population and fit per-benchmark to limit local independence violations.
12	
13	**(b) Binary leakage $\to$ continuous exposure.** Item compromise IRT uses binary indicators (leaked / not leaked). LLM contamination is graded: a model may have seen an item zero, once, or hundreds of times during training. We replace binary indicators with continuous exposure scores $e_{ij} \in [0,1]$ estimated from detection signals.
14	
15	**(c) Stable ability $\to$ regime-conditional ability.** In educational testing, ability is approximately constant regardless of item compromise status. For LLMs, contamination can alter internal representations, so we model ability as conditional on the contamination regime and recover clean ability via counterfactual inference.
16	
17	### 3.2 Stage 1: Multi-Signal Exposure Mapping
18	
19	We estimate per-item exposure scores from three complementary contamination detection signals:
20	
21	**S1: Embedding similarity.** Cosine similarity between the sentence embedding of each benchmark item and its nearest neighbor in the SFT training corpus, computed via a frozen encoder. High similarity indicates verbatim or near-verbatim inclusion.
22	
23	**S2: Min-K++ (Zhang et al., 2024).** A membership inference signal based on the model's own token-level surprisal distribution. Items seen during training are expected to exhibit lower perplexity on their rarest tokens. We include this signal despite known failure modes (Section 5.2) to systematically characterize signal reliability across scales.
24	
25	**S4: Self-critique (Weller et al., 2024).** A generation-based signal where the model is prompted to assess whether it has encountered a given item during training.
26	
27	We exclude S3 (ConStat; Dekoninck et al., 2024) because its gap-based statistic produces zero values for items where all answer options have identical surprisal, diluting the signal, and its low item coverage introduces selection bias.
28	
29	**Aggregation.** We fuse signals via Reciprocal Rank Fusion (RRF; Cormack et al., 2009):
30	
31	$$e_i^{\text{raw}} = \sum_{s \in \mathcal{S}} \frac{w_s}{k + \text{rank}_s(i)}$$
32	
33	where $\text{rank}_s(i)$ is the rank of item $i$ under signal $s$ (rank 1 = most suspicious), $k=60$ is the smoothing constant, and $w_s = 1$ for all signals. Raw scores are min-max normalized per model to obtain $e_{ij} \in [0,1]$.
34	
35	RRF is a training-free fusion method. This is a deliberate design choice rather than a limitation: any learned aggregator requires labeled training data, but contamination labels are precisely what we lack---the aggregator's training data may itself be contaminated. We term this the *meta-circularity* problem. RRF sidesteps it by operating on rank orderings without parameter estimation.
36	
37	### 3.3 Stage 2: Contamination-Augmented IRT
38	
39	We extend the four-parameter logistic (4PL) IRT model with a contamination covariate. For each benchmark $k$, fitted independently:
40	
41	$$P(y_{ijk}=1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr)$$
42	
43	where $\sigma(\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i$ is item difficulty, $c_i \in (0,1)$ is the guessing asymptote, $d_i \in (0,1)$ is the ceiling asymptote, $\theta_j$ is model ability, $e_{ij}$ is the exposure score from Stage 1, and $\gamma_k$ is the benchmark-specific contamination effect.
44	
45	The contamination term $\gamma_k \cdot e_{ij}$ enters additively on the logit scale, outside the discrimination parameter $a_i$. This makes $\gamma_k$ directly interpretable: it represents the logit shift for a maximally exposed item ($e_{ij}=1$) relative to a clean item ($e_{ij}=0$), uniformly across items regardless of their discrimination.
46	
47	Crucially, $\gamma_k$ is signed: $\gamma_k > 0$ indicates performance inflation (memorization benefit), while $\gamma_k < 0$ indicates interference or forgetting---a possibility absent from the implicit "contamination = uniform inflation" assumption in most prior work. Per-benchmark fitting (rather than a joint model with shared $\gamma$) is our primary specification, reflecting the empirical finding that contamination effects are heterogeneous across benchmarks (Section 5.1).
48	
49	We also fit 2PL+$\gamma$ as a reduced model (omitting $c_i$, $d_i$) for benchmarks where guessing and ceiling effects are minimal, such as free-form generation tasks.
50	
51	**Inference.** We use Stan's No-U-Turn Sampler (NUTS) with 4 chains, 1000 warmup + 1000 sampling iterations, and target acceptance rate 0.95. Weakly informative priors: $\theta_j \sim \mathcal{N}(0,1)$, $a_i \sim \text{LogNormal}(0, 0.5)$, $b_i \sim \mathcal{N}(0,1)$, $c_i \sim \text{Beta}(5, 20)$, $d_i \sim \text{Beta}(20, 5)$, $\gamma_k \sim \mathcal{N}(0,1)$. Convergence requires $\hat{R} < 1.01$ and bulk ESS $> 400$.
52	
53	**Calibrated scores.** The decontaminated score for model $j$ on benchmark $k$ is the posterior expectation of the counterfactual under zero exposure:
54	
55	$$\hat{s}_{jk}^{\text{clean}} = \frac{1}{I_k}\sum_{i=1}^{I_k} P(y_{ijk}=1 \mid e_{ij}=0)$$
56	
57	with posterior uncertainty propagated through the MCMC samples to yield credible intervals. This counterfactual---"what accuracy would this model achieve if none of the items had been exposed?"---is the central quantity of interest for calibration.
58	
59	### 3.4 Fisher Information and Identifiability
60	
61	The reliability of $\gamma_k$ estimation depends on two factors: the discriminative quality of exposure scores (signal AUC) and the number of models $J$. We analyze identifiability via the expected Fisher Information $\mathcal{I}(\gamma)$ for the 4PL+$\gamma$ model (full derivation in Appendix A).
62	
63	The key insight is that $\mathcal{I}(\gamma)$ depends on the variance of exposure scores across models for each item. When signal AUC is low, exposure scores become nearly uniform across contaminated and clean items, collapsing $\text{Var}(e_{\cdot i})$ toward zero and rendering $\gamma$ structurally unidentifiable regardless of sample size.
64	
65	We validate these predictions via a simulation sweep across 24 conditions (4 AUC levels $\times$ 4 ensemble sizes, plus 8 extreme-$\gamma$ conditions; 10 seeds each, 240 runs total; Section 5.3). Recovery was successful down to AUC $= 0.55$, the lowest value tested, with bias $< 0.05$ and 95% CI coverage $\geq 90\%$ at $J \geq 50$; the lower bound of signal quality required for identifiability remains open. Posterior CI width scales as $J^{-0.48}$ (empirically estimated), close to the parametric $J^{-0.5}$ rate.
66	
67	This analysis reveals a *domain-method mismatch*: IRT-based LLM evaluation studies typically pool $J = 8$--$30$ models per benchmark (e.g., Polo et al., 2024; Lalor et al., 2024), well below the $J \geq 50$ regime where our simulations show reliable $\gamma$ recovery. This structural gap---not merely insufficient data, but a fundamental mismatch between the sample sizes available in LLM evaluation and the requirements of the statistical method---is itself a central finding of this work.
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf50c362-62e3-4d6e-a09f-17409f85911b",
  "isSidechain": false,
  "promptId": "a6e775ec-3f10-4982-9c94-8b07992debf7",
  "type": "user",
  "uuid": "767eaae6-4264-4d05-bc0a-70bb63e8d937",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/method.md",
      "content": "## 3 Method\n\nContamCal is a two-stage framework that maps observed item responses and contamination exposure signals to calibrated ability estimates. Stage 1 produces per-item exposure scores from multiple detection signals via training-free fusion. Stage 2 fits a contamination-augmented IRT model that decomposes observed performance into latent ability and contamination effects.\n\n### 3.1 Problem Formulation\n\nLet $y_{ijk} \\in \\{0,1\\}$ denote the binary response of model $j$ ($j=1,\\ldots,J$) to item $i$ ($i=1,\\ldots,I_k$) on benchmark $k$. Standard IRT models assume $P(y_{ijk}=1) = f(\\theta_j, \\boldsymbol{\\xi}_i)$ where $\\theta_j$ is latent ability and $\\boldsymbol{\\xi}_i$ are item parameters. When training data contains benchmark items, observed ability $\\hat{\\theta}_j$ confounds genuine capability with memorization.\n\nOur goal is to estimate $\\theta_j^{\\text{clean}}$, the decontaminated ability---what model $j$'s performance would be had it never encountered the test items during training. We approach this through contamination-augmented IRT, drawing on item compromise IRT (Eckerly, 2017; Sinharay, 2017) and explanatory IRT (De Boeck & Wilson, 2004). Adapting these frameworks to LLM evaluation requires three structural modifications:\n\n**(a) Independent examinees $\\to$ shared item distribution.** Classical IRT assumes independent test-takers. In LLM evaluation, a single model produces all item responses, and items are fixed across models. We treat the model ensemble as the examinee population and fit per-benchmark to limit local independence violations.\n\n**(b) Binary leakage $\\to$ continuous exposure.** Item compromise IRT uses binary indicators (leaked / not leaked). LLM contamination is graded: a model may have seen an item zero, once, or hundreds of times during training. We replace binary indicators with continuous exposure scores $e_{ij} \\in [0,1]$ estimated from detection signals.\n\n**(c) Stable ability $\\to$ regime-conditional ability.** In educational testing, ability is approximately constant regardless of item compromise status. For LLMs, contamination can alter internal representations, so we model ability as conditional on the contamination regime and recover clean ability via counterfactual inference.\n\n### 3.2 Stage 1: Multi-Signal Exposure Mapping\n\nWe estimate per-item exposure scores from three complementary contamination detection signals:\n\n**S1: Embedding similarity.** Cosine similarity between the sentence embedding of each benchmark item and its nearest neighbor in the SFT training corpus, computed via a frozen encoder. High similarity indicates verbatim or near-verbatim inclusion.\n\n**S2: Min-K++ (Zhang et al., 2024).** A membership inference signal based on the model's own token-level surprisal distribution. Items seen during training are expected to exhibit lower perplexity on their rarest tokens. We include this signal despite known failure modes (Section 5.2) to systematically characterize signal reliability across scales.\n\n**S4: Self-critique (Weller et al., 2024).** A generation-based signal where the model is prompted to assess whether it has encountered a given item during training.\n\nWe exclude S3 (ConStat; Dekoninck et al., 2024) because its gap-based statistic produces zero values for items where all answer options have identical surprisal, diluting the signal, and its low item coverage introduces selection bias.\n\n**Aggregation.** We fuse signals via Reciprocal Rank Fusion (RRF; Cormack et al., 2009):\n\n$$e_i^{\\text{raw}} = \\sum_{s \\in \\mathcal{S}} \\frac{w_s}{k + \\text{rank}_s(i)}$$\n\nwhere $\\text{rank}_s(i)$ is the rank of item $i$ under signal $s$ (rank 1 = most suspicious), $k=60$ is the smoothing constant, and $w_s = 1$ for all signals. Raw scores are min-max normalized per model to obtain $e_{ij} \\in [0,1]$.\n\nRRF is a training-free fusion method. This is a deliberate design choice rather than a limitation: any learned aggregator requires labeled training data, but contamination labels are precisely what we lack---the aggregator's training data may itself be contaminated. We term this the *meta-circularity* problem. RRF sidesteps it by operating on rank orderings without parameter estimation.\n\n### 3.3 Stage 2: Contamination-Augmented IRT\n\nWe extend the four-parameter logistic (4PL) IRT model with a contamination covariate. For each benchmark $k$, fitted independently:\n\n$$P(y_{ijk}=1) = c_i + (d_i - c_i)\\,\\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\bigr)$$\n\nwhere $\\sigma(\\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i$ is item difficulty, $c_i \\in (0,1)$ is the guessing asymptote, $d_i \\in (0,1)$ is the ceiling asymptote, $\\theta_j$ is model ability, $e_{ij}$ is the exposure score from Stage 1, and $\\gamma_k$ is the benchmark-specific contamination effect.\n\nThe contamination term $\\gamma_k \\cdot e_{ij}$ enters additively on the logit scale, outside the discrimination parameter $a_i$. This makes $\\gamma_k$ directly interpretable: it represents the logit shift for a maximally exposed item ($e_{ij}=1$) relative to a clean item ($e_{ij}=0$), uniformly across items regardless of their discrimination.\n\nCrucially, $\\gamma_k$ is signed: $\\gamma_k > 0$ indicates performance inflation (memorization benefit), while $\\gamma_k < 0$ indicates interference or forgetting---a possibility absent from the implicit \"contamination = uniform inflation\" assumption in most prior work. Per-benchmark fitting (rather than a joint model with shared $\\gamma$) is our primary specification, reflecting the empirical finding that contamination effects are heterogeneous across benchmarks (Section 5.1).\n\nWe also fit 2PL+$\\gamma$ as a reduced model (omitting $c_i$, $d_i$) for benchmarks where guessing and ceiling effects are minimal, such as free-form generation tasks.\n\n**Inference.** We use Stan's No-U-Turn Sampler (NUTS) with 4 chains, 1000 warmup + 1000 sampling iterations, and target acceptance rate 0.95. Weakly informative priors: $\\theta_j \\sim \\mathcal{N}(0,1)$, $a_i \\sim \\text{LogNormal}(0, 0.5)$, $b_i \\sim \\mathcal{N}(0,1)$, $c_i \\sim \\text{Beta}(5, 20)$, $d_i \\sim \\text{Beta}(20, 5)$, $\\gamma_k \\sim \\mathcal{N}(0,1)$. Convergence requires $\\hat{R} < 1.01$ and bulk ESS $> 400$.\n\n**Calibrated scores.** The decontaminated score for model $j$ on benchmark $k$ is the posterior expectation of the counterfactual under zero exposure:\n\n$$\\hat{s}_{jk}^{\\text{clean}} = \\frac{1}{I_k}\\sum_{i=1}^{I_k} P(y_{ijk}=1 \\mid e_{ij}=0)$$\n\nwith posterior uncertainty propagated through the MCMC samples to yield credible intervals. This counterfactual---\"what accuracy would this model achieve if none of the items had been exposed?\"---is the central quantity of interest for calibration.\n\n### 3.4 Fisher Information and Identifiability\n\nThe reliability of $\\gamma_k$ estimation depends on two factors: the discriminative quality of exposure scores (signal AUC) and the number of models $J$. We analyze identifiability via the expected Fisher Information $\\mathcal{I}(\\gamma)$ for the 4PL+$\\gamma$ model (full derivation in Appendix A).\n\nThe key insight is that $\\mathcal{I}(\\gamma)$ depends on the variance of exposure scores across models for each item. When signal AUC is low, exposure scores become nearly uniform across contaminated and clean items, collapsing $\\text{Var}(e_{\\cdot i})$ toward zero and rendering $\\gamma$ structurally unidentifiable regardless of sample size.\n\nWe validate these predictions via a simulation sweep across 24 conditions (4 AUC levels $\\times$ 4 ensemble sizes, plus 8 extreme-$\\gamma$ conditions; 10 seeds each, 240 runs total; Section 5.3). Recovery was successful down to AUC $= 0.55$, the lowest value tested, with bias $< 0.05$ and 95% CI coverage $\\geq 90\\%$ at $J \\geq 50$; the lower bound of signal quality required for identifiability remains open. Posterior CI width scales as $J^{-0.48}$ (empirically estimated), close to the parametric $J^{-0.5}$ rate.\n\nThis analysis reveals a *domain-method mismatch*: IRT-based LLM evaluation studies typically pool $J = 8$--$30$ models per benchmark (e.g., Polo et al., 2024; Lalor et al., 2024), well below the $J \\geq 50$ regime where our simulations show reliable $\\gamma$ recovery. This structural gap---not merely insufficient data, but a fundamental mismatch between the sample sizes available in LLM evaluation and the requirements of the statistical method---is itself a central finding of this work.\n",
      "numLines": 68,
      "startLine": 1,
      "totalLines": 68
    }
  },
  "sourceToolAssistantUUID": "bf50c362-62e3-4d6e-a09f-17409f85911b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T04:08:18.230Z_

<details open><summary>🔧 Tool call — Read · `toolu_011UpHppEPLYu2jTB6rfrQdj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "767eaae6-4264-4d05-bc0a-70bb63e8d937",
  "isSidechain": false,
  "requestId": "req_011Cb7UzPutt6RJSXTeJY8Ha",
  "type": "assistant",
  "uuid": "d916430c-b9c2-4b14-8128-83701a2f0025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDy1fJJDbUVEjCHkGTETF4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15108,
      "cache_read_input_tokens": 11841,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15108
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

_source line 15_

```json
{
  "type": "last-prompt",
  "leafUuid": "d916430c-b9c2-4b14-8128-83701a2f0025",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Rewrite Method section with 2PL+γ primary model",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1"
}
```

---

### Tool result

_source line 17 · 2026-05-17T04:08:18.617Z_

<details><summary>↩ Tool result · `toolu_011UpHppEPLYu2jTB6rfrQdj`</summary>

```text
1	% ============================================================
2	% Literature Map Entries (keys from literature_map.yaml ids)
3	% ============================================================
4	
5	@inproceedings{adams_1997_mrcml,
6	  author    = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},
7	  title     = {The Multidimensional Random Coefficients Multinomial Logit Model},
8	  booktitle = {Applied Psychological Measurement},
9	  volume    = {21},
10	  number    = {1},
11	  pages     = {1--23},
12	  year      = {1997}
13	}
14	
15	@article{angelopoulos_2023_conformal,
16	  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},
17	  title         = {A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
18	  journal       = {Foundations and Trends in Machine Learning},
19	  year          = {2023},
20	  url           = {https://arxiv.org/abs/2107.07511}
21	}
22	
23	@article{brown_2024_ppp,
24	  author  = {Brown, Jeremy M. and Thomson, Robert C.},
25	  title   = {The Expected Behaviors of Posterior Predictive Tests and Their Unexpected Interpretation},
26	  journal = {Molecular Biology and Evolution},
27	  volume  = {41},
28	  number  = {3},
29	  pages   = {msae051},
30	  year    = {2024}
31	}
32	
33	@article{burnell_2023_structure,
34	  author        = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Murfet, Daniel and Zheng, Hananel and Hern\'{a}ndez-Orallo, Jos\'{e}},
35	  title         = {Revealing the Structure of Language Model Capabilities},
36	  journal       = {arXiv preprint},
37	  year          = {2023},
38	  eprint        = {2306.10062},
39	  archiveprefix = {arXiv},
40	  url           = {https://arxiv.org/abs/2306.10062}
41	}
42	
43	@inproceedings{carlini_2021_extracting,
44	  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and Lee, Katherine and Roberts, Adam and Brown, Tom and Song, Dawn and Erlingsson, Ulfar and Oprea, Alina and Raffel, Colin},
45	  title     = {Extracting Training Data from Large Language Models},
46	  booktitle = {Proceedings of the 30th USENIX Security Symposium},
47	  year      = {2021},
48	  url       = {https://arxiv.org/abs/2012.07805}
49	}
50	
51	@inproceedings{chiang_2024_chatbot_arena,
52	  author    = {Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios N. and Li, Tianle and Li, Dacheng and Zhang, Hao and Zhu, Banghua and Jordan, Michael and Gonzalez, Joseph E. and Stoica, Ion},
53	  title     = {Chatbot Arena: An Open Platform for Evaluating {LLMs} by Human Preference},
54	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
55	  year      = {2024},
56	  url       = {https://arxiv.org/abs/2403.04132}
57	}
58	
59	@inproceedings{choi_2025_kds,
60	  author    = {Choi, Yujin and Kim, Heeyoung and Lee, Jihoon and Park, Changho},
61	  title     = {How Contaminated Is Your Benchmark? Quantifying Dataset Leakage in Large Language Models with Kernel Divergence},
62	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
63	  year      = {2025},
64	  url       = {https://arxiv.org/abs/2502.00678}
65	}
66	
67	@inproceedings{cormack_2009_rrf,
68	  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},
69	  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},
70	  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},
71	  pages     = {758--759},
72	  year      = {2009},
73	  publisher = {ACM},
74	  url       = {https://dl.acm.org/doi/10.1145/1571941.1572114}
75	}
76	
77	@book{deboeck_2004_explanatory_irt,
78	  author    = {De Boeck, Paul and Wilson, Mark},
79	  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},
80	  publisher = {Springer},
81	  year      = {2004},
82	  address   = {New York},
83	  url       = {https://link.springer.com/book/10.1007/978-1-4757-3990-9}
84	}
85	
86	@article{dekoninck_2024_constat,
87	  author        = {Dekoninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},
88	  title         = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
89	  journal       = {arXiv preprint},
90	  year          = {2024},
91	  eprint        = {2405.16281},
92	  archiveprefix = {arXiv},
93	  url           = {https://arxiv.org/abs/2405.16281}
94	}
95	
96	@inproceedings{deng_2024_tsguessing,
97	  author    = {Deng, Chunyuan and Zhao, Yilun and Tang, Xiangru and Gerstein, Mark and Cohan, Arman},
98	  title     = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},
99	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
100	  year      = {2024},
101	  url       = {https://arxiv.org/abs/2311.09783}
102	}
103	
104	@inproceedings{dong_2024_cdd,
105	  author    = {Dong, Yihong and Jiang, Xue and Liu, Huanyu and Jin, Zhi and Li, Ge},
106	  title     = {Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models},
107	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},
108	  year      = {2024},
109	  url       = {https://arxiv.org/abs/2402.15938}
110	}
111	
112	@incollection{eckerly_2017_item_compromise,
113	  author    = {Eckerly, Carol},
114	  title     = {Detecting Preknowledge and Item Compromise: Understanding the Status Quo},
115	  booktitle = {Handbook of Quantitative Methods for Detecting Cheating on Tests},
116	  publisher = {Routledge},
117	  year      = {2017},
118	  url       = {https://www.routledge.com/9781138821811}
119	}
120	
121	@article{ercikan_2008_dif_cancellation,
122	  author  = {Ercikan, Kadriye and Arim, Rodrigo G. and Oliveri, Maria Elena},
123	  title   = {Differential Item Functioning Amplification and Cancellation in a Reading Test},
124	  journal = {Practical Assessment, Research, and Evaluation},
125	  volume  = {14},
126	  number  = {3},
127	  year    = {2008}
128	}
129	
130	@inproceedings{golchin_2024_time_travel,
131	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
132	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
133	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
134	  year      = {2024},
135	  url       = {https://arxiv.org/abs/2308.08493}
136	}
137	
138	@inproceedings{guo_2017_calibration,
139	  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
140	  title     = {On Calibration of Modern Neural Networks},
141	  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},
142	  pages     = {1321--1330},
143	  year      = {2017},
144	  url       = {https://arxiv.org/abs/1706.04599}
145	}
146	
147	@article{habba_2025_growing_pains,
148	  author        = {Habba, Maryam and Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},
149	  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},
150	  journal       = {arXiv preprint},
151	  year          = {2025},
152	  eprint        = {2604.12843},
153	  archiveprefix = {arXiv},
154	  url           = {https://arxiv.org/abs/2604.12843}
155	}
156	
157	@book{holland_1993_dif,
158	  author    = {Holland, Paul W. and Wainer, Howard},
159	  title     = {Differential Item Functioning},
160	  publisher = {Lawrence Erlbaum Associates},
161	  year      = {1993},
162	  address   = {Hillsdale, NJ}
163	}
164	
165	@article{kievit_2013_simpsons_paradox,
166	  author  = {Kievit, Rogier A. and Frankenhuis, Willem E. and Waldorp, Lourens J. and Borsboom, Denny},
167	  title   = {Simpson's Paradox in Psychological Science: A Practical Guide},
168	  journal = {Frontiers in Psychology},
169	  volume  = {4},
170	  pages   = {513},
171	  year    = {2013}
172	}
173	
174	@inproceedings{lalor_2024_irt_nlp,
175	  author    = {Lalor, John P. and Yang, Yi and Rodriguez, Pedro and Smith, Noah A.},
176	  title     = {Item Response Theory for Natural Language Processing},
177	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: Tutorial Abstracts (EACL)},
178	  year      = {2024},
179	  url       = {https://aclanthology.org/2024.eacl-tutorials.2/}
180	}
181	
182	@article{li_2024_atlas,
183	  author        = {Li, Guanzhong and Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},
184	  title         = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},
185	  journal       = {arXiv preprint},
186	  year          = {2024},
187	  eprint        = {2511.04689},
188	  archiveprefix = {arXiv},
189	  url           = {https://arxiv.org/abs/2511.04689}
190	}
191	
192	@article{li_2024_open_llm_leaderboard,
193	  author        = {Li, Aidar Myrzakhan and Shen, Sondos Mahmoud Bsharat and Jia, Zhiqiang},
194	  title         = {Open-{LLM}-Leaderboard: From Multi-choice to Open-style Questions for {LLMs} Evaluation, Benchmark, and Arena},
195	  journal       = {arXiv preprint},
196	  year          = {2024},
197	  eprint        = {2406.07545},
198	  archiveprefix = {arXiv},
199	  url           = {https://arxiv.org/abs/2406.07545}
200	}
201	
202	@inproceedings{li_2025_dcr,
203	  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},
204	  title     = {Decontaminated Calibration and Ranking for Trustworthy {LLM} Evaluation},
205	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
206	  year      = {2025}
207	}
208	
209	@article{liang_2023_helm,
210	  author        = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya and Newman, Benjamin and Yuan, Binhang and Yan, Bobby and Zhang, Ce and Cosgrove, Christian and Manning, Christopher D. and R\'{e}, Christopher and Acosta-Navas, Diana and Hudson, Drew A. and others},
211	  title         = {Holistic Evaluation of Language Models},
212	  journal       = {Transactions on Machine Learning Research},
213	  year          = {2023},
214	  url           = {https://arxiv.org/abs/2211.09110}
215	}
216	
217	@article{luettgau_2025_hibayes,
218	  author        = {Luettgau, Lennart and Polo, Felipe Maia and Zhuang, Yuekai and Yurochkin, Mikhail and Sun, Yuekai},
219	  title         = {{HiBayES}: A Hierarchical Bayesian Modeling Framework for {AI} Evaluation Statistics},
220	  journal       = {arXiv preprint},
221	  year          = {2025},
222	  eprint        = {2505.05602},
223	  archiveprefix = {arXiv},
224	  url           = {https://arxiv.org/abs/2505.05602}
225	}
226	
227	@article{mislevy_1986_bayes_irt,
228	  author  = {Mislevy, Robert J.},
229	  title   = {Bayes Modal Estimation in Item Response Models},
230	  journal = {Psychometrika},
231	  volume  = {51},
232	  number  = {2},
233	  pages   = {177--195},
234	  year    = {1986}
235	}
236	
237	@article{oren_2023_proving_contamination,
238	  author        = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},
239	  title         = {Proving Test Set Contamination in Black Box Language Models},
240	  journal       = {arXiv preprint},
241	  year          = {2023},
242	  eprint        = {2310.17623},
243	  archiveprefix = {arXiv},
244	  url           = {https://arxiv.org/abs/2310.17623}
245	}
246	
247	@inproceedings{polo_2024_tinybenchmarks,
248	  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},
249	  title     = {{tinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},
250	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
251	  year      = {2024},
252	  url       = {https://arxiv.org/abs/2402.14992}
253	}
254	
255	@book{reckase_2009_mirt,
256	  author    = {Reckase, Mark D.},
257	  title     = {Multidimensional Item Response Theory},
258	  publisher = {Springer},
259	  year      = {2009},
260	  address   = {New York}
261	}
262	
263	@article{sanmartin_2009_irt,
264	  author  = {San Mart\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},
265	  title   = {Consequential Validity and Item Response Theory},
266	  journal = {Psychometrika},
267	  volume  = {74},
268	  number  = {2},
269	  pages   = {349--367},
270	  year    = {2009}
271	}
272	
273	@article{schaeffer_2026_generative_contamination,
274	  author        = {Schaeffer, Rylan and Kazdan, Joshua and Abbasi, Ali and Liu, Hailey and others},
275	  title         = {Quantifying the Effect of Test Set Contamination on Generative Evaluations},
276	  journal       = {arXiv preprint},
277	  year          = {2026},
278	  eprint        = {2601.04301},
279	  archiveprefix = {arXiv},
280	  url           = {https://arxiv.org/abs/2601.04301}
281	}
282	
283	@inproceedings{shi_2023_minkprob,
284	  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
285	  title     = {Detecting Pretraining Data from Large Language Models},
286	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
287	  year      = {2024},
288	  url       = {https://arxiv.org/abs/2310.16789}
289	}
290	
291	@inproceedings{shokri_2017_mia,
292	  author    = {Shokri, Reza and Stronati, Marco and Song, Congzheng and Shmatikov, Vitaly},
293	  title     = {Membership Inference Attacks Against Machine Learning Models},
294	  booktitle = {Proceedings of the 2017 IEEE Symposium on Security and Privacy (S\&P)},
295	  year      = {2017},
296	  url       = {https://arxiv.org/abs/1610.05820}
297	}
298	
299	@article{sinharay_2017_preknowledge,
300	  author  = {Sinharay, Sandip},
301	  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},
302	  journal = {Journal of Educational and Behavioral Statistics},
303	  volume  = {42},
304	  number  = {1},
305	  year    = {2017},
306	  url     = {https://pubmed.ncbi.nlm.nih.gov/29881099/}
307	}
308	
309	@article{sinharay_2025_irt_fit,
310	  author  = {Sinharay, Sandip},
311	  title   = {Assessment of Fit of Item Response Theory Models: A Critical Review of the Status Quo and Some Future Directions},
312	  journal = {British Journal of Mathematical and Statistical Psychology},
313	  volume  = {78},
314	  pages   = {711--733},
315	  year    = {2025}
316	}
317	
318	@inproceedings{sun_2025_emperors_new_clothes,
319	  author    = {Sun, Yifan and Li, Zhen and Zhang, Yingji and Chen, Fei},
320	  title     = {The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for {LLM} Benchmark Data Contamination},
321	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
322	  year      = {2025},
323	  url       = {https://arxiv.org/abs/2503.16402}
324	}
325	
326	@article{talts_2018_sbc,
327	  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},
328	  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},
329	  journal       = {arXiv preprint},
330	  year          = {2018},
331	  eprint        = {1804.06788},
332	  archiveprefix = {arXiv},
333	  url           = {https://arxiv.org/abs/1804.06788}
334	}
335	
336	@article{wang_2024_mmlu_pro,
337	  author        = {Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and Li, Tianle and Ku, Max and Wang, Kai and Zhuang, Alex and Fan, Rongqi and Huang, Xiang and Chen, Wenhu},
338	  title         = {{MMLU-Pro}: A More Robust and Challenging Multi-Task Language Understanding Benchmark},
339	  journal       = {arXiv preprint},
340	  year          = {2024},
341	  eprint        = {2406.01574},
342	  archiveprefix = {arXiv},
343	  url           = {https://arxiv.org/abs/2406.01574}
344	}
345	
346	@article{white_2024_livebench,
347	  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},
348	  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},
349	  journal       = {arXiv preprint},
350	  year          = {2024},
351	  eprint        = {2406.19314},
352	  archiveprefix = {arXiv},
353	  url           = {https://arxiv.org/abs/2406.19314}
354	}
355	
356	@article{wust_2025_selfcritique,
357	  author        = {W\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},
358	  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},
359	  journal       = {arXiv preprint},
360	  year          = {2025},
361	  eprint        = {2510.09259},
362	  archiveprefix = {arXiv},
363	  url           = {https://arxiv.org/abs/2510.09259}
364	}
365	
366	@inproceedings{xu_2025_dcr,
367	  author    = {Xu, Yiyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},
368	  title     = {{DCR}: Quantifying Data Contamination in {LLMs} Evaluation},
369	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
370	  year      = {2025},
371	  url       = {https://arxiv.org/abs/2507.11405}
372	}
373	
374	@article{yang_2023_rethinking_benchmark,
375	  author        = {Yang, Shuo and Wei, Xin and Shi, Weicheng and Xu, Feiyu},
376	  title         = {Rethinking Benchmark and Contamination for Language Models with Rephrased Samples},
377	  journal       = {arXiv preprint},
378	  year          = {2023},
379	  eprint        = {2311.04850},
380	  archiveprefix = {arXiv},
381	  url           = {https://arxiv.org/abs/2311.04850}
382	}
383	
384	@inproceedings{zhang_2024_gsm1k,
385	  author    = {Zhang, Hugh Mee and Da, Jeff and Lee, Nayeon and Zheng, Lianmin and Sheng, Ying and Gonzalez, Joseph E. and Stoica, Ion},
386	  title     = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},
387	  booktitle = {arXiv preprint},
388	  year      = {2024},
389	  eprint    = {2405.00332},
390	  url       = {https://arxiv.org/abs/2405.00332}
391	}
392	
393	@inproceedings{zhang_2024_minkpp,
394	  author    = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},
395	  title     = {{Min-K\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
396	  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},
397	  year      = {2025},
398	  url       = {https://arxiv.org/abs/2404.02936}
399	}
400	
401	@inproceedings{zheng_2023_chatbot_arena,
402	  author    = {Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},
403	  title     = {Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},
404	  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS)},
405	  year      = {2023},
406	  url       = {https://arxiv.org/abs/2306.05685}
407	}
408	
409	@inproceedings{zhou_2025_psnirt,
410	  author    = {Zhou, Guanyu and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},
411	  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},
412	  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},
413	  year      = {2026},
414	  url       = {https://arxiv.org/abs/2505.15055}
415	}
416	
417	% ============================================================
418	% Existing Entries (preserved for backward compatibility)
419	% ============================================================
420	
421	% --- Core Methodology ---
422	
423	@book{lord1980,
424	  author    = {Lord, Frederic M.},
425	  title     = {Applications of Item Response Theory to Practical Testing Problems},
426	  publisher = {Lawrence Erlbaum Associates},
427	  year      = {1980},
428	  address   = {Hillsdale, NJ}
429	}
430	
431	@article{eckerly2017,
432	  author  = {Eckerly, Carol},
433	  title   = {Detecting Item Compromise in the Context of Item Response Theory},
434	  journal = {Applied Psychological Measurement},
435	  volume  = {41},
436	  number  = {2},
437	  pages   = {87--101},
438	  year    = {2017}
439	}
440	
441	@article{sinharay2017,
442	  author  = {Sinharay, Sandip},
443	  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},
444	  journal = {Journal of Educational and Behavioral Statistics},
445	  volume  = {42},
446	  number  = {1},
447	  pages   = {46--68},
448	  year    = {2017}
449	}
450	
451	@book{deboeck2004,
452	  author    = {De Boeck, Paul and Wilson, Mark},
453	  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},
454	  publisher = {Springer},
455	  year      = {2004},
456	  address   = {New York}
457	}
458	
459	@article{adams1997,
460	  author  = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},
461	  title   = {The Multidimensional Random Coefficients Multinomial Logit Model},
462	  journal = {Applied Psychological Measurement},
463	  volume  = {21},
464	  number  = {1},
465	  pages   = {1--23},
466	  year    = {1997}
467	}
468	
469	@article{mislevy1986,
470	  author  = {Mislevy, Robert J.},
471	  title   = {Bayes Modal Estimation in Item Response Models},
472	  journal = {Psychometrika},
473	  volume  = {51},
474	  number  = {2},
475	  pages   = {177--195},
476	  year    = {1986}
477	}
478	
479	@article{sanmartin2009,
480	  author  = {San Mart\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},
481	  title   = {Consequential Validity of Item Response Theory Models for Measuring Latent Constructs},
482	  journal = {Psychometrika},
483	  volume  = {74},
484	  number  = {2},
485	  pages   = {349--367},
486	  year    = {2009}
487	}
488	
489	@article{maris2009,
490	  author  = {Maris, Gunter and Bechger, Timo},
491	  title   = {On Interpreting the Model Parameters for the Three Parameter Logistic Model},
492	  journal = {Measurement},
493	  volume  = {7},
494	  number  = {2},
495	  pages   = {75--88},
496	  year    = {2009}
497	}
498	
499	@inproceedings{cormack2009,
500	  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},
501	  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},
502	  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},
503	  pages     = {758--759},
504	  year      = {2009},
505	  publisher = {ACM}
506	}
507	
508	% --- Bayesian Inference & Diagnostics ---
509	
510	@article{hoffman2014,
511	  author  = {Hoffman, Matthew D. and Gelman, Andrew},
512	  title   = {The {No-U-Turn} Sampler: Adaptively Setting Path Lengths in {Hamiltonian Monte Carlo}},
513	  journal = {Journal of Machine Learning Research},
514	  volume  = {15},
515	  number  = {47},
516	  pages   = {1593--1623},
517	  year    = {2014}
518	}
519	
520	@article{carpenter2017,
521	  author  = {Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Goodrich, Ben and Betancourt, Michael and Brubaker, Marcus and Guo, Jiqiang and Li, Peter and Riddell, Allen},
522	  title   = {Stan: A Probabilistic Programming Language},
523	  journal = {Journal of Statistical Software},
524	  volume  = {76},
525	  number  = {1},
526	  pages   = {1--32},
527	  year    = {2017}
528	}
529	
530	@article{talts2018sbc,
531	  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},
532	  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},
533	  journal       = {arXiv preprint},
534	  year          = {2018},
535	  eprint        = {1804.06788},
536	  archiveprefix = {arXiv}
537	}
538	
539	@article{ulitzsch2022,
540	  author  = {Ulitzsch, Esther and Nestler, Steffen},
541	  title   = {Automatic Differentiation Variational Inference for Item Response Theory Models},
542	  journal = {British Journal of Mathematical and Statistical Psychology},
543	  volume  = {75},
544	  number  = {3},
545	  pages   = {421--447},
546	  year    = {2022}
547	}
548	
549	% --- Contamination Detection Methods ---
550	
551	@inproceedings{duan2025minkpp,
552	  author    = {Duan, Jiawen and Xie, Cheng and Zhang, Jian and Li, Kai},
553	  title     = {{Min-K\%++}: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models},
554	  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},
555	  year      = {2025}
556	}
557	
558	@inproceedings{dekoninck2024constat,
559	  author    = {De Koninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},
560	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
561	  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},
562	  year      = {2024}
563	}
564	
565	@article{wust2025selfcritique,
566	  author        = {W\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},
567	  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},
568	  journal       = {arXiv preprint},
569	  year          = {2025},
570	  eprint        = {2510.09259},
571	  archiveprefix = {arXiv}
572	}
573	
574	@inproceedings{xu2025kds,
575	  author    = {Xu, Yanyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},
576	  title     = {Knowledge Distillation Signatures for Efficient Contamination Detection},
577	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
578	  year      = {2025},
579	  note      = {arXiv:2502.00678}
580	}
581	
582	@inproceedings{oren2024proving,
583	  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},
584	  title     = {Proving Test Set Contamination in Black Box Language Models},
585	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
586	  year      = {2024}
587	}
588	
589	% --- Contamination Analysis & Mitigation ---
590	
591	@inproceedings{xu2025emperor,
592	  author    = {Xu, Yiwen and Song, Kaijie and Zhou, Jianfeng and Chen, Liang},
593	  title     = {The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models},
594	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
595	  year      = {2025},
596	  note      = {arXiv:2503.16402}
597	}
598	
599	@article{dong2026dose,
600	  author        = {Dong, Yifan and Li, Xinran and Chen, Difan and Wang, Zhengyu},
601	  title         = {Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales},
602	  journal       = {arXiv preprint},
603	  year          = {2026},
604	  eprint        = {2601.04301},
605	  archiveprefix = {arXiv}
606	}
607	
608	@article{yang2026rl,
609	  author        = {Yang, Shuo and Wei, Xin and Zhang, Zhiwei and Xu, Feiyu},
610	  title         = {Reinforcement Learning Amplifies Contamination in {LLM} Benchmark Evaluation},
611	  journal       = {arXiv preprint},
612	  year          = {2026},
613	  eprint        = {2601.06103},
614	  archiveprefix = {arXiv}
615	}
616	
617	@article{wang2025fragility,
618	  author        = {Wang, Yuxin and Zhao, Yucheng and Li, Cheng and Zhang, Meng},
619	  title         = {On the Fragility of Benchmark Evaluations for Large Language Models},
620	  journal       = {arXiv preprint},
621	  year          = {2025},
622	  eprint        = {2510.02386},
623	  archiveprefix = {arXiv}
624	}
625	
626	@inproceedings{zhang2025forget,
627	  author    = {Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi},
628	  title     = {How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models},
629	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
630	  year      = {2025}
631	}
632	
633	% --- IRT for LLM Evaluation ---
634	
635	@inproceedings{gu2026psnirt,
636	  author    = {Gu, Jiaqi and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},
637	  title     = {{PSN-IRT}: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory},
638	  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},
639	  year      = {2026}
640	}
641	
642	@article{polo2026growing,
643	  author        = {Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},
644	  title         = {Growing Pains: Understanding the Limitations and Potential of {IRT} for {LLM} Evaluation at Scale},
645	  journal       = {arXiv preprint},
646	  year          = {2026},
647	  eprint        = {2604.12843},
648	  archiveprefix = {arXiv}
649	}
650	
651	@article{lyu2025atlas,
652	  author        = {Lyu, Haoran and Ding, Yufei and Wang, Hainiu and Peng, Nanyun},
653	  title         = {{ATLAS}: Adaptive Testing via Latent Ability Scoring for Large Language Models},
654	  journal       = {arXiv preprint},
655	  year          = {2025},
656	  eprint        = {2511.04689},
657	  archiveprefix = {arXiv}
658	}
659	
660	@article{zhuang2025hibayes,
661	  author        = {Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},
662	  title         = {{HiBayES}: Hierarchical {Bayesian} Evaluation System for Language Models},
663	  journal       = {arXiv preprint},
664	  year          = {2025},
665	  eprint        = {2505.05602},
666	  archiveprefix = {arXiv}
667	}
668	
669	@inproceedings{lalor2024irt,
670	  author    = {Lalor, John P. and Yang, Yi and Smith, Noah A.},
671	  title     = {Benchmarking Large Language Models with Item Response Theory},
672	  booktitle = {Proceedings of the 38th AAAI Conference on Artificial Intelligence},
673	  year      = {2024}
674	}
675	
676	% --- Score Adjustment & Decontamination ---
677	
678	@inproceedings{li2025dcr,
679	  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},
680	  title     = {{DCR}: Decontaminated Calibration and Ranking for Benchmark Evaluation},
681	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
682	  year      = {2025}
683	}
684	
685	@inproceedings{yang2024inference,
686	  author    = {Yang, Shuo and Wei, Xin and Shi, Weicheng},
687	  title     = {Inference-Time Decontamination of Large Language Models for Benchmark Evaluation},
688	  booktitle = {Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP Findings)},
689	  year      = {2024}
690	}
691	
692	@article{rao2026silicon,
693	  author        = {Rao, Sumedh and Raji, Inioluwa Deborah and Liang, Percy},
694	  title         = {The Silicon Bureaucracy: Evaluating the Evaluators in {LLM} Benchmarking},
695	  journal       = {arXiv preprint},
696	  year          = {2026},
697	  eprint        = {2603.21636},
698	  archiveprefix = {arXiv}
699	}
700	
701	% --- Benchmarking ---
702	
703	@inproceedings{hendrycks2021mmlu,
704	  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
705	  title     = {Measuring Massive Multitask Language Understanding},
706	  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},
707	  year      = {2021}
708	}
709	
710	@article{cobbe2021gsm8k,
711	  author        = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
712	  title         = {Training Verifiers to Solve Math Word Problems},
713	  journal       = {arXiv preprint},
714	  year          = {2021},
715	  eprint        = {2110.14168},
716	  archiveprefix = {arXiv}
717	}
718	
719	@inproceedings{clark2018arc,
720	  author    = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
721	  title     = {Think you have Solved Question Answering? {Try ARC}, the {AI2} Reasoning Challenge},
722	  journal   = {arXiv preprint},
723	  year      = {2018},
724	  eprint    = {1803.05457},
725	  archiveprefix = {arXiv}
726	}
727	
728	@article{chen2021humaneval,
729	  author        = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and Ray, Alex and Puri, Raul and Krueger, Gretchen and Petrov, Michael and Khlaaf, Heidy and Sastry, Girish and Mishkin, Pamela and Chan, Brooke and Gray, Scott and Ryder, Nick and Pavlov, Mikhail and Power, Alethea and Kaiser, Lukasz and Bavarian, Mohammad and Winter, Clemens and Tillet, Philippe and Such, Felipe Petroski and Cummings, Dave and Plappert, Matthias and Chanez, Fotios and Barnes, Elizabeth and Herbert-Voss, Ariel and Guss, William Hebgen and Nichol, Alex and Paino, Alex and Tezak, Nikolas and Tang, Jie and Babuschkin, Igor and Balaji, Suchir and Jain, Shantanu and Saunders, William and Hesse, Christopher and Carr, Andrew N. and Leike, Jan and Achiam, Josh and Misra, Vedant and Morikawa, Evan and Radford, Alec and Knight, Matthew and Brundage, Miles and Murati, Mira and Mayer, Katie and Welinder, Peter and McGrew, Bob and Amodei, Dario and McCandlish, Sam and Sutskever, Ilya and Zaremba, Wojciech},
730	  title         = {Evaluating Large Language Models Trained on Code},
731	  journal       = {arXiv preprint},
732	  year          = {2021},
733	  eprint        = {2107.03374},
734	  archiveprefix = {arXiv}
735	}
736	
737	@inproceedings{chang2025benchmarking,
738	  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},
739	  title     = {A Survey on Evaluation of Large Language Models},
740	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
741	  year      = {2025}
742	}
743	
744	@article{white2024livebench,
745	  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},
746	  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},
747	  journal       = {arXiv preprint},
748	  year          = {2024},
749	  eprint        = {2406.19314},
750	  archiveprefix = {arXiv}
751	}
752	
753	@inproceedings{polo2024tinybenchmarks,
754	  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},
755	  title     = {{TinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},
756	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
757	  year      = {2024}
758	}
759	
760	@inproceedings{han2026probing,
761	  author    = {Han, Yucheng and Wu, Chongxuan and Qi, Jiashi and Zhou, Jie},
762	  title     = {Targeted Probing for Contamination Effects in Large Language Model Evaluations},
763	  booktitle = {Findings of the 2026 Conference of the European Chapter of the Association for Computational Linguistics (EACL Findings)},
764	  year      = {2026},
765	  note      = {arXiv:2510.07175}
766	}
767	
768	% --- Differential Item Functioning (DIF) ---
769	
770	@book{holland1993dif,
771	  author    = {Holland, Paul W. and Wainer, Howard},
772	  title     = {Differential Item Functioning},
773	  publisher = {Lawrence Erlbaum Associates},
774	  year      = {1993},
775	  address   = {Hillsdale, NJ}
776	}
777	
778	@incollection{thissen1993dif,
779	  author    = {Thissen, David and Steinberg, Lynne and Wainer, Howard},
780	  title     = {Detection of Differential Item Functioning Using the Parameters of Item Response Models},
781	  booktitle = {Differential Item Functioning},
782	  editor    = {Holland, Paul W. and Wainer, Howard},
783	  publisher = {Lawrence Erlbaum Associates},
784	  pages     = {67--113},
785	  year      = {1993}
786	}
787	
788	@book{zumbo1999dif,
789	  author    = {Zumbo, Bruno D.},
790	  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},
791	  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defence},
792	  year      = {1999},
793	  address   = {Ottawa, ON}
794	}
795	
796	% --- ML Calibration ---
797	
798	@inproceedings{guo2017calibration,
799	  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
800	  title     = {On Calibration of Modern Neural Networks},
801	  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},
802	  pages     = {1321--1330},
803	  year      = {2017}
804	}
805	
806	% --- Conformal Prediction ---
807	
808	@article{angelopoulos2023conformal,
809	  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},
810	  title         = {Conformal Prediction: A Gentle Introduction},
811	  journal       = {Foundations and Trends in Machine Learning},
812	  volume        = {16},
813	  number        = {4},
814	  pages         = {494--591},
815	  year          = {2023}
816	}
817	
818	% --- Data Attribution ---
819	
820	@inproceedings{pruthi2020tracin,
821	  author    = {Pruthi, Garima and Liu, Frederick and Kale, Satyen and Sundararajan, Mukund},
822	  title     = {Estimating Training Data Influence by Tracing Gradient Descent},
823	  booktitle = {Advances in Neural Information Processing Systems 33 (NeurIPS)},
824	  year      = {2020}
825	}
826	
827	@inproceedings{park2023trak,
828	  author    = {Park, Sung Min and Georgiev, Kristian and Ilyas, Andrew and Lecun, Guillaume and Madry, Aleksander},
829	  title     = {{TRAK}: Attributing Model Behavior at Scale},
830	  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},
831	  year      = {2023}
832	}
833	
834	% --- Multidimensional IRT ---
835	
836	@book{reckase2009mirt,
837	  author    = {Reckase, Mark D.},
838	  title     = {Multidimensional Item Response Theory},
839	  publisher = {Springer},
840	  year      = {2009},
841	  address   = {New York}
842	}
843	
844	% --- Exposure-Ability Collinearity & IRT Identifiability ---
845	
846	@article{sanmartin2015,
847	  author  = {San Mart\'{i}n, Ernesto and Gonz\'{a}lez, Jorge and Tuerlinckx, Francis},
848	  title   = {On the Unidentifiability of the Fixed-Effects {3PL} Model},
849	  journal = {Psychometrika},
850	  volume  = {80},
851	  number  = {2},
852	  pages   = {450--467},
853	  year    = {2015},
854	  doi     = {10.1007/s11336-014-9404-2}
855	}
856	
857	@article{mislevy1987,
858	  author  = {Mislevy, Robert J.},
859	  title   = {Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters},
860	  journal = {Applied Psychological Measurement},
861	  volume  = {11},
862	  number  = {1},
863	  pages   = {81--91},
864	  year    = {1987},
865	  doi     = {10.1177/014662168701100106}
866	}
867	
868	@book{wainer2007testlet,
869	  author    = {Wainer, Howard and Bradlow, Eric T. and Wang, Xiaohui},
870	  title     = {Testlet Response Theory and Its Applications},
871	  publisher = {Cambridge University Press},
872	  year      = {2007}
873	}
874	
875	% --- Measurement Error & Attenuation Bias ---
876	
877	@book{carroll2006,
878	  author    = {Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},
879	  title     = {Measurement Error in Nonlinear Models: A Modern Perspective},
880	  edition   = {2nd},
881	  publisher = {Chapman \& Hall/CRC},
882	  year      = {2006},
883	  isbn      = {9781584886334}
884	}
885	
886	@book{fuller1987,
887	  author    = {Fuller, Wayne A.},
888	  title     = {Measurement Error Models},
889	  publisher = {Wiley},
890	  year      = {1987},
891	  series    = {Wiley Series in Probability and Statistics},
892	  isbn      = {9780471861874}
893	}
894	
895	@article{stefanski1985,
896	  author  = {Stefanski, Leonard A. and Carroll, Raymond J.},
897	  title   = {Covariate Measurement Error in Logistic Regression},
898	  journal = {Annals of Statistics},
899	  volume  = {13},
900	  number  = {4},
901	  pages   = {1335--1351},
902	  year    = {1985},
903	  doi     = {10.1214/aos/1176349741}
904	}
905	
906	@article{battauz2011,
907	  author  = {Battauz, Michela and Bellio, Ruggero},
908	  title   = {Structural Modeling of Measurement Error in Generalized Linear Models with {Rasch} Measures as Covariates},
909	  journal = {Psychometrika},
910	  volume  = {76},
911	  number  = {1},
912	  pages   = {40--56},
913	  year    = {2011},
914	  doi     = {10.1007/s11336-010-9195-z}
915	}
916	
917	@article{westfall2016,
918	  author  = {Westfall, Jacob and Yarkoni, Tal},
919	  title   = {Statistically Controlling for Confounding Constructs Is Harder than You Think},
920	  journal = {PLoS ONE},
921	  volume  = {11},
922	  number  = {3},
923	  pages   = {e0152719},
924	  year    = {2016},
925	  doi     = {10.1371/journal.pone.0152719}
926	}
927	
928	@article{jerzak2026,
929	  author  = {Jerzak, Connor T. and Jessee, Stephen A.},
930	  title   = {Attenuation Bias with Latent Predictors},
931	  journal = {arXiv preprint arXiv:2507.22218},
932	  year    = {2026}
933	}
934	
935	% --- IRT Information & Power Analysis ---
936	
937	@book{embretson2000,
938	  author    = {Embretson, Susan E. and Reise, Steven P.},
939	  title     = {Item Response Theory for Psychologists},
940	  publisher = {Lawrence Erlbaum Associates},
941	  year      = {2000},
942	  address   = {Mahwah, NJ}
943	}
944	
945	@book{thissen2001,
946	  author    = {Thissen, David and Wainer, Howard},
947	  title     = {Test Scoring},
948	  publisher = {Lawrence Erlbaum Associates},
949	  year      = {2001},
950	  address   = {Mahwah, NJ}
951	}
952	
953	% --- 4PL Model & Identifiability ---
954	
955	@article{barton1981,
956	  author  = {Barton, Mark A. and Lord, Frederic M.},
957	  title   = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},
958	  journal = {ETS Research Report Series},
959	  volume  = {1981},
960	  number  = {1},
961	  pages   = {i--8},
962	  year    = {1981},
963	  doi     = {10.1002/j.2333-8504.1981.tb01255.x}
964	}
965	
966	@article{culpepper2016,
967	  author  = {Culpepper, Steven Andrew},
968	  title   = {Revisiting the 4-Parameter Item Response Model: {B}ayesian Estimation and Application},
969	  journal = {Psychometrika},
970	  volume  = {81},
971	  number  = {4},
972	  pages   = {1142--1163},
973	  year    = {2016},
974	  doi     = {10.1007/s11336-015-9477-6}
975	}
976	
977	@article{liao2012,
978	  author  = {Liao, Wen-Wei and Ho, Rong-Guey and Yen, Yung-Chin and Cheng, Hao-Chang},
979	  title   = {The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses},
980	  journal = {Social Behavior and Personality},
981	  volume  = {40},
982	  number  = {10},
983	  pages   = {1679--1694},
984	  year    = {2012},
985	  doi     = {10.2224/sbp.2012.40.10.1679}
986	}
987	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d916430c-b9c2-4b14-8128-83701a2f0025",
  "isSidechain": false,
  "promptId": "a6e775ec-3f10-4982-9c94-8b07992debf7",
  "type": "user",
  "uuid": "ba185dd1-0b7f-41a1-9213-3eafa42e40d4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib",
      "content": "% ============================================================\n% Literature Map Entries (keys from literature_map.yaml ids)\n% ============================================================\n\n@inproceedings{adams_1997_mrcml,\n  author    = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},\n  title     = {The Multidimensional Random Coefficients Multinomial Logit Model},\n  booktitle = {Applied Psychological Measurement},\n  volume    = {21},\n  number    = {1},\n  pages     = {1--23},\n  year      = {1997}\n}\n\n@article{angelopoulos_2023_conformal,\n  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  title         = {A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},\n  journal       = {Foundations and Trends in Machine Learning},\n  year          = {2023},\n  url           = {https://arxiv.org/abs/2107.07511}\n}\n\n@article{brown_2024_ppp,\n  author  = {Brown, Jeremy M. and Thomson, Robert C.},\n  title   = {The Expected Behaviors of Posterior Predictive Tests and Their Unexpected Interpretation},\n  journal = {Molecular Biology and Evolution},\n  volume  = {41},\n  number  = {3},\n  pages   = {msae051},\n  year    = {2024}\n}\n\n@article{burnell_2023_structure,\n  author        = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Murfet, Daniel and Zheng, Hananel and Hern\\'{a}ndez-Orallo, Jos\\'{e}},\n  title         = {Revealing the Structure of Language Model Capabilities},\n  journal       = {arXiv preprint},\n  year          = {2023},\n  eprint        = {2306.10062},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2306.10062}\n}\n\n@inproceedings{carlini_2021_extracting,\n  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and Lee, Katherine and Roberts, Adam and Brown, Tom and Song, Dawn and Erlingsson, Ulfar and Oprea, Alina and Raffel, Colin},\n  title     = {Extracting Training Data from Large Language Models},\n  booktitle = {Proceedings of the 30th USENIX Security Symposium},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2012.07805}\n}\n\n@inproceedings{chiang_2024_chatbot_arena,\n  author    = {Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios N. and Li, Tianle and Li, Dacheng and Zhang, Hao and Zhu, Banghua and Jordan, Michael and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {Chatbot Arena: An Open Platform for Evaluating {LLMs} by Human Preference},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.04132}\n}\n\n@inproceedings{choi_2025_kds,\n  author    = {Choi, Yujin and Kim, Heeyoung and Lee, Jihoon and Park, Changho},\n  title     = {How Contaminated Is Your Benchmark? Quantifying Dataset Leakage in Large Language Models with Kernel Divergence},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.00678}\n}\n\n@inproceedings{cormack_2009_rrf,\n  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},\n  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},\n  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages     = {758--759},\n  year      = {2009},\n  publisher = {ACM},\n  url       = {https://dl.acm.org/doi/10.1145/1571941.1572114}\n}\n\n@book{deboeck_2004_explanatory_irt,\n  author    = {De Boeck, Paul and Wilson, Mark},\n  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},\n  publisher = {Springer},\n  year      = {2004},\n  address   = {New York},\n  url       = {https://link.springer.com/book/10.1007/978-1-4757-3990-9}\n}\n\n@article{dekoninck_2024_constat,\n  author        = {Dekoninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},\n  title         = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2405.16281},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2405.16281}\n}\n\n@inproceedings{deng_2024_tsguessing,\n  author    = {Deng, Chunyuan and Zhao, Yilun and Tang, Xiangru and Gerstein, Mark and Cohan, Arman},\n  title     = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2311.09783}\n}\n\n@inproceedings{dong_2024_cdd,\n  author    = {Dong, Yihong and Jiang, Xue and Liu, Huanyu and Jin, Zhi and Li, Ge},\n  title     = {Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.15938}\n}\n\n@incollection{eckerly_2017_item_compromise,\n  author    = {Eckerly, Carol},\n  title     = {Detecting Preknowledge and Item Compromise: Understanding the Status Quo},\n  booktitle = {Handbook of Quantitative Methods for Detecting Cheating on Tests},\n  publisher = {Routledge},\n  year      = {2017},\n  url       = {https://www.routledge.com/9781138821811}\n}\n\n@article{ercikan_2008_dif_cancellation,\n  author  = {Ercikan, Kadriye and Arim, Rodrigo G. and Oliveri, Maria Elena},\n  title   = {Differential Item Functioning Amplification and Cancellation in a Reading Test},\n  journal = {Practical Assessment, Research, and Evaluation},\n  volume  = {14},\n  number  = {3},\n  year    = {2008}\n}\n\n@inproceedings{golchin_2024_time_travel,\n  author    = {Golchin, Shahriar and Surdeanu, Mihai},\n  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2308.08493}\n}\n\n@inproceedings{guo_2017_calibration,\n  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  title     = {On Calibration of Modern Neural Networks},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},\n  pages     = {1321--1330},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{habba_2025_growing_pains,\n  author        = {Habba, Maryam and Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2604.12843}\n}\n\n@book{holland_1993_dif,\n  author    = {Holland, Paul W. and Wainer, Howard},\n  title     = {Differential Item Functioning},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1993},\n  address   = {Hillsdale, NJ}\n}\n\n@article{kievit_2013_simpsons_paradox,\n  author  = {Kievit, Rogier A. and Frankenhuis, Willem E. and Waldorp, Lourens J. and Borsboom, Denny},\n  title   = {Simpson's Paradox in Psychological Science: A Practical Guide},\n  journal = {Frontiers in Psychology},\n  volume  = {4},\n  pages   = {513},\n  year    = {2013}\n}\n\n@inproceedings{lalor_2024_irt_nlp,\n  author    = {Lalor, John P. and Yang, Yi and Rodriguez, Pedro and Smith, Noah A.},\n  title     = {Item Response Theory for Natural Language Processing},\n  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: Tutorial Abstracts (EACL)},\n  year      = {2024},\n  url       = {https://aclanthology.org/2024.eacl-tutorials.2/}\n}\n\n@article{li_2024_atlas,\n  author        = {Li, Guanzhong and Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2511.04689},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2511.04689}\n}\n\n@article{li_2024_open_llm_leaderboard,\n  author        = {Li, Aidar Myrzakhan and Shen, Sondos Mahmoud Bsharat and Jia, Zhiqiang},\n  title         = {Open-{LLM}-Leaderboard: From Multi-choice to Open-style Questions for {LLMs} Evaluation, Benchmark, and Arena},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.07545},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2406.07545}\n}\n\n@inproceedings{li_2025_dcr,\n  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},\n  title     = {Decontaminated Calibration and Ranking for Trustworthy {LLM} Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@article{liang_2023_helm,\n  author        = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya and Newman, Benjamin and Yuan, Binhang and Yan, Bobby and Zhang, Ce and Cosgrove, Christian and Manning, Christopher D. and R\\'{e}, Christopher and Acosta-Navas, Diana and Hudson, Drew A. and others},\n  title         = {Holistic Evaluation of Language Models},\n  journal       = {Transactions on Machine Learning Research},\n  year          = {2023},\n  url           = {https://arxiv.org/abs/2211.09110}\n}\n\n@article{luettgau_2025_hibayes,\n  author        = {Luettgau, Lennart and Polo, Felipe Maia and Zhuang, Yuekai and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {{HiBayES}: A Hierarchical Bayesian Modeling Framework for {AI} Evaluation Statistics},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2505.05602},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2505.05602}\n}\n\n@article{mislevy_1986_bayes_irt,\n  author  = {Mislevy, Robert J.},\n  title   = {Bayes Modal Estimation in Item Response Models},\n  journal = {Psychometrika},\n  volume  = {51},\n  number  = {2},\n  pages   = {177--195},\n  year    = {1986}\n}\n\n@article{oren_2023_proving_contamination,\n  author        = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},\n  title         = {Proving Test Set Contamination in Black Box Language Models},\n  journal       = {arXiv preprint},\n  year          = {2023},\n  eprint        = {2310.17623},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2310.17623}\n}\n\n@inproceedings{polo_2024_tinybenchmarks,\n  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},\n  title     = {{tinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.14992}\n}\n\n@book{reckase_2009_mirt,\n  author    = {Reckase, Mark D.},\n  title     = {Multidimensional Item Response Theory},\n  publisher = {Springer},\n  year      = {2009},\n  address   = {New York}\n}\n\n@article{sanmartin_2009_irt,\n  author  = {San Mart\\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},\n  title   = {Consequential Validity and Item Response Theory},\n  journal = {Psychometrika},\n  volume  = {74},\n  number  = {2},\n  pages   = {349--367},\n  year    = {2009}\n}\n\n@article{schaeffer_2026_generative_contamination,\n  author        = {Schaeffer, Rylan and Kazdan, Joshua and Abbasi, Ali and Liu, Hailey and others},\n  title         = {Quantifying the Effect of Test Set Contamination on Generative Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.04301},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2601.04301}\n}\n\n@inproceedings{shi_2023_minkprob,\n  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},\n  title     = {Detecting Pretraining Data from Large Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2310.16789}\n}\n\n@inproceedings{shokri_2017_mia,\n  author    = {Shokri, Reza and Stronati, Marco and Song, Congzheng and Shmatikov, Vitaly},\n  title     = {Membership Inference Attacks Against Machine Learning Models},\n  booktitle = {Proceedings of the 2017 IEEE Symposium on Security and Privacy (S\\&P)},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1610.05820}\n}\n\n@article{sinharay_2017_preknowledge,\n  author  = {Sinharay, Sandip},\n  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},\n  journal = {Journal of Educational and Behavioral Statistics},\n  volume  = {42},\n  number  = {1},\n  year    = {2017},\n  url     = {https://pubmed.ncbi.nlm.nih.gov/29881099/}\n}\n\n@article{sinharay_2025_irt_fit,\n  author  = {Sinharay, Sandip},\n  title   = {Assessment of Fit of Item Response Theory Models: A Critical Review of the Status Quo and Some Future Directions},\n  journal = {British Journal of Mathematical and Statistical Psychology},\n  volume  = {78},\n  pages   = {711--733},\n  year    = {2025}\n}\n\n@inproceedings{sun_2025_emperors_new_clothes,\n  author    = {Sun, Yifan and Li, Zhen and Zhang, Yingji and Chen, Fei},\n  title     = {The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for {LLM} Benchmark Data Contamination},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.16402}\n}\n\n@article{talts_2018_sbc,\n  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},\n  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},\n  journal       = {arXiv preprint},\n  year          = {2018},\n  eprint        = {1804.06788},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/1804.06788}\n}\n\n@article{wang_2024_mmlu_pro,\n  author        = {Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and Li, Tianle and Ku, Max and Wang, Kai and Zhuang, Alex and Fan, Rongqi and Huang, Xiang and Chen, Wenhu},\n  title         = {{MMLU-Pro}: A More Robust and Challenging Multi-Task Language Understanding Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.01574},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2406.01574}\n}\n\n@article{white_2024_livebench,\n  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},\n  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.19314},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2406.19314}\n}\n\n@article{wust_2025_selfcritique,\n  author        = {W\\\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},\n  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2510.09259}\n}\n\n@inproceedings{xu_2025_dcr,\n  author    = {Xu, Yiyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},\n  title     = {{DCR}: Quantifying Data Contamination in {LLMs} Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.11405}\n}\n\n@article{yang_2023_rethinking_benchmark,\n  author        = {Yang, Shuo and Wei, Xin and Shi, Weicheng and Xu, Feiyu},\n  title         = {Rethinking Benchmark and Contamination for Language Models with Rephrased Samples},\n  journal       = {arXiv preprint},\n  year          = {2023},\n  eprint        = {2311.04850},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2311.04850}\n}\n\n@inproceedings{zhang_2024_gsm1k,\n  author    = {Zhang, Hugh Mee and Da, Jeff and Lee, Nayeon and Zheng, Lianmin and Sheng, Ying and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},\n  booktitle = {arXiv preprint},\n  year      = {2024},\n  eprint    = {2405.00332},\n  url       = {https://arxiv.org/abs/2405.00332}\n}\n\n@inproceedings{zhang_2024_minkpp,\n  author    = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},\n  title     = {{Min-K\\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2404.02936}\n}\n\n@inproceedings{zheng_2023_chatbot_arena,\n  author    = {Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},\n  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{zhou_2025_psnirt,\n  author    = {Zhou, Guanyu and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},\n  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},\n  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2505.15055}\n}\n\n% ============================================================\n% Existing Entries (preserved for backward compatibility)\n% ============================================================\n\n% --- Core Methodology ---\n\n@book{lord1980,\n  author    = {Lord, Frederic M.},\n  title     = {Applications of Item Response Theory to Practical Testing Problems},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1980},\n  address   = {Hillsdale, NJ}\n}\n\n@article{eckerly2017,\n  author  = {Eckerly, Carol},\n  title   = {Detecting Item Compromise in the Context of Item Response Theory},\n  journal = {Applied Psychological Measurement},\n  volume  = {41},\n  number  = {2},\n  pages   = {87--101},\n  year    = {2017}\n}\n\n@article{sinharay2017,\n  author  = {Sinharay, Sandip},\n  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},\n  journal = {Journal of Educational and Behavioral Statistics},\n  volume  = {42},\n  number  = {1},\n  pages   = {46--68},\n  year    = {2017}\n}\n\n@book{deboeck2004,\n  author    = {De Boeck, Paul and Wilson, Mark},\n  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},\n  publisher = {Springer},\n  year      = {2004},\n  address   = {New York}\n}\n\n@article{adams1997,\n  author  = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},\n  title   = {The Multidimensional Random Coefficients Multinomial Logit Model},\n  journal = {Applied Psychological Measurement},\n  volume  = {21},\n  number  = {1},\n  pages   = {1--23},\n  year    = {1997}\n}\n\n@article{mislevy1986,\n  author  = {Mislevy, Robert J.},\n  title   = {Bayes Modal Estimation in Item Response Models},\n  journal = {Psychometrika},\n  volume  = {51},\n  number  = {2},\n  pages   = {177--195},\n  year    = {1986}\n}\n\n@article{sanmartin2009,\n  author  = {San Mart\\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},\n  title   = {Consequential Validity of Item Response Theory Models for Measuring Latent Constructs},\n  journal = {Psychometrika},\n  volume  = {74},\n  number  = {2},\n  pages   = {349--367},\n  year    = {2009}\n}\n\n@article{maris2009,\n  author  = {Maris, Gunter and Bechger, Timo},\n  title   = {On Interpreting the Model Parameters for the Three Parameter Logistic Model},\n  journal = {Measurement},\n  volume  = {7},\n  number  = {2},\n  pages   = {75--88},\n  year    = {2009}\n}\n\n@inproceedings{cormack2009,\n  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},\n  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},\n  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages     = {758--759},\n  year      = {2009},\n  publisher = {ACM}\n}\n\n% --- Bayesian Inference & Diagnostics ---\n\n@article{hoffman2014,\n  author  = {Hoffman, Matthew D. and Gelman, Andrew},\n  title   = {The {No-U-Turn} Sampler: Adaptively Setting Path Lengths in {Hamiltonian Monte Carlo}},\n  journal = {Journal of Machine Learning Research},\n  volume  = {15},\n  number  = {47},\n  pages   = {1593--1623},\n  year    = {2014}\n}\n\n@article{carpenter2017,\n  author  = {Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Goodrich, Ben and Betancourt, Michael and Brubaker, Marcus and Guo, Jiqiang and Li, Peter and Riddell, Allen},\n  title   = {Stan: A Probabilistic Programming Language},\n  journal = {Journal of Statistical Software},\n  volume  = {76},\n  number  = {1},\n  pages   = {1--32},\n  year    = {2017}\n}\n\n@article{talts2018sbc,\n  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},\n  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},\n  journal       = {arXiv preprint},\n  year          = {2018},\n  eprint        = {1804.06788},\n  archiveprefix = {arXiv}\n}\n\n@article{ulitzsch2022,\n  author  = {Ulitzsch, Esther and Nestler, Steffen},\n  title   = {Automatic Differentiation Variational Inference for Item Response Theory Models},\n  journal = {British Journal of Mathematical and Statistical Psychology},\n  volume  = {75},\n  number  = {3},\n  pages   = {421--447},\n  year    = {2022}\n}\n\n% --- Contamination Detection Methods ---\n\n@inproceedings{duan2025minkpp,\n  author    = {Duan, Jiawen and Xie, Cheng and Zhang, Jian and Li, Kai},\n  title     = {{Min-K\\%++}: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},\n  year      = {2025}\n}\n\n@inproceedings{dekoninck2024constat,\n  author    = {De Koninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},\n  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year      = {2024}\n}\n\n@article{wust2025selfcritique,\n  author        = {W\\\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},\n  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{xu2025kds,\n  author    = {Xu, Yanyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},\n  title     = {Knowledge Distillation Signatures for Efficient Contamination Detection},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  note      = {arXiv:2502.00678}\n}\n\n@inproceedings{oren2024proving,\n  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},\n  title     = {Proving Test Set Contamination in Black Box Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024}\n}\n\n% --- Contamination Analysis & Mitigation ---\n\n@inproceedings{xu2025emperor,\n  author    = {Xu, Yiwen and Song, Kaijie and Zhou, Jianfeng and Chen, Liang},\n  title     = {The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  note      = {arXiv:2503.16402}\n}\n\n@article{dong2026dose,\n  author        = {Dong, Yifan and Li, Xinran and Chen, Difan and Wang, Zhengyu},\n  title         = {Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.04301},\n  archiveprefix = {arXiv}\n}\n\n@article{yang2026rl,\n  author        = {Yang, Shuo and Wei, Xin and Zhang, Zhiwei and Xu, Feiyu},\n  title         = {Reinforcement Learning Amplifies Contamination in {LLM} Benchmark Evaluation},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.06103},\n  archiveprefix = {arXiv}\n}\n\n@article{wang2025fragility,\n  author        = {Wang, Yuxin and Zhao, Yucheng and Li, Cheng and Zhang, Meng},\n  title         = {On the Fragility of Benchmark Evaluations for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.02386},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{zhang2025forget,\n  author    = {Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi},\n  title     = {How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025}\n}\n\n% --- IRT for LLM Evaluation ---\n\n@inproceedings{gu2026psnirt,\n  author    = {Gu, Jiaqi and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},\n  title     = {{PSN-IRT}: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory},\n  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},\n  year      = {2026}\n}\n\n@article{polo2026growing,\n  author        = {Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {Growing Pains: Understanding the Limitations and Potential of {IRT} for {LLM} Evaluation at Scale},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv}\n}\n\n@article{lyu2025atlas,\n  author        = {Lyu, Haoran and Ding, Yufei and Wang, Hainiu and Peng, Nanyun},\n  title         = {{ATLAS}: Adaptive Testing via Latent Ability Scoring for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2511.04689},\n  archiveprefix = {arXiv}\n}\n\n@article{zhuang2025hibayes,\n  author        = {Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {{HiBayES}: Hierarchical {Bayesian} Evaluation System for Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2505.05602},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{lalor2024irt,\n  author    = {Lalor, John P. and Yang, Yi and Smith, Noah A.},\n  title     = {Benchmarking Large Language Models with Item Response Theory},\n  booktitle = {Proceedings of the 38th AAAI Conference on Artificial Intelligence},\n  year      = {2024}\n}\n\n% --- Score Adjustment & Decontamination ---\n\n@inproceedings{li2025dcr,\n  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},\n  title     = {{DCR}: Decontaminated Calibration and Ranking for Benchmark Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@inproceedings{yang2024inference,\n  author    = {Yang, Shuo and Wei, Xin and Shi, Weicheng},\n  title     = {Inference-Time Decontamination of Large Language Models for Benchmark Evaluation},\n  booktitle = {Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP Findings)},\n  year      = {2024}\n}\n\n@article{rao2026silicon,\n  author        = {Rao, Sumedh and Raji, Inioluwa Deborah and Liang, Percy},\n  title         = {The Silicon Bureaucracy: Evaluating the Evaluators in {LLM} Benchmarking},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2603.21636},\n  archiveprefix = {arXiv}\n}\n\n% --- Benchmarking ---\n\n@inproceedings{hendrycks2021mmlu,\n  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},\n  title     = {Measuring Massive Multitask Language Understanding},\n  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},\n  year      = {2021}\n}\n\n@article{cobbe2021gsm8k,\n  author        = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  title         = {Training Verifiers to Solve Math Word Problems},\n  journal       = {arXiv preprint},\n  year          = {2021},\n  eprint        = {2110.14168},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{clark2018arc,\n  author    = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},\n  title     = {Think you have Solved Question Answering? {Try ARC}, the {AI2} Reasoning Challenge},\n  journal   = {arXiv preprint},\n  year      = {2018},\n  eprint    = {1803.05457},\n  archiveprefix = {arXiv}\n}\n\n@article{chen2021humaneval,\n  author        = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and Ray, Alex and Puri, Raul and Krueger, Gretchen and Petrov, Michael and Khlaaf, Heidy and Sastry, Girish and Mishkin, Pamela and Chan, Brooke and Gray, Scott and Ryder, Nick and Pavlov, Mikhail and Power, Alethea and Kaiser, Lukasz and Bavarian, Mohammad and Winter, Clemens and Tillet, Philippe and Such, Felipe Petroski and Cummings, Dave and Plappert, Matthias and Chanez, Fotios and Barnes, Elizabeth and Herbert-Voss, Ariel and Guss, William Hebgen and Nichol, Alex and Paino, Alex and Tezak, Nikolas and Tang, Jie and Babuschkin, Igor and Balaji, Suchir and Jain, Shantanu and Saunders, William and Hesse, Christopher and Carr, Andrew N. and Leike, Jan and Achiam, Josh and Misra, Vedant and Morikawa, Evan and Radford, Alec and Knight, Matthew and Brundage, Miles and Murati, Mira and Mayer, Katie and Welinder, Peter and McGrew, Bob and Amodei, Dario and McCandlish, Sam and Sutskever, Ilya and Zaremba, Wojciech},\n  title         = {Evaluating Large Language Models Trained on Code},\n  journal       = {arXiv preprint},\n  year          = {2021},\n  eprint        = {2107.03374},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{chang2025benchmarking,\n  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},\n  title     = {A Survey on Evaluation of Large Language Models},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@article{white2024livebench,\n  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},\n  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.19314},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{polo2024tinybenchmarks,\n  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},\n  title     = {{TinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024}\n}\n\n@inproceedings{han2026probing,\n  author    = {Han, Yucheng and Wu, Chongxuan and Qi, Jiashi and Zhou, Jie},\n  title     = {Targeted Probing for Contamination Effects in Large Language Model Evaluations},\n  booktitle = {Findings of the 2026 Conference of the European Chapter of the Association for Computational Linguistics (EACL Findings)},\n  year      = {2026},\n  note      = {arXiv:2510.07175}\n}\n\n% --- Differential Item Functioning (DIF) ---\n\n@book{holland1993dif,\n  author    = {Holland, Paul W. and Wainer, Howard},\n  title     = {Differential Item Functioning},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1993},\n  address   = {Hillsdale, NJ}\n}\n\n@incollection{thissen1993dif,\n  author    = {Thissen, David and Steinberg, Lynne and Wainer, Howard},\n  title     = {Detection of Differential Item Functioning Using the Parameters of Item Response Models},\n  booktitle = {Differential Item Functioning},\n  editor    = {Holland, Paul W. and Wainer, Howard},\n  publisher = {Lawrence Erlbaum Associates},\n  pages     = {67--113},\n  year      = {1993}\n}\n\n@book{zumbo1999dif,\n  author    = {Zumbo, Bruno D.},\n  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},\n  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defence},\n  year      = {1999},\n  address   = {Ottawa, ON}\n}\n\n% --- ML Calibration ---\n\n@inproceedings{guo2017calibration,\n  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  title     = {On Calibration of Modern Neural Networks},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},\n  pages     = {1321--1330},\n  year      = {2017}\n}\n\n% --- Conformal Prediction ---\n\n@article{angelopoulos2023conformal,\n  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  title         = {Conformal Prediction: A Gentle Introduction},\n  journal       = {Foundations and Trends in Machine Learning},\n  volume        = {16},\n  number        = {4},\n  pages         = {494--591},\n  year          = {2023}\n}\n\n% --- Data Attribution ---\n\n@inproceedings{pruthi2020tracin,\n  author    = {Pruthi, Garima and Liu, Frederick and Kale, Satyen and Sundararajan, Mukund},\n  title     = {Estimating Training Data Influence by Tracing Gradient Descent},\n  booktitle = {Advances in Neural Information Processing Systems 33 (NeurIPS)},\n  year      = {2020}\n}\n\n@inproceedings{park2023trak,\n  author    = {Park, Sung Min and Georgiev, Kristian and Ilyas, Andrew and Lecun, Guillaume and Madry, Aleksander},\n  title     = {{TRAK}: Attributing Model Behavior at Scale},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year      = {2023}\n}\n\n% --- Multidimensional IRT ---\n\n@book{reckase2009mirt,\n  author    = {Reckase, Mark D.},\n  title     = {Multidimensional Item Response Theory},\n  publisher = {Springer},\n  year      = {2009},\n  address   = {New York}\n}\n\n% --- Exposure-Ability Collinearity & IRT Identifiability ---\n\n@article{sanmartin2015,\n  author  = {San Mart\\'{i}n, Ernesto and Gonz\\'{a}lez, Jorge and Tuerlinckx, Francis},\n  title   = {On the Unidentifiability of the Fixed-Effects {3PL} Model},\n  journal = {Psychometrika},\n  volume  = {80},\n  number  = {2},\n  pages   = {450--467},\n  year    = {2015},\n  doi     = {10.1007/s11336-014-9404-2}\n}\n\n@article{mislevy1987,\n  author  = {Mislevy, Robert J.},\n  title   = {Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters},\n  journal = {Applied Psychological Measurement},\n  volume  = {11},\n  number  = {1},\n  pages   = {81--91},\n  year    = {1987},\n  doi     = {10.1177/014662168701100106}\n}\n\n@book{wainer2007testlet,\n  author    = {Wainer, Howard and Bradlow, Eric T. and Wang, Xiaohui},\n  title     = {Testlet Response Theory and Its Applications},\n  publisher = {Cambridge University Press},\n  year      = {2007}\n}\n\n% --- Measurement Error & Attenuation Bias ---\n\n@book{carroll2006,\n  author    = {Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},\n  title     = {Measurement Error in Nonlinear Models: A Modern Perspective},\n  edition   = {2nd},\n  publisher = {Chapman \\& Hall/CRC},\n  year      = {2006},\n  isbn      = {9781584886334}\n}\n\n@book{fuller1987,\n  author    = {Fuller, Wayne A.},\n  title     = {Measurement Error Models},\n  publisher = {Wiley},\n  year      = {1987},\n  series    = {Wiley Series in Probability and Statistics},\n  isbn      = {9780471861874}\n}\n\n@article{stefanski1985,\n  author  = {Stefanski, Leonard A. and Carroll, Raymond J.},\n  title   = {Covariate Measurement Error in Logistic Regression},\n  journal = {Annals of Statistics},\n  volume  = {13},\n  number  = {4},\n  pages   = {1335--1351},\n  year    = {1985},\n  doi     = {10.1214/aos/1176349741}\n}\n\n@article{battauz2011,\n  author  = {Battauz, Michela and Bellio, Ruggero},\n  title   = {Structural Modeling of Measurement Error in Generalized Linear Models with {Rasch} Measures as Covariates},\n  journal = {Psychometrika},\n  volume  = {76},\n  number  = {1},\n  pages   = {40--56},\n  year    = {2011},\n  doi     = {10.1007/s11336-010-9195-z}\n}\n\n@article{westfall2016,\n  author  = {Westfall, Jacob and Yarkoni, Tal},\n  title   = {Statistically Controlling for Confounding Constructs Is Harder than You Think},\n  journal = {PLoS ONE},\n  volume  = {11},\n  number  = {3},\n  pages   = {e0152719},\n  year    = {2016},\n  doi     = {10.1371/journal.pone.0152719}\n}\n\n@article{jerzak2026,\n  author  = {Jerzak, Connor T. and Jessee, Stephen A.},\n  title   = {Attenuation Bias with Latent Predictors},\n  journal = {arXiv preprint arXiv:2507.22218},\n  year    = {2026}\n}\n\n% --- IRT Information & Power Analysis ---\n\n@book{embretson2000,\n  author    = {Embretson, Susan E. and Reise, Steven P.},\n  title     = {Item Response Theory for Psychologists},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {2000},\n  address   = {Mahwah, NJ}\n}\n\n@book{thissen2001,\n  author    = {Thissen, David and Wainer, Howard},\n  title     = {Test Scoring},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {2001},\n  address   = {Mahwah, NJ}\n}\n\n% --- 4PL Model & Identifiability ---\n\n@article{barton1981,\n  author  = {Barton, Mark A. and Lord, Frederic M.},\n  title   = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},\n  journal = {ETS Research Report Series},\n  volume  = {1981},\n  number  = {1},\n  pages   = {i--8},\n  year    = {1981},\n  doi     = {10.1002/j.2333-8504.1981.tb01255.x}\n}\n\n@article{culpepper2016,\n  author  = {Culpepper, Steven Andrew},\n  title   = {Revisiting the 4-Parameter Item Response Model: {B}ayesian Estimation and Application},\n  journal = {Psychometrika},\n  volume  = {81},\n  number  = {4},\n  pages   = {1142--1163},\n  year    = {2016},\n  doi     = {10.1007/s11336-015-9477-6}\n}\n\n@article{liao2012,\n  author  = {Liao, Wen-Wei and Ho, Rong-Guey and Yen, Yung-Chin and Cheng, Hao-Chang},\n  title   = {The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses},\n  journal = {Social Behavior and Personality},\n  volume  = {40},\n  number  = {10},\n  pages   = {1679--1694},\n  year    = {2012},\n  doi     = {10.2224/sbp.2012.40.10.1679}\n}\n",
      "numLines": 987,
      "startLine": 1,
      "totalLines": 987
    }
  },
  "sourceToolAssistantUUID": "d916430c-b9c2-4b14-8128-83701a2f0025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "leafUuid": "ba185dd1-0b7f-41a1-9213-3eafa42e40d4",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Rewrite Method section with 2PL+γ primary model",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1"
}
```

---

### Assistant

_source line 20 · 2026-05-17T04:08:22.224Z_

Now let me read the writing norms skill file as required.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba185dd1-0b7f-41a1-9213-3eafa42e40d4",
  "isSidechain": false,
  "requestId": "req_011Cb7UzvtE2r1eWiPsoBb8H",
  "type": "assistant",
  "uuid": "9d61fec1-f6ae-4b38-8efa-e3e40dcc19b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfK5bUuHrFkMBK5PzJhtmR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24562,
      "cache_read_input_tokens": 26949,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24562,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 26949,
          "cache_creation_input_tokens": 24562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24562
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

_source line 21 · 2026-05-17T04:08:26.050Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PbdjRQ4CfrieQBJRGv7SKc`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d61fec1-f6ae-4b38-8efa-e3e40dcc19b3",
  "isSidechain": false,
  "requestId": "req_011Cb7UzvtE2r1eWiPsoBb8H",
  "type": "assistant",
  "uuid": "8423c8b3-99a4-41bc-8d9f-9fd27670b94c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfK5bUuHrFkMBK5PzJhtmR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24562,
      "cache_read_input_tokens": 26949,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24562,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 26949,
          "cache_creation_input_tokens": 24562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24562
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

_source line 22 · 2026-05-17T04:08:26.061Z_

<details><summary>↩ Tool result · `toolu_01PbdjRQ4CfrieQBJRGv7SKc`</summary>

````text
1	---
2	name: latex-paper
3	description: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。
4	scope: global
5	tags:
6	- latex
7	- paper-writing
8	- academic
9	- citation
10	- submission
11	version: 1
12	roles:
13	- agent
14	- worker
15	---
16	
17	# LaTeX 论文写作全流程
18	
19	ML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。
20	
21	---
22	
23	## 1. 工作模式
24	
25	开始前选择模式：
26	
27	| 模式 | 说明 | 适用 |
28	|------|------|------|
29	| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |
30	| **Improve** | 改写已有章节，强化论证 | 修改稿 |
31	| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |
32	
33	---
34	
35	## 2. Claim-Evidence 方法论
36	
37	**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**
38	
39	### 2.1 一句话贡献
40	
41	在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。
42	
43	### 2.2 Claim-Evidence Map
44	
45	为每个 contribution 建立 claim→evidence 映射表：
46	
47	| Contribution | Claim | Evidence | Table/Figure |
48	|-------------|-------|----------|-------------|
49	| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |
50	| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |
51	| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |
52	
53	**没有直接证据支撑的 claim 必须删除或降级为 discussion。**
54	
55	### 2.3 章节起草顺序
56	
57	```
58	1. Introduction + Experiments（先确定 claim 和 evidence）
59	2. Method（评估问题稳定后再写细节）
60	3. Related Work
61	4. Abstract + Title（核心 claim 定型后最后写）
62	```
63	
64	### 2.4 Quality Gates
65	
66	投稿前必须通过：
67	- [ ] 前两段出现显式 novelty 声明
68	- [ ] 每个 contribution 有可验证的 evidence
69	- [ ] Abstract / Intro / Conclusion 的 claim 一致
70	- [ ] Limitations 真实且技术性诚实
71	- [ ] 审稿人两分钟内能识别 delta
72	
73	---
74	
75	## 3. 引用防幻觉（CRITICAL）
76	
77	**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**
78	
79	### 3.1 黄金法则
80	
81	```
82	IF 无法程序化获取引用:
83	    → 标记 [CITATION NEEDED] 或 \cite{PLACEHOLDER_verify}
84	    → 明确告知用户
85	    → 绝不编造看似合理的引用
86	```
87	
88	### 3.2 五步验证流程
89	
90	```
91	1. SEARCH  → Semantic Scholar API 搜索关键词
92	2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）
93	3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）
94	4. CHECK   → 确认你引用的 claim 确实出自该论文
95	5. ADD     → 加入 .bib 文件
96	```
97	
98	### 3.3 API 速查
99	
100	| API | 用途 | 限制 |
101	|-----|------|------|
102	| **Semantic Scholar** | ML/AI 论文搜索 | 1 RPS (免费) |
103	| **CrossRef** | DOI → BibTeX | 需 mailto 头 |
104	| **arXiv** | 预印本搜索 | 3s 间隔 |
105	
106	```python
107	# DOI → BibTeX（最可靠的方式）
108	import requests
109	def doi_to_bibtex(doi: str) -> str:
110	    r = requests.get(f"https://doi.org/{doi}",
111	                     headers={"Accept": "application/x-bibtex"})
112	    r.raise_for_status()
113	    return r.text
114	
115	# Semantic Scholar 搜索
116	from semanticscholar import SemanticScholar
117	sch = SemanticScholar()
118	results = sch.search_paper("attention mechanism transformers", limit=5)
119	for p in results:
120	    print(f"{p.title} | DOI: {p.externalIds.get('DOI', 'N/A')}")
121	```
122	
123	### 3.4 引用处理规则
124	
125	| 情况 | 处理 |
126	|------|------|
127	| 找到论文 + DOI + BibTeX | 直接用 |
128	| 找到论文，无 DOI | 用 arXiv BibTeX |
129	| 论文存在但无法获取 BibTeX | 标记 placeholder，告知用户 |
130	| 不确定论文是否存在 | 标记 `[CITATION NEEDED]`，告知用户 |
131	| "我觉得有篇关于 X 的论文" | **绝不引用** — 先搜索或标记 |
132	
133	---
134	
135	## 4. 顶会模板速查
136	
137	### 4.1 ML/AI 会议
138	
139	| 会议 | 页数限制 | 主文件 | 样式文件 | 必须项 |
140	|------|---------|--------|---------|--------|
141	| **NeurIPS** | 9 页 | `main.tex` | `neurips.sty` | Paper Checklist |
142	| **ICML** | 8 页 (+1 camera-ready) | `example_paper.tex` | `icml2026.sty` | Broader Impact |
143	| **ICLR** | 9 页 (+1) | `iclr_conference.tex` | `iclr_conference.sty` | LLM 使用声明 |
144	| **ACL/EMNLP** | 8 页 (long) | `acl_latex.tex` | `acl.sty` | Limitations 必须 |
145	| **AAAI** | 7 页 (+1) | `aaai_template.tex` | `aaai.sty` | 严格样式 |
146	| **COLM** | 9 页 (+1) | `colm_conference.tex` | `colm_conference.sty` | 语言模型聚焦 |
147	
148	### 4.2 系统会议
149	
150	| 会议 | 页数限制 | 模板类型 | 关键要求 |
151	|------|---------|---------|---------|
152	| **OSDI** | 12 页 (+2) | USENIX `usenix.sty` | Research / Operational 双 track |
153	| **NSDI** | 12 页 | USENIX | Introduction 预筛 |
154	| **ASPLOS** | 12 页 | ACM `acmart.cls (sigplan)` | 前 2 页快速评审 |
155	| **SOSP** | 12 页 | ACM `acmart.cls (sigplan)` | 可选 Artifact Evaluation |
156	
157	### 4.3 模板使用原则
158	
159	```bash
160	# 1. 复制整个模板目录（不要只拷 .tex）
161	cp -r templates/neurips2025/ ~/papers/my-paper/
162	
163	# 2. 先编译未修改的模板，确认能跑通
164	latexmk -pdf main.tex
165	
166	# 3. 逐章替换内容，频繁编译
167	```
168	
169	**禁止事项：**
170	- 不要修改 `.sty` 文件
171	- 不要在会议模板间复制 `\usepackage` 行
172	- 不要只复制 `.tex` 而不带 `.sty/.bst`
173	
174	---
175	
176	## 5. 写作规范
177	
178	### 5.1 时间分配（Neel Nanda）
179	
180	花**大致相等**的时间在：
181	1. Abstract
182	2. Introduction
183	3. 图表
184	4. **其余所有内容加起来**
185	
186	审稿人读论文的顺序：标题 → 摘要 → 引言 → 图表 → 也许正文。
187	
188	### 5.2 Abstract 五句法（Sebastian Farquhar）
189	
190	```
191	1. 你做了什么（"We introduce/prove/demonstrate..."）
192	2. 为什么这很难且重要
193	3. 怎么做的（含专业关键词以便检索）
194	4. 有什么证据
195	5. 最惊人的数字/结果
196	```
197	
198	删除一切泛泛的开头：~~"Large language models have achieved remarkable success..."~~
199	
200	### 5.3 句子级清晰度（Gopen & Swan）
201	
202	| 原则 | 规则 |
203	|------|------|
204	| 主谓紧邻 | 不要在主语和动词之间插入长从句 |
205	| 重点在句尾 | 把关键数字/结论放在句末 |
206	| 旧信息在前 | 先放读者已知的内容，再引入新概念 |
207	| 动词表达动作 | "We analyzed" 而非 "We performed an analysis" |
208	
209	### 5.4 常见修改
210	
211	| 问题 | 修复 |
212	|------|------|
213	| Abstract 太泛 | 删第一句（如果它能放在任何 ML 论文前面） |
214	| Introduction 超 1.5 页 | 背景挪到 Related Work |
215	| 实验没有显式 claim | 每个实验前加 "This tests whether..." |
216	| 缺统计显著性 | 加 error bars + 运行次数 + 计算方法 |
217	
218	---
219	
220	## 6. 投稿工程链
221	
222	### 6.1 构建
223	
224	```bash
225	# 推荐：latexmk 一键构建
226	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
227	
228	# 手动：需要多次编译
229	pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
230	```
231	
232	### 6.2 Lint + 格式化
233	
234	```bash
235	# Lint: 检查常见 LaTeX 问题
236	chktex main.tex
237	
238	# 格式化: 减少 diff 噪声
239	latexindent -w main.tex
240	```
241	
242	### 6.3 图表格式
243	
244	| 类型 | 格式 | 说明 |
245	|------|------|------|
246	| 矢量图（plot、diagram） | PDF | matplotlib: `plt.savefig('fig.pdf')` |
247	| 照片/heatmap | PNG 600dpi 或 TIFF | 栅格图 |
248	| 表格 | `booktabs` 包 | `\toprule/\midrule/\bottomrule` |
249	
250	```latex
251	\usepackage{booktabs}
252	\begin{tabular}{lcc}
253	\toprule
254	Method & Accuracy $\uparrow$ & Latency $\downarrow$ \\
255	\midrule
256	Baseline & 85.2 & 45ms \\
257	\textbf{Ours} & \textbf{92.1} & 38ms \\
258	\bottomrule
259	\end{tabular}
260	```
261	
262	**图表规范：**
263	- 用色盲友好色板（Okabe-Ito 或 Paul Tol）
264	- 图内不放标题（用 caption）
265	- Caption 独立可理解（不依赖正文）
266	- 最佳值加粗，标注方向符号（↑ 越高越好，↓ 越低越好）
267	
268	### 6.4 投稿打包
269	
270	```bash
271	# 清理辅助文件
272	latexmk -c
273	
274	# 打包投稿
275	zip -r submission.zip main.tex *.sty *.bst *.bib figures/ --exclude='*.aux' --exclude='*.log'
276	```
277	
278	### 6.5 常见失败点
279	
280	| 问题 | 解决 |
281	|------|------|
282	| 图片格式混用导致编译失败 | 统一用 PDF |
283	| 字体未嵌入 | `pdffonts output.pdf` 检查 |
284	| Overfull box 过多 | 关键位置手动调行 |
285	| 引用缺字段 | 检查 DOI/年份/期刊名 |
286	| 超页数 | 用 `\vspace{-Xpt}` 微调，或精简内容 |
287	
288	---
289	
290	## 7. 会议转投
291	
292	当论文被拒或转投其他会议时：
293	
294	### 7.1 ML/AI 会议间转换
295	
296	| 转换 | 页数变化 | 关键调整 |
297	|------|---------|---------|
298	| NeurIPS → ICML | 9→8 | 删 1 页，加 Broader Impact |
299	| ICML → ICLR | 8→9 | 可扩展实验 + LLM 声明 |
300	| NeurIPS → ACL | 9→8 | 按 NLP 惯例重组 + Limitations |
301	| ICLR → AAAI | 9→7 | 大幅精简，严格样式 |
302	
303	### 7.2 转投原则
304	
305	1. **永远用目标模板重新开始** — 复制目标模板，迁移内容，不要合并 preamble
306	2. **只迁移正文内容** — 不复制 `\usepackage`、header/footer 命令
307	3. **根据审稿意见改进** — 但不要在新稿中提及旧投稿（双盲）
308	4. **检查目标会议特殊要求** — checklist、ethics statement、LLM 声明等
309	
310	---
311	
312	## 8. 投前清单
313	
314	### 通用清单
315	
316	- [ ] Abstract/Intro/Conclusion 的 claim 一致
317	- [ ] 每个 contribution 有对应 evidence
318	- [ ] 所有引用已程序化验证（无幻觉引用）
319	- [ ] Error bars + 运行次数 + 统计方法
320	- [ ] Limitations 章节存在且诚实
321	- [ ] 匿名化（双盲审稿）
322	- [ ] 符合页数限制
323	- [ ] 所有图表有自包含 caption
324	- [ ] `.bib` 中无缺失字段
325	- [ ] PDF 编译无 warning
326	
327	### 会议特定
328	
329	| 会议 | 额外要求 |
330	|------|---------|
331	| NeurIPS | 16 项 Paper Checklist（附录，不计页数） |
332	| ICML | Broader Impact Statement |
333	| ICLR | LLM 使用声明 |
334	| ACL/EMNLP | Limitations 章节（必须），Ethics Statement |
335	| AAAI | 严格样式文件合规 |
336	
337	---
338	
339	## 参考资源
340	
341	**写作方法论：**
342	- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) — What/Why/So What 框架
343	- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 五句法 Abstract
344	- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 读者预期 7 原则
345	- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词
346	- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度
347	
348	**API：**
349	- [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/) | [arXiv](https://info.arxiv.org/help/api/)
350	
351	**会议官方：**
352	- [NeurIPS](https://neurips.cc/) | [ICML](https://icml.cc/) | [ICLR](https://iclr.cc/) | [ACL](https://www.aclweb.org/) | [AAAI](https://aaai.org/) | [EMNLP](https://2025.emnlp.org/)
353	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "8423c8b3-99a4-41bc-8d9f-9fd27670b94c",
  "isSidechain": false,
  "promptId": "a6e775ec-3f10-4982-9c94-8b07992debf7",
  "type": "user",
  "uuid": "32a33829-0977-4cc2-ab04-24a82aa8bb75",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
      "content": "---\nname: latex-paper\ndescription: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。\nscope: global\ntags:\n- latex\n- paper-writing\n- academic\n- citation\n- submission\nversion: 1\nroles:\n- agent\n- worker\n---\n\n# LaTeX 论文写作全流程\n\nML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。\n\n---\n\n## 1. 工作模式\n\n开始前选择模式：\n\n| 模式 | 说明 | 适用 |\n|------|------|------|\n| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |\n| **Improve** | 改写已有章节，强化论证 | 修改稿 |\n| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |\n\n---\n\n## 2. Claim-Evidence 方法论\n\n**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**\n\n### 2.1 一句话贡献\n\n在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。\n\n### 2.2 Claim-Evidence Map\n\n为每个 contribution 建立 claim→evidence 映射表：\n\n| Contribution | Claim | Evidence | Table/Figure |\n|-------------|-------|----------|-------------|\n| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |\n| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |\n| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |\n\n**没有直接证据支撑的 claim 必须删除或降级为 discussion。**\n\n### 2.3 章节起草顺序\n\n```\n1. Introduction + Experiments（先确定 claim 和 evidence）\n2. Method（评估问题稳定后再写细节）\n3. Related Work\n4. Abstract + Title（核心 claim 定型后最后写）\n```\n\n### 2.4 Quality Gates\n\n投稿前必须通过：\n- [ ] 前两段出现显式 novelty 声明\n- [ ] 每个 contribution 有可验证的 evidence\n- [ ] Abstract / Intro / Conclusion 的 claim 一致\n- [ ] Limitations 真实且技术性诚实\n- [ ] 审稿人两分钟内能识别 delta\n\n---\n\n## 3. 引用防幻觉（CRITICAL）\n\n**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**\n\n### 3.1 黄金法则\n\n```\nIF 无法程序化获取引用:\n    → 标记 [CITATION NEEDED] 或 \\cite{PLACEHOLDER_verify}\n    → 明确告知用户\n    → 绝不编造看似合理的引用\n```\n\n### 3.2 五步验证流程\n\n```\n1. SEARCH  → Semantic Scholar API 搜索关键词\n2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）\n3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）\n4. CHECK   → 确认你引用的 claim 确实出自该论文\n5. ADD     → 加入 .bib 文件\n```\n\n### 3.3 API 速查\n\n| API | 用途 | 限制 |\n|-----|------|------|\n| **Semantic Scholar** | ML/AI 论文搜索 | 1 RPS (免费) |\n| **CrossRef** | DOI → BibTeX | 需 mailto 头 |\n| **arXiv** | 预印本搜索 | 3s 间隔 |\n\n```python\n# DOI → BibTeX（最可靠的方式）\nimport requests\ndef doi_to_bibtex(doi: str) -> str:\n    r = requests.get(f\"https://doi.org/{doi}\",\n                     headers={\"Accept\": \"application/x-bibtex\"})\n    r.raise_for_status()\n    return r.text\n\n# Semantic Scholar 搜索\nfrom semanticscholar import SemanticScholar\nsch = SemanticScholar()\nresults = sch.search_paper(\"attention mechanism transformers\", limit=5)\nfor p in results:\n    print(f\"{p.title} | DOI: {p.externalIds.get('DOI', 'N/A')}\")\n```\n\n### 3.4 引用处理规则\n\n| 情况 | 处理 |\n|------|------|\n| 找到论文 + DOI + BibTeX | 直接用 |\n| 找到论文，无 DOI | 用 arXiv BibTeX |\n| 论文存在但无法获取 BibTeX | 标记 placeholder，告知用户 |\n| 不确定论文是否存在 | 标记 `[CITATION NEEDED]`，告知用户 |\n| \"我觉得有篇关于 X 的论文\" | **绝不引用** — 先搜索或标记 |\n\n---\n\n## 4. 顶会模板速查\n\n### 4.1 ML/AI 会议\n\n| 会议 | 页数限制 | 主文件 | 样式文件 | 必须项 |\n|------|---------|--------|---------|--------|\n| **NeurIPS** | 9 页 | `main.tex` | `neurips.sty` | Paper Checklist |\n| **ICML** | 8 页 (+1 camera-ready) | `example_paper.tex` | `icml2026.sty` | Broader Impact |\n| **ICLR** | 9 页 (+1) | `iclr_conference.tex` | `iclr_conference.sty` | LLM 使用声明 |\n| **ACL/EMNLP** | 8 页 (long) | `acl_latex.tex` | `acl.sty` | Limitations 必须 |\n| **AAAI** | 7 页 (+1) | `aaai_template.tex` | `aaai.sty` | 严格样式 |\n| **COLM** | 9 页 (+1) | `colm_conference.tex` | `colm_conference.sty` | 语言模型聚焦 |\n\n### 4.2 系统会议\n\n| 会议 | 页数限制 | 模板类型 | 关键要求 |\n|------|---------|---------|---------|\n| **OSDI** | 12 页 (+2) | USENIX `usenix.sty` | Research / Operational 双 track |\n| **NSDI** | 12 页 | USENIX | Introduction 预筛 |\n| **ASPLOS** | 12 页 | ACM `acmart.cls (sigplan)` | 前 2 页快速评审 |\n| **SOSP** | 12 页 | ACM `acmart.cls (sigplan)` | 可选 Artifact Evaluation |\n\n### 4.3 模板使用原则\n\n```bash\n# 1. 复制整个模板目录（不要只拷 .tex）\ncp -r templates/neurips2025/ ~/papers/my-paper/\n\n# 2. 先编译未修改的模板，确认能跑通\nlatexmk -pdf main.tex\n\n# 3. 逐章替换内容，频繁编译\n```\n\n**禁止事项：**\n- 不要修改 `.sty` 文件\n- 不要在会议模板间复制 `\\usepackage` 行\n- 不要只复制 `.tex` 而不带 `.sty/.bst`\n\n---\n\n## 5. 写作规范\n\n### 5.1 时间分配（Neel Nanda）\n\n花**大致相等**的时间在：\n1. Abstract\n2. Introduction\n3. 图表\n4. **其余所有内容加起来**\n\n审稿人读论文的顺序：标题 → 摘要 → 引言 → 图表 → 也许正文。\n\n### 5.2 Abstract 五句法（Sebastian Farquhar）\n\n```\n1. 你做了什么（\"We introduce/prove/demonstrate...\"）\n2. 为什么这很难且重要\n3. 怎么做的（含专业关键词以便检索）\n4. 有什么证据\n5. 最惊人的数字/结果\n```\n\n删除一切泛泛的开头：~~\"Large language models have achieved remarkable success...\"~~\n\n### 5.3 句子级清晰度（Gopen & Swan）\n\n| 原则 | 规则 |\n|------|------|\n| 主谓紧邻 | 不要在主语和动词之间插入长从句 |\n| 重点在句尾 | 把关键数字/结论放在句末 |\n| 旧信息在前 | 先放读者已知的内容，再引入新概念 |\n| 动词表达动作 | \"We analyzed\" 而非 \"We performed an analysis\" |\n\n### 5.4 常见修改\n\n| 问题 | 修复 |\n|------|------|\n| Abstract 太泛 | 删第一句（如果它能放在任何 ML 论文前面） |\n| Introduction 超 1.5 页 | 背景挪到 Related Work |\n| 实验没有显式 claim | 每个实验前加 \"This tests whether...\" |\n| 缺统计显著性 | 加 error bars + 运行次数 + 计算方法 |\n\n---\n\n## 6. 投稿工程链\n\n### 6.1 构建\n\n```bash\n# 推荐：latexmk 一键构建\nlatexmk -pdf -interaction=nonstopmode -halt-on-error main.tex\n\n# 手动：需要多次编译\npdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex\n```\n\n### 6.2 Lint + 格式化\n\n```bash\n# Lint: 检查常见 LaTeX 问题\nchktex main.tex\n\n# 格式化: 减少 diff 噪声\nlatexindent -w main.tex\n```\n\n### 6.3 图表格式\n\n| 类型 | 格式 | 说明 |\n|------|------|------|\n| 矢量图（plot、diagram） | PDF | matplotlib: `plt.savefig('fig.pdf')` |\n| 照片/heatmap | PNG 600dpi 或 TIFF | 栅格图 |\n| 表格 | `booktabs` 包 | `\\toprule/\\midrule/\\bottomrule` |\n\n```latex\n\\usepackage{booktabs}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Accuracy $\\uparrow$ & Latency $\\downarrow$ \\\\\n\\midrule\nBaseline & 85.2 & 45ms \\\\\n\\textbf{Ours} & \\textbf{92.1} & 38ms \\\\\n\\bottomrule\n\\end{tabular}\n```\n\n**图表规范：**\n- 用色盲友好色板（Okabe-Ito 或 Paul Tol）\n- 图内不放标题（用 caption）\n- Caption 独立可理解（不依赖正文）\n- 最佳值加粗，标注方向符号（↑ 越高越好，↓ 越低越好）\n\n### 6.4 投稿打包\n\n```bash\n# 清理辅助文件\nlatexmk -c\n\n# 打包投稿\nzip -r submission.zip main.tex *.sty *.bst *.bib figures/ --exclude='*.aux' --exclude='*.log'\n```\n\n### 6.5 常见失败点\n\n| 问题 | 解决 |\n|------|------|\n| 图片格式混用导致编译失败 | 统一用 PDF |\n| 字体未嵌入 | `pdffonts output.pdf` 检查 |\n| Overfull box 过多 | 关键位置手动调行 |\n| 引用缺字段 | 检查 DOI/年份/期刊名 |\n| 超页数 | 用 `\\vspace{-Xpt}` 微调，或精简内容 |\n\n---\n\n## 7. 会议转投\n\n当论文被拒或转投其他会议时：\n\n### 7.1 ML/AI 会议间转换\n\n| 转换 | 页数变化 | 关键调整 |\n|------|---------|---------|\n| NeurIPS → ICML | 9→8 | 删 1 页，加 Broader Impact |\n| ICML → ICLR | 8→9 | 可扩展实验 + LLM 声明 |\n| NeurIPS → ACL | 9→8 | 按 NLP 惯例重组 + Limitations |\n| ICLR → AAAI | 9→7 | 大幅精简，严格样式 |\n\n### 7.2 转投原则\n\n1. **永远用目标模板重新开始** — 复制目标模板，迁移内容，不要合并 preamble\n2. **只迁移正文内容** — 不复制 `\\usepackage`、header/footer 命令\n3. **根据审稿意见改进** — 但不要在新稿中提及旧投稿（双盲）\n4. **检查目标会议特殊要求** — checklist、ethics statement、LLM 声明等\n\n---\n\n## 8. 投前清单\n\n### 通用清单\n\n- [ ] Abstract/Intro/Conclusion 的 claim 一致\n- [ ] 每个 contribution 有对应 evidence\n- [ ] 所有引用已程序化验证（无幻觉引用）\n- [ ] Error bars + 运行次数 + 统计方法\n- [ ] Limitations 章节存在且诚实\n- [ ] 匿名化（双盲审稿）\n- [ ] 符合页数限制\n- [ ] 所有图表有自包含 caption\n- [ ] `.bib` 中无缺失字段\n- [ ] PDF 编译无 warning\n\n### 会议特定\n\n| 会议 | 额外要求 |\n|------|---------|\n| NeurIPS | 16 项 Paper Checklist（附录，不计页数） |\n| ICML | Broader Impact Statement |\n| ICLR | LLM 使用声明 |\n| ACL/EMNLP | Limitations 章节（必须），Ethics Statement |\n| AAAI | 严格样式文件合规 |\n\n---\n\n## 参考资源\n\n**写作方法论：**\n- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) — What/Why/So What 框架\n- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 五句法 Abstract\n- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 读者预期 7 原则\n- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词\n- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度\n\n**API：**\n- [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/) | [arXiv](https://info.arxiv.org/help/api/)\n\n**会议官方：**\n- [NeurIPS](https://neurips.cc/) | [ICML](https://icml.cc/) | [ICLR](https://iclr.cc/) | [ACL](https://www.aclweb.org/) | [AAAI](https://aaai.org/) | [EMNLP](https://2025.emnlp.org/)\n",
      "numLines": 353,
      "startLine": 1,
      "totalLines": 353
    }
  },
  "sourceToolAssistantUUID": "8423c8b3-99a4-41bc-8d9f-9fd27670b94c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Assistant

_source line 23 · 2026-05-17T04:08:59.460Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me write the new method.tex based on the writing plan's outline. Key changes from the existing version:

1. **2PL+γ as PRIMARY**: Main equation uses 2PL, 4PL is the MC extension
2. **Per-domain γ_k**: MMLU etc. have domain structure, can fit per-domain γ
3. **Fisher Info streamlined**: Only key conclusions (AUC=0.55, N≥50, scaling law), full derivation in Appendix A
4. **§3.5 as independent section**: Clearly distinguish calibration value (θ) vs diagnostic value (γ), with concrete numbers


5. **1100-word budget** with strict style constraints: no em-dashes, no -ing phrase endings, no "Furthermore/Moreover/Additionally" chains, and avoiding "delve into/leverage/utilize"
6. **All quantitative claims need evidence sources**, and LaTeX equations must be numbered with proper citation keys from references.bib

Let me structure the sections as: Problem Formulation, Multi-Signal Exposure Mapping, Contamination-Augmented IRT, Fisher Information and Identifiability, then the calibration vs. diagnostic distinction section.

For the final section on calibration value decomposition, I need to explain how we separate the true ability signal from contamination effects. The key insight is that when a student's response reflects both their actual knowledge and external factors like guessing or item compromise, we can decompose the observed score into these components. I'll frame this around the IRT likelihood and how the contamination model allows us to estimate what the "clean" ability measure would be. This connects back to the identifiability constraints and uses the Fisher information framework to show when we can reliably separate these signals. I'm setting up the problem formally: responses come from a standard IRT model, but when benchmarks appear in training data, observed ability gets contaminated by memorization. I need to estimate clean ability and diagnose contamination effects per domain, so I'm adapting item compromise and explanatory IRT frameworks with three key modifications for LLMs—shifting from independent test-takers to a shared item pool, treating leakage as continuous rather than binary, and accounting for ability that varies across different training regimes.

Now I'm planning the section structure carefully to fit the word budget: problem formulation gets about 150 words, then multi-signal exposure mapping around 200, the contamination-augmented IRT section takes the bulk at 350 words since it's the core contribution, followed by Fisher information and identifiability at 200 words, and finally calibration value decomposition at 200 words to reach roughly 1100 total.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32a33829-0977-4cc2-ab04-24a82aa8bb75",
  "isSidechain": false,
  "requestId": "req_011Cb7V1Ux2yQtueXHe6u6qV",
  "type": "assistant",
  "uuid": "d747762b-802c-4d7c-9d35-d30eda00a13f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHzrqGkm1cjN9PtszcUm2J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5529,
      "cache_read_input_tokens": 51511,
      "output_tokens": 4054,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4054,
          "cache_read_input_tokens": 51511,
          "cache_creation_input_tokens": 5529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5529
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

_source line 24 · 2026-05-17T04:08:59.464Z_

Now I have all the context. Let me write the restructured Method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d747762b-802c-4d7c-9d35-d30eda00a13f",
  "isSidechain": false,
  "requestId": "req_011Cb7V1Ux2yQtueXHe6u6qV",
  "type": "assistant",
  "uuid": "543020ce-62fd-40e8-aa50-29e848c86358",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHzrqGkm1cjN9PtszcUm2J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5529,
      "cache_read_input_tokens": 51511,
      "output_tokens": 4054,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4054,
          "cache_read_input_tokens": 51511,
          "cache_creation_input_tokens": 5529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5529
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

_source line 25 · 2026-05-17T04:10:00.308Z_

<details open><summary>🔧 Tool call — Write · `toolu_012vNDGPzWW6aQrWZLowUZCg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\nContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nLet $y_{ijk} \\in \\{0,1\\}$ denote the binary response of model~$j$ ($j=1,\\ldots,J$) to item~$i$ ($i=1,\\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\\theta_j, \\boldsymbol{\\xi}_i)$ where $\\theta_j$ is latent ability and $\\boldsymbol{\\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\\hat{\\theta}_j$ confounds genuine capability with memorization.\n\nOur goal is twofold: (1)~estimate $\\theta_j^{\\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \\citep{eckerly2017,sinharay2017} and explanatory IRT \\citep{deboeck2004}, adapting these frameworks through three structural modifications for LLM evaluation.\n\n\\textit{Adaptation~1: Independent examinees $\\to$ shared item pool.} Classical IRT assumes independent test-takers. In LLM evaluation, a fixed item set is shared across all models, and responses within a single model may exhibit residual correlations beyond the scalar~$\\theta_j$ \\citep{sanmartin2009}. We mitigate this by fitting per-benchmark models.\n\n\\textit{Adaptation~2: Binary leakage $\\to$ continuous exposure.} Item compromise IRT uses binary indicators \\citep{sinharay2017}. LLM contamination is graded: a model may have encountered an item zero, once, or hundreds of times. We replace binary indicators with continuous exposure scores $e_{ij} \\in [0,1]$ derived from detection signals, following the explanatory IRT tradition \\citep{deboeck2004}.\n\n\\textit{Adaptation~3: Stable ability $\\to$ regime-conditional ability.} In educational testing, ability is approximately constant. For LLMs, the training regime (SFT vs.\\ RL) qualitatively changes both internal representations and signal reliability. We recover clean ability via counterfactual inference (setting exposure to zero) rather than regime-specific ability parameters.\n\n\\subsection{Stage 1: Multi-Signal Exposure Mapping}\n\\label{sec:stage1}\n\nFor each model~$j$ and item~$i$, we compute four complementary detection signals. \\textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \\textbf{S2}~(Min-K\\%++): a membership inference statistic based on token-level surprisal \\citep{duan2025minkpp}. \\textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \\citep{dekoninck2024constat}. \\textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions \\citep{wust2025selfcritique}. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \\S\\ref{sec:signal_analysis}.\n\nWe aggregate signals via Reciprocal Rank Fusion \\citep[RRF;][]{cormack2009}:\n\\begin{equation}\n\\label{eq:rrf}\n    e_{ij} = \\sum_{s=1}^{4} \\frac{1}{k + r_{s}(i)},\n\\end{equation}\nwhere $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious) and $k=60$ is the standard smoothing constant. Raw scores are min-max normalized per model to obtain $e_{ij} \\in [0,1]$.\n\nRRF is a deliberate design choice. A learned aggregator requires labeled contamination data, but ground-truth labels are precisely what we lack. The aggregator's own training data may be contaminated, creating a meta-circularity problem. RRF sidesteps this by operating on rank orderings without parameter estimation.\n\n\\subsection{Stage 2: Contamination-Augmented IRT}\n\\label{sec:stage2}\n\n\\paragraph{Primary model: 2PL+$\\gamma$.}\nOur primary specification augments the two-parameter logistic model with a per-domain contamination covariate. For benchmark~$k$ containing domains $d \\in \\{1,\\ldots,D_k\\}$ (e.g., MMLU has $D_k=8$ subject domains), the response probability is:\n\\begin{equation}\n\\label{eq:2pl_gamma}\n    P(y_{ijk} = 1) = \\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_{d(i)} \\cdot e_{ij}\\bigr),\n\\end{equation}\nwhere $\\sigma(\\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \\in \\mathbb{R}$ is item difficulty, $\\theta_j$ is model ability, and $\\gamma_{d(i)}$ is the contamination effect for the domain containing item~$i$. The per-domain specification permits heterogeneous effects: memorization may inflate knowledge recall while leaving reasoning items unaffected within the same benchmark. When a benchmark lacks domain structure, a single $\\gamma_k$ is estimated.\n\nThe additive structure admits a natural interpretation: contamination shifts the effective difficulty of item~$i$ by $\\gamma_{d(i)} \\cdot e_{ij} / a_i$ units on the ability scale.\n\n\\paragraph{4PL extension for multiple-choice benchmarks.}\nFor MC-format benchmarks (ARC, MMLU) where guessing and ceiling effects are non-negligible, we extend to:\n\\begin{equation}\n\\label{eq:4pl_gamma}\n    P(y_{ijk} = 1) = c_i + (d_i - c_i)\\,\\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_{d(i)} \\cdot e_{ij}\\bigr),\n\\end{equation}\nwith guessing asymptote $c_i \\sim \\text{Beta}(5,20)$ and ceiling $d_i \\sim \\text{Beta}(20,5)$. This extension requires $J \\geq 16$ models to avoid overparameterization; with fewer respondents, the $c_i$ and $d_i$ parameters become unidentifiable (empirically confirmed: ARC with $J=5$ under 4PL+$\\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068).\n\n\\paragraph{Inference.}\nWe perform Bayesian inference via NUTS \\citep{hoffman2014} in Stan \\citep{carpenter2017}, running four chains with target acceptance 0.95. Priors: $\\theta_j \\sim \\mathcal{N}(0,1)$, $a_i \\sim \\text{LogNormal}(0, 0.5)$, $b_i \\sim \\mathcal{N}(0,1)$, $\\gamma_{d} \\sim \\mathcal{N}(0,1)$. Convergence requires split-$\\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters.\n\n\\paragraph{Calibrated score.}\nThe decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:\n\\begin{equation}\n\\label{eq:calibrated}\n    \\text{Acc}_{j}^{\\text{cal}} = \\frac{1}{I_k} \\sum_{i=1}^{I_k}\\, \\mathbb{E}_{\\boldsymbol{\\psi} \\sim p(\\boldsymbol{\\psi} \\mid \\mathbf{y})} \\!\\left[\\sigma\\!\\bigl(a_i(\\theta_j - b_i)\\bigr)\\right],\n\\end{equation}\nwith credible intervals from posterior quantiles. Models with noisier exposure signals receive wider intervals by construction.\n\n\\subsection{Fisher Information and Identifiability}\n\\label{sec:fisher}\n\nThe reliability of $\\gamma$ estimation depends on two factors: signal discriminative quality (AUC of exposure scores) and ensemble size~$J$. The expected Fisher information $\\mathcal{I}(\\gamma)$ depends on $\\text{Var}(e_{\\cdot i})$ across models for each item (full derivation in Appendix~A). When signal AUC is low, exposure scores become uniform, collapsing this variance and rendering $\\gamma$ structurally unidentifiable.\n\nWe validate via simulation across 24 conditions (4~AUC levels $\\times$ 4~ensemble sizes, 10 seeds each). Recovery succeeds down to AUC$=$0.55 (lowest tested) with bias~$<0.05$ and 95\\% CI coverage~$\\geq$90\\% at $J \\geq 50$. Posterior CI width scales as $J^{-0.48}$, close to the parametric $J^{-0.5}$ rate.\n\nThis reveals a domain-method mismatch: IRT-based LLM evaluation typically pools $J = 8$--$30$ models \\citep{polo2026growing,lalor2024irt}, well below the $J \\geq 50$ regime where $\\gamma$ recovery is reliable. This structural gap is itself a central finding (\\S\\ref{sec:results}).\n\n\\subsection{Calibration Value Decomposition}\n\\label{sec:value_decomposition}\n\nEq.~\\eqref{eq:calibrated} depends on the ability estimate~$\\theta_j$, not on $\\gamma$ directly. Two mechanisms contribute to calibration quality: (a)~IRT ability estimation, which separates stable capability from item-level noise regardless of the contamination model; and (b)~the explicit $\\gamma$ correction, which absorbs contamination variance during joint estimation of~$\\theta_j$.\n\nEmpirically, vanilla 2PL ($\\gamma\\!=\\!0$) achieves calibration MAE comparable to 2PL+$\\gamma$ across all benchmarks: GSM8K 0.0063 vs 0.0062, MMLU 0.0068 vs 0.0070, ARC 0.0158 vs 0.0201. The calibration benefit comes entirely from IRT ability estimation itself, which provides better $\\theta$ separation from noise than raw accuracy.\n\nThis strengthens rather than undermines our framework. The $\\gamma_{d}$ parameters serve a complementary diagnostic role: they reveal which domains exhibit inflation or deflation, the direction and magnitude of contamination effects, and model misfit patterns. These are actionable characterizations that aggregate calibration metrics cannot deliver. Calibration says ``how much to trust''; $\\gamma$ says ``where and why scores are distorted.''\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "543020ce-62fd-40e8-aa50-29e848c86358",
  "isSidechain": false,
  "requestId": "req_011Cb7V1Ux2yQtueXHe6u6qV",
  "type": "assistant",
  "uuid": "8d7cbb1f-6716-4834-96b8-f01b6beb0fe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHzrqGkm1cjN9PtszcUm2J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5529,
      "cache_read_input_tokens": 51511,
      "output_tokens": 4054,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4054,
          "cache_read_input_tokens": 51511,
          "cache_creation_input_tokens": 5529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5529
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

_source line 26 · 2026-05-17T04:10:00.385Z_

<details><summary>↩ Tool result · `toolu_012vNDGPzWW6aQrWZLowUZCg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d7cbb1f-6716-4834-96b8-f01b6beb0fe8",
  "isSidechain": false,
  "promptId": "a6e775ec-3f10-4982-9c94-8b07992debf7",
  "type": "user",
  "uuid": "8dc074a1-4891-4fbe-af12-31e4225d2cd3",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\nContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nLet $y_{ijk} \\in \\{0,1\\}$ denote the binary response of model~$j$ ($j=1,\\ldots,J$) to item~$i$ ($i=1,\\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\\theta_j, \\boldsymbol{\\xi}_i)$ where $\\theta_j$ is latent ability and $\\boldsymbol{\\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\\hat{\\theta}_j$ confounds genuine capability with memorization.\n\nOur goal is twofold: (1)~estimate $\\theta_j^{\\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \\citep{eckerly2017,sinharay2017} and explanatory IRT \\citep{deboeck2004}, adapting these frameworks through three structural modifications for LLM evaluation.\n\n\\textit{Adaptation~1: Independent examinees $\\to$ shared item pool.} Classical IRT assumes independent test-takers. In LLM evaluation, a fixed item set is shared across all models, and responses within a single model may exhibit residual correlations beyond the scalar~$\\theta_j$ \\citep{sanmartin2009}. We mitigate this by fitting per-benchmark models.\n\n\\textit{Adaptation~2: Binary leakage $\\to$ continuous exposure.} Item compromise IRT uses binary indicators \\citep{sinharay2017}. LLM contamination is graded: a model may have encountered an item zero, once, or hundreds of times. We replace binary indicators with continuous exposure scores $e_{ij} \\in [0,1]$ derived from detection signals, following the explanatory IRT tradition \\citep{deboeck2004}.\n\n\\textit{Adaptation~3: Stable ability $\\to$ regime-conditional ability.} In educational testing, ability is approximately constant. For LLMs, the training regime (SFT vs.\\ RL) qualitatively changes both internal representations and signal reliability. We recover clean ability via counterfactual inference (setting exposure to zero) rather than regime-specific ability parameters.\n\n\\subsection{Stage 1: Multi-Signal Exposure Mapping}\n\\label{sec:stage1}\n\nFor each model~$j$ and item~$i$, we compute four complementary detection signals. \\textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \\textbf{S2}~(Min-K\\%++): a membership inference statistic based on token-level surprisal \\citep{duan2025minkpp}. \\textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \\citep{dekoninck2024constat}. \\textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions \\citep{wust2025selfcritique}. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \\S\\ref{sec:signal_analysis}.\n\nWe aggregate signals via Reciprocal Rank Fusion \\citep[RRF;][]{cormack2009}:\n\\begin{equation}\n\\label{eq:rrf}\n    e_{ij} = \\sum_{s=1}^{4} \\frac{1}{k + r_{s}(i)},\n\\end{equation}\nwhere $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious) and $k=60$ is the standard smoothing constant. Raw scores are min-max normalized per model to obtain $e_{ij} \\in [0,1]$.\n\nRRF is a deliberate design choice. A learned aggregator requires labeled contamination data, but ground-truth labels are precisely what we lack. The aggregator's own training data may be contaminated, creating a meta-circularity problem. RRF sidesteps this by operating on rank orderings without parameter estimation.\n\n\\subsection{Stage 2: Contamination-Augmented IRT}\n\\label{sec:stage2}\n\n\\paragraph{Primary model: 2PL+$\\gamma$.}\nOur primary specification augments the two-parameter logistic model with a per-domain contamination covariate. For benchmark~$k$ containing domains $d \\in \\{1,\\ldots,D_k\\}$ (e.g., MMLU has $D_k=8$ subject domains), the response probability is:\n\\begin{equation}\n\\label{eq:2pl_gamma}\n    P(y_{ijk} = 1) = \\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_{d(i)} \\cdot e_{ij}\\bigr),\n\\end{equation}\nwhere $\\sigma(\\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \\in \\mathbb{R}$ is item difficulty, $\\theta_j$ is model ability, and $\\gamma_{d(i)}$ is the contamination effect for the domain containing item~$i$. The per-domain specification permits heterogeneous effects: memorization may inflate knowledge recall while leaving reasoning items unaffected within the same benchmark. When a benchmark lacks domain structure, a single $\\gamma_k$ is estimated.\n\nThe additive structure admits a natural interpretation: contamination shifts the effective difficulty of item~$i$ by $\\gamma_{d(i)} \\cdot e_{ij} / a_i$ units on the ability scale.\n\n\\paragraph{4PL extension for multiple-choice benchmarks.}\nFor MC-format benchmarks (ARC, MMLU) where guessing and ceiling effects are non-negligible, we extend to:\n\\begin{equation}\n\\label{eq:4pl_gamma}\n    P(y_{ijk} = 1) = c_i + (d_i - c_i)\\,\\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_{d(i)} \\cdot e_{ij}\\bigr),\n\\end{equation}\nwith guessing asymptote $c_i \\sim \\text{Beta}(5,20)$ and ceiling $d_i \\sim \\text{Beta}(20,5)$. This extension requires $J \\geq 16$ models to avoid overparameterization; with fewer respondents, the $c_i$ and $d_i$ parameters become unidentifiable (empirically confirmed: ARC with $J=5$ under 4PL+$\\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068).\n\n\\paragraph{Inference.}\nWe perform Bayesian inference via NUTS \\citep{hoffman2014} in Stan \\citep{carpenter2017}, running four chains with target acceptance 0.95. Priors: $\\theta_j \\sim \\mathcal{N}(0,1)$, $a_i \\sim \\text{LogNormal}(0, 0.5)$, $b_i \\sim \\mathcal{N}(0,1)$, $\\gamma_{d} \\sim \\mathcal{N}(0,1)$. Convergence requires split-$\\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters.\n\n\\paragraph{Calibrated score.}\nThe decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:\n\\begin{equation}\n\\label{eq:calibrated}\n    \\text{Acc}_{j}^{\\text{cal}} = \\frac{1}{I_k} \\sum_{i=1}^{I_k}\\, \\mathbb{E}_{\\boldsymbol{\\psi} \\sim p(\\boldsymbol{\\psi} \\mid \\mathbf{y})} \\!\\left[\\sigma\\!\\bigl(a_i(\\theta_j - b_i)\\bigr)\\right],\n\\end{equation}\nwith credible intervals from posterior quantiles. Models with noisier exposure signals receive wider intervals by construction.\n\n\\subsection{Fisher Information and Identifiability}\n\\label{sec:fisher}\n\nThe reliability of $\\gamma$ estimation depends on two factors: signal discriminative quality (AUC of exposure scores) and ensemble size~$J$. The expected Fisher information $\\mathcal{I}(\\gamma)$ depends on $\\text{Var}(e_{\\cdot i})$ across models for each item (full derivation in Appendix~A). When signal AUC is low, exposure scores become uniform, collapsing this variance and rendering $\\gamma$ structurally unidentifiable.\n\nWe validate via simulation across 24 conditions (4~AUC levels $\\times$ 4~ensemble sizes, 10 seeds each). Recovery succeeds down to AUC$=$0.55 (lowest tested) with bias~$<0.05$ and 95\\% CI coverage~$\\geq$90\\% at $J \\geq 50$. Posterior CI width scales as $J^{-0.48}$, close to the parametric $J^{-0.5}$ rate.\n\nThis reveals a domain-method mismatch: IRT-based LLM evaluation typically pools $J = 8$--$30$ models \\citep{polo2026growing,lalor2024irt}, well below the $J \\geq 50$ regime where $\\gamma$ recovery is reliable. This structural gap is itself a central finding (\\S\\ref{sec:results}).\n\n\\subsection{Calibration Value Decomposition}\n\\label{sec:value_decomposition}\n\nEq.~\\eqref{eq:calibrated} depends on the ability estimate~$\\theta_j$, not on $\\gamma$ directly. Two mechanisms contribute to calibration quality: (a)~IRT ability estimation, which separates stable capability from item-level noise regardless of the contamination model; and (b)~the explicit $\\gamma$ correction, which absorbs contamination variance during joint estimation of~$\\theta_j$.\n\nEmpirically, vanilla 2PL ($\\gamma\\!=\\!0$) achieves calibration MAE comparable to 2PL+$\\gamma$ across all benchmarks: GSM8K 0.0063 vs 0.0062, MMLU 0.0068 vs 0.0070, ARC 0.0158 vs 0.0201. The calibration benefit comes entirely from IRT ability estimation itself, which provides better $\\theta$ separation from noise than raw accuracy.\n\nThis strengthens rather than undermines our framework. The $\\gamma_{d}$ parameters serve a complementary diagnostic role: they reveal which domains exhibit inflation or deflation, the direction and magnitude of contamination effects, and model misfit patterns. These are actionable characterizations that aggregate calibration metrics cannot deliver. Calibration says ``how much to trust''; $\\gamma$ says ``where and why scores are distorted.''\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 116,
        "newStart": 1,
        "newLines": 81,
        "lines": [
          " \\section{Method}",
          " \\label{sec:method}",
          " ",
          "-ContamCal operates in two stages. Stage~1 (\\S\\ref{sec:stage1}) estimates per-item contamination exposure by fusing multiple detection signals into a single score. Stage~2 (\\S\\ref{sec:stage2}--\\S\\ref{sec:calibrated}) embeds these scores as covariates in a contamination-augmented IRT model, performing Bayesian inference to produce calibrated benchmark scores with credible intervals.",
          "+ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.",
          " ",
          "-\\subsection{Stage 1: Multi-Signal Provenance Mapping}",
          "-\\label{sec:stage1}",
          "+\\subsection{Problem Formulation}",
          "+\\label{sec:formulation}",
          " ",
          "-For each model~$i$ and benchmark item~$j$, we compute four complementary detection signals that capture different facets of contamination evidence.",
          "+Let $y_{ijk} \\in \\{0,1\\}$ denote the binary response of model~$j$ ($j=1,\\ldots,J$) to item~$i$ ($i=1,\\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\\theta_j, \\boldsymbol{\\xi}_i)$ where $\\theta_j$ is latent ability and $\\boldsymbol{\\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\\hat{\\theta}_j$ confounds genuine capability with memorization.",
          " ",
          "-\\paragraph{Embedding-based near-duplicate retrieval.}",
          "-We embed both training corpus segments and benchmark items using a sentence transformer encoder and build a FAISS index over training embeddings for efficient retrieval. The signal $s_1(i,j)$ is the maximum cosine similarity between item~$j$ and the top-$K$ retrieved training segments for model~$i$'s training corpus, capturing semantic overlap that survives paraphrasing and surface-level reformulation.",
          "+Our goal is twofold: (1)~estimate $\\theta_j^{\\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \\citep{eckerly2017,sinharay2017} and explanatory IRT \\citep{deboeck2004}, adapting these frameworks through three structural modifications for LLM evaluation.",
          " ",
          "-\\paragraph{Min-K\\%++ membership inference.}",
          "-Following \\citet{duan2025minkpp}, we compute the average log-probability of the $k\\%$ least-likely tokens in each benchmark item under model~$i$, z-scored against a reference (clean) model. Contaminated items yield systematically higher (less negative) Min-K\\%++ scores, as the model assigns elevated probability to tokens it has memorized during training. The signal $s_2(i,j)$ is the resulting membership inference statistic. We use a simplified variant that z-normalizes per-item against a single reference model's mean and standard deviation, rather than the per-token z-scoring of the original formulation; since the downstream RRF aggregation operates on ranks rather than raw scores, this simplification preserves signal ordering while reducing computational cost.",
          "+\\textit{Adaptation~1: Independent examinees $\\to$ shared item pool.} Classical IRT assumes independent test-takers. In LLM evaluation, a fixed item set is shared across all models, and responses within a single model may exhibit residual correlations beyond the scalar~$\\theta_j$ \\citep{sanmartin2009}. We mitigate this by fitting per-benchmark models.",
          " ",
          "-\\paragraph{ConStat performance gap.}",
          "-For each benchmark item, we generate a semantically equivalent paraphrased variant using an independent rewriter model. The signal $s_3(i,j)$ is the accuracy gap between model~$i$'s performance on the original item versus its paraphrased counterpart \\citep{dekoninck2024constat}. A model that has memorized the original surface form but genuinely understands the underlying concept should perform comparably on both versions; a large gap indicates surface-level memorization rather than robust capability.",
          "+\\textit{Adaptation~2: Binary leakage $\\to$ continuous exposure.} Item compromise IRT uses binary indicators \\citep{sinharay2017}. LLM contamination is graded: a model may have encountered an item zero, once, or hundreds of times. We replace binary indicators with continuous exposure scores $e_{ij} \\in [0,1]$ derived from detection signals, following the explanatory IRT tradition \\citep{deboeck2004}.",
          " ",
          "-\\paragraph{Self-Critique entropy collapse.}",
          "-When model~$i$ is prompted to evaluate the correctness of its own response to item~$j$, contaminated items elicit low-entropy self-evaluation distributions---the model exhibits overconfidence in its assessment of memorized content \\citep{wust2025selfcritique}. The signal $s_4(i,j)$ is the negative entropy of the self-critique distribution. This signal is particularly valuable because it operates at the meta-cognitive level and exhibits greater robustness to RL post-training than signals relying on token-level statistics (\\S\\ref{sec:signal_survival}).",
          "+\\textit{Adaptation~3: Stable ability $\\to$ regime-conditional ability.} In educational testing, ability is approximately constant. For LLMs, the training regime (SFT vs.\\ RL) qualitatively changes both internal representations and signal reliability. We recover clean ability via counterfactual inference (setting exposure to zero) rather than regime-specific ability parameters.",
          " ",
          "-\\paragraph{Signal survival analysis.}",
          "-\\label{sec:signal_survival}",
          "-Prior work suggests that detection signals do not degrade uniformly across training regimes. \\citet{wang2025fragility} demonstrate that RL post-training with GRPO substantially degrades probability-based detection signals (Min-K\\%++, ConStat), while entropy-based approaches such as Self-Critique retain greater robustness by exploiting policy collapse rather than probability gaps. This motivates our inclusion of Self-Critique alongside probability-based signals: if the signal~$\\times$~regime interaction is confirmed in our controlled experiments, it has two practical consequences. First, exposure estimates for RL-trained models would carry higher uncertainty, which the measurement error model in Stage~2 propagates into appropriately wider credible intervals. Second, a cliff-like (rather than gradual) degradation pattern would imply that RL fundamentally restructures the model's relationship to memorized content, rather than merely attenuating detection signals. We systematically evaluate signal survival across training regimes in \\S\\ref{sec:experiments}.% TODO: fill in quantitative AUC values from exp-008 results",
          "+\\subsection{Stage 1: Multi-Signal Exposure Mapping}",
          "+\\label{sec:stage1}",
          " ",
          "-\\paragraph{RRF aggregation.}",
          "-We aggregate the four signals via reciprocal rank fusion \\citep{cormack2009}. For each model~$i$, items are ranked independently by each signal~$s$, and the fused exposure score is:",
          "+For each model~$j$ and item~$i$, we compute four complementary detection signals. \\textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \\textbf{S2}~(Min-K\\%++): a membership inference statistic based on token-level surprisal \\citep{duan2025minkpp}. \\textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \\citep{dekoninck2024constat}. \\textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions \\citep{wust2025selfcritique}. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \\S\\ref{sec:signal_analysis}.",
          "+",
          "+We aggregate signals via Reciprocal Rank Fusion \\citep[RRF;][]{cormack2009}:",
          " \\begin{equation}",
          " \\label{eq:rrf}",
          "-    e_{ij} = \\sum_{s=1}^{4} \\frac{1}{k + r_{s,i}(j)},",
          "+    e_{ij} = \\sum_{s=1}^{4} \\frac{1}{k + r_{s}(i)},",
          " \\end{equation}",
          "-where $r_{s,i}(j)$ is the rank of item~$j$ under signal~$s$ for model~$i$, and $k = 60$ is the standard RRF smoothing constant. RRF is a deliberate design choice over learned aggregation (\\emph{e.g.}, logistic regression over signal scores). A learned aggregator requires labeled training data indicating which items are truly contaminated---but ground-truth contamination labels are precisely what we lack, and the aggregator's training data may itself be contaminated, creating meta-circularity. RRF avoids this by requiring no training, providing a robust, parameter-free fusion baseline.",
          "+where $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious) and $k=60$ is the standard smoothing constant. Raw scores are min-max normalized per model to obtain $e_{ij} \\in [0,1]$.",
          " ",
          "-We note that KDS \\citep{xu2025kds} provides a complementary detection signal based on knowledge distillation signatures, but requires per-model LoRA fine-tuning at $O(N^2)$ computational cost. We include KDS in ablation experiments but exclude it from the default pipeline for scalability.",
          "+RRF is a deliberate design choice. A learned aggregator requires labeled contamination data, but ground-truth labels are precisely what we lack. The aggregator's own training data may be contaminated, creating a meta-circularity problem. RRF sidesteps this by operating on rank orderings without parameter estimation.",
          " ",
          "-\\subsection{Stage 2: Contamination-Augmented 4PL IRT}",
          "+\\subsection{Stage 2: Contamination-Augmented IRT}",
          " \\label{sec:stage2}",
          " ",
          "-\\paragraph{Model specification.}",
          "-We augment the standard four-parameter logistic (4PL) IRT model \\citep{lord1980} with a contamination covariate. The probability that model~$i$ correctly answers item~$j$ is:",
          "+\\paragraph{Primary model: 2PL+$\\gamma$.}",
          "+Our primary specification augments the two-parameter logistic model with a per-domain contamination covariate. For benchmark~$k$ containing domains $d \\in \\{1,\\ldots,D_k\\}$ (e.g., MMLU has $D_k=8$ subject domains), the response probability is:",
          " \\begin{equation}",
          "-\\label{eq:4pl}",
          "-    P(y_{ij} = 1 \\mid \\boldsymbol{\\psi}) = c_j + (d_j - c_j)\\,\\sigma\\!\\bigl(a_j(\\theta_i - b_j) + \\gamma \\cdot \\tau_{ij}\\bigr),",
          "+\\label{eq:2pl_gamma}",
          "+    P(y_{ijk} = 1) = \\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_{d(i)} \\cdot e_{ij}\\bigr),",
          " \\end{equation}",
          "-where $\\sigma(\\cdot)$ denotes the logistic function, $y_{ij} \\in \\{0,1\\}$ is the binary response, and $\\boldsymbol{\\psi}$ collects all parameters. The standard IRT parameters are: $\\theta_i \\in \\mathbb{R}$ (ability of model~$i$), $a_j > 0$ (discrimination of item~$j$), $b_j \\in \\mathbb{R}$ (difficulty of item~$j$), $c_j \\in [0,1]$ (guessing/lower asymptote), and $d_j \\in [0,1]$ (upper asymptote/slip parameter). The contamination-specific parameters are: $\\gamma \\in \\mathbb{R}$ (global contamination effect) and $\\tau_{ij} \\geq 0$ (latent true exposure of model~$i$ to item~$j$).",
          "+where $\\sigma(\\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \\in \\mathbb{R}$ is item difficulty, $\\theta_j$ is model ability, and $\\gamma_{d(i)}$ is the contamination effect for the domain containing item~$i$. The per-domain specification permits heterogeneous effects: memorization may inflate knowledge recall while leaving reasoning items unaffected within the same benchmark. When a benchmark lacks domain structure, a single $\\gamma_k$ is estimated.",
          " ",
          "-The additive structure $a_j(\\theta_i - b_j) + \\gamma \\cdot \\tau_{ij}$ admits a natural interpretation: contamination exposure shifts the effective ability of a model on a given item by $\\gamma \\cdot \\tau_{ij} / a_j$ units on the ability scale. When $\\tau_{ij} = 0$ (no contamination), Eq.~\\eqref{eq:4pl} reduces to the standard 4PL model. A positive~$\\gamma$ indicates that contamination inflates performance, as expected.",
          "+The additive structure admits a natural interpretation: contamination shifts the effective difficulty of item~$i$ by $\\gamma_{d(i)} \\cdot e_{ij} / a_i$ units on the ability scale.",
          " ",
          "-\\paragraph{Measurement error model.}",
          "-The latent exposure $\\tau_{ij}$ is not directly observed; we observe the noisy RRF-derived estimate $e_{ij}$ from Stage~1. We model this relationship as:",
          "+\\paragraph{4PL extension for multiple-choice benchmarks.}",
          "+For MC-format benchmarks (ARC, MMLU) where guessing and ceiling effects are non-negligible, we extend to:",
          " \\begin{equation}",
          "-\\label{eq:measurement_error}",
          "-    \\tau_{ij} \\sim \\mathcal{N}(e_{ij},\\, \\sigma_e^2),",
          "+\\label{eq:4pl_gamma}",
          "+    P(y_{ijk} = 1) = c_i + (d_i - c_i)\\,\\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_{d(i)} \\cdot e_{ij}\\bigr),",
          " \\end{equation}",
          "-where $\\sigma_e^2$ is the measurement error variance, estimated jointly with other model parameters. This formulation treats the observed exposure scores as noisy proxies for latent contamination and has two critical consequences. First, uncertainty in the detection signals is automatically propagated into the posterior over ability~$\\theta_i$ and contamination effect~$\\gamma$, yielding appropriately wider credible intervals when signals are unreliable. Second, under RL post-training---where signal degradation is severe (\\S\\ref{sec:signal_survival})---the posterior distribution of~$\\tau_{ij}$ becomes more diffuse, producing wider credible intervals that honestly reflect our reduced ability to distinguish contaminated from clean items.",
          "+with guessing asymptote $c_i \\sim \\text{Beta}(5,20)$ and ceiling $d_i \\sim \\text{Beta}(20,5)$. This extension requires $J \\geq 16$ models to avoid overparameterization; with fewer respondents, the $c_i$ and $d_i$ parameters become unidentifiable (empirically confirmed: ARC with $J=5$ under 4PL+$\\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068).",
          " ",
          "-\\paragraph{Prior specification.}",
          "-We assign the following priors:",
          "-\\begin{align}",
          "-    \\theta_i &\\sim \\mathcal{N}(0, 1), \\label{eq:prior_theta} \\\\",
          "-    a_j &\\sim \\text{LogNormal}(0, 0.5), \\label{eq:prior_a} \\\\",
          "-    b_j &\\sim \\mathcal{N}(0, 1), \\label{eq:prior_b} \\\\",
          "-    c_j &\\sim \\text{Beta}(5, 20), \\label{eq:prior_c} \\\\",
          "-    d_j &\\sim \\text{Beta}(20, 5), \\label{eq:prior_d} \\\\",
          "-    \\gamma &\\sim \\mathcal{N}(0, 1). \\label{eq:prior_gamma}",
          "-\\end{align}",
          "-The $\\text{Beta}(5, 20)$ prior on~$c_j$ encodes the expectation that guessing rates are low (mean $\\approx 0.2$) but non-negligible for multiple-choice items. The $\\text{Beta}(20, 5)$ prior on~$d_j$ reflects the expectation that upper asymptotes are high (mean $\\approx 0.8$) but not necessarily unity, allowing for careless errors or ambiguous items. The $\\text{LogNormal}(0, 0.5)$ prior on~$a_j$ constrains discrimination to be positive with moderate magnitude (median $= 1$). The weakly informative $\\mathcal{N}(0, 1)$ prior on~$\\gamma$ permits both positive and negative contamination effects; we conduct sensitivity analyses under $\\mathcal{N}(0, 0.5)$ and $\\mathcal{N}(0, 2)$ to assess robustness to this specification (\\S\\ref{sec:experiments}).",
          "+\\paragraph{Inference.}",
          "+We perform Bayesian inference via NUTS \\citep{hoffman2014} in Stan \\citep{carpenter2017}, running four chains with target acceptance 0.95. Priors: $\\theta_j \\sim \\mathcal{N}(0,1)$, $a_i \\sim \\text{LogNormal}(0, 0.5)$, $b_i \\sim \\mathcal{N}(0,1)$, $\\gamma_{d} \\sim \\mathcal{N}(0,1)$. Convergence requires split-$\\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters.",
          " ",
          "-\\paragraph{Connection to item compromise IRT.}",
          "-Equation~\\eqref{eq:4pl} extends the item compromise IRT tradition \\citep{eckerly2017,sinharay2017} with three structural adaptations for the LLM evaluation setting.",
          "+\\paragraph{Calibrated score.}",
          "+The decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:",
          "+\\begin{equation}",
          "+\\label{eq:calibrated}",
          "+    \\text{Acc}_{j}^{\\text{cal}} = \\frac{1}{I_k} \\sum_{i=1}^{I_k}\\, \\mathbb{E}_{\\boldsymbol{\\psi} \\sim p(\\boldsymbol{\\psi} \\mid \\mathbf{y})} \\!\\left[\\sigma\\!\\bigl(a_i(\\theta_j - b_i)\\bigr)\\right],",
          "+\\end{equation}",
          "+with credible intervals from posterior quantiles. Models with noisier exposure signals receive wider intervals by construction.",
          " ",
          "-\\emph{Adaptation~1: Independent examinees $\\to$ shared item pool.} In educational testing, each examinee independently samples from a population ability distribution. In LLM evaluation, a single model responds to all items, and its responses are correlated through shared model parameters. This alters the local independence assumption: conditional on~$\\theta_i$, item responses within a single model may remain correlated through model-specific idiosyncrasies not captured by the scalar ability parameter \\citep{mislevy1986,sanmartin2009}. We mitigate this by fitting IRT models per-benchmark---reducing the scope of potential violations---and empirically assessing residual correlations via posterior predictive checks (\\S\\ref{sec:experiments}).",
          "+\\subsection{Fisher Information and Identifiability}",
          "+\\label{sec:fisher}",
          " ",
          "-\\emph{Adaptation~2: Binary leakage $\\to$ continuous exposure.} Classical item compromise models use binary indicators $e_{ij} \\in \\{0, 1\\}$ \\citep{sinharay2017}. We generalize to continuous exposure scores $\\tau_{ij} \\in \\mathbb{R}^+$ derived from noisy detection signals, which is standard in explanatory IRT \\citep{deboeck2004} but necessitates the measurement error formulation of Eq.~\\eqref{eq:measurement_error} to prevent attenuation bias from regression dilution \\citep{maris2009}.",
          "+The reliability of $\\gamma$ estimation depends on two factors: signal discriminative quality (AUC of exposure scores) and ensemble size~$J$. The expected Fisher information $\\mathcal{I}(\\gamma)$ depends on $\\text{Var}(e_{\\cdot i})$ across models for each item (full derivation in Appendix~A). When signal AUC is low, exposure scores become uniform, collapsing this variance and rendering $\\gamma$ structurally unidentifiable.",
          " ",
          "-\\emph{Adaptation~3: Stable ability $\\to$ regime-conditional ability.} An examinee's ability is typically assumed stable across test items. For LLMs, the training regime (SFT vs.\\ RL) qualitatively changes both the model's ability profile and the reliability of detection signals. We handle this through the signal survival analysis (\\S\\ref{sec:signal_survival}), which informs the measurement error variance, rather than through regime-specific ability parameters---preserving model parsimony while acknowledging regime effects through the uncertainty channel.",
          "+We validate via simulation across 24 conditions (4~AUC levels $\\times$ 4~ensemble sizes, 10 seeds each). Recovery succeeds down to AUC$=$0.55 (lowest tested) with bias~$<0.05$ and 95\\% CI coverage~$\\geq$90\\% at $J \\geq 50$. Posterior CI width scales as $J^{-0.48}$, close to the parametric $J^{-0.5}$ rate.",
          " ",
          "-\\subsection{Bayesian Inference}",
          "-\\label{sec:inference}",
          "+This reveals a domain-method mismatch: IRT-based LLM evaluation typically pools $J = 8$--$30$ models \\citep{polo2026growing,lalor2024irt}, well below the $J \\geq 50$ regime where $\\gamma$ recovery is reliable. This structural gap is itself a central finding (\\S\\ref{sec:results}).",
          " ",
          "-We perform full Bayesian inference using the No-U-Turn Sampler \\citep[NUTS;][]{hoffman2014} implemented in CmdStanPy \\citep{carpenter2017}. We run four independent Markov chains and assess convergence via three diagnostics: split-$\\hat{R} < 1.01$ for all parameters, effective sample size $\\text{ESS} > 400$ per parameter, and fewer than 0.1\\% divergent transitions. The target acceptance probability is set to $\\texttt{adapt\\_delta} = 0.95$ to reduce divergences in the high-curvature posterior geometry induced by the 4PL model's bounded response function.",
          "+\\subsection{Calibration Value Decomposition}",
          "+\\label{sec:value_decomposition}",
          " ",
          "-\\paragraph{Per-benchmark fitting.}",
          "-Rather than fitting a single IRT model jointly across all benchmarks, we fit separate models per benchmark. This design choice reduces the scope of local independence violations: within a single benchmark, items share a common knowledge domain, making the conditional independence assumption more defensible than across heterogeneous benchmarks encompassing knowledge recall, mathematical reasoning, and code generation \\citep{sanmartin2009}. Per-benchmark fitting also naturally yields benchmark-specific contamination effects~$\\gamma_k$ (\\S\\ref{sec:calibrated}), the primary specification in our framework.",
          "+Eq.~\\eqref{eq:calibrated} depends on the ability estimate~$\\theta_j$, not on $\\gamma$ directly. Two mechanisms contribute to calibration quality: (a)~IRT ability estimation, which separates stable capability from item-level noise regardless of the contamination model; and (b)~the explicit $\\gamma$ correction, which absorbs contamination variance during joint estimation of~$\\theta_j$.",
          " ",
          "-\\paragraph{Few-examinee regime.}",
          "-Standard IRT applications assume large examinee populations ($N > 200$), but current LLM evaluation studies may include as few as 20--50 models. In this low-$N$ regime, item parameter estimation becomes unstable without informative priors. We address this by incorporating empirical Bayes priors for item parameters derived from the Growing Pains study \\citep{polo2026growing}, which provides item parameter estimates from a pool of 400+ models. Specifically, the item difficulty and discrimination priors are centered at the Growing Pains point estimates with moderately inflated variances, serving as a regularizing anchor while permitting data-driven updating. We validate this prior transfer procedure via simulation-based calibration \\citep[SBC;][]{talts2018sbc}, confirming that posteriors are well-calibrated under the specified priors across a range of sample sizes (\\S\\ref{sec:experiments}). Automatic differentiation variational inference \\citep[ADVI;][]{ulitzsch2022} is explored as a scalability option for larger item pools in the appendix, though preliminary results indicate ADVI may fail to converge for the 4PL specification due to the bounded response function's multimodal posterior geometry; we include the comparison for completeness.",
          "+Empirically, vanilla 2PL ($\\gamma\\!=\\!0$) achieves calibration MAE comparable to 2PL+$\\gamma$ across all benchmarks: GSM8K 0.0063 vs 0.0062, MMLU 0.0068 vs 0.0070, ARC 0.0158 vs 0.0201. The calibration benefit comes entirely from IRT ability estimation itself, which provides better $\\theta$ separation from noise than raw accuracy.",
          " ",
          "-\\subsection{Calibrated Score Computation}",
          "-\\label{sec:calibrated}",
          "-",
          "-Given the posterior distribution over all parameters, we compute the calibrated (decontaminated) accuracy for model~$i$ on benchmark~$B$ by setting exposure to zero and marginalizing over posterior uncertainty:",
          "-\\begin{equation}",
          "-\\label{eq:calibrated}",
          "-    \\text{Acc}_{i}^{\\text{cal}} = \\frac{1}{|B|} \\sum_{j \\in B}\\, \\mathbb{E}_{\\boldsymbol{\\psi} \\sim p(\\boldsymbol{\\psi} \\mid \\mathbf{y})} \\!\\left[ c_j + (d_j - c_j)\\,\\sigma\\!\\bigl(a_j(\\theta_i - b_j)\\bigr) \\right],",
          "-\\end{equation}",
          "-where the expectation is taken over posterior draws of~$\\boldsymbol{\\psi}$ and the contamination term $\\gamma \\cdot \\tau_{ij}$ has been removed. This counterfactual quantity answers: \\emph{what would model~$i$'s expected accuracy be on benchmark~$B$ had it never been exposed to any test items during training?}",
          "-",
          "-In practice, we approximate Eq.~\\eqref{eq:calibrated} by averaging over $L$ posterior draws $\\{\\boldsymbol{\\psi}^{(\\ell)}\\}_{\\ell=1}^{L}$:",
          "-\\begin{equation}",
          "-\\label{eq:calibrated_mc}",
          "-    \\widehat{\\text{Acc}}_{i}^{\\text{cal}} = \\frac{1}{L} \\sum_{\\ell=1}^{L} \\frac{1}{|B|} \\sum_{j \\in B} \\left[ c_j^{(\\ell)} + (d_j^{(\\ell)} - c_j^{(\\ell)})\\,\\sigma\\!\\bigl(a_j^{(\\ell)}(\\theta_i^{(\\ell)} - b_j^{(\\ell)})\\bigr) \\right].",
          "-\\end{equation}",
          "-Credible intervals at level~$\\alpha$ are obtained from the empirical quantiles of $\\{\\text{Acc}_{i}^{\\text{cal},(\\ell)}\\}_{\\ell=1}^{L}$. We report 50\\%, 80\\%, and 95\\% intervals. By construction, models with higher exposure scores and noisier detection signals---whose $\\tau_{ij}$ posteriors are more diffuse---receive wider credible intervals, encoding the principle that calibration is only as reliable as its inputs.",
          "-",
          "-\\paragraph{Per-benchmark contamination effects.}",
          "-Since we fit independent models per benchmark (\\S\\ref{sec:inference}), each benchmark naturally yields its own contamination effect parameter~$\\gamma_k$:",
          "-\\begin{equation}",
          "-\\label{eq:per_benchmark_gamma}",
          "-    P(y_{ij} = 1 \\mid \\boldsymbol{\\psi}_k) = c_j + (d_j - c_j)\\,\\sigma\\!\\bigl(a_j(\\theta_i - b_j) + \\gamma_k \\cdot \\tau_{ij}\\bigr),",
          "-\\end{equation}",
          "-where $\\gamma_k$ is the contamination effect specific to benchmark~$k$, with independent priors $\\gamma_k \\sim \\mathcal{N}(0, 1)$. This is the primary specification, permitting heterogeneous contamination effects across benchmarks.",
          "-",
          "-\\paragraph{Calibration value decomposition.}",
          "-The calibrated score in Eq.~\\eqref{eq:calibrated} depends on the ability estimate~$\\theta_i$, not on $\\gamma_k$ directly. Two distinct mechanisms contribute to calibration quality: (a)~the IRT ability estimation itself, which separates stable model capability from item-specific noise regardless of the contamination model; and (b)~the explicit $\\gamma_k$ correction, which reweights items based on exposure during the joint estimation of~$\\theta_i$. In principle, including $\\gamma_k$ should yield better $\\theta_i$ estimates by absorbing contamination variance. In practice, we compare calibration MAE between the full model (2PL+$\\gamma$) and vanilla 2PL ($\\gamma\\!=\\!0$) to quantify the marginal calibration contribution of the contamination covariate (\\S\\ref{sec:results}). The $\\gamma_k$ parameters serve a complementary diagnostic role: they reveal which domains or benchmarks exhibit inflation, deflation, or model misfit, providing actionable characterization that aggregate calibration metrics cannot deliver.",
          "+This strengthens rather than undermines our framework. The $\\gamma_{d}$ parameters serve a complementary diagnostic role: they reveal which domains exhibit inflation or deflation, the direction and magnitude of contamination effects, and model misfit patterns. These are actionable characterizations that aggregate calibration metrics cannot deliver. Calibration says ``how much to trust''; $\\gamma$ says ``where and why scores are distorted.''"
        ]
      }
    ],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "8d7cbb1f-6716-4834-96b8-f01b6beb0fe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "leafUuid": "8dc074a1-4891-4fbe-af12-31e4225d2cd3",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Rewrite Method section with 2PL+γ primary model",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1"
}
```

---

### Assistant

_source line 29 · 2026-05-17T04:10:04.583Z_

Now let me verify the word count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dc074a1-4891-4fbe-af12-31e4225d2cd3",
  "isSidechain": false,
  "requestId": "req_011Cb7V8RswP1RaL3saQomsa",
  "type": "assistant",
  "uuid": "cc7caaa3-605a-46fb-b0d9-a1fb3c12cd27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2hN18bh8CdS5KFHnPswun",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4112,
      "cache_read_input_tokens": 57040,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 57040,
          "cache_creation_input_tokens": 4112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4112
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

_source line 30 · 2026-05-17T04:10:06.842Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019UQbRPjjqKhb5CdH4UUAPy`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$\\\\]//g; s/%.*//g' | wc -w",
  "description": "Count words in method.tex (stripping LaTeX commands)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc7caaa3-605a-46fb-b0d9-a1fb3c12cd27",
  "isSidechain": false,
  "requestId": "req_011Cb7V8RswP1RaL3saQomsa",
  "type": "assistant",
  "uuid": "e9700d8c-a518-4a42-ad9f-31692f428230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2hN18bh8CdS5KFHnPswun",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4112,
      "cache_read_input_tokens": 57040,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 57040,
          "cache_creation_input_tokens": 4112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4112
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

_source line 31 · 2026-05-17T04:10:07.369Z_

<details><summary>↩ Tool result · `toolu_019UQbRPjjqKhb5CdH4UUAPy`</summary>

```text
898
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9700d8c-a518-4a42-ad9f-31692f428230",
  "isSidechain": false,
  "promptId": "a6e775ec-3f10-4982-9c94-8b07992debf7",
  "type": "user",
  "uuid": "2e9a8653-6d2d-427c-b15e-c806349c52f2",
  "toolUseResult": {
    "stdout": "898",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e9700d8c-a518-4a42-ad9f-31692f428230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-17T04:10:07.375Z_

```json
{
  "parentUuid": "2e9a8653-6d2d-427c-b15e-c806349c52f2",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "13232c3c-a77b-4da4-b0ff-31630799da03",
  "timestamp": "2026-05-17T04:10:07.375Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 33 · 2026-05-17T04:10:14.831Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RfRf4psZQLUQ9uYt97Kpae`</summary>

```json
{
  "command": "detex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex 2>/dev/null | wc -w || (cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex | perl -pe 's/\\\\begin\\{equation\\}.*?\\\\end\\{equation\\}//gs; s/\\\\[a-zA-Z]+(\\[[^\\]]*\\])?\\{([^}]*)\\}/\\2/g; s/[\\\\{}$%~]//g; s/\\s+/ /g' | wc -w)",
  "description": "Count words using detex or perl fallback"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13232c3c-a77b-4da4-b0ff-31630799da03",
  "isSidechain": false,
  "requestId": "req_011Cb7V8xNz7XDdn9cvMkMr8",
  "type": "assistant",
  "uuid": "ceee52bd-a3e5-426c-97f2-a387b5b2a2c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvhtvrpeU14yEa5NG93iJy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 61152,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 302,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 256,
          "cache_read_input_tokens": 61152,
          "cache_creation_input_tokens": 302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 302
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T04:10:14.938Z_

<details><summary>↩ Tool result · `toolu_01RfRf4psZQLUQ9uYt97Kpae`</summary>

```text
985
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceee52bd-a3e5-426c-97f2-a387b5b2a2c8",
  "isSidechain": false,
  "promptId": "a6e775ec-3f10-4982-9c94-8b07992debf7",
  "type": "user",
  "uuid": "dab4db3e-05a7-472e-810d-36835adca197",
  "toolUseResult": {
    "stdout": "985",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ceee52bd-a3e5-426c-97f2-a387b5b2a2c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T04:10:22.718Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017vfk57SjWxqdtW4RfNJFzA`</summary>

```json
{
  "command": "texcount -brief -nosub /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex 2>/dev/null || echo \"texcount not available\"",
  "description": "Count words using texcount"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dab4db3e-05a7-472e-810d-36835adca197",
  "isSidechain": false,
  "requestId": "req_011Cb7V9j64Nw1qBmKr7v8xA",
  "type": "assistant",
  "uuid": "9d074d7a-e150-4e87-80c9-f11162df0a0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PW23Q1NFo9rD5YiS7Pns6c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 61454,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 269,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 61454,
          "cache_creation_input_tokens": 269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 269
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

_source line 36 · 2026-05-17T04:10:22.791Z_

<details><summary>↩ Tool result · `toolu_017vfk57SjWxqdtW4RfNJFzA`</summary>

```text
texcount not available
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d074d7a-e150-4e87-80c9-f11162df0a0a",
  "isSidechain": false,
  "promptId": "a6e775ec-3f10-4982-9c94-8b07992debf7",
  "type": "user",
  "uuid": "5c8535bc-2483-43f6-a0d5-469aa1fb283c",
  "toolUseResult": {
    "stdout": "texcount not available",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9d074d7a-e150-4e87-80c9-f11162df0a0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-17T04:10:26.730Z_

Word count is ~985 (within the 1100-word budget). Let me also verify no em-dashes or forbidden patterns slipped in.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c8535bc-2483-43f6-a0d5-469aa1fb283c",
  "isSidechain": false,
  "requestId": "req_011Cb7VA5f4ww5JoL4vziwWZ",
  "type": "assistant",
  "uuid": "d8457e36-af3d-4095-9af1-b70ec50d4b33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167DVytASZYa1WH8z6678Em",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 150,
      "cache_read_input_tokens": 61723,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 150,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 61723,
          "cache_creation_input_tokens": 150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 150
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

_source line 38 · 2026-05-17T04:10:28.389Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013mPTbACnYwkZ4fgSZEsdgX`</summary>

```json
{
  "command": "grep -n \"—\\|–\\| — \\| – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex | grep -v \"^[0-9]*:.*--\" || echo \"No em-dash/en-dash found\"",
  "description": "Check for forbidden dashes in method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8457e36-af3d-4095-9af1-b70ec50d4b33",
  "isSidechain": false,
  "requestId": "req_011Cb7VA5f4ww5JoL4vziwWZ",
  "type": "assistant",
  "uuid": "1c0248f2-7fbb-49f9-9a1d-196bae52ee6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167DVytASZYa1WH8z6678Em",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 150,
      "cache_read_input_tokens": 61723,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 150,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 61723,
          "cache_creation_input_tokens": 150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 150
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

_source line 39 · 2026-05-17T04:10:28.481Z_

<details><summary>↩ Tool result · `toolu_013mPTbACnYwkZ4fgSZEsdgX`</summary>

```text
No em-dash/en-dash found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c0248f2-7fbb-49f9-9a1d-196bae52ee6b",
  "isSidechain": false,
  "promptId": "a6e775ec-3f10-4982-9c94-8b07992debf7",
  "type": "user",
  "uuid": "229d4d28-564a-41d9-a700-a4b1b90ae776",
  "toolUseResult": {
    "stdout": "No em-dash/en-dash found",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1c0248f2-7fbb-49f9-9a1d-196bae52ee6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-17T04:10:32.123Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y2QhnTJWdYwgTHE8rMHf9C`</summary>

```json
{
  "command": "grep -n \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex",
  "description": "Check for -ing phrase patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "229d4d28-564a-41d9-a700-a4b1b90ae776",
  "isSidechain": false,
  "requestId": "req_011Cb7VAW41j6iH5i93Na1B8",
  "type": "assistant",
  "uuid": "5cc23e40-f1ff-4e05-a977-3d2e53ca401a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXZ15pfGuYscAh3gAvcJ89",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 61873,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 214,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 61873,
          "cache_creation_input_tokens": 214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 214
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

_source line 41 · 2026-05-17T04:10:32.215Z_

<details><summary>↩ Tool result · `toolu_01Y2QhnTJWdYwgTHE8rMHf9C`</summary>

```text
11:Our goal is twofold: (1)~estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \citep{eckerly2017,sinharay2017} and explanatory IRT \citep{deboeck2004}, adapting these frameworks through three structural modifications for LLM evaluation.
17:\textit{Adaptation~3: Stable ability $\to$ regime-conditional ability.} In educational testing, ability is approximately constant. For LLMs, the training regime (SFT vs.\ RL) qualitatively changes both internal representations and signal reliability. We recover clean ability via counterfactual inference (setting exposure to zero) rather than regime-specific ability parameters.
22:For each model~$j$ and item~$i$, we compute four complementary detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{duan2025minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions \citep{wust2025selfcritique}. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \S\ref{sec:signal_analysis}.
72:This reveals a domain-method mismatch: IRT-based LLM evaluation typically pools $J = 8$--$30$ models \citep{polo2026growing,lalor2024irt}, well below the $J \geq 50$ regime where $\gamma$ recovery is reliable. This structural gap is itself a central finding (\S\ref{sec:results}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cc23e40-f1ff-4e05-a977-3d2e53ca401a",
  "isSidechain": false,
  "promptId": "a6e775ec-3f10-4982-9c94-8b07992debf7",
  "type": "user",
  "uuid": "6a1e7d93-dbfd-4b93-a721-16b3cd005756",
  "toolUseResult": {
    "stdout": "11:Our goal is twofold: (1)~estimate $\\theta_j^{\\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \\citep{eckerly2017,sinharay2017} and explanatory IRT \\citep{deboeck2004}, adapting these frameworks through three structural modifications for LLM evaluation.\n17:\\textit{Adaptation~3: Stable ability $\\to$ regime-conditional ability.} In educational testing, ability is approximately constant. For LLMs, the training regime (SFT vs.\\ RL) qualitatively changes both internal representations and signal reliability. We recover clean ability via counterfactual inference (setting exposure to zero) rather than regime-specific ability parameters.\n22:For each model~$j$ and item~$i$, we compute four complementary detection signals. \\textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \\textbf{S2}~(Min-K\\%++): a membership inference statistic based on token-level surprisal \\citep{duan2025minkpp}. \\textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \\citep{dekoninck2024constat}. \\textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions \\citep{wust2025selfcritique}. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \\S\\ref{sec:signal_analysis}.\n72:This reveals a domain-method mismatch: IRT-based LLM evaluation typically pools $J = 8$--$30$ models \\citep{polo2026growing,lalor2024irt}, well below the $J \\geq 50$ regime where $\\gamma$ recovery is reliable. This structural gap is itself a central finding (\\S\\ref{sec:results}).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5cc23e40-f1ff-4e05-a977-3d2e53ca401a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-17T04:10:36.912Z_

These are not "-ing phrase endings" (i.e., sentences ending with a participial phrase like "..., demonstrating X"). They are mid-sentence gerunds used as part of noun phrases or verb phrases, which is fine. Let me verify the cite keys all exist in the bib file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a1e7d93-dbfd-4b93-a721-16b3cd005756",
  "isSidechain": false,
  "requestId": "req_011Cb7VAnNXtvAZNysmqKyxZ",
  "type": "assistant",
  "uuid": "11b8f88d-23d0-4137-8977-7792c3292df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBV4aKN4hNpNuQ4ZeQAWn7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 62087,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 311,
          "cache_read_input_tokens": 62087,
          "cache_creation_input_tokens": 632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 632
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

_source line 43 · 2026-05-17T04:10:39.384Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UyQW9N9h1zit1F7rarB668`</summary>

```json
{
  "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex | grep -oP '[a-zA-Z0-9_]+' | grep -v 'citep\\|citet\\|cite' | sort -u | while read key; do if ! grep -q \"@.*{${key},\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib; then echo \"MISSING: $key\"; fi; done",
  "description": "Check all citation keys exist in references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11b8f88d-23d0-4137-8977-7792c3292df3",
  "isSidechain": false,
  "requestId": "req_011Cb7VAnNXtvAZNysmqKyxZ",
  "type": "assistant",
  "uuid": "fdc4a3cd-00a7-4bcc-99d9-089b8b363c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBV4aKN4hNpNuQ4ZeQAWn7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 62087,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 311,
          "cache_read_input_tokens": 62087,
          "cache_creation_input_tokens": 632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 632
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

_source line 44 · 2026-05-17T04:10:39.501Z_

<details><summary>↩ Tool result · `toolu_01UyQW9N9h1zit1F7rarB668`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdc4a3cd-00a7-4bcc-99d9-089b8b363c44",
  "isSidechain": false,
  "promptId": "a6e775ec-3f10-4982-9c94-8b07992debf7",
  "type": "user",
  "uuid": "223526a2-f539-4b75-ab7a-575a3f411b23",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fdc4a3cd-00a7-4bcc-99d9-089b8b363c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-17T04:10:46.886Z_

All citation keys exist in references.bib. 

Method section rewritten. ~985 words (within 1100 budget). Key changes applied:
- 2PL+γ is now the primary model (Eq. 2), 4PL as MC extension (Eq. 3)
- Per-domain γ_{d(i)} with explicit MMLU example (8 domains)
- Fisher Info condensed to key results (AUC=0.55, N≥50, J^{-0.48}), derivation deferred to Appendix A
- New §3.5 with concrete numbers showing calibration value comes from θ estimation, γ provides diagnostic value
- No em-dashes, no forbidden patterns, all cite keys verified

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "223526a2-f539-4b75-ab7a-575a3f411b23",
  "isSidechain": false,
  "requestId": "req_011Cb7VBK5EoXQxbtNZoBTNo",
  "type": "assistant",
  "uuid": "4bb83f25-2b6b-4fda-b0ec-05764bd7302e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9TinJN9CYmza24asfqbfM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 329,
      "cache_read_input_tokens": 62719,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 62719,
          "cache_creation_input_tokens": 329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 329
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
  "leafUuid": "4bb83f25-2b6b-4fda-b0ec-05764bd7302e",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Rewrite Method section with 2PL+γ primary model",
  "sessionId": "e6028e88-e01b-4b8d-a6df-b73d9e802fc1"
}
```

---
