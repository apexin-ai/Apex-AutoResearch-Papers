# agent / loop_5.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`7a28c52e593df3b846c6.json`](../../sessions/7a/7a28c52e593df3b846c6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-16T01:36:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`cuda:0`, `cuda:1`（westd-19183）。不要用其他 GPU 编号
- westd 是 **SeetaCloud**（非 AutoDL），不适用 `network_turbo`/`ModelScope` 等 AutoDL 方案
- 服务器**无外网**：所有 HF 操作必须 `local_files_only=True`，模型/数据必须提前下载到本地
- Untrained model 是 `from_config()` 重新初始化 LLM（6.74B random），保留 SigLIP（0.80B frozen）——不是 checkpoint 差异
- `submit_training_job` 的 command 必须自带环境激活（`source /root/miniconda3/bin/activate && ...`），不要假设 .venv
- 分析 Worker 不得覆盖 registry 的 `spec` 字段

### 2. 🖥️ 基础设施快照
- 服务器：**westd-19183**，2× GPU
- 工作目录：`/root/vla-ssd`（代码仓库）
- 数据/模型/缓存：`/root/autodl-tmp/vla-ssd/`（根分区只有 ~30GB，大文件全在这）
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- Features 缓存：`/root/autodl-tmp/vla-ssd/results/` 下各子目录
- 活跃进程：**worker_ssh_plan012-clip-extract_20260516T013043**（running，turn 30，progress "8/10"——正在提取 CLIP-ViT 特征用于 plan_012）
- Crons：0 活跃（reconcile 已同步）
- WandB：未配置（本项目全部是本地 probe/RSA 分析，不用 WandB）

### 3. 📊 当前状态
**所有 P0 实验完成，三条 Claim 证据闭合。** 项目处于 paper writing 启动前的最后准备阶段。

Registry：42 DONE（29 success / 7 negative / 6 killed-legacy），3 QUEUED（lg_output_head_analysis、lg_instruction_ablation 是历史遗留 killed 实验未清理状态；plan_012_clip_vit_control 是唯一活跃的 P1 实验）。

上一个 session 完成的关键工作：
- plan_008 random instruction control → success（三重不变性闭合 Claim 3）
- plan_009 CKA verification → success（RSA-CKA dissociation 成为新 finding）
- untrained last_preaction probe → success（redistribution is training-dependent，D034）
- Re-dream evidence compilation worker 已完成
- Writing plan (writing_plan.yaml) 已生成，含 section outline + evidence mapping
- plan_012 CLIP-ViT 特征提取 worker 正在运行（8/10 进度）

等待中：
- **plan012-clip-extract worker 回调**（分钟级，8/10 接近完成）
- **Director 审批启动 Paper Agent**（re-dream 完成后应已提交，等 Director 决策）

### 4. 📋 待办（条件触发式）
- plan012-clip-extract worker 完成 → 对 CLIP-ViT 特征跑 RSA + action probe → 与 SigLIP/DINO 三方对比 → 更新 registry + paper_framing.md C2 应对 → 汇报 Director
- Director 批准 Paper Agent → 按 writing_plan.yaml 派多个 Worker 并行写各 section（Method + Results 优先，Introduction + Related Work 并行）
- plan_012 RSA 结果出来后 → 若 CLIP RSA 显著 > DINO 但 < SigLIP → 强化 "VL pretraining provides geometric alignment" narrative；若 CLIP ≈ SigLIP → 说明 VL pretraining 通用而非 SigLIP 特有
- Paper 写作启动后 → plan_010 LIBERO-Spatial（P2）可并行，时间紧则跳过，Limitations 注明

### 5. 🎯 战略上下文
**核心结论（三条 Claim）**：
1. Frozen vision encoder (SigLIP) 是 action-relevant 表征的源头（RSA=0.615 >> VLA 0.50 >> DINO 0.388）
2. LLM 降解 distributed geometric structure 但通过 **训练依赖的** attention 将信号 concentrate 到 readout token（trained readout R²=0.731 > projector 0.706；untrained readout 0.686 < projector）
3. Training 教 routing 而非 creating（distributed RSA invariant，CI includes 0）

**决策链**：D027 Option B 死亡 → D028 SigLIP smoking gun → D030 Dream 未达标 → D031 redistribution pivot → D032 Option A 锁定 → D033 DINO≈Proj geometric-functional dissociation → D034 training-dependent redistribution

**易错点**：
- image_mean 是论文主文的公平聚合口径，last_preaction 放 supplementary。不要在主文混用
- DINO R² (0.712) ≈ Projector R² (0.706) 但 DINO RSA (0.388) << Projector RSA (0.615)——这是 "geometric alignment vs information content" 的关键区分，不要搞混
- CKA 排序与 RSA **反转**（Claim 2 必须限定为 "geometric degradation"，不能泛化为 "representation quality"）
- lg_output_head_analysis 和 lg_instruction_ablation 的 QUEUED 状态是历史遗留，实际已 killed，可以清理但不要重跑
- CoRL deadline：Abstract **May 26**（10 天），Paper **May 29**（13 天）——时间紧，Paper Agent 应尽快启动


---
