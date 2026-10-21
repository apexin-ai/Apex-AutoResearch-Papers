# code rsft generate resume

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsft-generate-resume_20260520T075154_result.json`
- **Structured JSON:** [`d9cbeaf8850d9df09207.json`](../../sessions/d9/d9cbeaf8850d9df09207.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。

## 改动摘要

**修改文件**: `/root/autodl-tmp/freige/freige/training/rsft_generate.py`（bjb2 服务器）

### 改动内容

1. **新增函数 `load_progress_from_jsonl(output_file, num_generations)`**（L158-197）
   - 扫描 `generations.jsonl`，统计每个 `doc_id` 的条目数
   - `count >= num_generations` 的 doc 标记为已完成
   - 如果存在不完整的 doc（崩溃中断导致 < N 条），自动截断这些条目（通过 `os.replace` 原子写入 tmp 文件），避免后续 append 产生重复

2. **新增参数 `--resume`**（L279-280）
   - `action="store_true"`，默认 False
   - 启用后从 `generations.jsonl` 重建已完成集合，不依赖 `progress.json`

3. **修改进度加载逻辑**（L329-332）
   - `--resume` → `load_progress_from_jsonl(output_file, args.num_generations)`
   - 否则 → 原有 `load_progress(output_dir)`（基于 `progress.json`）

### 使用方式

```bash
# 崩溃后恢复（从现有 14976 行 jsonl 续跑）
python -m freige.training.rsft_generate \
    --base_model ... --sft_adapter ... --data_path ... \
    --output_dir /root/autodl-tmp/rsft_generations_14b \
    --resume
```

### 关键字段

- Resume 使用的 doc_id 字段: `doc_id`（jsonl 每行的 `"doc_id"` 字段）
- 完整性判定: `doc_id` 出现次数 >= `--num_generations`（默认 8）
- 已有的 append 写入 + `fout.flush()` + `save_progress()` 机制保持不变

---
