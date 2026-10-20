# exp c2 qw n500 setup

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_c2-qw-n500-setup_20260514T134630_result.json`
- **Structured JSON:** [`0bb1a98a69a50d48895d.json`](../../sessions/0b/0bb1a98a69a50d48895d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动：

- **cuda:2**: 14049 MiB — Qwen importance (s015→s020→s025→s030) 正在运行
- **cuda:3**: 14049 MiB — Qwen random (s015→s020→s025→s030) 正在运行
- **cuda:0/1**: DeepSeek 实验不受影响

**配置总结**：
| GPU | Screen Session | Conditions |
|-----|---------------|------------|
| cuda:2 | `c2_qw_gpu2` | imp_s015, imp_s020, imp_s025, imp_s030 |
| cuda:3 | `c2_qw_gpu3` | rand_s015, rand_s020, rand_s025, rand_s030 |

- 模型: Qwen2.5-7B-Instruct, bfloat16, seed=42
- 数据: math500.json (500 problems)
- Registry: `c2_qw_n500` → RUNNING
- 日志: `/root/autodl-tmp/pacs/logs/n500_qw_{imp,rand}_s0{15,20,25,30}.log`
- 输出: `/root/autodl-tmp/pacs/profiling_output_n500_bf16_qw_{imp,rand}_s0{15,20,25,30}/`

---
