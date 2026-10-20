# ssh prepare 14b inference v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare-14b-inference-v2_20260520T070610_result.json`
- **Structured JSON:** [`590a5747271ab4071eda.json`](../../sessions/59/590a5747271ab4071eda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入并验证。汇总：

---

## 写入的文件

| 文件 | 路径 |
|------|------|
| Export 配置 | `/root/autodl-tmp/struct_self_consist_ie/export_config_qwen25_14b_fewnerd.yaml` |
| Inference 脚本 | `/root/autodl-tmp/struct_self_consist_ie/run_14b_fewnerd_inference.sh` |

## 14B Adapter 路径
`/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-14b-fewnerd-qlora-s42/` (4.7GB)

## 磁盘空间
- `/root/autodl-tmp/`: **183GB 可用** (350G 总 / 168G 已用 / 48%)
- checkpoints 目录: 86GB
- 14B merged 需 ~28GB → **空间充足**

## 14B 训练进度
- **31973 / 41180** = **77.6%**，epoch 3.88/5.0
- 速度: ~2.2s/step
- 剩余: 9207 steps × 2.2s ≈ **5.6 小时** (日志显示 ETA ~5:25)
- loss=0.0138, grad_norm=0.30
- 预计完成时间: 约 **今天 ~凌晨 4:30** (基于当前 23:00 + 5.5h)

## Inference 预估耗时
7B 参考: FewNERD 37648 instances × N=8, 单卡 vLLM。14B 模型吞吐约为 7B 的 40-50%，预估单 seed 约 **3-5 小时**（取决于 5090 显存带宽）。3 seeds 并行在 2-3 张卡上可 5 小时内全部完成。

## Post-Completion Checklist

```
1. Export:
   source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
   cd /root/autodl-tmp/struct_self_consist_ie
   llamafactory-cli export export_config_qwen25_14b_fewnerd.yaml

2. 验证 merged 模型:
   du -sh checkpoints/qwen25-14b-fewnerd-merged/  # 预期 ~28GB

3. SCP merged 模型到 5090-b:
   scp -r checkpoints/qwen25-14b-fewnerd-merged/ autodl-5090-b:/root/autodl-tmp/struct_self_consist_ie/checkpoints/

4. 启动 inference (5090-b):
   GPU 0: nohup bash run_14b_fewnerd_inference.sh 42 0 &
   GPU 1: nohup bash run_14b_fewnerd_inference.sh 123 1 &
   GPU 2: nohup bash run_14b_fewnerd_inference.sh 456 2 &  (可选)

5. 监控: tail -f logs/14b_fewnerd_seed*.log
```

---
