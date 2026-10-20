# diag mvp 001 server check

**verifier tts struct ie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_mvp-001-server-check_20260511T181802_result.json`
- **Structured JSON:** [`7e36edc3cd1804d67fa7.json`](../../sessions/7e/7e36edc3cd1804d67fa7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是完整报告。

---

## MVP 实验报告：StructTTS SciERC NER

### 1. 诊断结果
- **服务器**: seetacloud-bjb2-structtts, 8× RTX 5090 32GB
- **GPU 状态**: 全部空闲 (0 MiB used)，无残留 vLLM 进程
- **脚本**: scripts/ 目录为空 → 全部重新创建 (prepare_data.py, inference.py, aggregate.py)
- **数据**: SciERC 原始数据存在 (processed_data/json/test.json, 100 docs)，shard 文件不存在 → 重新生成
- **修复**: PyTorch torch.compile duplicate template assertion bug → 直接 patch `select_algorithm.py`

### 2. F1 矩阵 (micro-F1 %, 3 seeds 均值 ± std)

| N | greedy | self_consistency | weighted_vote | oracle | random |
|---|--------|-----------------|---------------|--------|--------|
| 1 | **42.05** | — | — | — | — |
| 4 | — | 41.88 ± 0.37 | 41.91 ± 0.37 | **45.92 ± 0.42** | 41.29 ± 0.72 |
| 8 | — | 42.20 ± 0.66 | **42.52 ± 0.32** | **47.45 ± 0.25** | 41.79 ± 0.58 |
| 16 | — | 41.40 ± 0.37 | **42.23 ± 0.38** | **48.54 ± 0.36** | 41.83 ± 0.86 |

### 3. Parse 成功率

| N | 成功/总数 | 成功率 |
|---|----------|--------|
| 1 | 100/100 | 100.0% |
| 4 | 1200/1200 | 100.0% |
| 8 | 2399/2400 | 99.96% |
| 16 | 4800/4800 | 100.0% |

### 4. Pass/Fail 判断

**🔶 Partial**

- **Oracle 显著提升**: oracle@N=16 (48.54) >> N=1 (42.05)，**+6.49 F1 点**，远超 3pt 阈值。Oracle 持续随 N 增长：N=4→45.92, N=8→47.45, N=16→48.54。
- **Self-consistency 未能捕获**: self-consistency 在所有 N 上均未能超过 N=1 (最佳: N=8 42.20 vs N=1 42.05，仅 +0.15)。
- **Weighted vote 微弱正向**: weighted_vote@N=8 (42.52) > N=1 (42.05)，+0.47 F1 点，但未达 ≥1.0 的 pass 阈值。
- **结论**: 多候选生成产生了有价值的多样性 (oracle 持续增长)，但当前的 exact-match self-consistency 选择策略不足以利用这种多样性。需要更好的验证/选择机制——正符合 StructTTS 的核心论点（IoU-based soft matching + structural verification）。

### 5. 结果文件路径
- 最终结果: `/root/projects/verifier-tts-struct-ie/results/final_results.json`
- 推理结果: `/root/projects/verifier-tts-struct-ie/results/test_shard_*_n*.jsonl` (80 files)
- Parse 统计: `/root/projects/verifier-tts-struct-ie/results/parse_stats_*.json` (80 files)
- 运行日志: `/root/projects/verifier-tts-struct-ie/results/run_all.log`

### 6. Parse Stats 汇总
80 个 parse_stats 文件覆盖全部 8 shards × 10 (n,seed) 组合。总计 8500 次 parse 中仅 1 次失败 (N=8)，parse 率 99.99%。Qwen3-8B 在结构化 JSON 输出上表现极佳。

### 关键洞察
Oracle-greedy gap 为 6.49 F1 点 (N=16)，表明模型在不同候选中确实产生了互补的正确实体。Self-consistency 失败的原因可能是 exact string matching——实体文本的微小差异（如 "word embeddings" vs "word embedding"）导致投票分裂。这正是 StructTTS 提出 IoU-based soft matching 的动机：下一步应实现 span-level IoU matching 替代 exact match，预期可显著缩小 oracle-aggregation gap。

---
