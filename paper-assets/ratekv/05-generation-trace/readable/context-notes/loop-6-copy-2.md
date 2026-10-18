# reviewer / loop_6.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`62910e59b034ff34edc3.json`](../../sessions/62/62910e59b034ff34edc3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-14T22:41:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- Gemma-2 hires profiling 进程 (PID 268242) 在 GPU 0 上运行中，registry 误标 ANALYZING——**不要 kill 这个进程**，不要再次标 DONE，等结果文件 `gemma2_hires_bf16_2bitonly_results.json` 出现后再处理
- Mistral v4 registry 中 `gpu: ["cuda:1"]` 但 command 写 `--gpu cuda:0`——实际进程跑在物理 GPU 1（CUDA_VISIBLE_DEVICES 映射），已完成，不影响
- analysis.tex 中 Llama 数据已更新为 hires 值（0.57, 0.85），**不要回退到旧 standard 值**（0.34, 0.71）
- Scatter 图 (`fig_concentration_scatter`) 不在论文 .tex 中引用——修改它不需要重编译论文

### 2. 🖥️ 基础设施快照
- 服务器：`westd-37397(root)`，工作目录 `/root/ratekv`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型路径：`/root/autodl-tmp/models/` 下有 Llama-3.1-8B、Mistral-7B-v0.3、Yi-1.5-9B；Gemma-2 在 `/root/autodl-tmp/.hf_cache/google/gemma-2-9b`；Qwen 在 `/root/autodl-tmp/.hf_cache/`
- Hires 校准数据：`/root/ratekv/calibration_hires.json`（64 seq × 2048 tok）
- 活跃进程：PID 268242（Gemma-2 hires profiling, GPU 0, ~20GB, ETA ~00:00 UTC）
- 本地论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/`

### 3. 📊 当前状态
**刚完成的审查**：
- Mistral v4 hires profiling：concentration=0.24, t1/t5=0.41（Table 3 旧值 0.22/0.18 需更新）→ 已报 Director [warning]
- Heatmap 修复（`generate_hires_heatmap.py`）：Llama/Yi/Mistral/Qwen 用 hires 数据，Gemma-2 标星号用 standard → 审查通过，已报 Director [info]
- Scatter delta 修复 worker 完成但**我未验证新数据是否正确**（原问题：Mistral=-0.432 应为-0.03，Yi=-0.096 应为 0.00）
- Llama C4 hires cross-dataset 实验失败：脚本名写错（`run_llama_c4_hires_crossdataset.py` vs 实际 `run_llama_c4_cross_dataset.py`）→ Agent 应已看到，未报 Director

**Registry RUNNING/ANALYZING**：
- `gemma2_hires_bf16_2bitonly` — ANALYZING（误标），实际 GPU 0 仍在跑，ETA ~00:00 UTC

### 4. 📋 待办
- Gemma-2 hires 结果文件出现 → 核实 concentration / t1/t5，对比 Table 3 standard 值（0.23, 0.18），确认 Flat 分类是否不变，报 Director
- Gemma-2 hires 完成后 → 检查 Agent 是否重跑 `generate_hires_heatmap.py` 去掉 Gemma-2 星号
- Scatter delta 修复 → 读 `gen_scatter_concentration.py` 验证 Mistral/Yi 新值是否与 Table 1 一致
- analysis.tex Mistral 值更新（0.22→0.24, 0.18→0.41）→ 确认 Agent 执行后检查 line 28（需拆分 Mistral/Gemma-2 共享描述）、line 43（Table 3）、line 72（diagnostic）
- Llama C4 cross-dataset 若重试 → 检查脚本名是否修正为 `run_llama_c4_cross_dataset.py`（已存在于服务器）或确认是否写了新脚本 `run_llama_c4_hires_crossdataset.py`

### 5. 🎯 战略上下文
- **核心结论**：只有 Qwen（spread, 0.61/0.57）从 constrained MCKP 获益 27.3%；Yi/Llama 是 spike（高 concentration 但单 outlier），Mistral/Gemma-2 是 flat——joint diagnostic（concentration ≥0.50 AND t1/t5 ≤0.70）正确分类全部 5 模型
- **最易判断错的事**：Llama hires constrained MCKP **比 uniform 差**（8.5042 vs 8.4701），但 standard MCKP 比 uniform 略好（8.4498 vs 8.4701）。Table 1 保留 standard 值 8.45 是正确的——不要因为 hires 结果而改 Table 1 Llama PPL
- **Qwen 数据路径变更**：heatmap 新脚本用 `hires_profiles.json`（20200 bytes, May 15）替代旧 `ppl_profiles_hires.json`（15525 bytes, May 14）——需确认论文 Qwen 值（0.61/0.57）仍与新文件一致
- **Flat 类别描述需调整**：Mistral hires t1/t5=0.41 不再算 "low"，Flat 定义应仅用 concentration < 0.50，去掉 "low t1/t5" 条件


---
