# GPU 状态检查 — westb-29275

**时间**: 2026-05-22 08:33 UTC

## GPU 显存占用

| GPU | 型号 | 显存占用 | 总显存 | 利用率 | 进程 |
|-----|------|---------|--------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 89,059 MiB | 97,887 MiB (91%) | 0% | VLLM::Worker_TP0 (PID 122321) |
| 1 | RTX PRO 6000 Blackwell | 89,059 MiB | 97,887 MiB (91%) | 0% | VLLM::Worker_TP1 (PID 122322) |
| 2 | RTX PRO 6000 Blackwell | 88,143 MiB | 97,887 MiB (90%) | 0% | VLLM::Worker_TP0 (PID 169402) |
| 3 | RTX PRO 6000 Blackwell | 88,143 MiB | 97,887 MiB (90%) | 0% | VLLM::Worker_TP1 (PID 169403) |

## vLLM 进程

| 模型 | GPU | 端口 | 主PID | TP | max-model-len | 启动时间 |
|------|-----|------|-------|----|---------------|---------|
| Qwen3-32B (`/root/autodl-tmp/models/Qwen3-32B/`) | 0,1 | 8000 | 121781 | 2 | 8192 | May21 |
| Llama-3.3-70B-Instruct (`/root/autodl-tmp/models/LLM-Research/Llama-3.3-70B-Instruct`) | 2,3 | 8003 | 168588 | 2 | 8192 | May21 |

两个 vLLM 实例均从 May 21 运行至今，GPU 利用率均为 0%（空闲，无推理请求）。

## 其他进程

- JupyterLab (PID 1233) — 系统自带，无 GPU 占用
- TensorBoard (PID 1235, port 6007) — 系统自带，无 GPU 占用
- 无其他训练进程

## 结论

**4 张 GPU 全部可释放。** 两个 vLLM 实例占满全部显存但 GPU 利用率为 0%，处于空闲状态。当前无实验依赖这些服务，kill 掉即可释放全部 4×98GB 显存。

关闭命令：
```bash
kill 121781 168588
```
