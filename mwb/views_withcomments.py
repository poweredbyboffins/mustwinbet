import json
import string
import logging
from decimal import *
import neurolab as nl
from django.template import RequestContext
from django.shortcuts import render_to_response
from mwb.models import Games
from mwb.models import Rescut
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ProbForm

logger = logging.getLogger(__name__)

def prob_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProbForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            probval = form.cleaned_data['prob']
            limitval = form.cleaned_data['results']
            print(probval)
            context = RequestContext(request)
            games_list = Games.objects.raw(" select row_number() OVER (ORDER BY greatest(winprob,loseprob) DESC) AS i, id, replace(lower(hometeam),' ','') as hometeam,replace(lower(awayteam),' ','') as awayteam,winprob,drawprob,loseprob,matchdate from gamepred where active_ind='Y' and (winprob >  %s or loseprob > %s) order by greatest(winprob,loseprob) desc limit %s",[probval,probval,limitval]) 
            games_dict = {'gameinfo' : games_list }
            return render_to_response('mwb/summary.html', games_dict, context)
            #summaryprob(request,probability)
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProbForm()

    return render(request, 'mwb/prob.html', {'form': form})

def index(request):
    context = RequestContext(request)
    #games_list = Games.objects.all()
    fplist = Games.objects.raw("select id,title,blurb from frontpage order by id") 
    fpdict = {'gameinfo' : fplist }
    return render_to_response('mwb/index.html', fpdict, context)
    #return render_to_response('mwb/index.html', {"obj_as_json": json.dumps(games_dict)})

def bet(request,data):
    context = RequestContext(request)
    data,bet = string.split(data,'&')
    data = string.replace(data,'_',' v ')
    return render_to_response('mwb/testarray.html', {'posts': data.split(","),'betcomp':bet}, context)

def summary(request,page):
    context = RequestContext(request)
    #games_list = Games.objects.all()
    print(page)
    if page=='6':
        games_list = Games.objects.raw(" select row_number() OVER (ORDER BY greatest(winprob,loseprob) DESC) AS i, id, replace(lower(hometeam),' ','') as hometeam,replace(lower(awayteam),' ','') as awayteam,winprob,drawprob,loseprob,matchdate,pctwin,pctnotwin,homeformadj,awayformadj,resultcomment(hometeam,awayteam,matchdate - integer '240',matchdate) commentary from gamepred where active_ind='Y' and winprob is not null order by greatest(winprob,loseprob) desc") 
    elif page=='1':
        games_list = Games.objects.raw(" select row_number() OVER (ORDER BY greatest(winprob,loseprob) DESC) AS i, id, replace(lower(hometeam),' ','') as hometeam,replace(lower(awayteam),' ','') as awayteam,winprob,drawprob,loseprob,matchdate,pctwin,pctnotwin,homeformadj,awayformadj,resultcomment(hometeam,awayteam,matchdate - integer '240',matchdate) commentary from gamepred where active_ind='Y' and winprob is not null order by greatest(winprob,loseprob) desc limit 10") 
    elif page=='2':
        games_list = Games.objects.raw(" select row_number() OVER (ORDER BY greatest(winprob,loseprob) DESC) AS i, id, replace(lower(hometeam),' ','') as hometeam,replace(lower(awayteam),' ','') as awayteam,winprob,drawprob,loseprob,matchdate,pctwin,pctnotwin,homeformadj,awayformadj,resultcomment(hometeam,awayteam,matchdate - integer '240',matchdate) commentary from gamepred where active_ind='Y' and winprob is not null order by greatest(winprob,loseprob) desc limit 5") 
    else: 
        games_list = Games.objects.raw(" select row_number() OVER (ORDER BY greatest(winprob,loseprob) DESC) AS i, id, replace(lower(hometeam),' ','') as hometeam,replace(lower(awayteam),' ','') as awayteam,winprob,drawprob,loseprob,matchdate,pctwin,pctnotwin,homeformadj,awayformadj,resultcomment(hometeam,awayteam,matchdate - integer '240',matchdate) commentary from gamepred where active_ind='Y' and (winprob > 50 or loseprob > 50) order by greatest(winprob,loseprob) desc limit 24") 
    games_dict = {'gameinfo' : games_list }
    return render_to_response('mwb/summary.html', games_dict, context)

