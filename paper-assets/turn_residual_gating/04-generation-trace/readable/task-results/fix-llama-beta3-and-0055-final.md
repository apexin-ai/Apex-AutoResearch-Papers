# fix llama beta3 and 0055 final

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_llama_beta3_and_0055_final_20260525T212557_result.json`
- **Structured JSON:** [`f56d10d2cbb49e4b1bcc.json`](../../sessions/f5/f56d10d2cbb49e4b1bcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done.

## Llama SS β=3
- **服务器搜索结果**：找到 β=3 eval 数据，来源文件 `/root/turn_residual_gating/results/llama_ss_eval/llama_ss_ar_n50.json`
  - β=0: GAR=0.1662, PPL=1.372
  - β=3: GAR=0.1726 (→ 论文四舍五入 0.173 ✓), PPL=1.502
  - β=5: GAR=0.7905, PPL=1.807
- **处理方式**：补注册到 `p1_llama_ss_eval` registry，新增 `ss_ar_b3_gar=0.1726` 和 `ss_ar_b3_ppl=1.5`
- **论文数字正确**，无需修改 `analysis.tex`/`appendix.tex`

## 0.055 验证
- `grep "0.055"` 搜索三个目录（`paper/`, `docs/paper/`, `artifacts/_project/paper/`）：**全部 0 hits**
- `grep "9.1×"` 搜索同三个目录：**全部 0 hits**
- 0.055 和 9.1× 已完全清除

---
