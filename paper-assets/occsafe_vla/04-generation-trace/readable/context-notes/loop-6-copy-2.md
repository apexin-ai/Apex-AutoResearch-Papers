# agent / loop_6.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`db8a35cb4c646b8bd3a1.json`](../../sessions/db/db8a35cb4c646b8bd3a1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-27T12:06:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-10894 cuda:0-3, westd-34685 cuda:0-3（共 8 张，全部在跑，无空闲）
- **DDL: May 28 12:00 UTC**（SafeRL Workshop @ RSS 2025）——所有决策以此为硬约束
- 论文数据**必须用 v2**——v1 数据（Full OCC BN=0.797）已被 D043 标记为不可复现，禁止纳入主 claim
- 禁止措辞：crossover interaction / BN-mediated gradient calibration / existence regularization / 跨 v1-v2 梯度数值比较
- D067: Cell 4 Detach LN 在 v2 多 seed 到位前标为 v1 数据（`$^\star$`），省略 ΔCAR
- D066: 放弃 binomial test 作为主要论证，改用 2×2 factorial ANOVA
- 10894 曾磁盘满（100%→已清理至 45%/139G free），checkpoint 保存风险已解除但需持续关注

### 2. 🖥️ 基础设施快照
- **westd-34685**: `/root/occsafe_vla`，conda env `occsafe`（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe`）
- **westd-10894**: `/root/occsafe_vla`，conda env `occsafe`，同上激活方式
- 模型：`/root/autodl-tmp/models/openvla-7b`（两台服务器均有）
- 数据：`/root/autodl-tmp/data/modified_libero_rlds/libero_spatial_no_noops`（55370 条）
- OCC 数据：`/root/occsafe_vla/occ_data`
- Checkpoints：`/root/autodl-tmp/checkpoints/&lt;exp_id>/`
- WANDB_MODE=disabled（所有实验）
- 磁盘：34685 正常 / 10894 250G 中 139G free (45%)
- **活跃进程（8 个，全部有 cron 监控）**：

| 服务器:GPU | exp_id | PID | Cell | ETA (UTC) |
|-----------|--------|-----|------|-----------|
| 34685:0 | detach_ln_v2_s1_35 | 681124/681204 | Cell 4 v2, seed 43 | ~12:58 May 27 |
| 34685:1 | detach_ln_s4 | 677568 | Cell 4, seed 46 | ~12:59 May 27 |
| 34685:2 | ablation_occ_detach_s4 | 735898 | Cell 3, seed 46 | ~13:46 May 27 |
| 34685:3 | mvp_occ_s4 | 736253 | Cell 1, seed 46 | ~13:52 May 27 |
| 10894:0 | full_occ_ln_v2_s1c_r2 | 481426 | Cell 2 v2, seed 43 | ~22:50 May 27 |
| 10894:1 | full_occ_ln_v2_s2_r2 | 481643 | Cell 2 v2, seed 44 | ~22:40 May 27 |
| 10894:2 | detach_ln_v2_s0c_r3 | 543255 | Cell 4 v2, seed 42 | ~06:20 May 28 |
| 10894:3 | full_occ_ln_s4 | 553813 | Cell 2, seed 46 | ~06:50 May 28 |

### 3. 📊 当前状态
8/8 GPU 满载，9 个 cron 在监控（reconcile 刚确认全部 still running）。0 个 Worker 在跑。

**v2 Factorial 数据进度**：

| Cell | Condition | v2 n (已有) | 训练中 | 完成后 v2 n |
|------|-----------|-------------|--------|-------------|
| 1 | Full OCC BN | 3 | +s4 | 4 |
| 2 | Full OCC LN | 1 | +s1c_r2, s2_r2, s4 | 4 |
| 3 | Detach BN | 4 | +s4 | 5 |
| 4 | Detach LN | 1 | +s1_35, s0c_r3 (+s4 is v1) | 3 (v2) |
| Vanilla | — | 3 | — | 3 ✅ |

**CRITICAL #9 关键路径**：Cell 2 和 Cell 4 各需 v2 n≥3 才能跑全 v2 2×2 ANOVA。
- Cell 2 v2 n=3: ~00:00 May 28（s1c_r2 + s2_r2 训练完 → eval 各 ~40min）
- Cell 4 v2 n=3: ~07:10 May 28（s0c_r3 训练完 → eval ~40min）
- 全 v2 ANOVA + Table 1 更新 + 最终编译: ~07:30-11:00 May 28
- DDL: May 28 12:00 UTC — **极紧，无 buffer**

D069 Reviewer 系统性审查已批准 5 项论文修复（梯度图 v1→v2、abstract 等），进行中。

### 4. 📋 待办（条件触发式）
- **批次① cron 回调（~13:00 May 27, 34685:0-1 完成）** → spawn eval Worker 跑 detach_ln_v2_s1_35 + detach_ln_s4 的 50-rollout SafeLIBERO eval → 结果更新 Cell 4 v2/v1 数据
- **批次② cron 回调（~13:50 May 27, 34685:2-3 完成）** → spawn eval Worker 跑 ablation_occ_detach_s4 + mvp_occ_s4 eval → 更新 Cell 3 n=5 / Cell 1 n=4(5) → 中间编译论文
- **批次③ cron 回调（~22:50 May 27, 10894:0-1 完成）** → eval full_occ_ln_v2_s1c_r2 + full_occ_ln_v2_s2_r2 → **Cell 2 v2 n=3 达成** → 可跑 partial ANOVA
- **批次④ cron 回调（~06:30 May 28, 10894:2-3 完成）** → eval detach_ln_v2_s0c_r3 + full_occ_ln_s4 → **Cell 4 v2 n=3 达成** → 全 v2 2×2 ANOVA + Table 1 最终更新
- **全 v2 ANOVA 完成 → 最终编译 + 提交**（预留 ~1h，不晚于 11:00 May 28）
- 任何实验 cron 回调 conclusion=failed → 诊断 + 汇报 Director（磁盘满/OOM 最可能）

### 5. 🎯 战略上下文
**核心结论**：gradient flow ON 损害 VLA 安全行为（CAR），detach 后 aux head ≈ Vanilla（统计不可区分 p=0.28）。BN 放大损害。论文以 2×2 factorial ANOVA 效应量为核心证据，梯度正交性（cosine≈0）为辅助排除证据。

**决策链关键节点**：D043 v2 推翻 v1 crossover → Plan B ordinal interaction；D057 所有 v1 机制证据失效；D066 放弃 binomial 改 ANOVA；D067 Cell 4 LN 暂标 v1 数据。

**易错点**：
- detach_ln_v2_s1_35 的 `run_root_dir` 实际是 `detach_ln_v2_s1`（不是 `detach_ln_v2_s1_35`），是 ghost process，eval 时 checkpoint 路径在 `/root/autodl-tmp/checkpoints/detach_ln_v2_s1/`
- detach_ln_s4 是 **v1 代码** Cell 4 数据（不是 v2），标 `$^\star$`
- full_occ_ln_s4 也是 v1 代码 Cell 2 扩展数据
- eval 命令需要 `conda activate occsafe`，50 rollout，SafeLIBERO benchmark
- Cell 1 高方差（std=0.064）是 feature 不是 bug——BN+gradient flow 导致训练不稳定，本身是 finding
- 10894 磁盘已清理但仍需关注——如果多个 checkpoint 同时保存可能再次紧张


---
