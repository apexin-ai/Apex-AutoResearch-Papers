# Reviewer coordination (archived snapshot) — Part 2 of 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-coordination-20260517-080106.md) · [Structured JSON](../../../sessions/90/90ff1a212b857b7c2624.json)

## Round 53

### Tool call

_source line 681 · 2026-05-17T07:45:31.595886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 682 · 2026-05-17T07:45:32.048179+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but how they internally process multimodal information at the token level remains unknown.
2	We perform a systematic token-level representational decomposition of a VLA (OpenVLA-7B on LIBERO) with factorial trained-vs-untrained control, combining cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers.
3	Three findings emerge.
4	First, the VLA exhibits strict token-level functional specialization: image tokens encode purely visual information (instruction classification at chance, $10\%$, across all layers), while the readout token serves as a multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning reorganizes instruction routing across depth: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads), enabling immediate instruction access ($99.6\%$ at L1 vs.\ pretrained $80.2\%$); untrained routing never exceeds $10\%$.
6	Third, the LLM applies a non-monotonic refinement of vision encoder geometry: RSA peaks at L12, probe $R^2$ peaks at L8--L13, with self-supervised DINOv2 providing the highest geometric foundation ($\rho = 0.692$, exceeding all internal representations).
7	These results reveal that VLAs maintain a strict division of labor between visual and multimodal tokens, with training primarily reshaping readout-token information integration (routing $+18$pp, attention $+46$pp) rather than visual representations ($\Delta \leq 1.7\%$).
8	These findings suggest that routing efficiency to the readout position may be a key design consideration; vision encoder quality emerges as a candidate lever for action-relevant representation quality.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 683 · 2026-05-17T07:45:32.048785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 684 · 2026-05-17T07:45:32.502195+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) process visual observations and language instructions through a large language model to produce robot actions~\cite{brohan2023_rt2,kim2024_openvla}.
5	A central but untested assumption is that all token types within the LLM contribute uniformly to action prediction.
6	Understanding the token-level division of labor is essential for designing efficient VLA architectures: if image tokens and readout tokens serve fundamentally different roles, then design choices (attention patterns, layer selection, action head placement) should reflect this specialization.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings hint at internal specialization but do not explain \emph{how} information is routed within the LLM, \emph{where} instruction identity is encoded, or \emph{what} training changes at the representational level.
10	No prior work has provided a systematic multi-metric decomposition of a VLA with factorial trained/untrained controls, leaving open whether image tokens carry instruction information, whether the readout token functions as a multimodal hub, and whether training creates new representational structure or reconfigures inherited geometry.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: 
…[truncated 2372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 685 · 2026-05-17T07:45:32.502688+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 686 · 2026-05-17T07:45:32.553303+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We decompose a VLA's internal representations with factorial trained-vs-untrained control, revealing: (1)~strict token-level specialization (instruction-blind image tokens, cross-validated readout hub); (2)~reorganized instruction routing from mid-depth (L9--L16) to entry-exit (L0--L1, L31); and (3)~non-monotonic vision encoder refinement (peak L12, readout $R^2$ $+0.069$, image $\Delta \leq 1.7\%$).
5	Vision encoder quality emerges as the primary design lever.
6	Code and representations will be released upon acceptance.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 687 · 2026-05-17T07:46:48.518141+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -c /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig_32layer_attention.pdf /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig_multi_layer_attn.pdf",
  "description": "Compare file sizes of 32-layer vs multi-layer figures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -c /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig_32layer_attention.pdf /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig_multi_layer_attn.pdf",
    "description": "Compare file sizes of 32-layer vs multi-layer figures"
  }
}
```

</details>

---


### Tool result

_source line 688 · 2026-05-17T07:46:49.472904+00:00_

25110 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig_32layer_attention.pdf
25110 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig_multi_layer_attn.pdf
50220 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 689 · 2026-05-17T07:46:49.573998+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "md5sum /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig_32layer_attention.pdf /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig_multi_layer_attn.pdf",
  "description": "MD5 comparison to confirm identical files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "tool_args": {
    "command": "md5sum /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig_32layer_attention.pdf /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig_multi_layer_attn.pdf",
    "description": "MD5 comparison to confirm identical files"
  }
}
```

</details>

---


### Tool result

_source line 690 · 2026-05-17T07:46:49.674707+00:00_

f88555cb19ab042e784c8309b223636a  /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig_32layer_attention.pdf
f88555cb19ab042e784c8309b223636a  /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig_multi_layer_attn.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 691 · 2026-05-17T07:46:55.249124+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 692 · 2026-05-17T07:46:55.299903+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 693 · 2026-05-17T07:47:33.732886+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

