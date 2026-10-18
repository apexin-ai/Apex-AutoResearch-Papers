# ssh westd 70b exp3 fix2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-70b-exp3-fix2_20260517T102550_result.json`
- **Structured JSON:** [`9eba1abcd55cd13fdb07.json`](../../sessions/9e/9eba1abcd55cd13fdb07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Exp 3 已经在正常运行，无需修复。**

状态：
- **脚本**: `scripts/run_d051_count_curves_llama70b.py --dataset fewnerd --seed 42 --model_path /root/autodl-tmp/models/llama-3.1-70b-instruct-fp8`
- **方案**: 已用方案 B（本地模型路径 `/root/autodl-tmp/models/llama-3.1-70b-instruct-fp8`），绕过了 httpx 问题
- **tmux session**: `exp3_70b`，启动于 18:24
- **当前进度**: `count_12_random_1` 已完成（41.3s/1000 samples），正在处理下一个 count 配置
- **推理正常**: vLLM 推理速度 ~25 it/s，无错误
- **httpx 版本**: 0.28.1（未降级，但因直接用本地路径所以不触发远程请求）

不需要任何干预，实验在正常推进中。

---
