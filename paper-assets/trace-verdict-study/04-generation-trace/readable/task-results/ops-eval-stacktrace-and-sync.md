# ops eval stacktrace and sync

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_stacktrace_and_sync_20260522T120506_result.json`
- **Structured JSON:** [`6e3410bb5f2f59e4d863.json`](../../sessions/6e/6e3410bb5f2f59e4d863.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

appendix.tex 修复完成：49,590 bytes / 795 lines，与本地一致。

---

### 报告

**1. exc_stacktrace_only 准确率**

| 指标 | 值 |
|------|-----|
| **Accuracy** | **99.83%** (1188/1190) |
| Pass Precision / Recall / F1 | 1.000 / 0.998 / 0.999 |
| Fail Precision / Recall / F1 | 0.994 / 1.000 / 0.997 |
| 95% CI | [99.58%, 100%] |
| Majority baseline | 71.5% |

结论：exc_stacktrace_only 达到 99.83%，与 exception_only (99.83%) 完全持平，远超 full_trace (~82%)。Stacktrace 单独即可承载几乎全部诊断信号。Registry 已更新为 DONE/success。

**2. Paper sync 验证**

11 个文件全部同步到 `/root/trace-verdict-study/docs/paper/`：

| 文件 | 大小 | 状态 |
|------|------|------|
| conclusion.tex | 571B | ✓ |
| related_work.tex | 2,964B | ✓ |
| discussion.tex | 3,484B | ✓ |
| main.tex | 4,152B | ✓ |
| introduction.tex | 4,891B | ✓ |
| method.tex | 5,083B | ✓ |
| arr_checklist.tex | 5,940B | ✓ |
| acl.sty | 11,615B | ✓ |
| references.bib | 17,755B | ✓ |
| experiments.tex | 19,294B | ✓ |
| appendix.tex | 49,590B | ✓ (已修复双写重复) |

**3. gradient_masking_seed123 命令确认**

`train_sft.py` 已支持 `--gradient_mask_ratio` 参数（line 138）。命令就绪：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/trace-verdict-study && \
/root/miniconda3/bin/python train/train_sft.py \
  --condition exception_only \
  --gpu 0 \
  --gradient_mask_ratio 0.998 \
  --gradient_checkpointing \
  --seed 123 \
  --wandb_project trace-verdict-study \
  --wandb_run_name gradient_masking_qwen7b_seed123 \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed123 \
  2>&1 | tee /root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed123.log
```

等 cuda:1 上的 exc_message_only 训练结束释放显存后，cuda:0 可直接启动（当前 cuda:0 空闲）。也可以现在就在 cuda:0 上启动，两个训练互不冲突。

---
