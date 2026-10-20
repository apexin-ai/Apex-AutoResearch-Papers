# diagnose openvla spatial standardized v1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_openvla_spatial_standardized_v1_20260522T092002_result.json`
- **Structured JSON:** [`1469dc613b8118af6cd2.json`](../../sessions/14/1469dc613b8118af6cd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验没有失败——它正在运行中。**

日志已经推进到 3400/5000，每 200 个样本约 80-90 秒。进程 PID 645141 在 GPU 0 上正常跑，68% 利用率，15.3GB 显存。

按当前速度估算：
- 剩余 1600 样本 ÷ 200 × ~85s ≈ **~11 分钟**后 wrong condition 跑完
- 之后还可能有 correct condition 的 counterfactual

```json
{
  "root_cause": "实验未失败。上次查看时日志停在 3000/5000，但进程仍在运行（PID 645141），当前已推进到 3400/5000。日志输出有 buffering 延迟，导致误判为中断。",
  "error_type": "none",
  "fix_steps": ["无需修复，等待完成即可"],
  "can_auto_fix": false,
  "partial_results": "Phase 6 counterfactual (wrong condition) 正在进行，3400/5000。GPU 1 上另有进程(PID 646058)也在运行。无 counterfactual 输出文件（推测完成后才写入）。"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "实验未失败。上次查看时日志停在 3000/5000，但进程仍在运行（PID 645141），当前已推进到 3400/5000。日志输出有 buffering 延迟，导致误判为中断。",
    "error_type": "none",
    "fix_steps": [
      "无需修复，等待完成即可"
    ],
    "can_auto_fix": false,
    "partial_results": "Phase 6 counterfactual (wrong condition) 正在进行，3400/5000。GPU 1 上另有进程(PID 646058)也在运行。无 counterfactual 输出文件（推测完成后才写入）。"
  }
}
```

</details>

---
