# code eval repo cls prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-repo-cls-prep_20260512T194143_result.json`
- **Structured JSON:** [`d63df4a52a3000d6bba1.json`](../../sessions/d6/d63df4a52a3000d6bba1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`eval_repo_level.py` 已存在且通过语法验证，无需新建 `eval_repo_verifier.py`。

**现有脚本** `eval_repo_level.py` 已覆盖所有需求：

| 需求参数 | 现有脚本 | 状态 |
|---------|---------|------|
| `--checkpoint_dir` | ✓ required | OK |
| `--data_dir` | ✓ default `data/swebench_full` | OK |
| `--output` (任务中叫 `--output_file`) | ✓ `--output` | OK |
| `--device` | ✓ default `cuda:0` | OK |
| `--batch_size` | ✓ default 16 | OK |
| `--max_seq_length` | ✓ default 2048 | OK（训练也是 2048） |
| metrics | accuracy, F1, precision, recall, confusion matrix | OK |
| `--save_predictions` | ✓ JSONL per-sample | OK |

**训练完成后运行命令：**

```bash
cd /home/sonny/exec-sim-repair-verifier
python eval_repo_level.py \
  --mode cls \
  --checkpoint_dir checkpoints_repo_cls_home/best \
  --output eval_repo_cls.json \
  --save_predictions \
  --device cuda:0
```

**备注：**
- 训练脚本 `train_repo_verifier.py` 的 `max_seq_length` 默认 2048，eval 脚本匹配
- 测试集 `swebench_test.jsonl` 有 9784 条样本
- System prompt 和 user template 与训练完全一致（都用 `"## Patch (git diff)\n{code}\n\n## Test\n{test}\n\nWill this test pass or fail?"`）
- `checkpoints_repo_cls_home/` 目前为空，训练尚未 save checkpoint（save_steps=200）

---
