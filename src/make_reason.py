import time
import openai


openai.api_key = 'API_KEY'  # 请替换为你的OpenAI API key

class Reason:
    @staticmethod
    def generate_answer_general(memory, player, model):
        prompt = [
            {
                "role": "system",
                "content": f"""あなたはゲームの参加者の'{player}'であり、人間だと思われているplayerを探し出す必要があります。
                如何にします会話データから、人間だと考えるplayerとその理由を返答してください。
                出力は日本語でお願いします。過去の発言は如何に示す通りです。'{memory}'"""
            },
        ]

        response = openai.ChatCompletion.create(
            model=model,
            messages=prompt,
            temperature=0.5,
            max_tokens=100,
        )
        answer = response['choices'][0]['message']['content']
        if '。' in answer:
            answer = answer[:answer.rfind('。')+1]
        return answer
    
    @staticmethod
    def read_file():
        with open("dialogue.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            print(lines)
        return lines

    @staticmethod
    def make_reason():
        player_functions = [
            "player1",
            "player2",
        ]

        messages = []  # メッセージを保持するリスト

        for round_num in range(1):
            print(f"\n--- Round {round_num+1} ---")
            id_number = 0
            with open("history.txt", "a", encoding="utf-8") as file:
                for i in range(len(player_functions)):
                    print(i)
                    id_number += 1
                    player = "player" + str(i+1)
                    memory = "".join(Reason.read_file())
                    answer = Reason.generate_answer_general(memory, player, model="gpt-3.5-turbo")
                    print(answer)
                    dialogueText = f"{player}:{answer}"
                    messages.append({
                        "id": id_number,
                        "text": answer,
                    })
                    file.write(answer + "\n")
                    with open("dialogue.txt", "a", encoding="utf-8") as dialogue_file:
                        dialogue_file.write(dialogueText + "\n")

                    time.sleep(2)

        return messages