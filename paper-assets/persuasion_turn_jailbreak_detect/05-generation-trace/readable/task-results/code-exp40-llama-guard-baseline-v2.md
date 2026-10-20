# code exp40 llama guard baseline v2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp40-llama-guard-baseline-v2_20260521T120435_result.json`
- **Structured JSON:** [`e7357a9092a801cf8d03.json`](../../sessions/e7/e7357a9092a801cf8d03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果 JSON 已保存到 `/root/persuasion_turn_jailbreak_detect/results/exp40_llama_guard_baseline.json`。

## Exp40 Llama Guard 3 8B Baseline 结果

| Dataset | Mode | F1-macro | Prec(J) | Rec(J) | F1(J) | Unparseable |
|---------|------|----------|---------|--------|-------|-------------|
| IID (Crescendo) | Full | 0.4325 | 0.8000 | 0.1053 | 0.1860 | 0 |
| IID (Crescendo) | K=2 | 0.4325 | 0.8000 | 0.1053 | 0.1860 | 0 |
| OOD DD | Full | 0.2525 | 0.5000 | 0.0125 | 0.0244 | 0 |
| OOD DD | K=2 | 0.2525 | 0.5000 | 0.0125 | 0.0244 | 0 |
| OOD AA | Full | 0.2387 | 0.0000 | 0.0000 | 0.0000 | 0 |
| OOD AA | K=2 | 0.2387 | 0.0000 | 0.0000 | 0.0000 | 0 |
| OOD FITD | Full | 0.2387 | 0.0000 | 0.0000 | 0.0000 | 0 |
| OOD FITD | K=2 | 0.2387 | 0.0000 | 0.0000 | 0.0000 | 0 |

**关键发现：**
- Llama Guard 3 8B 在所有数据集上表现极差，几乎把所有对话都判为 "safe"
- IID Crescendo recall 仅 10.5%（38 个 jailbreak 样本只检出 4 个），precision 80%
- OOD AA / FITD recall = 0%，完全无法检测
- OOD DD 仅检出 1/80 个 jailbreak 样本
- Full 和 K=2 结果完全一致（说明模型主要依赖最后一轮判断，与 Llama Guard 只评估最后一条消息的设计一致）
- unparseable rate = 0（输出格式解析正常）

**bug 修复说明：** 脚本中已有 `hasattr(encoded, 'input_ids')` 的修复。transformers 5.8.1 中 `apply_chat_template(return_tensors="pt")` 返回 `BatchEncoding` 而非裸 tensor，`hasattr` 分支正确提取了 `input_ids` tensor，脚本运行无报错。

---
