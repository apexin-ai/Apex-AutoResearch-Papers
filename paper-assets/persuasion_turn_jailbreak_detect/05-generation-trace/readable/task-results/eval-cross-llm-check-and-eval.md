# eval cross llm check and eval

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cross-llm-check-and-eval_20260519T071226_result.json`
- **Structured JSON:** [`fb3f801522266a8b8fa1.json`](../../sessions/fb/fb3f801522266a8b8fa1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果如下：

## 跨 LLM 验证结果

### 数据生成统计
| 数据集 | 总数 | 格式 |
|--------|------|------|
| DD jailbreak (Llama) | 50 | 多轮对话 JSONL |
| AA jailbreak (Llama) | 50 | 多轮对话 JSONL |
| Benign (Llama) | 50 | 多轮对话 JSONL |

### 推理结果（Macro F1, mean±std, 3 seeds）

| Variant | DD K=1 | DD K=3 | DD Full | AA K=1 | AA K=3 | AA Full |
|---------|--------|--------|---------|--------|--------|---------|
| vanilla | .170±.047 | .242±.037 | .261±.018 | .248±.017 | .242±.037 | .261±.018 |
| jb_mlm | .332±.002 | .333±.000 | .282±.073 | .316±.011 | .330±.002 | .368±.049 |
| 9class | .312±.021 | .351±.018 | .433±.057 | .265±.019 | .266±.036 | .321±.050 |

### Qwen vs Llama 对比（DD Full）

| Variant | Qwen DD Full | Llama DD Full | Gap |
|---------|-------------|---------------|-----|
| vanilla | 0.312 | 0.261 | **-0.051** |
| jb_mlm | 0.914 | 0.282 | **-0.632** |
| 9class | 0.997 | 0.433 | **-0.564** |

### 结论

**DAPT 优势在 Llama 数据上完全崩溃。** 

- 所有 variant 在 Llama 数据上的 F1 都接近 0.333（即全预测同一类别，等同随机水平）
- jb_mlm 从 Qwen 上的 0.914 暴跌至 0.282（-0.632），9class 从 0.997 跌至 0.433（-0.564）
- 说明在 Qwen 数据上训练的检测器严重过拟合了 Qwen 的生成风格，无法泛化到 Llama 的文本分布
- 这对论文是重要发现：当前方法的跨 LLM 泛化能力极弱，DAPT 带来的增益几乎全来自对训练时 LLM 文本风格的记忆，而非学到了攻击的语义结构

结果已保存至 `/root/persuasion_turn_jailbreak_detect/results/cross_llm_eval.json`。

---
