# infra m1 script review

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_m1_script_review_20260512T151301_result.json`
- **Structured JSON:** [`e5b91d45176759c8c31d.json`](../../sessions/e5/e5b91d45176759c8c31d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已收集完毕。以下是审查报告。

---

## 审查报告：run_m1_extraction.sh

### 脚本当前内容

```bash
#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/structfuse

OUTPUT_DIR="/root/autodl-tmp/structfuse/m1_extraction"
mkdir -p "$OUTPUT_DIR"

python extraction/batch_extract.py \
  --metadata /root/autodl-tmp/swe_smith_metadata.jsonl \
  --output-dir "$OUTPUT_DIR" \
  --repos-dir /root/autodl-tmp/structfuse/repos/ \
  --workers 4 \
  --timeout 300 \
  --python-only \
  --skip-log "$OUTPUT_DIR/skip_log.jsonl" \
  2>&1 | tee /root/autodl-tmp/structfuse/m1_extraction.log
```

### 检查结果

| 检查项 | 状态 | 说明 |
|--------|------|------|
| Metadata 文件 | **OK** | `/root/autodl-tmp/swe_smith_metadata.jsonl` 存在，59,136 行，28.5MB |
| 输出路径 | **OK** | `/root/autodl-tmp/structfuse/m1_extraction/`，在数据盘 |
| 断点续传 | **OK** | 代码 L473-474 检查输出文件是否存在，已完成的 instance 自动跳过；已 clone 的 repo 也复用 |
| 超时设置 | **OK** | `--timeout 300` (5min/repo CodeQL DB 创建)，clone 超时硬编码 600s |
| `--python-only` | **OK** | 只处理纯 Python patch 的 instance |

### 需要修改的问题

#### 1. **CRITICAL: CodeQL 不在 PATH 中**
- CodeQL binary 在 `/opt/codeql/codeql`，但系统 PATH 不含 `/opt/codeql`
- `batch_extract.py` L98 直接调用 `"codeql"`，运行时会报 `FileNotFoundError`
- **修复**：脚本开头加 `export PATH="/opt/codeql:$PATH"`

#### 2. **CRITICAL: 磁盘空间严重不足**
- `/root/autodl-tmp/` 仅剩 **31GB**（总 169GB，已用 139GB）
- ~222 个唯一 (repo, commit) 需要 clone repo + 创建 CodeQL DB，且**代码不清理**：
  - repos 保留在 `repos_dir/` 不删除（L328: 如果存在就复用）
  - CodeQL DB 保留在 `repos_dir/repo__name_codeql_db` 不删除（L501-503）
- 保守估计 222 repos (~50-200MB each) + 222 DBs (~50-200MB each) = **40-80GB**，远超 31GB
- **修复**：需要清理已有数据腾出空间，或在 `process_repo_group()` 末尾添加 CodeQL DB 清理逻辑（处理完一个 group 后删除该 group 的 DB）

#### 3. **Workers = 4，要求是 8**
- 服务器有 192 CPU，当前 `--workers 4` 偏保守
- 但注意：CodeQL 用 `--threads=0`（使用全部 CPU），多 worker 并行时每个 CodeQL 进程都抢全部 CPU
- **建议**：改为 `--workers 8`，同时将 CodeQL `--threads` 改为固定值（如 24=192/8）以避免竞争。但 `--threads` 在 `batch_extract.py` 里是硬编码的（L103: `"--threads=0"`），需改代码或接受 CPU 竞争

### 耗时预估

脚本内置估算公式（L620-624）：
- 每 group 120s DB 创建 + 每 instance 30s 查询
- 222 groups × 120s + N_instances × 30s（N 取决于 `--python-only` 过滤后剩余数量）
- 假设过滤后 ~50K instances：222×120 + 50000×30 = 26,640 + 1,500,000 ≈ **424h serial**
- 4 workers ≈ **106h**，8 workers ≈ **53h**

实际会快于此估算——Beniget fallback 比 CodeQL 快得多，且 resume 可跳过已完成部分。

### 总结：需要 3 项修改才能启动

1. 脚本加 `export PATH="/opt/codeql:$PATH"`
2. 清理磁盘或加 CodeQL DB 自动清理逻辑（至少需要 50GB+ 可用空间）
3. `--workers 4` → `--workers 8`

---
