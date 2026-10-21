# code exp006 strip chain fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp006-strip-chain-fix_20260515T012404_result.json`
- **Structured JSON:** [`d698761065d06abdba9e.json`](../../sessions/d6/d698761065d06abdba9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修复总结

### 修改了两个文件

**1. `run_irt_calibration.py` 第 43 行** — 目录名解析正则（根本原因）
```python
# 修复前
DOSAGE_PATTERN = re.compile(r"_d(\d+)_s(\d+)(_para)?(_aligned)?$")

# 修复后
DOSAGE_PATTERN = re.compile(r"_d(\d+)(?:_v\d+)?_s(\d+)(_para)?(_aligned)?(?:_v\d+)?$")
```
支持目录名中 dosage 后和末尾两个位置的版本号后缀。

**2. `run_exp006.py` 第 119、161 行** — signal 目录匹配 strip 链
```python
# 修复前
sig_dirname = m["dirname"].replace("_para_aligned", "").replace("_aligned", "").replace("_para", "")

# 修复后（两处）
sig_dirname = m["dirname"].replace("_para_aligned", "").replace("_aligned", "").replace("_para", "").replace("_v1", "").replace("_v2", "").replace("_v3", "").replace("_v4", "")
```

### dry-run 结果

| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| 加载模型数 | 18 | **19** (≥16 ✓) |
| 新增 | — | `Qwen2.5-3B_d000_v2_s42_aligned` |

### 仍 skip 的目录（非代码问题）

| 目录 | 原因 |
|------|------|
| `*_DEPRECATED` (3个) | 末尾 `_DEPRECATED` 不匹配正则（预期行为） |
| `*_raw` (2个) | 无 `_d{dosage}_s{seed}` 模式 |
| `Qwen2.5-3B_d100_v2_s42_aligned` | 目录为空，无 `eval_results.json` |
| `*_para_aligned` 系列 | `skip_para=True` 默认过滤（预期行为） |

---
