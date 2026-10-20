# reviewer / loop_7.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`8f264873b2b8512ffa60.json`](../../sessions/8f/8f264873b2b8512ffa60.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-17T08:01:06+00:00'
---

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


---
