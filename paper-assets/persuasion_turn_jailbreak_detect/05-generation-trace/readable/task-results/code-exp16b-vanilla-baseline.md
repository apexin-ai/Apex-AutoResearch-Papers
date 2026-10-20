# code exp16b vanilla baseline

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16b-vanilla-baseline_20260520T003800_result.json`
- **Structured JSON:** [`c0e665ec5cb02be0d219.json`](../../sessions/c0/c0e665ec5cb02be0d219.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练和评估完成。

```
训练: val_loss=0.4227, val_acc=0.8243 (epoch 19/20)

eval (vanilla baseline vs MLM DAPT):
                      Vanilla    MLM
  llama_only_test F1: 0.8556    (对比 MLM 的值)
  mixed_test F1:      0.6491
  dd_ood F1:          0.4570
  aa_ood F1:          0.7920    (MLM: 0.8152)
  toxicchat F1:       0.2092
```

MLM DAPT 在 aa_ood 上 0.8152 vs vanilla 0.7920，增量 +0.023。其他 benchmark 的 MLM 值需要对比 `exp16b_llama_mlm_results.json`，要我拉出来做完整对比表吗？

---
