# code bugfix eval p2b

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bugfix_eval_p2b_20260512T125853_result.json`
- **Structured JSON:** [`84fbbc1f94b3b835c10e.json`](../../sessions/84/84fbbc1f94b3b835c10e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

**修改文件**：服务器 `/root/structfuse/scripts/eval_p2b.py`（本地无副本，无需同步）

**修改内容**：

1. **第 1-2 行（新增）**：文件最顶部加 `import os` + `os.environ["CUDA_VISIBLE_DEVICES"] = "4"`，在所有其他 import 之前
2. **第 34-37 行（原第 31 行）**：`model.load_state_dict(state_dict, strict=False)` → 保留 `strict=False` 但捕获返回值，打印 missing/unexpected keys，并 assert missing_keys 为空

语法验证通过。

---
