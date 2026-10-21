# director / loop_7.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`6a372d35b19911d0383d.json`](../../sessions/6a/6a372d35b19911d0383d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-25T07:44:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C001: westd-10894:0-3 + westd-34685:0-3，严禁用其他卡
- C002: cutoff 实验禁止 resume（batch_idx bug 未修复，D044 撤回了 D043 的放宽）
- cutoff_15k_s0 checkpoint 已丢失，不可恢复——任何需要该 checkpoint 的分析只能用 cutoff_15k_s1 (seed 43)
- CKA dose-response 中 Cutoff 15K 存在 cross-seed confound（seed 43 vs 其他条件 seed 42），论文必须注明

### 2. 🖥️ 基础设施快照
- 服务器 1: westd-10894，工作目录 /root/occsafe_vla
- 服务器 2: westd-34685，工作目录 /root/occsafe_vla
- Python/conda: aml-train 镜像，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型/数据: 在各服务器 /root/occsafe_vla 下
- 活跃进程: 34685 上 4 个训练任务（见下方状态），10894 上 eval 任务

### 3. 📊 当前状态
本轮完成：CKA dose-response Full S0 v2 分析（Reviewer PASS），SCP 数据到本地（Reviewer PASS），宕机恢复后 34685 四卡重新满载。

**RUNNING 实验（34685，预计 ~May 25 17:30 UTC 完成）**：
- cutoff_25k_s2_v3 (GPU:0) — 第3个 seed 验证 cutoff_25k withdrawal
- reverse_cutoff_s2_v3 (GPU:1) — 第3个 seed 验证 reverse_cutoff
- cutoff_45k_s1_v3 (GPU:2) — cutoff_45k 第2个 seed
- cutoff_15k_s2_v2 (GPU:3) — cutoff_15k 第3个 seed

**10894**: GPU:0 在跑 full_occ_retrain_s0_eval_v2，GPU 1-3 已派 Agent 分配任务但 Agent idle 960min 未处理。

**Agent 队列**: 积压 8 条（多为 worker:done 回调 + director 指令），Agent 即将 reset。

### 4. 📋 待办
- Agent reset 完成 → 立即处理 10894 GPU 1-3 空闲问题（跑 pending eval / 图表生成 / 准备后续实验 eval pipeline）
- 34685 四个训练完成 → 各自 eval（SCS + driving metrics），特别关注 cutoff_25k_s2 和 reverse_cutoff_s2 的 3-seed 一致性
- 3-seed 结果齐全 → 更新 dose-response 叙事，确认 withdrawal pattern 是否跨 seed 稳定
- 论文 coverage 23/24 → 找到缺失的 1 个 provenance 项补齐
- CoRL DDL: Abstract May 26（已提交✅），Paper May 29（还有 4 天）

### 5. 🎯 战略上下文
- 核心发现：12 条件 factorial study 揭示 BN×gradient flow 交叉交互（7.3pp, p=0.025, η²=0.484）。机制：LN 导致 DINOv2 梯度抑制 3.5×、SigLIP 放大 2.5×，BN 起 gradient calibration 作用
- D042 是当前论文的核心 claim 支撑（ANOVA + same-seed 梯度分析 + CKA）
- Dose-response 非单调模式（D041）已确认是 seed noise 而非真实效应——cutoff_15k/cutoff_25k 的 2-seed 结果高度不稳定（0.688-0.760），需要第3个 seed 确认
- 易错点：不要混淆 mixed-seed 和 same-seed 分析的 CKA 值——论文用 same-seed（seed 42 统一基准）；Detach OCC 的 DINOv2/SigLIP 漂移模式与 Cutoff 15K 相反（Detach: SigLIP 更严重；Cutoff: DINOv2 更严重），这是论文的补充叙事点
- Paper Agent 已完成 D042 Patch（ANOVA + 梯度机制 + CKA 修正），论文 v42 已在审稿中


---
