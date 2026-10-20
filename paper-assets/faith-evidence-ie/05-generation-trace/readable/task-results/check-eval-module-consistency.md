# check eval module consistency

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_module_consistency_20260518T104319_result.json`
- **Structured JSON:** [`a134fc22586665626edb.json`](../../sessions/a1/a134fc22586665626edb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结论：PASS — 同一代码

```
模块一致性检查:
  freige.eval.inference → /root/autodl-tmp/freige/freige/eval/inference.py
  eval.inference        → /root/autodl-tmp/freige/eval/inference.py
  MD5: f08477ee40cb1194d3845213db1a1179 (两文件完全相同)
  大小: 21096 bytes, 最后修改 May 17 21:02 (同一时间)
  结论: PASS — 两个路径指向内容完全相同的文件，eval 结果跨模型可比

当前运行中的 8B eval 进程 (全部使用 python -m freige.eval.inference):
  PID 523341 — LLaMA-3.1-8B, CUDA:3, seed=s42
  PID 523748 — Qwen3-8B, CUDA:0, seed=s42
  PID 524157 — Qwen3-8B, CUDA:1, seed=s43
```

项目结构存在两份 `eval/inference.py`（`freige/eval/` 和 `freige/freige/eval/`），但 md5 完全一致，不影响结果。无需重跑 8B eval。

---
