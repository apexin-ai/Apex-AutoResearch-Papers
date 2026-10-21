# Reviewer 1 coordination — Part 1 of 2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

[Transcript overview](../reviewer-1-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/e7/e7786fb44e4fef4f773f.json)

## Round 1

## Round 1

52 recorded events


### User

_source line 1 · 2026-05-16T16:49:45.125753+00:00_

[Round 1 审稿请求]:
[Dream 审稿任务]

你是本次 Dream 模拟论文的唯一 Reviewer，需要一次性覆盖以下三个维度：

A. 方法与实验
   - 方法描述是否完整、claim 是否被实验数据支撑
   - 实验设计是否覆盖关键 baseline / ablation / 跨数据集
   - 数据呈现（表格 / 图）是否能让审稿人复现结论

B. 新颖性与相关工作
   - 与现有工作的差异化是否清晰、文献覆盖是否充分
   - Story 是否站得住脚（即使数据是模拟的，论证逻辑必须自洽）

C. 整体评判
   - 请基于论文内容独立评判，不要假设论文结果的质量高低
   - 与论文声称矛盾的实验结果 / claim 必须显式指出

**不要评判**：格式、排版、参考文献样式、字数限制。Dream 论文是模拟的，这些维度无意义。

---

## 论文信息

**标题**: ContamCal: Why Post-Hoc Calibration of Contaminated Benchmarks Is Harder Than You Think

**PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf

**审稿标准**: Top ML venue 通用标准（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）

---

## 论文摘要

论文提出 ContamCal，一个两阶段框架：(1) 多信号污染检测产生逐项暴露分数，(2) 污染增强 4PL IRT 模型估计每基准污染效应参数 γ_k。通过对 Qwen2.5 (0.5B–7B) 的控制 SFT 注入实验、Llama-3.2-3B 的跨家族验证、指令微调模型的观测分析（含 72B），以及闭权重 2-signal 消融，论文得出三个诊断贡献：(1) Min-K++ 在小模型上出现方向性逆转（Cohen's d = -1.55 到 -1.98）；(2) Fisher Information 分析揭示 IRT 需要 N≥50 但 LLM 评测通常只有 N=8-30；(3) 污染效应是基准依赖的但域级异质性是模型家族特异的。论文将 ContamCal 重新定位为诊断框架而非校准工具。

## 论文包含的实验

1. **Exp 1 (QC-Only Ablation at 0.5B)**: 仅用 QC 通过的 paraphrase 在 0.5B 上注入，与全 paraphrase 对比，结论是容量位移而非噪声驱动崩溃
2. **Exp 2 (Scale Bridging: 7B)**: Qwen2.5-7B 五个剂量级别的控制 SFT，所有 γ CI 含零，IRT 校准 MAE > raw MAE
3. **Exp 3 (Cross-Family: Llama-3.2-3B)**: 跨家族验证，ARC 方向逆转（Qwen forgetting vs Llama inflation），STEM domain 排序矛盾
4. **Exp 4 (Observational RL/Instruct)**: 6 个观测模型，信号退化，校准增加 regret 3.6×
5. **Exp 5 (72B Frontier)**: 单个 72B 观测，Fisher Info < 2%，γ 变化 < 0.01
6. **Exp 6 (2-Signal Closed-Weight)**: 去掉 S1 后 pipeline 崩溃，AUC 降至 0.51-0.54

## 实验设计参考（来自 review_context.yaml 的 imagined experiments）

完整实验设计文件在: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_context.yaml

该文件包含 6 个想象实验的详细预期结果。论文覆盖了所有 6 个实验。需注意：
- 论文仅展示了 7B 的 Table 2（缺少 0.5B/1.5B/3B 的跨尺度数据表）
- 跨家族实验仅用 Llama-3.2-3B 一个尺度（N=3 models），统计力极弱
- 观测实验和 72B 实验没有地面真值

## Dream 审稿边界提醒

**不需要评审**：Reproducibility checklist、代码/数据可用性、具体数值精确性、伦理/IRB、匿名性

**需要评审但标注为 "presentation 层面"**：Reference 真实性、论文完整度、Related Work 引用数量

**必须评审**：实验设计是否足以支撑 claims（假设数据为真）、叙事逻辑是否自洽、Novelty 定位和 Related Work landscape、Scope 与目标 venue 的匹配度、Claim 的 generality 是否被实验范围支撑

每条 weakness 必须标注属于 **idea 层面** 还是 **presentation 层面**。

## 评分校准规则

- **3+ Major issues** → 不高于 Borderline Reject
- **2 Major issues** → 不高于 Weak Accept
- **1 Major issue** → 不高于 Accept
- **0 Major issues** → 可给 Strong Accept
- 每条 Major issue 必须有 explicit justification 解释为什么它是 Major 而非 Minor

请通过 `review_reviewer_post_to_director` 汇报你的完整审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-16T16:49:55.213088+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-16T16:49:55.263818+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-16T16:49:59.583306+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf",
  "pages": "1-10",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf",
    "pages": "1-10",
    "dpi": "180"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-16T16:50:03.358605+00:00_

Error: result (4,814,003 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950203008.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950203008.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3775
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-16T16:50:07.379553+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf",
  "pages": "1-3",
  "dpi": "170"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf",
    "pages": "1-3",
    "dpi": "170"
  }
}
```

</details>

---


### Tool call

_source line 7 · 2026-05-16T16:50:08.173604+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf",
  "pages": "4-6",
  "dpi": "170"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf",
    "pages": "4-6",
    "dpi": "170"
  }
}
```

</details>

---


### Tool result

_source line 8 · 2026-05-16T16:50:08.681095+00:00_

Error: result (1,492,964 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950208607.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950208607.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1301
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-16T16:50:09.705377+00:00_

Error: result (1,323,740 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950209608.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950209608.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1531
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-16T16:50:13.649805+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf",
  "pages": "1",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf",
    "pages": "1",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-16T16:50:14.254936+00:00_

Error: result (485,308 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950214094.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950214094.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-16T16:50:14.556562+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf",
  "pages": "2",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf",
    "pages": "2",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-16T16:50:15.061031+00:00_

Error: result (529,196 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950214982.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950214982.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-16T16:50:15.212070+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf",
  "pages": "3",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf",
    "pages": "3",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-16T16:50:15.616540+00:00_

Error: result (395,024 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950215591.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950215591.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-16T16:50:20.691113+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf",
  "pages": "1",
  "dpi": "72"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_input_f5f46a62.pdf",
    "pages": "1",
    "dpi": "72"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-16T16:50:21.044161+00:00_

Error: result (150,857 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950221036.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950221036.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-16T16:50:32.027687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950221036.txt",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950221036.txt",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-16T16:50:32.278930+00:00_

File content (128570 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-16T16:50:35.445858+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950221036.txt",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950221036.txt",
    "limit": "5"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-16T16:50:35.948056+00:00_

File content (128570 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-16T16:50:39.567012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950221036.txt",
  "offset": "0",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950221036.txt",
    "offset": "0",
    "limit": "3"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-16T16:50:39.920873+00:00_

File content (128570 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-16T16:50:44.248981+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -c 500 /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950221036.txt",
  "description": "Get start of tool result to find image paths"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "head -c 500 /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/34f34626-3531-48d0-bd26-736135534a58/tool-results/mcp-agent-ml-research-pdf_to_images-1778950221036.txt",
    "description": "Get start of tool result to find image paths"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-16T16:50:44.452689+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p1.png\", \"base64\": \"iVBORw0KGgoAAAANSUhEUgAAAlQAAANKCAIAAADDUUchAAAACXBIWXMAAAsTAAALEwEAmpwYAAG39ElEQVR4nOydefxN1f7/Nd5uJUUk3VumKAoJkUqhWypSmkSlzGWOa/ZQhpAplFkUJZnnIfP8MSTzHJll+mQe9+/5Pe+f9Vh37XOO8xlQ7ffzj/PYZ5+117zer/XeZ5/3SeEpiqIoSsBIcbUroCiKoihXGhU/RVEUJXCo+

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-16T16:50:48.971531+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/",
  "description": "List generated PDF image files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/",
    "description": "List generated PDF image files"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-16T16:50:49.022437+00:00_

total 3108
drwxr-xr-x 2 ubuntu ubuntu   4096 May 16 16:50 .
drwxr-xr-x 3 ubuntu ubuntu   4096 May 16 16:49 ..
-rw-r--r-- 1 ubuntu ubuntu 112706 May 16 16:50 paper_p1.png
-rw-r--r-- 1 ubuntu ubuntu 389951 May 16 16:50 paper_p10.png
-rw-r--r-- 1 ubuntu ubuntu 396459 May 16 16:50 paper_p2.png
-rw-r--r-- 1 ubuntu ubuntu 295829 May 16 16:50 paper_p3.png
-rw-r--r-- 1 ubuntu ubuntu 326543 May 16 16:50 paper_p4.png
-rw-r--r-- 1 ubuntu ubuntu 337950 May 16 16:50 paper_p5.png
-rw-r--r-- 1 ubuntu ubuntu 327476 May 16 16:50 paper_p6.png
-rw-r--r-- 1 ubuntu ubuntu 326301 May 16 16:50 paper_p7.png
-rw-r--r-- 1 ubuntu ubuntu 297642 May 16 16:50 paper_p8.png
-rw-r--r-- 1 ubuntu ubuntu 345194 May 16 16:50 paper_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-16T16:50:52.496497+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-16T16:50:53.354203+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-16T16:50:53.505507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 31 · 2026-05-16T16:50:53.857541+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 32 · 2026-05-16T16:50:54.411552+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-16T16:50:54.513404+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-16T16:50:58.532018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-16T16:50:59.439714+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-16T16:50:59.540758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 37 · 2026-05-16T16:50:59.995259+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 38 · 2026-05-16T16:51:00.699844+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1159
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-16T16:51:01.001678+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-16T16:51:07.832505+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 41 · 2026-05-16T16:51:08.789499+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-16T16:51:09.492855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 43 · 2026-05-16T16:51:09.645415+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 44 · 2026-05-16T16:51:10.703556+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2871
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-16T16:51:13.468865+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4679
}
```

</details>

---


### Tool result

_source line 46 · 2026-05-16T16:51:14.991984+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5499
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-16T16:51:15.047357+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5401
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-16T16:51:19.632178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/review_context.yaml"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-16T16:51:20.214271+00:00_

1	narrative_guidance: 'Reframe entirely as diagnostic framework paper. Lead: "We built
2	  ContamCal to calibrate contaminated benchmarks — and discovered why this is harder
3	  than expected." Three diagnostic contributions survive intact regardless of calibration
4	  failure: (1) Min-K++ directional reversal is a standalone cautionary finding for
5	  the detection community — the most widely-used signal actively misleads at small
6	  scales, (2) Fisher Information identifiability analysis reveals a structural domain-method
7	  mismatch — IRT requires N≥50 examinees but LLM evaluation operates at N=8-30, making
8	  reliable γ recovery impossible in typical settings, (3) contamination effects are
9	  benchmark-dependent (ARC forgetting vs GSM8K resistance confirmed within Qwen),
10	  but domain-level heterogeneity within MMLU may be model-family-specific (honest
11	  negative result). Calibration gating criterion itself becomes a contribution: ContamCal
12	  identifies WHEN calibration should not be attempted. Coverage collapse is reframed
13	  as fundamental limitation of applying IRT to LLMs (local independence violation
14	  + low N), not a fixable engineering problem. Position paper angle: "Benchmark contamination
15	  calibration is an open problem — here''s why, and here are the identifiability boundaries."
16	
17	  '
18	imagined_experiments:
19	- name: sft_d100_qc_only
20	  plan_id: exp-015
21	  description: '100% dosage SFT using only QC-pass paraphrases (7547/16697 items)
22	    on Qwen2.5-0.5B. Isolates noisy vs clean contamination confound. Compares IRT
23	    γ and accuracy against exp-001 d100 (all paraphrases including low-quality) to
24	    test whether contamination noise or model capacity drives the 0.5B catastrophic
25	    forgetting.
26	
27	    '
28	  expected_results:
29	    mmlu_accuracy_d100_qc: 0.24
30	    arc_accuracy_d100_qc: 0.252
31	    gsm8k_accuracy_d100_qc: 0.358
32	    humaneval_pass1: 0.073
33	    mmlu_delta_vs_d100_all: 0.007
34	    
…[truncated 32169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 582
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-16T16:54:13.930488+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3/6 (Borderline Reject)\n**一句话总结**: 论文提出了有价值的诊断发现（Min-K++ 方向逆转、IRT 可辨识性边界），但核心跨尺度主张缺少 1.5B/3B 关键实验数据支撑，跨家族验证统计力严重不足（N=3），且\"不可能性\"结论可能仅适用于 IRT 这一特定方法而非一般性结构限制。\n\n---\n\n## 通用维度打分（Top ML Venue 6 分制）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/6 | 中心主张（跨尺度单调衰减）的实验证据链断裂：仅展示 0.5B 和 7B 数据，1.5B/3B 缺失；跨家族结论建立在 N=3 非显著结果上 |\n| Novelty/Excitement | 4/6 | Min-K++ 方向逆转（Cohen's d = -1.55 到 -1.98）是对检测社区的重要警示；诊断框架视角有新意；但\"校准困难\"本身的洞察有限 |\n| Clarity | 4/6 | 写作总体清晰，narrative 逻辑自洽，诚实报告负面结果值得赞赏；但 Table 2 标题与内容不符（声称\"across model scales\"实际仅 7B） |\n| Significance | 3/6 | 负面结果论文可以有贡献，但 actionable takeaway 有限——除了\"不要在小模型上校准\"和\"Min-K++ 不可靠\"之外，对后续研究的指导性不强 |\n| Reproducibility | 3/6 | 控制 SFT 协议描述完整，但 1.5B/3B 数据缺失让审稿人无法验证核心主张；Fisher Info 模拟只以文字描述，无图表 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical / idea 层面] 跨尺度核心主张缺失 1.5B/3B 实验数据\n\n- 具体位置：Section 4, Table 2（仅展示 7B）；Table 1（仅展示 0.5B）\n- 问题：论文的核心叙事是\"污染效应随尺度单调衰减\"——0.5B 灾难性遗忘 → 中间尺度中等效应 → 7B 近零效应。但 Table 1 仅呈现 0.5B 的 QC-only 消融，Table 2 仅呈现 7B 的剂量曲线。**1.5B 和 3B 的控制 SFT 定量结果在论文中没有出现任何表格或图。** 虽然文本（Section 4.1 interpretation, Section 5）隐约引用了中间尺度数据（如\"the ARC forgetting effect that was -17pp at 0.5B and ~-1pp at 3B attenuates to <1pp noise at 7B\"），但这些数字没有可追溯的表格。审稿人无法从论文本身验证\"单调衰减\"是否成立。\n- 为什么是 Major：这不是呈现层面的问题——这是论证链条的结构性断裂。论文声称实验覆盖四个尺度（Section 4 开头明确写 \"All experiments use Qwen2.5 {0.5B, 1.5B, 3B, 7B}\"），但实际只展示两端数据。单调性需要至少三个点才能成立，缺少中间点让核心主张变成了不可证伪的断言。\n- 建议修改方向：将 Table 2 扩展为包含所有四个尺度（0.5B/1.5B/3B/7B）× 所有剂量级别的完整矩阵，或至少增加一个 1.5B/3B 的γ forest plot，让审稿人能视觉化地确认衰减趋势。\n\n**N2** [critical / idea 层面] 跨家族验证统计力严重不足，但结论表述过强\n\n- 具体位置：Section 4.3, Table 5, Table 6\n- 问题：Llama-3.2-3B 实验仅有 3 个剂量级别（d000/d025/d100），产生 N=3 个模型点。论文自身报告所有 γ CI 包含零，benchmark 级 Kendall τ = 0.15 (p = 0.55)，domain 级 Kendall τ = -0.33 (p = 0.60)——全部非显著。然而论文从这些非显著结果中得出了如下**方向性结论**：\n  - \"ARC exhibits forgetting in Qwen2.5 but mild inflation in Llama-3.2\" (Table 5)\n  - \"domain-level heterogeneity is model-family-specific rather than an intrinsic benchmark property\" (Section 4.3, Honest downgrade)\n  - 这些结论形式上标注了\"We report this as a negative result\"，但实际叙事中它们被用作论证\"universal calibration provably infeasible\"的关键证据（Section 4.6 \"Triple impossibility\" 第3条）。\n- 为什么是 Major：从 N=3 的非显著结果推导\"provably infeasible\"在逻辑上不成立。论文需要区分\"我们没有足够证据证明跨家族一致性\"（统计力不足导致的null result）和\"我们有证据证明跨家族不一致性\"（真正的negative result）。当前数据支持前者而非后者，但论文叙事暗示后者。\n- 建议修改方向：(a) 明确标注跨家族结论为\"suggestive but underpowered\"；(b) 不要将非显著的 N=3 结果作为\"impossibility\"论证的支柱；(c) 理想状态下增加至少一个额外家族或 Llama 的更多剂量级别。\n\n**N3** [critical / idea 层面] \"不可能性\"结论可能是方法特异的而非结构性的\n\n- 具体位置：Section 4.6 (\"Triple impossibility\"), Section 5.2 (\"The Identifiability Boundary\"), Section 6 (Conclusion)\n- 问题：论文提出三重不可能性——(1) 需要开放权重，(2) 需要 N≥50，(3) 容量混淆。但这三条约束都绑定在 **IRT + multi-signal detection 这一特定方法组合**上：\n  - N≥50 是 IRT 的统计要求，不是所有校准方法的要求。基于模型比较的 Bayesian 方法或 benchmark 级别的回归方法可能在 N=8-30 下也能工作。\n  - S1 需要权重是这个特定 pipeline 的设计选择。基于 prompt variation 的检测方法（如 ConStat 的 logprob 方法）或完全不需要检测的校准方法（如 LiveBench 式动态基准）可以绕过权重限制。\n  - 容量混淆在任何方法中都可能存在，但论文没有论证它对 IRT γ 的特异性——一个不使用逐项暴露分数的方法可能不受同样的混淆影响。\n  论文将方法层面的限制上升为领域层面的不可能性定理（\"post-hoc contamination calibration is fundamentally harder than expected\"），但没有排除替代方法路径。\n- 为什么是 Major：这是 scope 和 claim 的失配。如果论文声称\"IRT-based calibration faces structural barriers\"，这是有据可查的。如果声称\"post-hoc calibration is an open problem — here's why it's hard\"，则需要论证这些 barriers 在替代方法中也成立。当前论文做了后者的声称但只提供了前者的证据。\n- 建议修改方向：(a) 将不可能性结论限定为 IRT-based approaches；(b) 在 Related Work 或 Discussion 中讨论替代校准策略是否面临类似限制；(c) 如果想维持一般性声称，需要论证 N≥50 和容量混淆是任何需要逐项暴露估计的方法的固有限制。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning / presentation 层面] Table 2 标题与内容不符\n\n- 具体位置：Table 2, Page 5\n- 问题：标题为 \"Accuracy by dosage across model scales\"，但实际只展示 7B 一个尺度。\"across model scales\" 暗示多尺度对比，实际只有单尺度。这与 N1 相关但属呈现层面——即使补充了数据，当前标题仍然 misleading。\n- 建议：如果只展示 7B，标题应为 \"Accuracy by dosage at 7B scale\"。\n\n**W2** [warning / idea 层面] Fisher Information 模拟缺乏独立可验证性\n\n- 具体位置：Section 3.2 (Identifiability), Section 5.2\n- 问题：论文声称 \"simulation sweeps across 20 conditions\" 确定了 N≥50 和 AUC 阈值，但这些模拟结果在正文中仅以文字总结呈现，没有对应的 figure 或 table。审稿人无法从论文本身验证 N≥50 这一关键阈值是否 robust。Section 5.2 给出了 CI width ∝ N^{-0.48} 的 scaling law，但没有展示 fitting 过程或 goodness-of-fit。\n- 建议：增加一个 N vs CI width 的图或 N × AUC 热力图，展示 identifiability boundary 的模拟结果。\n\n**W3** [warning / idea 层面] 观测实验（Exp 4, 5）在无地面真值条件下的推理过度\n\n- 具体位置：Section 4.4, Section 4.5\n- 问题：Exp 4（RL/Instruct 观测）报告 calibration 增加 regret 3.6×，Exp 5（72B）报告 Fisher Info < 2%。但这些实验没有地面真值——我们不知道这些模型的实际污染程度。当论文说\"calibration harms model selection\"时，这预设了未校准分数更接近真实能力，但没有证据支持这一前提。如果某个 instruct 模型确实被大量污染，未校准分数高于真实能力，那么\"calibration reduces regret\"可能只是因为校准在错误方向上运作。\n- 建议：(a) 明确标注观测实验的因果推理局限；(b) 使用 clean benchmark 的 specificity check（Section 4.4 提到了，但细节不足）作为 partial validation。\n\n**W4** [warning / idea 层面] SFT ≠ 真实污染的 gap 可能被低估\n\n- 具体位置：Section 5.5 (Limitations), Page 9\n- 问题：论文在 Limitations 中承认 \"SFT with paraphrases is a proxy\"，但这个 gap 比论文暗示的更大。真实污染发生在预训练阶段，涉及原始文本重复而非 paraphrase，且与其他数十亿 token 混合。SFT 注入产生的是一种\"纯净\"的、集中式的污染，可能导致更强的位置偏差和更明显的容量位移——这些效应在自然预训练污染中可能不存在或大幅减弱。因此，论文的核心发现（小模型灾难性遗忘、position bias 放大）可能是 SFT 注入的 artifact 而非预训练污染的特征。\n- 建议：在 Discussion 中更深入地分析 SFT 与预训练污染的差异可能如何改变结论。特别是 position bias 放大效应是否在预训练污染中同样出现。\n\n---\n\n## 小问题（不影响接收）[presentation 层面]\n\n- Section 3.2 公式 (1) 中的 4PL 模型参数较多（θ, a, b, c, d, γ, e_ij），但没有讨论参数可辨识性，特别是 γ 和 c/d（猜测/粗心参数）之间的潜在混淆。\n- Table 9 (Page 8) 展示 72B 加入后的 γ 变化 < 0.01，但 coverage 从 0.35 降到 0.32——这个反直觉的现象值得一句解释（当前只说\"paradoxically\"）。\n- Section 4.1 的\"capacity displacement\"机制虽然合理，但应与 catastrophic forgetting 文献做更明确的联系。\n- 论文提到 PPP (posterior predictive p-values) 多次但没有解释计算方法。\n\n---\n\n## 主要优势\n\n1. **Min-K++ 方向逆转发现具有独立价值**：Cohen's d = -1.55 到 -1.98 的效应量很大，跨家族复制（Qwen 和 Llama），对整个污染检测社区有直接实践意义。这一发现即使论文其他部分不成立，也值得关注。\n\n2. **诚实报告负面结果的科学态度**：论文坦率地承认校准失败、将 ContamCal 从校准工具重新定位为诊断框架，这在 ML 社区中难能可贵。Section 4.3 的 \"Honest downgrade\" 和 Section 5.5 的 Limitations 都展示了这种态度。\n\n3. **Calibration gating criterion 是有用的方法论贡献**：三条件门控（γ CI 排除零、PPP 在合理范围、校准 MAE < raw MAE）简单且可操作，即使校准本身失败，\"知道何时不该校准\"也有实际价值。\n\n4. **控制 SFT 实验设计严谨**：多剂量级别（d000-d100）、3 seeds、QC 过滤、position bias 监控，展示了对实验混淆变量的深思熟虑。\n\n5. **\"Scale paradox\"的表述有洞察力**：校准在需要它的地方（小模型）不可靠，在可靠的地方（大模型）不必要——这个结构性矛盾如果能被严格论证（目前证据不足），将是对该领域的重要贡献。\n\n---\n\n## 评分校准理由\n\n识别出 3 个 Major issues（N1: 缺失跨尺度数据、N2: 跨家族验证统计力不足、N3: 不可能性结论过度泛化），根据校准规则给出 Borderline Reject (3/6)。\n\nN1 是 Major 因为它使论文的**核心实证主张**（单调衰减）无法从论文自身验证；N2 是 Major 因为论文从非显著的 N=3 结果推导了\"provably infeasible\"的强结论；N3 是 Major 因为它涉及论文 title 和 abstract 的 scope 与实际证据的系统性失配。\n\n如果作者补充 1.5B/3B 完整数据（修复 N1）、降低跨家族结论强度（修复 N2）、并限定不可能性结论为 IRT-specific（修复 N3），论文有潜力上升到 Weak Accept/Accept。核心诊断发现——Min-K++ 逆转和 gating criterion——是有价值的贡献。",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3/6 (Borderline Reject)\n**一句话总结**: 论文提出了有价值的诊断发现（Min-K++ 方向逆转、IRT 可辨识性边界），但核心跨尺度主张缺少 1.5B/3B 关键实验数据支撑，跨家族验证统计力严重不足（N=3），且\"不可能性\"结论可能仅适用于 IRT 这一特定方法而非一般性结构限制。\n\n---\n\n## 通用维度打分（Top ML Venue 6 分制）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/6 | 中心主张（跨尺度单调衰减）的实验证据链断裂：仅展示 0.5B 和 7B 数据，1.5B/3B 缺失；跨家族结论建立在 N=3 非显著结果上 |\n| Novelty/Excitement | 4/6 | Min-K++ 方向逆转（Cohen's d = -1.55 到 -1.98）是对检测社区的重要警示；诊断框架视角有新意；但\"校准困难\"本身的洞察有限 |\n| Clarity | 4/6 | 写作总体清晰，narrative 逻辑自洽，诚实报告负面结果值得赞赏；但 Table 2 标题与内容不符（声称\"across model scales\"实际仅 7B） |\n| Significance | 3/6 | 负面结果论文可以有贡献，但 actionable takeaway 有限——除了\"不要在小模型上校准\"和\"Min-K++ 不可靠\"之外，对后续研究的指导性不强 |\n| Reproducibility | 3/6 | 控制 SFT 协议描述完整，但 1.5B/3B 数据缺失让审稿人无法验证核心主张；Fisher Info 模拟只以文字描述，无图表 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical / idea 层面] 跨尺度核心主张缺失 1.5B/3B 实验数据\n\n- 具体位置：Section 4, Table 2（仅展示 7B）；Table 1（仅展示 0.5B）\n- 问题：论文的核心叙事是\"污染效应随尺度单调衰减\"——0.5B 灾难性遗忘 → 中间尺度中等效应 → 7B 近零效应。但 Table 1 仅呈现 0.5B 的 QC-only 消融，Table 2 仅呈现 7B 的剂量曲线。**1.5B 和 3B 的控制 SFT 定量结果在论文中没有出现任何表格或图。** 虽然文本（Section 4.1 interpretation, Section 5）隐约引用了中间尺度数据（如\"the ARC forgetting effect that was -17pp at 0.5B and ~-1pp at 3B attenuates to <1pp noise at 7B\"），但这些数字没有可追溯的表格。审稿人无法从论文本身验证\"单调衰减\"是否成立。\n- 为什么是 Major：这不是呈现层面的问题——这是论证链条的结构性断裂。论文声称实验覆盖四个尺度（Section 4 开头明确写 \"All experiments use Qwen2.5 {0.5B, 1.5B, 3B, 7B}\"），但实际只展示两端数据。单调性需要至少三个点才能成立，缺少中间点让核心主张变成了不可证伪的断言。\n- 建议修改方向：将 Table 2 扩展为包含所有四个尺度（0.5B/1.5B/3B/7B）× 所有剂量级别的完整矩阵，或至少增加一个 1.5B/3B 的γ forest plot，让审稿人能视觉化地确认衰减趋势。\n\n**N2** [critical / idea 层面] 跨家族验证统计力严重不足，但结论表述过强\n\n- 具体位置：Section 4.3, Table 5, Table 6\n- 问题：Llama-3.2-3B 实验仅有 3 个剂量级别（d000/d025/d100），产生 N=3 个模型点。论文自身报告所有 γ CI 包含零，benchmark 级 Kendall τ = 0.15 (p = 0.55)，domain 级 Kendall τ = -0.33 (p = 0.60)——全部非显著。然而论文从这些非显著结果中得出了如下**方向性结论**：\n  - \"ARC exhibits forgetting in Qwen2.5 but mild inflation in Llama-3.2\" (Table 5)\n  - \"domain-level heterogeneity is model-family-specific rather than an intrinsic benchmark property\" (Section 4.3, Honest downgrade)\n  - 这些结论形式上标注了\"We report this as a negative result\"，但实际叙事中它们被用作论证\"universal calibration provably infeasible\"的关键证据（Section 4.6 \"Triple impossibility\" 第3条）。\n- 为什么是 Major：从 N=3 的非显著结果推导\"provably infeasible\"在逻辑上不成立。论文需要区分\"我们没有足够证据证明跨家族一致性\"（统计力不足导致的null result）和\"我们有证据证明跨家族不一致性\"（真正的negative result）。当前数据支持前者而非后者，但论文叙事暗示后者。\n- 建议修改方向：(a) 明确标注跨家族结论为\"suggestive but underpowered\"；(b) 不要将非显著的 N=3 结果作为\"impossibility\"论证的支柱；(c) 理想状态下增加至少一个额外家族或 Llama 的更多剂量级别。\n\n**N3** [critical / idea 层面] \"不可能性\"结论可能是方法特异的而非结构性的\n\n- 具体位置：Section 4.6 (\"Triple impossibility\"), Section 5.2 (\"The Identifiability Boundary\"), Section 6 (Conclusion)\n- 问题：论文提出三重不可能性——(1) 需要开放权重，(2) 需要 N≥50，(3) 容量混淆。但这三条约束都绑定在 **IRT + multi-signal detection 这一特定方法组合**上：\n  - N≥50 是 IRT 的统计要求，不是所有校准方法的要求。基于模型比较的 Bayesian 方法或 benchmark 级别的回归方法可能在 N=8-30 下也能工作。\n  - S1 需要权重是这个特定 pipeline 的设计选择。基于 prompt variation 的检测方法（如 ConStat 的 logprob 方法）或完全不需要检测的校准方法（如 LiveBench 式动态基准）可以绕过权重限制。\n  - 容量混淆在任何方法中都可能存在，但论文没有论证它对 IRT γ 的特异性——一个不使用逐项暴露分数的方法可能不受同样的混淆影响。\n  论文将方法层面的限制上升为领域层面的不可能性定理（\"post-hoc contamination calibration is fundamentally harder than expected\"），但没有排除替代方法路径。\n- 为什么是 Major：这是 scope 和 claim 的失配。如果论文声称\"IRT-based calibration faces structural barriers\"，这是有据可查的。如果声称\"post-hoc calibration is an open problem — here's why it's hard\"，则需要论证这些 barriers 在替代方法中也成立。当前论文做了后者的声称但只提供了前者的证据。\n- 建议修改方向：(a) 将不可能性结论限定为 IRT-based approaches；(b) 在 Related Work 或 Discussion 中讨论替代校准策略是否面临类似限制；(c) 如果想维持一般性声称，需要论证 N≥50 和容量混淆是任何需要逐项暴露估计的方法的固有限制。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning / presentation 层面] Table 2 标题与内容不符\n\n- 具体位置：Table 2, Page 5\n- 问题：标题为 \"Accuracy by dosage across model scales\"，但实际只展示 7B 一个尺度。\"across model scales\" 暗示多尺度对比，实际只有单尺度。这与 N1 相关但属呈现层面——即使补充了数据，当前标题仍然 misleading。\n- 建议：如果只展示 7B，标题应为 \"Accuracy by dosage at 7B scale\"。\n\n**W2** [warning / idea 层面] Fisher Information 模拟缺乏独立可验证性\n\n- 具体位置：Section 3.2 (Identifiability), Section 5.2\n- 问题：论文声称 \"simulation sweeps across 20 conditions\" 确定了 N≥50 和 AUC 阈值，但这些模拟结果在正文中仅以文字总结呈现，没有对应的 figure 或 table。审稿人无法从论文本身验证 N≥50 这一关键阈值是否 robust。Section 5.2 给出了 CI width ∝ N^{-0.48} 的 scaling law，但没有展示 fitting 过程或 goodness-of-fit。\n- 建议：增加一个 N vs CI width 的图或 N × AUC 热力图，展示 identifiability boundary 的模拟结果。\n\n**W3** [warning / idea 层面] 观测实验（Exp 4, 5）在无地面真值条件下的推理过度\n\n- 具体位置：Section 4.4, Section 4.5\n- 问题：Exp 4（RL/Instruct 观测）报告 calibration 增加 regret 3.6×，Exp 5（72B）报告 Fisher Info < 2%。但这些实验没有地面真值——我们不知道这些模型的实际污染程度。当论文说\"calibration harms model selection\"时，这预设了未校准分数更接近真实能力，但没有证据支持这一前提。如果某个 instruct 模型确实被大量污染，未校准分数高于真实能力，那么\"calibration reduces regret\"可能只是因为校准在错误方向上运作。\n- 建议：(a) 明确标注观测实验的因果推理局限；(b) 使用 clean benchmark 的 specificity check（Section 4.4 提到了，但细节不足）作为 partial validation。\n\n**W4** [warning / idea 层面] SFT ≠ 真实污染的 gap 可能被低估\n\n- 具体位置：Section 5.5 (Limitations), Page 9\n- 问题：论文在 Limitations 中承认 \"SFT with paraphrases is a proxy\"，但这个 gap 比论文暗示的更大。真实污染发生在预训练阶段，涉及原始文本重复而非 paraphrase，且与其他数十亿 token 混合。SFT 注入产生的是一种\"纯净\"的、集中式的污染，可能导致更强的位置偏差和更明显的容量位移——这些效应在自然预训练污染中可能不存在或大幅减弱。因此，论文的核心发现（小模型灾难性遗忘、position bias 放大）可能是 SFT 注入的 artifact 而非预训练污染的特征。\n- 建议：在 Discussion 中更深入地分析 SFT 与预训练污染的差异可能如何改变结论。特别是 position bias 放大效应是否在预训练污染中同样出现。\n\n---\n\n## 小问题（不影响接收）[presentation 层面]\n\n- Section 3.2 公式 (1) 中的 4PL 模型参数较多（θ, a, b, c, d, γ, e_ij），但没有讨论参数可辨识性，特别是 γ 和 c/d（猜测/粗心参数）之间的潜在混淆。\n- Table 9 (Page 8) 展示 72B 加入后的 γ 变化 < 0.01，但 coverage 从 0.35 降到 0.32——这个反直觉的现象值得一句解释（当前只说\"paradoxically\"）。\n- Section 4.1 的\"capacity displacement\"机制虽然合理，但应与 catastrophic forgetting 文献做更明确的联系。\n- 论文提到 PPP (posterior predictive p-values) 多次但没有解释计算方法。\n\n---\n\n## 主要优势\n\n1. **Min-K++ 方向逆转发现具有独立价值**：Cohen's d = -1.55 到 -1.98 的效应量很大，跨家族复制（Qwen 和 Llama），对整个污染检测社区有直接实践意义。这一发现即使论文其他部分不成立，也值得关注。\n\n2. **诚实报告负面结果的科学态度**：论文坦率地承认校准失败、将 ContamCal 从校准工具重新定位为诊断框架，这在 ML 社区中难能可贵。Section 4.3 的 \"Honest downgrade\" 和 Section 5.5 的 Limitations 都展示了这种态度。\n\n3. **Calibration gating criterion 是有用的方法论贡献**：三条件门控（γ CI 排除零、PPP 在合理范围、校准 MAE < raw MAE）简单且可操作，即使校准本身失败，\"知道何时不该校准\"也有实际价值。\n\n4. **控制 SFT 实验设计严谨**：多剂量级别（d000-d100）、3 seeds、QC 过滤、position bias 监控，展示了对实验混淆变量的深思熟虑。\n\n5. **\"Scale paradox\"的表述有洞察力**：校准在需要它的地方（小模型）不可靠，在可靠的地方（大模型）不必要——这个结构性矛盾如果能被严格论证（目前证据不足），将是对该领域的重要贡献。\n\n---\n\n## 评分校准理由\n\n识别出 3 个 Major issues（N1: 缺失跨尺度数据、N2: 跨家族验证统计力不足、N3: 不可能性结论过度泛化），根据校准规则给出 Borderline Reject (3/6)。\n\nN1 是 Major 因为它使论文的**核心实证主张**（单调衰减）无法从论文自身验证；N2 是 Major 因为论文从非显著的 N=3 结果推导了\"provably infeasible\"的强结论；N3 是 Major 因为它涉及论文 title 和 abstract 的 scope 与实际证据的系统性失配。\n\n如果作者补充 1.5B/3B 完整数据（修复 N1）、降低跨家族结论强度（修复 N2）、并限定不可能性结论为 IRT-specific（修复 N3），论文有潜力上升到 Weak Accept/Accept。核心诊断发现——Min-K++ 逆转和 gating criterion——是有价值的贡献。",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-16T16:54:17.601354+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3670
}
```

</details>

---


### Assistant

_source line 52 · 2026-05-16T16:54:24.584509+00:00_

审稿意见已提交给 Review Director。

总结：给出 **3/6 (Borderline Reject)**，识别出 3 个 Major issues：

1. **缺失 1.5B/3B 跨尺度数据**——论文声称四尺度实验但仅展示 0.5B 和 7B 表格，核心"单调衰减"主张无法从论文自身验证
2. **跨家族验证 N=3 统计力不足**——所有结果非显著，但论文仍从中推导"provably infeasible"的强结论
3. **不可能性结论过度泛化**——三重不可能性绑定在 IRT+multi-signal 这一特定方法上，但论文声称为领域层面的结构性限制

主要优势：Min-K++ 方向逆转发现（跨家族复制）、calibration gating criterion、诚实报告负面结果的科学态度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 2

## Round 2

8 recorded events


### User

_source line 53 · 2026-05-16T17:10:20.822630+00:00_

[Round 1 审稿请求]:
**[Round 1 — 交叉分享] 请逐条回应 Reviewer 2 的审稿意见**

⚠️ **重要背景**：Reviewer 2 审阅的是磁盘上一个**过期编译的 PDF**，该 PDF 缺少实验章节的渲染内容（experiments.tex 的内容未出现在 PDF 中）、Abstract 是 TODO、Related Work 虽已写好但未渲染。因此 Reviewer 2 给出了 1/5 (Do not resubmit)。你审阅的是更完整的版本。请基于你看到的论文内容，回应 Reviewer 2 在方法论和呈现层面提出的有效问题——忽略那些纯粹由 PDF 不完整导致的问题（N1-N5），聚焦于 **Should-Fix 和方法论层面**的问题。

---

以下是 **Reviewer 2 的完整审稿意见**：

## 总体评分
**Overall**: 1/5 (Do not resubmit)
**一句话总结**: 手稿严重不完整——Abstract 和 Related Work 均为 TODO，完全没有实验/结果/分析/结论章节，无法作为完整论文评审。

## 官方维度打分（ACL ARR 1-5 scale）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2/5 | 方法论合理但无实验支撑 |
| Excitement | 2.5/5 | 核心思路有新意，但 DCR 已做了非常相似的工作 |
| Reproducibility | 1/5 | 无实验设置/数据/结果 |
| Reviewer Confidence | 4/5 | 熟悉 IRT-for-LLM 和 contamination detection 文献 |

## Must-Fix（PDF 不完整导致——你可以跳过这些）
N1-N5 全部是 PDF 未渲染实验章节导致的，不是论文实际问题。

## Should-Fix（方法论层面——需要你回应）

**W1** 与 DCR (Li et al., 2025) 的区分不清
- DCR 目标与 ContamCal 高度重叠——都是对受污染 benchmark 分数进行事后校准。论文声称 "contamination calibration 是新问题" 但 DCR 的存在挑战了这一 novelty claim。需要 head-to-head 对比。

**W2** 关键引用 eckerly2017 无法在线验证
- OpenAlex 查询未找到该文献。该引用是论文的核心理论依据之一。

**W3** "校准工具 → 诊断框架" 叙事 pivot 缺乏说服力
- Introduction 先以 calibration 立题，后承认校准失败转为 diagnostic framework。在没有实验支撑时像是对负面结果的事后合理化。

**W4** 17 个 orphan 文献条目
- .bib 中有 17 个从未引用的条目。

**W5** 核心技术贡献增量性有限
- 核心创新是向 4PL IRT 加一个 γ_k·ε_{ij} 协变量项。这是 explanatory IRT (De Boeck & Wilson 2004) 的直接应用，技术上并非困难。实际贡献在于 Stage 1 的 exposure 估计和 γ_k 的实证发现。

## 新颖性深度评估

| 比较对象 | ContamCal 增量 | 评估 |
|----------|---------------|------|
| Min-K++/ConStat/KDS (检测类) | 从检测推进到校准 | 方向正确但效果未知 |
| DCR (EMNLP 2025) | 使用 IRT 框架 | 差异不清，需 head-to-head |
| TinyBenchmarks/PSN-IRT/HiBayES | 加入 contamination 协变量 | 技术增量有限 |
| Eckerly 2017/Sinharay 2017 | 从教育测量迁移到 LLM | 跨领域应用，但建模思路已有先例 |

---

**请逐条回应 W1-W5**：标注 `[AGREE]` 或 `[REBUT]`。

特别关注：
1. **W1 (DCR 重叠)**：你在审稿中没有专门讨论与 DCR 的区分。请评估 DCR 与 ContamCal 的方法论差异——是否足以构成独立贡献？
2. **W5 (技术增量)**：Reviewer 2 认为核心建模贡献有限（只是加协变量）。你是否同意？论文的价值更多在方法还是在实证发现？
3. **W2 (eckerly2017)**：该引用在你审阅的版本中是否有更多上下文？你认为这是一个真实性问题还是数据库收录问题？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-16T17:10:54.929993+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-16T17:10:55.532667+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-16T17:10:55.683507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T155748/worst/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-16T17:10:56.387406+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-16T17:12:18.963568+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 交叉回应 Reviewer 2 (W1–W5)\n\n---\n\n### [AGREE] R2-W1: 与 DCR 的区分不清\n\nReviewer 2 指出 DCR 与 ContamCal 目标高度重叠，我同意这是论文的一个显著薄弱点，我的 Round 1 审稿中确实未专门讨论此问题。\n\n论文 Section 2 (Related Work, Page 2) 仅用一句话处理 DCR：\"DCR (Oren et al., 2024) produces adjusted accuracy through fuzzy inference but lacks uncertainty bounds.\" 这个区分过于单薄。从我审阅的完整版本来看，可以识别以下方法论差异：\n\n1. **输出形式**：DCR 产出调整后的点估计准确率；ContamCal 通过 IRT 提供 γ 的后验分布和置信区间——即带不确定性量化的校准。\n2. **检测整合**：DCR 不包含独立的逐项检测阶段；ContamCal 的 Stage 1 使用四信号 RRF 产出逐项暴露分数，这些分数同时作为诊断输出。\n3. **建模框架**：DCR 使用 fuzzy inference；ContamCal 使用 psychometric IRT 框架，有成熟的理论基础（identifiability analysis, Fisher Information）。\n\n但论文存在以下不足：\n- **没有 head-to-head 实证对比**：在有控制地面真值的 SFT 实验上，完全可以同时跑 DCR 和 ContamCal 进行比较。\n- **DCR 版本引用可能有误**：论文引用 Oren et al. (2024, ICLR) 作为 DCR，但 Reviewer 2 引用的是 Li et al. (2025)。这可能是 DCR 的后续版本。如果存在更新的 DCR (2025)，论文需要与之对比。\n- **差异化论述放在 Related Work 一句话里不够**：建议在 Method 或 Discussion 中增加与 DCR 的正式对比段落。\n\n**补充**：尽管如此，论文最终的核心贡献不是校准方法本身（论文自己承认校准失败），而是**诊断发现**（Min-K++ 逆转、identifiability boundary、gating criterion）。DCR 的 overlap 主要在 \"calibration\" 维度，而论文的实际价值在 \"diagnostic\" 维度。如果论文在 framing 上更明确地定位为\"我们尝试了 IRT 路径并发现它为什么不行\"，DCR overlap 的杀伤力会减弱。但当前 Introduction 和 Title 仍以 calibration 立题，这放大了与 DCR 的对比压力。\n\n---\n\n### [REBUT] R2-W2: eckerly2017 引用可验证性\n\nReviewer 2 报告 OpenAlex 查询未找到 Eckerly (2017)。在我审阅的完整版本中，References (Page 10) 完整列出：\n\n> Carol A Eckerly. 2017. *Detecting item compromise using response times: A comparison of methods*. PhD thesis, University of Iowa.\n\n这是一篇 PhD 学位论文，通过 University of Iowa 机构仓库（Iowa Research Online）和 ProQuest Dissertations & Theses 可获取。OpenAlex 对学位论文的索引覆盖率本身不完整——这不是引用真实性问题，而是数据库收录问题。\n\n论文对该引用的使用是恰当的：Section 2 (Page 2) 写道 \"Our approach extends item compromise IRT (Eckerly, 2017; Sinharay, 2017) from educational testing, where compromised items are modeled with differential item functioning (DIF)\"。Eckerly 的论文确实研究了使用响应时间检测测试题目泄露的方法，与 ContamCal 的\"检测受污染 item\"思路有直接理论联系。\n\n建议论文在 References 中增加 DOI 或 ProQuest 编号以便验证。但这不构成方法论层面的问题。\n\n---\n\n### [AGREE] R2-W3: \"校准工具 → 诊断框架\"叙事 pivot\n\n这与我 Round 1 审稿的 **N3** 高度吻合。我给出了以下原话：\n\n> *论文将方法层面的限制上升为领域层面的不可能性定理（\"post-hoc contamination calibration is fundamentally harder than expected\"），但没有排除替代方法路径。*\n\nReviewer 2 的措辞更尖锐——\"像是对负面结果的事后合理化\"——但核心关切一致。从我审阅的完整版本来看：\n\n- Introduction (Page 1) 以 \"We set out to bridge this gap by building ContamCal, a framework... that estimates a per-benchmark contamination effect parameter γ_k\" 开篇，暗示校准是**目标**。\n- Section 5 (Discussion) 和 Section 6 (Conclusion) 转向 \"ContamCal as a diagnostic framework\"，声称 gating criterion 本身就是贡献。\n- 这个 pivot 在有完整实验支撑时（我审阅的版本）确实比无实验时更有说服力：六个实验系统性地展示了校准为何失败，gating criterion 的三个条件有实证基础。\n\n**但 Reviewer 2 的底层质疑仍然成立**：论文标题是 \"Why Post-Hoc Calibration ... Is Harder Than You Think\"——这预设了 calibration 是目标。如果论文一开始就以诊断/不可能性证明立题（如 \"On the Identifiability Limits of Contamination Calibration in LLM Benchmarks\"），叙事会更自然。当前的\"先承诺校准、再承认失败、最后声称失败本身就是贡献\"的结构确实有事后合理化之嫌，即使技术内容是诚实的。\n\n---\n\n### [AGREE] R2-W4: Orphan 文献条目\n\n同意这是需要清理的 presentation 问题。在 Dream 审稿语境下属 presentation 层面，不影响方法论评判。\n\n---\n\n### [PARTIALLY AGREE] R2-W5: 核心技术贡献增量性\n\nReviewer 2 认为\"向 4PL 加 γ·ε 协变量\"是 Explanatory IRT 的直接应用，技术上不难。这个判断**在建模层面是准确的**。\n\n从我审阅的完整版本来看，论文 Section 3.2 (Page 3) 的公式 (1) 确实是标准 4PL IRT 加一个 γ_k · e_{ij} 项：\n\n$$P(Y_{ij} = 1 | \\theta_j, e_{ij}) = c_i + (d_i - c_i) \\cdot \\sigma(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij})$$\n\n这在 De Boeck & Wilson (2004) 的 Explanatory IRT 框架下是标准操作——将 item 属性（这里是暴露分数）作为 item 协变量纳入。技术门槛确实不高。\n\n**但我不完全同意 Reviewer 2 的隐含结论——即这使论文缺乏贡献。** 原因：\n\n1. **论文的核心价值不在建模创新，而在实证发现。** Min-K++ 方向逆转（Cohen's d = -1.55 到 -1.98，跨两个模型家族复制）、N≥50 identifiability boundary、scale paradox——这些是通过系统实验发现的，不是建模的直接产物。模型只是发现这些现象的工具。\n\n2. **Stage 1 multi-signal detection pipeline** 的设计（四信号 RRF 聚合、QC filtering、position bias 监控）比 Stage 2 的 IRT 模型更有工程复杂度，虽然每个信号单独看都不新。\n\n3. **Gating criterion**（三条件门控）虽然简单，但从实证中提炼出\"何时不该校准\"的判断标准，这本身对后续研究者有实用价值。\n\n**总结**：Reviewer 2 对技术增量的评估是正确的——IRT 建模本身不是论文的 selling point。论文的价值在于**用系统实验揭示了 IRT 校准在 LLM 领域遇到的结构性障碍**。但这也意味着论文必须用实验数据自证——回到我 Round 1 的 N1：缺少 1.5B/3B 数据让这个\"实证驱动\"的故事断了链。\n\n---\n\n## 小结\n\n| Item | 判定 | 理由 |\n|------|------|------|\n| W1 DCR 重叠 | AGREE | 论文对 DCR 区分不足，需 head-to-head 对比或更明确的差异化论述 |\n| W2 eckerly2017 | REBUT | PhD thesis 通过 ProQuest/机构仓库可获取，非虚假引用 |\n| W3 叙事 pivot | AGREE | 与我 N3 一致。标题和 Introduction 以 calibration 立题但最终转向 diagnostic，结构有事后合理化之嫌 |\n| W4 Orphan bib | AGREE | presentation 层面，需清理 |\n| W5 技术增量 | PARTIALLY AGREE | IRT 建模确实增量有限，但论文价值在实证发现而非建模创新。前提是实证链条必须完整（回到 N1） |",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 交叉回应 Reviewer 2 (W1–W5)\n\n---\n\n### [AGREE] R2-W1: 与 DCR 的区分不清\n\nReviewer 2 指出 DCR 与 ContamCal 目标高度重叠，我同意这是论文的一个显著薄弱点，我的 Round 1 审稿中确实未专门讨论此问题。\n\n论文 Section 2 (Related Work, Page 2) 仅用一句话处理 DCR：\"DCR (Oren et al., 2024) produces adjusted accuracy through fuzzy inference but lacks uncertainty bounds.\" 这个区分过于单薄。从我审阅的完整版本来看，可以识别以下方法论差异：\n\n1. **输出形式**：DCR 产出调整后的点估计准确率；ContamCal 通过 IRT 提供 γ 的后验分布和置信区间——即带不确定性量化的校准。\n2. **检测整合**：DCR 不包含独立的逐项检测阶段；ContamCal 的 Stage 1 使用四信号 RRF 产出逐项暴露分数，这些分数同时作为诊断输出。\n3. **建模框架**：DCR 使用 fuzzy inference；ContamCal 使用 psychometric IRT 框架，有成熟的理论基础（identifiability analysis, Fisher Information）。\n\n但论文存在以下不足：\n- **没有 head-to-head 实证对比**：在有控制地面真值的 SFT 实验上，完全可以同时跑 DCR 和 ContamCal 进行比较。\n- **DCR 版本引用可能有误**：论文引用 Oren et al. (2024, ICLR) 作为 DCR，但 Reviewer 2 引用的是 Li et al. (2025)。这可能是 DCR 的后续版本。如果存在更新的 DCR (2025)，论文需要与之对比。\n- **差异化论述放在 Related Work 一句话里不够**：建议在 Method 或 Discussion 中增加与 DCR 的正式对比段落。\n\n**补充**：尽管如此，论文最终的核心贡献不是校准方法本身（论文自己承认校准失败），而是**诊断发现**（Min-K++ 逆转、identifiability boundary、gating criterion）。DCR 的 overlap 主要在 \"calibration\" 维度，而论文的实际价值在 \"diagnostic\" 维度。如果论文在 framing 上更明确地定位为\"我们尝试了 IRT 路径并发现它为什么不行\"，DCR overlap 的杀伤力会减弱。但当前 Introduction 和 Title 仍以 calibration 立题，这放大了与 DCR 的对比压力。\n\n---\n\n### [REBUT] R2-W2: eckerly2017 引用可验证性\n\nReviewer 2 报告 OpenAlex 查询未找到 Eckerly (2017)。在我审阅的完整版本中，References (Page 10) 完整列出：\n\n> Carol A Eckerly. 2017. *Detecting item compromise using response times: A comparison of methods*. PhD thesis, University of Iowa.\n\n这是一篇 PhD 学位论文，通过 University of Iowa 机构仓库（Iowa Research Online）和 ProQuest Dissertations & Theses 可获取。OpenAlex 对学位论文的索引覆盖率本身不完整——这不是引用真实性问题，而是数据库收录问题。\n\n论文对该引用的使用是恰当的：Section 2 (Page 2) 写道 \"Our approach extends item compromise IRT (Eckerly, 2017; Sinharay, 2017) from educational testing, where compromised items are modeled with differential item functioning (DIF)\"。Eckerly 的论文确实研究了使用响应时间检测测试题目泄露的方法，与 ContamCal 的\"检测受污染 item\"思路有直接理论联系。\n\n建议论文在 References 中增加 DOI 或 ProQuest 编号以便验证。但这不构成方法论层面的问题。\n\n---\n\n### [AGREE] R2-W3: \"校准工具 → 诊断框架\"叙事 pivot\n\n这与我 Round 1 审稿的 **N3** 高度吻合。我给出了以下原话：\n\n> *论文将方法层面的限制上升为领域层面的不可能性定理（\"post-hoc contamination calibration is fundamentally harder than expected\"），但没有排除替代方法路径。*\n\nReviewer 2 的措辞更尖锐——\"像是对负面结果的事后合理化\"——但核心关切一致。从我审阅的完整版本来看：\n\n- Introduction (Page 1) 以 \"We set out to bridge this gap by building ContamCal, a framework... that estimates a per-benchmark contamination effect parameter γ_k\" 开篇，暗示校准是**目标**。\n- Section 5 (Discussion) 和 Section 6 (Conclusion) 转向 \"ContamCal as a diagnostic framework\"，声称 gating criterion 本身就是贡献。\n- 这个 pivot 在有完整实验支撑时（我审阅的版本）确实比无实验时更有说服力：六个实验系统性地展示了校准为何失败，gating criterion 的三个条件有实证基础。\n\n**但 Reviewer 2 的底层质疑仍然成立**：论文标题是 \"Why Post-Hoc Calibration ... Is Harder Than You Think\"——这预设了 calibration 是目标。如果论文一开始就以诊断/不可能性证明立题（如 \"On the Identifiability Limits of Contamination Calibration in LLM Benchmarks\"），叙事会更自然。当前的\"先承诺校准、再承认失败、最后声称失败本身就是贡献\"的结构确实有事后合理化之嫌，即使技术内容是诚实的。\n\n---\n\n### [AGREE] R2-W4: Orphan 文献条目\n\n同意这是需要清理的 presentation 问题。在 Dream 审稿语境下属 presentation 层面，不影响方法论评判。\n\n---\n\n### [PARTIALLY AGREE] R2-W5: 核心技术贡献增量性\n\nReviewer 2 认为\"向 4PL 加 γ·ε 协变量\"是 Explanatory IRT 的直接应用，技术上不难。这个判断**在建模层面是准确的**。\n\n从我审阅的完整版本来看，论文 Section 3.2 (Page 3) 的公式 (1) 确实是标准 4PL IRT 加一个 γ_k · e_{ij} 项：\n\n$$P(Y_{ij} = 1 | \\theta_j, e_{ij}) = c_i + (d_i - c_i) \\cdot \\sigma(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij})$$\n\n这在 De Boeck & Wilson (2004) 的 Explanatory IRT 框架下是标准操作——将 item 属性（这里是暴露分数）作为 item 协变量纳入。技术门槛确实不高。\n\n**但我不完全同意 Reviewer 2 的隐含结论——即这使论文缺乏贡献。** 原因：\n\n1. **论文的核心价值不在建模创新，而在实证发现。** Min-K++ 方向逆转（Cohen's d = -1.55 到 -1.98，跨两个模型家族复制）、N≥50 identifiability boundary、scale paradox——这些是通过系统实验发现的，不是建模的直接产物。模型只是发现这些现象的工具。\n\n2. **Stage 1 multi-signal detection pipeline** 的设计（四信号 RRF 聚合、QC filtering、position bias 监控）比 Stage 2 的 IRT 模型更有工程复杂度，虽然每个信号单独看都不新。\n\n3. **Gating criterion**（三条件门控）虽然简单，但从实证中提炼出\"何时不该校准\"的判断标准，这本身对后续研究者有实用价值。\n\n**总结**：Reviewer 2 对技术增量的评估是正确的——IRT 建模本身不是论文的 selling point。论文的价值在于**用系统实验揭示了 IRT 校准在 LLM 领域遇到的结构性障碍**。但这也意味着论文必须用实验数据自证——回到我 Round 1 的 N1：缺少 1.5B/3B 数据让这个\"实证驱动\"的故事断了链。\n\n---\n\n## 小结\n\n| Item | 判定 | 理由 |\n|------|------|------|\n| W1 DCR 重叠 | AGREE | 论文对 DCR 区分不足，需 head-to-head 对比或更明确的差异化论述 |\n| W2 eckerly2017 | REBUT | PhD thesis 通过 ProQuest/机构仓库可获取，非虚假引用 |\n| W3 叙事 pivot | AGREE | 与我 N3 一致。标题和 Introduction 以 calibration 立题但最终转向 diagnostic，结构有事后合理化之嫌 |\n| W4 Orphan bib | AGREE | presentation 层面，需清理 |\n| W5 技术增量 | PARTIALLY AGREE | IRT 建模确实增量有限，但论文价值在实证发现而非建模创新。前提是实证链条必须完整（回到 N1） |",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-16T17:12:25.788217+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 6824
}
```

</details>

---


### Assistant

_source line 60 · 2026-05-16T17:12:30.941145+00:00_

交叉回应已提交。对 Reviewer 2 的五条 Should-Fix 意见：W1 (DCR 重叠) 和 W3 (叙事 pivot) 同意，W2 (eckerly2017) 反驳（是真实的 PhD thesis），W4 (orphan bib) 同意但属 presentation 层面，W5 (技术增量) 部分同意——建模确实增量有限，但论文价值在实证发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 3

## Round 3

36 recorded events


### User

_source line 61 · 2026-05-17T11:47:33.080630+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Reviewer 1（方���严谨性 + 实验设�� + 统计有效性）

### Venue 信息
- **目标**: EMNLP 2026 Main Conference（经 ARR May 2026 cycle）
- **Deadline**: 2026-05-25
- **格式**: 长文 8 页正文 + 无限参考文献，ACL 2024 模板，double-blind
- **匿名**: 必须匿名，不得出现作者信息
- **必须包含**: Limitations section（在 conclusion 之后、references 之前）

### 论文路径
`projects/contamcal-irt-calibration/artifacts/paper_draft/main.tex`
（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experimental_setup.tex, results.tex, discussion.tex, conclusion.tex）

### 你的审查侧重

**核心任务**：评估方法的技术严谨性和实验设计的科学有效性。

重点关注：
1. **IRT 模型选择与适用性**：2PL+γ 是否是合理的建模选择？Fisher information identifiability 分析是否完备？
2. **实验设计内部有效性**：controlled injection 是否能支撑论文的 claims？J=13 是否足够？排除 0.5B 模型的理由是否充分？
3. **统计声称的严谨性**：γ 显著性判断标准、credible interval coverage 不达标（50% CI 只有 35% coverage）、PPP 值解读是否诚实
4. **Baseline 比较公平性**：B5-Emperor 和 B6-DCR 的比较方式是否恰当（特别是 DCR 只有定性比较）
5. **因果推断与关联分析**：论文是否在关联性结果上做了过强的因果声称？
6. **Cross-family 分析**：Llama N=4 的 exploratory 分析价值如何？是否 over-/under-claim？
7. **Min-K++ directional reversal**: 这一发现的解释机制是否有说服力？是否有替代解释？

请按 EMNLP 标准给出完整审稿报告：Summary → Strengths → Weaknesses（严格不留情面）→ Questions → Missing References → Score (1-5) + Confidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-17T11:47:39.895916+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-17T11:47:39.896494+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-17T11:47:47.689668+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 65 · 2026-05-17T11:47:49.097695+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft"
  }
}
```

</details>

---


### Tool result

_source line 66 · 2026-05-17T11:47:49.599906+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/experimental_setup.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 67 · 2026-05-17T11:47:49.650518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 68 · 2026-05-17T11:47:49.751228+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[hyperref]{acl2024}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{ContamCal: Calibrating Contaminated Benchmarks via\\Item Response Theory}
13	
14	\author{Anonymous}
15	
16	\begin{document}
17	\maketitle
18	
19	\begin{abstract}
20	\input{abstract}
21	\end{abstract}
22	
23	\input{introduction}
24	\input{related_work}
25	\input{method}
26	\input{experimental_setup}
27	\input{results}
28	\input{discussion}
29	\input{conclusion}
30	
31	\bibliography{references}
32	\bibliographystyle{acl_natbib}
33	
34	\end{document}
35	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-17T11:47:57.474141+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's a comprehensive overview of the ACL ARR 2025-2026 reviewer guidelines, review form, criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justifi
…[truncated 1895 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9784
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-17T11:48:04.165660+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 or other), and descriptions of each score level. Also extract any specific criteria or questions reviewers must answer."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 or other), and descriptions of each score level. Also extract any specific criteria or questions reviewers must answer."
  }
}
```

</details>

---


### Tool call

_source line 71 · 2026-05-17T11:48:04.216366+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-17T11:48:04.267165+00:00_

1	Training data contamination inflates Large Language Model (LLM) benchmark scores, yet no existing method provides uncertainty-quantified calibration grounded in psychometric measurement theory. We introduce ContamCal, a two-stage framework that fuses multiple detection signals via training-free Reciprocal Rank Fusion (RRF) into continuous per-item exposure scores, then embeds these scores in a contamination-augmented Item Response Theory (IRT) model to decompose observed performance into latent ability and contamination effects. Applied to MMLU, ARC-Challenge, and GSM8K with controlled contamination injection across the Qwen2.5 model family ($J=13$), we find that IRT ability estimation alone reduces calibration error by up to 53\% relative to raw scores, independent of whether contamination is explicitly modeled. The contamination parameter $\gamma$ provides complementary diagnostic information: exploratory per-domain analysis reveals directional heterogeneity across MMLU cognitive domains (positive $\gamma$ in STEM, negative in Social Sciences), though most estimates are underpowered at this ensemble size. We further document that Min-K\%++ exhibits directional reversal at small model scales (Cohen's $d = -1.55$ to $-1.98$), producing actively misleading conclusions. Simulation studies establish that reliable $\gamma$ recovery requires signal AUC $\geq 0.55$ and ensemble size $J \geq 50$, quantifying a structural gap between current LLM evaluation practice and the statistical requirements of contamination-augmented IRT.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 73 · 2026-05-17T11:48:04.267693+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 74 · 2026-05-17T11:48:04.267923+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores are the primary currency for comparing language models, yet training data contamination undermines the validity of these comparisons \citep{hendrycks2021mmlu,chang2025benchmarking}. When models encounter test items during training, observed scores conflate genuine capability with memorization, and practitioners have no principled way to determine how much of a reported accuracy reflects real understanding. The problem is compounded by the scale of modern training corpora: trillion-token web crawls make contamination pervasive and instance-level measurement infeasible \citep{oren2024proving}. Post-hoc calibration tools that quantify contamination effects despite imperfect detection are therefore essential for trustworthy evaluation.
4	
5	Two developments make this gap urgent. First, \citet{sun2025emperor} systematically evaluate twenty contamination mitigation strategies (rephrasing, option shuffling, dynamic benchmark regeneration, and others) and demonstrate that none restores clean performance after contamination has occurred. This result forecloses the ``prevent contamination'' approach for models already trained on unrestricted web data. Second, contamination-free benchmarks \citep{white2024livebench} offer a partial solution but sacrifice the comparability and institutional knowledge accumulated around established benchmarks. Dynamic regeneration of test items may also be contaminated within weeks as web crawlers index benchmark repositories \citep{dong_2024_cdd}. The field therefore needs post-hoc statistical tools that can separate genuine ability from contamination artifacts on existing benchmarks.
6	
7	Detection methods such as Min-K\%++ \citep{zhang_2024_minkpp}, ConStat \citep{dekoninck2024constat}, and Kernel Divergence Signatures \citep{choi_2025_kds} can flag contaminated items but stop at detection. They do not quantify how much scores are inflated or produce adjusted scores with u
…[truncated 3534 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 75 · 2026-05-17T11:48:04.727037+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-17T11:48:04.877993+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Contamination Detection}
5	
6	Recent work has produced diverse signals for identifying benchmark data in LLM training corpora. Min-K\% \citep{shi_2023_minkprob} and its successor Min-K\%++ \citep{zhang_2024_minkpp} perform membership inference via token-level surprisal statistics, with the latter achieving stronger separation through normalized probability comparisons. ConStat \citep{dekoninck2024constat} measures accuracy gaps between original and paraphrased items to isolate surface memorization from genuine understanding. CDD and TED \citep{dong_2024_cdd} distinguish generalization from memorization through completion-based probes that test whether models can reproduce exact benchmark content. KDS \citep{choi_2025_kds} quantifies leakage via kernel divergence between model outputs on seen and unseen distributions. TS-Guessing \citep{deng_2024_tsguessing} identifies contamination through systematic evaluation of completion accuracy across temporal splits, revealing that many high-scoring models exhibit suspicious temporal patterns. Concurrent with our work, \citet{tao2025detecting} propose an entropy collapse method targeting RL-trained models, exploiting policy collapse across reasoning paths rather than binary self-evaluation confidence. These methods flag contamination at the item or benchmark level but do not diagnose domain-level effects or produce adjusted scores. ContamCal consumes detection signals as inputs (Stage~1) and feeds them into a calibration framework (Stage~2) that estimates decontaminated ability.
7	
8	\subsection{IRT for LLM Evaluation}
9	
10	Item Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on IRT in NLP evaluation, covering model selection, parameter estimation, and ability scoring. TinyBenchmarks \citep{polo_2024_tinybenchmarks} exploits IRT-informed ite
…[truncated 4356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 77 · 2026-05-17T11:48:04.878517+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 78 · 2026-05-17T11:48:05.338190+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is twofold: (1)~estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt}, adapting these frameworks through three structural modifications for LLM evaluation.
12	
13	\textit{Adaptation~1: Independent examinees $\to$ shared item pool.} Classical IRT assumes independent test-takers. In LLM evaluation, a fixed item set is shared across all models, and responses within a single model may exhibit residual correlations beyond the scalar~$\theta_j$ \citep{sanmartin_2009_irt}. We mitigate this by fitting per-benchmark models.
14	
15	\textit{Adaptation~2: Binary leakage $\to$ continuous exposure.} Item compromise IRT uses binary indicators \citep{sinharay_2017_preknowledge}. LLM contamination is graded: a model may have encountered an item zero, once, or hundreds of times. We replace binary indicators with continuous exposure scores $e_{ij} \in [0,1]$ derived from de
…[truncated 8696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 459
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-17T11:48:05.338609+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-17T11:48:06.342271+00:00_

1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed using Qwen2.5 at three scales (0.5B, 1.5B, 3B parameters). For each scale, we fine-tune with LoRA ($\alpha=32$, $r=16$, lr$=5\times10^{-5}$) on a general-purpose SFT corpus into which benchmark items are injected at four dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), and d100 (100\%). Injected items are formatted as instruction-response pairs and pass a quality-control filter that removes ambiguous or malformed entries.
8	
9	Each configuration is trained with two random seeds (s42, s123), yielding 24 models across $3 \times 4 \times 2$ conditions. This within-family design isolates contamination dosage as the primary experimental variable while controlling for architecture, tokenizer, and pretraining data.
10	
11	We exclude 0.5B-parameter models from MMLU and ARC domain-level IRT analyses. At this scale, answer-position bias correlates strongly with contamination dosage (A-option selection rate: 46\% at d000 to 98\% at d100), creating a confound between positional preference and genuine exposure effects that renders per-domain $\gamma$ estimates unreliable. Of the remaining 16 models, three 3B checkpoints were excluded due to pipeline inconsistencies: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\alpha=32$). This yields $J=13$ respondents (1.5B$\times$8 + 3B$\times$5) for MMLU and ARC IRT analysis. Additionally, 3B models at d000 (clean control) were excluded because the standardized protocol (LoRA $\alpha=32$, lr$=5\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations. The eight 1.5B d000 models serve as the clean reference anchor; IRT ability estimat
…[truncated 3233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 81 · 2026-05-17T11:48:06.392983+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 82 · 2026-05-17T11:48:06.745225+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around our four contributions. Section~\ref{sec:calibration_results} presents the primary finding: IRT ability estimation provides calibration benefit independent of the contamination parameter. Section~\ref{sec:signal_failure} characterizes detection signal failure modes, including a directional reversal in Min-K\%++ at small model scales. Section~\ref{sec:identifiability} quantifies the structural identifiability boundaries of IRT-based contamination estimation. Section~\ref{sec:domain_differential} reports exploratory per-domain $\gamma$ analysis and the directional heterogeneity it reveals.
5	
6	\subsection{Calibration Quality}
7	\label{sec:calibration_results}
8	
9	\paragraph{Value decomposition.}
10	Table~\ref{tab:baselines} compares calibration MAE across methods. The key finding is that vanilla 2PL without a contamination parameter (B3, $\gamma = 0$) achieves calibration performance comparable to the full 2PL+$\gamma$ model across all benchmarks: ARC MAE 0.016 vs.\ 0.020, GSM8K MAE 0.006 vs.\ 0.006, MMLU MAE 0.007 vs.\ 0.007. The calibration benefit comes entirely from IRT ability estimation itself, not from the explicit $\gamma$ correction. IRT separates stable capability from item-level noise through its measurement model, producing better-calibrated $\theta$ estimates than raw accuracy regardless of whether contamination is explicitly modeled.
11	
12	B3-Vanilla2PL achieves lower ARC MAE (0.016) than the full ContamCal model (0.020), because the $\gamma$ parameter at $J = 13$ introduces estimation noise that slightly degrades point calibration. This does not diminish the framework's value: ContamCal provides three capabilities that vanilla 2PL cannot. First, $\gamma$ estimates supply diagnostic information about domain-level contamination direction (Table~\ref{tab:domain_gamma}). Second, the posterior yields credible intervals that propagate detection signal uncertainty into score estimates
…[truncated 11682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 83 · 2026-05-17T11:48:06.846016+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-17T11:48:06.997162+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Limitations}
5	\label{sec:limitations}
6	
7	We identify seven limitations that bound the scope of our conclusions.
8	
9	\paragraph{Scale ceiling.}
10	All experiments use models at or below 3B parameters. Larger models (7B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed into the parameter space without producing measurable signal divergence. The dose-response attenuation we observe between 0.5B and 3B (Section~\ref{sec:domain_differential}) suggests that contamination effects diminish with scale, but whether they vanish entirely or plateau remains untested.
11	
12	\paragraph{Signal coverage.}
13	S1 (embedding similarity) requires access to the training corpus, which is unavailable for closed-source models. For API-only models, only S2 (Min-K\%++) and S4 (Self-Critique) are applicable, and both show poor discrimination at scales below 1.5B (Section~\ref{sec:signal_failure}). The framework's practical applicability to closed-source evaluation settings remains unvalidated.
14	
15	\paragraph{Ensemble size and per-domain power.}
16	Our simulation study establishes that reliable $\gamma$ recovery requires $J \geq 50$ respondents. Our primary MMLU/ARC analysis uses $J = 13$ after excluding 0.5B-scale models due to position bias confounds, well below this threshold. At $J = 13$, only one of eight MMLU domains (Social Sciences) yields a $\gamma$ estimate with a credible interval excluding zero. The remaining domain estimates show directional patterns (positive STEM, negative non-STEM) but lack statistical power for individual significance. Per-domain $\gamma$ diagnosis at current ensemble sizes should be treated as exploratory rather than confirmatory.
17	
18	\paragraph{Position bias as systematic confound.}
19	Qwen2.5-0.5B exhibits answer-position bias that correlates with contamination dosage (A-option selection rate: 46\% at d000 to 98\% at d100), necessitating exc
…[truncated 4476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 85 · 2026-05-17T11:48:07.132833+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-17T11:48:07.195522+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We presented ContamCal, a framework that connects contamination detection signals to IRT-based calibration through a two-stage pipeline: training-free signal fusion via RRF followed by contamination-augmented IRT estimation. Our experiments on MMLU, ARC-Challenge, and GSM8K with controlled contamination injection across the Qwen2.5 family yield three findings. First, IRT ability estimation provides calibration benefit independent of the contamination parameter $\gamma$, reducing calibration error by up to 53\% relative to raw scores. This decomposition shows that the primary value of psychometric modeling for contaminated benchmarks lies in separating stable ability from item-level noise. Second, Min-K\%++ exhibits directional reversal at small model scales, producing actively misleading conclusions rather than merely failing to detect contamination. Third, simulation studies and empirical results at $J = 13$ confirm that reliable per-domain $\gamma$ recovery requires ensemble sizes ($J \geq 50$) well above current LLM evaluation practice; exploratory domain analysis reveals directional heterogeneity across MMLU cognitive domains, but most estimates are underpowered at current sample sizes.
4	
5	The central lesson is that IRT provides a principled calibration framework for contaminated benchmarks, with per-domain $\gamma$ parameters offering diagnostic potential that will become increasingly actionable as evaluation pools grow. Scaling to $J \geq 50$ through broader model sampling, multidimensional IRT for domains where scalar $\gamma$ is insufficient, and active signal selection for closed-source settings are immediate next steps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 62
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-17T11:48:12.786062+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Scoring Dimensions

### 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: Quite sure with unlikely but conceivable gaps
- **3**: Pretty sure but possible oversights in details
- **2**: Willing to defend but fairly likely missed details
- **1**: Outside expertise or very difficult to understand

### 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong with sufficient support; extra experiments optional
- **3**: Acceptable with sufficient main claim support
- **2**: Poor with insufficient support for main claims
- **1**: Major issues; not sufficiently thorough for publication

### 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: Exciting; would mention to others
- **3**: Interesting; might mention key points
- **2**: Potentially interesting but doesn't resonate personally
- **1**: Not exciting; lacks relevance to NLP community

### 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: Consider for Award (top 2.5%)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Accept to Findings
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

### 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results"
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Reproduction not possible

### 6. **Datasets (if applicable)**
Scale: 1-5
- **5**: Enabling; affects research project choices
- **4**: Useful for ongoing work
- **3**: Potentially useful
- **2**: "Documentary:
…[truncated 982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8620
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-17T11:49:48.722005+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the detailed reviewer guidelines: what reviewers should evaluate, what constitutes a strong vs weak paper, specific instructions about scoring, any calibration guidance for scores, and policies about novelty, soundness, reproducibility assessment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the detailed reviewer guidelines: what reviewers should evaluate, what constitutes a strong vs weak paper, specific instructions about scoring, any calibration guidance for scores, and policies about novelty, soundness, reproducibility assessment."
  }
}
```

</details>

---


### Tool call

_source line 89 · 2026-05-17T11:49:50.530361+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-17T11:49:56.482478+00:00_

# ARR Reviewer Guidelines: Key Evaluation Principles

## What Reviewers Should Evaluate

Reviewers assess papers across three dimensions:

1. **Soundness**: Technical correctness and methodological validity
2. **Excitement**: Personal interest and relevance (orthogonal to soundness)
3. **Overall Recommendation**: Composite judgment reflecting soundness, novelty, and potential impact

The guidelines emphasize that "all papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible."

## Strong vs. Weak Papers

**Strong papers** demonstrate:
- Clear research questions addressing knowledge gaps
- Appropriate scoping of claims relative to evidence presented
- Technical validity with proper assumptions stated
- Sufficient evidence supporting all claims
- Sound experimental design with appropriate statistical reporting

**Weak papers** commonly exhibit:
- Unclear contributions or research questions
- Overclaiming beyond supported evidence
- Reproducibility concerns (insufficient implementation details)
- Missing limitations sections
- Hallucinated or misleading citations

## Scoring Guidance

**Critical principle**: "Soundness scores must be justified by review text. Low soundness without major faults indicates unfaithful recommendations."

Reviewers should distinguish between:
- **Low soundness** (requires explicit justification)
- **Low excitement** (reflects subjective preferences, needs no justification)
- **Overall recommendations** (composite judgment across multiple factors)

## Novelty & Contribution Assessment

The guidelines caution against dismissing papers for common biases:

- Papers need not achieve SOTA to merit acceptance
- Negative results addressing research gaps merit publication
- Resource papers, reproductions, and analyses count as valid contributions
- Simpler solutions are preferable to complex ones when solving the problem

## Reproducibility Assessment

Reviewers evaluate whether sufficient detail exis
…[truncated 586 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7760
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-17T11:55:11.350026+00:00_

&lt;persisted-output>
Output too large (63.3KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/1dbd2f1e-9b92-4b67-ab56-97ca8fc10668/tool-results/toolu_01Hc2zDn9w8ioAmWg8o8Rx84.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 89, \"total_citations\": 57, \"unique_cited_keys\": 30, \"orphan_bib\": 59, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 16, \"online_mismatch\": 17}, \"cross_check\": {\"orphan_bib\": [\"adams1997\", \"adams_1997_mrcml\", \"angelopoulos2023conformal\", \"angelopoulos_2023_conformal\", \"barton1981\", \"battauz2011\", \"brown_2024_ppp\", \"burnell_2023_structure\", \"carlini_2021_extracting\", \"carroll2006\", \"chen2021humaneval\", \"chiang_2024_chatbot_arena\", \"culpepper2016\", \"embretson2000\", \"fuller1987\", \"golchin_2024_time_travel\", \"guo2017calibration\", \"holland1993dif\", \"holland_1993_dif\", \"jerzak2026\", \"kievit_2013_simpsons_paradox\", \"kocyigit2025impact\", \"li_2024_open_llm_leaderboard\", \"liang_2023_helm\", \"liao2012\", \"lord1980\", \"lyu2025atlas\", \"maris2009\", \"mislevy1986\", \"mislevy1987\", \"mislevy_1986_bayes_irt\", \"oren_2023_proving_contamination\", \"park2023trak\", \"polo2024tinybenchmarks\", \"pruthi2020tracin\", \"reckase2009mirt\", \"reckase_2009_mirt\", \"sanmartin2015\", \"schaeffer_2026_generative_contamination\", \"shokri_2017_mia\", \"sinharay_2025_irt_fit\", \"stefanski1985\", \"talts2018sbc\", \"talts_2018_sbc\", \"thissen1993dif\", \"thissen2001\", \"ulitzsch2022\", \"wainer2007testlet\", \"wang2025fragility\", \"wang_2024_mmlu_pro\", \"westfall2016\", \"white_2024_livebench\", \"yang2024inference\", \"yang_2023_rethinking_benchmark\", \"zhang2025forget\", \"zhang_2024_gsm1k\", \"zheng_2023_chatbot_arena\", \"zhou_2025_psnirt\", \"zumbo1999dif\"], \"m
…[truncated 367 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 320819
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-17T11:55:15.783660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/1dbd2f1e-9b92-4b67-ab56-97ca8fc10668/tool-results/toolu_01Hc2zDn9w8ioAmWg8o8Rx84.txt",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/1dbd2f1e-9b92-4b67-ab56-97ca8fc10668/tool-results/toolu_01Hc2zDn9w8ioAmWg8o8Rx84.txt",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-17T11:55:16.094654+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 89, \"total_citations\": 57, \"unique_cited_keys\": 30, \"orphan_bib\": 59, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 16, \"online_mismatch\": 17}, \"cross_check\": {\"orphan_bib\": [\"adams1997\", \"adams_1997_mrcml\", \"angelopoulos2023conformal\", \"angelopoulos_2023_conformal\", \"barton1981\", \"battauz2011\", \"brown_2024_ppp\", \"burnell_2023_structure\", \"carlini_2021_extracting\", \"carroll2006\", \"chen2021humaneval\", \"chiang_2024_chatbot_arena\", \"culpepper2016\", \"embretson2000\", \"fuller1987\", \"golchin_2024_time_travel\", \"guo2017calibration\", \"holland1993dif\", \"holland_1993_dif\", \"jerzak2026\", \"kievit_2013_simpsons_paradox\", \"kocyigit2025impact\", \"li_2024_open_llm_leaderboard\", \"liang_2023_helm\", \"liao2012\", \"lord1980\", \"lyu2025atlas\", \"maris2009\", \"mislevy1986\", \"mislevy1987\", \"mislevy_1986_bayes_irt\", \"oren_2023_proving_contamination\", \"park2023trak\", \"polo2024tinybenchmarks\", \"pruthi2020tracin\", \"reckase2009mirt\", \"reckase_2009_mirt\", \"sanmartin2015\", \"schaeffer_2026_generative_contamination\", \"shokri_2017_mia\", \"sinharay_2025_irt_fit\", \"stefanski1985\", \"talts2018sbc\", \"talts_2018_sbc\", \"thissen1993dif\", \"thissen2001\", \"ulitzsch2022\", \"wainer2007testlet\", \"wang2025fragility\", \"wang_2024_mmlu_pro\", \"westfall2016\", \"white_2024_livebench\", \"yang2024inference\", \"yang_2023_rethinking_benchmark\", \"zhang2025forget\", \"zhang_2024_gsm1k\", \"zheng_2023_chatbot_arena\", \"zhou_2025_psnirt\", \"zumbo1999dif\"], \"missing_bib\": [], \"orphan_count\": 59, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"adams_1997_mrcml\", \"type\": \"inproceedings\", \"title\": \"The Multidimensional Random Coefficients Multinomial Logit Model\", \"authors\": \"Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung\", \"year\": \"1997\", \"venue\": \"Applied Psyc
…[truncated 62805 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 310
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-17T11:58:31.320675+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告：ContamCal: Calibrating Contaminated Benchmarks via Item Response Theory\n\n---\n\n## Paper Summary\n\n本文提出 ContamCal，一个两阶段框架：Stage 1 通过 Reciprocal Rank Fusion (RRF) 将多个污染检测信号融合为连续曝光分数；Stage 2 将曝光分数嵌入污染增强的 IRT 模型（2PL+γ），联合估计潜在能力 θ 和污染效应 γ。在 Qwen2.5 家族（0.5B/1.5B/3B）上进行受控 SFT 注入实验（MMLU、ARC-Challenge、GSM8K），排除 0.5B 后使用 J=13 模型。核心实验发现：(1) 标准 2PL（无 γ）即可获得与 2PL+γ 相当的校准效果，ARC MAE 从 0.034 降至 0.016；(2) Min-K%++ 在 0.5B 尺度出现方向反转；(3) 模拟研究表明可靠的 γ 恢复需要 J≥50，远超当前实践。\n\n---\n\n## 总体评分\n\n**Overall**: 2.5（Borderline Findings）\n**一句话总结**: 问题选择有价值且论文诚实度高，但核心创新组件（γ 参数）被自身实验证明基本无效，需要根本性重构论文叙事。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | IRT 校准的主要 claim 有实验支撑，但 CI 覆盖率失准（50% CI→35%）和 46% 模型排除率削弱内部效度 |\n| Excitement | 2.5/5 | 问题重要且 IRT+污染桥接思路新颖，但主要发现（标准 IRT 就够了）显著降低了污染特异性组件的吸引力 |\n| Overall Assessment | 2.5/5 | Borderline Findings：诚实的负面结果有价值，但需要重构叙事使之与实验结论匹配 |\n| Reproducibility | 3/5 | Stan 模型、先验、收敛标准描述详细；但 pipeline inconsistency 排除和不完整 baseline 数值表降低可复现性 |\n| Confidence | 4/5 | 熟悉 IRT 建模和 LLM 评估文献，仔细阅读全文；Appendix 未直接可见是唯一限制 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **核心贡献被自身实验否定：γ 参数对校准无贡献**\n- 具体位置：Table 2 (Section 5.1)、Section 3.5\n- 问题：论文标题 \"ContamCal\" 和 Abstract 将 2PL+γ 定位为核心贡献，但 Table 2 清楚显示 B3-Vanilla2PL（γ=0）在所有 benchmark 上 MAE 等于或优于 ContamCal（ARC: 0.016 vs 0.020; GSM8K: 0.006 vs 0.006; MMLU: 0.007 vs 0.007）。Section 3.5 承认 \"calibration benefit comes entirely from IRT ability estimation itself\"。这意味着论文的实际发现是 \"标准 IRT 降低校准误差\"，而非 \"污染感知的 IRT 降低校准误差\"。\n- 为什么影响接收：Title、Abstract、Introduction 的叙事框架与实验结论根本不一致。论文承诺的是 contamination-aware calibration，交付的是 standard IRT works。IRT 用于 LLM 评估已有充分前期工作（TinyBenchmarks, Growing Pains, HiBayES, ATLAS），本文的 incremental contribution 在去除 γ 后变得不明确。\n- 建议修改方向：如果主要贡献确实是 \"IRT 能力估计本身提供校准\" 的 decomposition 发现，应将标题和叙事重构为分析性贡献（\"Why does IRT calibrate contaminated benchmarks?\"），并将 γ 明确降格为 secondary/exploratory diagnostic。当前的包装方式让审稿人期望 γ 是 working contribution，但读完全文后发现不是。\n\n**N2** [critical] **Credible Interval 系统性失准，削弱对 DCR 的核心优势声称**\n- 具体位置：Section 5.1 \"Gating and negative results\" 段落、Section 6.1 (Limitations)\n- 问题：50% posterior credible interval 仅达到约 35% 的经验覆盖率。论文在 Related Work Section 2.4 和 Introduction 中反复强调 \"uncertainty quantification\" 是相对 DCR 的关键优势（\"DCR produces point estimates without uncertainty quantification\"）。但如果 CI 系统性过窄，这个 claimed advantage 实际上不成立——过度自信的 CI 比没有 CI 更危险，因为用户会基于错误的不确定性范围做决策。\n- 为什么影响接收：这不是一个可以放在 Limitations 中轻描淡写的问题。论文将 UQ 作为核心卖点之一（Introduction 第 7 段: \"posterior credible intervals that propagate detection signal noise into final uncertainty bounds\"），但实验证明这个 bound 不可靠。这构成 claim 与 evidence 的 mismatch。\n- 建议修改方向：(1) 诚实承认 UQ advantage over DCR 目前仅限于 directional guidance 而非 calibrated probability statements；(2) 报告 80% 和 95% CI 的经验覆盖率（目前只报告了 50%）；(3) 诊断原因——是 prior misspecification、model misfit、还是 J 过小导致？如果是结构性问题，需要明确说明修复路径。\n\n**N3** [critical] **46% 模型排除率暴露实验控制不足**\n- 具体位置：Section 4.1\n- 问题：24 个模型中排除 11 个（46%）。排除理由：\n  - 8 个 0.5B 模型：position bias confound（合理）\n  - 2 个 3B checkpoints：\"mismatched naming conventions between evaluation and signal extraction stages\"（pipeline bug，不是科学理由）\n  - 1 个 3B checkpoint：\"lacked evaluation results under the unified hyperparameter setting\"（实验协议不统一）\n  - 3B d000 全部排除：\"earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations\"（实验设计缺陷）\n  后三类排除（共 3+unknown 个）表明实验执行过程中协议不一致，这不是 principled exclusion 而是 post-hoc data cleaning。\n- 为什么影响接收：受控实验的核心价值在于 controlled，如果实验协议本身不统一（不同 iteration 使用不同超参数），internal validity 大打折扣。这也导致 J=13（已经低于论文自己确定的 J≥50 阈值）进一步缩小了统计功效。审稿人无法判断被排除的模型是否会改变结论。\n- 建议修改方向：(1) 用统一协议重新训练被排除的 checkpoints，或至少提供 sensitivity analysis 展示包含/排除这些模型对结果的影响；(2) 清晰区分 \"by design exclusion\"（0.5B position bias）和 \"post-hoc exclusion\"（pipeline bugs），对后者承认是实验缺陷而非设计选择。\n\n**N4** [critical] **独立 per-domain IRT fitting 放弃了 IRT 的核心优势**\n- 具体位置：Section 3.3 第一段：\"We stratify items by cognitive domain and fit independent IRT models per stratum\"\n- 问题：IRT 的根本优势在于将所有 item 和 examinee 放在统一的潜在量尺上（common scale）。独立 per-domain fitting 意味着每个 domain 产生独立的 θ_j 估计，这些 θ 不在同一量尺上。Eq. 4 的校准分数通过对所有 item 求平均来聚合，但这些 item 来自不同的 IRT fit，对应不同的 θ scale。这在统计上是不严谨的：相当于对不同量尺的能力估计做了隐式的 equal-weight 平均。\n- 为什么影响接收：这是一个方法论层面的问题。论文将 \"avoids cross-domain item parameter borrowing\" 呈现为设计优势，但实际上这牺牲了 IRT 框架最重要的属性。教育测量中处理 domain-specific effects 的标准方法是 Multidimensional IRT (MIRT) 或 hierarchical IRT，而非独立 fitting。论文在 Future Directions 中提到 MIRT，但没有解释为什么现在不用。\n- 建议修改方向：(1) 增加一个 hierarchical IRT 或 MIRT 对比实验，展示独立 fitting 与共享 θ 的差异；(2) 至少在方法章节讨论这一设计选择的代价，而非仅作为优势呈现。\n\n**N5** [critical] **与最直接可比方法 DCR 的比较不充分**\n- 具体位置：Section 4.4 (B6-DCR)、Section 2.4\n- 问题：DCR (Xu et al., 2025) 是唯一同样尝试 contamination score adjustment 的方法。论文以 \"no public implementation is available\" 为由仅做定性比较。但 DCR 论文已发表（bib 中标注为 EMNLP 2025），其方法描述应足以支持 reimplementation。对于一篇声称解决同一问题的 full paper，仅做定性比较是不可接受的。\n- 为什么影响接收：缺少与最直接竞争者的定量比较，审稿人无法判断 ContamCal 相对 DCR 的实际优势。论文声称的三个优势（UQ、domain heterogeneity、IRT grounding）全部是理论层面的，没有实验验证——尤其是 UQ 优势已被 N2 中的 CI 失准问题削弱。\n- 建议修改方向：(1) 根据 DCR 论文描述 reimplementation；(2) 如果确实无法实现，至少在 DCR 报告的 benchmark 上做数值比较（从论文中提取数字）；(3) 在 Limitations 中明确承认这是一个重要缺口。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **缺少 Oracle Exposure 验证**\n- 具体位置：Section 4.1 controlled injection design\n- 问题：受控注入实验提供了 ground-truth 污染标签（d000 vs d005/d025/d100），但这些标签从未被用作 exposure variable 的 oracle 版本。一个简单的消融——用 binary injection status 替代检测信号作为 e_{ij}——可以干净地分离 \"IRT framework effectiveness\" 和 \"detection signal quality\" 两个因素。当前设计将两者混为一谈。\n- 建议：增加 Oracle-2PL+γ baseline，其中 e_{ij} = injection_dosage / 100。这可以回答一个关键问题：如果检测信号是完美的，γ 是否变得 significant？\n\n**W2** [warning] **Min-K%++ 方向反转的泛化性声称过强**\n- 具体位置：Section 5.2、Section 6.2 (\"Min-K++ should not be trusted at scales below 1.5B\")\n- 问题：方向反转仅在 Qwen2.5-0.5B 上观察到（N=1 架构）。Llama-3.2 仅在 3B 尺度测试。Section 6.2 的实践建议（\"Min-K++ should not be trusted at scales below 1.5B parameters\"）将单一架构的发现泛化为跨架构的通用建议，这是 over-claim。\n- 建议：将建议修改为 \"Min-K++ may exhibit directional reversal at sub-1.5B scales, as documented for Qwen2.5-0.5B; validation on other architectures is needed before general conclusions can be drawn.\"\n\n**W3** [warning] **RRF κ=60 无敏感性分析**\n- 具体位置：Section 3.2, Eq. 1\n- 问题：κ=60 是 IR 领域的标准值，但 contamination detection 的 rank distribution 可能与 document retrieval 有本质差异。没有对 κ 值的敏感性分析。如果结果对 κ 敏感，framework robustness 受质疑。\n- 建议：增加 κ ∈ {10, 30, 60, 120} 的敏感性分析，报告 exposure score 和最终 MAE 的变化。\n\n**W4** [warning] **Cross-family 分析 (Llama N=4) 价值有限**\n- 具体位置：Section 4.2、Section 5.4 最后一段\n- 问题：4 个模型、单 seed、其中一个 MMLU 排除（format collapse），一个 d000 排除（data loading error）。有效 MMLU 模型仅 2 个。论文正确标注为 exploratory，但即使如此，N=2 的 \"cross-family analysis\" 能提供的信息极为有限，且占用了宝贵的正文空间。\n- 建议：压缩至 1-2 句并移入 Appendix，或增加更多 family（如 Mistral、Phi）使分析具有统计意义。\n\n**W5** [warning] **GSM8K 11× overcorrection ratio 的实践含义未充分讨论**\n- 具体位置：Section 5.1 \"Gating and negative results\"\n- 问题：论文诚实报告了 GSM8K 的 overcorrection ratio 为 11×（校正 11 单位噪声 per 1 单位真实污染效应）。但这意味着在 γ 不显著的情况下，框架可能引入比原始误差更大的 spurious correction。论文提出了 \"gating criteria\" 但没有讨论：如果一个 practitioner 不知道 γ 是否显著（真实场景中没有 ground truth），如何决定是否使用 γ correction？\n- 建议：讨论实际部署场景中的决策流程——何时 practitioners 应该使用完整 2PL+γ vs. 回退到 vanilla 2PL？提供明确的 decision rules。\n\n**W6** [warning] **Table 2 不完整：缺少 B1/B2/B4/B5/B6 数值**\n- 具体位置：Table 2 (Section 5.1)\n- 问题：Table 2 仅包含 B0-Raw、B3-Vanilla2PL 和 ContamCal 三个方法。B1-Remove&Rescore、B2-Single2PL+γ、B4-LinearRegression、B5-Emperor、B6-DCR 的数值仅在文本中零散提及或 \"compared in the text\"（\"full numerical comparison in Appendix C\"）。正文主表应包含所有 baselines 的核心数值。\n- 建议：扩展 Table 2 包含所有 7 个 baselines 的 MAE 和 τ（DCR 标注为 N/A 或定性）。\n\n**W7** [warning] **外部效度受限：仅 LoRA SFT injection**\n- 具体位置：Section 6.1 \"Single injection protocol\"\n- 问题：所有实验使用 LoRA-based SFT injection。真实世界的污染发生在 pretraining 阶段（trillion-token web crawl 中包含 benchmark 数据），其分布特征与 SFT injection 可能完全不同。论文在 Introduction 中将 pretraining contamination 作为核心动机（\"trillion-token web crawls make contamination pervasive\"），但实验设计仅验证了 SFT 场景。\n- 建议：在 Limitations 中更显著地讨论这一 gap，或增加至少一个 pretraining-style contamination 的实验（例如 continued pretraining with benchmark data mixed in）。\n\n---\n\n## 小问题（不影响接收）\n\n- .bib 文件有 89 个条目但仅 30 个被引用（59 orphans），应清理。\n- Abstract 偏长（约 180 词），但在 ARR 可接受范围内。\n- Appendix A/C/E 在正文中被引用但在投稿材料中未直接可见，无法验证 Fisher information 推导和完整 baseline 数值。\n- Table 1 (domain γ) 中 ARC 的 CI 写法不一致（\"CI excl. 0\" 而非给出具体区间）。\n- Section 3.3 Eq. 2 中 γ_k 的下标 k 表示 stratum，但在描述 single-stratum benchmarks 时又使用 γ 无下标，符号不完全一致。\n\n---\n\n## Questions to Authors\n\nQ1. 如果用 ground-truth injection status（而非检测信号）作为 exposure variable，γ 是否变得 significant？这能回答 \"γ 不显著是因为信号噪声还是因为框架本身的问题\" 这一关键区分。\n\nQ2. 50% CI 的 35% 覆盖率——80% 和 95% CI 的经验覆盖率分别是多少？如果 95% CI 覆盖率也低于名义水平，整个 Bayesian UQ 框架的可靠性如何保障？\n\nQ3. 独立 per-domain fitting 中，不同 domain 的 θ_j 估计之间的相关性是多少？如果高度相关，为什么不用共享 θ 的 hierarchical/MIRT 模型？如果不相关，Eq. 4 的跨 domain 平均是否有意义？\n\nQ4. 3B d000 因 \"inconsistent hyperparameters across retraining iterations\" 被排除——具体是哪些超参数不一致？是否有可能用一致的设置重新训练？\n\nQ5. 论文声称 ARC 通过了 gating criteria（γ CI excluding zero, τ=0.756），但 vanilla 2PL 的 ARC MAE (0.016) 低于 ContamCal (0.020)。如何协调 \"γ is significant for ARC\" 与 \"adding γ worsens calibration for ARC\"？\n\n---\n\n## Missing References\n\n- **Multidimensional IRT for LLMs**: Zhou et al. (2025/2026) PSN-IRT（已在 bib 中但未引用）讨论了 LLM evaluation 中的多维 IRT，与本文的 per-domain 独立 fitting vs. MIRT 选择高度相关。\n- **Measurement invariance / DIF in LLM context**: 论文引用了教育测量中的 DIF 文献，但未讨论 measurement invariance across model families 的问题——cross-family analysis 实质上是在检验这一假设。\n- **Conformal prediction for LLM evaluation**: Angelopoulos & Bates (2023) 已在 bib 中但未引用，conformal prediction 可作为 CI miscalibration 的替代 UQ 方法。\n\n---\n\n## 主要优势\n\n1. **问题定位准确且时机合适**：将污染检测与测量理论校准桥接，填补了两个独立发展的研究线之间的空白。IRT + contamination 的组合思路新颖。\n\n2. **罕见的实验诚实度**：论文系统性地报告负面结果（γ 对校准无贡献、CI 覆盖不足、GSM8K overcorrection 11×），这在该领域的论文中不常见。Value decomposition（Section 3.5）将 IRT 贡献与 γ 贡献分开是一个有信息量的分析。\n\n3. **Identifiability boundary 分析有实际价值**：J≥50 的发现和 AUC-J 联合边界为该领域设定了明确的统计功效标准，对未来使用 IRT 进行 LLM 评估的研究具有指导意义。\n\n4. **Min-K%++ 方向反转**：虽然泛化性存疑（W2），但对单一架构的发现本身（Cohen's d = -1.55 to -1.98）是一个有价值的负面发现，对检测实践有直接警示意义。\n\n5. **Psychometric formalization 扎实**：三个 adaptation（Section 3.1）将教育测量的 item compromise IRT 框架合理地调整到 LLM 评估场景，学术严谨性较好。\n\n---\n\n**总结**：本文选择了一个重要且 timely 的问题，技术框架构建合理，且在负面结果报告上展现了罕见的诚实度。但核心创新组件（γ）被自身实验证明对校准无贡献，CI 可靠性不足以支撑 UQ 优势声称，实验排除率过高且 DCR 比较不充分。需要：(1) 根据实验结论重构叙事，将 \"IRT calibration decomposition\" 而非 \"contamination-aware calibration\" 作为主线；(2) 修复 CI 覆盖或诚实限定 UQ 声称；(3) 增加 oracle exposure ablation 和更完整的 baseline 数值比较。若能完成这些修改，论文有 Findings 级别的潜力。",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告：ContamCal: Calibrating Contaminated Benchmarks via Item Response Theory\n\n---\n\n## Paper Summary\n\n本文提出 ContamCal，一个两阶段框架：Stage 1 通过 Reciprocal Rank Fusion (RRF) 将多个污染检测信号融合为连续曝光分数；Stage 2 将曝光分数嵌入污染增强的 IRT 模型（2PL+γ），联合估计潜在能力 θ 和污染效应 γ。在 Qwen2.5 家族（0.5B/1.5B/3B）上进行受控 SFT 注入实验（MMLU、ARC-Challenge、GSM8K），排除 0.5B 后使用 J=13 模型。核心实验发现：(1) 标准 2PL（无 γ）即可获得与 2PL+γ 相当的校准效果，ARC MAE 从 0.034 降至 0.016；(2) Min-K%++ 在 0.5B 尺度出现方向反转；(3) 模拟研究表明可靠的 γ 恢复需要 J≥50，远超当前实践。\n\n---\n\n## 总体评分\n\n**Overall**: 2.5（Borderline Findings）\n**一句话总结**: 问题选择有价值且论文诚实度高，但核心创新组件（γ 参数）被自身实验证明基本无效，需要根本性重构论文叙事。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | IRT 校准的主要 claim 有实验支撑，但 CI 覆盖率失准（50% CI→35%）和 46% 模型排除率削弱内部效度 |\n| Excitement | 2.5/5 | 问题重要且 IRT+污染桥接思路新颖，但主要发现（标准 IRT 就够了）显著降低了污染特异性组件的吸引力 |\n| Overall Assessment | 2.5/5 | Borderline Findings：诚实的负面结果有价值，但需要重构叙事使之与实验结论匹配 |\n| Reproducibility | 3/5 | Stan 模型、先验、收敛标准描述详细；但 pipeline inconsistency 排除和不完整 baseline 数值表降低可复现性 |\n| Confidence | 4/5 | 熟悉 IRT 建模和 LLM 评估文献，仔细阅读全文；Appendix 未直接可见是唯一限制 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **核心贡献被自身实验否定：γ 参数对校准无贡献**\n- 具体位置：Table 2 (Section 5.1)、Section 3.5\n- 问题：论文标题 \"ContamCal\" 和 Abstract 将 2PL+γ 定位为核心贡献，但 Table 2 清楚显示 B3-Vanilla2PL（γ=0）在所有 benchmark 上 MAE 等于或优于 ContamCal（ARC: 0.016 vs 0.020; GSM8K: 0.006 vs 0.006; MMLU: 0.007 vs 0.007）。Section 3.5 承认 \"calibration benefit comes entirely from IRT ability estimation itself\"。这意味着论文的实际发现是 \"标准 IRT 降低校准误差\"，而非 \"污染感知的 IRT 降低校准误差\"。\n- 为什么影响接收：Title、Abstract、Introduction 的叙事框架与实验结论根本不一致。论文承诺的是 contamination-aware calibration，交付的是 standard IRT works。IRT 用于 LLM 评估已有充分前期工作（TinyBenchmarks, Growing Pains, HiBayES, ATLAS），本文的 incremental contribution 在去除 γ 后变得不明确。\n- 建议修改方向：如果主要贡献确实是 \"IRT 能力估计本身提供校准\" 的 decomposition 发现，应将标题和叙事重构为分析性贡献（\"Why does IRT calibrate contaminated benchmarks?\"），并将 γ 明确降格为 secondary/exploratory diagnostic。当前的包装方式让审稿人期望 γ 是 working contribution，但读完全文后发现不是。\n\n**N2** [critical] **Credible Interval 系统性失准，削弱对 DCR 的核心优势声称**\n- 具体位置：Section 5.1 \"Gating and negative results\" 段落、Section 6.1 (Limitations)\n- 问题：50% posterior credible interval 仅达到约 35% 的经验覆盖率。论文在 Related Work Section 2.4 和 Introduction 中反复强调 \"uncertainty quantification\" 是相对 DCR 的关键优势（\"DCR produces point estimates without uncertainty quantification\"）。但如果 CI 系统性过窄，这个 claimed advantage 实际上不成立——过度自信的 CI 比没有 CI 更危险，因为用户会基于错误的不确定性范围做决策。\n- 为什么影响接收：这不是一个可以放在 Limitations 中轻描淡写的问题。论文将 UQ 作为核心卖点之一（Introduction 第 7 段: \"posterior credible intervals that propagate detection signal noise into final uncertainty bounds\"），但实验证明这个 bound 不可靠。这构成 claim 与 evidence 的 mismatch。\n- 建议修改方向：(1) 诚实承认 UQ advantage over DCR 目前仅限于 directional guidance 而非 calibrated probability statements；(2) 报告 80% 和 95% CI 的经验覆盖率（目前只报告了 50%）；(3) 诊断原因——是 prior misspecification、model misfit、还是 J 过小导致？如果是结构性问题，需要明确说明修复路径。\n\n**N3** [critical] **46% 模型排除率暴露实验控制不足**\n- 具体位置：Section 4.1\n- 问题：24 个模型中排除 11 个（46%）。排除理由：\n  - 8 个 0.5B 模型：position bias confound（合理）\n  - 2 个 3B checkpoints：\"mismatched naming conventions between evaluation and signal extraction stages\"（pipeline bug，不是科学理由）\n  - 1 个 3B checkpoint：\"lacked evaluation results under the unified hyperparameter setting\"（实验协议不统一）\n  - 3B d000 全部排除：\"earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations\"（实验设计缺陷）\n  后三类排除（共 3+unknown 个）表明实验执行过程中协议不一致，这不是 principled exclusion 而是 post-hoc data cleaning。\n- 为什么影响接收：受控实验的核心价值在于 controlled，如果实验协议本身不统一（不同 iteration 使用不同超参数），internal validity 大打折扣。这也导致 J=13（已经低于论文自己确定的 J≥50 阈值）进一步缩小了统计功效。审稿人无法判断被排除的模型是否会改变结论。\n- 建议修改方向：(1) 用统一协议重新训练被排除的 checkpoints，或至少提供 sensitivity analysis 展示包含/排除这些模型对结果的影响；(2) 清晰区分 \"by design exclusion\"（0.5B position bias）和 \"post-hoc exclusion\"（pipeline bugs），对后者承认是实验缺陷而非设计选择。\n\n**N4** [critical] **独立 per-domain IRT fitting 放弃了 IRT 的核心优势**\n- 具体位置：Section 3.3 第一段：\"We stratify items by cognitive domain and fit independent IRT models per stratum\"\n- 问题：IRT 的根本优势在于将所有 item 和 examinee 放在统一的潜在量尺上（common scale）。独立 per-domain fitting 意味着每个 domain 产生独立的 θ_j 估计，这些 θ 不在同一量尺上。Eq. 4 的校准分数通过对所有 item 求平均来聚合，但这些 item 来自不同的 IRT fit，对应不同的 θ scale。这在统计上是不严谨的：相当于对不同量尺的能力估计做了隐式的 equal-weight 平均。\n- 为什么影响接收：这是一个方法论层面的问题。论文将 \"avoids cross-domain item parameter borrowing\" 呈现为设计优势，但实际上这牺牲了 IRT 框架最重要的属性。教育测量中处理 domain-specific effects 的标准方法是 Multidimensional IRT (MIRT) 或 hierarchical IRT，而非独立 fitting。论文在 Future Directions 中提到 MIRT，但没有解释为什么现在不用。\n- 建议修改方向：(1) 增加一个 hierarchical IRT 或 MIRT 对比实验，展示独立 fitting 与共享 θ 的差异；(2) 至少在方法章节讨论这一设计选择的代价，而非仅作为优势呈现。\n\n**N5** [critical] **与最直接可比方法 DCR 的比较不充分**\n- 具体位置：Section 4.4 (B6-DCR)、Section 2.4\n- 问题：DCR (Xu et al., 2025) 是唯一同样尝试 contamination score adjustment 的方法。论文以 \"no public implementation is available\" 为由仅做定性比较。但 DCR 论文已发表（bib 中标注为 EMNLP 2025），其方法描述应足以支持 reimplementation。对于一篇声称解决同一问题的 full paper，仅做定性比较是不可接受的。\n- 为什么影响接收：缺少与最直接竞争者的定量比较，审稿人无法判断 ContamCal 相对 DCR 的实际优势。论文声称的三个优势（UQ、domain heterogeneity、IRT grounding）全部是理论层面的，没有实验验证——尤其是 UQ 优势已被 N2 中的 CI 失准问题削弱。\n- 建议修改方向：(1) 根据 DCR 论文描述 reimplementation；(2) 如果确实无法实现，至少在 DCR 报告的 benchmark 上做数值比较（从论文中提取数字）；(3) 在 Limitations 中明确承认这是一个重要缺口。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **缺少 Oracle Exposure 验证**\n- 具体位置：Section 4.1 controlled injection design\n- 问题：受控注入实验提供了 ground-truth 污染标签（d000 vs d005/d025/d100），但这些标签从未被用作 exposure variable 的 oracle 版本。一个简单的消融——用 binary injection status 替代检测信号作为 e_{ij}——可以干净地分离 \"IRT framework effectiveness\" 和 \"detection signal quality\" 两个因素。当前设计将两者混为一谈。\n- 建议：增加 Oracle-2PL+γ baseline，其中 e_{ij} = injection_dosage / 100。这可以回答一个关键问题：如果检测信号是完美的，γ 是否变得 significant？\n\n**W2** [warning] **Min-K%++ 方向反转的泛化性声称过强**\n- 具体位置：Section 5.2、Section 6.2 (\"Min-K++ should not be trusted at scales below 1.5B\")\n- 问题：方向反转仅在 Qwen2.5-0.5B 上观察到（N=1 架构）。Llama-3.2 仅在 3B 尺度测试。Section 6.2 的实践建议（\"Min-K++ should not be trusted at scales below 1.5B parameters\"）将单一架构的发现泛化为跨架构的通用建议，这是 over-claim。\n- 建议：将建议修改为 \"Min-K++ may exhibit directional reversal at sub-1.5B scales, as documented for Qwen2.5-0.5B; validation on other architectures is needed before general conclusions can be drawn.\"\n\n**W3** [warning] **RRF κ=60 无敏感性分析**\n- 具体位置：Section 3.2, Eq. 1\n- 问题：κ=60 是 IR 领域的标准值，但 contamination detection 的 rank distribution 可能与 document retrieval 有本质差异。没有对 κ 值的敏感性分析。如果结果对 κ 敏感，framework robustness 受质疑。\n- 建议：增加 κ ∈ {10, 30, 60, 120} 的敏感性分析，报告 exposure score 和最终 MAE 的变化。\n\n**W4** [warning] **Cross-family 分析 (Llama N=4) 价值有限**\n- 具体位置：Section 4.2、Section 5.4 最后一段\n- 问题：4 个模型、单 seed、其中一个 MMLU 排除（format collapse），一个 d000 排除（data loading error）。有效 MMLU 模型仅 2 个。论文正确标注为 exploratory，但即使如此，N=2 的 \"cross-family analysis\" 能提供的信息极为有限，且占用了宝贵的正文空间。\n- 建议：压缩至 1-2 句并移入 Appendix，或增加更多 family（如 Mistral、Phi）使分析具有统计意义。\n\n**W5** [warning] **GSM8K 11× overcorrection ratio 的实践含义未充分讨论**\n- 具体位置：Section 5.1 \"Gating and negative results\"\n- 问题：论文诚实报告了 GSM8K 的 overcorrection ratio 为 11×（校正 11 单位噪声 per 1 单位真实污染效应）。但这意味着在 γ 不显著的情况下，框架可能引入比原始误差更大的 spurious correction。论文提出了 \"gating criteria\" 但没有讨论：如果一个 practitioner 不知道 γ 是否显著（真实场景中没有 ground truth），如何决定是否使用 γ correction？\n- 建议：讨论实际部署场景中的决策流程——何时 practitioners 应该使用完整 2PL+γ vs. 回退到 vanilla 2PL？提供明确的 decision rules。\n\n**W6** [warning] **Table 2 不完整：缺少 B1/B2/B4/B5/B6 数值**\n- 具体位置：Table 2 (Section 5.1)\n- 问题：Table 2 仅包含 B0-Raw、B3-Vanilla2PL 和 ContamCal 三个方法。B1-Remove&Rescore、B2-Single2PL+γ、B4-LinearRegression、B5-Emperor、B6-DCR 的数值仅在文本中零散提及或 \"compared in the text\"（\"full numerical comparison in Appendix C\"）。正文主表应包含所有 baselines 的核心数值。\n- 建议：扩展 Table 2 包含所有 7 个 baselines 的 MAE 和 τ（DCR 标注为 N/A 或定性）。\n\n**W7** [warning] **外部效度受限：仅 LoRA SFT injection**\n- 具体位置：Section 6.1 \"Single injection protocol\"\n- 问题：所有实验使用 LoRA-based SFT injection。真实世界的污染发生在 pretraining 阶段（trillion-token web crawl 中包含 benchmark 数据），其分布特征与 SFT injection 可能完全不同。论文在 Introduction 中将 pretraining contamination 作为核心动机（\"trillion-token web crawls make contamination pervasive\"），但实验设计仅验证了 SFT 场景。\n- 建议：在 Limitations 中更显著地讨论这一 gap，或增加至少一个 pretraining-style contamination 的实验（例如 continued pretraining with benchmark data mixed in）。\n\n---\n\n## 小问题（不影响接收）\n\n- .bib 文件有 89 个条目但仅 30 个被引用（59 orphans），应清理。\n- Abstract 偏长（约 180 词），但在 ARR 可接受范围内。\n- Appendix A/C/E 在正文中被引用但在投稿材料中未直接可见，无法验证 Fisher information 推导和完整 baseline 数值。\n- Table 1 (domain γ) 中 ARC 的 CI 写法不一致（\"CI excl. 0\" 而非给出具体区间）。\n- Section 3.3 Eq. 2 中 γ_k 的下标 k 表示 stratum，但在描述 single-stratum benchmarks 时又使用 γ 无下标，符号不完全一致。\n\n---\n\n## Questions to Authors\n\nQ1. 如果用 ground-truth injection status（而非检测信号）作为 exposure variable，γ 是否变得 significant？这能回答 \"γ 不显著是因为信号噪声还是因为框架本身的问题\" 这一关键区分。\n\nQ2. 50% CI 的 35% 覆盖率——80% 和 95% CI 的经验覆盖率分别是多少？如果 95% CI 覆盖率也低于名义水平，整个 Bayesian UQ 框架的可靠性如何保障？\n\nQ3. 独立 per-domain fitting 中，不同 domain 的 θ_j 估计之间的相关性是多少？如果高度相关，为什么不用共享 θ 的 hierarchical/MIRT 模型？如果不相关，Eq. 4 的跨 domain 平均是否有意义？\n\nQ4. 3B d000 因 \"inconsistent hyperparameters across retraining iterations\" 被排除——具体是哪些超参数不一致？是否有可能用一致的设置重新训练？\n\nQ5. 论文声称 ARC 通过了 gating criteria（γ CI excluding zero, τ=0.756），但 vanilla 2PL 的 ARC MAE (0.016) 低于 ContamCal (0.020)。如何协调 \"γ is significant for ARC\" 与 \"adding γ worsens calibration for ARC\"？\n\n---\n\n## Missing References\n\n- **Multidimensional IRT for LLMs**: Zhou et al. (2025/2026) PSN-IRT（已在 bib 中但未引用）讨论了 LLM evaluation 中的多维 IRT，与本文的 per-domain 独立 fitting vs. MIRT 选择高度相关。\n- **Measurement invariance / DIF in LLM context**: 论文引用了教育测量中的 DIF 文献，但未讨论 measurement invariance across model families 的问题——cross-family analysis 实质上是在检验这一假设。\n- **Conformal prediction for LLM evaluation**: Angelopoulos & Bates (2023) 已在 bib 中但未引用，conformal prediction 可作为 CI miscalibration 的替代 UQ 方法。\n\n---\n\n## 主要优势\n\n1. **问题定位准确且时机合适**：将污染检测与测量理论校准桥接，填补了两个独立发展的研究线之间的空白。IRT + contamination 的组合思路新颖。\n\n2. **罕见的实验诚实度**：论文系统性地报告负面结果（γ 对校准无贡献、CI 覆盖不足、GSM8K overcorrection 11×），这在该领域的论文中不常见。Value decomposition（Section 3.5）将 IRT 贡献与 γ 贡献分开是一个有信息量的分析。\n\n3. **Identifiability boundary 分析有实际价值**：J≥50 的发现和 AUC-J 联合边界为该领域设定了明确的统计功效标准，对未来使用 IRT 进行 LLM 评估的研究具有指导意义。\n\n4. **Min-K%++ 方向反转**：虽然泛化性存疑（W2），但对单一架构的发现本身（Cohen's d = -1.55 to -1.98）是一个有价值的负面发现，对检测实践有直接警示意义。\n\n5. **Psychometric formalization 扎实**：三个 adaptation（Section 3.1）将教育测量的 item compromise IRT 框架合理地调整到 LLM 评估场景，学术严谨性较好。\n\n---\n\n**总结**：本文选择了一个重要且 timely 的问题，技术框架构建合理，且在负面结果报告上展现了罕见的诚实度。但核心创新组件（γ）被自身实验证明对校准无贡献，CI 可靠性不足以支撑 UQ 优势声称，实验排除率过高且 DCR 比较不充分。需要：(1) 根据实验结论重构叙事，将 \"IRT calibration decomposition\" 而非 \"contamination-aware calibration\" 作为主线；(2) 修复 CI 覆盖或诚实限定 UQ 声称；(3) 增加 oracle exposure ablation 和更完整的 baseline 数值比较。若能完成这些修改，论文有 Findings 级别的潜力。",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-17T11:58:35.237482+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3916
}
```

</details>

---


### Assistant

_source line 96 · 2026-05-17T11:58:45.524999+00:00_

审稿报告已提交至 Review Director。

**核心判断**：Overall 2.5（Borderline Findings）。

5 个 Must-Fix 问题：
1. **γ 对校准无贡献**——Table 2 显示 vanilla 2PL 等于或优于 2PL+γ，论文标题/叙事与结论不匹配
2. **CI 覆盖率失准**（50% CI → 35%），削弱了论文声称的 UQ 优势
3. **46% 模型排除率**，其中多项因 pipeline inconsistency 而非科学理由
4. **独立 per-domain fitting 放弃了 IRT 统一量尺**，且未与 MIRT/hierarchical IRT 对比
5. **DCR 仅做定性比较**，对最直接竞争者缺乏定量验证

主要优势：问题定位准确、负面结果诚实度高、identifiability boundary 分析有实际指导价值。若能重构叙事（以 IRT decomposition 而非 γ correction 为主线）并补充 oracle ablation、完整 baseline 表和 CI 诊断，有 Findings 级别潜力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 4

## Round 4

4 recorded events


### User

_source line 97 · 2026-05-17T12:02:19.734398+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：
- **[AGREE]** 同意并简要说明理由
- **[REBUT]** 反驳并提供具体证据（cite Section/Table/Figure）

特别注意你们是否在以下问题上有分歧需要讨论：
- N4（格式不合规）：你是否也注意到 Limitations 位置、缺失 Figure/Appendix 的问题？
- W3（RRF 退化为 S1-only）：你在 W1 中提到了 oracle exposure，但 Reviewer 2 从另一个角度（multi-signal 卖点失效）切入，你如何看？
- Value Decomposition 专项评价：Reviewer 2 认为 "diagnostic value 的 circularity" 是关键问题，你是否同意？

---

## Reviewer 2 完整审稿报告

### 总体评分
Overall: 2.5/5 (Borderline Findings)
一句话总结: 研究方向有价值且写作质量高，但核心贡献（γ 参数）被自身实验证明在当前条件下不优于 vanilla 2PL，论文本质上是一个包装精良的 negative result，同时投稿材料处于未完成状态（缺 Figure 环境、缺 Appendix 文件、PDF 与源码不同步）。

### Must-Fix 问题

**N1** [critical] 核心叙事自相矛盾：标题承诺 contamination calibration，实验证明 γ 不必要
- Table 2 显示 vanilla 2PL (B3, γ=0) 在所有 benchmark 上 MAE 与 ContamCal 持平或更优：ARC 0.016 vs 0.020，GSM8K 0.006 vs 0.006，MMLU 0.007 vs 0.007
- "Value decomposition" framing 试图将 negative result 重新包装为 positive contribution，但产生根本性信服力问题
- 建议：彻底 reframe 以 "IRT alone suffices" 为主论点，或展示 γ 真正有帮助的条件

**N2** [critical] J=13 远低于论文自身建立的 J≥50 阈值，核心框架无法在当前规模下验证
- 8 个 MMLU domains 中仅 Social Sciences 的 γ CI 排除零
- 论文用自己的 identifiability analysis 证明了自己的 empirical analysis 是 underpowered
- 建议：更激进地 pool models 至 J≥30，或展示 J=13 + high-AUC signal 联合条件下 γ 能 recover

**N3** [critical] 仅测试 ≤3B 模型，严重限制实际价值
- 实际关心 contamination 的用户主要关注 7B+ 模型
- dose-response 数据显示 contamination effects 从 0.5B 到 3B 显著衰减，外推到 7B+ 效应可能消失
- 建议：至少补充 Qwen2.5-7B 和一个 8B 级别模型

**N4** [critical] 格式不合规：Limitations 位置错误 + 投稿材料不完整
- Limitations 是 Discussion 的 subsection 而非独立 section（ARR 要求独立 \section*{Limitations} 在 Conclusion 后）
- 正文引用 Appendix A/C/E 但源码无 appendix 文件
- 正文引用 4 个 Figure 但无 \begin{figure} 环境
- 编译的 PDF 与源码不同步

### Should-Fix 问题

**W1** [warning] 50% CI 仅 35% coverage，Bayesian UQ 名不副实
- 论文将 UQ 作为相对 DCR 的关键优势，但自身测试显示 CI 不可靠

**W2** [warning] 与 DCR 仅定性比较，最直接 baseline 缺失
- DCR 算法描述足够完整，重新实现并不困难

**W3** [warning] Contribution 2 (RRF 融合) 在实践中退化为 S1-only
- S2 方向反转，S4 接近随机/marginal
- "training-free" 和 "multi-signal" 两个卖点在实践中都被削弱
- S1 需要训练语料访问，限制闭源模型适用性

**W4** [warning] LoRA SFT injection 不代表真实 contamination
- 真实 contamination 主要发生在 pretraining 阶段

**W5** [warning] Related Work 遗漏直接竞争工作
- Zhou et al. (2026) PSN-IRT、Kocyigit et al. (2025)、Han et al. (2026) 在 bib 中存在但未引用
- 30 个引用对 EMNLP 长文偏少，59 个 orphan entries

### Value Decomposition 专项评价
- 当前处理逻辑自洽但 persuasion 失败
- "diagnostic value 的 circularity"：γ 的 diagnostic value 依赖 significance，但 7/8 domains 不显著
- 建议将论文定位转向 "IRT as calibration tool + diagnostic framework + identifiability roadmap"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-17T12:04:03.178275+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE] R2-N1: 核心叙事自相矛盾（γ 不必要）**\n与我的 R1-N1 完全一致。Table 2 的数据不可辩驳：vanilla 2PL 在所有三个 benchmark 上 MAE 持平或更优。R2 用 \"negative result 重新包装为 positive contribution\" 的措辞比我更准确。补充一个我自己发现的证据：Section 5.1 第二段明确写道 \"B3-Vanilla2PL achieves lower ARC MAE (0.016) than the full ContamCal model (0.020), because the γ parameter at J=13 introduces estimation noise that slightly degrades point calibration\"——论文自己承认 γ 不仅不帮忙，还引入了噪声。两位 reviewer 在这一点上高度一致，应视为最核心的修改要求。\n\n**[AGREE] R2-N2: J=13 远低于 J≥50**\n与我的 R1-N3（排除率分析）互补。R2 聚焦于 sample size 本身不足，我聚焦于排除过程暴露的实验控制问题，两个角度共同说明 J=13 的实验基础薄弱。补充：cross-family analysis 将 pool 扩展到 N=18-28（Section 5.4），γ 在所有 benchmark 上仍然 non-significant（MMLU γ=0.35 CI[-0.63,1.32], GSM8K γ=-0.13, ARC γ=0.01）。这说明即使 pool 到 J~28，γ 依然无法 recover，进一步支持 R2 的判断。R2 建议的 \"J=13 + high-AUC signal 联合条件\" 是一个合理的折中方案——论文的 simulation 显示 high AUC (≥0.90) 时 J=16 就能 recover γ（Section 5.3），如果实证中 S1 AUC > 0.95，为什么经验分析中 γ 仍不显著？这是论文需要回答的问题。\n\n**[AGREE with nuance] R2-N3: 仅 ≤3B 模型**\n我将此列为 W7（should-fix），R2 升级为 N3（critical）。我同意这是一个重要问题：Section 5.4 的 dose-response 数据显示 contamination effects 从 0.5B 到 3B 显著衰减（0.5B 时 Math accuracy 从 0.25 跳至 0.60，3B 时仅增加 3-5pp），外推趋势确实暗示 7B+ 效应可能消失。但我不完全同意将其列为 critical/must-fix：\n\n理由：论文的核心贡献是 framework + methodology + identifiability boundary analysis，这些是 scale-agnostic 的。IRT 框架本身不依赖于模型规模。identifiability 分析（J≥50, AUC≥0.55 的 boundary）是通过 simulation 建立的，不受限于 3B。缺少 7B+ 验证确实限制了 practical impact，但不 invalidate 方法论贡献。我倾向于保持 should-fix 级别，要求作者在 camera-ready 中增加 7B 实验，而非在 resubmission 前强制要求。\n\n但如果 Director 认为 practical applicability 对 EMNLP acceptance 是必要条件，我可以支持升级为 critical。\n\n**[AGREE] R2-N4: 格式不合规 + 投稿材料不完整**\n这是 R2 独有的发现，我在自己的审稿中仅将其列为小问题。回顾论文源码后确认：\n\n1. **Limitations 位置**：确实是 `\\subsection{Limitations}` 在 `\\section{Discussion}` 内（discussion.tex line 5-6），而非 ARR 要求的独立 `\\section*{Limitations}` 在 Conclusion 之后。这是格式违规。\n\n2. **Figure 缺失**：正文引用了 Figure 1-4（fig:signal_heatmap, fig:identifiability_heatmap, fig:domain_gamma, fig:dose_response），但整个源码中没有 `\\begin{figure}` 环境。我在审稿时通过文本理解了论文想表达的内容，但这确实意味着投稿材料不完整——reviewer 无法验证视觉展示的质量和准确性。\n\n3. **Appendix 缺失**：正文引用 Appendix A（Fisher information 推导）、C（完整 baseline 数值）、E（power calculations），但源码中无 appendix 文件。\n\nR2 将此列为 critical 是合理的。对于 ARR submission，这些不是 \"待完善\" 的细节而是基本完整性要求。如果这是提交前的最终版本，这些缺失意味着关键 claims 无法被验证（尤其是 Appendix A 中的 Fisher information 推导和 Appendix C 中的完整 baseline 数值）。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R2-W1: 50% CI → 35% coverage**\n与我的 R1-N2 相同，但我将其列为 critical 而 R2 列为 warning。我认为应维持 critical 级别：论文在 Introduction (paragraph 7) 和 Related Work (Section 2.4) 中明确将 UQ 作为相对 DCR 的核心优势。CI 不可靠直接削弱了这一核心 claim，不仅仅是一个 \"遗憾的发现\"。R2 在这一点上比我更温和。\n\n**[AGREE] R2-W2: DCR 仅定性比较**\n与我的 R1-N5 完全一致。我同样认为 DCR 的方法描述足以支持 reimplementation。\n\n**[AGREE] R2-W3: RRF 融合退化为 S1-only**\n这是 R2 的独特视角，我在审稿中未直接指出此问题。R2 的论点很有力：\n\n论文的 Contribution 2 是 \"Multi-signal exposure detection via RRF\"（Introduction, contribution list item 2），卖点包含 \"training-free\" 和 \"multi-signal\"。但 Section 5.2 的数据显示：\n- S2 (Min-K%++) 在 0.5B 方向反转，1.5B 仅 mild positive (d≈+0.3)，3B moderate (d≈+0.7)\n- S4 (Self-Critique) 在 0.5B AUC≈0.50（随机），1.5B-3B 仅 marginal\n- S1 (embedding similarity) AUC > 0.95 across all scales\n\nRRF 融合的效果依赖于信号互补性。当 2/3 的信号是噪声或反向信号时，RRF 实际上退化为 S1-only——或者更糟，S2 的反向信号可能污染融合结果。这不仅削弱了 \"multi-signal\" 卖点，还引出一个实际问题：为什么不直接用 S1？\n\n这个问题与我的 R1-W1（oracle exposure 缺失）形成互补。我的角度是 \"应该测试完美信号的效果\"，R2 的角度是 \"现有信号融合实际上不工作\"。两者共同指向同一个 gap：论文需要更清晰地分析 Stage 1 的实际贡献。\n\n补充一个 R2 未提到的维度：S1 (embedding similarity) 需要访问训练语料，这在闭源模型场景下不可用（Section 6.1 已承认）。如果实际有效的信号仅是 S1，框架的适用范围被显著限制在开源模型。\n\n**[AGREE] R2-W4: LoRA SFT ≠ 真实 contamination**\n与我的 R1-W7 一致。\n\n**[AGREE partially] R2-W5: Related Work 遗漏**\n同意 orphan entries 应清理（59 个未引用），30 个引用对 EMNLP 长文确实偏少。但 \"遗漏直接竞争工作\" 的严重程度取决于这些工作与本文的实际重叠度。Zhou et al. PSN-IRT 确实高度相关（我在 R1 Missing References 中也提到了），应该引用并在 Related Work 中讨论。\n\n---\n\n### Value Decomposition 专项回应\n\n**[AGREE] \"diagnostic value 的 circularity\" 是关键问题**\n\nR2 对这个问题的刻画比我更精确。我在 R1-N1 中指出了 γ 对校准无贡献的事实，但 R2 进一步揭示了一层逻辑循环：\n\n1. 论文承认 γ 不提供校准优势，转而声称 γ 提供 \"diagnostic value\"（Section 3.5, Section 5.1）\n2. 这个 diagnostic value 的前提是 γ 估计足够精确以区分正/负方向\n3. 但 8 个 MMLU domains 中 7 个 γ 不显著（Table 1），无法可靠判断方向\n4. 论文说 \"at sufficient ensemble sizes (J≥50), these become precise quantitative diagnostics\"（Section 3.5 末段）——但这是一个关于未来可能性的承诺，不是当前贡献\n5. 因此当前论文的 diagnostic contribution = 1 个显著 domain (Social Sciences) + 方向性 pattern (positive STEM, negative non-STEM) that lacks statistical support\n\n这形成了闭环：γ 不帮助校准 → γ 的价值在诊断 → 诊断需要显著性 → 当前条件下不显著 → γ 的价值在哪里？\n\nR2 建议的 reframing \"IRT as calibration tool + diagnostic framework + identifiability roadmap\" 我也同意。与其试图同时展示 γ 的校准和诊断价值，不如坦诚定位为：(1) IRT 本身就是好的校准工具（已证明），(2) 我们建立了 γ 诊断的理论框架（已建立），(3) 我们用 simulation 量化了何时该框架能工作（已量化），(4) 当前经验规模不够但这正是该领域需要前进的方向。这种 \"roadmap paper\" 的定位更诚实，也更能让审稿人接受。\n\n---\n\n### 总结：两位 Reviewer 的高度共识\n\nR1 和 R2 在以下问题上完全一致：\n1. **γ 对校准无贡献**是核心问题（R1-N1 = R2-N1）\n2. **J=13 不足**（R1-N3 + R2-N2）\n3. **CI 覆盖率失准**（R1-N2 vs R2-W1，我认为应取 critical 级别）\n4. **DCR 比较不充分**（R1-N5 = R2-W2）\n5. **LoRA SFT 不代表真实污染**（R1-W7 = R2-W4）\n\nR2 额外发现了我遗漏的问题：\n- **格式不合规 + 材料不完整**（R2-N4）——我确认这是真实问题\n- **RRF 退化为 S1-only**（R2-W3）——这是一个有力的新视角\n\n我额外发现了 R2 未强调的问题：\n- **独立 per-domain fitting 放弃统一 ability scale**（R1-N4）\n- **46% 排除率的 pipeline bug 原因**（R1-N3 细节）\n- **GSM8K 11× overcorrection 的实践含义**（R1-W5）\n- **RRF κ=60 无敏感性分析**（R1-W3）\n\n建议 Director 在综合意见中将 γ 无效 + CI 失准 + 材料不完整作为三个并列的 must-fix，并要求 reframing 为 \"IRT calibration roadmap\" 而非 \"contamination-aware calibration system\"。",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE] R2-N1: 核心叙事自相矛盾（γ 不必要）**\n与我的 R1-N1 完全一致。Table 2 的数据不可辩驳：vanilla 2PL 在所有三个 benchmark 上 MAE 持平或更优。R2 用 \"negative result 重新包装为 positive contribution\" 的措辞比我更准确。补充一个我自己发现的证据：Section 5.1 第二段明确写道 \"B3-Vanilla2PL achieves lower ARC MAE (0.016) than the full ContamCal model (0.020), because the γ parameter at J=13 introduces estimation noise that slightly degrades point calibration\"——论文自己承认 γ 不仅不帮忙，还引入了噪声。两位 reviewer 在这一点上高度一致，应视为最核心的修改要求。\n\n**[AGREE] R2-N2: J=13 远低于 J≥50**\n与我的 R1-N3（排除率分析）互补。R2 聚焦于 sample size 本身不足，我聚焦于排除过程暴露的实验控制问题，两个角度共同说明 J=13 的实验基础薄弱。补充：cross-family analysis 将 pool 扩展到 N=18-28（Section 5.4），γ 在所有 benchmark 上仍然 non-significant（MMLU γ=0.35 CI[-0.63,1.32], GSM8K γ=-0.13, ARC γ=0.01）。这说明即使 pool 到 J~28，γ 依然无法 recover，进一步支持 R2 的判断。R2 建议的 \"J=13 + high-AUC signal 联合条件\" 是一个合理的折中方案——论文的 simulation 显示 high AUC (≥0.90) 时 J=16 就能 recover γ（Section 5.3），如果实证中 S1 AUC > 0.95，为什么经验分析中 γ 仍不显著？这是论文需要回答的问题。\n\n**[AGREE with nuance] R2-N3: 仅 ≤3B 模型**\n我将此列为 W7（should-fix），R2 升级为 N3（critical）。我同意这是一个重要问题：Section 5.4 的 dose-response 数据显示 contamination effects 从 0.5B 到 3B 显著衰减（0.5B 时 Math accuracy 从 0.25 跳至 0.60，3B 时仅增加 3-5pp），外推趋势确实暗示 7B+ 效应可能消失。但我不完全同意将其列为 critical/must-fix：\n\n理由：论文的核心贡献是 framework + methodology + identifiability boundary analysis，这些是 scale-agnostic 的。IRT 框架本身不依赖于模型规模。identifiability 分析（J≥50, AUC≥0.55 的 boundary）是通过 simulation 建立的，不受限于 3B。缺少 7B+ 验证确实限制了 practical impact，但不 invalidate 方法论贡献。我倾向于保持 should-fix 级别，要求作者在 camera-ready 中增加 7B 实验，而非在 resubmission 前强制要求。\n\n但如果 Director 认为 practical applicability 对 EMNLP acceptance 是必要条件，我可以支持升级为 critical。\n\n**[AGREE] R2-N4: 格式不合规 + 投稿材料不完整**\n这是 R2 独有的发现，我在自己的审稿中仅将其列为小问题。回顾论文源码后确认：\n\n1. **Limitations 位置**：确实是 `\\subsection{Limitations}` 在 `\\section{Discussion}` 内（discussion.tex line 5-6），而非 ARR 要求的独立 `\\section*{Limitations}` 在 Conclusion 之后。这是格式违规。\n\n2. **Figure 缺失**：正文引用了 Figure 1-4（fig:signal_heatmap, fig:identifiability_heatmap, fig:domain_gamma, fig:dose_response），但整个源码中没有 `\\begin{figure}` 环境。我在审稿时通过文本理解了论文想表达的内容，但这确实意味着投稿材料不完整——reviewer 无法验证视觉展示的质量和准确性。\n\n3. **Appendix 缺失**：正文引用 Appendix A（Fisher information 推导）、C（完整 baseline 数值）、E（power calculations），但源码中无 appendix 文件。\n\nR2 将此列为 critical 是合理的。对于 ARR submission，这些不是 \"待完善\" 的细节而是基本完整性要求。如果这是提交前的最终版本，这些缺失意味着关键 claims 无法被验证（尤其是 Appendix A 中的 Fisher information 推导和 Appendix C 中的完整 baseline 数值）。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R2-W1: 50% CI → 35% coverage**\n与我的 R1-N2 相同，但我将其列为 critical 而 R2 列为 warning。我认为应维持 critical 级别：论文在 Introduction (paragraph 7) 和 Related Work (Section 2.4) 中明确将 UQ 作为相对 DCR 的核心优势。CI 不可靠直接削弱了这一核心 claim，不仅仅是一个 \"遗憾的发现\"。R2 在这一点上比我更温和。\n\n**[AGREE] R2-W2: DCR 仅定性比较**\n与我的 R1-N5 完全一致。我同样认为 DCR 的方法描述足以支持 reimplementation。\n\n**[AGREE] R2-W3: RRF 融合退化为 S1-only**\n这是 R2 的独特视角，我在审稿中未直接指出此问题。R2 的论点很有力：\n\n论文的 Contribution 2 是 \"Multi-signal exposure detection via RRF\"（Introduction, contribution list item 2），卖点包含 \"training-free\" 和 \"multi-signal\"。但 Section 5.2 的数据显示：\n- S2 (Min-K%++) 在 0.5B 方向反转，1.5B 仅 mild positive (d≈+0.3)，3B moderate (d≈+0.7)\n- S4 (Self-Critique) 在 0.5B AUC≈0.50（随机），1.5B-3B 仅 marginal\n- S1 (embedding similarity) AUC > 0.95 across all scales\n\nRRF 融合的效果依赖于信号互补性。当 2/3 的信号是噪声或反向信号时，RRF 实际上退化为 S1-only——或者更糟，S2 的反向信号可能污染融合结果。这不仅削弱了 \"multi-signal\" 卖点，还引出一个实际问题：为什么不直接用 S1？\n\n这个问题与我的 R1-W1（oracle exposure 缺失）形成互补。我的角度是 \"应该测试完美信号的效果\"，R2 的角度是 \"现有信号融合实际上不工作\"。两者共同指向同一个 gap：论文需要更清晰地分析 Stage 1 的实际贡献。\n\n补充一个 R2 未提到的维度：S1 (embedding similarity) 需要访问训练语料，这在闭源模型场景下不可用（Section 6.1 已承认）。如果实际有效的信号仅是 S1，框架的适用范围被显著限制在开源模型。\n\n**[AGREE] R2-W4: LoRA SFT ≠ 真实 contamination**\n与我的 R1-W7 一致。\n\n**[AGREE partially] R2-W5: Related Work 遗漏**\n同意 orphan entries 应清理（59 个未引用），30 个引用对 EMNLP 长文确实偏少。但 \"遗漏直接竞争工作\" 的严重程度取决于这些工作与本文的实际重叠度。Zhou et al. PSN-IRT 确实高度相关（我在 R1 Missing References 中也提到了），应该引用并在 Related Work 中讨论。\n\n---\n\n### Value Decomposition 专项回应\n\n**[AGREE] \"diagnostic value 的 circularity\" 是关键问题**\n\nR2 对这个问题的刻画比我更精确。我在 R1-N1 中指出了 γ 对校准无贡献的事实，但 R2 进一步揭示了一层逻辑循环：\n\n1. 论文承认 γ 不提供校准优势，转而声称 γ 提供 \"diagnostic value\"（Section 3.5, Section 5.1）\n2. 这个 diagnostic value 的前提是 γ 估计足够精确以区分正/负方向\n3. 但 8 个 MMLU domains 中 7 个 γ 不显著（Table 1），无法可靠判断方向\n4. 论文说 \"at sufficient ensemble sizes (J≥50), these become precise quantitative diagnostics\"（Section 3.5 末段）——但这是一个关于未来可能性的承诺，不是当前贡献\n5. 因此当前论文的 diagnostic contribution = 1 个显著 domain (Social Sciences) + 方向性 pattern (positive STEM, negative non-STEM) that lacks statistical support\n\n这形成了闭环：γ 不帮助校准 → γ 的价值在诊断 → 诊断需要显著性 → 当前条件下不显著 → γ 的价值在哪里？\n\nR2 建议的 reframing \"IRT as calibration tool + diagnostic framework + identifiability roadmap\" 我也同意。与其试图同时展示 γ 的校准和诊断价值，不如坦诚定位为：(1) IRT 本身就是好的校准工具（已证明），(2) 我们建立了 γ 诊断的理论框架（已建立），(3) 我们用 simulation 量化了何时该框架能工作（已量化），(4) 当前经验规模不够但这正是该领域需要前进的方向。这种 \"roadmap paper\" 的定位更诚实，也更能让审稿人接受。\n\n---\n\n### 总结：两位 Reviewer 的高度共识\n\nR1 和 R2 在以下问题上完全一致：\n1. **γ 对校准无贡献**是核心问题（R1-N1 = R2-N1）\n2. **J=13 不足**（R1-N3 + R2-N2）\n3. **CI 覆盖率失准**（R1-N2 vs R2-W1，我认为应取 critical 级别）\n4. **DCR 比较不充分**（R1-N5 = R2-W2）\n5. **LoRA SFT 不代表真实污染**（R1-W7 = R2-W4）\n\nR2 额外发现了我遗漏的问题：\n- **格式不合规 + 材料不完整**（R2-N4）——我确认这是真实问题\n- **RRF 退化为 S1-only**（R2-W3）——这是一个有力的新视角\n\n我额外发现了 R2 未强调的问题：\n- **独立 per-domain fitting 放弃统一 ability scale**（R1-N4）\n- **46% 排除率的 pipeline bug 原因**（R1-N3 细节）\n- **GSM8K 11× overcorrection 的实践含义**（R1-W5）\n- **RRF κ=60 无敏感性分析**（R1-W3）\n\n建议 Director 在综合意见中将 γ 无效 + CI 失准 + 材料不完整作为三个并列的 must-fix，并要求 reframing 为 \"IRT calibration roadmap\" 而非 \"contamination-aware calibration system\"。",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-17T12:04:06.944120+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3765
}
```

</details>

---


### Assistant

_source line 100 · 2026-05-17T12:04:13.259686+00:00_

交叉回应已提交。

两位 Reviewer 在核心问题上高度一致（γ 无效、J 不足、CI 失准、DCR 比较缺失）。我的回应确认了 R2 独有发现（格式不合规 R2-N4、RRF 退化 R2-W3），同时补充了 R2 未覆盖的问题（独立 per-domain fitting 放弃统一 scale、46% 排除率中的 pipeline bug、GSM8K overcorrection 11×）。唯一分歧在于模型规模限制（≤3B）的严重性：R2 列为 critical，我倾向 should-fix，因为框架和 identifiability 分析本身是 scale-agnostic 的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 5

## Round 5

34 recorded events


### User

_source line 101 · 2026-05-17T14:16:17.584609+00:00_

[Round 3 审稿请求]:
## Round 3 审稿任务 — Reviewer 1: 方法严谨性 + 实验有效性

### Venue 信息
- **目标**: EMNLP 2026（ARR May 2026 cycle）
- **Deadline**: 2026-05-25
- **格式**: Long paper, 8 页正文上限, ACL LaTeX template [review], double-blind
- **Limitations**: 需在 references 之前作为独立 section，不计入页数
- **评分**: 5=Award, 4=Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit

### 论文路径
- 主文件: `projects/contamcal-irt-calibration/docs/paper/main.tex`
- 各章节: `abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `experimental_setup.tex`, `results.tex`, `discussion.tex`, `conclusion.tex`, `appendix.tex`
- 图片: `docs/paper/figures/` (4 个 PDF: fig_signal_heatmap, fig_identifiability_heatmap, fig_domain_gamma, fig_dose_response)
- 参考文献: `references.bib` (91 entries, 33 actually cited)

### 你的审查侧重

**核心关注**: 方法论是否站得住脚、实验设计是否有效、统计分析是否可信、baseline 比较是否公平。

请重点审查以下方面：

1. **IRT 建模有效性**
   - 2PL+γ 模型假设是否合理？独立 per-domain fitting 导致的 θ scale 不可比性是否被充分讨论？
   - Eq.4 的 additive γ 结构是否过于简化（linear contamination effect）？
   - Bayesian 推断设置（priors, convergence criteria）是否标准？

2. **统计分析质量**
   - CI 覆盖率：论文报告 50% CI 只达到 ~35% empirical coverage，是否报告了 80%/95% 覆盖率？这对 UQ claim 的影响？
   - PPP 值：ARC PPP=0.003（Round 1 发现），论文是否在 results 中正确处理了这个 misfit？
   - 显著性判断：8/8 MMLU 域中仅 1 个显著，γ pooled 不显著——统计结论是否过度乐观？

3. **实验设计**
   - 46% 模型排除率（24→13）：0.5B position bias 排除合理，但 3 个 3B 因 pipeline bugs 排除——是否有 sensitivity analysis 说明排除影响？
   - J=13 vs 论文自己建立的 J≥50 阈值：论文如何处理自己证明自己 underpowered 的矛盾？
   - SFT injection vs 真实 pretraining contamination：生态效度限制是否充分讨论？

4. **Baseline 比较公平性**
   - 主表（Tab baselines）仅展示 B0/B3/ContamCal，完整 B0-B6 在附录但用不同配置（ARC: J=8 0.5B+1.5B; GSM8K: 0.5B）——与主分析 J=13 1.5B+3B 不一致，是否构成 cherry-picking？
   - DCR 数值（ARC 0.245, GSM8K 0.263）远高于其他方法。论文声称"no public implementation"但给出了数值——来源和可复现性？
   - GSM8K 附录表: B0-Raw MAE=0.003 而 ContamCal MAE=0.020，ContamCal 反而让校准变差 6.7×——这是否被充分讨论？

5. **关键缺失实验**
   - Oracle Exposure ablation：ground-truth injection labels 存在但从未用作 oracle e_{ij}。这个零成本消融实验能回答"如果信号完美，γ 是否显著？"
   - Cross-family 仅 Llama N=4（single seed），是否足以支撑"跨家族泛化"的 claim？

### Round 1-2 遗留 open issues（你负责的部分，请逐条检查修复状态）

- **R2-N1 [Critical]**: γ 无校准收益——核心叙事不匹配。Title/Abstract 仍 promise contamination-aware calibration？
- **R2-N2 [Critical]**: CI 覆盖失准——50% CI 仅 35% 实际覆盖。是否新增 80%/95% 覆盖率报告？
- **R2-N3 [Critical]**: 46% 排除率——pipeline bug 作为排除理由。是否有 sensitivity analysis？
- **R2-N4 [Critical]**: J=13 远低于 J≥50 阈值——论文如何处理自证 underpowered？
- **R2-N5 [Critical]**: DCR 比较不充分——是否有数值比较？来源？
- **R2-W2 [Warning]**: Oracle Exposure ablation 缺失
- **R2-W4 [Warning]**: 独立 fitting 破坏 common scale
- **R1-A1 [Warning]**: ARC PPP=0.003 系统性 misfit
- **R1-C2 [Critical]**: Cross-family N=3(4) 不充分

### 输出格式
请按以下结构输出：
1. Summary (2-3 句)
2. Strengths (S1, S2, ...)
3. Weaknesses — 分为 Must-Fix (N1, N2, ...) 和 Should-Fix (W1, W2, ...)
4. Questions (Q1, Q2, ...)
5. Missing References
6. Overall Assessment (评分 1-5 按 EMNLP 标准 + confidence 1-5)
7. Detailed Comments (逐节)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-17T14:16:38.510752+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-17T14:16:38.561497+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-17T14:16:51.289909+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 105 · 2026-05-17T14:16:52.744963+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 106 · 2026-05-17T14:16:53.699989+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{ContamCal: Calibrating Contaminated Benchmarks via\\Item Response Theory}
13	
14	\author{Anonymous}
15	
16	\begin{document}
17	\maketitle
18	
19	\begin{abstract}
20	\input{abstract}
21	\end{abstract}
22	
23	\input{introduction}
24	\input{related_work}
25	\input{method}
26	\input{experimental_setup}
27	\input{results}
28	\input{discussion}
29	\input{conclusion}
30	
31	\bibliography{references}
32	
33	\input{appendix}
34	
35	\end{document}
36	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 107 · 2026-05-17T14:16:53.800836+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 108 · 2026-05-17T14:16:53.801191+00:00_

1	Training data contamination undermines the validity of Large Language Model (LLM) benchmark comparisons, yet existing approaches stop at detection without quantifying how much scores are inflated or providing calibrated estimates with uncertainty bounds. We introduce ContamCal, a framework grounded in Item Response Theory (IRT) that bridges this gap: it fuses multiple detection signals via training-free Reciprocal Rank Fusion into continuous per-item exposure scores, then embeds them in a contamination-augmented IRT model to jointly estimate latent ability and contamination effects. Our central finding is a decomposition result: applied to MMLU, ARC-Challenge, and GSM8K with controlled contamination injection across Qwen2.5 and Llama-3.2, IRT ability estimation alone reduces calibration error by up to 53\% relative to raw scores, independent of whether contamination is explicitly modeled. Cross-family validation (up to $J=28$) confirms that calibrated MAE remains below 0.02 across all benchmarks and model families, with IRT absorbing family-specific contamination responses into $\theta$ estimates. The contamination parameter $\gamma$ provides complementary diagnostic value: within-family analysis across eight MMLU cognitive domains reveals directional heterogeneity, with Social Sciences reaching significance ($\gamma = -0.57$, CI excluding zero), though domain-level patterns are family-specific and do not generalize across architectures. We further document that Min-K\%++ exhibits directional reversal at small model scales (Cohen's $d = -1.55$ to $-1.98$), where the signal is actively misleading rather than merely ineffective. Simulation studies establish that reliable $\gamma$ recovery requires signal AUC $\geq 0.55$ and $J \geq 50$, a threshold that exposes a structural gap between current LLM evaluation practice and the statistical requirements of contamination-augmented IRT.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 109 · 2026-05-17T14:16:53.801422+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 110 · 2026-05-17T14:16:53.902051+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection, resource allocation, and research priorities for large language models, yet training data contamination undermines the validity of these scores in ways that current evaluation cannot quantify \citep{hendrycks2021mmlu,chang2025benchmarking}. When models encounter test items during training, observed accuracy conflates genuine capability with memorization, and practitioners have no principled way to determine how much of a reported score reflects real understanding. The problem is compounded by the scale of modern training corpora: trillion-token web crawls make contamination pervasive and instance-level measurement infeasible \citep{oren2024proving}. Post-hoc calibration that quantifies contamination effects despite imperfect detection is therefore essential for trustworthy evaluation.
4	
5	Two developments make this gap urgent. First, \citet{sun2025emperor} systematically evaluate twenty contamination mitigation strategies (rephrasing, option shuffling, dynamic benchmark regeneration, and others) and demonstrate that none restores clean performance after contamination has occurred. This result forecloses the ``prevent contamination'' approach for models already trained on unrestricted web data. Second, contamination-free benchmarks \citep{white2024livebench} offer a partial solution but sacrifice the comparability and institutional knowledge accumulated around established benchmarks. Dynamic regeneration of test items may also be contaminated within weeks as web crawlers index benchmark repositories \citep{dong_2024_cdd}. The field therefore needs post-hoc statistical tools that can separate genuine ability from contamination artifacts on existing benchmarks.
6	
7	Detection methods such as Min-K\%++ \citep{zhang_2024_minkpp}, ConStat \citep{dekoninck2024constat}, and Kernel Divergence Signatures \citep{choi_2025_kds} can flag contaminated items but stop at detection. They d
…[truncated 4118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-17T14:16:59.423630+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here is information about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text
…[truncated 1491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8133
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-17T14:17:02.593285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-17T14:17:02.644074+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is twofold: (1)~estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt}, adapting these frameworks through three structural modifications for LLM evaluation.
12	
13	\textit{Adaptation~1: Independent examinees $\to$ shared item pool.} Classical IRT assumes independent test-takers. In LLM evaluation, a fixed item set is shared across all models, and responses within a single model may exhibit residual correlations beyond the scalar~$\theta_j$ \citep{sanmartin_2009_irt}. We mitigate this by fitting per-benchmark models.
14	
15	\textit{Adaptation~2: Binary leakage $\to$ continuous exposure.} Item compromise IRT uses binary indicators \citep{sinharay_2017_preknowledge}. LLM contamination is graded: a model may have encountered an item zero, once, or hundreds of times. We replace binary indicators with continuous exposure scores $e_{ij} \in [0,1]$ derived from de
…[truncated 6727 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-17T14:17:03.095910+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-17T14:17:03.549206+00:00_

1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed using Qwen2.5 \citep{qwen2024qwen25} at three scales (0.5B, 1.5B, 3B parameters). For each scale, we fine-tune with Low-Rank Adaptation \citep[LoRA;][]{hu2022lora} ($\alpha=32$, $r=16$, lr$=5\times10^{-5}$) on a general-purpose SFT corpus into which benchmark items are injected at four dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), and d100 (100\%). Injected items are formatted as instruction-response pairs and pass a quality-control filter that removes ambiguous or malformed entries.
8	
9	Each configuration is trained with two random seeds (s42, s123), yielding 24 models across $3 \times 4 \times 2$ conditions. This within-family design isolates contamination dosage as the primary experimental variable while controlling for architecture, tokenizer, and pretraining data.
10	
11	We exclude 0.5B models from MMLU and ARC IRT analyses due to answer-position bias that correlates with dosage (A-option rate: 46\% at d000 to 98\% at d100). Three 3B checkpoints are excluded for pipeline inconsistencies (details in Appendix~\ref{sec:exclusion_details}), yielding $J=13$ respondents (1.5B$\times$8 + 3B$\times$5). The eight 1.5B d000 models serve as the clean reference anchor; 3B ability estimates are anchored via joint fitting with these controls. GSM8K retains all scales.
12	
13	\subsection{Cross-Family Analysis}
14	\label{sec:cross_family}
15	
16	To test whether IRT calibration is robust to inclusion of new model families, we fine-tune Llama-3.2-3B \citep{grattafiori2024llama3} under the same protocol (d000, d005, d025, d100) with a single seed, yielding $J=4$ additional models. This analysis is \textbf{exploratory}: the single-seed design provides limited statistical power, and we report post-hoc power calculations in Appendix~E using Qwen $J=13$ effect sizes as reference.
17	
18	L
…[truncated 2019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-17T14:17:03.549640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-17T14:17:04.102734+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Calibration Quality}
5	\label{sec:calibration_results}
6	
7	\paragraph{Value decomposition.}
8	Table~\ref{tab:baselines} compares calibration MAE across methods. Vanilla 2PL without a contamination parameter (B3, $\gamma = 0$) achieves calibration comparable to the full 2PL+$\gamma$ model: ARC MAE 0.016 vs.\ 0.020, GSM8K 0.006 vs.\ 0.006, MMLU 0.007 vs.\ 0.007. The calibration benefit comes from IRT ability estimation itself, which separates stable capability from item-level noise regardless of whether contamination is explicitly modeled. The IRT model successfully differentiates ability across scales: the mean ability gap between 3B and 1.5B models is $\Delta\theta = 0.50$ (95\% CI $[0.43, 0.57]$) in the pooled analysis, with all eight domain-level estimates also excluding zero (Appendix~\ref{sec:theta_separation}). B3 achieves lower ARC MAE than ContamCal because $\gamma$ at $J = 13$ introduces estimation noise. ContamCal nonetheless provides three capabilities beyond vanilla 2PL: $\gamma$ estimates supply domain-level contamination diagnostics (Table~\ref{tab:domain_gamma}), the posterior yields credible intervals that propagate signal uncertainty, and gating criteria provide principled exclusion rules for benchmarks where $\gamma$ is non-significant.
9	
10	\paragraph{Gating and negative results.}
11	ARC passes gating: MAE reduction of 0.014 relative to B0-Raw (0.034 $\to$ 0.020) and $\gamma$ CI excluding zero ($\tau = 0.733$). GSM8K fails gating ($\gamma$ non-significant). We report two honest negatives: credible interval coverage falls below nominal levels (50\% CI achieves $\sim$35\% empirical coverage), and the GSM8K overcorrection ratio is 11$\times$ due to the non-significant $\gamma$ being applied uniformly.
12	
13	\paragraph{Comparison to baselines.}
14	B0-Raw shows substantial miscalibration on ARC (MAE$=$0.034) but minimal on MMLU (MAE$=$0.016) where diverse domains partially cancel errors. B1-R
…[truncated 10395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-17T14:17:04.103252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-17T14:17:04.153908+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	We discuss limitations in Appendix~\ref{sec:limitations}, including scale ceiling (all models $\leq$3B), signal coverage gaps for closed-source models, ensemble size constraints ($J=13$ vs.\ the $J \geq 50$ needed for reliable $\gamma$ recovery), position bias confounds at the 0.5B scale, and under-coverage of posterior credible intervals.
5	
6	\paragraph{Implications for practice.}
7	Our findings carry four recommendations. For benchmark developers, IRT-based calibration should be standard infrastructure: vanilla 2PL alone reduces MAE by 53\% on ARC without any detection signals, and cross-family validation confirms this benefit generalizes across architectures (\S\ref{sec:cross_family_validation}). For detection practitioners, Min-K\%++ should not be trusted below 1.5B parameters due to directional reversal (\S\ref{sec:signal_failure}). For leaderboard operators, adding IRT to evaluation pipelines is a low-cost improvement that does not require contamination detection. For researchers, per-domain breakdowns should be reported alongside aggregate scores, as contamination may affect cognitive domains differently.
8	
9	\paragraph{Future directions.}
10	Scaling to $J \geq 50$ by pooling respondents across checkpoints, seeds, and training configurations would enable confirmatory tests of the directional heterogeneity observed here. Multidimensional IRT could model domain-specific ability dimensions that interact differently with contamination. Active signal selection via Fisher information optimization could reduce the requirement for full corpus access, enabling application to closed-source models.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-17T14:17:10.991076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-17T14:17:11.393827+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We presented ContamCal, a framework that connects contamination detection signals to IRT-based calibration through a two-stage pipeline: training-free signal fusion via RRF followed by contamination-augmented IRT estimation. Our experiments on MMLU, ARC-Challenge, and GSM8K with controlled contamination injection across Qwen2.5 and Llama-3.2 yield three findings. First, IRT ability estimation provides calibration benefit independent of the contamination parameter $\gamma$, reducing calibration error by up to 53\% relative to raw scores; cross-family validation (up to $J=28$) confirms that calibrated MAE remains below 0.02 across all benchmarks and families, with IRT absorbing differential contamination susceptibility into $\theta$. Second, Min-K\%++ exhibits directional reversal at small model scales: the signal is actively misleading rather than merely ineffective. Third, $\gamma$ diagnosis is family-specific: within-family analysis at $J = 13$ reveals directional heterogeneity across MMLU cognitive domains (Social Sciences reaching significance), but cross-family pooling collapses $\gamma$ as contamination effects are absorbed into family-specific $\theta$ trajectories.
4	
5	The central lesson is that IRT provides a principled calibration framework for contaminated benchmarks, with per-domain $\gamma$ parameters offering diagnostic potential that will become increasingly actionable as evaluation pools grow. Scaling to $J \geq 50$ through broader model sampling, multidimensional IRT for domains where scalar $\gamma$ is insufficient, and active signal selection for closed-source settings are immediate next steps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-17T14:17:11.545151+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-17T14:17:11.846497+00:00_

1	\appendix
2	
3	\section{Limitations}
4	\label{sec:limitations}
5	
6	We identify seven limitations that bound the scope of our conclusions.
7	
8	\paragraph{Scale ceiling.}
9	All experiments use models at or below 3B parameters. Larger models (7B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.
10	
11	\paragraph{Signal coverage.}
12	S1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination below 1.5B (\S\ref{sec:signal_failure}).
13	
14	\paragraph{Ensemble size and per-domain power.}
15	Reliable $\gamma$ recovery requires $J \geq 50$. Our $J = 13$ yields significance for only one of eight MMLU domains. Per-domain $\gamma$ diagnosis at current ensemble sizes is exploratory.
16	
17	\paragraph{Position bias.}
18	Qwen2.5-0.5B exhibits position bias correlated with dosage (A-option rate: 46\% at d000 to 98\% at d100), necessitating exclusion from MC IRT analyses and reducing ensemble size.
19	
20	\paragraph{Credible interval coverage.}
21	50\% posterior CIs achieve $\sim$35\% empirical coverage, functioning as directional indicators rather than precise probability statements.
22	
23	\paragraph{Model misfit in non-STEM domains.}
24	A single linear $\gamma$ cannot capture non-monotone contamination effects within a domain. Richer specifications may be required.
25	
26	\paragraph{Single injection protocol.}
27	We use LoRA-based SFT injection exclusively. Pretraining-stage leakage may produce different signatures.
28	
29	\section{4PL Extension}
30	\label{sec:4pl_details}
31	
32	For MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:
33	\begin{equation}
34	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
35	\end{equation}
36	with $c_i \sim \text{Beta}(5,20)$ and $d_i \si
…[truncated 5926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-17T14:17:11.897201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-17T14:17:11.897807+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination detection and mitigation.}
5	Membership inference approaches include Min-K\% \citep{shi_2023_minkprob} and Min-K\%++ \citep{zhang_2024_minkpp} (token-level surprisal), ConStat \citep{dekoninck2024constat} (accuracy gaps on paraphrased items), CDD/TED \citep{dong_2024_cdd} (completion-based probes), KDS \citep{choi_2025_kds} (kernel divergence), and TS-Guessing \citep{deng_2024_tsguessing} (temporal splits). Concurrent with our work, \citet{tao2025detecting} propose an entropy collapse method for RL-trained models. These methods flag contamination but do not produce adjusted scores. On the mitigation side, \citet{sun2025emperor} systematically evaluate twenty approaches (rephrasing, option shuffling, dynamic construction) and find that none reliably restores clean performance, motivating post-hoc correction. DCR \citep{xu2025dcr} estimates decontaminated scores via fuzzy inference but produces point estimates without uncertainty quantification or domain-level diagnosis. ContamCal consumes detection signals as inputs and feeds them into a calibration framework that estimates decontaminated ability with credible intervals.
6	
7	\paragraph{IRT for LLM evaluation.}
8	Item Response Theory has gained traction as a principled alternative to raw accuracy. \citet{lalor_2024_irt_nlp} provide a comprehensive IRT tutorial for NLP; TinyBenchmarks \citep{polo_2024_tinybenchmarks} uses IRT-informed item selection for efficient evaluation; Growing Pains \citep{habba_2025_growing_pains} validates IRT at scale on 400+ models and identifies low-respondent limitations; HiBayES \citep{luettgau_2025_hibayes} adds hierarchical Bayesian inference for credible intervals; ATLAS \citep{li_2024_atlas} applies IRT for adaptive testing. All treat items as equally trustworthy. ContamCal augments IRT with contamination covariates $\gamma_k$ within the item response function, drawing on the educational measurement trad
…[truncated 852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-17T14:18:08.465906+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-17T14:18:08.567026+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-17T14:18:15.933503+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. I need: 1) All scoring dimensions (soundness, excitement, overall, etc.) with their exact scale descriptions. 2) What reviewers are asked to evaluate. 3) Any specific guidance on how to score each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. I need: 1) All scoring dimensions (soundness, excitement, overall, etc.) with their exact scale descriptions. 2) What reviewers are asked to evaluate. 3) Any specific guidance on how to score each dimension."
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-17T14:18:20.710685+00:00_

# ACL Rolling Review Form: Scoring Dimensions and Guidance

## Primary Scoring Dimensions

### 1. **Soundness** (5-point scale with half-increments)
- **Scale**: 1 (Major Issues) to 5 (Excellent)
- **Evaluation focus**: Scientific rigor, claim support, methodological validity
- **Key guidance**: For experimental papers, assess "depth and/or breadth of research questions," technical soundness, and evaluation methodology. Position papers should adequately represent field state.

### 2. **Excitement** (5-point scale with half-increments)
- **Scale**: 1 (Not Exciting) to 5 (Highly Exciting)
- **Nature**: "Excitement is subjective and does not necessarily follow what is popular"
- **Factors**: Conceptual breakthroughs, evidence challenging assumptions, community impact, personal relevance to reviewer

### 3. **Overall Assessment** (7-point scale)
- **Scale**: 1 (Do not resubmit) to 5 (Consider for Award)
- **Key decision points**: Award consideration, Conference acceptance, Findings track, Resubmission recommendations
- **Guidance**: "Outstanding papers should be either fascinating, controversial, surprising, impressive, or potentially field-changing"

## Supplementary Evaluation Areas

- Reviewer Confidence (5-point scale)
- Reproducibility (5-point scale)
- Datasets value (5-point scale, if applicable)
- Software value (5-point scale, if applicable)
- Limitations and societal impact assessment
- Ethical concerns review

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4777
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-17T14:19:12.160515+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-17T14:19:12.160865+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-17T14:22:10.074818+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 3 Review — Reviewer 1 (方法严谨性 + 实验有效性)\n\n**Paper**: ContamCal: Calibrating Contaminated Benchmarks via Item Response Theory\n**Venue**: EMNLP 2026 (ARR May 2026)\n\n---\n\n## 1. Summary\n\n本文提出 ContamCal，通过 RRF 信号融合 + 2PL+γ IRT 模型对受污染 benchmark 进行校准。核心发现是 IRT ability estimation 本身提供了主要校准收益（ARC MAE 降低 53%），独立于 γ 是否被建模。实验在 Qwen2.5 (0.5B/1.5B/3B) 和 Llama-3.2-3B 上进行 SFT 注入实验。论文自 R1/R2 以来在叙事重构方面有显著改善（从\"γ 是核心\"转向\"IRT 分解\"），但核心统计和实验问题仍未完全解决。\n\n---\n\n## 2. Strengths\n\n**S1. 研究问题定位准确且有价值。** 桥接检测信号与计量理论框架的思路填补了真实空白。Introduction (§1) 对现有方法的定位清晰：检测方法止于 binary flags，IRT 方法忽略污染，DCR 缺乏 UQ。\n\n**S2. 诚实报告负面结果。** 论文坦承：(1) γ pooled 不显著 (§5.4)，(2) CI 覆盖不足 (§5.1)，(3) GSM8K 过度矫正 (§5.1)，(4) Min-K\\%++ 方向性逆转 (§5.2)。这种诚实在投稿论文中难能可贵。\n\n**S3. Simulation study 为方法论贡献提供了独立价值。** Figure 2 的 identifiability boundary map (AUC × J) 对社区具有参考意义，量化了\"多少模型才够\"的问题。\n\n**S4. Signal failure mode 发现有实际意义。** Min-K\\%++ 在 0.5B 的方向性逆转 (Cohen's d = -1.55 to -1.98) 是对从业者的重要警告，该发现独立于 ContamCal 框架有效。\n\n**S5. 跨家族验证尝试（尽管 N 不足）。** 从 R1/R2 的纯 Qwen 分析扩展到 Llama-3.2，且正确标注为\"exploratory\"。\n\n---\n\n## 3. Weaknesses\n\n### Must-Fix (影响接收决定)\n\n**N1 [Critical] Title/Abstract 与核心发现仍存在 framing 张力**\n\n- 具体位置：Title, Abstract (line 1-2), Contributions list (§1)\n- 问题：论文标题\"ContamCal: Calibrating Contaminated Benchmarks via IRT\"和方法名暗示 contamination-specific modeling 是核心贡献。但实验证明 B3-Vanilla2PL（无 γ）在所有 benchmark 上达到相当甚至更优的校准（ARC: B3 MAE=0.016 < ContamCal 0.020）。Abstract 首句仍写\"existing approaches stop at detection without quantifying how much scores are inflated\"，暗示 ContamCal 解决了这个问题，但 γ 在 8/8 MMLU 域中仅 1 个显著，pooled 不显著。\n- 与 R2-N1 对比：论文已显著改善叙事（加入\"decomposition result\"），但 Title 和 Contribution 1 的措辞仍让读者期待 γ 带来校准收益，而非\"γ 不贡献校准但提供诊断\"。\n- 建议：Title 改为强调 IRT calibration 而非 contamination-specific correction（例：\"IRT-Based Calibration of Contaminated LLM Benchmarks: Ability Estimation Suffices\"）。或在 Abstract 第三句明确写出\"γ does not improve calibration beyond vanilla IRT\"。\n\n**N2 [Critical] CI 覆盖率报告不完整，UQ claim 缺乏支撑**\n\n- 具体位置：§4.3 claims \"credible interval coverage at 50%, 80%, and 95% levels\" as metric; §5.1 only reports 50% CI (~35%)\n- 问题：论文在 experimental setup 中列出三个 CI 覆盖率级别作为评估指标，但 results 仅报告 50% level 且承认严重不足（35% vs 50% nominal）。80% 和 95% 覆盖率完全缺失。Abstract 和 Contribution 1 都 claim \"credible intervals\"作为方法优势，但实证表明这些 CI 系统性过窄。如果 50% CI 仅覆盖 35%，95% CI 可能仅覆盖 ~70%，这对 UQ claim 是致命打击。\n- 与 R2-N2 状态：未修复。仍只报告 50% level。\n- 建议：必须报告全部三个 level 的覆盖率。如果 95% CI 也显著低于 nominal，需要 (a) 讨论 posterior mis-specification 的可能原因（prior misfit? model misspecification? thin tails?），(b) 调整论文 claim——不能同时声称 UQ 是优势又承认 CI 不准。\n\n**N3 [Critical] Within-family ARC PPP 值缺失，疑似隐藏 misfit**\n\n- 具体位置：§5.1 \"ARC passes gating\" — 仅报告 MAE 和 γ CI，未给 PPP\n- 问题：Cross-family ARC PPP=0.45（Table 3，可接受），但 R1 发现 within-family J=13 ARC PPP=0.003，表明模型在 within-family 分析中存在系统性 misfit。论文结果部分对 within-family ARC PPP 完全沉默。如果 PPP=0.003 仍然成立，则§5.1 声称\"ARC passes gating\"是误导性的——ARC 的 γ 显著性可能是 model misfit 的 artifact 而非真实 contamination effect。\n- 与 R1-A1 状态：未修复。PPP 值仍未在 within-family results 中报告。\n- 建议：显式报告 within-family ARC PPP。如果确实 < 0.05，必须讨论 (a) 2PL+γ 对 ARC 的 fit adequacy，(b) γ 显著性是否受 misfit 影响，(c) 是否需要 4PL 或其他 specification。\n\n**N4 [Critical] J=13 自证 underpowered 的内在矛盾未解决**\n\n- 具体位置：§3.4 establishes J≥50 threshold; §5.3 operates at J=13; Contribution 4 claims \"identifiability boundaries and domain-level diagnosis\"\n- 问题：论文自己的 simulation study 证明 reliable γ recovery 需要 J≥50 (Figure 2)。在 J=13 下，8/8 MMLU 域中仅 1 个 γ 显著。论文已加\"exploratory\"标签，但 Contribution 4 仍作为主要贡献列出\"domain-level diagnosis\"。这构成逻辑矛盾：一个 contribution 声称方法可以做 domain-level diagnosis，另一个 contribution 证明当前数据量做不到。\n- 与 R2-N4 状态：部分改善（加了\"exploratory\"）但核心矛盾未解。\n- 建议：将 Contribution 4 重新措辞，明确区分 simulation-derived boundary（方法论贡献）和 empirical domain analysis（underpowered 探索性结果）。不应将两者合并为单一 contribution。\n\n**N5 [Critical] Baseline 配置不一致构成 cherry-picking 风险**\n\n- 具体位置：Table 4 (main, J=13, 1.5B+3B) vs Table 5 (appendix, J=8, 0.5B+1.5B ARC) vs Table 6 (appendix, 0.5B GSM8K)\n- 问题：\n  (a) 主表展示 ContamCal 最优结果的配置 (J=13)，附录展示不同配置下的完整 baseline。附录 ARC 表 (J=8) 中 ContamCal 4PL+γ MAE=0.035，比主表的 0.020 差 75%。附录 GSM8K (0.5B) 中 B0-Raw MAE=0.003 而 ContamCal MAE=0.020，即 ContamCal 使校准恶化 6.7×。\n  (b) DCR 报告 MAE=0.245 (ARC) 和 0.263 (GSM8K)，论文声称\"no public implementation\"（§4.4: \"qualitative comparison\"），但附录给出精确数字。这些数字来源不明。如果是自行实现，应说明实现细节和超参数；如果来自 DCR 原文，应注明不同实验条件下的比较公平性。\n  (c) §5.1 声称\"GSM8K overcorrection ratio is 11×\"但未解释具体来源——是 J=13 分析中的什么结果导致 11× overcorrection？\n- 与 R2-N5 状态：DCR 数值已呈现但来源仍不明。\n- 建议：(a) 主表应包含全部 7 个 baseline 在统一配置下的结果，或明确说明为何不同 baseline 需要不同配置。(b) DCR 数字必须注明来源。(c) GSM8K 0.5B overcorrection 应在 Discussion 中作为方法适用边界讨论。\n\n**N6 [Critical] Oracle Exposure Ablation 仍然缺失**\n\n- 具体位置：整篇论文\n- 问题：论文拥有 ground-truth injection labels（精确知道哪些 items 被注入），但从未用这些作为 oracle e_{ij}（注入=1，未注入=0）运行 IRT 模型。这个零成本消融实验能回答关键问题：\"如果检测信号完美（AUC=1.0），γ 在 J=13 下是否变得显著？\"如果 oracle exposure 下 γ 仍不显著，说明 underpowered 是 J 不足导致；如果显著，说明 RRF 信号质量是瓶颈。这直接关系到论文 Contribution 2（信号融合）的价值论证。\n- 与 R2-W2 状态：未修复，升级为 Critical——因为该实验零成本且直接回答核心争议。\n- 建议：添加 Oracle Exposure 消融，报告 (a) oracle γ 显著性，(b) oracle MAE，(c) oracle CI coverage。\n\n### Should-Fix (影响评分但不一票否决)\n\n**W1 [Warning] 46% 排除率缺乏 sensitivity analysis**\n\n- 具体位置：§4.1, Appendix C\n- 问题：24 models → 13 (46% exclusion)。排除理由：0.5B position bias（合理）+ 3B pipeline bugs（工程问题非科学理由）。Appendix C 的排除细节提到\"mismatched naming conventions\"和\"inconsistent hyperparameters\"——这些是执行错误，不是系统性设计选择。论文未提供 sensitivity analysis 说明：如果包含被排除的 3B 模型（即使数据不完美），结论是否改变？\n- 与 R2-N3 状态：Appendix C 新增了排除细节，但仍无 sensitivity analysis。\n- 建议：至少报告 J=16 (包含所有 3B) 或 J=21 (包含 0.5B for GSM8K) 下的 key metrics 对比。\n\n**W2 [Warning] Independent per-domain fitting 破坏 θ common scale**\n\n- 具体位置：§3.2 \"Each stratum is fitted independently\"\n- 问题：独立 per-domain fitting 意味着不同域的 θ 不在同一 scale 上。Table 2 的跨域 γ 比较（Math +0.50 vs Social Sci -0.57）在统计上不严谨，因为 γ 的 scale 依赖于 domain-specific θ 和 a_i 参数。论文声称\"STEM domains show positive γ while Humanities are negative\"暗示了跨域比较，但独立 fitting 下这种比较缺乏统计基础。\n- 与 R2-W4 状态：未修复。\n- 建议：要么 (a) 使用共同 θ scale（hierarchical model 或 linking），要么 (b) 在 Discussion 中明确声明跨域 γ 的 magnitude 不可直接比较，只有 sign 和 significance 有意义。\n\n**W3 [Warning] Cross-family validation 统计 power 不足以支撑\"泛化\"claim**\n\n- 具体位置：§4.2 (N=4, single seed), §5.5 cross-family results\n- 问题：Llama-3.2-3B 仅 4 models (single seed)，MMLU 排除 d100 后仅 3 个 data points。论文已标注\"exploratory\"，但 Contribution 1 仍写 \"validated across two model families (Qwen2.5 and Llama-3.2, up to J=28)\"。\"Validated\"一词对 single-seed N=3-4 数据过于强烈。Cross-family J=28 (Table 3, GSM8K) 包含大量 Qwen 模型，Llama 贡献仅 4/28=14%。\n- 与 R1-C2 状态：改善（加了 exploratory 和 power calculation reference），但 Contribution 措辞仍 overclaim。\n- 建议：Contribution 1 中将\"validated\"替换为\"tested exploratorily\"或\"preliminary evidence from\"。\n\n**W4 [Warning] Additive γ 线性结构未经验证**\n\n- 具体位置：Eq. 4 (§3.2)\n- 问题：Eq. 4 假设 contamination effect 是 additive linear in e_{ij}。但污染效应可能是非线性的——低暴露无影响，高暴露饱和。论文未提供任何 linearity 检验（如残差分析、非参数替代比较）。如果真实效应是 threshold-like，linear γ 会被 averaged down 导致不显著。\n- 建议：在 Discussion/Limitations 中加入 additive linearity assumption 的讨论。最好提供残差 vs exposure 的散点图或 GAM 拟合作为诊断。\n\n**W5 [Warning] SFT injection 生态效度限制讨论不足**\n\n- 具体位置：Limitations §A \"Single injection protocol\"\n- 问题：LoRA SFT injection 与真实 pretraining contamination 存在根本差异：(a) SFT 在 representation space 已形成后注入，pretraining leakage 在形成过程中发生；(b) SFT 格式化为 instruction-response pairs，pretraining 是 raw text；(c) 0.5B 的 catastrophic 行为（position bias）可能是 SFT-specific artifact。Limitations 仅一句带过。\n- 建议：扩展 Limitations 讨论，明确哪些发现预期能推广到 pretraining contamination，哪些可能是 SFT-specific。\n\n---\n\n## 4. Questions\n\n**Q1.** Within-family ARC PPP 值具体是多少？如果 PPP < 0.05，如何解释\"ARC passes gating\"？\n\n**Q2.** §5.1 提到\"GSM8K overcorrection ratio is 11×\"。这是指什么配置下的什么比率？ContamCal MAE / B0-Raw MAE 在主表中是 0.006/0.169 ≈ 0.035，不是 11×。如果指附录 0.5B 配置 (0.020/0.003 ≈ 6.7×)，也不是 11×。请澄清。\n\n**Q3.** DCR 的 MAE=0.245/0.263 如何获得？是自行实现 DCR、从原论文数据推算、还是在相同实验条件下重新运行？\n\n**Q4.** 如果用 oracle exposure (ground-truth injection labels) 替代 RRF scores，γ 显著性和 CI coverage 如何变化？\n\n**Q5.** Cross-family pooling 时 θ scale identification 如何处理？是否有 linking 或 anchor items？Table 3 的 J=28 (GSM8K) 中 Qwen 和 Llama 的 θ 是否在同一 scale 上？\n\n**Q6.** Contribution 1 声称\"up to J=28\"——这个 J=28 仅在 GSM8K cross-family 中出现。MMLU (J=18) 和 ARC (J=20) 的 cross-family 结果是否同样支撑 MAE < 0.02 的 claim？（Table 3 confirms yes, 但需要明确 MMLU J=18 中 Llama 仅贡献 3/18=17%）。\n\n---\n\n## 5. Missing References\n\n- **Chalmers (2012), mirt R package**: 多维 IRT 的标准实现，Discussion 提到 multidimensional IRT 但未引用\n- **Bock & Aitkin (1981), Marginal Maximum Likelihood**: IRT 参数估计的经典方法，与 Bayesian 估计的对比值得引用\n- **Kolen & Brennan (2014), Test Equating**: 关于 θ scale linking 的权威参考，直接相关于 W2 的 common scale 问题\n- **Roberts et al. (2024), Contamination in the Wild**: 如果存在关于 pretraining-stage contamination 特征的实证研究，应引用以支撑 ecological validity 讨论\n\n---\n\n## 6. Overall Assessment\n\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5 (High — 方法论和统计分析是我的核心专长)\n\n**理由**：\n\n论文提出了一个有意义的研究问题，且\"IRT 本身提供校准收益\"是一个 clean finding。诚实报告负面结果值得肯定。但存在多个结构性问题阻止 main conference 接收：\n\n(1) Title/framing 与核心发现不匹配——方法名暗示 contamination-specific calibration 是贡献，但 γ 不贡献校准；\n(2) 统计基础不完整——CI coverage 报告不全，within-family ARC PPP 缺失，UQ claims 缺乏实证支撑；\n(3) 自证 underpowered——J=13 远低于自己建立的 J≥50 threshold，domain-level γ diagnosis 缺乏 power；\n(4) Oracle ablation 缺失——ground-truth labels 在手却未用作 ablation，留下关键因果问题未回答；\n(5) Baseline 比较公平性存疑——主表和附录使用不同配置，DCR 来源不明。\n\n如果解决 N1 (reframe title/claims), N2 (report full CI coverage), N3 (report ARC PPP), N6 (add oracle ablation)，论文可以达到 3.5 (Borderline Conference)。当前版本的核心贡献（IRT calibration works for contaminated benchmarks）是成立的，但包装和证据链的完整性不足以支撑 main conference。\n\n---\n\n## 7. Detailed Comments by Section\n\n### Abstract\n- \"fuses multiple detection signals\" — 实际上 RRF 在 0.5B 退化为 S1-only（§5.2），\"multiple signals\"仅在 1.5B+ 有效\n- \"contamination parameter γ provides complementary diagnostic value\" — 准确但弱化了——8/8 只有 1 个显著，读者会问\"那还有什么价值？\"\n- \"Social Sciences reaching significance (γ = -0.57, CI excluding zero)\" — 在 8 个独立检验中仅 1 个显著，未做多重比较校正（Bonferroni 下 α=0.00625，可能不再显著）\n\n### Introduction\n- 段落结构清晰，从 problem → urgency → gap → our approach → contributions 的叙事线完整\n- 但 Contribution 1 \"validated across two model families\" overclaims（见 W3）\n- Contribution 4 将 simulation boundary 和 empirical diagnosis 混为一谈（见 N4）\n\n### Method (§3)\n- 技术上 sound，priors 选择标准，convergence criteria 合理（split-R̂ < 1.01, ESS > 400）\n- Eq. 4 的 additive structure 清楚但 linearity 未经验证（W4）\n- RRF 设计 justification 充分（避免 meta-circularity）\n- §3.4 Fisher information 讨论为 identifiability claim 提供理论基础\n\n### Experimental Setup (§4)\n- LoRA 参数清楚 (α=32, r=16, lr=5e-5)\n- 排除理由在 Appendix C 中可见但属工程错误非设计选择\n- \"GSM8K retains all scales\" 与主表 J=13 配置的关系不清楚——是否 GSM8K 主分析也限于 1.5B+3B？\n\n### Results (§5)\n- Table 4 清楚展示 decomposition：B3 ≈ ContamCal on calibration\n- 但缺失关键信息：within-family ARC PPP，80%/95% CI coverage\n- §5.1 的 \"overcorrection ratio is 11×\" 出处不明\n\n### Discussion\n- Limitations 列了 7 条，覆盖面广\n- 但缺少：(a) 方法何时不应使用（GSM8K 0.5B case），(b) additive linearity limitation，(c) within-family ARC misfit 的 implication\n\n### Appendix\n- Table 5 (ARC J=8) 中 B3-Vanilla4PL MAE=0.071 表明 4PL 在小 J 下不稳定——与 §A.2 的\"J≥16 for 4PL\"一致\n- Table 6 (GSM8K 0.5B) 暴露了 ContamCal 在 well-calibrated data 上的 overcorrection 问题\n\n---\n\n## R1-R2 Open Issues 状态总结\n\n| Issue | Status | 评估 |\n|-------|--------|------|\n| R2-N1 γ无校准收益 framing | 部分修复 | Title 仍 misleading，Contributions 措辞需调整 |\n| R2-N2 CI 覆盖 | 未修复 | 仍只报告 50% level |\n| R2-N3 46% 排除率 | 部分修复 | 加了 Appendix C 细节，无 sensitivity analysis |\n| R2-N4 J=13 vs J≥50 | 部分修复 | 加了\"exploratory\"标签，但 Contribution 4 矛盾仍在 |\n| R2-N5 DCR 比较 | 部分修复 | 有数值，来源不明 |\n| R2-W2 Oracle ablation | 未修复 | 升级为 Critical |\n| R2-W4 θ common scale | 未修复 | |\n| R1-A1 ARC PPP=0.003 | 未修复 | Within-family PPP 未报告 |\n| R1-C2 Cross-family N=3-4 | 部分修复 | 加了 exploratory + power ref，但 Contribution 1 overclaims |\n\n---\n\n## ARR 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 方法论框架 sound，但 CI 不准、ARC PPP 缺失、oracle ablation 缺位削弱了统计结论的可信度 |\n| Excitement | 3/5 | 问题有价值，\"IRT alone suffices\"是 clean insight，但 γ 贡献微弱限制了影响力 |\n| Reproducibility | 3.5/5 | Hyperparams 清晰，Stan 模型可复现，但 DCR 不可复现，排除标准涉及工程 bugs 难以系统化 |\n| Overall | 3.0 | Findings track — 有价值的探索性研究，需要更完整的统计证据和更准确的 framing |",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 3 Review — Reviewer 1 (方法严谨性 + 实验有效性)\n\n**Paper**: ContamCal: Calibrating Contaminated Benchmarks via Item Response Theory\n**Venue**: EMNLP 2026 (ARR May 2026)\n\n---\n\n## 1. Summary\n\n本文提出 ContamCal，通过 RRF 信号融合 + 2PL+γ IRT 模型对受污染 benchmark 进行校准。核心发现是 IRT ability estimation 本身提供了主要校准收益（ARC MAE 降低 53%），独立于 γ 是否被建模。实验在 Qwen2.5 (0.5B/1.5B/3B) 和 Llama-3.2-3B 上进行 SFT 注入实验。论文自 R1/R2 以来在叙事重构方面有显著改善（从\"γ 是核心\"转向\"IRT 分解\"），但核心统计和实验问题仍未完全解决。\n\n---\n\n## 2. Strengths\n\n**S1. 研究问题定位准确且有价值。** 桥接检测信号与计量理论框架的思路填补了真实空白。Introduction (§1) 对现有方法的定位清晰：检测方法止于 binary flags，IRT 方法忽略污染，DCR 缺乏 UQ。\n\n**S2. 诚实报告负面结果。** 论文坦承：(1) γ pooled 不显著 (§5.4)，(2) CI 覆盖不足 (§5.1)，(3) GSM8K 过度矫正 (§5.1)，(4) Min-K\\%++ 方向性逆转 (§5.2)。这种诚实在投稿论文中难能可贵。\n\n**S3. Simulation study 为方法论贡献提供了独立价值。** Figure 2 的 identifiability boundary map (AUC × J) 对社区具有参考意义，量化了\"多少模型才够\"的问题。\n\n**S4. Signal failure mode 发现有实际意义。** Min-K\\%++ 在 0.5B 的方向性逆转 (Cohen's d = -1.55 to -1.98) 是对从业者的重要警告，该发现独立于 ContamCal 框架有效。\n\n**S5. 跨家族验证尝试（尽管 N 不足）。** 从 R1/R2 的纯 Qwen 分析扩展到 Llama-3.2，且正确标注为\"exploratory\"。\n\n---\n\n## 3. Weaknesses\n\n### Must-Fix (影响接收决定)\n\n**N1 [Critical] Title/Abstract 与核心发现仍存在 framing 张力**\n\n- 具体位置：Title, Abstract (line 1-2), Contributions list (§1)\n- 问题：论文标题\"ContamCal: Calibrating Contaminated Benchmarks via IRT\"和方法名暗示 contamination-specific modeling 是核心贡献。但实验证明 B3-Vanilla2PL（无 γ）在所有 benchmark 上达到相当甚至更优的校准（ARC: B3 MAE=0.016 < ContamCal 0.020）。Abstract 首句仍写\"existing approaches stop at detection without quantifying how much scores are inflated\"，暗示 ContamCal 解决了这个问题，但 γ 在 8/8 MMLU 域中仅 1 个显著，pooled 不显著。\n- 与 R2-N1 对比：论文已显著改善叙事（加入\"decomposition result\"），但 Title 和 Contribution 1 的措辞仍让读者期待 γ 带来校准收益，而非\"γ 不贡献校准但提供诊断\"。\n- 建议：Title 改为强调 IRT calibration 而非 contamination-specific correction（例：\"IRT-Based Calibration of Contaminated LLM Benchmarks: Ability Estimation Suffices\"）。或在 Abstract 第三句明确写出\"γ does not improve calibration beyond vanilla IRT\"。\n\n**N2 [Critical] CI 覆盖率报告不完整，UQ claim 缺乏支撑**\n\n- 具体位置：§4.3 claims \"credible interval coverage at 50%, 80%, and 95% levels\" as metric; §5.1 only reports 50% CI (~35%)\n- 问题：论文在 experimental setup 中列出三个 CI 覆盖率级别作为评估指标，但 results 仅报告 50% level 且承认严重不足（35% vs 50% nominal）。80% 和 95% 覆盖率完全缺失。Abstract 和 Contribution 1 都 claim \"credible intervals\"作为方法优势，但实证表明这些 CI 系统性过窄。如果 50% CI 仅覆盖 35%，95% CI 可能仅覆盖 ~70%，这对 UQ claim 是致命打击。\n- 与 R2-N2 状态：未修复。仍只报告 50% level。\n- 建议：必须报告全部三个 level 的覆盖率。如果 95% CI 也显著低于 nominal，需要 (a) 讨论 posterior mis-specification 的可能原因（prior misfit? model misspecification? thin tails?），(b) 调整论文 claim——不能同时声称 UQ 是优势又承认 CI 不准。\n\n**N3 [Critical] Within-family ARC PPP 值缺失，疑似隐藏 misfit**\n\n- 具体位置：§5.1 \"ARC passes gating\" — 仅报告 MAE 和 γ CI，未给 PPP\n- 问题：Cross-family ARC PPP=0.45（Table 3，可接受），但 R1 发现 within-family J=13 ARC PPP=0.003，表明模型在 within-family 分析中存在系统性 misfit。论文结果部分对 within-family ARC PPP 完全沉默。如果 PPP=0.003 仍然成立，则§5.1 声称\"ARC passes gating\"是误导性的——ARC 的 γ 显著性可能是 model misfit 的 artifact 而非真实 contamination effect。\n- 与 R1-A1 状态：未修复。PPP 值仍未在 within-family results 中报告。\n- 建议：显式报告 within-family ARC PPP。如果确实 < 0.05，必须讨论 (a) 2PL+γ 对 ARC 的 fit adequacy，(b) γ 显著性是否受 misfit 影响，(c) 是否需要 4PL 或其他 specification。\n\n**N4 [Critical] J=13 自证 underpowered 的内在矛盾未解决**\n\n- 具体位置：§3.4 establishes J≥50 threshold; §5.3 operates at J=13; Contribution 4 claims \"identifiability boundaries and domain-level diagnosis\"\n- 问题：论文自己的 simulation study 证明 reliable γ recovery 需要 J≥50 (Figure 2)。在 J=13 下，8/8 MMLU 域中仅 1 个 γ 显著。论文已加\"exploratory\"标签，但 Contribution 4 仍作为主要贡献列出\"domain-level diagnosis\"。这构成逻辑矛盾：一个 contribution 声称方法可以做 domain-level diagnosis，另一个 contribution 证明当前数据量做不到。\n- 与 R2-N4 状态：部分改善（加了\"exploratory\"）但核心矛盾未解。\n- 建议：将 Contribution 4 重新措辞，明确区分 simulation-derived boundary（方法论贡献）和 empirical domain analysis（underpowered 探索性结果）。不应将两者合并为单一 contribution。\n\n**N5 [Critical] Baseline 配置不一致构成 cherry-picking 风险**\n\n- 具体位置：Table 4 (main, J=13, 1.5B+3B) vs Table 5 (appendix, J=8, 0.5B+1.5B ARC) vs Table 6 (appendix, 0.5B GSM8K)\n- 问题：\n  (a) 主表展示 ContamCal 最优结果的配置 (J=13)，附录展示不同配置下的完整 baseline。附录 ARC 表 (J=8) 中 ContamCal 4PL+γ MAE=0.035，比主表的 0.020 差 75%。附录 GSM8K (0.5B) 中 B0-Raw MAE=0.003 而 ContamCal MAE=0.020，即 ContamCal 使校准恶化 6.7×。\n  (b) DCR 报告 MAE=0.245 (ARC) 和 0.263 (GSM8K)，论文声称\"no public implementation\"（§4.4: \"qualitative comparison\"），但附录给出精确数字。这些数字来源不明。如果是自行实现，应说明实现细节和超参数；如果来自 DCR 原文，应注明不同实验条件下的比较公平性。\n  (c) §5.1 声称\"GSM8K overcorrection ratio is 11×\"但未解释具体来源——是 J=13 分析中的什么结果导致 11× overcorrection？\n- 与 R2-N5 状态：DCR 数值已呈现但来源仍不明。\n- 建议：(a) 主表应包含全部 7 个 baseline 在统一配置下的结果，或明确说明为何不同 baseline 需要不同配置。(b) DCR 数字必须注明来源。(c) GSM8K 0.5B overcorrection 应在 Discussion 中作为方法适用边界讨论。\n\n**N6 [Critical] Oracle Exposure Ablation 仍然缺失**\n\n- 具体位置：整篇论文\n- 问题：论文拥有 ground-truth injection labels（精确知道哪些 items 被注入），但从未用这些作为 oracle e_{ij}（注入=1，未注入=0）运行 IRT 模型。这个零成本消融实验能回答关键问题：\"如果检测信号完美（AUC=1.0），γ 在 J=13 下是否变得显著？\"如果 oracle exposure 下 γ 仍不显著，说明 underpowered 是 J 不足导致；如果显著，说明 RRF 信号质量是瓶颈。这直接关系到论文 Contribution 2（信号融合）的价值论证。\n- 与 R2-W2 状态：未修复，升级为 Critical——因为该实验零成本且直接回答核心争议。\n- 建议：添加 Oracle Exposure 消融，报告 (a) oracle γ 显著性，(b) oracle MAE，(c) oracle CI coverage。\n\n### Should-Fix (影响评分但不一票否决)\n\n**W1 [Warning] 46% 排除率缺乏 sensitivity analysis**\n\n- 具体位置：§4.1, Appendix C\n- 问题：24 models → 13 (46% exclusion)。排除理由：0.5B position bias（合理）+ 3B pipeline bugs（工程问题非科学理由）。Appendix C 的排除细节提到\"mismatched naming conventions\"和\"inconsistent hyperparameters\"——这些是执行错误，不是系统性设计选择。论文未提供 sensitivity analysis 说明：如果包含被排除的 3B 模型（即使数据不完美），结论是否改变？\n- 与 R2-N3 状态：Appendix C 新增了排除细节，但仍无 sensitivity analysis。\n- 建议：至少报告 J=16 (包含所有 3B) 或 J=21 (包含 0.5B for GSM8K) 下的 key metrics 对比。\n\n**W2 [Warning] Independent per-domain fitting 破坏 θ common scale**\n\n- 具体位置：§3.2 \"Each stratum is fitted independently\"\n- 问题：独立 per-domain fitting 意味着不同域的 θ 不在同一 scale 上。Table 2 的跨域 γ 比较（Math +0.50 vs Social Sci -0.57）在统计上不严谨，因为 γ 的 scale 依赖于 domain-specific θ 和 a_i 参数。论文声称\"STEM domains show positive γ while Humanities are negative\"暗示了跨域比较，但独立 fitting 下这种比较缺乏统计基础。\n- 与 R2-W4 状态：未修复。\n- 建议：要么 (a) 使用共同 θ scale（hierarchical model 或 linking），要么 (b) 在 Discussion 中明确声明跨域 γ 的 magnitude 不可直接比较，只有 sign 和 significance 有意义。\n\n**W3 [Warning] Cross-family validation 统计 power 不足以支撑\"泛化\"claim**\n\n- 具体位置：§4.2 (N=4, single seed), §5.5 cross-family results\n- 问题：Llama-3.2-3B 仅 4 models (single seed)，MMLU 排除 d100 后仅 3 个 data points。论文已标注\"exploratory\"，但 Contribution 1 仍写 \"validated across two model families (Qwen2.5 and Llama-3.2, up to J=28)\"。\"Validated\"一词对 single-seed N=3-4 数据过于强烈。Cross-family J=28 (Table 3, GSM8K) 包含大量 Qwen 模型，Llama 贡献仅 4/28=14%。\n- 与 R1-C2 状态：改善（加了 exploratory 和 power calculation reference），但 Contribution 措辞仍 overclaim。\n- 建议：Contribution 1 中将\"validated\"替换为\"tested exploratorily\"或\"preliminary evidence from\"。\n\n**W4 [Warning] Additive γ 线性结构未经验证**\n\n- 具体位置：Eq. 4 (§3.2)\n- 问题：Eq. 4 假设 contamination effect 是 additive linear in e_{ij}。但污染效应可能是非线性的——低暴露无影响，高暴露饱和。论文未提供任何 linearity 检验（如残差分析、非参数替代比较）。如果真实效应是 threshold-like，linear γ 会被 averaged down 导致不显著。\n- 建议：在 Discussion/Limitations 中加入 additive linearity assumption 的讨论。最好提供残差 vs exposure 的散点图或 GAM 拟合作为诊断。\n\n**W5 [Warning] SFT injection 生态效度限制讨论不足**\n\n- 具体位置：Limitations §A \"Single injection protocol\"\n- 问题：LoRA SFT injection 与真实 pretraining contamination 存在根本差异：(a) SFT 在 representation space 已形成后注入，pretraining leakage 在形成过程中发生；(b) SFT 格式化为 instruction-response pairs，pretraining 是 raw text；(c) 0.5B 的 catastrophic 行为（position bias）可能是 SFT-specific artifact。Limitations 仅一句带过。\n- 建议：扩展 Limitations 讨论，明确哪些发现预期能推广到 pretraining contamination，哪些可能是 SFT-specific。\n\n---\n\n## 4. Questions\n\n**Q1.** Within-family ARC PPP 值具体是多少？如果 PPP < 0.05，如何解释\"ARC passes gating\"？\n\n**Q2.** §5.1 提到\"GSM8K overcorrection ratio is 11×\"。这是指什么配置下的什么比率？ContamCal MAE / B0-Raw MAE 在主表中是 0.006/0.169 ≈ 0.035，不是 11×。如果指附录 0.5B 配置 (0.020/0.003 ≈ 6.7×)，也不是 11×。请澄清。\n\n**Q3.** DCR 的 MAE=0.245/0.263 如何获得？是自行实现 DCR、从原论文数据推算、还是在相同实验条件下重新运行？\n\n**Q4.** 如果用 oracle exposure (ground-truth injection labels) 替代 RRF scores，γ 显著性和 CI coverage 如何变化？\n\n**Q5.** Cross-family pooling 时 θ scale identification 如何处理？是否有 linking 或 anchor items？Table 3 的 J=28 (GSM8K) 中 Qwen 和 Llama 的 θ 是否在同一 scale 上？\n\n**Q6.** Contribution 1 声称\"up to J=28\"——这个 J=28 仅在 GSM8K cross-family 中出现。MMLU (J=18) 和 ARC (J=20) 的 cross-family 结果是否同样支撑 MAE < 0.02 的 claim？（Table 3 confirms yes, 但需要明确 MMLU J=18 中 Llama 仅贡献 3/18=17%）。\n\n---\n\n## 5. Missing References\n\n- **Chalmers (2012), mirt R package**: 多维 IRT 的标准实现，Discussion 提到 multidimensional IRT 但未引用\n- **Bock & Aitkin (1981), Marginal Maximum Likelihood**: IRT 参数估计的经典方法，与 Bayesian 估计的对比值得引用\n- **Kolen & Brennan (2014), Test Equating**: 关于 θ scale linking 的权威参考，直接相关于 W2 的 common scale 问题\n- **Roberts et al. (2024), Contamination in the Wild**: 如果存在关于 pretraining-stage contamination 特征的实证研究，应引用以支撑 ecological validity 讨论\n\n---\n\n## 6. Overall Assessment\n\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5 (High — 方法论和统计分析是我的核心专长)\n\n**理由**：\n\n论文提出了一个有意义的研究问题，且\"IRT 本身提供校准收益\"是一个 clean finding。诚实报告负面结果值得肯定。但存在多个结构性问题阻止 main conference 接收：\n\n(1) Title/framing 与核心发现不匹配——方法名暗示 contamination-specific calibration 是贡献，但 γ 不贡献校准；\n(2) 统计基础不完整——CI coverage 报告不全，within-family ARC PPP 缺失，UQ claims 缺乏实证支撑；\n(3) 自证 underpowered——J=13 远低于自己建立的 J≥50 threshold，domain-level γ diagnosis 缺乏 power；\n(4) Oracle ablation 缺失——ground-truth labels 在手却未用作 ablation，留下关键因果问题未回答；\n(5) Baseline 比较公平性存疑——主表和附录使用不同配置，DCR 来源不明。\n\n如果解决 N1 (reframe title/claims), N2 (report full CI coverage), N3 (report ARC PPP), N6 (add oracle ablation)，论文可以达到 3.5 (Borderline Conference)。当前版本的核心贡献（IRT calibration works for contaminated benchmarks）是成立的，但包装和证据链的完整性不足以支撑 main conference。\n\n---\n\n## 7. Detailed Comments by Section\n\n### Abstract\n- \"fuses multiple detection signals\" — 实际上 RRF 在 0.5B 退化为 S1-only（§5.2），\"multiple signals\"仅在 1.5B+ 有效\n- \"contamination parameter γ provides complementary diagnostic value\" — 准确但弱化了——8/8 只有 1 个显著，读者会问\"那还有什么价值？\"\n- \"Social Sciences reaching significance (γ = -0.57, CI excluding zero)\" — 在 8 个独立检验中仅 1 个显著，未做多重比较校正（Bonferroni 下 α=0.00625，可能不再显著）\n\n### Introduction\n- 段落结构清晰，从 problem → urgency → gap → our approach → contributions 的叙事线完整\n- 但 Contribution 1 \"validated across two model families\" overclaims（见 W3）\n- Contribution 4 将 simulation boundary 和 empirical diagnosis 混为一谈（见 N4）\n\n### Method (§3)\n- 技术上 sound，priors 选择标准，convergence criteria 合理（split-R̂ < 1.01, ESS > 400）\n- Eq. 4 的 additive structure 清楚但 linearity 未经验证（W4）\n- RRF 设计 justification 充分（避免 meta-circularity）\n- §3.4 Fisher information 讨论为 identifiability claim 提供理论基础\n\n### Experimental Setup (§4)\n- LoRA 参数清楚 (α=32, r=16, lr=5e-5)\n- 排除理由在 Appendix C 中可见但属工程错误非设计选择\n- \"GSM8K retains all scales\" 与主表 J=13 配置的关系不清楚——是否 GSM8K 主分析也限于 1.5B+3B？\n\n### Results (§5)\n- Table 4 清楚展示 decomposition：B3 ≈ ContamCal on calibration\n- 但缺失关键信息：within-family ARC PPP，80%/95% CI coverage\n- §5.1 的 \"overcorrection ratio is 11×\" 出处不明\n\n### Discussion\n- Limitations 列了 7 条，覆盖面广\n- 但缺少：(a) 方法何时不应使用（GSM8K 0.5B case），(b) additive linearity limitation，(c) within-family ARC misfit 的 implication\n\n### Appendix\n- Table 5 (ARC J=8) 中 B3-Vanilla4PL MAE=0.071 表明 4PL 在小 J 下不稳定——与 §A.2 的\"J≥16 for 4PL\"一致\n- Table 6 (GSM8K 0.5B) 暴露了 ContamCal 在 well-calibrated data 上的 overcorrection 问题\n\n---\n\n## R1-R2 Open Issues 状态总结\n\n| Issue | Status | 评估 |\n|-------|--------|------|\n| R2-N1 γ无校准收益 framing | 部分修复 | Title 仍 misleading，Contributions 措辞需调整 |\n| R2-N2 CI 覆盖 | 未修复 | 仍只报告 50% level |\n| R2-N3 46% 排除率 | 部分修复 | 加了 Appendix C 细节，无 sensitivity analysis |\n| R2-N4 J=13 vs J≥50 | 部分修复 | 加了\"exploratory\"标签，但 Contribution 4 矛盾仍在 |\n| R2-N5 DCR 比较 | 部分修复 | 有数值，来源不明 |\n| R2-W2 Oracle ablation | 未修复 | 升级为 Critical |\n| R2-W4 θ common scale | 未修复 | |\n| R1-A1 ARC PPP=0.003 | 未修复 | Within-family PPP 未报告 |\n| R1-C2 Cross-family N=3-4 | 部分修复 | 加了 exploratory + power ref，但 Contribution 1 overclaims |\n\n---\n\n## ARR 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 方法论框架 sound，但 CI 不准、ARC PPP 缺失、oracle ablation 缺位削弱了统计结论的可信度 |\n| Excitement | 3/5 | 问题有价值，\"IRT alone suffices\"是 clean insight，但 γ 贡献微弱限制了影响力 |\n| Reproducibility | 3.5/5 | Hyperparams 清晰，Stan 模型可复现，但 DCR 不可复现，排除标准涉及工程 bugs 难以系统化 |\n| Overall | 3.0 | Findings track — 有价值的探索性研究，需要更完整的统计证据和更准确的 framing |",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-17T14:22:13.992607+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3917
}
```

</details>

---


### Assistant

_source line 134 · 2026-05-17T14:22:22.761003+00:00_

Round 3 审稿已提交给 Director。

核心判断：**Overall 3.0 (Findings)**。论文的"IRT alone suffices for calibration"是有价值的发现，诚实报告负面结果值得肯定。但六个 Critical 问题阻止 main conference 接收：

1. Title/framing 仍暗示 γ 是核心贡献，与实验结果矛盾
2. CI coverage 仅报告 50% level（35% 实际覆盖），80%/95% 缺失
3. Within-family ARC PPP 疑似 0.003 但未报告
4. J=13 自证 underpowered 与 Contribution 4 的 domain diagnosis claim 矛盾
5. Baseline 配置不一致，DCR 来源不明
6. Oracle Exposure 消融（零成本）缺失，关键因果问题未回答

R1-R2 的 9 个 open issues 中仅 0 个完全修复，5 个部分修复，4 个未修复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 6

## Round 6

16 recorded events


### User

_source line 135 · 2026-05-17T14:27:02.950223+00:00_

[Round 3 审稿请求]:
## 交叉分享 — 请回应 Reviewer 2 的完整审稿意见

以下是 Reviewer 2 的 Round 3 完整审稿意见。请逐条回应：对每个 Weakness/Question，标注 [AGREE] 并说明理由，或 [REBUT] 并提供具体证据（cite Section/Table/Figure）。

---

## Reviewer 2 审稿意见原文

**Overall**: 2.5 / 5 (Borderline Findings)
**一句话总结**: 论文提出了一个有原则的 IRT+contamination 框架，但核心发现（vanilla 2PL 已够用）与标题/framing 的 contamination-aware 叙事存在根本张力，加之格式合规问题构成 desk reject 风险，当前版本不适合主会议接收。

**ARR 维度打分**: Soundness 3.0, Excitement 2.5, Reproducibility 3.5, Overall 2.5, Confidence 4/5

**Strengths**:
- S1: 问题定位精准，桥接 detection 和 calibration 两条研究线
- S2: 诚实报告 negative results（GSM8K 11× overcorrection, CI under-coverage, γ collapse）
- S3: Min-K%++ 方向性反转（Cohen's d = -1.55 to -1.98）有实际影响力
- S4: Bayesian 推断流程规范（NUTS, split-R̂, ESS, PPP, Fisher information）
- S5: Cross-family validation 增强 θ calibration 可信度

**Must-Fix**:

**N1 [critical]** Title/Abstract 与核心发现的根本矛盾（遗留 R2-N1，未修复）
- Title 暗示 contamination-aware calibration 是关键，但 B3-Vanilla2PL(γ=0) 在 ARC 上 MAE=0.016 优于 ContamCal 的 0.020
- 建议重新定位 title 和 framing，以 "IRT decomposition" 为主线

**N2 [critical]** ARR 格式不合规——Desk reject 风险（遗留 R2-N6，未修复）
- Limitations 在 appendix 中、references 之后，违反 ARR 要求
- 全文无 Ethics Statement / Ethical Considerations
- 两个问题均为 desk reject 级别

**N3 [critical]** 贡献新颖性不足
- IRT for LLM eval 已有 TinyBenchmarks/Growing Pains/HiBayES/ATLAS/PSN-IRT（PSN-IRT 在 bib 中但未引用）
- Contribution 1 是 empirical observation 而非 method contribution
- Contribution 2 (RRF) 退化为 S1-only
- 真正有独立价值的是 Contribution 3-4，但更适合 short paper / Findings

**Should-Fix**:
- W1: 主表仅 3/7 baselines，信息密度低（R2-W5 未修复）
- W2: Related Work 仅 3 段 ~40 行，缺 PSN-IRT/Kocyigit/Yang/Zhang 等直接相关引用；bib 91 entries 仅 cite 33（R2-W8 部分修复）
- W3: LoRA SFT ≠ pretraining contamination，生态效度不足（R2-W6）
- W4: Discussion ~10 行，Conclusion ~5 行，对 long paper 过于简短
- W5: GSM8K 11× 过校正无实践决策规则（R2-W7 未修复）
- W6: RRF→S1-only 但 Contribution 2 声明未调整（R2-W1）
- W7: Appendix baseline tables 使用不同实验配置（J=8/0.5B vs 主文 J=13/1.5B+3B）

**Questions**:
- Q1: 如果 detection 不重要，Stage 1 的价值是什么？为什么不直接推荐 vanilla 2PL？
- Q2: Table 2 中 STEM domains γ 均为 +0.50 且 CI 几乎相同——是否存在共线性 artifact？
- Q3: Cross-family pooling 中 Llama 仅 J=3-4，严重不平衡是否影响 θ 估计？
- Q4: Qwen Δθ=+0.57 但 Llama Δθ≈+0.05，IRT 的 θ 是否被 contamination 污染？
- Q5: 50% CI 仅 35% 覆盖率——是否表明 local independence 假设违反导致 model misspecification？

**Missing References**: Zhou et al. PSN-IRT (AAAI 2026), Kocyigit et al. (NeurIPS 2025), Yang et al. inference-time decontamination (EMNLP Findings 2024), Zhang et al. decontamination (ICML 2025), Schaeffer et al. (2026), Holland and Wainer (1993) DIF。58 个 orphan bib entries 需清理。

---

请对 R2 的每个 Must-Fix (N1-N3)、Should-Fix (W1-W7)、Question (Q1-Q5) 逐条标注 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-17T14:27:56.931223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-17T14:27:57.283049+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{ContamCal: Calibrating Contaminated Benchmarks via\\Item Response Theory}
13	
14	\author{Anonymous}
15	
16	\begin{document}
17	\maketitle
18	
19	\begin{abstract}
20	\input{abstract}
21	\end{abstract}
22	
23	\input{introduction}
24	\input{related_work}
25	\input{method}
26	\input{experimental_setup}
27	\input{results}
28	\input{discussion}
29	\input{conclusion}
30	
31	\bibliography{references}
32	
33	\input{appendix}
34	
35	\end{document}
36	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-17T14:27:57.785287+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
  "offset": "87",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
    "offset": "87",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-17T14:27:58.287579+00:00_

87	\begin{table}[t]
88	\centering
89	\caption{Per-domain $\gamma$ estimates (2PL+$\gamma$, $J$=13 Qwen2.5). Only Social Sciences reaches significance. Results are exploratory at this ensemble size.}
90	\label{tab:domain_gamma}
91	\footnotesize
92	\begin{tabular}{lcc}
93	\toprule
94	Domain & $\gamma$ [95\% CI] & Sig. \\
95	\midrule
96	MMLU: Math & +0.50 [$-$0.21, 1.20] & No \\
97	MMLU: Science & +0.50 [$-$0.19, 1.20] & No \\
98	MMLU: CS/Eng & +0.50 [$-$0.43, 1.40] & No \\
99	MMLU: Medical & +0.24 [$-$0.42, 0.88] & No \\
100	MMLU: Other & +0.13 [$-$0.61, 0.89] & No \\
101	MMLU: Business/Law & +0.04 [$-$0.50, 0.58] & No \\
102	MMLU: Humanities & $-$0.31 [$-$0.85, 0.26] & No \\
103	MMLU: Social Sci & $-$0.57 [$-$1.05, $-$0.10] & Yes \\
104	\midrule
105	MMLU: Pooled & +0.11 [$-$0.40, 0.63] & No \\
106	ARC-Challenge & $-$1.46 [CI excl.\ 0] & Yes \\
107	GSM8K & +0.06 [CI incl.\ 0] & No \\
108	\bottomrule
109	\end{tabular}
110	\end{table}
111	
112	\begin{table}[t]
113	\centering
114	\caption{Calibration comparison under the primary $J$=13 configuration (MAE$\downarrow$, Kendall $\tau$$\uparrow$). B3 and ContamCal produce identical $\tau$ on MMLU and GSM8K and near-identical on ARC ($\Delta$=0.003), confirming that $\gamma$ serves diagnosis, not calibration. Full seven-baseline comparison (B0--B6) in Appendix~\ref{sec:full_baselines}.}
115	\label{tab:baselines}
116	\footnotesize
117	\resizebox{\columnwidth}{!}{%
118	\begin{tabular}{lcc|cc|cc}
119	\toprule
120	 & \multicolumn{2}{c|}{ARC} & \multicolumn{2}{c|}{GSM8K} & \multicolumn{2}{c}{MMLU} \\
121	Method & MAE & $\tau$ & MAE & $\tau$ & MAE & $\tau$ \\
122	\midrule
123	B0-Raw & 0.034 & 0.756 & 0.169 & -- & 0.016 & -- \\
124	B3-Vanilla2PL & \textbf{0.016} & 0.730 & \textbf{0.006} & 0.730 & \textbf{0.007} & 0.638 \\
125	ContamCal & 0.020 & 0.733 & \textbf{0.006} & 0.730 & \textbf{0.007} & 0.638 \\
126	\bottomrule
127	\end{tabular}}
128	\end{table}
129	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-17T14:27:58.790004+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ethics|ethical|limitations|societal|impact",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "-i": "True",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ethics|ethical|limitations|societal|impact",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
    "-i": "True",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-17T14:27:58.843944+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/discussion.tex:4:We discuss limitations in Appendix~\ref{sec:limitations}, including scale ceiling (all models $\leq$3B), signal coverage gaps for closed-source models, ensemble size constraints ($J=13$ vs.\ the $J \geq 50$ needed for reliable $\gamma$ recovery), position bias confounds at the 0.5B scale, and under-coverage of posterior credible intervals.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:3:\section{Limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:4:\label{sec:limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex:6:We identify seven limitations that bound the scope of our conclusions.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib:525:@article{kocyigit2025impact,
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib:527:  title         = {The Impact of Post-training on Data Contamination Detection in Large Language Models},
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.aux:1064:\@writefile{toc}{\contentsline {section}{\numberline {A}Limitations}{10}{appendix.A}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.aux:1065:\newlabel{sec:limitations}{{A}{10}{Limitations}{appendix.A}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-17T14:28:08.682876+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "psn.irt|zhou.*psn|zhou.*irt",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib",
  "-i": "True",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "psn.irt|zhou.*psn|zhou.*irt",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib",
    "-i": "True",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-17T14:28:10.101263+00:00_

387-  url       = {https://arxiv.org/abs/2306.05685}
388-}
389-
390:@inproceedings{zhou_2025_psnirt,
391-  author    = {Zhou, Hongli and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},
392-  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},
393-  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 1418
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-17T14:28:10.503369+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "kocyigit|yang.*decontam|zhang.*decontam|schaeffer|holland.*wainer",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib",
  "-i": "True",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "kocyigit|yang.*decontam|zhang.*decontam|schaeffer|holland.*wainer",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib",
    "-i": "True",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-17T14:28:10.554166+00:00_

146-}
147-
148-@book{holland_1993_dif,
149:  author    = {Holland, Paul W. and Wainer, Howard},
150-  title     = {Differential Item Functioning},
151-  publisher = {Lawrence Erlbaum Associates},
152-  year      = {1993},
--
265-  year    = {2009}
266-}
267-
268:@article{schaeffer_2026_generative_contamination,
269:  author        = {Schaeffer, Rylan and Kazdan, Joshua and Abbasi, Ali and Liu, Hailey and Kheirkhah, Brando Miranda and Shao, Sanmi and Nakhost, Hadi},
270-  title         = {Quantifying the Effect of Test Set Contamination on Generative Evaluations},
271-  journal       = {arXiv preprint},
272-  year          = {2026},
--
522-  note      = {arXiv:2503.16402}
523-}
524-
525:@article{kocyigit2025impact,
526:  author        = {Kocyigit, Murat Yildirim and Yildirim, Ekin Akyurek},
527-  title         = {The Impact of Post-training on Data Contamination Detection in Large Language Models},
528-  booktitle     = {Advances in Neural Information Processing Systems (NeurIPS)},
529-  year          = {2025},
--
631-% --- Differential Item Functioning (DIF) ---
632-
633-@book{holland1993dif,
634:  author    = {Holland, Paul W. and Wainer, Howard},
635-  title     = {Differential Item Functioning},
636-  publisher = {Lawrence Erlbaum Associates},
637-  year      = {1993},
--
642-  author    = {Thissen, David and Steinberg, Lynne and Wainer, Howard},
643-  title     = {Detection of Differential Item Functioning Using the Parameters of Item Response Models},
644-  booktitle = {Differential Item Functioning},
645:  editor    = {Holland, Paul W. and Wainer, Howard},
646-  publisher = {Lawrence Erlbaum Associates},
647-  pages     = {67--113},
648-  year      = {1993}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-17T14:28:16.176064+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "zhou_2025_psnirt|kocyigit|schaeffer_2026|holland_1993|holland1993",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "zhou_2025_psnirt|kocyigit|schaeffer_2026|holland_1993|holland1993",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-17T14:28:16.226873+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-17T14:30:22.214687+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 — 对 Reviewer 2 Round 3 审稿意见\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE] R2-N1: Title/Abstract 与核心发现的根本矛盾**\n\n完全同意。这与我的 R1-N1 高度一致。B3-Vanilla2PL 在 ARC 上 MAE=0.016 优于 ContamCal 的 0.020（Table 4），在 MMLU 和 GSM8K 上两者持平。Title \"ContamCal\" 和 Abstract 首句\"existing approaches stop at detection without quantifying how much scores are inflated\"暗示 contamination-specific modeling 是核心贡献，但实验反驳了这一叙事。论文已在 §5.1 中加入 decomposition 讨论，但 title 和 contributions list 的措辞仍需根本性调整。两位 Reviewer 对此一致，应视为最高优先级修改。\n\n**[AGREE] R2-N2: ARR 格式不合规——Desk reject 风险**\n\n同意，这是我 Round 3 审查的遗漏，感谢 R2 发现。已验证：\n\n1. **Limitations 位置错误**：`main.tex` 第 31 行 `\\bibliography{references}` 之后才 `\\input{appendix}`，appendix.tex 第 3 行为 `\\section{Limitations}`。ARR 要求 Limitations 作为独立 section 出现在 references 之前，不计入页数。当前放置违反规定。\n\n2. **Ethics Statement 完全缺失**：全文 grep \"ethics|ethical\" 在 .tex 文件中无任何 section 级别声明。ARR review form 明确评估\"ethical concerns\"，缺失 Ethics Statement 是 desk reject 风险。\n\n这两个问题修复成本极低（移动 Limitations、添加 Ethics Statement），但不修复的后果是 desk reject，应视为阻塞性问题。\n\n**[PARTIALLY AGREE] R2-N3: 贡献新颖性不足**\n\n部分同意，具体逐条评估：\n\n- R2 称\"IRT for LLM eval 已有 TinyBenchmarks/Growing Pains/HiBayES/ATLAS/PSN-IRT\"——**同意这些是密切相关工作**。已验证 `zhou_2025_psnirt`（PSN-IRT, AAAI 2026）在 bib 中但从未 `\\cite`，这是严重疏漏。PSN-IRT 也做 IRT + LLM evaluation，如果它已经涉及 contamination adjustment，ContamCal 的增量需要仔细区分。\n\n- R2 称\"Contribution 1 是 empirical observation 而非 method contribution\"——**同意**。\"IRT alone reduces MAE by 53%\"是一个 empirical finding，不是方法贡献。Method 贡献是 2PL+γ 框架本身，但 γ 不贡献校准，这使得 method 贡献的价值打折。\n\n- R2 称\"Contribution 2 (RRF) 退化为 S1-only\"——**部分不同意**。在 0.5B 确实退化，但在 1.5B+ 下 S2 有 mild positive discrimination (d≈+0.3, §5.2)，RRF 并非完全冗余。不过 Contribution 2 的措辞确实 overclaim——\"Multi-signal exposure detection via RRF\"暗示多信号均有贡献，应调整为\"Signal fusion with documented failure modes\"或类似措辞。\n\n- R2 称\"真正有独立价值的是 Contribution 3-4，适合 short paper / Findings\"——**部分同意**。Min-K\\%++ 方向性逆转（Contribution 3）和 identifiability boundary（Contribution 4 的 simulation 部分）确实是最 robust 的贡献，可独立于 ContamCal 框架成立。但我认为作为 Findings long paper 仍有足够内容量，不必降为 short paper。\n\n**总体判断**：novelty 问题是 real concern 但非 fatal——关键是需要 (a) cite 并区分 PSN-IRT，(b) 重新定位 contributions 的措辞以匹配实际发现。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R2-W1: 主表仅 3/7 baselines**\n\n同意。Table 4 仅展示 B0/B3/ContamCal，将完整 B0-B6 放在附录且配置不同（我的 N5 也指出）。主表应至少包含 B2 (Single2PL+γ) 和 B4 (LinearRegression) 以展示 IRT vs linear correction 的对比。在 long paper 8 页限制内，一个 7-row table 不会占太多空间。\n\n**[AGREE] R2-W2: Related Work 过薄，orphan bib entries**\n\n同意。已验证：`zhou_2025_psnirt` (PSN-IRT), `kocyigit2025impact`, `schaeffer_2026_generative_contamination`, `holland_1993_dif` / `holland1993dif`（重复条目！）均在 bib 中但未被任何 .tex 文件 `\\cite`。PSN-IRT 是直接竞争者，不引用不讨论是重大遗漏。58 个 orphan entries 应清理——这也是工程质量问题。\n\n补充发现：bib 中 `holland_1993_dif` 和 `holland1993dif` 是同一本书的重复条目。\n\n**[AGREE] R2-W3: LoRA SFT ≠ pretraining contamination**\n\n同意，与我的 W5 一致。SFT injection 在 representation 已形成后注入，与 pretraining leakage 机制不同。0.5B 的 catastrophic position bias (A-option 46%→98%) 很可能是 SFT-specific artifact。Limitations 中仅一句\"Single injection protocol\"带过，不足以让读者评估 ecological validity。\n\n**[PARTIALLY AGREE] R2-W4: Discussion/Conclusion 过短**\n\n部分同意。Discussion 确实仅 ~11 行（指向 Appendix 讨论 limitations + 4 条实践建议 + future directions），对 long paper 偏薄。但我注意到 Discussion 的实质内容大量在 §5 Results 各段落中以\"paragraph\"形式内联讨论（如 §5.1 gating/negative results, §5.4 within-family heterogeneity, §5.5 θ asymmetry）。问题不是内容缺失，而是组织方式——Discussion section 名义上过短，但讨论散布在 Results 中。\n\n建议：不一定需要扩充 Discussion 本身，但应将 Results 中的讨论性段落（如 overcorrection 的实践影响、γ 作为诊断 vs 校准的定位、方法适用边界）整合到 Discussion 中。\n\n**[AGREE] R2-W5: GSM8K 11× overcorrection 无实践决策规则**\n\n同意，与我的 N5(c) 一致。§5.1 提到\"overcorrection ratio is 11×\"但 (a) 具体计算来源不明（我的 Q2 也问了这个），(b) 没有给出\"何时不应使用 ContamCal\"的实践指导。如果 B0-Raw MAE 已经很低（如 GSM8K 0.5B 的 0.003），应用 ContamCal 反而有害。方法论文需要清晰的适用边界。\n\n**[AGREE] R2-W6: RRF→S1-only 但 Contribution 2 未调整**\n\n同意。§5.2 诚实报告了 S2 reversal 和 S4 near-random，但 Contribution 2 仍写\"Multi-signal exposure detection via RRF\"，未反映实际降级。至少应在 Contribution 2 中加入 caveat，或将其定位为\"signal fusion framework with documented failure boundary\"。\n\n**[AGREE] R2-W7: Appendix baselines 不同配置**\n\n同意，与我的 N5(a) 一致。Table 5 (ARC, J=8, 0.5B+1.5B) 和 Table 6 (GSM8K, 0.5B) 使用完全不同于主分析 (J=13, 1.5B+3B) 的配置。如果只看附录，ContamCal 4PL+γ ARC MAE=0.035（vs 主表 0.020），GSM8K MAE=0.020（vs 主表 0.006）。没有统一配置下的完整 baseline 比较，读者无法公正评估。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] R2-Q1: 如果 detection 不重要，Stage 1 价值何在？**\n\n这是整篇论文最尖锐的问题。如果 vanilla 2PL 足以校准，Stage 1 (RRF exposure) 的唯一价值是为 γ 提供输入——但 γ 在多数情况下不显著。论文的回答是\"γ 有诊断价值\"，但 8/8 仅 1 个显著，这个诊断价值很弱。我在 R1-N6 提出的 oracle ablation 也指向同一问题：如果 oracle exposure 下 γ 仍不显著，整个 Stage 1 + γ pipeline 的价值接近零，论文应直接推荐 vanilla 2PL。如果 oracle 下 γ 显著，则问题出在信号质量，Stage 1 的价值在于信号改进的方向。这是 ContamCal 作为完整框架的存亡问题。\n\n**[AGREE] R2-Q2: STEM domains γ 均为 +0.50，疑似共线性 artifact**\n\n重要发现，我未在 R1 review 中注意到。Table 2 中 Math (+0.50, [-0.21, 1.20])、Science (+0.50, [-0.19, 1.20])、CS/Eng (+0.50, [-0.43, 1.40]) 的 point estimates 完全相同，前两者 CI 几乎一致。在独立 per-domain fitting 下，三个独立模型产生同一 point estimate 的概率极低（除非 MCMC 初始化或 prior 引导了这个结果）。可能的解释：(a) 这些域的 exposure score 分布高度相似，导致 γ 的似然面相同；(b) prior γ ~ N(0,1) 在 small J 下主导了 posterior，point estimate 被 pulled 到相似位置；(c) 舍入误差（如果实际值是 0.496, 0.501, 0.503 被 rounded to 0.50）。无论哪种，论文应讨论此 pattern 的原因。\n\n**[AGREE] R2-Q3: Cross-family Llama J=3-4 严重不平衡**\n\n同意。GSM8K J=28 中 Llama 仅 4/28=14%；MMLU J=18 中 Llama 仅 3/18=17%（d100 excluded for format collapse）。θ 估计由 Qwen 主导。Table 3 的\"cross-family\"标签 overstate 了 Llama 的贡献——这更像是\"Qwen family with Llama augmentation\"。\n\n**[PARTIALLY AGREE] R2-Q4: θ 是否被 contamination 污染？**\n\n这触及了一个深层问题。论文的 Eq. 3 计算 calibrated score 时使用 θ_j，但 θ_j 是从包含 contaminated responses 的数据中估计的。如果 Qwen Δθ=+0.57（d000→d100）而 Llama Δθ≈+0.05，说明 Qwen 的 θ 吸收了污染效应。论文的框架认为这是 feature（\"IRT absorbs contamination into θ\"），且声称 calibrated score 的低 MAE 验证了这一点。\n\n**但我认为 R2 的担忧部分成立**：如果 θ 已被 contamination inflate，Eq. 3 的 calibrated score 也会被 inflate。论文声称 calibrated MAE 低是因为 IRT\"分离了 ability 和 noise\"，但更准确地说是因为 IRT 的 item parameter estimation 重新标定了 difficulty scale，使得 P(correct | θ, a, b) 的期望值恰好接近 clean accuracy。这个校准是否 robust 还是仅在 SFT injection 设置下的 coincidence，需要更多实验验证（如不同 injection 比例、不同 model families 的 cross-validation）。\n\n**部分不同意的理由**：IRT 的校准机制有理论支撑——joint estimation 中 item parameters 和 θ 互相约束。如果某个 model 因 memorization 在 hard items 上表现异常好，这会推高 θ 但也会影响 item difficulty 估计。关键是有 clean control models (d000) 作为 anchor，它们的存在约束了 item parameters 的估计，从而间接约束了 contaminated models 的 θ。所以 θ 被\"污染\"的程度取决于 contaminated models 在 pool 中的比例和 clean anchor 的稳定性。\n\n**[AGREE] R2-Q5: 50% CI 35% coverage = local independence violation?**\n\n合理假设。§3.1 Adaptation 1 承认 LLM responses 可能有 residual correlations beyond scalar θ，但仅以\"fitting per-benchmark models\"作为 mitigation。对于同一模型，domain 内的 items 可能有高度相关的 memorization patterns（memorize one factual QA → likely memorize related ones）。这违反 local independence，会导致 posterior variance 被低估（因为有效样本量小于名义样本量），从而 CI 过窄。这与 35% coverage (vs 50% nominal) 的方向一致。论文应在 Limitations 中讨论这一可能性并建议 testlet IRT 或 local dependence modeling 作为改进方向。\n\n---\n\n### Missing References 回应\n\n**[AGREE]** PSN-IRT (Zhou et al., AAAI 2026)：已验证在 bib 中 (`zhou_2025_psnirt`) 但从未 cite。作为直接使用 IRT for LLM evaluation 的同期工作，不引用不讨论是重大遗漏。\n\n**[AGREE]** Kocyigit et al. (NeurIPS 2025)：在 bib 中 (`kocyigit2025impact`)，关于 post-training 对 contamination detection 的影响，直接相关于 §5.2 signal failure modes。未 cite。\n\n**[AGREE]** Schaeffer et al. (2026)：在 bib 中 (`schaeffer_2026_generative_contamination`)，关于 generative evaluation 中的 contamination 量化，相关但非直接竞争。未 cite。\n\n**[AGREE]** Holland and Wainer (1993) DIF：在 bib 中有两个重复条目 (`holland_1993_dif` 和 `holland1993dif`)。DIF 是 §3.2 讨论的理论基础之一（Related Work 中提到 \"DIF cancellation\"），但引用的是 `ercikan_2008_dif_cancellation` 而非原始 DIF 专著。应引用。\n\n**[PARTIALLY AGREE]** Yang et al., Zhang et al.：未验证是否在 bib 中，但如果存在 inference-time decontamination 和 ICML 2025 decontamination 工作，应在 Related Work 中讨论。\n\n**[AGREE]** 58 个 orphan bib entries 需清理：这反映工程质量问题，但不影响技术评估。\n\n---\n\n### 对 R2 Overall Assessment 的评价\n\nR2 给出 2.5 (Borderline Findings)。我给出 3.0 (Findings)。差距主要在两个方面：\n\n1. **格式问题的权重**：R2 将 N2 (Limitations 位置 + Ethics 缺失) 视为 critical desk reject 风险并压低评分。我同意这是严重问题，但修复成本极低（< 30 分钟）。这类格式问题不应从实质性角度影响论文的科学价值评估。\n\n2. **Novelty 评价**：R2 认为 Excitement 仅 2.5，核心理由是 \"IRT for LLM eval 不新\"。我认为 contamination-augmented IRT（将 detection signals 作为 covariates）是 incremental but genuine novelty，且 signal failure modes + identifiability boundary 的组合贡献足以支撑 Findings。但我同意如果 PSN-IRT 已做了类似事情，novelty claim 需要重新评估——这取决于 PSN-IRT 的具体内容。\n\n**两位 Reviewer 的共识**（应视为强信号）：\n- Title/framing 必须调整（N1）\n- γ 不贡献校准是核心发现，论文应围绕此重构\n- Oracle ablation 缺失是关键实验空白\n- Cross-family validation underpowered\n- CI coverage 报告不完整",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 — 对 Reviewer 2 Round 3 审稿意见\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE] R2-N1: Title/Abstract 与核心发现的根本矛盾**\n\n完全同意。这与我的 R1-N1 高度一致。B3-Vanilla2PL 在 ARC 上 MAE=0.016 优于 ContamCal 的 0.020（Table 4），在 MMLU 和 GSM8K 上两者持平。Title \"ContamCal\" 和 Abstract 首句\"existing approaches stop at detection without quantifying how much scores are inflated\"暗示 contamination-specific modeling 是核心贡献，但实验反驳了这一叙事。论文已在 §5.1 中加入 decomposition 讨论，但 title 和 contributions list 的措辞仍需根本性调整。两位 Reviewer 对此一致，应视为最高优先级修改。\n\n**[AGREE] R2-N2: ARR 格式不合规——Desk reject 风险**\n\n同意，这是我 Round 3 审查的遗漏，感谢 R2 发现。已验证：\n\n1. **Limitations 位置错误**：`main.tex` 第 31 行 `\\bibliography{references}` 之后才 `\\input{appendix}`，appendix.tex 第 3 行为 `\\section{Limitations}`。ARR 要求 Limitations 作为独立 section 出现在 references 之前，不计入页数。当前放置违反规定。\n\n2. **Ethics Statement 完全缺失**：全文 grep \"ethics|ethical\" 在 .tex 文件中无任何 section 级别声明。ARR review form 明确评估\"ethical concerns\"，缺失 Ethics Statement 是 desk reject 风险。\n\n这两个问题修复成本极低（移动 Limitations、添加 Ethics Statement），但不修复的后果是 desk reject，应视为阻塞性问题。\n\n**[PARTIALLY AGREE] R2-N3: 贡献新颖性不足**\n\n部分同意，具体逐条评估：\n\n- R2 称\"IRT for LLM eval 已有 TinyBenchmarks/Growing Pains/HiBayES/ATLAS/PSN-IRT\"——**同意这些是密切相关工作**。已验证 `zhou_2025_psnirt`（PSN-IRT, AAAI 2026）在 bib 中但从未 `\\cite`，这是严重疏漏。PSN-IRT 也做 IRT + LLM evaluation，如果它已经涉及 contamination adjustment，ContamCal 的增量需要仔细区分。\n\n- R2 称\"Contribution 1 是 empirical observation 而非 method contribution\"——**同意**。\"IRT alone reduces MAE by 53%\"是一个 empirical finding，不是方法贡献。Method 贡献是 2PL+γ 框架本身，但 γ 不贡献校准，这使得 method 贡献的价值打折。\n\n- R2 称\"Contribution 2 (RRF) 退化为 S1-only\"——**部分不同意**。在 0.5B 确实退化，但在 1.5B+ 下 S2 有 mild positive discrimination (d≈+0.3, §5.2)，RRF 并非完全冗余。不过 Contribution 2 的措辞确实 overclaim——\"Multi-signal exposure detection via RRF\"暗示多信号均有贡献，应调整为\"Signal fusion with documented failure modes\"或类似措辞。\n\n- R2 称\"真正有独立价值的是 Contribution 3-4，适合 short paper / Findings\"——**部分同意**。Min-K\\%++ 方向性逆转（Contribution 3）和 identifiability boundary（Contribution 4 的 simulation 部分）确实是最 robust 的贡献，可独立于 ContamCal 框架成立。但我认为作为 Findings long paper 仍有足够内容量，不必降为 short paper。\n\n**总体判断**：novelty 问题是 real concern 但非 fatal——关键是需要 (a) cite 并区分 PSN-IRT，(b) 重新定位 contributions 的措辞以匹配实际发现。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R2-W1: 主表仅 3/7 baselines**\n\n同意。Table 4 仅展示 B0/B3/ContamCal，将完整 B0-B6 放在附录且配置不同（我的 N5 也指出）。主表应至少包含 B2 (Single2PL+γ) 和 B4 (LinearRegression) 以展示 IRT vs linear correction 的对比。在 long paper 8 页限制内，一个 7-row table 不会占太多空间。\n\n**[AGREE] R2-W2: Related Work 过薄，orphan bib entries**\n\n同意。已验证：`zhou_2025_psnirt` (PSN-IRT), `kocyigit2025impact`, `schaeffer_2026_generative_contamination`, `holland_1993_dif` / `holland1993dif`（重复条目！）均在 bib 中但未被任何 .tex 文件 `\\cite`。PSN-IRT 是直接竞争者，不引用不讨论是重大遗漏。58 个 orphan entries 应清理——这也是工程质量问题。\n\n补充发现：bib 中 `holland_1993_dif` 和 `holland1993dif` 是同一本书的重复条目。\n\n**[AGREE] R2-W3: LoRA SFT ≠ pretraining contamination**\n\n同意，与我的 W5 一致。SFT injection 在 representation 已形成后注入，与 pretraining leakage 机制不同。0.5B 的 catastrophic position bias (A-option 46%→98%) 很可能是 SFT-specific artifact。Limitations 中仅一句\"Single injection protocol\"带过，不足以让读者评估 ecological validity。\n\n**[PARTIALLY AGREE] R2-W4: Discussion/Conclusion 过短**\n\n部分同意。Discussion 确实仅 ~11 行（指向 Appendix 讨论 limitations + 4 条实践建议 + future directions），对 long paper 偏薄。但我注意到 Discussion 的实质内容大量在 §5 Results 各段落中以\"paragraph\"形式内联讨论（如 §5.1 gating/negative results, §5.4 within-family heterogeneity, §5.5 θ asymmetry）。问题不是内容缺失，而是组织方式——Discussion section 名义上过短，但讨论散布在 Results 中。\n\n建议：不一定需要扩充 Discussion 本身，但应将 Results 中的讨论性段落（如 overcorrection 的实践影响、γ 作为诊断 vs 校准的定位、方法适用边界）整合到 Discussion 中。\n\n**[AGREE] R2-W5: GSM8K 11× overcorrection 无实践决策规则**\n\n同意，与我的 N5(c) 一致。§5.1 提到\"overcorrection ratio is 11×\"但 (a) 具体计算来源不明（我的 Q2 也问了这个），(b) 没有给出\"何时不应使用 ContamCal\"的实践指导。如果 B0-Raw MAE 已经很低（如 GSM8K 0.5B 的 0.003），应用 ContamCal 反而有害。方法论文需要清晰的适用边界。\n\n**[AGREE] R2-W6: RRF→S1-only 但 Contribution 2 未调整**\n\n同意。§5.2 诚实报告了 S2 reversal 和 S4 near-random，但 Contribution 2 仍写\"Multi-signal exposure detection via RRF\"，未反映实际降级。至少应在 Contribution 2 中加入 caveat，或将其定位为\"signal fusion framework with documented failure boundary\"。\n\n**[AGREE] R2-W7: Appendix baselines 不同配置**\n\n同意，与我的 N5(a) 一致。Table 5 (ARC, J=8, 0.5B+1.5B) 和 Table 6 (GSM8K, 0.5B) 使用完全不同于主分析 (J=13, 1.5B+3B) 的配置。如果只看附录，ContamCal 4PL+γ ARC MAE=0.035（vs 主表 0.020），GSM8K MAE=0.020（vs 主表 0.006）。没有统一配置下的完整 baseline 比较，读者无法公正评估。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] R2-Q1: 如果 detection 不重要，Stage 1 价值何在？**\n\n这是整篇论文最尖锐的问题。如果 vanilla 2PL 足以校准，Stage 1 (RRF exposure) 的唯一价值是为 γ 提供输入——但 γ 在多数情况下不显著。论文的回答是\"γ 有诊断价值\"，但 8/8 仅 1 个显著，这个诊断价值很弱。我在 R1-N6 提出的 oracle ablation 也指向同一问题：如果 oracle exposure 下 γ 仍不显著，整个 Stage 1 + γ pipeline 的价值接近零，论文应直接推荐 vanilla 2PL。如果 oracle 下 γ 显著，则问题出在信号质量，Stage 1 的价值在于信号改进的方向。这是 ContamCal 作为完整框架的存亡问题。\n\n**[AGREE] R2-Q2: STEM domains γ 均为 +0.50，疑似共线性 artifact**\n\n重要发现，我未在 R1 review 中注意到。Table 2 中 Math (+0.50, [-0.21, 1.20])、Science (+0.50, [-0.19, 1.20])、CS/Eng (+0.50, [-0.43, 1.40]) 的 point estimates 完全相同，前两者 CI 几乎一致。在独立 per-domain fitting 下，三个独立模型产生同一 point estimate 的概率极低（除非 MCMC 初始化或 prior 引导了这个结果）。可能的解释：(a) 这些域的 exposure score 分布高度相似，导致 γ 的似然面相同；(b) prior γ ~ N(0,1) 在 small J 下主导了 posterior，point estimate 被 pulled 到相似位置；(c) 舍入误差（如果实际值是 0.496, 0.501, 0.503 被 rounded to 0.50）。无论哪种，论文应讨论此 pattern 的原因。\n\n**[AGREE] R2-Q3: Cross-family Llama J=3-4 严重不平衡**\n\n同意。GSM8K J=28 中 Llama 仅 4/28=14%；MMLU J=18 中 Llama 仅 3/18=17%（d100 excluded for format collapse）。θ 估计由 Qwen 主导。Table 3 的\"cross-family\"标签 overstate 了 Llama 的贡献——这更像是\"Qwen family with Llama augmentation\"。\n\n**[PARTIALLY AGREE] R2-Q4: θ 是否被 contamination 污染？**\n\n这触及了一个深层问题。论文的 Eq. 3 计算 calibrated score 时使用 θ_j，但 θ_j 是从包含 contaminated responses 的数据中估计的。如果 Qwen Δθ=+0.57（d000→d100）而 Llama Δθ≈+0.05，说明 Qwen 的 θ 吸收了污染效应。论文的框架认为这是 feature（\"IRT absorbs contamination into θ\"），且声称 calibrated score 的低 MAE 验证了这一点。\n\n**但我认为 R2 的担忧部分成立**：如果 θ 已被 contamination inflate，Eq. 3 的 calibrated score 也会被 inflate。论文声称 calibrated MAE 低是因为 IRT\"分离了 ability 和 noise\"，但更准确地说是因为 IRT 的 item parameter estimation 重新标定了 difficulty scale，使得 P(correct | θ, a, b) 的期望值恰好接近 clean accuracy。这个校准是否 robust 还是仅在 SFT injection 设置下的 coincidence，需要更多实验验证（如不同 injection 比例、不同 model families 的 cross-validation）。\n\n**部分不同意的理由**：IRT 的校准机制有理论支撑——joint estimation 中 item parameters 和 θ 互相约束。如果某个 model 因 memorization 在 hard items 上表现异常好，这会推高 θ 但也会影响 item difficulty 估计。关键是有 clean control models (d000) 作为 anchor，它们的存在约束了 item parameters 的估计，从而间接约束了 contaminated models 的 θ。所以 θ 被\"污染\"的程度取决于 contaminated models 在 pool 中的比例和 clean anchor 的稳定性。\n\n**[AGREE] R2-Q5: 50% CI 35% coverage = local independence violation?**\n\n合理假设。§3.1 Adaptation 1 承认 LLM responses 可能有 residual correlations beyond scalar θ，但仅以\"fitting per-benchmark models\"作为 mitigation。对于同一模型，domain 内的 items 可能有高度相关的 memorization patterns（memorize one factual QA → likely memorize related ones）。这违反 local independence，会导致 posterior variance 被低估（因为有效样本量小于名义样本量），从而 CI 过窄。这与 35% coverage (vs 50% nominal) 的方向一致。论文应在 Limitations 中讨论这一可能性并建议 testlet IRT 或 local dependence modeling 作为改进方向。\n\n---\n\n### Missing References 回应\n\n**[AGREE]** PSN-IRT (Zhou et al., AAAI 2026)：已验证在 bib 中 (`zhou_2025_psnirt`) 但从未 cite。作为直接使用 IRT for LLM evaluation 的同期工作，不引用不讨论是重大遗漏。\n\n**[AGREE]** Kocyigit et al. (NeurIPS 2025)：在 bib 中 (`kocyigit2025impact`)，关于 post-training 对 contamination detection 的影响，直接相关于 §5.2 signal failure modes。未 cite。\n\n**[AGREE]** Schaeffer et al. (2026)：在 bib 中 (`schaeffer_2026_generative_contamination`)，关于 generative evaluation 中的 contamination 量化，相关但非直接竞争。未 cite。\n\n**[AGREE]** Holland and Wainer (1993) DIF：在 bib 中有两个重复条目 (`holland_1993_dif` 和 `holland1993dif`)。DIF 是 §3.2 讨论的理论基础之一（Related Work 中提到 \"DIF cancellation\"），但引用的是 `ercikan_2008_dif_cancellation` 而非原始 DIF 专著。应引用。\n\n**[PARTIALLY AGREE]** Yang et al., Zhang et al.：未验证是否在 bib 中，但如果存在 inference-time decontamination 和 ICML 2025 decontamination 工作，应在 Related Work 中讨论。\n\n**[AGREE]** 58 个 orphan bib entries 需清理：这反映工程质量问题，但不影响技术评估。\n\n---\n\n### 对 R2 Overall Assessment 的评价\n\nR2 给出 2.5 (Borderline Findings)。我给出 3.0 (Findings)。差距主要在两个方面：\n\n1. **格式问题的权重**：R2 将 N2 (Limitations 位置 + Ethics 缺失) 视为 critical desk reject 风险并压低评分。我同意这是严重问题，但修复成本极低（< 30 分钟）。这类格式问题不应从实质性角度影响论文的科学价值评估。\n\n2. **Novelty 评价**：R2 认为 Excitement 仅 2.5，核心理由是 \"IRT for LLM eval 不新\"。我认为 contamination-augmented IRT（将 detection signals 作为 covariates）是 incremental but genuine novelty，且 signal failure modes + identifiability boundary 的组合贡献足以支撑 Findings。但我同意如果 PSN-IRT 已做了类似事情，novelty claim 需要重新评估——这取决于 PSN-IRT 的具体内容。\n\n**两位 Reviewer 的共识**（应视为强信号）：\n- Title/framing 必须调整（N1）\n- γ 不贡献校准是核心发现，论文应围绕此重构\n- Oracle ablation 缺失是关键实验空白\n- Cross-family validation underpowered\n- CI coverage 报告不完整",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-17T14:30:26.181419+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3966
}
```

</details>

---


### Assistant

_source line 150 · 2026-05-17T14:30:35.817729+00:00_

已完成两份报告的提交：

1. **Round 3 独立审稿** — Overall 3.0 (Findings)，识别 6 个 Critical issues (framing 张力、CI 覆盖不全、ARC PPP 缺失、J=13 自证 underpowered、baseline 配置不一致、oracle ablation 缺失) 和 5 个 Warning。

2. **对 R2 的交叉回应** — 对 R2 的 N1/N2 完全同意，N3 部分同意（novelty 有但需重新定位）。7 个 Should-Fix 中 6 个 AGREE，W4 部分同意。5 个 Questions 中 4 个 AGREE，Q4 部分同意（θ 吸收 contamination 有理论支撑但 robustness 需验证）。两位 Reviewer 的最强共识：title/framing 必须改、oracle ablation 必须补、格式问题必须修。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 7

## Round 7

50 recorded events


### User

_source line 151 · 2026-05-17T17:25:12.823732+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重**: 方法严谨性 + 实验设计 + 统计推断

### 论文信息
- **标题**: "Decomposing Contamination from Calibration: An IRT Approach to LLM Benchmark Evaluation"
- **路径**: `projects/contamcal-irt-calibration/docs/paper/main.tex` (分文件结构，各章节 `\input` 引入)
- **目标 Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)
- **截止日期**: 2026-05-25
- **类型**: Long paper

### Venue 格式要求
- 8 页正文 + 无限参考文献
- ACL style template, `[review]` option
- Double-blind (作者 "Anonymous")
- Limitations section 在 references 前，不计入页数
- Ethics Statement 推荐
- 附录不计入页数

### 你需要重点审查的方面

1. **IRT 模型规范的严谨性**
   - 2PL+γ 模型假设是否合理（additive γ, linear exposure effect）
   - 独立 per-domain fitting vs. shared θ scale 的取舍是否有充分论证
   - Bayesian inference (NUTS in Stan) 的收敛诊断是否充分
   - 先验选择的合理性（特别是 γ ~ N(0,1) 是否 informative 或 noninformative）

2. **实验设计**
   - SFT injection 作为 contamination proxy 的 ecological validity
   - 模型排除率和 J 值选择（J=13 vs J=16 vs J=24 跨不同分析）
   - 0.5B 排除的正当性
   - Cross-family (Llama) 分析的统计功效
   - Baseline 比较的公平性（统一条件？同等 J？）

3. **统计推断与声明**
   - γ 的 identifiability 声明（AUC≥0.55, J≥50）是否有充分理论/实验支撑
   - Oracle ablation 的逻辑：perfect labels → non-significant γ 说明什么
   - CI coverage 报告（MMLU over-covers, ARC under-covers）的解释
   - 域级 γ 显著性（仅 Social Sciences）在无多重比较校正下的可解释性
   - ARC PPP=0.03 的 model fit 问题

4. **核心发现的可信度**
   - "Aggregate contamination effect ~0.6-0.7pp" 是否是 SFT injection 特有的 artifact
   - "Raw accuracy is already well-calibrated" 结论的适用范围
   - Min-K%++ directional reversal 的因果解释是否合理

请产出完整审稿报告，包含 Strengths、Weaknesses（逐条、分 must-fix / should-fix / minor）、Questions、Missing References、Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-17T17:25:18.486405+00:00_

called Skill

<details open><summary>🔧 Tool call — Skill</summary>

```json
{
  "skill": "review-reviewer-session-start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Skill",
  "tool_args": {
    "skill": "review-reviewer-session-start"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-17T17:25:18.486753+00:00_

&lt;tool_use_error>Unknown skill: review-reviewer-session-start&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Skill",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-17T17:25:22.810655+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-17T17:25:22.861701+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-17T17:25:25.275628+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-17T17:25:25.326344+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-17T17:25:27.840461+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start*",
    "path": "/home/ubuntu"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-17T17:25:28.294373+00:00_

/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-17T17:25:30.012727+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-17T17:25:30.064899+00:00_

1	---
2	name: review-reviewer-session-start
3	description: Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。
4	priority: 8
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 2
11	roles: []
12	---
13	
14	# Review Reviewer Session 启动流程
15	
16	执行顺序：
17	1. 读取论文文件（`projects/{project}/paper/main.tex` 或类似路径）
18	2. 检查论文格式状态：
19	   - 页数是否在 venue 要求内（若已知 venue）
20	   - LaTeX 是否可编译（调用 `ssh_execute` 运行 `pdflatex` 或 `latexmk`）
21	   - 图表是否有标题和标签
22	3. 视觉检查：如果已有编译好的 PDF，使用 `paper-visual-review` skill 渲染关键页面（首页、图表页、参考文献页），检查排版溢出、公式渲染、图表质量等视觉问题
23	4. 检查投稿材料清单：
24	   - cover letter 是否存在
25	   - 补充材料是否准备
26	   - 参考文献格式是否正确
27	5. 向 Review Director 汇报（`review_reviewer_post_to_director`）：
28	   - 论文当前状态
29	   - 发现的格式问题（如有）
30	   - 视觉检查结果（如有）
31	   - 缺少的材料（如有）
32	
33	此流程在 Review Director 分配任务后执行。
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-17T17:25:34.802178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-17T17:25:36.311389+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{Decomposing Contamination from Calibration:\\An IRT Approach to LLM Benchmark Evaluation}
13	
14	\author{Anonymous}
15	
16	\begin{document}
17	\maketitle
18	
19	\begin{abstract}
20	\input{abstract}
21	\end{abstract}
22	
23	\input{introduction}
24	\input{related_work}
25	\input{method}
26	\input{experimental_setup}
27	\input{results}
28	\input{conclusion}
29	
30	\input{limitations}
31	\input{ethics}
32	
33	\bibliography{references}
34	
35	\input{appendix}
36	
37	\end{document}
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1509
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-17T17:25:36.311902+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-17T17:25:36.362287+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-17T17:25:43.305199+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-17T17:25:43.355960+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-17T17:25:43.356535+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-17T17:25:52.198878+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, I've found comprehensive information about ACL Rolling Review 2026 reviewer guidelines and review criteria. Here's what I found:

## Reviewer Guidelines and Standards

The reviews will not be specific to a confere
…[truncated 1539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8842
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-17T17:25:58.661024+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales. List every dimension reviewers must score (e.g., soundness, excitement, overall assessment) with their scale descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales. List every dimension reviewers must score (e.g., soundness, excitement, overall assessment) with their scale descriptions."
  }
}
```

</details>

---


### Tool call

_source line 171 · 2026-05-17T17:25:58.812007+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 172 · 2026-05-17T17:25:58.812420+00:00_

1	Training data contamination undermines the validity of Large Language Model (LLM) benchmark comparisons, yet existing detection methods stop at binary flags without quantifying score inflation or providing calibrated estimates. We investigate whether Item Response Theory (IRT) can separate genuine ability from contamination artifacts on existing benchmarks. Using controlled contamination injection across Qwen2.5 (0.5B--3B) and three benchmarks (MMLU, ARC-Challenge, GSM8K), we find a surprising null result: SFT-injected contamination shifts aggregate accuracy by only ${\sim}$0.6--0.7 percentage points, an effect smaller than the estimation noise of any correction method. Raw accuracy is already well-calibrated; neither IRT ability estimation nor contamination-specific $\gamma$ correction improves upon it. To connect detection signals with a measurement-theoretic framework, we develop ContamCal, a two-stage pipeline that uses training-free Reciprocal Rank Fusion (RRF) for exposure-based item filtering, then fits a contamination-augmented IRT model (2PL+$\gamma$). Item filtering improves IRT calibration: RRF-guided selection on 300 items achieves $\tau = 0.73$ vs.\ $\tau = 0.46$ on random subsets of comparable size ($\Delta\tau = 0.27$). Although $\gamma$ does not improve aggregate calibration, it provides a contamination existence diagnostic and reveals domain-level heterogeneity: Social Sciences shows a significant negative effect ($\gamma = -0.57$) within the Qwen family. We further document that Min-K\%++ exhibits directional reversal at small model scales (Cohen's $d = -1.55$ to $-1.98$), where the signal is actively misleading rather than merely ineffective, and that B6-DCR systematically overcorrects (MAE 0.108--0.314). Simulation studies establish that reliable $\gamma$ recovery requires signal AUC $\geq 0.55$ and $J \geq 50$, exposing a structural gap between current practice and the statistical requirements for contamination diagnosis via IRT.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 173 · 2026-05-17T17:25:58.862920+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 174 · 2026-05-17T17:25:59.316766+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection, resource allocation, and research priorities for large language models, yet training data contamination undermines the validity of these scores in ways that current evaluation cannot quantify \citep{hendrycks2021mmlu,chang2025benchmarking}. When models encounter test items during training, observed accuracy conflates genuine capability with memorization, and practitioners have no principled way to determine how much of a reported score reflects real understanding. The problem is compounded by the scale of modern training corpora: trillion-token web crawls make contamination pervasive and instance-level measurement infeasible \citep{oren2024proving}. Post-hoc calibration that quantifies contamination effects despite imperfect detection is therefore essential for trustworthy evaluation.
4	
5	Two developments make this gap urgent. First, \citet{sun2025emperor} systematically evaluate twenty contamination mitigation strategies (rephrasing, option shuffling, dynamic benchmark regeneration, and others) and demonstrate that none restores clean performance after contamination has occurred. This result forecloses the ``prevent contamination'' approach for models already trained on unrestricted web data. Second, contamination-free benchmarks \citep{white2024livebench} offer a partial solution but sacrifice the comparability and institutional knowledge accumulated around established benchmarks. Dynamic regeneration of test items may also be contaminated within weeks as web crawlers index benchmark repositories \citep{dong_2024_cdd}. The field therefore needs post-hoc statistical tools that can separate genuine ability from contamination artifacts on existing benchmarks.
6	
7	Detection methods such as Min-K\%++ \citep{zhang_2024_minkpp}, ConStat \citep{dekoninck2024constat}, and Kernel Divergence Signatures \citep{choi_2025_kds} can flag contaminated items but stop at detection. They d
…[truncated 4145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 175 · 2026-05-17T17:25:59.317227+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 176 · 2026-05-17T17:25:59.772651+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is twofold: (1)~estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt}, adapting these frameworks through three structural modifications for LLM evaluation.
12	
13	\textit{Adaptation~1: Shared item pool.} A fixed item set is shared across all models, introducing residual correlations beyond scalar $\theta_j$ \citep{sanmartin_2009_irt}; we mitigate by fitting per-benchmark models.
14	\textit{Adaptation~2: Continuous exposure.} We replace binary leakage indicators with continuous scores $e_{ij} \in [0,1]$ derived from detection signals, as LLM contamination is graded rather than binary.
15	\textit{Adaptation~3: Counterfactual ability.} Training regime changes (SFT vs.\ RL) alter both representations and signal reliability; we recover clean ability via counterfactual inference (setting $e_{ij}=0$) rather than regime-specific parameters.
16	
17	\subsection{Sta
…[truncated 5521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 177 · 2026-05-17T17:25:59.773139+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 178 · 2026-05-17T17:26:00.175243+00:00_

1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed using Qwen2.5 \citep{qwen2024qwen25} at three scales (0.5B, 1.5B, 3B parameters). For each scale, we fine-tune with Low-Rank Adaptation \citep[LoRA;][]{hu2022lora} ($\alpha=32$, $r=16$, lr$=5\times10^{-5}$) on a general-purpose SFT corpus into which benchmark items are injected at four dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), and d100 (100\%). Injected items are formatted as instruction-response pairs and pass a quality-control filter that removes ambiguous or malformed entries.
8	
9	Each configuration is trained with two random seeds (s42, s123), yielding 24 models across $3 \times 4 \times 2$ conditions. This within-family design isolates contamination dosage as the primary experimental variable while controlling for architecture, tokenizer, and pretraining data.
10	
11	We exclude 0.5B models from MMLU and ARC IRT due to answer-position bias that correlates with dosage (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}). Three initial 3B checkpoints trained with inconsistent LoRA hyperparameters were retrained under the unified protocol ($\alpha=32$, lr$=5\times10^{-5}$; Appendix~\ref{sec:exclusion_details}). Our pooled calibration analysis (Table~\ref{tab:baselines}) uses $J=16$ respondents for MMLU/ARC (1.5B$\times$8 + 3B$\times$8) and $J=24$ for GSM8K (all scales retained). Domain-level $\gamma$ analysis (Table~\ref{tab:domain_gamma}, \S\ref{sec:domain_differential}) uses $J=13$ (1.5B$\times$8 + 3B$\times$5), as it preceded completion of the 3B retraining. The eight 1.5B d000 models serve as the clean reference anchor in both configurations.
12	
13	\subsection{Cross-Family Analysis}
14	\label{sec:cross_family}
15	
16	To test whether IRT calibration is robust to inclusion of new model families, we fine-tune Llama-3.2-3B \citep{grattafiori202
…[truncated 2322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 179 · 2026-05-17T17:26:00.175728+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 180 · 2026-05-17T17:26:00.229711+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Calibration Quality}
5	\label{sec:calibration_results}
6	
7	\paragraph{Item filtering improves calibration.}
8	RRF-guided item filtering substantially improves IRT calibration quality over random item subsets of comparable size. On a random 2000-item MMLU subset (same $J=13$ model set), vanilla 2PL achieves $\tau = 0.460$; on the 300-item RRF-selected subset, $\tau = 0.73$ ($\Delta\tau = 0.27$, controlled for model composition). Signal-guided filtering concentrates items where contamination effects are detectable, enabling sharper ability-dosage separation. Exclusion sensitivity analysis (removing 0--50\% of top-exposure items from random 2000-item subsets, $J=13$) yields $\tau$ ranging from 0.46 to 0.60 with no monotonic trend, and $\gamma$ remains non-significant at all exclusion rates.
9	
10	\paragraph{Aggregate contamination effects are negligible.}
11	Table~\ref{tab:baselines} compares calibration on 300 RRF-filtered items ($J=16$). Raw accuracy achieves the lowest MAE (MMLU 0.006, ARC 0.007), outperforming all correction methods including vanilla 2PL and ContamCal. This occurs because SFT-injected contamination shifts aggregate accuracy by only ${\sim}$0.6pp on MMLU and ${\sim}$0.7pp on ARC across dosage levels, an effect smaller than the estimation noise introduced by any correction procedure. The IRT model differentiates ability across scales ($\Delta\theta = 0.50$, 95\% CI $[0.43, 0.57]$ pooled; Appendix~\ref{sec:theta_separation}), confirming that $\theta$ estimation is functioning correctly; the calibration gap arises because correction overshoots a near-zero true effect.
12	
13	\paragraph{Diagnostic value of $\gamma$.}
14	Although $\gamma$ does not improve aggregate calibration, within-family domain analysis reveals Social Sciences as the only domain reaching significance ($\gamma = -0.57$, Table~\ref{tab:domain_gamma}). ContamCal's value lies in this decomposition: it quantifies \textit{why} raw
…[truncated 11459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-17T17:26:03.850977+00:00_

# ARR Reviewer Scoring Dimensions

Based on the guidelines, reviewers must provide **three scores**:

## 1. **Soundness**
Assesses technical correctness and validity. Scores must be justified by review text. Low soundness scores require explicit explanation of identified flaws.

## 2. **Excitement**
Reflects personal interest and subjective appeal. This dimension is "orthogonal to the assessment of the soundness of the paper" and "do not necessarily come with explicit reasons."

## 3. **Overall Assessment**
A composite recommendation integrating soundness, excitement, novelty, and impact. This represents "an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue."

## Additional Scoring Component

**Reproducibility** receives a separate score, which should also be justified in the review text.

---

## Key Principle

The guidelines emphasize that "soundness scores must be justified by the text of the review." If scoring indicates low soundness without documented problems, the review itself requires revision. This prevents reviewers from letting unconscious biases drive assessments without evidential support.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5189
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-17T17:26:10.981011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-17T17:26:11.333585+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination detection and mitigation.}
5	Membership inference for contamination detection builds on the foundations of training data extraction \citep{carlini_2021_extracting} and membership inference attacks \citep{shokri_2017_mia}. Current approaches include Min-K\% \citep{shi_2023_minkprob} and Min-K\%++ \citep{zhang_2024_minkpp} (token-level surprisal), ConStat \citep{dekoninck2024constat} (accuracy gaps on paraphrased items), CDD/TED \citep{dong_2024_cdd} (completion-based probes), KDS \citep{choi_2025_kds} (kernel divergence), TS-Guessing \citep{deng_2024_tsguessing} (temporal splits), and Time Travel \citep{golchin_2024_time_travel} (guided generation probes). Concurrent with our work, \citet{tao2025detecting} propose an entropy collapse method for RL-trained models. \citet{kocyigit2025impact} show that post-training procedures (RLHF, DPO) degrade detection signal reliability, complicating the application of token-level methods to instruction-tuned models. \citet{zhang_2024_gsm1k} construct GSM1K as a parallel test set to quantify GSM8K contamination, demonstrating that performance gaps between original and regenerated items serve as a natural experiment for contamination measurement. These methods flag contamination but do not produce adjusted scores. On the mitigation side, \citet{sun2025emperor} systematically evaluate twenty approaches and find that none reliably restores clean performance; inference-time decontamination \citep{yang2024inference} and decontamination via forgetting \citep{zhang2025forget} similarly show limited effectiveness. DCR \citep{xu2025dcr} estimates decontaminated scores via fuzzy inference but produces point estimates without uncertainty quantification or domain-level diagnosis. ContamCal consumes detection signals as inputs and feeds them into a calibration framework that estimates decontaminated ability with credible intervals.
6	
7	\paragraph{IRT for LLM eval
…[truncated 2632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-17T17:26:11.334051+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-17T17:26:11.837013+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	We investigated whether IRT can separate ability from contamination artifacts on LLM benchmarks, finding three results: (1)~aggregate contamination effects from SFT injection are negligible (${\sim}$0.6--0.7pp), so raw accuracy is already well-calibrated and no correction method improves upon it; (2)~Min-K\%++ exhibits directional reversal at small scales; (3)~domain-level $\gamma$ is exploratory at $J=13$, requiring $J \geq 50$ for confirmation.
4	
5	\paragraph{Why not just use raw accuracy?}
6	Because the contamination effect is near zero (${\sim}$1pp), raw accuracy is the best aggregate estimator. IRT's value is not in improving MAE but in the decomposition analysis that \textit{explains why}: $\gamma$ quantifies that the effect is too small to distort rankings, provides a contamination existence diagnostic (Social Sciences $\gamma$ reaching significance), and reveals domain-level heterogeneity invisible to aggregate scoring. If future contamination produces larger effects (e.g., pretraining-phase exposure), the framework applies directly with no methodological changes. B6-DCR's systematic overcorrection (MAE 0.108--0.314) demonstrates the practical risk of correction methods that assume large effects without measurement-theoretic grounding.
7	
8	\paragraph{Circularity.}
9	Filtering items by exposure signal and then fitting IRT is not circular: $\tau$ measures $\theta$-dosage rank correlation, not $\gamma$ significance, and the oracle ablation confirms that even perfect binary labels do not produce a significant pooled $\gamma$.
10	
11	\paragraph{Implications and future work.}
12	Min-K\%++ should not be trusted below 1.5B. The negligible aggregate effect under SFT injection does not preclude larger effects under pretraining contamination; scaling to $J \geq 50$ and testing on naturally contaminated models are natural next steps.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-17T17:26:11.837449+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-17T17:26:11.837689+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	We identify nine limitations that bound the scope of our conclusions.
5	
6	\paragraph{Scale ceiling.}
7	All experiments use models at or below 3B parameters. Larger models (7B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.
8	
9	\paragraph{Signal coverage.}
10	S1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination below 1.5B (\S\ref{sec:signal_failure}).
11	
12	\paragraph{Ensemble size and per-domain power.}
13	Reliable $\gamma$ recovery requires $J \geq 50$. Our domain-level analysis ($J = 13$) yields significance for only one of eight MMLU domains. Per-domain $\gamma$ diagnosis at current ensemble sizes is exploratory.
14	
15	\paragraph{Position bias.}
16	Qwen2.5-0.5B exhibits position bias correlated with dosage (A-option rate: 46\% at d000 to 98\% at d100), necessitating exclusion from MC IRT analyses and reducing ensemble size.
17	
18	\paragraph{Credible interval coverage.}
19	Credible interval coverage (computed on 18 available checkpoints for MMLU and 20 for ARC) is benchmark-dependent at all levels: MMLU over-covers (50\% CI: 83\%, 80\% CI: 89\%, 95\% CI: 100\%) while ARC under-covers (50\% CI: 45\%, 80\% CI: 65\%, 95\% CI: 90\%). This reflects differential model fit quality rather than providing uniformly calibrated uncertainty.
20	
21	\paragraph{Model misfit in non-STEM domains.}
22	A single linear $\gamma$ cannot capture non-monotone contamination effects within a domain. Richer specifications may be required.
23	
24	\paragraph{SFT ecological validity.}
25	We use LoRA-based SFT injection exclusively. Pretraining-stage leakage, which occurs during large-scale web crawl ingestion, may produce qualitatively different contamination signatures: distributed exposure across many training st
…[truncated 1205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-17T17:26:12.940932+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-17T17:26:13.743547+00:00_

1	\section*{Ethics Statement}
2	
3	All experiments use publicly available, open-weight language models (Qwen2.5 and Llama-3.2) under their respective licenses. Contamination injection is performed via standard supervised fine-tuning on existing public benchmark items; no new data collection involving human subjects is conducted. All evaluation benchmarks (MMLU, ARC-Challenge, GSM8K) are publicly released datasets. This work does not involve private user data, personally identifiable information, or human annotation.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 802
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-17T17:26:15.148512+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-17T17:26:15.148975+00:00_

1	\appendix
2	
3	\section{4PL Extension}
4	\label{sec:4pl_details}
5	
6	For MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:
7	\begin{equation}
8	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
9	\end{equation}
10	with $c_i \sim \text{Beta}(5,20)$ and $d_i \sim \text{Beta}(20,5)$. This requires $J \geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\gamma$ at $J=13$; pooled calibration uses $J=16$.
11	
12	\section{Model Exclusion Details}
13	\label{sec:exclusion_details}
14	
15	Of the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\alpha=32$, lr$=5\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.
16	
17	\paragraph{Model sets across analyses.}
18	Table~\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\S\ref{sec:injection}). Core findings ($\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.
19	
20	\begin{table}[h]
21	\centering
22	\caption{Model set composition across analyses.}
23	\label{tab:model_sets}
24	\footnotesize
25	\begin{tabular}{lcll}
26	\toprule
27	Analysis & $J$ & Model Set & Section \\
28	\midrule
29	Pooled baselines & 16 & 8$\times$Qwen-1.5B + 8$\times$Qwen-3B & \S\ref{sec:calibration_results} \\
30	Domain $\gamma$ & 13 & 8$\times$Qwen-1.5B + 5$\times$Qwen-3B & \S\ref{sec:domain_differential} \\
31	Cross-family & 16--
…[truncated 5469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-17T17:26:15.500863+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales, descriptions, and any guidance. List each field reviewers must fill out."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales, descriptions, and any guidance. List each field reviewers must fill out."
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-17T17:26:21.286614+00:00_

# ACL ARR Review Form - Complete Structure

## Required Review Fields

### 1. **Paper Summary**
Reviewer describes the paper's topic and identifies any potential misunderstandings.

### 2. **Summary of Strengths**
Reviewer identifies reasons for publication, including novel methodology, empirical results, theoretical analysis, or clarity.

### 3. **Summary of Weaknesses**
Numbered concerns about correctness, limited impact, clarity, or other publication concerns.

### 4. **Comments/Suggestions/Typos**
Additional improvement suggestions beyond addressing stated weaknesses.

### 5. **Reviewer Confidence**
Scale 1-5: "Not my area" (1) to "Positive evaluation is correct" (5)

### 6. **Soundness**
Scale 1-5 (with .5 increments): Evaluates scientific rigor, experimental design, and claim support. Range from "Major Issues" (1) to "Excellent" (5).

### 7. **Excitement**
Scale 1-5 (with .5 increments): Subjective assessment of innovation, impact potential, and relevance. Ranges from "Not Exciting" (1) to "Highly Exciting" (5).

### 8. **Overall Assessment**
Scale 1-5 (with .5 increments): "Do not resubmit" (1) through "Consider for Award" (5), including Findings and Conference categories.

### 9. **Best Paper Justification**
Required if rating is "Consider for Award" or "Borderline Award."

## Additional Assessment Areas

- **Limitations and Societal Impact**
- **Ethical Concerns** (referencing ACL code of ethics)
- **Needs Ethics Review** (binary decision)
- **Reproducibility** (Scale 1-5)
- **Datasets** (Scale 1-5, if applicable)
- **Software** (Scale 1-5, if applicable)
- **Author Identity Knowledge** (Scale 1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5785
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-17T17:26:27.065136+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-17T17:26:27.115727+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-17T17:26:29.781661+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-17T17:28:35.668548+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 43, \"total_citations\": 70, \"unique_cited_keys\": 43, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 26, \"online_not_found\": 9, \"online_mismatch\": 8}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"carlini_2021_extracting\", \"type\": \"inproceedings\", \"title\": \"Extracting Training Data from Large Language Models\", \"authors\": \"Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew a...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 30th USENIX Security Symposium\"}, {\"key\": \"choi_2025_kds\", \"type\": \"inproceedings\", \"title\": \"How Contaminated Is Your Benchmark? Measuring Dataset Leakage in Large Language Models with Kernel Divergence\", \"authors\": \"Choi, Hyeong Kyu and Khanov, Maxim and Wei, Hongxin and Li, Yixuan\", \"year\": \"2025\", \"venue\": \"Proceedings of the 42nd International Conference on Machine Learning (ICML)\"}, {\"key\": \"cormack_2009_rrf\", \"type\": \"inproceedings\", \"title\": \"Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods\", \"authors\": \"Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan\", \"year\": \"2009\", \"venue\": \"Proceedings of the 32nd International ACM SIGIR Conference on Research and Devel...\"}, {\"key\": \"deboeck_2004_explanatory_irt\", \"type\": \"book\", \"title\": \"Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach\", \"authors\": \"De Boeck, Paul and Wilson, Mark\", \"year\": \"2004\", \"venue\": \"\"}, {\"key\": \"deng_2024_tsguessing\", \"type\": \"inproceedings\", \"title\": \"Investigating Data Contamination in Modern Benchmarks for Large Language Models\", \"authors\": \"Deng, Chunyuan and Zhao, Yilun and Tang, Xiangru and Gerstein, Mark and Cohan, A...\", \"year\": \"2024\", \"venu
…[truncated 34498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 125886
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-17T17:31:28.790702+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 方法框架有创新性（IRT + contamination covariate），但核心 null finding 的可信度受制于 SFT injection 的 ecological validity 和 additive γ 假设的不可验证性；统计推断有多处不严谨。\n\n---\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 γ 模型假设（additive linear）的充分性未验证；oracle ablation 的解释存在逻辑漏洞；域级显著性缺多重比较校正；ARC model fit 不合格仍纳入主表 |\n| Excitement | 3.5/5 | 将 IRT item compromise 理论引入 LLM contamination 分析的思路新颖；null finding 本身有实用价值但需更强的外部效度支撑 |\n| Reproducibility | 3.5/5 | Stan 代码细节（先验、链数、收敛标准）描述较完整；但 S4 (Self-Critique) 具体实现细节不足；exclusion criteria 涉及多次 ad-hoc 决策 |\n| Overall Assessment | 3.0 | 方法有价值，但实验设计和统计推断的多处问题阻碍了核心 claim 的可信度。适合 Findings，但需修复关键统计推断问题 |\n\n**Reviewer Confidence**: 4/5（IRT 和实验设计是我的专长领域）\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] SFT injection 作为 contamination proxy 的 ecological validity 不足以支撑核心 claim\n\n- 具体位置：§4.1, §5.1, Abstract (\"Raw accuracy is already well-calibrated\"), Limitations §7\n- 问题：论文最核心的发现是 \"aggregate contamination effect ~0.6-0.7pp, raw accuracy is already well-calibrated\"。但这一发现完全建立在 LoRA-based SFT injection (α=32, r=16) 的基础上，仅覆盖 0.5B-3B 模型。Pretraining-stage contamination（实际场景中最常见的形式）通过 trillion-token web crawl 在数以万计的 training steps 中分布式暴露，其效应机制与 SFT 集中注入根本不同。论文在 Limitations 中承认 \"Pretraining-stage leakage... may produce qualitatively different contamination signatures\"，但 Abstract 和 Conclusion 仍以无条件语气声称 \"raw accuracy is already well-calibrated\"。\n- 为什么影响接收：这是全文 framing 的根基。如果 null finding 是 SFT injection 的 artifact（而非 contamination 的一般性质），则论文的核心贡献从 \"contamination doesn't matter\" 降级为 \"SFT injection at 0.5B-3B doesn't matter much\"，后者的 impact 显著降低。\n- 建议修改方向：(1) Abstract/Introduction/Conclusion 中所有 claim 必须明确限定为 \"under SFT injection at ≤3B scale\"；(2) 讨论 pretraining contamination 的已知 effect size（如 Zhang et al. 2024 GSM1K 发现的 performance gap）作为对比锚点；(3) 最好能补充至少一个 naturally contaminated model 的案例分析。\n\n**N2** [critical] Additive linear γ 假设未经充分验证，oracle ablation 的解释存在逻辑漏洞\n\n- 具体位置：Eq. 2 (§3.2), §5.1 Oracle ablation, Limitations §9\n- 问题：2PL+γ 模型假设 contamination 效应在 logit scale 上对 exposure score 线性可加（Eq. 2: $a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}$）。Oracle ablation 显示即使 AUC=1.0 的 perfect binary labels，pooled γ 仍然不显著（γ = -0.012, CI [-0.145, 0.119]）。作者将其解释为 \"effect heterogeneity: injection inflates some items while disrupting others\"。但这个解释有两个问题：\n  (a) 如果 item-level effects 方向相反，则 additive γ 根本不是正确的模型规范——它会将相反方向的效应平均掉，给出一个接近零的估计，这是模型 misspecification 而非 genuine null finding。\n  (b) 如果 contamination 具有 threshold 效应或与 item discrimination 交互（如 Limitations §9 承认的），线性 γ 同样会被稀释为零。\n  论文无法区分 \"真的没有 contamination effect\" vs. \"有 effect 但 linear γ 捕捉不到\"。\n- 为什么影响接收：这直接影响 \"γ does not improve aggregate calibration\" 这一核心发现的可信度。\n- 建议修改方向：(1) 测试 item-level γ_i 或 γ * a_i 交互项模型，看是否能恢复 item-level effects；(2) 测试 threshold 模型（如 e_ij > cutoff 的 binary 处理）；(3) 如不做这些消融，必须在 claim 中明确 \"under the linear additive specification\"。\n\n**N3** [critical] 域级 γ 显著性（仅 Social Sciences）在无多重比较校正下的可解释性\n\n- 具体位置：Table 2, §5.4, Contribution 5\n- 问题：Table 2 对 MMLU 的 8 个 cognitive domain 分别拟合独立 IRT 模型，在 α=0.05 下只有 Social Sciences 达到显著（γ = -0.57, CI [-1.05, -0.10]）。作者明确声明 \"without multiple comparison correction\"，但仍将其作为 Contribution 5 并反复引用为 ContamCal 的 diagnostic value 的核心证据。在 8 次独立检验下，Bonferroni 校正后 α = 0.00625，Social Sciences 的 CI 上界为 -0.10，在校正后极可能不再显著。即使用更宽松的 Benjamini-Hochberg，只有 1/8 显著的模式也无法通过 FDR 校正。\n- 为什么影响接收：这是论文 \"diagnostic value\" narrative 的主要实证支撑。如果这唯一的显著结果在统计校正后消失，论文关于 γ 提供 domain-level diagnosis 的 claim 失去实验支持。\n- 建议修改方向：(1) 报告 Bonferroni 或 BH 校正后的结果；(2) 如果校正后不显著，调整 framing 为 \"suggestive pattern requiring higher-powered replication\"；(3) 讨论 J=13 在 8 个域分别拟合时每个域的有效样本量。\n\n**N4** [critical] ARC-Challenge model fit 不合格（PPP < 0.05）但仍纳入 Table 3 主要结果\n\n- 具体位置：§5.4 \"ARC-Challenge model fit is marginal across all tested configurations (PPP < 0.05 at J=8, 13, and 16)\", Table 3 (tab:baselines)\n- 问题：论文在 §5.4 明确报告 ARC-Challenge 在所有 J 配置下 PPP < 0.05，表明 2PL+γ 模型对 ARC 拟合不佳。但 Table 3 仍然报告 ARC 的完整 baseline 对比结果（包括 ContamCal MAE=0.020, τ=0.609），且在 Abstract 中引用 ARC 的 \"~0.7pp\" 效应。一个 model fit 不合格的 benchmark 上的数值结论本身不可靠。\n- 为什么影响接收：这是基本的统计规范问题——如果模型不拟合数据，从模型推出的校准数值不具参考价值。\n- 建议修改方向：(1) 在 Table 3 中 ARC 列加注 PPP 值，提醒读者解读需谨慎；(2) 考虑从 Abstract 中移除 ARC 的具体数值（~0.7pp）；(3) 讨论 ARC misfit 的原因（是 item pool 异质性还是模型规范不足？）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] J 值在不同分析间不一致，且远低于 identifiability threshold\n\n- 具体位置：§4.1, Appendix B (Table A1), §5.3\n- 问题：pooled baselines 用 J=16，domain γ 用 J=13，GSM8K 用 J=24，cross-family 用 J=18-28。论文自己的 simulation (§5.3) 证明 reliable γ recovery 需要 J≥50，但所有实验都远低于此。更具体地，J=13 的 domain-level analysis 每个域只有 13 个 respondent（8×1.5B + 5×3B），且 3B 比 1.5B 少——这意味着 3B 的 contamination dosage 覆盖不完整。J 值不一致源于实验进度（\"domain-level runs preceded the 3B retraining\"），这本身反映了实验设计的不严谨。\n- 建议：(1) 在一个统一的 J 下重做核心分析（至少 J=16）；(2) 如果不可行，在每张表和每个 figure 中明确标注 J 值和具体 model composition；(3) 讨论 J=13 vs J=16 结果的一致性。\n\n**W2** [warning] RRF-filtered 300 items vs random 2000 items 的对比可能存在 confound\n\n- 具体位置：§5.1 \"RRF-guided item filtering substantially improves IRT calibration\"\n- 问题：τ = 0.73 (300 RRF-filtered) vs τ = 0.46 (2000 random) 的对比不控制 item discrimination。RRF filtering 选出的 300 items 可能恰好有更高的 discrimination parameter（a_i），这本身就会改善 IRT calibration，与 contamination signal 无关。正确的对比应该是：(a) 300 random items（控制 item 数量）；(b) 300 items filtered by discrimination alone（控制 item 质量）；(c) 300 RRF-filtered items。\n- 建议：加入 discrimination-matched random subset 的对比。\n\n**W3** [warning] CI coverage 报告不完整\n\n- 具体位置：Limitations §5 (\"MMLU over-covers... ARC under-covers\")\n- 问题：50% CI coverage: MMLU 83%, ARC 45%；80% CI: MMLU 89%, ARC 65%；95% CI: MMLU 100%, ARC 90%。ARC 在 50% 和 80% 水平严重 under-cover，说明模型的 uncertainty 估计过于自信。结合 ARC PPP < 0.05 的 model fit 问题，ARC 上的所有 credible interval 都不可信。MMLU 在 50% 水平的 83% over-coverage 也表明 posterior 过于保守。这些数字仅在 Limitations 中提到，但对解读主要结果至关重要。\n- 建议：在主文结果部分报告 CI coverage，并讨论对 claim 可信度的影响。\n\n**W4** [warning] Cross-family analysis (Llama) 统计功效极低\n\n- 具体位置：§4.2, §5.5, Appendix E (mentioned but content not shown)\n- 问题：J=4 Llama models (单一 seed)，其中 MMLU d100 还被排除（catastrophic format collapse），实际 MMLU 只有 J=3 (d000, d005, d025)。论文声称 \"post-hoc power calculations in Appendix E\"，但 Appendix E 在投稿版中未找到独立内容（只出现在 §4.2 作为引用）。用 J=3-4 得出 \"RRF exposure scores generalize across architectures\" 和 \"calibration generalizes; diagnosis does not\" 的结论缺乏统计基础。\n- 建议：(1) 大幅弱化 cross-family generalization 的 claim 措辞；(2) 补充 Appendix E 的完整 power analysis。\n\n**W5** [warning] γ ~ N(0,1) 先验的合理性和 sensitivity analysis 缺失\n\n- 具体位置：§3.2 Inference paragraph\n- 问题：γ ~ N(0,1) 在 logit scale 上意味着 contamination effect 的先验预期覆盖 [-2, +2] 的范围（95% prior CI）。在 logit scale 上，±2 对应非常大的 probability shift。这个先验是 weakly informative 还是 informative 取决于 exposure score 的分布——如果 e_ij 接近 0 或 1，γ 的实际效应被 e_ij 调制后可以从接近 0 到 ±2。论文没有报告 e_ij 的经验分布，也没有做 prior sensitivity analysis。\n- 建议：(1) 报告 RRF scores e_ij 的分布（mean, SD, min, max）；(2) 至少用一个替代先验（如 N(0, 0.5) 或 N(0, 2)）做 sensitivity check。\n\n**W6** [warning] Min-K%++ directional reversal 的因果解释缺少证据\n\n- 具体位置：§5.2, Contribution 3\n- 问题：论文假设 \"SFT injection at 0.5B disrupts the token-level surprisal landscape so severely that contaminated items (overfit at the response level) paradoxically show reduced token-level fluency\"。这只是一个猜测（\"We hypothesize\"），缺乏任何直接验证。可能的替代解释包括：(a) 0.5B 模型的 position bias confound（论文已发现 A-option rate 从 46% 到 98%）改变了 token distribution，而非 surprisal landscape 的 disruption；(b) LoRA at 0.5B 的 rank-16 已经接近 full-rank，导致 catastrophic forgetting。\n- 建议：(1) 提供 token-level surprisal distribution 的直接比较（contaminated vs clean items at 0.5B）；(2) 或者明确将此作为 \"observed phenomenon, mechanism TBD\" 而非 contribution。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 2 (domain gamma): PPP 值全部标记为 \"---\"。如果未计算 per-domain PPP，这是一个重要缺失（domain-level model fit 未验证）；如果计算了但结果不好而省略，更令人担忧。\n- §3.2 Eq. 2 的 additive structure interpretation (\"contamination shifts the effective difficulty of item i by γ_k · e_ij / a_i\") 在数学上只在 linearization 近似下成立，不是精确的。\n- B2-Single2PL+γ 在 Table 3 中缺失，但在 §4.4 baselines 列表中被定义。\n- \"Calibration\" 一词在 ML 社区中的歧义：尽管 §2 Related Work 已做澄清，Abstract 中直接使用 \"well-calibrated\" 不加限定仍可能误导读者。\n- 引用验证：43 条引用中 9 条未在 OpenAlex 找到（含 sun2025emperor, kocyigit2025impact 等较新论文，可能是 indexing delay），8 条有 minor mismatch（多为 author parsing 差异），整体引用质量可接受。\n\n---\n\n## 缺失引用\n\n- **Pretraining contamination effect size**: 论文未引用直接测量 pretraining contamination effect size 的工作。Zhang et al. (2024, GSM1K) 虽被引用但主要用于 related work，未作为 calibration anchor。如果有更多关于 pretraining contamination 导致多少 pp 分数膨胀的已有证据，应与本文的 SFT 结果做对比。\n- **IRT model comparison / selection**: 论文未引用 WAIC, LOO-CV, 或 Bayes Factor 等模型比较文献，但在 2PL vs 4PL vs 2PL+γ 的选择上需要这类工具。\n- **Bayesian workflow**: Gelman et al. (2020) \"Bayesian Workflow\" 或 Gabry et al. (2019) \"Visualization in Bayesian workflow\" 在先验选择和 posterior predictive checking 方面是标准参考。\n\n---\n\n## 主要优势\n\n1. **问题定位准确且有实用价值**：将 contamination detection（binary flag）和 calibration（score adjustment）连接起来，填补了两个研究方向之间的空白。Framing 清晰，动机充分。\n2. **方法框架设计优雅**：将 IRT item compromise 理论和 explanatory IRT 引入 LLM evaluation 是一个有价值的跨领域迁移。RRF 的 training-free 设计避免了 meta-circularity 问题。\n3. **Negative result 的诚实报告**：论文坦承 null finding（γ 不显著、raw accuracy dominates），这种诚实在 ML 社区中比较少见且值得肯定。\n4. **Identifiability 分析有前瞻价值**：simulation study 建立的 \"AUC ≥ 0.55, J ≥ 50\" threshold 对未来 IRT-based evaluation 研究有实际指导意义。\n5. **Min-K%++ directional reversal 发现有即时实用价值**：documenting 小模型上 detection signal 的反转是社区需要知道的 fact。\n6. **写作质量好**：叙事连贯，技术细节充分，limitations 讨论全面诚实。\n\n---\n\n## 总结与建议\n\n论文提出了一个有价值的框架（ContamCal），将 contamination detection 和 IRT calibration 连接起来。但核心 null finding 的外部效度（SFT vs pretraining）、linear γ 的模型规范充分性、以及域级统计推断的严谨性构成了三个相互关联的根本问题：null finding 可能是 SFT injection 的局限 + linear γ misspecification 的共同 artifact，而非 contamination 本身的性质。如果修复 N1-N4 中的 claim scoping 和统计推断问题，该工作可以作为 Findings 接收。要达到 Main conference 水平，需要 (1) 至少一个 pretraining contamination 的验证案例，(2) 替代 γ 规范的消融实验，(3) 多重比较校正后仍成立的 domain-level evidence。",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 方法框架有创新性（IRT + contamination covariate），但核心 null finding 的可信度受制于 SFT injection 的 ecological validity 和 additive γ 假设的不可验证性；统计推断有多处不严谨。\n\n---\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 γ 模型假设（additive linear）的充分性未验证；oracle ablation 的解释存在逻辑漏洞；域级显著性缺多重比较校正；ARC model fit 不合格仍纳入主表 |\n| Excitement | 3.5/5 | 将 IRT item compromise 理论引入 LLM contamination 分析的思路新颖；null finding 本身有实用价值但需更强的外部效度支撑 |\n| Reproducibility | 3.5/5 | Stan 代码细节（先验、链数、收敛标准）描述较完整；但 S4 (Self-Critique) 具体实现细节不足；exclusion criteria 涉及多次 ad-hoc 决策 |\n| Overall Assessment | 3.0 | 方法有价值，但实验设计和统计推断的多处问题阻碍了核心 claim 的可信度。适合 Findings，但需修复关键统计推断问题 |\n\n**Reviewer Confidence**: 4/5（IRT 和实验设计是我的专长领域）\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] SFT injection 作为 contamination proxy 的 ecological validity 不足以支撑核心 claim\n\n- 具体位置：§4.1, §5.1, Abstract (\"Raw accuracy is already well-calibrated\"), Limitations §7\n- 问题：论文最核心的发现是 \"aggregate contamination effect ~0.6-0.7pp, raw accuracy is already well-calibrated\"。但这一发现完全建立在 LoRA-based SFT injection (α=32, r=16) 的基础上，仅覆盖 0.5B-3B 模型。Pretraining-stage contamination（实际场景中最常见的形式）通过 trillion-token web crawl 在数以万计的 training steps 中分布式暴露，其效应机制与 SFT 集中注入根本不同。论文在 Limitations 中承认 \"Pretraining-stage leakage... may produce qualitatively different contamination signatures\"，但 Abstract 和 Conclusion 仍以无条件语气声称 \"raw accuracy is already well-calibrated\"。\n- 为什么影响接收：这是全文 framing 的根基。如果 null finding 是 SFT injection 的 artifact（而非 contamination 的一般性质），则论文的核心贡献从 \"contamination doesn't matter\" 降级为 \"SFT injection at 0.5B-3B doesn't matter much\"，后者的 impact 显著降低。\n- 建议修改方向：(1) Abstract/Introduction/Conclusion 中所有 claim 必须明确限定为 \"under SFT injection at ≤3B scale\"；(2) 讨论 pretraining contamination 的已知 effect size（如 Zhang et al. 2024 GSM1K 发现的 performance gap）作为对比锚点；(3) 最好能补充至少一个 naturally contaminated model 的案例分析。\n\n**N2** [critical] Additive linear γ 假设未经充分验证，oracle ablation 的解释存在逻辑漏洞\n\n- 具体位置：Eq. 2 (§3.2), §5.1 Oracle ablation, Limitations §9\n- 问题：2PL+γ 模型假设 contamination 效应在 logit scale 上对 exposure score 线性可加（Eq. 2: $a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}$）。Oracle ablation 显示即使 AUC=1.0 的 perfect binary labels，pooled γ 仍然不显著（γ = -0.012, CI [-0.145, 0.119]）。作者将其解释为 \"effect heterogeneity: injection inflates some items while disrupting others\"。但这个解释有两个问题：\n  (a) 如果 item-level effects 方向相反，则 additive γ 根本不是正确的模型规范——它会将相反方向的效应平均掉，给出一个接近零的估计，这是模型 misspecification 而非 genuine null finding。\n  (b) 如果 contamination 具有 threshold 效应或与 item discrimination 交互（如 Limitations §9 承认的），线性 γ 同样会被稀释为零。\n  论文无法区分 \"真的没有 contamination effect\" vs. \"有 effect 但 linear γ 捕捉不到\"。\n- 为什么影响接收：这直接影响 \"γ does not improve aggregate calibration\" 这一核心发现的可信度。\n- 建议修改方向：(1) 测试 item-level γ_i 或 γ * a_i 交互项模型，看是否能恢复 item-level effects；(2) 测试 threshold 模型（如 e_ij > cutoff 的 binary 处理）；(3) 如不做这些消融，必须在 claim 中明确 \"under the linear additive specification\"。\n\n**N3** [critical] 域级 γ 显著性（仅 Social Sciences）在无多重比较校正下的可解释性\n\n- 具体位置：Table 2, §5.4, Contribution 5\n- 问题：Table 2 对 MMLU 的 8 个 cognitive domain 分别拟合独立 IRT 模型，在 α=0.05 下只有 Social Sciences 达到显著（γ = -0.57, CI [-1.05, -0.10]）。作者明确声明 \"without multiple comparison correction\"，但仍将其作为 Contribution 5 并反复引用为 ContamCal 的 diagnostic value 的核心证据。在 8 次独立检验下，Bonferroni 校正后 α = 0.00625，Social Sciences 的 CI 上界为 -0.10，在校正后极可能不再显著。即使用更宽松的 Benjamini-Hochberg，只有 1/8 显著的模式也无法通过 FDR 校正。\n- 为什么影响接收：这是论文 \"diagnostic value\" narrative 的主要实证支撑。如果这唯一的显著结果在统计校正后消失，论文关于 γ 提供 domain-level diagnosis 的 claim 失去实验支持。\n- 建议修改方向：(1) 报告 Bonferroni 或 BH 校正后的结果；(2) 如果校正后不显著，调整 framing 为 \"suggestive pattern requiring higher-powered replication\"；(3) 讨论 J=13 在 8 个域分别拟合时每个域的有效样本量。\n\n**N4** [critical] ARC-Challenge model fit 不合格（PPP < 0.05）但仍纳入 Table 3 主要结果\n\n- 具体位置：§5.4 \"ARC-Challenge model fit is marginal across all tested configurations (PPP < 0.05 at J=8, 13, and 16)\", Table 3 (tab:baselines)\n- 问题：论文在 §5.4 明确报告 ARC-Challenge 在所有 J 配置下 PPP < 0.05，表明 2PL+γ 模型对 ARC 拟合不佳。但 Table 3 仍然报告 ARC 的完整 baseline 对比结果（包括 ContamCal MAE=0.020, τ=0.609），且在 Abstract 中引用 ARC 的 \"~0.7pp\" 效应。一个 model fit 不合格的 benchmark 上的数值结论本身不可靠。\n- 为什么影响接收：这是基本的统计规范问题——如果模型不拟合数据，从模型推出的校准数值不具参考价值。\n- 建议修改方向：(1) 在 Table 3 中 ARC 列加注 PPP 值，提醒读者解读需谨慎；(2) 考虑从 Abstract 中移除 ARC 的具体数值（~0.7pp）；(3) 讨论 ARC misfit 的原因（是 item pool 异质性还是模型规范不足？）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] J 值在不同分析间不一致，且远低于 identifiability threshold\n\n- 具体位置：§4.1, Appendix B (Table A1), §5.3\n- 问题：pooled baselines 用 J=16，domain γ 用 J=13，GSM8K 用 J=24，cross-family 用 J=18-28。论文自己的 simulation (§5.3) 证明 reliable γ recovery 需要 J≥50，但所有实验都远低于此。更具体地，J=13 的 domain-level analysis 每个域只有 13 个 respondent（8×1.5B + 5×3B），且 3B 比 1.5B 少——这意味着 3B 的 contamination dosage 覆盖不完整。J 值不一致源于实验进度（\"domain-level runs preceded the 3B retraining\"），这本身反映了实验设计的不严谨。\n- 建议：(1) 在一个统一的 J 下重做核心分析（至少 J=16）；(2) 如果不可行，在每张表和每个 figure 中明确标注 J 值和具体 model composition；(3) 讨论 J=13 vs J=16 结果的一致性。\n\n**W2** [warning] RRF-filtered 300 items vs random 2000 items 的对比可能存在 confound\n\n- 具体位置：§5.1 \"RRF-guided item filtering substantially improves IRT calibration\"\n- 问题：τ = 0.73 (300 RRF-filtered) vs τ = 0.46 (2000 random) 的对比不控制 item discrimination。RRF filtering 选出的 300 items 可能恰好有更高的 discrimination parameter（a_i），这本身就会改善 IRT calibration，与 contamination signal 无关。正确的对比应该是：(a) 300 random items（控制 item 数量）；(b) 300 items filtered by discrimination alone（控制 item 质量）；(c) 300 RRF-filtered items。\n- 建议：加入 discrimination-matched random subset 的对比。\n\n**W3** [warning] CI coverage 报告不完整\n\n- 具体位置：Limitations §5 (\"MMLU over-covers... ARC under-covers\")\n- 问题：50% CI coverage: MMLU 83%, ARC 45%；80% CI: MMLU 89%, ARC 65%；95% CI: MMLU 100%, ARC 90%。ARC 在 50% 和 80% 水平严重 under-cover，说明模型的 uncertainty 估计过于自信。结合 ARC PPP < 0.05 的 model fit 问题，ARC 上的所有 credible interval 都不可信。MMLU 在 50% 水平的 83% over-coverage 也表明 posterior 过于保守。这些数字仅在 Limitations 中提到，但对解读主要结果至关重要。\n- 建议：在主文结果部分报告 CI coverage，并讨论对 claim 可信度的影响。\n\n**W4** [warning] Cross-family analysis (Llama) 统计功效极低\n\n- 具体位置：§4.2, §5.5, Appendix E (mentioned but content not shown)\n- 问题：J=4 Llama models (单一 seed)，其中 MMLU d100 还被排除（catastrophic format collapse），实际 MMLU 只有 J=3 (d000, d005, d025)。论文声称 \"post-hoc power calculations in Appendix E\"，但 Appendix E 在投稿版中未找到独立内容（只出现在 §4.2 作为引用）。用 J=3-4 得出 \"RRF exposure scores generalize across architectures\" 和 \"calibration generalizes; diagnosis does not\" 的结论缺乏统计基础。\n- 建议：(1) 大幅弱化 cross-family generalization 的 claim 措辞；(2) 补充 Appendix E 的完整 power analysis。\n\n**W5** [warning] γ ~ N(0,1) 先验的合理性和 sensitivity analysis 缺失\n\n- 具体位置：§3.2 Inference paragraph\n- 问题：γ ~ N(0,1) 在 logit scale 上意味着 contamination effect 的先验预期覆盖 [-2, +2] 的范围（95% prior CI）。在 logit scale 上，±2 对应非常大的 probability shift。这个先验是 weakly informative 还是 informative 取决于 exposure score 的分布——如果 e_ij 接近 0 或 1，γ 的实际效应被 e_ij 调制后可以从接近 0 到 ±2。论文没有报告 e_ij 的经验分布，也没有做 prior sensitivity analysis。\n- 建议：(1) 报告 RRF scores e_ij 的分布（mean, SD, min, max）；(2) 至少用一个替代先验（如 N(0, 0.5) 或 N(0, 2)）做 sensitivity check。\n\n**W6** [warning] Min-K%++ directional reversal 的因果解释缺少证据\n\n- 具体位置：§5.2, Contribution 3\n- 问题：论文假设 \"SFT injection at 0.5B disrupts the token-level surprisal landscape so severely that contaminated items (overfit at the response level) paradoxically show reduced token-level fluency\"。这只是一个猜测（\"We hypothesize\"），缺乏任何直接验证。可能的替代解释包括：(a) 0.5B 模型的 position bias confound（论文已发现 A-option rate 从 46% 到 98%）改变了 token distribution，而非 surprisal landscape 的 disruption；(b) LoRA at 0.5B 的 rank-16 已经接近 full-rank，导致 catastrophic forgetting。\n- 建议：(1) 提供 token-level surprisal distribution 的直接比较（contaminated vs clean items at 0.5B）；(2) 或者明确将此作为 \"observed phenomenon, mechanism TBD\" 而非 contribution。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 2 (domain gamma): PPP 值全部标记为 \"---\"。如果未计算 per-domain PPP，这是一个重要缺失（domain-level model fit 未验证）；如果计算了但结果不好而省略，更令人担忧。\n- §3.2 Eq. 2 的 additive structure interpretation (\"contamination shifts the effective difficulty of item i by γ_k · e_ij / a_i\") 在数学上只在 linearization 近似下成立，不是精确的。\n- B2-Single2PL+γ 在 Table 3 中缺失，但在 §4.4 baselines 列表中被定义。\n- \"Calibration\" 一词在 ML 社区中的歧义：尽管 §2 Related Work 已做澄清，Abstract 中直接使用 \"well-calibrated\" 不加限定仍可能误导读者。\n- 引用验证：43 条引用中 9 条未在 OpenAlex 找到（含 sun2025emperor, kocyigit2025impact 等较新论文，可能是 indexing delay），8 条有 minor mismatch（多为 author parsing 差异），整体引用质量可接受。\n\n---\n\n## 缺失引用\n\n- **Pretraining contamination effect size**: 论文未引用直接测量 pretraining contamination effect size 的工作。Zhang et al. (2024, GSM1K) 虽被引用但主要用于 related work，未作为 calibration anchor。如果有更多关于 pretraining contamination 导致多少 pp 分数膨胀的已有证据，应与本文的 SFT 结果做对比。\n- **IRT model comparison / selection**: 论文未引用 WAIC, LOO-CV, 或 Bayes Factor 等模型比较文献，但在 2PL vs 4PL vs 2PL+γ 的选择上需要这类工具。\n- **Bayesian workflow**: Gelman et al. (2020) \"Bayesian Workflow\" 或 Gabry et al. (2019) \"Visualization in Bayesian workflow\" 在先验选择和 posterior predictive checking 方面是标准参考。\n\n---\n\n## 主要优势\n\n1. **问题定位准确且有实用价值**：将 contamination detection（binary flag）和 calibration（score adjustment）连接起来，填补了两个研究方向之间的空白。Framing 清晰，动机充分。\n2. **方法框架设计优雅**：将 IRT item compromise 理论和 explanatory IRT 引入 LLM evaluation 是一个有价值的跨领域迁移。RRF 的 training-free 设计避免了 meta-circularity 问题。\n3. **Negative result 的诚实报告**：论文坦承 null finding（γ 不显著、raw accuracy dominates），这种诚实在 ML 社区中比较少见且值得肯定。\n4. **Identifiability 分析有前瞻价值**：simulation study 建立的 \"AUC ≥ 0.55, J ≥ 50\" threshold 对未来 IRT-based evaluation 研究有实际指导意义。\n5. **Min-K%++ directional reversal 发现有即时实用价值**：documenting 小模型上 detection signal 的反转是社区需要知道的 fact。\n6. **写作质量好**：叙事连贯，技术细节充分，limitations 讨论全面诚实。\n\n---\n\n## 总结与建议\n\n论文提出了一个有价值的框架（ContamCal），将 contamination detection 和 IRT calibration 连接起来。但核心 null finding 的外部效度（SFT vs pretraining）、linear γ 的模型规范充分性、以及域级统计推断的严谨性构成了三个相互关联的根本问题：null finding 可能是 SFT injection 的局限 + linear γ misspecification 的共同 artifact，而非 contamination 本身的性质。如果修复 N1-N4 中的 claim scoping 和统计推断问题，该工作可以作为 Findings 接收。要达到 Main conference 水平，需要 (1) 至少一个 pretraining contamination 的验证案例，(2) 替代 γ 规范的消融实验，(3) 多重比较校正后仍成立的 domain-level evidence。",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-17T17:31:33.662773+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4872
}
```

</details>

---


### Assistant

_source line 200 · 2026-05-17T17:31:47.084545+00:00_

审稿报告已提交给 Review Director。

核心评价：**Overall 3.0 (Findings)**。方法框架（IRT + contamination covariate）有创新性，但存在四个 Must-Fix 问题：

1. **SFT injection 的 ecological validity** 不足以支撑 "raw accuracy is already well-calibrated" 的无条件 claim
2. **Additive linear γ 假设未验证**，oracle ablation 的 null result 无法区分 "真的没效应" vs "模型规范错误捕捉不到效应"
3. **域级 γ 显著性（仅 Social Sciences 1/8）缺多重比较校正**，Bonferroni 校正后极可能不再显著
4. **ARC PPP < 0.05** 模型拟合不合格但仍纳入主表报告数值结论

另有 6 个 Should-Fix（J 值不一致、RRF filtering confound、CI coverage、cross-family 功效不足、先验 sensitivity 缺失、Min-K%++ 因果解释无验证）。修复 claim scoping 和统计推断后适合 Findings 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 8

## Round 8

4 recorded events


### User

_source line 201 · 2026-05-17T17:34:25.887991+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应，对每个 Must-Fix 和 Should-Fix 问题标注 **[AGREE]** 或 **[REBUT]**，并提供你的理由（如适用，cite 论文中具体 Section/Table/Figure）。

---

### Reviewer 2 Overall: 3.0 (Findings)

**Must-Fix:**

**N1** [critical] 标题与核心发现之间的叙事断裂
- 标题 "Decomposing Contamination from Calibration" 承诺分解框架，但核心结论是"没有什么可分解的"（aggregate effect ~0.6-0.7pp, raw accuracy 最佳）。论文将此转化为 "diagnostic value" 叙事，但本质是 negative result wrapped in a methods paper。
- 建议：调整为 "does contamination need calibration" 的实证调查风格。

**N2** [critical] Null finding 的泛化性严重受限
- 仅基于 SFT injection 在 ≤3B 模型。2026 年已有 pretraining-level dose-response 研究（arXiv 2601.04301）表明 pretraining contamination 的效应显著大于 SFT。
- 建议：至少在 7B 上复现一个条件；引用 pretraining contamination 文献。

**N3** [critical] RRF multi-signal fusion 的实际贡献被自身实验否定
- S2 在 0.5B reverse，S4 在 <1.5B near-random。§5.2 承认 "RRF fusion degrades to S1-only"。Multi-signal fusion 在当前实验条件下无 added value。
- 建议：在 1.5B/3B 提供 RRF vs S1-only 的直接 ablation；或诚实降格 RRF 贡献。

**Should-Fix:**

**W1** Oracle ablation 解释不充分——"effect heterogeneity" vs "model misspecification" 未区分
**W2** 五个贡献过多且分散，稀释核心 story
**W3** 重要相关工作遗漏：Han et al. (EACL Findings 2026) "Quantifying Data Contamination in Psychometric Evaluations of LLMs" 是最直接的 concurrent work；arXiv 2601.04301; Chen et al. (EMNLP 2025) survey
**W4** Cross-family validation J=3-4 统计功效不足
**W5** Table 2 (domain γ) 缺少所有 domain 的 PPP 值
**W6** Abstract ~258 words，超过 ACL 推荐 150-250 words，数字过密

---

请对以上每个问题给出 [AGREE] 或 [REBUT]，并说明理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-17T17:35:48.903566+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: 标题与核心发现之间的叙事断裂**\n\n同意。标题 \"Decomposing Contamination from Calibration\" 暗示框架能有效分解两者，但论文的核心结论恰恰是 aggregate level 上无需分解（~0.6-0.7pp, raw accuracy 最佳）。论文试图用 \"diagnostic value\" 叙事挽救，但这个 pivot 在 Introduction (§1) 第四段才出现，且与 Contribution 1 (\"Empirical decomposition of contamination effects\") 的措辞矛盾——\"decomposition\" 暗示分出了有意义的成分，而实际结果是 contamination 成分接近零。\n\nR2 建议改为实证调查风格是合理的。我补充认为，如果保留当前标题，Introduction 的叙事线需要从第一段就铺设 \"decomposition 的结果可能是 null\" 的预期，而非在 Results 才 reveal surprise。当前写法（§1 para 4: \"Our experiments yield a surprising null result\"）是典型的实验报告风格，不符合顶会论文的故事驱动写法。\n\n**[AGREE] R2-N2: Null finding 的泛化性严重受限**\n\n完全同意，这与我的 N1 一致。SFT injection 在 ≤3B 模型上的 null finding 不能推广到 pretraining contamination。R2 引用的 arXiv 2601.04301 我无法独立核实，但论文自身在 Limitations (§7, \"SFT ecological validity\" paragraph) 已承认 \"Pretraining-stage leakage... may produce qualitatively different contamination signatures\"。更关键的是，论文已引用的 Zhang et al. (2024, GSM1K) 发现了 original vs regenerated items 之间的 performance gap，这提供了 pretraining contamination effect 可能非零的间接证据——但论文从未将自己的 SFT 结果与这个已知参照点做定量对比。\n\n我补充一点：即使无法在 7B 上复现（计算资源限制），论文至少应该在 Discussion 中做一个 back-of-envelope 估算——如果 pretraining contamination 的 effect size 是 SFT 的 5-10 倍（基于已有文献），ContamCal 在 J=50 条件下是否有足够 power 检测到？这种 prospective power analysis 能大幅增强论文的前瞻价值。\n\n**[AGREE with nuance] R2-N3: RRF multi-signal fusion 的实际贡献被自身实验否定**\n\n大部分同意，但有细微补充。R2 正确指出 §5.2 承认 \"RRF fusion degrades to S1-only performance\"——但这一表述主要针对 0.5B scale。在 3B 上，S2 的 Cohen's d ≈ +0.7（§5.2），具有中等判别力，RRF 理论上应优于 S1-only。**问题在于论文未提供 RRF vs S1-only 在 1.5B/3B 上的直接 ablation 对比**（τ, MAE, γ significance）。这是一个明显的实验缺口。\n\n我部分 rebut R2 \"multi-signal fusion 无 added value\" 的绝对表述：RRF 的设计动机（training-free, 避免 meta-circularity）在方法论层面是合理的（§3.1），且如果 S2 在更大模型上判别力更强，RRF 的 value 会显现。但在当前实验条件下，R2 的批评成立——论文需要在 3B 上展示 RRF > S1-only 的实证证据，否则 RRF 作为贡献确实站不住脚。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: Oracle ablation 解释不充分——\"effect heterogeneity\" vs \"model misspecification\" 未区分**\n\n完全同意，这与我的 N2 一致。Oracle ablation (§5.1: γ = -0.012, CI [-0.145, 0.119], PPP=0.41) 是论文中最重要的消融实验之一，但作者将 non-significant γ 归因于 \"effect heterogeneity\" 而未考虑 model misspecification。如我在 N2 中详述：additive linear γ 可能在 item-level effects 方向相反时被平均为零，这是模型规范问题而非数据问题。论文需要测试 item-level γ_i 或交互项模型来区分这两种解释。\n\n**[AGREE with reservation] R2-W2: 五个贡献过多且分散**\n\n部分同意。五个 contributions 确实分散了论文焦点——(1) null finding, (2) item filtering, (3) Min-K%++ reversal, (4) identifiability boundaries, (5) domain diagnosis 覆盖了从 \"contamination 不重要\" 到 \"detection signal 失效\" 到 \"IRT 样本量要求\" 的跨度过大。核心 story 应该是 (1)+(2)+(4)，即 \"IRT 框架在什么条件下能诊断 contamination\"。\n\n但我也理解作者的困境：null finding 作为 sole contribution 难以支撑 long paper，因此需要 side findings 填充。我建议将 (3) Min-K%++ reversal 和 (5) domain diagnosis 整合为 \"empirical observations\" 子节，而非独立 contributions。\n\n**[AGREE in principle] R2-W3: 重要相关工作遗漏**\n\n我无法独立核实 R2 引用的三篇具体论文（Han et al. EACL Findings 2026; arXiv 2601.04301; Chen et al. EMNLP 2025 survey），但如果 Han et al. 确实在 psychometric evaluation 框架下研究 LLM contamination，这是最直接的 concurrent work，必须引用和比较。作者应通过 web search 核实这些引用的存在性和相关性，并在 Related Work §2 \"IRT for LLM evaluation\" 段落中加入讨论。\n\n我在自己的审稿中也指出了引用缺失：论文未引用 Bayesian model comparison (WAIC/LOO-CV) 和 Bayesian workflow 的标准参考文献，这对先验选择和模型比较的严谨性有影响。\n\n**[AGREE] R2-W4: Cross-family validation J=3-4 统计功效不足**\n\n完全同意，与我的 W4 一致。MMLU 上排除 d100 后仅 J=3 Llama models，单一 seed。论文声称 \"post-hoc power calculations in Appendix E\" 但我在 Appendix 中未找到独立的 Appendix E 内容（Appendix 只有 A-D 节）。如果 power analysis 未实际提供，这是一个 missing evidence 的问题。\n\n**[AGREE] R2-W5: Table 2 (domain γ) 缺少所有 domain 的 PPP 值**\n\n完全同意，与我的小问题列表一致。Per-domain PPP 对判断 domain-level IRT model fit 至关重要。鉴于 ARC 已知 PPP < 0.05（§5.4），MMLU 的某些 domain（特别是 item 数较少的 domain）也可能存在 misfit。省略 PPP 值让读者无法判断 domain-level γ 估计是否可靠。\n\n**[AGREE] R2-W6: Abstract ~258 words，超过 ACL 推荐 150-250 words，数字过密**\n\n同意。Abstract 数字密度过高（~0.6-0.7pp, τ = 0.73 vs 0.46, Δτ = 0.27, γ = -0.57, Cohen's d = -1.55 to -1.98, MAE 0.108-0.314, AUC ≥ 0.55, J ≥ 50），审稿人 30 秒内难以提取核心信息。Abstract 应聚焦 2-3 个关键数字，其余移入正文。\n\n---\n\n### 综合意见\n\nR2 和我的审稿在核心判断上高度一致：**null finding 的外部效度（N1/N2 ↔ 我的 N1）**和 **linear γ 假设的充分性（W1 ↔ 我的 N2）**是最关键的两个问题。R2 额外提出的 RRF 贡献被自身实验否定（N3）是一个我未充分展开但同意的重要观察。\n\n两位 reviewer 均给出 Overall 3.0 (Findings)，反映了一致的判断：方法框架有价值，但当前实验证据不足以支撑核心 claims 的普遍性。",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: 标题与核心发现之间的叙事断裂**\n\n同意。标题 \"Decomposing Contamination from Calibration\" 暗示框架能有效分解两者，但论文的核心结论恰恰是 aggregate level 上无需分解（~0.6-0.7pp, raw accuracy 最佳）。论文试图用 \"diagnostic value\" 叙事挽救，但这个 pivot 在 Introduction (§1) 第四段才出现，且与 Contribution 1 (\"Empirical decomposition of contamination effects\") 的措辞矛盾——\"decomposition\" 暗示分出了有意义的成分，而实际结果是 contamination 成分接近零。\n\nR2 建议改为实证调查风格是合理的。我补充认为，如果保留当前标题，Introduction 的叙事线需要从第一段就铺设 \"decomposition 的结果可能是 null\" 的预期，而非在 Results 才 reveal surprise。当前写法（§1 para 4: \"Our experiments yield a surprising null result\"）是典型的实验报告风格，不符合顶会论文的故事驱动写法。\n\n**[AGREE] R2-N2: Null finding 的泛化性严重受限**\n\n完全同意，这与我的 N1 一致。SFT injection 在 ≤3B 模型上的 null finding 不能推广到 pretraining contamination。R2 引用的 arXiv 2601.04301 我无法独立核实，但论文自身在 Limitations (§7, \"SFT ecological validity\" paragraph) 已承认 \"Pretraining-stage leakage... may produce qualitatively different contamination signatures\"。更关键的是，论文已引用的 Zhang et al. (2024, GSM1K) 发现了 original vs regenerated items 之间的 performance gap，这提供了 pretraining contamination effect 可能非零的间接证据——但论文从未将自己的 SFT 结果与这个已知参照点做定量对比。\n\n我补充一点：即使无法在 7B 上复现（计算资源限制），论文至少应该在 Discussion 中做一个 back-of-envelope 估算——如果 pretraining contamination 的 effect size 是 SFT 的 5-10 倍（基于已有文献），ContamCal 在 J=50 条件下是否有足够 power 检测到？这种 prospective power analysis 能大幅增强论文的前瞻价值。\n\n**[AGREE with nuance] R2-N3: RRF multi-signal fusion 的实际贡献被自身实验否定**\n\n大部分同意，但有细微补充。R2 正确指出 §5.2 承认 \"RRF fusion degrades to S1-only performance\"——但这一表述主要针对 0.5B scale。在 3B 上，S2 的 Cohen's d ≈ +0.7（§5.2），具有中等判别力，RRF 理论上应优于 S1-only。**问题在于论文未提供 RRF vs S1-only 在 1.5B/3B 上的直接 ablation 对比**（τ, MAE, γ significance）。这是一个明显的实验缺口。\n\n我部分 rebut R2 \"multi-signal fusion 无 added value\" 的绝对表述：RRF 的设计动机（training-free, 避免 meta-circularity）在方法论层面是合理的（§3.1），且如果 S2 在更大模型上判别力更强，RRF 的 value 会显现。但在当前实验条件下，R2 的批评成立——论文需要在 3B 上展示 RRF > S1-only 的实证证据，否则 RRF 作为贡献确实站不住脚。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: Oracle ablation 解释不充分——\"effect heterogeneity\" vs \"model misspecification\" 未区分**\n\n完全同意，这与我的 N2 一致。Oracle ablation (§5.1: γ = -0.012, CI [-0.145, 0.119], PPP=0.41) 是论文中最重要的消融实验之一，但作者将 non-significant γ 归因于 \"effect heterogeneity\" 而未考虑 model misspecification。如我在 N2 中详述：additive linear γ 可能在 item-level effects 方向相反时被平均为零，这是模型规范问题而非数据问题。论文需要测试 item-level γ_i 或交互项模型来区分这两种解释。\n\n**[AGREE with reservation] R2-W2: 五个贡献过多且分散**\n\n部分同意。五个 contributions 确实分散了论文焦点——(1) null finding, (2) item filtering, (3) Min-K%++ reversal, (4) identifiability boundaries, (5) domain diagnosis 覆盖了从 \"contamination 不重要\" 到 \"detection signal 失效\" 到 \"IRT 样本量要求\" 的跨度过大。核心 story 应该是 (1)+(2)+(4)，即 \"IRT 框架在什么条件下能诊断 contamination\"。\n\n但我也理解作者的困境：null finding 作为 sole contribution 难以支撑 long paper，因此需要 side findings 填充。我建议将 (3) Min-K%++ reversal 和 (5) domain diagnosis 整合为 \"empirical observations\" 子节，而非独立 contributions。\n\n**[AGREE in principle] R2-W3: 重要相关工作遗漏**\n\n我无法独立核实 R2 引用的三篇具体论文（Han et al. EACL Findings 2026; arXiv 2601.04301; Chen et al. EMNLP 2025 survey），但如果 Han et al. 确实在 psychometric evaluation 框架下研究 LLM contamination，这是最直接的 concurrent work，必须引用和比较。作者应通过 web search 核实这些引用的存在性和相关性，并在 Related Work §2 \"IRT for LLM evaluation\" 段落中加入讨论。\n\n我在自己的审稿中也指出了引用缺失：论文未引用 Bayesian model comparison (WAIC/LOO-CV) 和 Bayesian workflow 的标准参考文献，这对先验选择和模型比较的严谨性有影响。\n\n**[AGREE] R2-W4: Cross-family validation J=3-4 统计功效不足**\n\n完全同意，与我的 W4 一致。MMLU 上排除 d100 后仅 J=3 Llama models，单一 seed。论文声称 \"post-hoc power calculations in Appendix E\" 但我在 Appendix 中未找到独立的 Appendix E 内容（Appendix 只有 A-D 节）。如果 power analysis 未实际提供，这是一个 missing evidence 的问题。\n\n**[AGREE] R2-W5: Table 2 (domain γ) 缺少所有 domain 的 PPP 值**\n\n完全同意，与我的小问题列表一致。Per-domain PPP 对判断 domain-level IRT model fit 至关重要。鉴于 ARC 已知 PPP < 0.05（§5.4），MMLU 的某些 domain（特别是 item 数较少的 domain）也可能存在 misfit。省略 PPP 值让读者无法判断 domain-level γ 估计是否可靠。\n\n**[AGREE] R2-W6: Abstract ~258 words，超过 ACL 推荐 150-250 words，数字过密**\n\n同意。Abstract 数字密度过高（~0.6-0.7pp, τ = 0.73 vs 0.46, Δτ = 0.27, γ = -0.57, Cohen's d = -1.55 to -1.98, MAE 0.108-0.314, AUC ≥ 0.55, J ≥ 50），审稿人 30 秒内难以提取核心信息。Abstract 应聚焦 2-3 个关键数字，其余移入正文。\n\n---\n\n### 综合意见\n\nR2 和我的审稿在核心判断上高度一致：**null finding 的外部效度（N1/N2 ↔ 我的 N1）**和 **linear γ 假设的充分性（W1 ↔ 我的 N2）**是最关键的两个问题。R2 额外提出的 RRF 贡献被自身实验否定（N3）是一个我未充分展开但同意的重要观察。\n\n两位 reviewer 均给出 Overall 3.0 (Findings)，反映了一致的判断：方法框架有价值，但当前实验证据不足以支撑核心 claims 的普遍性。",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-17T17:35:52.470020+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3566
}
```

</details>

---


### Assistant

_source line 204 · 2026-05-17T17:35:57.227709+00:00_

交叉回应已提交给 Review Director。对 R2 的 9 个问题中，我给出 7 个 [AGREE]、2 个 [AGREE with nuance/reservation]，核心共识集中在 SFT ecological validity、linear γ misspecification 风险、以及 cross-family 统计功效不足三个方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 9

## Round 9

44 recorded events


### User

_source line 205 · 2026-05-18T01:29:53.585924+00:00_

[Round 5 审稿请求]:
## Round 5 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）

### Venue 信息
- **目标**: EMNLP 2026 (通过 ACL Rolling Review)
- **Deadline**: 2026-05-25
- **格式**: Long paper ≤ 8 页正文 + 无限 references/appendix; Limitations/Ethics 不计入页数
- **模板**: ACL style, `[review]` option, double-blind
- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit

### 论文路径
`projects/contamcal-irt-calibration/docs/paper/main.tex`（各章节为独立 .tex 文件：abstract.tex, introduction.tex, related_work.tex, method.tex, experimental_setup.tex, results.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）

### 你的审查侧重
**方法严谨性 + 实验有效性**，重点关注：

1. **IRT 建模**
   - 2PL+γ 模型的统计假设是否合理（additive linear γ, independent per-domain fitting）
   - γ identifiability 分析（Fisher information, simulation study 设计）
   - 贝叶斯推断设置（priors, convergence diagnostics, PPP interpretation）
   - Prior sensitivity analysis 的充分性

2. **实验设计**
   - SFT injection 作为 contamination proxy 的生态效度（ecological validity）
   - Model exclusion 逻辑（0.5B 排除、3B checkpoint 重训练、Llama d100 排除）
   - J 值在不同分析中的不一致性（13/16/24/28）及其对结论的影响
   - Cross-family analysis（Llama J=4, single seed）的统计功效

3. **核心发现的可靠性**
   - Null finding（~0.6-0.7pp aggregate effect）是否可能是 SFT artifact 而非 general property
   - Oracle ablation 的双重解释（genuine null vs model misspecification）
   - Social Sciences γ=-0.57 是否在多重比较校正下存活
   - ARC PPP < 0.05 对 ARC 相关结论的影响

4. **信号分析**
   - RRF vs S1-only ablation 的完整性
   - Min-K%++ directional reversal 的因果解释
   - Signal AUC heatmap 的覆盖度

### 历史审稿关键 issue（供参考，但请独立评估当前论文）
- R2-W6 (critical): SFT ecological validity — 所有 claims 是否已限定为 "under SFT injection at ≤3B"
- R3-W10 (critical): Additive linear γ assumption — oracle ablation 是否同时讨论了 null effect 和 misspecification 两种解释
- R4-N1 (critical): 8 domains 中仅 1 个 significant — 是否有多重比较讨论
- R3-N3 (critical): ARC PPP < 0.05 — IRT-derived ARC 结果是否有充分 caveat
- R2-W1 (critical): RRF 在 1.5B/3B 退化为 S1-only — 是否有 ablation 证据

请提供完整审稿报告，包括 Summary, Strengths, Weaknesses（逐条编号），Questions, Overall Assessment（使用 EMNLP 评分标准），Confidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-18T01:30:18.958720+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-18T01:30:18.959211+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-18T01:30:18.962294+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-18T01:30:19.016096+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-18T01:30:19.019588+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-18T01:30:19.019975+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-18T01:30:26.712090+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2024 2025 reviewer guidelines review form criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2024 2025 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 213 · 2026-05-18T01:30:28.724174+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/contamcal-irt-calibration/docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/contamcal-irt-calibration/docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
  }
}
```

</details>

---


### Tool result

_source line 214 · 2026-05-18T01:30:28.925508+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-18T01:30:33.953601+00:00_

Web search results for query: "ACL Rolling Review 2024 2025 reviewer guidelines review form criteria dimensions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"aclrollingreview/acguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/acguidelines.md"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

I've successfully performed the web search for ACL Rolling Review 2024-2025 reviewer guidelines. Here are the key findings:

## Reviewer Scoring Dimensions

Starting with February 2025, ARR 
…[truncated 1385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7241
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-18T01:30:38.373721+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form 2025 soundness excitement overall assessment scoring scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form 2025 soundness excitement overall assessment scoring scale"
  }
}
```

</details>

---


### Tool call

_source line 217 · 2026-05-18T01:30:39.128450+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 218 · 2026-05-18T01:30:39.229534+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-18T01:30:46.078800+00:00_

Web search results for query: "ACL Rolling Review review form 2025 soundness excitement overall assessment scoring scale"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL ARR 2025 February | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FFebruary"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL ARR 2025 July | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FJuly"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here's information about the ACL Rolling Review form 2025:

## Scoring Scales

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be justified by the text of the review.

### Excitement Score
How
…[truncated 1094 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7705
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-18T01:30:51.522032+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-18T01:30:51.573535+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-18T01:30:52.128026+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-18T01:30:53.033835+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{Does LLM Benchmark Contamination Need Calibration?\\An IRT Decomposition Study}
13	
14	\author{Anonymous}
15	
16	\begin{document}
17	\maketitle
18	
19	\begin{abstract}
20	\input{abstract}
21	\end{abstract}
22	
23	\input{introduction}
24	\input{related_work}
25	\input{method}
26	\input{experimental_setup}
27	\input{results}
28	\input{conclusion}
29	
30	\input{limitations}
31	\input{ethics}
32	
33	\bibliography{references}
34	
35	\input{appendix}
36	
37	\end{document}
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-18T01:30:53.084580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-18T01:30:53.185422+00:00_

1	Training data contamination undermines the validity of Large Language Model (LLM) benchmark comparisons, yet existing detection methods stop at binary flags without quantifying score inflation. We investigate whether Item Response Theory (IRT) can separate genuine ability from contamination artifacts on existing benchmarks. Using controlled SFT injection across Qwen2.5 (0.5B--3B) and three benchmarks (MMLU, ARC-Challenge, GSM8K), we find that under SFT injection at $\leq$3B, contamination shifts aggregate accuracy by only ${\sim}$0.6--0.7 percentage points, smaller than the estimation noise of any correction method; raw accuracy is already well-calibrated. We develop ContamCal, a two-stage pipeline combining signal-guided item filtering with a contamination-augmented IRT model (2PL+$\gamma$). Item filtering improves calibration ($\tau = 0.73$ on 300 RRF-selected items vs.\ $\tau = 0.46$ on random 2000-item subsets, $\Delta\tau = 0.27$). The $\gamma$ parameter reveals domain-level heterogeneity: Social Sciences shows the strongest negative effect ($\gamma = -0.57$, posterior $P(\gamma<0) = 99.1\%$) within the Qwen family, a pattern requiring higher-powered replication. We further document that Min-K\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$). Simulation studies establish that reliable $\gamma$ recovery requires signal AUC $\geq 0.55$ and $J \geq 50$, exposing a structural gap between current practice and the statistical requirements for contamination diagnosis via IRT.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-18T01:30:53.236152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-18T01:30:53.287038+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection, resource allocation, and research priorities for large language models, yet training data contamination undermines the validity of these scores in ways that current evaluation cannot quantify \citep{hendrycks2021mmlu,chang2025benchmarking}. When models encounter test items during training, observed accuracy conflates genuine capability with memorization, and practitioners have no principled way to determine how much of a reported score reflects real understanding. The problem is compounded by the scale of modern training corpora: trillion-token web crawls make contamination pervasive and instance-level measurement infeasible \citep{oren2024proving}. Post-hoc calibration that quantifies contamination effects despite imperfect detection is therefore essential for trustworthy evaluation.
4	
5	Two developments make this gap urgent. First, \citet{sun2025emperor} systematically evaluate twenty contamination mitigation strategies (rephrasing, option shuffling, dynamic benchmark regeneration, and others) and demonstrate that none restores clean performance after contamination has occurred. This result forecloses the ``prevent contamination'' approach for models already trained on unrestricted web data. Second, contamination-free benchmarks \citep{white2024livebench} offer a partial solution but sacrifice the comparability and institutional knowledge accumulated around established benchmarks. Dynamic regeneration of test items may also be contaminated within weeks as web crawlers index benchmark repositories \citep{dong_2024_cdd}. The field therefore needs post-hoc statistical tools that can separate genuine ability from contamination artifacts on existing benchmarks.
6	
7	Detection methods such as Min-K\%++ \citep{zhang_2024_minkpp}, ConStat \citep{dekoninck2024constat}, and Kernel Divergence Signatures \citep{choi_2025_kds} can flag contaminated items but stop at detection. They d
…[truncated 3792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-18T01:30:59.217101+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment scales with all options listed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment scales with all options listed."
  }
}
```

</details>

---


### Tool call

_source line 229 · 2026-05-18T01:30:59.671869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 230 · 2026-05-18T01:31:00.174410+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is twofold: (1)~estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt}, adapting these frameworks through three structural modifications for LLM evaluation.
12	
13	\textit{Shared item pool.} A fixed item set is shared across all models, introducing residual correlations beyond scalar $\theta_j$ \citep{sanmartin_2009_irt}; we mitigate by fitting per-benchmark models.
14	\textit{Continuous exposure.} We replace binary leakage indicators with continuous scores $e_{ij} \in [0,1]$ derived from detection signals, as LLM contamination is graded rather than binary.
15	\textit{Counterfactual ability.} Training regime changes (SFT vs.\ RL) alter both representations and signal reliability; we recover clean ability via counterfactual inference (setting $e_{ij}=0$) rather than regime-specific parameters.
16	
17	\subsection{Stage 1: Multi-Signal Exposure Mapping}
18	\l
…[truncated 5746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 231 · 2026-05-18T01:31:00.174793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 232 · 2026-05-18T01:31:00.576657+00:00_

1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed using Qwen2.5 \citep{qwen2024qwen25} at three scales (0.5B, 1.5B, 3B parameters). For each scale, we fine-tune with Low-Rank Adaptation \citep[LoRA;][]{hu2022lora} ($\alpha=32$, $r=16$, lr$=5\times10^{-5}$) on a general-purpose SFT corpus into which benchmark items are injected at four dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), and d100 (100\%). Injected items are formatted as instruction-response pairs and pass a quality-control filter that removes ambiguous or malformed entries.
8	
9	Each configuration is trained with two random seeds (s42, s123), yielding 24 models across $3 \times 4 \times 2$ conditions. This within-family design isolates contamination dosage as the primary experimental variable while controlling for architecture, tokenizer, and pretraining data.
10	
11	We exclude 0.5B models from MMLU and ARC IRT due to answer-position bias that correlates with dosage (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}). Three initial 3B checkpoints trained with inconsistent LoRA hyperparameters were retrained under the unified protocol ($\alpha=32$, lr$=5\times10^{-5}$; Appendix~\ref{sec:exclusion_details}). Our pooled calibration analysis (Table~\ref{tab:baselines}) uses $J=16$ respondents for MMLU/ARC (1.5B$\times$8 + 3B$\times$8) and $J=24$ for GSM8K (all scales retained). Domain-level $\gamma$ analysis (Table~\ref{tab:domain_gamma}, \S\ref{sec:domain_differential}) uses $J=13$ (1.5B$\times$8 + 3B$\times$5), as it preceded completion of the 3B retraining. The eight 1.5B d000 models serve as the clean reference anchor in both configurations.
12	
13	\subsection{Cross-Family Analysis}
14	\label{sec:cross_family}
15	
16	To test whether IRT calibration is robust to inclusion of new model families, we fine-tune Llama-3.2-3B \citep{grattafiori202
…[truncated 2344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 233 · 2026-05-18T01:31:00.577052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 234 · 2026-05-18T01:31:00.728006+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Calibration Quality}
5	\label{sec:calibration_results}
6	
7	\paragraph{Item filtering improves calibration.}
8	RRF-guided item filtering substantially improves IRT calibration quality over random item subsets. On a random 2000-item MMLU subset (same $J=13$ model set), vanilla 2PL achieves $\tau = 0.46$; on the 300-item RRF-selected subset, $\tau = 0.73$ ($\Delta\tau = 0.27$, controlled for model composition). Signal-guided filtering concentrates items where contamination effects are detectable, enabling sharper ability-dosage separation. Exclusion sensitivity analysis (removing 0--50\% of top-exposure items from random 2000-item subsets, $J=13$) yields $\tau$ ranging from 0.46 to 0.60 with no monotonic trend, and $\gamma$ remains non-significant at all exclusion rates. The $\tau$ improvement is not driven by item discrimination: mean $a_i$ does not differ between RRF-selected and random subsets (Cohen's $d = 0.098$, $p > 0.05$; $r_{\text{exposure}, a_i} = -0.013$).
9	
10	\paragraph{RRF vs.\ single-signal ablation.}
11	Replacing RRF with S1-only exposure for item selection and IRT fitting causes convergence failure: MMLU S1-only yields $\hat{R} = 1.53$ (ESS$=$7), while ARC S1-only converges to a degenerate solution ($\gamma = 6.84$, PPP$=$0.000). The root cause is exposure variance compression: S1-only top-300 items concentrate in a narrow score band ($[0.749, 0.867]$), creating collinearity between $\gamma \cdot e_{ij}$ and difficulty parameters. Multi-signal RRF fusion preserves broader exposure distributions that enable $\gamma$ identification. RRF's value is therefore not only signal quality aggregation but exposure variance for IRT parameter separability. To control for subset size, we evaluated random 300-item subsets (5 seeds, $J=16$): $\tau = 0.554 \pm 0.048$, significantly lower than RRF-selected items ($\tau = 0.731$, $\Delta\tau = 0.177$), confirming that signal-guided item selection provides a mea
…[truncated 14646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-18T01:31:04.596591+00:00_

# ACL Rolling Review Form - Complete Scoring Structure

## Core Evaluation Dimensions

**Soundness** (5-point scale)
- 5 = Excellent: "one of the most thorough I have seen, given its type"
- 4 = Strong: "sufficient support for all of its claims"
- 3 = Acceptable: "sufficient support for its main claims"
- 2 = Poor: "main claims are not sufficiently supported"
- 1 = Major Issues: "not yet sufficiently thorough to warrant publication"

**Excitement** (5-point scale)
- 5 = Highly Exciting: would recommend to others
- 4 = Exciting: would mention to others
- 3 = Interesting: might mention or attend presentation
- 2 = Potentially Interesting: "does not resonate with me"
- 1 = Not Exciting: lacks relevance to computational linguistics

**Reviewer Confidence** (5-point scale)
- 5 = "Positive that my evaluation is correct"
- 4 = "Quite sure" about assessment validity
- 3 = "Pretty sure, but there's a chance I missed something"
- 2 = "Willing to defend my evaluation" but likely missed details
- 1 = "Not my area" or paper is difficult to understand

**Overall Assessment** (recommendation scale)
- 5 = Consider for Award (top 2.5%)
- 4.5 = Borderline Award
- 4 = Conference acceptance
- 3.5 = Borderline Conference
- 3 = Findings acceptance
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = Do not resubmit

## Additional Evaluation Areas

Reproducibility, ethical concerns, limitations, dataset value, software value, and author anonymity assessment also included.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5379
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-18T01:31:10.825219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-18T01:31:11.881452+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination detection and mitigation.}
5	Membership inference for contamination detection builds on the foundations of training data extraction \citep{carlini_2021_extracting} and membership inference attacks \citep{shokri_2017_mia}. Current approaches include Min-K\% \citep{shi_2023_minkprob} and Min-K\%++ \citep{zhang_2024_minkpp} (token-level surprisal), ConStat \citep{dekoninck2024constat} (accuracy gaps on paraphrased items), CDD/TED \citep{dong_2024_cdd} (completion-based probes), KDS \citep{choi_2025_kds} (kernel divergence), TS-Guessing \citep{deng_2024_tsguessing} (temporal splits), and Time Travel \citep{golchin_2024_time_travel} (guided generation probes). Concurrent with our work, \citet{tao2025detecting} propose an entropy collapse method for RL-trained models. \citet{kocyigit2025impact} show that post-training procedures (RLHF, DPO) degrade detection signal reliability; token-level methods become unreliable on instruction-tuned models. \citet{zhang_2024_gsm1k} construct GSM1K as a parallel test set to quantify GSM8K contamination: performance gaps between original and regenerated items serve as a natural experiment for contamination measurement. Recent surveys \citep{chen2025benchmarking,singh2024evaluation} systematically categorize these approaches. These methods flag contamination but do not produce adjusted scores. On the mitigation side, \citet{sun2025emperor} systematically evaluate twenty approaches and find that none reliably restores clean performance; inference-time decontamination \citep{yang2024inference} and decontamination via forgetting \citep{zhang2025forget} similarly show limited effectiveness. DCR \citep{xu2025dcr} estimates decontaminated scores via fuzzy inference but produces point estimates without uncertainty quantification or domain-level diagnosis. ContamCal consumes detection signals as inputs and feeds them into a calibration framework that estimates decon
…[truncated 2815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1056
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-18T01:31:11.932097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-18T01:31:12.434761+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	We investigated whether IRT can separate ability from contamination artifacts on LLM benchmarks, finding three results: (1)~under SFT injection at $\leq$3B, aggregate contamination effects are negligible (${\sim}$0.6--0.7pp), so raw accuracy is already well-calibrated and no correction method improves upon it; (2)~Min-K\%++ exhibits directional reversal at small scales; (3)~domain-level $\gamma$ is exploratory at $J=13$, requiring $J \geq 50$ for confirmation.
4	
5	\paragraph{Why not just use raw accuracy?}
6	Under SFT injection at $\leq$3B, the contamination effect is near zero (${\sim}$0.6--0.7pp), making raw accuracy the best aggregate estimator. IRT's value is not in improving MAE but in the decomposition analysis that \textit{explains why}: $\gamma$ quantifies that the effect is too small to distort rankings, provides a contamination existence diagnostic (Social Sciences posterior $P(\gamma<0) = 99.1\%$, robust to prior specification; Appendix~\ref{sec:prior_sensitivity}), and reveals domain-level heterogeneity invisible to aggregate scoring. If future contamination produces larger effects (e.g., pretraining-phase exposure), the framework applies directly with no methodological changes. B6-DCR's systematic overcorrection (MAE 0.108--0.314) demonstrates the practical risk of correction methods that assume large effects without measurement-theoretic grounding.
7	
8	\paragraph{Circularity.}
9	Filtering items by exposure signal and then fitting IRT is not circular: $\tau$ measures $\theta$-dosage rank correlation, not $\gamma$ significance, and the oracle ablation confirms that even perfect binary labels do not produce a significant pooled $\gamma$.
10	
11	\paragraph{Implications and future work.}
12	Min-K\%++ should not be trusted at the 0.5B scale. The negligible aggregate effect under SFT injection does not preclude larger effects under pretraining contamination \citep{schaeffer2026causally}; scali
…[truncated 90 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-18T01:31:12.435431+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-18T01:31:12.737045+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	We identify nine limitations that bound the scope of our conclusions.
5	
6	\paragraph{Scale ceiling.}
7	All experiments use models at or below 3B parameters. Larger models (7B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.
8	
9	\paragraph{Signal coverage.}
10	S1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination below 1.5B (\S\ref{sec:signal_failure}).
11	
12	\paragraph{Ensemble size and per-domain power.}
13	Reliable $\gamma$ recovery requires $J \geq 50$. Our domain-level analysis ($J = 13$) yields a strong directional signal (posterior $P(\gamma<0) > 99\%$) for only one of eight MMLU domains. Per-domain $\gamma$ diagnosis at current ensemble sizes is exploratory.
14	
15	\paragraph{Position bias.}
16	Qwen2.5-0.5B exhibits position bias correlated with dosage (A-option rate: 46\% at d000 to 98\% at d100), necessitating exclusion from MC IRT analyses and reducing ensemble size.
17	
18	\paragraph{Credible interval coverage.}
19	CI coverage is benchmark-dependent (\S\ref{sec:calibration_results}), computed on 18 checkpoints for MMLU and 20 for ARC. The model does not provide uniformly calibrated uncertainty across benchmarks.
20	
21	\paragraph{Model misfit in non-STEM domains.}
22	A single linear $\gamma$ cannot capture non-monotone contamination effects within a domain. Richer specifications may be required.
23	
24	\paragraph{SFT ecological validity.}
25	We use LoRA-based SFT injection exclusively. Pretraining-stage leakage, which occurs during large-scale web crawl ingestion, may produce qualitatively different contamination signatures: distributed exposure across many training steps rather than concentrated fine-tuning. The position bias observed at 0.5B (A-option rate escalating from 46\% t
…[truncated 1091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-18T01:31:12.737497+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-18T01:31:12.838304+00:00_

1	\appendix
2	
3	\section{4PL Extension}
4	\label{sec:4pl_details}
5	
6	For MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:
7	\begin{equation}
8	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
9	\end{equation}
10	with $c_i \sim \text{Beta}(5,20)$ and $d_i \sim \text{Beta}(20,5)$. This requires $J \geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\gamma$ at $J=13$; pooled calibration uses $J=16$.
11	
12	\section{Model Exclusion Details}
13	\label{sec:exclusion_details}
14	
15	Of the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\alpha=32$, lr$=5\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.
16	
17	\paragraph{Model sets across analyses.}
18	Table~\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\S\ref{sec:injection}). Core findings ($\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.
19	
20	\begin{table}[h]
21	\centering
22	\caption{Model set composition across analyses.}
23	\label{tab:model_sets}
24	\footnotesize
25	\begin{tabular}{lcll}
26	\toprule
27	Analysis & $J$ & Model Set & Section \\
28	\midrule
29	Pooled baselines & 16 & 8$\times$Qwen-1.5B + 8$\times$Qwen-3B & \S\ref{sec:calibration_results} \\
30	Domain $\gamma$ & 13 & 8$\times$Qwen-1.5B + 5$\times$Qwen-3B & \S\ref{sec:domain_differential} \\
31	Cross-family & 16--
…[truncated 7143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-18T01:31:18.669046+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-18T01:31:18.821528+00:00_

1	\section*{Ethics Statement}
2	
3	All experiments use publicly available, open-weight language models (Qwen2.5 and Llama-3.2) under their respective licenses. Contamination injection is performed via standard supervised fine-tuning on existing public benchmark items; no new data collection involving human subjects is conducted. All evaluation benchmarks (MMLU, ARC-Challenge, GSM8K) are publicly released datasets. This work does not involve private user data, personally identifiable information, or human annotation.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-18T01:34:17.717527+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 5 审稿报告 — Reviewer 1（方法严谨性 + 实验有效性）\n\n**论文**: \"Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 方法框架合理且报告诚实，但核心 null finding 受限于 SFT 生态效度、additive γ 可能 misspecified、唯一 significant domain finding 未经多重比较校正，实际贡献度有限。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 方法论总体合理但存在关键假设未验证（additive linear γ vs oracle null）、多重比较缺失、ARC model fit 不合格仍报告结果 |\n| Excitement | 2.5/5 | 问题本身有价值（bridging detection and calibration），但 null finding + 严格限定条件（SFT ≤3B）大幅降低实际影响力 |\n| Reproducibility | 4/5 | 实验细节充分，模型配置、超参、排除逻辑均有说明；Stan 代码未提及是否开源 |\n| Confidence | 4/5 | 我对 IRT、贝叶斯推断、LLM 评估文献熟悉，对本文方法和统计分析有信心评估 |\n\n---\n\n## Summary\n\n本文提出 ContamCal，一个两阶段框架：Stage 1 用 RRF 融合多个检测信号生成连续 exposure score，Stage 2 将其嵌入 2PL+γ IRT 模型进行校准。在 Qwen2.5 (0.5B-3B) 的 SFT injection 实验中发现：(1) 聚合 contamination 效应仅~0.6-0.7pp，raw accuracy 已是最优估计；(2) Min-K%++ 在 0.5B 出现方向反转；(3) domain-level γ 在 Social Sciences 显示 P(γ<0)=99.1% 的方向信号。论文对 null finding 的报告坦诚透明，identifiability simulation 和 prior sensitivity analysis 增加了方法论价值。\n\n---\n\n## 主要优势\n\n1. **问题定位精准**: 将 detection 和 calibration 两条独立文献桥接，填补了 \"检测后怎么办\" 的空白（§1, Related Work §2）。\n2. **Null finding 的负责任报告**: 不过度渲染方法有效性，坦承 raw accuracy 优于所有校正方法（Table 3），并解释 why（效应太小，校正 overshoot）。\n3. **Identifiability simulation 有方法论价值**: J≥50 at AUC≥0.55 的边界条件为社区提供了 IRT-based contamination 研究的操作指南（Figure 2, §4.3）。\n4. **RRF vs S1-only ablation 信息量大**: 揭示了 exposure variance compression 导致 IRT convergence failure 的机制（§4.1），不仅是方法设计决策的 justification，也是对 IRT 应用的实践洞察。\n5. **Prior sensitivity analysis 区分了 prior-dominated vs data-dominated 结论**: Pooled γ 随 prior 变化 2.6×，Social Sciences 仅变化 1.2×（Appendix C, Table 6），方法论上严谨。\n6. **写作质量高**: 逻辑清晰、主线统一、limitations 部分诚实（9条），讨论部分直面 \"why not raw accuracy\" 的核心质疑。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Oracle ablation 无法区分 genuine null 与 model misspecification，但结论未充分限定\n\n- 具体位置：§4.1 Oracle ablation paragraph, §6 Limitations \"Additive γ linearity\"\n- 问题：Oracle ablation（ground-truth binary labels, AUC=1.0）产出 γ=-0.012 (CI [-0.145, 0.119])，论文提出两种解释：(a) 真实效应接近零，(b) additive linear γ 是 misspecified。但论文在 Abstract、Introduction contribution list、Conclusion 中将 \"aggregate contamination effects are negligible\" 作为核心发现，未在这些位置同等强调 misspecification 可能性。如果 γ 是 misspecified（例如 threshold-like effect），则 \"0.6-0.7pp\" 这个数字本身可能就是 model artifact，不能作为 \"不需要校准\" 的证据。\n- 为什么影响接收：这是论文的核心 claim（Contribution 1），如果两种解释不能区分，claim 的可信度被根本性削弱。\n- 建议修改方向：(1) 在 Abstract/Introduction 中明确写 \"under the additive linear specification\" 或 \"assuming linear contamination effects\"；(2) 提供 non-linear specification（如 threshold model 或 piecewise linear）的 oracle 结果作为对比；如果不可行，至少将 misspecification caveat 提升到 Conclusion 的显著位置而非仅在 Limitations 中提及。\n\n**N2** [critical] Social Sciences γ=-0.57 未经多重比较校正\n\n- 具体位置：§4.4 Table 4, §4.1 \"Diagnostic value of γ\" paragraph\n- 问题：8 个 MMLU domain 独立检验，仅 Social Sciences 达到 P(γ<0)=99.1%。按 Bonferroni 校正（α=0.05/8=0.00625），阈值为 P(γ<0)≥99.375%，Social Sciences 不通过。按 Holm-Bonferroni 或 FDR 控制结果类似。论文完全没有讨论多重比较问题。\n- 为什么影响接收：这是论文 Contribution 3 的核心证据。如果校正后不显著，论文的三个贡献中有两个是纯 null finding（Contribution 1 和 3），大幅降低 novelty。\n- 建议修改方向：(1) 报告 Bonferroni/FDR-adjusted p-values；(2) 如果校正后不显著，将 Social Sciences finding 明确降级为 \"suggestive pattern requiring replication\"（目前措辞已接近但不够明确）；(3) 考虑用 hierarchical prior (partial pooling across domains) 替代独立 domain fitting 来自然控制 shrinkage。\n\n**N3** [critical] ARC PPP<0.05 下的 ARC 结果呈现方式\n\n- 具体位置：Table 3 caption (\"PPP=0.003; IRT-derived ARC estimates should be interpreted with caution\"), §4.4 (\"ARC-Challenge model fit is marginal across all tested configurations (PPP < 0.05 at J=8, 13, and 16)\")\n- 问题：PPP=0.003 表明 2PL+γ 模型对 ARC 数据的 fit 不可接受。论文仍在 Table 3 中与 MMLU 并列报告 ARC 的 MAE 和 τ，给读者留下两者同等可靠的印象。Caption 中的 caveat 很容易被忽略。更严重的是，§4.4 确认 ARC 在所有 J 配置下 PPP 都 <0.05，这意味着 2PL+γ 从结构上不适合 ARC 数据，而非样本量不足。\n- 为什么影响接收：Table 3 是论文支撑 Contribution 1（raw accuracy 最优）的核心证据。如果 ARC 列的 IRT 结果无效，则 \"calibration across benchmarks\" 的结论仅靠 MMLU 一个 benchmark 支撑。\n- 建议修改方向：(1) 将 ARC IRT 结果移入 Appendix 并标注 \"model fit unacceptable\"；(2) 或在 Table 3 中用灰色/删除线标注 ARC IRT 行；(3) 讨论 ARC 为什么 fit 差（item discrimination 分布？ceiling effect？format mismatch？）。\n\n**N4** [critical] SFT injection 生态效度限制了核心 claim 的适用范围\n\n- 具体位置：§3.1, §6 Limitations \"SFT ecological validity\", Abstract (\"Under SFT injection at ≤3B\"), Title\n- 问题：论文标题 \"Does LLM Benchmark Contamination Need Calibration?\" 暗示的是通用结论，但所有证据仅来自 LoRA SFT injection at ≤3B。真实世界 contamination 发生在 pretraining 阶段（trillion-token web crawl），机制完全不同：(a) exposure 分布在数百万 training steps 中而非集中在几百步 SFT；(b) pretraining contamination 不会引入 instruction formatting artifact；(c) pretraining 对 larger models 的效应可能更大。论文在 Limitations 中承认这一点并引用 Schaeffer et al. (2026)，但 Introduction §1 para 4 (\"Our experiments yield a surprising null result\") 和 Conclusion 的 framing 不够限定。\n- 为什么影响接收：如果 SFT injection 是一个不能代表真实 contamination 的 proxy，则整个实验装置的外部有效性存疑。审稿人会问：为什么我应该相信 SFT injection 的 null finding 能推广到 pretraining contamination？\n- 建议修改方向：(1) 标题改为更限定的版本，如 \"IRT Decomposition of SFT-Injected Benchmark Contamination\"；(2) Introduction 中显式讨论 SFT vs pretraining contamination 的已知差异，而非仅在 Limitations 中提及；(3) 如有 pretraining contamination 的间接证据（如 Schaeffer et al. 的数据），进行简要对比。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] J 值跨分析的不一致性削弱方法论连贯性\n\n- 具体位置：§3.1 (J=16/24), §4.4 (J=13), Table 5 (cross-family J=18/28/20), Appendix B Table 1\n- 问题：核心分析使用 J=13（domain-level），pooled baselines 使用 J=16，cross-family 使用 J=18-28。差异原因是 \"domain-level runs preceded completion of 3B retraining\"（§3.1）。这意味着 domain-level analysis（论文最有趣的 finding）是在不完整数据上进行的，后续的完整数据（J=16）并没有用于重新验证 domain-level 结果。\n- 建议：在 J=16 配置下重跑 domain-level γ 分析，或解释为什么没有这样做。\n\n**W2** [warning] Cross-family analysis (Llama J=4, single seed) 统计功效不足以支撑结论\n\n- 具体位置：§3.2, §4.5\n- 问题：Llama 分析仅 4 个模型（d000/d005/d025/d100 各 1 个 seed）。论文标注为 \"exploratory\" 但仍在 §4.5 得出结论：\"calibration generalizes; diagnosis does not\" 和 \"θ estimation generalizes across model families\"。从 J=4 single-seed 数据得出跨 family 泛化结论过于强烈。另外 Llama d100 MMLU 被排除（catastrophic format collapse），说明 Llama 的 SFT injection 机制与 Qwen 根本不同，进一步质疑跨 family 结论的有效性。\n- 建议：降低结论强度为 \"preliminary evidence\"，或增加 Llama 的 seed 数量。\n\n**W3** [warning] RRF 在 1.5B/3B 实际上被 S1 主导，但论文强调 \"multi-signal fusion is necessary\"\n\n- 具体位置：§4.2 Signal reliability, §4.1 RRF vs S1 ablation\n- 问题：Figure 1 显示 S1 在所有 scale/dosage 组合下 AUC>0.95，而 S2/S4 在 0.5B 近似随机、1.5B+ 仅 marginal。那么在 1.5B/3B，RRF 本质上是 S1 signal + noise from S2/S4。论文声称 \"multi-signal fusion is necessary\"（§4.1），但实际的 ablation 证据仅表明 S1-only *item selection* 导致 exposure variance compression（score band [0.749, 0.867]）。这是 item selection 的属性，不是 signal quality aggregation 的属性。RRF 的价值可能仅仅是引入了 rank-based variance，而非真正的 multi-signal information gain。\n- 建议：区分 \"RRF is necessary for exposure variance\" 与 \"RRF provides superior signal quality\"。目前的表述混淆了这两个概念。可以报告 S1 + random perturbation 是否也能达到类似的 exposure variance。\n\n**W4** [warning] Min-K%++ 方向反转的因果解释不充分\n\n- 具体位置：§4.2 \"Min-K%++ directional reversal\" paragraph\n- 问题：Cohen's d=-1.55 to -1.98 是非常大的 effect size。论文提出三个可能解释（SFT 破坏 token-level fluency、position bias confound、near-full-rank LoRA）但均未验证。如果 position bias 是真正原因（0.5B 模型 A-option rate 达 98%），那这不是 Min-K%++ 本身的 failure，而是 SFT injection 在 0.5B 产生了 catastrophic behavior 的副产品。论文已排除 0.5B from IRT analyses，但仍将 Min-K%++ reversal 作为独立 finding（Contribution 2），这可能是在描述 SFT artifact 而非 Min-K%++ 的固有缺陷。\n- 建议：测试 Min-K%++ 在 non-SFT 0.5B models（如原始 Qwen2.5-0.5B vs 其他公开 0.5B models）上的行为，以区分 scale-dependent failure 和 SFT-specific artifact。\n\n**W5** [warning] Credible interval coverage 不均匀且解释不足\n\n- 具体位置：§4.1 \"Credible interval coverage is benchmark-dependent\"\n- 问题：MMLU 严重 over-coverage（50% CI covers 83%），ARC under-coverage（50% CI covers 45%）。论文仅说 \"reflecting differential model fit quality\" 但未深入。Over-coverage 意味着 posterior 过度 dispersed（CI 太宽），实际上不提供有意义的 uncertainty quantification。在 MMLU 上，95% CI 覆盖 100% 意味着 CI 完全无信息。\n- 建议：讨论 over-coverage 的原因（prior 太宽？model 过参数化？item response heterogeneity？）并考虑是否影响 \"ContamCal provides calibrated uncertainty\" 的 claim。\n\n---\n\n## 小问题（不影响接收）\n\n1. §2 Method Eq.1: RRF normalization 是 per-model min-max，这意味着不同 model 之间的 $e_{ij}$ 不可比较。但 IRT 将不同 model 的 response 放在同一模型中，$\\gamma_k \\cdot e_{ij}$ 的 cross-model 解释需要讨论。\n2. Table 3: B1b 的 \"b\" 未解释（似乎有 B1a 但未在正文中出现）。\n3. §4.4: \"ARC-Challenge model fit is marginal across all tested configurations (PPP < 0.05 at J=8, 13, and 16)\" — 在多个 J 下都不 fit 的事实应更早引入（在 Table 3 之前），否则读者先看到 ARC 结果再被告知不可靠。\n4. Appendix B: \"three 3B checkpoints were removed: two had mismatched naming conventions\" — 这暗示 pipeline 工程问题而非有原则的排除。应更清楚地说明这些 checkpoint 是否包含有效数据。\n5. Ethics Statement 过于简短，未讨论 ContamCal 被用于不当目的（如 gaming 排行榜）的可能性。\n6. §1 \"our primary pipeline uses the remaining three signals (S = {S1, S2, S4})\" — 但 S2/S4 在大部分 scale 上 near-random，这意味着 \"primary pipeline\" 实质上接近 S1-only。\n\n---\n\n## Questions for Authors\n\n1. 是否可以在 J=16 配置下重跑 domain-level γ 分析以确认 Social Sciences finding？\n2. Oracle ablation 中，是否尝试过 non-linear specifications（如 $\\gamma \\cdot \\mathbb{1}[e_{ij} > \\tau]$ 或 piecewise linear）来区分 genuine null 和 misspecification？\n3. RRF 的 exposure variance 贡献是否可以通过 S1 + uniform noise 复现？如果可以，那 S2/S4 的实际 signal contribution 是什么？\n4. 如何回应以下质疑：SFT injection 在 ≤3B 可能根本不是 contamination 的有效 proxy（因为 SFT 修改的参数比例远大于 pretraining exposure），因此 null finding 只说明 \"SFT 不能有效制造 contamination-like score inflation\"？\n5. Stan 代码和实验数据是否计划开源？\n\n---\n\n## Overall Assessment\n\n**3.0 — Findings**\n\n论文提出了一个有价值的框架（将检测信号嵌入 IRT 进行校准），实验设计在受控条件下合理，null finding 的报告诚实透明。但存在以下根本限制：(1) SFT injection 作为 contamination proxy 的生态效度存疑，核心 null finding 可能仅反映 proxy 的局限性而非 contamination 的真实属性；(2) additive linear γ 的 oracle ablation 无法区分 genuine null 和 misspecification；(3) 唯一 significant domain finding 未经多重比较校正；(4) ARC benchmark 上 model fit 不可接受但仍与 MMLU 并列报告。这些问题使得三个贡献中有效贡献度有限：Contribution 1 受 N1/N4 限制，Contribution 3 受 N2 限制，Contribution 2（signal failure mode documentation）是 solid 但属于 empirical observation 而非方法论贡献。综合来看，论文适合 Findings track：方法框架有参考价值，null finding 对社区有信息量，但证据强度和影响力不足以支撑主会议接收。",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 5 审稿报告 — Reviewer 1（方法严谨性 + 实验有效性）\n\n**论文**: \"Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 方法框架合理且报告诚实，但核心 null finding 受限于 SFT 生态效度、additive γ 可能 misspecified、唯一 significant domain finding 未经多重比较校正，实际贡献度有限。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 方法论总体合理但存在关键假设未验证（additive linear γ vs oracle null）、多重比较缺失、ARC model fit 不合格仍报告结果 |\n| Excitement | 2.5/5 | 问题本身有价值（bridging detection and calibration），但 null finding + 严格限定条件（SFT ≤3B）大幅降低实际影响力 |\n| Reproducibility | 4/5 | 实验细节充分，模型配置、超参、排除逻辑均有说明；Stan 代码未提及是否开源 |\n| Confidence | 4/5 | 我对 IRT、贝叶斯推断、LLM 评估文献熟悉，对本文方法和统计分析有信心评估 |\n\n---\n\n## Summary\n\n本文提出 ContamCal，一个两阶段框架：Stage 1 用 RRF 融合多个检测信号生成连续 exposure score，Stage 2 将其嵌入 2PL+γ IRT 模型进行校准。在 Qwen2.5 (0.5B-3B) 的 SFT injection 实验中发现：(1) 聚合 contamination 效应仅~0.6-0.7pp，raw accuracy 已是最优估计；(2) Min-K%++ 在 0.5B 出现方向反转；(3) domain-level γ 在 Social Sciences 显示 P(γ<0)=99.1% 的方向信号。论文对 null finding 的报告坦诚透明，identifiability simulation 和 prior sensitivity analysis 增加了方法论价值。\n\n---\n\n## 主要优势\n\n1. **问题定位精准**: 将 detection 和 calibration 两条独立文献桥接，填补了 \"检测后怎么办\" 的空白（§1, Related Work §2）。\n2. **Null finding 的负责任报告**: 不过度渲染方法有效性，坦承 raw accuracy 优于所有校正方法（Table 3），并解释 why（效应太小，校正 overshoot）。\n3. **Identifiability simulation 有方法论价值**: J≥50 at AUC≥0.55 的边界条件为社区提供了 IRT-based contamination 研究的操作指南（Figure 2, §4.3）。\n4. **RRF vs S1-only ablation 信息量大**: 揭示了 exposure variance compression 导致 IRT convergence failure 的机制（§4.1），不仅是方法设计决策的 justification，也是对 IRT 应用的实践洞察。\n5. **Prior sensitivity analysis 区分了 prior-dominated vs data-dominated 结论**: Pooled γ 随 prior 变化 2.6×，Social Sciences 仅变化 1.2×（Appendix C, Table 6），方法论上严谨。\n6. **写作质量高**: 逻辑清晰、主线统一、limitations 部分诚实（9条），讨论部分直面 \"why not raw accuracy\" 的核心质疑。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Oracle ablation 无法区分 genuine null 与 model misspecification，但结论未充分限定\n\n- 具体位置：§4.1 Oracle ablation paragraph, §6 Limitations \"Additive γ linearity\"\n- 问题：Oracle ablation（ground-truth binary labels, AUC=1.0）产出 γ=-0.012 (CI [-0.145, 0.119])，论文提出两种解释：(a) 真实效应接近零，(b) additive linear γ 是 misspecified。但论文在 Abstract、Introduction contribution list、Conclusion 中将 \"aggregate contamination effects are negligible\" 作为核心发现，未在这些位置同等强调 misspecification 可能性。如果 γ 是 misspecified（例如 threshold-like effect），则 \"0.6-0.7pp\" 这个数字本身可能就是 model artifact，不能作为 \"不需要校准\" 的证据。\n- 为什么影响接收：这是论文的核心 claim（Contribution 1），如果两种解释不能区分，claim 的可信度被根本性削弱。\n- 建议修改方向：(1) 在 Abstract/Introduction 中明确写 \"under the additive linear specification\" 或 \"assuming linear contamination effects\"；(2) 提供 non-linear specification（如 threshold model 或 piecewise linear）的 oracle 结果作为对比；如果不可行，至少将 misspecification caveat 提升到 Conclusion 的显著位置而非仅在 Limitations 中提及。\n\n**N2** [critical] Social Sciences γ=-0.57 未经多重比较校正\n\n- 具体位置：§4.4 Table 4, §4.1 \"Diagnostic value of γ\" paragraph\n- 问题：8 个 MMLU domain 独立检验，仅 Social Sciences 达到 P(γ<0)=99.1%。按 Bonferroni 校正（α=0.05/8=0.00625），阈值为 P(γ<0)≥99.375%，Social Sciences 不通过。按 Holm-Bonferroni 或 FDR 控制结果类似。论文完全没有讨论多重比较问题。\n- 为什么影响接收：这是论文 Contribution 3 的核心证据。如果校正后不显著，论文的三个贡献中有两个是纯 null finding（Contribution 1 和 3），大幅降低 novelty。\n- 建议修改方向：(1) 报告 Bonferroni/FDR-adjusted p-values；(2) 如果校正后不显著，将 Social Sciences finding 明确降级为 \"suggestive pattern requiring replication\"（目前措辞已接近但不够明确）；(3) 考虑用 hierarchical prior (partial pooling across domains) 替代独立 domain fitting 来自然控制 shrinkage。\n\n**N3** [critical] ARC PPP<0.05 下的 ARC 结果呈现方式\n\n- 具体位置：Table 3 caption (\"PPP=0.003; IRT-derived ARC estimates should be interpreted with caution\"), §4.4 (\"ARC-Challenge model fit is marginal across all tested configurations (PPP < 0.05 at J=8, 13, and 16)\")\n- 问题：PPP=0.003 表明 2PL+γ 模型对 ARC 数据的 fit 不可接受。论文仍在 Table 3 中与 MMLU 并列报告 ARC 的 MAE 和 τ，给读者留下两者同等可靠的印象。Caption 中的 caveat 很容易被忽略。更严重的是，§4.4 确认 ARC 在所有 J 配置下 PPP 都 <0.05，这意味着 2PL+γ 从结构上不适合 ARC 数据，而非样本量不足。\n- 为什么影响接收：Table 3 是论文支撑 Contribution 1（raw accuracy 最优）的核心证据。如果 ARC 列的 IRT 结果无效，则 \"calibration across benchmarks\" 的结论仅靠 MMLU 一个 benchmark 支撑。\n- 建议修改方向：(1) 将 ARC IRT 结果移入 Appendix 并标注 \"model fit unacceptable\"；(2) 或在 Table 3 中用灰色/删除线标注 ARC IRT 行；(3) 讨论 ARC 为什么 fit 差（item discrimination 分布？ceiling effect？format mismatch？）。\n\n**N4** [critical] SFT injection 生态效度限制了核心 claim 的适用范围\n\n- 具体位置：§3.1, §6 Limitations \"SFT ecological validity\", Abstract (\"Under SFT injection at ≤3B\"), Title\n- 问题：论文标题 \"Does LLM Benchmark Contamination Need Calibration?\" 暗示的是通用结论，但所有证据仅来自 LoRA SFT injection at ≤3B。真实世界 contamination 发生在 pretraining 阶段（trillion-token web crawl），机制完全不同：(a) exposure 分布在数百万 training steps 中而非集中在几百步 SFT；(b) pretraining contamination 不会引入 instruction formatting artifact；(c) pretraining 对 larger models 的效应可能更大。论文在 Limitations 中承认这一点并引用 Schaeffer et al. (2026)，但 Introduction §1 para 4 (\"Our experiments yield a surprising null result\") 和 Conclusion 的 framing 不够限定。\n- 为什么影响接收：如果 SFT injection 是一个不能代表真实 contamination 的 proxy，则整个实验装置的外部有效性存疑。审稿人会问：为什么我应该相信 SFT injection 的 null finding 能推广到 pretraining contamination？\n- 建议修改方向：(1) 标题改为更限定的版本，如 \"IRT Decomposition of SFT-Injected Benchmark Contamination\"；(2) Introduction 中显式讨论 SFT vs pretraining contamination 的已知差异，而非仅在 Limitations 中提及；(3) 如有 pretraining contamination 的间接证据（如 Schaeffer et al. 的数据），进行简要对比。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] J 值跨分析的不一致性削弱方法论连贯性\n\n- 具体位置：§3.1 (J=16/24), §4.4 (J=13), Table 5 (cross-family J=18/28/20), Appendix B Table 1\n- 问题：核心分析使用 J=13（domain-level），pooled baselines 使用 J=16，cross-family 使用 J=18-28。差异原因是 \"domain-level runs preceded completion of 3B retraining\"（§3.1）。这意味着 domain-level analysis（论文最有趣的 finding）是在不完整数据上进行的，后续的完整数据（J=16）并没有用于重新验证 domain-level 结果。\n- 建议：在 J=16 配置下重跑 domain-level γ 分析，或解释为什么没有这样做。\n\n**W2** [warning] Cross-family analysis (Llama J=4, single seed) 统计功效不足以支撑结论\n\n- 具体位置：§3.2, §4.5\n- 问题：Llama 分析仅 4 个模型（d000/d005/d025/d100 各 1 个 seed）。论文标注为 \"exploratory\" 但仍在 §4.5 得出结论：\"calibration generalizes; diagnosis does not\" 和 \"θ estimation generalizes across model families\"。从 J=4 single-seed 数据得出跨 family 泛化结论过于强烈。另外 Llama d100 MMLU 被排除（catastrophic format collapse），说明 Llama 的 SFT injection 机制与 Qwen 根本不同，进一步质疑跨 family 结论的有效性。\n- 建议：降低结论强度为 \"preliminary evidence\"，或增加 Llama 的 seed 数量。\n\n**W3** [warning] RRF 在 1.5B/3B 实际上被 S1 主导，但论文强调 \"multi-signal fusion is necessary\"\n\n- 具体位置：§4.2 Signal reliability, §4.1 RRF vs S1 ablation\n- 问题：Figure 1 显示 S1 在所有 scale/dosage 组合下 AUC>0.95，而 S2/S4 在 0.5B 近似随机、1.5B+ 仅 marginal。那么在 1.5B/3B，RRF 本质上是 S1 signal + noise from S2/S4。论文声称 \"multi-signal fusion is necessary\"（§4.1），但实际的 ablation 证据仅表明 S1-only *item selection* 导致 exposure variance compression（score band [0.749, 0.867]）。这是 item selection 的属性，不是 signal quality aggregation 的属性。RRF 的价值可能仅仅是引入了 rank-based variance，而非真正的 multi-signal information gain。\n- 建议：区分 \"RRF is necessary for exposure variance\" 与 \"RRF provides superior signal quality\"。目前的表述混淆了这两个概念。可以报告 S1 + random perturbation 是否也能达到类似的 exposure variance。\n\n**W4** [warning] Min-K%++ 方向反转的因果解释不充分\n\n- 具体位置：§4.2 \"Min-K%++ directional reversal\" paragraph\n- 问题：Cohen's d=-1.55 to -1.98 是非常大的 effect size。论文提出三个可能解释（SFT 破坏 token-level fluency、position bias confound、near-full-rank LoRA）但均未验证。如果 position bias 是真正原因（0.5B 模型 A-option rate 达 98%），那这不是 Min-K%++ 本身的 failure，而是 SFT injection 在 0.5B 产生了 catastrophic behavior 的副产品。论文已排除 0.5B from IRT analyses，但仍将 Min-K%++ reversal 作为独立 finding（Contribution 2），这可能是在描述 SFT artifact 而非 Min-K%++ 的固有缺陷。\n- 建议：测试 Min-K%++ 在 non-SFT 0.5B models（如原始 Qwen2.5-0.5B vs 其他公开 0.5B models）上的行为，以区分 scale-dependent failure 和 SFT-specific artifact。\n\n**W5** [warning] Credible interval coverage 不均匀且解释不足\n\n- 具体位置：§4.1 \"Credible interval coverage is benchmark-dependent\"\n- 问题：MMLU 严重 over-coverage（50% CI covers 83%），ARC under-coverage（50% CI covers 45%）。论文仅说 \"reflecting differential model fit quality\" 但未深入。Over-coverage 意味着 posterior 过度 dispersed（CI 太宽），实际上不提供有意义的 uncertainty quantification。在 MMLU 上，95% CI 覆盖 100% 意味着 CI 完全无信息。\n- 建议：讨论 over-coverage 的原因（prior 太宽？model 过参数化？item response heterogeneity？）并考虑是否影响 \"ContamCal provides calibrated uncertainty\" 的 claim。\n\n---\n\n## 小问题（不影响接收）\n\n1. §2 Method Eq.1: RRF normalization 是 per-model min-max，这意味着不同 model 之间的 $e_{ij}$ 不可比较。但 IRT 将不同 model 的 response 放在同一模型中，$\\gamma_k \\cdot e_{ij}$ 的 cross-model 解释需要讨论。\n2. Table 3: B1b 的 \"b\" 未解释（似乎有 B1a 但未在正文中出现）。\n3. §4.4: \"ARC-Challenge model fit is marginal across all tested configurations (PPP < 0.05 at J=8, 13, and 16)\" — 在多个 J 下都不 fit 的事实应更早引入（在 Table 3 之前），否则读者先看到 ARC 结果再被告知不可靠。\n4. Appendix B: \"three 3B checkpoints were removed: two had mismatched naming conventions\" — 这暗示 pipeline 工程问题而非有原则的排除。应更清楚地说明这些 checkpoint 是否包含有效数据。\n5. Ethics Statement 过于简短，未讨论 ContamCal 被用于不当目的（如 gaming 排行榜）的可能性。\n6. §1 \"our primary pipeline uses the remaining three signals (S = {S1, S2, S4})\" — 但 S2/S4 在大部分 scale 上 near-random，这意味着 \"primary pipeline\" 实质上接近 S1-only。\n\n---\n\n## Questions for Authors\n\n1. 是否可以在 J=16 配置下重跑 domain-level γ 分析以确认 Social Sciences finding？\n2. Oracle ablation 中，是否尝试过 non-linear specifications（如 $\\gamma \\cdot \\mathbb{1}[e_{ij} > \\tau]$ 或 piecewise linear）来区分 genuine null 和 misspecification？\n3. RRF 的 exposure variance 贡献是否可以通过 S1 + uniform noise 复现？如果可以，那 S2/S4 的实际 signal contribution 是什么？\n4. 如何回应以下质疑：SFT injection 在 ≤3B 可能根本不是 contamination 的有效 proxy（因为 SFT 修改的参数比例远大于 pretraining exposure），因此 null finding 只说明 \"SFT 不能有效制造 contamination-like score inflation\"？\n5. Stan 代码和实验数据是否计划开源？\n\n---\n\n## Overall Assessment\n\n**3.0 — Findings**\n\n论文提出了一个有价值的框架（将检测信号嵌入 IRT 进行校准），实验设计在受控条件下合理，null finding 的报告诚实透明。但存在以下根本限制：(1) SFT injection 作为 contamination proxy 的生态效度存疑，核心 null finding 可能仅反映 proxy 的局限性而非 contamination 的真实属性；(2) additive linear γ 的 oracle ablation 无法区分 genuine null 和 misspecification；(3) 唯一 significant domain finding 未经多重比较校正；(4) ARC benchmark 上 model fit 不可接受但仍与 MMLU 并列报告。这些问题使得三个贡献中有效贡献度有限：Contribution 1 受 N1/N4 限制，Contribution 3 受 N2 限制，Contribution 2（signal failure mode documentation）是 solid 但属于 empirical observation 而非方法论贡献。综合来看，论文适合 Findings track：方法框架有参考价值，null finding 对社区有信息量，但证据强度和影响力不足以支撑主会议接收。",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-18T01:34:22.135851+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4418
}
```

</details>

---


### Assistant

_source line 248 · 2026-05-18T01:34:29.605190+00:00_

审稿报告已提交。

核心评价：**Overall 3.0 (Findings)**。方法框架合理、null finding 报告诚实，但四个 critical issue 限制了贡献度——(1) oracle ablation 无法区分 genuine null 与 γ misspecification 却未在核心 claim 中充分限定，(2) Social Sciences 唯一 significant finding 不过 Bonferroni 校正，(3) ARC PPP=0.003 下结果仍并列呈现，(4) SFT injection 生态效度限制了 "不需要校准" 这一核心结论的外推性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 10

## Round 10

4 recorded events


### User

_source line 249 · 2026-05-18T01:40:47.934230+00:00_

[Round 5 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿原文

请逐条回应 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿意见：

## Reviewer 2 评分
**Overall**: 3.0 (Findings)
**Soundness**: 3.5/5, **Excitement**: 2.5/5, **Reproducibility**: 4/5, **Confidence**: 4/5

## Must-Fix 问题

**N1** [critical] 页面超限：主要内容超出 8 页
- Tables 2 和 3 float 到 page 9 顶部，Discussion and Conclusion 尾部文本延续到 page 9。主要内容约 8.5-8.6 页。ACL Long paper 限制 ≤ 8 页正文（Limitations/Ethics/References/Appendix 不计）。
- 建议：将 Table 2（per-domain γ）移至 Appendix，压缩 §5.1 RRF ablation 段落，Table 3 考虑 inline 报告。

**N2** [critical] 技术新颖性有限：2PL+γ 是 standard explanatory IRT/DIF 的领域应用
- 论文自己承认 "ContamCal's γ parameter is formally an instance of explanatory DIF"。与 Han et al. EACL 2026 差异仅在 continuous vs binary exposure 和 domain-level stratification——这是 modeling detail 变体。
- 建议：明确定位为 empirical investigation；与 Han et al. 做更细致对比。

**N3** [critical] 叙事不一致：Framing 在 method paper 和 empirical investigation 之间摇摆
- Title 副标题暗示 method contribution；Introduction ¶1-3 建立 calibration 是核心目标的期待；但 Results 发现 raw accuracy 最好。Contributions 1-3 分属不同类型（empirical finding / engineering trick / exploratory analysis），缺乏统一主线。
- 建议：从第一段就以 empirical investigation 切入。将 ContamCal 定位为 investigative instrument 而非最终产品。

## Should-Fix 问题

**W1** Abstract 数字密度过高（~202 words, 8-9 个数值，每 ~22 词一个数字）。

**W2** 实验范围过窄（SFT injection only, ≤3B），null finding 普适性存疑。

**W3** "Diagnostic value" 叙事说服力不足——8 domains 中 1 个 significant、J=13 不足 confirmatory、family-specific 不推广。

**W4** Cross-family validation 标题 ("Cross-Family Validation") 对 J=4 single-seed 数据过强。

**W5** 与 Han et al. EACL 2026 差异化不够深入（仅一句话区分 continuous vs binary）。

**W6** -ing 分词短语结尾模式散见多处，属轻度 AI 写作痕迹。

## Missing References
1. Lord (1980) "Applications of Item Response Theory"
2. Hambleton, Swaminathan & Rogers (1991) "Fundamentals of IRT"
3. Liang et al. (2023) HELM
4. Magar & Schwartz (2022) "Data Contamination: From Memorization to Exploitation"

## 格式合规
页数 ❌（约 8.5 页），其余全部 ✅。

---

请对以上每条 N1-N3 和 W1-W6 逐一给出 [AGREE] 或 [REBUT] 回应。对 Missing References 也请给出判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-18T01:42:11.889606+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 5 交叉回应 — Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 页面超限**\n\n同意。我未做 PDF 编译验证，但从内容量判断（Results §4 包含 3 个 table + 3 个 figure + 密集文字），8.5 页的估算合理。ACL style 对正文 ≤8 页是硬限制，Tables 2/3 浮动到 page 9 即为 desk-reject 风险。R2 的压缩建议（Table 2 移入 Appendix、Table 3 inline 化）是可行方案。\n\n补充：Table 4（domain γ）是论文 Contribution 3 的核心证据，如果移入 Appendix 会削弱这一贡献的可见性。建议优先压缩 §4.1 的 RRF ablation 段落（目前约 15 行详述 S1-only failure 的技术细节，可精简为 3-4 行 + pointer to Appendix）和 §4.2 的 Min-K%++ 描述。\n\n---\n\n**[AGREE] R2-N2: 技术新颖性有限**\n\n同意。2PL+γ 确实是 explanatory IRT/DIF 的直接应用，continuous exposure 和 domain stratification 是 modeling 变体而非根本创新。论文自己在 Related Work §2 para 3 承认 \"formally an instance of explanatory DIF\"。与 Han et al. (2026) 的区别（continuous vs binary, domain-level stratification, counterfactual inference）是实现细节差异，不构成独立方法贡献。\n\n不过我与 R2 对定位建议的看法略有不同：论文已经在 Conclusion 中将 ContamCal 定位为 \"investigative instrument\"（§5: \"ContamCal's value lies in this decomposition\"），问题是 Introduction 的 framing 没有与此一致（这正是 R2-N3 指出的叙事问题）。如果从头定位为 empirical investigation + methodology negative result，技术新颖性的要求会降低，评价标准转向 empirical contribution 的力度。\n\n---\n\n**[AGREE] R2-N3: 叙事不一致**\n\n同意，且这与我在 R1-N4 中指出的标题过宽问题相关联。具体证据：\n\n- Title \"Does LLM Benchmark Contamination Need Calibration?\" — 暗示通用 question paper\n- Subtitle \"An IRT Decomposition Study\" — 暗示 empirical study\n- Introduction §1 para 3: \"No existing method bridges detection signals and a measurement-theoretic calibration framework\" — 建立了 method gap 的叙事期待\n- Introduction §1 para 4: \"We develop ContamCal to investigate this question\" — 定位为工具\n- Results §4.1: \"Raw accuracy achieves the lowest MAE\" — 工具被自己的实验证伪\n- Contributions list: 1 是 empirical null finding, 2 是 engineering observation, 3 是 exploratory analysis\n\n这三类贡献确实缺乏统一主线。一个更一致的 framing 应该是：**\"我们问 IRT 能否校准 contamination，答案是在当前条件下不需要，以下是为什么以及在什么条件下会需要\"** — 以 question-driven empirical investigation 为主线，ContamCal 作为回答这个问题的工具而非贡献本身。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Abstract 数字密度过高**\n\n同意。重新数 Abstract 中的数值/符号：0.6-0.7pp, τ=0.73, 300, τ=0.46, 2000, Δτ=0.27, γ=-0.57, 99.1%, d=-1.55, -1.98, AUC≥0.55, J≥50 — 共 12 个量化信息点。对于 ~202 words 的 abstract 来说确实过于密集，读起来像 results summary 而非 story。与 CLAUDE.md 中的论文写作规范\"Abstract 不是 Results 的缩写，最多引用 2-3 个关键数字\"形成对比。\n\n---\n\n**[AGREE] R2-W2: 实验范围过窄**\n\n同意，与我的 R1-N4 一致。SFT injection at ≤3B 是高度限定的条件，null finding 的外部有效性依赖于这一 proxy 能代表真实 contamination，但论文缺乏证据支持这一假设。\n\n---\n\n**[AGREE] R2-W3: \"Diagnostic value\" 叙事说服力不足**\n\n同意，与我的 R1-N2（多重比较）一致。8 domains 中 1 个 P(γ<0)=99.1% 未经多重比较校正，J=13 被论文自己的 simulation study 标为 exploratory（需 J≥50），family-specific 不推广。作为 Contribution 3 的支撑证据链不够强。\n\n---\n\n**[AGREE] R2-W4: Cross-family validation 标题过强**\n\n同意，与我的 R1-W2 一致。§4.5 标题 \"Cross-Family Validation\" 暗示了 confirmatory validation，但 J=4 single-seed + Llama d100 MMLU excluded = 实际可用数据仅 3 个 Llama models。建议改为 \"Cross-Family Exploratory Analysis\" 或 \"Preliminary Cross-Family Evidence\"。\n\n---\n\n**[REBUT] R2-W5: 与 Han et al. (2026) 差异化不够深入**\n\n部分不同意。Related Work §2 para 2 确实只有一句话区分（\"Neither models contamination as a continuous covariate for score calibration\"），这确实太简短。但我认为实际差异比 R2 描述的更大：\n\n1. Han et al. 使用 psychometric DIF 检验 item parameters 是否因 contamination 改变（detection-oriented），而本文使用 explanatory DIF 进行 score calibration（correction-oriented）— 这是目标的根本不同\n2. Han et al. 的 DIF 是 group-based（contaminated group vs clean group），本文是 continuous covariate — 这不仅是 modeling detail，而是允许 partial exposure 的语义区别\n3. 本文的 counterfactual inference（设 $e_{ij}=0$ 取 posterior expectation）在 Han et al. 中没有对应操作\n\n但 R2 的建议（做更细致对比）仍然合理：论文应该在 Related Work 中用 3-4 句话而非 1 句话来区分，并在 Method §2.1 中讨论为什么 continuous > binary 在 LLM contamination 场景下更合适（因为 web crawl exposure 是 graded 而非 all-or-nothing）。\n\n---\n\n**[AGREE] R2-W6: -ing 分词短语**\n\n同意这是一个存在的问题，但影响极低。学术论文中 -ing phrases 只要不过度就不是显著问题。如果只是散见（而非系统性），属于可快速修复的 minor polish。\n\n---\n\n### Missing References 评估\n\n1. **Lord (1980) \"Applications of Item Response Theory\"** — [AGREE] 应引用。论文大量使用 IRT 框架但仅引用了 Lalor et al. (2024) tutorial 和 De Boeck (2004) explanatory IRT。作为 IRT 的经典基础文献，Lord (1980) 应在 §2 Method 或 Related Work 中出现。\n\n2. **Hambleton, Swaminathan & Rogers (1991) \"Fundamentals of IRT\"** — [AGREE] 同上理由。两本 IRT 经典教科书至少应引一本作为 framework foundation。\n\n3. **Liang et al. (2023) HELM** — [AGREE] HELM 是大规模 LLM evaluation 的代表性工作，论文讨论 benchmark evaluation 但未引 HELM，是一个覆盖缺口。\n\n4. **Magar & Schwartz (2022) \"Data Contamination: From Memorization to Exploitation\"** — [AGREE] 这是 contamination 影响的早期系统研究，Related Work §2 para 1 的 detection/mitigation 综述中应包含。\n\n总结：4 条 missing reference 建议均合理，反映了论文在 (a) IRT 基础文献和 (b) contamination 早期文献上的引用不足。\n\n---\n\n### 总结\n\nR2 的 6 条 Must-Fix/Should-Fix 中，我同意 5 条，部分反驳 1 条（W5 的严重程度）。R2 对叙事一致性（N3）和页面超限（N1）的识别是我未重点覆盖的角度，补充了我的 R1 review 中关于方法论假设和统计检验的侧重。两份 review 在核心判断上高度一致：论文框架有参考价值但证据强度受限，适合 Findings track（Overall 3.0）。",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 5 交叉回应 — Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 页面超限**\n\n同意。我未做 PDF 编译验证，但从内容量判断（Results §4 包含 3 个 table + 3 个 figure + 密集文字），8.5 页的估算合理。ACL style 对正文 ≤8 页是硬限制，Tables 2/3 浮动到 page 9 即为 desk-reject 风险。R2 的压缩建议（Table 2 移入 Appendix、Table 3 inline 化）是可行方案。\n\n补充：Table 4（domain γ）是论文 Contribution 3 的核心证据，如果移入 Appendix 会削弱这一贡献的可见性。建议优先压缩 §4.1 的 RRF ablation 段落（目前约 15 行详述 S1-only failure 的技术细节，可精简为 3-4 行 + pointer to Appendix）和 §4.2 的 Min-K%++ 描述。\n\n---\n\n**[AGREE] R2-N2: 技术新颖性有限**\n\n同意。2PL+γ 确实是 explanatory IRT/DIF 的直接应用，continuous exposure 和 domain stratification 是 modeling 变体而非根本创新。论文自己在 Related Work §2 para 3 承认 \"formally an instance of explanatory DIF\"。与 Han et al. (2026) 的区别（continuous vs binary, domain-level stratification, counterfactual inference）是实现细节差异，不构成独立方法贡献。\n\n不过我与 R2 对定位建议的看法略有不同：论文已经在 Conclusion 中将 ContamCal 定位为 \"investigative instrument\"（§5: \"ContamCal's value lies in this decomposition\"），问题是 Introduction 的 framing 没有与此一致（这正是 R2-N3 指出的叙事问题）。如果从头定位为 empirical investigation + methodology negative result，技术新颖性的要求会降低，评价标准转向 empirical contribution 的力度。\n\n---\n\n**[AGREE] R2-N3: 叙事不一致**\n\n同意，且这与我在 R1-N4 中指出的标题过宽问题相关联。具体证据：\n\n- Title \"Does LLM Benchmark Contamination Need Calibration?\" — 暗示通用 question paper\n- Subtitle \"An IRT Decomposition Study\" — 暗示 empirical study\n- Introduction §1 para 3: \"No existing method bridges detection signals and a measurement-theoretic calibration framework\" — 建立了 method gap 的叙事期待\n- Introduction §1 para 4: \"We develop ContamCal to investigate this question\" — 定位为工具\n- Results §4.1: \"Raw accuracy achieves the lowest MAE\" — 工具被自己的实验证伪\n- Contributions list: 1 是 empirical null finding, 2 是 engineering observation, 3 是 exploratory analysis\n\n这三类贡献确实缺乏统一主线。一个更一致的 framing 应该是：**\"我们问 IRT 能否校准 contamination，答案是在当前条件下不需要，以下是为什么以及在什么条件下会需要\"** — 以 question-driven empirical investigation 为主线，ContamCal 作为回答这个问题的工具而非贡献本身。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Abstract 数字密度过高**\n\n同意。重新数 Abstract 中的数值/符号：0.6-0.7pp, τ=0.73, 300, τ=0.46, 2000, Δτ=0.27, γ=-0.57, 99.1%, d=-1.55, -1.98, AUC≥0.55, J≥50 — 共 12 个量化信息点。对于 ~202 words 的 abstract 来说确实过于密集，读起来像 results summary 而非 story。与 CLAUDE.md 中的论文写作规范\"Abstract 不是 Results 的缩写，最多引用 2-3 个关键数字\"形成对比。\n\n---\n\n**[AGREE] R2-W2: 实验范围过窄**\n\n同意，与我的 R1-N4 一致。SFT injection at ≤3B 是高度限定的条件，null finding 的外部有效性依赖于这一 proxy 能代表真实 contamination，但论文缺乏证据支持这一假设。\n\n---\n\n**[AGREE] R2-W3: \"Diagnostic value\" 叙事说服力不足**\n\n同意，与我的 R1-N2（多重比较）一致。8 domains 中 1 个 P(γ<0)=99.1% 未经多重比较校正，J=13 被论文自己的 simulation study 标为 exploratory（需 J≥50），family-specific 不推广。作为 Contribution 3 的支撑证据链不够强。\n\n---\n\n**[AGREE] R2-W4: Cross-family validation 标题过强**\n\n同意，与我的 R1-W2 一致。§4.5 标题 \"Cross-Family Validation\" 暗示了 confirmatory validation，但 J=4 single-seed + Llama d100 MMLU excluded = 实际可用数据仅 3 个 Llama models。建议改为 \"Cross-Family Exploratory Analysis\" 或 \"Preliminary Cross-Family Evidence\"。\n\n---\n\n**[REBUT] R2-W5: 与 Han et al. (2026) 差异化不够深入**\n\n部分不同意。Related Work §2 para 2 确实只有一句话区分（\"Neither models contamination as a continuous covariate for score calibration\"），这确实太简短。但我认为实际差异比 R2 描述的更大：\n\n1. Han et al. 使用 psychometric DIF 检验 item parameters 是否因 contamination 改变（detection-oriented），而本文使用 explanatory DIF 进行 score calibration（correction-oriented）— 这是目标的根本不同\n2. Han et al. 的 DIF 是 group-based（contaminated group vs clean group），本文是 continuous covariate — 这不仅是 modeling detail，而是允许 partial exposure 的语义区别\n3. 本文的 counterfactual inference（设 $e_{ij}=0$ 取 posterior expectation）在 Han et al. 中没有对应操作\n\n但 R2 的建议（做更细致对比）仍然合理：论文应该在 Related Work 中用 3-4 句话而非 1 句话来区分，并在 Method §2.1 中讨论为什么 continuous > binary 在 LLM contamination 场景下更合适（因为 web crawl exposure 是 graded 而非 all-or-nothing）。\n\n---\n\n**[AGREE] R2-W6: -ing 分词短语**\n\n同意这是一个存在的问题，但影响极低。学术论文中 -ing phrases 只要不过度就不是显著问题。如果只是散见（而非系统性），属于可快速修复的 minor polish。\n\n---\n\n### Missing References 评估\n\n1. **Lord (1980) \"Applications of Item Response Theory\"** — [AGREE] 应引用。论文大量使用 IRT 框架但仅引用了 Lalor et al. (2024) tutorial 和 De Boeck (2004) explanatory IRT。作为 IRT 的经典基础文献，Lord (1980) 应在 §2 Method 或 Related Work 中出现。\n\n2. **Hambleton, Swaminathan & Rogers (1991) \"Fundamentals of IRT\"** — [AGREE] 同上理由。两本 IRT 经典教科书至少应引一本作为 framework foundation。\n\n3. **Liang et al. (2023) HELM** — [AGREE] HELM 是大规模 LLM evaluation 的代表性工作，论文讨论 benchmark evaluation 但未引 HELM，是一个覆盖缺口。\n\n4. **Magar & Schwartz (2022) \"Data Contamination: From Memorization to Exploitation\"** — [AGREE] 这是 contamination 影响的早期系统研究，Related Work §2 para 1 的 detection/mitigation 综述中应包含。\n\n总结：4 条 missing reference 建议均合理，反映了论文在 (a) IRT 基础文献和 (b) contamination 早期文献上的引用不足。\n\n---\n\n### 总结\n\nR2 的 6 条 Must-Fix/Should-Fix 中，我同意 5 条，部分反驳 1 条（W5 的严重程度）。R2 对叙事一致性（N3）和页面超限（N1）的识别是我未重点覆盖的角度，补充了我的 R1 review 中关于方法论假设和统计检验的侧重。两份 review 在核心判断上高度一致：论文框架有参考价值但证据强度受限，适合 Findings track（Overall 3.0）。",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-18T01:42:15.908888+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4019
}
```

</details>

---


### Assistant

_source line 252 · 2026-05-18T01:42:22.191233+00:00_

交叉回应已提交。对 R2 的 3 条 Must-Fix 和 6 条 Should-Fix 逐条给出了判断：同意 N1（页面超限）、N2（技术新颖性有限）、N3（叙事不一致）、W1-W4、W6，部分反驳 W5（Han et al. 差异化实际比 R2 描述的更大，但同意应在论文中展开）。4 条 Missing References 均���意。两份 review 核心判断一致：Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 11

## Round 11

36 recorded events


### User

_source line 253 · 2026-05-18T04:46:06.362632+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验设计**

### 论文信息
- **标题**: "Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study"
- **论文路径**: `projects/contamcal-irt-calibration/docs/paper/main.tex`（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experimental_setup.tex, results.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）
- **References**: `projects/contamcal-irt-calibration/docs/paper/references.bib`

### Venue 要求（EMNLP 2026 via ARR May cycle）
- **Deadline**: 2026-05-25
- **页数限制**: Long paper ≤8 pages content + unlimited references; Limitations section required (不计页数); Ethics statement optional (不计页数)
- **模板**: ACL template with `[review]` option
- **匿名**: Double-blind
- **格式**: A4, 11pt
- **评分标准**: 5=Award (~top 2.5%), 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

### 你的审查重点

请重点审查以下方面：

1. **IRT 建模合理性**:
   - 2PL+γ 模型的 additive linear γ 假设是否合理？oracle ablation 结论是否站得住脚？
   - 独立 per-domain fitting vs hierarchical model 的选择是否有充分论证？
   - Bayesian inference 设置（priors, convergence criteria, chain数）是否规范？
   - PPP 作为 model fit 指标在不同 benchmark 上的表现差异（MMLU acceptable vs ARC marginal）是否有充分解释？

2. **统计分析**:
   - J=13/16 ensemble size 下的 γ 结论的 statistical power 是否充分？
   - Social Sciences P(γ<0)=99.1% 的 multiplicity correction 处理是否妥当？
   - Prior sensitivity analysis 的覆盖面和结论是否合理？
   - CI coverage analysis（MMLU over-coverage, ARC under-coverage）的 root cause 分析

3. **实验设计**:
   - Controlled SFT injection 的 ecological validity（vs pretraining contamination）
   - 0.5B exclusion 的合理性和影响
   - Cross-family analysis（Llama J=4, single seed）的 power 和结论边界
   - Model set inconsistency（J=13 vs J=16 across analyses）的影响
   - RRF filtering（300 items from 14042）的 item selection bias

4. **Identifiability analysis**:
   - Simulation study 设计（20 conditions, 10 seeds, 200 runs）是否充分？
   - J≥50 threshold 的实际可行性讨论
   - Fisher information argument 的严谨性

5. **Calibration claims**:
   - "Raw accuracy is already well-calibrated" 的 claim scope（仅 SFT injection at ≤3B）
   - MAE 比较中 raw accuracy 优于所有 correction methods 的解释力
   - 0.6-0.7pp aggregate effect 作为 "model-free observation" 的定性

请给出：Summary、Strengths（逐条）、Weaknesses（逐条，分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（含评分和置信度）、Detailed Comments。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-18T04:46:16.880760+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-18T04:46:16.931382+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-18T04:46:22.729057+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-18T04:46:23.585538+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{Does LLM Benchmark Contamination Need Calibration?\\An IRT Decomposition Study}
13	
14	\author{Anonymous}
15	
16	\begin{document}
17	\maketitle
18	
19	\begin{abstract}
20	\input{abstract}
21	\end{abstract}
22	
23	\input{introduction}
24	\input{related_work}
25	\input{method}
26	\input{experimental_setup}
27	\input{results}
28	\input{conclusion}
29	
30	\input{limitations}
31	\input{ethics}
32	
33	\bibliography{references}
34	
35	\input{appendix}
36	
37	\end{document}
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-18T04:46:23.636690+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-18T04:46:24.046870+00:00_

1	We investigate whether Item Response Theory (IRT) can separate genuine ability from contamination artifacts on Large Language Model (LLM) benchmarks. Using controlled SFT injection across Qwen2.5 (0.5B--3B) and three benchmarks (MMLU, ARC-Challenge, GSM8K) as a testbed, we find that contamination shifts aggregate accuracy by only ${\sim}$0.6--0.7 percentage points, smaller than the estimation noise of any correction method; raw accuracy is already well-calibrated. We develop ContamCal, a two-stage pipeline that combines multi-signal item filtering with a contamination-augmented IRT model (2PL+$\gamma$). Signal-guided filtering substantially improves ability-dosage rank correlation over random subsets, while single-signal selection causes IRT convergence failure. Min-K\%++ exhibits strong directional reversal at the 0.5B scale. Domain-level analysis reveals heterogeneity: Social Sciences shows a negative $\gamma$ effect with high posterior confidence (uncorrected for multiplicity), a suggestive pattern that requires replication. Simulation studies establish that reliable $\gamma$ recovery requires $J \geq 50$, well above current practice. This structural gap between available ensemble sizes and statistical requirements limits contamination diagnosis via IRT.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 410
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-18T04:46:24.199865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-18T04:46:24.652259+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection, resource allocation, and research priorities for large language models, yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. The community has responded with twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, yet a fundamental question remains unanswered: what is the actual effect size of contamination on aggregate scores? Without this measurement, every mitigation decision is made in the dark. Quantifying the real effect of contamination on scores is therefore a prerequisite for any calibration decision.
4	
5	The literature implicitly assumes that the effect is large. Mitigation papers develop elaborate countermeasures; replacement benchmarks sacrifice comparability with established evaluations; correction methods like DCR \citep{xu2025dcr} apply aggressive adjustments. Yet no study has directly measured the aggregate effect size under controlled conditions with uncertainty quantification. The absence of this measurement leaves the field unable to distinguish settings where contamination genuinely distorts rankings from those where it is detectable but practically harmless.
6	
7	Detection methods such as Min-K\%++ \citep{zhang_2024_minkpp}, ConStat \citep{dekoninck2024constat}, and Kernel Divergence Signatures \citep{choi_2025_kds} can flag contaminated items but stop at binary classification. They do not quantify how much scores are inflated or produce adjusted scores with uncertainty estimates. IRT-based evaluation frameworks \citep{polo_2024_tinybenchmarks,habba_2025_growing_pains} apply psychometric ability estimation to improve 
…[truncated 3287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-18T04:46:24.703059+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-18T04:46:25.005573+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination detection and mitigation.}
5	Membership inference for contamination detection builds on the foundations of training data extraction \citep{carlini_2021_extracting}, membership inference attacks \citep{shokri_2017_mia}, and early contamination analyses \citep{magar_2022_contamination}. Current approaches include Min-K\% \citep{shi_2023_minkprob} and Min-K\%++ \citep{zhang_2024_minkpp} (token-level surprisal), ConStat \citep{dekoninck2024constat} (accuracy gaps on paraphrased items), CDD/TED \citep{dong_2024_cdd} (completion-based probes), KDS \citep{choi_2025_kds} (kernel divergence), TS-Guessing \citep{deng_2024_tsguessing} (temporal splits), and Time Travel \citep{golchin_2024_time_travel} (guided generation probes). Concurrent with our work, \citet{tao2025detecting} propose an entropy collapse method for RL-trained models. \citet{kocyigit2025impact} show that post-training procedures (RLHF, DPO) degrade detection signal reliability; token-level methods become unreliable on instruction-tuned models. \citet{zhang_2024_gsm1k} construct GSM1K as a parallel test set to quantify GSM8K contamination: performance gaps between original and regenerated items serve as a natural experiment for contamination measurement. Recent surveys \citep{chen2025benchmarking,singh2024evaluation} systematically categorize these approaches. These methods flag contamination but do not produce adjusted scores. On the mitigation side, \citet{sun2025emperor} systematically evaluate twenty approaches and find that none reliably restores clean performance; inference-time decontamination \citep{yang2024inference} and decontamination via forgetting \citep{zhang2025forget} similarly show limited effectiveness. DCR \citep{xu2025dcr} estimates decontaminated scores via fuzzy inference but produces point estimates without uncertainty quantification or domain-level diagnosis. ContamCal consumes detection signals as inputs 
…[truncated 3302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-18T04:46:25.056238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-18T04:46:25.709689+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is twofold: (1)~estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt}. We adapt these frameworks through three structural modifications for LLM evaluation.
12	
13	\textit{Shared item pool.} A fixed item set is shared across all models and introduces residual correlations beyond scalar $\theta_j$ \citep{sanmartin_2009_irt}; we mitigate by fitting per-benchmark models.
14	\textit{Continuous exposure.} We replace binary leakage indicators with continuous scores $e_{ij} \in [0,1]$ derived from detection signals, as LLM contamination is graded rather than binary.
15	\textit{Counterfactual ability.} Training regime changes (SFT vs.\ RL) alter both representations and signal reliability; we recover clean ability via counterfactual inference (setting $e_{ij}=0$) rather than regime-specific parameters.
16	
17	\subsection{Stage 1: Multi-Signal Exposure Mapping}
18	
…[truncated 5870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-18T04:46:25.710188+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-18T04:46:39.031272+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

I found comprehensive information about ACL Rolling Review (ARR) reviewer guidelines for 2025-2026. Here are the key details:

## Reviewer Scores and Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified b
…[truncated 1392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 13321
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-18T04:46:44.709005+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-18T04:46:45.061421+00:00_

1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed using Qwen2.5 \citep{qwen2024qwen25} at three scales (0.5B, 1.5B, 3B parameters). For each scale, we fine-tune with Low-Rank Adaptation \citep[LoRA;][]{hu2022lora} ($\alpha=32$, $r=16$, lr$=5\times10^{-5}$) on a general-purpose SFT corpus into which benchmark items are injected at four dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), and d100 (100\%). Injected items are formatted as instruction-response pairs and pass a quality-control filter that removes ambiguous or malformed entries.
8	
9	Each configuration is trained with two random seeds (s42, s123) for a total of 24 models across $3 \times 4 \times 2$ conditions. This within-family design isolates contamination dosage as the primary experimental variable while controlling for architecture, tokenizer, and pretraining data.
10	
11	We exclude 0.5B models from MMLU and ARC IRT due to answer-position bias that correlates with dosage (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}). Three initial 3B checkpoints trained with inconsistent LoRA hyperparameters were retrained under the unified protocol ($\alpha=32$, lr$=5\times10^{-5}$; Appendix~\ref{sec:exclusion_details}). Our pooled calibration analysis (Table~\ref{tab:baselines}) uses $J=16$ respondents for MMLU/ARC (1.5B$\times$8 + 3B$\times$8) and $J=24$ for GSM8K (all scales retained). Domain-level $\gamma$ analysis (Table~\ref{tab:domain_gamma}, \S\ref{sec:domain_differential}) uses $J=13$ (1.5B$\times$8 + 3B$\times$5), as it preceded completion of the 3B retraining. The eight 1.5B d000 models serve as the clean reference anchor in both configurations.
12	
13	\subsection{Cross-Family Analysis}
14	\label{sec:cross_family}
15	
16	To test whether IRT calibration is robust to inclusion of new model families, we fine-tune Llama-3.2-3B \citep{grattafio
…[truncated 2412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-18T04:46:45.062192+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-18T04:46:45.566463+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Calibration Quality}
5	\label{sec:calibration_results}
6	
7	\paragraph{Item filtering improves calibration.}
8	RRF-guided item filtering substantially improves IRT calibration quality over random item subsets. On a random 2000-item MMLU subset (same $J=13$ model set), vanilla 2PL achieves $\tau = 0.46$; on the 300-item RRF-selected subset, $\tau = 0.73$ ($\Delta\tau = 0.27$, controlled for model composition). Signal-guided filtering concentrates items where contamination effects are detectable, and enables sharper ability-dosage separation. Exclusion sensitivity analysis (removing 0--50\% of top-exposure items from random 2000-item subsets, $J=13$) yields $\tau$ ranging from 0.46 to 0.60 with no monotonic trend, and $\gamma$ remains non-significant at all exclusion rates. The $\tau$ improvement is not driven by item discrimination: mean $a_i$ does not differ between RRF-selected and random subsets (Cohen's $d = 0.098$, $p > 0.05$; $r_{\text{exposure}, a_i} = -0.013$).
9	
10	\paragraph{RRF vs.\ single-signal ablation.}
11	S1-only item selection causes IRT convergence failure ($\hat{R} = 1.53$, ESS$=$7) due to exposure variance compression: top-300 S1 items concentrate in a narrow score band, which creates collinearity between $\gamma \cdot e_{ij}$ and difficulty parameters. Multi-signal RRF fusion preserves broader exposure distributions necessary for $\gamma$ identifiability. Random 300-item subsets ($J=16$, 5 seeds) yield $\tau = 0.554 \pm 0.048$, which confirms that RRF's advantage ($\tau = 0.731$, $\Delta\tau = 0.177$) reflects informative item selection, not subset size.
12	
13	\paragraph{Aggregate contamination effects are negligible.}
14	Table~\ref{tab:baselines} compares calibration on 300 RRF-filtered items ($J=16$). Raw accuracy achieves the lowest MAE (MMLU 0.006) and outperforms all correction methods including vanilla 2PL and ContamCal. This occurs because SFT-injected contamination shifts aggreg
…[truncated 13418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-18T04:46:45.566832+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-18T04:46:46.521076+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	We investigated whether IRT can separate ability from contamination artifacts on LLM benchmarks. Three results emerge: (1)~under SFT injection at $\leq$3B, aggregate contamination effects are negligible (${\sim}$0.6--0.7pp), so raw accuracy is already well-calibrated and no correction method improves upon it; (2)~Min-K\%++ exhibits directional reversal at small scales; (3)~domain-level $\gamma$ is exploratory at $J=13$ and requires $J \geq 50$ for confirmation.
4	
5	\paragraph{Diagnostic value beyond aggregate calibration.}
6	Under SFT injection at $\leq$3B, raw accuracy is the best aggregate estimator because the contamination effect is near zero (${\sim}$0.6--0.7pp). The IRT framework's value lies in \textit{explaining why} rather than improving MAE: $\gamma$ quantifies that the effect is too small to distort rankings, provides a contamination existence diagnostic at domain granularity (Social Sciences posterior $P(\gamma<0) = 99.1\%$, robust to prior specification; Appendix~\ref{sec:prior_sensitivity}), and reveals heterogeneity invisible to aggregate scoring. The framework applies directly to settings with larger effects (e.g., pretraining-phase exposure) with no methodological changes. B6-DCR's systematic overcorrection (MAE 0.108) demonstrates the practical risk of correction methods that assume large effects without measurement-theoretic grounding.
7	
8	\paragraph{Circularity.}
9	Filtering items by exposure signal and then fitting IRT is not circular: $\tau$ measures $\theta$-dosage rank correlation, not $\gamma$ significance, and the oracle ablation confirms that even perfect binary labels do not produce a significant pooled $\gamma$.
10	
11	\paragraph{Implications and future work.}
12	Min-K\%++ should not be trusted at the 0.5B scale under SFT injection. The negligible aggregate effect under SFT injection does not preclude larger effects under pretraining contamination \citep{schaeffer2026caus
…[truncated 246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-18T04:46:46.672134+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-18T04:46:46.973869+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	We identify nine limitations that bound the scope of our conclusions.
5	
6	\paragraph{Scale ceiling.}
7	All experiments use models at or below 3B parameters. Larger models (7B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.
8	
9	\paragraph{Signal coverage.}
10	S1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination below 1.5B (\S\ref{sec:signal_failure}).
11	
12	\paragraph{Ensemble size and per-domain power.}
13	Reliable $\gamma$ recovery requires $J \geq 50$. Our domain-level analysis ($J = 13$) yields a strong directional signal (posterior $P(\gamma<0) > 99\%$) for only one of eight MMLU domains. Per-domain $\gamma$ diagnosis at current ensemble sizes is exploratory.
14	
15	\paragraph{Position bias.}
16	Qwen2.5-0.5B exhibits position bias correlated with dosage (A-option rate: 46\% at d000 to 98\% at d100); these models are excluded from MC IRT analyses, which reduces ensemble size.
17	
18	\paragraph{Credible interval coverage.}
19	CI coverage is benchmark-dependent (\S\ref{sec:calibration_results}), computed on 18 checkpoints for MMLU and 20 for ARC. The model does not provide uniformly calibrated uncertainty across benchmarks.
20	
21	\paragraph{Model misfit in non-STEM domains.}
22	A single linear $\gamma$ cannot capture non-monotone contamination effects within a domain. Richer specifications may be required.
23	
24	\paragraph{SFT ecological validity.}
25	We use LoRA-based SFT injection exclusively. Pretraining-stage leakage, which occurs during large-scale web crawl ingestion, may produce qualitatively different contamination signatures: distributed exposure across many training steps rather than concentrated fine-tuning. The position bias observed at 0.5B (A-option rate escalating from 46
…[truncated 1099 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-18T04:46:47.124947+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-18T04:46:47.477394+00:00_

1	\appendix
2	
3	\section{4PL Extension}
4	\label{sec:4pl_details}
5	
6	For MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:
7	\begin{equation}
8	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
9	\end{equation}
10	with $c_i \sim \text{Beta}(5,20)$ and $d_i \sim \text{Beta}(20,5)$. This requires $J \geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\gamma$ at $J=13$; pooled calibration uses $J=16$.
11	
12	\section{Model Exclusion Details}
13	\label{sec:exclusion_details}
14	
15	Of the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\alpha=32$, lr$=5\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.
16	
17	\paragraph{Model sets across analyses.}
18	Table~\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\S\ref{sec:injection}). Core findings ($\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.
19	
20	\begin{table}[h]
21	\centering
22	\caption{Model set composition across analyses.}
23	\label{tab:model_sets}
24	\footnotesize
25	\begin{tabular}{lcll}
26	\toprule
27	Analysis & $J$ & Model Set & Section \\
28	\midrule
29	Pooled baselines & 16 & 8$\times$Qwen-1.5B + 8$\times$Qwen-3B & \S\ref{sec:calibration_results} \\
30	Domain $\gamma$ & 13 & 8$\times$Qwen-1.5B + 5$\times$Qwen-3B & \S\ref{sec:domain_differential} \\
31	Cross-family & 16--
…[truncated 9865 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-18T04:46:48.431548+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and what each score level means. Focus on soundness, excitement, overall assessment scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, descriptions, and what each score level means. Focus on soundness, excitement, overall assessment scales."
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-18T04:46:57.745511+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure; unlikely but possible to have missed something
- **3**: Pretty sure; might have missed details despite general familiarity
- **2**: Willing to defend evaluation but likely missed some details or novelty assessment
- **1**: "Not my area, or paper is very hard to understand"

## Soundness
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: "Exciting: I would mention this paper to others and/or make effort to attend"
- **3**: "Interesting: I might mention some points and/or attend if time permits"
- **2**: "Potentially Interesting: does not resonate with me, but might with others"
- **1**: "Not Exciting: does not resonate with me and wouldn't with the broader community"

## Overall Assessment
Scale: 1-5 (with half-point increments)
- **5**: Consider for Award (top 2.5% papers)
- **4**: Conference acceptance
- **3**: Findings track acceptance
- **2**: Needs substantial revisions for next submission cycle
- **1**: Do not resubmit or not relevant to computational linguistics

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9313
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-18T04:47:37.285129+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-18T04:47:37.737532+00:00_

1	\section*{Ethics Statement}
2	
3	All experiments use publicly available, open-weight language models (Qwen2.5 and Llama-3.2) under their respective licenses. Contamination injection is performed via standard supervised fine-tuning on existing public benchmark items; no new data collection involving human subjects is conducted. All evaluation benchmarks (MMLU, ARC-Challenge, GSM8K) are publicly released datasets. This work does not involve private user data, personally identifiable information, or human annotation.
4	
5	We acknowledge a dual-use risk: the contamination injection protocol we describe could be used to deliberately inflate benchmark scores. We mitigate this by focusing on detection and measurement rather than injection optimization, and by releasing detection signals rather than injection recipes. Our finding that SFT injection at $\leq$3B produces negligible aggregate effects may itself reduce the incentive for such manipulation at small scales. The measurement framework is intended to improve evaluation transparency, not to enable gaming.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-18T04:47:38.240055+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool call

_source line 283 · 2026-05-18T04:47:38.542086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 284 · 2026-05-18T04:48:24.262664+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 52, \"total_citations\": 83, \"unique_cited_keys\": 52, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 30, \"online_not_found\": 10, \"online_mismatch\": 12}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"carlini_2021_extracting\", \"type\": \"inproceedings\", \"title\": \"Extracting Training Data from Large Language Models\", \"authors\": \"Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew a...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 30th USENIX Security Symposium\"}, {\"key\": \"choi_2025_kds\", \"type\": \"inproceedings\", \"title\": \"How Contaminated Is Your Benchmark? Measuring Dataset Leakage in Large Language Models with Kernel Divergence\", \"authors\": \"Choi, Hyeong Kyu and Khanov, Maxim and Wei, Hongxin and Li, Yixuan\", \"year\": \"2025\", \"venue\": \"Proceedings of the 42nd International Conference on Machine Learning (ICML)\"}, {\"key\": \"cormack_2009_rrf\", \"type\": \"inproceedings\", \"title\": \"Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods\", \"authors\": \"Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan\", \"year\": \"2009\", \"venue\": \"Proceedings of the 32nd International ACM SIGIR Conference on Research and Devel...\"}, {\"key\": \"deboeck_2004_explanatory_irt\", \"type\": \"book\", \"title\": \"Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach\", \"authors\": \"De Boeck, Paul and Wilson, Mark\", \"year\": \"2004\", \"venue\": \"\"}, {\"key\": \"deng_2024_tsguessing\", \"type\": \"inproceedings\", \"title\": \"Investigating Data Contamination in Modern Benchmarks for Large Language Models\", \"authors\": \"Deng, Chunyuan and Zhao, Yilun and Tang, Xiangru and Gerstein, Mark and Cohan, A...\", \"year\": \"2024\", \"ve
…[truncated 41656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 46022
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-18T04:48:24.313737+00:00_

1	% ============================================================
2	% Literature Map Entries (keys from literature_map.yaml ids)
3	% ============================================================
4	
5	@inproceedings{carlini_2021_extracting,
6	  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and Lee, Katherine and Roberts, Adam and Brown, Tom and Song, Dawn and Erlingsson, Ulfar and Oprea, Alina and Raffel, Colin},
7	  title     = {Extracting Training Data from Large Language Models},
8	  booktitle = {Proceedings of the 30th USENIX Security Symposium},
9	  year      = {2021},
10	  url       = {https://arxiv.org/abs/2012.07805}
11	}
12	
13	@inproceedings{choi_2025_kds,
14	  author    = {Choi, Hyeong Kyu and Khanov, Maxim and Wei, Hongxin and Li, Yixuan},
15	  title     = {How Contaminated Is Your Benchmark? Measuring Dataset Leakage in Large Language Models with Kernel Divergence},
16	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
17	  year      = {2025},
18	  url       = {https://arxiv.org/abs/2502.00678}
19	}
20	
21	@inproceedings{cormack_2009_rrf,
22	  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},
23	  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},
24	  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},
25	  pages     = {758--759},
26	  year      = {2009},
27	  publisher = {ACM},
28	  url       = {https://dl.acm.org/doi/10.1145/1571941.1572114}
29	}
30	
31	@book{deboeck_2004_explanatory_irt,
32	  author    = {De Boeck, Paul and Wilson, Mark},
33	  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},
34	  publisher = {Springer},
35	  year      = {2004},
36	  address   = {New York},
37	  url       = {https://link.springer.com/book/10.1007/978-1-4757-3990-9}
…[truncated 23627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 45771
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-18T04:53:07.332254+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿完成\n\n**论文**: \"Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study\"\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5（Findings 水准）\n**Confidence**: 4 / 5\n**一句话总结**: 研究问题重要且 null result 有价值，但 SFT injection 的生态效度、线性 γ 潜在误设定、以及 J=13 下的 domain-level 推断与论文自身 J≥50 标准的矛盾，构成方法论层面的显著 gap。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 核心方法合理但 oracle ablation 暴露的 γ 误设定未解决；domain-level 结论的统计 power 不足；CI coverage 问题削弱了 uncertainty quantification 的贡献声明 |\n| Excitement | 3.5 / 5 | 研究问题及时、null result 有社区价值、identifiability analysis 是有用的方法论贡献；但 scope 限于 SFT ≤3B 显著降低了对实际 contamination 问题的回答力度 |\n\n---\n\n## 主要优势\n\n1. **研究问题定义精准**：直接量化 contamination 的 aggregate effect size，填补了\"检测多、度量少\"的文献空白。Introduction 的叙事线（从 effect size 缺失到 measurement model 构建）逻辑清晰。\n\n2. **诚实的 null result**：发现 raw accuracy 在 SFT injection ≤3B 条件下已经 well-calibrated（~0.6-0.7pp shift），没有过度包装成方法优越性，反而质疑了现有 correction 方法（DCR MAE=0.108 的 overcorrection 案例尤其有说服力）。\n\n3. **Identifiability analysis 提供了可操作的 boundary**：simulation study 建立了 J≥50 at AUC≥0.55 的操作阈值（Figure 2），posterior CI width 与 J^{-0.48} 的经验收敛率验证了理论预期。这为后续 IRT-based contamination 研究提供了 design guideline。\n\n4. **Min-K%++ directional reversal 的发现**：0.5B 尺度下 Cohen's d = -1.55 to -1.98 的方向反转（Section 5.2）是重要的实践警示，有独立的社区价值。\n\n5. **RRF 的 meta-circularity 论证**：用 rank-based fusion 避开 learned aggregator 需要 contamination labels 的循环问题（Section 3.2），设计合理且论证充分。\n\n6. **Limitations 章节异常详尽**：列出 9 项限制，体现了作者的自我批判能力。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **Ecological validity：SFT injection 的 null result 不能回答标题提出的问题**\n\n- 具体位置：Title、Abstract、Section 4.1、Section 6 para 1\n- 问题：标题问 \"Does LLM Benchmark Contamination Need Calibration?\"，但全部实验仅涵盖 LoRA-based SFT injection at ≤3B。Pretraining-phase contamination 是实际场景中最常见的形式，论文自身承认 \"pretraining-phase contamination, which may produce larger effects\"。SFT injection 在机制上与 pretraining leakage 有本质差异。\n- 为什么影响接收：论文的核心 claim（\"raw accuracy is already well-calibrated\"）的 scope 被标题/abstract 的 framing 大幅放大。Scope-claim gap 是主要问题。\n- 建议：修改标题限定 scope；Abstract/Introduction 中前移 scope limitation。\n\n**N2** [critical] **Oracle ablation 暴露的 γ 误设定未获充分解决**\n\n- 具体位置：Section 5.1 \"Oracle ablation\"、Limitations para 9\n- 问题：即使 AUC=1.0，pooled γ 仍 non-significant（γ=-0.012）。论文给出 effect heterogeneity 和 misspecification 两个解释，但未测试 non-linear specifications 来区分 \"no effect\" vs \"wrong model\"。\n- 为什么影响接收：如果 functional form 错误，null result 可能是模型不够灵敏的 artifact，核心 claim 的可信度依赖于此区分。\n- 建议：测试至少一个 non-linear γ specification（如 threshold model）。\n\n**N3** [critical] **J=13 domain-level 结论与 J≥50 identifiability 标准的自我矛盾**\n\n- 具体位置：Section 5.3 (J≥50)、Section 5.4 (J=13 domain γ)、Abstract、Contribution list\n- 问题：论文建立了 J≥50 标准后以 J=13 进行 domain analysis，并在 Abstract/Introduction 中将 Social Sciences P(γ<0)=99.1% 作为 key finding 展示。虽标注 \"exploratory\"，但实际呈现权重与 caution 不匹配。\n- 为什么影响接收：内部自洽性问题——不能同时声称 J≥50 是必要条件并以 J=13 的结果为核心贡献。\n- 建议：(a) 主文改用 J=16 结果；(b) 降低 domain γ 在 Abstract/Introduction 的权重。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] Multiplicity correction 处理不一致（引用 Gelman 2012 但未实施其推荐的 hierarchical model）\n**W2** [warning] Cross-family analysis (Llama J=4, single seed) 的结论边界不明确\n**W3** [warning] ARC PPP=0.003 结果仍出现在主文中\n**W4** [warning] CI coverage 异常（MMLU over-coverage 83%, ARC under-coverage 45%）未获充分诊断\n**W5** [warning] RRF filtering 的 item selection bias（300/14042, 仅报告 τ 未报告 MAE 的 random 对照）\n**W6** [warning] \"Model-free observation\" 的 confound（SFT data composition 变化 vs contamination effect 未分离）\n\n---\n\n## Questions to Authors\n\nQ1: 是否测试过 non-linear γ specifications？\nQ2: SFT training 是否收敛？Training curves 未报告。\nQ3: Hierarchical model 是否可在 camera-ready 前实现？\nQ4: S1 不可用时（无 corpus access），RRF 退化为 S2+S4 的 applicability 讨论不足。\nQ5: Within-family GSM8K 的 PPP 在哪里？\n\n---\n\n## Missing References\n\n- Xu et al. (2024) \"Benchmarking Benchmark Leakage in Large Language Models\" (arXiv 2404.18824)\n- Li et al. (2024) \"Task Contamination: Language Models May Not Be Few-Shot Anymore\" (AAAI 2024)\n\n---\n\n审稿完毕，请 Director 审阅。",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿完成\n\n**论文**: \"Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study\"\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5（Findings 水准）\n**Confidence**: 4 / 5\n**一句话总结**: 研究问题重要且 null result 有价值，但 SFT injection 的生态效度、线性 γ 潜在误设定、以及 J=13 下的 domain-level 推断与论文自身 J≥50 标准的矛盾，构成方法论层面的显著 gap。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 核心方法合理但 oracle ablation 暴露的 γ 误设定未解决；domain-level 结论的统计 power 不足；CI coverage 问题削弱了 uncertainty quantification 的贡献声明 |\n| Excitement | 3.5 / 5 | 研究问题及时、null result 有社区价值、identifiability analysis 是有用的方法论贡献；但 scope 限于 SFT ≤3B 显著降低了对实际 contamination 问题的回答力度 |\n\n---\n\n## 主要优势\n\n1. **研究问题定义精准**：直接量化 contamination 的 aggregate effect size，填补了\"检测多、度量少\"的文献空白。Introduction 的叙事线（从 effect size 缺失到 measurement model 构建）逻辑清晰。\n\n2. **诚实的 null result**：发现 raw accuracy 在 SFT injection ≤3B 条件下已经 well-calibrated（~0.6-0.7pp shift），没有过度包装成方法优越性，反而质疑了现有 correction 方法（DCR MAE=0.108 的 overcorrection 案例尤其有说服力）。\n\n3. **Identifiability analysis 提供了可操作的 boundary**：simulation study 建立了 J≥50 at AUC≥0.55 的操作阈值（Figure 2），posterior CI width 与 J^{-0.48} 的经验收敛率验证了理论预期。这为后续 IRT-based contamination 研究提供了 design guideline。\n\n4. **Min-K%++ directional reversal 的发现**：0.5B 尺度下 Cohen's d = -1.55 to -1.98 的方向反转（Section 5.2）是重要的实践警示，有独立的社区价值。\n\n5. **RRF 的 meta-circularity 论证**：用 rank-based fusion 避开 learned aggregator 需要 contamination labels 的循环问题（Section 3.2），设计合理且论证充分。\n\n6. **Limitations 章节异常详尽**：列出 9 项限制，体现了作者的自我批判能力。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **Ecological validity：SFT injection 的 null result 不能回答标题提出的问题**\n\n- 具体位置：Title、Abstract、Section 4.1、Section 6 para 1\n- 问题：标题问 \"Does LLM Benchmark Contamination Need Calibration?\"，但全部实验仅涵盖 LoRA-based SFT injection at ≤3B。Pretraining-phase contamination 是实际场景中最常见的形式，论文自身承认 \"pretraining-phase contamination, which may produce larger effects\"。SFT injection 在机制上与 pretraining leakage 有本质差异。\n- 为什么影响接收：论文的核心 claim（\"raw accuracy is already well-calibrated\"）的 scope 被标题/abstract 的 framing 大幅放大。Scope-claim gap 是主要问题。\n- 建议：修改标题限定 scope；Abstract/Introduction 中前移 scope limitation。\n\n**N2** [critical] **Oracle ablation 暴露的 γ 误设定未获充分解决**\n\n- 具体位置：Section 5.1 \"Oracle ablation\"、Limitations para 9\n- 问题：即使 AUC=1.0，pooled γ 仍 non-significant（γ=-0.012）。论文给出 effect heterogeneity 和 misspecification 两个解释，但未测试 non-linear specifications 来区分 \"no effect\" vs \"wrong model\"。\n- 为什么影响接收：如果 functional form 错误，null result 可能是模型不够灵敏的 artifact，核心 claim 的可信度依赖于此区分。\n- 建议：测试至少一个 non-linear γ specification（如 threshold model）。\n\n**N3** [critical] **J=13 domain-level 结论与 J≥50 identifiability 标准的自我矛盾**\n\n- 具体位置：Section 5.3 (J≥50)、Section 5.4 (J=13 domain γ)、Abstract、Contribution list\n- 问题：论文建立了 J≥50 标准后以 J=13 进行 domain analysis，并在 Abstract/Introduction 中将 Social Sciences P(γ<0)=99.1% 作为 key finding 展示。虽标注 \"exploratory\"，但实际呈现权重与 caution 不匹配。\n- 为什么影响接收：内部自洽性问题——不能同时声称 J≥50 是必要条件并以 J=13 的结果为核心贡献。\n- 建议：(a) 主文改用 J=16 结果；(b) 降低 domain γ 在 Abstract/Introduction 的权重。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] Multiplicity correction 处理不一致（引用 Gelman 2012 但未实施其推荐的 hierarchical model）\n**W2** [warning] Cross-family analysis (Llama J=4, single seed) 的结论边界不明确\n**W3** [warning] ARC PPP=0.003 结果仍出现在主文中\n**W4** [warning] CI coverage 异常（MMLU over-coverage 83%, ARC under-coverage 45%）未获充分诊断\n**W5** [warning] RRF filtering 的 item selection bias（300/14042, 仅报告 τ 未报告 MAE 的 random 对照）\n**W6** [warning] \"Model-free observation\" 的 confound（SFT data composition 变化 vs contamination effect 未分离）\n\n---\n\n## Questions to Authors\n\nQ1: 是否测试过 non-linear γ specifications？\nQ2: SFT training 是否收敛？Training curves 未报告。\nQ3: Hierarchical model 是否可在 camera-ready 前实现？\nQ4: S1 不可用时（无 corpus access），RRF 退化为 S2+S4 的 applicability 讨论不足。\nQ5: Within-family GSM8K 的 PPP 在哪里？\n\n---\n\n## Missing References\n\n- Xu et al. (2024) \"Benchmarking Benchmark Leakage in Large Language Models\" (arXiv 2404.18824)\n- Li et al. (2024) \"Task Contamination: Language Models May Not Be Few-Shot Anymore\" (AAAI 2024)\n\n---\n\n审稿完毕，请 Director 审阅。",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-18T04:53:11.656083+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4323
}
```

</details>

---


### Assistant

_source line 288 · 2026-05-18T04:53:20.502003+00:00_

审稿意见已提交给 Review Director。

总结：评分 **3.0/5 (Findings)**。三个 critical issues：(1) SFT injection 的生态效度不足以支撑标题暗示的 scope；(2) oracle ablation 暴露的 linear γ 误设定问题未解决，无法区分 "no effect" 和 "wrong model"；(3) J=13 domain-level 推断与论文自身建立的 J≥50 标准自相矛盾。六个 should-fix 问题涉及 multiplicity correction、cross-family power、ARC model misfit、CI coverage、RRF selection bias、以及 data composition confound。论文的优势在于问题定义精准、null result 诚实、identifiability analysis 有方法论价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 12

## Round 12

10 recorded events


### User

_source line 289 · 2026-05-18T04:53:53.870765+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整 Round 1 审稿意见。请对每个 Must-Fix 和 Should-Fix 逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

### Reviewer 2 的 Must-Fix 问题

**R2-N1** [critical] 技术新颖性不足：2PL+γ 是标准 explanatory IRT/DIF 的直接应用
- 论文在 Related Work (Section 2, para 3) 中已承认 γ 参数 "is formally an instance of explanatory DIF"
- 三项声称的改编（continuous exposure、domain-level stratification、counterfactual inference）均为标准做法
- RRF fusion (Eq.1) 是 IR 标准技术
- 建议：更明确定位为 empirical study；突出 identifiability analysis 作为独立贡献

**R2-N2** [critical] Null finding 范围过窄（SFT ≤3B），标题暗示一般性结论
- 论文回答的实际问题是 "Does SFT-injected contamination at ≤3B need calibration?"
- SFT 是粗糙模拟，小模型上效果本身可能很弱
- 对 practitioner 最关心的 pretraining contamination 无直接适用性
- 建议：标题限定 scope；增加 7B+ pilot；或深入论证 SFT 作为 contamination proxy 的生态效度

**R2-N3** [critical] Oracle ablation 暴露根本性模型规格问题
- AUC=1.0 时 pooled γ 仍 non-significant
- 两种解释（heterogeneity vs misspecification）含义截然不同
- 如果模型在 oracle 条件下都无法检测效应，ContamCal 在何种意义上有用？
- 建议：在 simulation 中测试 threshold model 下 linear γ 的 recovery behavior

### Reviewer 2 的 Should-Fix 问题

**R2-W1** Han et al. (EACL 2026) 差异化不充分——calibration focus 作为差异化 claim 是 self-undermining 的
**R2-W2** Diagnostic value claim 证据单薄——仅 1/8 domain 显著，未过 Bonferroni
**R2-W3** Contribution 2（signal filtering + Min-K%++ reversal）与 question-driven framing 不一致
**R2-W4** k 索引重载（benchmark → stratum）造成符号混乱
**R2-W5** J 值频繁切换（13/16/18/20/24/28），叙事连贯性受损

### Reviewer 2 的 Minor 问题

- M1: "Additionally" 过渡词
- M2: Abstract 数字密度偏高（~6+ 定量结论）
- M3: Appendix Table 5 vs 正文 J 值不一致
- M4: S4 (Self-Critique) 计算细节不足
- M5: Appendix E (ARC, J=8, S1-only) 可比性有限
- M6: 页数接近上限需自查

### Reviewer 2 的 Missing References
1. Camilli & Shepard (1994) — DIF 方法论经典
2. Swaminathan & Rogers (1990) — logistic regression DIF with continuous covariates
3. Roberts et al. (2025) or similar — IRT identifiability with small J

---

请逐条给出 [AGREE] 或 [REBUT]，附理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-18T04:54:22.474453+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex",
  "offset": "6",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex",
    "offset": "6",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-18T04:54:22.927106+00:00_

6	
7	\paragraph{IRT for LLM evaluation.}
8	Item Response Theory \citep{lord_1980_irt,hambleton_1991_irt} has gained traction as a principled alternative to raw accuracy in holistic evaluation frameworks \citep{liang_2023_helm}. \citet{lalor_2024_irt_nlp} provide a comprehensive IRT tutorial for NLP; TinyBenchmarks \citep{polo_2024_tinybenchmarks} uses IRT-informed item filtering for efficient evaluation; Growing Pains \citep{habba_2025_growing_pains} validates IRT at scale on 400+ models and identifies low-respondent limitations; HiBayES \citep{luettgau_2025_hibayes} adds hierarchical Bayesian inference for credible intervals; ATLAS \citep{li_2024_atlas} applies IRT for adaptive testing. Most directly related, PSN-IRT \citep{zhou_2025_psnirt} applies IRT to LLM benchmarks with prompt sensitivity as a difficulty axis. \citet{han2026quantifying} use psychometric DIF to quantify contamination effects on item parameters; their approach differs from ours in three ways: they use group-based binary contamination indicators (clean vs.\ contaminated) rather than continuous RRF exposure scores, focus on detecting contamination rather than calibrating scores, and evaluate on naturally contaminated models rather than controlled injection. Neither provides continuous-covariate score calibration with uncertainty quantification. ContamCal differs by introducing contamination covariates $\gamma_k$ that explicitly capture how exposure shifts item difficulty; this enables both calibration and per-domain contamination diagnosis.
9	
10	\paragraph{Differential item functioning and explanatory IRT.}
11	ContamCal's $\gamma$ parameter is formally an instance of explanatory DIF \citep{holland_1993_dif,thissen1993dif}: it models how an item-level covariate (contamination exposure) differentially affects response probability across items. In educational measurement, DIF detects unfairness when items function differently across demographic groups \citep{zumbo1999dif}; in our setting, the ``gro
…[truncated 1195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-18T04:54:23.429365+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex",
  "offset": "8",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex",
    "offset": "8",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-18T04:54:23.881957+00:00_

8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is twofold: (1)~estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt}. We adapt these frameworks through three structural modifications for LLM evaluation.
12	
13	\textit{Shared item pool.} A fixed item set is shared across all models and introduces residual correlations beyond scalar $\theta_j$ \citep{sanmartin_2009_irt}; we mitigate by fitting per-benchmark models.
14	\textit{Continuous exposure.} We replace binary leakage indicators with continuous scores $e_{ij} \in [0,1]$ derived from detection signals, as LLM contamination is graded rather than binary.
15	\textit{Counterfactual ability.} Training regime changes (SFT vs.\ RL) alter both representations and signal reliability; we recover clean ability via counterfactual inference (setting $e_{ij}=0$) rather than regime-specific parameters.
16	
17	\subsection{Stage 1: Multi-Signal Exposure Mapping}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-18T04:54:23.932643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex",
  "offset": "11",
  "limit": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex",
    "offset": "11",
    "limit": "6"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-18T04:54:23.983183+00:00_

11	Our contributions are as follows:
12	\begin{enumerate}
13	    \item \textbf{Null finding with identifiability analysis.} Under SFT injection at $\leq$3B, contamination shifts aggregate accuracy by only ${\sim}$0.6--0.7pp, smaller than the estimation noise of any correction method. Simulation studies establish that reliable $\gamma$ recovery requires $J \geq 50$ at signal AUC $\geq 0.55$, well above current LLM evaluation practice ($J = 8$--$30$). These thresholds delineate when contamination-augmented IRT transitions from exploratory to confirmatory.
14	    \item \textbf{Signal-guided filtering and failure modes.} RRF-guided item filtering improves IRT calibration over random subsets ($\Delta\tau = 0.18$ vs.\ size-matched random, $0.27$ vs.\ full 2000-item random). Single-signal item selection causes IRT convergence failure due to exposure variance compression, which establishes multi-signal fusion as a necessary condition for $\gamma$ identifiability. We document a directional reversal in Min-K\%++ at the 0.5B scale (Cohen's $d = -1.55$ to $-1.98$), where the signal is actively misleading rather than merely ineffective.
15	\end{enumerate}
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-18T04:56:23.423963+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — 对 Reviewer 2 Round 1 意见的交叉回应\n\n---\n\n### Must-Fix 回应\n\n**[AGREE] R2-N1: 技术新颖性不足**\n同意。论文在 Section 2 para 3 已承认 γ \"is formally an instance of explanatory DIF\"。三项 adaptation（continuous exposure、domain stratification、counterfactual inference）均为 psychometrics/explanatory IRT 的标准做法。RRF 是 IR 成熟技术。建议重定位为 empirical measurement study + identifiability boundary analysis，后者（J≥50 threshold, Figure 2）是真正有独立方法论贡献的部分。\n\n**[AGREE] R2-N2: Null finding 范围过窄**\n完全同意，与我的 R1-N1 一致。补充两点：(1) LoRA SFT (α=32, r=16) 是 parameter-efficient lightweight fine-tuning，与 pretraining contamination 的 full-parameter optimization 在 representation-level 影响不可比；(2) ≤3B 模型 baseline accuracy 偏低（MMLU ~0.55-0.65），model capacity for memorization 可能不足以产生 aggregate effect，7B+ 模型可能有 qualitatively different 结果。\n\n**[AGREE] R2-N3: Oracle ablation 暴露模型规格问题**\n完全同意，与我的 R1-N2 一致。R2 建议在 simulation 中测试 threshold ground-truth 下 linear γ 的 recovery，比我的建议更精确。这个实验仅需修改 simulation code（现有 20 conditions × 10 seeds 框架），成本很低，但能明确区分 \"no effect\" vs \"wrong model\"。论文当前的叙事顺序（先列 heterogeneity 再 \"alternatively\" misspecification）可能误导读者。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R2-W1**: Han et al. 差异化中 \"calibration focus\" 在 null result 下 self-undermining。建议改为 controlled testbed + identifiability analysis + signal failure characterization 作为差异化维度。\n\n**[AGREE] R2-W2**: Diagnostic value 证据单薄。1/8 domain 勉强显著（J=13 未过 Bonferroni, J=16 刚过），7/8 domains P(γ<0) 在 7.8%-44.1% 范围，不足以支撑 diagnostic capability 的 claim。\n\n**[REBUT] R2-W3**: 部分不同意。Signal filtering 是 IRT pipeline 的 necessary condition（S1-only 导致 convergence failure, Section 5.1），不报告则读者无法理解 pipeline 为何需要 Stage 1。Min-K%++ reversal (d=-1.55 to -1.98) 有独立实用价值。但同意 Contribution list 的并列呈现权重过强，应调整 framing 为 \"pipeline prerequisite + side finding\"。\n\n**[AGREE] R2-W4**: k 索引重载。与我的 R1-M1 一致。\n\n**[AGREE] R2-W5**: J 值频繁切换（7 个不同 J 值）。与我对 model set inconsistency 的 concern 一致。核心问题是 J=13 vs J=16 交替出现，应统一使用 J=16。\n\n---\n\n### Minor 全部 [AGREE]\n\nM1-M6 均合理。特别同意 M4（S4 Self-Critique 计算细节不足影响 reproducibility）和 M2（Abstract 数字密度过高）。\n\n### Missing References 全部 [AGREE]\n\nCamilli & Shepard (1994)、Swaminathan & Rogers (1990) 是 DIF 领域应引用的经典。\n\n---\n\n### 两位 Reviewer 的一致性总结\n\nR1 和 R2 在以下核心问题上完全一致：\n1. **Scope-claim gap**（SFT ≤3B vs 标题的一般性）— R1-N1 ≈ R2-N2\n2. **Oracle ablation / γ misspecification** — R1-N2 ≈ R2-N3\n3. **Domain-level 统计力不足** — R1-N3 ≈ R2-W2（R1 标为 Must-Fix, R2 标为 Should-Fix）\n4. **J 值不一致** — R1 model set inconsistency ≈ R2-W5\n\n唯一实质分歧：R2-W3（Contribution 2 与 framing 不一致），我部分 rebut——signal filtering 是 pipeline 必要组成，但同意 framing 需调整。\n\nR2 额外提出的重要点（R1 未充分覆盖）：R2-N1 的技术新颖性不足，我完全同意且认为应列为 Must-Fix 级别。建议论文明确定位为 empirical study 而非 method paper。",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — 对 Reviewer 2 Round 1 意见的交叉回应\n\n---\n\n### Must-Fix 回应\n\n**[AGREE] R2-N1: 技术新颖性不足**\n同意。论文在 Section 2 para 3 已承认 γ \"is formally an instance of explanatory DIF\"。三项 adaptation（continuous exposure、domain stratification、counterfactual inference）均为 psychometrics/explanatory IRT 的标准做法。RRF 是 IR 成熟技术。建议重定位为 empirical measurement study + identifiability boundary analysis，后者（J≥50 threshold, Figure 2）是真正有独立方法论贡献的部分。\n\n**[AGREE] R2-N2: Null finding 范围过窄**\n完全同意，与我的 R1-N1 一致。补充两点：(1) LoRA SFT (α=32, r=16) 是 parameter-efficient lightweight fine-tuning，与 pretraining contamination 的 full-parameter optimization 在 representation-level 影响不可比；(2) ≤3B 模型 baseline accuracy 偏低（MMLU ~0.55-0.65），model capacity for memorization 可能不足以产生 aggregate effect，7B+ 模型可能有 qualitatively different 结果。\n\n**[AGREE] R2-N3: Oracle ablation 暴露模型规格问题**\n完全同意，与我的 R1-N2 一致。R2 建议在 simulation 中测试 threshold ground-truth 下 linear γ 的 recovery，比我的建议更精确。这个实验仅需修改 simulation code（现有 20 conditions × 10 seeds 框架），成本很低，但能明确区分 \"no effect\" vs \"wrong model\"。论文当前的叙事顺序（先列 heterogeneity 再 \"alternatively\" misspecification）可能误导读者。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R2-W1**: Han et al. 差异化中 \"calibration focus\" 在 null result 下 self-undermining。建议改为 controlled testbed + identifiability analysis + signal failure characterization 作为差异化维度。\n\n**[AGREE] R2-W2**: Diagnostic value 证据单薄。1/8 domain 勉强显著（J=13 未过 Bonferroni, J=16 刚过），7/8 domains P(γ<0) 在 7.8%-44.1% 范围，不足以支撑 diagnostic capability 的 claim。\n\n**[REBUT] R2-W3**: 部分不同意。Signal filtering 是 IRT pipeline 的 necessary condition（S1-only 导致 convergence failure, Section 5.1），不报告则读者无法理解 pipeline 为何需要 Stage 1。Min-K%++ reversal (d=-1.55 to -1.98) 有独立实用价值。但同意 Contribution list 的并列呈现权重过强，应调整 framing 为 \"pipeline prerequisite + side finding\"。\n\n**[AGREE] R2-W4**: k 索引重载。与我的 R1-M1 一致。\n\n**[AGREE] R2-W5**: J 值频繁切换（7 个不同 J 值）。与我对 model set inconsistency 的 concern 一致。核心问题是 J=13 vs J=16 交替出现，应统一使用 J=16。\n\n---\n\n### Minor 全部 [AGREE]\n\nM1-M6 均合理。特别同意 M4（S4 Self-Critique 计算细节不足影响 reproducibility）和 M2（Abstract 数字密度过高）。\n\n### Missing References 全部 [AGREE]\n\nCamilli & Shepard (1994)、Swaminathan & Rogers (1990) 是 DIF 领域应引用的经典。\n\n---\n\n### 两位 Reviewer 的一致性总结\n\nR1 和 R2 在以下核心问题上完全一致：\n1. **Scope-claim gap**（SFT ≤3B vs 标题的一般性）— R1-N1 ≈ R2-N2\n2. **Oracle ablation / γ misspecification** — R1-N2 ≈ R2-N3\n3. **Domain-level 统计力不足** — R1-N3 ≈ R2-W2（R1 标为 Must-Fix, R2 标为 Should-Fix）\n4. **J 值不一致** — R1 model set inconsistency ≈ R2-W5\n\n唯一实质分歧：R2-W3（Contribution 2 与 framing 不一致），我部分 rebut——signal filtering 是 pipeline 必要组成，但同意 framing 需调整。\n\nR2 额外提出的重要点（R1 未充分覆盖）：R2-N1 的技术新颖性不足，我完全同意且认为应列为 Must-Fix 级别。建议论文明确定位为 empirical study 而非 method paper。",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-18T04:56:27.322697+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3898
}
```

</details>

---


### Assistant

_source line 298 · 2026-05-18T04:56:34.797239+00:00_

交叉回应已提交。

总结：R2 的 3 个 Must-Fix 中全部 AGREE，5 个 Should-Fix 中 4 个 AGREE、1 个部分 REBUT（R2-W3: signal filtering 是 pipeline 必要前提，不完全偏离 framing），6 个 Minor 全部 AGREE，3 个 Missing References 全部 AGREE。

两位 Reviewer 的核心关切高度一致：scope-claim gap、oracle ablation misspecification、domain-level statistical power 不足。R2 额外提出的技术新颖性问题（R2-N1）是我 Round 1 未充分覆盖的有效观察。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 13

## Round 13

66 recorded events


### User

_source line 299 · 2026-05-21T07:25:44.987814+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计 + 统计声明可靠性**。

## Venue 信息
- **EMNLP 2026** via ACL Rolling Review (ARR May cycle)
- Deadline: 2026-05-25
- Long paper 正文 ≤ 8 页（Limitations + Ethics 不计入；References 无限）
- ACL 模板，double-blind 匿名
- Limitations 章节必须存在（缺失 desk-reject）

## 论文路径
`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex`

## 你的审查侧重

请重点评估以下维度：

1. **方法论严谨性**:
   - 2PL+γ IRT 模型的数学正确性和假设合理性
   - RRF multi-signal fusion 的统计性质
   - Dose-response profile classification algorithm 的合理性和鲁棒性
   - Bayesian inference 设置（priors, convergence diagnostics, PPP）是否恰当
   - 可识别性分析（identifiability simulation）是否充分

2. **实验设计**:
   - 控制变量注入方案（SFT injection with LoRA）的生态效度
   - 模型/家族选择的代表性和覆盖度
   - Cross-seed 和 cross-benchmark 验证的充分性
   - DiD 分析的因果推断有效性
   - Baselines 是否全面公平

3. **统计声明可靠性**:
   - 所有 CI、p-value、PPP 是否正确报告
   - 多重比较校正是否恰当
   - 效应量（Cohen's d, pp 差异）是否合理解读
   - Cross-seed stability 声明是否与 n=3 样本量匹配
   - Ensemble size J 对各分析的影响是否充分讨论

4. **可复现性**:
   - 实验细节是否足以复现
   - 超参数选择是否有依据
   - 代码/数据可用性声明

请按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 结构输出你的审稿意见。对每个 Weakness 标注严重程度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-21T07:25:51.138662+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-21T07:25:51.189590+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-21T07:25:53.969508+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*review-reviewer-session-start*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*review-reviewer-session-start*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-21T07:25:54.070377+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-21T07:25:56.536802+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/skills/**/*review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/skills/**/*review*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-21T07:25:56.738731+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-21T07:26:00.653341+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-21T07:26:00.703968+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-21T07:26:05.536264+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf",
  "project": "contamcal-irt-calibration",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf",
    "project": "contamcal-irt-calibration",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 309 · 2026-05-21T07:26:06.492466+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 310 · 2026-05-21T07:26:06.947672+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 291.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 489.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.8}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibratio
…[truncated 322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool call

_source line 311 · 2026-05-21T07:26:06.998385+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-21T07:26:14.071659+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

I found information about the ACL Rolling Review 2026. Here are the search results:

## Key Information Found:

**Reviewer Guidelines and Expectations:**
ARR developed detailed guidelines and suggestions for each step of the reviewing process, including a list of common problems in both reviews and NLP papers to watch out for.

**Review Form and Criteria:**
The reviewer and AC guidelines include codes for (meta-)review issues (I1-I12) that can be reported by the authors.

**Reviewer Responsibilities and Policies:**
- Authors should make sure all authors submit their checklists and (meta-)reviews on time and in accordance with the guidelines.

**Highly Irresponsible Reviewer Policy:**
Starting in May 2025, ARR adopted a new policy on 'highly irrespon
…[truncated 769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7579
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-21T07:27:00.786777+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 50, \"total_citations\": 69, \"unique_cited_keys\": 50, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 31, \"online_not_found\": 8, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"camilli_1994_dif\", \"type\": \"book\", \"title\": \"Methods for Identifying Biased Test Items\", \"authors\": \"Camilli, Gregory and Shepard, Lorrie A.\", \"year\": \"1994\", \"venue\": \"\"}, {\"key\": \"swaminathan_1990_dif\", \"type\": \"article\", \"title\": \"Detecting Differential Item Functioning Using Logistic Regression Procedures\", \"authors\": \"Swaminathan, Hariharan and Rogers, H. Jane\", \"year\": \"1990\", \"venue\": \"Journal of Educational Measurement\"}, {\"key\": \"holland_1993_dif\", \"type\": \"book\", \"title\": \"Differential Item Functioning\", \"authors\": \"Holland, Paul W. and Wainer, Howard\", \"year\": \"1993\", \"venue\": \"\"}, {\"key\": \"xu_2024_leakage\", \"type\": \"article\", \"title\": \"Benchmarking Benchmark Leakage in Large Language Models\", \"authors\": \"Xu, Ruijie and Wang, Zengzhi and Fan, Run-Ze and Liu, Pengfei\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"li_2024_task_contamination\", \"type\": \"inproceedings\", \"title\": \"Task Contamination: Language Models May Not Be Few-Shot Anymore\", \"authors\": \"Li, Changmao and Flanigan, Jeffrey\", \"year\": \"2024\", \"venue\": \"Proceedings of the 38th AAAI Conference on Artificial Intelligence\"}, {\"key\": \"liang_2023_helm\", \"type\": \"article\", \"title\": \"Holistic Evaluation of Language Models\", \"authors\": \"Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu,...\", \"year\": \"2023\", \"venue\": \"Annals of the New York Academy of Sciences\"}, {\"key\": \"magar_2022_contamination\", \"type\": \"inproceedings\",
…[truncated 37962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 53788
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-21T07:27:07.162446+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 315 · 2026-05-21T07:27:07.667429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 316 · 2026-05-21T07:27:08.703683+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1541
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-21T07:27:08.705003+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1037
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-21T07:27:08.734678+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 319 · 2026-05-21T07:27:09.141820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 320 · 2026-05-21T07:27:09.697878+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 963
}
```

</details>

---


### Tool call

_source line 321 · 2026-05-21T07:27:09.698293+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 322 · 2026-05-21T07:27:10.556607+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1414
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-21T07:27:10.557832+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-21T07:27:10.558167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 325 · 2026-05-21T07:27:11.061509+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 326 · 2026-05-21T07:27:11.518036+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 327 · 2026-05-21T07:27:11.518506+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-21T07:27:12.425490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-21T07:27:12.980612+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1919
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-21T07:27:12.981080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-21T07:27:15.041545+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3523
}
```

</details>

---


### Tool result

_source line 332 · 2026-05-21T07:27:15.044754+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2619
}
```

</details>

---


### Tool call

_source line 333 · 2026-05-21T07:27:15.047478+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and scoring scales used by ACL Rolling Review reviewers. I need all the official dimensions (e.g., soundness, excitement, reproducibility, overall assessment) and their rating scales with descriptions for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and scoring scales used by ACL Rolling Review reviewers. I need all the official dimensions (e.g., soundness, excitement, reproducibility, overall assessment) and their rating scales with descriptions for each score level."
  }
}
```

</details>

---


### Tool result

_source line 334 · 2026-05-21T07:27:15.199065+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2217
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-21T07:27:23.689390+00:00_

# ARR Review Form Criteria

Based on the ARR Reviewer Guidelines, the official review form includes three primary scoring dimensions:

## Scoring Dimensions

**1. Soundness**
The guidelines state reviewers must ensure that "soundness scores must be justified by the text of the review." Low soundness scores require explicit justification in the review content; unexplained low scores indicate the review doesn't faithfully represent the recommendation.

**2. Excitement**
Described as a separate, subjective dimension reflecting personal interest. The guidelines note this is "orthogonal to the assessment of the soundness of the paper" and doesn't require explicit justification.

**3. Overall Assessment**
A composite recommendation score reflecting "soundness, excitement, and also other factors like novelty and impact." This represents the explicit recommendation for paper acceptance outcomes.

## Additional Scoring Elements

**Reproducibility**: Justified scores assessing whether sufficient details exist for experiment reproduction, including code/data availability and hyperparameter documentation.

**Confidence**: Reviewers can indicate confidence levels, with instructions to specify when expertise doesn't cover certain submission aspects.

## Key Principle

The guidelines emphasize that "all papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible," though excitement levels may vary among acceptable papers.

The document doesn't provide granular numerical scales (like 1-5 ratings) but emphasizes that all scores must be justified through substantive review text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8641
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-21T07:27:32.176226+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf",
  "project": "contamcal-irt-calibration",
  "pages": "11-18",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf",
    "project": "contamcal-irt-calibration",
    "pages": "11-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 337 · 2026-05-21T07:27:32.730046+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form scoring scale 1-5 soundness excitement overall assessment numerical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form scoring scale 1-5 soundness excitement overall assessment numerical"
  }
}
```

</details>

---


### Tool result

_source line 338 · 2026-05-21T07:27:34.242874+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 573.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 584.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.2}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 396.9}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 395.1}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 475.2}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 114.1}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2066
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-21T07:27:41.699539+00:00_

Web search results for query: "ACL Rolling Review review form scoring scale 1-5 soundness excitement overall assessment numerical"

Links: [{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/acguidelines.md at main · yoshitomo-matsubara/aclrollingreview","url":"https://github.com/yoshitomo-matsubara/aclrollingreview/blob/main/acguidelines.md"},{"title":"Program Chairs' Report on Peer Review at ACL 2023","url":"http://www.cs.umd.edu/~jbg/docs/2023_acl_peer_review_report.pdf"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"}]

Based on the search results, here's what I found about the ACL Rolling Review (ARR) scoring system:

## Overview of Scoring

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Scoring Scales

Both soundness and excitement u
…[truncated 1150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8969
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-21T07:27:44.669246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 341 · 2026-05-21T07:27:45.171069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-21T07:27:46.365659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 343 · 2026-05-21T07:27:47.654758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-21T07:27:47.655185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 345 · 2026-05-21T07:27:47.706047+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 346 · 2026-05-21T07:27:49.828791+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5159
}
```

</details>

---


### Tool call

_source line 347 · 2026-05-21T07:27:49.829223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-21T07:27:49.829701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-21T07:27:51.948880+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2119
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-21T07:27:51.949294+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form with ALL scoring dimensions, their numerical scales, and the description for each score level. Include soundness, excitement, overall assessment, reproducibility, confidence, and any other scored dimensions. I need the exact scale descriptions (e.g., 5 = ..., 4 = ..., etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form with ALL scoring dimensions, their numerical scales, and the description for each score level. Include soundness, excitement, overall assessment, reproducibility, confidence, and any other scored dimensions. I need the exact scale descriptions (e.g., 5 = ..., 4 = ..., etc.)."
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-21T07:27:54.978475+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 9807
}
```

</details>

---


### Tool result

_source line 352 · 2026-05-21T07:27:56.740538+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 9034
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-21T07:27:56.747230+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 9092
}
```

</details>

---


### Tool result

_source line 354 · 2026-05-21T07:27:56.952382+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 10586
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-21T07:27:57.356919+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 9701
}
```

</details>

---


### Tool result

_source line 356 · 2026-05-21T07:27:57.457997+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7628
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-21T07:28:01.775456+00:00_

# ARR Review Form Scoring Dimensions

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me"

## Overall Assessment
- **5**: "Consider for Award: top 2.5% papers"
- **4**: "Conference: could be accepted to an ACL conference"
- **3**: "Findings: could be accepted to Findings of the ACL"
- **2**: "Resubmit next cycle: needs substantial revisions"
- **1**: "Do not resubmit: fully redone or not relevant"

## Reproducibility
- **5**: "They could easily reproduce the results"
- **4**: "They could mostly reproduce the results"
- **3**: "They could reproduce with some difficulty"
- **2**: "They would be hard pressed to reproduce the results"
- **1**: "They would not be able to reproduce the results"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9826
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-21T07:31:10.461030+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见：方法严谨性 + 实验设计 + 统计声明可靠性\n\n**论文标题**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n\n---\n\n## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 将 benchmark contamination 建模为 psychometric dose-response 问题的思路新颖且有价值，但核心实验在统计功效边界上运行（n=3 seeds, J=13–16 models），多个关键 claim 的证据强度不足以支撑其表述力度。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 方法论框架扎实（explanatory IRT + RRF fusion），但经验验证在 identifiability 边界运行；DiD 无显著性可能是 power 不足而非真阴性；多处 claim 强于证据 |\n| Excitement | 3.5/5 | 将 contamination 视为连续剂量效应并建立 dose-response taxonomy 是真正的 conceptual novelty；若统计问题得到解决，有潜力影响社区对 benchmark contamination 的思考方式 |\n| Reproducibility | 3/5 | 模型和 benchmark 公开，方法描述详细，但无代码/数据发布承诺（Ethics Statement 仅说 \"publicly available\" 数据集）；IRT 模型的 Stan 实现细节分散在正文和 appendix 中 |\n| Confidence | 4/5 | 对 IRT 建模、Bayesian inference、实验设计有较强专业背景；对个别 contamination detection signal 的内部机制了解较浅 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Cross-seed stability 声明与 n=3 样本量严重不匹配\n\n- 具体位置：Section 5.3, Table 3\n- 问题：论文以 n=3 random seeds 为基础声称 dose-response pattern 的 \"cross-seed stability\"（例如 \"strict sign consistency requires all seeds to share the same sign of Δacc(d0)\"）。但 n=3 下任何方差估计的置信区间都极宽——即使 3/3 seeds 同方向，bootstrap 置信水平也仅 ~87.5%（远低于惯例 95%）。Table 3 报告了 per-seed Δacc 范围（如 Qwen-7B: \"−1.38 to +1.19\"），但未提供 seed 间变异性的正式统计检验或置信区间。论文的 taxonomy-level consistency criteria（\"2/5 families agree\" for strict sign consistency）本身就是在小样本上二次聚合，统计可靠性存疑。\n- 为什么影响接收：dose-response taxonomy 是论文的核心贡献（Contribution 1），如果分类在更多 seeds 下不稳定，整个框架的实用价值成问题。\n- 建议修改方向：(1) 增加到至少 n=5–10 seeds（对于 0.5B–3B 模型，LoRA SFT 成本可控）；(2) 报告 bootstrap CI 覆盖 seed 变异性；(3) 降低 claim 力度，明确标注 \"preliminary taxonomy under limited replication\"。\n\n**N2** [critical] IRT 模型 identifiability 在经验 ensemble size (J=13–16) 下刚好处于边界\n\n- 具体位置：Section 3.3 (Identifiability), Appendix D, Appendix P\n- 问题：Appendix D 的 simulation 显示 AUC recovery 在 J≥16 时达到 >0.85，95% CI coverage 在 J=13–16 时为 nominal（~0.93）。但经验分析中，排除后实际 J=16（Section 5, Appendix G: 16 out of 16 models retained after exclusion for seed=42, but other seeds may differ）。这意味着论文的统计推断恰好运行在 simulation 验证的下界。更关键的是：\n  - Appendix P 的 DGP simulation 显示 CI coverage 在 J 增大时反而下降（Table 11: J=500 时 coverage 仅 0.68–1.00），论文解释为 \"the intervals become overcondident as J increases because the model converges to a biased point estimate\"。这暗示 2PL+γ 模型存在系统性偏差，在大 J 下会过度自信。\n  - 论文的 identifiability simulation 使用的是 uniform exposure（Appendix D），但实际 RRF exposure 分布是 right-skewed 的（Section 3.2 提到 \"most model-item pairs receiving near-zero exposure\"）。在高度偏斜的 exposure 分布下，γ 的 identifiability 可能更差。\n- 为什么影响接收：如果 IRT 参数估计不可靠，下游的 dose-response classification 和 calibration 结论都会受影响。\n- 建议修改方向：(1) 在 simulation 中使用与实际 RRF exposure 分布匹配的 skewed exposure 而非 uniform；(2) 明确报告每个 seed 下实际 J 和 exclusion 情况；(3) 讨论 CI coverage 随 J 下降的理论原因及其对当前结论的影响。\n\n**N3** [critical] DiD 分析的 null result 可能是 statistical power 不足而非真阴性\n\n- 具体位置：Section 5.4, Table 4, Figure 2\n- 问题：论文声称 \"All DiD non-significant: contamination operates via global capability modulation\"（Contribution 2）。但 DiD 检验的 power 取决于：(1) per-item 效应量——如果 contamination 同时提升全局能力并有微小 item-specific 效应，DiD 可能检测不到后者；(2) n=3 seeds 提供的 within-cell 变异性极有限；(3) treated vs. untreated item 的划分阈值（d025）可能不够灵敏。Table 4 显示 DID 值范围从 −0.8 到 +0.6pp，这些效应量在 n=3 下的 power 是多少？论文未做 power analysis。\n- 此外，Figure 2 的 symmetry 声明（\"confirm symmetry (gap < 0.4pp)\"）依赖于视觉判断而非正式检验。\n- 为什么影响接收：将 \"no significant effect\" 等同于 \"no effect\" 是经典的 absence-of-evidence ≠ evidence-of-absence 错误。如果论文要做因果声明（\"causal evidence\"），必须证明 power 足够。\n- 建议修改方向：(1) 做 post-hoc power analysis 报告最小可检测效应量（MDES）；(2) 将结论从 \"contamination operates via global modulation\" 弱化为 \"we find no evidence of item-specific memorization at the current power level\"；(3) 讨论如果存在例如 0.5pp 的 item-specific 效应，当前设计是否能检测到。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] RRF fusion 缺乏 calibration 验证\n\n- 具体位置：Section 3.2, Eq. (1)\n- 问题：RRF 来自信息检索（Cormack et al., 2009），其 rank-based fusion 假设各 signal 的 rank ordering 有意义且可比较。但论文未验证：(1) RRF score v_ij 的数值大小是否反映真实 contamination 程度（而非仅是排名结果）；(2) 4 个 signal 中任何一个翻转排序时 fusion 的鲁棒性；(3) signal 间相关性——如果 S1-S4 高度相关，RRF 相当于对同一信息加权平均，并不比单一 signal 好。Table 5 显示 RRF-guided selection 比 random 好（MAE 0.006 vs 较高值），但这仅间接验证了 RRF 选择了 \"好的\" items，而非 v_ij 本身是 calibrated contamination measure。\n- 建议：(1) 报告 4 个 signal 间的 rank correlation；(2) 做 leave-one-signal-out 消融验证 RRF 的 complementarity；(3) 对 v_ij 做 calibration plot（predicted vs. actual contamination）——在 controlled injection 设定下这是可行的。\n\n**W2** [warning] SFT injection 的 ecological validity 未充分量化\n\n- 具体位置：Section 4.1, Limitations (page 9)\n- 问题：真实的 benchmark leakage 发生在 pretraining 阶段（trillion-token web crawl），而本文用 post-training LoRA SFT 注入。论文在 Limitations 中承认这一点（\"pretraining-stage leakage...may produce qualitatively different contamination signatures\"），但正文的 contribution 表述（\"we perform controlled SFT injection...and discover qualitatively different dose-response patterns\"）和标题（\"Profiling Contamination Dose-Response\"）暗示更广泛的适用性。\n- SFT injection 在 AUGMENT mode（将 contaminated items appended to, not replacing, base SFT data）下进行——这进一步偏离真实场景，因为实际的 web crawl 泄露不会在 fine-tuning 数据中以这种方式出现。\n- 建议：(1) 在 abstract/intro 中明确限定为 \"post-training contamination\"；(2) 设计一个小规模的 pretraining injection 实验（即使只用 0.5B 模型）以验证 dose-response pattern 是否 transfer；(3) 讨论 AUGMENT vs REPLACE mode 的影响。\n\n**W3** [warning] Baseline 比较中 ContamCal 的优势不够显著\n\n- 具体位置：Section 5.5, Table 5, Tables 12-13 (Appendix R)\n- 问题：Table 5 中 ContamCal (4PL+γ) 在 MMLU 上 MAE=0.035，而 B4-LinearRegression MAE=0.071——improvement 约 50%。但在 ARC 上 ContamCal MAE=0.035 vs B4 MAE=0.056（更小的差距），在 GSM8K 上（Table 13）ContamCal MAE=0.020 vs B4 MAE=0.003（B4 反而更好！）。B6-DCR 在 Table 5 中无 MAE 值（marked as \"—\"），论文仅说 \"B6-DCR systematically overcorrects\"，未定量比较。\n- 在 full baseline comparison (Table 12, ARC, pooled 0.5B+1.5B), ContamCal MAE=0.035 vs B0-Raw 0.059, B3-Vanilla4PL 0.071, B4-LinearRegression 0.056。改善存在但不大，且在 GSM8K 上反而不如最简单的 B4。\n- 建议：(1) 在所有 benchmark 上统一报告所有 baseline 的 MAE，不要选择性报告；(2) 明确讨论 ContamCal 在 GSM8K 上不如 B4 的原因；(3) 考虑用 paired bootstrap test 检验 MAE 差异是否显著。\n\n**W4** [warning] Bayesian 和 frequentist 术语混用\n\n- 具体位置：多处，例如 Section 5.1 (\"significant\"), Section 5.2 (\"statistically significant at p < 0.05\"), Section 5.4 (\"non-significant\")\n- 问题：论文使用 Bayesian MCMC 推断（NUTS in Stan），posterior credible intervals 在语义上不同于 frequentist confidence intervals。但正文中多次使用 \"significant\" \"p-value\" 等 frequentist 术语：\n  - Section 5.1 提到 \"CI excludes zero\" 作为 significance 判据——这是 Bayesian credible interval 的解读，与 p-value 不同\n  - Table 1 注释中出现 \"p < 0.0005\"——这里的 p 是 PPP (posterior predictive p-value)？还是 frequentist p？未说明\n  - Section 5.4 的 DiD 检验似乎使用的是 frequentist t-test（\"p > .05; ns\"），而 IRT 参数本身是 Bayesian 估计\n  - Section 5.2 提到 \"not statistically significant at p < 0.05\"——同样未说明 p 的来源\n- 建议：(1) 统一统计框架，明确标注每个检验是 Bayesian 还是 frequentist；(2) 对 Bayesian CI，使用 \"credible interval\" 而非 \"confidence interval\"；(3) 对 PPP，明确标注。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Algorithm 1 的 threshold τ 在正文中说是 \"explicit and adaptive\"（Section 3.4），但 τ 的具体取值（0.5, 0.75, 1.0, 1.25, 1.5, 2.0 pp）在 Appendix K Table 9 中给出。正文应提供 default τ 值或至少指向 appendix。\n- **M2**: Section 3.2 将 |S| = 3 作为 \"our primary pipeline\"（排除 S2 和 S4 因为某些模型不支持），但 Table 5 的 calibration 分析使用的是 \"300 RRF-filtered items\"——是用 3 signal 还是 4 signal 的 RRF？不清楚。\n- **M3**: Appendix G 的 model exclusion criteria（\"mismatched naming conventions between evaluation and signal extraction stages\"）过于模糊，无法复现。\n- **M4**: Figure 1 被引用为 dose-response pattern 的可视化，但图中仅展示了一个 benchmark (MMLU) 的一个 seed (seed=42) 的结果。应在 caption 中说明这是代表性示例。\n- **M5**: Eq. (2) 定义了 decontamination accuracy Acc_j^*，但未解释 \"posterior expectation under zero exposure\" 在实践中如何计算——是将 v_ij 设为 0 后重新计算 posterior mean of θ_j，还是直接将 γ_i · v_ij 从 logit 中减去？这两种做法在非线性模型中结果不同。\n- **M6**: 引用格式：部分 bib 条目年份与 OpenAlex 不匹配（如 holland_1993_dif 标注 1993 但 API 返回 2009，lord_1980_irt 标注 1980 但 API 返回 2012——可能是再版）。建议核查。\n\n---\n\n## Questions to Authors\n\n**Q1**: Appendix P 显示 CI coverage 随 J 增大而下降（Table 11），论文解释为 \"model converges to a biased point estimate\"。能否详细解释这个 bias 的来源？这是否意味着 2PL+γ 模型在大样本下是 misspecified 的？如果是，为什么在小 J 下 coverage 反而好——是因为 prior 在 dominating？\n\n**Q2**: RRF exposure score v_ij 的分布是 right-skewed 的（大部分 items 接近 zero）。在 IRT 模型中，γ_i 的估计主要依赖有非零 v_ij 的 items。但如果绝大多数 items 的 v_ij ≈ 0，γ_i 实际上由少数高 exposure items 驱动。这是否引入了 leverage effect？有没有做 influential observation 诊断？\n\n**Q3**: Table 2 的 cross-benchmark transfer 结论基于 d100 exposure。在 lower dosage 下（d005, d025）transfer pattern 是否一致？\n\n**Q4**: 论文排除了 0.5B 模型因 position bias（\"A-option rate: 46% at d000 to 98% at d100\"）。这个现象本身非常有趣——SFT contamination 是否将 0.5B 模型 \"trained\" 为总选 A？这是否暗示 small models 的 dose-response 可能完全不同于 medium/large models？论文是否考虑过将 position bias correction 后的 0.5B 结果作为补充分析？\n\n---\n\n## Missing References\n\n- **Recht et al. (2019)** \"Do ImageNet Classifiers Generalize to ImageNet?\" — 关于 benchmark overfitting 的经典工作，与 contamination 主题高度相关。\n- **Yang et al. (2023)** \"Rethinking Benchmark and Contamination for Language Models with Rephrased Samples\" — 直接相关的 contamination 通过 rephrasing 减轻的工作。\n- **Bakhtin et al. (2024)** 或其他关于 pretraining data deduplication 对 contamination 影响的工作——论文讨论了 post-training contamination 但未引用 pretraining decontamination 的方法论工作。\n\n---\n\n## 主要优势\n\n1. **概念新颖性**：将 benchmark contamination 建模为连续剂量-效应关系并用 psychometric 框架分析是真正的新视角。Dose-response taxonomy（Immune/Collapse/V-Recovery/Benefit）提供了比二分法（contaminated/clean）更丰富的分析维度。\n2. **实验设计的 controlled injection 方法论**：用 LoRA SFT 在已知 ground truth 下注入 contamination，使得可以对 detection 方法进行有控制的评估——这在现有文献中较少见。\n3. **Appendix 的 thoroughness**：18 个 appendix sections 覆盖了 identifiability simulation、DGP robustness、sensitivity analysis、convergence diagnostics 等——表明作者对方法论细节的认真态度。\n4. **多 baseline 比较**：7 个 baseline 方法（包括 raw accuracy、remove-and-rescore、vanilla IRT、linear regression、Emperor、DCR）提供了较全面的参照。\n5. **Within-family domain analysis**（Section 5.7）揭示了 STEM 与 Social Sciences 在 contamination 敏感性上的差异，这是一个有实际价值的发现。\n",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见：方法严谨性 + 实验设计 + 统计声明可靠性\n\n**论文标题**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\n\n---\n\n## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 将 benchmark contamination 建模为 psychometric dose-response 问题的思路新颖且有价值，但核心实验在统计功效边界上运行（n=3 seeds, J=13–16 models），多个关键 claim 的证据强度不足以支撑其表述力度。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 方法论框架扎实（explanatory IRT + RRF fusion），但经验验证在 identifiability 边界运行；DiD 无显著性可能是 power 不足而非真阴性；多处 claim 强于证据 |\n| Excitement | 3.5/5 | 将 contamination 视为连续剂量效应并建立 dose-response taxonomy 是真正的 conceptual novelty；若统计问题得到解决，有潜力影响社区对 benchmark contamination 的思考方式 |\n| Reproducibility | 3/5 | 模型和 benchmark 公开，方法描述详细，但无代码/数据发布承诺（Ethics Statement 仅说 \"publicly available\" 数据集）；IRT 模型的 Stan 实现细节分散在正文和 appendix 中 |\n| Confidence | 4/5 | 对 IRT 建模、Bayesian inference、实验设计有较强专业背景；对个别 contamination detection signal 的内部机制了解较浅 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Cross-seed stability 声明与 n=3 样本量严重不匹配\n\n- 具体位置：Section 5.3, Table 3\n- 问题：论文以 n=3 random seeds 为基础声称 dose-response pattern 的 \"cross-seed stability\"（例如 \"strict sign consistency requires all seeds to share the same sign of Δacc(d0)\"）。但 n=3 下任何方差估计的置信区间都极宽——即使 3/3 seeds 同方向，bootstrap 置信水平也仅 ~87.5%（远低于惯例 95%）。Table 3 报告了 per-seed Δacc 范围（如 Qwen-7B: \"−1.38 to +1.19\"），但未提供 seed 间变异性的正式统计检验或置信区间。论文的 taxonomy-level consistency criteria（\"2/5 families agree\" for strict sign consistency）本身就是在小样本上二次聚合，统计可靠性存疑。\n- 为什么影响接收：dose-response taxonomy 是论文的核心贡献（Contribution 1），如果分类在更多 seeds 下不稳定，整个框架的实用价值成问题。\n- 建议修改方向：(1) 增加到至少 n=5–10 seeds（对于 0.5B–3B 模型，LoRA SFT 成本可控）；(2) 报告 bootstrap CI 覆盖 seed 变异性；(3) 降低 claim 力度，明确标注 \"preliminary taxonomy under limited replication\"。\n\n**N2** [critical] IRT 模型 identifiability 在经验 ensemble size (J=13–16) 下刚好处于边界\n\n- 具体位置：Section 3.3 (Identifiability), Appendix D, Appendix P\n- 问题：Appendix D 的 simulation 显示 AUC recovery 在 J≥16 时达到 >0.85，95% CI coverage 在 J=13–16 时为 nominal（~0.93）。但经验分析中，排除后实际 J=16（Section 5, Appendix G: 16 out of 16 models retained after exclusion for seed=42, but other seeds may differ）。这意味着论文的统计推断恰好运行在 simulation 验证的下界。更关键的是：\n  - Appendix P 的 DGP simulation 显示 CI coverage 在 J 增大时反而下降（Table 11: J=500 时 coverage 仅 0.68–1.00），论文解释为 \"the intervals become overcondident as J increases because the model converges to a biased point estimate\"。这暗示 2PL+γ 模型存在系统性偏差，在大 J 下会过度自信。\n  - 论文的 identifiability simulation 使用的是 uniform exposure（Appendix D），但实际 RRF exposure 分布是 right-skewed 的（Section 3.2 提到 \"most model-item pairs receiving near-zero exposure\"）。在高度偏斜的 exposure 分布下，γ 的 identifiability 可能更差。\n- 为什么影响接收：如果 IRT 参数估计不可靠，下游的 dose-response classification 和 calibration 结论都会受影响。\n- 建议修改方向：(1) 在 simulation 中使用与实际 RRF exposure 分布匹配的 skewed exposure 而非 uniform；(2) 明确报告每个 seed 下实际 J 和 exclusion 情况；(3) 讨论 CI coverage 随 J 下降的理论原因及其对当前结论的影响。\n\n**N3** [critical] DiD 分析的 null result 可能是 statistical power 不足而非真阴性\n\n- 具体位置：Section 5.4, Table 4, Figure 2\n- 问题：论文声称 \"All DiD non-significant: contamination operates via global capability modulation\"（Contribution 2）。但 DiD 检验的 power 取决于：(1) per-item 效应量——如果 contamination 同时提升全局能力并有微小 item-specific 效应，DiD 可能检测不到后者；(2) n=3 seeds 提供的 within-cell 变异性极有限；(3) treated vs. untreated item 的划分阈值（d025）可能不够灵敏。Table 4 显示 DID 值范围从 −0.8 到 +0.6pp，这些效应量在 n=3 下的 power 是多少？论文未做 power analysis。\n- 此外，Figure 2 的 symmetry 声明（\"confirm symmetry (gap < 0.4pp)\"）依赖于视觉判断而非正式检验。\n- 为什么影响接收：将 \"no significant effect\" 等同于 \"no effect\" 是经典的 absence-of-evidence ≠ evidence-of-absence 错误。如果论文要做因果声明（\"causal evidence\"），必须证明 power 足够。\n- 建议修改方向：(1) 做 post-hoc power analysis 报告最小可检测效应量（MDES）；(2) 将结论从 \"contamination operates via global modulation\" 弱化为 \"we find no evidence of item-specific memorization at the current power level\"；(3) 讨论如果存在例如 0.5pp 的 item-specific 效应，当前设计是否能检测到。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] RRF fusion 缺乏 calibration 验证\n\n- 具体位置：Section 3.2, Eq. (1)\n- 问题：RRF 来自信息检索（Cormack et al., 2009），其 rank-based fusion 假设各 signal 的 rank ordering 有意义且可比较。但论文未验证：(1) RRF score v_ij 的数值大小是否反映真实 contamination 程度（而非仅是排名结果）；(2) 4 个 signal 中任何一个翻转排序时 fusion 的鲁棒性；(3) signal 间相关性——如果 S1-S4 高度相关，RRF 相当于对同一信息加权平均，并不比单一 signal 好。Table 5 显示 RRF-guided selection 比 random 好（MAE 0.006 vs 较高值），但这仅间接验证了 RRF 选择了 \"好的\" items，而非 v_ij 本身是 calibrated contamination measure。\n- 建议：(1) 报告 4 个 signal 间的 rank correlation；(2) 做 leave-one-signal-out 消融验证 RRF 的 complementarity；(3) 对 v_ij 做 calibration plot（predicted vs. actual contamination）——在 controlled injection 设定下这是可行的。\n\n**W2** [warning] SFT injection 的 ecological validity 未充分量化\n\n- 具体位置：Section 4.1, Limitations (page 9)\n- 问题：真实的 benchmark leakage 发生在 pretraining 阶段（trillion-token web crawl），而本文用 post-training LoRA SFT 注入。论文在 Limitations 中承认这一点（\"pretraining-stage leakage...may produce qualitatively different contamination signatures\"），但正文的 contribution 表述（\"we perform controlled SFT injection...and discover qualitatively different dose-response patterns\"）和标题（\"Profiling Contamination Dose-Response\"）暗示更广泛的适用性。\n- SFT injection 在 AUGMENT mode（将 contaminated items appended to, not replacing, base SFT data）下进行——这进一步偏离真实场景，因为实际的 web crawl 泄露不会在 fine-tuning 数据中以这种方式出现。\n- 建议：(1) 在 abstract/intro 中明确限定为 \"post-training contamination\"；(2) 设计一个小规模的 pretraining injection 实验（即使只用 0.5B 模型）以验证 dose-response pattern 是否 transfer；(3) 讨论 AUGMENT vs REPLACE mode 的影响。\n\n**W3** [warning] Baseline 比较中 ContamCal 的优势不够显著\n\n- 具体位置：Section 5.5, Table 5, Tables 12-13 (Appendix R)\n- 问题：Table 5 中 ContamCal (4PL+γ) 在 MMLU 上 MAE=0.035，而 B4-LinearRegression MAE=0.071——improvement 约 50%。但在 ARC 上 ContamCal MAE=0.035 vs B4 MAE=0.056（更小的差距），在 GSM8K 上（Table 13）ContamCal MAE=0.020 vs B4 MAE=0.003（B4 反而更好！）。B6-DCR 在 Table 5 中无 MAE 值（marked as \"—\"），论文仅说 \"B6-DCR systematically overcorrects\"，未定量比较。\n- 在 full baseline comparison (Table 12, ARC, pooled 0.5B+1.5B), ContamCal MAE=0.035 vs B0-Raw 0.059, B3-Vanilla4PL 0.071, B4-LinearRegression 0.056。改善存在但不大，且在 GSM8K 上反而不如最简单的 B4。\n- 建议：(1) 在所有 benchmark 上统一报告所有 baseline 的 MAE，不要选择性报告；(2) 明确讨论 ContamCal 在 GSM8K 上不如 B4 的原因；(3) 考虑用 paired bootstrap test 检验 MAE 差异是否显著。\n\n**W4** [warning] Bayesian 和 frequentist 术语混用\n\n- 具体位置：多处，例如 Section 5.1 (\"significant\"), Section 5.2 (\"statistically significant at p < 0.05\"), Section 5.4 (\"non-significant\")\n- 问题：论文使用 Bayesian MCMC 推断（NUTS in Stan），posterior credible intervals 在语义上不同于 frequentist confidence intervals。但正文中多次使用 \"significant\" \"p-value\" 等 frequentist 术语：\n  - Section 5.1 提到 \"CI excludes zero\" 作为 significance 判据——这是 Bayesian credible interval 的解读，与 p-value 不同\n  - Table 1 注释中出现 \"p < 0.0005\"——这里的 p 是 PPP (posterior predictive p-value)？还是 frequentist p？未说明\n  - Section 5.4 的 DiD 检验似乎使用的是 frequentist t-test（\"p > .05; ns\"），而 IRT 参数本身是 Bayesian 估计\n  - Section 5.2 提到 \"not statistically significant at p < 0.05\"——同样未说明 p 的来源\n- 建议：(1) 统一统计框架，明确标注每个检验是 Bayesian 还是 frequentist；(2) 对 Bayesian CI，使用 \"credible interval\" 而非 \"confidence interval\"；(3) 对 PPP，明确标注。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Algorithm 1 的 threshold τ 在正文中说是 \"explicit and adaptive\"（Section 3.4），但 τ 的具体取值（0.5, 0.75, 1.0, 1.25, 1.5, 2.0 pp）在 Appendix K Table 9 中给出。正文应提供 default τ 值或至少指向 appendix。\n- **M2**: Section 3.2 将 |S| = 3 作为 \"our primary pipeline\"（排除 S2 和 S4 因为某些模型不支持），但 Table 5 的 calibration 分析使用的是 \"300 RRF-filtered items\"——是用 3 signal 还是 4 signal 的 RRF？不清楚。\n- **M3**: Appendix G 的 model exclusion criteria（\"mismatched naming conventions between evaluation and signal extraction stages\"）过于模糊，无法复现。\n- **M4**: Figure 1 被引用为 dose-response pattern 的可视化，但图中仅展示了一个 benchmark (MMLU) 的一个 seed (seed=42) 的结果。应在 caption 中说明这是代表性示例。\n- **M5**: Eq. (2) 定义了 decontamination accuracy Acc_j^*，但未解释 \"posterior expectation under zero exposure\" 在实践中如何计算——是将 v_ij 设为 0 后重新计算 posterior mean of θ_j，还是直接将 γ_i · v_ij 从 logit 中减去？这两种做法在非线性模型中结果不同。\n- **M6**: 引用格式：部分 bib 条目年份与 OpenAlex 不匹配（如 holland_1993_dif 标注 1993 但 API 返回 2009，lord_1980_irt 标注 1980 但 API 返回 2012——可能是再版）。建议核查。\n\n---\n\n## Questions to Authors\n\n**Q1**: Appendix P 显示 CI coverage 随 J 增大而下降（Table 11），论文解释为 \"model converges to a biased point estimate\"。能否详细解释这个 bias 的来源？这是否意味着 2PL+γ 模型在大样本下是 misspecified 的？如果是，为什么在小 J 下 coverage 反而好——是因为 prior 在 dominating？\n\n**Q2**: RRF exposure score v_ij 的分布是 right-skewed 的（大部分 items 接近 zero）。在 IRT 模型中，γ_i 的估计主要依赖有非零 v_ij 的 items。但如果绝大多数 items 的 v_ij ≈ 0，γ_i 实际上由少数高 exposure items 驱动。这是否引入了 leverage effect？有没有做 influential observation 诊断？\n\n**Q3**: Table 2 的 cross-benchmark transfer 结论基于 d100 exposure。在 lower dosage 下（d005, d025）transfer pattern 是否一致？\n\n**Q4**: 论文排除了 0.5B 模型因 position bias（\"A-option rate: 46% at d000 to 98% at d100\"）。这个现象本身非常有趣——SFT contamination 是否将 0.5B 模型 \"trained\" 为总选 A？这是否暗示 small models 的 dose-response 可能完全不同于 medium/large models？论文是否考虑过将 position bias correction 后的 0.5B 结果作为补充分析？\n\n---\n\n## Missing References\n\n- **Recht et al. (2019)** \"Do ImageNet Classifiers Generalize to ImageNet?\" — 关于 benchmark overfitting 的经典工作，与 contamination 主题高度相关。\n- **Yang et al. (2023)** \"Rethinking Benchmark and Contamination for Language Models with Rephrased Samples\" — 直接相关的 contamination 通过 rephrasing 减轻的工作。\n- **Bakhtin et al. (2024)** 或其他关于 pretraining data deduplication 对 contamination 影响的工作——论文讨论了 post-training contamination 但未引用 pretraining decontamination 的方法论工作。\n\n---\n\n## 主要优势\n\n1. **概念新颖性**：将 benchmark contamination 建模为连续剂量-效应关系并用 psychometric 框架分析是真正的新视角。Dose-response taxonomy（Immune/Collapse/V-Recovery/Benefit）提供了比二分法（contaminated/clean）更丰富的分析维度。\n2. **实验设计的 controlled injection 方法论**：用 LoRA SFT 在已知 ground truth 下注入 contamination，使得可以对 detection 方法进行有控制的评估——这在现有文献中较少见。\n3. **Appendix 的 thoroughness**：18 个 appendix sections 覆盖了 identifiability simulation、DGP robustness、sensitivity analysis、convergence diagnostics 等——表明作者对方法论细节的认真态度。\n4. **多 baseline 比较**：7 个 baseline 方法（包括 raw accuracy、remove-and-rescore、vanilla IRT、linear regression、Emperor、DCR）提供了较全面的参照。\n5. **Within-family domain analysis**（Section 5.7）揭示了 STEM 与 Social Sciences 在 contamination 敏感性上的差异，这是一个有实际价值的发现。\n",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-21T07:31:14.911191+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4450
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-21T07:31:18.739709+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-21T07:31:18.790672+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-21T07:31:23.407233+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-21T07:31:23.457875+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 364 · 2026-05-21T07:31:30.605011+00:00_

审稿意见已提交给 Review Director。

**总结**：Overall 3.5（Borderline Conference）。核心创新——用 IRT dose-response 框架分析 contamination——有价值，但三个 critical 问题需要解决：(1) n=3 seeds 不足以支撑 cross-seed stability 声明；(2) IRT identifiability 恰好在经验 ensemble size 的边界上，且 simulation 用的 uniform exposure 与实际 skewed 分布不匹配；(3) DiD null result 缺乏 power analysis，不能等同于 "no item-specific effect"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 14

## Round 14

20 recorded events


### User

_source line 365 · 2026-05-21T07:34:46.462682+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（cite 论文中的 Section/Table/Figure）。

---

# Reviewer 2 审稿意见（新颖性 + Related Work + 写作质量 + 格式合规）

**Overall**: 3.5 — Borderline Conference

## Must-Fix

**N1** [critical] N=4 模型族支撑 4 类分类学，泛化性不足
- 4 个模型族恰好观测到 4 种模式，可能是 post-hoc 描述。Table 1 每种模式恰好对应一个模型族，加深 overfitting-to-sample 担忧。"taxonomy" 的核心价值在于泛化——N=K 分类对 K 个观测无预测力。
- 建议：增加模型族验证（LLaMA-3, Mistral, Yi）；或将 "taxonomy" 改为 "observed response profiles"。

**N2** [critical] 与 Han et al. (2026) 的差异化论证不充分
- Han et al. (2026, EACL Findings) 已将 DIF 应用于 LLM 污染。论文仅用两句话区分。未讨论 continuous vs. binary exposure 的实际效果差异，也未将 Han et al. 方法实现为 baseline。
- 建议：增加详细 methodological comparison；理想情况下将 Han et al. 实现为 baseline。

## Should-Fix

**W1** [warning] 正文疑似超过 8 页限制
- Section 6 从 p.8 底部延伸至 p.9，估计正文约 8.3-8.5 页。

**W2** [warning] DID 分析统计效力不足以排除 item-specific effects
- N=300 items 检测 ~1pp 效应的 power 可能不足。"absence of evidence ≠ evidence of absence"。
- 建议：报告 power analysis 或 minimum detectable effect size。

**W3** [warning] 跨种子稳定性偏弱（n=3 seeds）
- sign consistency 仅 2/5 agree。大多数模型族的分类学标签对 seed 选择敏感。

**W4** [warning] Algorithm 1 硬编码阈值缺乏充分 justification
- ≥6 个硬编码阈值，Appendix 仅报告 "30/30" 粗粒度结果，缺乏 sensitivity curve。

## Minor
- M1: "pp" 首次使用未定义
- M2: Gemma-2 排除在 Section 5.2 出现突然
- M3: Limitations 10 个点可精简至 4-5 个
- M4: 引用年份问题（holland_1993_dif, lord_1980_irt）
- M5: Figure 1 浮动体位置需确认

## Missing References
- Golchin & Surdeanu (2024) "Time Travel in LLMs" (ICLR 2024)
- Sainz et al. (2023) per-benchmark contamination measurement (EMNLP 2023 Findings)
- Yang et al. (2023) rephrased samples contamination

## 新颖性评估
新颖性主要来自实验范式而非方法论。Global modulation finding 最强。定位：适合 Findings，borderline Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-21T07:35:33.550479+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf",
  "project": "contamcal-irt-calibration",
  "pages": "1,4,6,7,8,9",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf",
    "project": "contamcal-irt-calibration",
    "pages": "1,4,6,7,8,9",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-21T07:35:34.404790+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 291.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 489.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.8}], \"total_pages\": 18, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-21T07:35:37.470890+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 369 · 2026-05-21T07:35:37.973516+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 370 · 2026-05-21T07:35:38.827575+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-21T07:35:38.831246+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-21T07:35:38.831836+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 373 · 2026-05-21T07:35:39.434575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 374 · 2026-05-21T07:35:39.939367+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1107
}
```

</details>

---


### Tool call

_source line 375 · 2026-05-21T07:35:39.941799+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-21T07:35:40.343916+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-21T07:35:40.747649+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1313
}
```

</details>

---


### Tool result

_source line 378 · 2026-05-21T07:35:41.153570+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1211
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-21T07:35:41.456031+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1112
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-21T07:37:31.673412+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix\n\n**[AGREE] R2-N1: N=4 模型族支撑 4 类分类学，泛化性不足**\n\n同意此问题的核心关切，但认为严重程度需要适度修正。\n\n补充证据：Table 1 (p.6) 实际展示了 5 个模型（非 4 个），其中 Benefit pattern 同时出现在 Gemma-2 7B 和 OLMo-2 7B 两个不同家族，说明分类并非严格 one-to-one。此外，Section 5.1 的 per-model 分析（seed=42）涵盖了更多 model sizes（Qwen2.5 从 0.5B 到 14B），在 family 内部展示了 size-dependent pattern 变化（如 Qwen 小模型 Benefit vs 大模型 Collapse）。\n\n然而 R2 的核心论点成立：4 个家族不足以声称 taxonomy 的泛化性。特别是：(1) 所有家族都是 2024-2025 年的 decoder-only transformer，缺乏架构多样性（无 MoE、无 encoder-decoder）；(2) Algorithm 1 (p.4) 的 pattern 枚举是从这 4 个家族归纳出来的，无法排除第 5 种 pattern 存在的可能。\n\nR2 建议将 \"taxonomy\" 改为 \"observed response profiles\" 是合理且低成本的修改。增加 LLaMA-3/Mistral 验证更能强化论文贡献，但可能超出 revision scope。\n\n**[AGREE with nuance] R2-N2: 与 Han et al. (2026) 的差异化论证不充分**\n\n同意论证需要加强，但不完全同意需要将其实现为 baseline。\n\nRelated work (p.2) 确实仅用 \"Han et al. (2026) apply psychometric DIF to quantify contamination on item parameters, using group-based binary indicators on naturally contaminated models. ContamCal differs by introducing continuous exposure covariates\" 两句话区分，这不够充分。\n\n关键方法论差异值得详细展开：(1) Han et al. 使用 binary group indicator（contaminated vs clean groups），而本文使用 continuous per-item exposure score v_ij——这在统计上是完全不同的建模策略（DIF 是 group comparison，explanatory IRT 是 regression-on-covariate）；(2) Han et al. 无法做 dose-response profiling，因为没有 dosage gradient；(3) 本文的 multi-signal RRF fusion 是独立贡献。\n\n但要求将 Han et al. 实现为 baseline 可能不现实：(1) Han et al. 的方法需要事先知道哪些模型是 \"contaminated group\"，这在本文的 controlled injection 设定下虽然可行但在实际应用中不可行；(2) 两种方法的 output 不直接可比（binary contamination flag vs continuous contamination estimate）。建议论文增加一个 detailed methodological comparison 段落即可，不必强求 baseline 实现。\n\n---\n\n## Should-Fix\n\n**[AGREE] R2-W1: 正文疑似超过 8 页限制**\n\n确认此问题。从 PDF 视觉检查：Section 6 (Discussion and Conclusion) 起始于 p.8 底部（约页面 75% 处），延伸至 p.9 约 55% 处，之后才是 Limitations 标题。Section 6 在 p.9 上包含至少 6 个 bold 小标题段落（\"Diverse patterns, not uniform inflation\"、\"SFT ecological validity\"、\"ARC-Challenge bootstrap stability\"、\"Signal coverage\"、\"Ensemble size and per-domain power\"、\"Position bias\"、\"Diagnostic value beyond aggregate calibration\"）。\n\nEMNLP 2026 规则明确要求正文（main text）严格 ≤8 页，Limitations 和 Ethics 不计入。按当前排版，正文约 8.4–8.5 页，超标约 0.4–0.5 页。这是可能导致 desk-reject 的格式问题。\n\n修改方向：Section 6 的多个小标题段落内容与正文 Sections 5.1-5.7 的 findings 高度重叠（例如 \"Position bias\" 已在 Section 4.1 最后一段讨论过），可大幅压缩或移至 Appendix。\n\n**[AGREE] R2-W2: DiD 分析统计效力不足以排除 item-specific effects**\n\n完全同意。我在自己的审稿意见中将此列为 N3 (critical)。\n\n补充 R2 的论点：Table 4 (p.8) 报告的 DiD 效应量范围为 −0.8pp 到 +0.6pp，在 n=3 seeds 下检测 ~1pp item-specific 效应的 power 极低。论文将 \"All DiD non-significant\" 直接升级为 \"causal evidence that SFT contamination operates through global capability modulation rather than item-specific memorization\"（p.1, Abstract; p.6, \"Baseline ability gradient\" section），这是典型的 absence-of-evidence ≠ evidence-of-absence 问题。至少需要 post-hoc power analysis 报告 MDES，否则因果声明不成立。\n\n**[AGREE] R2-W3: 跨种子稳定性偏弱（n=3 seeds）**\n\n完全同意。我在自己的审稿意见中将此列为 N1 (critical) 并做了更详细的分析。\n\n补充一个 R2 未提到的细节：Section 5.3 (p.7) 自己承认 \"strict sign consistency requires all seeds to share the same sign of Δacc(d0)\" 但仅 2/5 families 满足此条件。论文随后放宽为 \"taxonomy-level consistency\"（4/5 families agree），但这个放宽标准（CB-based aggregation rule where mean Δ ≥ 1pp 即算 non-zero）本身降低了分类精度。当一个 taxonomy 需要通过放宽一致性标准才能显示 \"stable\" 时，这恰好印证了 R2 的担忧。\n\n**[AGREE with nuance] R2-W4: Algorithm 1 硬编码阈值缺乏充分 justification**\n\n部分同意。Algorithm 1 (p.4) 确实使用了多个阈值（τ for significance, r for recovery ratio, 以及 mid-trajectory volatility check 的 δ_max 等）。Appendix K (Table 9) 报告 \"30/30 model-seed-threshold combinations\" 全部通过，但这是粗粒度的 pass/fail 报告，缺乏 sensitivity curve 展示分类如何随阈值连续变化。\n\n但我认为严重程度应低于 R2 的评估。理由：(1) Table 9 的 30 种组合覆盖了 τ ∈ {0.5, 0.75, 1.0, 1.25, 1.5, 2.0} × r ∈ {1, 1.4, 5, 6, 7} pp，这是一个合理的 grid；(2) 论文的分类主要用 direction（sign of mean Δ）作为 primary criterion（Section 3.4: \"adopts direction as the primary taxonomy criterion\"），阈值仅影响边缘 case。添加一条 sensitivity curve（classification label vs τ for each family）即可解决此问题，不需要重新设计算法。\n\n---\n\n## Minor\n\n**[AGREE] R2-M1**: \"pp\" (percentage points) 确实在 Abstract 首次出现时未定义。应在首次使用时括号注明。\n\n**[AGREE] R2-M2**: Section 5.2 (p.6) 中 \"Gemma-2 excluded due to catastrophic forgetting\" 确实出现突然。建议在首次提及时简要说明原因或指向 Appendix。\n\n**[REBUT] R2-M3**: Limitations 10 个点可精简至 4-5 个。\n\n不同意。EMNLP 2026 要求 Limitations 章节必须存在但不计入页数。当前 Limitations（p.9）覆盖了 scale ceiling、seed sensitivity、cross-seed analysis、ecological validity、format sensitivity、calibration quality 等多个维度，且每点仅 1-2 句话。对于一篇方法论论文，全面列出局限性是负责任的做法。真正的问题不是 Limitations 太长，而是 R2-W1 指出的 Section 6 正文超页——应压缩 Section 6 而非 Limitations。\n\n**[AGREE] R2-M4**: 引用年份问题。我的 reference verification 也发现了 holland_1993_dif 和 lord_1980_irt 的年份不匹配（可能是再版 vs 原版）。应统一为原版年份并核实。\n\n**[AGREE] R2-M5**: Figure 1 浮动体位置应确认不违反 ACL 模板的 float 规范。\n\n---\n\n## Missing References\n\n**[AGREE]** Golchin & Surdeanu (2024) \"Time Travel in LLMs\" 是直接相关的 contamination detection 工作，应在 Related Work 的 contamination detection 段落中引用。\n\n**[AGREE]** Sainz et al. (2023) 的 per-benchmark contamination measurement 与本文的 per-benchmark analysis 直接相关。\n\n**[AGREE]** Yang et al. (2023) rephrased samples — 我在自己的审稿意见中也建议了此引用。\n\n---\n\n## 新颖性评估回应\n\nR2 将论文新颖性定位为 \"实验范式而非方法论\"，我部分不同意。\n\n2PL+γ 模型引入 continuous contamination covariate 到 explanatory IRT 框架，在方法论上确实有创新——这不是简单地将现有方法应用到新数据，而是设计了一个新的统计模型来量化 contamination 的 item-level 效应。RRF multi-signal fusion 虽然借用了 IR 技术，但其在 contamination detection 领域的应用和与 IRT 的结合是原创的。\n\n然而 R2 的判断——\"Global modulation finding 最强\"——我同意。如果 DiD 的 power 问题能解决（增加 seeds 或做 power analysis），这个发现本身足以支撑 Conference 接收。\n\n**总结**：R2 的审稿意见整体准确且建设性。N1（taxonomy 泛化性）和 W1（页数超标）是需要作者认真回应的问题。W2 和 W3 与我的 N1/N3 高度一致，交叉验证了这些问题的严重性。\n",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix\n\n**[AGREE] R2-N1: N=4 模型族支撑 4 类分类学，泛化性不足**\n\n同意此问题的核心关切，但认为严重程度需要适度修正。\n\n补充证据：Table 1 (p.6) 实际展示了 5 个模型（非 4 个），其中 Benefit pattern 同时出现在 Gemma-2 7B 和 OLMo-2 7B 两个不同家族，说明分类并非严格 one-to-one。此外，Section 5.1 的 per-model 分析（seed=42）涵盖了更多 model sizes（Qwen2.5 从 0.5B 到 14B），在 family 内部展示了 size-dependent pattern 变化（如 Qwen 小模型 Benefit vs 大模型 Collapse）。\n\n然而 R2 的核心论点成立：4 个家族不足以声称 taxonomy 的泛化性。特别是：(1) 所有家族都是 2024-2025 年的 decoder-only transformer，缺乏架构多样性（无 MoE、无 encoder-decoder）；(2) Algorithm 1 (p.4) 的 pattern 枚举是从这 4 个家族归纳出来的，无法排除第 5 种 pattern 存在的可能。\n\nR2 建议将 \"taxonomy\" 改为 \"observed response profiles\" 是合理且低成本的修改。增加 LLaMA-3/Mistral 验证更能强化论文贡献，但可能超出 revision scope。\n\n**[AGREE with nuance] R2-N2: 与 Han et al. (2026) 的差异化论证不充分**\n\n同意论证需要加强，但不完全同意需要将其实现为 baseline。\n\nRelated work (p.2) 确实仅用 \"Han et al. (2026) apply psychometric DIF to quantify contamination on item parameters, using group-based binary indicators on naturally contaminated models. ContamCal differs by introducing continuous exposure covariates\" 两句话区分，这不够充分。\n\n关键方法论差异值得详细展开：(1) Han et al. 使用 binary group indicator（contaminated vs clean groups），而本文使用 continuous per-item exposure score v_ij——这在统计上是完全不同的建模策略（DIF 是 group comparison，explanatory IRT 是 regression-on-covariate）；(2) Han et al. 无法做 dose-response profiling，因为没有 dosage gradient；(3) 本文的 multi-signal RRF fusion 是独立贡献。\n\n但要求将 Han et al. 实现为 baseline 可能不现实：(1) Han et al. 的方法需要事先知道哪些模型是 \"contaminated group\"，这在本文的 controlled injection 设定下虽然可行但在实际应用中不可行；(2) 两种方法的 output 不直接可比（binary contamination flag vs continuous contamination estimate）。建议论文增加一个 detailed methodological comparison 段落即可，不必强求 baseline 实现。\n\n---\n\n## Should-Fix\n\n**[AGREE] R2-W1: 正文疑似超过 8 页限制**\n\n确认此问题。从 PDF 视觉检查：Section 6 (Discussion and Conclusion) 起始于 p.8 底部（约页面 75% 处），延伸至 p.9 约 55% 处，之后才是 Limitations 标题。Section 6 在 p.9 上包含至少 6 个 bold 小标题段落（\"Diverse patterns, not uniform inflation\"、\"SFT ecological validity\"、\"ARC-Challenge bootstrap stability\"、\"Signal coverage\"、\"Ensemble size and per-domain power\"、\"Position bias\"、\"Diagnostic value beyond aggregate calibration\"）。\n\nEMNLP 2026 规则明确要求正文（main text）严格 ≤8 页，Limitations 和 Ethics 不计入。按当前排版，正文约 8.4–8.5 页，超标约 0.4–0.5 页。这是可能导致 desk-reject 的格式问题。\n\n修改方向：Section 6 的多个小标题段落内容与正文 Sections 5.1-5.7 的 findings 高度重叠（例如 \"Position bias\" 已在 Section 4.1 最后一段讨论过），可大幅压缩或移至 Appendix。\n\n**[AGREE] R2-W2: DiD 分析统计效力不足以排除 item-specific effects**\n\n完全同意。我在自己的审稿意见中将此列为 N3 (critical)。\n\n补充 R2 的论点：Table 4 (p.8) 报告的 DiD 效应量范围为 −0.8pp 到 +0.6pp，在 n=3 seeds 下检测 ~1pp item-specific 效应的 power 极低。论文将 \"All DiD non-significant\" 直接升级为 \"causal evidence that SFT contamination operates through global capability modulation rather than item-specific memorization\"（p.1, Abstract; p.6, \"Baseline ability gradient\" section），这是典型的 absence-of-evidence ≠ evidence-of-absence 问题。至少需要 post-hoc power analysis 报告 MDES，否则因果声明不成立。\n\n**[AGREE] R2-W3: 跨种子稳定性偏弱（n=3 seeds）**\n\n完全同意。我在自己的审稿意见中将此列为 N1 (critical) 并做了更详细的分析。\n\n补充一个 R2 未提到的细节：Section 5.3 (p.7) 自己承认 \"strict sign consistency requires all seeds to share the same sign of Δacc(d0)\" 但仅 2/5 families 满足此条件。论文随后放宽为 \"taxonomy-level consistency\"（4/5 families agree），但这个放宽标准（CB-based aggregation rule where mean Δ ≥ 1pp 即算 non-zero）本身降低了分类精度。当一个 taxonomy 需要通过放宽一致性标准才能显示 \"stable\" 时，这恰好印证了 R2 的担忧。\n\n**[AGREE with nuance] R2-W4: Algorithm 1 硬编码阈值缺乏充分 justification**\n\n部分同意。Algorithm 1 (p.4) 确实使用了多个阈值（τ for significance, r for recovery ratio, 以及 mid-trajectory volatility check 的 δ_max 等）。Appendix K (Table 9) 报告 \"30/30 model-seed-threshold combinations\" 全部通过，但这是粗粒度的 pass/fail 报告，缺乏 sensitivity curve 展示分类如何随阈值连续变化。\n\n但我认为严重程度应低于 R2 的评估。理由：(1) Table 9 的 30 种组合覆盖了 τ ∈ {0.5, 0.75, 1.0, 1.25, 1.5, 2.0} × r ∈ {1, 1.4, 5, 6, 7} pp，这是一个合理的 grid；(2) 论文的分类主要用 direction（sign of mean Δ）作为 primary criterion（Section 3.4: \"adopts direction as the primary taxonomy criterion\"），阈值仅影响边缘 case。添加一条 sensitivity curve（classification label vs τ for each family）即可解决此问题，不需要重新设计算法。\n\n---\n\n## Minor\n\n**[AGREE] R2-M1**: \"pp\" (percentage points) 确实在 Abstract 首次出现时未定义。应在首次使用时括号注明。\n\n**[AGREE] R2-M2**: Section 5.2 (p.6) 中 \"Gemma-2 excluded due to catastrophic forgetting\" 确实出现突然。建议在首次提及时简要说明原因或指向 Appendix。\n\n**[REBUT] R2-M3**: Limitations 10 个点可精简至 4-5 个。\n\n不同意。EMNLP 2026 要求 Limitations 章节必须存在但不计入页数。当前 Limitations（p.9）覆盖了 scale ceiling、seed sensitivity、cross-seed analysis、ecological validity、format sensitivity、calibration quality 等多个维度，且每点仅 1-2 句话。对于一篇方法论论文，全面列出局限性是负责任的做法。真正的问题不是 Limitations 太长，而是 R2-W1 指出的 Section 6 正文超页——应压缩 Section 6 而非 Limitations。\n\n**[AGREE] R2-M4**: 引用年份问题。我的 reference verification 也发现了 holland_1993_dif 和 lord_1980_irt 的年份不匹配（可能是再版 vs 原版）。应统一为原版年份并核实。\n\n**[AGREE] R2-M5**: Figure 1 浮动体位置应确认不违反 ACL 模板的 float 规范。\n\n---\n\n## Missing References\n\n**[AGREE]** Golchin & Surdeanu (2024) \"Time Travel in LLMs\" 是直接相关的 contamination detection 工作，应在 Related Work 的 contamination detection 段落中引用。\n\n**[AGREE]** Sainz et al. (2023) 的 per-benchmark contamination measurement 与本文的 per-benchmark analysis 直接相关。\n\n**[AGREE]** Yang et al. (2023) rephrased samples — 我在自己的审稿意见中也建议了此引用。\n\n---\n\n## 新颖性评估回应\n\nR2 将论文新颖性定位为 \"实验范式而非方法论\"，我部分不同意。\n\n2PL+γ 模型引入 continuous contamination covariate 到 explanatory IRT 框架，在方法论上确实有创新——这不是简单地将现有方法应用到新数据，而是设计了一个新的统计模型来量化 contamination 的 item-level 效应。RRF multi-signal fusion 虽然借用了 IR 技术，但其在 contamination detection 领域的应用和与 IRT 的结合是原创的。\n\n然而 R2 的判断——\"Global modulation finding 最强\"——我同意。如果 DiD 的 power 问题能解决（增加 seeds 或做 power analysis），这个发现本身足以支撑 Conference 接收。\n\n**总结**：R2 的审稿意见整体准确且建设性。N1（taxonomy 泛化性）和 W1（页数超标）是需要作者认真回应的问题。W2 和 W3 与我的 N1/N3 高度一致，交叉验证了这些问题的严重性。\n",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-21T07:37:35.691066+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4017
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-21T07:37:40.773460+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-21T07:37:40.824030+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 384 · 2026-05-21T07:37:48.217110+00:00_

已提交对 Reviewer 2 的逐条回应。总结：

- **N1 (taxonomy 泛化性)**: AGREE，但指出 Table 1 实际有 5 个模型且 Benefit 跨 2 个家族，严重程度需修正
- **N2 (Han et al. 差异化)**: AGREE 需加强论证，但 REBUT 要求实现为 baseline（两种方法 output 不直接可比）
- **W1 (页数超标)**: AGREE，确认正文约 8.4-8.5 页，Section 6 需大幅压缩
- **W2 (DiD power)**: AGREE，与我的 N3 完全一致
- **W3 (n=3 seeds)**: AGREE，与我的 N1 完全一致
- **W4 (硬编码阈值)**: 部分 AGREE，但严重程度低于 R2 评估
- **M3 (Limitations 长度)**: REBUT——问题在于 Section 6 超页，而非 Limitations 太长
- 其余 Minor 和 Missing References 均 AGREE

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 15

## Round 15

56 recorded events


### User

_source line 385 · 2026-05-21T15:55:30.986753+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**

### 论文信息
- **标题**: "Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families"
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf`

### Venue 要求
- **Venue**: EMNLP 2026 (ARR May cycle)
- **Deadline**: 2026-05-25
- **格式**: ACL 模板，Long paper，正文 ≤8 页，参考文献不限
- **Limitations**: 必需章节（不计入页数）
- **匿名**: Double-blind
- **评分标准 (Overall Assessment)**: 5=Consider for Award（约前2.5%），4.5=Borderline Award，4=Conference（可被主会议接收），3.5=Borderline Conference，3=Findings（可被Findings接收），2.5=Borderline Findings，2=Resubmit next cycle，1.5=Resubmit after next cycle，1=Do not resubmit

### 你的审查重点

请从以下角度严格审查：

1. **方法论严谨性**：
   - IRT 模型的设定是否合理？参数可识别性是否有保证？
   - 贝叶斯推断过程是否正确（先验选择、MCMC 收敛诊断、后验分析）？
   - 统计检验是否恰当？效应量是否有实际意义（而非仅统计显著）？
   - 是否存在混淆变量、选择偏差、或循环论证？

2. **实验设计**：
   - 实验覆盖的模型家族、规模、benchmark 是否足够支撑论文的 claim？
   - 控制变量是否充分？ablation 是否完整？
   - 训练细节（超参数、随机种子、数据划分）是否可复现？
   - 负面结果（如 gamma 不显著）是否被诚实报告？

3. **统计分析**：
   - 表格和图表中的数字是否一致？
   - 置信区间/可信区间是否正确报告？
   - 多重比较校正是否必要且已执行？
   - dose-response 关系的建模是否有替代方案被考虑？

请给出结构化审稿意见：Summary → Strengths → Weaknesses (按严重程度排列) → Questions → Minor Issues → Score (使用 EMNLP 评分标准)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-21T15:55:40.930275+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-21T15:55:40.980874+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-21T15:55:45.771486+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 389 · 2026-05-21T15:55:46.676897+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf",
  "pages": "1-8",
  "project": "contamcal-irt-calibration",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf",
    "pages": "1-8",
    "project": "contamcal-irt-calibration",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 390 · 2026-05-21T15:55:55.466540+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility. Conference recommendations may also consi
…[truncated 1256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9695
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-21T15:55:56.472422+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 437.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 407.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 428.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.8}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.8}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9795
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-21T15:56:02.804455+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-21T15:56:02.804880+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-21T15:56:03.306861+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 395 · 2026-05-21T15:56:03.811487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 396 · 2026-05-21T15:56:04.316900+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool call

_source line 397 · 2026-05-21T15:56:04.317338+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 398 · 2026-05-21T15:56:04.670654+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-21T15:56:05.072960+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-21T15:56:13.339995+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need: 1) All numbered questions/dimensions, 2) The scale for each (e.g., 1-5), 3) What each score level means, 4) Any special instructions for reviewers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need: 1) All numbered questions/dimensions, 2) The scale for each (e.g., 1-5), 3) What each score level means, 4) Any special instructions for reviewers."
  }
}
```

</details>

---


### Tool call

_source line 401 · 2026-05-21T15:56:13.792120+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 402 · 2026-05-21T15:56:14.297759+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 403 · 2026-05-21T15:56:14.298288+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 404 · 2026-05-21T15:56:15.254289+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 405 · 2026-05-21T15:56:15.254759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-21T15:56:15.707474+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-21T15:56:16.012799+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 758
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-21T15:56:16.013123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-21T15:56:16.716843+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool result

_source line 410 · 2026-05-21T15:56:16.918720+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-21T15:56:19.829497+00:00_

# ACL Rolling Review Form Structure

## Scoring Dimensions

**1. Reviewer Confidence (Scale: 1-5)**
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: "Quite sure" with unlikely but possible errors
- 3: "Pretty sure, but there's a chance I missed something"
- 2: Willing to defend but "fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

**2. Soundness (Scale: 1-5 with half-point increments)**
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong with sufficient support; extras not essential
- 3: Acceptable; main claims supported with minor gaps
- 2: "Poor: Some of the main claims are not sufficiently supported"
- 1: "Major Issues" warranting rejection or irrelevance

**3. Excitement (Scale: 1-5 with half-point increments)**
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: Would mention to colleagues or attend presentation
- 3: Might mention or attend if time permits
- 2: Doesn't resonate personally but may appeal broadly
- 1: "Not Exciting" and unlikely relevant to community

**4. Overall Assessment (Scale: 1-5 with half-point increments)**
- 5: Consider for award consideration
- 4: Conference acceptance appropriate
- 3: Findings track suitable
- 2: Needs substantial revisions
- 1: Requires complete rework or lacks relevance

## Narrative Sections

- Paper Summary
- Strengths
- Weaknesses
- Comments/Suggestions/Typos
- Limitations and Societal Impact
- Ethical Concerns
- Reproducibility (Scale: 1-5)
- Datasets value (Scale: 1-5)
- Software value (Scale: 1-5)
- Author identity disclosure (Scale: 1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6489
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-21T15:56:25.656063+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf",
  "pages": "9-18",
  "project": "contamcal-irt-calibration",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf",
    "pages": "9-18",
    "project": "contamcal-irt-calibration",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-21T15:56:27.364536+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 551.6}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 556.2}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 559.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 400.2}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 441.7}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 437.1}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.6}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 371.6}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamca
…[truncated 338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1708
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-21T15:56:30.882924+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 415 · 2026-05-21T15:56:31.392464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 416 · 2026-05-21T15:56:32.246898+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1363
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-21T15:56:32.248059+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-21T15:56:32.248499+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 419 · 2026-05-21T15:56:32.750158+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 420 · 2026-05-21T15:56:33.105365+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 421 · 2026-05-21T15:56:33.105786+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 422 · 2026-05-21T15:56:33.760730+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-21T15:56:33.813617+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 707
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-21T15:56:37.779626+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-21T15:56:38.634907+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-21T15:56:38.685624+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 427 · 2026-05-21T15:56:39.139831+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 428 · 2026-05-21T15:56:39.592866+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 429 · 2026-05-21T15:56:39.593440+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 430 · 2026-05-21T15:56:40.330173+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1190
}
```

</details>

---


### Tool call

_source line 431 · 2026-05-21T15:56:40.330647+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images/main_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 432 · 2026-05-21T15:56:40.332938+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 739
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-21T15:56:40.776572+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 445
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-21T16:03:53.283878+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\"\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n**参照标准**: ACL ARR Review Form (Soundness / Excitement / Overall Assessment)\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 研究问题重要、实验设计规范、IRT 框架合理，但分类法基于 ad-hoc 算法缺乏统计建模基础，核心因果声称（架构决定脆弱性）证据不足，且 N=4 家族的样本量对分类法泛化性构成根本限制。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | IRT 方法论扎实，贝叶斯推断流程规范（R̂ < 1.01, ESS > 500, PPP），但 Algorithm 1 的阈值设定 ad hoc，统一 LoRA 配置引入未讨论的混淆 |\n| Excitement | 3.5/5 | Dose-response 框架新颖且有方法论贡献，但核心发现（不同模型不同反应）在直觉上可预期；分类法的实用价值受限于泛化性不足 |\n| Reproducibility | 4/5 | 超参数（LoRA r=16, α=32, lr=5e-5）、种子、MCMC 配置（4 chains）、收敛诊断报告充分，附录极为详尽 |\n| Reviewer Confidence | 4/5 | 熟悉 IRT、贝叶斯推断、LLM 评估方法和 DIF 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 分类法（Taxonomy）基于 ad-hoc 算法而非正式 dose-response 建模\n\n- **具体位置**：Section 3.3, Algorithm 1 (Page 5)\n- **问题**：Algorithm 1 使用多个硬编码阈值（噪声阈值 τ = 2pp, 模式阈值 n = 5, 晚期增益下限 ρ = 0.3, 饱和增益 λ = 0.5pp）将 dose-response 曲线分为 Immune / Collapse / V-Recovery / Benefit 四类。虽然 Appendix P (Table 14) 显示五个家族在\"reasonable parameter range\"内均达到 100% 分类稳定性，但该方法本质上是描述性规则分类，而非模型驱动的统计推断。药理学和毒理学中有成熟的参数化 dose-response 模型（如 sigmoidal Emax、log-logistic 4 参数模型、Hill 方程），可通过似然比检验或信息准则（AIC/BIC）在竞争模型间做正式选择。当前方法的根本缺陷是**无法量化分类的不确定性**——一个家族被标记为\"Collapse\"而不是\"V-Recovery\"的置信度是多少？当数据点在分类边界附近时（如 Qwen-7B 的 V-Recovery 与 Benefit 之间），规则分类无法给出概率性判断。\n- **为什么影响接收**：分类法是论文三大贡献之一（Contribution 1, Section 1）。如果分类法缺乏统计基础，后续基于分类的所有推论（\"架构决定脆弱性\"、\"65–70% 脆弱带\"等）都建立在不稳固的地基上。\n- **建议修改方向**：(1) 拟合参数化 dose-response 模型（如 4 参数 log-logistic）到每个家族的 accuracy-vs-dosage 曲线，通过参数比较（EC50, Hill slope, Emax）量化家族间差异；(2) 为分类结果提供不确定性度量（如 bootstrap 置信度或后验概率）；(3) 若坚持使用 Algorithm 1，至少应正式讨论为何不采用参数化 dose-response 建模，以及该选择的 trade-off。\n\n**N2** [critical] \"架构而非基线能力决定脆弱性\"的因果声称证据不足\n\n- **具体位置**：Section 6 第一段 (\"architecture, not baseline ability alone, determines contamination vulnerability\")；Section 1, Contribution 1；Abstract (\"showing that architecture rather than baseline ability determines vulnerability\")\n- **问题**：该因果声称主要基于两条证据：(a) OLMo-2 (53.8% MMLU) 表现为 Benefit，与基线更高的 Qwen-7B (66.1%) 的 V-Recovery 不同，说明基线能力不是唯一决定因素；(b) 在 Qwen2.5 家族内部，14B (69.4%) 比 7B (66.1%) 更脆弱，但前者基线更高。然而，**不同模型家族在\"架构\"之外存在大量混淆变量**：预训练数据的分布和规模、tokenizer 词表大小和覆盖率、预训练目标（如 Phi-4 的合成数据策略）、训练步数和学习率调度、数据去重和质量过滤策略。论文无法将这些因素与架构本身（attention 类型、层数、FFN 结构等）分离。即使在 Qwen2.5 内部，14B 与 7B 可能使用了不同的预训练数据量和训练步数，而非仅仅是参数量的差异。\n- **为什么影响接收**：这是论文的**标题级声称**——\"Across Model Families\"暗示家族间差异的根源已被识别。如果因果推断不成立，论文的贡献定位需要降级。\n- **建议修改方向**：(1) 将 \"architecture determines\" 弱化为 \"baseline ability alone does not determine\"，这是数据能支撑的结论；(2) 在 Section 6 中系统列出无法排除的混淆因素；(3) 避免在 Abstract 和 Title 中暗示因果关系。当前发现是重要的**描述性**结果（不同家族确实表现不同），不需要因果包装来保持价值。\n\n**N3** [critical] N=4 训练家族对分类法泛化性的根本限制\n\n- **具体位置**：Section 4.1 (实验设置), Section 5.1 (Cross-family results), Table 1\n- **问题**：论文从 4 个训练家族（Phi-4, Qwen-14B, OLMo-2, Qwen-7B/Gemma-2）中归纳出 4 类 dose-response 模式，并用 1 个 held-out 家族（LLaMA-3.1-8B）验证。关键问题：\n  - **4 类模式恰好由 4 个家族产生**：每种模式仅由 1 个家族代表（Immune→Phi-4, Collapse→Qwen-14B, V-Recovery→OLMo-2/Qwen-7B, Benefit→Gemma-2）。无法排除这些模式是特定于具体模型的 idiosyncratic 行为，而非真正可泛化的\"类型\"。\n  - **Held-out 验证仅覆盖一种模式**：LLaMA-3.1-8B 被分类为 Immune，但 Collapse、V-Recovery、Benefit 三种模式均无独立验证。\n  - **规模范围有限**：所有模型 ≤14B。对 70B+ 模型的适用性完全未知，而这恰恰是实践中污染检测最重要的场景。\n  - **仅覆盖 LoRA SFT**：real-world 污染更多发生在 pre-training 阶段（web crawl 泄露），与 LoRA SFT 注入的机制可能有本质差异。Limitations 中提到了这一点，但未讨论其对分类法泛化性的影响。\n- **为什么影响接收**：分类法的学术价值在于泛化性。一个 N=4 的归纳、N=1 的验证，很难让读者相信这是通用的类型学而非实验条件下的巧合。\n- **建议修改方向**：(1) 将分类法明确定位为\"初步观察/假说生成\"而非\"已验证的类型学\"；(2) 在 Section 6 和 Limitations 中清晰讨论 N=4 的局限性和泛化风险；(3) 具体列出哪些额外实验能增强泛化性（如更多家族、更大模型、full fine-tuning、pre-training 注入等）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 统一 LoRA 配置（r=16）引入的未讨论混淆\n\n- **具体位置**：Section 4.1 (\"unified LoRA configuration (r = 16, α = 32, lr = 5 × 10⁻⁵, bf16)\")\n- **问题**：所有模型使用相同 LoRA 超参（r=16），但 LoRA 的相对表达能力与模型参数量成反比。对 14B 模型，r=16 的参数占比远小于对 7B 模型。这意味着\"treatment strength\"在不同规模模型间不等价。Phi-4 14B 的 Immune 模式可能部分源于 LoRA 容量不足以实现有效 memorization——虽然 Qwen-14B 同为 14B 且表现为 Collapse 可以部分反驳这一假说，但两者架构差异可能导致 LoRA 对不同 layer 的影响效率不同。论文完全未讨论这一混淆。\n- **建议**：(1) 在 Limitations 中讨论 LoRA 容量作为混淆因素；(2) 理想情况下补充 r∈{8, 16, 32, 64} 的消融实验或至少在一个家族上测试。\n\n**W2** [warning] DID 零结果的功效限制在正文中表述不够审慎\n\n- **具体位置**：Section 5.4, Table 3, Appendix N (MDES 1.25–2.05pp)\n- **问题**：正文 Section 5.4 标题为 \"No detectable item-specific memorization\"，但 Appendix N 的 MDES 分析显示最小可检测效应量为 1.25pp（MMLU at d025, 80% power）至 2.05pp。这意味着 ≤1.25pp 的 item-specific 效应无法被排除。论文在 Section 5.4 末尾提到\"ARC's limited power precludes the same conclusions there\"，但对 MMLU 的功效限制在正文中未充分说明。将\"no detectable memorization\"作为 Section 标题和 Contribution 2 强调，容易被误读为\"memorization does not exist\"而非\"we lack power to detect small effects\"。\n- **建议**：(1) 将 Section 5.4 标题改为更审慎的表述（如 \"Limited Evidence for Item-Specific Memorization\"）；(2) 在正文中明确报告 MDES 数值而非仅放在附录；(3) 讨论 1.25pp 的 item-specific 效应在实践中是否重要。\n\n**W3** [warning] 曝光分数（s_ij）的分类性能未定量报告\n\n- **具体位置**：Section 3.1 (Stage 1: Multi-Signal Exposure Mapping), Section 5.6 (Detection Signal Failure Modes)\n- **问题**：Stage 1 构造的曝光分数 s_ij 通过 RRF 融合 4 个信号（S1 embedding similarity, S2 token-level surprisal, S3 contamination gap, S4 self-critique），直接作为协变量进入 IRT 模型。s_ij 的测量误差会传递到 γ 的估计中（衰减偏差/attenuation bias）。但论文未报告 s_ij 在已知污染标签（d000 vs. d100 的 item membership）下的分类性能指标（如 ROC-AUC、precision-recall）。Section 5.6 定性讨论了 Min-K%++ 的失败模式，Table 4 比较了不同方法的 MAE，但缺乏 s_ij 本身作为二分类器的系统评估。\n- **建议**：在附录中补充 s_ij 在 d005/d025/d050/d100 下区分 treated vs. untreated items 的 AUC 及 PR 曲线，以便读者评估协变量质量。\n\n**W4** [warning] \"65–70% MMLU 基线脆弱带\"声称的数据支撑薄弱\n\n- **具体位置**：Section 5.1 第二段 (\"Contamination vulnerability concentrates in the 65–70% MMLU baseline band\"), Abstract, Figure 1 caption\n- **问题**：该声称基于 5 个模型的数据点：Phi-4 (76.4%) Immune, Qwen-14B (69.4%) Collapse, Qwen-7B (66.1%) V-Recovery, OLMo-2 (~64%) V-Recovery, Gemma-2 (~62%) Benefit。实际数据显示的是\"76% 以上免疫，62–69% 受不同方式影响\"，而非精确的\"65–70% band\"。此外 Gemma-2 在 ~62% 显示 Benefit（明显受影响），但论文将 62% 描述为\"extreme baseline\"with \"limited sensitivity\"，这与 Benefit 分类矛盾。用 5 个数据点声称一个精确百分比区间是对稀疏数据的过度拟合。\n- **建议**：弱化为定性描述（如 \"models with moderate baseline accuracy appear more vulnerable than those with very high baselines\"），避免给出看似精确但实际上 under-determined 的百分比区间。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 3.2 中 2PL+γ 的先验分布仅以\"priors\"一词一带而过，正文中应至少给出 θ 和 γ 的先验形式。Appendix 中有但读者不应被迫翻附录来评估模型设定的合理性。\n- Figure 1: 两个子图 y 轴范围不同（MMLU ~60–80%, ARC-Challenge ~55–80%），虽然合理但两条曲线的视觉斜率不直接可比。建议在 caption 中提醒读者注意 y 轴差异。\n- Table 2 (page 7): \"Con.\" 列（consistency）的定义（\"25 strict sign consistency on …\"）较难直接从表中理解，建议改用更自解释的列名或在表注中展开。\n- Limitations 中列出了 LoRA vs. pre-training 污染的差异，但未讨论 instruction tuning vs. continued pre-training 这两种常见污染路径在效应机制上的差异，建议补充一句。\n- Section 5.2 (Cross-Benchmark Transfer): GSM8K 分析排除了 Qwen-7B（due to CvT collapse）后仅剩 4 个家族，进一步削弱了跨 benchmark 结论的泛化性。\n- Section 5.5 (Calibration Quality): Table 4 将 ContamCal 与 6 个 baseline 比较，但 baseline 选择中 B5-Emperor 引用的是 Sun et al. (2025) 的缓解策略而非校准方法，两者目标不完全对齐，比较公平性值得说明。\n\n---\n\n## 主要优势\n\n1. **研究问题定义清晰且有实际价值**：现有文献多做二元（污染/干净）比较，本文首次系统建模连续 dose-response 关系，填补了重要方法论空白。\n2. **实验设计严谨**：控制 SFT 注入 + 已知 ground truth + 多种子 + 多家族 + held-out 验证 + 跨 benchmark 迁移——这是为数不多遵循了实验因果推断范式的 LLM 评估研究。\n3. **IRT 框架的引入恰当且技术实施扎实**：将测量理论（2PL+γ, explanatory DIF）与 LLM 评估结合是有意义的方法论贡献。贝叶斯推断提供了校准的可信区间，收敛诊断（R̂, ESS, PPP）报告充分。\n4. **诚实报告零结果和局限**：DID 非显著（Section 5.4）、ARC 功效不足、cross-seed CI 宽度等不利结果均如实报告，未做选择性呈现。\n5. **附录极为详尽**（10 页）：涵盖收敛诊断（Appendix I）、功效分析（Appendix N）、阈值鲁棒性（Appendix P）、domain 分解（Appendix Q）、4PL 扩展（Appendix G）等，达到了高标准的可复现性。\n6. **跨 benchmark 迁移分析增加深度**：GSM8K 上发现的方向性反转（Qwen-7B directional reversal）和多模式转移模式（null, consistent, directional reversal）提供了超越单一 benchmark 的见解。\n\n---\n\n## 问题（需要作者回应）\n\nQ1: γ 参数的识别来源——是主要从同一模型内不同 item 的 s_ij 变异中识别（within-model cross-item），还是从不同 dosage 配置间的 s_ij 分布差异中识别（cross-dosage）？如果是后者，θ 和 γ 的分离依赖什么排除限制？\n\nQ2: Algorithm 1 产出的分类是否对输入数据的 noise 敏感？如果在每个 dosage 下的 accuracy 加上 ±1pp 的均匀噪声，有多少家族的分类会发生变化？\n\nQ3: 论文将 Phi-4 的 Immune 归因于架构，但 Phi-4 以大量使用合成数据（synthetic data）进行预训练著称。是否考虑过 Phi-4 的 immunity 更可能源于预训练数据策略而非架构本身？\n\nQ4: 如果将 LoRA rank 从 16 提升到 64（增加记忆容量），Phi-4 的分类是否可能从 Immune 变为其他模式？这对\"架构决定脆弱性\"的结论有何影响？\n\n---\n\n**总结**：论文在重要问题上做了扎实的工作，IRT 框架和控制实验设计是明确的贡献。主要问题集中在三点：(1) 分类法需要更强的统计基础，(2) 因果声称需要降级为描述性发现，(3) 泛化性限制需要更坦诚地讨论。如果三个 Must-Fix 得到充分处理（主要是文本层面的弱化声称 + 方法论讨论的补充），本文具备 Conference/Findings 接收的潜力。",
  "reviewer_id": "1",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families\"\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n**参照标准**: ACL ARR Review Form (Soundness / Excitement / Overall Assessment)\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 研究问题重要、实验设计规范、IRT 框架合理，但分类法基于 ad-hoc 算法缺乏统计建模基础，核心因果声称（架构决定脆弱性）证据不足，且 N=4 家族的样本量对分类法泛化性构成根本限制。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | IRT 方法论扎实，贝叶斯推断流程规范（R̂ < 1.01, ESS > 500, PPP），但 Algorithm 1 的阈值设定 ad hoc，统一 LoRA 配置引入未讨论的混淆 |\n| Excitement | 3.5/5 | Dose-response 框架新颖且有方法论贡献，但核心发现（不同模型不同反应）在直觉上可预期；分类法的实用价值受限于泛化性不足 |\n| Reproducibility | 4/5 | 超参数（LoRA r=16, α=32, lr=5e-5）、种子、MCMC 配置（4 chains）、收敛诊断报告充分，附录极为详尽 |\n| Reviewer Confidence | 4/5 | 熟悉 IRT、贝叶斯推断、LLM 评估方法和 DIF 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 分类法（Taxonomy）基于 ad-hoc 算法而非正式 dose-response 建模\n\n- **具体位置**：Section 3.3, Algorithm 1 (Page 5)\n- **问题**：Algorithm 1 使用多个硬编码阈值（噪声阈值 τ = 2pp, 模式阈值 n = 5, 晚期增益下限 ρ = 0.3, 饱和增益 λ = 0.5pp）将 dose-response 曲线分为 Immune / Collapse / V-Recovery / Benefit 四类。虽然 Appendix P (Table 14) 显示五个家族在\"reasonable parameter range\"内均达到 100% 分类稳定性，但该方法本质上是描述性规则分类，而非模型驱动的统计推断。药理学和毒理学中有成熟的参数化 dose-response 模型（如 sigmoidal Emax、log-logistic 4 参数模型、Hill 方程），可通过似然比检验或信息准则（AIC/BIC）在竞争模型间做正式选择。当前方法的根本缺陷是**无法量化分类的不确定性**——一个家族被标记为\"Collapse\"而不是\"V-Recovery\"的置信度是多少？当数据点在分类边界附近时（如 Qwen-7B 的 V-Recovery 与 Benefit 之间），规则分类无法给出概率性判断。\n- **为什么影响接收**：分类法是论文三大贡献之一（Contribution 1, Section 1）。如果分类法缺乏统计基础，后续基于分类的所有推论（\"架构决定脆弱性\"、\"65–70% 脆弱带\"等）都建立在不稳固的地基上。\n- **建议修改方向**：(1) 拟合参数化 dose-response 模型（如 4 参数 log-logistic）到每个家族的 accuracy-vs-dosage 曲线，通过参数比较（EC50, Hill slope, Emax）量化家族间差异；(2) 为分类结果提供不确定性度量（如 bootstrap 置信度或后验概率）；(3) 若坚持使用 Algorithm 1，至少应正式讨论为何不采用参数化 dose-response 建模，以及该选择的 trade-off。\n\n**N2** [critical] \"架构而非基线能力决定脆弱性\"的因果声称证据不足\n\n- **具体位置**：Section 6 第一段 (\"architecture, not baseline ability alone, determines contamination vulnerability\")；Section 1, Contribution 1；Abstract (\"showing that architecture rather than baseline ability determines vulnerability\")\n- **问题**：该因果声称主要基于两条证据：(a) OLMo-2 (53.8% MMLU) 表现为 Benefit，与基线更高的 Qwen-7B (66.1%) 的 V-Recovery 不同，说明基线能力不是唯一决定因素；(b) 在 Qwen2.5 家族内部，14B (69.4%) 比 7B (66.1%) 更脆弱，但前者基线更高。然而，**不同模型家族在\"架构\"之外存在大量混淆变量**：预训练数据的分布和规模、tokenizer 词表大小和覆盖率、预训练目标（如 Phi-4 的合成数据策略）、训练步数和学习率调度、数据去重和质量过滤策略。论文无法将这些因素与架构本身（attention 类型、层数、FFN 结构等）分离。即使在 Qwen2.5 内部，14B 与 7B 可能使用了不同的预训练数据量和训练步数，而非仅仅是参数量的差异。\n- **为什么影响接收**：这是论文的**标题级声称**——\"Across Model Families\"暗示家族间差异的根源已被识别。如果因果推断不成立，论文的贡献定位需要降级。\n- **建议修改方向**：(1) 将 \"architecture determines\" 弱化为 \"baseline ability alone does not determine\"，这是数据能支撑的结论；(2) 在 Section 6 中系统列出无法排除的混淆因素；(3) 避免在 Abstract 和 Title 中暗示因果关系。当前发现是重要的**描述性**结果（不同家族确实表现不同），不需要因果包装来保持价值。\n\n**N3** [critical] N=4 训练家族对分类法泛化性的根本限制\n\n- **具体位置**：Section 4.1 (实验设置), Section 5.1 (Cross-family results), Table 1\n- **问题**：论文从 4 个训练家族（Phi-4, Qwen-14B, OLMo-2, Qwen-7B/Gemma-2）中归纳出 4 类 dose-response 模式，并用 1 个 held-out 家族（LLaMA-3.1-8B）验证。关键问题：\n  - **4 类模式恰好由 4 个家族产生**：每种模式仅由 1 个家族代表（Immune→Phi-4, Collapse→Qwen-14B, V-Recovery→OLMo-2/Qwen-7B, Benefit→Gemma-2）。无法排除这些模式是特定于具体模型的 idiosyncratic 行为，而非真正可泛化的\"类型\"。\n  - **Held-out 验证仅覆盖一种模式**：LLaMA-3.1-8B 被分类为 Immune，但 Collapse、V-Recovery、Benefit 三种模式均无独立验证。\n  - **规模范围有限**：所有模型 ≤14B。对 70B+ 模型的适用性完全未知，而这恰恰是实践中污染检测最重要的场景。\n  - **仅覆盖 LoRA SFT**：real-world 污染更多发生在 pre-training 阶段（web crawl 泄露），与 LoRA SFT 注入的机制可能有本质差异。Limitations 中提到了这一点，但未讨论其对分类法泛化性的影响。\n- **为什么影响接收**：分类法的学术价值在于泛化性。一个 N=4 的归纳、N=1 的验证，很难让读者相信这是通用的类型学而非实验条件下的巧合。\n- **建议修改方向**：(1) 将分类法明确定位为\"初步观察/假说生成\"而非\"已验证的类型学\"；(2) 在 Section 6 和 Limitations 中清晰讨论 N=4 的局限性和泛化风险；(3) 具体列出哪些额外实验能增强泛化性（如更多家族、更大模型、full fine-tuning、pre-training 注入等）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 统一 LoRA 配置（r=16）引入的未讨论混淆\n\n- **具体位置**：Section 4.1 (\"unified LoRA configuration (r = 16, α = 32, lr = 5 × 10⁻⁵, bf16)\")\n- **问题**：所有模型使用相同 LoRA 超参（r=16），但 LoRA 的相对表达能力与模型参数量成反比。对 14B 模型，r=16 的参数占比远小于对 7B 模型。这意味着\"treatment strength\"在不同规模模型间不等价。Phi-4 14B 的 Immune 模式可能部分源于 LoRA 容量不足以实现有效 memorization——虽然 Qwen-14B 同为 14B 且表现为 Collapse 可以部分反驳这一假说，但两者架构差异可能导致 LoRA 对不同 layer 的影响效率不同。论文完全未讨论这一混淆。\n- **建议**：(1) 在 Limitations 中讨论 LoRA 容量作为混淆因素；(2) 理想情况下补充 r∈{8, 16, 32, 64} 的消融实验或至少在一个家族上测试。\n\n**W2** [warning] DID 零结果的功效限制在正文中表述不够审慎\n\n- **具体位置**：Section 5.4, Table 3, Appendix N (MDES 1.25–2.05pp)\n- **问题**：正文 Section 5.4 标题为 \"No detectable item-specific memorization\"，但 Appendix N 的 MDES 分析显示最小可检测效应量为 1.25pp（MMLU at d025, 80% power）至 2.05pp。这意味着 ≤1.25pp 的 item-specific 效应无法被排除。论文在 Section 5.4 末尾提到\"ARC's limited power precludes the same conclusions there\"，但对 MMLU 的功效限制在正文中未充分说明。将\"no detectable memorization\"作为 Section 标题和 Contribution 2 强调，容易被误读为\"memorization does not exist\"而非\"we lack power to detect small effects\"。\n- **建议**：(1) 将 Section 5.4 标题改为更审慎的表述（如 \"Limited Evidence for Item-Specific Memorization\"）；(2) 在正文中明确报告 MDES 数值而非仅放在附录；(3) 讨论 1.25pp 的 item-specific 效应在实践中是否重要。\n\n**W3** [warning] 曝光分数（s_ij）的分类性能未定量报告\n\n- **具体位置**：Section 3.1 (Stage 1: Multi-Signal Exposure Mapping), Section 5.6 (Detection Signal Failure Modes)\n- **问题**：Stage 1 构造的曝光分数 s_ij 通过 RRF 融合 4 个信号（S1 embedding similarity, S2 token-level surprisal, S3 contamination gap, S4 self-critique），直接作为协变量进入 IRT 模型。s_ij 的测量误差会传递到 γ 的估计中（衰减偏差/attenuation bias）。但论文未报告 s_ij 在已知污染标签（d000 vs. d100 的 item membership）下的分类性能指标（如 ROC-AUC、precision-recall）。Section 5.6 定性讨论了 Min-K%++ 的失败模式，Table 4 比较了不同方法的 MAE，但缺乏 s_ij 本身作为二分类器的系统评估。\n- **建议**：在附录中补充 s_ij 在 d005/d025/d050/d100 下区分 treated vs. untreated items 的 AUC 及 PR 曲线，以便读者评估协变量质量。\n\n**W4** [warning] \"65–70% MMLU 基线脆弱带\"声称的数据支撑薄弱\n\n- **具体位置**：Section 5.1 第二段 (\"Contamination vulnerability concentrates in the 65–70% MMLU baseline band\"), Abstract, Figure 1 caption\n- **问题**：该声称基于 5 个模型的数据点：Phi-4 (76.4%) Immune, Qwen-14B (69.4%) Collapse, Qwen-7B (66.1%) V-Recovery, OLMo-2 (~64%) V-Recovery, Gemma-2 (~62%) Benefit。实际数据显示的是\"76% 以上免疫，62–69% 受不同方式影响\"，而非精确的\"65–70% band\"。此外 Gemma-2 在 ~62% 显示 Benefit（明显受影响），但论文将 62% 描述为\"extreme baseline\"with \"limited sensitivity\"，这与 Benefit 分类矛盾。用 5 个数据点声称一个精确百分比区间是对稀疏数据的过度拟合。\n- **建议**：弱化为定性描述（如 \"models with moderate baseline accuracy appear more vulnerable than those with very high baselines\"），避免给出看似精确但实际上 under-determined 的百分比区间。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 3.2 中 2PL+γ 的先验分布仅以\"priors\"一词一带而过，正文中应至少给出 θ 和 γ 的先验形式。Appendix 中有但读者不应被迫翻附录来评估模型设定的合理性。\n- Figure 1: 两个子图 y 轴范围不同（MMLU ~60–80%, ARC-Challenge ~55–80%），虽然合理但两条曲线的视觉斜率不直接可比。建议在 caption 中提醒读者注意 y 轴差异。\n- Table 2 (page 7): \"Con.\" 列（consistency）的定义（\"25 strict sign consistency on …\"）较难直接从表中理解，建议改用更自解释的列名或在表注中展开。\n- Limitations 中列出了 LoRA vs. pre-training 污染的差异，但未讨论 instruction tuning vs. continued pre-training 这两种常见污染路径在效应机制上的差异，建议补充一句。\n- Section 5.2 (Cross-Benchmark Transfer): GSM8K 分析排除了 Qwen-7B（due to CvT collapse）后仅剩 4 个家族，进一步削弱了跨 benchmark 结论的泛化性。\n- Section 5.5 (Calibration Quality): Table 4 将 ContamCal 与 6 个 baseline 比较，但 baseline 选择中 B5-Emperor 引用的是 Sun et al. (2025) 的缓解策略而非校准方法，两者目标不完全对齐，比较公平性值得说明。\n\n---\n\n## 主要优势\n\n1. **研究问题定义清晰且有实际价值**：现有文献多做二元（污染/干净）比较，本文首次系统建模连续 dose-response 关系，填补了重要方法论空白。\n2. **实验设计严谨**：控制 SFT 注入 + 已知 ground truth + 多种子 + 多家族 + held-out 验证 + 跨 benchmark 迁移——这是为数不多遵循了实验因果推断范式的 LLM 评估研究。\n3. **IRT 框架的引入恰当且技术实施扎实**：将测量理论（2PL+γ, explanatory DIF）与 LLM 评估结合是有意义的方法论贡献。贝叶斯推断提供了校准的可信区间，收敛诊断（R̂, ESS, PPP）报告充分。\n4. **诚实报告零结果和局限**：DID 非显著（Section 5.4）、ARC 功效不足、cross-seed CI 宽度等不利结果均如实报告，未做选择性呈现。\n5. **附录极为详尽**（10 页）：涵盖收敛诊断（Appendix I）、功效分析（Appendix N）、阈值鲁棒性（Appendix P）、domain 分解（Appendix Q）、4PL 扩展（Appendix G）等，达到了高标准的可复现性。\n6. **跨 benchmark 迁移分析增加深度**：GSM8K 上发现的方向性反转（Qwen-7B directional reversal）和多模式转移模式（null, consistent, directional reversal）提供了超越单一 benchmark 的见解。\n\n---\n\n## 问题（需要作者回应）\n\nQ1: γ 参数的识别来源——是主要从同一模型内不同 item 的 s_ij 变异中识别（within-model cross-item），还是从不同 dosage 配置间的 s_ij 分布差异中识别（cross-dosage）？如果是后者，θ 和 γ 的分离依赖什么排除限制？\n\nQ2: Algorithm 1 产出的分类是否对输入数据的 noise 敏感？如果在每个 dosage 下的 accuracy 加上 ±1pp 的均匀噪声，有多少家族的分类会发生变化？\n\nQ3: 论文将 Phi-4 的 Immune 归因于架构，但 Phi-4 以大量使用合成数据（synthetic data）进行预训练著称。是否考虑过 Phi-4 的 immunity 更可能源于预训练数据策略而非架构本身？\n\nQ4: 如果将 LoRA rank 从 16 提升到 64（增加记忆容量），Phi-4 的分类是否可能从 Immune 变为其他模式？这对\"架构决定脆弱性\"的结论有何影响？\n\n---\n\n**总结**：论文在重要问题上做了扎实的工作，IRT 框架和控制实验设计是明确的贡献。主要问题集中在三点：(1) 分类法需要更强的统计基础，(2) 因果声称需要降级为描述性发现，(3) 泛化性限制需要更坦诚地讨论。如果三个 Must-Fix 得到充分处理（主要是文本层面的弱化声称 + 方法论讨论的补充），本文具备 Conference/Findings 接收的潜力。",
    "reviewer_id": "1",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-21T16:03:57.264975+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3981
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-21T16:04:05.171533+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-21T16:04:05.375019+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-21T16:04:09.648814+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-21T16:04:09.699500+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 440 · 2026-05-21T16:04:19.192527+00:00_

Round 1 审稿完成。评分 **Overall 3.5 (Borderline Conference)**，核心问题三点：

1. **N1**: Algorithm 1 分类法缺乏正式 dose-response 统计建模基础，无法量化分类不确定性
2. **N2**: "架构决定脆弱性"的因果声称超出了数据能支撑的范围（存在大量未控制的混淆变量），应降级为描述性发现
3. **N3**: N=4 家族归纳 + N=1 验证的样本量对分类法泛化性构成根本限制

四个 Should-Fix：统一 LoRA 配置的混淆、DID 零结果功效不足的表述、曝光分数分类性能未报告、"65–70% 脆弱带"声称过于精确。

优势方面：控制实验设计严谨、IRT 贝叶斯框架实施扎实、零结果诚实报告、附录详尽。若三个 Must-Fix 得到处理（主要是弱化声称 + 补充方法论讨论），具备 Conference/Findings 接收潜力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1"
}
```

</details>

---


## Round 16

## Round 16

16 recorded events


### User

_source line 441 · 2026-05-21T16:04:58.106544+00:00_

[Round 1 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 — Round 1 审稿意见

### 总体评分
**Overall**: 3.5 — Borderline Conference

### Must-Fix 问题

**N1** [critical] LoRA SFT 注入的生态效度根本性不足
- 具体位置：Section 4.1, Limitations (p.9)
- 问题：所有污染实验均通过 LoRA SFT 注入基准题目（Section 4.1: "unified LoRA configuration"），但真实世界的 benchmark contamination 发生在预训练阶段，与 SFT 微调在学习机制上截然不同。SFT 直接优化答案匹配，而预训练中的偶然暴露是隐式的。论文在 Limitations 中仅一句话提及，但这不是边缘局限——它直接影响 4 个 dose-response pattern 的推断效度。Schaeffer et al. (2026) 已通过预训练污染展示了不同的 dose-response 关系，其结论与本文基于 SFT 的发现可能存在本质差异。
- 为什么影响接收：如果 dose-response pattern 是 LoRA SFT 的 artifact，论文核心贡献的实际应用价值大幅降低。

**N2** [critical] 分类法理论基础薄弱，泛化性不足
- 具体位置：Algorithm 1 (p.5), Section 5.1 (p.6), Table 1 (p.6)
- 问题：四分类法完全基于经验归纳，依赖任意阈值（τ=2pp, n=5, ρ=0.3, λ=0.5pp）。Appendix P (Table 14) 的敏感性测试范围很窄。更关键的是仅 4 个独立家族，V-recovery 只在 Qwen-7B 上观察到（n=1）。
- 为什么影响接收：n=1 的 pattern 不足以构成 robust taxonomy class；4 个家族不支撑泛化 claim。

### Should-Fix 问题

**W1** [warning] "Dose-response" 框架缺乏正式的 dose-response 建模
- 论文借用药理学术语但没有拟合参数化曲线（Hill equation / sigmoid E_max model），仅在 5 个离散剂量上做分类比较。

**W2** [warning] 与 Schaeffer et al. (2026) 和 Han et al. (2026) 的关系讨论不充分
- 这两篇是最直接的竞争/互补工作，但前者仅在 Conclusion 一句话提及，后者在 Related Work 一句。

**W3** [warning] DID 零效应的过度解读
- 正文声称 "no detectable item-specific memorization"，但 Appendix N 显示 MDES 在 1.25–2.05pp（n=3 seeds）。应 reframe 为 "effects below detection threshold" 而非无效应。

**W4** [warning] Calibration 比较基线不够强
- Table 4 的基线偏简单，缺少更先进的 calibration 方法（如 Bayesian calibration、ensemble methods）。

### 小问题
- Figure 1 仅展示 seed=42，主图应展示 error bars
- "catastrophic collapse" 用于 ≤25pp 下降略显夸张
- ARC IRT marginal model fit (PPP=0.003) 应在正文讨论而非仅放附录
- 引用 `holland_1993_dif` 年份 mismatch 需确认

### 缺失的重要相关工作
1. 药理学 dose-response 建模经典文献（Hill 1910; Ritz et al. 2015）
2. Balloccu et al. (2024) "Leak, Cheat, Repeat" (EACL 2024)
3. Bordt et al. (2025) "How Much Can We Forget about Data Contamination?"

### 主要优势
1. 研究问题精准且有实际价值
2. 四家族 × 五剂量 × 三基准 × 多 seed 的 factorial design 严谨
3. Cross-benchmark transfer 的 GSM8K 方向反转发现有趣
4. IRT 框架提供置信区间，对实践者有用
5. 附录极其充实，体现良好实验规范

### 格式合规
- ✅ 正文 8 页，符合 EMNLP 2026 Long paper 限制
- ✅ ACL 模板正确
- ✅ Limitations 章节存在且有实质内容
- ✅ Ethics Statement 存在
- ✅ 匿名性完整，未发现身份泄露
- ✅ 参考文献格式基本规范

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-21T16:05:24.297629+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf",
  "pages": "1-2,5-9",
  "project": "contamcal-irt-calibration",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.pdf",
    "pages": "1-2,5-9",
    "project": "contamcal-irt-calibration",
    "dpi": "150"
  }
}
```

</details>

---
