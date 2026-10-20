# code 72b fs save and fewnerd pipeline

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_72b-fs-save-and-fewnerd-pipeline_20260519T231301_result.json`
- **Structured JSON:** [`6ede8434e097c591f91f.json`](../../sessions/6e/6ede8434e097c591f91f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果汇总：

---

### 任务 1: 本地 JSON ✅
`artifacts/72b_fewshot_signal_summary.json` 已写入。

### 任务 2: FewNERD FS 推理进度
- **进度: 97% (291504/301184)**，已运行 6h09m，预计 **~12 分钟后完成**
- 完成后需要跑 compute_signals → bootstrap → format_for_scaling pipeline

### 任务 3: 72B FS Scaling Curve DATA dict

```python
    # ── Qwen3-72B FS ──
    (72, "fs", "SciERC")          : {"lp_rho": 0.06, "sj_rho": 0.293, "vc_rho": 0.258, "degen": 16.6, "construction_lp_delta": -0.08, "greedy_f1": 0.461, "oracle_f1": 0.604},
    (72, "fs", "CoNLL")           : {"lp_rho": 0.106, "sj_rho": 0.442, "vc_rho": 0.426, "degen": 70.0, "construction_lp_delta": 0.03, "greedy_f1": 0.745, "oracle_f1": 0.796},
```

### 任务 4: 7B 训练进度
| 数据集 | 进度 | Step | Loss | ETA |
|--------|------|------|------|-----|
| **FewNERD** | **80.4%** (16550/20590) | epoch 4.02 | 0.0078 | **~2h52m** |
| **WNUT17** | **100%** ✅ (535/535) | epoch 5.0 | 0.028 | 完成 (18m02s) |

GPU 利用率: 72%, 66%, 78%, 91% (4 GPU 全活跃)。

---
