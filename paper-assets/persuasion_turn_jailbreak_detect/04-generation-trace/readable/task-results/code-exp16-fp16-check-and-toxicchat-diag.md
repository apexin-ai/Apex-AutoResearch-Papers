# code exp16 fp16 check and toxicchat diag

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-fp16-check-and-toxicchat-diag_20260520T005802_result.json`
- **Structured JSON:** [`4d8dd3a04adec42c85e5.json`](../../sessions/4d/4d8dd3a04adec42c85e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因完全清楚了。汇报结果：

---

## fp16 影响: **不需要重跑**

- exp16 所有 checkpoint 均为 **torch.float32** 存储
- exp17 checkpoint 同样是 float32
- `src/evaluate.py`（exp16 用）的 baseline 路径显式指定 `dtype=torch.float32`，treatment 路径通过 `DeBERTaMultiTask`（fp32 初始化）+ `load_state_dict` 加载 fp32 权重
- exp17 eval 中的 `.float()` 是 no-op
- **结论：exp16 的 64 个结果不受影响，无需重跑**

---

## ToxicChat 低分诊断

### 数据路径
- exp16 和 exp17 用 **同一文件**: `data/mhj/toxicchat_plan002_eval.jsonl`（242 条：204 jailbreak + 38 benign）
- eval 逻辑功能等价（都提取 user turns、binary label）
- **不是 eval 代码 bug**

### 根因：单轮 jailbreak 检测失败

ToxicChat 的结构特殊：
| 类别 | 数量 | user turns | 来源 |
|------|------|-----------|------|
| jailbreak | 204 | **全部 1 轮** | toxicchat-human |
| benign | 38 | 6-10 轮 | qwen3-8b 合成 |

训练数据分布：
| 数据集 | JB 单轮 | BN 单轮 | JB 轮数范围 | BN 轮数范围 |
|--------|---------|---------|------------|------------|
| mixed_500 | **0/174** | 0/176 | 5-12 | 5-10 |
| expanded_1000 | **0/350** | 0/350 | 5-12 | 6-14 |

**两个训练集都没有任何单轮对话。** 模型在单轮输入上的行为是 OOD 外推。

抽样验证（9class seed42 on ToxicChat）：

| 模型 | 1-turn JB 检出 | multi-turn BN 检出 |
|------|---------------|-------------------|
| **exp16** | 183/204 (89.7%) | 38/38 (100%) |
| **exp17** | 37/204 (18.1%) | 38/38 (100%) |

exp17 模型把 **167/204 单轮 jailbreak 错判为 benign**，而 multi-turn benign 全对。

### 为什么 exp17 比 exp16 差

两个模型都从未见过单轮数据，单轮行为是外推。exp16 "碰巧" 能检测单轮 jailbreak（DeBERTa embedding 恰好落在 GRU 判别区域的 jailbreak 侧），exp17 则不行。expanded_1000 数据量更大、轮数更多（均值 8.5-9.1 vs 7.9-8.2），GRU 更强地学到了"序列长度"这个 spurious feature，导致单轮外推行为恶化。

DD/AA OOD 不受影响，因为它们都是多轮 jailbreak。

### 建议
1. **训练集加入单轮 jailbreak 样本**（从 ToxicChat 采样加入训练集，或合成单轮 jailbreak 数据）
2. 或者在论文中将 ToxicChat 标注为 **"zero-shot single-turn transfer"** 而非标准 OOD benchmark，因为当前模型架构（GRU 序列分类器）天然不适合单轮场景
3. 当前 exp17 DD/AA OOD 结果可信（多轮对多轮），ToxicChat 低分是 distribution shift 而非模型退化

---
