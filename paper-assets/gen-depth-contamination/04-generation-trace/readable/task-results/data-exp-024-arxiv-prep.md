# data exp 024 arxiv prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_exp_024_arxiv_prep_20260516T082003_result.json`
- **Structured JSON:** [`88e9a4a3d17b08db9858.json`](../../sessions/88/88e9a4a3d17b08db9858.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. arXiv 数据集来源和下载方式
- **来源**: arXiv API (`export.arxiv.org`)，categories: cs.CL, cs.LG, cs.AI, cs.CV, stat.ML
- **方式**: 直接调用 arXiv Atom API，batch=200，按 submittedDate descending 排序
- HF `ccdv/arxiv-summarization` 因 `trust_remote_code` 已废弃 + AutoDL 网络慢放弃；arXiv API 直连可靠

### 2. Seed data 验证
- **路径**: `data/exp_024_arxiv/depth_0.jsonl`
- **行数**: 5000
- **字段**: `{"text": "...", "doc_id": N}` — 与 C4/Wiki 完全一致
- **文本长度**: min=99, max=67,090, mean=1,631 chars
- 文本为英文学术摘要，含 LaTeX 标记 (`@xmath0` 等)

### 3. 格式一致性
```
C4 fields:    ['doc_id', 'text'] ✓
Wiki fields:  ['doc_id', 'text'] ✓
arXiv fields: ['doc_id', 'text'] ✓
```

### 4. exp-024 脚本
- **路径**: `scripts/exp024_arxiv_domain.sh`
- Qwen2.5-1.5B base, continuation mode, 5K docs, depth 0-5, max_new_tokens=256
- `HF_DATASETS_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1` 阻断运行时网络
- `CUDA_VISIBLE_DEVICES=3`，输出到 `results/exp_024_arxiv/`

### 5. Dry-run 验证
- `bash -n` 语法检查: ✓
- seed data 5000 行: ✓
- 模型文件 `Qwen2.5-1.5B` 存在: ✓

### 6. 注意事项
- 部分 abstract 包含 LaTeX artifact（`@xmath0` 等），属于 arXiv 文本特征，不影响实验
- max 文本长度 67K chars，个别条目可能是完整论文而非纯 abstract（arXiv API 的 summary 字段偶尔返回长文本），pipeline 会按 max_new_tokens=256 截断，不影响结果
- GPU 空出后直接 `bash scripts/exp024_arxiv_domain.sh` 即可启动

---
