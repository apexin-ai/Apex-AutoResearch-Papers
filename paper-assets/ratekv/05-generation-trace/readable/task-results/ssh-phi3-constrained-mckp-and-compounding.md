# ssh phi3 constrained mckp and compounding

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_phi3_constrained_mckp_and_compounding_20260516T021003_result.json`
- **Structured JSON:** [`0bfd32c9bbf872e2da6a.json`](../../sessions/0b/0bfd32c9bbf872e2da6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正在运行。模型已加载，solver 分配完成，正在评估 WikiText-2 PPL。

关键中间结果：
- **Constrained MCKP**: 388×4bit + 8×2bit + 4×8bit (mem=0.25)
- **Unconstrained MCKP**: 301×4bit + 66×2bit + 33×8bit (mem=0.25)
- **Greedy**: 与 Unconstrained 完全一致
- **Uniform-4bit**: 400×4bit (mem=0.25)
- Constrained 总 distortion (2.47) 比 Uniform (2.61) 低 5.2%，说明非均匀分配在 Spread 模式下仍有收益

token 长度警告是 Phi-3 的 131072 context window 限制，WikiText-2 eval 不受影响（每段 2048 tokens）。

实验预计运行 ~30-40 分钟（14B 模型 5 次 PPL eval）。constrained MCKP 完成后再提交 compounding sweep（共享 cuda:1）。

需要我等进程完成后自动提交 compounding sweep 吗？

---
