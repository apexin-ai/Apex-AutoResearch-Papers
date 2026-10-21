# director / loop_1.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`4fac22edcc20ea7f3909.json`](../../sessions/4f/4fac22edcc20ea7f3909.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-13T19:35:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-4090x4 (bjb1-18228) cuda:0/1/2/3 + autodl-4090 (bjb2-40593) cuda:0。不得使用其他服务器/GPU
- **代码部署反复失败**：本 session 遇到 5 次"修复在本地但未同步到服务器"的问题。任何代码修改后必须要求 Agent 贴 grep/md5sum 证明服务器上的文件已更新，不要信任"已部署"的口头汇报
- **kill 命令反复失效**：Agent 多次报告进程已 kill 但实际未死。必须要求 Agent 用 ssh_execute（不是 ssh_read_only）执行 kill -9，并贴 nvidia-smi 输出证明
- SFT gate 尚未正式通过（D013），不要假设 smolvla_libero 可用——等 v5 eval 结果

### 2. 🖥️ 基础设施快照
- **autodl-4090x4** (bjb1-18228): 4× RTX 4090, 工作目录 `/root/acr-vla-conformal-refinement/`
  - eval-spatial-v4 刚被 kill，camera_names 修复中，即将启动 v5
  - precompute-v4-shard0/1/2 在 cuda:1/2/3 运行中（~35min total，可能已完成或接近完成）
  - wrapper 已部署修复版（11327 bytes, flip/resize_with_pad/unnorm 全有）
  - evaluate.py 正在被修复（加 camera_names）
- **autodl-4090** (bjb2-40593): 1× RTX 4090 D, 同一工作目录
  - 修复版 wrapper + evaluate.py 已部署（含 camera_names）
  - eval-object-v4-full 在运行中
- 模型: `lerobot/smolvla_libero` (HuggingFace, 已缓存)
- 数据: LIBERO demos 在两台服务器均已就绪
- Precompute cache: `/root/autodl-tmp/crm_cache_v4/`（v3 及以前全部无效已清除）

### 3. 📊 当前状态
刚批准 RESET_BOTH（Reviewer + 自己）。Agent 正在处理 camera_names 修复指令。

**Registry 活跃实验：**
- `eval-object-v4-full` (bjb2-40593 cuda:0) — RUNNING，10 tasks × 10 rollouts
- `precompute-v4-shard0/1/2` (bjb1-18228 cuda:1/2/3) — RUNNING，可能已接近完成
- `eval-spatial-v4-full` — 刚 killed，camera_names 修复后将启动 v5

**等待中：**
- Agent Worker `worker_infra_camera-names-fix` 或类似 — 修复 evaluate.py + 重启 eval v5
- Precompute-v4 cron 回调（180s 间隔）
- Paper Agent: Related Work + bib 修正已完成

### 4. 📋 待办
- precompute-v4 完成 → shard 合并 + 数据完整性检查 + 准备 CRM 训练脚本
- eval-spatial-v5-full 完成 → **关键节点**：10 tasks × 10 rollouts 成功率
  - ≥80% → SFT gate 正式通过，story 照原 framing
  - 50-80% → SFT gate 通过但调低 nominal baseline 期望
  - <30% → 需换模型（OpenVLA 等）
- eval-spatial-v5 ≥30% + precompute-v4 完成 → 立即启动 CRM 训练（plan_001）
- CRM 训练完成 → eval CRM mode on spatial + LIBERO-Plus → plan_001 首个完整结果
- eval-object-v4 完成 → 汇报 object benchmark 成功率

### 5. 🎯 战略上下文
- **决策链**: D008(SmolVLA 未微调) → D009(试社区 checkpoint) → D010(0% 走 SFT) → D012(55.6% 取消 SFT) → D013(55.6% 不可靠，wrapper 重写) → D014(v3 代码未部署)
- **投稿目标**: ICLR 2027 (D011，CoRL 2026 已放弃)
- **MVP 已通过**: plan_000 在 3D 点到达任务上确认 per-DOF > scalar > none
- **核心风险**: smolvla_libero 在正确 wrapper 下的真实成功率仍未知。这是整个项目的 gate——如果 <30% 需要换模型
- **最容易判断错的事**: Agent 说"已修复/已 kill/已部署"不代表真的做了。必须要求贴证据（grep output / nvidia-smi / file timestamp）
- **Paper 进展**: Related Work + bibliography (32 refs) 已完成初稿，Method section draft 也有。等实验数据后启动 Full Draft
- **GPU 预算**: ~180h 剩余，P0+P1 需 ~110h，充足


---
