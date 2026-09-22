"""A very simple, beginner-friendly agentic AI example.

Goal: "Check application health and alert if something is wrong."

This is deliberately tiny: it has a goal, observes state, and decides an
action -- which is what makes it "agentic" rather than a plain script.
A restart is never taken automatically; it always waits for a human
in-the-loop approval, and remembers the decision for next time.
"""

from dataclasses import dataclass, field


agent = {
    "role": "DevOps Health Agent",
    "goal": "Ensure application is running",
    "tools": ["kubectl", "slack"],
    "rules": ["Do not restart without approval"],
}


@dataclass
class Memory:
    """Very small long-term memory: which past issues were approved to auto-fix."""

    approved_actions: set = field(default_factory=set)

    def remember(self, issue_signature: str) -> None:
        self.approved_actions.add(issue_signature)

    def was_previously_approved(self, issue_signature: str) -> bool:
        return issue_signature in self.approved_actions


def kubectl(command: str) -> str:
    """Stand-in for a real kubectl call -- replace with subprocess.run in production."""
    print(f"$ kubectl {command}")
    return "Running"  # or "CrashLoopBackOff", "Pending", ...


def notify(channel: str, message: str) -> None:
    print(f"[{channel}] {message}")


def ask_human(question: str) -> bool:
    """Human-in-the-loop approval gate."""
    answer = input(f"{question} [y/N] ").strip().lower()
    return answer == "y"


def run_health_agent(pod_name: str, memory: Memory) -> None:
    status = kubectl(f"get pod {pod_name}")

    if status == "Running":
        print(f"{pod_name}: healthy, nothing to do.")
        return

    notify("Slack", f"{pod_name} is down (status={status})")

    issue_signature = f"{pod_name}:{status}"
    if memory.was_previously_approved(issue_signature):
        print("This exact issue was approved before -- restarting automatically.")
        kubectl(f"rollout restart deployment {pod_name}")
        return

    if ask_human(f"{pod_name} is not running. Can I restart it?"):
        kubectl(f"rollout restart deployment {pod_name}")
        memory.remember(issue_signature)
        print("Restarted, and remembered: this issue is safe to auto-restart next time.")
    else:
        print("No action taken. Waiting for human investigation.")


if __name__ == "__main__":
    memory = Memory()
    run_health_agent("api-service", memory)
