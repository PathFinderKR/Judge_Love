from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Story
from .forms import StoryForm
from .utils import summarize, judgement_llama, judgement_gemma, judgement_mixtral, appeal, supreme_decision
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import io
import urllib, base64

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 윈도우 환경에서 사용할 수 있는 한글 폰트
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

MAX_APPEALS = 3  # 최대 항소 횟수

@login_required
def story_view(request):
    user_story = Story.objects.filter(author=request.user).first()
    partner_story = Story.objects.exclude(author=request.user).first()

    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            if user_story:
                user_story.text = form.cleaned_data['text']
                user_story.save()
            else:
                user_story = form.save(commit=False)
                user_story.author = request.user
                user_story.save()

            if partner_story:
                return redirect('result')
            return redirect('story')

    else:
        form = StoryForm(instance=user_story)

    waiting_for_partner = not partner_story

    return render(request, 'stories/story.html', {
        'form': form,
        'user_story': user_story,
        'waiting_for_partner': waiting_for_partner,
    })

@login_required
def result_view(request):
    user_story = Story.objects.filter(author=request.user).first()
    partner_story = Story.objects.exclude(author=request.user).first()

    if user_story and partner_story:
        combined_story = f"User 1: {user_story.text}\n\nUser 2: {partner_story.text}"
        try:
            summary = summarize(combined_story)
            judgement_result = judgement_llama(summary)
            male_percentage, female_percentage = extract_percentages(judgement_result)

            fig, ax = plt.subplots()
            ax.bar(['Male', 'Female'], [male_percentage, female_percentage], color=['blue', 'green'])
            ax.set_ylabel('잘못의 비율 (%)')
            ax.set_title('잘못의 비율 비교')

            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            string = base64.b64encode(buf.read())
            uri = urllib.parse.quote(string)

            appeal_messages = request.session.get('appeal_messages', [])
            appeal_results = request.session.get('appeal_results', [])
            appeal_graphs = request.session.get('appeal_graphs', [])

            appeals = zip(appeal_messages, appeal_results, appeal_graphs)

            request.session['graph'] = uri

            return render(request, 'stories/result.html', {
                'user_story': user_story,
                'summary': summary,
                'judgement_result': judgement_result,
                'graph': uri,
                'appeals': appeals,
                'remaining_appeals': MAX_APPEALS - user_story.appeal_count
            })
        except Exception as e:
            print(f"Error: {e}")

    return redirect('story')

def extract_percentages(judgement_result):
    import re
    pattern = r'남자\s*(\d+)%\s*,\s*여자\s*(\d+)%'
    match = re.search(pattern, judgement_result)
    if match:
        male_percentage = int(match.group(1))
        female_percentage = int(match.group(2))
        return male_percentage, female_percentage
    return 0, 0

@login_required
def appeal_view(request):
    user_story = Story.objects.filter(author=request.user).first()
    if user_story.appeal_count >= MAX_APPEALS:
        return redirect('result')

    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['text']
            partner_story = Story.objects.exclude(author=request.user).first()
            combined_story = f"User 1: {user_story.text}\n\nUser 2: {partner_story.text}"
            summary = summarize(combined_story)
            previous_judgement_result = judgement_llama(summary)

            try:
                appeal_result = appeal(previous_judgement_result, user_message)
                male_percentage, female_percentage = extract_percentages(appeal_result)

                fig, ax = plt.subplots()
                ax.bar(['Male', 'Female'], [male_percentage, female_percentage], color=['blue', 'green'])
                ax.set_ylabel('잘못의 비율 (%)')
                ax.set_title('잘못의 비율 비교')

                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                string = base64.b64encode(buf.read())
                appeal_uri = urllib.parse.quote(string)

                appeal_messages = request.session.get('appeal_messages', [])
                appeal_results = request.session.get('appeal_results', [])
                appeal_graphs = request.session.get('appeal_graphs', [])
                appeal_messages.append(user_message)
                appeal_results.append(appeal_result)
                appeal_graphs.append(appeal_uri)
                request.session['appeal_messages'] = appeal_messages
                request.session['appeal_results'] = appeal_results
                request.session['appeal_graphs'] = appeal_graphs

                appeals = zip(appeal_messages, appeal_results, appeal_graphs)

                user_story.appeal_count += 1
                user_story.save()

                return render(request, 'stories/result.html', {
                    'user_story': user_story,
                    'summary': summary,
                    'judgement_result': previous_judgement_result,
                    'graph': request.session.get('graph'),
                    'appeals': appeals,
                    'remaining_appeals': MAX_APPEALS - user_story.appeal_count
                })
            except Exception as e:
                print(f"Error: {e}")

    return redirect('story')

@login_required
def supreme_appeal_view(request):
    if request.method == 'POST':
        user_story = Story.objects.filter(author=request.user).first()
        partner_story = Story.objects.exclude(author=request.user).first()

        if user_story and partner_story:
            combined_story = f"User 1: {user_story.text}\n\nUser 2: {partner_story.text}"
            try:
                summary = summarize(combined_story)
                judgement1 = judgement_llama(summary)
                judgement2 = judgement_gemma(summary)
                judgement3 = judgement_mixtral(summary)
                supreme_result = supreme_decision(judgement1, judgement2, judgement3)

                male_percentage, female_percentage = extract_percentages(supreme_result)

                fig, ax = plt.subplots()
                ax.bar(['Male', 'Female'], [male_percentage, female_percentage], color=['blue', 'green'])
                ax.set_ylabel('잘못의 비율 (%)')
                ax.set_title('최종 잘못의 비율 비교')

                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                string = base64.b64encode(buf.read())
                supreme_graph = urllib.parse.quote(string)

                return render(request, 'stories/supreme_result.html', {
                    'user_story': user_story,
                    'supreme_result': supreme_result,
                    'supreme_graph': supreme_graph
                })
            except Exception as e:
                print(f"Error: {e}")

    return redirect('result')
