# ssh check evaluate save predictions

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_evaluate_save_predictions_20260515T141131_result.json`
- **Structured JSON:** [`2c4c990b40b6ca825190.json`](../../sessions/2c/2c4c990b40b6ca825190.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

### evaluate.py 当前状态

**不支持 `--save_predictions`。** 没有该参数，也没有保存 per-sample predictions 的逻辑。

推理循环（`main()` 约第 120-140 行）中已经收集了 `labels`, `preds`, `raw_preds` 三个列表，但只用它们计算 aggregate metrics，最终只写入 `results = {condition, checkpoint_dir, metrics, confidence_intervals}` 到 `eval_results.json`。

### Qwen eval_results.json

只有 4 个 key：`condition`, `checkpoint_dir`, `metrics`, `confidence_intervals`。**没有 per-sample predictions 数据。**

### 需要修改的地方

在 `main()` 函数中加两处改动即可：

1. **添加 `--save_predictions` 参数**（argparse 部分，约第 100 行）：
   ```python
   parser.add_argument("--save_predictions", action="store_true",
                       help="Save per-sample predictions to predictions.jsonl")
   ```

2. **推理循环结束后保存 per-sample 数据**（约第 145 行，`compute_metrics` 调用之前或之后）：
   ```python
   if args.save_predictions:
       pred_path = os.path.join(os.path.dirname(os.path.abspath(args.output)), "predictions.jsonl")
       with open(pred_path, "w") as f:
           for i, item in enumerate(test_data):
               json.dump({"id": i, "label": labels[i], "pred": preds[i], "raw_pred": raw_preds[i]}, f)
               f.write("\n")
       print(f"Predictions saved to {pred_path}")
   ```

不需要改推理循环本身——`labels`, `preds`, `raw_preds` 已经在收集了，只是没有写出来。

---
