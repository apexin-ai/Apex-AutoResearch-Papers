# reviewer / loop_3.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`839b421b7b9f01d72c0e.json`](../../sessions/83/839b421b7b9f01d72c0e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-15T19:02:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配：westd-19183 的 cuda:0 和 cuda:1，两张卡都可用，无越界风险
- 特征提取脚本用 `--gpu 0` + `CUDA_VISIBLE_DEVICES=N` 映射物理卡号，spec 里必须标注物理卡号
- AutoDL 服务器无外网：所有 HF 模型必须 `local_files_only=True`，否则 AutoProcessor.from_pretrained 会 crash（已踩坑两次）
- lg_dino_extract 的 spec 被 analyze worker 覆盖过（seed 42→0, command 改错），reproduce.command 是正确的。已报 Director，但下次审查注意 spec 不一定可信，以 reproduce 和 logs 为准

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183（2×RTX PRO 6000 Blackwell 96GB）
- 工作目录：`/root/vla-ssd`（代码），`/root/autodl-tmp/vla-ssd/`（数据/特征/结果）
- Python：`/root/miniconda3/bin/python`（conda base，不是 venv）
- 模型 checkpoints：`/root/autodl-tmp/vla-ssd/checkpoints/`（openvla-7b, openvla-7b-untrained, dinov2-large）
- 数据：`/root/autodl-tmp/vla-ssd/data/libero/libero_goal/`（10 tasks × 50 demos）和 `libero_10/`
- 特征目录：`trained_libero_goal/`, `untrained_libero_goal/`, `dinov2_libero_goal/`（均在 features/ 下）
- 无 W&B 配置，不检查 W&B
- 活跃进程：审查时两卡均空闲（0%/0MiB）

### 3. 📊 当前状态
**刚完成**：LIBERO-Goal Goal Classification 三组实验（trained/untrained/DINO）+ timestep accuracy 分析的完整审查。

**关键结论**：
- Sanity-GC gate FAIL（DINO traj_acc=100%）
- G2-GC gate FAIL（trained vs untrained Δ=0）
- 但 timestep 分析挽回了方向：DINO bin 0（初始帧）仅 43.2%，trained VLA bin 0 = 100%
- **缺失**：untrained VLA 的 timestep accuracy 未跑——这是判定 language grounding 的关键数据点，已向 Director 报告

**Registry**：25 个实验全部 DONE（无 RUNNING/PREPARING），等待 Director 决策下一步

**等待中**：Director 对 Goal Classification 方向 FAIL 的响应 + untrained VLA timestep 分析是否执行

### 4. 📋 待办
- untrained VLA timestep_accuracy.json 出现 → 对比 bin 0 accuracy：≈43%(≈DINO) → 确认 language grounding 成立；≈100%(≈trained) → language grounding 不成立，需换方向
- Director 转发任何新 framing 提案 → Read `negative-framing-review.skill.md`，四维度审查
- 新实验提交（如 initial-frame-only GC 或 instruction-conditioned action prediction）→ 常规审查流程
- 论文章节写作审查请求 → 先查 red-section skill 合规，再按 5.1/5.2 维度审

### 5. 🎯 战略上下文
**项目方向链**：MVP-1 temporal distance FAIL(D008) → MVP-2 action prediction FAIL(D014) → Pivot to LIBERO-Goal(D015) → D017 确认用 LIBERO-10 fine-tuned checkpoint → Goal Classification Sanity-GC FAIL → timestep 分析发现 early-frame 有希望

**核心 story 候选**：LIBERO-10 negative + LIBERO-Goal positive 对比叙事 + layer-wise mechanistic depth

**下一个"我"最容易判断错的事**：
1. **不要因 Sanity-GC FAIL 就判 LIBERO-Goal 方向全死**——timestep 分析显示 initial frame 有 vision-ambiguity，DINO 43% vs trained VLA 100% 是有意义的 gap。但必须等 untrained VLA timestep 数据才能下结论
2. **不要信 lg_dino_extract 的 spec 字段**（seed=0 是错的，实际 seed=42）——以 reproduce.command 为准
3. **lg_gc_trained 的 100% accuracy 不能直接解读为 language grounding**——untrained VLA 全 timestep 也 traj_acc=100%。差异只在 frame-level accuracy 的细微处（trained 100.0% vs untrained 99.7-100.0%），这不够写论文
4. **CoRL 2026 DDL: Abstract May 26 (11d), Paper May 29 (14d)**——时间紧但 GPU 充足，不要套人类工时判断


---
