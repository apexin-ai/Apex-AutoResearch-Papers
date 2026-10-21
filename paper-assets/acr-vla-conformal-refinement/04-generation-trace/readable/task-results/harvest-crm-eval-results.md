# harvest crm eval results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_crm-eval-results_20260523T004025_result.json`
- **Structured JSON:** [`b20c78c8a0411bd01577.json`](../../sessions/b2/b20c78c8a0411bd01577.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 收集结果汇总

**所有 eval 仍在运行中**，约完成 50-60%，预计还需 1-1.5h。

### 关键发现

1. **bjb2-28827 Spatial CRM 全部失败** — 启动命令误加 `--input_mode obs_only`（参数不存在）。3 个 seed 的 CRM spatial eval 全部报错退出。Spatial CRM 数据靠 bjb1-32546 的正确运行实例。

2. **初步趋势不乐观**（部分数据）：
   - **Object CRM** ~52% vs VLA-only baseline 66.0% → CRM 拉低
   - **Spatial CRM** ~72% vs wrapper VLA-only ~76% → CRM 略低（但高于 lerobot 58%）
   - **Goal CRM** ~56% vs baseline 78.5% → CRM 显著拉低

3. **Goal seed44 无法部署** — bjb1 cuda:3 被 4-suite 训练占用（已跑 12h52m），bjb2 cuda:3,4,5 被 VLA-only spatial 占用。最早可用：VLA-only spatial 完成后在 bjb2 部署。

### 当前 GPU 分配

| 服务器 | GPU | 任务 | 进度 |
|--------|-----|------|------|
| bjb2-28827 | 0,1,2 | Object CRM s42/43/44 | 5/10 tasks |
| bjb2-28827 | 3,4,5 | Spatial VLA-only s42/43/44 | 6/10 tasks |
| bjb1-32546 | 0,1,2 | Spatial CRM s42/43/44 | 5-6/10 tasks |
| bjb1-32546 | 3 | CRM 4-suite training r4 | 12h52m elapsed |
| bjb1-32546 | 4,5 | Goal CRM s42/43 | 4-5/10 tasks |

中间报告已写入 `artifacts/crm_eval_results_harvest.md`。完整结果需等 eval 全部跑完后再次收集。

---
