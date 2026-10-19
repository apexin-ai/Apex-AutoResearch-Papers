"""Patch train_a1_sdf_aux.py: Fix 2 (warmup dead code)."""

path = "/root/colliforce-vla/scripts/train_a1_sdf_aux.py"
with open(path) as f:
    code = f.read()

# ============================================================
# Fix 2: Replace dead grad-scaling warmup with gradient hooks
# ============================================================

# Phase 2 transition: add gradient hooks
old_transition = (
    '            self._lora_warmup_steps = 300\n'
    '            _m = model.module if hasattr(model, "module") else model\n'
    '            self._lora_params = []\n'
    '            n_unfrozen = 0\n'
    '            for name, p in _m.named_parameters():\n'
    '                if "lora" in name.lower():\n'
    '                    p.requires_grad = True\n'
    '                    n_unfrozen += p.numel()\n'
    '                    self._lora_params.append(p)\n'
    '            n_total_trainable = n_unfrozen\n'
    '            for p in self.sdf_decoder.parameters():\n'
    '                n_total_trainable += p.numel()\n'
    '            for p in self.ee_extractor.parameters():\n'
    '                n_total_trainable += p.numel()\n'
    '            logging.info(\n'
    '                "Phase 2: unfroze %d LoRA params at step %d (total trainable: %d, LoRA warmup: %d steps)",\n'
    '                n_unfrozen, global_step, n_total_trainable, self._lora_warmup_steps,\n'
    '            )'
)
new_transition = (
    '            self._lora_warmup_steps = 100\n'
    '            self._lora_warmup_scale = 0.0\n'
    '            self._lora_grad_hooks = []\n'
    '            _m = model.module if hasattr(model, "module") else model\n'
    '            self._lora_params = []\n'
    '            n_unfrozen = 0\n'
    '            for name, p in _m.named_parameters():\n'
    '                if "lora" in name.lower():\n'
    '                    p.requires_grad = True\n'
    '                    n_unfrozen += p.numel()\n'
    '                    self._lora_params.append(p)\n'
    '                    h = p.register_hook(lambda grad, s=self: grad * s._lora_warmup_scale)\n'
    '                    self._lora_grad_hooks.append(h)\n'
    '            n_total_trainable = n_unfrozen\n'
    '            for p in self.sdf_decoder.parameters():\n'
    '                n_total_trainable += p.numel()\n'
    '            for p in self.ee_extractor.parameters():\n'
    '                n_total_trainable += p.numel()\n'
    '            logging.info(\n'
    '                "Phase 2: unfroze %d LoRA params at step %d (total trainable: %d, LoRA grad warmup: %d steps)",\n'
    '                n_unfrozen, global_step, n_total_trainable, self._lora_warmup_steps,\n'
    '            )'
)
assert old_transition in code, "A1 phase2 transition not found"
code = code.replace(old_transition, new_transition)

# Replace dead grad scaling logic
old_grad_scale = (
    '        # Phase 2 LoRA warmup: scale gradients linearly for first N steps\n'
    "        if self.phase == 2 and hasattr(self, '_phase2_start'):\n"
    '            steps_in = global_step - self._phase2_start\n'
    '            if steps_in < self._lora_warmup_steps:\n'
    '                scale = steps_in / self._lora_warmup_steps\n'
    '                for p in self._lora_params:\n'
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
assert old_grad_scale in code, "A1 grad scale block not found"
code = code.replace(old_grad_scale, new_grad_scale)

# Update on_cleanup
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
assert old_cleanup in code, "A1 on_cleanup not found"
code = code.replace(old_cleanup, new_cleanup)

with open(path, 'w') as f:
    f.write(code)

print("A1 patched successfully")
