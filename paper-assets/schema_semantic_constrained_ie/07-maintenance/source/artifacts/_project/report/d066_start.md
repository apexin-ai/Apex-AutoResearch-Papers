# d066 SciERC Beam Sweep — 启动报告

**日期**: 2026-05-20 07:23 CST
**服务器**: westd-21461, GPU1

## 启动信息

| 项目 | 值 |
|------|-----|
| PID | 132459 (wrapper) / 132469 (python) |
| GPU | GPU1 (NVIDIA RTX PRO 6000 Blackwell, 98GB) |
| GPU 内存 | 18999 MiB / 97887 MiB |
| 模型 | Qwen3-8B LoRA SciERC merged (`/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged`) |
| 数据集 | SciERC test (551 docs) |
| 日志 | `/root/autodl-tmp/schema_outputs/d066_beam_sweep_scierc_gpu1.log` |

## 启动命令

```bash
cd /root/schema_semantic_constrained_ie
nohup bash scripts/d066_beam_sweep_scierc_gpu1.sh > /root/autodl-tmp/schema_outputs/d066_beam_sweep_scierc_gpu1.log 2>&1 &
```

## 脚本配置 (GPU1-only wrapper)

仅运行 Qwen3-8B 部分，避免与 GPU0 上的任务冲突。

**Beam widths**: k=1, 2, 4, 8
**Modes**: unconstrained, full_s1 (constrained)
**总计**: 8 runs (4 beam × 2 modes)

每个 run 的参数:
- `--decoding_strategy beam --num_beams {k}`
- `--max_new_tokens 2048`
- `--seed 42`
- `--skip_on_error`
- `CUDA_VISIBLE_DEVICES=1 --device cuda:0`

输出文件模式: `/root/autodl-tmp/schema_outputs/d066_beam_sweep/qwen_scierc_beam{k}_{mode}.jsonl`

## Run 顺序

1. `qwen_scierc_beam1_unconstrained`
2. `qwen_scierc_beam1_full_s1`
3. `qwen_scierc_beam2_unconstrained`
4. `qwen_scierc_beam2_full_s1`
5. `qwen_scierc_beam4_unconstrained`
6. `qwen_scierc_beam4_full_s1`
7. `qwen_scierc_beam8_unconstrained`
8. `qwen_scierc_beam8_full_s1`

每轮结束后自动运行 `violation_checker.py` 生成 violation 报告。

## GPU 分配确认

- GPU0: 空闲 (0MiB, 0%) — d064 cascade 已完成
- GPU1: d066 Qwen beam sweep (18999MiB, 87%)

## 预计完成时间

SciERC 551 docs, 8 runs。根据之前估算 ~1-1.5h 总计。
预计完成: ~08:30-09:00 CST (2026-05-20)

## 备注

- 原始 `d066_beam_sweep_scierc.sh` 同时跑 GPU0(Llama) + GPU1(Qwen)，但因 GPU0 状态不确定，创建了 `d066_beam_sweep_scierc_gpu1.sh` 仅跑 GPU1 Qwen 部分
- GPU0 的 Llama beam sweep 可在确认 GPU0 空闲后单独启动
