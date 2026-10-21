# diagnose scale 14b t15 a050 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scale_14b_t15_a050_s42_fp32_20260522T093206_result.json`
- **Structured JSON:** [`7a817a64d9b02defd709.json`](../../sessions/7a/7a817a64d9b02defd709.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结果

**时间线（本地 UTC+8 / UTC）：**

| 时间 (本地) | 事件 |
|---|---|
| 16:29 | t10_a060 和 t10_a075 在 gen 2 metrics 打印时崩溃: `TypeError: unsupported format string passed to NoneType.__format__`（`iterative_train.py:358`，mauve 返回 None 时用 `:.4f` 格式化） |
| 16:55 | t10 首次重启尝试（_s42_fp32_v2.log, 458 bytes）—— 同样崩溃或被立即杀掉 |
| 17:02 | t10 再次重启为 v2，`--start_gen 2` |
| **17:07** | **t15_a050 和 t15_a060 被 SIGTERM 杀掉**（它们运行正常，gen 1 mauve=0.0330 成功） |
| 17:08 | t15 重启为 v2，`--start_gen 2` |
| 17:12 | `iterative_train.py` 被修改——mauve None 格式化 bug 修复为 `if metrics.get('mauve') is not None else 'N/A'` |

**根因**：另一个 Agent session 在处理 t10 的 TypeError 崩溃时，顺带 SIGTERM 杀掉了仍在正常运行的 t15 实验。这是 C004 的典型违规模式。

**关键风险**：当前 4 个 v2 进程（PID 655758/655834/656957/657037）在 17:02-17:08 启动，**早于代码修复（17:12）**。它们加载的是旧代码。如果 gen 2+ 的 mauve 再次返回 None，会撞同一个 TypeError。

```json
{"root_cause":"Another Agent session SIGTERM-killed both t15 experiments at 17:07 while fixing t10 TypeError crash (iterative_train.py:358, mauve=None formatted with :.4f). t15 experiments were healthy (gen1 mauve=0.0330 succeeded). Log evidence: both logs end with 'Terminated\\nEXIT_CODE=143' at Gen 2 start. No OOM in dmesg, no system-level kill in journalctl.","error_type":"external_kill","fix_steps":["Kill all 4 v2 processes (PID 655758/655834/656957/657037) — they loaded pre-fix code and will crash on None mauve","Verify iterative_train.py line 359 has the None-safe format (already patched at 17:12)","Restart all 4 experiments with --start_gen 2, which will load the fixed code","Add mauve offline fallback: set MAUVE_DEVICE_BATCH_SIZE or cache GPT-2 tokenizer locally to avoid HF connectivity dependency"],"can_auto_fix":true,"affects_other_experiments":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "Another Agent session SIGTERM-killed both t15 experiments at 17:07 while fixing t10 TypeError crash (iterative_train.py:358, mauve=None formatted with :.4f). t15 experiments were healthy (gen1 mauve=0.0330 succeeded). Log evidence: both logs end with 'Terminated\\nEXIT_CODE=143' at Gen 2 start. No OOM in dmesg, no system-level kill in journalctl.",
    "error_type": "external_kill",
    "fix_steps": [
      "Kill all 4 v2 processes (PID 655758/655834/656957/657037) — they loaded pre-fix code and will crash on None mauve",
      "Verify iterative_train.py line 359 has the None-safe format (already patched at 17:12)",
      "Restart all 4 experiments with --start_gen 2, which will load the fixed code",
      "Add mauve offline fallback: set MAUVE_DEVICE_BATCH_SIZE or cache GPT-2 tokenizer locally to avoid HF connectivity dependency"
    ],
    "can_auto_fix": true,
    "affects_other_experiments": true
  }
}
```

</details>

---
