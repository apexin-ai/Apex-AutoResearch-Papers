# diagnose mvp p2b contrastive training

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_p2b_contrastive_training_20260512T131712_result.json`
- **Structured JSON:** [`069aeca730aafcc63026.json`](../../sessions/06/069aeca730aafcc63026.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：并发 ModelScope 下载将模型 safetensors 分片文件移至 `._____temp/` 临时目录且未 finalize 回主目录。Run 1 已加载模型到显存不受影响，Run 2 启动时文件已不在预期路径，触发 `FileNotFoundError`，`set -e` 导致脚本立即退出，Run 3-9 未执行。

**已完成**：
- Registry `failure_reason` 字段已更新
- 诊断报告已注册为 artifact (`art_20260512_6211d5`)

**修复要点**：将 `._____temp/*.safetensors` 移回主目录后，从 Run 2 开始重跑即可。建议将模型目录迁至 `/root/autodl-tmp/` 避免与 ModelScope cache 路径冲突。

---
