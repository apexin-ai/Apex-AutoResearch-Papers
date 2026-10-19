"""Patch train_a3_hook.py: Fix 1 (per-module LoRA rank) + Fix 2 (warmup dead code)."""

path = "/root/colliforce-vla/scripts/train_a3_hook.py"
with open(path) as f:
    code = f.read()

# ============================================================
# Fix 1: inject_lora per-module rank/alpha
# ============================================================

old_inject = (
    'def inject_lora(model: nn.Module, rank: int = 16, alpha: float = 16.0):\n'
    '    """Inject LoRA into paligemma + action expert attention & MLP projections.\n'
    '    Returns list of all LoRA parameters (~53M with rank=32).\n'
    '    """\n'
    '    lora_params = []\n'
    '\n'
    '    # Paligemma language model layers\n'
    '    pali_layers = model.paligemma_with_expert.paligemma.language_model.model.layers\n'
    '    for layer in pali_layers:\n'
    '        for name in TARGET_MODULES:\n'
    '            parent = layer.self_attn if name in ("q_proj", "k_proj", "v_proj", "o_proj") else layer.mlp\n'
    '            _replace_linear(parent, name, rank, alpha)\n'
    '            lora_mod = getattr(parent, name)\n'
    '            lora_params.extend([lora_mod.lora_A, lora_mod.lora_B])\n'
    '\n'
    '    # Action expert layers\n'
    '    expert_layers = model.paligemma_with_expert.gemma_expert.model.layers\n'
    '    for layer in expert_layers:\n'
    '        for name in TARGET_MODULES:\n'
    '            parent = layer.self_attn if name in ("q_proj", "k_proj", "v_proj", "o_proj") else layer.mlp\n'
    '            _replace_linear(parent, name, rank, alpha)\n'
    '            lora_mod = getattr(parent, name)\n'
    '            lora_params.extend([lora_mod.lora_A, lora_mod.lora_B])\n'
    '\n'
    '    return lora_params'
)

new_inject = (
    'def inject_lora(model: nn.Module, pali_rank: int = 16, pali_alpha: float = 16.0,\n'
    '                expert_rank: int = 32, expert_alpha: float = 32.0):\n'
    '    """Inject LoRA with per-module rank/alpha matching baseline openpi config:\n'
    '    PaliGemma (Gemma 2B) -> rank=16, alpha=16; Action Expert (Gemma 300M) -> rank=32, alpha=32.\n'
    '    Returns (all_lora_params, pali_lora_params, expert_lora_params).\n'
    '    """\n'
    '    pali_lora_params = []\n'
    '    expert_lora_params = []\n'
    '\n'
    '    # PaliGemma language model layers\n'
    '    pali_layers = model.paligemma_with_expert.paligemma.language_model.model.layers\n'
    '    for layer in pali_layers:\n'
    '        for name in TARGET_MODULES:\n'
    '            parent = layer.self_attn if name in ("q_proj", "k_proj", "v_proj", "o_proj") else layer.mlp\n'
    '            _replace_linear(parent, name, pali_rank, pali_alpha)\n'
    '            lora_mod = getattr(parent, name)\n'
    '            pali_lora_params.extend([lora_mod.lora_A, lora_mod.lora_B])\n'
    '\n'
    '    # Action Expert layers\n'
    '    expert_layers = model.paligemma_with_expert.gemma_expert.model.layers\n'
    '    for layer in expert_layers:\n'
    '        for name in TARGET_MODULES:\n'
    '            parent = layer.self_attn if name in ("q_proj", "k_proj", "v_proj", "o_proj") else layer.mlp\n'
    '            _replace_linear(parent, name, expert_rank, expert_alpha)\n'
    '            lora_mod = getattr(parent, name)\n'
    '            expert_lora_params.extend([lora_mod.lora_A, lora_mod.lora_B])\n'
    '\n'
    '    all_params = pali_lora_params + expert_lora_params\n'
    '    return all_params, pali_lora_params, expert_lora_params'
)

assert old_inject in code, "inject_lora function not found"
code = code.replace(old_inject, new_inject)

# Fix 1b: Update call site
old_call = '        self.lora_params = inject_lora(_m, rank=32, alpha=32.0)'
new_call = (
    '        self.lora_params, self._pali_lora_params, self._expert_lora_params = inject_lora(\n'
    '            _m, pali_rank=16, pali_alpha=16.0, expert_rank=32, expert_alpha=32.0)'
)
assert old_call in code, "inject_lora call not found"
code = code.replace(old_call, new_call)

