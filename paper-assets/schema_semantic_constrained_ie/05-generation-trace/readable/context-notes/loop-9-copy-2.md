# agent / loop_9.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`ce24e80b56020d033c50.json`](../../sessions/ce/ce24e80b56020d033c50.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-15T17:34:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: **仅 cuda:0, cuda:1 on westd-16980**，无其他服务器/GPU 可用
- `type_mask_processor.py` 当前可能是 CF fallback 版本（为已杀的 w1_cf_fallback_docred 恢复的）。**跑 constrained eval 前必须确认是 clean 版本**，服务器上有 3 个版本并存：clean(.py), CF fallback(_cf_fallback.py), backup(.py.bak)
- `kill_job` 不杀子进程——kill 后必须 `nvidia-smi | grep python` 确认无残留（历史事故: PID 276937 存活 51min 占 GPU）
- `submit_training_job` 命令必须用 `bash -c` 包裹，内含 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- WANDB_MODE=disabled（项目未配 wandb key），不要尝试 wandb 相关操作

### 2. 🖥️ 基础设施快照
- **服务器**: westd-16980, 2× NVIDIA RTX PRO 6000 Blackwell (94GB each), CUDA 12.8
- **工作目录**: `/root/schema_semantic_constrained_ie`
- **Python**: `/root/miniconda3/bin/python` (conda base), torch 2.10.0+cu128, transformers 4.57.6
- **环境激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型路径**:
  - Qwen3-8B: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`
  - Llama-3.1-8B-Instruct: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`
  - Qwen LoRA merged: `/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged`
  - Llama LoRA merged: 路径未记录在 memory.md，需 SSH 确认（训练已完成 w5_llama_lora_scierc_training=success）
- **活跃进程**: 无（reconcile_crons=0，无 RUNNING 实验）
- **cuda:0**: 空闲（Llama LoRA 训练已完成）
- **cuda:1**: 空闲（w1_cf_fallback_docred 已杀）

### 3. 📊 当前状态
上一轮完成了 W5 composability 全线验证（Qwen SciERC 2×2 matrix 完整）和 Llama LoRA SciERC 训练。正在推进 Llama SciERC 2×2 matrix 的最后一格。

**Registry 非 DONE 实验**:
- `w5_llama_lora_scierc_constrained_eval` — **PENDING**（等审批）：Fine-tuned Llama + OntoCoDec constrained eval，Llama SciERC 2×2 最后一格
- `w1_cf_fallback_llama_docred` — PREPARING/killed：已取消（D027）
- `w1_cf_fallback_llama_scierc` — PREPARING/killed：已取消（D020）

**等待中**:
- w5_llama_lora_scierc_constrained_eval 审批通过 → 需提交到 cuda:0 或 cuda:1
- Paper Agent 正在写入 2×2 composability matrix + 更新 Abstract/Conclusion（W1 写作 in_progress）
- 无活跃 Worker / Cron 回调

**统计**: 26 success / 1 negative / 2 killed / 1 pending = 32 total

### 4. 📋 待办（条件触发式）
- **w5_llama_lora_scierc_constrained_eval 审批通过** → (1) SSH 确认 Llama LoRA merged checkpoint 路径 (2) 确认 type_mask_processor.py 是 clean 版本 (3) submit_on_allocated 提交 constrained eval
- **Llama constrained eval 完成 (success)** → 构建 Llama SciERC 2×2 matrix，与 Qwen 2×2 对比，更新 paper → 强化 cross-model composability claim
- **Llama constrained eval 完成 (negative: DR 未降)** → red-section framing 提案，可能需要限定 composability claim 为 Qwen-specific
- **Paper Agent W1 写作完成** → 全文编译，Round 2 review
- **May 19** → 内部稿交付 deadline
- **May 25** → EMNLP ARR 提交 deadline
- **两块 GPU 都空着** → 除了 Llama constrained eval，考虑是否启动 DocRED LoRA fine-tune（ROADMAP 标为"可选"）

### 5. 🎯 战略上下文
**项目核心**: OntoCoDec = 两层约束解码（grammar + semantic），编译 IE ontology schema 为 token-level constraints，消除 LLM IE 的 ontology violations。

**决策链关键节点**:
- D025: W5 composability 确认——FT+OntoCoDec DR=0%, F1 -0.09pp（Qwen SciERC）
- D020: W1 CF fallback 定为 analytical finding（CF↔DR 根本性张力，非实验修复）
- D027: 杀掉 w1_cf_fallback_docred（代码实际没有 CF fallback 逻辑，跑的是重复 full_s1）

**目标分数路径**: 当前估 3.75-4.0/5 (Accept)，Llama LoRA 成功 → 4.0+ (强 Accept)

**易错点**:
- Llama LoRA merged checkpoint 路径未记录——**第一件事必须 SSH 确认**，不要猜
- `type_mask_processor.py` 可能仍是 CF fallback 版本——constrained eval 前必须检查并恢复 clean 版本
- DocRED full_s1 的 DR 只降到 10.19%（vs SciERC 0.93%），原因是 constraint tightness 差异（DocRED avg 0.842 vs SciERC 0.333）——这是 feature 不是 bug，论文已定位为 "effectiveness scales inversely with constraint tightness"
- Issue Tracker 16 项中 15 已 resolved，W1 (CF fallback) 是最后一项（analytical finding + 写作中）
- **两块 GPU 当前全部空闲**——违反"分配了但没跑即失职"红线，需尽快提交 Llama constrained eval 或向 Director 汇报空闲状态


---
