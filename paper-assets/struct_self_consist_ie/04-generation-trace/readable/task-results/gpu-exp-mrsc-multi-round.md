# gpu exp mrsc multi round

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp_mrsc_multi_round_20260520T162935_result.json`
- **Structured JSON:** [`d5937d5759773f9c2309.json`](../../sessions/d5/d5937d5759773f9c2309.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程稳定运行中（3:49，GPU 91%）。

实验状态总结：
- **脚本**: `run_mrsc.py` 已部署并通过 dry run 验证
- **进程**: PID 215236 在 GPU 3 上运行，GPU 利用率 90-100%
- **数据**: 37,648 instances（675MB JSONL），Qwen2.5-7B-FewNERD-merged
- **预计完成**: ~30-45 分钟（数据加载 ~3min + ~50K 验证 forward passes）
- **日志**: `/root/autodl-tmp/struct_self_consist_ie/output/exp_mrsc_multi_round.log`（Python stdout 缓冲，完成后一次性刷新）
- **结果文件**: `output/exp_mrsc_multi_round/mrsc_results.json`

查看进度命令：
```bash
# 进程状态
ps -p 215236 -o pid,etime

# GPU 利用率
nvidia-smi --query-gpu=index,utilization.gpu --format=csv,noheader

# 日志（完成后内容会刷新）
tail -50 /root/autodl-tmp/struct_self_consist_ie/output/exp_mrsc_multi_round.log

# 结果文件
cat /root/autodl-tmp/struct_self_consist_ie/output/exp_mrsc_multi_round/mrsc_results.json
```

Dry run 中 P(yes) 分离度很好（in-gold: 0.99 vs not-in-gold: 0.33），全量结果值得期待。

---
