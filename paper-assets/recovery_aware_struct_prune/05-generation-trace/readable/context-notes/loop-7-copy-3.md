# reviewer / loop_7.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`873f8e39440862870239.json`](../../sessions/87/873f8e39440862870239.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-15T13:55:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- westb-23072 只能用 cuda:0, cuda:1（C001）
- westd-11672 只能用 cuda:0, cuda:1（C003）
- westd 上 `--gpu N` 参数不可靠，必须用 `CUDA_VISIBLE_DEVICES=N` 前缀控制物理 GPU（已因此 OOM 3 次）
- westd 根分区磁盘紧张，SFT checkpoint 必须 `save_total_limit=1` 或 `save_strategy=no`（已因序列化+磁盘满崩溃 2 次）
- 原始 "RASP 29% vs Standard 1%" claim 已被证伪（eval bug），任何引用此数据的结论都是错的

### 2. 🖥️ 基础设施快照
- **westb-23072**（root）：`/root/recovery_aware_struct_prune`，conda base `/root/miniconda3`
  - 模型：`/root/autodl-tmp/pruned_rasp_20`, `/root/autodl-tmp/pruned_standard_20`
  - SFT checkpoints：`/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20/`, `sft_standard_20/`
  - wandb entity: xiaoyucorynne-, project: recovery_aware_struct_prune
- **westd-11672**（root）：`/root/recovery_aware_struct_prune`，conda base `/root/miniconda3`
  - Alpha ablation 模型：`/root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_{0.0..4.0}`
  - SFT ablation：`/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_4.0`（已完成）
  - GraSP 模型：`/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/`

### 3. 📊 当前状态
**我刚完成的审查**：SFT α=4.0 成功（62%），GraSP baseline 部分结果（8% at 50 samples），GRPO v5 崩溃分析，OOM 清理确认。

**RUNNING**：
- `grpo_stage2_rasp_20_v6`：westb GPU 0，max_completion_length=1024，是 v5 truncation 修复版。**这是决定性实验**。
- `grpo_stage2_standard_20_v6`：westb GPU 1，同参数负对照。

**PREPARING（westd）**：
- `sft_grasp_20_westd`：PID 38514 on GPU 0，GraSP SFT（8%→?），刚开始加载
- `grasp_baseline_westd` eval N=100：PID 38120 on GPU 0，与 SFT 共享 GPU（潜在 OOM 风险）
- `sft-alpha-1p0`：新注册，用途不明
- westd GPU 1 完全空闲

### 4. 📋 待办（条件触发式）
- GRPO v6 RASP 完成 → **最高优先级审查**：对比 GRPO v6 Standard，如果 RASP > Standard ≥5pp 则 recovery 故事成立；如果差距 <5pp 项目需要 pivot
- GRPO v6 出现 reward=0 / grad_norm→0 → 立即报 Director，这是第 7 次 GRPO 失败，方法论本身有问题
- GraSP SFT 完成 → 审查 post-SFT accuracy，与 Standard 64% / RASP 57% / α=4.0 62% 对比
- GraSP eval N=100 + SFT 在同一 GPU 0 上 → 监控是否 OOM
- westd GPU 1 持续空闲 → 提醒 Director 安排任务（SFT α=1.0 或 α=2.0）

### 5. 🎯 战略上下文
**核心数据链**：
- Post-prune: Standard 27%, RASP 31%, α=4.0 40%, GraSP ~8%（差异大部分在噪声内，除了 GraSP 和 α=4.0）
- Post-SFT: Standard 64%, α=4.0 62%, RASP 57%（Standard 恢复最好，与 RASP 叙事矛盾）
- Post-GRPO: **未知——v6 是最后机会**。v1-v5 全部失败（sampling collapse / truncation / OOM / shape mismatch）

**最容易判断错的事**：
1. Agent 的 registry notes 说 "α=4.0 is +5pp higher than RASP, confirming higher α amplifies recovery"——这是 spin。α=4.0 的 62% vs RASP 的 57% 在 ~1 SE 范围内，不是 confirmation。而且 Standard 64% > α=4.0 62%，叙事方向反了。
2. 不要信 registry 里旧的 `mvp_rasp_pipeline_v4` notes（仍写着 "29x advantage"），那是 eval bug 时代的遗留。
3. westd calibration=256 vs westb calibration=512——两边的 pruned 模型不完全相同，直接对比要加 caveat。
4. GRPO 在这个项目上已失败 6 次（v1-v5 + Standard v2），根因是 pruned R1 distill 模型在 sampling mode 下退化。v6 用 1024 tokens + beta=0.01 KL + temp=0.4 + rep_penalty=1.15 是最后一搏，如果还崩就是方法论问题。


---