```json
{
  "text": "## 审查报告 — 论文更新后全文一致性核实（experiments.tex / abstract.tex / introduction.tex / conclusion.tex）\n\n### CRITICAL\n\n**1. [severity: critical] fig_32layer_attention.pdf 是 4 层版本的副本，不是 32 层图**\n\n`artifacts/figures/paper/fig_32layer_attention.pdf` 与 `fig_multi_layer_attn.pdf` MD5 完全一致（`f88555cb19ab042e784c8309b223636a`），大小均为 25,110 bytes。视觉确认该图只有 L1/L8/L16/L31 四个数据点。\n\n远程服务器上实际生成了两个正确的 32 层图：\n- `/root/autodl-tmp/vla-ssd/results/attention/fig_full_32layer_attention.pdf` (20,195 bytes) — 双 panel 版\n- `/root/vla-ssd/scripts/fig_32layer_attention_profile.pdf` (14,867 bytes) — 单 panel 版\n\n但传输过程出错，本地保存的是旧的 4 层版本。\n\n**影响**：experiments.tex:102 引用此文件，Figure caption 描述 32 层数据（\"across all 32 LLM layers\"），但如果提交当前版本，审稿人看到的图只有 4 个点。**必须重新传输正确的 32 层图。**\n\n**2. [severity: critical] Abstract/Introduction 与 Experiments 数据自相矛盾：untrained 10% 阈值**\n\n- Abstract (line 5): \"untrained routing never exceeds $10\\%$\"\n- Introduction (line 22): \"Untrained routing never exceeds $10\\%$ at any layer\"\n- Experiments (line 62): \"The untrained model allocates 0/32 instruction-dominant heads ($11.7\\%$ text attention, $87.8\\%$ image)\"\n\n$11.7\\% > 10\\%$，论文自相矛盾。\n\n根因：两套数据源不一致。Registry 中 `l1_mean_text_attn.untrained = 0.117`（原始实验），32 层分析显示 `mean_text ≈ 0.078`（不同初始化方案）。论文同时引用了两个数据源的数字但没有统一。\n\n**建议**：要么统一用 11.7% 并改 abstract/intro 为 \"never exceeds 12%\"，要么确认哪个数据源是权威的并全文统一。\n\n### WARNING\n\n**3. [severity: warning] Abstract \"routing +18pp\" 含义模糊**\n\nAbstract line 7: \"routing $+18$pp, attention $+46$pp\"。\n- \"+46pp\" 清楚：trained text attn 57.7% - untrained 11.7% = 46.0pp\n- \"+18pp\" 最可能是 L31 probe 准确率差（100% - 82% = 18pp），但 probe 准确率不是 \"routing\"\n\n两个 +Xpp 并列，读者会以为都是 attention 指标。建议明确标注来源，如 \"probe accuracy $+18$pp at L31, attention $+46$pp\"。\n\n**4. [severity: warning] Conclusion \"primary design lever\" vs Abstract \"candidate lever\" 不一致**\n\n- Conclusion (line 5): \"Vision encoder quality emerges as the primary design lever.\" — 断言式\n- Abstract (line 8): \"vision encoder quality emerges as a candidate lever\" — 带 hedge\n\n同一篇论文中，对同一结论的 confidence level 不应在 abstract 和 conclusion 之间变化。建议统一为 \"candidate lever\" 或至少 \"a key design lever\"。\n\n**5. [severity: warning] Introduction \"No prior work has provided...\" 功能等同于 \"first\" claim**\n\nIntroduction line 10: \"No prior work has provided a systematic multi-metric decomposition...\"。这在语义上等于 \"We are the first to...\"，上一轮审稿已要求删除显式 \"first\" claims。建议改为 \"Prior work has not yet provided...\" 或 \"Existing analyses have focused on ... but have not combined ...\"，降低 novelty claim 的绝对性。\n\n### INFO\n\n**6. [severity: info] Table 3 \"Mode\" 列缩写未定义**\n\nTable 3 的 Mode 列使用 \"immed.+stable / gradual+stable / incid.+forget\"，这些缩写在正文中没有解释。建议加脚注定义，或在 caption 中简述。\n\n**7. [severity: info] 32 层数据核实通过**\n\nexperiments.tex 中所有 32 层数据与 registry 和远程 JSON 交叉验证一致：\n- Trained L0-L1: 21-24 heads ✓\n- Llama2base L9-L16: 15-22 heads ✓  \n- Trained L31: 18 heads ✓\n- Llama2base L31: 8 heads ✓\n- Untrained 全层 0/32 heads ✓\n- Probe accuracy: trained 99.6%@L1, llama2base 80.2%@L1, untrained 82%@L31 ✓",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "## 审查报告 — 论文更新后全文一致性核实（experiments.tex / abstract.tex / introduction.tex / conclusion.tex）\n\n### CRITICAL\n\n**1. [severity: critical] fig_32layer_attention.pdf 是 4 层版本的副本，不是 32 层图**\n\n`artifacts/figures/paper/fig_32layer_attention.pdf` 与 `fig_multi_layer_attn.pdf` MD5 完全一致（`f88555cb19ab042e784c8309b223636a`），大小均为 25,110 bytes。视觉确认该图只有 L1/L8/L16/L31 四个数据点。\n\n远程服务器上实际生成了两个正确的 32 层图：\n- `/root/autodl-tmp/vla-ssd/results/attention/fig_full_32layer_attention.pdf` (20,195 bytes) — 双 panel 版\n- `/root/vla-ssd/scripts/fig_32layer_attention_profile.pdf` (14,867 bytes) — 单 panel 版\n\n但传输过程出错，本地保存的是旧的 4 层版本。\n\n**影响**：experiments.tex:102 引用此文件，Figure caption 描述 32 层数据（\"across all 32 LLM layers\"），但如果提交当前版本，审稿人看到的图只有 4 个点。**必须重新传输正确的 32 层图。**\n\n**2. [severity: critical] Abstract/Introduction 与 Experiments 数据自相矛盾：untrained 10% 阈值**\n\n- Abstract (line 5): \"untrained routing never exceeds $10\\%$\"\n- Introduction (line 22): \"Untrained routing never exceeds $10\\%$ at any layer\"\n- Experiments (line 62): \"The untrained model allocates 0/32 instruction-dominant heads ($11.7\\%$ text attention, $87.8\\%$ image)\"\n\n$11.7\\% > 10\\%$，论文自相矛盾。\n\n根因：两套数据源不一致。Registry 中 `l1_mean_text_attn.untrained = 0.117`（原始实验），32 层分析显示 `mean_text ≈ 0.078`（不同初始化方案）。论文同时引用了两个数据源的数字但没有统一。\n\n**建议**：要么统一用 11.7% 并改 abstract/intro 为 \"never exceeds 12%\"，要么确认哪个数据源是权威的并全文统一。\n\n### WARNING\n\n**3. [severity: warning] Abstract \"routing +18pp\" 含义模糊**\n\nAbstract line 7: \"routing $+18$pp, attention $+46$pp\"。\n- \"+46pp\" 清楚：trained text attn 57.7% - untrained 11.7% = 46.0pp\n- \"+18pp\" 最可能是 L31 probe 准确率差（100% - 82% = 18pp），但 probe 准确率不是 \"routing\"\n\n两个 +Xpp 并列，读者会以为都是 attention 指标。建议明确标注来源，如 \"probe accuracy $+18$pp at L31, attention $+46$pp\"。\n\n**4. [severity: warning] Conclusion \"primary design lever\" vs Abstract \"candidate lever\" 不一致**\n\n- Conclusion (line 5): \"Vision encoder quality emerges as the primary design lever.\" — 断言式\n- Abstract (line 8): \"vision encoder quality emerges as a candidate lever\" — 带 hedge\n\n同一篇论文中，对同一结论的 confidence level 不应在 abstract 和 conclusion 之间变化。建议统一为 \"candidate lever\" 或至少 \"a key design lever\"。\n\n**5. [severity: warning] Introduction \"No prior work has provided...\" 功能等同于 \"first\" claim**\n\nIntroduction line 10: \"No prior work has provided a systematic multi-metric decomposition...\"。这在语义上等于 \"We are the first to...\"，上一轮审稿已要求删除显式 \"first\" claims。建议改为 \"Prior work has not yet provided...\" 或 \"Existing analyses have focused on ... but have not combined ...\"，降低 novelty claim 的绝对性。\n\n### INFO\n\n**6. [severity: info] Table 3 \"Mode\" 列缩写未定义**\n\nTable 3 的 Mode 列使用 \"immed.+stable / gradual+stable / incid.+forget\"，这些缩写在正文中没有解释。建议加脚注定义，或在 caption 中简述。\n\n**7. [severity: info] 32 层数据核实通过**\n\nexperiments.tex 中所有 32 层数据与 registry 和远程 JSON 交叉验证一致：\n- Trained L0-L1: 21-24 heads ✓\n- Llama2base L9-L16: 15-22 heads ✓  \n- Trained L31: 18 heads ✓\n- Llama2base L31: 8 heads ✓\n- Untrained 全层 0/32 heads ✓\n- Probe accuracy: trained 99.6%@L1, llama2base 80.2%@L1, untrained 82%@L31 ✓",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 694 · 2026-05-17T07:47:35.038269+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 1305
}
```

