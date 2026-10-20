# code write repair only script

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_write_repair_only_script_20260514T181201_result.json`
- **Structured JSON:** [`b360265dcf3e89bed4c8.json`](../../sessions/b3/b360265dcf3e89bed4c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`repair_only.py` 已创建并通过验证。

- 当前 JSON 有 126 条记录，其中 50 条需要 repair（43 disagree + 7 single_error）
- `--dry-run` 正常工作，参数解析正确
- pipeline 完成后合并 JSONL 时加 `--input-jsonl results/mvp_v4_full.jsonl` 即可覆盖全部 204 样本

运行命令：
```bash
cd /root/autodl-tmp/crdd
python3 src/repair_only.py \
  --input results/mvp_v4_full.json \
  --input-jsonl results/mvp_v4_full.jsonl \
  --output results/mvp_v4_repair_fixed.json
```

---
