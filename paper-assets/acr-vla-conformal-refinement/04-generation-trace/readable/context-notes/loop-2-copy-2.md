# agent / loop_2.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`e96ab0c85dc534f0ebe8.json`](../../sessions/e9/e96ab0c85dc534f0ebe8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-14T02:26:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`bjb1-18228:cuda:0/1/2/3` + `bjb2-40593:cuda:0`，共 5 张。白名单外的 GPU 一律 push back Director
- bjb2-40593 只有 1× RTX 4090 D（注意是 D 版本），仅分配 cuda:0
- SmolVLA 在 AutoDL 上必须 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`，否则 AutoProcessor 联网失败导致静默崩溃
- submit_training_job 的 command 必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && ...`
- Ablation 实验（plan_002/003/006/007/009/010/011）**必须**用 baseline 超参 bs=32/lr=1e-3，否则 confound 对比
- evaluate.py 的 vla_only 模式必须 K=1（已有自动覆盖），其他模式用 K=10
- env.reset() 必须在 set_init_state() **之前**调用，不能省也不能调换顺序

### 2. 🖥️ 基础设施快照
- **bjb1-18228**（4× RTX 4090）：工作目录 `/root/acr-vla-conformal-refinement`，Python `/root/miniconda3/bin/python`（conda base），数据盘 `/root/autodl-tmp/`
  - 模型：`/root/autodl-tmp/models/smolvla_libero/`
  - CRM checkpoint（per-DOF baseline）：`/root/autodl-tmp/checkpoints/crm/crm_best.pt`（val_loss=0.009046）
  - CRM checkpoint（scalar-unc A4）：`/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt`（val_loss=0.008379）
  - CRM checkpoint（obs-only A3）：`/root/autodl-tmp/checkpoints/crm/obs_only/crm_best.pt`（val_loss=0.018312）
  - Precompute cache K=10：`/root/autodl-tmp/crm_cache/`（26737 samples，spatial+object）
  - Precompute cache K=5：`/root/autodl-tmp/crm_cache_k5/`（26737 samples）
  - Eval 输出：`/root/autodl-tmp/eval_results/`
  - HF cache：`/root/autodl-tmp/.hf_cache`
- **bjb2-40593**（1× RTX 4090 D）：同样路径结构，`/root/acr-vla-conformal-refinement`，conda base
- **活跃进程**（全部有 cron 监控）：
  - `eval-acr-spatial-v2`：PID 117814，cuda:1，bjb1-18228（ACR-VLA 主结果）
  - `eval-reconvla-spatial-v3`：PID 118108，cuda:2，bjb1-18228（SampleConsensus baseline）
  - `eval-scalar-unc-spatial`：PID 143206，cuda:3，bjb1-18228（scalar CRM ablation eval）
  - `crm-train-k5`：PID 139839，cuda:0，bjb1-18228（K=5 ablation 训练）
  - `eval-object-v8-full`：PID 125830，cuda:0，bjb2-40593（SmolVLA object baseline）

### 3. 📊 当前状态
5 张 GPU 全部在跑，0 个 Worker 活跃。上一轮完成了：CRM baseline 训练、obs-only ablation（2x worse，确认 conformal features critical）、scalar-unc ablation（val_loss 0.008 略优于 per-DOF 的 0.009）、SmolVLA spatial baseline（30%）。

**RUNNING 实验清单**：
| exp_id | GPU | 用途 |
|--------|-----|------|
| eval-acr-spatial-v2 | bjb1:cuda:1 | **ACR-VLA 主实验**——per-DOF CRM 矫正 spatial，核心结果 |
| eval-reconvla-spatial-v3 | bjb1:cuda:2 | SampleConsensus baseline（scalar argmin），与 ACR-VLA 对比 |
| eval-scalar-unc-spatial | bjb1:cuda:3 | Scalar CRM ablation eval，验证 per-DOF vs scalar 在 task success 上的差异 |
| crm-train-k5 | bjb1:cuda:0 | K=5 sensitivity ablation 训练，与 K=10 baseline 对比 |
| eval-object-v8-full | bjb2:cuda:0 | SmolVLA object baseline，等结果 |

**等待中**：5 个 cron 监控回调。无 Worker 回调。无 Director 待决策。

### 4. 📋 待办（条件触发式）
- `eval-acr-spatial-v2` 完成 → **最关键**：ACR-VLA 成功率 vs SmolVLA 30% baseline。≥35% = 正向（per-DOF correction 有效），<30% = negative（需 Framing 提案）
- `eval-reconvla-spatial-v3` 完成 → SampleConsensus 成功率。与 ACR-VLA 对比得出 "correction vs selection" 优势。注意：当前 SampleConsensus 是 raw argmin，低估了真实 ReconVLA（CQR + argmin）
- `eval-scalar-unc-spatial` 完成 → 与 ACR-VLA(per-DOF) 对比。scalar val_loss 更低(0.008 vs 0.009) 但 hypothesis 是 per-DOF 在 task success 上赢
- `crm-train-k5` 完成 → 启动 `eval-k5-spatial`（K=5 CRM eval），与 K=10 对比做 K sensitivity 分析
- `eval-object-v8-full` 完成 → SmolVLA object baseline 数字，后续需要 ACR-VLA object eval
- **三个 spatial eval 都完成后** → 汇总表格（VLA-only 30% / SampleConsensus X% / Scalar-CRM Y% / ACR-VLA Z%）→ 向 Director 汇报 + 更新 report.md
- Object eval 完成 + ACR-VLA spatial 有结果 → 铺 ACR-VLA object eval + SampleConsensus object eval（需要在 bjb2 上跑）

### 5. 🎯 战略上下文
- **投稿目标**：ICLR 2027（DDL Sep-Oct 2026），CoRL 2026 已放弃（D011）
- **核心 claim**：Per-DOF conformal statistics → dimension-selective action correction 优于 scalar selection（ReconVLA 的路线）
- **MVP 已验证**（synthetic 3D reaching）：per-DOF 比 scalar 好 6.75%，比 none 好 16.71%
- **关键悬念**：scalar CRM 在 val_loss 上略优于 per-DOF (0.008 vs 0.009)。如果 scalar 在 task success 上也赢，核心 claim 受挑战——但 hypothesis 是 val_loss 不能完全预测 task success，per-DOF 的维度选择性在复杂任务（spatial 中 0% 那些）上的优势体现在 success rate
- **易踩坑**：
  1. 不要把 SampleConsensus（raw argmin）等同于 ReconVLA（CQR + argmin），SampleConsensus 低估了 ReconVLA
  2. EXIT_CODE=129 不一定是失败——tmux SIGHUP，看 log 确认
  3. 代码修改后两台服务器（bjb1/bjb2）必须同步部署验证
  4. 数据增强代码只有 1 种（CGS 高斯噪声），论文声称 3 种——写论文时需修正
  5. SmolVLA baseline 30% 很低，"next_to" 类任务 90-100% 但精确空间任务（on/in/from）几乎 0%——ACR-VLA 的价值在后者


---
