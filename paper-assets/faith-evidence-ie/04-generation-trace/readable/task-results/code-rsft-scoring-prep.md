# code rsft scoring prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsft_scoring_prep_20260516T140123_result.json`
- **Structured JSON:** [`dae5a86d5c3e15e20cdc.json`](../../sessions/da/dae5a86d5c3e15e20cdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已保存到 `memory.md`（`save_project_file` 白名单限制，无法写自定义文件名）。

验证完成，总结：

1. **rsft_score_filter.py 可用** — 导入 OK，argparse 参数确认
2. **Candidate gen 输出路径**:
   - 1.7B → `/root/autodl-tmp/freige/outputs/rsft_candidates_1_7b` (GPU 0, 57/3053 docs)
   - 8B → `/root/autodl-tmp/freige/outputs/rsft_candidates_8b` (GPU 3, 47/3053 docs)
3. **GPU 需求**: NLI 模型 ~400MB，轻量，任意单卡可运行
4. **阻塞项**: generation 仍在运行（预计 10-13 小时），需等完成后再执行 scoring
5. **命令模板已准备好**，含 CUDA_VISIBLE_DEVICES 设置（遵守 C002/C003）

---
