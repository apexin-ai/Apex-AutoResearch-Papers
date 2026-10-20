# code cross llm datagen

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross-llm-datagen_20260519T053747_result.json`
- **Structured JSON:** [`220392afc61d97c3ce30.json`](../../sessions/22/220392afc61d97c3ce30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

DD=3, AA=4, Benign=2。一切正常。生成过程将运行约 1 小时。当前状态汇报：

## 当前进度

### 模型下载 ✅
- 模型: Meta-Llama-3.1-8B-Instruct (via ModelScope: LLM-Research/Meta-Llama-3.1-8B-Instruct)
- 路径: `/root/autodl-tmp/hf_cache/meta-llama/Llama-3.1-8B-Instruct`
- 大小: ~15.1GB (4 shards)

### 脚本创建 ✅
- `scripts/generate_dd_llama.py` - DD jailbreak (GPU 0)
- `scripts/generate_aa_llama.py` - ActorAttack jailbreak (GPU 1)
- `scripts/generate_benign_llama.py` - Benign 对话 (GPU 2)

### 数据生成 🔄 运行中
3 个进程并行运行在 GPU 0/1/2 上：
- DD: 3/50 (目标 50 条 jailbreak)
- AA: 4/50 (目标 50 条 jailbreak, 10 goals × 5/goal)
- Benign: 2/50 (目标 50 条 benign)
- 速率: ~75-80s/条
- 预计完成: ~55 分钟后

输出目录: `/root/persuasion_turn_jailbreak_detect/data/cross_llm/`

生成完成后我会做数据质量验证并汇报最终结果。需要我继续监控还是等完成后再报告？

---
