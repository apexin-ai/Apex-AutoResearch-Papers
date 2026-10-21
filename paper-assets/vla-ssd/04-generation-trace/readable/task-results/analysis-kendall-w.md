# analysis kendall w

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kendall_w_20260519T154932_result.json`
- **Structured JSON:** [`896348508a3f16f47987.json`](../../sessions/89/896348508a3f16f47987.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。

**Cross-Layer Kendall's W = 0.7186** (χ²=68.99, df=32, p=0.000168)

三个训练条件对层级 action R² 排名高度一致（W>0.7, p<0.001）。早期-中期层（L2-L9）普遍排名高，晚期层（L28-L31）排名低。

**Cross-Task at L0: W = 1.0**（平凡结果——L0 所有条件共享相同 SigLIP 视觉特征）。

**数据限制**: 峰值层（trained L8, llama2base L4, untrained L0）的 per-task R² 在远程服务器上，本地日志因 SSH 8KB 截断无法恢复。需要在服务器上执行以下命令获取完整 cross-task 数据：

```python
python -c "import json; d=json.load(open('/root/autodl-tmp/vla-ssd/results/functional_validation/fulllayer_action_probe.json')); lb=json.load(open('/root/autodl-tmp/vla-ssd/results/action_probe/llama2base_action_probe.json')); print(json.dumps({'trained_L8': d['trained']['image_mean']['layer_8']['per_task_R2'], 'untrained_L0': d['untrained']['image_mean']['layer_0']['per_task_R2'], 'llama2base_L4': lb['llama2base_image_mean']['layer_4']['per_task_R2']}))"
```

---
