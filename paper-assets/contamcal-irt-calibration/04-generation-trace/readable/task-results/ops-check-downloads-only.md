# ops check downloads only

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-downloads-only_20260518T102005_result.json`
- **Structured JSON:** [`52e6b448f0068f1615af.json`](../../sessions/52/52e6b448f0068f1615af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

输出被截断了，中间部分丢失。以下是收到的完整输出：

```
=== 14B INCOMPLETE ===
/root/autodl-tmp/models/Qwen2.5-14B/.cache/huggingface/download/0h2PhEN4wf4qC6Njm74VvfC6t1E=.e7efa1adc8257218813dcb494bb2a3d5775fa268735ab39e5b8119e233c21462.incomplete
/root/autodl-tmp/models/Qwen2.5-14B/.cache/huggingface/download/EHpm-K7rdV4CgBWL-uyhsBxgY_o=.68127c9bc4fab170f7aaf63d5c7ac9e182afd10b74a1c6bb8025afefc11447cb.incomplete
/root/autodl-tmp/models/Qwen2.5-14B/.cache/huggingface/download/6g1A1Sffu6ppCoytuuyE76A1WOI=.c2754167c1cbaf94b9af9c7eb646a2286a596f9ded5e2e3c4c5e6a4464352c9e.incomplete
COUNT: 3
=== 14B SAFETENSORS ===
5
26G	/root/autodl-tmp/models/Qwen2.5-14B/
=== GEMMA INCOMPLETE ===
/root/autodl-tmp/models/gemma-2-9b/.cache/huggingface/download/0h2PhEN4wf4qC6Njm74VvfC6t1E=.73b2e0b94e18b25a2f7a3abda70ab350053be6c615599cb3772f27efb2ae21eb.incomplete
/root/autodl-tmp/models/gemma-2-9b/.cache/huggingface/download/aESknW7TOKEmfryZ2OONv6DRGfk=.25d2f65b06a3ffc288fc1653554fa33b9d913f47f9b797be7785db19d3ed1f08.incomplete
/root/autodl-tmp/models/gemma-2-9b/.cache/huggingface/download/EHpm-K7rdV4CgBWL-uyhsBxgY_o=.95310f8181c07b98a18facfbbbdaa7bcf28aafaddb9c33cd9dfa008706206970.incomplete
/root/autodl-tmp/models/gemma-2-9b/.cache/huggingface/download/bUZ-Wph4eKxfWpbgEc4sIyI6tC8=.f4aa5f7d5510456fba5eb22421432a65487b1d0864fbd59ca6f8dfac65184d32.incomplete
COUNT: 4
=== GEMMA SAFETENSORS ===
4
23G	/root/autodl-tmp/models/gemma-2-9b/
=== PHI-4 STATUS ===
1.6G	/root/autodl-tmp/models/phi-4/
6
=== OLMO-2 STATUS ===
13G	/root/autodl-tmp/models/OLMo-2-1124-7B/
5
=== NVIDIA-SMI ===
Mon May 18 18:20:35 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:16:00.0 Off |                  Off |
| N/A   69C    P0            448W /  600W |   63281MiB /  97887MiB |     96%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |
| N/A   28C    P8             33W /  600W |       0MiB /  97887MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |
| N/A   28C    P8             33W /  600W |       0MiB /  97887MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:D8:00.0 Off |                  Off |
| N/A   34C    P0            198W /  600W |       0MiB /  97887MiB |    100%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            17819      C   python                               63268MiB |
+-----------------------------------------+------------------------+----------------------+
```

**(中间 nvidia-smi 进程表到 7B PILOT PID 之间的输出被截断，约 10736 字符丢失——主要是 PID 17819 的 torch inductor compile worker 子进程列表)**

```
=== 7B PILOT PID ===
```
（PID 17819 的 ps aux 匹配行在截断区域内，但从 nvidia-smi 可见 PID 17819 在 GPU 0 上运行，占用 63268MiB）

可见的 compile worker 子进程（截断尾部保留的部分）：
```
root 18244 ... torch._inductor.compile_worker.__main__.py --parent=17819 --workers=32
root 18246 ... torch._inductor.compile_worker.__main__.py --parent=17819 --workers=32
root 18248 ... torch._inductor.compile_worker.__main__.py --parent=17819 --workers=32
root 18250 ... torch._inductor.compile_worker.__main__.py --parent=17819 --workers=32
root 18252 ... torch._inductor.compile_worker.__main__.py --parent=17819 --workers=32
root 18254 ... torch._inductor.compile_worker.__main__.py --parent=17819 --workers=32
```

```
=== DOWNLOAD PROCESSES ===
root  5060  0.0  0.0   4364  3060 ?  S  14:58  0:00 bash /root/autodl-tmp/models/download_all.sh
root  5063  0.0  0.0   4364   236 ?  S  14:58  0:00 bash /root/autodl-tmp/models/download_all.sh
root  5066  1.7  0.0 722528 329564 ? Sl 14:58  3:36 /root/miniconda3/bin/python /root/miniconda3/bin/hf download Qwen/Qwen2.5-14B --local-dir /root/autodl-tmp/models/Qwen2.5-14B
root  6378  0.0  0.0   4172  2348 ?  Ss 15:10  0:00 SCREEN -dmS dl_gemma bash -c export PATH=/root/miniconda3/bin:$PATH && export HF_ENDPOINT=https://hf-mirror.com && export HF_HUB_ENABLE_HF_TRANSFER=0 && export HF_HUB_DISABLE_XET=1 && export HF_TOKEN=[REDACTED_HF_TOKEN] && hf download google/gemma-2-9b --local-dir /root/autodl-tmp/models/gemma-2-9b --token $HF_TOKEN 2>&1 | tee /tmp/dl_gemma.log; echo "GEMMA_DONE" >> /tmp/dl_gemma.log
root  6379  0.0  0.0   4364  3160 pts/0 Ss+ 15:10  0:00 bash -c export PATH=...
root  6380  2.0  0.0 732720 380024 pts/0 Sl+ 15:10  3:48 /root/miniconda3/bin/python /root/miniconda3/bin/hf download google/gemma-2-9b --local-dir /root/autodl-tmp/models/gemma-2-9b --token [REDACTED_HF_TOKEN]
```

---
