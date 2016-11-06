import json
from django.http import JsonResponse
import string
import logging
from django.contrib import auth
from django.contrib.auth.models import User
from decimal import *
#import neurolab as nl
from django.template import RequestContext
from django.shortcuts import render_to_response
from mwb.models import Games
from mwb.models import Results
from mwb.models import Rescut
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ProbForm
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.db import connection
import pandas as pd
#from mwb.pandata import *
#from mwb.pandcls import *

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
    data,bet = data.split('&')
    data = data.replace('_',' v ')
    return render_to_response('mwb/testarray.html', {'posts': data.split(","),'betcomp':bet}, context)

def summary(request,page):
    context = RequestContext(request)
    #games_list = Games.objects.all()
    print(page)
    if page=='6':
        games_list = Games.objects.raw("select row_number() OVER (ORDER BY greatest(result,result2) DESC) AS i, id,hometeam,awayteam,winprob,drawprob,loseprob,matchdate,pctwin,pctnotwin,homeformadj,awayformadj,commentary from predview where er<>'X' order by greatest(result,result2) desc") 
    elif page=='1':
         #games_list = Games.objects.raw("select row_number() OVER (ORDER BY greatest(result,result2) DESC) AS i, id,hometeam,awayteam,winprob,drawprob,loseprob,matchdate,pctwin,pctnotwin,homeformadj,awayformadj,commentary from predview where er<>'X' order by greatest(result,result2) desc limit 10")
         games_list = Games.objects.raw("select row_number() OVER (ORDER BY PRED DESC) as i,'' id,hometeam,awayteam,0 winprob,0 drawprob,0 loseprob,matchdate,0 ptcwin,0 pctnotwin,0 homeformadj,0 awayformadj,commentary  from pred where abs(pred) > 40 and data_type='RESULT' and matchdate between current_date and current_date + integer '6' " )
    elif page=='2':
         #games_list = Games.objects.raw("select row_number() OVER (ORDER BY result DESC) AS i, id,hometeam,awayteam,winprob,drawprob,loseprob,matchdate,pctwin,pctnotwin,homeformadj,awayformadj,commentary from predview where er='H' order by result desc limit 10")
         games_list = Games.objects.raw("select row_number() OVER (ORDER BY p1.PRED DESC) as i,0 id,p1.hometeam,p1.awayteam,0 winprob,0 drawprob,0 loseprob,p1.matchdate,0 ptcwin,0 pctnotwin,0 homeformadj,0 awayformadj,'Lay Favourite or Draw' commentary from pred p1 where data_type='RESULT' and abs(pred) < 40 and matchdate between current_date and current_date + integer '6'")
    elif page=='3':
         #games_list = Games.objects.raw("select row_number() OVER (ORDER BY result2 DESC) AS i, id,hometeam,awayteam,winprob,drawprob,loseprob,matchdate,pctwin,pctnotwin,homeformadj,awayformadj,'' commentary from predview where er='A' order by result2 desc limit 10")
         games_list = Games.objects.raw("select row_number() OVER (ORDER BY PRED DESC) as i,'' id,hometeam,awayteam,0 winprob,0 drawprob,0 loseprob,matchdate,0 ptcwin,0 pctnotwin,0 homeformadj,0 awayformadj,commentary  from pred where data_type='GOALS' and matchdate between current_date and current_date + integer '6'")
    elif page=='4':
         #games_list = Games.objects.raw("select row_number() OVER (ORDER BY result3 DESC) AS i, id,hometeam,awayteam,winprob,drawprob,loseprob,matchdate,pctwin,pctnotwin,homeformadj,awayformadj,commentary from predview where er<>'X' order by result3 desc limit 10")
         games_list = Games.objects.raw("select row_number() OVER (ORDER BY p1.PRED DESC) as i,0 id,p1.hometeam,p1.awayteam,0 winprob,0 drawprob,0 loseprob,p1.matchdate,0 pctwin,0 pctnotwin,0 homeformadj,0 awayformadj,'Score Prediction '||cast(cast((p2.pred+p1.pred)/200 as integer) as varchar(10))||'-'||cast(cast((p2.pred-p1.pred)/200 as integer) as varchar(10)) commentary from pred p1 inner join pred p2 on p1.hometeam=p2.hometeam and p1.awayteam=p2.awayteam and p1.data_type='GOALS' and p2.data_type='RESULT' and p1.matchdate=p2.matchdate and p1.matchdate between current_date and current_date + integer '6'")
    elif page=='5':
         games_list = Games.objects.raw("select row_number() OVER (ORDER BY result4 DESC) AS i, id,hometeam,awayteam,winprob,drawprob,loseprob,matchdate,pctwin,pctnotwin,homeformadj,awayformadj,commentary from predview order by result4 desc limit 10")
    else: 
        games_list = Games.objects.raw(" select row_number() OVER (ORDER BY greatest(winprob,loseprob) DESC) AS i, id, replace(lower(hometeam),' ','') as hometeam,replace(lower(awayteam),' ','') as awayteam,winprob,drawprob,loseprob,matchdate,pctwin,pctnotwin,homeformadj,awayformadj,commentary from gamepred where active_ind='Y' and (winprob > 50 or loseprob > 50) order by greatest(winprob,loseprob) desc limit 24") 
    games_dict = {'gameinfo' : games_list }
    return render_to_response('mwb/summary.html', games_dict, context)

