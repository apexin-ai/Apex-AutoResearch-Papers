# reviewer / loop_7.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`cb1a702b38d6a05b918e.json`](../../sessions/cb/cb1a702b38d6a05b918e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-26T12:02:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-10894 cuda:0-3，westd-34685 cuda:0-3。越界进程立即 CRITICAL + 要求 kill
- cutoff / reverse_cutoff 实验禁止 --resume（C002）
- 10894 上 eval 日志路径在 `/root/runs/occsafe_vla/`，不在 `/root/autodl-tmp/logs/`——之前反复踩坑
- Registry filter 用 `{"exp_id": "xxx"}` 经常返回空，用 `limit=N` 按更新时间降序查更可靠

### 2. 🖥️ 基础设施快照
- **westd-10894**: `/root/occsafe_vla`，训练日志 `/root/runs/occsafe_vla/*.log`，checkpoints `/root/autodl-tmp/checkpoints/`
- **westd-34685**: `/root/occsafe_vla`，同结构
- 两台服务器均 4×A800-96GB
- 10894 当前：cuda:0 跑 reverse_cutoff_s2_v2（~14% 进度），cuda:1/2/3 **空闲**（eval 已完成，PREPARING 实验未启动）
- 34685 当前：4 卡满载（vanilla_v2_s1/s2, detach_ln_s3, cutoff_25k_s1_v2），IO 问题已解决（CKA 进程已 kill），速度恢复 ~1.09 it/s

### 3. 📊 当前状态
刚完成 10894 三组 s3 eval 结果审查并提交报告（第 6 份，累计 11 份）：
- mvp_occ_s3_v2_eval: CAR=0.776, TSR=0.906 → DONE ✅
- ablation_occ_detach_s3_v2_eval: CAR=0.794, TSR=0.922 → DONE ✅
- full_occ_ln_s3_v2_eval: CAR=0.740, TSR=0.842 → ANALYZING（Agent 未录入 metrics）

**Registry RUNNING**: reverse_cutoff_s2_v2 (10894:0), vanilla_v2_s1 (34685:0), vanilla_v2_s2 (34685:1), detach_ln_s3 (34685:2), cutoff_25k_s1_v2 (34685:3)
**Registry PREPARING（未启动！）**: full_occ_ln_v2_s0, full_occ_ln_v2_s1, detach_ln_v2_s0 — 自 11:18 UTC 起一直卡在 PREPARING，已在报告中 WARNING

**已知 bug**: torchrun 退出时 `destroy_process_group()` 警告导致 cron on_failed 误触发。已报告 3 次，Agent 已人工修正 registry，但 cron 逻辑未修复——后续训练完成仍可能收到假 failed 通知

### 4. 📋 待办
- full_occ_ln_s3_v2_eval 状态变 DONE → 核实 metrics 与日志一致（CAR=0.740, TSR=0.842）
- PREPARING 实验（full_occ_ln_v2_s0/s1, detach_ln_v2_s0）启动 → 核实 GPU 分配在白名单内
- 34685 四个训练完成 → 审查结果 + 催 eval 启动
- reverse_cutoff_s2_v2 完成后 → 10894:0 释放给 detach_ln_v2_s1（全 v2 factorial 的瓶颈，预计 May 27 ~06:40 UTC）
- Agent 更新 partial_anova_v2 加入 s3 数据 → 审查新统计结论（预期效应量从 g=-1.023 缩至 ~-0.78，方向不变但 Cell 1 方差很大）

### 5. 🎯 战略上下文
- **核心 story**: Plan B — ordinal interaction，所有 OCC 条件 ≤ Vanilla，Grad OFF > Grad ON，无 crossover
- **v2 rebuild 背景**: v1 的机制证据（gradient collapse, CKA degradation）被发现是代码 bug artifacts，全部实验用 v2 代码重跑
- **当前 factorial 数据**: Cell 1 n=3 (mean=0.725, std=0.064), Cell 2 n=1 (0.740), Cell 3 n=4 (mean=0.767, std=0.024), Cell 4 无 v2 数据, Vanilla n=1 (0.768)
- **最容易判断错的事**:
  1. Cell 1 s1 (0.654) 可能是 outlier——其他两个 seed (0.746, 0.776) 明显更高。如果后续 seed 确认 0.654 是异常值，Cell 1 均值会升至 ~0.76，梯度效应几乎消失
  2. cron on_failed 通知 ≠ 真失败，先看日志尾部确认 EXIT_CODE 和 checkpoint 是否存在
  3. 不要假设 PREPARING 实验会自动启动——本 session 已两次发现 GPU 空闲几十分钟无人管
- **CoRL 2026 deadline**: May 29，距今 ~2.5 天。detach_ln_v2_s1 是 factorial 数据完整的瓶颈（May 27 ~18:00 UTC）


---
