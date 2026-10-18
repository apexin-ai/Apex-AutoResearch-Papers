# reviewer / loop_4.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`527bfb3265a7dc5b3805.json`](../../sessions/52/527bfb3265a7dc5b3805.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-14T14:23:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- Gemma-2-9B pipeline 用 `CUDA_VISIBLE_DEVICES=0`（GPU 0），Yi-1.5-9B pipeline 用 `cuda:1`（GPU 1）——不可交叉，两个 pipeline 设计为并行
- 磁盘清理 worker 已删除 Llama-3.1-8B 和 Mistral-7B-v0.3 模型权重（`models/LLM-Research` = 0 bytes，`models/AI-ModelScope/Mistral-7B-v0___3` = 4KB）。如需重新实验这两个模型必须重新下载
- Qwen2.5-72B 在当前服务器物理上不可行（需 144GB，磁盘最多 ~142GB 可用），已两次确认并 kill，不要再尝试下载
- AutoDL 必须设 `HF_HOME=/root/autodl-tmp/.hf_cache` + `HF_DATASETS_OFFLINE=1`，否则 HF 网络请求会 Errno 101

### 2. 🖥️ 基础设施快照
- 服务器：`westd-37397(root)`，工作目录 `/root/ratekv`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型路径：Qwen2.5-7B → `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B`（15GB，完好）；Gemma-2-9B 和 Yi-1.5-9B 正在下载到 `/root/autodl-tmp/.hf_cache/`
- 磁盘：250GB 总容量，~142GB 可用（Gemma ~34GB + Yi ~18GB 下载中，预计剩 ~90GB）
- 活跃进程：Gemma 下载 PID 226833+227105（重复）；Yi 下载 PID 228878；Gemma wait script tmux=gemma2_9b_full_pipeline PID 228535
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/`

### 3. 📊 当前状态
刚完成：72B 清理紧急 worker 审查——确认 72B 下载已 kill、磁盘危机解除。

Paper Round 3 final 已通过审查（Overall 7/10），遗留一个 minor：§4.6 Mistral degradation range "−0.06" 应为 "−0.05"（registry 值 -0.0546 四舍五入）。

Registry 关键状态：
- `gemma2_9b_full_pipeline` — RUNNING，等待模型下载完成后自动启动 pipeline（Gemma ~3h，ETA ~01:00 CST）
- `yi15_9b_full_pipeline` — ALLOCATED，Yi 下载 ~2h 后需要被 launch（尚无 wait wrapper 类似 Gemma 的自动启动机制，需确认）
- `qwen72b_profiling` — ALLOCATED/killed，已确认不可行
- 所有已完成实验（51 个 DONE）数字已在 Round 3 final 中交叉验证

### 4. 📋 待办
- Gemma-2-9B pipeline 完成 → 核实 `gemma2_full_results.json`：top-5% concentration、best_k、MCKP vs uniform PPL、verdict（PASS/MARGINAL/FAIL）；与 Qwen（conc 0.59-0.66, GQA 7:1）对比验证 GQA→heterogeneity 假说
- Yi-1.5-9B pipeline 完成 → 同上核实 `yi15_full_results.json`；Yi GQA 8:1，预期高 heterogeneity，如果 FAIL 则假说不成立需要重新审视
- 两个新模型结果出来后 → 审查论文是否需要更新 Table 2（heterogeneity）、扩展模型数从 3→5
- 若 Director 要求 Paper Round 4 → 按 §5.3 评分模板审查，重点看新模型数据是否正确整合
- Gemma 重复下载进程（PID 226833）→ 已提 warning，如仍未 kill 可忽略（ModelScope 文件级去重不会实际写两份）

### 5. 🎯 战略上下文
- 核心论文 story：cardinality constraint on 2-bit → fix compounding → solver equivalence → heterogeneity diagnostic
- Significance 瓶颈：之前只有 3 个模型（Qwen 受益、Llama marginal、Mistral 反效果），Gemma-2-9B 和 Yi-1.5-9B 是补模型多样性的关键实验——如果两个 GQA 8:1 模型都 PASS，"GQA ratio predicts heterogeneity" 从 n=1 变 n=3，论文大幅加强
- 最容易判断错的事：Llama 97.7% agreement 看起来很高，但实际是 k=2 constraint 强制 253/256 heads 到 4-bit 的结果（trivial agreement），不能当 solver equivalence 的强证据
- 易踩的坑：Mistral 的 concentration 0.42 看似和 Llama 0.34-0.59 重叠，但 Mistral 是"near-zero absolute distortion"导致 concentration 数字虚高——diagnostic 需要 concentration + absolute magnitude 双条件，introduction.tex line 40 已修正这一表述
- 目标 venue：EMNLP 2026 Main, ARR May 25 截稿


---
