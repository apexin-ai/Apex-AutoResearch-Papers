# director / loop_2.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`28b0ca0b7a9b52877b51.json`](../../sessions/28/28b0ca0b7a9b52877b51.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-16T01:16:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0, cuda:1** @ westb-13953，不得使用其他 GPU
- 服务器: westb-13953 (connect.westb.seetacloud.com)，AutoDL 实例，重启后端口会变
- 代码路径: `/root/acib/`，模型/数据放 `/root/autodl-tmp/`
- **WANDB_API_KEY 未配置**——提交含 wandb 参数的实验前必须先 `export WANDB_MODE=disabled` 或配置 key
- AutoDL 网络: pip/git 前必须 `source /etc/network_turbo`；HF 下载设 `HF_HUB_DISABLE_XET=1` + SSL 证书环境变量

### 2. 🖥️ 基础设施快照
- 服务器: westb-13953, 2× RTX PRO 6000 Blackwell 96GB
- 工作目录: `/root/acib/`
- Python: conda base (`/root/miniconda3/bin/python`)，不是 venv
- 环境: lerobot 0.5.1, torch 2.10.0+cu128, transformers 5.8.1, mujoco 3.8.1
- EGL 渲染: `MUJOCO_GL=egl PYOPENGL_PLATFORM=egl`
- 模型 checkpoint: `lerobot/smolvla_libero`（标准）, `lerobot/smolvla_libero_plus`（data-aug baseline）
- 活跃进程（截至上次检查）:
  - GPU 0: mvp1_baseline_plus_remaining eval (PID 471056)
  - GPU 1: mvp1_baseline_std_remaining eval (PID 508625)
  - acib_v4_agg_kl: RUNNING（aggregate rate KL 版本训练）
- 无 cron 任务记录

### 3. 📊 当前状态
**阶段**: MVP 验证，目标 CoRL 2026（abstract 5/26, paper 5/29，距今 10/13 天）

**RUNNING 实验**:
- `acib_v4_agg_kl` — 核心 MVP 实验：aggregate rate KL 替代 per-token KL，修复 scorer collapse 根因（D013）。这是 v1→v3→v4 第三次迭代，前两次均因 scorer collapse 失败
- `mvp1_baseline_std_remaining` — 标准 baseline eval 补跑（之前 processor 缓存 bug 导致 7/8 suite 崩溃，D008 修复后重跑）
- `mvp1_baseline_plus_remaining` — data-aug baseline eval 补跑（同上）

**ANALYZING**: `acib_v3_train`（killed，已确认 scorer collapse，作为对照保留）

**等待中**: 无 pending Worker 回调或 Director 决策。Reviewer 刚被 RESET。

### 4. 📋 待办（条件触发式）
- acib_v4_agg_kl 训练完成 → 检查 IB loss 是否保持正值 + scorer sparsity > 0（非均匀权重）→ 若 collapse 再次发生需要第四次架构迭代；若成功 → 启动 ACIB-S eval on LIBERO-Plus
- mvp1_baseline_std_remaining 完成 → 汇总 4 suite SR，与官方数值 (spatial 90%/object 96%/goal 92%/long 71%) 交叉验证
- mvp1_baseline_plus_remaining 完成 → 汇总 data-aug baseline SR，这是互补性论证的关键对照
- 两个 baseline 都完成 → 计算 robustness gap（标准 vs plus），确认 ACIB 的提升空间
- MVP pass → 执行 post-mvp-kickoff skill：写 paper_framing.md → experiment_plan.yaml → dream_simulate → update_roadmap

### 5. 🎯 战略上下文
**核心假设**: ACIB（Action-Conditioned Information Bottleneck）作为 IB-grounded token-level 干预，是 data-aug 的**互补正则化器**，能在 VLA 64-token compact regime 下提升视觉扰动鲁棒性。

**决策链关键节点**:
- D005: 用官方 checkpoint 跳过 fine-tuning
- D006: framing 从"替代 data-aug"转向"互补 data-aug"（审稿人必问 smolvla_libero_plus 对比）
- D007→D011→D012→D013: scorer collapse 三次迭代——v1(β太大) → v3(β小但 warmup 后仍 collapse) → v4(per-token KL 本身有平凡解，改 aggregate rate KL)

**易错点**:
- **Scorer collapse 是本项目最大技术风险**。v4 的 aggregate rate KL 是第三次尝试，如果仍 collapse，需要根本性重新设计 scorer 架构（不是再调超参）
- 不要把 `acib_v3_train` 的指标当正面证据——它已确认 collapse，保留仅作对照
- Baseline eval 之前因 processor 缓存 bug 大面积崩溃过（D008），检查结果时注意区分"真实 SR"和"崩溃导致的 0%"
- memory.md 记录了 SmolVLA 架构细节（64 tokens × 960-dim, PixelShuffle factor=4）和 LIBERO-Plus 实际是 7 维 21 子维度（非 4 维），论文写作时必须用正确数字
- DDL 极紧（CoRL abstract 5/26），MVP 还没过，时间压力很大——不要在非关键路径上花时间


---
