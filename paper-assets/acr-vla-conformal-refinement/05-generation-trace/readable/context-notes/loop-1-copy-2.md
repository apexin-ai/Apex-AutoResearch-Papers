# agent / loop_1.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`6d4e58b708f0490b2571.json`](../../sessions/6d/6d4e58b708f0490b2571.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-13T22:47:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-18228 GPU 白名单: cuda:0/1/2/3（4× RTX 4090）。bjb2-40593 只有 cuda:0（1× RTX 4090 D）
- CRM 训练 batch_size 必须 ≥512 + lr 线性缩放（bs=32 在 4090 上仅 10% util，Director 明令禁止）
- Worker 修改代码后必须显式部署到服务器 + grep 验证关键特征，不能假设自动同步（D014 教训，第五次）
- evaluate.py env_args 必须包含 `"camera_names": ["agentview", "robot0_eye_in_hand"]`，否则 SmolVLA 只用单目退化
- MUJOCO_EGL_DEVICE_ID 必须为 0（系统只有 1 个 EGL 设备），用 torch.cuda.set_device() 选 GPU
- **引用诚信正在审查中**：ReconVLA (chen2026reconvla) 引用已确认失实，DiU (xing2026diu) 待核查。论文中所有非经典引用需要 WebSearch 验证后才能使用

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 4× RTX 4090, 工作目录 `/root/acr-vla-conformal-refinement/`, Python `/root/miniconda3/bin/python`, conda base
- **bjb2-40593**: 1× RTX 4090 D, 同上路径结构
- 模型: `/root/autodl-tmp/models/smolvla_libero/` (两台服务器都有)
- 数据: `/root/autodl-tmp/libero_data/` (spatial + object)
- Precompute cache: `/root/autodl-tmp/crm_cache/` (K=10, 26,737 samples), `/root/autodl-tmp/crm_cache_k5/` (K=5, 已完成)
- CRM checkpoint: `/root/autodl-tmp/checkpoints/crm/` (crm-train-v1 的 best checkpoint，但训练 EXIT_CODE=129 失败，**需确认 checkpoint 是否可用**)
- 环境变量: `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl`
- 活跃进程:
  - eval-spatial-v5-full: PID 73756, bjb1 cuda:0, cron 300s
  - eval-reconvla-spatial-v2: PID 87787, bjb1 cuda:2, cron 300s
  - eval-object-v4-full: PID 103768, bjb2 cuda:0, cron 300s
- **空闲 GPU**: bjb1 cuda:1, bjb1 cuda:3（crm-train-v1 和 precompute-k5 完成后释放）

### 3. 📊 当前状态
**刚做完：**
- precompute-k5 成功 (K=5 cache 完成)
- crm-train-v1 失败 (EXIT_CODE=129, epoch 32/50, best val_loss=0.009412 at epoch 31)
- Introduction + Experiments 框架写完（占位数字待填）
- Claim 强度分析完成：C1 Moderate (MVP only), C2/C3 No Evidence

**正在等待的 Worker 回调（5 个并行）：**
1. `worker_diagnose_crm-train-v1-failure` — CRM 失败诊断，看是否有 best checkpoint 可恢复
2. `worker_research_reconvla-deep-read` — ReconVLA 原文深度阅读 + ACR-VLA 差异化分析
3. `worker_audit_data-augmentation-code` — CRM 训练增强代码核实（论文声称 3 种增强 vs 代码只有 noise）
4. `worker_audit_diu-citation-check` — DiU 引用核查
5. `worker_diagnose_eval-object-v4-task1` — object eval Task 1 全失败诊断

**还有之前的 Worker 未确认：**
- `worker_research_reconvla-citation-audit` — 可能已完成但未读取
- `worker_analysis_mvp-data-backfill` — MVP 数据补录

### 4. 📋 待办（条件触发式）
- CRM 诊断 Worker 回调 → 如有 best checkpoint 可用 → 直接启动 CRM eval (ACR-VLA mode)；如无 → 重启 CRM 训练 (bs=512, lr=0.016)，cuda:1
- eval-spatial-v5-full cron 完成 → SFT gate 判定：≥80% proceed / 50-80% adjust / <30% 换模型
- eval-reconvla-spatial-v2 完成 → 重命名结果为 SampleConsensus baseline（不能叫 ReconVLA）
- eval-object-v4-full 完成 → 汇报 object suite 成功率
- ReconVLA 深度阅读 Worker 回调 → 汇报差异化分析给 Director，决定是否调整论文 framing
- 引用审计全部完成 → 汇总所有可疑引用，修改 references.bib 和论文文本
- cuda:1 空闲 + CRM 重启/完成后 → 启动 K=3 precompute（消融下界）
- cuda:3 空闲 → 可用于 A3 ablation (obs_only CRM) 训练，C1 的 make-or-break test
- precompute-k5 完成 → K=5 CRM 训练（bs=512, cuda:1 or cuda:3）

### 5. 🎯 战略上下文
- **投稿目标**: ICLR 2027 (DDL Sep-Oct 2026)，~4-5 个月
- **核心假设**: Per-DOF conformal features (40D CGS) > scalar Euclidean > no uncertainty，目前仅 MVP 合成数据验证，LIBERO 零验证
- **最大风险**: C1 的 A3 ablation — 如果 CRM without conformal features 仅差 <2%，核心 claim 不成立
- **引用危机进行中**: ReconVLA 引用确认失实（我们的 `--mode reconvla` 是自造的 argmin-Euclidean 启发式，与 ReconVLA 论文无关）。真实 ReconVLA 也是 CP-based 方法，是最直接竞争者。DiU 引用待核查。这可能需要调整论文 framing
- **eval-object Task 1 全失败**: 可能是 object suite 本身难度高，也可能是 bug，诊断中
- **关键路径**: CRM checkpoint 恢复/重训 → ACR-VLA eval → A3/A4 ablation → 首个 real LIBERO 结果
- **易错点**:
  - 不要把 `--mode reconvla` 的结果归因给 ReconVLA 论文，已确认是不同方法
  - eval 数据只有 2/10 tasks 完成，不要用部分均值做决策
  - CRM 重训必须用 bs≥512，否则 Director 会 CRITICAL
  - 两台服务器代码版本必须一致，改一台要同步另一台


---
