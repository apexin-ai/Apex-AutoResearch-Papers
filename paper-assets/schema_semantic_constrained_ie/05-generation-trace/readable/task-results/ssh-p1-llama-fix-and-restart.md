# ssh p1 llama fix and restart

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p1_llama_fix_and_restart_20260518T221956_result.json`
- **Structured JSON:** [`54344ba7d69d64b8b423.json`](../../sessions/54/54344ba7d69d64b8b423.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行：

**修复内容：**
1. **peft AWQ dispatcher 报错** — `pip install optimum` 未解决根本问题（`gptqmodel` 类名不兼容），改用 monkey-patch 直接在 `awq.py` 模块上 patch `is_gptqmodel_available = lambda: False`
2. **checkpoint 路径** — `output_dir` 和 `merged_dir` 默认值及 bash 脚本中所有引用均改到 `/root/autodl-tmp/checkpoints/`

**当前状态：**
- Step 0（SFT 数据）已完成
- Step 1（训练）进行中：1/39 steps，GPU 0 占用 55.6GB，util 100%
- 数据卷剩余 109GB，空间充足

---
