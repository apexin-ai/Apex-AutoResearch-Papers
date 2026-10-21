# prepare full eval d008

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prepare_full_eval_d008_20260514T184132_result.json`
- **Structured JSON:** [`aacccd34a23c311ea363.json`](../../sessions/aa/aacccd34a23c311ea363.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### 产出

**脚本已创建并部署到服务器：**
- `src/run_full_eval_d008.sh` — 串行版，单 GPU，~8h
- `src/run_full_eval_d008_parallel.sh` — 并行版，双 GPU，~4h

**`--max_samples` 行为：** 默认 `None`，不传该参数即使用全部 1319 samples。不需要改 eval_gsm8k.py。

**GSM8K test set：** 确认 1319 samples，本地已缓存。

**耗时估算：** N=100 约 7-15 min → N=1319 约 **90-200 min（~2h）per eval**。串行 4 个 ~8h，并行版 ~4h。

**GRPO 完成后执行命令：**
```bash
# 推荐：并行版（两个 GPU 都空闲时）
nohup bash src/run_full_eval_d008_parallel.sh > results/eval_d008.log 2>&1 &

# 或串行版（只用一个 GPU）
nohup bash src/run_full_eval_d008.sh 0 > results/eval_d008.log 2>&1 &
```

**checkpoint 自动选择：** recovered 目录若有 `checkpoint-*` 子目录，自动选编号最大的；若没有则直接用目录本身。

---
