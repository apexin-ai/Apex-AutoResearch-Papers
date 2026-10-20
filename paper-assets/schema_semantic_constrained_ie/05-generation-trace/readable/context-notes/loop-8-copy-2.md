# agent / loop_8.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`59c6542fd101fd89cfa7.json`](../../sessions/59/59c6542fd101fd89cfa7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-15T14:29:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 cuda:0, cuda:1 on westd-16980**。不可用其他 GPU，Director 指令也不能覆盖
- submit_training_job 命令必须用 `bash -c '...'` 包裹（tmux 默认 sh，source/conda activate 是 bash built-in，否则 EXIT_CODE=127）
- Python 路径用绝对路径 `/root/miniconda3/bin/python`（aml-train 镜像，conda base 环境）
- DDL: **ARR May 25, 2026**（10 天），不可建议降级 venue
- W1 CF fallback 实验 conclusion 出来前，**不动 paper 的 CF 相关段落**
- D019 已确认代码已是 pair-based → W2 是**纯写作修复**，不要改代码

### 2. 🖥️ 基础设施快照
- **服务器**: westd-16980, account=root
- **工作目录**: `/root/schema_semantic_constrained_ie`
- **Python**: `/root/miniconda3/bin/python`（conda base，不要创建 venv）
- **环境激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型路径**: Qwen3-8B 在默认 HF cache; Llama-3.1-8B 在 `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`
- **约束文件**: `data/docred/ontology_constraints_docred.json` (96 rels), SciERC 在默认位置
- **核心代码**: `compiler/` (ontology_compiler.py, type_mask_processor.py), `run_constrained_extraction.py` (652 行, 5 模式)
- **活跃进程**:
  - `w1_cf_fallback_scierc_pilot`: PID 270088, cuda:0, cron 监控中
  - `llama_docred_full_s1_mt6144`: PID 247487, cuda:1, cron 监控中
- **活跃 Worker**: `worker_research_pair_based_impl_plan_20260515T141200` (running, turn 4, 正在 SSH 读代码分析 pair-based 实现)
- **Cron**: 2 个活跃（对应上述两个 RUNNING 实验）

### 3. 📊 当前状态
**刚做完**: D019 决策——确认代码已是 pair-based（σ(r) enforcement），取消代码改动，W2 降级为纯写作修复。派了 Worker 调研 pair-based 实现细节（正在运行）。

**Registry 概况**: 成功 20 / 负向 0 / 失败 0 / killed 1 / RUNNING 2 / PREPARING 3

**RUNNING**:
1. `w1_cf_fallback_scierc_pilot` (cuda:0) — Qwen SciERC CF fallback pilot，验证 CF violation 在 fallback 模式下的行为
2. `llama_docred_full_s1_mt6144` (cuda:1) — Llama DocRED full S1 with max_tokens=6144，重跑以获得完整结果

**PREPARING** (等 GPU 释放):
- `w1_cf_fallback_llama_scierc` — Llama SciERC CF fallback
- `w1_cf_fallback_docred` — Qwen DocRED CF fallback
- `w1_cf_fallback_llama_docred` — Llama DocRED CF fallback

**等待中**:
- Worker `pair_based_impl_plan` 回调 → 产出 W2 写作修复方案
- `w1_cf_fallback_scierc_pilot` cron 回调 → 分析 + 启动下一个 CF fallback 实验
- `llama_docred_full_s1_mt6144` cron 回调 → 分析 + 释放 cuda:1 给 D018 W5 LoRA

### 4. 📋 待办（条件触发式）
- `w1_cf_fallback_scierc_pilot` 完成 → 分析 CF 结果 → 决定 CF fallback 代码是否需调整 → 提交 `w1_cf_fallback_docred` (cuda:0) + `w1_cf_fallback_llama_scierc` (cuda:1 若已释放)
- `llama_docred_full_s1_mt6144` 完成 → 分析 Llama DocRED 完整结果 → 释放 cuda:1 → 启动 D018 W5 LoRA fine-tune (Qwen3-8B SciERC, ~6 GPU-hrs, cuda:1)
- `pair_based_impl_plan` Worker 回调 → 根据调研结果写 W2 §3 形式化修复（pair-based notation 统一）
- W5 LoRA 训练完成 → unconstrained fine-tuned eval → gate: DR>2% 才继续 constrained eval → 分析 composability
- 全部 W1 CF fallback 4 实验完成 → DR-CF Pareto 图 + violation budget → 写入论文
- 所有实验完成 → Track C 写作重构（§3 形式化 + narrative arc + claim 升级评估）

### 5. 🎯 战略上下文
**项目**: OntoCoDec — 两层约束解码（grammar + semantic）编译 IE ontology 为 token-level constraints，消除 LLM IE 的 ontology violations。投 EMNLP 2026。

**核心结论链**:
- D010: Dream 评分 Weak Reject 2.75/5 → 制定 6 项结构性补强
- D012: Bootstrap CI framing 定稿（逐数据集报告）
- D013: Post-hoc baseline framing（不以 F1 论高低，多维对比）
- D014: Tightness scaling = tightness × model RV baseline 双因素
- D016: Llama CI 修复完成，全部 p-values 写入论文
- D018: W5 LoRA 批准（条件启动）
- D019: 代码已是 pair-based，W2 降级为写作修复

**关键数字**: SciERC DR↓94% (0.93% 残余), DocRED DR↓45% (10.19% 残余, Qwen) / DR↓90.2% (Llama)。R-F1 从不下降。CF 是已知 limitation (9.90% SciERC)。

**最容易判断错的事**:
1. **不要把 CF fallback 和 semantic fallback 搞混**: CF = cross-field consistency violation (entity type 在 entity list vs relation 中不一致)；semantic fallback = grammar∩semantic=∅ 时退化为 grammar-only。两个独立概念
2. **Grammar-only DR 上升不是 bug**: DocRED grammar_only DR=26.17% > unconstrained 18.46%，这是因为 grammar 消除 RV 后暴露了 latent DR violations。这是**论文卖点**不是弱点
3. **ET 指标待 D011 v2 checker 修正**: DocRED ET 数字可能需要更新（triple-counting 问题）
4. **Llama fallback 数据单位是 token-level，Qwen 是 triple-level**: 不可直接对比绝对值，只能说趋势一致
5. **W1 CF fallback 是 critical priority**（Round 1 Issue Tracker 唯一 in_progress 的 critical）——所有 GPU 时间优先给它，W5 LoRA 是条件启动（等 cuda:1 释放）


---
