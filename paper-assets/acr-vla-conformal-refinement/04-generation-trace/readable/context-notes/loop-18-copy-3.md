# reviewer / loop_18.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_18.md`
- **Structured JSON:** [`02f941d17081246b25f8.json`](../../sessions/02/02f941d17081246b25f8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_wall_time
updated: '2026-05-19T11:19:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- **LTO eval 的 task_names 过滤**：evaluate.py 中绝对不能有 `.replace("_", " ")`。之前这个 bug 导致 5 个 held-out tasks 只匹配 2 个，已修复但 train_crm.py 中的 replace 是正确的（因为 HDF5 task names 用空格）。两个文件的 task name 格式不同，不要统一处理。
- **CRM v3_norm 训练无日志**：checkpoint 在 `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`（bjb1-18228），但没有任何训练日志。已确认 input_dim=990（obs_only），训练数据来自 Spatial+Object（26,737 samples）。不要尝试"找到"训练日志——它不存在，这是已知的 traceability gap（已报告 Director）。
- **bjb1-18228 上的实验被批量 kill 过**：GPU 清理 Worker 在 ~04:30 UTC kill 了 6 个实验（norm003-seed43/45/46/49, norm005-seed46, perdof-norm03-seed48）。这些实验的 partial 数据已丢失。不要把它们当成 "failed" 去排查 bug——是人为终止。
- **Batched inference 代码已同步到所有 4 台服务器**：MD5 = `f06be4d8fd62a1db9fcdd9d09549d683`。已运行的实验不受影响（代码在启动时加载到内存），新实验会使用 batched path。

### 2. 🖥️ 基础设施快照
- **4 台服务器**：bjb2-28827(root, 6 GPU), bjb1-32546(root, 6 GPU), bjb1-18228(root, 4 GPU), bjb2-40593(root, 1 GPU)
- **工作目录**：`/root/acr-vla-conformal-refinement`（所有服务器相同）
- **Python**：`/root/miniconda3/bin/python`（bjb1-18228 无 `python3`，必须用绝对路径）
- **CRM checkpoint**：`/root/autodl-tmp/checkpoints/crm_v3_norm/{obs_only,perdof,scalar}/crm_best.pt`
- **LTO checkpoint**：`/root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/crm_best.pt`（bjb1-18228 only）
- **SmolVLA**：`/root/autodl-tmp/models/smolvla_libero/`
- **Cache**：`/root/autodl-tmp/crm_cache_v3/{object,spatial}/`（26,737 total samples）
- **ssh_read_only 限制**：不能用 `;` `|` `&&` `>`，python -c 必须用单表达式（如 `print(__import__('torch').load(...)['key'].shape)`）

### 3. 📊 当前状态
**刚完成**：D067 Adaptive K 论文影响评估（建议不升 C4，batched 下无延迟优势）。LTO eval bug 修复验证通过。ROADMAP 审查完成。

**关键 RUNNING 实验**（按优先级）：
- **P0 K=5 seeds**：seed46(bjb1-18228 cuda:3 独占), seed47(bjb1-18228 cuda:0 独占), seed48(bjb1-32546 GPU2) — ETA ~6h
- **P0 LTO eval**：`eval-lto-splitA-heldout-r2`(bjb1-18228 cuda:1, CRM K=5), `eval-lto-splitA-vla-only-r3`(bjb1-18228 cuda:1 共享) — 5/5 held-out tasks
- **P1 K=5 argmin**：seed42(bjb2-28827 cuda:4), seed43(bjb1-18228 cuda:2), seed44(bjb2-28827 cuda:1) — component decomposition at K=5
- **P2 Spatial**：K=10 seed43(bjb2-40593), seed44(bjb2-28827), seed45(bjb1-32546); K=5 seed42(bjb2-28827), seed43(bjb1-32546)
- **Fill 实验**：obs_only norm005-seed48, perdof norm005-seed47, perdof norm003-seed47（bjb1-18228 各 GPU 双跑）
- **Magnitude sweep**：bjb1-32546 和 bjb2-28827 上还有 ~10 个 norm003/norm005/perdof 实验

**等待中**：
- 用户决策：K=5 vs K=10 primary（batched 下延迟相同，K=10 统计更强）
- Adaptive K 实验部署（9 experiments, 3 seeds × 3 thresholds）— 待用户回复后执行

### 4. 📋 待办（条件触发式）
- K=5 seed46/47/48 完成 → 更新 K=5 统计（目标 n≥7, p≈0.003），重新评估 K=5 vs K=10 primary 决策
- LTO eval heldout-r2 + vla-only-r3 完成 → 对比 CRM vs VLA-only 在 held-out tasks 上的 SR，评估泛化 claim 是否成立
- K=5 argmin seed42/43/44 完成 → 验证 K=5 下 selection ≈ 0 是否仍成立（K=10 decomposition 的 K=5 版本）
- Spatial K=10 seed43/44/45 完成 → Table 1 Spatial 行填充，多 benchmark 证据
- 用户回复 K=5 vs K=10 → 可能需要回切 primary 到 K=10（所有 K=10 数据已存在）
- Adaptive K 实验部署通知 → 审查实验配置（threshold 值、seeds、benchmark）
- ε=0.03 magnitude 数据仍然稀薄（n≤2）→ 如有 GPU 空闲建议补跑
- default-seed47 即将完成（bjb1-32546, task 9/10 时进度 ~95%）→ 审查结果

### 5. 🎯 战略上下文
**核心叙事**："Correction Over Selection" — CRM learned correction 是 active mechanism（+5.2pp），multi-sampling 是 enabling condition（提供 centered starting point），selection 本身 ≈ 0。obs_only conditioning 稳定，perdof collapse。

**决策链**：D058(CRM是correction非selection) → D063(K=5捕获82%收益) → D064(component decomposition) → D065(reframe为analysis paper) → D066(K=5 primary) → D067(batched inference + adaptive K)

**最容易判断错的事**：
1. **不要假设 Adaptive K 有延迟优势**——batched 下 K=2≈K=5≈314ms，full path 反而 2× 慢。我已多次向 Director 强调这一点。
2. **不要混淆 train_crm.py 和 evaluate.py 的 task_name 格式**——training 用空格（HDF5 demo descriptions），eval 用下划线（LIBERO env names）。两者的 replace 逻辑必须不同。
3. **ε=0.03 magnitude "稳定" claim 有风险**——多个 seed 被 kill 后仅剩 n≤2，是 magnitude curve 最薄弱的点。
4. **K=5 vs K=10 primary 决策可能反转**——batched 消除了 K=5 的延迟优势，K=10 有更强统计（n=7, p=0.0025）。等用户回复。
5. **Latency 叙事要谨慎**——paper_framing 中说 VLA-Pilot 2.41s "prohibitive" 但我们 pipeline 1.778s 也不是 realtime。已报告但未修复。

**Memory 文件**：`memory/crm_training_data.md`（CRM v3_norm 训练数据组成）、`memory/latency_inconsistency.md`（pipeline vs VLA-Pilot 延迟对比问题）


---
