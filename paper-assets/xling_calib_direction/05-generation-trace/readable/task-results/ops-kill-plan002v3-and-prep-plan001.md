# ops kill plan002v3 and prep plan001

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_plan002v3_and_prep_plan001_20260521T132712_result.json`
- **Structured JSON:** [`69f1ea2d055f7b14cf2a.json`](../../sessions/69/69f1ea2d055f7b14cf2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型完整，32 个 shard 齐全。汇总：

---

**1. plan_002_v3 状态**: 已 kill（SIGTERM 成功），tmux session 已清理。**4 卡 GPU 全部 clean（0 MiB x 4）**。

**2. Qwen3 模型完整本地路径**:
```
/root/autodl-tmp/models/Qwen3-235B-GPTQ-Int4/
```
32 个 safetensors shard + tokenizer 齐全。

**3. extract_activations_large.py 参数格式**:
```
--model           # HuggingFace model name or local path (required)
--languages       # nargs+, 默认 20 语言
--layers          # 逗号分隔, 默认 "0,4,8,12,16,20,24,28,31"
--output_dir      # 默认 ./activations
--n_shot          # 默认 5
--max_samples     # 0=全部
--dtype           # bfloat16 | float16
--quantization    # none | int4 | int8
--save_interval   # 默认 500
--split_ratio     # 默认 0.0
--split_seed      # 默认 42
--subjects        # 可选，限定 MMLU 科目
```

脚本用 `device_map="auto"`，GPTQ 模型已经是 int4 量化，`--quantization` 参数用于 bitsandbytes 量化——GPTQ 模型应传 `--quantization none`（默认值即可）。

**4. 磁盘**: /root/autodl-tmp/ **99GB 可用**（350G 总量，已用 252G，72%）。

注意：Qwen3-235B-A22B 有 94 层，`--layers` 默认值 `"0,4,8,12,16,20,24,28,31"` 是给 32 层模型的，需要改为适合 94 层的采样（如 `0,8,16,24,32,48,64,80,93`）。

---
