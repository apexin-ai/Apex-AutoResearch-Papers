# check d003 wikitext completion

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d003_wikitext_completion_20260512T154738_result.json`
- **Structured JSON:** [`3fd1b45294b37906733e.json`](../../sessions/3f/3fd1b45294b37906733e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果 JSON 已获取。日志文件 tail 超时（可能文件很大），exit file 无 session，tmux 不允许 read-only。关键信息都在 JSON 里。

## D003 wikitext_32k 结果

### 完整结果 JSON

```json
{
  "experiment": "d003_wikitext_32k",
  "config": {
    "model": "/root/carc/models/DeepSeek-R1-Distill-Qwen-14B",
    "budget_ratio": 0.5,
    "budget": 13107,
    "grace_window": 175,
    "seq_len": 32768,
    "total_tokens": 32768,
    "prefill_len": 26214,
    "eval_len": 6554
  },
  "results": [
    {"strategy": "full",      "ppl": 7.1822, "elapsed_seconds": 244.7},
    {"strategy": "ema_0.9",   "ppl": 7.7788, "elapsed_seconds": 1278.9},
    {"strategy": "ema_0.7",   "ppl": 8.1367, "elapsed_seconds": 1281.9},
    {"strategy": "ema_0.5",   "ppl": 8.1352, "elapsed_seconds": 1282.5},
    {"strategy": "random",    "ppl": 7.6432, "elapsed_seconds": 253.0},
    {"strategy": "recency",   "ppl": 7.1758, "elapsed_seconds": 253.3}
  ],
  "summary": {
    "full_ppl": 7.1822,
    "best_ema_ppl": 7.7788,
    "random_ppl": 7.6432,
    "recency_ppl": 7.1758,
    "ema_vs_random_gap_pct": -1.77,
    "ema_beats_recency": false,
    "pass": false
  }
}
```

### 判定: **FAIL**

`"pass": false`。核心问题：

| 策略 | PPL | 与 full 差距 |
|------|-----|-------------|
| full (oracle) | 7.1822 | — |
| **recency** | **7.1758** | **-0.09%** (略优于 full) |
| random | 7.6432 | +6.42% |
| **ema_0.9 (best)** | **7.7788** | **+8.30%** |
| ema_0.5 | 8.1352 | +13.27% |
| ema_0.7 | 8.1367 | +13.29% |

EMA 策略全面劣于 random baseline（best ema 7.7788 vs random 7.6432，差 -1.77%），更远逊于 recency（7.1758）。Recency 几乎追平 full attention，说明在 wikitext 32k 上下文中，最近的 token 最重要，attention-score-based eviction 反而引入了噪声。

**Exit code**: 无 exit file（`~/runs/` 路径下不存在），但 JSON 完整输出表明脚本正常运行结束。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "experiment": "d003_wikitext_32k",
    "config": {
      "model": "/root/carc/models/DeepSeek-R1-Distill-Qwen-14B",
      "budget_ratio": 0.5,
      "budget": 13107,
      "grace_window": 175,
      "seq_len": 32768,
      "total_tokens": 32768,
      "prefill_len": 26214,
      "eval_len": 6554
    },
    "results": [
      {
        "strategy": "full",
        "ppl": 7.1822,
        "elapsed_seconds": 244.7
      },
      {
        "strategy": "ema_0.9",
        "ppl": 7.7788,
        "elapsed_seconds": 1278.9
      },
      {
        "strategy": "ema_0.7",
        "ppl": 8.1367,
        "elapsed_seconds": 1281.9
      },
      {
        "strategy": "ema_0.5",
        "ppl": 8.1352,
        "elapsed_seconds": 1282.5
      },
      {
        "strategy": "random",
        "ppl": 7.6432,
        "elapsed_seconds": 253.0
      },
      {
        "strategy": "recency",
        "ppl": 7.1758,
        "elapsed_seconds": 253.3
      }
    ],
    "summary": {
      "full_ppl": 7.1822,
      "best_ema_ppl": 7.7788,
      "random_ppl": 7.6432,
      "recency_ppl": 7.1758,
      "ema_vs_random_gap_pct": -1.77,
      "ema_beats_recency": false,
      "pass": false
    }
  }
}
```

</details>

---
