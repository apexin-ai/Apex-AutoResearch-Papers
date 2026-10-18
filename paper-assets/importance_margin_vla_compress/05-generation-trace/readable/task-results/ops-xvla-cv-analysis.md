# ops xvla cv analysis

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_xvla-cv-analysis_20260520T094958_result.json`
- **Structured JSON:** [`2b2ab73fb9bb30ad8b90.json`](../../sessions/2b/2b2ab73fb9bb30ad8b90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
X-VLA CV 数据: 无（脚本未计算 CV）
  分析内容: attention entropy ratio + pruning curve，无 L2 norm / CV 指标
  可从 entropy 数据计算 CV:
    overall entropy CV = std/mean = 0.1159/0.6138 = 0.189
    per-layer entropy CV (std/mean):
      L0:  0.0079/0.4569 = 0.017
      L1:  0.0167/0.3381 = 0.049
      L2:  0.0166/0.3838 = 0.043
      ...
      L22: 0.0211/0.7933 = 0.027
      L23: 0.0200/0.7125 = 0.028

π0 CV 参考: 无对应数据（服务器上只有 π0 evaluation baseline，无 importance analysis）
  D104 提到的 π0 CV=0.038 可能是 L2 norm 基础的 CV，与此处 entropy-based CV 不可直接对比

分析文件列表:
  /root/autodl-tmp/importance_margin_vla_compress/eval_results/xvla_attention_entropy_perlayer.json
  /root/autodl-tmp/importance_margin_vla_compress/analyze_xvla_token_importance.py

注意: 若需与 π0 CV=0.038 对比，需额外跑 L2 norm analysis（对 vision token hidden states 计算 per-token L2 norm 的 CV），当前 entropy-based 指标衡量的是 attention 分布均匀度，不是 token representation 的变异系数。
```

---
