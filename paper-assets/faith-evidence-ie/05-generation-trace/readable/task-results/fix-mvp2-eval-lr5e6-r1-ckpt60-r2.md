# fix mvp2 eval lr5e6 r1 ckpt60 r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mvp2_eval_lr5e6_r1_ckpt60_r2_20260514T222815_result.json`
- **Structured JSON:** [`9860a18cea70781de90d.json`](../../sessions/98/9860a18cea70781de90d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 检查项 | 结果 |
|--------|------|
| checkpoint-60 | ✅ 存在，adapter_model.safetensors 252MB |
| cuda:1 | ✅ 空闲，0MiB / 32607MiB，无进程 |
| 语法检查 | ✅ `bash -n` 通过 |

**脚本路径**: `/root/autodl-tmp/scripts/eval_lr5e6_ckpt60.sh`

相比模板的改动：
- `--checkpoints 20` → `60`
- `--output_dir` → `/root/autodl-tmp/eval_results/lr5e6_r1_ckpt60`
- 新增 `export PYTHONUNBUFFERED=1`
- `cd /root/autodl-tmp` 保持不变（修复原来 cd 到 freige 内部的问题）

可以提交运行了。

---
