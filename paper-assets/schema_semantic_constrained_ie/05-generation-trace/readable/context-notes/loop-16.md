# agent / loop_16.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_16.md`
- **Structured JSON:** [`7ae982db244fb134a7ea.json`](../../sessions/7a/7ae982db244fb134a7ea.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-17T11:07:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文所有 .tex 文件在 `artifacts/_project/paper/` 目录下，不是项目根目录
- Beam search 表格中 DocRED greedy 行已改为 matched 50-doc 数据（SF1），不要再用 998-doc 全集数据
- appendix_discussion.tex 中 R²=0.99 仅适用于 calibrated models (Qwen+Llama, n=4)，Mistral 需单独说明偏差原因（ET>5%）
- 不要在论文正文中使用 em-dash（— 或 –），已全文清零，新增文本也禁止

### 2. 🖥️ 基础设施快照
- 实验服务器：westd-16980（Qwen + Llama 推理）、westd-21461（Mistral 推理）
- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/`
- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/`
- GPU：2x NVIDIA RTX PRO 6000 Blackwell 98GB（训练用单卡）
- 无活跃训练进程，当前只有 2 个 Worker 在做代码分析（非 GPU 任务）

### 3. 📊 当前状态
正在执行 Director 的 Round 4 审稿修改清单（~20 项，分 3 批）。

**已完成**：
- Batch 1+2 全部文本编辑（MF1-2, SF2-4/6/9, M1-2/4-5/7/9-10, Q1, 全文 em-dash 清零, References 补充）
- Batch 3 中 3 项：SF1（beam 表 matched greedy 已更新）、SF8（reproducibility appendix 已创建）、M6+Q4（CF-DR 转移性论证已写入 appendix_discussion.tex）

**等待中的 Worker**：
- `worker_code_r4_sf5_sf7_llama_docred_20260517T105428`（RUNNING, turn 8）：Llama DocRED parse-failure 分析 + 全模型 DocRED fallback coverage 数据
- `worker_code_r4_m3q3_semantic_only_et_20260517T110021`（RUNNING, turn 7）：semantic-only 配置为何增加 ET 违规的机制解释

### 4. 📋 待办
- SF5+SF7 Worker 回调 → 读产出 → 将 Llama parse-failure 解释写入 §5 DocRED 或 appendix；将 fallback coverage 数据写入 appendix_discussion.tex 对应段落
- M3+Q3 Worker 回调 → 读产出 → 将 semantic-only ET 增加的机制解释写入 §5 SciERC 的 semantic-only 段落或 appendix
- 两个 Worker 都完成 → 向 Director 汇报 Batch 3 全部完成，附完整修改清单勾选状态

### 5. 🎯 战略上下文
- 这是 EMNLP 2026 ARR 投稿的 Round 4 审稿修改，目标是堵住审稿人攻击面
- 核心 narrative：OntoCoDec 两层约束（grammar + semantic）对 IE 的 DR 违规减少 42-99%，零 F1 降级；dual-factor pattern（schema tightness × baseline violation rate）解释残余 DR
- R² 从 0.886 改为 0.99（排除 Mistral 后 calibrated models only），这是 MF1 关键修改
- 易踩坑：DocRED 数据有两套——998-doc 全集（主表用）和 50-doc 子集（beam 表用，现在已 matched）。不要混用。SF1 matched greedy 的具体数值见 `artifacts/r4_sf1_matched_greedy_results.md`
- 新创建的文件：`appendix_reproducibility.tex`（已加入 main.tex \input）


---
