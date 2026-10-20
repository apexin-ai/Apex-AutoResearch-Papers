# diagnose dead experiments

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_dead-experiments_20260516T015143_result.json`
- **Structured JSON:** [`9fd39096a340e09bf419.json`](../../sessions/9f/9fd39096a340e09bf419.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已全部更新。诊断总结：

---

## 诊断结果

### plan-006-confound-fix — SUCCESS
匹配生成参数后（rp=1.0, max_tokens=256），paraphrastic chains 仍然比 continuation 更快丢失 depth signal，确认结论非参数混淆所致：
- **3-class F1**: para 0.727 vs cont 0.788, delta **-0.061**
- **Binary F1**: para 0.613 vs cont 0.749
- **Depth retention**: para 0.995 vs cont 0.826（para 几乎不丢样本但分类更难，cont 丢更多样本但剩余样本 signal 更强）
- **Cross-transfer**: para→cont 0.769, cont→para 0.606（不对称，说明 continuation 的 depth features 更具判别力）

### plan-012-qwen06b-v2 — SUCCESS（此前被误判为 failed）
进程正常退出并写出完整结果文件，但因无 sentinel/W&B 被自动标记为 failed。实际结果：
- **5-class F1**: 0.5873 ± 0.0047（原版 0.5828, delta **+0.0045**）
- **3-class F1**: 0.9054 ± 0.0037（原版 0.9052, delta **+0.0002**）
- seed 42→123、LoRA r 16→32 的变化对性能影响可忽略（<0.5%），**确认 QLoRA depth classifier 对超参不敏感**

---
