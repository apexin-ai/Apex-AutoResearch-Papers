# code fix pipeline memory leak

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_pipeline_memory_leak_20260514T174736_result.json`
- **Structured JSON:** [`614b26018fee70547873.json`](../../sessions/61/614b26018fee70547873.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。修改总结：

**pipeline.py 改动：**
1. **Resume 内存优化** — 新增 `_load_done_ids()` 函数，从 JSON/JSONL 文件只提取 ID 集合，不在内存中保留完整记录
2. **JSONL 逐条追加写入** — 每处理完一个样本立即 append 一行 JSON 到 `.jsonl` 文件，不再在内存中累积 results 列表。首次从 JSON array resume 时自动转换为 JSONL 格式
3. **内存清理** — 每个样本处理完后 `del rec` + `gc.collect()`

**evaluate_mvp.py 改动：**
- `load_results()` 自动识别 JSON array 和 JSONL 两种格式

**文件安全：**
- `pipeline.py.bak` 和 `mvp_v4_full.json.bak125` 已备份
- 续跑时会自动将 `mvp_v4_full.json` 转换为 `mvp_v4_full.jsonl`（原文件不动），新样本追加到 JSONL

**启动命令参考：**
```bash
cd /root/autodl-tmp/crdd && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 src/pipeline.py --resume results/mvp_v4_full.json
```

代码已验证就绪，等你用 `submit_training_job` 提交。

---
