# code phase0 eval

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase0-eval_20260519T170924_result.json`
- **Structured JSON:** [`232d8e4125d0201886d5.json`](../../sessions/23/232d8e4125d0201886d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。4 个脚本已写入 `/root/afford_invar/scripts/phase0/`:

| 脚本 | 功能 |
|------|------|
| `diversity_metrics.py` | 计算 1-BLEU、embedding divergence (all-MiniLM-L6-v2)、双向 NLI entailment (nli-deberta-v3-small) |
| `tier_classifier.py` | 按 BLEU/embed_sim 阈值分 Tier-1/2/3，输出分布统计和样例 |
| `kl_divergence.py` | 加载 OpenVLA-OFT，提取 layer-18 attention 对 image tokens 的分布，计算 KL divergence。支持 `--dry-run` |
| `run_phase0.py` | 串联 1→2→3，输出 PASS/MARGINAL/FAIL 判定 |

所有脚本 `--help` 正常，`kl_divergence.py --dry-run` 正确检测到模型权重。依赖 (sentence-transformers, nltk) 已安装。

---
