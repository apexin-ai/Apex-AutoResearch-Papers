# code exp20 deepcontext proxy

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp20-deepcontext-proxy_20260520T133408_result.json`
- **Structured JSON:** [`26db6a624658707e1fe2.json`](../../sessions/26/26db6a624658707e1fe2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练完成。结果如下：

```
exp20 DeepContext Proxy (BERT-base + BiGRU) Results:

BERT-base (no DAPT):
  seed42:  IID=1.000  DD_OOD=0.285  AA_OOD=0.244
  seed123: IID=0.987  DD_OOD=0.310  AA_OOD=0.271
  seed456: IID=1.000  DD_OOD=0.360  AA_OOD=0.310
  mean:    IID=0.996±0.006  DD_OOD=0.318±0.031  AA_OOD=0.275±0.027

对比 DeBERTa-v3 (exp1):
  BERT-base (no DAPT):    IID=0.996±0.006  DD_OOD=0.318±0.031  AA_OOD=0.275±0.027
  DeBERTa vanilla:        IID=1.000±0.000  DD_OOD=0.312±0.043  AA_OOD=???
  DeBERTa 9-class:        IID=1.000±0.000  DD_OOD=0.994±0.005  AA_OOD=0.939±0.047
```

关键发现：
- BERT-base vanilla（DD_OOD=0.318）与 DeBERTa vanilla（DD_OOD=0.312）OOD 性能几乎相同，说明 **encoder 选择本身对 OOD 性能影响极小**
- DeBERTa 9-class 相比两个 vanilla baseline 有巨大提升（DD_OOD: 0.31→0.99, AA_OOD: 0.27→0.94），进一步确认 **DAPT（而非 encoder capacity）是驱动 OOD 泛化的核心因素**
- Checkpoints 保存在 `checkpoints/exp20_bert_base_seed{42,123,456}/best.pt`

---
