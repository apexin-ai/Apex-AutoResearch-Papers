# diagnose scale 14b mauve none

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scale_14b_mauve_none_20260522T083239_result.json`
- **Structured JSON:** [`2a2c8ed3057e7845a3b5.json`](../../sessions/2a/2a2c8ed3057e7845a3b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因

**双层故障：**

1. **环境问题（主因）**：1.4B 实验的启动命令未设置 `HF_HOME=/root/autodl-tmp/.hf_cache`。MAUVE 库需要 GPT-2-large 作为 featurizer，模型已缓存在 `/root/autodl-tmp/.hf_cache/` 但 MAUVE 在默认的 `~/.cache/huggingface/`（空目录）找不到，又无法连接 huggingface.co 下载。对比：成功的 410M 实验启动时设置了 `HF_HOME` + `TRANSFORMERS_OFFLINE=1`。

2. **代码 bug（次因）**：`metrics.py:343` 在 MAUVE 失败时设 `results["mauve"] = None`（其他指标用 `float("nan")`），`iterative_train.py:358` 对 None 执行 `:.4f` 格式化导致 TypeError。

### 崩溃位置

两个实验都在 **Gen 1** 完成训练、保存 checkpoint 后，计算 metrics 阶段崩溃。

### Checkpoint 状况

| 实验 | gen_0 | gen_1 checkpoint | gen_1 metrics |
|---|---|---|---|
| t10_a060_s42_fp32_14b | metrics + synthetic_data | 5.3G (完整) | mauve=null，其余正常 |
| t10_a075_s42_fp32_14b | metrics + synthetic_data | 5.3G (完整) | mauve=null，其余正常 |

### 代码修复

- `metrics.py:343`: `None` → `float("nan")`
- `iterative_train.py:358`: `metrics['mauve']` → `metrics.get('mauve', float('nan'))`
- 已修复：westd-17855、westd-19828、本地 artifacts/

### 恢复方式

可用 `--start_gen 2` 从断点恢复，启动命令必须加：
```bash
export HF_HOME=/root/autodl-tmp/.hf_cache
export TRANSFORMERS_OFFLINE=1
export HF_HUB_OFFLINE=1
```

诊断报告已写入 `artifacts/scale_14b_mauve_bug_diagnosis.md`。

---
