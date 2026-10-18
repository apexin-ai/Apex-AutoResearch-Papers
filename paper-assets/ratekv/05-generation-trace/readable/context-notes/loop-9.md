# agent / loop_9.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`12b117a00cdc86a238bf.json`](../../sessions/12/12b117a00cdc86a238bf.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-15T12:57:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-37397 的 cuda:0 和 cuda:1，不得用其他设备
- t1/t5 canonical 公式：`top1_concentration / top5_concentration`（不是 delta 比值）。脚本修复 Worker 已派但未确认完成，接手后先验证
- KIVI eval 没有 baseline——不要引用 "KIVI baseline=9.19"，那是误报。论文 baseline 直接对比：Qwen=9.8106, Llama=8.0922
- Gemma-2 eval 必须用 BOS fix（prepend BOS + sliding window stride=512, max_length=2048），否则 PPL=711
- AutoDL 磁盘 205/250GB (82%)，OPT-6.7B 已放弃（下载太慢），不要再尝试下载大模型

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397，2× RTX PRO 6000 Blackwell 96GB
- 工作目录：`/root/ratekv/`
- Python：`/root/miniconda3/bin/python`（conda base，不是 venv）
- HF cache：`/root/autodl-tmp/.hf_cache`（必须设 `HF_HOME`）
- 模型路径：
  - Qwen2.5-7B: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B`
  - Qwen2.5-14B: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-14B`（确认实际路径）
  - Llama-3.1-8B: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B`
  - Pythia-1.4B: `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b`
  - Gemma-2-9B: `/root/autodl-tmp/.hf_cache/google/gemma-2-9b`
  - Yi-1.5-9B, Mistral-7B-v0.3: 在 `/root/autodl-tmp/` 下
- 活跃进程：
  - Pythia constrained pipeline: Worker `worker_exp_pythia14b_constrained_pipeline_20260515T123706` running
  - t1/t5 脚本修复: Worker `worker_code_fix_t1t5_scripts_20260515T121718` running
  - Qwen14B constrained: PID 329678 可能还在跑（tmux session），检查日志 `/root/ratekv/logs/qwen14b_constrained_pipeline.log`
- Artifacts 目录：`/root/ratekv/artifacts/`（服务器端），本地 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/`

### 3. 📊 当前状态
**刚完成**：
- KIVI baseline 全部 8 个 PPL 数（2 models × 2 bits × r128/r0）→ registry DONE
- W1 profiling：Qwen14B (Flat, conc=0.33, t1/t5=0.68) + Pythia (Flat, conc=0.24, t1/t5=0.28) → registry DONE
- qwen14b_constrained_pipeline → registry DONE (success)
- Registry 已修正：所有 shape 从 Spike → Flat（t1/t5 公式 bug 修复后）

**正在跑**：
- `worker_exp_pythia14b_constrained_pipeline_20260515T123706`：cuda:0 Pythia constrained vs uniform（~10-15min）
- `worker_code_fix_t1t5_scripts_20260515T121718`：修复服务器上 profiling 脚本的 t1/t5 计算

**等待**：
- Pythia constrained Worker 回调 → 提取结果 → registry → 汇报 Director
- t1/t5 fix Worker 回调 → 确认修复

### 4. 📋 待办
- Pythia constrained Worker 完成 → 提取 PPL 数（uniform vs constrained vs unconstrained），验证 Flat 预测（MCKP ≈ uniform），registry → DONE，汇报 Director
- t1/t5 fix Worker 完成 → 确认所有 profiling 脚本一致
- Director 审批 long-context eval → 写脚本 Qwen-7B 8K sequence PPL（Dream P2 建议）
- cuda:1 空闲 → 等 Director 分配（候选：long-context 8K spot-check / multi-seed / Gemma-2 compounding）
- KIVI 数字需要补 unquantized baseline 验证（eval 代码相同，理论上 baseline 应匹配论文数字，但建议跑一次确认）

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 ARR May 25（距今 ~10 天）
- **核心 narrative (D053)**：concentration-dependent benefit + cardinality constraint。三档：Spread (catastrophic) / Flat (solver irrelevant) / 中间。Qwen-7B 是唯一 Spread
- **7 模型 shape 分布修正后**：Spread ×1 (Qwen-7B), Flat ×4 (Qwen-14B, Pythia, Mistral, Gemma-2), Spike ×2 (Yi, Llama)——注意 Yi/Llama 的 shape 可能也需要用 canonical t1/t5 重新计算
- **易踩坑**：
  1. Yi-1.5 和 Llama 的 t1/t5 可能也受旧公式影响——registry 里存的是旧值，接手后应检查这两个模型的 shape 是否需要修正
  2. Qwen14B constrained 结果文件可能还在服务器上等待提取（PID 329678），检查 `/root/ratekv/artifacts/qwen14b_constrained_pipeline_results.json`
  3. KIVI 对比时记住：KIVI 用 asymmetric per-channel + group_size=32，我们用 symmetric per-head 无分组——方法论差异大，论文定位是 "complementary approach" 而非 "strictly better"
  4. Pythia-1.4B 是 1.4B 不是 14B，文件名 `run_pythia14b_hires_profiling.py` 容易误读
- **Director 实验队列**（按优先级）：KIVI ✅ → Pythia constrained (running) → long-context 8K → multi-seed → Gemma-2 compounding


---
