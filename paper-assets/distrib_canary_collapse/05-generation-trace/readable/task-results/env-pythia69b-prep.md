# env pythia69b prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_env_pythia69b_prep_20260518T064729_result.json`
- **Structured JSON:** [`b537fe9a232ab3df347a.json`](../../sessions/b5/b537fe9a232ab3df347a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载 6.1GB/~14GB，运行 7 分钟，预计还需 ~8 分钟。

## D060 完成总结

**已完成:**

1. **模型下载**: 进行中 (6.1/14GB)，后台 PID 327619，路径 `/root/autodl-tmp/.hf_cache/pythia-6.9b-local/`

2. **显存预估**: 标准训练需 ~112GB → OOM (单 GPU 98GB)。方案: `gradient_checkpointing` + `adamw_bnb_8bit` → ~72GB，26GB 余量

3. **脚本修改**: `iterative_train.py` 已添加 `--gradient_checkpointing` 和 `--optim` 参数，不影响已有实验（默认值与原行为一致）

4. **4 组实验配置**: 已写入 artifact，关键参数:
   - `--gradient_checkpointing --optim adamw_bnb_8bit --gen_batch_size 4`
   - Phase 1: wiki α=1.0 s42/s43 并行
   - Phase 2: wiki α=0.75 s42 + C4 α=1.0 s42 并行

5. **训练时间预估**: ~4.5-5h/gen，~45-50h/experiment。建议先跑 1 gen 测实际速度

6. **磁盘风险**: 95GB free，6.9B checkpoint ~28GB/gen。需训练中清理旧 checkpoint

**阻塞项**: 两个 GPU 当前被 gpt2m 和 pythia-1.4b s43 占用，需等完成后启动 6.9B 实验。

产出: `artifacts/d060_pythia69b_prep.md`

---
