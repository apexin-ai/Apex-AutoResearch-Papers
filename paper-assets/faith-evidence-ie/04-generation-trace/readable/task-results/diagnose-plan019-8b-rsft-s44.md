# diagnose plan019 8b rsft s44

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan019_8b_rsft_s44_20260518T233934_result.json`
- **Structured JSON:** [`c193b48f0feca60eccdb.json`](../../sessions/c1/c193b48f0feca60eccdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

RSFT 输出目录完整：checkpoint-1134 = 3018 samples / (batch 1 × grad_accum 8) × 3 epochs = 1134 steps，正好对应训练全部完成。

诊断结果：

```json
{
  "exp_id": "plan019_8b_rsft_s44",
  "root_cause": "日志路径错误：registry 记录 plan019_8b_rsft_s44.log 但该文件不存在。实际 RSFT 训练已完成——输出目录 /root/autodl-tmp/rsft_output_qwen3_8b_k1_s44/ 有完整 adapter (698MB) 和 checkpoint-1134 (= 3ep × 378 steps，与 3018 samples / grad_accum 8 精确匹配)。监控系统因找不到 log + 无 W&B run（服务器 HF_HUB_OFFLINE=1 环境下 wandb 可能未上传）而误判 failed。",
  "error_type": "infrastructure",
  "actually_succeeded": true,
  "fix_steps": [
    "将 registry 状态从 failed 更新为 completed",
    "补登 RSFT 输出路径: /root/autodl-tmp/rsft_output_qwen3_8b_k1_s44/",
    "后续提交任务时确保 log 重定向路径与 registry 一致"
  ],
  "can_auto_fix": true
}
```

```json
{
  "exp_id": "plan019_8b_sft_s44_eval",
  "root_cause": "eval 实际已成功完成。输出目录有 metrics.json (ign_f1=0.4681, evi_f1_joint=0.3839, 985 docs, inference_time=6951s) 和 predictions.json (7.4MB)。进程正常退出后 PID 消失，监控未检测到 sentinel 而误报。",
  "error_type": "infrastructure",
  "actually_succeeded": true,
  "metrics_summary": {
    "ign_f1": 0.4681,
    "evi_f1": 0.8361,
    "evi_f1_joint": 0.3839,
    "edcr": 0.6697,
    "field_compliance_rate": 0.6883,
    "n_truncated": 306
  },
  "fix_steps": [
    "将 registry 状态更新为 completed",
    "录入 metrics 到实验追踪表"
  ],
  "can_auto_fix": true
}
```

**总结**：两个实验都实际成功完成，均为监控误判。实验1是日志路径不匹配导致监控找不到 log；实验2是进程正常退出后缺少 sentinel 标记。RSFT adapter 和 eval metrics 都已完整落盘。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "exp_id": "plan019_8b_sft_s44_eval",
    "root_cause": "eval 实际已成功完成。输出目录有 metrics.json (ign_f1=0.4681, evi_f1_joint=0.3839, 985 docs, inference_time=6951s) 和 predictions.json (7.4MB)。进程正常退出后 PID 消失，监控未检测到 sentinel 而误报。",
    "error_type": "infrastructure",
    "actually_succeeded": true,
    "metrics_summary": {
      "ign_f1": 0.4681,
      "evi_f1": 0.8361,
      "evi_f1_joint": 0.3839,
      "edcr": 0.6697,
      "field_compliance_rate": 0.6883,
      "n_truncated": 306
    },
    "fix_steps": [
      "将 registry 状态更新为 completed",
      "录入 metrics 到实验追踪表"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
