# diagnose exp 002 signals 15B instruct mmlu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_002_signals_15B_instruct_mmlu_20260516T191453_result.json`
- **Structured JSON:** [`498eb5be36783da4f47a.json`](../../sessions/49/498eb5be36783da4f47a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。结论明确：

**实验并非失败——它已成功完成并正常退出。** 进程被检测为 "dead" 是因为它正常结束了（exit 0），而非崩溃。

证据：
- 输出目录包含完整的 signals 文件：`signal_s1_embedding_mmlu.json`、`signal_s2_minkpp_mmlu.json`、`signal_s4_selfcritique_mmlu.json`（含全部 14042 样本的 chunks）
- `signals_merged_mmlu.json` 已生成（所有 signal 合并完成）
- `exposure_aggregated.json` 和 `exposure_scores.json` 已生成（最终聚合步骤完成）
- 额外还计算了 arc_challenge 和 gsm8k 的 signals（因为 `--signal all --benchmark mmlu` 但 exposure 聚合包含多个 benchmark）
- GPU cuda:4 当前仅 579MiB 占用（进程已释放显存）
- 无 sentinel 文件是因为 `compute_signals.py` 脚本本身不写 sentinel（非 submit_training_job 框架）
- 无 W&B metrics 是因为 signals 计算脚本不上报 W&B

```json
{"root_cause":"进程正常完成后退出（非崩溃），监控系统将正常退出的进程误判为 dead。输出目录包含完整结果：3 个 benchmark × 3 个 signal + merged + exposure_aggregated，共 16 个文件","error_type":"infrastructure","fix_steps":["无需修复——实验已成功完成","将实验状态从 failed 改为 completed","注册产出文件到 artifacts"],"can_auto_fix":true,"partial_output":"无（完整输出）","model_cached":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "进程正常完成后退出（非崩溃），监控系统将正常退出的进程误判为 dead。输出目录包含完整结果：3 个 benchmark × 3 个 signal + merged + exposure_aggregated，共 16 个文件",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复——实验已成功完成",
      "将实验状态从 failed 改为 completed",
      "注册产出文件到 artifacts"
    ],
    "can_auto_fix": true,
    "partial_output": "无（完整输出）",
    "model_cached": true
  }
}
```

</details>

---