def acca(request):
    context = RequestContext(request)
    games_list = Games.objects.raw("select row_number() OVER (ORDER BY PRED DESC) as i,'' id,hometeam,awayteam,0 winprob,0 drawprob,0 loseprob,matchdate,0 ptcwin,0 pctnotwin,0 homeformadj,0 awayformadj,commentary  from pred where abs(pred) > 40 and data_type='RESULT' and matchdate between current_date and current_date + integer '6' " )
    games_dict = {'gameinfo' : games_list }
    return render_to_response('mwb/summary.html', games_dict, context)

def shocks(request):
    context = RequestContext(request)
    games_list = Games.objects.raw("select row_number() OVER (ORDER BY p1.PRED DESC) as i,0 id,p1.hometeam,p1.awayteam,0 winprob,0 drawprob,0 loseprob,p1.matchdate,0 ptcwin,0 pctnotwin,0 homeformadj,0 awayformadj,'Lay Favourite or Draw' commentary from pred p1 where data_type='RESULT' and abs(pred) < 40 and matchdate between current_date and current_date + integer '6'")
    games_dict = {'gameinfo' : games_list }
    return render_to_response('mwb/summary.html', games_dict, context)

def goals(request):
    context = RequestContext(request)
    games_list = Games.objects.raw("select row_number() OVER (ORDER BY PRED DESC) as i,'' id,hometeam,awayteam,0 winprob,0 drawprob,0 loseprob,matchdate,0 ptcwin,0 pctnotwin,0 homeformadj,0 awayformadj,commentary  from pred where data_type='GOALS' and matchdate between current_date and current_date + integer '6'")
    games_dict = {'gameinfo' : games_list }
    return render_to_response('mwb/summary.html', games_dict, context)

def exact_score(request):
    context = RequestContext(request)
    games_list = Games.objects.raw("select row_number() OVER (ORDER BY p1.PRED DESC) as i,0 id,p1.hometeam,p1.awayteam,0 winprob,0 drawprob,0 loseprob,p1.matchdate,0 pctwin,0 pctnotwin,0 homeformadj,0 awayformadj,'Score Prediction '||cast(cast((p2.pred+p1.pred)/200 as integer) as varchar(10))||'-'||cast(cast((p2.pred-p1.pred)/200 as integer) as varchar(10)) commentary from pred p1 inner join pred p2 on p1.hometeam=p2.hometeam and p1.awayteam=p2.awayteam and p1.data_type='GOALS' and p2.data_type='RESULT' and p1.matchdate=p2.matchdate and p1.matchdate between current_date and current_date + integer '6'")
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
    return render(request, "mwb/registration/login.html", {
        'form': form,
    })

