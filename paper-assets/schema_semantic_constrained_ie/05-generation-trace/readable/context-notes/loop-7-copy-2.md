# agent / loop_7.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`a2444869b4328f9b195f.json`](../../sessions/a2/a2444869b4328f9b195f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-15T11:22:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-16980 的 cuda:0 和 cuda:1，不可用其他 GPU
- 模型路径：`/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`（Llama）和 `/root/autodl-tmp/models/Qwen/Qwen3-8B`（Qwen），不要假设其他路径
- 论文已提交审稿（apr_20260515T081453_7j0q），不要修改 paper/ 目录下文件除非 Director 明确指示
- EMNLP ARR 截止 May 25，所有实验必须为此服务

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980，工作目录 `/root/schema_semantic_constrained_ie`
- Python：`/root/miniconda3/bin/python`，conda base 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：Llama `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`；Qwen `/root/autodl-tmp/models/Qwen/Qwen3-8B`
- 数据：`data/docred/dev.json`（DocRED），`data/scierc/test.json`（SciERC）
- 约束文件：`data/docred/ontology_constraints_docred.json`，`data/scierc/ontology_constraints_scierc.json`
- 活跃进程：`llama_docred_unconstrained_mt6144`（PID 246947，cuda:0，tmux session 应存在，cron 监控中）
- cuda:1 空闲（`llama_docred_full_s1_mt6144` 已失败退出）

### 3. 📊 当前状态
刚收到 `llama_docred_full_s1_mt6144` 失败回调（EXIT_CODE=1，仅跑 22 秒）。已派诊断 Worker `worker_diag_llama_docred_full_s1_mt6144_20260515T082058` 去 SSH 读日志，**尚未回调**——这是最优先要处理的。

Registry 状态：
- `llama_docred_unconstrained_mt6144`：RUNNING，cuda:0，PID 246947——max_new_tokens=6144 的 unconstrained baseline
- `llama_docred_full_s1_mt6144`：DONE(failed)——max_new_tokens=6144 的 full_s1 约束版本
- 其余 20 个实验全部 DONE（19 success，1 killed）

等待中：
- 诊断 Worker 回调 → 根据根因决定修复重跑
- `llama_docred_unconstrained_mt6144` cron 监控 → 完成后做 on-experiment-done 流程

### 4. 📋 待办
- 诊断 Worker 回调到达 → 读诊断报告，根据根因修复代码/参数 → 重新提交 `llama_docred_full_s1_mt6144` 到 cuda:1
- `llama_docred_unconstrained_mt6144` cron 回调（success）→ 分析 mt6144 unconstrained 结果 → 与之前 unconstrained（默认 max_tokens）对比 → 更新 registry + report.md → 汇报 Director
- 两个 mt6144 实验都完成后 → 对比 mt6144 vs 默认 max_tokens 的 DR 差异 → 这是 P1 max tokens 实验的核心数据点 → 写入论文（如果 Director 同意）
- cuda:1 空闲 → 修复后立即重跑，不要让 GPU 闲着

### 5. 🎯 战略上下文
- 项目处于论文审稿阶段，核心实验已完成。这批 mt6144 实验是 P1 补充实验，验证 max_new_tokens 对约束解码效果的影响
- 核心结论：OntoCoDec 双层约束解码在 Qwen3-8B 和 Llama-3.1-8B 上均显著降低 violation rate（DR 45-99.4%），R-F1 无损或微升
- 22 秒就崩 → 极大概率是 Python 启动阶段错误（import 失败 / 参数解析 / 文件路径 / OOM 加载模型），不太可能是推理过程中的问题
- 易踩坑：之前的 `llama_docred_full_s1`（默认 max_tokens）是成功的，mt6144 版本唯一区别是 `--max_new_tokens 6144`，所以问题可能与 token 长度相关的初始化有关（比如 grammar 编译对 6144 tokens 的处理）
- D014 决策：tightness scaling claim 已从单因素改为双因素，不要回退
- D015 决策：论文标题已去掉 "Near-Complete"，不要加回来


---
