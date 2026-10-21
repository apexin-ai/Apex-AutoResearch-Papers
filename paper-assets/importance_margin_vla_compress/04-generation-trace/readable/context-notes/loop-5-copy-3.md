# reviewer / loop_5.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`c946cda0199338fd6e57.json`](../../sessions/c9/c946cda0199338fd6e57.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-16T14:45:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-27271 只允许 cuda:0, cuda:1（2× RTX PRO 6000 96GB）
- cqa1-33015 有 4× RTX 4090 D 24GB，当前使用 cuda:0 和 cuda:1，cuda:2/3 空闲
- `HuggingFaceVLA/libero` 数据集需要 HF_TOKEN 认证（已用替代方案绕过）
- AutoDL 网络：必须 `source /etc/network_turbo` + 设置 SSL 证书环境变量，否则 HF 下载全部超时
- aloha_sim_insertion success rate 路径已死（D039）— 不要再投 GPU 在 aloha SR 上

### 2. 🖥️ 基础设施快照
- **westd-27271**: 工作目录 `/root/autodl-tmp/importance_margin_vla_compress`，conda base，Python `/root/miniconda3/bin/python`
  - HF cache: `/root/autodl-tmp/.hf_cache/lerobot/smolvla_base`
  - 当前空闲（plan_005 脚本崩溃后无活跃进程）
- **cqa1-33015**: 同样工作目录结构，conda base
  - LIBERO 数据集: `/root/autodl-tmp/.hf_cache/lerobot/hub/datasets--HuggingFaceVLA--libero/`（已完整 383 blobs）
  - LIBERO env: libero 0.1.1 + robosuite 1.4.0 + mujoco 3.8.1
  - 活跃训练:
    - `libero_full_ft_baseline` PID 8985, tmux, cuda:0, 100K steps
    - `libero_lora_baseline` PID 9062, tmux, cuda:1, 100K steps
  - 日志: `~/runs/importance_margin_vla_compress/libero_full_ft_baseline.log` / `libero_lora_baseline.log`

### 3. 📊 当前状态
刚确认 LIBERO 双实验启动成功（full expert FT + LoRA baseline 并行跑在 cqa1）。首步 loss 1.18/1.28，GPU 显存 2.7/2.1GB（warmup 阶段）。

Registry RUNNING:
- `libero_full_ft_baseline` — 验证 full expert FT 能否复现 >50% SR（官方 87.3%）
- `libero_lora_baseline` — 验证 LoRA + flow matching 是否系统性 mode collapse

plan_005 (formal bound) 在 westd 崩溃（`IMMSmolVLAWrapper` 无 `.model` 属性），等 Agent 修复。

### 4. 📋 待办
- LIBERO 训练进行 1-2h 后 → 检查 loss 曲线 + GPU 利用率是否正常（4090 24GB 可能 OOM）
- libero_full_ft 跑到 ~10K steps → 检查 diversity std（如果也 collapse → flow matching 根本性问题，不只是 LoRA）
- libero_lora 跑到 ~10K steps → 与 full_ft 对比 loss，如果 LoRA 显著差 → 确认 LoRA 是病因
- 任一实验 OOM/crash → 立即报 Director，建议降 batch size 或用 gradient accumulation
- plan_005 修复后 → 审查 bound tightness ratio（paper_framing 预期 6-10x loose）
- westd 双卡长期空闲(>2h) → 报 Director 建议用于 LIBERO seed=43/44 并行训练

### 5. 🎯 战略上下文
**决策链**: D034(MVP pass) → D035(mode collapse确认) → D036(Dream framing修正) → D037(annealing失败) → D038(alpha=16不够) → D039(aloha SR已死，LIBERO升P0)

**核心判断**: SmolVLA 官方不用 LoRA 训 LIBERO（用 full expert FT 达 87.3%）。如果 LoRA 在 LIBERO 上也 collapse → IMM 框架需要从"LoRA plugin"转为"full FT compatible"方案，这是论文 framing 的根本性变化。

**易错点**:
1. 不要把 aggregate diversity std (0.03-0.04) 当作"一般性低" — 实际是部分 obs ODE 混沌 + 部分 obs 完全 collapse 的平均（inference pipeline audit 发现）
2. D038 说 "alpha=16 std=0.007" 是错的（实际 0.029-0.041），但结论方向正确（都是 0% SR）
3. 100K steps × bs=4 在 4090 上约 20-25h — 别过早标记"训练太慢"
4. CoRL DDL May 29（13天），LIBERO 是 critical path，westd 空闲是可接受的（先验证再并行）


---
