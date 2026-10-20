# code d063 val eval prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d063-val-eval-prep_20260514T120133_result.json`
- **Structured JSON:** [`c61a85ba0ae269fa98c2.json`](../../sessions/c6/c61a85ba0ae269fa98c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### 修改内容

**`eval_repo_verifier.py`** 新增 `--split {val,test}` 参数（默认 `test`，向后兼容）：
- 数据加载从硬编码 `swebench_test.jsonl` 改为 `swebench_{split}.jsonl`
- 报告标题和输出 JSON 均包含 split 标识
- 头部注释已更新

**数据文件无需创建**——`data/swebench_full/` 下已有：
- `swebench_val.jsonl`：9335 samples
- `swebench_test.jsonl`：9784 samples

**注意**：`eval_repo_cls.py` 已有 `--split` 支持，sweep 脚本 (`run_val_sweep.sh`, `run_westd_val_sweep.sh`) 已在用它。

### Val sweep 命令模板

```bash
# eval_repo_verifier.py val sweep
python3 eval_repo_verifier.py \
  --checkpoint_dir &lt;CKPT_PATH> \
  --split val \
  --output val_eval_results/&lt;tag>_val.json \
  --save_predictions \
  --device cuda:0

# 选出 best checkpoint 后，在 test set 报最终数字
python3 eval_repo_verifier.py \
  --checkpoint_dir &lt;BEST_CKPT_PATH> \
  --split test \
  --output final_test_result.json \
  --save_predictions \
  --device cuda:0
```

---
