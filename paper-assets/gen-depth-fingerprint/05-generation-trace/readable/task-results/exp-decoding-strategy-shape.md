# exp decoding strategy shape

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_decoding_strategy_shape_20260521T062400_result.json`
- **Structured JSON:** [`a65dcd401234a73ab523.json`](../../sessions/a6/a65dcd401234a73ab523.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部自动化管线已就绪。当前状态总结：

**正在运行的任务：**
- `cuda:0`: Pythia-2.8B greedy→topk (~9.5h)
- `cuda:1`: OLMo-2-1B greedy→topk (~6h)

**自动后续链：**
- OLMo 完成 → Qwen3-1.7B (cuda:1) → 全部 feature 提取 → 分析
- Pythia 完成 → Pythia feature 提取 (cuda:0)

**Nucleus 基线已计算（对照用）：**

| Model | entropy_min d | entropy_max d | tail_decay d | Silhouette |
|-------|:---:|:---:|:---:|:---:|
| Pythia-2.8B | 0.035 | 0.259 | 0.070 | 0.598 |
| OLMo-2-1B | 0.061 | 0.060 | 0.226 | 0.686 |
| Qwen3-1.7B | 0.052 | 0.020 | 0.092 | 0.672 |

**已上传文件：**
- `/root/gen-depth-fingerprint/generate_chain_decoding.py` — 生成脚本
- `/root/gen-depth-fingerprint/analyze_decoding_strategy.py` — 分析脚本
- `/root/gen-depth-fingerprint/start_qwen_after_olmo.sh` — 自动链
- `appendix_decoding_strategy.tex` — 模板（待填数据）

预计全部完成时间约 11 小时。管线完成后需要：填入 tex 实际数值、写分析文字、保存结果到 artifacts。可以随时 `tail /tmp/gen_pythia.log` 或 `tail /tmp/gen_olmo.log` 查看进度。

---
