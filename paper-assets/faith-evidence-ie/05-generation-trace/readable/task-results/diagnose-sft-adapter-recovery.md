# diagnose sft adapter recovery

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sft-adapter-recovery_20260520T160314_result.json`
- **Structured JSON:** [`661ea9f3312a22658a98.json`](../../sessions/66/661ea9f3312a22658a98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### rsync 状态
**仍在运行**，3 个 rsync 进程活跃。从 16:31 开始已跑约 7.5 小时，当前进度：

| 时间 | 已传输 | 占比 |
|------|--------|------|
| 16:31 | 14G | 4% |
| 00:01 (最新) | 206G | 59% |

bjb2 源头总量 **208G**，但 westd 已显示 206G——看起来 rsync 快完成 autodl-tmp 的传输了，不过 59% 是占磁盘总容量 350G 的比例，实际数据传输可能接近完成。

### 源头 bjb2-12179：4 个 adapter 目录**完好**

| 目录 | 大小 | 核心文件 |
|------|------|---------|
| sft_output_qwen3_8b_bf16 | 4.6G | adapter_model.safetensors (698MB) + checkpoint-190/570 |
| sft_output_qwen3_8b_s43 | 4.6G | 同上 |
| sft_output_qwen3_8b_s44 | 4.6G | 同上 |
| sft_output_qwen3_8b_no_evidence | 4.6G | 同上 |

### 目标 westd-37389：4 个目录**全空**（0 字节）

目录已创建（rsync 先建目录结构），但文件尚未传输到位。

### 结论

**rsync 还没传到这些目录。** 源头文件完好，无需重训。当前 rsync 已传 206G / 208G，接近完成。

**建议：等 rsync 自然完成。** 按当前速率（约 26G/h），剩余量很小，预计 1-2 小时内完成。完成后检查 4 个目录是否填充即可。如果急需，可以单独 rsync 这 4 个目录优先传输。

---
