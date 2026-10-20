# code 7b scale prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_7b_scale_prep_20260516T075022_result.json`
- **Structured JSON:** [`b37d202b0690446bf042.json`](../../sessions/b3/b37d202b0690446bf042.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## 修改结果

**修改的文件：**
- `/root/contamcal-irt-calibration/exp001/train_sft.py` — 添加 `--gradient-checkpointing` CLI 参数，传递给 SFTConfig（含 `use_reentrant=False`），记录到 train_config.json

**新建文件：**
- `exp001/configs/qwen25_7b.yaml` — 7B 训练参数配置
- `exp001/configs/run_7b_example.sh` — 启动命令示例

**显存估算（A100-80G, Qwen2.5-7B LoRA + GC）：**
- 模型权重 (bf16): ~14GB
- LoRA params + optimizer: ~0.5GB
- Activations (batch=2, seq=2048, with GC): ~8-10GB
- **总计: ~25GB** — A100-80G 余量充足

**DeepSpeed：** 已安装 (0.18.9)，但单卡 25GB 用量无需启用。保留备用。

**evaluate.py：** 已用 `device_map="auto"`，7B inference (~14GB) 无需修改。

**向后兼容：** `--gradient-checkpointing` 默认 False，0.5B/1.5B/3B 训练行为不变。

**未解决：**
- A100 机器尚未到位，无法实际运行验证
- 7B 模型需预先下载到 HF cache（约 14GB）

---
