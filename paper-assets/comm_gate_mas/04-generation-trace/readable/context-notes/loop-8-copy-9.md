# reviewer / loop_8.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`2322c0bdfe295737a89f.json`](../../sessions/23/2322c0bdfe295737a89f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-04-28T00:39:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- comm_gate_mas 只能用 **cuda:1**（westb-4x6000-a）。cuda:0/2/3 是其他项目，越界即 CRITICAL
- vLLM 启动命令必须带 `CUDA_VISIBLE_DEVICES=1`，否则 vLLM 抢 cuda:0（历史教训，见 memory feedback_vllm_cuda_visible_devices.md）
- GPU 实验启动前必须 `pgrep` 检查是否已有同名进程（反重复进程 guard，历史两次踩坑）
- Reviewer 角色只读——不执行实验、不修改文件，唯一输出渠道是 `reviewer_post_to_director`

### 2. 🖥️ 基础设施快照
- 服务器：**westb-4x6000-a**，工作目录 `/root/autodl-tmp/comm_gate_mas`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型路径：`/root/autodl-tmp/models/Llama-3.1-8B-Instruct`（当前 vLLM 服务），`Qwen2.5-7B-Instruct`/`Qwen3-8B`/`72B-AWQ` 等均在同目录
- vLLM 当前状态：**Llama-3.1-8B-Instruct on port 8001, cuda:1**（PID 997411/997778）
- P2 实验进程：PID 999735（`pruning_validation.py --mode online_oracle`，seed_42 运行中）
- GPU 0: pseudo_label_bias_decomp 项目；GPU 3: al_calib_imbalance_shift 项目——与我无关

### 3. 📊 当前状态
**刚完成的审查**：
1. stochastic_10seed_qwen_t07 — DONE, success。10-seed 全部验证通过（Δ=+0.30±1.80pp, TOST δ=-3pp p=0.000129）。聚合脚本有 bug（全零输出）但原始 JSON 数据有效，分析 worker 绕过了 bug
2. 写作整合审查 — 发现 **abstract 与正文矛盾**（abstract 写 "single seed" 但正文已是 10 seeds），已提 CRITICAL 给 Director
3. vLLM 切换到 Llama — 确认完成，P2 已启动

**Registry 关键状态**：
- `p2_oracle_online_llama_v3`: **RUNNING**（3 seeds × 200 tasks，预计 ~3h）
- `llama_length_only_gsm8k_5seed`: PREPARING（P2 之后排队）
- `stochastic_10seed_qwen_t07`: DONE ✅
- `prompt_mod_qwen25_gsm8k_v2`: DONE ✅

**等待中**：P2 完成回调 → 需审查 oracle online Llama 结果

### 4. 📋 待办
- P2 oracle_online_llama_v3 完成 → 审查 3-seed aggregate metrics（核对 non-inferiority δ=-3pp 是否 hold），检查 oracle cache hit rate，验证 CUDA_VISIBLE_DEVICES=1
- llama_length_only_5seed 启动 → 验证 GPU 边界 + seed 列表与 registry 一致
- Llama heuristic 3-seed 启动 → 同上
- Director 修复 abstract "single seed" → 确认修改后 abstract 与 body 一致
- 若收到 Framing 提案 → 立即 Read `negative-framing-review` skill，按四维度审查
- 写作章节审查请求 → 检查 red-section skill 是否被 Agent 查看（L1 硬约束 #1）

### 5. 🎯 战略上下文
- **核心叙事**：Dissociation finding — perturbation sensitivity ≠ pruning safety，ack 消息最易扰动但可安全剪枝
- **D210**：Qwen stochastic 10-seed 通过，Llama stochastic 多 seed 跳过（已有 2-seed 1000 tasks 的 Fisher combined 证据，pooled Δ=-2.2pp NS）。"Backbone-dependent boundary" 叙事
- **D208**：P1 oracle precompute 跳过，直接用现有 GPT-4o oracle（1760/1782 msgs）
- **NeurIPS DDL**：Abstract 5/3-4, Paper 5/5-6。P2 硬限 4/29 00:00 UTC
- **易错点**：
  - 不要把 Llama stochastic 的 "single seed" 与 "2-seed Fisher combined" 混淆——后者是 2 batches × 500 tasks，不是 2 random seeds
  - Qwen3 的 -14pp 是 char<80 threshold 结果（offline replay），char<30 的结果是 -1pp NS（online）——两种 mode 不可直接对比
  - `scripts/run_10seed_stochastic.sh` 的聚合解析有 bug（输出全零），但原始 seed JSON 文件数据正确。如果有人引用脚本聚合输出，必须警告
  - abstract 目前仍写 "single seed"，这是已提交的 CRITICAL，等 Director 处理


---
