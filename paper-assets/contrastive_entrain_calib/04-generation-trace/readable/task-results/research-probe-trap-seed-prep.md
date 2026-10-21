# research probe trap seed prep

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_probe-trap-seed-prep_20260524T125455_result.json`
- **Structured JSON:** [`5e27805401b42f245c97.json`](../../sessions/5e/5e27805401b42f245c97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。汇总：

## 关键发现

1. **脚本不在服务器上** — `run_exp008v3_binary_probe_grpo.py` 和 `probe_module.py` 只存在于本地 artifacts，需要上传到 westd-29046 的 `/root/contrastive_entrain_calib/training/`

2. **所有依赖数据就绪** — Qwen3-8B (16GB), 训练数据 (362条), NLI 模型, activations.pt, directions.pt 均在位

3. **单 GPU 完全可行** — RTX PRO 6000 Blackwell (98GB) 远超所需 (~30-40GB peak)。无需 DeepSpeed，用 `CUDA_VISIBLE_DEVICES=0` 即可

4. **需要修改**:
   - SEED 从硬编码常量改为 argparse 参数
   - 添加 `--max_steps` (默认 2000) 和 `--output_dir` 参数
   - save_steps=500 已满足需求 (产出 4 个 checkpoint)

5. **时间预估**: ~20-25 小时/seed, 3 seed 串行 ~60-75 小时。可以用两张卡并行跑 2 个 seed 加速

6. **原始配置**: GRPO with R1=0.25 (binary probe 0/1) + R3=0.75 (NLI), LoRA r=64/alpha=64 (4 modules), effective bs=16, num_generations=2

报告已写入 `artifacts/exp008v3_multiseed_prep.md`。下一步是修改脚本并上传——需要我继续执行吗？

---