</details>

---


### Assistant

_source line 695 · 2026-05-17T07:47:41.934292+00:00_

报告已发送。发现 2 个 critical 问题：

1. **图文件错误**：`fig_32layer_attention.pdf` 实际是 4 层版副本（MD5 一致），需重新从远程传输正确的 32 层图。
2. **数据矛盾**：Abstract/Introduction 说 untrained routing "never exceeds 10%" 但 Experiments 中写 11.7%，论文自相矛盾。

另有 3 个 warning（"+18pp" 含义模糊、conclusion/abstract hedge 不一致、"No prior work" 等同 first claim）和 2 个 info 级发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer"
}
```

</details>

---


## Round 54

## Round 54

2 recorded events


### User

_source line 696 · 2026-05-17T08:00:22.559175+00:00_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 697 · 2026-05-17T08:01:06.446660+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 服务器 `westd-19183`，GPU 白名单需通过 `read_project_file` 或 registry 确认（之前项目配置为 2x RTX PRO 6000）
- 本地 artifacts 中 `fig_32layer_attention.pdf` 是**错误文件**（4 层版副本，MD5=f88555cb19ab042e784c8309b223636a）。正确的 32 层图在远程服务器，未成功传输。**不要基于本地这个文件做任何审查判断**
- Reviewer 只读，不执行实验、不修改文件，唯一输出渠道 `reviewer_post_to_director`

### 2. 🖥️ 基础设施快照
- 服务器：`westd-19183`，远程工作目录 `/root/vla-ssd`（代码）+ `/root/autodl-tmp/vla-ssd`（数据/结果）
- 模型：OpenVLA-7B，Llama-2-7B base 控制条件 checkpoint 在远程
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/`
- 论文 tex：`docs/paper/*.tex`，artifacts：`artifacts/` 下按子目录分类
- 远程 32 层图（正确版本）：
  - `/root/autodl-tmp/vla-ssd/results/attention/fig_full_32layer_attention.pdf` (20,195 bytes, 双 panel)
  - `/root/vla-ssd/scripts/fig_32layer_attention_profile.pdf` (14,867 bytes, 单 panel)
