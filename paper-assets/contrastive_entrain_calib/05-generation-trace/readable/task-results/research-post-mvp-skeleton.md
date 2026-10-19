# research post mvp skeleton

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_post_mvp_skeleton_20260518T064059_result.json`
- **Structured JSON:** [`fdba2bad1f788f6382da.json`](../../sessions/fd/fdba2bad1f788f6382da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No `register_artifact` tool available.文件已写入:

`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/post_mvp_experiment_skeleton.md`

文档包含 7 个部分:

1. **主实验** — R1(方向对齐) + R2(对比) + R3(行为) 三路 reward 的 GRPO 训练，Qwen3-8B + LoRA rank 64，~55 H100-hr
2. **4 个 Baseline** — Vanilla、R3-only、ACT-style、Binary Probe Penalty，合计 ~71 hr
3. **4 个 Ablation (A1-A4)** — A1/A2 从主实验 checkpoint 分叉节省 GPU，A3 条件执行（需 A2 >= 5pp 且预算允许）
4. **5 类评估** — SYCON Bench (ToF/NoF)、SycophancyEval、MT-Bench、MMLU + 6 个项目特有分析指标
5. **GPU 预算** — mandatory ~190 hr / 条件 A3 ~20 hr，含 checkpoint 共享策略图
6. **可提前准备的工作** — 评估管线、GRPO 框架、NLI 评分器、rollout 生成器（均不依赖 MVP）
7. **依赖 MVP 的工作** — R1 层选择、reward 权重范围、A3 是否执行、是否 pivot

---
