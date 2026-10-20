# code train sft best model config

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_train_sft_best_model_config_20260515T132321_result.json`
- **Structured JSON:** [`00ea1f750a82ccd0051b.json`](../../sessions/00/00ea1f750a82ccd0051b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法验证通过，修改完成。

### 修改汇总

文件：`/root/trace-verdict-study/train/train_sft.py`

**已有（无需改动）：**
- L144: `eval_strategy="epoch"`
- L145: `save_strategy="epoch"`

**新增 4 行（L149-152，插入在 `seed=args.seed` 之后）：**

```diff
         seed=args.seed,
+        save_total_limit=3,
+        load_best_model_at_end=True,
+        metric_for_best_model="eval_loss",
+        greater_is_better=False,
         max_steps=args.max_steps,
```

效果：训练结束后自动加载 eval_loss 最低的 checkpoint 作为 best model，最多保留 3 个 checkpoint。

---
