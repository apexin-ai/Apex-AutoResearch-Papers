# agent / loop_4.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`c1a22d1cad306f6f0e72.json`](../../sessions/c1/c1a22d1cad306f6f0e72.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-15T22:23:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**cuda:0, cuda:1**（westd-19183），禁止用其他 GPU
- 服务器**无外网**：所有 HuggingFace/AutoProcessor 操作必须 `local_files_only=True`
- **分析 Worker 不得覆盖 spec 字段**（registry 里的 command/server/data_path 等）
- Untrained model = `from_config()` 重新初始化 LLM（6.74B random），**保留 SigLIP**（0.80B frozen）
- Token 聚合统一用 **last pre-action token**，不要改
- Instruction ablation 代码已修复 bug：`if args.task_instruction:` 对空字符串返回 False，现在用显式 None 检查
- Scope 限定 **OpenVLA-class architecture**，不 over-claim generality

### 2. 🖥️ 基础设施快照
- 服务器：**westd-19183**，工作目录 `/root/vla-ssd/`
- Python/conda：用 `detect_image` 检测镜像类型再决定（aml-train 用 conda base: `/root/miniconda3/bin/python`）
- 数据盘：`/root/autodl-tmp/vla-ssd/`（大文件、模型、HF cache）
- HF cache：`HF_HOME=/root/autodl-tmp/.hf_cache`
- W&B：无活跃 run（本项目主要是离线 RSA 分析，不走 W&B）
- 活跃 Worker：`worker_ssh_d027-siglip-only-rsa_20260515T221202`（RUNNING，正在执行 SigLIP-only RSA smoking gun 实验）
- 活跃 Cron：0（reconcile 返回空）
- GPU 状态：2× RTX PRO 6000，当前 0/2 占用（d027_siglip_only_rsa ALLOCATED 待提交，worker 正在处理）

### 3. 📊 当前状态
**刚完成**：d027_trained_no_inst_rsa (SUCCESS) — trained VLA with empty instruction RSA，完成了 2×2 matrix 的最后一格。

**正在进行**：Worker `worker_ssh_d027-siglip-only-rsa` 正在执行 d027_siglip_only_rsa（ALLOCATED 状态）——这是 **SMOKING GUN** 实验：从 SigLIP+projector 直接提取特征（不过 LLM），跑 RSA。如果 RSA ≈ 0.48 = vision encoder 单独就能解释全部 action-relevant structure，complete_mvp 条件满足。

**Registry 摘要**：35 实验，19 success / 7 negative / 6 killed / 0 failed。唯一非 DONE 的：d027_siglip_only_rsa (ALLOCATED)，lg_instruction_ablation + lg_output_head_analysis (QUEUED/killed，已被 d021 系列替代，可忽略)。

**等待中**：Worker 完成回调（d027-siglip-only-rsa）。无 Director 决策待回。

### 4. 📋 待办（条件触发式）
- Worker `d027-siglip-only-rsa` 回调 DONE →
  - RSA ≈ 0.45-0.50 → smoking gun 确认，update_registry(conclusion=success)，汇报 Director "[资源] ..."，调 complete_mvp，启动 Paper Agent 写作流程
  - RSA ≈ 0.39（DINO 水平）→ projector/LLM 架构有贡献，conclusion=negative，产出 Framing 调整提案给 Director
  - 中间值 → 部分支持，汇报 Director 让其决策
- complete_mvp 后 → 读 paper_framing.md + writing_plan.yaml（如有），派 Worker 开始论文章节写作（CoRL abstract DDL May 26，仅剩 11 天）
- 任何实验完成 → 按 on-experiment-done skill 执行全套流程（registry + report.md + 文献联动 + 反思实验计划）

### 5. 🎯 战略上下文
**核心结论链**：7 轮实验 + 2 benchmark 一致显示 trained ≈ untrained >> DINO，instruction 无影响。Option B（instruction drives conditioning）被 Δ=0.0044 明确否证。D027 锁定 **Option A2 "Vision Encoder Dominance"**——frozen SigLIP 决定 action-relevant 表征，LLM 是 passthrough。

**MVP Gate**：SigLIP-only RSA 是最后一个 data point。如果 ≈ 0.48 则 complete_mvp，如果 ≈ 0.39 则需要 reframe（不太可能，因为 projector 权重 trained=untrained 完全一致）。

**易错点**：
- d027_trained_no_inst_rsa 的结果需要合并到 2×2 matrix 里汇报（trained no-inst 这格现在有数据了）
- 不要把 lg_ 前缀的旧实验（已 killed）和 d021_/d027_ 前缀的新实验搞混——lg_ 是被替代的旧版
- CoRL DDL 很紧（abstract May 26 = 11 天），complete_mvp 后必须立即启动多 Worker 并行写论文
- Output head analysis 结论是 "shallow adaptation 不成立"，但发现了 **projector bottleneck** 机制（vision backbone + projector 在 trained/untrained 间完全一致，cos_sim=1.0）——这是支持 A2 framing 的因果证据
- Grant 2026 用的是 OFT checkpoint（非标准 fine-tuning），Related Work 必须 qualify 这个差异
- 论文写作前必须读 red-section skill 规范


---
