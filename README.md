# Agentic AI in DevOps — Training AI Like We Train Engineers

Notes and a minimal worked example on **Agentic AI in DevOps**: what turns a script into an "agent," and how the same human-in-the-loop training model used to grow junior DevOps engineers into senior ones applies to training AI agents.

> 📖 Full write-up: [Agentic AI in DevOps: Training AI Like We Train Engineers](https://www.linkedin.com/pulse/agentic-ai-devops-training-like-we-train-engineers-gaurav-khatri-55yrc/) by **Gaurav Khatri**

## From automation to agentic AI

Traditional DevOps automation is rule-based: CI/CD pipelines, shell scripts, Terraform modules, monitoring alerts. **Agentic AI** goes further — it understands a goal, breaks it into tasks, takes actions, observes the results, and learns and adapts. Just like a junior DevOps engineer growing into a senior one.

| Human DevOps engineer | AI agent |
|---|---|
| Training & practice | Prompt + memory |
| SOPs & runbooks | Tool instructions |
| Mentorship | Human feedback |
| Experience | Long-term memory |

## What is an AI agent (not a chatbot)?

An agent has:

- **Goal** — e.g. "Fix production issue"
- **Planner** — decides next steps
- **Tools** — `kubectl`, AWS CLI, Terraform
- **Memory** — remembers past incidents
- **Feedback loop** — learns from outcomes

## Architecture

```
Developer → AI Agent → DevOps Tools → Cloud Infrastructure
    ↑                                        ↓
    └──────────── Human Feedback ←── Observability
```

1. Human defines the goal
2. AI agent plans actions
3. Agent executes via tools
4. System provides feedback
5. Human reviews and improves the agent

## Worked example: a Kubernetes incident

**Human instruction:** "Pods are restarting frequently. Investigate and fix."

**Agent plan:** check pod status → analyze logs → identify root cause → suggest or apply a fix.

```bash
kubectl get pods -n production
kubectl logs api-service-7c9f8
kubectl describe pod api-service-7c9f8
```

**Agent reasoning:** memory limit exceeded → increase the memory request/limit:

```yaml
resources:
  requests:
    memory: "512Mi"
  limits:
    memory: "1Gi"
```

Human approves → agent learns → faster resolution next time.

## Minimal example — see [`health_agent.py`](./health_agent.py)

A beginner-friendly, goal-driven health check agent: it has a role, a goal, a tool, and a human-in-the-loop approval step before it acts — which is what makes it "agentic" rather than just a script.

```python
agent = {
    "role": "DevOps Health Agent",
    "goal": "Ensure application is running",
    "tools": ["kubectl", "slack"],
    "rules": ["Do not restart without approval"],
}
```

| Automation script | Agentic AI |
|---|---|
| Fixed logic | Goal-driven |
| No memory | Learns outcomes |
| No approval flow | Human-in-the-loop |

## Human-in-the-loop is the superpower

Agentic AI does not replace DevOps engineers. It reduces repetitive work, speeds up incident response, and improves reliability — while humans set goals, approve actions, and teach better decisions. AI is the junior engineer; humans are the architects.

## Where it fits today

- CI/CD optimization
- Incident response
- Cost optimization
- Security posture management
- Cloud architecture suggestions

---

**Author:** [Gaurav Khatri](https://www.linkedin.com/in/gaurav-khatri-devops/) — DevOps Engineer @ Sarv.com | Kubernetes (EKS), Docker, GitOps & CI/CD
