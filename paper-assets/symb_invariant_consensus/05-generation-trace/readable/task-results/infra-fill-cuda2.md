# infra fill cuda2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fill-cuda2_20260522T233023_result.json`
- **Structured JSON:** [`8ed176ec8a1899c4db85.json`](../../sessions/8e/8ed176ec8a1899c4db85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 全部通过。

**产出汇总：**

| 项目 | 状态 |
|------|------|
| **cuda:2 状态** | 已清理旧 Mistral vLLM 残留，空闲→重新部署 |
| **选择的实验** | Qwen2.5-14B PW seed789（优先级 1，无已有结果） |
| **vLLM** | 已启动，PID 711315，port 8007，`--enforce-eager` + `VLLM_USE_FLASHINFER_SAMPLER=0`（Blackwell GPU 需要） |
| **脚本路径** | `/root/symb_invariant_consensus/scripts/run_qwen25_pw_seed789_cuda2.sh` |
| **Dry-run** | vLLM 端点可达、`run_full_mvp` 可导入、数据文件存在 |

**启动命令**（供 Agent 用 `submit_training_job` 提交）：
```
command: bash /root/symb_invariant_consensus/scripts/run_qwen25_pw_seed789_cuda2.sh
server: westd-16639
gpu: cuda:2
```

**注意**：首次启动失败是因为 Blackwell GPU (sm_120) 不被 FlashInfer 支持，通过参照 cuda:0 的启动参数（`VLLM_USE_FLASHINFER_SAMPLER=0` + `--enforce-eager`）解决。

---
