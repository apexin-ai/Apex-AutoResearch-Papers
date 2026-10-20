# code exp16 leak check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-leak-check_20260519T234739_result.json`
- **Structured JSON:** [`b5bba7ef3497e76612a0.json`](../../sessions/b5/b5bba7ef3497e76612a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Source-label 并无 confound，是均衡的。汇总全部结果。

---

## 排查结论

### 1. Conversation_id 级别泄漏: **无**
- Train=350, Val=74, Test=76，三个集合完全不相交，0 重叠

### 2. 内容级别泄漏: **无**
- 350/74/76 个对话内容 MD5 哈希全部唯一，无重复内容

### 3. Label/Source 分布
| Split | n | benign | jailbreak | llama | qwen |
|-------|---|--------|-----------|-------|------|
| train | 350 | 176 | 174 | 176 | 174 |
| val | 74 | 36 | 38 | 36 | 38 |
| test | 76 | 38 | 38 | 38 | 38 |

- Source × Label 交叉：**均衡**（每个 source 中 benign/jailbreak 各半），无 confound
- Attack types: train 有 10 种（含 Role+Obfuscation），test 只有 9 种（缺 Role+Obfuscation）

### 4. Train Loss 曲线确认
BiGRU 分类器（在预计算 DeBERTa embedding 上训练）：
- **Epoch 1**: Train Loss ~0.08–0.10, Val Loss ~0.03–0.06, Val Acc=0.9865
- **Epoch 2–20**: Train Loss=0.0000, Val Loss 持续上升（0.11→0.18），Val Acc 恒定 0.9865
- Best model 保存在 **Epoch 1**（val_loss 最低）

→ **Train Loss=0.0 是因为 BiGRU 在 Epoch 2 即完全记忆了训练集**（tiny model + pre-computed embeddings），是典型过拟合，不是泄漏。

### 5. 真正的问题：不是泄漏，是分布过拟合

| Test Set | 9class F1 | vanilla F1 |
|----------|-----------|------------|
| **mixed_test** (ID) | **1.0000** | 0.8146 |
| **qwen_test** (ID) | **1.0000** | 0.9605 |
| dd_ood | 0.3798 | — |
| aa_ood | 0.1753 | — |
| llama_aa | **0.0741** | — |
| toxicchat | 0.8646 | — |

**F1=1.0 在 in-distribution test 上是真实的，不存在数据泄漏。** 但 OOD 表现崩溃（最低 0.07）说明 9-class persuasion 特征高度分布特异——模型学到的是训练集中特定 attack type 的模式（如 turn-level persuasion strategy），而非通用的 jailbreak 信号。76 个测试样本也太小，完全正确的方差很大。

---
