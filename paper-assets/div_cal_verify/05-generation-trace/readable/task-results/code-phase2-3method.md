# code phase2 3method

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2_3method_20260513T031708_result.json`
- **Structured JSON:** [`63ef8735e12a8c3f9c58.json`](../../sessions/63/63ef8735e12a8c3f9c58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 产出汇总

**1. 兼容性审查**：3 个方法均兼容 `--self_iterate`，无需修复代码。
- Contriever 始终独立加载在 CPU，rgds/external_only 的选择逻辑在生成后训练前执行，不干扰 feedback loop
- 每个方法是独立进程，student 从头加载，无状态泄漏

**2. Phase 1b 完整参数**：`gpt2, self_iterate, 8 generations, 500k tokens, 3 epochs, lr=5e-5, batch=4, grad_accum=8, seq_len=512, gpu_ids=0, seed=42`

**3. 脚本路径**：`/root/div_cal_verify/run_phase2.sh`（已 chmod +x）
- 输出目录：`/root/autodl-tmp/div_cal_verify/results_phase2/{uncurated,rgds,external_only}/`
- 3 方法串行，参数与 Phase 1b 完全一致

**4. 启动命令**：
```bash
nohup bash /root/div_cal_verify/run_phase2.sh 0 > /root/autodl-tmp/div_cal_verify/results_phase2/phase2.log 2>&1 &
```
参数 `0` 指定 GPU ID（默认为 1，按需调整）。

---
