# diagnose exp 018 llama8b depth

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_018_llama8b_depth_20260516T153756_result.json`
- **Structured JSON:** [`34489a452efcd48b6de0.json`](../../sessions/34/34489a452efcd48b6de0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**没有失败**——它成功完成了。

## 诊断结论

日志最后一行 `23:27:38 [INFO] Pipeline complete.`，所有产出文件齐全：
- `data/exp_018_llama8b/`: depth_0 到 depth_5 的 6 个 JSONL（每层 ~4MB，5000 samples）+ features.csv
- `results/exp_018_llama8b/`: pairwise_auc.json, jsd.json, ordinal_results.json, feature_importance.json, summary.txt

进程在 23:27 正常退出（exit code 0）。cron 检测到"进程死亡"是因为进程正常结束后 PID 消失，不是崩溃。没有 W&B metrics 是因为这个 pipeline 没有集成 W&B logging（它直接写 JSON 结果文件）。

## 关键结果

| Metric | Value |
|--------|-------|
| K* (max depth AUC > 0.60) | **2** |
| AUC(0v1) | 0.9225 |
| AUC(1v2) | 0.6123 |
| AUC(2v3) | 0.5274 (≈random) |
| Ordinal MAE | 1.3146 |
| Top feature | surp_d1_skew |

```json
{"root_cause":"实验未失败——进程正常完成(exit 0)，日志末尾为 '23:27:38 [INFO] Pipeline complete.'。cron 误报是因为正常退出后 PID 消失","error_type":"infrastructure","fix_steps":["无需修复——实验已成功完成","cron 监控脚本应区分正常退出(exit 0)和异常退出(exit != 0)","如需 W&B tracking，需在 run_pipeline.py 中集成 wandb.log"],"can_auto_fix":false,"partial_results":"全部完成: 6 depth layers × 5000 samples 生成完毕，features extracted，pairwise AUC/JSD/ordinal classification 分析完成。K*=2，即 LLaMA-3.1-8B continuation 模式下 depth ≥ 3 后特征分布趋于饱和(AUC ≈ 0.52)"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "实验未失败——进程正常完成(exit 0)，日志末尾为 '23:27:38 [INFO] Pipeline complete.'。cron 误报是因为正常退出后 PID 消失",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复——实验已成功完成",
      "cron 监控脚本应区分正常退出(exit 0)和异常退出(exit != 0)",
      "如需 W&B tracking，需在 run_pipeline.py 中集成 wandb.log"
    ],
    "can_auto_fix": false,
    "partial_results": "全部完成: 6 depth layers × 5000 samples 生成完毕，features extracted，pairwise AUC/JSD/ordinal classification 分析完成。K*=2，即 LLaMA-3.1-8B continuation 模式下 depth ≥ 3 后特征分布趋于饱和(AUC ≈ 0.52)"
  }
}
```

</details>

---
