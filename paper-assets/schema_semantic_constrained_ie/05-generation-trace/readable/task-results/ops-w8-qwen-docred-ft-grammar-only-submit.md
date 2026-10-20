# ops w8 qwen docred ft grammar only submit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_w8_qwen_docred_ft_grammar_only_submit_20260516T091401_result.json`
- **Structured JSON:** [`16ccf62fc4d03d60c3c1.json`](../../sessions/16/16ccf62fc4d03d60c3c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型已加载到 GPU（18.9GB VRAM）。进程 PID 18555 正在运行。Grammar 编译 96 个 relation types 需要几分钟，之后开始推理。

实验提交成功：
- **Server**: westd-21461, cuda:0
- **PID**: 18550 (wrapper) / 18555 (GPU subprocess)  
- **VRAM**: 18.9 GB
- **tmux session**: w8_qwen_docred_ft_grammar_only
- **Log**: ~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_grammar_only.log
- **预期运行时间**: ~5-6h (998 samples + constrained decoding)

Checkpoint 从 westd-16980 通过 sshpass + scp 成功传输到 westd-21461（16GB，通过 AutoDL SSH 代理）。

---
