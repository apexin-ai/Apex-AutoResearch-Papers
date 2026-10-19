# fix bm25 starcoder model path

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bm25_starcoder_model_path_20260514T180543_result.json`
- **Structured JSON:** [`4d5177e6319144599e19.json`](../../sessions/4d/4d5177e6319144599e19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，汇总：

| 脚本 | 修改前 | 修改后 |
|------|--------|--------|
| `scripts/run_m2_full_bm25_starcoder.sh` (L17) | `/root/autodl-tmp/structfuse/models/bigcode/starcoder2-3b` | `/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b` |

其他脚本状态：
- `run_m2_full_starcoder_resume.sh` — 路径已是正确的 `/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b`，无需修改
- `scripts/run_m2_full_bm25_qwen.sh` — 路径 `/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B`，`config.json` 存在，路径有效

---
