# gsm8k_profiling_ds 诊断报告

**结论：实验成功完成，Cron 误报。**

## 失败根因

**不是真正的失败。** 两个进程（PID 245311 importance, PID 245312 random）均正常跑完全部 50/50 problems 后自然退出。Cron 监控检测到 PID 不存在后标记为 failed，属于 false positive。

佐证：
- Exit file `/tmp/agent-ml-exit/gsm8k_ds_imp.exit` 内容：`0|2026-05-15T16:28:20Z`（exit code = 0）
- 日志无任何 traceback、OOM、CUDA error
- "无 W&B metrics" 也是误判——该 profiling 脚本不使用 W&B，结果存本地 JSON

## 进程退出时的状态

| 进程 | 最后日志时间 | 完成度 | 结果 |
|------|-------------|--------|------|
| ds_importance (PID 245311) | 2026-05-16 00:14:24 | 50/50 | **PASS** — low vs mid CI non-overlapping at sparsity 0.3 |
| ds_random (PID 245312) | 2026-05-16 00:35:51 | 50/50 | **FAIL** — random masking 各 phase 间差异无统计显著性 |

运行时长：importance ~2.4h，random ~2.7h（random 比 importance 慢约 20min，因在 GPU 1 共享资源）。

## 产出文件（完整，无需抢救）

```
analysis_output/gsm8k/ds_importance/
  profiling_results.json  (2.1MB)
  generations.json        (179KB)

analysis_output/gsm8k/ds_random/
  profiling_results.json  (2.2MB)
  generations.json        (179KB)
```

## 关键实验结果摘要

**DS + Importance masking (PASS):**
- low_sparsity 各 level II ≈ 0（baseline 区域无 importance 差异，符合预期）
- high_sparsity 0.3: II = +73.82, CI = [+9.93, +154.48]（强正信号）
- mid_sparsity 0.3: II = +291.36, CI = [+28.35, +570.06]

**DS + Random masking (FAIL):**
- 所有 phase 类型在所有 sparsity level 均有正 II（random 也造成损失）
- 无法区分 phase 类型，importance masking 的选择性优势未体现

## 修复建议

无需修复代码或重跑实验。需要做的是：
1. **更新 registry 状态**：将 `gsm8k_profiling_ds` 从 `failed` 改为 `completed`
2. **改进 Cron 监控逻辑**：检测到进程退出时，应先检查 exit code（读 `/tmp/agent-ml-exit/*.exit`）再判定成败

## gsm8k_profiling_qw 健康状态

| PID | 方法 | 状态 | 运行时长 | GPU | VRAM |
|-----|------|------|----------|-----|------|
| 245313 | qw_importance | Rl (running) | ~2h | GPU 2 | 49.3GB / 97.9GB |
| 245314 | qw_random | Rl (running) | ~2h | GPU 3 | 21.5GB / 97.9GB |

两个 QW 实验进程健康运行中，GPU 利用率 96-97%。预计还需 ~1-2h 完成。

---
*诊断时间：2026-05-16 00:38 UTC*
