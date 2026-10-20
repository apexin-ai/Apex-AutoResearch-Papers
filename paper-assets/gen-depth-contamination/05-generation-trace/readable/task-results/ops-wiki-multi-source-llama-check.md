# ops wiki multi source llama check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_wiki_multi_source_llama_check_20260520T113702_result.json`
- **Structured JSON:** [`4077fd8945ea800b5373.json`](../../sessions/40/4077fd8945ea800b5373.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：LLaMA-8B 未缺失，3 个 generator 全部参与了 multi-source 实验

Director 的前提有误。以下是完整证据链：

### 1. 数据完整存在
`/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_llama8b/` 包含 depth 0-5 的 JSONL 文件 + features.csv（30,000 rows, 5,000 docs）。

### 2. 单源实验已完成
Registry 中 `exp_wiki_llama8b` 状态 DONE，K\*=1，1v2 AUC=0.5954。

### 3. Multi-source 脚本确实定义了 3 个 generator
```python
SOURCES = {
    "qwen1b5": {...},
    "llama8b": {...},   # ← 在列表中
    "mistral7b": {...},
}
```

### 4. 日志确认 3 个 generator 全部加载并采样
```
Loaded qwen1b5: 30000 rows, 5000 docs
Loaded llama8b: 30000 rows, 5000 docs
Loaded mistral7b: 30000 rows, 5000 docs
→ 每个采样 1000 docs → 6000 rows，总计 18000 rows
```

llama8b 还经过了完整的 Qwen scorer rescore 流程（313 batches），产出保存在 `features_llama8b_qwen_scorer.csv`。

### 5. results.json 明确记录 3 个 generator
```json
"generators": ["qwen1b5", "llama8b", "mistral7b"]
```

### 6. "metrics 只有 2 个" 的原因
Registry 中没有 `exp_wiki_multi_source` 条目（未注册）。Director 可能看的是 registry 里的**单源实验**（`exp_wiki_llama8b` K\*=1 不如 `exp_023_wiki` 和 `exp_wiki_mistral7b` 显眼），或者误读了某个中间报告。实际 multi-source 结果用了全部 3 个 generator。

### 7. 关于 1v2 AUC 0.579
这是**3 个 generator 混合后**的 unified scorer with\_label 结果，不是 2 个。K\*=1（低于 θ=0.60），与 Wiki 域 single-source 中多数 generator K\*=1 一致（llama8b K\*=1, mistral7b K\*=1, 仅 qwen K\*=2）。混合后被两个 K\*=1 的 generator 拉低是预期行为。

**建议**：将 `exp_wiki_multi_source` 的 results.json 注册到 registry，避免后续再产生混淆。

---
