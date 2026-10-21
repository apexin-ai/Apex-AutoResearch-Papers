# diagnose eval math500 sft cka only 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_sft_cka_only_20_20260518T023345_result.json`
- **Structured JSON:** [`fedbe6883886a9edc787.json`](../../sessions/fe/fedbe6883886a9edc787.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认：从 `src/` 目录运行就能导入 `model_utils`。

根因确定：实验命令从项目根目录执行 `python src/eval_math500.py`，但 `eval_math500.py` 内部 `from model_utils import load_pruned_model` 需要 `model_utils.py`（同在 `src/` 下）。Python 不会自动把脚本所在目录加到搜索路径，导致 `ModuleNotFoundError` 启动即崩。无日志是因为 crash 发生在 logging 初始化之前的 import 阶段。

```json
{"root_cause":"ModuleNotFoundError: No module named 'model_utils' — 从项目根目录运行 python src/eval_math500.py 时，src/ 不在 sys.path 中，无法导入同目录下的 model_utils.py","error_type":"infrastructure","fix_steps":["方案A: cd /root/recovery_aware_struct_prune/src && CUDA_VISIBLE_DEVICES=2 python eval_math500.py --model_path ... --output_path ...","方案B: PYTHONPATH=/root/recovery_aware_struct_prune/src CUDA_VISIBLE_DEVICES=2 python src/eval_math500.py ...","方案C: 在 eval_math500.py 开头加 sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "ModuleNotFoundError: No module named 'model_utils' — 从项目根目录运行 python src/eval_math500.py 时，src/ 不在 sys.path 中，无法导入同目录下的 model_utils.py",
    "error_type": "infrastructure",
    "fix_steps": [
      "方案A: cd /root/recovery_aware_struct_prune/src && CUDA_VISIBLE_DEVICES=2 python eval_math500.py --model_path ... --output_path ...",
      "方案B: PYTHONPATH=/root/recovery_aware_struct_prune/src CUDA_VISIBLE_DEVICES=2 python src/eval_math500.py ...",
      "方案C: 在 eval_math500.py 开头加 sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
