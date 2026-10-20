# debug scale 14b mauve none

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_scale_14b_mauve_none_20260522T083259_result.json`
- **Structured JSON:** [`de68abc952d27f53a2e2.json`](../../sessions/de/de68abc952d27f53a2e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

19828 离线模式加载成功。

---

## 诊断与修复完成

### 根因
**MAUVE 库需要 `gpt2-large` 作为 featurizer，但两台 AutoDL 服务器无法连接 HuggingFace，且本地无缓存。** `compute_mauve()` 抛异常 → `compute_all_metrics()` 捕获后设 `metrics["mauve"] = None` → `iterative_train.py` 的 `f"mauve={metrics['mauve']:.4f}"` 对 None 调用 `:.4f` 格式化导致 TypeError。

410M 实验不受影响是因为它们之前跑的时候 gpt2-large 已经在缓存中（或者环境不同）。

### 已执行的修复

| 修复项 | westd-17855 | westd-19828 |
|--------|-------------|-------------|
| `metrics.py`: mauve 失败改为 `float("nan")` | 已是（之前修过） | 已是（之前修过） |
| `iterative_train.py`: None 防御 | `.get('mauve', float('nan'))` (之前修过，但有 bug — get 在 key 存在时不用 default；配合 metrics.py 改 nan 后可工作) | 新增 `_mauve_s` None 检查 |
| 下载 gpt2-large 到 HF 缓存 | ✅ | ✅ |
| 创建 `HF_HUB_CACHE` 路径 symlink | ✅ | ✅ |
| 验证离线加载 | ✅ | ✅ |

### 代码 diff

**iterative_train.py (19828)** — line 357-361:
```diff
-              f"mauve={metrics['mauve']:.4f}")
+        _mauve_s = f"{metrics['mauve']:.4f}" if metrics.get('mauve') is not None else 'N/A'
+              f"mauve={_mauve_s}")
```

**metrics.py (两台)** — 无需改动，已使用 `float("nan")`。

**文件系统**:
```
ln -s .hf_cache/hub/models--gpt2-large → .hf_cache/models--gpt2-large
```

### 运行中实验风险评估

| 实验 | 服务器 | 状态 | 风险 |
|------|--------|------|------|
| `t15_a060_s42_fp32_14b` | 17855 | gen 1 训练中 | **低** — 内存中有防御代码 + gpt2-large 已缓存，gen 1+ MAUVE 应正常计算 |
| `t15_a050_s42_fp32_14b` | 17855 | gen 1 训练中 | **低** — 同上 |
| `t10_a050_s42_fp32_19828` | 19828 | gen 1 训练中 (~30%) | **中** — 内存中是旧代码（mauve=None 会 crash）。但 gpt2-large 现已缓存，如果 MAUVE 计算成功则不 crash。如果 tokenizer 加载时 hang（无 TRANSFORMERS_OFFLINE），可能卡住 |

### 需要重启的实验
- `scale_14b_t10_a075_s42_fp32` (17855) — gen 1 crash，checkpoint 已保存，可 `--start_gen 2`
- `scale_14b_t10_a060_s42_fp32` (17855) — 同上

---
