# agent / loop_6.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`dd2fa275be1c8c5b74ac.json`](../../sessions/dd/dd2fa275be1c8c5b74ac.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-15T01:27:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-18228 GPU 白名单: cuda:0-3（4× RTX 4090）；bjb2-40593 只有 cuda:0（1× RTX 4090 D）
- SmolVLA 基线锁定 30%（spatial K=1），不要重跑基线，除非 wrapper 代码改动
- CRM checkpoint 必须用 v3-norm 版本（内嵌 normalization stats），v2 及以前全部废弃（D016 state 6D→8D bug）
- precompute cache 只能用 v5+（precompute-v4 及以前 state 维度错误）
- evaluate.py 中 env.reset() 必须在 set_init_state() 之前，否则静默产生错误结果
- CoRL 2026 abstract DDL ~May 26（D021），时间窗口极紧

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 工作目录 `/root/acr-vla-conformal-refinement/`，Python 路径待 SSH 确认（conda base 或 venv）
  - cuda:0 — eval-acr-spatial-v4-obs-only-r2（running）
  - cuda:1 — eval-argmin-only-spatial（running，已出 3/10 tasks = 53.3%）
  - cuda:2 — eval-tiny-correction-spatial（running，已出 3/10 tasks = 53.3%）
  - cuda:3 — eval-acr-spatial-v4-small（running，已出 T1=60%）
- **bjb2-40593**: 工作目录同上，cuda:0 — eval-vla-mean-spatial-t10（running 或已完成）
- 模型 checkpoint: `/root/acr-vla-conformal-refinement/checkpoints/` 下 crm-v3-norm-perdof / scalar / obs-only
- HF cache / 数据: 在各服务器 `/root/autodl-tmp/` 或本地
- GPU 预算: ~200h 总计，~80h 已用，~120h 剩余

### 3. 📊 当前状态
刚完成 eval-acr-spatial-v4-default-r2 分析：max_norm=1.42（默认）→ 0/5 on T1，确认 D019"normalization alone 不够"。VLA-mean 31% 完成，证明 K=10 averaging 无增益（+1pp noise）。

**Registry RUNNING**:
- eval-argmin-only-spatial: K=10 argmin 无 CRM，已 53.3%（3/10 tasks）——sample selection alone 就很强
- eval-tiny-correction-spatial: max_norm=0.05，已 53.3%（3/10）——与 argmin-only 齐平，correction 可能无害但也无益
- eval-acr-spatial-v4-small: max_norm=0.1，T1=60%（1/10）
- eval-acr-spatial-v4-obs-only-r2: CRM obs-only 模式，测 conformal features 是否真有用
- eval-vla-mean-spatial-t10: VLA-mean 最后一个 task（T10）

**等待中**: 无 Worker 回调待处理。5 个 eval cron 在监控中。eval-acr-spatial-v4-scalar 已 prepared 等 GPU。

### 4. 📋 待办（条件触发式）
- argmin-only + tiny-correction + v4-small 三个都完成 → 对比表：若 argmin-only ≈ tiny-correction >> v4-default → **reframe 为 "sample selection + calibrated magnitude bound"**，提 Framing 调整提案给 Director
- v4-obs-only-r2 完成 → 若 obs_only ≈ perdof → per-DOF conformal features 对 CRM 无关键贡献（D020 confirmed），kill claim 1 原始表述，转向 "structured uncertainty enables magnitude calibration"
- v4-obs-only-r2 完成 + v4-small 完成 → 排 eval-acr-spatial-v4-scalar 上空出的 GPU
- 全部 spatial ablation 完成 → spawn Worker 更新 paper_framing.md + 写 experiment results section
- CoRL 2026 DDL 逼近（~May 26）→ 若 spatial 4-way 结果清晰，立即铺 object benchmark eval（plan_008）

### 5. 🎯 战略上下文
**核心悬念**: ACR-VLA 全量 correction 把 30% baseline 打到 2.5%。但 argmin-only（纯 sample selection）= 53.3%，远超 baseline。**correction delta 本身有害**，magnitude control 是关键——tiny-correction（0.05）和 argmin-only 齐平（53.3%）暗示 CRM 即使极小修正也没增益，per-DOF 的价值可能在 selection 而非 correction。

**Decision chain**: D016（state bug）→ D018（1500x scale root cause）→ D019（norm 不够）→ D020（obs_only 训练 loss 更低？conformal features 可能 hurt）→ D021（回 CoRL 2026）

**易踩的坑**:
1. 不要把 argmin-only 53.3% 和 baseline 30% 直接对比——argmin-only 用 K=10 采样（10× 推理成本），baseline K=1
2. obs_only val_loss (0.0165) < perdof (0.0358) 不等于 obs_only eval 更好——training loss 和 task success 不一定正相关
3. v3-norm checkpoint 内嵌了 normalization stats，eval 代码会自动加载——如果手动改 checkpoint 路径要确认 norm stats 存在
4. 文献支持 magnitude control（PLD/TRANSIC/ResiP/DRC/DAWN），但都是 training-time 方法。inference-time calibrated bound 是本项目的 novelty angle，不要丢掉


---
