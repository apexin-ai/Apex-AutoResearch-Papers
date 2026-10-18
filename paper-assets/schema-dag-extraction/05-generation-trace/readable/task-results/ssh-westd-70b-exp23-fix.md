# ssh westd 70b exp23 fix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-70b-exp23-fix_20260517T093802_result.json`
- **Structured JSON:** [`36f314c8d3924071ee77.json`](../../sessions/36/36f314c8d3924071ee77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验状态确认：

**汇报：**

1. **batch_config_exp2.json 传输** — 成功。在 westd 上直接从 similarity matrix + D051 random batches 重新生成（BCS 值验证与 cqa1 一致：count_8 low=0.4715 / high=0.9706）

2. **vLLM 服务状态** — 70B FP8 模型已加载到两张 GPU（TP=2），每张 36.7GB/97.9GB 显存占用。vLLM Worker_TP0 和 Worker_TP1 进程运行中

3. **Exp 2 和 Exp 3 已启动** — 在 tmux session `exp23_70b` 中串行运行：
   - Exp 2: `run_bcs_controlled_llama70b.py --stage all --resume`（BCS-controlled RE，count_8 + count_16，各 10 batches）
   - Exp 3: `run_d051_count_curves_llama70b.py --dataset fewnerd`（Few-NERD count curves，25 batches × 6 count levels）

4. **GPU 利用率** — 两张 GPU 已被占用（模型加载完成中），马上开始推理

5. **预计完成时间** — 基于 Exp 1（FewRel 125 batches ≈ 26min）：
   - Exp 2: ~30-40 min（含模型加载，20 batches + bootstrap analysis）
   - Exp 3: ~40-50 min（模型复用，150 batches）
   - 总计: ~1.5h，预计 19:15-19:30 UTC 完成，远在 deadline (5/18 12:00 UTC) 之前

---
