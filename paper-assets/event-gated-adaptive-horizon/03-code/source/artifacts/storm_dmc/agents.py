"""
ActorCriticAgent for continuous action spaces (DMC).

Key changes vs original STORM:
1. Actor outputs mean + log_std for TanhGaussian policy (not Categorical logits)
2. sample() returns continuous actions in [-1, 1] via tanh squashing
3. update() computes Gaussian log_prob with tanh correction
4. Entropy uses Gaussian entropy as approximation
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.distributions as distributions
from torch.distributions import Normal
import copy
from torch.cuda.amp import autocast

from sub_models.functions_losses import SymLogTwoHotLoss
from utils import EMAScalar


def percentile(x, percentage):
    flat_x = torch.flatten(x)
    kth = max(1, int(percentage * len(flat_x)))
    per = torch.kthvalue(flat_x, kth).values
    return per


def calc_lambda_return(rewards, values, termination, gamma, lam, dtype=torch.float32):
    inv_termination = (termination * -1) + 1
    batch_size, batch_length = rewards.shape[:2]
    gamma_return = torch.zeros((batch_size, batch_length + 1), dtype=dtype, device="cuda")
    gamma_return[:, -1] = values[:, -1]
    for t in reversed(range(batch_length)):
        gamma_return[:, t] = (
            rewards[:, t]
            + gamma * inv_termination[:, t] * (1 - lam) * values[:, t]
            + gamma * inv_termination[:, t] * lam * gamma_return[:, t + 1]
        )
    return gamma_return[:, :-1]


class ActorCriticAgent(nn.Module):
    def __init__(self, feat_dim, num_layers, hidden_dim, action_dim,
                 gamma, lambd, entropy_coef, agent_lr=3e-5) -> None:
        super().__init__()
        self.gamma = gamma
        self.lambd = lambd
        self.entropy_coef = entropy_coef
        self.action_dim = action_dim
        self.use_amp = True
        self.tensor_dtype = torch.bfloat16 if self.use_amp else torch.float32

        self.symlog_twohot_loss = SymLogTwoHotLoss(255, -20, 20)

        # Actor: outputs mean and log_std for TanhGaussian policy
        actor_layers = [
            nn.Linear(feat_dim, hidden_dim, bias=False),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
        ]
        for i in range(num_layers - 1):
            actor_layers.extend([
                nn.Linear(hidden_dim, hidden_dim, bias=False),
                nn.LayerNorm(hidden_dim),
                nn.ReLU(),
            ])
        self.actor_body = nn.Sequential(*actor_layers)
        self.actor_mean = nn.Linear(hidden_dim, action_dim)
        self.actor_log_std = nn.Linear(hidden_dim, action_dim)

        # Critic: same as original (symlog two-hot value)
        critic_layers = [
            nn.Linear(feat_dim, hidden_dim, bias=False),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
        ]
        for i in range(num_layers - 1):
            critic_layers.extend([
                nn.Linear(hidden_dim, hidden_dim, bias=False),
                nn.LayerNorm(hidden_dim),
                nn.ReLU(),
            ])
        self.critic = nn.Sequential(*critic_layers, nn.Linear(hidden_dim, 255))
        self.slow_critic = copy.deepcopy(self.critic)

        self.lowerbound_ema = EMAScalar(decay=0.99)
        self.upperbound_ema = EMAScalar(decay=0.99)

        self.optimizer = torch.optim.Adam(self.parameters(), lr=agent_lr, eps=1e-5)
        self.scaler = torch.cuda.amp.GradScaler(enabled=self.use_amp)

    @torch.no_grad()
    def update_slow_critic(self, decay=0.98):
        for slow_param, param in zip(self.slow_critic.parameters(), self.critic.parameters()):
            slow_param.data.copy_(slow_param.data * decay + param.data * (1 - decay))

    def policy(self, x):
        """Returns (mean, log_std) for the TanhGaussian policy."""
        h = self.actor_body(x)
        mean = self.actor_mean(h)
        log_std = self.actor_log_std(h).clamp(-5.0, 2.0)
        return mean, log_std

    def value(self, x):
        raw_value = self.critic(x)
        return self.symlog_twohot_loss.decode(raw_value)

    @torch.no_grad()
    def slow_value(self, x):
        raw_value = self.slow_critic(x)
        return self.symlog_twohot_loss.decode(raw_value)

    @torch.no_grad()
    def sample(self, latent, greedy=False):
        """
        Sample action from policy. Returns tanh-squashed continuous action.
        latent: (B, 1, feat_dim) or (B, L, feat_dim)
        Returns: (B, 1, action_dim) or (B, L, action_dim) in [-1, 1]
        """
        self.eval()
        with torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=self.use_amp):
            mean, log_std = self.policy(latent)
            if greedy:
                action = torch.tanh(mean)
            else:
                dist = Normal(mean, log_std.exp())
                action = torch.tanh(dist.sample())
        return action

    def sample_as_env_action(self, latent, greedy=False):
        """Returns numpy action for env.step(). Shape: (num_envs, action_dim)."""
        action = self.sample(latent, greedy)
        return action.detach().cpu().squeeze(1).numpy()

    def update(self, latent, action, old_logprob, old_value, reward, termination, logger=None):
        """
        Update policy and value on imagined data.
        latent: (B, T+1, feat_dim)
        action: (B, T, action_dim) — tanh-squashed continuous actions from imagination
        reward: (B, T)
        termination: (B, T)
        """
        self.train()
        with torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=self.use_amp):
            # Actor: compute log_prob and entropy for imagined actions
            mean, log_std = self.policy(latent[:, :-1])  # (B, T, action_dim)
            std = log_std.exp()
            dist = Normal(mean, std)

            # Invert tanh to get pre-squash action for log_prob computation
            pre_tanh = torch.atanh(action.clamp(-0.999, 0.999))
            # Log-prob with tanh correction: log p(a) = log p(u) - sum log(1 - tanh(u)^2)
            log_prob = dist.log_prob(pre_tanh).sum(dim=-1) - torch.log(
                1.0 - action.pow(2) + 1e-6
            ).sum(dim=-1)
            # Gaussian entropy (approximation, ignoring tanh)
            entropy = dist.entropy().sum(dim=-1)

            # Critic: value computation
            raw_value = self.critic(latent)  # (B, T+1, 255)
            slow_value = self.slow_value(latent)
            slow_lambda_return = calc_lambda_return(reward, slow_value, termination, self.gamma, self.lambd)
            value = self.symlog_twohot_loss.decode(raw_value)
            lambda_return = calc_lambda_return(reward, value, termination, self.gamma, self.lambd)

            # Value loss
            value_loss = self.symlog_twohot_loss(raw_value[:, :-1], lambda_return.detach())
            slow_value_reg_loss = self.symlog_twohot_loss(raw_value[:, :-1], slow_lambda_return.detach())

            # Normalized advantage
            lower_bound = self.lowerbound_ema(percentile(lambda_return, 0.05))
            upper_bound = self.upperbound_ema(percentile(lambda_return, 0.95))
            S = upper_bound - lower_bound
            norm_ratio = torch.max(torch.ones(1).cuda(), S)
            norm_advantage = (lambda_return - value[:, :-1]) / norm_ratio

            # Policy loss (REINFORCE-style)
            policy_loss = -(log_prob * norm_advantage.detach()).mean()
            entropy_loss = entropy.mean()

            loss = policy_loss + value_loss + slow_value_reg_loss - self.entropy_coef * entropy_loss

        self.scaler.scale(loss).backward()
        self.scaler.unscale_(self.optimizer)
        torch.nn.utils.clip_grad_norm_(self.parameters(), max_norm=100.0)
        self.scaler.step(self.optimizer)
        self.scaler.update()
        self.optimizer.zero_grad(set_to_none=True)

        self.update_slow_critic()

        if logger is not None:
            logger.log("ActorCritic/policy_loss", policy_loss.item())
            logger.log("ActorCritic/value_loss", value_loss.item())
            logger.log("ActorCritic/entropy_loss", entropy_loss.item())
            logger.log("ActorCritic/S", S.item())
            logger.log("ActorCritic/norm_ratio", norm_ratio.item())
            logger.log("ActorCritic/total_loss", loss.item())
