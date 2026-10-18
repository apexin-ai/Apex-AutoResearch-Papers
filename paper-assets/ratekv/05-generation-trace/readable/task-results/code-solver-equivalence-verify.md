# code solver equivalence verify

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_solver_equivalence_verify_20260516T084502_result.json`
- **Structured JSON:** [`7593877243c6d78f7396.json`](../../sessions/75/7593877243c6d78f7396.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入并验证通过。`--skip-ppl` 快速检查结果：

**Llama-3.1-8B (k=2)**: PERFECT MATCH — 256/256 heads 完全一致，distortion Δ=0.00000000

**Mistral-7B-v0.3 (k=2)**: 255/256 match，1 head tie-break（head 31,7: greedy=8bit, mckp=4bit），但 distortion Δ=0.00000000（该 head 在 4-bit 和 8-bit 下 distortion 都是 0.0，属于无代价 tie-break）

## 脚本结构

```
run_solver_equivalence_verify.py
├── solve_greedy_constrained()    — 带 cardinality constraint 的 greedy downgrade
├── compare_allocations()         — 逐 head bit-width 对比
├── load_llama_profiles()         — 合并 hires 2-bit + standard 4/8-bit
├── load_mistral_profiles()       — 直接加载 hires 2/4/8-bit
├── run_verification()            — 单模型完整流程（solver + 可选 PPL eval）
└── main()                        — argparse 入口，支持 --skip-ppl / --models / --max_2bit
```

**运行命令**（GPU 可用时）：
```bash
python run_solver_equivalence_verify.py  # 完整版含 PPL eval，~60min
python run_solver_equivalence_verify.py --models llama --skip-ppl  # 单模型快速
```

---
