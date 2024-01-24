from pathlib import Path

from chatgpt4pcg.competition import chat_with_chatgpt, run_evaluation
from chatgpt4pcg.models.trial_context import TrialContext
from chatgpt4pcg.models.trial_loop import TrialLoop
from dotenv import load_dotenv


class Original(TrialLoop):
    @staticmethod
    def run(ctx: TrialContext, target_character: str) -> str:
        prompt_template = open(Path("prompts/original.txt"), "r").read()
        response = chat_with_chatgpt(ctx, [{"role": "user", "content": prompt_template
                                     .replace("<OBJECT>", target_character)}])
        return response


class FS1(TrialLoop):
    @staticmethod
    def run(ctx: TrialContext, target_character: str) -> str:
        prompt_template = open(Path("prompts/fs1.txt"), "r").read()
        response = chat_with_chatgpt(ctx, [{"role": "user", "content": prompt_template
                                     .replace("<OBJECT>", target_character)}])
        return response


class FS2(TrialLoop):
    @staticmethod
    def run(ctx: TrialContext, target_character: str) -> str:
        prompt_template = open(Path("prompts/fs2.txt"), "r").read()
        response = chat_with_chatgpt(ctx, [{"role": "user", "content": prompt_template
                                     .replace("<OBJECT>", target_character)}])
        return response


class FS3(TrialLoop):
    @staticmethod
    def run(ctx: TrialContext, target_character: str) -> str:
        prompt_template = open(Path("prompts/fs3.txt"), "r").read()
        response = chat_with_chatgpt(ctx, [{"role": "user", "content": prompt_template
                                     .replace("<OBJECT>", target_character)}])
        return response


if __name__ == "__main__":
    load_dotenv()
    run_evaluation("original", Original)
    run_evaluation("fs1", FS1)
    run_evaluation("fs2", FS2)
    run_evaluation("fs3", FS3)
