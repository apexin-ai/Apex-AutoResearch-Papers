# ssh reviewer fixes

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_reviewer-fixes_20260515T172933_result.json`
- **Structured JSON:** [`71187e5bb6812c85b286.json`](../../sessions/71/71187e5bb6812c85b286.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项修复完成。

### Fix 1: visual_similarity_gate.py GPU 硬编码
- **第 27 行**：`cuda:1` → `cuda:0`
- 脚本已有 `--device` 参数（支持 `auto/cpu/cuda:N`），无需额外加 `--gpu`。`auto` 模式现在默认用 `cuda:0`，用户可通过 `--device cuda:2` 指定其他 GPU
- 语法验证通过

### Fix 2: .bak 文件清理
删除 3 个文件：
- `scripts/extract_features.py.bak`
- `scripts/train_probes.py.bak`
- `scripts/analyze_goal_probes.py.bak`

确认 `scripts/` 下已无 .bak 文件。

### 额外发现
无其他问题。

---
