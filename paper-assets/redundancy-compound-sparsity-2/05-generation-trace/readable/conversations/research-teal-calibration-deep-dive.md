# research teal calibration deep dive

**redundancy compound sparsity 2** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/chats/worker_research_teal_calibration_deep_dive_20260512T081939.jsonl`
- **Structured JSON:** [`b603031111733712e5f3.json`](../../sessions/b6/b603031111733712e5f3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

67 recorded events

### Tool call

_source line 1 · 2026-05-12T08:23:06.491626+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__clone_repo,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__clone_repo,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-12T08:23:06.492018+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T08:23:06.492214+00:00_

called mcp__agent-ml-research__clone_repo

<details open><summary>🔧 Tool call — mcp__agent-ml-research__clone_repo</summary>

```json
{
  "url": "https://github.com/FasterDecoding/TEAL",
  "name": "teal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "mcp__agent-ml-research__clone_repo",
  "tool_args": {
    "url": "https://github.com/FasterDecoding/TEAL",
    "name": "teal"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-12T08:23:06.492349+00:00_

Error executing tool clone_repo: clone_repo() got an unexpected keyword argument 'name'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "mcp__agent-ml-research__clone_repo",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-12T08:23:06.492496+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "git clone https://github.com/FasterDecoding/TEAL /tmp/teal_repo 2>&1",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "tool_args": {
    "command": "git clone https://github.com/FasterDecoding/TEAL /tmp/teal_repo 2>&1",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-12T08:23:06.492630+00:00_

Cloning into '/tmp/teal_repo'...

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-12T08:23:06.492748+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/teal_repo -type f -name \"*.py\" -o -name \"*.md\" -o -name \"*.json\" -o -name \"*.yaml\" -o -name \"*.sh\" | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/teal_repo -type f -name \"*.py\" -o -name \"*.md\" -o -name \"*.json\" -o -name \"*.yaml\" -o -name \"*.sh\" | head -80"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-12T08:23:06.492878+00:00_

/tmp/teal_repo/utils/utils.py
/tmp/teal_repo/utils/eval_ppl.py
/tmp/teal_repo/utils/data.py
/tmp/teal_repo/utils/__init__.py
/tmp/teal_repo/teal/self_attn.py
/tmp/teal_repo/teal/ppl_test.py
/tmp/teal_repo/teal/model.py
/tmp/teal_repo/teal/mlp.py
/tmp/teal_repo/teal/greedyopt.py
/tmp/teal_repo/teal/grab_acts.py
/tmp/teal_repo/scripts/benchmark_gemv.py
/tmp/teal_repo/kernels/sparse_gemv.py
/tmp/teal_repo/kernels/kernel_utils.py
/tmp/teal_repo/kernels/compile_wrapper.py
/tmp/teal_repo/kernels/__init__.py
/tmp/teal_repo/gpt-fast/tp.py
/tmp/teal_repo/gpt-fast/tokenizer.py
/tmp/teal_repo/gpt-fast/setup.py
/tmp/teal_repo/gpt-fast/scripts/tp_run.sh
/tmp/teal_repo/gpt-fast/scripts/run.sh
/tmp/teal_repo/gpt-fast/scripts/prepare.sh
/tmp/teal_repo/gpt-fast/scripts/download.sh
/tmp/teal_repo/gpt-fast/scripts/download.py
/tmp/teal_repo/gpt-fast/scripts/convert_hf_checkpoint.py
/tmp/teal_repo/gpt-fast/scripts/base_run.sh
/tmp/teal_repo/gpt-fast/quantize.py
/tmp/teal_repo/gpt-fast/model.py
/tmp/teal_repo/gpt-fast/mixtral-moe/tp.py
/tmp/teal_repo/gpt-fast/mixtral-moe/scripts/download.py
/tmp/teal_repo/gpt-fast/mixtral-moe/scripts/convert_hf_checkpoint.py
/tmp/teal_repo/gpt-fast/mixtral-moe/quantize.py
/tmp/teal_repo/gpt-fast/mixtral-moe/model.py
/tmp/teal_repo/gpt-fast/mixtral-moe/generate.py
/tmp/teal_repo/gpt-fast/mixtral-moe/README.md
/tmp/teal_repo/gpt-fast/generate.py
/tmp/teal_repo/gpt-fast/eval.py
/tmp/teal_repo/gpt-fast/distribution.py
/tmp/teal_repo/gpt-fast/__init__.py
/tmp/teal_repo/gpt-fast/README.md
/tmp/teal_repo/gpt-fast/GPTQ.py
/tmp/teal_repo/gpt-fast/CONTRIBUTING.md
/tmp/teal_repo/gpt-fast/CODE_OF_CONDUCT.md
/tmp/teal_repo/__init__.py
/tmp/teal_repo/README.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-12T08:23:06.493014+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/teal/grab_acts.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/teal/grab_acts.py"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T08:23:06.493176+00:00_

1	# should get data, tokenizer, then layer by layer grab activations and save histograms + the activations themselves
2	
3	
4	
5	import argparse
6	import os
7	
8	import torch
9	import transformers
10	
11	import sys
12	
13	current_dir = os.path.dirname(os.path.abspath(__file__))
14	parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
15	sys.path.append(parent_dir)
16	sys.path.append(os.path.join(parent_dir, 'utils'))
17	
18	
19	from utils.utils import get_tokenizer, get_sparse_model
20	
21	from teal.model import LlamaSparseForCausalLM, LlamaSparseConfig
22	from teal.model import MistralSparseForCausalLM, MistralSparseConfig
23	
24	from transformers import AutoConfig, AutoModelForCausalLM
25	
26	AutoConfig.register("llama_sparse", LlamaSparseConfig)
27	AutoConfig.register("mistral_sparse", MistralSparseConfig)
28	
29	AutoModelForCausalLM.register(LlamaSparseConfig, LlamaSparseForCausalLM)
30	AutoModelForCausalLM.register(MistralSparseConfig, MistralSparseForCausalLM)
31	
32	parser = argparse.ArgumentParser(description="Parse command line arguments for the script.")
33	parser.add_argument('--model_name', type=str, default="meta-llama/Llama-2-7b-hf",help='Name of the model to use')
34	parser.add_argument('--output_path', type=str, required=True,help='Path to the output') # contains 1. model itself, 2. histograms, 3. activations
35	args = parser.parse_args()
36	
37	tokenizer = get_tokenizer(args.model_name)
38	model = get_sparse_model(args.model_name, device="auto", histogram_path=os.path.join(args.output_path, "histograms"), grab_acts=True)
39	
40	from utils.data import get_dataset
41	from tqdm import tqdm
42	import gc
43	
44	# build histograms
45	dataset = get_dataset(
46	    "tatsu-lab/alpaca",
47	    subset=None,
48	    split="train",
49	    size=300
50	)
51	text = ""
52	for sample in tqdm(dataset):
53	    text += sample["text"] + "\n\n"
54	
55	print(len(text))
56	bsz, seq_len = 10, 2048
57	
58	encodings = tokenizer(text, truncation=True, return_tensors
…[truncated 1510 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-12T08:23:06.493323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/teal/greedyopt.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/teal/greedyopt.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T08:23:06.493522+00:00_

1	
2	import os
3	import sys
4	import argparse
5	import torch
6	import csv
7	from copy import deepcopy
8	
9	
10	current_dir = os.path.dirname(os.path.abspath(__file__))
11	parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
12	sys.path.append(parent_dir)
13	sys.path.append(os.path.join(parent_dir, 'utils'))
14	
15	from teal.model import LlamaSparseForCausalLM, LlamaSparseConfig, MistralSparseForCausalLM, MistralSparseConfig
16	from transformers import AutoConfig, AutoModelForCausalLM
17	AutoConfig.register("llama_sparse", LlamaSparseConfig)
18	AutoModelForCausalLM.register(LlamaSparseConfig, LlamaSparseForCausalLM)
19	AutoConfig.register("mistral_sparse", MistralSparseConfig)
20	AutoModelForCausalLM.register(MistralSparseConfig, MistralSparseForCausalLM)
21	from utils.utils import get_sparse_model, get_tokenizer
22	
23	import torch.cuda
24	
25	
26	weight_dict = {
27	    "Llama-3-8B": {
28	        'q': 1, 'k': 1/4, 'v': 1/4, 'o': 1,
29	        'gate': 3.5, 'up': 3.5, 'down': 3.5
30	    },
31	    "Llama-3-70B": {
32	        'q': 1, 'k': 1/8, 'v': 1/8, 'o': 1,
33	        'gate': 3.5, 'up': 3.5, 'down': 3.5
34	    },
35	    "Llama-2-7B": {
36	        'q': 1, 'k': 1/8, 'v': 1/8, 'o': 1,
37	        'gate': 2.6875, 'up': 2.6875, 'down': 2.6875
38	    },
39	    "Llama-2-13B": {
40	        'q': 1, 'k': 1/8, 'v': 1/8, 'o': 1,
41	        'gate': 2.7, 'up': 2.7, 'down': 2.7
42	    },
43	    "Llama-2-70B": {
44	        'q': 1, 'k': 1/8, 'v': 1/8, 'o': 1,
45	        'gate': 3.5, 'up': 3.5, 'down': 3.5
46	    },
47	    "Mistral-7B": {
48	        'q': 1, 'k': 1/8, 'v': 1/8, 'o': 1,
49	        'gate': 3.5, 'up': 3.5, 'down': 3.5
50	    },
51	
52	}
53	
54	def set_layer_sparsities(layer, sparsities):
55	    layer.mlp.sparse_fns['gate'].set_threshold(sparsities['gate'])
56	    layer.mlp.sparse_fns['up'].set_threshold(sparsities['up'])
57	    layer.mlp.sparse_fns['down'].set_threshold(sparsities['down'])
58	
59	    layer.self_attn.sparse_fns['q'].set_threshold(sparsities['
…[truncated 6600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-12T08:23:06.493680+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/teal/model.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/teal/model.py"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T08:23:06.493849+00:00_

1	import sys
2	import os
3	current_dir = os.path.dirname(os.path.abspath(__file__))
4	parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
5	sys.path.append(parent_dir)
6	sys.path.append(os.path.join(parent_dir, 'utils'))
7	
8	
9	
10	import torch
11	import torch.nn.functional as F
12	from torch import nn
13	
14	from transformers.models.llama.modeling_llama import (
15	    LlamaDecoderLayer,
16	    LlamaConfig,
17	    LlamaForCausalLM,
18	)
19	from transformers.models.mistral.modeling_mistral import (
20	    MistralDecoderLayer,
21	    MistralConfig,
22	    MistralForCausalLM
23	)
24	from transformers.models.llama.configuration_llama import LlamaConfig
25	
26	from teal.mlp import _monkeypatch_mlp
27	from teal.self_attn import _monkeypatch_self_attn
28	from utils.eval_ppl import eval_ppl
29	
30	from transformers.configuration_utils import PretrainedConfig
31	
32	from utils.utils import ActivationModule, get_layer_greedy_sparsities
33	
34	import types
35	
36	def _monkeypatch_layer(layer, path, grabbing_mode=False):
37	    layer.path = path
38	    layer.grabbing_mode = grabbing_mode
39	    layer.mlp = _monkeypatch_mlp(layer.mlp, f"{path}/mlp", grabbing_mode=grabbing_mode)
40	    layer.self_attn = _monkeypatch_self_attn(layer.self_attn, f"{path}/self_attn", grabbing_mode=grabbing_mode)
41	    return layer
42	
43	class SparseModelMixin:
44	    @classmethod
45	    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
46	        # Extract custom arguments
47	        histogram_path = kwargs.pop('histogram_path', None)
48	        grab_acts = kwargs.pop('grab_acts', False)
49	
50	        greedy_sparsity_path = kwargs.pop('greedy_sparsity_path', None)
51	        greedy_sparsity_level = kwargs.pop('greedy_sparsity_level', None)
52	
53	        uniform_sparsity = kwargs.pop('uniform_sparsity', None)
54	        mlp_sparsity = kwargs.pop('mlp_sparsity', None)
55	        self_attn_sparsity = kwargs.pop('self_attn_sparsity', None)
56	        app
…[truncated 5539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-12T08:23:06.493990+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/teal/mlp.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/teal/mlp.py"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-12T08:23:06.494110+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/teal/self_attn.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/teal/self_attn.py"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T08:23:06.494244+00:00_

1	import sys
2	import os
3	current_dir = os.path.dirname(os.path.abspath(__file__))
4	parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
5	sys.path.append(parent_dir)
6	sys.path.append(os.path.join(parent_dir, 'utils'))
7	
8	import types
9	from torch import nn
10	
11	from utils.utils import ActivationModule, Distribution, SparsifyFn, get_module_device
12	
13	
14	def _monkeypatch_mlp(mlp, file_path, grabbing_mode=False):
15	    mlp.forward_old = mlp.forward
16	    mlp.forward = types.MethodType(_mlp_forward, mlp)
17	
18	    mlp.file_path = file_path
19	    mlp.grabbing_mode = grabbing_mode
20	
21	    if not grabbing_mode:
22	        mlp.distrs = {}
23	        mlp.distrs['h1'] = Distribution(file_path, hidden_type='h1')
24	        mlp.distrs['h2'] = Distribution(file_path, hidden_type='h2')
25	
26	
27	        mlp.sparse_fns = nn.ModuleDict({
28	            'gate': SparsifyFn(mlp.distrs['h1']).to(get_module_device(mlp)),
29	            'up': SparsifyFn(mlp.distrs['h1']).to(get_module_device(mlp)),
30	            'down': SparsifyFn(mlp.distrs['h2']).to(get_module_device(mlp)),
31	        })
32	
33	    mlp.activation_module = ActivationModule(file_path)
34	
35	    return mlp
36	
37	def _mlp_forward(self, x, activation_module=None):
38	    if hasattr(self, 'config') and self.config.pretraining_tp > 1:
39	        # TODO: UNTESTED
40	
41	        assert 1 == 0, "Pretraining TP > 1 not implemented yet"
42	    else:
43	        if self.grabbing_mode:
44	            self.activation_module.grab_activations(x, 'h1')
45	
46	            intermediate_states = self.act_fn(self.gate_proj(x)) * self.up_proj(x)
47	            self.activation_module.grab_activations(intermediate_states, 'h2')
48	            down_proj = self.down_proj(intermediate_states)
49	        else:
50	            x_gate = self.sparse_fns['gate'](x)
51	            x_up = self.sparse_fns['up'](x)
52	
53	            intermediate_states = self.act_fn(self.gate_proj(x_gate)) * self.up_proj(x_up)
54	      
…[truncated 167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T08:23:06.494447+00:00_

1	import sys
2	import os
3	current_dir = os.path.dirname(os.path.abspath(__file__))
4	parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
5	sys.path.append(parent_dir)
6	sys.path.append(os.path.join(parent_dir, 'utils'))
7	
8	import types
9	
10	import torch
11	import torch.nn as nn
12	
13	from transformers.models.llama.modeling_llama import (
14	    apply_rotary_pos_emb,
15	)
16	
17	from utils.utils import ActivationModule, Distribution, SparsifyFn, get_module_device
18	
19	from transformers.modeling_flash_attention_utils import _flash_attention_forward
20	
21	def _monkeypatch_self_attn(self_attn, file_path, grabbing_mode=False):
22	    self_attn.forward_old = self_attn.forward
23	
24	    self_attn.forward = types.MethodType(_FA2_forward, self_attn)
25	
26	    self_attn.file_path = file_path
27	    self_attn.grabbing_mode = grabbing_mode
28	
29	    if not grabbing_mode:
30	        self_attn.distrs = {}
31	        self_attn.distrs['h1'] = Distribution(file_path, hidden_type='h1')
32	        self_attn.distrs['h2'] = Distribution(file_path, hidden_type='h2')
33	
34	        self_attn.sparse_fns = nn.ModuleDict({
35	            'q': SparsifyFn(self_attn.distrs['h1']).to(get_module_device(self_attn)),
36	            'k': SparsifyFn(self_attn.distrs['h1']).to(get_module_device(self_attn)),
37	            'v': SparsifyFn(self_attn.distrs['h1']).to(get_module_device(self_attn)),
38	            'o': SparsifyFn(self_attn.distrs['h2']).to(get_module_device(self_attn))
39	        })
40	
41	    self_attn.activation_module = ActivationModule(file_path)
42	
43	    return self_attn
44	
45	
46	def _FA2_forward(
47	    self,
48	    hidden_states: torch.Tensor,
49	    attention_mask = None, #: Optional[torch.LongTensor] = None,
50	    position_ids = None, #: Optional[torch.LongTensor] = None,
51	    past_key_value = None, #: Optional[Cache] = None,
52	    output_attentions = False, #: bool = False,
53	    use_cache = False, #: bool = False,
54	    cache_position = None, 
…[truncated 5189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-12T08:23:06.494612+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/README.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/README.md"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T08:23:06.494794+00:00_

1	# Training-Free Acivation Sparsity in Large Language Models
2	
3	[[Paper](https://www.arxiv.org/abs/2408.14690)][[Blog](https://www.together.ai/blog/teal-training-free-activation-sparsity-in-large-language-models)]
4	
5	
6	TEAL induces up to 40-50% model-wide activation sparsity in modern LLMs with minimal degradation, resulting in an up to 1.53-1.8x speedup in single-batch decoding.
7	
8	&lt;div align="center">
9	    &lt;img src="figures/clickbait.png" width="500" height="auto"/>
10	  &lt;/a>
11	&lt;/div>
12	
13	The current release supports:
14	- FP16 inference for Llama-2/3 models using uniform sparsities
15	- Accuracy evaluation for Llama-2/3 and Mistral models using uniform and block-wise greedy sparsities
16	
17	
18	## News
19	
20	- [01/2025] 🔥 TEAL is accepted to ICLR 2025 as a Spotlight!
21	- [08/2024] 🔥 Arxiv release!
22	
23	## Abstract
24	
25	Activation sparsity can enable practical inference speedups in large language models (LLMs) by reducing the compute and memory-movement required for matrix
26	multiplications during the forward pass. However, existing methods face limitations that inhibit widespread adoption. Some approaches are tailored towards
27	older models with ReLU-based sparsity, while others require extensive continued
28	pre-training on up to hundreds of billions of tokens. This paper describes TEAL
29	(**T**raining-Fre**e** **A**ctivation Sparsity in **L**LMs), a simple training-free method that
30	applies magnitude-based activation sparsity to hidden states throughout the entire
31	model. TEAL achieves 40-50% model-wide sparsity with minimal performance
32	degradation across Llama-2, Llama-3, and Mistral families, with sizes varying
33	from 7B to 70B. We improve existing sparse kernels and demonstrate wall-clock
34	decoding speed-ups of up to 1.53× and 1.8× at 40% and 50% model-wide sparsity.
35	TEAL is compatible with weight quantization, enabling further efficiency gains.
36	
37	
38	
39	## Contents
40	
41	- [Install](#Install)
42	- [Demo](#Demo)
43	
…[truncated 3784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-12T08:23:06.494972+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/utils/utils.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/utils/utils.py"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T08:23:06.495158+00:00_

1	import transformers
2	import torch
3	import torch.nn as nn
4	from transformers import AutoConfig
5	from collections import defaultdict
6	
7	import os
8	
9	class SparsifyFn(nn.Module):
10	    def __init__(self, distr, init_sparsity=None,init_threshold=None, apply_prefill=True):
11	        super(SparsifyFn, self).__init__()
12	
13	        assert init_sparsity is None or init_threshold is None, "init_sparsity and init_threshold cannot both be specified"
14	
15	        if init_sparsity is not None:
16	            thresh = distr.icdf(0.5 + init_sparsity/2)
17	        elif init_threshold is not None:
18	            thresh = init_threshold
19	        else:
20	            init_sparsity = 0
21	            thresh = 0
22	        
23	        self.register_buffer("a", torch.tensor([thresh]).to(torch.float16))
24	
25	        self.distr = distr
26	        self.apply_prefill = apply_prefill
27	
28	    def set_threshold(self, sparsity):
29	        self.threshold = self.distr.icdf(0.5 + sparsity/2).item() if sparsity != 0.0 else 0.0
30	        self.sparsity_level = sparsity
31	
32	    def forward(self, x):
33	
34	        # NOTE: we can + should change this to sparsify 99% of tokens instead of 50%
35	        # I just finished the evals for the paper at 50% before I noticed the prefill sparsification phenomenon (Section 5.4.3)
36	        if x.size(1) > 1 and self.apply_prefill:
37	            half_seq_len = x.size(1) // 2
38	            # half_seq_len = int(0.99 * x.size(1))
39	            last_context = x[:, -half_seq_len:, :]
40	            modified_context = self.apply(last_context)
41	            
42	            x = torch.cat((x[:, :-half_seq_len, :], modified_context), dim=1)
43	            return x
44	        
45	        if x.size(1) > 1 and not self.apply_prefill:
46	            return x
47	
48	        assert x.size(1) == 1, "supposedly x is decode only"
49	        return self.apply(x)
50	
51	    def apply(self, x):
52	        return x.abs().gt(self.threshold) * x
53	    
54	 
…[truncated 8442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-12T08:23:06.495634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/utils/data.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/utils/data.py"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-12T08:23:06.495876+00:00_

1	import torch
2	from datasets import load_dataset
3	from transformers import default_data_collator
4	
5	
6	def _preprocess(tokenizer, examples, max_length=128):
7	    return tokenizer(
8	        examples["text"], padding="max_length", truncation=True, max_length=max_length
9	    )
10	
11	
12	def get_dataset(dataset_name, subset, split, size=None, start=0):
13	    if size is None:
14	        dataset = load_dataset(dataset_name, subset, trust_remote_code=True)[split]
15	    else:
16	        dataset = load_dataset(dataset_name, subset, streaming=True, trust_remote_code=True)[split]
17	        dataset = dataset.skip(start).take(size)
18	
19	    return dataset
20	
21	
22	def get_dataloader(dataset, tokenizer, batch_size, num_workers=4, max_length=128):
23	    dataset = dataset.map(
24	        lambda examples: _preprocess(tokenizer, examples, max_length),
25	        batched=True,
26	        batch_size=batch_size,
27	        remove_columns=["text", "timestamp", "url"],
28	    )
29	    dataloader = torch.utils.data.DataLoader(
30	        dataset,
31	        batch_size=batch_size,
32	        num_workers=0,
33	        collate_fn=default_data_collator,
34	    )
35	    return dataloader

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-12T08:23:06.496034+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/teal_repo/models -type f | head -60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/teal_repo/models -type f | head -60"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-12T08:23:06.496161+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/teal_repo/scripts -type f | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/teal_repo/scripts -type f | head -20"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-12T08:23:06.496280+00:00_

/tmp/teal_repo/scripts/ppl_test.bash
/tmp/teal_repo/scripts/greedyopt.bash
/tmp/teal_repo/scripts/grab_acts.bash
/tmp/teal_repo/scripts/benchmark_gemv.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T08:23:06.496438+00:00_

/tmp/teal_repo/models/Mistral-7B/lookup/layer-9/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-8/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-7/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-6/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-5/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-4/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-31/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-30/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-3/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-29/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-28/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-27/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-26/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-25/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-24/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-23/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-22/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-21/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-20/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-2/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-19/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-18/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-17/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-16/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-15/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-14/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-13/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-12/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-11/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-10/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-1/results.csv
/tmp/teal_repo/models/Mistral-7B/lookup/layer-0/results.csv
/tmp/teal_repo/models/Mistral-7B/histograms/layer-9/self_a
…[truncated 1999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-12T08:23:06.496615+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/teal_repo/models -maxdepth 1 -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/teal_repo/models -maxdepth 1 -type d"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T08:23:06.496740+00:00_

/tmp/teal_repo/models
/tmp/teal_repo/models/Mistral-7B
/tmp/teal_repo/models/Llama-3-8B
/tmp/teal_repo/models/Llama-3-70B
/tmp/teal_repo/models/Llama-2-7B
/tmp/teal_repo/models/Llama-2-70B
/tmp/teal_repo/models/Llama-2-13B

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-12T08:23:06.496855+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -5 /tmp/teal_repo/models/Mistral-7B/lookup/layer-0/results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "tool_args": {
    "command": "head -5 /tmp/teal_repo/models/Mistral-7B/lookup/layer-0/results.csv"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-12T08:23:06.496972+00:00_

Effective Sparsity,Activation Error,Baseline Error,q,k,v,o,gate,up,down
0.0038461538461538464,1.5735626220703125e-05,2.086162567138672e-05,0.05,0.0,0.0,0.0,0.0,0.0,0.0
0.007692307692307693,1.5735626220703125e-05,2.7239322662353516e-05,0.1,0.0,0.0,0.0,0.0,0.0,0.0
0.01153846153846154,1.5735626220703125e-05,3.3855438232421875e-05,0.15000000000000002,0.0,0.0,0.0,0.0,0.0,0.0
0.015384615384615385,1.5795230865478516e-05,4.106760025024414e-05,0.2,0.0,0.0,0.0,0.0,0.0,0.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-12T08:23:06.497088+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport torch\nh = torch.load('/tmp/teal_repo/models/Mistral-7B/histograms/layer-0/mlp/histograms.pt', map_location='cpu', weights_only=False)\nprint('Keys:', list(h.keys()))\nfor k,v in h.items():\n    print(f'  {k}: shape={v.shape}, dtype={v.dtype}, min={v.min().item():.6f}, max={v.max().item():.6f}')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport torch\nh = torch.load('/tmp/teal_repo/models/Mistral-7B/histograms/layer-0/mlp/histograms.pt', map_location='cpu', weights_only=False)\nprint('Keys:', list(h.keys()))\nfor k,v in h.items():\n    print(f'  {k}: shape={v.shape}, dtype={v.dtype}, min={v.min().item():.6f}, max={v.max().item():.6f}')\n\""
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-12T08:23:06.497204+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 2, in &lt;module>
    import torch
ModuleNotFoundError: No module named 'torch'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-12T08:23:06.497320+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/teal/ppl_test.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/teal/ppl_test.py"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-12T08:23:06.497461+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
import torch
h = torch.load…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-12T08:23:06.497582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/scripts/grab_acts.bash"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/scripts/grab_acts.bash"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-12T08:23:06.497697+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
import torch
h = torch.load…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-12T08:23:06.497810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/scripts/greedyopt.bash"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/scripts/greedyopt.bash"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-12T08:23:06.497933+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
import torch
h = torch.load…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-12T08:23:06.498061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/scripts/grab_acts.bash"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/scripts/grab_acts.bash"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-12T08:23:06.498174+00:00_

1	# Specify output path to store activations and histograms
2	
3	
4	CUDA_VISIBLE_DEVICES=0 python teal/grab_acts.py --model_name meta-llama/Llama-2-7b-hf --output_path $OUTPUT_PATH
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-12T08:23:06.498286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/scripts/greedyopt.bash"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/scripts/greedyopt.bash"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-12T08:23:06.498395+00:00_

1	CUDA_VISIBLE_DEVICES=0 python teal/greedyopt.py --model_name meta-llama/Llama-2-7b-hf --model_type Llama-2-7B --teal_path $OUTPUT_PATH --target_sparsity 0.9 --base_step_size 0.025 --last_fraction 0.25

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-12T08:23:06.498530+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/teal/ppl_test.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/teal/ppl_test.py"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-12T08:23:06.498670+00:00_

1	import sys,os
2	# sys.path.append('../')
3	current_dir = os.path.dirname(os.path.abspath(__file__))
4	parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
5	sys.path.append(parent_dir)
6	# sys.path.append(os.path.join(parent_dir, 'utils'))
7	
8	import torch
9	from tqdm import tqdm
10	import os
11	import argparse
12	
13	
14	
15	if __name__ == "__main__":
16	    from utils.utils import get_tokenizer, get_sparse_model
17	    from utils.eval_ppl import eval_ppl
18	
19	    from teal.model import LlamaSparseForCausalLM, LlamaSparseConfig
20	    from teal.model import MistralSparseForCausalLM, MistralSparseConfig
21	
22	    from utils.data import get_dataset
23	
24	    from transformers import AutoConfig, AutoModelForCausalLM
25	
26	    AutoConfig.register("llama_sparse", LlamaSparseConfig)
27	    AutoConfig.register("mistral_sparse", MistralSparseConfig)
28	
29	    AutoModelForCausalLM.register(LlamaSparseConfig, LlamaSparseForCausalLM)
30	    AutoModelForCausalLM.register(MistralSparseConfig, MistralSparseForCausalLM)
31	
32	    parser = argparse.ArgumentParser(description="Parse command line arguments for the script.")
33	    parser.add_argument('--model_name', type=str, default="meta-llama/Llama-2-7b-hf",help='Name of the model to use')
34	    parser.add_argument('--teal_path', type=str, required=True,help='Path to the teal input')
35	    parser.add_argument('--greedy_flag', action='store_true', help='Flag for greedy')
36	    parser.add_argument('--sparsity', type=float, default=0.5, help='Sparsity level')
37	    args = parser.parse_args()
38	
39	    tokenizer = get_tokenizer(args.model_name)
40	    model = get_sparse_model(args.model_name, device="auto", histogram_path=os.path.join(args.teal_path, "histograms"))
41	
42	    dataset = get_dataset(
43	        "tatsu-lab/alpaca",
44	        subset=None,
45	        split="train",
46	        size=250
47	    )
48	
49	
50	    print("Evaluating dense PPL")
51	    print("="*40)
52	    dense_ppl = eval_ppl(model,
…[truncated 659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-12T08:23:06.498813+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/teal_repo/models/Llama-2-7B -type f | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/teal_repo/models/Llama-2-7B -type f | head -20"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-12T08:23:06.498938+00:00_

/tmp/teal_repo/models/Llama-2-7B/lookup/layer-9/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-8/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-7/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-6/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-5/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-4/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-31/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-30/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-3/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-29/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-28/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-27/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-26/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-25/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-24/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-23/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-22/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-21/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-20/results.csv
/tmp/teal_repo/models/Llama-2-7B/lookup/layer-2/results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-12T08:23:06.499056+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -5 /tmp/teal_repo/models/Llama-2-7B/lookup/layer-0/results.csv 2>/dev/null || echo \"NO_LOOKUP\"; find /tmp/teal_repo/models/Llama-2-7B -maxdepth 1 -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "tool_args": {
    "command": "head -5 /tmp/teal_repo/models/Llama-2-7B/lookup/layer-0/results.csv 2>/dev/null || echo \"NO_LOOKUP\"; find /tmp/teal_repo/models/Llama-2-7B -maxdepth 1 -type d"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-12T08:23:06.499170+00:00_

Effective Sparsity,Activation Error,Baseline Error,q,k,v,o,gate,up,down
0.004145077720207254,0.0003795623779296875,0.00067138671875,0.0,0.0,0.0,0.0,0.0,0.0,0.018604651162790697
0.008290155440414507,0.0004425048828125,0.00083160400390625,0.0,0.0,0.0,0.0,0.0,0.0,0.037209302325581395
0.012435233160621761,0.000553131103515625,0.0009307861328125,0.0,0.0,0.0,0.0,0.0,0.0,0.05581395348837209
0.016580310880829015,0.000682830810546875,0.00099945068359375,0.0,0.0,0.0,0.0,0.0,0.0,0.07441860465116279
/tmp/teal_repo/models/Llama-2-7B
/tmp/teal_repo/models/Llama-2-7B/lookup
/tmp/teal_repo/models/Llama-2-7B/histograms

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-12T08:23:06.499313+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/teal_repo/models/Llama-2-7B/histograms -maxdepth 3 -type f | head -15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/teal_repo/models/Llama-2-7B/histograms -maxdepth 3 -type f | head -15"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-12T08:23:06.499452+00:00_

/tmp/teal_repo/models/Llama-2-7B/histograms/layer-9/self_attn/histograms.pt
/tmp/teal_repo/models/Llama-2-7B/histograms/layer-9/mlp/histograms.pt
/tmp/teal_repo/models/Llama-2-7B/histograms/layer-8/self_attn/histograms.pt
/tmp/teal_repo/models/Llama-2-7B/histograms/layer-8/mlp/histograms.pt
/tmp/teal_repo/models/Llama-2-7B/histograms/layer-7/self_attn/histograms.pt
/tmp/teal_repo/models/Llama-2-7B/histograms/layer-7/mlp/histograms.pt
/tmp/teal_repo/models/Llama-2-7B/histograms/layer-6/self_attn/histograms.pt
/tmp/teal_repo/models/Llama-2-7B/histograms/layer-6/mlp/histograms.pt
/tmp/teal_repo/models/Llama-2-7B/histograms/layer-5/self_attn/histograms.pt
/tmp/teal_repo/models/Llama-2-7B/histograms/layer-5/mlp/histograms.pt
/tmp/teal_repo/models/Llama-2-7B/histograms/layer-4/self_attn/histograms.pt
/tmp/teal_repo/models/Llama-2-7B/histograms/layer-4/mlp/histograms.pt
/tmp/teal_repo/models/Llama-2-7B/histograms/layer-31/self_attn/histograms.pt
/tmp/teal_repo/models/Llama-2-7B/histograms/layer-31/mlp/histograms.pt
/tmp/teal_repo/models/Llama-2-7B/histograms/layer-30/self_attn/histograms.pt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-12T08:23:06.499576+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/gpt-fast/model.py",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/gpt-fast/model.py",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-12T08:23:06.499704+00:00_

1	# Copyright (c) Meta Platforms, Inc. and affiliates.
2	# All rights reserved.
3	
4	# This source code is licensed under the license found in the
5	# LICENSE file in the root directory of this source tree.
6	from dataclasses import dataclass
7	from typing import Optional
8	
9	import torch
10	import torch.nn as nn
11	from torch import Tensor
12	from torch.nn import functional as F
13	
14	import sys, os
15	sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # hack import parent dir
16	from kernels.sparse_gemv import SparseGEMV
17	
18	import types
19	
20	def find_multiple(n: int, k: int) -> int:
21	    if n % k == 0:
22	        return n
23	    return n + k - (n % k)
24	
25	@dataclass
26	class ModelArgs:
27	    block_size: int = 2048
28	    vocab_size: int = 32000
29	    n_layer: int = 32
30	    n_head: int = 32
31	    dim: int = 4096
32	    intermediate_size: int = None
33	    n_local_heads: int = -1
34	    head_dim: int = 64
35	    rope_base: float = 10000
36	    norm_eps: float = 1e-5
37	
38	    sparsify: bool = False
39	    hist_path: str = None
40	
41	    def __post_init__(self):
42	        if self.n_local_heads == -1:
43	            self.n_local_heads = self.n_head
44	        if self.intermediate_size is None:
45	            hidden_dim = 4 * self.dim
46	            n_hidden = int(2 * hidden_dim / 3)
47	            self.intermediate_size = find_multiple(n_hidden, 256)
48	        self.head_dim = self.dim // self.n_head
49	
50	    @classmethod

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-12T08:23:06.499862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/teal_repo/utils/eval_ppl.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/teal_repo/utils/eval_ppl.py"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-12T08:23:06.500032+00:00_

1	import sys,os
2	# sys.path.append('../')
3	current_dir = os.path.dirname(os.path.abspath(__file__))
4	parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
5	sys.path.append(parent_dir)
6	sys.path.append(os.path.join(parent_dir, 'utils'))
7	
8	from utils.data import get_dataset
9	import torch
10	from tqdm import tqdm
11	import os
12	
13	def eval_ppl(model, tokenizer, device,dataset=None, debug=False, context_size=2048, window_size=512):
14	    text = ""
15	    for sample in dataset:
16	        text += sample["text"] + "\n\n"
17	
18	    encodings = tokenizer(text, return_tensors="pt")
19	
20	    if debug:
21	        print(tokenizer.decode(encodings.input_ids[0][:100]))
22	
23	    max_length = context_size + window_size
24	    stride = window_size
25	    seq_len = encodings.input_ids.size(1)
26	    # make seq_len a multiple of stride
27	    seq_len = seq_len - (seq_len % stride)
28	
29	    if debug:
30	        print(f"seq_len: {seq_len}")
31	
32	    if debug:
33	        pbar = tqdm(range(0, seq_len, stride))
34	    else:
35	        pbar = range(0, seq_len, stride)
36	
37	    model_vocab_size = model.get_input_embeddings().weight.size(0)
38	    tokenizer_vocab_size = len(tokenizer)
39	
40	    if model_vocab_size != tokenizer_vocab_size:
41	        # resize model embeddings to fit tokenizer
42	        if model_vocab_size != tokenizer_vocab_size:
43	            print("Resize model embeddings to fit tokenizer")
44	        model.resize_token_embeddings(tokenizer_vocab_size)
45	
46	    model.eval()
47	    nlls = []
48	
49	    for begin_loc in pbar:
50	        end_loc = begin_loc + max_length
51	        input_ids = encodings.input_ids[:, begin_loc:end_loc].to(device)
52	        target_ids = input_ids.clone()
53	        target_ids[:, :-stride] = -100
54	
55	        with torch.no_grad():
56	            outputs = model(input_ids, labels=target_ids)
57	            # print(outputs.logits.shape)
58	            neg_log_likelihood = outputs.loss
59	
60	        if debu
…[truncated 395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-12T08:23:06.500197+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /tmp/teal_repo/models/Llama-3-8B -maxdepth 1 -type d && echo \"---\" && find /tmp/teal_repo/models/Llama-3-8B/histograms -maxdepth 3 -type f | head -5 && echo \"---\" && find /tmp/teal_repo/models/Llama-3-70B -maxdepth 1 -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "tool_args": {
    "command": "find /tmp/teal_repo/models/Llama-3-8B -maxdepth 1 -type d && echo \"---\" && find /tmp/teal_repo/models/Llama-3-8B/histograms -maxdepth 3 -type f | head -5 && echo \"---\" && find /tmp/teal_repo/models/Llama-3-70B -maxdepth 1 -type d"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-12T08:23:06.500356+00:00_

/tmp/teal_repo/models/Llama-3-8B
/tmp/teal_repo/models/Llama-3-8B/lookup
/tmp/teal_repo/models/Llama-3-8B/histograms
---
/tmp/teal_repo/models/Llama-3-8B/histograms/lookup/layer-9/results.csv
/tmp/teal_repo/models/Llama-3-8B/histograms/lookup/layer-8/results.csv
/tmp/teal_repo/models/Llama-3-8B/histograms/lookup/layer-7/results.csv
/tmp/teal_repo/models/Llama-3-8B/histograms/lookup/layer-6/results.csv
/tmp/teal_repo/models/Llama-3-8B/histograms/lookup/layer-5/results.csv
---
/tmp/teal_repo/models/Llama-3-70B
/tmp/teal_repo/models/Llama-3-70B/lookup
/tmp/teal_repo/models/Llama-3-70B/histograms

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-12T08:23:06.500584+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "tail -3 /tmp/teal_repo/models/Llama-2-7B/lookup/layer-0/results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "tool_args": {
    "command": "tail -3 /tmp/teal_repo/models/Llama-2-7B/lookup/layer-0/results.csv"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-12T08:23:06.500724+00:00_

0.8953367875647663,0.1845703125,0.19921875,0.9500000000000003,0.9500000000000003,0.9000000000000002,0.9500000000000003,0.8372093023255804,0.8372093023255804,0.9488372093023243
0.8994818652849734,0.1875,0.2021484375,0.9500000000000003,0.9500000000000003,0.9000000000000002,0.9500000000000003,0.8372093023255804,0.8558139534883711,0.9488372093023243
0.9036269430051806,0.19140625,0.205078125,0.9500000000000003,0.9500000000000003,0.9000000000000002,0.9500000000000003,0.8558139534883711,0.8558139534883711,0.9488372093023243

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-12T08:23:06.500862+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/ 2>/dev/null || echo \"DIR_NOT_EXIST\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/ 2>/dev/null || echo \"DIR_NOT_EXIST\""
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-12T08:23:06.500978+00:00_

_project
code_survey_report.md
manifest.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-12T08:23:06.501126+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/teal_calibration_notes.md",
  "content": "# TEAL 校准流程技术笔记\n\n基于 https://github.com/FasterDecoding/TEAL (ICLR 2025 Spotlight) 代码分析。\n\n---\n\n## 1. grab_acts.py — Activation Histogram 收集\n\n### 调用命令\n\n```bash\nCUDA_VISIBLE_DEVICES=0 python teal/grab_acts.py \\\n  --model_name meta-llama/Llama-2-7b-hf \\\n  --output_path $OUTPUT_PATH\n```\n\n### 流程\n\n1. 加载模型（`get_sparse_model`），设置 `grab_acts=True` 进入 grabbing mode\n2. 加载 **tatsu-lab/alpaca** 数据集的前 **300 条** train split，拼成一段长文本\n3. Tokenize 成 `[bsz=10, seq_len=2048]` 的 input_ids\n4. 手动逐层前向（不是 `model.forward`）：\n   - 先 `embed_tokens` + `rotary_emb` 得到初始 hidden_states 和 position_embeddings\n   - 逐层：保存 `hidden_states` → `act_{i}.pt`（给 greedyopt 用），然后过这一层\n5. 每层前向过程中，monkeypatched 的 forward 在关键位置调用 `activation_module.grab_activations(x, key)` 收集激活值\n\n### 收集的激活点位\n\n**Self-Attention 模块**（`self_attn.py:_FA2_forward`）：\n- `h1`: attention 输入 `hidden_states`（即 q/k/v_proj 的输入）\n- `h2`: attention 输出 `attn_output`（即 o_proj 的输入）\n\n**MLP 模块**（`mlp.py:_mlp_forward`）：\n- `h1`: MLP 输入 `x`（即 gate_proj 和 up_proj 的输入）\n- `h2`: 中间激活 `act_fn(gate_proj(x)) * up_proj(x)`（即 down_proj 的输入）\n\n### Histogram 计算（`ActivationModule.find_histogram`）\n\n```python\ndef find_histogram(self, num_bins=10000, outlier_threshold=0.01):\n```\n\n- 将所有 batch 的激活值 flatten、排序\n- 去掉上下各 1% 的 outlier 确定 `[lower_bound, upper_bound]`\n- 在此范围内生成 9999 个等距 bin，加上两端的极值 bin → 共 **10000 个 bins**\n- 调用 `torch.histogram` 得到 counts\n- 计算 bin_centers = (bins[:-1] + bins[1:]) / 2\n\n### 输出文件结构\n\n```\n$OUTPUT_PATH/\n├── histograms/\n│   └── layer-{i}/\n│       ├── mlp/\n│       │   └── histograms.pt      # dict: {h1, h1_centers, h2, h2_centers}\n│       └── self_attn/\n│           └── histograms.pt      # dict: {h1, h1_centers, h2, h2_centers}\n└── activations/\n    ├── act_0.pt                   # shape: [bsz=10, seq_len=2048, hidden_dim]\n    ├── act_1.pt\n    └── ...act_{N-1}.pt\n```\n\n每个 `histograms.pt` 包含 4 个 tensor：\n\n| Key | Shape | 含义 |\n|-----|-------|------|\n| `h1` | `[9999]` | hidden_type=h1 的 bin counts (float32) |\n| `h1_centers` | `[9999]` | 对应 bin 中心值 (float32) |\n| `h2` | `[9999]` | hidden_type=h2 的 bin counts (float32) |\n| `h2_centers` | `[9999]` | 对应 bin 中心值 (float32) |\n\n### 关键细节\n\n- histogram 是关于激活值绝对大小的分布，近似零均值单峰分布\n- `Distribution.icdf(q)` 通过 CDF 反函数直接从 histogram 计算 threshold\n- `SparsifyFn.set_threshold(sparsity)` 调用 `distr.icdf(0.5 + sparsity/2)` — 因为分布关于零对称，sparsity=0.5 意味着去掉中间 50% 的小值\n- 实际稀疏化：`x.abs().gt(threshold) * x`（magnitude pruning）\n\n---\n\n## 2. greedyopt.py — Block-wise Greedy Threshold 优化\n\n### 调用命令\n\n```bash\nCUDA_VISIBLE_DEVICES=0 python teal/greedyopt.py \\\n  --model_name meta-llama/Llama-2-7b-hf \\\n  --model_type Llama-2-7B \\\n  --teal_path $OUTPUT_PATH \\\n  --target_sparsity 0.9 \\\n  --base_step_size 0.025 \\\n  --last_fraction 0.25\n```\n\n### 核心算法\n\n对每一层独立进行 greedy 搜索，为 7 个 projection（q, k, v, o, gate, up, down）分配不同的 sparsity level：\n\n1. 加载该层的 `act_{i}.pt` 作为输入，用 dense forward 计算 `target_acts`\n2. 初始化所有 projection 的 sparsity = 0\n3. 循环直到 effective sparsity 达到 target：\n   - 对每个 projection 尝试增加 `step_size`\n   - 选择导致 activation error 最小的那个 projection\n   - 更新该 projection 的 sparsity\n4. Error 计算：只用序列后 25%（`last_fraction=0.25`）的 token 位置的 L2 norm\n\n### Weight Dict（加权 effective sparsity 计算）\n\n不同 projection 对总计算量的贡献权重不同：\n\n```python\n# Llama-2-7B 为例\n'q': 1, 'k': 1/8, 'v': 1/8, 'o': 1,\n'gate': 2.6875, 'up': 2.6875, 'down': 2.6875\n```\n\n- k/v 权重小：因为 GQA/MQA 下 k/v head 数少\n- gate/up/down 权重大：intermediate_size 大于 hidden_size（Llama-2-7B: 11008 vs 4096 ≈ 2.6875x）\n- effective_sparsity = Σ(sparsity_i × weight_i) / Σ(weight_i)\n\n### step_size 调整\n\n```python\nstep_sizes[proj] = base_step_size * (1 / weights[proj])\n```\n\n权重大的 projection，step_size 更小（搜索更精细）。\n\n### 输出格式\n\n```\n$OUTPUT_PATH/lookup/layer-{i}/results.csv\n```\n\nCSV 格式：\n```\nEffective Sparsity, Activation Error, Baseline Error, q, k, v, o, gate, up, down\n0.004145, 0.000380, 0.000671, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0186\n0.008290, 0.000443, 0.000832, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0372\n...\n```\n\n使用时通过 `get_layer_greedy_sparsities(layer_sparsities, results_dir)` 查表：给定 target effective sparsity，找到最近的行，读出各 projection 的 sparsity。\n\n---\n\n## 3. Threshold 计算的两条路径\n\n### 路径 A: Uniform（直接 CDF）\n\n```python\nmodel.set_uniform_sparsity(0.5)\n# → 对所有层所有 projection 调用：\n# SparsifyFn.set_threshold(0.5) → distr.icdf(0.5 + 0.5/2) = distr.icdf(0.75)\n```\n\n- 不需要 greedyopt，只需要 histograms\n- 每个 projection 查自己的 histogram CDF 反函数\n- 所有 projection 使用相同的 sparsity level\n\n### 路径 B: Block-wise Greedy\n\n```python\nmodel.load_greedy_sparsities(greedy_path, 0.5)\n```\n\n- 需要先运行 greedyopt 生成 lookup 表\n- 每个 projection 的 sparsity 不同（由 greedy 搜索决定）\n- 但最终 threshold 仍然是通过 `distr.icdf(0.5 + sparsity/2)` 从 histogram 算出\n- 优势：同样的 effective sparsity 下 error 更小\n\n### 可以跳过 greedy 吗？\n\n**可以。** Uniform 模式完全绕过 greedyopt，只需 histograms。论文显示 uniform 模式在 40-50% sparsity 下已有不错效果，greedy 在高 sparsity（>50%）下收益更大。\n\n---\n\n## 4. DeepSeek-R1-Distill-Qwen-14B 适配分析\n\n### 架构对比\n\n| 特性 | Llama-2/3 | Qwen2 (DeepSeek-R1-Distill-Qwen-14B) |\n|------|-----------|---------------------------------------|\n| Config 类 | `LlamaConfig` | `Qwen2Config` |\n| Decoder Layer | `LlamaDecoderLayer` | `Qwen2DecoderLayer` |\n| Attention | `LlamaFlashAttention2` | `Qwen2FlashAttention2` |\n| MLP | `LlamaMLP` | `Qwen2MLP` |\n| Attention proj | q_proj, k_proj, v_proj, o_proj | q_proj, k_proj, v_proj, o_proj |\n| MLP proj | gate_proj, up_proj, down_proj | gate_proj, up_proj, down_proj |\n| RoPE | 标准 RoPE | 标准 RoPE |\n| Norm | RMSNorm | RMSNorm |\n| GQA heads (14B) | - | num_heads=40, num_kv_heads=8 |\n| hidden_size (14B) | - | 5120 |\n| intermediate_size (14B) | - | 13824 |\n| num_layers (14B) | - | 48 |\n| bias | 无 | attention 有 bias (`attention_bias=True`) |\n\n### 关键差异和修改点\n\n#### 4.1 模型类注册\n\nTEAL 目前硬编码 `LlamaSparseForCausalLM` 和 `MistralSparseForCausalLM`。需要新增 `Qwen2SparseForCausalLM`：\n\n```python\nfrom transformers.models.qwen2.modeling_qwen2 import Qwen2ForCausalLM, Qwen2DecoderLayer\nfrom transformers.models.qwen2.configuration_qwen2 import Qwen2Config\n\nclass Qwen2SparseConfig(Qwen2Config):\n    model_type = \"qwen2_sparse\"\n\nclass Qwen2SparseForCausalLM(SparseModelMixin, Qwen2ForCausalLM):\n    config_class = Qwen2SparseConfig\n    _no_split_modules = [\"Qwen2DecoderLayer\"]\n```\n\n#### 4.2 get_sparse_model 适配\n\n`utils/utils.py:get_sparse_model` 需要扩展 class_name 白名单：\n\n```python\nassert class_name in [..., \"Qwen2ForCausalLM\", \"Qwen2SparseForCausalLM\"]\n```\n\n`get_model_class_name` 返回 `\"Qwen2ForCausalLM\"`，需要添加对应的分支选择 `Qwen2SparseForCausalLM`。\n\n#### 4.3 build_sparse_layers 适配\n\n`model.py:build_sparse_layers` 中 isinstance 检查需要加入 `Qwen2DecoderLayer`：\n\n```python\nif isinstance(layer, (LlamaDecoderLayer, MistralDecoderLayer, Qwen2DecoderLayer)):\n```\n\n#### 4.4 self_attn.py 适配\n\n`_FA2_forward` 中的 attention 实现需要匹配 Qwen2 的 forward 签名。Qwen2 attention 的 forward 参数与 Llama 略有不同，但核心的 q/k/v/o_proj 命名一致。关键差异：\n- Qwen2 attention 有 `bias`（q_proj.bias 等）\n- Qwen2 的 `rotary_emb` 可能传入 `position_ids` 而非 `value_states`（需检查 transformers 版本）\n\n但由于 TEAL 的 monkeypatch 方式是替换整个 forward，只要替换后的 forward 正确处理了这些差异即可。projection 层名称完全一致（q_proj/k_proj/v_proj/o_proj/gate_proj/up_proj/down_proj）。\n\n#### 4.5 TEAL 组件名映射\n\n| TEAL 内部名 | 实际 projection | Qwen2 匹配 |\n|------------|----------------|------------|\n| h1 (attn) | attn 输入 → q/k/v_proj 输入 | 一致 |\n| h2 (attn) | attn 输出 → o_proj 输入 | 一致 |\n| h1 (mlp) | mlp 输入 → gate/up_proj 输入 | 一致 |\n| h2 (mlp) | 中间激活 → down_proj 输入 | 一致 |\n| sparse_fns['q'] | SparsifyFn on h1 distr | 一致 |\n| sparse_fns['k'] | SparsifyFn on h1 distr | 一致 |\n| sparse_fns['v'] | SparsifyFn on h1 distr | 一致 |\n| sparse_fns['o'] | SparsifyFn on h2 distr | 一致 |\n| sparse_fns['gate'] | SparsifyFn on h1 distr | 一致 |\n| sparse_fns['up'] | SparsifyFn on h1 distr | 一致 |\n| sparse_fns['down'] | SparsifyFn on h2 distr | 一致 |\n\n#### 4.6 greedyopt weight_dict\n\n需要为 DeepSeek-R1-Distill-Qwen-14B 添加权重配置：\n\n```python\n\"Qwen2-14B\": {\n    'q': 1,\n    'k': 1/5,        # num_kv_heads/num_heads = 8/40 = 1/5\n    'v': 1/5,\n    'o': 1,\n    'gate': 13824/5120,  # intermediate_size/hidden_size ≈ 2.7\n    'up': 13824/5120,\n    'down': 13824/5120\n}\n```\n\n#### 4.7 grab_acts.py 适配\n\n`grab_acts.py` 手动调用 `model.model.rotary_emb(hidden_states, position_ids)` 并逐层传播。Qwen2 模型中 `rotary_emb` 签名可能不同（有的版本接受 `seq_len` 而非 `position_ids`），需要检查并适配。`position_embeddings` 在当前代码中实际未被使用（layer forward 内部会自己计算），所以这一行主要是兼容性问题。\n\n---\n\n## 5. 已有预校准模型\n\n### models/ 目录\n\n| 模型 | histograms | lookup (greedy) |\n|------|-----------|-----------------|\n| Llama-2-7B | 32 layers × {mlp, self_attn} | 32 layers results.csv |\n| Llama-2-13B | 40 layers × {mlp, self_attn} | 40 layers results.csv |\n| Llama-2-70B | 80 layers × {mlp, self_attn} | 80 layers results.csv |\n| Llama-3-8B | 32 layers × {mlp, self_attn} + lookup 嵌套 | 32 layers results.csv |\n| Llama-3-70B | 80 layers × {mlp, self_attn} + lookup 嵌套 | 80 layers results.csv |\n| Mistral-7B | 32 layers × {mlp, self_attn} | 32 layers results.csv |\n\n### 数据格式可复用性\n\n完全可以复用相同结构给新模型。只需：\n1. 运行 grab_acts.py 生成 histograms/ 和 activations/\n2. （可选）运行 greedyopt.py 生成 lookup/\n3. 产出文件格式完全一致（histograms.pt + results.csv）\n\n---\n\n## 6. 校准耗时和 GPU 内存预估\n\n### DeepSeek-R1-Distill-Qwen-14B (48 layers, 14B params)\n\n#### grab_acts.py\n\n- **内存需求**: 模型 FP16 ≈ 28GB，输入激活 [10, 2048, 5120] ≈ 200MB，逐层释放后峰值约 **30-32GB**（需要 1x A100-40G 或 1x A6000-48G）\n- **耗时**: 逐层前向 48 层 × (forward + histogram 计算)，预计 **10-20 分钟**\n- **磁盘**: histograms ≈ 48 × 2 × 4 × 10000 × 4B ≈ 15MB（很小）；activations ≈ 48 × 10 × 2048 × 5120 × 2B ≈ **9.4GB**\n\n#### greedyopt.py\n\n- **内存需求**: 模型在 CPU，逐层移到 GPU。GPU 上：单层参数 + 输入激活 + forward 计算。14B 模型单层约 600MB，激活约 200MB，峰值 GPU 约 **2-4GB**（内存友好）\n- **耗时**: 每层 greedy 搜索，每步试 7 个 projection，步数 ≈ target_sparsity / base_step_size ≈ 18-36 步（step_size=0.025, target=0.9），每步 7 次 forward → 每层约 126-252 次 forward。48 层总计约 6000-12000 次单层 forward，预计 **1-3 小时**\n- **磁盘**: lookup CSV 每层几十 KB，总计约 **2-3MB**\n\n#### 总计\n\n| 阶段 | GPU 内存 | 耗时 | 磁盘 |\n|------|---------|------|------|\n| grab_acts | ~30-32GB | 10-20 min | ~10GB (activations 为主) |\n| greedyopt | ~2-4GB | 1-3 hours | ~3MB |\n| **仅 uniform** | ~30-32GB | 10-20 min | ~15MB |\n\n如果只用 uniform sparsity，可以跳过 greedyopt 和 activations 保存，只需 histograms，耗时和磁盘都大幅减少。\n\n---\n\n## 7. 快速适配方案总结\n\n对 DeepSeek-R1-Distill-Qwen-14B，最小修改集：\n\n1. **新建** `Qwen2SparseForCausalLM` 和 `Qwen2SparseConfig`（`model.py`，~10 行）\n2. **扩展** `get_sparse_model` 的模型类白名单（`utils.py`，~5 行）\n3. **扩展** `build_sparse_layers` 的 isinstance 检查（`model.py`，1 行）\n4. **验证** Qwen2 的 attention forward 与 monkeypatch 兼容（可能需要调整 `_FA2_forward` 的 rotary_emb 调用）\n5. **添加** greedyopt weight_dict 条目（`greedyopt.py`，~5 行）\n6. **适配** `grab_acts.py` 的 rotary_emb 调用（1-2 行）\n\n由于 Qwen2 的 projection 命名与 Llama 完全一致（q_proj/k_proj/v_proj/o_proj/gate_proj/up_proj/down_proj），mlp.py 和 self_attn.py 的 monkeypatch 逻辑无需修改。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/teal_calibration_notes.md",
    "content": "# TEAL 校准流程技术笔记\n\n基于 https://github.com/FasterDecoding/TEAL (ICLR 2025 Spotlight) 代码分析。\n\n---\n\n## 1. grab_acts.py — Activation Histogram 收集\n\n### 调用命令\n\n```bash\nCUDA_VISIBLE_DEVICES=0 python teal/grab_acts.py \\\n  --model_name meta-llama/Llama-2-7b-hf \\\n  --output_path $OUTPUT_PATH\n```\n\n### 流程\n\n1. 加载模型（`get_sparse_model`），设置 `grab_acts=True` 进入 grabbing mode\n2. 加载 **tatsu-lab/alpaca** 数据集的前 **300 条** train split，拼成一段长文本\n3. Tokenize 成 `[bsz=10, seq_len=2048]` 的 input_ids\n4. 手动逐层前向（不是 `model.forward`）：\n   - 先 `embed_tokens` + `rotary_emb` 得到初始 hidden_states 和 position_embeddings\n   - 逐层：保存 `hidden_states` → `act_{i}.pt`（给 greedyopt 用），然后过这一层\n5. 每层前向过程中，monkeypatched 的 forward 在关键位置调用 `activation_module.grab_activations(x, key)` 收集激活值\n\n### 收集的激活点位\n\n**Self-Attention 模块**（`self_attn.py:_FA2_forward`）：\n- `h1`: attention 输入 `hidden_states`（即 q/k/v_proj 的输入）\n- `h2`: attention 输出 `attn_output`（即 o_proj 的输入）\n\n**MLP 模块**（`mlp.py:_mlp_forward`）：\n- `h1`: MLP 输入 `x`（即 gate_proj 和 up_proj 的输入）\n- `h2`: 中间激活 `act_fn(gate_proj(x)) * up_proj(x)`（即 down_proj 的输入）\n\n### Histogram 计算（`ActivationModule.find_histogram`）\n\n```python\ndef find_histogram(self, num_bins=10000, outlier_threshold=0.01):\n```\n\n- 将所有 batch 的激活值 flatten、排序\n- 去掉上下各 1% 的 outlier 确定 `[lower_bound, upper_bound]`\n- 在此范围内生成 9999 个等距 bin，加上两端的极值 bin → 共 **10000 个 bins**\n- 调用 `torch.histogram` 得到 counts\n- 计算 bin_centers = (bins[:-1] + bins[1:]) / 2\n\n### 输出文件结构\n\n```\n$OUTPUT_PATH/\n├── histograms/\n│   └── layer-{i}/\n│       ├── mlp/\n│       │   └── histograms.pt      # dict: {h1, h1_centers, h2, h2_centers}\n│       └── self_attn/\n│           └── histograms.pt      # dict: {h1, h1_centers, h2, h2_centers}\n└── activations/\n    ├── act_0.pt                   # shape: [bsz=10, seq_len=2048, hidden_dim]\n    ├── act_1.pt\n    └── ...act_{N-1}.pt\n```\n\n每个 `histograms.pt` 包含 4 个 tensor：\n\n| Key | Shape | 含义 |\n|-----|-------|------|\n| `h1` | `[9999]` | hidden_type=h1 的 bin counts (float32) |\n| `h1_centers` | `[9999]` | 对应 bin 中心值 (float32) |\n| `h2` | `[9999]` | hidden_type=h2 的 bin counts (float32) |\n| `h2_centers` | `[9999]` | 对应 bin 中心值 (float32) |\n\n### 关键细节\n\n- histogram 是关于激活值绝对大小的分布，近似零均值单峰分布\n- `Distribution.icdf(q)` 通过 CDF 反函数直接从 histogram 计算 threshold\n- `SparsifyFn.set_threshold(sparsity)` 调用 `distr.icdf(0.5 + sparsity/2)` — 因为分布关于零对称，sparsity=0.5 意味着去掉中间 50% 的小值\n- 实际稀疏化：`x.abs().gt(threshold) * x`（magnitude pruning）\n\n---\n\n## 2. greedyopt.py — Block-wise Greedy Threshold 优化\n\n### 调用命令\n\n```bash\nCUDA_VISIBLE_DEVICES=0 python teal/greedyopt.py \\\n  --model_name meta-llama/Llama-2-7b-hf \\\n  --model_type Llama-2-7B \\\n  --teal_path $OUTPUT_PATH \\\n  --target_sparsity 0.9 \\\n  --base_step_size 0.025 \\\n  --last_fraction 0.25\n```\n\n### 核心算法\n\n对每一层独立进行 greedy 搜索，为 7 个 projection（q, k, v, o, gate, up, down）分配不同的 sparsity level：\n\n1. 加载该层的 `act_{i}.pt` 作为输入，用 dense forward 计算 `target_acts`\n2. 初始化所有 projection 的 sparsity = 0\n3. 循环直到 effective sparsity 达到 target：\n   - 对每个 projection 尝试增加 `step_size`\n   - 选择导致 activation error 最小的那个 projection\n   - 更新该 projection 的 sparsity\n4. Error 计算：只用序列后 25%（`last_fraction=0.25`）的 token 位置的 L2 norm\n\n### Weight Dict（加权 effective sparsity 计算）\n\n不同 projection 对总计算量的贡献权重不同：\n\n```python\n# Llama-2-7B 为例\n'q': 1, 'k': 1/8, 'v': 1/8, 'o': 1,\n'gate': 2.6875, 'up': 2.6875, 'down': 2.6875\n```\n\n- k/v 权重小：因为 GQA/MQA 下 k/v head 数少\n- gate/up/down 权重大：intermediate_size 大于 hidden_size（Llama-2-7B: 11008 vs 4096 ≈ 2.6875x）\n- effective_sparsity = Σ(sparsity_i × weight_i) / Σ(weight_i)\n\n### step_size 调整\n\n```python\nstep_sizes[proj] = base_step_size * (1 / weights[proj])\n```\n\n权重大的 projection，step_size 更小（搜索更精细）。\n\n### 输出格式\n\n```\n$OUTPUT_PATH/lookup/layer-{i}/results.csv\n```\n\nCSV 格式：\n```\nEffective Sparsity, Activation Error, Baseline Error, q, k, v, o, gate, up, down\n0.004145, 0.000380, 0.000671, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0186\n0.008290, 0.000443, 0.000832, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0372\n...\n```\n\n使用时通过 `get_layer_greedy_sparsities(layer_sparsities, results_dir)` 查表：给定 target effective sparsity，找到最近的行，读出各 projection 的 sparsity。\n\n---\n\n## 3. Threshold 计算的两条路径\n\n### 路径 A: Uniform（直接 CDF）\n\n```python\nmodel.set_uniform_sparsity(0.5)\n# → 对所有层所有 projection 调用：\n# SparsifyFn.set_threshold(0.5) → distr.icdf(0.5 + 0.5/2) = distr.icdf(0.75)\n```\n\n- 不需要 greedyopt，只需要 histograms\n- 每个 projection 查自己的 histogram CDF 反函数\n- 所有 projection 使用相同的 sparsity level\n\n### 路径 B: Block-wise Greedy\n\n```python\nmodel.load_greedy_sparsities(greedy_path, 0.5)\n```\n\n- 需要先运行 greedyopt 生成 lookup 表\n- 每个 projection 的 sparsity 不同（由 greedy 搜索决定）\n- 但最终 threshold 仍然是通过 `distr.icdf(0.5 + sparsity/2)` 从 histogram 算出\n- 优势：同样的 effective sparsity 下 error 更小\n\n### 可以跳过 greedy 吗？\n\n**可以。** Uniform 模式完全绕过 greedyopt，只需 histograms。论文显示 uniform 模式在 40-50% sparsity 下已有不错效果，greedy 在高 sparsity（>50%）下收益更大。\n\n---\n\n## 4. DeepSeek-R1-Distill-Qwen-14B 适配分析\n\n### 架构对比\n\n| 特性 | Llama-2/3 | Qwen2 (DeepSeek-R1-Distill-Qwen-14B) |\n|------|-----------|---------------------------------------|\n| Config 类 | `LlamaConfig` | `Qwen2Config` |\n| Decoder Layer | `LlamaDecoderLayer` | `Qwen2DecoderLayer` |\n| Attention | `LlamaFlashAttention2` | `Qwen2FlashAttention2` |\n| MLP | `LlamaMLP` | `Qwen2MLP` |\n| Attention proj | q_proj, k_proj, v_proj, o_proj | q_proj, k_proj, v_proj, o_proj |\n| MLP proj | gate_proj, up_proj, down_proj | gate_proj, up_proj, down_proj |\n| RoPE | 标准 RoPE | 标准 RoPE |\n| Norm | RMSNorm | RMSNorm |\n| GQA heads (14B) | - | num_heads=40, num_kv_heads=8 |\n| hidden_size (14B) | - | 5120 |\n| intermediate_size (14B) | - | 13824 |\n| num_layers (14B) | - | 48 |\n| bias | 无 | attention 有 bias (`attention_bias=True`) |\n\n### 关键差异和修改点\n\n#### 4.1 模型类注册\n\nTEAL 目前硬编码 `LlamaSparseForCausalLM` 和 `MistralSparseForCausalLM`。需要新增 `Qwen2SparseForCausalLM`：\n\n```python\nfrom transformers.models.qwen2.modeling_qwen2 import Qwen2ForCausalLM, Qwen2DecoderLayer\nfrom transformers.models.qwen2.configuration_qwen2 import Qwen2Config\n\nclass Qwen2SparseConfig(Qwen2Config):\n    model_type = \"qwen2_sparse\"\n\nclass Qwen2SparseForCausalLM(SparseModelMixin, Qwen2ForCausalLM):\n    config_class = Qwen2SparseConfig\n    _no_split_modules = [\"Qwen2DecoderLayer\"]\n```\n\n#### 4.2 get_sparse_model 适配\n\n`utils/utils.py:get_sparse_model` 需要扩展 class_name 白名单：\n\n```python\nassert class_name in [..., \"Qwen2ForCausalLM\", \"Qwen2SparseForCausalLM\"]\n```\n\n`get_model_class_name` 返回 `\"Qwen2ForCausalLM\"`，需要添加对应的分支选择 `Qwen2SparseForCausalLM`。\n\n#### 4.3 build_sparse_layers 适配\n\n`model.py:build_sparse_layers` 中 isinstance 检查需要加入 `Qwen2DecoderLayer`：\n\n```python\nif isinstance(layer, (LlamaDecoderLayer, MistralDecoderLayer, Qwen2DecoderLayer)):\n```\n\n#### 4.4 self_attn.py 适配\n\n`_FA2_forward` 中的 attention 实现需要匹配 Qwen2 的 forward 签名。Qwen2 attention 的 forward 参数与 Llama 略有不同，但核心的 q/k/v/o_proj 命名一致。关键差异：\n- Qwen2 attention 有 `bias`（q_proj.bias 等）\n- Qwen2 的 `rotary_emb` 可能传入 `position_ids` 而非 `value_states`（需检查 transformers 版本）\n\n但由于 TEAL 的 monkeypatch 方式是替换整个 forward，只要替换后的 forward 正确处理了这些差异即可。projection 层名称完全一致（q_proj/k_proj/v_proj/o_proj/gate_proj/up_proj/down_proj）。\n\n#### 4.5 TEAL 组件名映射\n\n| TEAL 内部名 | 实际 projection | Qwen2 匹配 |\n|------------|----------------|------------|\n| h1 (attn) | attn 输入 → q/k/v_proj 输入 | 一致 |\n| h2 (attn) | attn 输出 → o_proj 输入 | 一致 |\n| h1 (mlp) | mlp 输入 → gate/up_proj 输入 | 一致 |\n| h2 (mlp) | 中间激活 → down_proj 输入 | 一致 |\n| sparse_fns['q'] | SparsifyFn on h1 distr | 一致 |\n| sparse_fns['k'] | SparsifyFn on h1 distr | 一致 |\n| sparse_fns['v'] | SparsifyFn on h1 distr | 一致 |\n| sparse_fns['o'] | SparsifyFn on h2 distr | 一致 |\n| sparse_fns['gate'] | SparsifyFn on h1 distr | 一致 |\n| sparse_fns['up'] | SparsifyFn on h1 distr | 一致 |\n| sparse_fns['down'] | SparsifyFn on h2 distr | 一致 |\n\n#### 4.6 greedyopt weight_dict\n\n需要为 DeepSeek-R1-Distill-Qwen-14B 添加权重配置：\n\n```python\n\"Qwen2-14B\": {\n    'q': 1,\n    'k': 1/5,        # num_kv_heads/num_heads = 8/40 = 1/5\n    'v': 1/5,\n    'o': 1,\n    'gate': 13824/5120,  # intermediate_size/hidden_size ≈ 2.7\n    'up': 13824/5120,\n    'down': 13824/5120\n}\n```\n\n#### 4.7 grab_acts.py 适配\n\n`grab_acts.py` 手动调用 `model.model.rotary_emb(hidden_states, position_ids)` 并逐层传播。Qwen2 模型中 `rotary_emb` 签名可能不同（有的版本接受 `seq_len` 而非 `position_ids`），需要检查并适配。`position_embeddings` 在当前代码中实际未被使用（layer forward 内部会自己计算），所以这一行主要是兼容性问题。\n\n---\n\n## 5. 已有预校准模型\n\n### models/ 目录\n\n| 模型 | histograms | lookup (greedy) |\n|------|-----------|-----------------|\n| Llama-2-7B | 32 layers × {mlp, self_attn} | 32 layers results.csv |\n| Llama-2-13B | 40 layers × {mlp, self_attn} | 40 layers results.csv |\n| Llama-2-70B | 80 layers × {mlp, self_attn} | 80 layers results.csv |\n| Llama-3-8B | 32 layers × {mlp, self_attn} + lookup 嵌套 | 32 layers results.csv |\n| Llama-3-70B | 80 layers × {mlp, self_attn} + lookup 嵌套 | 80 layers results.csv |\n| Mistral-7B | 32 layers × {mlp, self_attn} | 32 layers results.csv |\n\n### 数据格式可复用性\n\n完全可以复用相同结构给新模型。只需：\n1. 运行 grab_acts.py 生成 histograms/ 和 activations/\n2. （可选）运行 greedyopt.py 生成 lookup/\n3. 产出文件格式完全一致（histograms.pt + results.csv）\n\n---\n\n## 6. 校准耗时和 GPU 内存预估\n\n### DeepSeek-R1-Distill-Qwen-14B (48 layers, 14B params)\n\n#### grab_acts.py\n\n- **内存需求**: 模型 FP16 ≈ 28GB，输入激活 [10, 2048, 5120] ≈ 200MB，逐层释放后峰值约 **30-32GB**（需要 1x A100-40G 或 1x A6000-48G）\n- **耗时**: 逐层前向 48 层 × (forward + histogram 计算)，预计 **10-20 分钟**\n- **磁盘**: histograms ≈ 48 × 2 × 4 × 10000 × 4B ≈ 15MB（很小）；activations ≈ 48 × 10 × 2048 × 5120 × 2B ≈ **9.4GB**\n\n#### greedyopt.py\n\n- **内存需求**: 模型在 CPU，逐层移到 GPU。GPU 上：单层参数 + 输入激活 + forward 计算。14B 模型单层约 600MB，激活约 200MB，峰值 GPU 约 **2-4GB**（内存友好）\n- **耗时**: 每层 greedy 搜索，每步试 7 个 projection，步数 ≈ target_sparsity / base_step_size ≈ 18-36 步（step_size=0.025, target=0.9），每步 7 次 forward → 每层约 126-252 次 forward。48 层总计约 6000-12000 次单层 forward，预计 **1-3 小时**\n- **磁盘**: lookup CSV 每层几十 KB，总计约 **2-3MB**\n\n#### 总计\n\n| 阶段 | GPU 内存 | 耗时 | 磁盘 |\n|------|---------|------|------|\n| grab_acts | ~30-32GB | 10-20 min | ~10GB (activations 为主) |\n| greedyopt | ~2-4GB | 1-3 hours | ~3MB |\n| **仅 uniform** | ~30-32GB | 10-20 min | ~15MB |\n\n如果只用 uniform sparsity，可以跳过 greedyopt 和 activations 保存，只需 histograms，耗时和磁盘都大幅减少。\n\n---\n\n## 7. 快速适配方案总结\n\n对 DeepSeek-R1-Distill-Qwen-14B，最小修改集：\n\n1. **新建** `Qwen2SparseForCausalLM` 和 `Qwen2SparseConfig`（`model.py`，~10 行）\n2. **扩展** `get_sparse_model` 的模型类白名单（`utils.py`，~5 行）\n3. **扩展** `build_sparse_layers` 的 isinstance 检查（`model.py`，1 行）\n4. **验证** Qwen2 的 attention forward 与 monkeypatch 兼容（可能需要调整 `_FA2_forward` 的 rotary_emb 调用）\n5. **添加** greedyopt weight_dict 条目（`greedyopt.py`，~5 行）\n6. **适配** `grab_acts.py` 的 rotary_emb 调用（1-2 行）\n\n由于 Qwen2 的 projection 命名与 Llama 完全一致（q_proj/k_proj/v_proj/o_proj/gate_proj/up_proj/down_proj），mlp.py 和 self_attn.py 的 monkeypatch 逻辑无需修改。\n"
  }
}
````

</details>

---

### Tool result

_source line 64 · 2026-05-12T08:23:06.501434+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/teal_calibration_notes.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-12T08:23:06.501582+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "teal_calibration_notes",
  "type": "report",
  "description": "TEAL 校准流程深度技术笔记：grab_acts.py 流程、histogram 数据格式、greedy optimization 算法、DeepSeek-R1-Distill-Qwen-14B 适配要点、预估资源需求",
  "project": "solver-verified-formalizer-rl",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/teal_calibration_notes.md",
  "tags": "['teal', 'calibration', 'activation-sparsity', 'qwen2', 'deepseek']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "teal_calibration_notes",
    "type": "report",
    "description": "TEAL 校准流程深度技术笔记：grab_acts.py 流程、histogram 数据格式、greedy optimization 算法、DeepSeek-R1-Distill-Qwen-14B 适配要点、预估资源需求",
    "project": "solver-verified-formalizer-rl",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/teal_calibration_notes.md",
    "tags": "['teal', 'calibration', 'activation-sparsity', 'qwen2', 'deepseek']"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-12T08:23:06.501741+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_687773\", \"name\": \"teal_calibration_notes\", \"type\": \"report\", \"description\": \"TEAL 校准流程深度技术笔记：grab_acts.py 流程、histogram 数据格式、greedy optimization 算法、DeepSeek-R1-Distill-Qwen-14B 适配要点、预估资源需求\", \"path\": \"projects/solver-verified-formalizer-rl/artifacts/_project/report/teal_calibration_notes.md\", \"url\": null, \"project\": \"solver-verified-formalizer-rl\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T08:22:50.451531+00:00\", \"tags\": [\"teal\", \"calibration\", \"activation-sparsity\", \"qwen2\", \"deepseek\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/solver-verified-formalizer-rl/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-12T08:23:06.501913+00:00_

技术笔记已完成并注册。核心发现：

1. **grab_acts.py** 用 Alpaca 300 条数据，逐层收集 `h1`（projection 输入）和 `h2`（projection 中间/输出）的激活分布 histogram（10000 bins），存为 `histograms.pt`

2. **greedyopt.py** 逐层 greedy 搜索 7 个 projection 的最优 sparsity 分配，输出 lookup CSV 表

3. **Threshold 两条路径**：Uniform 只需 histograms（通过 CDF 反函数直接算），Greedy 额外需要 lookup 表但同 sparsity 下 error 更小

4. **Qwen2 适配**工作量不大——projection 命名完全一致（q/k/v/o_proj, gate/up/down_proj），主要修改：新建 `Qwen2SparseForCausalLM` 类、扩展模型白名单、添加 weight_dict 条目、验证 rotary_emb 兼容性

5. **资源预估**：14B 模型 grab_acts 需 ~30GB GPU / 10-20 分钟；greedyopt 需 ~4GB GPU / 1-3 小时；仅 uniform 模式可跳过 greedyopt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_teal_calibration_deep_dive_20260512T081939"
}
```

</details>

---
