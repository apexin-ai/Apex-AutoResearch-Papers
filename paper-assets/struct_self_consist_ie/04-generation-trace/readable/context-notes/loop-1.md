# director / loop_1.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`b56fe88b85cb10833d80.json`](../../sessions/b5/b56fe88b85cb10833d80.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-14T08:43:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0-3（autodl-5090 全部 4 张 RTX 5090 32GB）。不存在其他服务器。
- AutoDL 根分区 30GB，所有大文件必须放 `/root/autodl-tmp/`
- ft_002_v2 LoRA r=32 在单卡 32GB 上需要 `batch_size=2 + gradient_checkpointing=true`，否则 step ~73 OOM（已踩过一次）
- MVP PASS 标准（D002/D003）：RE ρ_sj ≥ 0.40 (full, gold-nonempty) AND ρ_sj > ρ_fk AND oracle headroom ≥ 2 F1。RE 是关键 subtask，NER 单独通过不算 PASS。
- Span realignment 是标准后处理，已集成默认开启。论文中需明确说明。

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-5090`，SSH: `ssh -p 21071 root@connect.bjb1.seetacloud.com`，密钥 `~/.ssh/id_ed25519`
- 工作目录：`/root/autodl-tmp/struct_self_consist_ie`
- Python：conda base (`/root/miniconda3/bin/python`)，env 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 环境初始化：`source /etc/network_turbo && source /root/autodl-tmp/struct_self_consist_ie/env.sh`
- 模型：ft_001 merged → `checkpoints/qwen3-8b-scierc-merged/`；ft_002_v2 LoRA → `checkpoints/qwen3-8b-scierc-lora-v2/`（需 merge）
- 基座模型：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
- 数据：SciERC → `data/scierc/{train,dev,test}.jsonl`（train 1861 / dev 275 / test 551 句）
- 代码：`code/` 下 `data_utils.py`, `evaluation.py`, `consistency.py`, `sampling.py`, `run_mvp_pilot.py`
- 活跃进程：ft_002_v2 训练应已完成（5 epochs, ~29min）；Gate 0 eval Worker 可能正在跑或刚完成

### 3. 📊 当前状态
ft_002_v2（LoRA r=32, 5 epochs）训练完成，Agent 正在执行 Gate 0 评测（merge LoRA → greedy eval → NER/RE F1）。这是 MVP 的关键判定点。

**Registry 关键条目**：
- ft_001: DONE, conclusion="success"（实际 gate0 partial: NER 60.4% PASS / RE 33.8% FAIL）
- ft_002: DONE/FAILED（OOM at step 73）
- ft_002_v2: 训练完成，正在 Gate 0 eval
- mvp_pilot_001: DONE/negative（ft_001 模型，RE full ρ=0.254 FAIL）
- mvp_pilot_003: DONE/negative（ft_001 模型修复版，NER ρ=0.381, RE full ρ=0.237 FAIL）

**等待中**：ft_002_v2 Gate 0 结果 → 决定是否跑 pilot_v4

### 4. 📋 待办
- ft_002_v2 Gate 0 RE F1 ≥ 40% → 立即跑 pilot (N=8, T=1.0, joint, max_tokens=1024, cuda:0)，用 `run_mvp_pilot.py`
- ft_002_v2 Gate 0 RE F1 30-40% → 考虑降 RE 阈值或追加 T=0.7 ablation
- ft_002_v2 Gate 0 RE F1 < 30% → 模型方案需要根本改变（更多数据/更大模型）
- Pilot 结果 RE full ρ_sj ≥ 0.40 + sj>fk → MVP PASS → `complete_mvp()`
- Pilot 结果 RE cond ρ_sj ≥ 0.40 但 full < 0.40 → MARGINAL，追加 N=16 time-boxed 1 天
- Pilot 结果 RE ρ < 0.30 across all → FAIL，pivot to negative finding 或 ARR August

### 5. 🎯 战略上下文
**决策链**：D001(MVP方案) → D002(收紧标准) → D003(SciERC RE替代EAE) → D004(Gate0 partial, 方案C) → D005(pilot FAIL but positive signals) → D006(stay-the-course等ft_002_v2)

**核心发现**：假设方向正确，瓶颈是模型 RE 质量。证据：(1) NER 全面支持 SJ>FK（ρ=0.381, 优势 4.5pp）；(2) RE conditional ρ 排除 knowledge-gap 后 SJ>FK (+0.063)；(3) Oracle headroom 巨大（NER +16pp, RE +22pp）。

**易错点**：
- RE 28% test instances 无 gold relations → correlation 计算必须排除 gold-empty，否则 artifact 严重扭曲 ρ
- pilot_001 vs pilot_003 RE ρ 下降是实验混杂（不同脚本+不同 max_tokens），不是真实退化
- Qwen3 训练时自动加 `&lt;think>` 块，推理时必须 `enable_thinking=False` 否则与 XGrammar 冲突
- Worker 有过"声称 done 但实际未执行"的情况，关键操作后必须 SSH 验证
- DDL: ARR May 2026-05-25（距今 11 天），备选 ARR August 2026-08-03


---
