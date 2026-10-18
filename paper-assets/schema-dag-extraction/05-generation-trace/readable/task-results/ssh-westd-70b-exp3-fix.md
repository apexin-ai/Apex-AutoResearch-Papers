# ssh westd 70b exp3 fix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-70b-exp3-fix_20260517T102041_result.json`
- **Structured JSON:** [`9b22aa2cf5257291aec0.json`](../../sessions/9b/9b22aa2cf5257291aec0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Exp 3 已成功重启并开始推理。

**汇报：**
- **脚本**: `scripts/run_d051_count_curves_llama70b.py --dataset fewnerd --seed 42 --model_path /root/autodl-tmp/models/llama-3.1-70b-instruct-fp8`
- **修复**: 安装了 `datasets` 包 + 补充了 `--model_path` 本地路径（默认值指向 HuggingFace Hub，服务器网络不通）
- **运行状态**: 正在处理 `count_12`（第一个 count），1000 samples，当前推理速度 ~2.16 it/s
- **tmux session**: `exp3_70b`
- **配置**: 6 个 count 点 × 25 batches × 1000 samples = 150 个推理 job
- **预计完成时间**: 按每个 count ~8 分钟估算（1000 prompts / ~2 it/s ≈ 500s），6 个 count × ~8 min ≈ **~50 分钟**（约 19:15 UTC）

---
