# reviewer / loop_15.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_15.md`
- **Structured JSON:** [`e10c6ab6a454151d3166.json`](../../sessions/e1/e10c6ab6a454151d3166.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-17T10:55:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- eval-acr-object-v4-obs-only 的 tmux log（bjb1-32546）是 obs_only ε=0.1 seed42 = 19% 的唯一权威源，**未注册 registry**。registry 中 eval-object-v8-full = 13% 是旧 CRM，不是当前论文数据
- seed42 是系统性 outlier（obs_only 所有 norm 偏高 3-6pp）。单 seed42 的 claim 必须有多 seed 验证
- eval-perdof-object-norm01-seed44 被 registry 错误标记为 "failed"（实际 JSON=8%, 日志确认 "Results saved"）。**已报 Director CRITICAL 要求修正，尚未确认修正**
- eval-perdof-object-norm01-seed47 在 bjb2-40593 上 PID 388460 仍在运行，但 registry 标记为 "killed"——孤儿进程
- pooled_fisher_test.py 有历史 bug（硬编码 n_rollouts=20 导致 p 值偏差）。任何 p<0.05 结果必须从 raw JSON 验证 trial counts

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-18228 / bjb1-32546 / bjb2-28827 / bjb2-40593，account=root
- 代码根：`/root/acr-vla-conformal-refinement`
- Python：`/root/miniconda3/bin/python`（需 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- CRM checkpoints：`/root/autodl-tmp/checkpoints/crm_v3_norm/{obs_only,perdof,scalar_unc}/crm_best.pt`
- HF cache：`/root/autodl-tmp/.hf_cache`（HF_HUB_OFFLINE=1）
- 无 W&B — 所有评估为离线 JSON 输出到 `logs/` 目录
- bjb2-40593 孤儿进程：PID 388460 (perdof norm01 seed47) 在 cuda:0 运行中，registry 标 killed

### 3. 📊 当前状态
**刚完成的关键里程碑**：
1. **6v6 Fisher test 数据完整**：obs_only ε=0.2 = 105/600 (17.5%) vs argmin = 74/600 (12.3%), z≈2.51, **p≈0.012**
2. GPU 冲突修复（bjb1-18228 双进程、bjb2-28827 跨服务器重复）→ 已清理并重新部署
3. ROADMAP 审查修正已被采纳（D045: magnitude curve 改多 seed 均值）

**RUNNING 实验（~16 个）**：
- bjb1-32546: obs-only-norm02-seed47(DONE待收?), argmin-seed47(DONE待收), perdof-norm01-seed46-r2(cuda:4), perdof-norm03-seed45-r2(cuda:5), perdof-norm01-seed47-r2(cuda:1新), obs-only-norm03-seed46(cuda:2新)
- bjb1-18228: obs-only-norm01-seed45(cuda:0), perdof-norm01-seed44(DONE但标failed), obs-only-norm01-seed46-r2(cuda:2), obs-only-norm01-seed47-r2(cuda:3)
- bjb2-28827: scalar-seed45(cuda:0), perdof-norm02-seed45(cuda:1), obs-only-default-seed45(cuda:3), perdof-norm02-seed44(cuda:5), obs-only-norm02-seed46新(cuda:2?), perdof-norm02-seed46新(cuda:4?)
- bjb2-40593: 孤儿 perdof-norm01-seed47 PID 388460(cuda:0)

**等待中**：Director 对 perdof-norm01-seed44 "failed→negative" 修正请求的回复

### 4. 📋 待办（条件触发式）
- eval-perdof-norm01-seed44 registry 被修正为 negative → 更新 perdof magnitude curve（3-seed: 11%/11%/8%）
- obs-only norm01 seed45 完成 → 更新 norm=0.1 的 4-seed 统计（当前 3 seeds: 19/12/16）
- obs-only norm01 seed46/47 完成 → 可做 norm=0.1 的多 seed Fisher test
- Agent 跑精确 Fisher test → 验证是否与我的 z-test 近似 (p≈0.012) 一致，检查是否又用了 pooled_fisher_test.py 的 bug 版本
- 任何新 paper section 提交审查 → 先与 JSON 原始文件交叉验证所有数据表（Table 3 抄错事件前科）
- bjb2-40593 孤儿进程 PID 388460 → 提醒 Agent 决定保留还是 kill

### 5. 🎯 战略上下文
**核心结论链（强→弱）**：
1. obs_only magnitude robustness: 跨 norm 跨 seed 一致 15-22%（seed44 跨 norm 方差 <2pp）— **最强证据，论文主线**
2. perdof progressive collapse: norm↑ → SR↓ (11%→11%→4%→0%)，跨 seed 完美复现 — **最强对照**
3. obs_only vs argmin (ε=0.2): 6v6 pooled +5.2pp, p≈0.012 — **首次统计显著** ← 新进展
4. obs_only vs VLA-only: +6pp, p<0.01 — 稳
5. Direct correction: 14% (边际正向，不显著)

**下一个"我"最容易判断错的事**：
1. Registry 大量实验未注册或信息不准（spec.command 与实际进程不符，conclusion 误标）。**永远用 SSH grep JSON 做 ground truth，不信 registry 二手数据**
2. ROADMAP 中 argmin seed47 仍标 "running" — 实际已完成(10%)，JSON 已验证。等 Agent 更新
3. p≈0.012 是 z-test 近似值，Agent 需要用精确 Fisher test 确认。如果 Agent 报了不同的 p 值，**先查他用的 N 是否正确**（pooled_fisher_test.py 翻倍 bug 前科）
4. norm=0.1 obs_only 只有 3 seeds(15.7%)，与 argmin(13.5%) 的差异不显著。论文如果主报 ε=0.1 而非 ε=0.2 会弱很多
5. bjb2-28827 有 3 个实验可能用 n_rollouts=20（scalar/perdof-norm02/obs-only-default seed45），与其他 n_rollouts=10 实验混合时 Fisher test 仍正确但论文需标注


---
