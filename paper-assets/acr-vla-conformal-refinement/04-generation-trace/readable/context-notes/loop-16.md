# director / loop_16.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_16.md`
- **Structured JSON:** [`230f12fd656168aee265.json`](../../sessions/23/230f12fd656168aee265.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_messages
updated: '2026-05-21T11:33:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-18228 cuda:0-3, bjb1-32546 cuda:0-5, bjb2-28827 cuda:0-5, bjb2-40593 cuda:0（共 17 GPU）
- **bjb2-40593 是唯一有正确 lerobot 环境的服务器**（手动 patch 过的 0.5.2，quicktest 72% SR）。其他服务器的 lerobot 版本不对（0.5.1 或 GitHub HEAD 均缺 VT key 映射），必须从 bjb2-40593 rsync lerobot 安装目录后才能跑 π0.5
- π0.5 跨服务器部署前必须：(1) rsync 整个 lerobot 包 (2) rsync 全部 .py 代码（evaluate.py + src/） (3) quick verify SR>0% 再全量部署。已因跳过验证浪费 ~18 GPU-hours（M042, M043）
- bjb2-40593 磁盘 89-90%，大文件存数据盘
- π0.5 eval 必须设 `TORCHDYNAMO_DISABLE=1`（M041）

### 2. 🖥️ 基础设施快照
- **bjb2-40593** (1×4090): 工作目录 /root/acr-vla-conformal-refinement, conda base, lerobot 0.5.2 (patched), quicktest 72% ✅
- **bjb1-32546** (6×4090): 同上目录, lerobot 需 rsync 修复, 代码已同步（evaluate.py 802行）, 6 GPU 空闲（π0.5 eval 进程已死）
- **bjb2-28827** (6×4090): 环境预装 Worker 完成过但 lerobot 版本未确认
- **bjb1-18228** (4×4090): 同上
- π0.5 模型缓存 ~7GB, SmolVLA CRM checkpoint 在各服务器 /root/acr-vla-conformal-refinement/ 下
- 无 W&B, 无 Git remote

### 3. 📊 当前状态
**关键阻塞**：π0.5 全量 baseline eval 第三次部署失败。根因链：图像翻转(M040) → evaluate.py 未同步(M042) → lerobot 版本不一致(M043)。修复方案已明确（rsync bjb2-40593 lerobot），但 Agent 反复 reset 未完成执行。

**SmolVLA 全部 LOCKED**：Plan A Object 18.3%±2.1%, Spatial 35.0%±1.0%; K=20 18.8%/34.3% ≈ K=2 (D102); Norm Sweep 全 ε 完成; Spatial Adaptive K 全完成; Random Selection ≈ VLA-only; Figure 2 v4 已生成。

**RUNNING**：可能全空（进程死了）。需要 SSH 检查。

**PREPARING**：45 个低优先级补种实验。

### 4. 📋 待办
- **P0** 启动后立即：rsync bjb2-40593 lerobot 到 bjb1-32546 → quick verify → 重部署 6 个 π0.5 baseline eval (Object+Spatial × 3 seeds)
- π0.5 baseline 出结果（预期 Object ~72%, Spatial 待定）→ 启动 CRM pipeline: precompute 2048D features → projection 2048→960 训练 → Plan A eval
- CRM pipeline 需要在 bjb2-40593 先做 precompute（可与 baseline eval 并行）
- π0.5 + CRM 结果出齐 → Paper Agent 写入 cross-VLA section + K=20 ablation + K=1 ablation (plan_702: 10.7% ≈ VLA-only)
- 论文 final review → submit_paper_to_review → submission prep。DDL 2026-05-29（≤7 天）

### 5. 🎯 战略上下文
- **CoRL 2026 DDL 5/29**，核心 story: "Adaptive inference-time compute for frozen VLAs, K=2 足够"
- SmolVLA 数据完备，论文主体 8 页编译 OK。**唯一缺口是 π0.5 cross-VLA 验证**
- π0.5 已 debug 6 轮（M037-M043），根因全部定位。72% quicktest 在 bjb2-40593 已验证。**问题纯粹是跨服务器环境同步**，不是代码/模型问题
- Reviewer 提醒：π0.5 72% baseline 上 CRM 增益空间有限（SmolVLA +7.5pp 是从 10.8%，π0.5 上绝对增益会小很多）。论文 framing 侧重"方法可迁移性"而非"绝对增益"
- OpenVLA CRM 0% (D093) 是 applicability boundary（near-deterministic），不是失败
- Agent 反复 reset 是主要效率瓶颈，发指令尽量用 `replace_agent_queue` 保持队列干净
- **最易踩的坑**：跨服务器部署时假设环境一致——必须 rsync + quick verify，已连续 3 次犯这个错


---
