# infra deberta data audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_deberta-data-audit_20260519T192508_result.json`
- **Structured JSON:** [`afd1152afb5a16ab4377.json`](../../sessions/af/afd1152afb5a16ab4377.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果明确：

### 1. 已完成的 2 个实验
- **wiki_pythia** (结果已保存 wiki_pythia.json)
- **wiki_olmo** (结果已保存 wiki_olmo.json)

### 2. 全部 5 个实验 config
脚本 `EXPERIMENTS` 字典定义了：
1. `wiki_pythia` → `data/exp_wiki_pythia` ✅ 已完成
2. `wiki_olmo` → `data/exp_wiki_olmo` ✅ 已完成
3. `wiki_qwen7b` → `data/exp_wiki_qwen7b` ← 当前正在运行（日志第 520 行）
4. `wiki_llama8b` → `data/exp_wiki_llama8b`
5. `wiki_mistral7b` → `data/exp_wiki_mistral7b`

### 3. 是否包含 C4 数据？
**否。全部 5 个实验都是 Wiki 域。** 脚本中没有任何 C4 相关配置。

### 4. cqa1 上有哪些 C4 数据？
**没有 C4 数据目录。** `data/` 下只有 wiki、arXiv、code 三类域的数据，无任何 `c4` 或 `qwen_rewrite` 目录。

### 5. 数据路径配置
```python
DATA_DIR = ROOT / "data"
EXPERIMENTS = {
    "wiki_pythia":    DATA_DIR / "exp_wiki_pythia",
    "wiki_olmo":      DATA_DIR / "exp_wiki_olmo",
    "wiki_qwen7b":    DATA_DIR / "exp_wiki_qwen7b",
    "wiki_llama8b":   DATA_DIR / "exp_wiki_llama8b",
    "wiki_mistral7b": DATA_DIR / "exp_wiki_mistral7b",
}
```

**结论：确认训练确实只用了 Wiki 数据，不包含 C4。如果需要 C4 域的 DeBERTa upper-bound，需要另起实验。**

---
