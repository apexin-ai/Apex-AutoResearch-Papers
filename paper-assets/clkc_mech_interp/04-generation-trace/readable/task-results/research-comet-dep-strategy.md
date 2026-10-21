# research comet dep strategy

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_comet_dep_strategy_20260521T162628_result.json`
- **Structured JSON:** [`a3503d57590f2500bfc7.json`](../../sessions/a3/a3503d57590f2500bfc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。汇总如下：

---

## 调研结果

### 冲突分析

unbabel-comet 2.2.7（最新版）的硬约束：
- `transformers<5.0,>=4.17` → 会把 5.9.0 降到 4.57.6
- `numpy<2.0.0` → 会把 2.3.2 降到 1.26.4
- `huggingface-hub<1.0`

**所有 unbabel-comet 版本（0.0.2 ~ 2.2.7）均不支持 transformers ≥ 5.0。** 方案 4（版本兼容）不可行。

### 各方案评估

| 方案 | 可行性 | 问题 |
|------|--------|------|
| 1. 执行顺序 | **差** | validate_translation.py 同时用 `transformers`（back-translate）和 `comet`（评分），两者必须共存。要拆脚本才行 |
| 2. 独立 conda env | **最佳** | 隔离干净，数据盘 234G 空间充足，脚本无需修改 |
| 3. 轻量替代 | **可用但降级** | sacrebleu（BLEU/chrF）无 ML 依赖但只衡量 n-gram 重合度，不如 COMET 的语义评估；BERTScore 也依赖 transformers |
| 4. 版本兼容 | **不可行** | COMET 全版本锁死 `transformers<5.0` |

### 推荐：方案 2 — 独立 conda env

```bash
# 创建隔离环境（装到数据盘）
conda create -p /root/autodl-tmp/envs/comet_env python=3.12 -y
conda activate /root/autodl-tmp/envs/comet_env

# 安装 COMET（会自带 transformers 4.x + numpy 1.x）
pip install unbabel-comet torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

# 运行验证
python src/validate_translation.py --comet_model Unbabel/wmt22-comet-da ...
```

优势：
- 主环境 transformers 5.9.0 完全不受影响
- validate_translation.py 代码零修改
- back-translate 用的 Qwen3-8B 在 transformers 4.57.6 下也能正常加载
- 一次性搭建，后续可复用

额外开销：约 2-3GB 磁盘（数据盘 234G 足够），搭建时间 5-10 分钟。

需要我现在执行搭建吗？

---
