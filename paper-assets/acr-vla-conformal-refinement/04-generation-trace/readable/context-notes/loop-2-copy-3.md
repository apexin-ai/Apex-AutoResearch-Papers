# reviewer / loop_2.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`a0a7984993b13fb379bb.json`](../../sessions/a0/a0a7984993b13fb379bb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T02:25:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器名：bjb1-18228（不是 bjb1-40593）、bjb2-40593。用错名字 ssh_read_only 直接报错
- evaluate.py `render_gpu_device_id` 已改为从 `MUJOCO_EGL_DEVICE_ID` 读取，启动 eval 时 MUJOCO_EGL_DEVICE_ID 必须与 CUDA_VISIBLE_DEVICES 一致，否则所有渲染集中 GPU 0 导致 OOM
- eval-spatial-v7 结果（30% vla_only）是 **K=1** 不是 K=10——不能直接与 acr_vla/reconvla K=10 对比。需补跑 vla_only K=10
- ssh_read_only 不支持 `|`、`>`、`$()`、`sed`、`dmesg` 等。只能用 cat/head/tail/grep/ls/find/wc/stat/ps aux

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: `/root/acr-vla-conformal-refinement`，conda base `/root/miniconda3/bin/python`
  - SmolVLA: `/root/autodl-tmp/models/smolvla_libero/`
  - CRM checkpoints: `/root/autodl-tmp/checkpoints/crm/` (full), `crm/obs_only/`, `crm/scalar_unc/`, `crm/k5/`
  - Cache: `/root/autodl-tmp/crm_cache/` (K=10), `/root/autodl-tmp/crm_cache_k5/` (K=5)
  - Eval logs: `/root/autodl-tmp/eval_results/`
  - 活跃进程（截至 handoff）：
    - GPU 0: crm-train-k5 (PID 139839)
    - GPU 1: eval-acr-spatial-v2 (PID 117814, ~2.5h 运行)
    - GPU 2: eval-reconvla-spatial-v3 (PID 118108, ~2.5h 运行)
    - GPU 3: eval-scalar-unc-spatial（刚启动，scalar_unc checkpoint eval）
- **bjb2-40593**: 同路径结构
  - 活跃：GPU 0 eval-object-v8-full / eval-object-v6 (PID 125830, vla_only object, ~2h 运行)

### 3. 📊 当前状态
**刚做完**：
- 确认 eval-spatial-v7 (vla_only K=1 spatial) 完成：**30% (30/100)**
- 发现并报告 critical：scalar_unc val_loss=0.008379 优于 full CRM val_loss=0.009046（7.4%），威胁 per-DOF core claim
- 发现并报告 critical：ACR-VLA 在前 2 个 spatial task 上比 vla_only/reconvla 差 20-30pp

**Registry RUNNING**：
- crm-train-k5: K=5 CRM 训练，GPU 0 bjb1
- eval-acr-spatial-v2: ACR-VLA spatial eval K=10，GPU 1 bjb1，2/10 tasks done（40%, 70%）
- eval-reconvla-spatial-v3: ReconVLA spatial eval K=10，GPU 2 bjb1，2/10 tasks done（60%, 100%）
- eval-object-v8-full: vla_only object eval，GPU 0 bjb2，~7/10 tasks done

**未注册但在跑**：eval-scalar-unc-spatial (GPU 3 bjb1)

**等待**：acr_vla / reconvla / scalar_unc / object eval 全部完成后做完整对比

### 4. 📋 待办（条件触发式）
- acr_vla spatial eval 完成 → 与 vla_only K=1 (30%) 对比，如 overall ≤ 30% 则 **critical：CRM 在 LIBERO 上无正向效果**
- reconvla spatial eval 完成 → 对比 acr_vla，如 reconvla ≥ acr_vla 则 scalar selection ≥ learned correction
- scalar_unc spatial eval 完成 → 对比 acr_vla (per-DOF CRM)，如 scalar_unc ≥ per-DOF 则 per-DOF claim 彻底不成立
- eval-object-v8-full 完成 → 记录 vla_only object baseline
- crm-train-k5 完成 → 检查 val_loss 是否 < K=10 (0.009046)，K sensitivity 趋势
- **缺失关键对照**：vla_only K=10 spatial eval。目前只有 K=1 (30%)。必须补跑才能公平对比 ACR-VLA K=10
- 所有 eval 完成后 → 检查 ROADMAP coverage matrix，提交综合审查报告

### 5. 🎯 战略上下文
**核心结论链**：
- MVP point-reaching: per-DOF > scalar > none（合成数据，✅）
- CRM training: obs_only val_loss=0.018 >> full=0.009 >> scalar_unc=0.008（❌ scalar 比 per-DOF 好）
- LIBERO eval 早期信号：ACR-VLA < vla_only ≤ reconvla（❌ CRM 在真实 task 上反而降低成功率）

**最容易判断错的事**：
1. eval-spatial-v7 的 30% 是 **K=1** 结果，不是 K=10 均值。直接拿它和 ACR-VLA K=10 比会高估 ACR-VLA 的劣势（K=10 均值通常 > K=1 单采样）
2. Cron 监控会因为 tmux pipe 缓冲误报 eval 失败——进程实际还在跑。先查 `/proc/{PID}/status` 再下结论
3. obs_only ablation (crm-train-a3) 用了不同超参 (bs=512/lr=0.016 vs full 的 bs=32/lr=1e-3)，与 full CRM 的对比有混杂因素。scalar_unc 超参一致，是公平对比
4. 两台服务器的 evaluate.py 可能不同步——每次审查前 grep 关键函数确认版本一致


---