- 无活跃训练进程（所有实验 DONE）

### 3. 📊 当前状态
刚完成论文全文一致性审查（experiments/abstract/intro/conclusion），已发 `reviewer_post_to_director`，包含：
- **2 个 CRITICAL**：(1) fig_32layer_attention.pdf 是 4 层副本需重传；(2) abstract/intro 说 "untrained routing never exceeds 10%" 但 experiments 写 11.7%，自相矛盾
- **3 个 WARNING**：(1) abstract "+18pp" 含义模糊；(2) conclusion "primary" vs abstract "candidate" lever 不一致；(3) intro "No prior work" 等同 first claim
- **2 个 INFO**：Table 3 Mode 缩写未定义；32 层数据核实通过

Registry 65 个实验全部 DONE。无 RUNNING/PREPARING。无等待中的 Worker 或 Cron。

### 4. 📋 待办（条件触发式）
- Paper Agent 提交修复后的 tex → 核实两个 CRITICAL 是否修复（10% vs 11.7% 统一、32 层图替换）
- 32 层图重传完成 → 视觉审查新图是否正确显示 32 个数据点
- Director 回复审查报告 / 要求进一步审查 → 按需执行
- Paper Agent 提交 Round 3 全文 → 按 §5 章节审查维度做完整对抗审查，含评分模板
- 页数检查：CoRL 8 页正文限制，添加 Llama-2 base 数据后可能超限 → 需确认

### 5. 🎯 战略上下文
- **核心三发现**：(C1) token 功能特化（image blind, readout hub）；(C2) VLA 训练重组 instruction routing（mid-depth→entry-exit）；(C3) vision encoder 几何非单调精化（inverted-U）
- **C2 叙事已确认**：32 层数据支持 "reorganizes"——trained=bookend/W-shape（L0-L1 + L31 peaks），llama2base=inverted-U（L9-L16 peak），untrained=0 everywhere。我之前基于 4 层数据持怀疑态度，32 层数据出来后已部分撤回
- **最易判断错的事**：untrained 的 mean_text_attn 有两个数据源（registry=0.117 即 11.7%，32 层分析=0.078 即 7.8%），原因是不同初始化方案。论文混用了两个数字。下一个审查者必须确认最终统一用哪个
- **时间线**：May 20 Round 3 review，May 26 Abstract DDL，May 29 Paper DDL（CoRL 2026）
- **Round 2 审稿分数**：R1=5/10, R2=5/10, R3=7/10，均分~5.3。Llama-2 base 控制实验是 Round 2 修复的核心增量
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer"
}
```

</details>

---
