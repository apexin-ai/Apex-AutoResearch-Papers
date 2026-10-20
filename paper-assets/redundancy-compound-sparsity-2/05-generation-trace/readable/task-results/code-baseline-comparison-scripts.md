# code baseline comparison scripts

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline_comparison_scripts_20260512T153722_result.json`
- **Structured JSON:** [`b2831b5570b1437f3e82.json`](../../sessions/b2/b2831b5570b1437f3e82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报结果：

---

### 产出

**`/root/carc/run_baseline_comparison.py`** — dry-run 通过
- 9 种方法：full + 7 个 kvpress baseline (H2O/KnormPress, SnapKV, StreamingLLM, ExpectedAttn, ObservedAttn, TOVA, KeyDiff) + CARC
- kvpress 方法用 sliding-window + press context manager 计算 PPL
- CARC 用 chunk-based 处理 + 每 chunk 后 eviction（key-norm 代理 EMA 分数）
- argparse 完整：`--compression-ratio`, `--seq-len`, `--methods`, `--output`, `--dry-run` 等
- 输出 JSON + 对比表

**`/root/carc/run_rkv_baseline.py`** — dry-run 通过
- 封装 `r_kv_baseline/HuggingFace/run_math.py`，自动处理路径
- 支持 5 种方法：rkv, fullkv, snapkv, streamingllm, h2o
- 支持 3 个数据集：aime24, gsm8k, math（数据已就绪）
- R-KV 使用 monkeypatch 替换 Qwen2 attention，支持 DeepSeek-R1-Distill-Qwen-14B

### 代码可用性

| Baseline | 状态 | 说明 |
|----------|------|------|
| **R-KV** | 可用 | 代码完整，数据就绪，rkv import OK。评估维度是生成质量（数学准确率），不是 PPL |
| **FASA** | 仓库为空 | 只有 README + 方法图，未开源代码。暂不可用作 baseline |
| **kvpress baselines** | 全部可用 | kvpress v0.5.3，7 个 Press 类均通过实例化验证 |

---
