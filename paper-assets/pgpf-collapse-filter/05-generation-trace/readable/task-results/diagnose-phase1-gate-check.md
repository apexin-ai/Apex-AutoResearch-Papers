# diagnose phase1 gate check

**pgpf collapse filter** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase1_gate_check_20260513T152420_result.json`
- **Structured JSON:** [`30260ce25ec373b9e546.json`](../../sessions/30/30260ce25ec373b9e546.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

| 项目 | 状态 |
|------|------|
| **进程** | 无相关进程运行 |
| **tmux** | 无 session |
| **GPU** | 2x NVIDIA RTX PRO 6000 Blackwell (98GB each)，0% 利用率，完全空闲 |
| **phase1 输出** | `outputs/phase1/no_filter/` 和 `outputs/phase1/random/` 目录已创建但**全部为空** |
| **phase0 输出** | 正常完成（有 checkpoint、summary.json、correlation_matrix.json） |

### 崩溃原因

日志末尾是明确的 traceback，**实验状态：crashed**。

**根因**：加载 embedding 模型 `dunzhang/stella_en_1.5B_v5` 失败。

```
OSError: dunzhang/stella_en_1.5B_v5 does not appear to have a file named 
pytorch_model.bin, model.safetensors, tf_model.h5, model.ckpt or flax_model.msgpack.
```

调用链：`recursive_loop.run()` → `scorer.set_reference_corpus()` → `SentenceTransformer("dunzhang/stella_en_1.5B_v5")` → `from_pretrained()` 失败。

这说明模型没有被正确下载到本地缓存，或者 AutoDL 网络限制导致 HuggingFace 下载失败（典型的 AutoDL 问题——需要 `source /etc/network_turbo` + 设置 `HF_HOME` 到数据盘）。phase1 在创建输出目录后、实际开始训练前就崩溃了。

---
