# code matched llama ar eval prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_matched_llama_ar_eval_prep_20260521T035027_result.json`
- **Structured JSON:** [`c90f954f419ce4356c98.json`](../../sessions/c9/c90f954f419ce4356c98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 修改内容

**`src/eval_phase2_gar.py`** — 3 处修改：
1. `build_conversation()` (L184): `system_prompt` 改为可选，`None` 时不加 system message（匹配 ultrachat 无 system prompt 的格式）
2. 新增 CLI 参数 `--ar-from-fixed`（L362）和 `--max-turns`（L364）
3. 新增对话加载分支（L402-415）：从 `--conversations-path` 提取 user turns，截断到 `--max-turns`，用 `build_conversation()` 生成 AR 响应

**`scripts/eval_llama_ar_matched.sh`** — 4 步 AR eval：
- AR Base + GAR-ours (N=50, T=4)
- AR Base + GAR-Dongre (N=50, T=4)
- AR TG + GAR-ours (N=50, T=4)
- AR TG + GAR-Dongre (N=50, T=4)

输出到 `runs/eval_llama_ar_matched/`，自动检测 TG checkpoint。

## 执行命令

```bash
bash /root/turn_residual_gating/scripts/eval_llama_ar_matched.sh
```

注意：AR 模式需要对每个 conversation 逐轮生成（50×4=200 次 model.generate），耗时远大于 TF eval。

---
