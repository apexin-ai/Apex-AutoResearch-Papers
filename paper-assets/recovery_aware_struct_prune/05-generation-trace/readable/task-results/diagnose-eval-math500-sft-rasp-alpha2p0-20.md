# diagnose eval math500 sft rasp alpha2p0 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_sft_rasp_alpha2p0_20_20260522T203005_result.json`
- **Structured JSON:** [`e402c2ce70107aa29eef.json`](../../sessions/e4/e402c2ce70107aa29eef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整诊断完成。

**时间线重构：**

| 时间 | 事件 |
|------|------|
| 05-22 13:48 | Pipeline 启动：RASP α=2.0 剪枝 |
| 05-22 13:49 | 剪枝完成（19.09% sparsity），模型保存 |
| 05-22 13:52 | SFT 阶段 **OOM 崩溃**：`torch.OutOfMemoryError` at `optimizer.step()` |
| 05-22 14:40 | SFT **被单独重跑**并成功完成（模型文件写入时间） |
| 05-22 23:06 | MATH-500 eval 单独启动（CUDA_VISIBLE_DEVICES=1） |
| 05-23 04:03 | Eval 完成：**accuracy = 24.0%** (120/500) |

**OOM 根因：** Pipeline 的 SFT 阶段在 `cuda:0` 启动时，该 GPU 上已有两个进程占用 66.33 GiB（Process 2234: 17.12 GiB + Process 11979: 49.21 GiB），本进程需要 28.62 GiB，总计 ~95 GiB 超过 GPU 容量 94.97 GiB。在 Adam optimizer 初始化 `exp_avg_sq` 时触发 OOM。

**Cron 误判：** Cron 监控的是原始 pipeline 进程（EXIT_CODE=1），后续 SFT 和 eval 是单独运行的，cron 检测不到 sentinel/W&B，判定失败。但实验实际已完成。

```json
{"root_cause":"SFT阶段OOM: cuda:0上3个进程竞争(17.12+49.21+28.62=~95GiB > 94.97GiB容量), Adam optimizer初始化exp_avg_sq时触发torch.OutOfMemoryError。但SFT后续被单独重跑成功(模型14:40写入), eval也完成(05-23 04:03, accuracy=24.0%)","error_type":"resource","actually_completed":true,"result_file":"/root/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20.json","fix_steps":["无需修复——实验已完成, accuracy=0.24 (120/500), 结果文件已生成","若需重跑pipeline: 用CUDA_VISIBLE_DEVICES指定空闲GPU避免资源竞争","建议cron增加对results目录的sentinel文件检测, 避免误判手动重跑的实验"]}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "SFT阶段OOM: cuda:0上3个进程竞争(17.12+49.21+28.62=~95GiB > 94.97GiB容量), Adam optimizer初始化exp_avg_sq时触发torch.OutOfMemoryError。但SFT后续被单独重跑成功(模型14:40写入), eval也完成(05-23 04:03, accuracy=24.0%)",
    "error_type": "resource",
    "actually_completed": true,
    "result_file": "/root/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20.json",
    "fix_steps": [
      "无需修复——实验已完成, accuracy=0.24 (120/500), 结果文件已生成",
      "若需重跑pipeline: 用CUDA_VISIBLE_DEVICES指定空闲GPU避免资源竞争",
      "建议cron增加对results目录的sentinel文件检测, 避免误判手动重跑的实验"
    ]
  }
}
```

</details>

---
