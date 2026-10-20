# director / loop_4.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`2560a39eee4d3fc8d815.json`](../../sessions/25/2560a39eee4d3fc8d815.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-15T14:02:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1（westd-16980 分配给本项目的卡）。不可用其他 GPU
- 论文 .tex 真源在本地 `artifacts/_project/paper/`，不在远程服务器。写作修改操作本地文件
- 训练代码/数据/checkpoint 真源在远程 `/root/schema_semantic_constrained_ie/`
- mt6144 实验正在跑（cuda:0 + cuda:1 各一个），CF fallback 实验必须等 mt6144 完成后才能启动，不可抢占

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980 (connect.westd.seetacloud.com)，用户 root
- 工作目录：`/root/schema_semantic_constrained_ie`
- Python/conda：aml-train 镜像，`/root/miniconda3/bin/python`，conda base 环境
- 模型：Qwen3-8B + Llama-3.1-8B-Instruct（路径见远程项目配置）
- 数据：SciERC (7 relations) + DocRED (96 relations)
- W&B：未配置
- 活跃进程：mt6144 两组实验 RUNNING（llama_docred_full_s1_mt6144 + llama_docred_unconstrained_mt6144），预计 unconstrained ~30min 内完成，full_s1 ~1-1.5h
- 本地 paper 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`

### 3. 📊 当前状态
**刚做完**：收到 Round 2 审稿报告（weak reject，4 个 Must-Fix + 5 个 Should-Fix）。已审查完整报告内容。Agent 已并行派发 2 个 Worker（CF fallback 日志修复 + CF 分析脚本框架），等待回调。

**RUNNING**：
- `llama_docred_full_s1_mt6144` — Llama DocRED max_new_tokens=6144 重跑（unconstrained 92%, full_s1 78%）
- `llama_docred_unconstrained_mt6144` — 同上 unconstrained 对照

**PREPARING（4 个 W1 CF fallback 实验）**：
- `w1_cf_fallback_llama_docred` / `w1_cf_fallback_llama_scierc` / `w1_cf_fallback_docred` / `w1_cf_fallback_scierc_pilot` — 等 mt6144 完成后立即启动

**等待中**：
- 2 个 Worker 回调（CF fallback 日志修复 + CF 分析脚本）
- mt6144 完成 cron 回调

### 4. 📋 待办
**⚠️ 用户最新指令（最高优先级）**：
> "仔细和reviewer一起反思需要怎么提升写作质量，哪怕是大实验，不要仅盯着小改小动，你的时间和资源都够，和reviewer也说明这一点，需要补的实验是肯定要补的，别等到最后再补实验"

**这条指令尚未执行——我在准备行动时触发了 WRITE HANDOFF。下一个"你"必须立即处理：**

1. **post_to_reviewer** 做全面反思：不限于 W1 CF fallback 小修，要求 Reviewer 评估所有审稿意见的写作质量提升方案，特别是大实验（W5 fine-tuned 模型验证、W6 latency 分析、W2 形式化重写）
2. **派 Agent 立即启动可并行的大实验**，不等 CF fallback 结果：
   - W3/W6：runtime/latency 测量（可用已有实验输出计时）
   - W5：fine-tuned 模型实验（如 GoLLIE + OntoCoDec，验证 composability claim）— 这是审稿最大短板，zero-shot R-F1~8% vs SOTA~50%
   - W9：Llama tokenizer single-token 唯一性验证
3. CF fallback Worker 回调 → 确认日志修复 + 分析脚本就绪
4. mt6144 完成 → 启动 4 个 W1 CF fallback 实验
5. 所有实验 + 写作修改完成 → `submit_paper_to_review(recommended_review_mode="continue")` 重新投稿

**用户还说了"论文修改出来之后再投一次稿"——已确认会在修改完成后自动触发重新投稿。**

### 5. 🎯 战略上下文
- **审稿总评 weak reject**，4 个 Must-Fix（W1 CF爆炸、W2 形式化不一致、W3 post-hoc F1更优、W4 表间数据不一致）+ 5 个 Should-Fix
- W1 CF fallback 实验已在推进，但**用户明确要求不要只盯小修**——W5（fine-tuned 模型）和 W6（latency）是拉开差距的关键，必须立即并行启动
- paper_framing.md 中 C2 已有 post-hoc 多维对比 framing，但缺 runtime 数据（W3/W6 共同需要）
- experiment_plan.yaml 为空——之前未维护，所有实验信息在 registry 和 paper_framing.md 中
- 目标 venue：EMNLP 2026 (ARR May 2026)，DDL May 25。时间足够做大实验
- **易错点**：不要觉得"时间紧只能修小问题"——用户已明确说时间资源够，大胆做。不要 fallback 思维
- **易错点**：W2 形式化问题（pair vs independent）需要确认 SciERC/DocRED 约束是否 rectangular——这是 Reviewer 最关键的 Q1，可能需要代码验证而非纯写作修改


---
