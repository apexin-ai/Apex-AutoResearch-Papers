# diag exp004 data loading

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp004-data-loading_20260518T173821_result.json`
- **Structured JSON:** [`97ff2e54efd22dad9279.json`](../../sessions/97/97ff2e54efd22dad9279.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整分析如下：

## exp-004 数据加载流程

### 数据文件
`/root/contrastive_entrain_calib/data/calibration_v2_1_expanded.jsonl` — 与 exp-008 相同。

### 数据结构
每条数据是 3-turn 对话：
1. **Turn 0 (user)**: 提问
2. **Turn 1 (assistant)**: 给出错误答案
3. **Turn 2 (user)**: 用户纠正/施压

**没有第 4 轮 assistant response。**

### exp-004 的关键处理方式

exp-004 **不需要第 4 轮**。它的 SFT target 是 **Turn 1（assistant 的第一次回复）**：

```python
# _tokenize_sample 的逻辑：
msgs = [{"role": t["role"], "content": t["content"]} for t in sample["turns"]]  # 全部 3 turns

full_ids = tokenizer.apply_chat_template(
    msgs, tokenize=True, add_generation_prompt=True  # ← 加 generation prompt
)

# 定位 assistant（Turn 1）的起止位置
pre_asst_ids = tokenizer.apply_chat_template(
    msgs[:1], tokenize=True, add_generation_prompt=True  # 只取 Turn 0
)
asst_start = len(pre_asst_ids)  # assistant 回复开始的 token 位置

# 找 <|im_end|> 确定 assistant 回复结束
asst_end = asst_start
while asst_end < len(full_ids) and full_ids[asst_end] != im_end_id:
    asst_end += 1
asst_end += 1

# labels: 只有 Turn 1 (assistant) 区间有 loss，其余 -100
labels = [-100] * len(full_ids)
for i in range(asst_start, min(asst_end, len(full_ids))):
    labels[i] = full_ids[i]
```

### SFT Target 定义

- **Input**: 完整 3-turn 对话 + generation prompt（作为 context）
- **Labels**: 只在 Turn 1（assistant 首次回复）的 token 位置计算 cross-entropy，其余位置 masked（-100）
- **resp_pos**: `len(full_ids) - 1`，即序列最后一个 token 的位置，用于提取 hidden state 做 L2 consistency loss

### 与 exp-008 的根本区别

exp-008 试图把 **Turn 3（第二轮 assistant response）** 作为 SFT target，但数据里根本没有 Turn 3。

exp-004 的做法完全不同：它把整个 3-turn 对话作为 input context，SFT target 是已有的 Turn 1（assistant 的初始回复）。本质上是在"给定完整对话上下文"的条件下，训练模型重现 assistant 的原始回答。

### 可复用到 exp-008 的方案

直接复用 exp-004 的 `_tokenize_sample` 方法：用 3-turn 数据 + `add_generation_prompt=True`，将 Turn 1 (assistant) 作为 SFT target。或者，如果 exp-008 需要训练模型在被纠正后的回复，需要先用 LLM 生成第 4 轮 assistant response 追加到数据中。

---
