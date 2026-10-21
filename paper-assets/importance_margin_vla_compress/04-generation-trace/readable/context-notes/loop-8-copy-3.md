# reviewer / loop_8.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`0d15fed38f080f0bd66b.json`](../../sessions/0d/0d15fed38f080f0bd66b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-18T00:56:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- cqa1-33015 项目 GPU 分配：需确认 `execution.gpu_ids`，当前 4 张 4090D 全在用（GPU 0-1 eval，GPU 2-3 训练）
- westd-27271：OpenVLA eval 固定 `CUDA_VISIBLE_DEVICES="0"`（脚本硬编码）
- Smart compress eval 的 `eval_success_rate_libero.py` **不支持 smart compress 模式**——已提交 CRITICAL 报告。任何用该脚本跑 smart compress checkpoint 的结果都是无效的（baseline 模式，compressor 权重被 `strict=False` 静默丢弃）
- Registry 中 `train_smart_compress_m32` 和 `m64` 的 `conclusion: failed` 是误判（cron 监控将正常退出判为死亡），训练均已成功完成，已提交 warning 要求修正

### 2. 🖥️ 基础设施快照
- **cqa1-33015** (root): `/root/autodl-tmp/importance_margin_vla_compress`，Python `/root/miniconda3/bin/python`，4x RTX 4090D
  - HF cache: `/root/autodl-tmp/.hf_cache`，W&B: offline 模式
  - Checkpoints: `checkpoints/smart_compress_{m16,m32,m64,m96}/checkpoint.pt` 均存在（m32/m64 训练完成，m96/m16 训练中持续保存）
  - 活跃进程：PID 363256 (M=32 eval, GPU 0), PID 364255 (M=64 eval, GPU 1) — **应 kill，结果无效**；M=96 训练 (GPU 2), M=16 训练 (GPU 3)
- **westd-27271** (root): `/root/autodl-tmp/importance_margin_vla_compress`，OpenVLA checkpoint `/root/autodl-tmp/openvla-libero-object`
  - 活跃进程：PID 755666 (OpenVLA k=0.7 eval, GPU 0)
- **本地 workspace**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/`

### 3. 📊 当前状态
刚完成对 smart compress eval CRITICAL bug 的诊断和上报。**核心发现：M=32/M=64 闭环 eval 使用了错误脚本（`eval_success_rate_libero.py`），以 baseline 模式运行，根本没有测试 smart compression。需要新脚本 `eval_smart_compress_libero.py` 加载 `SmartCompressWrapper` + `forward_inference()`。**

Registry RUNNING 实验：
- `eval_openvla_pruning_k07` — westd，Task 2 进行中，Task 1 = 74%（baseline 78%，-4pp）
- `train_smart_compress_m96` — cqa1 GPU 2，step ~58k/100k
- `smart_compress_m16` — cqa1 GPU 3，step ~55k/100k

等待中：
- Director 对 CRITICAL 报告的回应（kill 无效 eval + 写新 eval 脚本）
- Director 对 registry 误判修正的回应
- OpenVLA k=0.7 完成（ETA ~2-3h）
- M=96 / M=16 训练完成（ETA ~3-4h）

### 4. 📋 待办（条件触发式）
- Director 批准 kill eval → 确认 PID 363256/364255 已终止，GPU 0-1 释放
- 新 eval 脚本 `eval_smart_compress_libero.py` 提交 → 审查脚本是否正确加载 `SmartCompressWrapper`、使用 `forward_inference()`、传入正确 M 值
- M=32/M=64 用新脚本重新 eval → 审查结果。**如果 SR 仍然 0%（即使用正确压缩路径），Claim 4 失败，paper 必须重构**
- OpenVLA k=0.7 完成 → 审查完整 10-task 结果，构建降解曲线（baseline 74% → k=0.7 → k=0.5 37.4%）
- M=96 / M=16 训练完成 → 确认 checkpoint 保存成功，用正确 eval 脚本启动评估
- 如果 smart compress 所有 M 值 SR 均 >0% → Claim 4 成立，审查幅度是否足以支撑"overcomes cliff-edge"的表述
- 如果 smart compress SR = 0% → 立即上报 CRITICAL，建议论文降级 Claim 4 或转为 negative result

### 5. 🎯 战略上下文
- **D068 Scenario B 已确认**：cliff-edge 是 SmolVLA 特有的（pixel_shuffle connector 导致），OpenVLA 表现 graded degradation。这是论文核心结论。
- **4 个 Core Claims**：(1) architecture-dependent compressibility, (2) pixel shuffle entanglement 是根因, (3) standard projectors（如 OpenVLA MLP）允许渐进降解, (4) learned compression 克服 cliff-edge
- **Claim 4 是最脆弱的**——目前零实验验证（eval 脚本错误）。如果 smart compress 也 0%，论文从 4 claims 缩为 3 claims（诊断性论文，无解决方案）。
- **易错点**：
  - 不要信 registry 中 m32/m64 的 `conclusion: failed`——训练成功，是 cron 误判
  - 不要用 `eval_success_rate_libero.py` 跑 smart compress——该脚本没有压缩前向路径
  - SmolVLA baseline 是 `libero_full_ft/step_099999` = 36%（100 eps），Task 0 (alphabet_soup) baseline = 0%，所以 eval 中 Task 0 全灭是预期行为
  - ACIS k=0.3 的 45% SR 从未被验证过（可能是 bypass baseline），不要引用
  - OpenVLA eval seed=7，smart compress 训练 seed=42——注意一致性
  - CoRL 2026 deadline：Abstract May 26（8 天），Paper May 29（11 天）


---
