# reviewer / loop_1.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`23fdf9c95528c13dedab.json`](../../sessions/23/23fdf9c95528c13dedab.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T10:00:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目配置服务器为 `autodl-5090` + `gpu-5090-2x-2(root)`，probe-002 实际跑在 `autodl-5090 cuda:0` — 未见 constraints.yaml 中有 gpu_ids 白名单，但需留意后续是否新增限制
- `baselines.py` 已修复 CosineSim 方向 bug（增加 `self.invert` 双向搜索），但 probe-multiseed 的 seed=123/456 评估使用了修复前的代码，CosineSim 数值需重跑
- Registry 中 `probe_001.metrics.baseline_cosine_sim` 仍为旧值 0.3129（应为 ~0.5606），尚未更新

### 2. 🖥️ 基础设施快照
- **gpu-5090-2x-2**: root 账号, conda base (`/root/miniconda3/bin/python`), 工作目录 `/root/autodl-tmp/agent_progress_probe`
- **autodl-5090**: root 账号, conda base, 同工作目录（probe-002 在此训练）
- 数据: `data/windows_labeled.jsonl` (59,496 windows), `data/embeddings.pt` (1.12GB, 54,809 windows, 1024-dim Qwen3-Embedding-0.6B)
- Checkpoints: `checkpoints/` (probe-001 seed=42 conf≥2), `checkpoints_full/` (probe-002 conf≥0), `checkpoints_seed123/`, `checkpoints_seed456/`
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/`
- W&B: 未配置（服务器无 WANDB_API_KEY）
- Dream: `dream_20260514T081656` PID 98830, status=imagining（可能已完成，D009 已基于其结果做了决策）

### 3. 📊 当前状态
**刚完成审查**: baseline-meanpool-lr 提交（registry DONE），probe-002 分析（test F1=0.8468），Dream pivot 审稿（D009 → temporal label model framing）

**Registry 实验状态**:
- `emb_001` DONE, `probe_001` DONE, `probe-002` DONE, `baseline-meanpool-lr` DONE
- `probe-multiseed` PENDING（实际已完成 mean=0.9185±0.0113，registry status 未更新）

**等待中**:
- 新 P0 实验启动: temporal-label-model / flyingsquid-baseline / outcome-bp-sensitivity
- cross-agent (OpenHands) 数据准备和 adapter 实现
- baseline-llm-judge（需 API key）
- Re-dream 验证新 framing
- Director 确认 EMNLP 5/25 vs ACL 8月 timeline

### 4. 📋 待办（条件触发式）
- temporal-label-model worker 完成 → 核查是否在 gold set 上显著优于 majority vote（≥5pp 是合理门禁），检查 HMM/temporal-weighted 实现是否正确利用了 LF 时序角色
- flyingsquid-baseline 完成 → 对比 temporal model vs FlyingSquid，如果 FlyingSquid 已接近 temporal model 则 Claim 1 novelty 受威胁
- cross-agent worker 完成 → 这是整篇论文最关键的实验（Claim 3），重点检查: (1) OpenHands adapter 对 multi-tool-calls/think step 的处理, (2) LF 在新格式上的覆盖率, (3) probe zero-shot vs LF oracle 退化程度
- outcome-bp-sensitivity 完成 → 检查 hold-out outcome_bp 后 probe F1 下降幅度，>5pp 说明信息泄露严重
- human-annotation 有进展 → 确认标注指南、annotator 数量、Fleiss κ 目标
- 任何实验跑在非项目服务器或非白名单 GPU 上 → severity critical

### 5. 🎯 战略上下文
**决策链**: D001(MVP方案) → D002-D006(LF修复+Phase 0.5) → D007(MVP通过 F1=0.9055) → D008(LF Oracle 揭示 command_repetition > probe on conf≥2) → D009(Dream 3/6 Weak Reject → pivot to temporal label model)

**最容易判断错的事**:
1. **不要把 probe conf≥2 的 0.9055 和 LF Oracle conf≥0 的数值直接对比** — 这是不同 test set。公平对比是 probe-002 (0.8468) vs LF All-Agreement (0.8543) on conf≥0 同一 test set，probe 输了 0.75pp
2. **command_repetition 在 conf≥2 上 0.9451 > probe 0.9055 有循环性** — 它是 majority_label 的主要贡献者（97.4% 覆盖率）。不要因此判定 probe 无价值，但也不能声称 probe "outperforms" LF methods
3. **Repeat-3 baseline 对 split 极度敏感**（0.6163–0.8432 across seeds），seed=42 是最保守情况。论文应报 mean±std
4. **Temporal label model 是论文新核心但尚未实现** — 它的成功直接决定 Claim 1 和 Claim 2 能否成立。"Student exceeds teacher" (probe > LF oracle) 需要 temporal model 先生成更好的标签
5. **Gold set (human annotation 400 windows) 不存在** — Claim 1/2 的验证都依赖它，目前仍标 P1 且需人工标注者


---
