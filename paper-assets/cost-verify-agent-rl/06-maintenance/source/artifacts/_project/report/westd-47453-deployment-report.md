# westd-47453 部署报告

## 服务器信息
- 主机: connect.westd.seetacloud.com:47453
- OS: Ubuntu 22.04.5 LTS
- GPU: 4× NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB each)
- Driver: 595.71.05 / CUDA 13.2 (runtime CUDA 12.8)

## 环境
- Python: 3.12.3 (miniconda3 base)
- PyTorch: 2.10.0+cu128
- vLLM: 0.18.1
- verl: 0.6.1 (editable, from /root/cost-verify-agent-rl/RAGEN/verl)
- ray: 2.55.1
- transformers: 4.57.6
- accelerate: 1.13.0
- deepspeed: 0.18.9
- peft: 0.19.0
- trl: 1.1.0
- ragen: 0.1 (editable)

## 磁盘
- 数据盘 (/root/autodl-tmp): 250GB total, 97GB free
- 根分区: 30GB total, 6.9GB free (代码/模型均在数据盘)

## 项目路径
- /root/cost-verify-agent-rl -> /root/autodl-tmp/cost-verify-agent-rl (symlink)
- 代码: /root/cost-verify-agent-rl/RAGEN/

## 注意事项
- GitHub 从该服务器不可达（已通过 bjb1 SCP 传输代码）
- 根分区空间紧张，所有大文件应写入 /root/autodl-tmp/
- setup.py 中 vllm==0.8.2 约束已过期，ragen 以 --no-deps 安装
- 如需同步代码更新：从 bjb1 scp（SSH key 已配置）

## 验证结果
- [x] 4 GPU 可见且空闲
- [x] torch.cuda 正常
- [x] import verl/vllm/ray/ragen 全部成功
- [x] 包版本与 bjb1-17606 一致
