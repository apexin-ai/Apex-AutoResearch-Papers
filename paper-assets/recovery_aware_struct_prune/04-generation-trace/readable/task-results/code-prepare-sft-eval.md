# code prepare sft eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-sft-eval_20260515T000847_result.json`
- **Structured JSON:** [`4a6f02107a47a62ebbd3.json`](../../sessions/4a/4a6f02107a47a62ebbd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已就绪，语法验证通过。

**修改内容：**

`eval_gsm8k.py` 新增：
- `--temperature` 和 `--do_sample` CLI 参数
- EOS 统计：每条 response 记录 `hit_eos`（最后 token 是否为 EOS）和 `response_length`
- 汇总指标：`natural_eos` / `truncated` 计数、`eos_rate`、平均/最大/最小 response 长度
- 进度日志每 50 条打印一次 acc + eos_rate + avg_len

`run_sft_eval.sh` 执行计划：
- GPU0：`sft_rasp_20` → sampling(temp=0.7) + greedy，共 2 轮
- GPU1：`sft_standard_20` → sampling(temp=0.7) + greedy，共 2 轮
- 两 GPU 并行，4 个 eval JSON 输出到 `/root/autodl-tmp/recovery_aware_struct_prune/eval_results/`
- 结束后自动打印 summary 表：accuracy + eos_rate + avg_len

SFT 完成后运行：
```bash
cd /root/recovery_aware_struct_prune/src && bash run_sft_eval.sh
```

---
