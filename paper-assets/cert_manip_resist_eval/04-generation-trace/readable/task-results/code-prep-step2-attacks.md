# code prep step2 attacks

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-step2-attacks_20260521T214143_result.json`
- **Structured JSON:** [`db4507700e1bdace5e9d.json`](../../sessions/db/db4507700e1bdace5e9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**产出** — `attack_data/` 目录 8 个 JSON 文件（2 数据集 × (1 clean + 3 attacked)）：

| 文件 | 大小 |
|------|------|
| `mmlu_clean_pairs.json` | 272 KB |
| `mmlu_prompt_injection_attacked.json` | 317 KB |
| `mmlu_sycophancy_attacked.json` | 321 KB |
| `mmlu_score_manipulation_attacked.json` | 315 KB |
| `arc_challenge_clean_pairs.json` | 199 KB |
| `arc_challenge_prompt_injection_attacked.json` | 244 KB |
| `arc_challenge_sycophancy_attacked.json` | 248 KB |
| `arc_challenge_score_manipulation_attacked.json` | 242 KB |

每个文件 300 条样本，字段包含 `question`, `response_a`, `response_b`, `ground_truth_winner`, `attacked_side`, `attack_name`。Step 2 可直接读取使用。

---
