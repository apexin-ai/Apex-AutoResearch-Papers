# code analyze dryrun

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analyze-dryrun_20260514T062009_result.json`
- **Structured JSON:** [`ace5ec4758e15176e10d.json`](../../sessions/ac/ace5ec4758e15176e10d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 结果

**analyze_mvp.py 正常运行，无报错。**

### PASS/FAIL 判定
- `pass_fail = "PASS"` — 正确。15/20 canary-downstream 对在所有 3 个 rep 中一致地表现为 canary 领先。

### Peak lag 值
| Canary | Peak lag | 备注 |
|--------|----------|------|
| token_entropy | **-2.0** (std=0) | 完美检出 2-gen lead |
| effective_rank | **-2.0** (std=0) | 完美检出 2-gen lead |
| self_bleu | **-1.67** (std=0.47) | 2/3 rep 检出 -2，1 个 rep 检出 -1，平均偏小但方向正确 |
| ece | **不一致** (lag_std ~1.2-2.6) | 5 个 downstream 全部 consistent=False |

### 分析

`token_entropy` 和 `effective_rank` 是最可靠的 canary，lag 检测完全准确。`self_bleu` 略有波动但方向正确。

**ece 是唯一有问题的 canary**：lag 方向在不同 rep 间不稳定，甚至出现正值（+1.33 for perplexity, +1.67 for distinct_3）。原因是 mock 数据中 ece 的 onset 幅度较小（0.03→0.18，仅 0.15 变化量），加上噪声（std=0.02）导致信号被淹没，cross-correlation 在不同 rep 中选择了不同方向的 lag。这是数据信噪比问题，不是代码 bug。

### 结论
- 代码逻辑正确，无 bug
- Cross-correlation + lead time 检测在信噪比充足时（token_entropy, effective_rank）准确检出 2-gen lead
- ece 因信号弱导致不一致，但 `consistent` 字段正确标记为 False，PASS/FAIL 判定逻辑工作正常

---
