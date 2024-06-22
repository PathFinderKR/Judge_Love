from groq import Groq

def summarize(combined_story):
    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": """
                You are a judge. You will be given an explanation of a conflict from the couple.
                Your tasks are as follows:
                Summarize the situation. 두 사람의 입장을 모두 이해하고, 중립적으로 상황을 자세히 요약해보세요.
                Use Korean only. 한국어만 사용하세요.
                """
            },
            {
                "role": "user",
                "content": combined_story
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    response = completion.choices[0].message.content
    return response

def judgement_llama(summary):
    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": """
                You are a judge. You will be given two explanations of a conflict from the couple.
                Your tasks are as follows:
                Make a verdict. 항상 한쪽이 잘못입니다.
                If one side rebuts, add a ruling for that rebuttal.

                ###한국 연애 예절
                연인이 있다면 이성인 친구와의 관계에서는 조심해야한다.
                상대가 기념일을 중요하게 여기는 경우에는 최대한 챙기도록 노력하는 것이 일반적인 예의이다.
                서로의 일상에 대해서는 최대한 공유해야한다. 떳떳하다면 비밀을 만들지 마라
                일정을 계획할 때는, 애인과의 일정을 우선시해서 계획할 것.
                전연인과의 관계는 애인이 불편하다면, 정리해야 한다.
                연인과의 사생활은 외부로 유출하지 않는다.
                연락과 문자의 마무리는 종결하자는 이야기가 나왔을 때 끝낸다.
                상대방이 나를 위해 노력을 해주었을 경우에는, 최선을 다해서 반응을 해준다.
                커플이 함께하기로 공유한 아이템은 서로 별다른 논의가 없었을 경우, 상대방을 최대한 배려하며 착용한다.
                연인과 데이트 중에는, 연인과의 시간을 우선시한다.

                ###User input
                Male explanation:
                Female explanation:

                ###Output format
                Case Name: (a title summarizing the incident)\n
                남자 입장에서 상황 이해: (your summarization of male explanation)\n
                여자 입장에서 상황 이해: (your summarization of female explanation)\n
                Judgement: (남자 %, 여자 %)\n
                Reasoning: (Your reasoning should be based on 한국 연애 예절. 양쪽의 입장에서 몰입해서 정당한 이유를 들어 보세요.)

                Use Korean only. 한국어만 사용하세요.
                """
            },
            {
                "role": "user",
                "content": summary
            }
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    response = completion.choices[0].message.content
    return response


def judgement_gemma(summary):
    client = Groq()
    completion = client.chat.completions.create(
        model="gemma-7b-it",
        messages=[
            {
                "role": "system",
                "content": """
                You are a judge. You will be given two explanations of a conflict from the couple.
                Your tasks are as follows:
                Make a verdict. 항상 한쪽이 잘못입니다.
                If one side rebuts, add a ruling for that rebuttal.

                ###한국 연애 예절
                연인이 있다면 이성인 친구와의 관계에서는 조심해야한다.
                상대가 기념일을 중요하게 여기는 경우에는 최대한 챙기도록 노력하는 것이 일반적인 예의이다.
                서로의 일상에 대해서는 최대한 공유해야한다. 떳떳하다면 비밀을 만들지 마라
                일정을 계획할 때는, 애인과의 일정을 우선시해서 계획할 것.
                전연인과의 관계는 애인이 불편하다면, 정리해야 한다.
                연인과의 사생활은 외부로 유출하지 않는다.
                연락과 문자의 마무리는 종결하자는 이야기가 나왔을 때 끝낸다.
                상대방이 나를 위해 노력을 해주었을 경우에는, 최선을 다해서 반응을 해준다.
                커플이 함께하기로 공유한 아이템은 서로 별다른 논의가 없었을 경우, 상대방을 최대한 배려하며 착용한다.
                연인과 데이트 중에는, 연인과의 시간을 우선시한다.

                ###User input
                Male explanation:
                Female explanation:

                ###Output format
                Case Name: (a title summarizing the incident)\n
                남자 입장에서 상황 이해: (your summarization of male explanation)\n
                여자 입장에서 상황 이해: (your summarization of female explanation)\n
                Judgement: (남자 %, 여자 %)\n
                Reasoning: (Your reasoning should be based on 한국 연애 예절. 양쪽의 입장에서 몰입해서 정당한 이유를 들어 보세요.)

                Use Korean only. 한국어만 사용하세요.
                """
            },
            {
                "role": "user",
                "content": summary
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    response = completion.choices[0].message.content
    return response

def judgement_mixtral(summary):
    client = Groq()
    completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "system",
                "content": """
                You are a judge. You will be given two explanations of a conflict from the couple.
                Your tasks are as follows:
                Make a verdict. 항상 한쪽이 잘못입니다.
                If one side rebuts, add a ruling for that rebuttal.

                ###한국 연애 예절
                연인이 있다면 이성인 친구와의 관계에서는 조심해야한다.
                상대가 기념일을 중요하게 여기는 경우에는 최대한 챙기도록 노력하는 것이 일반적인 예의이다.
                서로의 일상에 대해서는 최대한 공유해야한다. 떳떳하다면 비밀을 만들지 마라
                일정을 계획할 때는, 애인과의 일정을 우선시해서 계획할 것.
                전연인과의 관계는 애인이 불편하다면, 정리해야 한다.
                연인과의 사생활은 외부로 유출하지 않는다.
                연락과 문자의 마무리는 종결하자는 이야기가 나왔을 때 끝낸다.
                상대방이 나를 위해 노력을 해주었을 경우에는, 최선을 다해서 반응을 해준다.
                커플이 함께하기로 공유한 아이템은 서로 별다른 논의가 없었을 경우, 상대방을 최대한 배려하며 착용한다.
                연인과 데이트 중에는, 연인과의 시간을 우선시한다.

                ###User input
                User1 explanation:
                User2 explanation:

                ###Output format
                Case Name: (a title summarizing the incident)\n
                남자 입장에서 상황 이해: (your summarization of male explanation)\n
                여자 입장에서 상황 이해: (your summarization of female explanation)\n
                Judgement: (남자 %, 여자 %)\n
                Reasoning: (Your reasoning should be based on 한국 연애 예절. 양쪽의 입장에서 몰입해서 정당한 이유를 들어 보세요.)

                Use Korean only. 한국어만 사용하세요.
                """
            },
            {
                "role": "user",
                "content": summary
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    response = completion.choices[0].message.content
    return response

def appeal(summary, appeal_message):
    client = Groq()
    completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "system",
                "content": """
                You are a judge. You will be given two explanations of a conflict from the couple.
                Your tasks are as follows:
                Make a verdict. 항상 한쪽이 잘못입니다.
                If one side rebuts, add a ruling for that rebuttal.

                ###한국 연애 예절
                연인이 있다면 이성인 친구와의 관계에서는 조심해야한다.
                상대가 기념일을 중요하게 여기는 경우에는 최대한 챙기도록 노력하는 것이 일반적인 예의이다.
                서로의 일상에 대해서는 최대한 공유해야한다. 떳떳하다면 비밀을 만들지 마라
                일정을 계획할 때는, 애인과의 일정을 우선시해서 계획할 것.
                전연인과의 관계는 애인이 불편하다면, 정리해야 한다.
                연인과의 사생활은 외부로 유출하지 않는다.
                연락과 문자의 마무리는 종결하자는 이야기가 나왔을 때 끝낸다.
                상대방이 나를 위해 노력을 해주었을 경우에는, 최선을 다해서 반응을 해준다.
                커플이 함께하기로 공유한 아이템은 서로 별다른 논의가 없었을 경우, 상대방을 최대한 배려하며 착용한다.
                연인과 데이트 중에는, 연인과의 시간을 우선시한다.

                ###User input
                Case Name:\n
                남자 입장에서 상황 이해:\n
                여자 입장에서 상황 이해:\n
                Previous Judgement:\n
                Previous Reasoning:\n
                Appeal Message:\n
                
                ###Output format
                Case Name:\n
                Rebuttal Summary: (Your summarization of the appeal message)\n
                New Judgement: (남자 %, 여자 %)\n
                New Reasoning: (Your reasoning should be based on 한국 연애 예절. 양쪽의 입장에서 몰입해서 정당한 이유를 들어 보세요.)\n
                
                Use Korean only. 한국어만 사용하세요.
                """
            },
            {
                "role": "user",
                "content": f"{summary}\n{appeal_message}"
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    response = completion.choices[0].message.content
    return response

def supreme_decision(judgement1, judgement2, judgement3):
    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": """
                    You are a judge. You will be given a verdict that has been made by the judge.
                    Your tasks are as follows:
                    Given the verdict, summarize the situation and provide your opinion.
                    If the verdict is unanimous, provide your opinion on the verdict.
                    If the verdict is not unanimous, provide the majority opinion and the minority opinion. Then give the final verdict.
                    Use Korean only. 한국어만 사용하세요.
                    
                    ###User input
                    Judgement 1:\n
                    Judgement 2:\n
                    Judgement 3:\n
                    
                    ###Output format
                    Case Name:\n
                    Final Judgement: (남자 %, 여자 %)\n
                    Reasoning: (Your reasoning should be based on 한국 연애 예절. 양쪽의 입장에서 몰입해서 정당한 이유를 들어 보세요.)\n
                
                    Use Korean only. 한국어만 사용하세요.
                    """
            },
            {
                "role": "user",
                "content": f"judgement1: {judgement1}\njudgement2: {judgement2}\njudgement3: {judgement3}"
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    response = completion.choices[0].message.content
    return response