# code fix method ablation spurious

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-method-ablation-spurious_20260514T224631_result.json`
- **Structured JSON:** [`74b9f1fe9aa47edc1b6b.json`](../../sessions/74/74b9f1fe9aa47edc1b6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，运行成功。

## 结果

### 含 TY vs 排除 TY 对比

| | 5-method (含 TY) | 4-method (排除 TY) |
|---|---|---|
| Spurious | 12/16 (75%) | 10/16 (62%) |
| Robust | 4/16 | 6/16 |

### 翻转 pairs（2 个）

| Pair | 5-method | 4-method | 原因 |
|---|---|---|---|
| **ece → distinct_2** | spurious (4/5) | **robust** (4/4) | toda_yamamoto n.s. |
| **ece → distinct_3** | spurious (4/5) | **robust** (4/4) | toda_yamamoto n.s. |

两个翻转 pair 都是 ECE→diversity，4 个非 TY 方法全部一致 SIG（4/4），唯独 TY 判 n.s.。与差分 Granger 验证结果一致（F=71-7643, 全部 4/4 sig）。

### 对 Claim 3 的影响

TY 的纳入/排除翻转了 2/16 pairs（12.5%），恰好是 ECE→distinct_2/3。这提供了两层证据：
1. **方法选择敏感性**：单一低 power 方法（TY at T=10）即可改变 12.5% 的结论
2. **ECE co-primary canary 地位加固**：排除已知 underpowered 的 TY 后，ECE→diversity 全部升级为 robust，与 Granger 因果检验吻合

产出已写入 `results/mvp/analysis/method_ablation.json`，`dual_classification` 段包含完整对比和 flipped_pairs。

---
