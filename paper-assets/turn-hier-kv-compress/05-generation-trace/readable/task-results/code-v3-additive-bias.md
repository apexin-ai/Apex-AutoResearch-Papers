# code v3 additive bias

**turn hier kv compress** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v3_additive_bias_20260513T154442_result.json`
- **Structured JSON:** [`ebb0107a4824ca253ab4.json`](../../sessions/eb/ebb0107a4824ca253ab4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 实施报告

### 修改文件

| 文件 | 变更 |
|------|------|
| `src/turnkv/eass.py` | 追加 `compute_structural_offset()` 和 `apply_additive_bias()` |
| `src/turnkv/press.py` | 重写：新增 `alpha`, `mode` 参数，三模式分发 |
| `src/turnkv/__init__.py` | 导出新函数 |
| `eval/evaluate.py` | 新增 `--alpha`, `--methods` 参数，支持三方对比 |
| `eval/config.py` | 新增 `alpha: float = 0.3` |
| `eval/metrics.py` | summary 增加 `pure_structural` 方法和 `structural_vs_ea` 对比 |

原文件均已备份为 `*_v2_backup.py`。

### 加法偏置实现细节

**公式**: `final_score = ea_score + α × normalized_offset`

**structural_offset 计算**:
1. 每个 segment 用 `_B_PRIOR` 表查 raw importance（SYSTEM_PROMPT=1.0, USER/ASSISTANT=0.6, THINKING_TRACE_older=0.15 等）
2. Token-weighted 零均值化 → offset 范围约 [-0.05, +0.35]（取决于 segment 分布）
3. Std-match 归一化：offset 的 std 对齐到 EA scores 的 std，使 α 成为直接的相对影响力控制

**α 含义**: α=0 纯 EA, α=0.3（默认）structural 贡献约 EA 的 30%, α=1.0 等权

### 三种评估模式调用

```bash
# 三方全对比（默认）
python eval/evaluate.py --alpha 0.3

# 只跑 uniform_ea 和 turnkv
python eval/evaluate.py --methods uniform_ea turnkv --alpha 0.3

# 扫描 α
python eval/evaluate.py --alpha 0.1
python eval/evaluate.py --alpha 0.3
python eval/evaluate.py --alpha 0.5

# 只跑 pure_structural 看结构信息单独效果
python eval/evaluate.py --methods pure_structural
```

### α 建议范围

从 0.1 开始扫到 0.5，步长 0.1。默认 0.3 是保守起点。

---
