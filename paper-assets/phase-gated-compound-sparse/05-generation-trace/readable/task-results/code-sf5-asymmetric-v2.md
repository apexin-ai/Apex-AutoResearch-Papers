# code sf5 asymmetric v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sf5_asymmetric_v2_20260515T110100_result.json`
- **Structured JSON:** [`518acb7b3fcc9cc13bff.json`](../../sessions/51/518acb7b3fcc9cc13bff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 全部被占用：

| GPU | PID | 进程 | 显存 |
|-----|-----|------|------|
| 0 | 218877 | `segment_sensitivity_v2.py --model deepseek` | 15.0 GB / 98 GB |
| 1 | 220988 | `mpl_sensitivity.py --model deepseek` | 15.0 GB / 98 GB |
| 2 | 219130 | `segment_sensitivity_v2.py --model qwen` | 15.0 GB / 98 GB |
| 3 | 221265 | `mpl_sensitivity.py --model qwen` | 15.0 GB / 98 GB |

每张卡都只用了 ~15GB，还剩 ~83GB 空闲。7B 模型 fp16 约需 14GB，理论上可以共享。

**代码改动已完成**（`/root/autodl-tmp/pacs/pacs/profiling/run_profiling.py`），共增加 ~15 行：
- 新增 `--head_sparsity` / `--kv_sparsity` 两个可选参数
- 必须成对使用，否则报错
- 指定时覆盖 `--sparsity_levels`，head mask 和 KV mask 分别使用不同稀疏率
- 不指定时行为完全不变

**实验无法启动**：4 张 GPU 都在跑其他实验（segment_sensitivity_v2 和 mpl_sensitivity），按规范不强制启动。

是否要在当前某张卡上共享运行（显存充足），还是等现有实验跑完？

---
