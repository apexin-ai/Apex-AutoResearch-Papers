# ops d066 16980 gpu1 check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d066_16980_gpu1_check_20260520T113403_result.json`
- **Structured JSON:** [`8857b47312f4f388ed7c.json`](../../sessions/88/8857b47312f4f388ed7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## d066 Beam Sweep 状态报告

### Llama beam2 unconstrained
- **文件**: `llama_docred_200_beam2_unconstrained.jsonl`
- **行数**: 200 行 ✅ **已完成**（200/200 docs）
- **大小**: 1.77 MB，最后修改 18:40

### Llama beam2 full_s1（GPU1 正在运行）
- **文件**: `llama_docred_200_beam2_full_s1.jsonl`
- **行数**: 99/200，**进行中**
- **进程 PID**: 750806，启动于 19:05，CPU 100%，GPU1 占用 18270 MiB
- 日志显示正常推理中（pad_token_id 设置提示）

### GPU 占用
| GPU | PID | 任务 | 显存 |
|-----|-----|------|------|
| GPU0 | 748197 | qwen beam8 full_s1 | 68134 MiB |
| GPU1 | 750806 | **llama beam2 full_s1** | 18270 MiB |

### 磁盘
`/root/autodl-tmp`: 171G/250G used (69%)，剩余 80G，充足。

### 小结
Llama beam2 unc 已完整输出 200 行。Llama beam2 s1 完成约 50%（99/200），两张 GPU 都在满载运行。

---
