# code fix sft oom

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-sft-oom_20260514T082310_result.json`
- **Structured JSON:** [`118673811110202e9e15.json`](../../sessions/11/118673811110202e9e15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果汇报：**

**1. 配置文件修改（sft_taxei.yaml + sft_vanilla.yaml 均已完成）：**

| 参数 | 修改前 | 修改后 |
|------|--------|--------|
| `per_device_train_batch_size` | 2 | 1 |
| `gradient_accumulation_steps` | 8 | 16 |
| `gradient_checkpointing` | (无) | true |
| `max_length` | 4096 | 4096（未变） |

有效 batch size 保持不变：1×16 = 2×8 = 16。

**2. OOM 验证通过。** 用 `sft_dryrun_vanilla.jsonl`（123 条，token 长度 345–4022）在 cuda:0 完成 3 步训练，无 OOM。

**3. 峰值显存：22.46 GiB / 32 GB**，剩余约 10 GB headroom。

**注意：** ms-swift 4.2.0 不支持 `--config &lt;yaml>` 参数。正式训练时需用命令行参数传入，或改用 ms-swift 的其他配置加载方式。YAML 文件可作为参数记录/文档使用。

---
