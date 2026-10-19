# ops verify plan001 now

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_plan001_now_20260521T134839_result.json`
- **Structured JSON:** [`e2b34c57ba3126fe509b.json`](../../sessions/e2/e2b34c57ba3126fe509b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan_001 状态报告

**状态：ALIVE — 模型权重加载完成，等待推理启动**

### GPU 占用
| GPU | 显存占用 | 总显存 | 占用率 |
|-----|---------|--------|--------|
| GPU 0 | 90.2 GiB | 95.6 GiB | 92% |
| GPU 1 | 91.4 GiB | 95.6 GiB | 96% |
| GPU 2 | 91.4 GiB | 95.6 GiB | 96% |
| GPU 3 | 91.4 GiB | 95.6 GiB | 96% |

4 卡均被 PID 299318 占用，GPU-Util 0%（模型刚加载完，尚未开始计算）。

### 进程
- **PID 299318 存活**，命令：`python -u code/extract_activations_large.py --model /root/autodl-tmp/models/Qwen3-235B-GPTQ-Int4/ --languages en zh ar hi sw ko de fr ja pt ru vi th bn te ur ta gu mr kn --layers 0,4,8,...,93 --output_dir /root/autodl-tmp/activations/qwen3_235b --dtype bfloat16 --max_samples 0 --quantization none --split_ratio 0.7 --split_seed 42`

### 日志最新状态
- 模型加载路径：`/root/autodl-tmp/models/Qwen3-235B-GPTQ-Int4/`
- 量化内核：**MarlinLinear**（GPTQ-Int4 高效推理内核）
- 权重加载：**100% 完成**（1977/1977 shards，耗时约 2 秒）
- 无报错。日志停在权重加载完成处，下一步应开始逐语言提取 activations。

### 注意
- 有一条 warning：`torch_dtype is deprecated, use dtype instead` — 无影响
- `cpp extensions` 跳过警告（torch 2.8 < 2.11 要求）— 不影响 GPTQ 推理，MarlinLinear 已正常选中
- `not a git repository` warning — 无影响

---
