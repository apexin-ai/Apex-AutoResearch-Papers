# debug repo level v2 failure

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_repo-level-v2-failure_20260512T160624_result.json`
- **Structured JSON:** [`e6b842c4d6e09fcdc67d.json`](../../sessions/e6/e6b842c4d6e09fcdc67d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both dry-runs completed. Here's the full diagnostic report.

---

## 诊断报告

### 失败原因

两个脚本（`train_repo_verifier.py` 和 `train_repo_cwm.py`）在 DataLoader 第一次取 batch 时崩溃，报错：

```
ValueError: type of {'input_ids': [...], 'attention_mask': [...]} unknown: &lt;class 'dict'>. 
Should be one of a python, numpy, or pytorch object.
```

根因：`ClassLabelCollator` 在 pop 掉 `class_label` 后把 features 传给 `DataCollatorForSeq2Seq` → `tokenizer.pad()`，而安装的 transformers 版本（v5.x）的 `pad()` 无法正确处理带有 variable-length list 的 feature dict 列表。这是第一次失败（KeyError: 'sample_weight'）的修复代码引入的新 bug — 引入了 `ClassLabelCollator` 包装 `DataCollatorForSeq2Seq`，但两者在这个 transformers 版本下不兼容。

### 修复内容

1. **替换 collator**：删除 `ClassLabelCollator` + `DataCollatorForSeq2Seq` 组合，改为 `WeightedDataCollator` — 手动实现 padding，完全绕过 `tokenizer.pad()`。
2. **删除无用 import**：`DataCollatorForSeq2Seq` 从两个文件中移除。
3. **修复 checkpoint 路径**：`--output_dir` 默认值从 `checkpoints_repo_cls/`（根分区）改为 `/root/autodl-tmp/checkpoints_repo_cls/`（数据盘），CWM 同理。

### 验证结果

两个 dry-run（`--max_steps 3 --no_wandb --batch_size 2`）均成功通过：

| 脚本 | 状态 | 步时 | loss 范围 |
|------|------|------|-----------|
| train_repo_verifier.py | EXIT_CODE=0 | ~7.4s/step | 61–178 |
| train_repo_cwm.py | Dry-run complete | ~10.8s/step | 11–23 |

### 训练命令

**CLS（分类器）— GPU 2：**
```bash
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=2 python train_repo_verifier.py \
  --output_dir /root/autodl-tmp/checkpoints_repo_cls \
  --run_name repo-level-cls-v3 \
  --device cuda:0
```

**CWM（Code World Model）— GPU 3：**
```bash
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=3 python train_repo_cwm.py \
  --output_dir /root/autodl-tmp/checkpoints_repo_cwm \
  --run_name repo-level-cwm-v3 \
  --device cuda:0
```

注意：v2 失败运行显示 0% truncation（70748 samples），说明用了更大的 `max_seq_length`（默认 2048 下有 3.8% truncation）。如果需要复现 v2 参数，需加 `--max_seq_length 4096` 或更高。

### 训练时间估算

以 `max_seq_length=2048, batch_size=2, grad_accumulation=16`（6633 steps × 3 epochs）计算：
- **CLS**: ~7.4s/step → **~13.6 小时**
- **CWM**: ~10.8s/step → **~20 小时**

如果用 `max_seq_length=4096`，时间大约翻倍（~27h / ~40h）。

---
