# diagnose eval adaptive k spatial p50 seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-adaptive-k-spatial-p50-seed43_20260520T064003_result.json`
- **Structured JSON:** [`2bdd72b837a314d6893a.json`](../../sessions/2b/2bdd72b837a314d6893a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

sentinel 目录为空（wrapper 写 sentinel 时 eval 本身就报错退了，可能根本没走到那步，或者 wrapper 没被用上）。诊断已足够清晰。

## 诊断结论

**根因**：启动命令引用了 `python /root/acr-vla-conformal-refinement/evaluate.py`，但实际文件位于 `/root/acr-vla-conformal-refinement/src/evaluate.py`（多了一层 `src/` 目录）。

`evaluate.py` 完整支持 `adaptive_k` 模式（第 74 行 choices 列表、第 302 行 `select_action_adaptive_k` 函数、第 22 行文档说明 `--mode adaptive_k`）。

```json
{"root_cause":"evaluate.py not found at /root/acr-vla-conformal-refinement/evaluate.py — file is at src/evaluate.py","correct_path":"/root/acr-vla-conformal-refinement/src/evaluate.py","error_type":"infrastructure","fix_steps":["change launch command from 'python /root/acr-vla-conformal-refinement/evaluate.py ...' to 'python /root/acr-vla-conformal-refinement/src/evaluate.py ...'"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "evaluate.py not found at /root/acr-vla-conformal-refinement/evaluate.py — file is at src/evaluate.py",
    "correct_path": "/root/acr-vla-conformal-refinement/src/evaluate.py",
    "error_type": "infrastructure",
    "fix_steps": [
      "change launch command from 'python /root/acr-vla-conformal-refinement/evaluate.py ...' to 'python /root/acr-vla-conformal-refinement/src/evaluate.py ...'"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
