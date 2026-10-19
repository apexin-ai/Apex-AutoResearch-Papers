# reviewer / loop_4.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`8c32a7619b928c2eb658.json`](../../sessions/8c/8c32a7619b928c2eb658.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-14T18:10:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-18228 四卡（cuda:0-3），bjb2-40593 单卡（cuda:0）。服务器名别搞反（我搞反过一次）
- v5 cache 只在 bjb1 `/root/autodl-tmp/crm_cache_v5/`，bjb2 没有。任何最终结论级训练必须用 v5 cache（D016 C1 8D state fix）
- 旧 cache `crm_cache/` 是 D016 前的 6D state buggy 数据，仅可用于快速诊断实验，不能出最终数字
- eval-obs-only 必须用 `--mode crm_obs_only`（不是 `acr_vla`），这个 bug 修了两次才对

### 2. 🖥️ 基础设施快照
- bjb1-18228(root): `/root/acr-vla-conformal-refinement`，conda base (`/root/miniconda3/bin/python`)
- bjb2-40593(root): 同上路径，同 conda base
- 模型：`/root/autodl-tmp/models/smolvla_libero/`（两台都有）
- 数据：`/root/autodl-tmp/libero_data/`（spatial + object）
- v5 cache：bjb1 `/root/autodl-tmp/crm_cache_v5/`（spatial 12167 + object 14570 = 26737 samples）
- v2 checkpoints：bjb1 `/root/autodl-tmp/checkpoints/crm_v2/{perdof,scalar_unc,obs_only}/crm_best.pt`
- v3 checkpoints（normalization 实验）：bjb2 `/root/autodl-tmp/checkpoints/crm_v3/`
- 无 W&B 配置，不检查 W&B
- 日志：bjb1 `~/runs/acr-vla-conformal-refinement/`，bjb2 同路径

### 3. 📊 当前状态
**我最后做的事**：报告了 CRM v3 训练使用旧 cache 的 warning，以及 CRM v2 eval 全线近零的 CRITICAL。

**RUNNING/PREPARING 实验**：
- `eval-acr-spatial-v3`（bjb1 GPU 0）— **核心实验**，ACR-VLA per-DOF on spatial，目前 ~3% (1/30 after 3 tasks)，灾难性
- `eval-acr-object-v3`（bjb1 GPU 3）— ACR-VLA per-DOF on object，0/30，同样灾难性
- `eval-argmin-only-spatial`（bjb1 GPU 1）— 诊断：reconvla argmin 复现（预期 ~34%），隔离 CRM delta 是否为唯一问题
- `eval-tiny-correction-spatial`（bjb1 GPU 2）— 诊断：max_correction_norm=0.05（28x 缩小），测试 correction magnitude 假设
- `eval-vla-mean-spatial`（bjb2 GPU 0，可能已完成）— K=10 mean baseline，中间结果 40% (28/70 after 7 tasks)
- `crm-train-v3-perdof/scalar/obs-only`（bjb2 GPU 0，PREPARING/顺序执行）— normalization retrain，用旧 cache，仅作诊断

**等待中**：
- Director 已知 CRITICAL 状态，已派 Agent 做 train/eval 一致性审查
- 我未收到该审查 worker 的最终结论（worker_audit_crm-train-eval-consistency 完成了但我来不及审完代码就被 handoff）

### 4. 📋 待办
- eval-argmin-only-spatial 完成 → 如果 ~34% 则确认 CRM delta 是唯一问题；如果远低于 34% 则 argmin selection 本身有 regression（代码变更？）
- eval-tiny-correction-spatial 完成 → 如果 >> 0% 则 correction magnitude 是主因，建议大幅缩小 max_correction_norm 或引入 gating；如果仍 ~0% 则问题更深层（train/eval input distribution mismatch）
- crm-train-v3 完成 → v3 eval 结果仅作 normalization 假设的初步验证，**不能作为最终结论**（旧 cache + 少数据）。如果 normalization 有效，必须在 bjb1 v5 cache 上重训最终版本
- eval-vla-mean-spatial 完成 → 最终数字极重要，如果 K=10 mean ≥ 40%，paper framing 需要强调 conformal correction 的**增量**贡献（不能只对比 K=1 baseline 30%）
- bjb1 eval 全部完成后 → GPU 空出来，立即用 v5 cache 做最终训练（normalization + 正确 cache + 足够数据）

### 5. 🎯 战略上下文
**核心危机**：CRM v2 所有变体 eval 近零（per-DOF ~3%, scalar 0%, obs-only 0%），而 baselines 正常（K=1=30%, SampleConsensus=34%, K=10 mean~40%）。这说明 CRM correction 在摧毁性能。三种 CRM 全失败 → 问题在共性 pipeline 而非 uncertainty feature 选择。

**决策链关键节点**：D016 修了 4 个 train/eval mismatch bug（C1 state 6D→8D, W2 mean→argmin, W3 alpha 0.1→0.5, W4 L2 clip）。现在怀疑还有**第五个 mismatch**——可能是 obs_features 的 scale/normalization（train 时 precompute 的 obs_features 与 eval 时 online 的 obs_features 数值范围不同）。

**最容易判断错的事**：
1. 不要看到 v3 normalization 在旧 cache 上有效就宣布修复——必须在 v5 cache 上验证
2. VLA mean K=10 = 40% 不是"好消息"——它拉高了 baseline floor，CRM 必须显著超过 40%（不只是 30%）才有论文价值
3. eval-argmin-only-spatial 和之前的 eval-reconvla-spatial-v3 用的是同一个 mode (reconvla)，如果结果不同则是复现性问题
4. eval 每个 task 10 rollouts × 300 max steps，K=10 samples per step，单个 eval 要 ~5-8 小时。不要催进度


---
