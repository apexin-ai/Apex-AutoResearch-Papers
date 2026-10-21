# deploy westd27271 simplerenv

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd27271_simplerenv_20260524T172013_result.json`
- **Structured JSON:** [`aacaa25be97857a5a486.json`](../../sessions/aa/aacaa25be97857a5a486.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GPU 都在工作：
- GPU0: 31GB / 95% 利用率（2 个 Python 进程 - 之前的测试进程还没退干净）
- GPU1: 15.5GB / 69% 利用率

实验正在正常运行。

---

## 部署完成汇报

### GPU 状态
| GPU | 显存 | 利用率 | 运行内容 |
|-----|------|--------|----------|
| GPU0 | 31GB / 94GB | 95% | SimplerEnv baseline: PutCarrotOnPlate + PutSpoonOnTableCloth (48 ep each) |
| GPU1 | 15.5GB / 94GB | 69% | SimplerEnv baseline: StackGreenCubeOnYellowCube + PutEggplantInBasket (48 ep each) |

### 解决的问题（共 7 个）
1. tensorflow 缺失 → 改为可选 import
2. SAPIEN 3.x 与 ManiSkill2 evaluator 不兼容 → 新写 ManiSkill3 评估脚本
3. transformers 5.5.4 vs OpenVLA 4.40.1 → monkeypatch `_supports_sdpa` + `GenerationMixin`
4. `python` 不在 PATH → 需 `conda activate base`
5. 网络不通 → `source /etc/network_turbo` 启用代理
6. openvla-7b 模型不完整 → 通过 HF mirror 下载到 `openvla-7b-hf/`
7. simpler_env `__init__` 强制 import ManiSkill2 → 内联 `get_image` 函数
8. `generate()` 被移出 PreTrainedModel → 手动 greedy decoding 替代
9. forward() 中 `past_key_values` 断言 → 移除断言
10. 图像 batch 维度 → squeeze

### 日志位置
- GPU0: `/root/autodl-tmp/logs/simplerenv_ms3_baseline_gpu0.log`
- GPU1: `/root/autodl-tmp/logs/simplerenv_ms3_baseline_gpu1.log`

### 预计时间
测试跑 2 ep 用了 18s（含模型加载），实际推理约 8s/ep。每 task 48 ep × 2 tasks × 8s ≈ 13 分钟/GPU。

### 注意
- `submit_training_job` 工具不存在，用了 `ssh_execute` + nohup
- 结果保存到 `/root/autodl-tmp/importance_margin_vla_compress/eval_results/`

---
