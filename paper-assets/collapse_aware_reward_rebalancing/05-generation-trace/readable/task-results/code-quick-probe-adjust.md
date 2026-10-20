# code quick probe adjust

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_quick-probe-adjust_20260516T074701_result.json`
- **Structured JSON:** [`440561a106acb1c33caf.json`](../../sessions/44/440561a106acb1c33caf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。修改摘要：

| 文件 | 变更 |
|------|------|
| `config.py` | `BASE_MODEL` → `/root/autodl-tmp/models/Qwen/Qwen3-0___6B`（权重下载中，目录已建立） |
| `evaluate.py` | 新增 `compute_mean_nn_distance()` 函数，`evaluate()` 返回值多了 `mean_nn_distance` 字段 |
| `run_quick_probe.py` | 新建，single_reward × 3 代，输出 JSON 到 `outputs/quick_probe_results.json`，结尾分析 Vendi Score 下降百分比 |
| `pipeline.py` | 添加 VRAM 优化 TODO 注释（当前保持分时加载策略不变）；metrics 打印新增 `nn_dist` |

---
