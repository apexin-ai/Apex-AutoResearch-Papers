# code plan 002 router sft prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-002-router-sft-prep_20260513T221215_result.json`
- **Structured JSON:** [`c1360e153c5f0a849965.json`](../../sessions/c1/c1360e153c5f0a849965.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。

**Plan-002 准备完成，总结：**

| 项目 | 状态 |
|------|------|
| `router_sft_train.py` 更新并部署到 westb-13313 | ✅ 506行，所有 imports OK |
| 数据加载：支持 `--data_path`（新 sft_triples.jsonl）+ `--data_dir`（旧格式） | ✅ |
| 标签映射：`internal-preferred` → `internal`, `det-preferred` → `deterministic`, `no-preference` 过滤 | ✅ |
| Prompt 模板：Qwen3 ChatML 格式（`<\|im_start\|>system/user`） | ✅ |
| 超参默认值：lr=2e-5, batch=32, max_seq_len=2048, epochs=3 | ✅ |
| Qwen3-1.7B HuggingFace model ID | `Qwen/Qwen3-1.7B` |
| Dry-run 验证 | ✅ 通过 |

Plan-001b 数据收集完成后，启动训练命令：
```bash
python src/router_sft_train.py \
  --data_path results/plan_001b/sft_triples.jsonl \
  --class_weights auto \
  --upsample_minority
```

---
