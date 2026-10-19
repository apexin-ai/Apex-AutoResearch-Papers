# ops check step10k eval feasibility

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_step10k_eval_feasibility_20260523T021155_result.json`
- **Structured JSON:** [`8f9caf12e36f8733f154.json`](../../sessions/8f/8f9caf12e36f8733f154.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已收齐。以下是报告：

---

## Mid-point Eval GPU 共存可行性报告

### 1. 当前 GPU 显存使用

| GPU | 已用 | 总量 | 剩余 | 利用率 |
|-----|------|------|------|--------|
| 0 | 27,045 MiB | 97,887 MiB | **70,206 MiB (~68.6 GB)** | 100% |
| 1 | 27,045 MiB | 97,887 MiB | **70,206 MiB** | 100% |
| 2 | 27,045 MiB | 97,887 MiB | **70,206 MiB** | 100% |
| 3 | 27,045 MiB | 97,887 MiB | **70,206 MiB** | 100% |

每个训练进程占 ~27 GB（比预估的 19 GB 高）。

### 2. 训练进度 & 到达 10K 估算

| Session | 当前 Step | 速度 | 预计到达 10K |
|---------|-----------|------|-------------|
| s1_l005 | 5168 | 4.61 s/step | ~6.2h 后 |
| s1_l01 | 5164 | 4.62 s/step | ~6.2h 后 |
| s2_l005 | 5158 | 4.62 s/step | ~6.2h 后 |
| s2_l01 | 5152 | 4.64 s/step | ~6.2h 后 |

4 个训练进度接近，全部约 **6 小时后** 到达 step 10K。

### 3. serve_policy 能否与训练共存

**Y — 可以共存。**

- 模型权重文件 7.1 GB（bf16/fp16），加载到 GPU 约占 ~8-10 GB（含推理 buffer）
- 每张 GPU 剩余 ~68.6 GB，远超 serve_policy 需求
- `policy_config.py` 支持 `pytorch_device` 参数，可指定 `"cuda:X"` 将 serve_policy 绑定到特定 GPU
- 启动时设 `CUDA_VISIBLE_DEVICES=0` 即可限定到某张 GPU，不会干扰其他 GPU 上的训练
- GPU 利用率虽然 100%，但这只是计算利用率，显存充裕才是关键约束——共存无压力

### 4. 训练脚本 Resume 支持

**支持。** 训练脚本有 `--resume` flag（line 84），传递到训练函数（line 314）。如需暂停训练腾出 GPU 也可安全恢复，但无需这样做。

### 5. Checkpoint 目录格式

路径模式：`/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/{run_name}/{step}/`

- 命名：`a1_sdf_pi05_object_pudding_seed{1,2}_l{005,01}`
- Step 目录：`2000/`, `4000/`, `best/`
- 每个 step 目录包含：`model.safetensors`, `optimizer.pt`, `metadata.pt`, `aux_metadata.pt`, `ee_extractor.pt`, `sdf_decoder.pt`, `assets/`
- save_interval=2000 确认，下一个 checkpoint 将在 step 6000

### 结论

serve_policy 可以安全地与训练共存在同一张 GPU 上（68.6 GB 剩余 vs ~10 GB 需求）。建议通过 `CUDA_VISIBLE_DEVICES` 指定 GPU，避免默认选到 `cuda:0` 后占用多卡。

---