# Fix 1c: Update logging
old_log_lines = [
    '        lora_total = sum(p.numel() for p in self.lora_params)',
    '        logging.info("  LoRA params (injected, frozen for Phase 1): %.2fM", lora_total / 1e6)',
]
new_log_lines = [
    '        pali_lora_total = sum(p.numel() for p in self._pali_lora_params)\n'
    '        expert_lora_total = sum(p.numel() for p in self._expert_lora_params)\n'
    '        lora_total = pali_lora_total + expert_lora_total',
    '        logging.info("  LoRA PaliGemma (rank=16): %.2fM", pali_lora_total / 1e6)\n'
    '        logging.info("  LoRA Action Expert (rank=32): %.2fM", expert_lora_total / 1e6)\n'
    '        logging.info("  LoRA total (frozen for Phase 1): %.2fM", lora_total / 1e6)',
]
for old, new in zip(old_log_lines, new_log_lines):
    assert old in code, f"log line not found: {old[:50]}"
    code = code.replace(old, new)

# ============================================================
# Fix 2: Replace dead grad-scaling warmup with gradient hooks
# ============================================================

old_warmup_block = (
    '            self._lora_warmup_steps = 300\n'
    '            unfrozen = 0\n'
    '            for p in self.lora_params:\n'
    '                p.requires_grad = True\n'
    '                unfrozen += p.numel()\n'
    '            logging.info("=== Phase 2 activated at step %d ===", global_step)\n'
    '            logging.info("  Unfroze LoRA params: %.2fM", unfrozen / 1e6)\n'
    '            logging.info("  LoRA LR warmup: %d steps", self._lora_warmup_steps)'
)
new_warmup_block = (
    '            self._lora_warmup_steps = 100\n'
    '            self._lora_warmup_scale = 0.0\n'
    '            self._lora_grad_hooks = []\n'
    '            unfrozen = 0\n'
    '            for p in self.lora_params:\n'
    '                p.requires_grad = True\n'
    '                unfrozen += p.numel()\n'
    '                h = p.register_hook(lambda grad, s=self: grad * s._lora_warmup_scale)\n'
    '                self._lora_grad_hooks.append(h)\n'
    '            logging.info("=== Phase 2 activated at step %d ===", global_step)\n'
    '            logging.info("  Unfroze LoRA params: %.2fM", unfrozen / 1e6)\n'
    '            logging.info("  LoRA grad warmup: %d steps (via register_hook)", self._lora_warmup_steps)'
)
assert old_warmup_block in code, "warmup block not found"
code = code.replace(old_warmup_block, new_warmup_block)

# Fix 2b: Replace dead grad scaling logic
old_grad_scale = (
    '        # Phase 2 LoRA warmup: scale gradients linearly for first N steps\n'
    "        if self.phase == 2 and hasattr(self, '_phase2_start'):\n"
    '            steps_in = global_step - self._phase2_start\n'
    '            if steps_in < self._lora_warmup_steps:\n'
    '                scale = steps_in / self._lora_warmup_steps\n'
    '                for p in self.lora_params:\n'
    '                    if p.grad is not None:\n'
    '                        p.grad.mul_(scale)'
)
new_grad_scale = (
    '        # Phase 2 LoRA warmup: linearly ramp gradient scale over first N steps\n'
    "        if self.phase == 2 and hasattr(self, '_phase2_start'):\n"
    '            steps_in = global_step - self._phase2_start\n'
    '            if steps_in < self._lora_warmup_steps:\n'
    '                self._lora_warmup_scale = (steps_in + 1) / self._lora_warmup_steps\n'
    "            elif hasattr(self, '_lora_grad_hooks') and self._lora_grad_hooks:\n"
    '                for h in self._lora_grad_hooks:\n'
    '                    h.remove()\n'
    '                self._lora_grad_hooks = []\n'
    '                self._lora_warmup_scale = 1.0\n'
    '                logging.info("LoRA gradient warmup complete at step %d", global_step)'
)
assert old_grad_scale in code, "grad scale block not found"
code = code.replace(old_grad_scale, new_grad_scale)

# Fix 2c: Update on_cleanup
old_cleanup = (
    '    def on_cleanup(self):\n'
    '        if self.hook_handle is not None:\n'
    '            self.hook_handle.remove()'
)
new_cleanup = (
    '    def on_cleanup(self):\n'
    '        if self.hook_handle is not None:\n'
    '            self.hook_handle.remove()\n'
    "        for h in getattr(self, '_lora_grad_hooks', []):\n"
    '            h.remove()'
)
assert old_cleanup in code, "on_cleanup not found"
code = code.replace(old_cleanup, new_cleanup)

with open(path, 'w') as f:
    f.write(code)

print("A3 patched successfully")
