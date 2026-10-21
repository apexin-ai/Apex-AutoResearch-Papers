## 服务器连通性检查 (2026-05-24)

### autodl-5090
- 连通性: **FAILED** — `[Errno None] Unable to connect to port 33216 on 106.38.204.136`
- 项目数据: 无法确认（连接失败）
- 备注: 可能实例已关机或端口已变更，需去 AutoDL 控制台确认

### gpu-5090-4x-3
- 连通性: **FAILED** — `[Errno None] Unable to connect to port 33216 on 106.38.204.136`
- 项目数据: 无法确认（连接失败）
- 备注: 与 autodl-5090 指向同一 IP:端口（106.38.204.136:33216），疑似同一台实例或配置错误

### westd-33183 GPU 状态 (2026-05-24)

#### cuda:0
- 型号: NVIDIA RTX PRO 6000 Black
- 显存: 0 / 97887 MiB
- 进程: 无
- 状态: **空闲**

#### 其他 GPU
- nvidia-smi 仅显示 1 张卡（cuda:0），与项目配置中"共 9 张卡"不符，可能容器或 CUDA_VISIBLE_DEVICES 限制

#### 磁盘
- /root: 26G / 30G (87%) — 仅剩 4.2G，偏紧
