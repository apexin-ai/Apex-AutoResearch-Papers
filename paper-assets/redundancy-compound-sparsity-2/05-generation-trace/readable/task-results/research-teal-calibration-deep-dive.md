# research teal calibration deep dive

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_teal_calibration_deep_dive_20260512T081939_result.json`
- **Structured JSON:** [`248592ddbd52234523f3.json`](../../sessions/24/248592ddbd52234523f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

技术笔记已完成并注册。核心发现：

1. **grab_acts.py** 用 Alpaca 300 条数据，逐层收集 `h1`（projection 输入）和 `h2`（projection 中间/输出）的激活分布 histogram（10000 bins），存为 `histograms.pt`

2. **greedyopt.py** 逐层 greedy 搜索 7 个 projection 的最优 sparsity 分配，输出 lookup CSV 表

3. **Threshold 两条路径**：Uniform 只需 histograms（通过 CDF 反函数直接算），Greedy 额外需要 lookup 表但同 sparsity 下 error 更小

4. **Qwen2 适配**工作量不大——projection 命名完全一致（q/k/v/o_proj, gate/up/down_proj），主要修改：新建 `Qwen2SparseForCausalLM` 类、扩展模型白名单、添加 weight_dict 条目、验证 rotary_emb 兼容性

5. **资源预估**：14B 模型 grab_acts 需 ~30GB GPU / 10-20 分钟；greedyopt 需 ~4GB GPU / 1-3 小时；仅 uniform 模式可跳过 greedyopt

---
