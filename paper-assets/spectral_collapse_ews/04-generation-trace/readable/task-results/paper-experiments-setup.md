# paper experiments setup

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_experiments_setup_20260516T135600_result.json`
- **Structured JSON:** [`8c6b3b3a72a89edefa16.json`](../../sessions/8c/8c6b3b3a72a89edefa16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入成功。更新内容摘要：

**相比原版的主要改动：**

1. **Datasets**：数据来源精确为 `monology/pile-uncopyrighted`；新增 ≥256 token 过滤条件（从 prepare_data.py 提取）
2. **Recursive Training Protocol**：补充 data mixing 公式 `⌊n_syn · r_t/(1-r_t)⌋`；补充 optimizer steps 随 ratio 变化的范围（1562–3125）
3. **Evaluation Metrics**：新增 Log-Determinant Proxy（代码中计算但原 tex 未写）；RankMe 和 ECE 补充公式；每个指标说明为什么选它
4. **Experimental Conditions**：新增 `tabular` 表格（Table 1）；linear-increasing 改用代码中 r_min=0.20, r_max=0.80 + budget-matched formula `(t-1)/(T-1)`；k 和 τ 标注 footnote "Calibrated from Phase~0 pilot"
5. **Statistical Design**：列出 3 seeds (42, 123, 7)；新增 Phase 0 go/no-go 三条件（单调下降 + 加速比 ≥1.5× + ppl 上升>20%）；新增 compute budget（130 generation-steps）

---
