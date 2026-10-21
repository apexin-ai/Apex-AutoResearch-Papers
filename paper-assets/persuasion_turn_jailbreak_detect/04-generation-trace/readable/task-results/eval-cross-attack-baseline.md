# eval cross attack baseline

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cross-attack-baseline_20260517T204805_result.json`
- **Structured JSON:** [`662574b3b8a79b9831a5.json`](../../sessions/66/662574b3b8a79b9831a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成，结果已保存到 `results/cross_attack_eval.json`。

## Cross-Attack Evaluation 结果汇总

**Models trained on: Crescendo (250) + v4c benign (230)**  
**Evaluated on: FITD (80) / DD (80) / v4c benign (subset)**

### Full Conversation F1 (macro)

| Scenario | Treatment | Baseline | TF-IDF |
|----------|-----------|----------|--------|
| FITD vs benign | **1.0000** | 1.0000 | 1.0000 |
| DD vs benign | **1.0000** | 1.0000 | 1.0000 |
| FITD+DD vs benign | **1.0000** | 0.9937 | 1.0000 |

### Early Detection (F1 macro) - FITD

| K | Treatment | Baseline | TF-IDF |
|---|-----------|----------|--------|
| 1 | **0.9812** | 0.7483 | 0.9687 |
| 2 | **0.9750** | 0.6866 | 1.0000 |
| 3 | **0.9937** | 0.8465 | 1.0000 |
| 5 | 1.0000 | 0.9875 | 1.0000 |

### Early Detection (F1 macro) - DD

| K | Treatment | Baseline | TF-IDF |
|---|-----------|----------|--------|
| 1 | 0.9812 | **1.0000** | 1.0000 |
| 2 | 0.9875 | 1.0000 | 1.0000 |
| 3 | 0.9937 | 1.0000 | 1.0000 |
| 5 | 1.0000 | 1.0000 | 1.0000 |

### Key Findings

1. **Full conversation: 完美泛化** — 所有模型在完整对话上都达到 F1 ~1.0，OOD 攻击类型的完整对话足够区分。

2. **Early detection FITD 是关键区分点** — Baseline GRU 在 K=1 和 K=2 时严重下降（F1=0.75, 0.69），recall 仅 0.53/0.43。Treatment GRU 保持 0.98+。这说明 persuasion-grounded embeddings 对 FITD 的早期检测有显著帮助。

3. **DD 区分度低** — Baseline GRU 在 DD 上即使 K=1 也是完美的，说明 DD 的第一轮 user turn 本身就有足够的信号（可能风格/内容差异明显）。

4. **TF-IDF 在 K>=2 时过于强** — TF-IDF 从 K=2 开始就是 1.0，这暗示 FITD/DD 与 benign 可能存在 topic/vocabulary 的分布差异（而非纯靠 persuasion pattern），需要在论文中讨论这个 confound。

---
