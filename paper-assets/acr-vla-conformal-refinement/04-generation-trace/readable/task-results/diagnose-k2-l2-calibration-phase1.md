# diagnose k2 l2 calibration phase1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_k2-l2-calibration-phase1_20260519T210033_result.json`
- **Structured JSON:** [`f94b632e6ff48792d700.json`](../../sessions/f9/f94b632e6ff48792d700.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

## 诊断结论

**k2-l2-calibration-phase1**：

- **之前的运行已成功完成**（exit code 0，2026-05-20 02:59 CST），输出 `fmvd_calibration.json`（3.3MB），包含完整的 Spearman ρ = 0.0825 (p < 1e-22) 等指标
- Cron 报 "failed" 是 **false positive**——脚本输出 JSON 而非 W&B，cron 检测不到 sentinel/W&B 标记就自动标记失败
- **当前有一个新的 k2_l2_calibration 运行**（PID 995736，04:32 启动，GPU 1），进度 11/50 episodes，预计还需 ~100 分钟，输出将写入 `logs/k2_l2_calibration.json`

**eval-vla-only-spatial-seed48**：服务器上无任何 seed48+spatial 相关文件或进程痕迹，该实验不在 bjb2-28827 上。

**系统状态**：6× RTX 4090 正常，5 个实验并行运行（GPU 0-5），无 OOM/重启迹象。

```json
{"root_cause":"Cron monitoring looked for W&B/sentinel markers but calibrate_fmvd.py outputs JSON to logs/fmvd_calibration.json. Exit file shows exit code 0 at 2026-05-19T18:59:06Z. Output file (3.3MB) is complete with valid JSON.","error_type":"false_positive","actually_succeeded":true,"metrics":{"spearman_rho":0.082528,"spearman_pvalue":2.33e-23,"fmvd_mean":0.054867,"fmvd_std":0.040291,"fmvd_P50":0.046693,"fmvd_P90":0.093805,"k10_variance_mean":0.004888,"n_steps_collected":14512},"fix_steps":["No fix needed — experiment completed successfully","Output at logs/fmvd_calibration.json","A new run targeting logs/k2_l2_calibration.json is currently in progress (PID 995736, ~11/50 episodes done)","eval-vla-only-spatial-seed48 was never on bjb2-28827 — check other servers"]}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "Cron monitoring looked for W&B/sentinel markers but calibrate_fmvd.py outputs JSON to logs/fmvd_calibration.json. Exit file shows exit code 0 at 2026-05-19T18:59:06Z. Output file (3.3MB) is complete with valid JSON.",
    "error_type": "false_positive",
    "actually_succeeded": true,
    "metrics": {
      "spearman_rho": 0.082528,
      "spearman_pvalue": 2.33e-23,
      "fmvd_mean": 0.054867,
      "fmvd_std": 0.040291,
      "fmvd_P50": 0.046693,
      "fmvd_P90": 0.093805,
      "k10_variance_mean": 0.004888,
      "n_steps_collected": 14512
    },
    "fix_steps": [
      "No fix needed — experiment completed successfully",
      "Output at logs/fmvd_calibration.json",
      "A new run targeting logs/k2_l2_calibration.json is currently in progress (PID 995736, ~11/50 episodes done)",
      "eval-vla-only-spatial-seed48 was never on bjb2-28827 — check other servers"
    ]
  }
}
```

</details>

---
