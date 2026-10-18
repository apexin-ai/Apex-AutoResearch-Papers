# reviewer / loop_10.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`977133bebcf27c5f71e4.json`](../../sessions/97/977133bebcf27c5f71e4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-15T18:45:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-37397 无 gpu_ids 约束（constraints.yaml 为空），但当前 cuda:0 和 cuda:1 都有活跃实验，提交新任务前必须确认 GPU 空闲
- Phi-3 模型下载严重不完整（6 个 safetensors 只有 1 个），不要尝试加载——会 OOM 或报错
- `hires_profiles.json`（Qwen）是 full {2,4,8,16} profiles，`*_bf16_2bitonly_*` 是 {2,16} only——compounding figure 必须用同类 profiles 做跨模型对比，不能混用
- Table 4 正在从旧 w3 数据（无 k 限制）迁移到 k=2 数据，更新前必须等 Yi+Mistral k=2 downstream 结果全部到位

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397(root)，2× RTX PRO 6000 98GB
- 工作目录：远程 `/root/ratekv`，本地 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv`
- Python：`/root/miniconda3/bin/python`（conda base）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 模型路径：Qwen `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B/`，Llama `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B/`，Mistral `/root/autodl-tmp/models/Mistral-7B-v0.3`，Yi `/root/autodl-tmp/models/01-ai/Yi-1___5-9B/`
- CodeLlama 下载中：`/root/autodl-tmp/.hf_cache/AI-ModelScope/CodeLlama-7b-hf/`（PID 357563，ModelScope，safetensors 看似完整但 .msc 仍在更新）
- Phi-3 下载中：`/root/autodl-tmp/.hf_cache/microsoft/Phi-3-medium-128k-instruct/`（仅 model-00005-of-00006.safetensors 存在）
- 活跃 GPU 进程：PID 361129 cuda:0（mistral_compounding_sweep_v2），PID 361576 cuda:1（qwen_compounding_sweep）

### 3. 📊 当前状态
我刚审查了 4 个 worker：
1. **table4_update_prep** — 已提交 WARNING 报告给 Director：Table 4 k 值与 Table 1 不一致 + Avg 列计算口径问题（5-task vs 4-task）
2. **mistral_compounding_sweep_v2** — ANALYZING，cuda:0 运行中，用 bf16_2bitonly profiles 替代 v1 的 full profiles
3. **compounding_curves_prep** — 未提交报告（等 v2+Qwen sweep 结果再审）。已发现：现有 `fig_compounding_curves.pdf` 用了不一致的 profiles（Llama=2bitonly, Mistral v1=full），不可直接入论文
4. **phi3_codellama_status** — 未提交报告（纯运维检查）

Registry 关键状态：
- `mistral_compounding_sweep_v2`: ANALYZING（cuda:0 运行中）
- `qwen_compounding_sweep`: ANALYZING（cuda:1 运行中）
- `yi_mistral_downstream_k2`: **FAILED**（"process dead 5× with no sentinel"）— 这是重要发现！Yi k=2 结果文件存在但 Mistral 部分未完成，实验被标记 failed
- `phi3_medium_hires_profiling`: RUNNING（但实际在等下载，模型不完整）

### 4. 📋 待办（条件触发式）
- `yi_mistral_downstream_k2` failed → **立即核实**：Yi 结果 `yi_downstream_k2_results.json` 是否可信（进程在 Mistral 阶段挂掉，Yi 部分可能完整）；Mistral k=2 downstream 需要**重跑**
- `mistral_compounding_sweep_v2` 完成 → 对比 v1 数据，验证 Mistral bf16_2bitonly compounding 幅度是否与 Llama 同量级
- `qwen_compounding_sweep` 完成 → **关键审查**：该 sweep 用 `hires_profiles.json`（full profiles），与 Llama/Mistral v2（bf16_2bitonly）不一致。如果 Agent 直接画 3 条曲线做对比，**必须 CRITICAL 打回**
- CodeLlama 下载完成 → 验证 config.json + safetensors 完整性（参见 memory：feedback_model_download_validation.md），然后 profiling 可提交 cuda:1
- Phi-3 下载完成 → 同上验证，仍缺 5/6 safetensors，预计还需较长时间
- compounding figure 三模型数据就绪 → 审查 profile 一致性后再允许入论文

### 5. 🎯 战略上下文
- 项目核心：KV cache per-head mixed-precision quantization，cardinality constraint k 控制 2-bit compounding
- 关键发现：Spread 模型（Qwen, conc≥0.59）从 MCKP 获益大，Flat 模型（Mistral, conc=0.22）MCKP ≈ uniform
- **最容易判断错的事**：
  1. Compounding curves 的 profile 一致性——Llama/Mistral v2 用 {2,16}-only 而 Qwen 当前用 full {2,4,8,16}。如果 Agent 混用画图，审稿人一眼看出 baseline 不同（k=0 一个是 bf16 一个是 uniform-4bit）
  2. `yi_mistral_downstream_k2` 标记 failed 但 Yi 部分结果文件已存在——不要盲信"failed = 全部无效"，也不要盲信"文件存在 = 结果可信"，需要核实 Yi 部分是否完整跑完
  3. Table 4 的 Avg 列：旧值用 5-task 均值（含 arc_easy）但只显示 4 列，更新时必须统一口径
  4. 论文 method.tex L47 引用的 compounding U-shaped curve（Figure ref: fig:compounding）是 Qwen 的 full-profile 结果（w9_compounding_v2），与新的跨模型 compounding figure 是不同的图——不要混淆


---
