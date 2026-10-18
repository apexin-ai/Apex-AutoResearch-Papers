# diagnose exp008 sdgd zero fewnerd

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp008_sdgd_zero_fewnerd_20260515T103240_result.json`
- **Structured JSON:** [`ece2825b65cd8f0c3ab3.json`](../../sessions/ec/ece2825b65cd8f0c3ab3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验没有失败，仍在运行。**

关键证据：

1. **进程存活**：PID 254943 (`sdgd_extract_gpu.py`) 仍在运行，CPU 20%
2. **vLLM 引擎存活**：PID 255250，占用 94212MiB GPU 显存
3. **sdgd_zero 已完成**：结果写入于 18:24，F1=0.2514，耗时 408.7s，8 batch 全部跑完
4. **single_pass 已完成**：结果写入于 18:26，F1=0.4451，耗时 77.3s
5. **dmesg 无 OOM/segfault**
6. **磁盘充足**：根分区 45%，数据盘 79%

日志看似"停在 batch 7/8 的 91%"是因为：
- `tail` 输出被截断（省略了 124869 字符的进度条内容）
- 实际上 sdgd_zero 全部 8 个 batch 已跑完，脚本已进入后续策略（single_pass 已完成，当前可能在跑 random_batch 或 per_type）

```json
{"root_cause":"实验未失败。进程 PID 254943 仍在运行，sdgd_zero (F1=0.2514) 和 single_pass (F1=0.4451) 均已完成并保存结果。日志中的'停顿'是 tail 输出截断导致的假象。","error_type":"none","fix_steps":["无需修复，等待实验自然完成","用 tail -f artifacts/exp008_run2.log 实时跟踪进度"],"can_auto_fix":false,"partial_results":"有。sdgd_zero: F1=0.2514 (8 batches, 408.7s); single_pass: F1=0.4451 (1 batch, 77.3s)。均在 artifacts/exp008/ 下。"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "实验未失败。进程 PID 254943 仍在运行，sdgd_zero (F1=0.2514) 和 single_pass (F1=0.4451) 均已完成并保存结果。日志中的'停顿'是 tail 输出截断导致的假象。",
    "error_type": "none",
    "fix_steps": [
      "无需修复，等待实验自然完成",
      "用 tail -f artifacts/exp008_run2.log 实时跟踪进度"
    ],
    "can_auto_fix": false,
    "partial_results": "有。sdgd_zero: F1=0.2514 (8 batches, 408.7s); single_pass: F1=0.4451 (1 batch, 77.3s)。均在 artifacts/exp008/ 下。"
  }
}
```

</details>

---
