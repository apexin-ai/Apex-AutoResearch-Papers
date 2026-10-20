# code gsm8k profiling prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k_profiling_prep_20260515T141031_result.json`
- **Structured JSON:** [`1e32a2bb3b5083e4ffb4.json`](../../sessions/1e/1e32a2bb3b5083e4ffb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**服务器上的文件** (`/root/autodl-tmp/pacs/`):
- `run_profiling_gsm8k.py` — GSM8K profiling 脚本，基于 `run_profiling_qwen.py`，复用相同 II 计算和 phase segmentation
- `data/gsm8k_test.json` — 预下载的 GSM8K test split (1319 题)
- `run_gsm8k_ds_gpu0.sh` — DeepSeek 全部 8 conditions (GPU 0)
- `run_gsm8k_qw_gpu1.sh` — Qwen 全部 8 conditions (GPU 1)

**启动命令**:
```bash
nohup bash run_gsm8k_ds_gpu0.sh > gsm8k_profiling/ds_full.log 2>&1 &
nohup bash run_gsm8k_qw_gpu1.sh > gsm8k_profiling/qw_full.log 2>&1 &
```

**Dry-run 验证通过**: 2 题 × 2048 tokens，phase 检测正常(18/11 phases)，II 计算正确，`per_problem_ii` 格式与 `extract_table2.py` 兼容。

**预估运行时间**: ~5.5 小时 (两个模型并行在 GPU 0/1 上)。

**与 MATH-500 的差异**: 仅数据加载方式不同（随机抽样 vs 分层抽样），prompt 模板、II 公式、phase segmentation、输出格式完全一致。

---
