# code alpha sweep prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpha-sweep-prep_20260514T173608_result.json`
- **Structured JSON:** [`95b5c23dfa4d7c03b2d6.json`](../../sessions/95/95b5c23dfa4d7c03b2d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 代码状态
`mix_datasets` 函数已有正确的 ratio < 1.0 混合逻辑（全量 synthetic + 按比例采样 real，边界值 0/1 退化正确）。缺少 `--accumulate` 累积历史 synthetic 的支持。

### 修改内容（iterative_train.py）
1. 新增 `--accumulate` CLI 参数（`store_true`，默认 False）
2. 主循环中新增 `synthetic_pool` 列表，`--accumulate` 时将每代 synthetic 追加并 concatenate 后传入 `mix_datasets`；默认只用当前代
3. 更新 docstring 和日志输出

### 混合逻辑说明

| synthetic_ratio | --accumulate OFF | --accumulate ON |
|---|---|---|
| 1.0 | 纯当代 synthetic | 纯累积 synthetic pool |
| 0.5 | 50% 当代 syn + 50% real | 50% 累积 pool + 50% real |
| 0.0 | 纯 real baseline | 纯 real baseline |

ratio=1.0 行为完全向后兼容（`--accumulate` 默认 OFF，`synthetic_pool` 不参与）。

### 产出
- `artifacts/iterative_train.py` — 已修改
- `artifacts/test_alpha_sweep.py` — dry-run 测试，9/9 通过

---
