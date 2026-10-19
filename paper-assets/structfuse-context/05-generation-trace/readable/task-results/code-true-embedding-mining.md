# code true embedding mining

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_true-embedding-mining_20260513T041546_result.json`
- **Structured JSON:** [`be719cbc4d152b557693.json`](../../sessions/be/be719cbc4d152b557693.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实现完成。总结：

### 修改内容

**文件**: `/root/structfuse/scripts/build_m1_training_data.py` (432 → 518 行, +86 行)

**核心变更**:
1. **新增 `EmbeddingMiner` 类** (line 119): 使用 Qwen2.5-Coder-3B 的 encoder 做 mean pooling + L2 normalize，批量编码文件，计算 cosine similarity
2. **修改 `build_candidate_pools` 签名**: 新增 `embedding_scores` 参数，"embedding" 策略用真正 cosine similarity 排序，"dataflow" 策略继续用 BM25
3. **新增 `--model-path` 参数**: 指定模型路径启用真正 embedding mining，不指定则回退到 BM25
4. **Repo 级 embedding 缓存**: 每个 repo 的所有文件只编码一次，跨 instance 复用

### 性能数据
- 模型加载: **3.2s** (Qwen2.5-Coder-3B, fp16, GPU 1)
- 8 文件编码: **0.4s** (首次), **0.0s** (缓存后)

### Smoke Test 结果
- 三个策略 MD5 全部不同: random(`984d`), embedding(`9c7a`), dataflow(`6366`)
- Strategy divergence: 100% — embedding vs dataflow 池完全不同
- BM25 回退模式正常，dynamic mode 不受影响

### 设计决策
- BM25 保留给 "dataflow" 策略（结构断连 + 文本相似性选 hard negatives）
- "embedding" 策略用模型 cosine similarity（论文 Claim 2 的实验依据）
- 不提供 `--model-path` 时两个策略都退化为 BM25（向后兼容）

### 注意事项
- bjb1 上无 M1 extraction 原始数据，smoke test 用合成数据。正式运行需先将 cqa1 上的 M1 数据 scp 过来，或直接在 cqa1 上执行

---
