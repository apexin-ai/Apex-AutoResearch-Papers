# code gsm8k fix rescore

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k-fix-rescore_20260514T065258_result.json`
- **Structured JSON:** [`519d0ba1645919a524d2.json`](../../sessions/51/519d0ba1645919a524d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

### 1. evaluate.py 修复内容

**行 186-188** (`extract_gsm8k_answer` 的 `####` 匹配路径):
```python
# 旧:
return match.group(1).strip().replace(",", "")
# 新:
answer = match.group(1).strip().replace(",", "")
answer = re.sub(r'[^-\d.]', '', answer)
return answer
```

**行 217-218** (gold answer 处理) + **行 382-383** (paraphrased eval 路径):
```python
# 新增一行:
gold_answer = re.sub(r'[^-\d.]', '', gold_answer)
```

### 2. Git

无本地 git repo，直接在服务器修改。

### 3. 重评分结果

| Model | Dosage | Seed | GSM8K_old | GSM8K_new | Δ | Flipped |
|---|---|---|---|---|---|---|
| Qwen2.5-3B | d000 | s42 | 0.1168 | 0.1198 | +0.30% | 4↑ 0↓ |
| Qwen2.5-3B | d000 | s123 | 0.1759 | 0.1812 | +0.53% | 7↑ 0↓ |
| Qwen2.5-1.5B | d000 | s42 | 0.6368 | 0.6543 | +1.74% | 23↑ 0↓ |
| Qwen2.5-1.5B | d000 | s123 | 0.6331 | 0.6535 | +2.05% | 27↑ 0↓ |
| Qwen2.5-0.5B | d000 | s123 | 0.3404 | 0.3412 | +0.08% | 1↑ 0↓ |
| Qwen2.5-0.5B | d005 | s42 | 0.3601 | 0.3624 | +0.23% | 3↑ 0↓ |

### 4. 结论：此 bug **不能**解释 3B GSM8K 倒挂

- 3B 修正后仅提升 +0.3%~+0.5%（4~7 个 item），accuracy 仍为 **12.0%/18.1%**
- 1.5B 受影响更大（+1.7%~+2.1%，23~27 item），修正后差距反而**更大**了
- 3B 的 bug 影响很小（仅 `$` 前缀和 unit 后缀各几个），说明 3B 的主要问题不是答案提取，而是**模型本身没有正确解题**（大量 pred 和 gold 数值完全不同）
- 倒挂的根因需要在别处找（可能是 SFT 数据/训练过程导致 3B 的 CoT 能力退化）

翻转详情中可以看到：`$18→18`、`48 hours→48`、`$480→480` 这类单位/货币前缀是主要 pattern。1.5B 模型更倾向于在答案中附带 `$`/单位，所以受影响更多。

---
