# ops fix gpt2m cache path

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-gpt2m-cache-path_20260515T115544_result.json`
- **Structured JSON:** [`62cacef1db18fb3b8861.json`](../../sessions/62/62cacef1db18fb3b8861.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

**修复前**：
- `hub/models--gpt2-medium/` → 2.8M（空壳）
- `models--gpt2-medium/`（hub 外）→ 1.5G（完整模型）

**修复后**：
- `hub/models--gpt2-medium/` → 1.5G（完整模型已就位）
- 旧位置已删除

**验证结果**：
- `params=354,823,168`
- `n_embd=1024, n_head=16, n_layer=24, n_positions=1024, vocab_size=50257`
- `GPT-2-medium LOAD OK`

注：该服务器 HuggingFace 网络不通，实验代码加载模型时需设置 `TRANSFORMERS_OFFLINE=1` 或 `local_files_only=True`。

---
