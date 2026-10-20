# code fix gpu arg

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-gpu-arg_20260515T005708_result.json`
- **Structured JSON:** [`480c8b973284f6d7960b.json`](../../sessions/48/480c8b973284f6d7960b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

**改动**：在 `train_sft.py` 第 112-113 行（`args = parser.parse_args()` 之后）添加：

```python
if args.gpu is not None:
    os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu
```

`--help` 验证通过，脚本正常加载。`--gpu` 参数现在会在模型加载之前设置 `CUDA_VISIBLE_DEVICES`，确保训练使用指定的 GPU。

---
