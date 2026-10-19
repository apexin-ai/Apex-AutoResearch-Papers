# code eval repobench

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_repobench_20260514T082145_result.json`
- **Structured JSON:** [`d7df305033cc97df0ad0.json`](../../sessions/d7/d7df305033cc97df0ad0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本确认正确。下面是完整的交付总结。

---

## 交付结果

### 1. RepoBench-R 数据集格式

| 字段 | 类型 | 说明 |
|------|------|------|
| `repo_name` | str | 仓库名 |
| `file_path` | str | 文件路径 |
| `context` | list[str] | 候选代码片段池（闭合检索池） |
| `import_statement` | str | 文件的 import 语句 |
| `code` | str | 待补全的代码上下文 |
| `next_line` | str | 下一行（ground truth） |
| `golden_snippet_index` | int | gold 答案在 context 中的索引 |

**Python 子集统计：**

| Subset | Split | Examples | Pool size |
|--------|-------|----------|-----------|
| python_cff | test_easy | 8,000 | 5-9 (mean 6.6) |
| python_cff | test_hard | 8,000 | 10-60 (mean 17.9) |
| python_cfr | test_easy | 4,000 | 5-9 (mean 6.7) |
| python_cfr | test_hard | 4,000 | 10-60 (mean 17.7) |

数据通过 `huggingface_hub.hf_hub_download` 下载 gzip pickle 文件，绕过 datasets 4.8.4 不兼容 legacy scripts 的问题。

### 2. eval_repobench.py

路径：`/root/structfuse/evaluation/eval_repobench.py`（476 行）

核心逻辑：
- **Query** = `import_statement + "\n" + code`
- **Candidates** = `context` 列表中的每个 snippet
- **Scoring** = bi-encoder 余弦相似度（与 eval_swebench.py 共用 `StructFuseRetriever`）
- **Metrics** = Recall@1/5/10, MRR
- 支持 resume、dry-run（mock 随机分数）、`--limit`

### 3. Dry-run 结果

**test_easy** (10 instances, pool ~6):
```
Recall@1: 0.10, Recall@5: 1.00, Recall@10: 1.00, MRR: 0.36
Chance R@1: 0.17
```

**test_hard** (200 instances, pool ~16):
```
Recall@1: 0.12, Recall@5: 0.42, Recall@10: 0.73, MRR: 0.26
Chance R@1: 0.06
```

随机分数的指标接近 chance level，验证通过。

### 4. 正式 eval 启动命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# python_cff test_easy
python /root/structfuse/evaluation/eval_repobench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \
    --output-dir /root/autodl-tmp/structfuse/eval_results/repobench_qwen_cff_easy \
    --subset python_cff --split test_easy

# python_cff test_hard
python /root/structfuse/evaluation/eval_repobench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \
    --output-dir /root/autodl-tmp/structfuse/eval_results/repobench_qwen_cff_hard \
    --subset python_cff --split test_hard
```

### 5. 预估耗时（单 GPU）

每个 instance 需编码 1 query + ~6-18 candidates。Qwen2.5-Coder-3B 在单 A6000 上约 30-50ms/encode：
- **test_easy** (8000 instances × ~7 candidates): ~30 分钟
- **test_hard** (8000 instances × ~18 candidates): ~60-90 分钟

### 6. 注意事项

- **网络依赖**：首次运行需下载 ~180MB python_cff.gz，必须开启 `network_turbo` 代理。数据下载后会缓存在 `~/.cache/huggingface/hub/`
- **datasets 库不兼容**：`tianyang/repobench-r` 使用 legacy dataset script，datasets>=4.0 无法直接 `load_dataset`，脚本改用 `hf_hub_download` + gzip/pickle 手动解析
- **pool size 差异**：test_easy 的池只有 5-9 个候选，Recall@5 几乎必然为 1.0，主要看 Recall@1 和 MRR；test_hard 池 10-60 个，指标区分度更好

---
