# agent / loop_13.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`25a9deddf8b3c7ade1aa.json`](../../sessions/25/25a9deddf8b3c7ade1aa.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-16T10:51:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-16980 cuda:0/1 + westd-21461 cuda:0/1，共 4 张，其他设备号禁用
- submit_on_allocated 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不能假设 .venv 存在
- GPU 编号脚本内始终写 `--gpu 0`（框架自动映射物理卡）
- Qwen3-8B tokenizer 有 regex warning 问题（Reviewer 已发现），w7 系列结果需注意可比性
- 不加 NYT29 第三数据集（D031 决策）；FT post-hoc baseline 必做

### 2. 🖥️ 基础设施快照
- **westd-16980**: 工作目录 `/root/schema_semantic_constrained_ie`，Python `/root/miniconda3/bin/python`，conda base env
  - 模型: `/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged`, `/root/autodl-tmp/checkpoints/llama3_8b_lora_scierc_merged`
  - DocRED checkpoints 同目录（qwen3_8b_lora_docred_merged, llama3_8b_lora_docred_merged）
  - 数据: `data/processed_data/test.json` (SciERC 551 samples), DocRED 数据在 `data/docred/`
  - 活跃: w5_qwen_docred_lora_constrained_eval PID=321568 cuda:1
- **westd-21461**: 同结构工作目录，Mistral 模型在 `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3`
  - 活跃: w6_mistral_docred_unconstrained PID=7740 cuda:0, w6_mistral_docred_constrained PID=8347 cuda:1
- W&B: 项目内自动上报，无需额外配置
- Cron 监控: 3 个活跃（上述 3 个 RUNNING 实验）

### 3. 📊 当前状态
刚收到 w7_qwen_scierc_ft_grammar_only 失败回调（进程死 5 次无产出）。已派 Worker `worker_diagnose_w7_qwen_scierc_ft_grammar_only_20260516T064258` SSH 到 westd-16980 查日志诊断根因。已向 Director 汇报。

**RUNNING 实验**:
- `w5_qwen_docred_lora_constrained_eval` — FT Qwen DocRED + constrained eval，验证 composability（westd-16980:cuda:1）
- `w6_mistral_docred_unconstrained` — Mistral DocRED zero-shot baseline（westd-21461:cuda:0）
- `w6_mistral_docred_constrained` — Mistral DocRED + OntoCoDec constrained（westd-21461:cuda:1）

**PREPARING**: w8_llama_docred_ft_grammar_only, w8_ft_posthoc_baseline, w7_llama_scierc_ft_semantic_only, w7_llama_scierc_ft_grammar_only, w7_qwen_scierc_ft_semantic_only

**等待中**: Worker 诊断回调（w7_qwen 失败原因）；westd-16980:cuda:0 空闲待复用

### 4. 📋 待办（条件触发式）
- Worker 诊断回调到达 → 读诊断报告 → 修复问题 → 重新提交 w7_qwen_scierc_ft_grammar_only 到 westd-16980:cuda:0
- w5_qwen_docred_lora_constrained_eval 完成 → 按 on-experiment-done 流程分析（composability 最后一格）→ 汇报 Director
- w6_mistral_docred_unconstrained/constrained 完成 → 分析 Mistral DocRED 数据 → 更新关键数字速查表 → 汇报
- westd-16980:cuda:0 修复重跑后若快速完成 → 接着排 w7_llama_scierc_ft_grammar_only
- 所有 w7 ablation 完成 → 排 w8_ft_posthoc_baseline（Dream 审稿要求）

### 5. 🎯 战略上下文
- **核心论点**: OntoCoDec 两层约束解码（grammar + semantic）自动编译 ontology schema 为 token constraints，消除 LLM IE 的 schema violations
- **投稿目标**: EMNLP 2026 ARR May 25（9 天后）
- **关键进展**: 3 模型（Qwen/Llama/Mistral）× 2 数据集（SciERC/DocRED）zero-shot 已完成；composability（FT+OntoCoDec）SciERC 2×2 已完成，DocRED 差 Qwen 最后一格（69% running）
- **当前瓶颈**: w7 FT-regime ablation（grammar_only / semantic_only）是 Dream 审稿暴露的结构性缺陷，必须补齐才能投稿。首个格子（Qwen grammar_only）就失败了，需快速修复
- **易错点**: 
  - w7 系列是 eval-only 实验（用已有 FT checkpoint + 约束解码的某一层），不是训练实验，运行时间应较短（~30-60min），如果超时大概率是 bug 不是 OOM
  - Mistral 在 SciERC 上 DR=56.94%（所有模型中最高），constrained 后仍有 13.4%——这不是 negative，是"复杂 violation profile 下 semantic 层的必要性证据"
  - D031 决策：不加 NYT29，专注现有 2 数据集深度 ablation


---
