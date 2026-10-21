# code autodl5090 multiseed fill

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_autodl5090_multiseed_fill_20260518T193925_result.json`
- **Structured JSON:** [`caac73b19dea24cadaa7.json`](../../sessions/ca/caac73b19dea24cadaa7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四张 GPU 全满载运行。汇报如下：

---

## 汇报

### GPU 使用状态（全部占满）

| GPU | 任务 | tmux session | 状态 |
|-----|------|-------------|------|
| cuda:0 | Qwen CoNLL n16 seed=123 | `qwen_conll_s123` | 推理中，~20 min 完成 |
| cuda:1 | LLaMA FewNERD LoRA 训练 | `llama_fewnerd` | 65%，约 4h 剩余（未碰） |
| cuda:2 | Qwen CoNLL n16 seed=456 | `qwen_conll_s456` | 推理中，~20 min 完成 |
| cuda:3 | Qwen SciERC T=1.2 seed=123 | `scierc_t12_s123` | 刚启动，SciERC 551 实例很快（~2 min） |

### cuda:3 FewNERD T=1.2 状态
已完成。输出在 `output/exp_031_fewnerd_t12/`（report.json + samples.jsonl）。

### 覆盖情况
**主实验 (T=1.0)：**
- Qwen SciERC n16: seed 42/123/456 全部完成
- Qwen CoNLL n16: seed 42 完成，seed 123/456 正在跑
- Qwen FewNERD n8: seed 42/123/456 全部完成

**温度消融 (T=1.2)：**
- SciERC: seed 42 完成，seed 123 正在跑（cuda:3）
- CoNLL: seed 42 完成
- FewNERD: seed 42 刚完成

### 新增启动
1. `exp_002_conll_n16_seed123` (cuda:0)
2. `exp_002_conll_n16_seed456` (cuda:2)
3. `exp_026_t12_seed123` (cuda:3，FewNERD 完成后接力)

---
