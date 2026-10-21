import torch
from torch.optim import Optimizer

def _zeropower_via_newtonschulz5(G, steps=5):
    assert G.ndim >= 2
    a, b, c = (3.4445, -4.7750, 2.0315)
    X = G.bfloat16()
    if G.size(-2) > G.size(-1):
        X = X.mT
    X = X / (X.norm(dim=(-2, -1), keepdim=True) + 1e-7)
    for _ in range(steps):
        A = X @ X.mT
        B = b * A + c * A @ A
        X = a * X + B @ X
    if G.size(-2) > G.size(-1):
        X = X.mT
    return X


class Muon(Optimizer):
    """Muon optimizer: Newton-Schulz spectral update for >=2D params, AdamW for 1D params."""

    def __init__(self, params, lr=0.02, momentum=0.95, nesterov=True, ns_steps=5,
                 adamw_lr=3e-4, adamw_betas=(0.9, 0.999), adamw_wd=0.05):
        defaults = dict(lr=lr, momentum=momentum, nesterov=nesterov, ns_steps=ns_steps,
                        adamw_lr=adamw_lr, adamw_betas=adamw_betas, adamw_wd=adamw_wd)
        super().__init__(params, defaults)

    @torch.no_grad()
    def step(self, closure=None):
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()

        for group in self.param_groups:
            lr = group['lr']
            beta = group['momentum']
            nesterov = group['nesterov']
            ns_steps = group['ns_steps']
            adamw_lr = group['adamw_lr']
            adamw_betas = group['adamw_betas']
            adamw_wd = group['adamw_wd']

            for p in group['params']:
                if p.grad is None:
                    continue
                grad = p.grad

                state = self.state[p]
                if len(state) == 0:
                    state['step'] = 0

                state['step'] += 1

                if p.ndim >= 2:
                    # Muon update for weight matrices
                    if 'momentum_buffer' not in state:
                        state['momentum_buffer'] = torch.zeros_like(grad)
                    buf = state['momentum_buffer']
                    buf.lerp_(grad, 1 - beta)
                    if nesterov:
                        update = grad.lerp(buf, beta)
                    else:
                        update = buf.clone()
                    # Newton-Schulz spectral normalization
                    orig_shape = update.shape
                    if update.ndim == 4:
                        update = update.view(len(update), -1)
                    update = _zeropower_via_newtonschulz5(update, steps=ns_steps)
                    update = update.to(p.dtype)
                    if update.ndim != len(orig_shape):
                        update = update.view(orig_shape)
                    update *= max(1, grad.size(-2) / grad.size(-1)) ** 0.5
                    p.add_(update, alpha=-lr)
                else:
                    # AdamW for biases, norms, embeddings
                    if 'exp_avg' not in state:
                        state['exp_avg'] = torch.zeros_like(p)
                        state['exp_avg_sq'] = torch.zeros_like(p)
                    exp_avg, exp_avg_sq = state['exp_avg'], state['exp_avg_sq']
                    b1, b2 = adamw_betas

                    # Weight decay
                    p.mul_(1 - adamw_lr * adamw_wd)

                    exp_avg.lerp_(grad, 1 - b1)
                    exp_avg_sq.lerp_(grad.square(), 1 - b2)

                    bias_correction1 = 1 - b1 ** state['step']
                    bias_correction2 = 1 - b2 ** state['step']
                    step_size = adamw_lr / bias_correction1
                    denom = (exp_avg_sq.sqrt() / (bias_correction2 ** 0.5)).add_(1e-8)
                    p.addcdiv_(exp_avg, denom, value=-step_size)

        return loss
