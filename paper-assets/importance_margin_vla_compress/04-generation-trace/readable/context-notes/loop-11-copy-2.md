# agent / loop_11.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`e13b2c79cd95af90c747.json`](../../sessions/e1/e13b2c79cd95af90c747.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-05-21T19:10:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0-3，4 台服务器各 4 卡，共 14 GPU（westd-27271 只用 0,1）
- VTC M64 v6 是第 6 次重试（v5 SIGKILL at step 17050），若再失败需彻查磁盘/OOM 而非盲目重试
- π0.5 random k=0.9 seed42 结果 12% SR 疑似 transient issue，seed43 正在重跑确认——不要用 seed42 的 12% 写入论文
- SmolVLA official sweep 结论已定（cliff-edge at all k），6 个 QUEUED 实验是补数据点，优先级低于 P0/P1
- CoRL abstract deadline May 26（5天），paper deadline May 29（8天）——时间极紧

### 2. 🖥️ 基础设施快照
- **westd-41074** (4 GPU): GPU0=π0.5 L2norm k=0.7, GPU1=π0.5 random k=0.5 seed43, GPU2=VTC M96 train (pid=68539, 54%+), GPU3=π0.5 random k=0.7 + M64v6 (pid=59671)
- **westd-38929** (4 GPU): GPU0=OpenVLA L2norm k=0.7, GPU1=OpenVLA random k=0.3, GPU2=OpenVLA random k=0.7, GPU3=OpenVLA L2norm k=0.5 v3. 有 2 个 Worker 正在部署 π0.5 cross-suite eval 和 VTC eval prep
- **cqa1-33015** (4 GPU): GPU0-3 = X-VLA multi-seed (L2norm k=0.3/0.7 s43, random k=0.3 s43/k=0.7 s44)
- **westd-27271** (2 GPU): GPU0=OpenVLA L2norm k=0.3 rerun, GPU1=VTC M32 train (pid=921279, 54%)
- 工作目录: `/root/autodl-tmp/importance_margin_vla_compress`
- 活跃 cron 6 个: train_openvla_sc_m96(pid=68539), train_openvla_sc_m32_vtconly(pid=921279), train_openvla_sc_m64_v6(pid=59671), eval_pi05_random_k09_seed43(pid=531274), eval_pi05_l2norm_k01(pid=531007), eval_openvla_l2norm_k09(pid=306593)

### 3. 📊 当前状态
14/14 GPU 满载运行。6 个 RUNNING 实验 + 6 个活跃 cron 监控。

**RUNNING 实验：**
| exp_id | 服务器 | 摘要 |
|--------|--------|------|
| train_openvla_sc_m96_seed42_v3 | westd-41074:2 | VTC M=96 训练，~54%+ |
| train_openvla_sc_m64_seed42_v6 | westd-41074:3 | VTC M=64 训练，第6次重试 |
| train_openvla_sc_m32_vtconly_seed42 | westd-27271:1 | VTC M=32 训练，~54% |
| eval_pi05_random_k09_object_seed43 | westd-41074 | 验证 k=0.9 seed42 异常 |
| eval_pi05_l2norm_k01_object_seed42 | westd-41074 | 极端压缩 90% 移除 |
| eval_openvla_l2norm_k09_object_seed42 | westd-27271:0 | 高保留率 scaling law 数据点 |

**活跃 Worker（2个）：**
- `worker_deploy_westd38929-pi05-cross-suite` — 在 westd-38929 部署 π0.5 cross-suite eval
- `worker_ops_vtc-eval-prep-westd38929` — 在 westd-38929 准备 VTC eval

**等待：** westd-38929 上 8 个 P1 eval（OpenVLA 4 + X-VLA 4）正在跑，Worker 正在为后续 π0.5 spatial eval 做准备。

### 4. 📋 待办（条件触发式）
- westd-38929 P1 eval 完成 → 立即用空出的 GPU 跑 π0.5 spatial suite (baseline/L2norm/random k=0.3/0.5) 或 SmolVLA QUEUED sweep
- VTC M96/M64/M32 训练完成 → spawn Worker 跑 gate eval，形成 M-sweep 曲线
- eval_pi05_random_k09_seed43 完成 → 若 SR ≈ seed42 的 12%，确认 k=0.9 异常是真实的（non-monotonic drop）；若 SR 正常（~80%+），seed42 作废，用 seed43 数据
- eval_pi05_l2norm_k01 完成 → 若仍有显著 SR，是 linear projection immunity 最强证据，直接写入论文 claim
- worker_deploy_westd38929-pi05-cross-suite 完成 → 确认 π0.5 spatial eval 代码/数据就绪，等 GPU 空出即提交
- Paper Agent Step 2 figures 完成 → 推进 Step 3 正文写作，fig_degradation_curve.pdf 已生成

### 5. 🎯 战略上下文
**核心发现（D139 confirmed）：** Connector type 决定 vision token 可压缩性。CV (coefficient of variation) 是预测指标：
- Linear projection (π0.5 CV=0.055, X-VLA CV=0.151) → 高度可压缩，pruning tolerance 高
- MLP projector (OpenVLA CV=0.215) → graded degradation
- Pixel-shuffle (SmolVLA) → catastrophic cliff-edge

**D140 关键发现：** k=0.3 时 π0.5 出现 method preference reversal（L2norm > random），与 k=0.5 处 random > L2norm 相反。X-VLA 无此现象。这暗示 linear projection 在极端压缩下的 token importance 分布变化。

**易错点：**
- 不要把不同 seed 的结果混在同一行——Table 3 刚修复过 5 个 seed 不一致错误（D143）
- π0.5 k=0.7 数据已有（random=77.2%, L2norm=55.0%），D142 确认 v1 已完成，ROADMAP 标的 "running" 可能是残留标记，需核实
- VTC 实验和 pruning 实验是两条独立线：pruning = 无训练直接裁剪测试 connector robustness；VTC = 训练新 compression module。不要混淆
- SmolVLA 的 cliff-edge 是跨所有 k 值的（k=0.95 也是 0% SR），不是只在高压缩率


---