"""
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
"""
@login_required(login_url='accounts/login2/')
def indepth2(request,data):
    context = RequestContext(request)
    home,away = string.split(data,'&')
    print(home)
    print(away)
    games_list = Games.objects.raw("select 1, id,hometeam,awayteam,winprob,drawprob,loseprob,matchdate,pctwin,pctnotwin,homeformadj,awayformadj,commentary from predview where hometeam =%s and awayteam=%s",[home,away])
    #games_list = Games.objects.raw(v_sql)
    #data = string.replace(data,'_',' v ')
    games_dict = {'gameinfo' : games_list }
    return render_to_response('mwb/indepth.html', games_dict, context)

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(list(zip([col[0] for col in desc], row)))
        for row in cursor.fetchall()
    ]
def indepth(request,data):
    home,away = string.split(data,'&')
    if not request.user.is_authenticated():
        form = UserCreationForm()
        return render(request, "mwb/registration/login.html", {
        'form': form,'home':home,'away':away
        })

    else:
       context = RequestContext(request)
       games_list = Games.objects.raw("select 1, id,hometeam,awayteam,winprob,drawprob,loseprob,matchdate,pctwin,pctnotwin,homeformadj,awayformadj,commentary from predview where hometeam =%s and awayteam=%s",[home,away])
       #games_list = Games.objects.raw(v_sql)
       #data = string.replace(data,'_',' v ')
       #home_mov_avg = Results.objects.raw("select mov_avg_form(%s,current_date) ftr",[home])
       cursor = connection.cursor()
       cursor.execute("select mov_avg_form(%s,current_date) homeavg",[home])
       #home_mov_avg = dictfetchall(cursor)  
       home_mov_avg = [item[0] for item in cursor.fetchall()]
       cursor.execute("select mov_avg_form(%s,current_date) awayavg",[away])
       #home_mov_avg = cursor.execute("select mov_avg_form(%s,current_date) ftr",[home])
       #away_mov_avg=dictfetchall(cursor)  
       away_mov_avg = [item[0] for item in cursor.fetchall()]
       #away_mov_avg = Results.objects.raw("select mov_avg_form(%s,current_date) ftr",[away])
       games_dict = {'gameinfo' : games_list ,'hma' : home_mov_avg , 'ama' : away_mov_avg}
       nd=games_dict.copy()
       #nd.update(home_mov_avg)
       #nd.update(away_mov_avg)
       print(nd)
       return render_to_response('mwb/indepth.html', nd, context)
def login_view(request):
    username1 = request.POST.get('username', '')
    password1 = request.POST.get('password', '')
    home = request.POST.get('home','')
    away = request.POST.get('away','')
    user = auth.authenticate(username=username1, password=password1)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("indepth="+home+"&"+away)
    else:
        #  create a user
        User.objects.create_user(username=username1,
                                 email=username1,
                                 password=password1)
        messages.add_message(request, messages.INFO, 'User created')
        #return HttpResponseRedirect("indepth")
        return HttpResponseRedirect("indepth="+home+"&"+away)
        #return render_to_response('mwb/indepth.html', games_dict, context)
"""
def pdata(request):
    context = RequestContext(request)
    dir = "/home/andy/lit-basin-8962/mwb/static/mwb/"
    dfh = pd.DataFrame()
    
    qry = "select hometeam,fthg from rescuttmp where matchdate >= '31-aug-2015' and fthg is not null"
    x = pandata(qry,dfh)
    y=pander(x.dfh)
    z=y.sumhome(x.dfh,'fthg')
    m=y.mean(x.dfh,'fthg')
    #m.to_csv(dir+'besthome.tsv', sep='\t')
    
    qry = "select hometeam,ftag from rescuttmp where matchdate >= '31-aug-2015' and fthg is not null"
    x = pandata(qry,dfh)
    y=pander(x.dfh)
    z=y.sumhome(x.dfh,'ftag')
    m=y.mean(x.dfh,'ftag')
    m.columns = ['fthg']
    j=m.reset_index().to_json(orient='records')
    
    #j=y.json(m)
    d=json.loads(j)
    print (d)
    return render_to_response('mwb/bcc3.html', {'goals':json.dumps(d)}, context)
    #print(j)
    
    #m.to_csv(dir+'worsthome.tsv', sep='\t')
"""    
def about(request):
    return render(request, "mwb/about.html", { })

