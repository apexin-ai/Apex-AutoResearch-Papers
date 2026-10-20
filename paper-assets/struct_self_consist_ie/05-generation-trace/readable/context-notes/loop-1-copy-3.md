# reviewer / loop_1.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`79b01bd6bc9932d92dc5.json`](../../sessions/79/79b01bd6bc9932d92dc5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T08:43:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1, cuda:2, cuda:3（autodl-5090 四卡全分配给本项目）
- ft_002_v2 训练用 CUDA_VISIBLE_DEVICES=1，LLaMA Factory 不在 yaml 里指定 GPU，必须靠环境变量
- train_config_v2.yaml 已改为 batch=2 + grad_accum=8 + gradient_checkpointing=true，**不要改回 batch=4**，32GB 5090 单卡会 OOM（step 73 处已验证两次）
- LoRA 适配器不能直接喂 vLLM，必须先 merge 成完整模型（mvp_pilot_002 就是因为这个 failed）
- AutoDL 网络：pip/git 前必须 `source /etc/network_turbo`；HF 下载设 `HF_HUB_DISABLE_XET=1` + SSL 证书环境变量

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (root) + gpu-5090-4x-2 (root)，4× RTX 5090 32GB
- 工作目录：`/root/autodl-tmp/struct_self_consist_ie`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 基础模型：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`
- ft_001 LoRA：`checkpoints/qwen3-8b-scierc-lora/`
- ft_001 merged：`checkpoints/qwen3-8b-scierc-merged/`（pilot_001/003 用的）
- ft_002_v2 LoRA：`checkpoints/qwen3-8b-scierc-lora-v2/`（训练完成，**尚未 merge**）
- 数据：`data/scierc/processed_data/`（551 test instances）
- 活跃进程：截至 handoff 时四卡全空闲，无活跃 PID
- GPU 3 有驱动残留（100% util / 0 MiB），非真实负载

### 3. 📊 当前状态
**刚完成但尚未发审查报告的**：
- ft_002_v2 训练完成（5 epochs, 585 steps, 28m41s），train_loss=0.0806, eval_loss=0.089
- mvp_pilot_003 已完成（用 ft_001 模型），verdict=FAIL，RE ρ_sj=0.237(full)/0.300(cond)

**Registry 状态**（6 条）：
- ft_001: DONE, conclusion="success"（实际 gate0_pass=false，conclusion 从未被修正，已标记 6 次）
- ft_002: DONE, conclusion="killed"（OOM，已关闭）
- ft_002_v2: **RUNNING**（实际已完成，status 未更新为 DONE）
- mvp_pilot_001: DONE, conclusion="negative", verdict=FAIL
- mvp_pilot_002: **ANALYZING**（实际 failed，status 未关闭）
- mvp_pilot_003: DONE, conclusion="negative", verdict=FAIL

**等待中**：ft_002_v2 需要 merge → gate0 评估 → 如果 RE F1 ≥ 40% 则跑 pilot

### 4. 📋 待办（条件触发式）
- ft_002_v2 LoRA merge 完成 → gate0 评估（realign + strict match），核查 NER/RE F1 是否过 40% 阈值
- gate0 RE F1 ≥ 40% → 用 merged 模型跑 mvp_pilot（N=8, T=1.0, joint subtask），关注 RE ρ_sj 是否 > 0.30
- gate0 RE F1 < 40% → 方案 C 宣告失败，需要 Director 决策（数据增强？更大模型？pivot？）
- 任何训练/推理启动 → 验证 CUDA_VISIBLE_DEVICES 在白名单内
- eval_loss 趋势：step 300 最低 0.0817，之后回升至 0.089（step 585）。**可能过拟合**，checkpoint-300 可能比 final 更优。建议 gate0 对比 checkpoint-300 vs checkpoint-585

### 5. 🎯 战略上下文
- **核心假设**：fine-tuned 模型的结构自一致性（soft Jaccard）与 per-instance F1 相关，可作为 test-time compute 自适应分配的置信信号
- **Gate 0**：NER F1 ≥ 56, RE F1 ≥ 40（SOTA 的 85%）。ft_001 NER 通过（60.4%），RE 未通过（33.8%）
- **Gate 1**：RE ρ_sj ≥ 0.40, sj > fk, oracle headroom ≥ 2pp。目前最好结果是 pilot_003 RE cond ρ_sj=0.300，距 0.40 差距大
- **mvp_pilot_003 vs 001 对比**（同一模型 ft_001）：parse failures 0 vs 164（代码修复），但 RE ρ 反而下降（cond: 0.352→0.300）。原因不明，可能 max_tokens 512→1024 或不同脚本（mvp_pilot.py vs run_mvp_pilot.py）导致。**不要简单认为"parse failure 修复=结果更好"**
- **eval_loss 拐点在 step 300**（epoch 2.57），之后轻微上升。如果 gate0 用 final checkpoint 效果不好，**一定要试 checkpoint-300/400**
- **ft_001 conclusion="success" 是历史遗留错误**，已标记 6 次未修正。不要信这个字段，看 gate0_pass=false
- **deadline**：ARR May 2026 截稿 2026-05-25，距今 11 天。项目 phase=mvp。


---
