# code llama hires pipeline

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_hires_pipeline_20260514T021824_result.json`
- **Structured JSON:** [`e12143be27a3b254a53a.json`](../../sessions/e1/e12143be27a3b254a53a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正常运行中 (PID 171900, 2.5 分钟已过, Rl 状态)。日志缓冲未刷新但 GPU 已占用 29.5GB，模型正在加载/初始化阶段。

任务完成总结：

**已完成：**
1. 查看了 run_exp_e.py（Qwen hires 模板）和 run_llama_pipeline.py（Llama lowres 模板）
2. 验证 calibration_hires.json 可直接复用（64/64 samples 均 >= 2048 Llama tokens）
3. 创建 `/root/ratekv/run_llama_hires_pipeline.py`，融合两个模板：
   - Phase 1: HiResProfiler（带 batching, batch_size=8）对 256 heads × {2,4,8}-bit profiling
   - Phase 2: Constrained MCKP (budget=0.25, max_2bit=18, L0 excluded)
   - Phase 3: bf16 WikiText-2 eval (baseline + hires MCKP + uniform 4-bit)
   - 自动对比 lowres 结果 (llama_results.json)
   - Tee 日志到 llama_hires_pipeline.log
4. Dry-run 验证通过（imports OK, 数据格式正确）
5. 以 nohup 提交到 cuda:0 (PID 171900)
6. Registry 更新为 RUNNING

**关键参数：**
- max_2bit=18（按 Qwen 8/112 比例缩放到 256 heads）
- calibration: 64×2048 (vs lowres 16×512)
- 全程 bf16

**预计耗时：** 256 heads × 3 bitwidths = 768 次 profiling eval，每次需 8 batch × forward pass。参考 Qwen 112 heads 耗时 65 min，Llama 256 heads 预计 ~2-3 小时。

---
