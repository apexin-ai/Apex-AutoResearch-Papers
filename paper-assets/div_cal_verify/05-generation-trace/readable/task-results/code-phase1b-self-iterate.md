# code phase1b self iterate

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase1b_self_iterate_20260513T010243_result.json`
- **Structured JSON:** [`1531248117097fb4a77c.json`](../../sessions/15/1531248117097fb4a77c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 修改内容

**run_mvp.py** (8 处修改):

| 行号 | 修改 |
|------|------|
| 8 | 新增 `from contextlib import nullcontext` |
| 56-57 | 添加 `--self_iterate` 参数 |
| 179-180 | `self_iterate` 时 `gen_device = student_device` |
| 193-197 | `self_iterate` 时 `gen_tokenizer = tokenizer`，跳过加载 generator tokenizer |
| 217-220 | `self_iterate` 时 `generator_model = student_model`，跳过加载独立 generator |
| 227 | `all_results` 记录 `self_iterate` 标志 |
| 239-245 | 生成阶段：`self_iterate` 时切 `eval()` + `no_grad()`，生成后切回 `train()` |

**核心机制**：`self_iterate` 模式下 `generator_model` 和 `student_model` 指向同一个 Python 对象。每代训练后 student 权重原地更新，下一代生成自动使用退化后的模型，形成经典 model collapse 的 feedback loop。

## 验证结果
- 语法检查：`SYNTAX OK`
- `--help` 输出：`--self_iterate` 参数正确显示

## run_phase1b.sh
路径：`/root/div_cal_verify/run_phase1b.sh`

注意事项（相对任务描述的调整）：
- 参数名使用实际代码中的 `--train_lr`/`--train_batch_size`/`--train_grad_accum`（非 `--lr`/`--batch_size`/`--grad_accum`）
- 添加了 `--gpu_ids 0`（因 `CUDA_VISIBLE_DEVICES` 重映射后只有 device 0 可见）
- 添加了 conda activate

## 启动命令
```bash
bash /root/div_cal_verify/run_phase1b.sh 1
```
或用于 submit_training_job：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && bash /root/div_cal_verify/run_phase1b.sh 1
```

---