def summaryprob(request,probval):
    context = RequestContext(request)

    games_list = Games.objects.raw(" select row_number() OVER (ORDER BY greatest(winprob,loseprob) DESC) AS i, id, replace(lower(hometeam),' ','') as hometeam,replace(lower(awayteam),' ','') as awayteam,winprob,drawprob,loseprob,matchdate from gamepred where active_ind='Y' and (winprob > probval or loseprob > probval) order by greatest(winprob,loseprob) desc limit 24") 
    games_dict = {'gameinfo' : games_list }
    return render_to_response('mwb/summary.html', games_dict, context)

def register(request):
    context = RequestContext(request)
    #games_list = Games.objects.all()
    fplist = Games.objects.raw("select id,type,blurb from register order by id") 
    fpdict = {'reginfo' : fplist }
    return render_to_response('mwb/register.html', fpdict, context)
    #return render_to_response('mwb/index.html', {"obj_as_json": json.dumps(games_dict)})

def register_sesh(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/books/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

def ann(request):
    context = RequestContext(request)
    # query the database
    # get factors for games

    # Train Data
    games_list = Rescut.objects.raw("select  id ,HomeTeam ,AwayTeam ,MatchDate ,FTHG ,FTAG , case FTR when 'H' then 1 when 'A' then 2 else 0.5 end ftr,coalesce(winprob,0) winprob,coalesce(drawprob,0) drawprob ,coalesce(loseprob,0) loseprob ,pctwin ,pctnotwin from factordata where matchdate <='30-oct-2014'") 

    #games_dict = {'gameinfo' : games_list }
    list1 = []
    tgtlist = []
    inputlist = []
    inputlist2 = []
    target = []
    list2 = []
    out = []
    x=0

    #input = [[0.6, 0.3,0.3], [0.7, 0.4,0.2], [0.2, 0.8,0.1], [0.2, 0.6,0.2]]
    #target = [[1], [1], [0], [0]]
    #target = [[1]]

    for i in range(90):
        list1[:]=[]
        tgtlist[:]=[]
        list1.append(games_list[i].winprob)
        list1.append(games_list[i].drawprob)
        list1.append(games_list[i].loseprob)
        list1.append(games_list[i].pctwin)
        list1.append(games_list[i].pctnotwin)
        inputlist.append(list1) 
        #del list1[:]
        #print inputlist
        tgtlist.append(games_list[i].ftr)
        target.append(tgtlist)
        x=x+1

    # Create net with 5 inputs and 1 neuron
    net = nl.net.newp([[0,100],[0,100],[0,100],[0,100],[0,100]],1)
    #net = nl.net.newp([[0,100]],1)

    # train with delta rule
    # see net.trainf
    error = net.train(inputlist, target, epochs=1000, show=100, lr=0.1)
    logger.error(error);
    #print inputlist[0]

    
    # Test Data
    testlist = Rescut.objects.raw("select  id ,HomeTeam ,AwayTeam ,MatchDate ,FTHG ,FTAG , case FTR when 'H' then 2 when 'A' then 1 else 0 end ftr,winprob ,drawprob ,loseprob ,pctwin ,pctnotwin from factordata where matchdate >'30-oct-2014'") 
    

    #test = [[0.2,0.7,0.1]]
    #out = net.sim(test)
    x=0
    for i in range(30):
        list2[:]=[]
        inputlist2[:]=[]
        list2.append(testlist[i].winprob)
        list2.append(testlist[i].drawprob)
        list2.append(testlist[i].loseprob)
        list2.append(testlist[i].pctwin)
        list2.append(testlist[i].pctnotwin)
        inputlist2.append(list2) 
        logger.error(testlist[i].hometeam + ' ' + testlist[i].awayteam)
        out=net.sim(inputlist2)
        logger.error(list2)
        logger.error(out)
        x+=1
#        
    outdict = {'annresult' :  out}

    #outdict = {'annresult' :  x}
    #outdict = {'annresult' :  inputlist}
    #outdict = {'annresult' :  inputlist}
    #outdict = {'annresult' :  games_list}
    return render_to_response('mwb/ann.html', outdict, context)
