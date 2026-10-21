# director / loop_14.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_14.md`
- **Structured JSON:** [`e7e1ab49432105a828d9.json`](../../sessions/e7/e7e1ab49432105a828d9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_messages
updated: '2026-05-21T03:15:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb2-40593 cuda:0, bjb1-18228 cuda:0-3, bjb1-32546 cuda:0-5, bjb2-28827 cuda:0-5。严禁使用白名单外 GPU
- 每 GPU 只能跑 1 个 LIBERO eval 进程（M034: 双进程导致 rollout 动态显存增长→OOM kill，无 traceback）。M036 刚复发过。
- Cron 报 failed 时**必须先 ssh_read_only `ps -p PID` + 检查 JSON 是否完整**，不验证不改 registry（M035: 已多次误标活跃实验为 failed）
- Adaptive K 必须是核心贡献（用户硬要求），固定 K=10 是 analysis baseline
- Plan A 代码 hardcode K=2，永远不扩展到 K=10。argmin-to-centroid（不是 sample mean）
- OpenVLA CRM 实验线已 CLOSED (D093, 0% SR)，不再追加

### 2. 🖥️ 基础设施快照
- **bjb2-40593** (1×4090): connect.bjb2.seetacloud.com, /root/acr-vla-conformal-refinement, conda base
- **bjb1-18228** (4×4090): connect.bjb1.seetacloud.com, 同上路径, conda base
- **bjb1-32546** (6×4090): connect.bjb1.seetacloud.com, 同上. python3 需 symlink `/usr/local/bin/python`，submit 命令前缀 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&`
- **bjb2-28827** (6×4090): connect.bjb2.seetacloud.com, 同上. python3 同样需 conda activate 前缀
- CRM checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
- SmolVLA: 自动从 HF 加载 (~5.7GB VRAM)
- π0.5: `lerobot/pi05_libero_finetuned` 已下载到 bjb2-40593 (~8.7GB VRAM), wrapper 在 `src/pi05_wrapper.py`
- bjb2-40593 磁盘 90%⚠️ (46GB 可用)

### 3. 📊 当前状态
**我这轮的主要工作**：处理 Agent 多次 reset（Loop 23 反复重启）+ 大批 cron false positive 涌入。发送了综合指令（registry 批量修正 + 9 GPU 填充 + π0.5 检查），Agent 在处理过程中又到硬限。

**Reviewer #47 确认的批量完成结果**（registry 可能尚未更新）：
- seed71(ε=0.1)=16%, seed72(ε=0.05)=11%⚠️outlier, seed73(ε=0.03)=16%, seed74(ε=0.1)=13%, seed75(ε=0.05)=15%
- seed64(ε=0.03)=17%, seed64(ε=0.05)=15%, seed64(ε=0.1)=15%, seed65(ε=0.03)=17%, seed65(ε=0.1)=15%, seed52-r3(ε=0.1)=15%
- seed62-r2/63-r2(norm003) 被 kill（M036），需重跑

**仍在跑（未确认是否完成）**：
- eval-pi05-baseline-object-seed42 (bjb2-40593:cuda:0, PID 802634) — 最关键实验
- seed66×3 + seed67×3 (bjb1-18228 + bjb1-32546:cuda:2 + bjb2-28827:cuda:5)
- seed51-r3 (bjb1-32546:cuda:0) — cron 报退出，未确认 SR

**空闲 GPU（Reviewer 确认）**：bjb2-28827 cuda:0-4 (5个), bjb1-32546 cuda:1,3,4,5 (4个) = 9 GPU 待填充

**已派但未确认执行的指令**：综合指令要求 (1) 批量修正上述 registry (2) 检查 π0.5 进度 (3) 在 9 GPU 上部署 norm003-seed76/77/78, norm005-seed76/77, seed62-r2-redo/63-r2-redo, norm01-seed76/77

### 4. 📋 待办
- Agent 新 session 上线 → 首先确认上述综合指令是否已执行（registry 修正 + GPU 填充）。未执行则重发
- π0.5 baseline 完成且 SR>0% → 检查 action diversity (K=2 L2 distance)，若 stochastic → precompute features → 训练 projection layer → Plan A eval
- π0.5 baseline SR=0% → 诊断归一化 (MEAN_STD vs QUANTILES)，修复后重跑
- Norm sweep 全部完成 → 生成 Figure 2 (norm sweep curve)，汇总统计表
- 用户未回复 threshold calibration 两个方向（1: 强调 K=2 efficiency, 2: recalibrate Pareto sweep）→ 等用户回复，不主动选
- GPU 释放后优先补 ε=0.03（种数最少 ~10）> ε=0.05（有 outlier 需验证）> ε=0.1

### 5. 🎯 战略上下文
**CoRL 2026 DDL 2026-05-29 (≤8 天)**。核心方法 Plan A: K=2 batched → L2 uncertainty → selective CRM, Object 18.3%±2.1%, Spatial 35.0%±1.0%。

**π0.5 是 DDL 前最关键实验** — 同时解决 M1 (narrow scope, "VLAs" 复数但只测了 SmolVLA) 和 R2-W1-new (11% absolute SR 太低)。π0.5 baseline 前 2 task SR=0%，归一化问题待确认。

**Norm sweep 累计表**（Reviewer #47）：ε=0.03 ~15.6% (n≈10), ε=0.05 ~14.0% (n≈15, 含 outlier 11%), ε=0.1 ~15.2% (n≈15), ε=0.2 17.2% (n=12, LOCKED)。

**决策链**: D092 Plan A GO → D093 OpenVLA CLOSED → D094 Plan A Spatial → D095 π0.5 实验线 → D096 π0.5 适配 GO

**易错点**:
- Plan A 的 uncertainty metric (flatten-L2 30D) 和 Adaptive K 的 (per-step-mean-L2 7D) 不同，阈值不可互换 (ratio ~2.77×)
- Agent 反复 reset 后丢失上下文——每次新 session 必须明确告知 seed62-r2/63-r2 已 kill、seed67 已部署、哪些 registry 已修正
- π0.5 CRM 不能直接迁移 (obs_dim 2048 vs 960)，需 projection layer
- Paper Agent session 活跃，Plan A 整合已完成（Abstract/Intro/Table 1/§4.3/Conclusion）


---
