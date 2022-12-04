from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer

bot = ChatBot('chatbot',read_only=False,logic_adapters=[
                            {
                                'import_path':'chatterbot.logic.bestMatch',
                                'default_response':'Sorry, I do not know!!',
                                'maximun_similariyt_threshaold':0.95
                                
                            }])

list_to_train=[
    "hi",#question
    "hi,there",#answer
    "What's your Namee?",
    "I'm just a Chatbot.",
    "What is your fav food?",
    "I like Cheese burger!!!",
    "What's your fav Sport?",
    "I really like Cricket and Football!!",
    "What's your fav music genre??",
    "I really like rap music like eminem,nas,divine,krsna...all fav!!",
]

chatterbotcorpustrainer=ChatterBotCorpusTrainer(bot)
# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)
chatterbotcorpustrainer.train('chatterbot.corpus.english')


def index(request):
    return render(request,'blog/index.html')

def specific(request):
    return HttpResponse("This is the specific url")

#def article(request,article_id):
#    return render(request,'blog/index.html',{'article_id':article_id})

def getResponse(request):
    userMessage=request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)

