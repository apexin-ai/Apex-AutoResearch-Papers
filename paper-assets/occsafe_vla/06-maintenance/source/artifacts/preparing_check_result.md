# PREPARING 实验状态检查报告

**检查时间**: 2026-05-29 ~11:50 UTC

## 汇总

| exp_id | server | PID | alive? | current_step | gpu_util |
|--------|--------|-----|--------|-------------|----------|
| full_occ_bn_eval_v2_s0 | westd-10894 | 67153 | DEAD | 0 (未启动) | N/A |
| full_occ_bn_lambda001_v2_s0 | westd-10894 | 67303 | DEAD | 0 (未启动) | N/A |
| full_occ_bn_lambda01_v2_s0 | westd-10894 | 67647 | DEAD | 0 (未启动) | N/A |
| full_occ_bn_v2_s4 | westd-34685 | 41373 | DEAD | 0 (未启动) | N/A |
| vanilla_v2_s3 | westd-34685 | 41522 | DEAD | 0 (未启动) | N/A |
| detach_bn_v2_s3 | westd-34685 | 41737 | DEAD | 0 (未启动) | N/A |

## 根因

**所有 6 个实验同一根因：`RuntimeError: No CUDA GPUs are available`**

错误链：
1. `cuInit: CUDA_ERROR_NO_DEVICE: no CUDA-capable device is detected`
2. `finetune.py:871` → `torch.cuda.set_device(device_id)` → `RuntimeError: No CUDA GPUs are available`
3. 崩溃时间：westd-10894 在 11:40:28-36，westd-34685 在 11:40:40-46

## GPU 可见性问题

两台服务器 nvidia-smi 当前均只报告 **1 张 GPU (index 0)**：

- westd-10894: GPU 0, 80% util, 62203/97887 MiB
- westd-34685: GPU 0, 99% util, 63949/97887 MiB

实验被分配到 cuda:1/2/3，但这些 GPU 对进程不可见，导致启动即崩溃。

可能原因：
- `CUDA_VISIBLE_DEVICES` 环境变量限制了可见 GPU
- GPU 1-3 掉线/故障
- 容器/cgroup 限制只暴露了 GPU 0

## 建议

| exp_id | 建议 |
|--------|------|
| 全部 6 个 | 标记 FAILED，原因 = `CUDA_ERROR_NO_DEVICE` |

后续行动：
1. 用 `ssh_execute` 检查 `nvidia-smi -L` 列出所有物理 GPU
2. 检查 `CUDA_VISIBLE_DEVICES` 环境变量和容器 cgroup GPU 分配
3. 确认 GPU 1-3 可用后重新提交全部 6 个实验
