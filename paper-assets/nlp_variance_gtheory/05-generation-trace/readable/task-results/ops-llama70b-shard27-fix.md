# ops llama70b shard27 fix

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama70b_shard27_fix_20260523T153243_result.json`
- **Structured JSON:** [`2255bb000c421addf00c.json`](../../sessions/22/2255bb000c421addf00c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 shard 验证通过。以下是完整报告：

---

## Shard 修复报告 — westd-32570

### 1. Shard 27 删除确认
文件在操作前已被删除（`rm` 返回 No such file），确认不存在旧损坏文件。

### 2. 下载 PID / 耗时
- **PID**: 332173
- **总耗时**: ~31 分钟（`Processing 6 items: 30:53`）
- **完成时间**: 2026-05-24 00:04:30
- **额外发现**: Shard 6 (`model-00006-of-00030.safetensors`) 也缺失，modelscope 一并重新下载

### 3. 文件验证（safetensors）
| Shard | 文件大小 | Tensor 数 | 状态 |
|-------|---------|----------|------|
| model-00027-of-00030.safetensors | 4.66 GB | 26 | ✓ PASSED |
| model-00006-of-00030.safetensors | 4.66 GB | 26 | ✓ PASSED |

### 4. 磁盘空间
```
/dev/md0  350G  148G  203G  43%  /root/autodl-tmp
```

### 5. 状态: **READY**

重启 inference 命令（用 `submit_training_job`，非 nohup）：
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/nlp_variance_gtheory && python scripts/exp_llama70b/run_llama70b_inference.py"
```

---
